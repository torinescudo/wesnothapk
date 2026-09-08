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


def wait_for(predicate, timeout):
    end = time.monotonic() + timeout
    while time.monotonic() < end:
        value = predicate()
        if value is not None and value is not False:
            return value
        time.sleep(2)
    raise AssertionError('Timed out waiting for the native game or UI')


try:
    adb('install', '-r', sys.argv[1])
    adb('shell', 'svc', 'wifi', 'disable')
    adb('shell', 'svc', 'data', 'disable')
    adb('shell', 'am', 'start', '-n', PACKAGE + '/org.wesnoth.Wesnoth.InitActivity')
    tutorial = wait_for(lambda: find(ui(), resource='phone_tutorial'), 40)
    screen('01-launcher')
    tap(tutorial)
    # Installation, native startup, and initial scenario loading are real here.
    wait_for(lambda: 'WesnothActivity' in adb('shell', 'dumpsys', 'activity', 'top'), 600)
    screen('02-tutorial-loaded')
    for step in range(90):
        nodes = ui()
        if find(nodes, text='Next unit', enabled=True) is not None:
            break
        adb('shell', 'input', 'keyevent', 'KEYCODE_ENTER')
        time.sleep(2)
    if find(ui(), text='Next unit', enabled=True) is None:
        raise AssertionError('Tutorial did not reach an interactive player turn')
    screen('03-interactive-game')
    tap(find(ui(), text='More'))
    wait_for(lambda: find(ui(), text='Objectives'), 15)
    screen('04-touch-menu')
    tap(find(ui(), text='Objectives', enabled=True))
    wait_for(lambda: find(ui(), text='Next unit') is not None
             and find(ui(), text='Next unit', enabled=True) is None, 20)
    screen('04b-native-objectives')
    adb('shell', 'input', 'keyevent', 'KEYCODE_ENTER')
    wait_for(lambda: find(ui(), text='Next unit', enabled=True), 20)
    tap(wait_for(lambda: find(ui(), text='Hide'), 15))
    wait_for(lambda: find(ui(), text='Controls'), 15)
    screen('05-collapsed-controls')
    tap(find(ui(), text='Controls'))
    wait_for(lambda: find(ui(), text='Next unit'), 15)
    adb('shell', 'am', 'force-stop', PACKAGE)
    adb('shell', 'am', 'start', '-n', PACKAGE + '/org.wesnoth.Wesnoth.InitActivity')
    tap(wait_for(lambda: find(ui(), resource='tap_label'), 30))
    wait_for(lambda: 'WesnothActivity' in adb('shell', 'dumpsys', 'activity', 'top'), 120)
    time.sleep(20)
    if not adb('shell', 'pidof', PACKAGE).strip():
        raise AssertionError('Game process exited after relaunch')
    screen('06-main-menu-relaunch')
    (OUTPUT / 'result.txt').write_text('PASS: offline install, tutorial, interactive controls, menu, collapse, relaunch\n')
finally:
    screen('last-screen')
    (OUTPUT / 'logcat.txt').write_text(adb('logcat', '-d', check=False))
