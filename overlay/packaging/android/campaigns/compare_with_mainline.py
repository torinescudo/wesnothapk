#!/usr/bin/env python3
"""Measure the original campaigns against mainline ones, field by field.

Both corpora are read with the same parser, so "the same level of detail" becomes
a number instead of an opinion: scenario WML volume, dialogue, scripting, map area
and terrain structure, and the art actually shipped with each campaign.

    python3 compare_with_mainline.py                # human readable report
    python3 compare_with_mainline.py --json out.json
    python3 compare_with_mainline.py --gate         # fails below the mainline floor

Run from a reconstructed source tree (prepare-source.py) so that
data/campaigns holds the mainline campaigns next to Brasa_y_Marea.

SPDX-License-Identifier: GPL-2.0-or-later
"""
from pathlib import Path
import argparse
import json
import re
import statistics
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CAMPAIGNS = ROOT / 'data/campaigns'
OURS = 'Brasa_y_Marea'

# WML tags whose presence separates a scripted scenario from a board setup.
DETAIL_TAGS = (
    'message', 'event', 'objectives', 'objective', 'side', 'unit', 'recall',
    'if', 'while', 'then', 'else', 'set_variable', 'variable', 'command',
    'store_unit', 'unstore_unit', 'scroll_to', 'sound', 'music', 'item',
    'terrain', 'endlevel', 'ai', 'filter', 'role', 'have_unit', 'kill',
    'moveto', 'story', 'part', 'label', 'gold', 'time', 'delay', 'animate',
    'remove_item', 'allow_recruit', 'disallow_recruit', 'capture_village',
)
# Terrain families used for the structure metrics.
WATER = ('Ww', 'Wo', 'Ww^', 'Wo^')
FOREST = ('^F',)
MOUNTAIN = ('Mm', 'Mv', 'Md', 'Me')
CASTLE = ('C', 'K')
ROAD = ('Rr', 'Rb', 'Ra', 'Re')
VILLAGE = ('^V',)
BRIDGE = ('^Bw',)
SWAMP = ('Ss', 'Sm')
SAND = ('Ds', 'Dd')
SNOW = ('Aa', 'Ai')
CAVE = ('Uu', 'Uh', 'Xu')
# Terrain no land unit can enter unless a bridge crosses it.
IMPASSABLE = ('Ww', 'Wo', 'Xu', 'Xo', 'Ww^')

SCENARIO_SKIP = ('utils', 'tests', 'macros', 'units', 'images', 'music',
                 'sounds', 'lua', 'ai', 'maps')


def tag_counts(text):
    return {tag: len(re.findall(r'\[%s\b' % re.escape(tag), text)) for tag in DETAIL_TAGS}


def scenario_files(campaign):
    found = []
    for path in sorted(campaign.rglob('*.cfg')):
        parts = [p.lower() for p in path.relative_to(campaign).parts[:-1]]
        if any(part in SCENARIO_SKIP for part in parts):
            continue
        body = path.read_text(encoding='utf-8', errors='replace')
        if re.search(r'^\s*\[scenario\]', body, re.M):
            found.append((path, body))
    return found


def attribute(text, key):
    """Return a WML attribute value, quoted (possibly multi-line) or bare."""
    quoted = re.search(r'\b%s\s*=\s*"((?:[^"\\]|\\.)*)"' % re.escape(key), text, re.S)
    if quoted:
        return quoted.group(1)
    bare = re.search(r'^\s*%s\s*=\s*([^\s#]+)' % re.escape(key), text, re.M)
    return bare.group(1) if bare else None


