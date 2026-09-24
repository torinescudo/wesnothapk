#!/usr/bin/env python3
"""Structured, deterministic map synthesis for the original campaigns.

Mainline maps are composed: coastlines that look like coastlines, rivers with
bridges where roads cross them, forest masses, ridges with passes, roads that
connect keeps with villages, and villages placed where they can be defended. This
module builds that structure instead of per-tile noise, and then proves the
result before a map is accepted: every village and every objective must be
reachable from both keeps, and no map is emitted until that holds.

Only terrain codes declared in data/core/terrain.cfg are used; `verify_vocabulary`
checks that against the source tree when it is available.

SPDX-License-Identifier: GPL-2.0-or-later
"""
from collections import deque
import math
import random
import zlib

# --- walkability, shared with the validator and the mainline comparison ---
IMPASSABLE_BASES = ('Ww', 'Wo', 'Qx', 'Ql', 'Xu', 'Xv', 'Xo', '_f', '_s', 'Wr', 'Wd')
FORD_OVERLAYS = ('^Bw/', '^Bw|', '^Bw\\')
FORD_SUFFIXES = ('f',)

# --- terrain vocabulary ---
GRASS = ('Gg', 'Gs')
DIRT = ('Gd', 'Gt')
HILLS = ('Hh', 'Hhd')
MOUNTAINS = ('Mm', 'Md', 'Mdd', 'Ms', 'Mv')
SAND = ('Ds', 'Dd')
SWAMP = ('Ss', 'Sm')
SNOW = ('Aa', 'Ai')
SHALLOW = ('Ww', 'Wwg', 'Wwt')
DEEP = ('Wo', 'Wog', 'Wot', 'Ww', 'Wwr')
CAVE_FLOOR = ('Uu', 'Uue')
CAVE_HILLS = ('Uh', 'Uhe')
CAVE_WALL = ('Xu', 'Xur', 'Xue', 'Xuc')
CAVE_DECOR = ('^Uf', '^Ufi', '^Qhh', '^Qhu')
RUIN_DECOR = ('^Eb', '^Ebn', '^Edp', '^Edb', '^Efs', '^Es')
# Dirt tracks and stone paths: the surfaces a road can take in the wild.
TRACKS = ('Rp', 'Rd', 'Rb')
FOREST_PINE = ('^Fp', '^Fpa')
FOREST_DECIDUOUS = ('^Fds', '^Fdf', '^Fda', '^Fdw')
FOREST_TROPICAL = ('^Fet', '^Feta', '^Fetd', '^Feth')
FOREST_MIXED = ('^Fms', '^Fma', '^Fmw', '^Fmf')
FOREST_DRY = ('^Ft', '^Ftd', '^Ftp', '^Ftr', '^Fts')
VILLAGE_GRASS = ('^Vh', '^Vha', '^Vhs', '^Vht', '^Vhh')
VILLAGE_COAST = ('^Vhc', '^Vhca', '^Vhhr')
VILLAGE_HILL = ('^Vd', '^Vda', '^Vdr')
VILLAGE_FOREST = ('^Vhr', '^Vhha')
VILLAGE_CAVE = ('^Vu', '^Vud')
VILLAGE_RUIN = ('^Vct', '^Vc', '^Vca')
ROAD = ('Rr', 'Rra', 'Rrc', 'Rrd')
ROAD_EARTH = ('Re',)
BRIDGE = ('^Bw/', '^Bw|', '^Bw\\')

CASTLE_RING = {'grass': ('Ce', 'Chr', 'Ch'), 'coast': ('Ch', 'Chr'), 'harbor': ('Ch', 'Chw'),
               'cave': ('Cud',), 'quarry': ('Cm', 'Cm'), 'ruins': ('Cd', 'Cdr'),
               'mountain': ('Cv', 'Cvr'), 'forest': ('Ce', 'Cer'), 'plains': ('Ce', 'Cf'),
               'islands': ('Ch', 'Chr')}
KEEP = {'grass': 'Ke', 'coast': 'Kh', 'harbor': 'Kh', 'cave': 'Kud', 'quarry': 'Km',
        'ruins': 'Kd', 'mountain': 'Kv', 'forest': 'Ke', 'plains': 'Ke', 'islands': 'Kh'}

# Relative cost of walking. Impassable terrain is absent on purpose.
COST = {'Rr': 1, 'Rra': 1, 'Rrc': 1, 'Rrd': 1, 'Re': 2, 'Rp': 2,
        'Gg': 2, 'Gs': 2, 'Gd': 2, 'Gt': 2, 'Hh': 3, 'Hhd': 3, 'Ds': 2, 'Dd': 3,
        'Mm': 6, 'Md': 5, 'Mdd': 5, 'Ms': 6, 'Mv': 6, 'Ss': 5, 'Sm': 4,
        'Aa': 3, 'Ai': 3, 'Uu': 2, 'Uue': 2, 'Uh': 3, 'Uhe': 3, 'Ce': 1, 'Ch': 1,
        'Cf': 1, 'Cm': 1, 'Cd': 2, 'Cdr': 2, 'Cv': 1, 'Chr': 1, 'Chw': 1, 'Cud': 1}

