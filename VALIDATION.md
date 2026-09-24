# Validation record

## Map design pass — 2026-09-24

`packaging/android/campaigns/MAP_DESIGN.md` is the breakdown of what a quality
map is made of, extracted by measuring and looking at mainline maps
(`map_preview.py` renders any .map to a comparable grid). The rules were then
implemented in `mapgen.py` and measured back:

| property | mainline | generated before | generated after |
| --- | ---: | ---: | ---: |
| largest same-terrain cluster, share of its tiles | 0.45 | 0.69 | 0.42 |
| tiles with no like neighbour | 0.044 | 0.015 | 0.073 |
| road tiles per map | 89 | 43.5 | 103 |
| villages touching a road | 0.33 | 0.83 | 0.15 |
| mean village-to-village distance | 5.8 | 4.05 | 7.2 |

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
