#!/usr/bin/env python3
"""Refresh this campaign pack in a previously built matching game-data archive.

Keeps all existing core files and compiled translations. Does not compile an
APK or modify saves. Full clean builds use package-phone-data.py instead.
SPDX-License-Identifier: GPL-2.0-or-later
"""
from pathlib import Path
import hashlib
import shutil
import zipfile
from validate_campaigns import validate

ROOT = Path(__file__).resolve().parents[3]
PACK = ROOT / 'data/campaigns/Brasa_y_Marea'
ASSET = ROOT / 'packaging/android/app/src/main/assets/gamedata.zip'
PREFIX = 'data/campaigns/Brasa_y_Marea/'


def main():
    validate()
    if not ASSET.is_file():
        raise SystemExit('Build the full matching game-data archive first.')
    temporary = ASSET.with_name('gamedata-campaign-update.tmp.zip')
    with zipfile.ZipFile(ASSET) as source, zipfile.ZipFile(temporary,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as output:
        assert source.testzip() is None, 'Original game-data archive is corrupt'
        for info in source.infolist():
            if info.filename.startswith(PREFIX):
                continue
            if info.is_dir():
                output.writestr(info,b'')
            else:
                with source.open(info) as src, output.open(info,'w') as dst:
                    shutil.copyfileobj(src,dst,1024*1024)
        output.writestr(PREFIX,b'')
        for path in sorted(PACK.rglob('*')):
            if any(p.startswith('.') for p in path.relative_to(PACK).parts):
                continue
            name = PREFIX+path.relative_to(PACK).as_posix()
            if path.is_dir():
                output.writestr(name+'/',b'')
            elif path.is_file():
                output.write(path,name)
    with zipfile.ZipFile(temporary) as archive:
        assert archive.testzip() is None
        assert len([n for n in archive.namelist() if n.startswith(PREFIX+'scenarios/') and n.endswith('.cfg')]) == 52
        assert any(n.startswith('translations/es/LC_MESSAGES/') for n in archive.namelist())
    temporary.replace(ASSET)
    with ASSET.open('rb') as stream:
        digest = hashlib.file_digest(stream,'sha256').hexdigest()
    ASSET.with_suffix('.zip.sha256').write_text(digest+'  gamedata.zip\n',encoding='ascii')
    print(f'Updated complete game data: {ASSET.stat().st_size():,} bytes; SHA-256 {digest}')


if __name__ == '__main__':
    main()
