# Validation record

## The build running on a phone — 2026-09-24

`app-arm64-v8a-debug.apk` from the `58f45d6` artifact (747 MB) installed on a
Xiaomi Redmi (arm64-v8a, Android 16 / API 36) and launched as
`org.wesnoth.phone/.Wesnoth.InitActivity`, running as version
`1.19.27+brasa-marea.2`.

Installing over the previous local build needed `adb install -d`: that build
shipped versionCode 1192706 and this one carried 1192702, which Android reports
as `INSTALL_FAILED_VERSION_DOWNGRADE`. The version code and name now move to
1192707 / 1.19.27+brasa-marea.3, so the next build installs as an update.

MIUI blocked the first attempts with `INSTALL_FAILED_USER_RESTRICTED`, and two
`SecurityException`s named the cause rather than leaving it a guess:
`INJECT_EVENTS` and `WRITE_SECURE_SETTINGS` were both denied, which is MIUI's
"USB debugging (Security settings)" switch being off. Enabling that switch
allowed the install. The device had no saved games at any point, so nothing was
at risk while this was sorted out.

## Phone interface and campaigns on the Android 15 emulator — 2026-09-24

Two runs make the record: the harness pass
(https://github.com/torinescudo/wesnothapk/actions/runs/35991136417, commit
018c397) and the full gameplay check that carries the map, art and story work
(https://github.com/torinescudo/wesnothapk/actions/runs/35991663042, commit
58f45d6). The version-code bump of commit 885b6fa then passed the same full
check on its own run (https://github.com/torinescudo/wesnothapk/actions/runs/
35994284299), so the packaging change is verified too. All green:
`smoke-test.py` and `campaign-smoke-test.py` drove the launcher, the campaign
picker, More > Objectives, the collapse/expand chevron and the End turn
confirmation on a real Android 15 emulator, then opened all six campaigns and
exercised all 52 objective transitions and campaign endings.

The way to that pass is what the harness now guards, and the record belongs
here because each failure was a real defect:

- a stale JNI action mask refused dialog-driven taps (End turn, Quit, and the
  More sheet), because "snapshot older than 500 ms" was folded into "nothing is
  available". `nativeGetPhoneActions` now reports `phone::stale_mask`, and the
  Java side keeps the last state and waits instead of refusing;
- the campaign picker was closed with the game's own BACK key, so the launcher
  window went away behind it;
