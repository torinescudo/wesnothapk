#!/usr/bin/env python3
"""Plan the campaigns' artwork for an image generator and install what it draws.

This module never draws. It writes the prompt plan the image generator consumes
(ART_PROMPTS.json, the same file the existing portraits and sprites came from),
reports which assets are still missing, and installs finished images: cropping,
scaling, alpha and file naming are mechanical, so the pass is reproducible.

    python3 artgen.py plan             # write ART_PROMPTS.json from the stories
    python3 artgen.py status           # which assets the campaigns still need
    python3 artgen.py install <dir>    # install generated files into the pack

`install` accepts files named after a prompt key, in any common image format:
    alba.png, sarel-el-cobrador.png, alba_01_1.png, litario-guardian.png

SPDX-License-Identifier: GPL-2.0-or-later
"""
from pathlib import Path
import argparse
import json
import sys
import zlib

from PIL import Image

import stories

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PACK = ROOT / 'data/campaigns/Brasa_y_Marea'
IMAGES = PACK / 'images/cbm'
PROMPTS = PACK / 'ART_PROMPTS.json'
SCENES_PER_CHAPTER = 2


def seed_for(*parts):
    """Deterministic seed per asset: regenerating reproduces the same image."""
    return zlib.crc32('|'.join(str(p) for p in parts).encode('utf-8'))

PORTRAIT_SIZE = (512, 768)
SCENE_SIZE = (1024, 512)

# Style clauses shared by every request, worded the way the existing, proven
# entries in ART_PROMPTS.json are.
PORTRAIT_STYLE = ('Original hand-painted high-fantasy game portrait. {subject} One single character, '
                  'head to below the knees, standing calmly with empty hands relaxed at their sides: '
                  'no weapon, no prop, no staff, nothing held. Generous margin above the head so '
                  'nothing is cropped, flat simple gradient background. Clean dark contours, rich '
                  'muted natural colours, readable silhouette compatible with traditional Battle for '
                  'Wesnoth illustration. Genuinely transparent PNG background, no scenery, no text, '
                  'no border or logo.')
SCENE_STYLE = ('Original hand-painted wide illustration for a Battle for Wesnoth story screen. '
               '{subject} An empty landscape: no people, no creatures, no vehicles, no banners. '
               'No lettering of any kind. Muted natural colours, clean readable shapes, clear '
               'foreground, midground and background layers, consistent with the same campaign '
               'character art.')
SPRITE_STYLE = ('Production game asset: ONE single isolated 2D pixel-art unit sprite for a '
                'hexagonal tactical fantasy game like Battle for Wesnoth. {subject} Three-quarter '
                'overhead battlefield view facing down-right, compact heroic proportions, strong '
                'silhouette that reads at 72x72 pixels. Full figure with equipment within the '
                'central 80 percent of a square canvas. Deliberate crisp pixel clusters, detailed '
                '1990s hand-pixelled style, small palette, no smooth painted portrait. Genuine '
                'transparent alpha background. No floor, no scenery, no UI, no letters, no labels, '
                'no sprite sheet. One unit only.')

BIOME_SCENE = {
    'forest': 'A forest chapter: layered pines and broadleaf masses, a cleared road, mist between trunks.',
    'coast': 'A coastal chapter: a long shoreline, breakers, a headland, boats drawn up on the sand.',
    'harbor': 'A harbour chapter: quays, moored hulls, warehouses, gulls, a town rising behind the docks.',
    'cave': 'A cavern chapter: columns of living rock, crystal seams catching the light, a narrow gallery.',
    'quarry': 'A quarry chapter: terraced stone, cranes and sledges, rubble, half-cut blocks.',
    'plains': 'A plains chapter: open fields, hedgerows, wind over dry grass, a road running to the horizon.',
    'mountain': 'A mountain chapter: ridgelines, scree, a pass between peaks, weather coming in.',
    'ruins': 'A ruined chapter: broken walls and columns, collapsed roofs, new growth through the stone.',
    'islands': 'An island chapter: several landmasses, sandbars between them, palms and reef water.',
}

ROLE_HINT = {
    'antagonist': 'a dangerous antagonist of the story',
    'protected': 'a civilian the player has to keep alive',
    'hero': 'the protagonist of the campaign',
    'companion': 'the protagonist\u2019s closest companion',
}

