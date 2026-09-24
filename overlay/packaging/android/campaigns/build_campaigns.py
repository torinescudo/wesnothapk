#!/usr/bin/env python3
"""Build the six original campaigns from authored stories and deterministic maps.

No network access. Re-run after editing stories.py; hand-authored narrative stays
separate from the shared, testable objective implementations.
SPDX-License-Identifier: GPL-2.0-or-later
"""
from pathlib import Path
import json
from mapgen import generate as generate_map
from stories import CAMPAIGNS, portrait_key

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
            'level': 2, 'alignment': alignment, 'experience': 70,
            'advances_to': f'CBM Hero {key} 2',
            'cost': 40, 'usage': 'fighter', 'description': campaign['premise']}, body)
        manifest.append('CBM Hero ' + key)
        # A protagonist grows through the campaign: the same character, at the
        # height the story reaches, with the strength the later maps demand.
        veteran = '{AMLA_DEFAULT}\n' + tag('abilities', body='{ABILITY_LEADERSHIP}')
        veteran += attack('Bastón' if key in ('sira', 'maura') else 'Arma de mano', melee, md + 3, mn + 1)
        veteran += attack('Luz de la linterna' if key == 'alba' else 'Ataque a distancia', ranged, rd + 3, rn + 1, True,
                          '{WEAPON_SPECIAL_MAGICAL}' if key in ('sira', 'maura') else '')
        content += tag('unit_type', {'id': f'CBM Hero {key} 2', 'name': f"{campaign['hero']}, {HERO_TITLES[key]}",
            'race': campaign['race'],
            'image': f'cbm/units/hero-{key}.png~SCALE(72,72)', 'profile': f'cbm/portraits/{key}.png~SCALE(400,600)',
            'gender': 'male' if key == 'darian' else 'female',
            'hitpoints': (58 if key == 'sira' else 48) + 16, 'movement': 6, 'movement_type': move,
            'level': 3, 'alignment': alignment, 'experience': 150, 'advances_to': 'null',
            'cost': 60, 'usage': 'fighter', 'description': campaign['ending']}, veteran)
        manifest.append(f'CBM Hero {key} 2')
    write('units/units.cfg', content)
    return manifest


BIOME_LABEL = {'forest': 'bosque', 'coast': 'costa', 'harbor': 'puerto', 'cave': 'caverna',
               'quarry': 'cantera', 'plains': 'llanura', 'mountain': 'montaña',
               'ruins': 'ruinas', 'islands': 'archipiélago'}
from stories import world as WORLD

# Map size follows what the chapter is: a skirmish does not need a battlefield.
MAP_SIZES = {'skirmish': (32, 24), 'battle': (40, 30), 'siege': (46, 34)}
# One map per shared place: generated the first time it is needed and reused by
# every chapter that fights over it.
SHARED_MAPS = {}


