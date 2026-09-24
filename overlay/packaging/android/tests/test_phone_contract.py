"""Check the independently maintained Java/JNI command protocol and resources."""
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[3]
APP = ROOT / 'packaging/android/app/src/main'
JAVA = APP / 'java/org/wesnoth/Wesnoth'


def resource_names(path, tag):
    root = ET.parse(path).getroot()
    return [node.attrib['name'] for node in root if node.tag == tag]


def string_map(path):
    root = ET.parse(path).getroot()
    values = {}
    for node in root:
        if node.tag == 'string':
            values[node.attrib['name']] = node.text
        elif node.tag == 'string-array':
            values[node.attrib['name']] = [item.text for item in node]
    return values


class PhoneContractTest(unittest.TestCase):
    def test_wire_ids_match_and_are_real_commands(self):
        native = (ROOT / 'src/phone_actions.hpp').read_text(encoding='utf-8')
        java = (JAVA / 'PhoneControls.java').read_text(encoding='utf-8')
        cpp_ids = re.findall(r'"([a-z]+)"', native)
        java_ids = re.findall(r'"([a-z]+)"', java.split('ACTIONS = {', 1)[1].split('};', 1)[0])
        self.assertEqual(cpp_ids, java_ids, 'Wire drift could execute the wrong game action')
        self.assertEqual(len(cpp_ids), len(set(cpp_ids)))
        self.assertLessEqual(len(cpp_ids), 31, 'JNI availability mask is a signed int')
        commands = (ROOT / 'src/hotkey/hotkey_command.cpp').read_text(encoding='utf-8')
        for command in cpp_ids:
            self.assertIn('"' + command + '"', commands)

    def test_phone_labels_exist_and_are_not_empty(self):
        names = string_map(APP / 'res/values/strings.xml')
        sources = [JAVA / 'PhoneControls.java', JAVA / 'InitActivity.java']
        for source in sources:
            java = source.read_text(encoding='utf-8')
            for name in set(re.findall(r'R\.string\.(phone_\w+)', java)):
                self.assertTrue(names.get(name), '{} is missing or empty'.format(name))

    def test_every_phone_string_is_translated(self):
        english = string_map(APP / 'res/values/strings.xml')
        spanish = string_map(APP / 'res/values-es/strings.xml')
        phone = {name for name in english if name.startswith('phone_')}
        self.assertEqual(phone, {name for name in spanish if name.startswith('phone_')},
                         'Phone strings must exist in both locales')
        for name in sorted(phone):
            self.assertTrue(spanish[name], '{} is empty in values-es'.format(name))

    def test_launcher_dialogs_use_resources(self):
        """A literal here would ship an English-only dialog to Spanish phones."""
        for source in (JAVA / 'InitActivity.java', JAVA / 'PhoneControls.java'):
            java = source.read_text(encoding='utf-8')
            literals = re.findall(r'\.set(?:Title|Message|Text)\("', java)
            self.assertEqual([], literals, '{} has hardcoded user-visible text'.format(source.name))

    def test_campaign_picker_covers_every_campaign(self):
        campaigns = (JAVA / 'PhoneCampaigns.java').read_text(encoding='utf-8')
        ids = re.findall(r'"([A-Za-z_0-9]+)"', campaigns.split('IDS = {', 1)[1].split('}', 1)[0])
        self.assertTrue(ids)
        for locale in ('values', 'values-es'):
            strings = string_map(APP / 'res' / locale / 'strings.xml')
            for name in ('phone_campaign_titles', 'phone_campaign_meta', 'phone_campaign_hooks'):
                self.assertEqual(len(ids), len(strings.get(name, [])),
                                 '{} must describe every campaign in {}'.format(name, locale))
                for entry in strings[name]:
                    self.assertTrue(entry, '{} has a blank entry in {}'.format(name, locale))

    def test_phone_colors_and_ids_are_defined(self):
        self.assertTrue(resource_names(APP / 'res/values/phone_colors.xml', 'color'))
        declared = set(resource_names(APP / 'res/values/phone_ids.xml', 'item'))
        for layout in (APP / 'res/layout').glob('*.xml'):
            declared |= set(re.findall(r'@\+id/(phone_\w+)', layout.read_text(encoding='utf-8')))
        used_ids = set()
        for source in JAVA.glob('*.java'):
            used_ids |= set(re.findall(r'R\.id\.(phone_\w+)', source.read_text(encoding='utf-8')))
        self.assertTrue(used_ids)
        self.assertLessEqual(used_ids, declared, 'Java refers to undeclared phone view ids')

    def test_reserved_event_id_does_not_collide(self):
        header = (ROOT / 'src/events.hpp').read_text(encoding='utf-8')
        offsets = re.findall(r'#define \w+ \(SDL_EVENT_USER \+ (\d+)\)', header)
        self.assertEqual(len(offsets), len(set(offsets)))


if __name__ == '__main__':
    unittest.main()