# Speaker keys the generator resolves to units; named characters get their own art.
SPECIAL = set(stories.SPECIAL_SPEAKERS)


def first_line(name):
    """The line a character first says, used to describe them in their own prompt."""
    for campaign in stories.CAMPAIGNS:
        for chapter in campaign['chapters']:
            for _, speaker, line in stories.beats(chapter):
                if speaker == name:
                    return line
    return ''


def campaign_of(name):
    for campaign in stories.CAMPAIGNS:
        for chapter in campaign['chapters']:
            for _, speaker, _ in stories.beats(chapter):
                if speaker == name:
                    return campaign
    return stories.CAMPAIGNS[0]


def role_of(name):
    for campaign in stories.CAMPAIGNS:
        for chapter in campaign['chapters']:
            if chapter['antagonist'] == name:
                return 'antagonist'
            if chapter['protected'] and chapter['protected'][0] == name:
                return 'protected'
    return 'side'


def portrait_subject(name):
    campaign = campaign_of(name)
    role = role_of(name)
    said = first_line(name)
    world = campaign['premise'].split('.')[0]
    parts = ['%s, %s in the world of %s (%s).' % (name, ROLE_HINT.get(role, 'a named character'),
                                                  campaign['title'], world)]
    if said:
        parts.append('They are the kind of person who says: "%s"' % said.strip())
    if role == 'antagonist':
        parts.append('Show them as an adversary: composed, well equipped, sure of themselves.')
    elif role == 'protected':
        parts.append('Show them as a civilian: practical clothes, no armour, unarmed.')
    else:
        parts.append('Show them as a working member of their community, with the tools of their trade.')
    return ' '.join(parts)


def scene_subject(campaign, index, chapter, scene):
    shot = 'Establishing shot' if scene == 1 else 'A second angle of the same place, later in the same day'
    return ('%s for the chapter "%s" of %s. %s The scene: %s'
            % (shot, chapter['title'], campaign['title'],
               BIOME_SCENE.get(chapter['biome'], ''), chapter['opening']))