# How a biome distributes its landscape before roads and villages are placed.
BIOMES = {
    'forest':   dict(water=0.010, river=True, forest=0.34, hill=0.14, mountain=0.05,
                     swamp=0.03, sand=0.00, snow=0.00, relief=2.1, villages=15),
    'coast':    dict(water=0.22, river=True, forest=0.12, hill=0.10, mountain=0.03,
                     swamp=0.03, sand=0.04, snow=0.00, relief=1.7, villages=13),
    'harbor':   dict(water=0.30, river=True, forest=0.06, hill=0.06, mountain=0.02,
                     swamp=0.02, sand=0.06, snow=0.00, relief=1.5, villages=15),
    'islands':  dict(water=0.40, river=False, forest=0.16, hill=0.10, mountain=0.02,
                     swamp=0.02, sand=0.10, snow=0.00, relief=2.0, villages=14),
    'cave':     dict(water=0.00, river=False, forest=0.00, hill=0.18, mountain=0.00,
                     swamp=0.00, sand=0.00, snow=0.00, relief=2.4, villages=14),
    'quarry':   dict(water=0.02, river=False, forest=0.10, hill=0.22, mountain=0.14,
                     swamp=0.00, sand=0.05, snow=0.00, relief=2.6, villages=14),
    'plains':   dict(water=0.06, river=True, forest=0.12, hill=0.08, mountain=0.02,
                     swamp=0.02, sand=0.03, snow=0.00, relief=1.3, villages=17),
    'mountain': dict(water=0.03, river=True, forest=0.16, hill=0.22, mountain=0.24,
                     swamp=0.00, sand=0.02, snow=0.05, relief=3.2, villages=13),
    'ruins':    dict(water=0.06, river=True, forest=0.14, hill=0.12, mountain=0.05,
                     swamp=0.03, sand=0.03, snow=0.02, relief=2.0, villages=16),
}


def base_of(code):
    return code.split('^')[0]


def quantile(values, fraction):
    """Value below which `fraction` of the samples fall: exact biome mixes."""
    if not values:
        return 0.0
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, int(fraction * len(ordered))))
    return ordered[index]


def is_walkable(code):
    """Water is passable only where a bridge or a ford crosses it."""
    if any(overlay in code for overlay in FORD_OVERLAYS):
        return True
    base = base_of(code)
    if base[2:] and base[2:] in FORD_SUFFIXES:
        return True
    return not base.startswith(IMPASSABLE_BASES)


def neighbours(x, y, width, height):
    """Wesnoth staggered columns: six neighbours, as in the engine's own map."""
    offset = -1 if x % 2 else 1
    for nx, ny in ((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y),
                   (x - 1, y + offset), (x + 1, y + offset)):
        if 0 <= nx < width and 0 <= ny < height:
            yield nx, ny


class Noise:
    """Deterministic value noise, enough for landform shaping without numpy."""

    def __init__(self, seed):
        self.seed = str(seed)

    def _hash(self, x, y, salt):
        # crc32, not hash(): python's string hash is salted per process, and a map
        # that changes between two runs of the same build is not a generated map.
        value = zlib.crc32(('%s|%s|%d|%d' % (self.seed, salt, x, y)).encode('utf-8'))
        return (value % 100000) / 100000.0

    def at(self, x, y, scale, salt='n'):
        gx, gy = x / scale, y / scale
        x0, y0 = math.floor(gx), math.floor(gy)
        tx, ty = gx - x0, gy - y0
        tx = tx * tx * (3 - 2 * tx)
        ty = ty * ty * (3 - 2 * ty)
        corners = (self._hash(x0, y0, salt), self._hash(x0 + 1, y0, salt),
                   self._hash(x0, y0 + 1, salt), self._hash(x0 + 1, y0 + 1, salt))
        top = corners[0] + (corners[1] - corners[0]) * tx
        bottom = corners[2] + (corners[3] - corners[2]) * tx
        return top + (bottom - top) * ty

    def fbm(self, x, y, scale, octaves=4, salt='n'):
        total, amplitude, norm = 0.0, 1.0, 0.0
        for octave in range(octaves):
            total += amplitude * self.at(x, y, scale / (2 ** octave), '%s%d' % (salt, octave))
            norm += amplitude
            amplitude *= 0.5
        return total / norm


