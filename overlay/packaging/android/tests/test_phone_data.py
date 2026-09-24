"""Contract checks for the packaged Brasa y Marea data.

Run with: python3 -m unittest discover -s packaging/android/tests
"""
import json
import re
import unittest
from pathlib import Path

DATA = Path(__file__).resolve().parents[3] / 'data' / 'campaigns' / 'Brasa_y_Marea'


class DataContract(unittest.TestCase):
    def setUp(self):
        manifest = json.loads((DATA / 'manifest.json').read_text(encoding='utf-8'))
        self.entries = manifest['scenarios']

    def test_every_scenario_map_exists_and_is_rectangular(self):
        for entry in self.entries:
            rows = (DATA / 'maps' / entry['map']).read_text(encoding='utf-8').splitlines()
            self.assertTrue(rows, entry['map'])
            widths = {len(r.split(',')) for r in rows}
            self.assertEqual(len(widths), 1, '%s has ragged rows' % entry['map'])

    def test_every_scenario_states_what_winning_takes(self):
        for entry in self.entries:
            text = (DATA / entry['file']).read_text(encoding='utf-8')
            self.assertIn('[goal]', text, entry['file'])
            self.assertIn('description=', text, '%s has an empty goal' % entry['file'])

    def test_speaker_names_stay_inside_the_label_budget(self):
        for entry in self.entries:
            text = (DATA / entry['file']).read_text(encoding='utf-8')
            for name in re.findall(r'speaker="([^"]+)"', text):
                self.assertLessEqual(len(name), 26,
                                     '%s: %r is too long for a nameplate' % (entry['file'], name))

    def test_shared_places_reuse_one_map(self):
        shared = {}
        for entry in self.entries:
            place = entry.get('shared')
            if place:
                shared.setdefault(place, set()).add(entry['map'])
        self.assertTrue(shared, 'no shared places are wired')
        for place, maps in shared.items():
            self.assertEqual(len(maps), 1, '%s is split over %s' % (place, sorted(maps)))


if __name__ == '__main__':
    unittest.main()