- two waits measured things the interface does not control: a full AI turn over
  a 1300-tile map (now asserted as "the player turn ended", not "the AI came
  back") and a launcher race when the game starts in under two seconds.

Failures are surfaced as CI annotations with the traceback and the tail of the
last UI dump, which is what turned each of those into a diagnosis instead of a
guess.

## Map design pass — 2026-09-24

`packaging/android/campaigns/MAP_DESIGN.md` is the breakdown of what a quality
map is made of, extracted by measuring and looking at mainline maps
(`map_preview.py` renders any .map to a comparable grid). The rules were then
implemented in `mapgen.py` and measured back:

| property (from `compare_with_mainline.py`) | mainline | generated before | generated after |
| --- | ---: | ---: | ---: |
| map tiles | 932 | 540 | 1341 |
| distinct terrain codes per map | 34.5 | 7 | 51.5 |
| road tiles per map | 60 | 43.5 | 101 |
| mean village-to-village distance | 4.38 | 4.05 | 5.78 |
| tiles with no like neighbour | 0.0813 | 0.1306 | 0.1681 |
| villages cut off from the main landmass | 689 | 1 | 0 |

The isolated-tile ratio is the one axis that got worse: the edge roughening that
gives the coasts inlets also leaves more single-tile breaks (0.17 against
mainline's 0.08). Every number above reproduces with
`python3 compare_with_mainline.py`; an earlier version of this table used a
separate measurement script whose definitions differed from the committed tool,
and those numbers have been replaced.

New passes: edge roughening (inlets, headlands and islets), rivers that start on
high ground and leave the frame, a road network with arterials, branches and
verges instead of spokes from the keeps, and village siting on landforms (shore,
mountain foot, forest edge) with at most a third of them touching a road. Roads
no longer pave over keeps or villages.

An independent look at rendered maps scores the generated ones 4-7/10 for
composition against 8-9 for the hand-made ones, up from 4-6 before this pass.
What is still visibly generated, and why this entry is a milestone and not the
end: coast detail is one scale where mainline has several, road webs branch but
do not loop, and settlements are attracted to features but not yet to crossings.

Verified: `python3 validate_campaigns.py` (which now also rejects ragged maps —
the engine's `gamemap::read` refuses rows of differing width — and compares the
manifest's village count with the map) and `python3 compare_with_mainline.py
--gate` both pass on the reconstructed tree.

## Campaign rework — 2026-09-24

The six campaigns were rebuilt from authored narrative and structured map
synthesis, then measured against the mainline campaigns with the same parser
(`packaging/android/campaigns/compare_with_mainline.py`, `--gate` in CI). Every
gated metric now clears the 25th percentile of the mainline campaigns.

| metric | before | after | mainline p25 | mainline median |
| --- | ---: | ---: | ---: | ---: |
| WML lines per scenario | 280 | 438 | 428 | 602 |
| dialogue lines per scenario | 7 | 33 | 23 | 31.5 |
| scripted events per scenario | 10 | 15 | 8.5 | 10 |
| story screens per scenario | 1 | 3 | 0 | 1.5 |
| map tiles | 540 | 1341 | 868 | 1184 |
| distinct terrain codes per map | 7 | 52 | 33 | 42 |
| villages per map | 10 | 15 | 13.5 | 17 |
| villages cut off from the main landmass | 1 | 0 | (mainline median includes naval maps) | |

- Narrative: 1,487 authored dialogue beats over 52 chapters, one module per
  campaign under `packaging/android/campaigns/stories/`. The schema and the
  authoring bar are documented in `stories/README.md` and enforced by
  `python3 -m stories --strict`.
- Maps: `mapgen.py` composes coastlines, rivers crossed by the roads that need
  them, forest masses, ridges, cost-routed roads and village bands, then proves
  every village and objective reachable from both keeps before the map is
  accepted, retrying with a new seed otherwise. Every terrain code is checked
  against `data/core/terrain.cfg`.
- Art: `ART_PROMPTS.json` now carries a prompt for every image the campaigns
  reference (38 portraits, 104 chapter scenes, 8 unit sprite sets) and
  `artgen.py status` reports what is installed. Until the image generation pass
  runs, chapters fall back to the portraits that already exist, so the build
  never points the engine at a file nobody has drawn.

Verified on the reconstructed tree: `python3 validate_campaigns.py` (structure,
assets, reachability, terrain variety, dialogue volume) and
`python3 compare_with_mainline.py --gate` both pass; CI runs both before
packaging. Not measured here: tactical balance, and art parity with hand-painted
mainline portraits, which depends on an image generation pass that has not been
run.

## Base port — 2026-09-08

- ARM64 and x86_64 engines compiled from upstream revision
  `682b77a27215f673397bfd2c6f65b854a01a6df8` with the phone interface overlay.
- Android 15 emulator passed offline first installation, interactive tutorial,
  touch menu, native objectives, collapsed controls and relaunch:
  https://github.com/torinescudo/wesnothapk/actions/runs/34244866898
- Full APK/data ZIP checksums and integrity passed. The original bundle contains
  44 core music tracks and 1,922 translation catalogs.
- Local persistent signature verifies with APK schemes v1, v2 and v3.

## Brasa y Marea expansion — 1.19.27+brasa-marea.2

- Six campaigns / 52 scenarios / 52 unique maps / 22 unit types.
- Structural WML parsing, scenario routes, known unit references and required
  map destinations pass. Strict resource validation runs before packaging.
- All twelve original Ogg Vorbis tracks decode successfully, contain finite
  samples and have measured peaks below 0.85 full scale.
- Java/JVM tests and Android lint pass (zero errors, 31 warnings).
- Four Python phone/data packaging contract tests pass.
- ARM64 native build, Android checks, complete data packaging and APK assembly
  passed: https://github.com/torinescudo/wesnothapk/actions/runs/34274771182
- Local signed ARM64 APK: 722,407,792 bytes; signature schemes v1/v2/v3 pass.
  SHA-256: `65bcfbae6735790c1c28c44f9f23c0bf4eeb3622f28abd6fb7e376a34238219d`.
- Nested archive integrity and checksum pass. All 144 campaign files in the APK
  match the authored sources byte for byte, including 21 PNGs and 12 Ogg tracks.
- Version .2 fixes a map-coordinate regression: native .map files contain an
  off-board border. The generator now includes that ring, keeping the authored
  WML destinations on their land routes. The validator rejects the old map
  layout and checks start markers against native border coordinates.
- Android 15 emulator: offline installation, tutorial, phone controls, Spanish
  selector and all six unmodified campaign openings passed.
- All 52 native objective checks and campaign transitions passed, including
  Nerea 12 and all 16 Darian scenarios. The harness also verifies exact arrival
  coordinates, duplicate beacon protection, protected-unit identity and new
  recruit sprite loading. All six campaigns reached their endings.
  Successful run: https://github.com/torinescudo/wesnothapk/actions/runs/34274771110
  Permanent result: [campaigns-2026-09-08.json](validation/campaigns-2026-09-08.json).

The emulator integration harness modifies only its extracted scenario files,
never the distributable APK. It exercises real objective events while bypassing
tactical combat. Its results must not be described as 52 manual playthroughs or
as validation of difficulty balance. No physical device is connected. Current
native libraries have 4 KiB alignment; 16 KiB-only devices remain unverified.