def resolve_map(campaign, scenario_text, body):
    """Find the map a scenario uses, as rows of terrain tokens."""
    for key in ('map_file', 'map_data'):
        value = attribute(scenario_text, key)
        if value is None:
            continue
        candidate = value.strip()
        if candidate.startswith('{') or candidate.startswith('$'):
            continue
        if '\n' in candidate or ',' in candidate:
            return parse_map_rows(candidate)
        for name in (candidate, candidate + '.map'):
            for path in (campaign / 'maps' / name, campaign / name,
                         campaign / 'maps' / Path(name).name):
                if path.is_file():
                    return parse_map_rows(path.read_text(encoding='utf-8', errors='replace'))
    # Inline through a macro include, e.g. map_data="{campaigns/X/maps/y.map}".
    for include in re.findall(r'\{([^{}]*\.map)\}', scenario_text):
        candidate = ROOT / 'data' / include.replace('campaigns/', 'campaigns/', 1)
        if candidate.is_file():
            return parse_map_rows(candidate.read_text(encoding='utf-8', errors='replace'))
        alt = campaign / include.split('/')[-1]
        if alt.is_file():
            return parse_map_rows(alt.read_text(encoding='utf-8', errors='replace'))
    return None


def parse_map_rows(text):
    rows = []
    for line in text.splitlines():
        cells = [cell.strip() for cell in line.split(',') if cell.strip()]
        if cells:
            rows.append(cells)
    return rows or None


def terrain_code(cell):
    parts = cell.split()
    return parts[-1] if parts else cell


def walkable_cell(code):
    """Bridges crossing or fords (Wwf) make water passable; chasms never are."""
    river = code.split('^')[0]
    if '^Bw' in code or '^V' in code or 'f' in river[2:]:
        return True
    return not code.startswith(IMPASSABLE)


def map_stats(rows):
    if not rows:
        return None
    height = len(rows)
    width = max(len(row) for row in rows)
    codes = [terrain_code(cell) for row in rows for cell in row]
    base = [code[:2] for code in codes]
    owners = [cell.split()[0] for row in rows for cell in row if len(cell.split()) > 1]
    villages = sum(1 for code in codes if any(v in code for v in VILLAGE))
    # Isolation: how often a tile's base terrain differs from all four neighbours.
    # Coherent mainline maps shape masses of terrain; noise generators do not.
    isolated = 0
    compared = 0
    for y, row in enumerate(rows):
        for x, cell in enumerate(row):
            here = terrain_code(cell)[:2]
            neighbours = []
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = y + dy, x + dx
                if 0 <= ny < height and 0 <= nx < len(rows[ny]):
                    neighbours.append(terrain_code(rows[ny][nx])[:2])
            if not neighbours:
                continue
            compared += 1
            if all(other != here for other in neighbours):
                isolated += 1
    walkable = [[walkable_cell(terrain_code(cell)) for cell in row] for row in rows]
    land = sum(1 for row in walkable for cell in row if cell)
    components, largest, stranded = connectivity(rows, walkable)
    return {
        'width': width,
        'height': height,
        'area': width * height,
        'distinct_terrain': len(set(codes)),
        'distinct_base': len(set(base)),
        'villages': villages,
        'owned_villages': sum(1 for owner in owners if owner.isdigit()),
        'neutral_villages': sum(1 for owner in owners if owner in ('*', '_')),
        'water': sum(1 for code in base if code in ('Ww', 'Wo')),
        'forest': sum(1 for code in codes if '^F' in code),
        'mountain': sum(1 for code in base if code in MOUNTAIN),
        'castle': sum(1 for code in base if code[0] in CASTLE),
        'road': sum(1 for code in base if code in ROAD),
        'bridge': sum(1 for code in codes if '^Bw' in code),
        'swamp': sum(1 for code in base if code in SWAMP),
        'sand': sum(1 for code in base if code in SAND),
        'snow': sum(1 for code in base if code in SNOW),
        'cave': sum(1 for code in base if code in CAVE),
        'isolated_ratio': round(isolated / compared, 4) if compared else 0.0,
        'components': components,
        'main_land_fraction': round(largest / land, 4) if land else 0.0,
        'stranded_villages': stranded,
    }


