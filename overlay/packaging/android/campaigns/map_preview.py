#!/usr/bin/env python3
"""Render .map files to PNG so map composition can be looked at, not just counted.

Map quality is a visual question first: terrain masses, coastline shape, road
networks and village spacing either read as a place or as noise. This draws one
tile per cell with a fixed palette, so a mainline map and a generated one can be
held next to each other.

    python3 map_preview.py OUT_DIR MAP [MAP ...]      # one PNG per map
    python3 map_preview.py --sheet OUT.png A.map B.map C.map   # one contact sheet

SPDX-License-Identifier: GPL-2.0-or-later
"""
from pathlib import Path
import argparse
import sys

from PIL import Image, ImageDraw

TILE = 14

# Colour per terrain family: enough to read composition at a glance.
FAMILIES = [
    (('Wo', 'Ww', 'Wr', 'Ws', 'Wd'), (36, 74, 110)),
    (('Iw', 'Ic', 'Ia', 'Is', 'Ir', 'Io'), (150, 190, 210)),
    (('Qx', 'Ql', 'Qt'), (60, 30, 34)),
    (('Xu', 'Xt', 'Xv', 'Ex'), (44, 40, 46)),
    (('Uu', 'Uh', 'Ur', 'Ut'), (86, 74, 64)),
    (('Mm', 'Md', 'Ms', 'Mv', 'Mt'), (122, 118, 116)),
    (('Hh', 'Hd', 'Ha', 'Ht'), (146, 138, 104)),
    (('Aa', 'Ai', 'At'), (228, 232, 238)),
    (('Ds', 'Dd', 'Dt'), (206, 182, 128)),
    (('Ss', 'Sm'), (92, 110, 84)),
    (('Rr', 'Rb', 'Re', 'Rp', 'Rd', 'Rt'), (150, 132, 108)),
    (('Gg', 'Gs', 'Gd', 'Gt', 'Gl'), (110, 148, 88)),
    (('C', 'K'), (150, 146, 138)),
    (('V', 'F', 'T', 'B', 'P', 'E', 'Q', 'D', 'O', 'X', 'Y', 'Z'), (120, 130, 120)),
]
BASE_COLOUR = (150, 150, 150)


def family_colour(code):
    base = code.split('^')[0]
    for prefixes, colour in FAMILIES:
        if base.startswith(prefixes):
            return colour
    return BASE_COLOUR


def lighten(colour, amount):
    return tuple(min(255, int(channel + (255 - channel) * amount)) for channel in colour)


def draw_map(text):
    # One chunk per comma, blanks included: the engine reads it that way, and a
    # dropped empty cell would shift a row instead of showing the gap.
    rows = [[cell.strip() for cell in line.split(',')]
            for line in text.splitlines() if line.strip()]
    width = max(len(row) for row in rows)
    height = len(rows)
    image = Image.new('RGB', (width * TILE, height * TILE), (20, 20, 24))
    draw = ImageDraw.Draw(image)
    for y, row in enumerate(rows):
        for x, cell in enumerate(row):
            parts = cell.split()
            owner = parts[0] if len(parts) > 1 else ''
            code = parts[-1]
            colour = family_colour(code)
            if '^F' in code:
                colour = (52, 92, 54)
            elif '^V' in code:
                colour = lighten(colour, 0.45)
            elif code.split('^')[0].startswith(('R', 'Re', 'Rp')):
                colour = (168, 148, 116)
            elif '^B' in code:
                colour = (176, 152, 108)
            left, top = x * TILE, y * TILE
            draw.rectangle([left, top, left + TILE - 1, top + TILE - 1], fill=colour)
            if '^V' in code:
                draw.ellipse([left + 4, top + 4, left + TILE - 5, top + TILE - 5], fill=(238, 214, 132))
            if owner.isdigit():
                keep = (232, 232, 236) if owner == '1' else (196, 96, 84)
                draw.rectangle([left + 2, top + 2, left + TILE - 3, top + TILE - 3], fill=keep)
    return image


def contact_sheet(paths, columns=3):
    tiles = [(path.name, draw_map(path.read_text(encoding='utf-8'))) for path in paths]
    width = max(image.width for _, image in tiles)
    height = max(image.height for _, image in tiles)
    rows = (len(tiles) + columns - 1) // columns
    sheet = Image.new('RGB', (columns * (width + 8), rows * (height + 8)), (16, 16, 20))
    for index, (name, image) in enumerate(tiles):
        left = (index % columns) * (width + 8) + 4
        top = (index // columns) * (height + 8) + 4
        sheet.paste(image, (left, top))
        ImageDraw.Draw(sheet).text((left + 4, top + 4), name, fill=(240, 232, 200))
    return sheet


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('output')
    parser.add_argument('--sheet', action='store_true',
                        help='put every map in one contact sheet')
    parser.add_argument('maps', nargs='+', type=Path)
    args = parser.parse_args(argv)
    paths = [path for path in args.maps if path.is_file()]
    if not paths:
        raise SystemExit('no map files given')
    if args.sheet:
        contact_sheet(paths).save(args.output, 'PNG')
        print('wrote %s with %d maps' % (args.output, len(paths)))
        return 0
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    for path in paths:
        draw_map(path.read_text(encoding='utf-8')).save(out / (path.stem + '.png'), 'PNG')
    print('wrote %d previews into %s' % (len(paths), out))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
