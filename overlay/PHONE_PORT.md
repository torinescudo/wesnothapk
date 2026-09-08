# Wesnoth Phone

Android phone interface on the complete upstream Wesnoth engine. A signed ARM64
base APK has been built and its x86_64 counterpart passed Android 15 emulator
gameplay checks. The Brasa y Marea campaign expansion is being validated separately.

Upstream: https://github.com/wesnoth/wesnoth
Base revision: 682b77a27215f673397bfd2c6f65b854a01a6df8 (1.19.27+dev).

The original engine, campaigns, multiplayer, add-ons, editor, and licenses remain
part of the project. See COPYING and copyright for upstream licensing.

## Implemented

- Landscape Android controls with 48 dp minimum button height and system-scaled
  labels. The bottom bar reserves surface space, accounts for display cutouts,
  scrolls on narrow phones, and collapses with a saved preference.
- Explicit Move / attack confirmation, next unit, recruit, undo, zoom, and
  confirmed end turn. More exposes objectives,
  save, recall, unit list, leader, unit details, preferences, quit, and touch help.
- JNI/SDL command bridge independent of custom keyboard bindings. Commands run
  on the game thread through the existing legality checks. Out-of-range commands,
  stale events, dialogs, and unavailable actions are rejected. Java polls an
  atomic availability snapshot; callbacks stop when the activity pauses.
- A launcher with Play Wesnoth, Learn to play, and six original Spanish campaigns.
  Native phone controls have Spanish translations. Matching campaigns, music,
  and translations are included in the APK and extracted on first launch.
- An arm64 Linux build script and GitHub Actions builds in
  https://github.com/torinescudo/wesnothapk.
  Packaging rejects missing native libraries instead of producing an empty APK.
- A data archive builder includes the checked-out campaigns, music, art, fonts,
  sounds, licenses, and compiled translations, with a SHA-256 companion file.
- Android API 23 launcher compatibility fixes, bounded ZIP extraction/patch
  paths, and game-data clearing that preserves sibling saves. Controller code
  handles revoked Bluetooth permissions, declares vibration access, and uses
  an explicitly scoped USB broadcast receiver.

## Build the actual APK

Use the environment from `utils/dockerbuilds/CI/Dockerfile-base-android` or the
upstream `wesnoth/wesnoth:android` Linux container. It needs JDK 17, Android SDK
35/build-tools 34, NDK 26.3.11579264, GNU build tools, SCons, and gettext (`msgfmt`).
The dependency scripts explicitly use `linux-x86_64` NDK tools.

From the repository root on Linux:

```sh
git submodule update --init --recursive
bash packaging/android/build-phone.sh
```

For 32-bit ARM set `ARCHS=armeabi-v7a`; the default is `arm64-v8a`.
The APK is `packaging/android/app/build/outputs/apk/debug/app-arm64-v8a-debug.apk`.
The matching data ZIP and checksum are in `packaging/android/dist/`.
The build repository reconstructs the pinned source and applies the published
overlay with `prepare-source.py`. Its **Build Wesnoth Phone APK** workflow builds
ARM64; **Android emulator gameplay checks** builds and exercises x86_64 on Android 15.

The application ID is `org.wesnoth.phone`, so it installs separately from the
upstream Android app. A persistent distribution signing key is kept locally in
the ignored `.phone-tools/signing/` directory. Never publish that directory.

Install the self-contained APK and tap Play Wesnoth or Learn to play. No separate
data import is necessary. Settings still supports manual ZIP data import and
save import/export. Saved games and preferences are stored outside `gamedata`,
so reinstalling bundled content preserves them.

## Local checks

```sh
python -m unittest discover -s packaging/android/tests
cd packaging/android
./gradlew :app:testDebugUnitTest :app:lintDebug
```

The Windows workspace has a portable JDK 17, Gradle 8.11.1, and Android SDK 35
under `.phone-tools/`. Its `local.properties` is local and ignored by Git.
No Linux/WSL distribution, Docker runtime, or system Android SDK was detected.

Verified on this Windows workspace on 2026-09-08:

- Android resources and Java compilation: passed.
- Android lint: zero errors, 31 warnings (not a device/runtime test).
- JVM tests: 3 passed, covering nested archive paths, traversal rejection, and
  game-data deletion while preserving sibling saves.
- Python checks: 4 passed, covering the Java/C++ command contract, string
  resources, SDL event IDs, and data ZIP content/order/checksum.
- Build script shell syntax and Git whitespace check: passed.
- Missing-library packaging check: rejected absent arm64 `libmain.so` as intended.
- Linux ARM64 dependencies compiled and cached successfully in GitHub Actions.
- Linux ARM64 and x86_64 native engines: built successfully.
- Base APK: nested ZIP integrity, content checksum, all native libraries, 44 core
  music tracks, and 1,922 translation catalogs verified. Persistent signing key
  verification passed for APK signature schemes v1, v2 and v3.
- Android 15 emulator: offline installation, interactive tutorial, touch menu,
  native objectives dialog, collapsing/reopening controls, and relaunch passed
  in https://github.com/torinescudo/wesnothapk/actions/runs/34244866898.

## Original Spanish campaigns

`data/campaigns/Brasa_y_Marea` contains six standalone campaigns with 3, 5, 7,
9, 12 and 16 scenarios. See its `README.es.md` for stories and controls.
The litarios and velarios have four two-level unit lines each. Six original
protagonists, portraits, map sprites and twelve procedural music compositions
are included. Source narrative and build/validation scripts live in
`packaging/android/campaigns/`.

Structural validation covers all 52 maps, scenario chains, unit identifiers,
objectives and resource references. The build repository's campaign emulator
test opens all six campaigns without modification, then injects test events
only into extracted emulator data to exercise the actual objective events and
transitions. This does not measure campaign balance or substitute for manual
playthroughs. See the build repository's `VALIDATION.md` for completed results.

## Practical limits

No physical phone is attached. The existing SDL/Wesnoth dialogs still need a
broader review on narrow/notched screens and at large font sizes; the new bar
does not replace every desktop dialog. Multiplayer and add-on networking have
not been exercised end to end. The current ARM64 native libraries have 4 KiB
ELF segment alignment; devices requiring 16 KiB pages need a rebuilt native
toolchain and separate verification. Emulator checks used Android 15 with 4 KiB
pages. Keep the persistent local signing key to allow updates without replacing
the installed application identity.
