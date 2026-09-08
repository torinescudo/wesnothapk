#!/usr/bin/env python3
"""Build the six original campaigns from authored stories and deterministic maps.

No network access. Re-run after editing stories.py; hand-authored narrative stays
separate from the shared, testable objective implementations.
SPDX-License-Identifier: GPL-2.0-or-later
"""
from pathlib import Path
import hashlib
import json
import math
import random
from stories import CAMPAIGNS

ROOT = Path(__file__).resolve().parents[3]
PACK = ROOT / 'data/campaigns/Brasa_y_Marea'
REL = 'campaigns/Brasa_y_Marea'


def q(text):
    return '"' + str(text).replace('"', "'") + '"'


def tag(name, attrs=None, body=''):
    lines = [f'[{name}]']
    lines += [f'    {k}={q(v)}' for k, v in (attrs or {}).items()]
    lines += ['    ' + line for line in body.splitlines()]
    lines.append(f'[/{name}]')
    return '\n'.join(lines) + '\n'


def message(who, text):
    return tag('message', {'speaker': who, 'message': text})


def event(name, body, attrs=None):
    return tag('event', {'name': name, **(attrs or {})}, body)


def endlevel(result):
    return tag('endlevel', {'result': result, 'bonus': 'yes',
                          'carryover_percentage': 40, 'carryover_add': 'yes'})


def write(relative, text):
    path = PACK / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8', newline='\n')


FACTIONS = {
    'outlaws': ('Outlaw', 'Thug,Poacher,Footpad'),
    'loyalists': ('Lieutenant', 'Spearman,Bowman,Heavy Infantryman'),
    'undead': ('Dark Sorcerer', 'Skeleton,Skeleton Archer,Ghoul,Vampire Bat'),
    'nagas': ('Naga Warrior', 'Naga Fighter,Naga Guard'),
    'velarios': ('CBM Velario Arconte', 'CBM Velario Lancero,CBM Velario Cosechador,CBM Velario Vigia,CBM Velario Cantor'),
    'litarios': ('CBM Litario Bastion', 'CBM Litario Guardian,CBM Litario Resonador,CBM Litario Tejedor,CBM Litario Explorador'),
}

VETERANS = {'outlaws':'Trapper', 'loyalists':'Swordsman', 'undead':'Revenant',
            'nagas':'Naga Warrior', 'velarios':'CBM Velario Prisma', 'litarios':'CBM Litario Bastion'}

HEROES = {
    'alba': ('smallfoot', 'lawful', 'pierce', 8, 3, 'fire', 5, 2),
    'sira': ('dwarvishfoot', 'neutral', 'impact', 10, 3, 'arcane', 7, 2),
    'iria': ('woodland', 'neutral', 'blade', 6, 3, 'pierce', 8, 3),
    'maura': ('smallfoot', 'chaotic', 'impact', 6, 2, 'arcane', 10, 3),
    'nerea': ('elusivefoot', 'neutral', 'blade', 8, 3, 'pierce', 7, 2),
    'darian': ('smallfoot', 'lawful', 'blade', 7, 3, 'pierce', 7, 2),
}

PROTECTED = {
    ('alba',1): ('Nima', 'Peasant'),
    ('sira',2): ('Varon de la Raíz', 'CBM Litario Explorador'),
    ('sira',4): ('Leth, aprendiz de ingeniería', 'Peasant'),
    ('iria',3): ('Esh', 'CBM Velario Vigia'),
    ('iria',5): ('Barun, portador del cristal', 'Peasant'),
    ('maura',3): ('Notario Kelm', 'Peasant'),
    ('maura',4): ('Udren, conductor del carro', 'Peasant'),
    ('nerea',1): ('Ciro, piloto del puerto', 'Peasant'),
    ('nerea',5): ('Talia', 'Peasant'),
    ('nerea',7): ('Yara, buceadora', 'Mermaid Initiate'),
    ('nerea',10): ('Issa, emisaria del arrecife', 'Naga Fighter'),
    ('darian',4): ('Seyth, intérprete', 'CBM Velario Cantor'),
    ('darian',5): ('Rella, delegada de los campos', 'Peasant'),
    ('darian',8): ('Sevrin', 'Deathblade'),
    ('darian',10): ('Myr, escribana de la capital', 'Peasant'),
    ('darian',14): ('Irena, portavoz de los barrios', 'Peasant'),
}


