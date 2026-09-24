#!/usr/bin/env python3
"""Exercise the installed native game, retaining screenshots and logs as evidence."""
from pathlib import Path
import re
import subprocess
import sys
import time
import xml.etree.ElementTree as ET

PACKAGE = 'org.wesnoth.phone'
OUTPUT = Path('smoke-results')
OUTPUT.mkdir(exist_ok=True)


def adb(*args, binary=False, check=True):
    result = subprocess.run(['adb', *args], capture_output=True, check=check, timeout=90)
    return result.stdout if binary else result.stdout.decode(errors='replace')


def screen(name):
    (OUTPUT / (name + '.png')).write_bytes(adb('exec-out', 'screencap', '-p', binary=True))


def ui():
    adb('shell', 'uiautomator', 'dump', '/sdcard/phone-ui.xml', check=False)
    xml = adb('shell', 'cat', '/sdcard/phone-ui.xml', check=False)
    (OUTPUT / 'latest-ui.xml').write_text(xml)
    try:
        nodes = list(ET.fromstring(xml).iter('node'))
        if any(n.get('resource-id') == 'android:id/immersive_cling_title' for n in nodes):
            tap(next(n for n in nodes if n.get('resource-id') == 'android:id/ok'))
            return []
        return nodes
    except ET.ParseError:
        return []


def find(nodes, text=None, resource=None, enabled=False):
    """Controls are found by resource id: the phone UI is translated, ids are not."""
    for node in nodes:
        if text is not None and node.get('text') != text:
            continue
        if resource is not None and node.get('resource-id') != PACKAGE + ':id/' + resource:
            continue
        if enabled and node.get('enabled') != 'true':
            continue
        return node
    return None


