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

## Brasa y Marea expansion — current work

- Six campaigns / 52 scenarios / 52 unique maps / 22 unit types.
- Structural WML parsing, scenario routes, known unit references and required
  map destinations pass. Strict resource validation runs before packaging.
- All twelve original Ogg Vorbis tracks decode successfully, contain finite
  samples and have measured peaks below 0.85 full scale.
- Java/JVM tests and Android lint pass (zero errors, 31 warnings).
- Four Python phone/data packaging contract tests pass.
- Native campaign opening/objective/transition tests are pending the new build.

The emulator integration harness modifies only its extracted scenario files,
never the distributable APK. It exercises real objective events while bypassing
tactical combat. Its results must not be described as 52 manual playthroughs or
as validation of difficulty balance. No physical device is connected. Current
native libraries have 4 KiB alignment; 16 KiB-only devices remain unverified.
