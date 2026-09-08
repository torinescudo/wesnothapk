# Validation record

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