def plan():
    """Write the prompt plan: every asset the campaigns reference, and nothing else."""
    existing = {}
    if PROMPTS.is_file():
        existing = json.loads(PROMPTS.read_text(encoding='utf-8'))
    authored = existing.get('portraits', {})
    plan_data = {'mode': 'built-in image generation',
                 'note': 'Prompts for every image the campaigns reference. '
                         'portraits and unit_sprites are authored and preserved; '
                         'characters and chapter_scenes are derived from the stories '
                         'and regenerated on every run. Install with artgen.py install.',
                 'portraits': dict(authored), 'characters': {}, 'chapter_scenes': {},
                 'unit_sprites': existing.get('unit_sprites', {}),
                 'hero_sprites': existing.get('hero_sprites', {})}
    for campaign in stories.CAMPAIGNS:
        key = campaign['key']
        if key not in plan_data['portraits']:
            plan_data['characters'][key] = PORTRAIT_STYLE.format(subject=(
                '%s, the protagonist of %s. %s' % (campaign['hero'], campaign['title'],
                                                   campaign['premise'])))
        for index, chapter in enumerate(campaign['chapters'], 1):
            for scene in range(1, SCENES_PER_CHAPTER + 1):
                scene_key = '%s_%02d_%d' % (key, index, scene)
                plan_data['chapter_scenes'][scene_key] = SCENE_STYLE.format(
                    subject=scene_subject(campaign, index, chapter, scene))
    for name in stories.characters():
        key = stories.portrait_key(name)
        if key not in plan_data['portraits']:
            plan_data['characters'][key] = PORTRAIT_STYLE.format(
                subject=portrait_subject(name))
    plan_data['unit_sprites'] = existing.get('unit_sprites', {})
    PROMPTS.write_text(json.dumps(plan_data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('wrote %d portrait prompts, %d chapter scenes, %d unit sprites into %s'
          % (len(plan_data['portraits']), len(plan_data['chapter_scenes']),
             len(plan_data['unit_sprites']), PROMPTS))
    return plan_data


def required():
    """Every asset the generated campaigns reference, as (kind, key) pairs."""
    wanted = []
    for campaign in stories.CAMPAIGNS:
        key = campaign['key']
        wanted.append(('portrait', key))
        for index, _ in enumerate(campaign['chapters'], 1):
            for scene in range(1, SCENES_PER_CHAPTER + 1):
                wanted.append(('scene', '%s_%02d_%d' % (key, index, scene)))
    for name in stories.characters():
        wanted.append(('portrait', stories.portrait_key(name)))
    return wanted


def target(kind, key):
    if kind == 'portrait':
        return IMAGES / 'portraits' / ('%s.png' % key)
    # Scenes are wide backgrounds with no alpha: JPEG keeps the repository light.
    return IMAGES / 'story' / ('%s.jpg' % key)


def status():
    missing = [(kind, key) for kind, key in required() if not target(kind, key).is_file()]
    present = len(required()) - len(missing)
    print('%d of %d required images are installed' % (present, len(required())))
    for kind in ('portrait', 'scene'):
        rows = [key for k, key in missing if k == kind]
        if rows:
            print('missing %s (%d): %s' % (kind, len(rows), ', '.join(rows[:12])
                                           + (' ...' if len(rows) > 12 else '')))
    return missing


def fit(image, size):
    """Cover-crop to the target size so nothing is stretched or letterboxed."""
    source = image.convert('RGBA')
    ratio = max(size[0] / source.width, size[1] / source.height)
    scaled = source.resize((max(1, int(source.width * ratio)), max(1, int(source.height * ratio))),
                           Image.LANCZOS)
    left = (scaled.width - size[0]) // 2
    top = int((scaled.height - size[1]) * 0.35)
    return scaled.crop((left, top, left + size[0], top + size[1]))


# --- generation through the local ComfyUI server ---------------------------
CHECKPOINT = 'sd_xl_base_1.0.safetensors'
PORTRAIT_LORA = 'daggerfall-000001.safetensors'
PORTRAIT_SIZE_GEN = (832, 1216)
SCENE_SIZE_GEN = (1344, 768)
NEGATIVE = ('text, letters, signature, watermark, logo, border, frame, collage, scenery, '
            'two figures, extra limbs, extra fingers, fused fingers, deformed hands, hands holding '
            'an object, weapon, prop, staff, raised weapon, wispy hair, fuzzy edges, halo, tight '
            'crop, cropped hair, busy straps, smudged detail, blurry, lowres, people, crowd, '
            'silhouette figures, animals, creatures, vehicles, banners')


def workflow(prompt, key, size, lora, seed):
    return {
        '4': {'class_type': 'CheckpointLoaderSimple',
              'inputs': {'ckpt_name': CHECKPOINT}},
        '10': {'class_type': 'LoraLoader',
               'inputs': {'lora_name': lora, 'strength_model': 0.75, 'strength_clip': 0.75,
                          'model': ['4', 0], 'clip': ['4', 1]}},
        '5': {'class_type': 'EmptyLatentImage',
              'inputs': {'width': size[0], 'height': size[1], 'batch_size': 1}},
        '6': {'class_type': 'CLIPTextEncode', 'inputs': {'text': prompt, 'clip': ['10', 1]}},
        '7': {'class_type': 'CLIPTextEncode', 'inputs': {'text': NEGATIVE, 'clip': ['10', 1]}},
        '3': {'class_type': 'KSampler',
              'inputs': {'seed': seed, 'steps': 28, 'cfg': 6.0, 'sampler_name': 'dpmpp_2m',
                         'scheduler': 'karras', 'denoise': 1.0, 'model': ['10', 0],
                         'positive': ['6', 0], 'negative': ['7', 0], 'latent_image': ['5', 0]}},
        '8': {'class_type': 'VAEDecode', 'inputs': {'samples': ['3', 0], 'vae': ['4', 2]}},
        '9': {'class_type': 'SaveImage',
              'inputs': {'filename_prefix': 'cbm-' + key, 'images': ['8', 0]}},
    }


def cutout(path):
    """Remove the background of a portrait, the way the existing art does.

    u2net is the model already cached on this machine: rembg's current default
    would download a 1 GB model first, at dial-up speed.
    """
    from rembg import new_session, remove
    result = remove(Image.open(path).convert('RGBA'), session=new_session('u2net'))
    result.save(path, 'PNG')


def generate(server, kinds, limit, staging):
    """Draw the pending prompts through the local ComfyUI server and install them."""
    import time
    import urllib.parse
    import urllib.request
    prompts = json.loads(PROMPTS.read_text(encoding='utf-8'))
    pending = [(kind, key) for kind, key in required() if not target(kind, key).is_file()]
    if kinds != 'all':
        pending = [row for row in pending if row[0] in kinds.split(',')]
    if limit:
        pending = pending[:limit]
    staging.mkdir(parents=True, exist_ok=True)
    print('generating %d images with %s' % (len(pending), server))
    for number, (kind, key) in enumerate(pending, 1):
        section = 'chapter_scenes' if kind == 'scene' else 'portraits'
        prompt = (prompts.get(section, {}).get(key)
                  or prompts.get('characters', {}).get(key))
        if not prompt:
            print('  [%d/%d] %s: no prompt in ART_PROMPTS.json' % (number, len(pending), key))
            continue
        size = SCENE_SIZE_GEN if kind == 'scene' else PORTRAIT_SIZE_GEN
        # '@' separates the key from ComfyUI's own counter, so 'alba' can never
        # pick up the files of 'alba_01_1'.
        graph = workflow(prompt, 'cbm@%s@' % key, size, PORTRAIT_LORA, seed_for('draw', key))
        body = json.dumps({'prompt': graph, 'client_id': 'wesnoth-phone'}).encode('utf-8')
        request = urllib.request.Request(server + '/prompt', data=body,
                                         headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(request, timeout=120) as response:
            prompt_id = json.load(response)['prompt_id']
        produced = []
        deadline = time.time() + 900
        while time.time() < deadline and not produced:
            with urllib.request.urlopen(server + '/history/' + prompt_id, timeout=60) as response:
                history = json.load(response).get(prompt_id)
            if history and history.get('outputs'):
                produced = [node['images'] for node in history['outputs'].values()
                            if node.get('images')][-1]
            if not produced:
                time.sleep(2)
        if not produced:
            print('  [%d/%d] %s: no image produced' % (number, len(pending), key))
            continue
        image = produced[-1]
        query = urllib.parse.urlencode({'filename': image['filename'],
                                        'subfolder': image.get('subfolder', ''),
                                        'type': image.get('type', 'output')})
        raw = staging / ('cbm@%s@.png' % key)
        with urllib.request.urlopen(server + '/view?' + query, timeout=120) as response:
            raw.write_bytes(response.read())
        destination = target(kind, key)
        destination.parent.mkdir(parents=True, exist_ok=True)
        frame = fit(Image.open(raw), PORTRAIT_SIZE if kind == 'portrait' else SCENE_SIZE)
        if kind == 'portrait':
            frame.save(destination, 'PNG', optimize=True)
            cutout(destination)
        else:
            frame.convert('RGB').save(destination, 'JPEG', quality=90, optimize=True)
        print('  [%d/%d] %s -> %s' % (number, len(pending), key, destination.name))
    return len(pending)



def install(source_dir):
    """Install generated files by prompt key, cropping and scaling them into place."""
    installed = 0
    for kind, key in required():
        destination = target(kind, key)
        for candidate in sorted(source_dir.glob('%s.*' % key)):
            if candidate.suffix.lower() not in ('.png', '.jpg', '.jpeg', '.webp'):
                continue
            size = PORTRAIT_SIZE if kind == 'portrait' else SCENE_SIZE
            destination.parent.mkdir(parents=True, exist_ok=True)
            frame = fit(Image.open(candidate), size)
            if kind == 'portrait':
                frame.save(destination, 'PNG', optimize=True)
            else:
                frame.convert('RGB').save(destination, 'JPEG', quality=90, optimize=True)
            installed += 1
            break
    print('installed %d images into %s' % (installed, IMAGES))
    return installed


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=('plan', 'status', 'install', 'generate'))
    parser.add_argument('directory', nargs='?', type=Path)
    parser.add_argument('--server', default='http://127.0.0.1:8188')
    parser.add_argument('--kinds', default='all')
    parser.add_argument('--limit', type=int, default=0)
    parser.add_argument('--staging', type=Path,
                        default=Path.home() / 'AppData/Local/Temp/phone-ui/art-out')
    args = parser.parse_args(argv)
    if args.action == 'plan':
        plan()
    elif args.action == 'status':
        return 1 if status() else 0
    elif args.action == 'generate':
        generate(args.server, args.kinds, args.limit, args.staging)
    else:
        if not args.directory or not args.directory.is_dir():
            print('install needs a directory of generated images')
            return 2
        install(args.directory)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