class MapBuilder:
    def __init__(self, key, index, biome, goal, seed):
        self.key, self.index, self.biome, self.goal = key, index, biome, goal
        self.rng = random.Random(seed)
        self.noise = Noise(seed)
        self.spec = BIOMES[biome]
        self.width = 36 + (index * 3) % 11
        self.height = 26 + (index * 5) % 8
        self.terrain = [['Gg'] * self.width for _ in range(self.height)]
        self.land = [[True] * self.width for _ in range(self.height)]
        self.roads = set()
        self.villages = []
        self.start = self.enemy = self.destination = self.prison = None
        self.points = []

    # --- landscape ---------------------------------------------------------
    def shape_land(self):
        """Build a landness field whose thresholds produce the biome's own mix."""
        spec = self.spec
        w, h = self.width, self.height
        self.level = [[0.0] * w for _ in range(h)]
        coastal = self.biome in ('coast', 'harbor')
        islands = self.biome == 'islands'
        for y in range(h):
            for x in range(w):
                noise = self.noise.fbm(x, y, 11.0, 4, 'height')
                if coastal:
                    tx, ty = x / (w - 1), y / (h - 1)
                    landness = 1.15 - 0.95 * (0.55 * tx + 0.55 * ty) + (noise - 0.5) * 0.5
                elif islands:
                    near = min(math.hypot((x - cx) / 5.5, (y - cy) / 4.0)
                               for cx, cy in self._island_centres())
                    landness = 1.0 - near + (noise - 0.5) * 0.5
                else:
                    landness = noise
                self.level[y][x] = landness
        if self.biome == 'cave':
            # A cave has no sea: the walls are terrain, and _cave_code digs them.
            for y in range(h):
                for x in range(w):
                    self.land[y][x] = True
        else:
            self.cut = quantile([self.level[y][x] for y in range(h) for x in range(w)],
                                spec['water'])
            for y in range(h):
                for x in range(w):
                    self.land[y][x] = self.level[y][x] > self.cut
        self._remove_specks()

    def _island_centres(self):
        w, h = self.width, self.height
        spots = [(w * 0.22, h * 0.32), (w * 0.62, h * 0.22), (w * 0.78, h * 0.66),
                 (w * 0.34, h * 0.72)]
        return spots[:3 + self.index % 2]

    def _remove_specks(self):
        """Delete one-tile islands and one-tile lakes: noise must not survive as specks."""
        for _ in range(2):
            for y in range(self.height):
                for x in range(self.width):
                    same = sum(1 for nx, ny in neighbours(x, y, self.width, self.height)
                               if self.land[ny][nx] == self.land[y][x])
                    if same == 0:
                        self.land[y][x] = not self.land[y][x]

    def paint_relief(self):
        """Peaks, hills, forests and plains by rank, so each biome gets its own share."""
        spec = self.spec
        land = [(y, x) for y in range(self.height) for x in range(self.width) if self.land[y][x]]
        levels = [self.level[y][x] for y, x in land]
        forests = [self.noise.fbm(x, y, 6.5, 3, 'forest') for y, x in land]
        peak_cut = quantile(levels, 1.0 - spec['mountain'])
        hill_cut = quantile(levels, max(0.0, 1.0 - spec['mountain'] - spec['hill']))
        forest_cut = quantile(forests, spec['forest'])
        for y in range(self.height):
            for x in range(self.width):
                level = self.level[y][x]
                if not self.land[y][x]:
                    self.terrain[y][x] = self._water_code(level)
                    continue
                if self.biome == 'cave':
                    self.terrain[y][x] = self._cave_code(x, y)
                    continue
                forest = self.noise.fbm(x, y, 6.5, 3, 'forest')
                if level > peak_cut:
                    self.terrain[y][x] = self._mountain_code(y, x)
                elif level > hill_cut:
                    self.terrain[y][x] = self._hill_code(y, x)
                elif forest < forest_cut:
                    self.terrain[y][x] = self._forest_code(y, x)
                else:
                    base = self.rng.choice(GRASS if level > 0.45 else ('Gg',))
                    if self.biome == 'ruins':
                        decor = self.noise.fbm(x, y, 5.0, 2, 'ruindecor')
                        if decor > 0.60:
                            base += self.rng.choice(RUIN_DECOR)
                    self.terrain[y][x] = base

    def _water_code(self, level):
        if self.biome in ('coast', 'harbor') and level < self.cut - 0.18:
            return self.rng.choice(DEEP)
        if self.rng.random() < 0.10:
            return self.rng.choice(SHALLOW)
        return 'Ww'

    def _cave_code(self, x, y):
        walls = self.noise.fbm(x, y, 5.5, 3, 'wall')
        hills = self.noise.fbm(x, y, 4.0, 2, 'cavehill')
        decor = self.noise.fbm(x, y, 5.0, 2, 'cavedecor')
        if walls < 0.34:
            return self.rng.choice(CAVE_WALL)
        base = self.rng.choice(CAVE_HILLS if hills > 0.62 else CAVE_FLOOR)
        if decor > 0.64:
            base += self.rng.choice(CAVE_DECOR)
        return base

    def _mountain_code(self, y, x):
        if self.biome == 'mountain' and self.level[y][x] > 0.74:
            return self.rng.choice(('Ms', 'Mv'))
        if self.biome in ('quarry', 'ruins'):
            return self.rng.choice(('Mm', 'Md'))
        return self.rng.choice(MOUNTAINS)

    def _hill_code(self, y, x):
        if self.biome == 'quarry':
            return self.rng.choice(('Hh', 'Hhd', 'Gd'))
        return self.rng.choice(HILLS)

    def _forest_code(self, y, x):
        table = {'forest': FOREST_PINE + FOREST_DECIDUOUS + FOREST_MIXED,
                 'plains': FOREST_PINE + FOREST_DRY,
                 'coast': FOREST_PINE + FOREST_MIXED,
                 'harbor': FOREST_TROPICAL,
                 'islands': FOREST_TROPICAL,
                 'mountain': FOREST_PINE + FOREST_MIXED,
                 'ruins': FOREST_DECIDUOUS + FOREST_DRY,
                 'quarry': FOREST_DRY + FOREST_PINE}[self.biome]
        # A forest is an overlay on ground: trees never stand on bare sky.
        base = self.rng.choice(('Gg', 'Gg', 'Gs', 'Hh'))
        return base + self.rng.choice(table)

    def smooth_terrain(self, passes=1):
        """Remove single-tile specks: masses are what make a map look drawn."""
        families = self._families()
        for _ in range(passes):
            snapshot = [['' for _ in range(self.width)] for _ in range(self.height)]
            for y in range(self.height):
                for x in range(self.width):
                    snapshot[y][x] = self._family(self._plain(self.terrain[y][x]), families)
            for y in range(self.height):
                for x in range(self.width):
                    if not self.land[y][x] or self.terrain[y][x].split()[0].isdigit():
                        continue
                    counts = {}
                    for nx, ny in neighbours(x, y, self.width, self.height):
                        if not self.land[ny][nx]:
                            continue
                        counts[snapshot[ny][nx]] = counts.get(snapshot[ny][nx], 0) + 1
                    own = snapshot[y][x]
                    if counts.get(own, 0) or not counts:
                        continue
                    winner = max(sorted(counts), key=lambda name: counts[name])
                    if winner in ('castle', 'ruin'):
                        continue
                    self.terrain[y][x] = self._representative(winner, y, x)

    def _family(self, code, families):
        if '^F' in code:
            return 'forest'
        base = base_of(code)
        for name, members in families.items():
            if base in members:
                return name
        return 'grass'

    def _representative(self, family, y, x):
        table = {'grass': ('Gg', 'Gs'), 'hill': HILLS, 'mountain': MOUNTAINS, 'sand': SAND,
                 'swamp': SWAMP, 'snow': SNOW, 'water': ('Ww',), 'cave': CAVE_FLOOR}
        if family == 'forest':
            return self._forest_code(y, x)
        return self.rng.choice(table.get(family, ('Gg',)))

    def scatter_details(self):
        """Break each mass with features of another family: mainline maps are textured.

        The measurement is the largest same-family cluster: mainline sits near
        0.45 of its own tiles, and a smoothed noise field drifts past 0.65.
        """
        companions = {
            'grass': ('hill', 'forest', 'grass'),
            'forest': ('grass', 'forest', 'hill'),
            'hill': ('grass', 'rock', 'forest'),
            'mountain': ('hill', 'rock', 'grass'),
            'sand': ('grass', 'swamp', 'sand'),
            'swamp': ('grass', 'sand', 'swamp'),
            'snow': ('hill', 'mountain', 'snow'),
            'cave': ('cave', 'hill', 'cave'),
            'ruin': ('grass', 'ruin', 'hill'),
            'water': ('sand', 'water', 'grass'),
        }
        for y in range(self.height):
            for x in range(self.width):
                code = self._plain(self.terrain[y][x])
                if self.noise.fbm(x, y, 1.9, 2, 'detail') < 0.55:
                    continue
                family = self._family(code, self._families())
                if family == 'castle':
                    continue
                if not self.land[y][x]:
                    if self.noise.fbm(x, y, 4.5, 2, 'shallows') > 0.68:
                        self.terrain[y][x] = self.rng.choice(SHALLOW)
                    continue
                choice = self.rng.choice(companions.get(family, ('grass',)))
                self.terrain[y][x] = self._detail_tile(choice, family, y, x)

    def roughen_edges(self):
        """Inlets, headlands and islets: a mass edge should be irregular.

        Mainline coasts and forests have high-frequency edges and islands, so the
        map reads as a crop of a bigger world instead of a smooth blob.
        """
        for y in range(self.height):
            for x in range(self.width):
                here = self.land[y][x]
                around = [(nx, ny) for nx, ny in neighbours(x, y, self.width, self.height)]
                if not around:
                    continue
                other = sum(1 for nx, ny in around if self.land[ny][nx] != here)
                if other == 0:
                    continue
                rough = self.noise.fbm(x, y, 1.7, 2, 'edge')
                if here and rough > 0.62:
                    self.land[y][x] = False
                    self.terrain[y][x] = self._water_code(self.cut)
                elif not here and rough < 0.34 and other >= 3:
                    # An islet just off the coast, the kind a boat can reach.
                    self.land[y][x] = True
                    self.terrain[y][x] = self.rng.choice(SAND + GRASS)

    def _detail_tile(self, choice, family, y, x):
        if choice == family:
            return self.terrain[y][x]
        table = {'grass': ('Gg', 'Gs'), 'hill': HILLS, 'rock': MOUNTAINS,
                 'forest': None, 'sand': SAND, 'swamp': SWAMP, 'snow': SNOW,
                 'cave': CAVE_FLOOR, 'water': SHALLOW}
        if choice == 'forest':
            return self._forest_code(y, x)
        return self.rng.choice(table.get(choice, ('Gg',)))

    def _families(self):
        return {
            'grass': GRASS + DIRT + TRACKS + ROAD + ROAD_EARTH + ('Gg', 'Gs'),
            'forest': (),
            'hill': HILLS,
            'mountain': MOUNTAINS,
            'sand': SAND,
            'swamp': SWAMP,
            'snow': SNOW,
            'water': DEEP + SHALLOW,
            'cave': CAVE_FLOOR + CAVE_HILLS + CAVE_WALL,
            'castle': tuple(name for names in CASTLE_RING.values() for name in names),
        }

    def carve_rivers(self):
        """Rivers start on high ground and leave the map: they have a source.

        A river that dies inland reads as a mistake; mainline rivers come from a
        ridge and run off the frame or into the sea.
        """
        if not self.spec['river']:
            return
        for branch in range(1 + self.index % 2):
            sources = [(self.level[y][x], x, y)
                       for y in range(1, self.height // 2) for x in range(2, self.width - 2)
                       if self.land[y][x]]
            if not sources:
                return
            _, x, y = max(sources)
            x += self.rng.randrange(-3, 4)
            y = max(1, y)
            steps = 0
            while 0 <= x < self.width and steps < self.height * 3:
                self.land[y][x] = False
                self.terrain[y][x] = 'Ww'
                if self.rng.random() < 0.35 and x + 1 < self.width:
                    self.land[y][x + 1] = False
                    self.terrain[y][x + 1] = 'Ww'
                if y + 1 >= self.height:
                    break  # leaves the frame, like a river reaching the lowlands
                # Walk downhill: the water finds the lowest neighbour ahead.
                options = [(self.level[ny][nx], nx, ny)
                           for nx, ny in neighbours(x, y + 1, self.width, self.height)
                           if ny > y or nx != x]
                if not options:
                    break
                _, x, y = min(options)
                steps += 1

    def decorate_edges(self):
        """Beaches, swamps and snow follow the landform instead of being sprinkled."""
        spec = self.spec
        sand_chance = min(0.85, 0.20 + spec['sand'] * 5)
        for y in range(self.height):
            for x in range(self.width):
                if self.land[y][x]:
                    continue
                for nx, ny in neighbours(x, y, self.width, self.height):
                    if not self.land[ny][nx]:
                        continue
                    base = base_of(self.terrain[ny][nx])
                    if base in HILLS + MOUNTAINS:
                        continue
                    if self.rng.random() < sand_chance:
                        self.terrain[ny][nx] = self.rng.choice(SAND)
                    elif spec['swamp'] and self.rng.random() < spec['swamp'] * 3:
                        self.terrain[ny][nx] = self.rng.choice(SWAMP)
        if spec['snow']:
            # Snow takes its own share of the high ground: without the cut it
            # buries the mountains and the biome mix stops being what it says.
            land_levels = [self.level[y][x] for y in range(self.height)
                           for x in range(self.width) if self.land[y][x]]
            snow_cut = quantile(land_levels, max(0.0, 1.0 - spec['snow']))
            for y in range(self.height):
                for x in range(self.width):
                    if self.land[y][x] and self.level[y][x] > snow_cut:
                        self.terrain[y][x] = self.rng.choice(SNOW)

    # --- structure ---------------------------------------------------------
    def place_castles(self):
        w, h = self.width, self.height
        if self.index % 4 == 0:
            self.start, self.enemy = (3, 3), (w - 4, h - 4)
        elif self.index % 4 == 1:
            self.start, self.enemy = (3, h // 2), (w - 4, h // 2)
        elif self.index % 4 == 2:
            self.start, self.enemy = (3, h - 4), (w - 4, 3)
        else:
            self.start, self.enemy = (w // 2, h - 4), (w // 2, 3)
        self.start = self._nearest_land(self.start)
        self.enemy = self._nearest_land(self.enemy)
        ring = CASTLE_RING[self.biome]
        for player, (x, y) in ((1, self.start), (2, self.enemy)):
            for nx, ny in [(x, y)] + list(neighbours(x, y, w, h)):
                if not self.land[ny][nx]:
                    continue
                self.terrain[ny][nx] = self.rng.choice(ring)
            self.terrain[y][x] = '%d %s' % (player, KEEP[self.biome])

    def _nearest_land(self, spot, radius=16):
        sx, sy = spot
        best = None
        for dy in range(-radius, radius + 1):
            for dx in range(-radius, radius + 1):
                x, y = sx + dx, sy + dy
                if not (2 <= x < self.width - 2 and 2 <= y < self.height - 2):
                    continue
                if not self.land[y][x]:
                    continue
                code = self._plain(self.terrain[y][x])
                if base_of(code) in CAVE_WALL:
                    continue
                distance = dx * dx + dy * dy
                if best is None or distance < best[0]:
                    best = (distance, x, y)
        if best is None:
            raise RuntimeError('no land for a keep in %s' % self.key)
        return best[1], best[2]

    def choose_targets(self):
        """Objectives are spread over the map and kept away from both keeps."""
        candidates = []
        for y in range(2, self.height - 2):
            for x in range(2, self.width - 2):
                if not self.land[y][x]:
                    continue
                code = self._plain(self.terrain[y][x])
                if not is_walkable(code) or base_of(code) in MOUNTAINS + CAVE_WALL:
                    continue
                if self._distance(x, y, *self.start) < 5 or self._distance(x, y, *self.enemy) < 5:
                    continue
                candidates.append((x, y))
        self.rng.shuffle(candidates)
        picked = []
        minimum = 5 if self.goal == 'beacons' else 7
        for x, y in candidates:
            if all(self._distance(x, y, px, py) >= minimum for px, py in picked):
                picked.append((x, y))
            if len(picked) >= 4:
                break
        while len(picked) < 4:
            # Fall back to spread quadrants rather than stacking one tile: two
            # objectives on the same hex would be indistinguishable.
            quadrant = [(self.width // 3, self.height // 3),
                        (2 * self.width // 3, self.height // 3),
                        (self.width // 3, 2 * self.height // 3),
                        (2 * self.width // 3, 2 * self.height // 3)][len(picked)]
            fallback = self._nearest_land(quadrant, 8)
            if all(self._distance(*fallback, px, py) >= 2 for px, py in picked):
                picked.append(fallback)
            else:
                picked.append((min(fallback[0] + len(picked), self.width - 3),
                               min(fallback[1] + len(picked), self.height - 3)))
        if self.goal == 'beacons':
            self.points = picked[:3]
            self.destination, self.prison = picked[0], picked[1]
        elif self.goal == 'rescue':
            self.prison, self.destination = picked[0], picked[1]
        else:
            self.destination = picked[0]

    def carve_roads(self):
        targets = [self.enemy]
        if self.destination:
            targets.append(self.destination)
        if self.prison:
            targets.append(self.prison)
        targets += self.points
        for target in targets:
            path = self._path(self.start, target)
            if not path:
                return False
            for x, y in path:
                self._lay_road(x, y)
        return True

    def _path(self, start, goal):
        """A* over terrain cost so roads follow the ground, not the straight line."""
        frontier = [(0.0, start)]
        came = {start: None}
        cost = {start: 0.0}
        while frontier:
            frontier.sort(key=lambda row: row[0])
            _, current = frontier.pop(0)
            if current == goal:
                path = []
                while current is not None:
                    path.append(current)
                    current = came[current]
                return list(reversed(path))
            for nx, ny in neighbours(current[0], current[1], self.width, self.height):
                code = self._plain(self.terrain[ny][nx])
                base = base_of(code)
                if base in CAVE_WALL:
                    continue
                if not is_walkable(code) and base not in ('Ww', 'Wo'):
                    continue
                # Water is crossable, but only where a detour would cost more: that
                # is what puts bridges on the roads instead of around the rivers.
                step = 12 if not is_walkable(code) else COST.get(base, 3)
                tentative = cost[current] + step
                if (nx, ny) not in cost or tentative < cost[(nx, ny)]:
                    cost[(nx, ny)] = tentative
                    came[(nx, ny)] = current
                    frontier.append((tentative, (nx, ny)))
        return None

    def _lay_road(self, x, y):
        cell = self.terrain[y][x]
        base = base_of(self._plain(cell))
        if cell.split()[0].isdigit() or '^V' in cell or base[:1] in CASTLE_RING:
            # A keep carries a start marker, a village is a place and a castle
            # ring is a fortification: roads go around all three.
            return
        code = self._plain(cell)
        self.roads.add((x, y))
        if not is_walkable(code) and base not in ('Ww', 'Wo'):
            return
        if base in ('Ww', 'Wo'):
            self.terrain[y][x] = base + self.rng.choice(BRIDGE)
            return
        if base in SAND:
            self.terrain[y][x] = self.rng.choice(ROAD_EARTH)
        elif base in TRACKS or self.biome == 'ruins':
            self.terrain[y][x] = self.rng.choice(ROAD_EARTH + ROAD[:1])
        else:
            self.terrain[y][x] = self.rng.choice(ROAD)

    def build_road_network(self):
        """Branches and verges on top of the arterials: a network, not spokes.

        The target is about a tenth of the map's tiles on road, three times what
        a set of spokes from the keeps produces.
        """
        # Branches from the middle of the arterial to the map's corners: roads
        # that go somewhere, instead of spokes that end at the objective.
        trunk = self._path(self.start, self.enemy) or []
        for index, corner in enumerate([(2, 2), (self.width - 3, 2),
                                        (2, self.height - 3), (self.width - 3, self.height - 3)]):
            if index % 2 != self.index % 2 or not trunk:
                continue
            try:
                target = self._nearest_land(corner, 6)
            except RuntimeError:
                continue  # that corner is open sea or a wall on this map
            origin = trunk[len(trunk) // 2]
            path = self._path(origin, target)
            if path:
                for x, y in path:
                    self._lay_road(x, y)
        # Spurs: short stubs off existing road, the verges and lookouts.
        for _ in range(5 + self.index % 3):
            if not self.roads:
                break
            x, y = sorted(self.roads)[self.rng.randrange(len(self.roads))]
            for _ in range(4 + self.rng.randrange(5)):
                steps = [(nx, ny) for nx, ny in neighbours(x, y, self.width, self.height)
                         if self.land[ny][nx] and (nx, ny) not in self.roads]
                if not steps:
                    break
                x, y = steps[self.rng.randrange(len(steps))]
                self._lay_road(x, y)

    def place_villages(self):
        """Settlements against a feature, spaced apart, rarely on the road.

        Mainline spreads villages about six tiles apart and puts only a third of
        them next to a road: a village belongs by a forest edge, a hill foot or a
        bay, which is also where a defender would want it.
        """
        wanted = self.spec['villages']
        candidates = []
        for y in range(2, self.height - 2):
            for x in range(2, self.width - 2):
                if not self.land[y][x]:
                    continue
                code = self._plain(self.terrain[y][x])
                base = base_of(code)
                if base in MOUNTAINS + CAVE_WALL + SAND + SWAMP + SNOW:
                    continue
                if self._distance(x, y, *self.start) < 4 or self._distance(x, y, *self.enemy) < 4:
                    continue
                families = {self._family(self._plain(self.terrain[ny][nx]), self._families())
                            for nx, ny in neighbours(x, y, self.width, self.height)
                            if self.land[ny][nx]}
                own = self._family(code, self._families())
                feature = len(families - {own, 'castle'})
                # A village wants a shore, a mountain foot or a forest edge: the
                # places a settlement can be found on a real map.
                siting = (3 if 'water' in families else 0) + (2 if 'mountain' in families else 0) \
                    + (2 if 'forest' in families else 0) + (1 if base in HILLS else 0)
                near_road = sum(1 for nx, ny in neighbours(x, y, self.width, self.height)
                                if (nx, ny) in self.roads) + (1 if (x, y) in self.roads else 0)
                score = siting + feature - near_road * 2
                candidates.append((score, x, y, near_road))
        candidates.sort(key=lambda row: (-row[0], row[1], row[2]))
        placed, roadside = [], 0
        for _, x, y, near_road in candidates:
            if len(placed) >= wanted:
                break
            if not all(self._distance(x, y, px, py) >= 5 for px, py in placed):
                continue
            if near_road and roadside + 1 > wanted // 3:
                continue  # at most a third of the villages may touch a road
            if near_road:
                roadside += 1
            placed.append((x, y))
        for x, y in placed:
            self.terrain[y][x] = self._village_code(x, y)
        self.villages = placed

    def _village_code(self, x, y):
        base = base_of(self._plain(self.terrain[y][x]))
        if self.biome == 'cave':
            table = VILLAGE_CAVE
        elif self.biome == 'ruins':
            table = VILLAGE_RUIN
        elif self.biome in ('coast', 'harbor'):
            table = VILLAGE_COAST + VILLAGE_GRASS
        elif base in HILLS:
            table = VILLAGE_HILL
        elif base in FOREST_PINE + FOREST_DECIDUOUS + FOREST_TROPICAL + FOREST_MIXED + FOREST_DRY:
            table = VILLAGE_FOREST
        else:
            table = VILLAGE_GRASS
        return base + self.rng.choice(table)

    def _plain(self, code):
        return code.split()[-1]

    def _distance(self, ax, ay, bx, by):
        return math.hypot(ax - bx, ay - by)

    # --- verification ------------------------------------------------------
    def reachable_from(self, origin):
        seen = {origin}
        queue = deque([origin])
        while queue:
            x, y = queue.popleft()
            for nx, ny in neighbours(x, y, self.width, self.height):
                if (nx, ny) in seen:
                    continue
                if not is_walkable(self._plain(self.terrain[ny][nx])):
                    continue
                seen.add((nx, ny))
                queue.append((nx, ny))
        return seen

    def verify(self):
        if self.start is None or self.enemy is None:
            return False, 'keeps not placed'
        for player, origin in (('1', self.start), ('2', self.enemy)):
            reached = self.reachable_from(origin)
            for village in self.villages:
                if village not in reached:
                    return False, 'village %s unreachable from keep %s' % (village, player)
            for name, target in (('destination', self.destination), ('prison', self.prison)):
                if target and target not in reached:
                    return False, '%s unreachable from keep %s' % (name, player)
            for point in self.points:
                if point not in reached:
                    return False, 'objective point unreachable from keep %s' % player
        for target in [self.destination, self.prison, *self.points]:
            if not target:
                continue
            code = self._plain(self.terrain[target[1]][target[0]])
            if not is_walkable(code) or base_of(code) in MOUNTAINS + CAVE_WALL:
                return False, 'objective on impassable terrain'
        return True, 'ok'

    def serialise(self):
        rows = []
        for y in range(self.height):
            rows.append([self.terrain[y][x] for x in range(self.width)])
        # The off-board ring must match the interior width: gamemap::read rejects
        # any map whose rows differ in length ("Map not a rectangle.").
        border = [rows[0][0]] * (self.width + 2)
        bordered = [border] + [[row[0]] + row + [row[-1]] for row in rows] + [border]
        return '\n'.join(', '.join(row) for row in bordered) + '\n'

    def wml_point(self, point):
        """Internal (x, y) to WML coordinates: the exported map carries a border ring."""
        return (point[0] + 1, point[1] + 1)

    def stats(self):
        codes = [self._plain(cell) for row in self.terrain for cell in row]
        return {
            'width': self.width,
            'height': self.height,
            'area': self.width * self.height,
            'distinct_terrain': len(set(codes)),
            'villages': len(self.villages),
            'forest': sum(1 for code in codes if '^F' in code),
            'water': sum(1 for code in codes if base_of(code) in DEEP + SHALLOW),
            'mountain': sum(1 for code in codes if base_of(code) in MOUNTAINS),
            'road': sum(1 for code in codes if base_of(code)[:1] == 'R'),
            'bridge': sum(1 for code in codes if '^B' in code),
            'sand': sum(1 for code in codes if base_of(code) in SAND),
            'swamp': sum(1 for code in codes if base_of(code) in SWAMP),
        }


def generate(key, index, biome, goal, seed=None, attempts=12):
    """Build one map, retrying with new seeds until its structure verifies."""
    reason = 'no attempt was made'
    for attempt in range(attempts):
        attempt_seed = '%s:%s:%s:%s:%s' % (seed or 'brasa-marea', key, index, biome, attempt)
        builder = MapBuilder(key, index, biome, goal, attempt_seed)
        builder.shape_land()
        builder.roughen_edges()
        builder.paint_relief()
        builder.smooth_terrain()
        builder.scatter_details()
        builder.carve_rivers()
        builder.decorate_edges()
        builder.place_castles()
        builder.choose_targets()
        if not builder.carve_roads():
            continue
        builder.place_villages()
        builder.build_road_network()
        ok, reason = builder.verify()
        if not ok:
            continue
        return {
            'rows': builder.serialise(),
            'start': builder.wml_point(builder.start),
            'enemy': builder.wml_point(builder.enemy),
            'destination': builder.wml_point(builder.destination) if builder.destination else None,
            'prison': builder.wml_point(builder.prison) if builder.prison else None,
            'points': [builder.wml_point(point) for point in builder.points],
            'villages': [builder.wml_point(v) for v in builder.villages],
            'stats': builder.stats(),
            'attempts': attempt + 1,
        }
    raise RuntimeError('no verifiable map for %s chapter %s (last reason: %s)'
                       % (key, index, reason))


def verify_vocabulary(terrain_cfg):
    """Every code this module can emit must exist in the engine's terrain list."""
    import re
    declared = set(re.findall(r'^\s*string\s*=\s*"?([A-Za-z0-9^|\\/_*!]+)',
                              terrain_cfg.read_text(encoding='utf-8'), re.M))
    overlays = {name for group in (FOREST_PINE, FOREST_DECIDUOUS, FOREST_TROPICAL, FOREST_MIXED,
                                  FOREST_DRY, VILLAGE_GRASS, VILLAGE_COAST, VILLAGE_HILL,
                                  VILLAGE_FOREST, VILLAGE_CAVE, VILLAGE_RUIN, BRIDGE,
                                  CAVE_DECOR, RUIN_DECOR)
                for name in group}
    bases = {name for group in (GRASS, DIRT, HILLS, MOUNTAINS, SAND, SWAMP, SNOW, SHALLOW,
                                DEEP, CAVE_FLOOR, CAVE_HILLS, CAVE_WALL, TRACKS, ROAD,
                                ROAD_EARTH) for name in group}
    bases |= {name for names in CASTLE_RING.values() for name in names}
    bases |= set(KEEP.values())
    unknown_bases = sorted(name for name in bases if name not in declared)
    unknown_overlays = sorted(name for name in overlays if name not in declared)
    if unknown_bases or unknown_overlays:
        raise AssertionError('terrain not declared in terrain.cfg: %s %s'
                             % (unknown_bases, unknown_overlays))
    return {'bases': len(bases), 'overlays': len(overlays)}
