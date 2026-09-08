#!/usr/bin/env python3
"""Original score for Brasa y Marea. No samples or borrowed melodies.

Deterministic additive instruments, authored modal themes, harmonic movements,
countermelodies and stereo early reflections. Requires numpy and soundfile.
SPDX-License-Identifier: GPL-2.0-or-later
"""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / '.phone-tools/python'))
import numpy as np
import soundfile as sf

RATE = 32000
OUT = ROOT / 'data/campaigns/Brasa_y_Marea/music/cbm'
# Degree melodies, including deliberate rests (-1), each eight beats long.
THEMES = {
 'alba': dict(root=62, scale=[0,2,3,5,7,9,10], bpm=84, meter=4,
              motif=[0,2,4,3,2,-1,1,0], chords=[0,5,3,4,0,2,5,0], voice='flute'),
 'sira': dict(root=48, scale=[0,2,3,5,7,8,10], bpm=72, meter=4,
              motif=[0,-1,4,3,0,1,2,-1], chords=[0,3,0,5,2,3,4,0], voice='bell'),
 'iria': dict(root=64, scale=[0,2,3,5,7,9,10], bpm=96, meter=3,
              motif=[4,6,5,2,3,1,0,-1], chords=[0,2,5,3,0,5,4,0], voice='pluck'),
 'maura': dict(root=50, scale=[0,1,3,5,7,8,10], bpm=76, meter=4,
              motif=[0,1,0,-1,4,3,1,0], chords=[0,1,0,5,3,1,4,0], voice='reed'),
 'nerea': dict(root=60, scale=[0,2,4,5,7,9,10], bpm=102, meter=3,
              motif=[0,2,4,5,4,2,1,4], chords=[0,3,5,4,0,2,3,0], voice='flute'),
 'darian': dict(root=62, scale=[0,2,4,5,7,9,11], bpm=88, meter=4,
              motif=[0,4,2,3,5,4,1,0], chords=[0,5,3,4,2,5,4,0], voice='reed'),
}


def pitch(theme, degree):
    octave, note = divmod(degree, 7)
    return theme['root'] + theme['scale'][note] + 12 * octave


def instrument(midi, duration, kind, phase=0):
    t = np.arange(int(duration * RATE), dtype=np.float64) / RATE
    f = 440 * 2 ** ((midi - 69) / 12)
    if kind == 'pluck':
        wave = sum(np.sin(2*np.pi*f*n*t + phase) * np.exp(-t*(1.5+n*.6)) / n**1.6 for n in range(1, 6))
        attack = .008
    elif kind == 'bell':
        wave = sum(np.sin(2*np.pi*f*r*t) * np.exp(-t*(.9+r*.32)) * a
                   for r,a in [(1,1),(2,.3),(3.01,.12),(4.15,.04)])
        attack = .012
    elif kind == 'flute':
        angle = 2*np.pi*f*t + .018*np.sin(2*np.pi*4.7*t)
        wave = np.sin(angle) + .12*np.sin(2*angle) + .025*np.sin(3*angle)
        attack = .11
    elif kind == 'reed':
        angle = 2*np.pi*f*t + .024*np.sin(2*np.pi*4.2*t)
        wave = np.sin(angle) + .23*np.sin(3*angle) + .07*np.sin(5*angle)
        attack = .16
    else:  # restrained string ensemble: detuned partials, no saw-wave buzz
        wave = sum(np.sin(2*np.pi*f*n*(1+detune)*t + phase) / n**2
                   for n in range(1, 5) for detune in (-.0018,.0018)) / 2
        attack = .3
    envelope = np.minimum(t/attack, 1) * np.minimum((duration-t)/min(.3,duration*.22),1)
    return (wave * np.maximum(envelope,0)).astype(np.float32)