def connectivity(rows, walkable):
    """Land components, the largest share of land, and villages cut off from it.

    Uses no ownership or start-position convention, so mainline and generated
    maps are measured the same way: a village on its own island is a defect for
    a land campaign, whichever tool produced the map.
    """
    seen = [[False] * len(row) for row in rows]
    villages_per_component = []
    components = 0
    largest = 0
    land = sum(1 for row in walkable for cell in row if cell)
    for y, row in enumerate(rows):
        for x in range(len(row)):
            if seen[y][x] or not walkable[y][x]:
                continue
            components += 1
            size = 0
            villages = 0
            stack = [(y, x)]
            while stack:
                cy, cx = stack.pop()
                if not (0 <= cy < len(rows) and 0 <= cx < len(rows[cy])):
                    continue
                if seen[cy][cx] or not walkable[cy][cx]:
                    continue
                seen[cy][cx] = True
                size += 1
                if any(v in terrain_code(rows[cy][cx]) for v in VILLAGE):
                    villages += 1
                stack.extend([(cy + 1, cx), (cy - 1, cx), (cy, cx + 1), (cy, cx - 1)])
            villages_per_component.append(villages)
            if size > largest:
                largest = size
    total_villages = sum(1 for row in rows for cell in row
                         if any(v in terrain_code(cell) for v in VILLAGE))
    # Villages outside the largest land component are the ones a land army cannot reach.
    reachable = max(villages_per_component, default=0)
    return components, largest if land else 0, max(0, total_villages - reachable)


def campaign_stats(campaign):
    scenarios = scenario_files(campaign)
    per_scenario = []
    maps = []
    totals = {tag: 0 for tag in DETAIL_TAGS}
    for path, body in scenarios:
        counts = tag_counts(body)
        for tag, value in counts.items():
            totals[tag] += value
        rows = resolve_map(campaign, body, body)
        stats = map_stats(rows)
        if stats:
            maps.append(stats)
        per_scenario.append({
            'file': str(path.relative_to(campaign)),
            'bytes': len(body.encode('utf-8')),
            'lines': body.count('\n') + 1,
            'messages': counts['message'],
            'speakers': sorted(set(re.findall(r'speaker\s*=\s*"([^"]*)"', body))),
            'map': stats,
            'tags': counts,
        })
    art = {'png': 0, 'bytes': 0, 'portraits': 0, 'units': 0, 'story': 0, 'icons': 0, 'maps': 0}
    for path in campaign.rglob('*'):
        if path.is_file() and path.suffix.lower() in ('.png', '.jpg', '.webp'):
            art['png'] += 1
            art['bytes'] += path.stat().st_size
            rel = '/'.join(p.lower() for p in path.relative_to(campaign).parts)
            if 'portrait' in rel:
                art['portraits'] += 1
            elif 'unit' in rel:
                art['units'] += 1
            elif 'story' in rel:
                art['story'] += 1
            elif 'icon' in rel:
                art['icons'] += 1
            elif 'map' in rel:
                art['maps'] += 1
    music = [p for p in campaign.rglob('*.ogg')]
    return {
        'name': campaign.name,
        'scenarios': len(scenarios),
        'lines': [s['lines'] for s in per_scenario],
        'total_lines': sum(s['lines'] for s in per_scenario),
        'messages': [s['messages'] for s in per_scenario],
        'total_messages': sum(s['messages'] for s in per_scenario),
        'speakers': sorted({speaker for s in per_scenario for speaker in s['speakers']}),
        'tags': totals,
        'maps': maps,
        'art': art,
        'music': {'tracks': len(music), 'bytes': sum(p.stat().st_size for p in music)},
        'detail': per_scenario,
    }


def median(values, default=0):
    return statistics.median(values) if values else default


