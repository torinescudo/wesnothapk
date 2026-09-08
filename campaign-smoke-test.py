#!/usr/bin/env python3
"""Test the real bundled campaigns on an Android emulator.

First checks all six unmodified openings, then injects an event-only harness
into the emulator's extracted data (never the APK) to exercise all 52 victory
conditions and campaign transitions. This is integration testing, not a claim
that tactical balance or every possible player strategy has been playtested.
"""
from pathlib import Path
import json
import re
import subprocess
import sys
import time
import xml.etree.ElementTree as ET

PACKAGE = 'org.wesnoth.phone'
ACTIVITY = PACKAGE + '/org.wesnoth.Wesnoth.WesnothActivity'
PACK = Path('overlay/data/campaigns/Brasa_y_Marea')
OUT = Path('campaign-results')
OUT.mkdir(exist_ok=True)
DEVICE_PACK = '/sdcard/Android/data/' + PACKAGE + '/files/gamedata/data/campaigns/Brasa_y_Marea'


def adb(*args, binary=False, check=True):
    r = subprocess.run(['adb',*args],capture_output=True,check=check,timeout=120)
    return r.stdout if binary else r.stdout.decode(errors='replace')


def screen(name):
    (OUT/(name+'.png')).write_bytes(adb('exec-out','screencap','-p',binary=True))


def ui():
    adb('shell','uiautomator','dump','/sdcard/campaign-ui.xml',check=False)
    text = adb('shell','cat','/sdcard/campaign-ui.xml',check=False)
    (OUT/'last-ui.xml').write_text(text)
    try:
        nodes = list(ET.fromstring(text).iter('node'))
        for n in nodes:
            if n.get('resource-id') == 'android:id/ok':
                if any(x.get('resource-id') == 'android:id/immersive_cling_title' for x in nodes):
                    tap(n)
        return nodes
    except ET.ParseError:
        return []