def attack(name, dtype, damage, count, ranged=False, special=''):
    icon = 'attacks/magic-missile.png' if ranged else 'attacks/sword-human.png'
    return tag('attack', {'name': name, 'description': name, 'type': dtype,
                         'range': 'ranged' if ranged else 'melee', 'damage': damage,
                         'number': count, 'icon': icon},
               tag('specials', body=special) if special else '')


def unit_types():
    content = ''
    for rid, singular, plural, names, desc in [
        ('litario', 'Litario', 'Litarios', 'Sira,Tarek,Onet,Vesh,Kora,Emet,Naru,Tessa',
         'Seres de basalto vivo atravesados por vetas luminosas. Nacen en cámaras donde la montaña conserva recuerdos. Resisten cortes y perforaciones, pero el frío vuelve frágiles sus vetas. Sus tejedores restauran piedra viva y sus resonadores combaten a distancia.'),
        ('velario', 'Velario', 'Velarios', 'Esh,Thess,Oth,Veyth,Uru,Neth,Sesher,Yss',
         'Pueblo alado de quitina nacarada y cuatro brazos. Almacenan luz en cristales y antiguamente sostenían ciudades en el cielo. Vuelan sobre agua y montañas; sus cuerpos ligeros son vulnerables a lanzas y fuego. Sus cantores curan con luz almacenada.')]:
        content += tag('race', {'id': 'cbm_' + rid, 'male_name': singular,
                               'female_name': singular[:-1] + 'a', 'plural_name': plural,
                               'num_traits': 2, 'markov_chain_size': 2,
                               'male_names': names, 'female_names': names, 'description': desc})
    # Four two-level lines for each original race. Full stats and attacks avoid
    # inheriting another species' animations, sounds or advancement tree.
    rosters = {
        'litario': [
            ('Guardian', 'Guardián de veta', 'Bastion', 'Bastión de basalto', 43, 4, 17, 'impact', 8, 3, 0, 'fighter'),
            ('Resonador', 'Resonador', 'Voz Profunda', 'Voz profunda', 30, 4, 19, 'arcane', 7, 3, 1, 'archer'),
            ('Tejedor', 'Tejedor de grietas', 'Restaurador', 'Restaurador', 31, 4, 18, 'impact', 5, 2, 2, 'healer'),
            ('Explorador', 'Buscavetas', 'Caminante', 'Caminante del estrato', 32, 6, 16, 'blade', 6, 3, 0, 'scout')],
        'velario': [
            ('Lancero', 'Lancero solar', 'Arconte', 'Arconte del alba', 32, 6, 18, 'pierce', 7, 3, 0, 'fighter'),
            ('Cosechador', 'Cosechador de luz', 'Prisma', 'Maestro del prisma', 27, 6, 20, 'fire', 6, 3, 1, 'archer'),
            ('Vigia', 'Vigía de las corrientes', 'Acechante', 'Acechante del cielo', 28, 8, 18, 'blade', 5, 3, 0, 'scout'),
            ('Cantor', 'Cantor de luz', 'Aurora', 'Cantor de aurora', 28, 6, 19, 'arcane', 5, 2, 2, 'healer')]
    }
    manifest = []
    for race, rows in rosters.items():
        title = race.capitalize()
        for short, label, advance, higher, hp, moves, cost, dtype, damage, count, kind, usage in rows:
            for level, uid, name in [(1, short, label), (2, advance, higher)]:
                fullid = f'CBM {title} {uid}'
                asset = f'cbm/units/{race}-{short.lower()}.png'
                profile = ('cbm/portraits/velario.png~SCALE(400,600)'
                           if race == 'velario' and short == 'Lancero'
                           else asset + '~SCALE(360,360)')
                # Runtime image scaling leaves the generated source art intact.
                body = ''
                if kind == 2:
                    body += tag('abilities', body='{ABILITY_HEALS}' if level == 1 else '{ABILITY_CURES}')
                if race == 'litario':
                    body += tag('resistance', {'blade': 70, 'pierce': 70, 'impact': 100, 'fire': 100, 'cold': 130, 'arcane': 110})
                else:
                    body += tag('resistance', {'blade': 100, 'pierce': 120, 'impact': 90, 'fire': 120, 'cold': 90, 'arcane': 100})
                body += attack('Golpe de veta' if race == 'litario' else 'Lanza de cristal',
                               dtype if kind == 0 else 'impact', damage + (3 if level == 2 else 0), count if kind == 0 else 2)
                if kind:
                    body += attack('Resonancia' if race == 'litario' else 'Destello', dtype,
                                   damage + (3 if level == 2 else 0), count, True, '{WEAPON_SPECIAL_MAGICAL}')
                if level == 2:
                    body += '{AMLA_DEFAULT}\n'
                content += tag('unit_type', {'id': fullid, 'name': name, 'race': 'cbm_' + race,
                    'image': asset + '~SCALE(72,72)', 'profile': profile,
                    'hitpoints': hp + (16 if level == 2 else 0), 'movement': moves,
                    'movement_type': 'dwarvishfoot' if race == 'litario' else 'smallfly',
                    'level': level, 'alignment': 'neutral' if race == 'litario' else 'lawful',
                    'experience': 40 if level == 1 else 90,
                    'advances_to': f'CBM {title} {advance}' if level == 1 else 'null',
                    'cost': cost + (15 if level == 2 else 0), 'usage': usage,
                    'description': f'{name}: ' + ('defiende la memoria de su montaña.' if race == 'litario' else 'protege los cristales que sostienen a su pueblo.')}, body)
                manifest.append(fullid)
    for campaign in CAMPAIGNS:
        key = campaign['key']
        move, alignment, melee, md, mn, ranged, rd, rn = HEROES[key]
        body = '{AMLA_DEFAULT}\n' + tag('abilities', body='{ABILITY_LEADERSHIP}')
        body += attack('Bastón' if key in ('sira', 'maura') else 'Arma de mano', melee, md, mn)
        body += attack('Luz de la linterna' if key == 'alba' else 'Ataque a distancia', ranged, rd, rn, True,
                       '{WEAPON_SPECIAL_MAGICAL}' if key in ('sira', 'maura') else '')
        if key == 'sira':
            body += tag('resistance', {'blade': 70, 'pierce': 70, 'cold': 130})
        if key == 'nerea':
            body += tag('movement_costs', {'shallow_water': 1, 'reef': 1})
            body += tag('defense', {'shallow_water': 40, 'reef': 30})
        content += tag('unit_type', {'id': 'CBM Hero ' + key, 'name': campaign['hero'], 'race': campaign['race'],
            'image': f'cbm/units/hero-{key}.png~SCALE(72,72)', 'profile': f'cbm/portraits/{key}.png~SCALE(400,600)',
            'gender': 'male' if key == 'darian' else 'female',
            'hitpoints': 58 if key == 'sira' else 48, 'movement': 6, 'movement_type': move,
            'level': 2, 'alignment': alignment, 'experience': 70, 'advances_to': 'null',
            'cost': 40, 'usage': 'fighter', 'description': campaign['premise']}, body)
        manifest.append('CBM Hero ' + key)
    write('units/units.cfg', content)
    return manifest


