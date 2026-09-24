"""The six original campaigns: one module per campaign, one dict per chapter.

Authored content only. `build_campaigns.py` turns these into WML; `README.md`
documents the schema and the quality bar a chapter has to meet.

    python -m stories            # structural check, prints per-campaign totals
    python -m stories --strict   # also fails when a chapter is below the bar

SPDX-License-Identifier: GPL-2.0-or-later
"""
from pathlib import Path
import re
import sys
import unicodedata

from . import alba, darian, iria, maura, nerea, sira

ORDER = ('alba', 'sira', 'iria', 'maura', 'nerea', 'darian')
MODULES = {'alba': alba, 'sira': sira, 'iria': iria, 'maura': maura,
           'nerea': nerea, 'darian': darian}
CAMPAIGNS = [MODULES[key].CAMPAIGN for key in ORDER]

CAMPAIGN_FIELDS = ('key', 'title', 'hero', 'companion', 'companion_type', 'race',
                   'recruit', 'enemy', 'length', 'premise', 'ending')
CHAPTER_FIELDS = ('title', 'goal', 'biome', 'antagonist', 'opening', 'intro',
                  'events', 'victory', 'protected', 'resolution')
GOALS = ('conquer', 'survive', 'escape', 'escort', 'rescue', 'beacons')
BIOMES = ('forest', 'coast', 'harbor', 'cave', 'quarry', 'plains', 'mountain',
          'ruins', 'islands')
# Speakers the generator resolves to a unit already on the map. Any other name is
# a character shown with their own portrait through an image message.
SPECIAL_SPEAKERS = ('narrator', 'hero', 'companion', 'antagonist', 'protected')
TRIGGER = re.compile(r'^(turn \d{1,2}|time limit|enemy leader defeated|'
                     r'village captured|half strength|beacon lit \d)$')

# Authoring floor for one chapter, checked by --strict. Measured against what
# mainline scenarios spend on dialogue.
QUALITY = {'intro_beats': 12, 'event_triggers': 3, 'victory_beats': 4,
           'total_beats': 22, 'opening_chars': 240, 'resolution_chars': 140}


def beats(chapter):
    """Every authored line in a chapter, with its trigger."""
    rows = [(None, speaker, line) for speaker, line in chapter['intro']]
    for trigger, lines in chapter['events']:
        rows += [(trigger, speaker, line) for speaker, line in lines]
    rows += [('victory', speaker, line) for speaker, line in chapter['victory']]
    return rows


def characters(campaigns=None):
    """Named speakers that need their own portrait, in a stable order."""
    names = set()
    for campaign in campaigns or CAMPAIGNS:
        for chapter in campaign['chapters']:
            for _, speaker, _ in beats(chapter):
                if speaker not in SPECIAL_SPEAKERS:
                    names.add(speaker)
    return sorted(names)


def portrait_key(name):
    """File name of a character's portrait, shared with the art generator."""
    plain = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('ascii')
    slug = re.sub(r'[^a-z0-9]+', '-', plain.lower()).strip('-')
    return slug or 'speaker'


def validate(campaigns=None):
    """Structural check. Raises on anything that would generate broken WML."""
    campaigns = campaigns or CAMPAIGNS
    assert len(campaigns) == len(ORDER), 'six campaigns are expected'
    assert [c['key'] for c in campaigns] == list(ORDER), 'campaign order changed'
    for campaign in campaigns:
        for field in CAMPAIGN_FIELDS:
            assert campaign.get(field), (campaign.get('key'), 'missing ' + field)
        assert len(campaign['premise']) >= 120, (campaign['key'], 'premise too thin')
        assert len(campaign['ending']) >= 120, (campaign['key'], 'ending too thin')
        titles = set()
        for chapter in campaign['chapters']:
            for field in CHAPTER_FIELDS:
                assert field in chapter, (campaign['key'], chapter.get('title'), field)
            assert chapter['goal'] in GOALS, (campaign['key'], chapter['goal'])
            assert chapter['biome'] in BIOMES, (campaign['key'], chapter['biome'])
            assert chapter['title'] not in titles, (campaign['key'], 'duplicate chapter title')
            titles.add(chapter['title'])
            assert chapter['opening'].strip() and chapter['resolution'].strip()
            # `events` and `victory` may still be empty while a chapter is being
            # written; the quality bar in report() is what requires them.
            assert chapter['intro'], (campaign['key'], chapter['title'], 'intro is empty')
            for field in ('intro', 'victory'):
                for row in chapter[field]:
                    assert isinstance(row, tuple) and len(row) == 2, (
                        campaign['key'], chapter['title'], field, row)
            for trigger, lines in chapter['events']:
                assert TRIGGER.match(trigger), (campaign['key'], chapter['title'], trigger)
                assert isinstance(lines, list), (campaign['key'], chapter['title'], trigger)
                for row in lines:
                    assert isinstance(row, tuple) and len(row) == 2, (
                        campaign['key'], chapter['title'], trigger, row)
            for _, speaker, line in beats(chapter):
                assert speaker.strip(), (campaign['key'], chapter['title'], 'empty speaker')
                assert line.strip(), (campaign['key'], chapter['title'], 'empty line')
                assert '  ' not in line, (campaign['key'], chapter['title'], 'double space')
            protected = chapter['protected']
            assert protected is None or (
                isinstance(protected, tuple) and len(protected) == 2 and all(protected))
    return report(campaigns)


def report(campaigns=None):
    campaigns = campaigns or CAMPAIGNS
    rows = []
    for campaign in campaigns:
        per_chapter = []
        for chapter in campaign['chapters']:
            lines = beats(chapter)
            per_chapter.append({
                'title': chapter['title'],
                'intro': len(chapter['intro']),
                'triggers': len(chapter['events']),
                'victory': len(chapter['victory']),
                'beats': len(lines),
                'opening_chars': len(chapter['opening']),
                'resolution_chars': len(chapter['resolution']),
            })
        rows.append({
            'key': campaign['key'],
            'chapters': len(campaign['chapters']),
            'beats': sum(row['beats'] for row in per_chapter),
            'beats_per_chapter': round(sum(row['beats'] for row in per_chapter)
                                       / len(per_chapter), 1),
            'below_bar': [row['title'] for row in per_chapter
                          if row['intro'] < QUALITY['intro_beats']
                          or row['triggers'] < QUALITY['event_triggers']
                          or row['victory'] < QUALITY['victory_beats']
                          or row['beats'] < QUALITY['total_beats']
                          or row['opening_chars'] < QUALITY['opening_chars']
                          or row['resolution_chars'] < QUALITY['resolution_chars']],
            'detail': per_chapter,
        })
    return {
        'campaigns': rows,
        'chapters': sum(row['chapters'] for row in rows),
        'beats': sum(row['beats'] for row in rows),
        'characters': len(characters(campaigns)),
        'below_bar': sum(len(row['below_bar']) for row in rows),
        'quality_bar': QUALITY,
    }


def main(argv):
    strict = '--strict' in argv
    summary = validate()
    for row in summary['campaigns']:
        flag = '' if not row['below_bar'] else '  below bar: %d' % len(row['below_bar'])
        print('%-8s chapters=%-3s beats=%-5s beats/chapter=%-6s%s'
              % (row['key'], row['chapters'], row['beats'], row['beats_per_chapter'], flag))
    print('total chapters=%s beats=%s named speakers=%s below_bar=%s'
          % (summary['chapters'], summary['beats'], summary['characters'],
             summary['below_bar']))
    if strict and summary['below_bar']:
        print('FAIL: %d chapters are below the authoring bar' % summary['below_bar'])
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