def compose(key, theme, battle):
    bpm = theme['bpm'] + (16 if battle else 0)
    beat = 60 / bpm
    meter = theme['meter']
    bars = 32
    duration = bars * meter * beat + 3
    mix = np.zeros((int(duration*RATE), 2), dtype=np.float32)
    rng = np.random.default_rng(sum(map(ord,key)) + int(battle))

    def add(at, midi, length, voice, volume, pan=0):
        wave = instrument(midi, length, voice, rng.uniform(0,.03)) * volume
        start = int(at*RATE)
        size = min(len(wave), len(mix)-start)
        if size > 0:
            mix[start:start+size,0] += wave[:size] * np.sqrt((1-pan)/2)
            mix[start:start+size,1] += wave[:size] * np.sqrt((1+pan)/2)

    for bar in range(bars):
        chord = theme['chords'][(bar//2) % 8]
        section = bar // 8
        at = bar * meter * beat
        # Harmonic bed and bass use inversions to limit voice movement.
        for degree, pan in zip([chord-7, chord-5, chord-3], [-.55,0,.55]):
            add(at, pitch(theme,degree), meter*beat+.2, 'strings', .065, pan)
        add(at, pitch(theme,chord-14), meter*beat*.85, 'pluck', .2, -.15)
        for step in range(meter*2):
            degree = chord + [0,4,2,4][step%4] - 7
            add(at+step*beat/2, pitch(theme,degree), beat*.9, 'pluck', .055 if not battle else .085, .35)
        if bar >= 2:
            for step in range(meter):
                degree = theme['motif'][(bar*meter+step)%8]
                if degree < 0:
                    continue
                # B section answers a third higher; final phrase resolves home.
                if section == 2:
                    degree += 2
                if bar >= 30:
                    degree = [4,2,1,0][min(step,3)]
                add(at+step*beat, pitch(theme,degree+7), beat*.84,
                    theme['voice'], .16 if not battle else .14, -.2)
        if section in (1,3) and bar % 2 == 0:
            add(at+beat*.5, pitch(theme,chord+4), beat*(meter-1), 'flute', .06, .55)
        # Quiet hand drum in travel themes, fuller pulse for battle variants.
        for step in range(meter):
            if not battle and step not in (0, meter-1):
                continue
            t = np.arange(int(.22*RATE))/RATE
            drum = np.sin(2*np.pi*(65*t + 35*.022*(1-np.exp(-t/.022))))*np.exp(-t*23)
            noise = rng.normal(0,.035,len(t))*np.exp(-t*45)
            wave = (drum+noise)*(.105 if battle else .045)
            pos = int((at+step*beat)*RATE)
            mix[pos:pos+len(t),:] += wave[:,None]
    dry = mix.copy()
    for delay, gain in [(.071,.10),(.113,.075),(.193,.055),(.307,.035)]:
        offset = int(delay*RATE)
        mix[offset:,0] += dry[:-offset,1]*gain
        mix[offset:,1] += dry[:-offset,0]*gain
    fade = int(RATE*2)
    mix[:RATE//2] *= np.linspace(0,1,RATE//2)[:,None]
    mix[-fade:] *= np.linspace(1,0,fade)[:,None]
    peak = float(np.max(np.abs(mix)))
    mix *= .82 / max(peak,.01)
    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT / f'{key}-{"battle" if battle else "journey"}.ogg'
    # libsndfile's Windows Vorbis encoder needs bounded write blocks to avoid
    # allocating a whole track on its native stack.
    with sf.SoundFile(target, 'w', samplerate=RATE, channels=2,
                      format='OGG', subtype='VORBIS') as stream:
        for start in range(0, len(mix), 4096):
            stream.write(mix[start:start+4096])
    decoded, rate = sf.read(target)
    assert rate == RATE and np.isfinite(decoded).all()
    assert np.max(np.abs(decoded)) < .99
    rms = float(np.sqrt(np.mean(decoded**2)))
    assert rms > .035, (target, rms)
    return dict(file=target.name, seconds=round(len(decoded)/rate,2), bpm=bpm,
                peak=round(float(np.max(np.abs(decoded))),4), rms=round(rms,4))


if __name__ == '__main__':
    report = [compose(key,t,battle) for key,t in THEMES.items() for battle in (False,True)]
    (OUT/'score.json').write_text(json.dumps({'method':'Original additive synthesis; no samples',
        'themes':THEMES, 'tracks':report}, ensure_ascii=False,indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report,indent=2))