def make_map(key, index, biome, goal):
    rng = random.Random(f'brasa-marea:{key}:{index}:{biome}')
    width, height = 22 + (index % 4) * 2, 16 + (index % 3) * 2
    tiles = [['Gg' for _ in range(width)] for _ in range(height)]
    choices = {
        'forest': ['Gg'] * 5 + ['Gs^Fp'] * 4 + ['Hh'],
        'coast': ['Gg'] * 6 + ['Ds'] * 2 + ['Hh', 'Gs^Fp'],
        'harbor': ['Gg'] * 5 + ['Rr'] * 3 + ['Ds', 'Hh'],
        'cave': ['Uu'] * 7 + ['Uh'] * 2 + ['Xu'],
        'quarry': ['Hh'] * 4 + ['Gg'] * 4 + ['Mm'] * 2,
        'plains': ['Gg'] * 7 + ['Gs^Fp', 'Hh', 'Ss'],
        'mountain': ['Hh'] * 4 + ['Mm'] * 3 + ['Gg'] * 3,
        'ruins': ['Gg'] * 5 + ['Rr'] * 3 + ['Hh', 'Gs^Fp'],
        'islands': ['Ww'] * 5 + ['Ds'] * 3 + ['Gg'] * 2,
    }[biome]
    for y in range(height):
        for x in range(width):
            tiles[y][x] = rng.choice(choices)
            field = math.sin(x*.47+index) + math.cos(y*.59-index*.3)
            if biome == 'forest':
                tiles[y][x] = 'Gs^Fp' if field > .05 else ('Hh' if field < -1.3 else 'Gg')
            elif biome == 'mountain':
                tiles[y][x] = 'Mm' if field > .75 else ('Hh' if field > -.8 else 'Gg')
            elif biome == 'cave':
                tiles[y][x] = 'Xu' if field > 1.1 else ('Uh' if field > .35 else 'Uu')
            elif biome == 'islands':
                centers = [(4,height//2),(width//2,4),(width-5,height//2),(width//2,height-4)]
                distance = min(((x-a)/4)**2+((y-b)/3)**2 for a,b in centers)
                tiles[y][x] = 'Gg' if distance < .55 else ('Ds' if distance < 1.1 else 'Ww')
            if biome in ('coast', 'harbor') and y > height - 5:
                tiles[y][x] = 'Ww' if y < height - 2 else 'Wo'
    start, enemy = (3, height // 2), (width - 3, height // 2)
    exithex = (width - 2, height - 4)
    prison = (width // 2, 4)
    points = [(width // 3, 4), (width // 2, height - 4), (width - 5, 5)]
    if index % 4 == 0:
        start, enemy = (3,4), (width-3,height-4)
        exithex = (width-2,height-2)
    elif index % 4 == 2:
        start, enemy = (3,height-4), (width-3,4)
        exithex = (width-2,3)
    elif index % 4 == 3:
        start, enemy = (width//2,height-3), (width//2,3)
        exithex, prison = (width-3,2), (width//3,4)
        points = [(width//3,4),(width-5,height//2),(5,height//2)]
    road = 'Uu' if biome == 'cave' else 'Rr'

    def set_tile(p, terrain):
        x, y = p
        tiles[y-1][x-1] = terrain

    # Connected two-hex-wide land routes make every required destination
    # reachable by all recruit types, including the escort, in every biome.
    for target in [enemy, exithex, prison, *points]:
        x, y = start
        while (x, y) != target:
            set_tile((x, y), road)
            if y + 1 <= height:
                set_tile((x, y + 1), road)
            if x != target[0] and (y == target[1] or rng.random() < .65):
                x += 1 if x < target[0] else -1
            else:
                y += 1 if y < target[1] else -1
        set_tile(target, road)
    # Villages in bands reward movement and provide healing for each army.
    for x in range(4, width - 2, 4):
        for y in (6, height - 5):
            village = {'cave':'Uu^Vud','ruins':'Gg^Vhr','harbor':'Gg^Vhc'}.get(biome,'Gg^Vh')
            set_tile((x, y), village)
    for number, keep in [(1, start), (2, enemy)]:
        x, y = keep
        for dx, dy in [(0,-1),(0,1),(-1,0),(1,0),(-1,1),(1,1)]:
            castle = {'cave':'Cud','ruins':'Chr','harbor':'Ch'}.get(biome,'Ce')
            set_tile((x+dx, y+dy), castle)
        keep_terrain = {'cave':'Kud','ruins':'Khr','harbor':'Kh'}.get(biome,'Ke')
        set_tile(keep, f'{number} ' + keep_terrain)
    for p in [exithex, prison, *points]:
        set_tile(p, road)
    set_tile((prison[0], prison[1]+1), road)
    return '\n'.join(', '.join(row) for row in tiles) + '\n', start, enemy, exithex, prison, points


GOALS = {
    'conquer': 'Derrota al líder enemigo.',
    'survive': 'Mantén con vida a tu protagonista hasta el comienzo del turno 12.',
    'escape': 'Lleva a tu protagonista al destino señalado con una bandera.',
    'escort': 'Escolta a la persona protegida hasta la bandera de salida.',
    'rescue': 'Llega con cualquier unidad a la prisión y escolta a la persona liberada hasta la bandera.',
    'beacons': 'Activa los tres puntos señalados llevando una unidad a cada uno.',
}


def scenario(c, index, row, manifest):
    title, goal, biome, antagonist, opening, ally, hero_line, resolution = row
    key, cid = c['key'], 'CBM_' + c['key']
    sid = f'{cid}_{index:02d}'
    following = f'{cid}_{index+1:02d}' if index < len(c['chapters']) else 'null'
    mapdata, start, enemy, destination, prison, points = make_map(key, index, biome, goal)
    write(f'maps/{key}_{index:02d}.map', mapdata)
    faction = c['enemy']
    if key == 'sira' and index == 3:
        faction = 'litarios'
    leader, recruits = FACTIONS[faction]
    if index > len(c['chapters']) // 2:
        recruits += ',' + VETERANS[faction]
    if key == 'darian' and index == 15:
        leader = 'CBM Hero maura'
    body = '{DEFAULT_SCHEDULE}\n'
    body += tag('music', {'name': f'cbm/{key}-journey.ogg', 'ms_after': 2000})
    body += tag('music', {'name': f'cbm/{key}-battle.ogg', 'append': 'yes', 'ms_after': 2000})
    body += tag('story', body=tag('part', {'story': opening, 'background': f'cbm/portraits/{key}.png~SCALE(540,810)', 'scale_background': 'no'}))
    recruit = c['recruit'].replace('Scout', 'Elvish Scout')
    if key == 'darian' and index >= 4:
        recruit += ',CBM Litario Guardian,CBM Litario Tejedor'
    if key == 'darian' and index >= 6:
        recruit += ',CBM Velario Lancero,CBM Velario Cantor'
    player = {'side': 1, 'controller': 'human', 'team_name': 'pacto', 'user_team_name': c['hero'],
              'id': cid + '_hero', 'name': c['hero'], 'type': 'CBM Hero ' + key,
              'canrecruit': 'yes', 'unrenamable': 'yes', 'recruit': recruit,
              'gold': 150 + min(index * 8, 100), 'income': 3,
              'village_gold': 2, 'fog': 'no', 'shroud': 'no', 'save_id': cid + '_army'}
    body += tag('side', player)
    enemy_gold = 100 + index * 6
    body += tag('side', {'side': 2, 'controller': 'ai', 'team_name': 'oposicion',
                        'user_team_name': antagonist, 'type': leader, 'id': sid + '_enemy',
                        'name': antagonist, 'canrecruit': 'yes', 'recruit': recruits,
                        'gold': enemy_gold, 'income': 2, 'village_gold': 2},
                tag('ai', {'aggression': .6, 'caution': .25, 'passive_leader': 'yes'}))
    conditions = tag('objective', {'description': GOALS[goal], 'condition': 'win'})
    conditions += tag('objective', {'description': 'Muerte de ' + c['hero'], 'condition': 'lose'})
    conditions += tag('objective', {'description': 'Muerte de ' + c['companion'], 'condition': 'lose'})
    if goal in ('escort', 'rescue'):
        conditions += tag('objective', {'description': 'Muerte de la persona protegida', 'condition': 'lose'})
    if goal != 'survive':
        conditions += tag('objective', {'description': 'Se agotan los turnos', 'condition': 'lose'})
    conditions += tag('gold_carryover', {'bonus': 'yes', 'carryover_percentage': 40})
    conditions += tag('note', {'description': 'Toca una casilla para preparar el movimiento y pulsa Mover/atacar. Puedes revisar estos objetivos desde Más.'})
    pre = tag('objectives', {'side': 1}, conditions)
    pre += tag('allow_recruit', {'side': 1, 'type': recruit})
    pre += '{VARIABLE cbm_points 0}\n{VARIABLE cbm_rescued no}\n'
    if goal in ('escort', 'rescue', 'escape'):
        pre += tag('item', {'x': destination[0], 'y': destination[1], 'image': 'items/gohere.png'})
        pre += tag('label', {'x': destination[0], 'y': destination[1], 'text': 'Destino'})
    if goal == 'beacons':
        for n, (x, y) in enumerate(points, 1):
            pre += tag('item', {'x': x, 'y': y, 'image': 'items/brazier.png'})
            pre += tag('label', {'x': x, 'y': y, 'text': f'Punto {n}'})
    if goal == 'rescue':
        pre += tag('item', {'x': prison[0], 'y': prison[1], 'image': 'items/cage.png'})
        pre += tag('label', {'x': prison[0], 'y': prison[1], 'text': 'Prisión'})
    body += event('prestart', pre)
    companion_id = cid + '_companion'
    companion = tag('unit', {'type': c['companion_type'], 'id': companion_id,
                            'name': c['companion'], 'side': 1, 'x': start[0], 'y': start[1]+1,
                            'unrenamable': 'yes'}, '{IS_LOYAL}\n')
    startbody = companion if index == 1 else tag('recall', {'id': companion_id, 'x': start[0], 'y': start[1]+1})
    # Companions are essential characters and persist on the recall list.
    # A debug jump into a later chapter supplies the missing companion too.
    if index > 1:
        startbody += tag('if', body=tag('have_unit', {'id': companion_id}) + tag('else', body=companion))
    startbody += message(companion_id, ally)
    startbody += message(cid + '_hero', hero_line)
    if index == 1:
        startbody += message('narrator', 'Crónicas de la Brasa y la Marea. Historia original en español. Las decisiones tácticas, las bajas y la experiencia se conservan entre escenarios. Puedes guardar la partida en cualquier turno.')
    escortid = sid + '_protected'
    protected_name, protected_type = PROTECTED.get((key,index), ('Viajero', 'Peasant'))
    def protected(x, y):
        return tag('unit', {'type': protected_type, 'id': escortid, 'name': protected_name,
                           'side': 1, 'x': x, 'y': y, 'random_traits': 'no',
                           'max_hitpoints': 36, 'hitpoints': 36, 'max_moves': 5, 'moves': 5}, '{IS_LOYAL}\n')
    if goal == 'escort':
        startbody += protected(start[0]+1, start[1])
    body += event('start', startbody)
    if goal == 'rescue':
        body += event('moveto', tag('filter', {'side': 1, 'x': prison[0], 'y': prison[1]}) +
                      tag('remove_item', {'x': prison[0], 'y': prison[1]}) + protected(prison[0], prison[1]+1) +
                      '{VARIABLE cbm_rescued yes}\n' + message(escortid, 'La puerta está abierta. Acompañadme hasta la bandera; no podré llegar sin ayuda.'))
    if goal in ('escape', 'escort', 'rescue'):
        body += event('moveto', tag('filter', {'id': cid + '_hero' if goal == 'escape' else escortid,
                                              'x': destination[0], 'y': destination[1]}) + endlevel('victory'))
    elif goal == 'beacons':
        for x, y in points:
            body += event('moveto', tag('filter', {'side': 1, 'x': x, 'y': y}) +
                          tag('remove_item', {'x': x, 'y': y}) +
                          tag('item', {'x': x, 'y': y, 'image': 'items/brazier-lit1.png'}) +
                          '{VARIABLE_OP cbm_points add 1}\n' +
                          message('narrator', 'Punto activado. Progreso: $cbm_points|/3.') +
                          tag('if', body=tag('variable', {'name': 'cbm_points', 'equals': 3}) +
                              tag('then', body=endlevel('victory'))))
    elif goal == 'survive':
        body += event('turn 12', message(cid + '_hero', '¡Se ha cumplido el plazo! Podemos completar la retirada.') + endlevel('victory'))
    else:
        body += event('enemies defeated', endlevel('victory'))
    # Limited reinforcements sustain pressure without infinite spawning or
    # blocking a victory after the enemy leader has been defeated.
    for turn in (4, 8):
        reinforcement = tag('unit', {'type': recruits.split(',')[turn % len(recruits.split(','))],
                                    'side': 2, 'x': enemy[0]-1, 'y': enemy[1]-2})
        body += event(f'turn {turn}', tag('if', body=tag('have_unit', {'id': sid + '_enemy'}) +
                                       tag('then', body=reinforcement)))
    body += event('last breath', tag('filter', {'id': cid + '_hero'}) +
                  message('unit', 'No podré terminar este camino…') + endlevel('defeat'))
    body += event('last breath', tag('filter', {'id': companion_id}) +
                  message('unit', 'Hasta aquí puedo acompañarte…') + endlevel('defeat'))
    if goal in ('escort', 'rescue'):
        body += event('die', tag('filter', {'id': escortid}) +
                      message('narrator', 'La persona que debías proteger ha muerto. La misión ha fracasado.') + endlevel('defeat'))
    body += event('time over', message('narrator', 'El plazo se ha agotado antes de completar la misión.') + endlevel('defeat'))
    victory = message('narrator', resolution)
    if index == len(c['chapters']):
        victory += message('narrator', c['ending'])
    if goal in ('escort', 'rescue'):
        victory += tag('kill', {'id': escortid, 'animate': 'no', 'fire_event': 'no'})
    victory += '{CLEAR_VARIABLE cbm_points,cbm_rescued}\n'
    body += event('victory', victory)
    text = tag('scenario', {'id': sid, 'name': title, 'next_scenario': following,
                           'map_file': f'{key}_{index:02d}.map', 'turns': 12 if goal == 'survive' else 32,
                           'victory_when_enemies_defeated': 'no', 'experience_modifier': 85}, body)
    write(f'scenarios/{key}/{index:02d}.cfg', text)
    manifest.append({'id': sid, 'campaign': cid, 'title': title, 'goal': goal,
                     'next': following, 'map': f'{key}_{index:02d}.map', 'biome': biome,
                     'start': start, 'enemy': enemy, 'destination': destination,
                     'prison': prison, 'points': points,
                     'file': f'scenarios/{key}/{index:02d}.cfg'})


def main():
    main_cfg = '# Original Spanish campaigns; names are unrelated to real-world Spain.\n'
    manifest = {'campaigns': [], 'scenarios': [], 'units': unit_types()}
    for rank, c in enumerate(CAMPAIGNS, 1):
        key = c['key']
        cid, define = 'CBM_' + key, 'CAMPAIGN_CBM_' + key.upper()
        main_cfg += tag('campaign', {'id': cid, 'rank': rank, 'name': c['title'], 'abbrev': 'CBM',
            'define': define, 'first_scenario': cid + '_01',
            'icon': f'data/{REL}/images/cbm/units/hero-{key}.png~SCALE(72,72)',
            'description': c['premise'] + '\n\n' + c['length'] + '\nDuración orientativa. Textos originales en español.',
            'end_text': 'Fin de «' + c['title'] + '»'},
            tag('difficulty', {'define': 'CBM_NORMAL', 'label': 'Viaje', 'description': 'Dificultad estándar',
                               'default': 'yes', 'image': f'data/{REL}/images/cbm/units/hero-{key}.png~SCALE(72,72)'}) +
            tag('about', {'title': 'Historia, diseño y recursos originales'}, tag('entry', {'name': 'Crónicas de la Brasa y la Marea · Wesnoth Phone'})))
        main_cfg += f'\n#ifdef {define}\n#define CBM_ACTIVE\n#enddef\n'
        main_cfg += f'{{{REL}/scenarios/{key}}}\n#endif\n'
        for index, row in enumerate(c['chapters'], 1):
            scenario(c, index, row, manifest['scenarios'])
        manifest['campaigns'].append({'id': cid, 'key': key, 'title': c['title'],
                                      'scenarios': len(c['chapters']), 'first': cid + '_01', 'define': define})
    main_cfg += f'\n#ifdef CBM_ACTIVE\n[binary_path]\n    path=data/{REL}\n[/binary_path]\n[units]\n{{{REL}/units}}\n[/units]\n#undef CBM_ACTIVE\n#endif\n'
    write('_main.cfg', main_cfg)
    write('manifest.json', json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    write('COPYING.txt', 'Campaign code, stories, procedural compositions and generated artwork: GPL-2.0-or-later.\n'
          'See the root COPYING file. Existing Wesnoth terrain, item art, core units and sound effects retain their original licenses and credits.\n'
          'Original raster portraits and unit illustrations were generated with the built-in image generation tool; prompts are in ART_PROMPTS.json.\n'
          'Music is an original procedural composition; source is packaging/android/campaigns/compose_music.py.\n')
    print(f'Generated {len(CAMPAIGNS)} campaigns, {len(manifest["scenarios"])} scenarios, {len(manifest["units"])} unit types in {PACK}')


if __name__ == '__main__':
    main()
