# Wesnoth Phone

Android phone controls for the complete Battle for Wesnoth engine. This project
builds upstream revision `682b77a27215f673397bfd2c6f65b854a01a6df8`
with the source changes in `overlay/`. It is a development build, not an official
Wesnoth release.

The phone interface adds large collapsible controls for move/attack confirmation, next unit, recruitment,
undo, zoom, and confirmed end turn. More provides saves, objectives and unit
information. Existing campaigns, multiplayer, add-ons, music, and game rules
come from the full upstream source.

**Crónicas de la Brasa y la Marea** adds six original Spanish-language fantasy
campaigns with 3, 5, 7, 9, 12 and 16 scenarios. They include two original races
(litarios and velarios), a campaign played as the villain Maura Vey, original
portraits/map sprites, and twelve original instrumental tracks. The launcher
offers direct campaign selection and the phone controls support Spanish.
See [the campaign guide](overlay/data/campaigns/Brasa_y_Marea/README.es.md).

## Build and download

The **Build Wesnoth Phone APK** workflow runs on pushes to `main`, or manually
from Actions. Its artifact contains an ARM64 APK with the full game data included.
The application ID is `org.wesnoth.phone`, so it installs separately from the
official app. Builds use a development signing key.

Install the APK and choose **Play Wesnoth**, **Learn to play**, or
**Campañas originales**. The first launch
unpacks the included game data, music, and translations without another download.
The separate **Android emulator gameplay checks** workflow builds x86_64 and
tests offline installation, the tutorial, touch menus, and relaunch on Android 15.
Screenshots and logs are retained as evidence of what actually ran. The campaign
checks open all six stories and use an emulator-only event harness to exercise
their 52 objective conditions and transitions. See [VALIDATION.md](VALIDATION.md)
for completed results and limits; these checks do not measure tactical balance.

## Source and licensing

Run `python3 prepare-source.py` to reconstruct the full source. It fetches the
exact upstream revision, initializes submodules, and copies the overlay. The
native build uses the upstream `wesnoth/wesnoth:android` Linux container.
Campaign narrative, deterministic map generation, music synthesis, resource
validation and source packaging tools are under `overlay/packaging/android/campaigns`.

Wesnoth and these changes use GPL-2.0-or-later except where the upstream source
specifies separate asset or bundled-library licenses. See `COPYING`,
`upstream-copyright`, and the reconstructed source for the complete notices.

Upstream: https://github.com/wesnoth/wesnoth
