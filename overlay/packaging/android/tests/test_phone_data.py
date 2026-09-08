"""Exercise the actual data packager with a small complete fixture."""
import hashlib
import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile

SPEC = importlib.util.spec_from_file_location(
    'phone_data', Path(__file__).resolve().parents[1] / 'package-phone-data.py')
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class PhoneDataTest(unittest.TestCase):
    def test_archive_preserves_content_and_import_directory_order(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name in ('data', 'fonts', 'images', 'sounds'):
                (root / name).mkdir()
                (root / name / 'sample').write_bytes(b'game content')
            (root / 'data/core/music').mkdir(parents=True)
            (root / 'data/core/music/theme.ogg').write_bytes(b'music')
            (root / 'data/.gitignore').write_text('ignored')
            for name in ('COPYING', 'copyright'):
                (root / name).write_text('license')
            previous_root = MODULE.ROOT
            try:
                MODULE.ROOT = root
                output = root / 'dist/data.zip'
                MODULE.package(output, english_only=True)
            finally:
                MODULE.ROOT = previous_root
            with zipfile.ZipFile(output) as archive:
                self.assertIsNone(archive.testzip())
                names = archive.namelist()
                self.assertIn('translations/', names)
                self.assertNotIn('data/.gitignore', names)
                self.assertEqual(archive.read('data/core/music/theme.ogg'), b'music')
                self.assertEqual(archive.read('COPYING'), b'license')
                seen = set()
                for name in names:
                    parent = Path(name.rstrip('/')).parent.as_posix()
                    if parent != '.':
                        self.assertIn(parent + '/', seen)
                    seen.add(name)
            digest = hashlib.sha256(output.read_bytes()).hexdigest()
            self.assertEqual(output.with_suffix('.zip.sha256').read_text(),
                             digest + '  data.zip\n')


if __name__ == '__main__':
    unittest.main()
