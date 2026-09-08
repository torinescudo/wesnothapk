#!/usr/bin/env python3
"""Create the reviewable campaign source/resource bundle, excluding local tools.
SPDX-License-Identifier: GPL-2.0-or-later
"""
from pathlib import Path
import hashlib
import zipfile
from validate_campaigns import validate

ROOT = Path(__file__).resolve().parents[3]
PACK = ROOT/'data/campaigns/Brasa_y_Marea'
OUT = ROOT/'phone-output/Brasa-y-Marea-fuentes.zip'

if __name__ == '__main__':
    validate()
    OUT.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(OUT,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as archive:
        for folder in (PACK,Path(__file__).parent):
            for path in sorted(folder.rglob('*')):
                if path.is_file() and '__pycache__' not in path.parts:
                    archive.write(path,path.relative_to(ROOT).as_posix())
        archive.write(ROOT/'COPYING','COPYING')
        archive.writestr('LEEME.txt',
            'Crónicas de la Brasa y la Marea — fuentes y recursos originales.\n'
            'Copia data/campaigns/Brasa_y_Marea dentro del árbol de datos de Wesnoth 1.19.27.\n'
            'El APK de Wesnoth Phone ya incluye este contenido; no necesita importar este ZIP.\n'
            'Las herramientas de packaging/android/campaigns se ejecutan desde el checkout completo.\n'
            'Consulta data/campaigns/Brasa_y_Marea/README.es.md y ART_PROMPTS.json.\n'
            'Código de construcción del port: https://github.com/torinescudo/wesnothapk\n')
    with zipfile.ZipFile(OUT) as archive:
        assert archive.testzip() is None
    OUT.with_suffix('.zip.sha256').write_text(hashlib.sha256(OUT.read_bytes()).hexdigest()+'  '+OUT.name+'\n')
    print(OUT,OUT.stat().st_size)
