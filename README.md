# Wesnoth Phone

Android phone controls for the complete Battle for Wesnoth engine. This project
builds upstream revision `682b77a27215f673397bfd2c6f65b854a01a6df8`
with the source changes in `overlay/`. It is a development build, not an official
Wesnoth release.

The phone interface adds large collapsible controls for next unit, recruitment,
undo, zoom, and confirmed end turn. More provides saves, objectives and unit
information. Existing campaigns, multiplayer, add-ons, music, and game rules
come from the full upstream source.

## Build and download

The **Build Wesnoth Phone APK** workflow runs on pushes to `main`, or manually
from Actions. Its artifact contains an ARM64 APK and matching full game data ZIP.
The application ID is `org.wesnoth.phone`, so it installs separately from the
official app. Builds use a development signing key.

Install the APK, then use its launcher Settings > local ZIP install to select
`wesnoth-phone-data.zip`. Data includes music and all available translations.
The first full native build is still being validated; see Actions for the actual
build status. Source checks are not evidence of successful phone gameplay.

## Source and licensing

Run `python3 prepare-source.py` to reconstruct the full source. It fetches the
exact upstream revision, initializes submodules, and copies the overlay. The
native build uses the upstream `wesnoth/wesnoth:android` Linux container.

Wesnoth and these changes use GPL-2.0-or-later except where the upstream source
specifies separate asset or bundled-library licenses. See `COPYING`,
`upstream-copyright`, and the reconstructed source for the complete notices.

Upstream: https://github.com/wesnoth/wesnoth