def tap(node):
    if node is None:
        raise AssertionError('Expected control is absent')
    left, top, right, bottom = map(int, re.findall(r'\d+', node.attrib['bounds']))
    adb('shell', 'input', 'tap', str((left + right) // 2), str((top + bottom) // 2))


def wait_for(predicate, timeout, label='the native game or UI'):
    end = time.monotonic() + timeout
    while time.monotonic() < end:
        value = predicate()
        if value is not None and value is not False:
            return value
        time.sleep(2)
    raise AssertionError('Timed out waiting for %s' % label)


def annotate(error):
    """Surface the failure as a CI annotation: logs are long, the reason is short."""
    import traceback
    tail = ''
    latest = OUTPUT / 'latest-ui.xml'
    if latest.is_file():
        tail = latest.read_text(errors='replace').replace('\n', ' ')[-300:]
    detail = traceback.format_exc().replace('\n', ' | ')[:1200]
    print('::error title=smoke failure::%s :: %s' % (str(error).replace('\n', ' ')[:200], detail),
          flush=True)
    if tail:
        print('::error title=smoke UI tail::%s' % tail, flush=True)


def in_bar(resource, enabled=True):
    return lambda: find(ui(), resource=resource, enabled=enabled)


try:
    adb('install', '-r', sys.argv[1])
    # The delayed Android immersive-mode hint can consume the first tap after
    # a fresh install. It is system UI, not one of the game's controls.
    adb('shell', 'settings', 'put', 'secure', 'immersive_mode_confirmations', 'confirmed')
    adb('shell', 'svc', 'wifi', 'disable')
    adb('shell', 'svc', 'data', 'disable')
    adb('shell', 'am', 'start', '-n', PACKAGE + '/org.wesnoth.Wesnoth.InitActivity')
    wait_for(lambda: find(ui(), resource='phone_tutorial'), 40, label='the launcher screen')
    screen('01-launcher')
    # The picker has to describe every bundled story before one is chosen.
    tap(find(ui(), resource='phone_campaigns'))
    wait_for(lambda: find(ui(), text='La última luz de Valdara'), 15, label='the campaign picker rows')
    screen('01b-campaign-picker')
    # Close with the dialog's own cancel button: BACK is the game's key, and the
    # launcher window must not be the thing that goes away.
    cancel = wait_for(lambda: next((n for n in ui() if n.get('resource-id') == 'android:id/button2'), None),
                      10, label='the campaign picker cancel button')
    tap(cancel)
    wait_for(lambda: find(ui(), resource='phone_tutorial'), 15, label='the launcher after closing the picker')
    print('Launcher and campaign picker shown', flush=True)
    for attempt in range(4):
        tap(wait_for(lambda: find(ui(), resource='phone_tutorial', enabled=True), 15,
                     label='the enabled tutorial button'))
        # Either the game comes up (data already installed) or the launcher
        # starts preparing it: asking for the launcher button again would race
        # with both.
        started = wait_for(lambda: 'game' if 'WesnothActivity' in adb(
                'shell', 'dumpsys', 'activity', 'top') else (
                'preparing' if find(ui(), resource='download_msg') is not None else None),
            30, label='the game or the data preparation to start')
        if started:
            print('Tutorial tap started:', started, flush=True)
            break
    else:
        raise AssertionError('Tutorial button did not start data preparation')
    print('Launcher started bundled-data preparation', flush=True)
    # Installation, native startup, and initial scenario loading are real here.
    wait_for(lambda: 'WesnothActivity' in adb('shell', 'dumpsys', 'activity', 'top'), 600, label='the native game activity')
    screen('02-tutorial-loaded')
    for step in range(90):
        nodes = ui()
        if find(nodes, resource='phone_action_cycle', enabled=True) is not None:
            break
        adb('shell', 'input', 'keyevent', 'KEYCODE_ENTER')
        time.sleep(2)
    if find(ui(), resource='phone_action_cycle', enabled=True) is None:
        raise AssertionError('Tutorial did not reach an interactive player turn')
    screen('03-interactive-game')
    print('Native tutorial reached an interactive turn', flush=True)
    tap(find(ui(), resource='phone_action_more'))
    wait_for(in_bar('phone_action_objectives', enabled=False), 15, label='the More sheet')
    screen('04-touch-menu')
    tap(find(ui(), resource='phone_action_objectives', enabled=True))
    wait_for(lambda: find(ui(), resource='phone_action_cycle') is not None
             and find(ui(), resource='phone_action_cycle', enabled=True) is None, 20, label='the objectives dialog to disable the bar')
    screen('04b-native-objectives')
    adb('shell', 'input', 'keyevent', 'KEYCODE_ENTER')
    wait_for(in_bar('phone_action_cycle'), 20, label='the bar to re-enable after the objectives dialog')
    tap(find(ui(), resource='phone_bar_toggle'))
    wait_for(lambda: find(ui(), resource='phone_action_cycle') is None, 15, label='the bar to collapse')
    screen('05-collapsed-controls')
    tap(find(ui(), resource='phone_bar_toggle'))
    wait_for(lambda: find(ui(), resource='phone_action_cycle') is not None, 15, label='the bar to expand again')
    screen('05b-expanded-controls')
    # Dialog-driven sends are the path a stale action mask used to refuse, so the
    # confirm on End turn has to keep working: it queues after the dialog closes.
    tap(find(ui(), resource='phone_action_endturn'))
    confirmation = wait_for(
        lambda: next((n for n in ui() if n.get('resource-id') == 'android:id/button1'), None),
        10, label='the end turn confirmation dialog')
    tap(confirmation)
    wait_for(in_bar('phone_action_cycle'), 240,
             label='the next player turn after confirming the end of one')
    screen('05c-end-turn-confirmed')
    adb('shell', 'am', 'force-stop', PACKAGE)
    adb('shell', 'am', 'start', '-n', PACKAGE + '/org.wesnoth.Wesnoth.InitActivity')
    tap(wait_for(lambda: find(ui(), resource='tap_label'), 30, label='the play button after relaunch'))
    wait_for(lambda: 'WesnothActivity' in adb('shell', 'dumpsys', 'activity', 'top'), 120, label='the native game activity after relaunch')
    time.sleep(20)
    if not adb('shell', 'pidof', PACKAGE).strip():
        raise AssertionError('Game process exited after relaunch')
    screen('06-main-menu-relaunch')
    (OUTPUT / 'result.txt').write_text('PASS: offline install, tutorial, interactive controls, menu, collapse, relaunch\n')
except Exception as error:
    annotate(error)
    raise
finally:
    screen('last-screen')
    (OUTPUT / 'logcat.txt').write_text(adb('logcat', '-d', check=False))