def mechanics_for(chapter, index, total):
    """Match the mechanics to the strategic difficulty the chapter is meant to have.

    Early chapters are skirmishes you can read at a glance, the middle is battle
    with a real deadline, and the end of a campaign is a siege or a voyage: fog
    or shroud arrives when the player can be expected to plan around it, not
    before. A goal also leaves its mark: escaping and escorting raise the
    reading load (you are moving through unknown ground), holding ground raises
    the pressure (the deadline is the weapon).
    """
    third = max(1, total // 3)
    if index <= third:
        name = 'skirmish'
    elif chapter['goal'] in ('escape', 'escort', 'rescue'):
        name = 'voyage'
    elif chapter['goal'] in ('survive', 'beacons'):
        name = 'siege'
    elif index <= 2 * third:
        name = 'battle'
    else:
        name = 'siege'
    mechanics = dict(WORLD.MECHANICS[name])
    if chapter['goal'] == 'survive':
        mechanics['turns'] = 12
    elif chapter['goal'] == 'escape':
        mechanics['turns'] = 22
    return mechanics


# The second thing each chapter asks of the player. Winning is never only the
# headline: these are the conditions that make a map a decision and not a march.
# Each one is checked where the scenario would be won, and losing it loses.
def secondary_condition(chapter, index, turns):
    kind = ('deaths', 'villages', 'hero_health', 'deadline')[index % 4]
    if kind == 'deaths':
        limit = 3 + index % 3
        return dict(kind=kind, limit=limit,
                    description='No pierdas más de %d unidades.' % limit)
    if kind == 'villages':
        limit = 2 + index % 2
        return dict(kind=kind, limit=limit,
                    description='Conserva al menos %d aldeas.' % limit)
    if kind == 'hero_health':
        return dict(kind=kind,
                    description='Mantén a tu protagonista por encima de la mitad de vida.')
    limit = max(6, turns - 4)
    return dict(kind=kind, limit=limit,
                description='Cumple el objetivo antes del turno %d.' % limit)


def strategy_for(chapter, index, total):
    """Give the enemy a plan that fits the fight, not a fixed set of numbers.

    A siege holds and waits, a battle presses the middle, a voyage harasses the
    column and a hunt chases: the AI's aggression, caution and goals follow the
    tactical situation the chapter is built around.
    """
    third = max(1, total // 3)
    if index <= third:
        name = 'skirmish'
    elif chapter['goal'] in ('escape', 'escort', 'rescue'):
        name = 'voyage'
    elif chapter['goal'] in ('survive', 'beacons'):
        name = 'siege'
    else:
        name = 'battle'
    return {
        'skirmish': dict(aggression=0.5, caution=0.4, attack_depth=2,
                         leader_value=6, village_value=2,
                         recruitment_pattern='fighter,archer,fighter'),
        'battle':   dict(aggression=0.8, caution=0.25, attack_depth=4,
                         leader_value=6, village_value=3,
                         recruitment_pattern='fighter,archer,fighter,scout'),
        'siege':    dict(aggression=0.35, caution=0.55, attack_depth=2,
                         leader_value=9, village_value=2,
                         recruitment_pattern='fighter,fighter,archer'),
        'voyage':   dict(aggression=0.5, caution=0.6, attack_depth=2,
                         leader_value=4, village_value=4,
                         recruitment_pattern='scout,fighter,archer'),
    }[name]


HERO_TITLES = {
    'alba': 'guardiana del faro',
    'sira': 'voz de las siete vetas',
    'iria': 'cartógrafa del cielo',
    'maura': 'archivera de ceniza',
    'nerea': 'capitana del olvido',
    'darian': 'correo de las brasas',
}

GOALS = {
    'conquer': 'Derrota al líder enemigo.',
    'survive': 'Mantén con vida a tu protagonista hasta el comienzo del turno 12.',
    'escape': 'Lleva a tu protagonista al destino señalado con una bandera.',
    'escort': 'Escolta a la persona protegida hasta la bandera de salida.',
    'rescue': 'Llega con cualquier unidad a la prisión y escolta a la persona liberada hasta la bandera.',
    'beacons': 'Activa los tres puntos señalados llevando una unidad a cada uno.',
}
# Chapter scenes are named after the chapter, so the art generator and the WML
# agree on one file per scene without either hard-coding the other's list.
STORY_SCENES = 2


def scene_art(key, index, scene):
    """The chapter scene if the art exists, otherwise the portrait that does.

    Generated art arrives in a separate pass (see ART_PROMPTS.json and
    artgen.py); until then a chapter still runs with the art it has, instead of
    pointing the engine at a file nobody has drawn.
    """
    for suffix in ('.jpg', '.png'):
        if (PACK / ('images/cbm/story/%s_%02d_%d%s' % (key, index, scene, suffix))).is_file():
            return 'cbm/story/%s_%02d_%d%s' % (key, index, scene, suffix)
    return 'cbm/portraits/%s.png~SCALE(1024,512)' % key


def portrait_ref(speaker):
    name = '%s.png' % portrait_key(speaker)
    path = PACK / 'images/cbm/portraits' / name
    return 'cbm/portraits/%s' % name if path.is_file() else None


def objective_line(chapter, turns):
    return 'Objetivo: ' + GOALS[chapter['goal']] + ' Turnos disponibles: %d.' % turns


def situation_line(chapter):
    return 'Terreno de %s. Al frente: %s.' % (BIOME_LABEL[chapter['biome']], chapter['antagonist'])


def dialogue(beats, ids, chapter):
    """One [message] per authored beat, with a portrait for named side characters."""
    out = ''
    for speaker, line in beats:
        attrs = {'message': line}
        if speaker == 'narrator':
            attrs['speaker'] = 'narrator'
        elif speaker in ('hero', 'companion', 'antagonist'):
            attrs['speaker'] = ids[speaker]
        elif speaker == 'protected':
            if not chapter['protected']:
                raise AssertionError('%s speaks as protected without one' % chapter['title'])
            attrs['speaker'] = ids['protected']
        else:
            attrs['speaker'] = 'narrator'
            attrs['caption'] = speaker
            portrait = portrait_ref(speaker)
            if portrait:
                attrs['image'] = portrait
        out += tag('message', attrs)
    return out


def triggered_event(trigger, beats, ids, chapter, turns, extra=''):
    """Map an authored trigger onto the engine event that fires it."""
    body = dialogue(beats, ids, chapter) + extra
    if trigger == 'time limit':
        return tag('event', {'name': 'turn %d' % max(1, turns - 2)}, body)
    if trigger == 'enemy leader defeated':
        return tag('event', {'name': 'die'},
                   tag('filter', {'side': 2, 'canrecruit': 'yes'}) + body)
    if trigger == 'village captured':
        return tag('event', {'name': 'capture'}, tag('filter', {'side': 1}) + body)
    if trigger == 'half strength':
        # The protected character matters most, but a chapter may wound the hero instead.
        who = ids['protected'] if chapter['protected'] else ids['hero']
        # The unit filter has no hitpoints key: a formula is how the engine reads it.
        return tag('event', {'name': 'attack end'},
                   tag('filter', {'id': who, 'formula': 'hitpoints * 2 < max_hitpoints'}) + body)
    if trigger.startswith('beacon lit '):
        return ''  # emitted next to the objective handler that counts the points
    return tag('event', {'name': trigger}, body)


def scenario(c, index, chapter, manifest):
    title = chapter['title']
    key, cid = c['key'], 'CBM_' + c['key']
    sid = '%s_%02d' % (cid, index)
    following = '%s_%02d' % (cid, index + 1) if index < len(c['chapters']) else 'null'
    turns = 12 if chapter['goal'] == 'survive' else 32
    mechanics = mechanics_for(chapter, index, len(c['chapters']))
    turns = mechanics['turns']
    secondary = secondary_condition(chapter, index, turns)
    strategy = strategy_for(chapter, index, len(c['chapters']))
    # A place two campaigns fight over is one place: the same map, two years,
    # two armies and two objectives on it.
    place = WORLD.SHARED.get((key, index))
    map_name = ('shared_%s.map' % place) if place else ('%s_%02d.map' % (key, index))
    if map_name in SHARED_MAPS:
        layout = SHARED_MAPS[map_name]
    else:
        layout = generate_map(key, index, chapter['biome'], chapter['goal'], size=mechanics['size'])
        SHARED_MAPS[map_name] = layout
        # A Wesnoth map is a rectangle: the generator can leave the last rows
        # short, so finish them with the terrain they end on.
        columns = max(len(r.split(',')) for r in layout['rows'])
        rows = []
        for row in layout['rows']:
            codes = [c for c in row.split(',') if c]
            fill = codes[-1] if codes else 'Gg'
            codes += [fill] * (columns - len(codes))
            rows.append(','.join(codes))
        write('maps/%s' % map_name, rows)
    start, enemy = layout['start'], layout['enemy']
    destination, prison, points = layout['destination'], layout['prison'], layout['points']

    escort_id = sid + '_protected'
    ids = {'hero': cid + '_hero', 'companion': cid + '_companion',
           'antagonist': sid + '_enemy', 'protected': escort_id}

    faction = c['enemy']
    if key == 'sira' and index == 3:
        faction = 'litarios'
    leader, recruits = FACTIONS[faction]
    if index > len(c['chapters']) // 2:
        recruits += ',' + VETERANS[faction]
    if key == 'darian' and index == 15:
        leader = 'CBM Hero maura'
    recruit = c['recruit'].replace('Scout', 'Elvish Scout')
    if key == 'darian' and index >= 4:
        recruit += ',CBM Litario Guardian,CBM Litario Tejedor'
    if key == 'darian' and index >= 6:
        recruit += ',CBM Velario Lancero,CBM Velario Cantor'

    # --- scenario header, music and story screens ---
    body = '{DEFAULT_SCHEDULE}\n'
    body += tag('music', {'name': 'cbm/%s-journey.ogg' % key, 'ms_after': 2000})
    body += tag('music', {'name': 'cbm/%s-battle.ogg' % key, 'append': 'yes', 'ms_after': 2000})
    hero_portrait = 'cbm/portraits/%s.png~SCALE(540,810)' % key
    body += tag('story', body=tag('part', {'story': chapter['opening'],
                                           'background': hero_portrait, 'scale_background': 'no'}))
    body += tag('story', body=tag('part', {'story': situation_line(chapter),
                                           'background': scene_art(key, index, 1),
                                           'scale_background': 'no'}))
    body += tag('story', body=tag('part', {'story': objective_line(chapter, turns),
                                           'background': scene_art(key, index, 2),
                                           'scale_background': 'no'}))

    # --- sides ---
    player = {'side': 1, 'controller': 'human', 'team_name': 'pacto', 'user_team_name': c['hero'],
              'id': ids['hero'], 'name': c['hero'], 'type': 'CBM Hero ' + key,
              'canrecruit': 'yes', 'unrenamable': 'yes', 'recruit': recruit,
              'gold': 150 + min(index * 8, 100), 'income': 3,
              'village_gold': 2,
              'fog': 'yes' if mechanics['fog'] else 'no',
              'shroud': 'yes' if mechanics['shroud'] else 'no', 'save_id': cid + '_army'}
    body += tag('side', player)
    body += tag('side', {'side': 2, 'controller': 'ai', 'team_name': 'oposicion',
                        'user_team_name': chapter['antagonist'], 'type': leader,
                        'id': ids['antagonist'], 'name': chapter['antagonist'],
                        'canrecruit': 'yes', 'recruit': recruits,
                        'gold': 100 + index * 6, 'income': 2, 'village_gold': 2},
                tag('ai', strategy) +
                tag('goal', {'name': 'Proteger al líder', 'value': 100000},
                    tag('criteria', {'id': ids['antagonist']})) +
                tag('goal', {'name': 'Alcanzar al protagonista', 'value': 20000},
                    tag('criteria', {'id': ids['hero']})))

    # --- prestart: conditions, recruit list, markers ---
    conditions = tag('objective', {'description': GOALS[chapter['goal']], 'condition': 'win'})
    conditions += tag('objective', {'description': 'Muerte de ' + c['hero'], 'condition': 'lose'})
    conditions += tag('objective', {'description': 'Muerte de ' + c['companion'], 'condition': 'lose'})
    if chapter['goal'] in ('escort', 'rescue'):
        conditions += tag('objective', {'description': 'Muerte de la persona protegida',
                                        'condition': 'lose'})
    if chapter['goal'] != 'survive':
        conditions += tag('objective', {'description': 'Se agotan los turnos', 'condition': 'lose'})
    conditions += tag('gold_carryover', {'bonus': 'yes', 'carryover_percentage': 40})
    conditions += tag('note', {'description': secondary['description']})
    conditions += tag('note', {'description': 'Toca una casilla para preparar el movimiento y '
                                              'pulsa Mover/atacar. Puedes revisar estos objetivos '
                                              'desde Más.'})
    pre = tag('objectives', {'side': 1}, conditions)
    pre += tag('allow_recruit', {'side': 1, 'type': recruit})
    pre += '{VARIABLE cbm_points 0}\n{VARIABLE cbm_rescued no}\n{VARIABLE cbm_losses 0}\n'
    if chapter['goal'] in ('escort', 'rescue', 'escape'):
        pre += tag('item', {'x': destination[0], 'y': destination[1], 'image': 'items/gohere.png'})
        pre += tag('label', {'x': destination[0], 'y': destination[1], 'text': 'Destino'})
    for number, point in enumerate(points, 1):
        pre += tag('item', {'x': point[0], 'y': point[1], 'image': 'items/brazier.png'})
        pre += tag('label', {'x': point[0], 'y': point[1], 'text': 'Punto %d' % number})
    if chapter['goal'] == 'rescue':
        pre += tag('item', {'x': prison[0], 'y': prison[1], 'image': 'items/cage.png'})
        pre += tag('label', {'x': prison[0], 'y': prison[1], 'text': 'Prisión'})
    body += event('prestart', pre)
    if secondary['kind'] == 'deaths':
        # A nested [event] would swallow its siblings in the WML tree: this
        # counter belongs at the top level like every other handler.
        body += event('die', tag('filter', {'side': 1}) + '{VARIABLE_OP cbm_losses add 1}\n')

    # --- start: companions, the protected character, and the opening dialogue ---
    companion = tag('unit', {'type': c['companion_type'], 'id': ids['companion'],
                            'name': c['companion'], 'side': 1, 'x': start[0], 'y': start[1] + 1,
                            'unrenamable': 'yes'}, '{IS_LOYAL}\n')
    startbody = companion if index == 1 else tag('recall', {'id': ids['companion'],
                                                           'x': start[0], 'y': start[1] + 1})
    if index > 1:
        startbody += tag('if', body=tag('have_unit', {'id': ids['companion']}) +
                         tag('else', body=companion))
    protected_name, protected_type = chapter['protected'] or ('Viajero', 'Peasant')
    if chapter['goal'] == 'escort':
        startbody += tag('unit', {'type': protected_type, 'id': escort_id, 'name': protected_name,
                                 'side': 1, 'x': start[0] + 1, 'y': start[1],
                                 'random_traits': 'no', 'max_hitpoints': 36, 'hitpoints': 36,
                                 'max_moves': 5, 'moves': 5}, '{IS_LOYAL}\n')
    startbody += tag('scroll_to', {'x': start[0], 'y': start[1]})
    startbody += dialogue(chapter['intro'], ids, chapter)
    body += event('start', startbody)

    # --- authored mid-scenario beats ---
    beacon_beats = {}
    for trigger, beats in chapter['events']:
        if trigger.startswith('beacon lit '):
            beacon_beats[int(trigger.rsplit(' ', 1)[1])] = beats
            continue
        body += triggered_event(trigger, beats, ids, chapter, turns)

    # --- objective handlers ---
    def victory_gate():
        """Winning takes the headline and the second condition: losing either loses."""
        check = secondary['kind']
        if check == 'deaths':
            fail = tag('variable', {'name': 'cbm_losses', 'numerical_greater_than': secondary['limit']})
        elif check == 'villages':
            fail = (tag('store_locations', {'terrain': '*^V*', 'owner': 1, 'variable': 'cbm_villages'},
                        body='') +
                    tag('variable', {'name': 'cbm_villages.length',
                                     'numerical_less_than': secondary['limit']}))
        elif check == 'hero_health':
            fail = tag('have_unit', {'id': ids['hero'], 'formula': 'hitpoints * 2 < max_hitpoints'})
        else:
            fail = tag('variable', {'name': 'turn_number',
                                    'numerical_greater_than': secondary['limit']})
        return tag('if', body=fail + tag('then', body=dialogue(
            [('narrator', secondary['description'] + ' La condición se ha incumplido.')], ids, chapter)
            + endlevel('defeat')) + tag('else', body=endlevel('victory')))

    def protected_unit(x, y):
        return tag('unit', {'type': protected_type, 'id': escort_id, 'name': protected_name,
                           'side': 1, 'x': x, 'y': y, 'random_traits': 'no',
                           'max_hitpoints': 36, 'hitpoints': 36, 'max_moves': 5, 'moves': 5},
                   '{IS_LOYAL}\n')

    if chapter['goal'] == 'rescue':
        body += event('moveto', tag('filter', {'side': 1, 'x': prison[0], 'y': prison[1]}) +
                      tag('remove_item', {'x': prison[0], 'y': prison[1]}) +
                      protected_unit(prison[0], prison[1] + 1) +
                      '{VARIABLE cbm_rescued yes}\n' +
                      tag('sound', {'name': 'rumble.ogg'}) +
                      dialogue([('protected', 'La puerta está abierta. Acompañadme hasta la '
                                             'bandera; no podré llegar sin ayuda.')], ids, chapter))
    if chapter['goal'] in ('escape', 'escort', 'rescue'):
        who = ids['hero'] if chapter['goal'] == 'escape' else escort_id
        body += event('moveto', tag('filter', {'id': who, 'x': destination[0],
                                              'y': destination[1]}) +
                      tag('sound', {'name': 'gold.ogg'}) + victory_gate())
    elif chapter['goal'] == 'beacons':
        for number, (px, py) in enumerate(points, 1):
            handler = tag('remove_item', {'x': px, 'y': py})
            handler += tag('item', {'x': px, 'y': py, 'image': 'items/brazier-lit%d.png' % min(number, 2)})
            handler += '{VARIABLE_OP cbm_points add 1}\n'
            handler += tag('scroll_to', {'x': px, 'y': py})
            handler += tag('sound', {'name': 'fire.wav'})
            handler += dialogue(beacon_beats.get(number, []), ids, chapter)
            handler += tag('objectives', {'side': 1},
                           tag('objective', {'description': GOALS[chapter['goal']], 'condition': 'win'}) +
                           tag('note', {'description': 'Puntos activados: $cbm_points|/3.'}))
            if number == len(points):
                handler += tag('if', body=tag('variable', {'name': 'cbm_points',
                                                           'numerical_equals': len(points)}) +
                               tag('then', body=victory_gate()))
            body += event('moveto', tag('filter', {'side': 1, 'x': px, 'y': py}) + handler)
    elif chapter['goal'] == 'survive':
        body += event('turn %d' % turns,
                      dialogue([('hero', 'Se ha cumplido el plazo. Podemos completar la retirada.')],
                               ids, chapter) + victory_gate())
    else:
        body += event('enemies defeated', dialogue([('narrator', 'La oposición se ha roto.')],
                                                  ids, chapter) + victory_gate())

    # --- pressure: two bounded reinforcements and an escalation, never infinite ---
    for turn in (4, 8):
        reinforcement = tag('unit', {'type': recruits.split(',')[turn % len(recruits.split(','))],
                                    'side': 2, 'x': enemy[0] - 1, 'y': enemy[1] - 2})
        body += event('turn %d' % turn,
                      tag('if', body=tag('have_unit', {'id': ids['antagonist']}) +
                          tag('then', body=reinforcement)))
    body += event('turn %d' % max(2, turns // 2),
                  tag('modify_side', {'side': 2, 'income': 4},
                      tag('ai', {'aggression': .8, 'caution': .15})))

    # --- defeat and victory ---
    body += event('last breath', tag('filter', {'id': ids['hero']}) +
                  dialogue([('hero', 'No podré terminar este camino…')], ids, chapter) +
                  endlevel('defeat'))
    body += event('last breath', tag('filter', {'id': ids['companion']}) +
                  dialogue([('companion', 'Hasta aquí puedo acompañarte…')], ids, chapter) +
                  endlevel('defeat'))
    if chapter['goal'] in ('escort', 'rescue'):
        body += event('die', tag('filter', {'id': escort_id}) +
                      dialogue([('narrator', 'La persona que debías proteger ha muerto. La misión '
                                             'ha fracasado.')], ids, chapter) + endlevel('defeat'))
    body += event('time over', dialogue([('narrator', 'El plazo se ha agotado antes de completar '
                                                    'la misión.')], ids, chapter) + endlevel('defeat'))
    victory = dialogue(chapter['victory'], ids, chapter)
    victory += dialogue([('narrator', chapter['resolution'])], ids, chapter)
    if index == len(c['chapters']):
        victory += dialogue([('narrator', c['ending'])], ids, chapter)
    if chapter['goal'] in ('escort', 'rescue'):
        victory += tag('kill', {'id': escort_id, 'animate': 'no', 'fire_event': 'no'})
    victory += '{CLEAR_VARIABLE cbm_points,cbm_rescued}\n'
    body += event('victory', victory)

    text = tag('scenario', {'id': sid, 'name': title, 'next_scenario': following,
                           'map_file': '%s_%02d.map' % (key, index), 'turns': turns,
                           'victory_when_enemies_defeated': 'no', 'experience_modifier': 85}, body)
    write('scenarios/%s/%02d.cfg' % (key, index), text)
    manifest.append({'id': sid, 'campaign': cid, 'title': title, 'goal': chapter['goal'],
                     'next': following, 'map': map_name,
                     'biome': chapter['biome'], 'size': mechanics['size'],
                     'turns': turns, 'fog': mechanics['fog'], 'shroud': mechanics['shroud'],
                     'shared': place,
                     'start': start, 'enemy': enemy,
                     'destination': destination, 'prison': prison, 'points': points,
                     'villages': layout['villages'], 'terrain': layout['stats'],
                     'file': 'scenarios/%s/%02d.cfg' % (key, index)})


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
