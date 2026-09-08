"""Check the independently maintained Java/JNI command protocol and resources."""
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[3]
APP = ROOT / 'packaging/android/app/src/main'


class PhoneContractTest(unittest.TestCase):
    def test_wire_ids_match_and_are_real_commands(self):
        native = (ROOT / 'src/phone_actions.hpp').read_text(encoding='utf-8')
        java = (APP / 'java/org/wesnoth/Wesnoth/PhoneControls.java').read_text(encoding='utf-8')
        cpp_ids = re.findall(r'"([a-z]+)"', native)
        java_ids = re.findall(r'"([a-z]+)"', java.split('ACTIONS = {', 1)[1].split('};', 1)[0])
        self.assertEqual(cpp_ids, java_ids, 'Wire drift could execute the wrong game action')
        self.assertEqual(len(cpp_ids), len(set(cpp_ids)))
        self.assertLessEqual(len(cpp_ids), 31, 'JNI availability mask is a signed int')
        commands = (ROOT / 'src/hotkey/hotkey_command.cpp').read_text(encoding='utf-8')
        for command in cpp_ids:
            self.assertIn('"' + command + '"', commands)

    def test_phone_labels_exist_and_are_not_empty(self):
        strings = ET.parse(APP / 'res/values/strings.xml').getroot()
        names = {node.attrib['name']: node.text for node in strings if node.tag == 'string'}
        java = (APP / 'java/org/wesnoth/Wesnoth/PhoneControls.java').read_text(encoding='utf-8')
        for name in set(re.findall(r'R\.string\.(phone_\w+)', java)):
            self.assertTrue(names.get(name), name)

    def test_reserved_event_id_does_not_collide(self):
        header = (ROOT / 'src/events.hpp').read_text(encoding='utf-8')
        offsets = re.findall(r'#define \w+ \(SDL_EVENT_USER \+ (\d+)\)', header)
        self.assertEqual(len(offsets), len(set(offsets)))


if __name__ == '__main__':
    unittest.main()
