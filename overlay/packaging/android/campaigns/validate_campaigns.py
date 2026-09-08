#!/usr/bin/env python3
"""Structural/content checks using Wesnoth's parser plus reachability checks.

Does not pretend to replace engine playtesting. Pass --allow-missing-art only
while generating art; release packaging must use the strict default.
SPDX-License-Identifier: GPL-2.0-or-later
"""
from pathlib import Path
from collections import deque, Counter
import argparse
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
PACK = ROOT / 'data/campaigns/Brasa_y_Marea'
sys.path.insert(0, str(ROOT / 'data/tools'))
from wesnoth.wmlparser3 import Parser


def parse(path):
    # Shared macros are supplied by core at runtime. Parse our authored WML
    # independently here; native engine tests additionally expand the macros.
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'\{[^{}]*\}', '', text)
    text = re.sub(r'^\s*#.*$', '', text, flags=re.M)
    return Parser().parse_text(text)


def walk(node):
    for child in node.get_all(tag=''):
        yield child
        yield from walk(child)


def reachable(grid, start):
    width, height = len(grid[0]), len(grid)
    found, queue = {tuple(start)}, deque([tuple(start)])
    while queue:
        x,y = queue.popleft()
        # Wesnoth staggered columns; using either diagonal in the road grid
        # is unnecessary: both horizontal/vertical steps are legal neighbors.
        offset = -1 if x % 2 else 1
        neighbors = [(x,y-1),(x,y+1),(x-1,y),(x+1,y),(x-1,y+offset),(x+1,y+offset)]
        for a,b in neighbors:
            if 1 <= a <= width and 1 <= b <= height and (a,b) not in found:
                terrain = grid[b-1][a-1].split()[-1].split('^')[0]
                if terrain not in ('Xu','Xv','Wo','Qxu','Ql'):
                    found.add((a,b))
                    queue.append((a,b))
    return found


def validate(allow_missing_art=False):
    m = json.loads((PACK/'manifest.json').read_text(encoding='utf-8'))
    assert [c['scenarios'] for c in m['campaigns']] == [3,5,7,9,12,16]
    assert len(m['scenarios']) == 52
    ids = {s['id'] for s in m['scenarios']}
    assert len(ids) == 52
    campaign_nodes = parse(PACK/'_main.cfg').get_all(tag='campaign')
    assert {n.get_text_val('id') for n in campaign_nodes} == {c['id'] for c in m['campaigns']}
    known = set(m['units'])
    for path in (ROOT/'data/core/units').rglob('*.cfg'):
        known.update(re.findall(r'^\s*id\s*=\s*"?([^"\r\n]+)', path.read_text(encoding='utf-8'), re.M))
    used_assets = set()
    terrain_codes = set(re.findall(r'^\s*string\s*=\s*"?([^"\s]+)',
        (ROOT/'data/core/terrain.cfg').read_text(encoding='utf-8'),re.M))
    maps = set()
    objective_counts = Counter()
    for chapter in m['scenarios']:
        tree = parse(PACK/chapter['file'])
        scenario = tree.get_all(tag='scenario')[0]
        assert scenario.get_text_val('id') == chapter['id']
        assert scenario.get_text_val('next_scenario') == chapter['next']
        assert chapter['next'] == 'null' or chapter['next'] in ids
        assert len(scenario.get_all(tag='side')) == 2
        assert scenario.get_text_val('victory_when_enemies_defeated') == 'no'
        names = [e.get_text_val('name') for e in scenario.get_all(tag='event')]
        assert 'victory' in names and 'time over' in names and names.count('last breath') == 2
        for node in walk(tree):
            for attr in ('type','recruit'):
                value = node.get_text_val(attr)
                if value and node.name.decode() in ('unit','side','allow_recruit'):
                    for unit in value.split(','):
                        assert unit in known, (chapter['id'], unit)
            for attr in ('image','background'):
                value = node.get_text_val(attr)
                if value:
                    used_assets.add(value.split('~')[0])
            if node.name == b'music':
                assert (PACK/'music'/node.get_text_val('name')).is_file()
        mapfile = PACK/'maps'/chapter['map']
        data = mapfile.read_text()
        digest = hashlib.sha256(data.encode()).hexdigest()
        assert digest not in maps, ('duplicate map', chapter['id'])
        maps.add(digest)
        grid = [[s.strip() for s in row.split(',')] for row in data.strip().splitlines()]
        assert len({len(row) for row in grid}) == 1
        for row in grid:
            for terrain in row:
                pieces = terrain.split()[-1].split('^')
                assert pieces[0] in terrain_codes, (chapter['id'],'unknown base terrain',pieces[0])
                for overlay in pieces[1:]:
                    assert '^'+overlay in terrain_codes, (chapter['id'],'unknown overlay',overlay)
        assert sum(t.startswith('1 ') for row in grid for t in row) == 1
        assert sum(t.startswith('2 ') for row in grid for t in row) == 1
        reached = reachable(grid, chapter['start'])
        for destination in [chapter['enemy'],chapter['destination'],chapter['prison'],*chapter['points']]:
            assert tuple(destination) in reached, (chapter['id'],'unreachable',destination)
        objective_counts[chapter['goal']] += 1
    units = parse(PACK/'units/units.cfg').get_all(tag='unit_type')
    assert len(units) == 22
    for unit in units:
        assert unit.get_text_val('advances_to') in known | {'null'}
        assert len(unit.get_all(tag='attack')) >= 2 or unit.get_text_val('usage') in ('fighter','scout')
        for attr in ('image','profile'):
            used_assets.add(unit.get_text_val(attr).split('~')[0])
    missing = []
    for name in sorted(used_assets):
        candidates = [PACK/'images'/name,ROOT/'data/core/images'/name,ROOT/'images'/name,ROOT/name]
        if not any(p.is_file() for p in candidates):
            missing.append(name)
    if missing and not allow_missing_art:
        raise AssertionError('Missing assets: ' + ', '.join(missing))
    for campaign in m['campaigns']:
        route, current = [], campaign['first']
        lookup = {s['id']:s for s in m['scenarios']}
        while current != 'null':
            assert current not in route, ('cycle',current)
            route.append(current)
            assert lookup[current]['campaign'] == campaign['id']
            current = lookup[current]['next']
        assert len(route) == campaign['scenarios']
    report = {'campaigns':6,'scenarios':52,'unique_maps':len(maps),'unit_types':len(units),
              'objectives':dict(objective_counts),'missing_assets':missing,
              'scope':'WML syntax, identifiers, assets, campaign routes and map reachability; not balance playtesting'}
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--allow-missing-art',action='store_true')
    args = parser.parse_args()
    validate(args.allow_missing_art)