def tap(node):
    x1,y1,x2,y2 = map(int,re.findall(r'\d+',node.get('bounds')))
    adb('shell','input','tap',str((x1+x2)//2),str((y1+y2)//2))


def launch(campaign, skip_story=False):
    adb('shell','am','force-stop',PACKAGE)
    args = ['shell','am','start','-n',ACTIVITY,'--es','phone_campaign',campaign]
    if skip_story:
        args += ['--es','phone_scenario',campaign+'_01']
    adb(*args)


def logs():
    return adb('logcat','-d','-v','brief')


def finish_scenario():
    # Wesnoth leaves a victorious map open for inspection. Enter only dismisses
    # dialogs; use the actual phone end-turn action to leave this linger phase.
    deadline = time.monotonic()+30
    while time.monotonic() < deadline:
        nodes = ui()
        end = next((n for n in nodes if n.get('text') in ('End turn','Terminar turno')
                    and n.get('enabled') == 'true'), None)
        if end is not None:
            tap(end)
            confirmation = next((n for n in ui() if n.get('resource-id') == 'android:id/button1'), None)
            if confirmation is not None:
                tap(confirmation)
                time.sleep(2)
                return
        adb('shell','input','keyevent','KEYCODE_ENTER')
        time.sleep(1)
    raise AssertionError('Could not leave victorious map using the phone controls')


def lua_hook(chapter):
    campaign, sid, goal = chapter['campaign'],chapter['id'],chapter['goal']
    x,y = chapter['destination']
    px,py = chapter['prison']
    points = '{' + ','.join('{'+f'{a},{b}'+'}' for a,b in chapter['points']) + '}'
    code = f'''
local sid = "{sid}"
local goal = "{goal}"
local hero_id = "{campaign}_hero"
local companion_id = "{campaign}_companion"
local protected_id = sid .. "_protected"
local function mark(text)
    wesnoth.log("warning", text)
end
local ok, failure = pcall(function()
    assert(wesnoth.units.get(hero_id), "missing protagonist")
    assert(wesnoth.units.get(companion_id), "missing companion")
    for _, type_id in ipairs(wesnoth.sides[1].recruit) do
        local recruit = wesnoth.units.create {{ type=type_id, side=1 }}
        assert(recruit.hitpoints > 0 and recruit.max_moves > 0, "invalid recruit " .. type_id)
        if type_id:sub(1,4) == "CBM " then
            local width, height = filesystem.image_size(wesnoth.unit_types[type_id].image)
            assert(width and height and width > 0 and height > 0, "undecodable unit art " .. type_id)
        end
    end
    wesnoth.wml_actions.message = function() end
    wesnoth.wml_actions.move_unit_fake = function() end
    local ready = false
    wesnoth.game_events.add {{ name="victory", action=function()
        assert(ready, "victory fired before the objective was completed")
        mark("CBM_PASS:" .. sid)
    end }}
    wesnoth.game_events.add {{ name="defeat", action=function()
        mark("CBM_FAIL:" .. sid .. ":unexpected defeat")
    end }}
    local function move(id,x,y)
        wesnoth.wml_actions.move_unit {{ id=id, to_x=x, to_y=y, fire_event=true }}
    end
    if goal == "beacons" then
        local points = {points}
        move(hero_id,points[1][1],points[1][2])
        assert(wml.variables.cbm_points == 1, "first point not counted")
        move(hero_id,points[1][1],points[1][2])
        assert(wml.variables.cbm_points == 1, "same point counted twice")
        move(hero_id,points[2][1],points[2][2])
        assert(wml.variables.cbm_points == 2, "second point not counted")
        ready = true
        move(hero_id,points[3][1],points[3][2])
    elseif goal == "rescue" or goal == "escort" or goal == "escape" then
        local companion = wesnoth.units.get(companion_id)
        local old_x, old_y = companion.x, companion.y
        move(companion_id,{x},{y})
        move(companion_id,old_x,old_y)
        if goal == "rescue" then
            assert(not wesnoth.units.get(protected_id), "captive escaped before rescue")
            move(hero_id,{px},{py})
            assert(wesnoth.units.get(protected_id), "rescue did not create protected unit")
        end
        ready = true
        move(goal == "escape" and hero_id or protected_id,{x},{y})
    elseif goal == "survive" then
        wesnoth.game_events.fire("turn 11")
        ready = true
        wesnoth.game_events.fire("turn 12")
    else
        ready = true
        wesnoth.wml_actions.kill {{ side=2, fire_event=true, animate=false }}
    end
end)
if not ok then mark("CBM_FAIL:" .. sid .. ":" .. tostring(failure)) end
'''
    return '\n[event]\nname="side 1 turn 1"\n[lua]\ncode=<<\n' + code + '\n>>\n[/lua]\n[/event]\n'


def check_logs(text):
    failures = re.findall(r'CBM_FAIL:[^\r\n]+',text)
    if failures:
        raise AssertionError('\n'.join(failures))
    if 'FATAL EXCEPTION' in text or 'Fatal signal 11' in text:
        raise AssertionError('Android/native crash; see logcat')


try:
    manifest = json.loads((PACK/'manifest.json').read_text())
    # smoke-test.py has already installed and initialized this exact APK.
    adb('shell','svc','wifi','disable')
    adb('shell','svc','data','disable')
    adb('logcat','-c')
    adb('shell','am','force-stop',PACKAGE)
    adb('shell','cmd','locale','set-app-locales',PACKAGE,'--user','current','--locales','es-ES')
    adb('shell','am','start','-n',PACKAGE+'/org.wesnoth.Wesnoth.InitActivity')
    time.sleep(3)
    campaign_button = next(n for n in ui() if n.get('resource-id') == PACKAGE+':id/phone_campaigns')
    tap(campaign_button)
    nodes = ui()
    titles = [n.get('text','') for n in nodes]
    screen('spanish-campaign-selector')
    for _ in range(3):
        if all(any(c['title'] in text for text in titles) for c in manifest['campaigns']):
            break
        listing = next(n for n in nodes if n.get('class') == 'android.widget.ListView')
        x1,y1,x2,y2 = map(int,re.findall(r'\d+',listing.get('bounds')))
        adb('shell','input','swipe',str((x1+x2)//2),str(y2-20),str((x1+x2)//2),str(y1+20),'450')
        nodes = ui()
        titles.extend(n.get('text','') for n in nodes)
    assert all(any(c['title'] in text for text in titles) for c in manifest['campaigns'])
    screen('spanish-campaign-selector-scrolled')
    for campaign in manifest['campaigns']:
        print('Opening', campaign['id'], flush=True)
        launch(campaign['id'])
        deadline = time.monotonic()+140
        while time.monotonic() < deadline:
            nodes = ui()
            active = any(n.get('text') in ('Next unit','Otra unidad') and n.get('enabled') == 'true' for n in nodes)
            if active:
                break
            adb('shell','input','keyevent','KEYCODE_ENTER')
            time.sleep(1)
        else:
            raise AssertionError('Campaign did not become playable: '+campaign['id'])
        screen('opening-'+campaign['key'])
        check_logs(logs())
        print('PASS opening', campaign['id'], flush=True)
    # Add automation only to the emulator's expanded campaign files.
    adb('shell','am','force-stop',PACKAGE)
    for chapter in manifest['scenarios']:
        original = (PACK/chapter['file']).read_text()
        prefix, suffix = original.rsplit('[/scenario]',1)
        target = OUT/'instrumented'/chapter['file']
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text(prefix+lua_hook(chapter)+'[/scenario]'+suffix)
        adb('push',str(target),DEVICE_PACK+'/'+chapter['file'])
    passed = set()
    for campaign in manifest['campaigns']:
        expected = {s['id'] for s in manifest['scenarios'] if s['campaign'] == campaign['id']}
        launch(campaign['id'], skip_story=True)
        deadline = time.monotonic() + 90*len(expected)
        while time.monotonic() < deadline:
            text = logs()
            check_logs(text)
            observed = set(re.findall(r'CBM_PASS:(CBM_\w+_\d{2})',text))
            new_passes = observed-passed
            passed.update(observed)
            if new_passes:
                print('PASS objectives', ', '.join(sorted(new_passes)), flush=True)
                finish_scenario()
            if expected <= passed:
                for _ in range(4):
                    adb('shell','input','keyevent','KEYCODE_ENTER')
                    time.sleep(1)
                break
            adb('shell','input','keyevent','KEYCODE_ENTER')
            time.sleep(1)
        else:
            raise AssertionError('Objectives/transitions did not finish: '+str(sorted(expected-passed)))
        screen('completed-'+campaign['key'])
        print('PASS',campaign['id'],len(expected),'objective transitions',flush=True)
    assert len(passed) == 52
    (OUT/'result.json').write_text(json.dumps({'unmodified_openings':6,'objective_transitions':sorted(passed),
        'scope':'Native Android WML objectives and transitions with injected test events; balance not measured'},indent=2))
finally:
    screen('last-screen')
    (OUT/'logcat.txt').write_text(logs())
