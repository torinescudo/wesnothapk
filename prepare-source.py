#!/usr/bin/env python3
"""Check out the pinned full Wesnoth source and apply this repository's overlay."""
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'source'
REVISION = '682b77a27215f673397bfd2c6f65b854a01a6df8'

if not SOURCE.exists():
    subprocess.run(['git', 'init', str(SOURCE)], check=True)
    subprocess.run(['git', '-C', str(SOURCE), 'remote', 'add', 'origin',
                    'https://github.com/wesnoth/wesnoth.git'], check=True)
subprocess.run(['git', '-C', str(SOURCE), 'fetch', '--depth=1', 'origin', REVISION], check=True)
subprocess.run(['git', '-C', str(SOURCE), 'checkout', '--detach', REVISION], check=True)
subprocess.run(['git', '-C', str(SOURCE), 'submodule', 'update', '--init', '--recursive', '--depth=1'], check=True)
shutil.copytree(ROOT / 'overlay', SOURCE, dirs_exist_ok=True)
print(f'Prepared full game at {REVISION} with phone changes')