def summarise(campaigns):
    scenarios = [c for c in campaigns if c['scenarios']]
    maps = [m for c in campaigns for m in c['maps']]
    return {
        'campaigns': len(scenarios),
        'scenarios': sum(c['scenarios'] for c in scenarios),
        'lines_per_scenario': median([median(c['lines']) for c in scenarios]),
        'messages_per_scenario': median([median(c['messages']) for c in scenarios]),
        'events_per_scenario': median([median([s['tags']['event'] for s in c['detail']]) for c in scenarios]),
        'objectives_per_scenario': median([median([s['tags']['objectives'] for s in c['detail']]) for c in scenarios]),
        'story_parts_per_scenario': median([median([s['tags']['part'] for s in c['detail']]) for c in scenarios]),
        'map_area': median([m['area'] for m in maps]),
        'map_distinct_terrain': median([m['distinct_terrain'] for m in maps]),
        'map_distinct_base': median([m['distinct_base'] for m in maps]),
        'map_villages': median([m['villages'] for m in maps]),
        'map_isolated_ratio': round(median([m['isolated_ratio'] for m in maps]), 4),
        'map_forest': median([m['forest'] for m in maps]),
        'map_mountain': median([m['mountain'] for m in maps]),
        'map_water': median([m['water'] for m in maps]),
        'map_road': median([m['road'] for m in maps]),
        'map_bridge': median([m['bridge'] for m in maps]),
        'map_components': median([m['components'] for m in maps]),
        'stranded_villages': sum(m['stranded_villages'] for m in maps),
        'maps_with_stranded_villages': sum(1 for m in maps if m['stranded_villages']),
        'art_per_campaign': median([c['art']['png'] for c in scenarios]),
        'art_per_scenario': round(median([c['art']['png'] / c['scenarios'] for c in scenarios]), 2),
        'music_tracks_per_campaign': median([c['music']['tracks'] for c in scenarios]),
    }


# Fields compared against the mainline floor. Every original campaign has to
# reach the 25th percentile of mainline campaigns for each of them.
GATE_FIELDS = {
    'lines_per_scenario': 'per-scenario WML lines',
    'messages_per_scenario': 'dialogue lines per scenario',
    'events_per_scenario': 'scripted events per scenario',
    'objectives_per_scenario': 'objective blocks per scenario',
    'story_parts_per_scenario': 'story screens per scenario',
    'map_area': 'map tiles',
    'map_distinct_terrain': 'distinct terrain codes per map',
    'map_villages': 'villages per map',
}


def percentile(values, fraction):
    values = sorted(values)
    if not values:
        return 0
    index = max(0, min(len(values) - 1, int(round(fraction * (len(values) - 1)))))
    return values[index]


def print_report(ours, mainline, floors, passed):
    print('metric                          Brasa y Marea   mainline p25   mainline median   floor   verdict')
    print('-' * 96)
    for field, label in GATE_FIELDS.items():
        mine = ours[field]
        floor = floors[field]
        verdict = 'ok' if mine >= floor else 'BELOW'
        print('%-30s %14s %14s %17s %7s   %s' % (
            label, mine, floor, mainline[field], floor, verdict))
    print()
    for field in ('map_isolated_ratio', 'map_road', 'map_bridge', 'map_components',
                  'stranded_villages', 'art_per_scenario', 'music_tracks_per_campaign'):
        print('%-30s %14s %14s' % (field, ours[field], mainline[field]))
    print()
    print('gate:', 'PASS' if passed else 'FAIL')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--json', type=Path)
    parser.add_argument('--gate', action='store_true')
    parser.add_argument('--ours', default=OURS)
    args = parser.parse_args()

    campaigns = sorted(p for p in CAMPAIGNS.iterdir() if p.is_dir())
    if not campaigns:
        raise SystemExit('No campaigns under %s. Run prepare-source.py first.' % CAMPAIGNS)
    results = [campaign_stats(c) for c in campaigns]
    mine = [c for c in results if c['name'] == args.ours]
    if not mine:
        raise SystemExit('%s not found under %s' % (args.ours, CAMPAIGNS))
    mainline = [c for c in results if c['name'] != args.ours and c['scenarios'] >= 4]
    ours_summary = summarise(mine)
    mainline_summary = summarise(mainline)
    floors = {field: percentile([summarise([c])[field] for c in mainline], 0.25)
              for field in GATE_FIELDS}
    floors['map_area'] = round(floors['map_area'])
    passed = all(ours_summary[field] >= floors[field] for field in GATE_FIELDS)
    print_report(ours_summary, mainline_summary, floors, passed)
    if args.json:
        args.json.write_text(json.dumps({
            'ours': ours_summary, 'mainline': mainline_summary, 'floors': floors,
            'passed': passed,
            'campaigns': {'ours': mine, 'mainline': mainline},
        }, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
        print('wrote', args.json)
    return 0 if passed or not args.gate else 1


if __name__ == '__main__':
    sys.exit(main())
