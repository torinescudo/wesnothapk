#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-or-later
"""Package matching full game data, music and gettext catalogs for offline import."""
import argparse
import hashlib
from pathlib import Path
import shutil
import subprocess
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[2]


def package(output, english_only=False):
    if not english_only and not shutil.which('msgfmt'):
        raise SystemExit('msgfmt is required for translations (install GNU gettext). '
                         'Use --english-only only for a development data archive.')
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as temporary:
        catalogs = Path(temporary) / 'translations'
        catalogs.mkdir()
        if not english_only:
            for po in sorted((ROOT / 'po').glob('*/*.po')):
                target = catalogs / po.stem / 'LC_MESSAGES' / (po.parent.name + '.mo')
                target.parent.mkdir(parents=True, exist_ok=True)
                subprocess.run(['msgfmt', '-o', str(target), str(po)], check=True)

        # Directory entries precede children for the upstream Android importer.
        with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
            for folder in ('data', 'fonts', 'images', 'sounds', 'translations'):
                source = catalogs if folder == 'translations' else ROOT / folder
                if not source.is_dir():
                    raise SystemExit(f'Missing {source}; complete the source checkout first.')
                archive.writestr(folder + '/', '')
                for entry in sorted(source.rglob('*')):
                    if any(part.startswith('.') for part in entry.relative_to(source).parts):
                        continue
                    name = folder + '/' + entry.relative_to(source).as_posix()
                    if entry.is_dir():
                        archive.writestr(name + '/', '')
                    elif entry.is_file():
                        archive.write(entry, name)
            for name in ('COPYING', 'copyright'):
                archive.write(ROOT / name, name)
        with output.open('rb') as stream:
            digest = hashlib.file_digest(stream, 'sha256').hexdigest()
        output.with_suffix(output.suffix + '.sha256').write_text(
            f'{digest}  {output.name}\n', encoding='ascii')
        print(f'{output} ({output.stat().st_size:,} bytes)')
        print('English development data' if english_only else 'Includes all available translations')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=ROOT / 'packaging/android/dist/wesnoth-phone-data.zip')
    parser.add_argument('--english-only', action='store_true')
    args = parser.parse_args()
    package(args.output, args.english_only)
