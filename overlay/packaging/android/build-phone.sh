#!/usr/bin/env bash
# SPDX-License-Identifier: GPL-2.0-or-later
set -euo pipefail
if [[ "$(uname -s)" != Linux ]]; then
    echo 'The native game build requires Linux (for example WSL2 or the upstream Docker image).' >&2
    exit 1
fi
for required in java python3 scons msgfmt; do
    command -v "$required" >/dev/null || { echo "Missing build tool: $required" >&2; exit 1; }
done
cd "$(dirname "$0")"
export ARCHS="${ARCHS:-arm64-v8a}"
export API="${API:-23}"
export BUILDBASEDIR="$PWD"
export PREFIXDIR="${PREFIXDIR:-$PWD/prefix}"
export DOWNLOADDIR="${DOWNLOADDIR:-$PWD/download}"
export BUILDDIR="${BUILDDIR:-$PWD/build}"
export BUILDDIR_PREFIX="${BUILDDIR_PREFIX:-$PWD/build-native}"
abis="${ARCHS// /,}"
bash ./gradlew buildCppDepends buildCppSource :app:testDebugUnitTest :app:lintDebug -PphoneAbis="$abis"
python3 package-phone-data.py
mkdir -p app/src/main/assets
cp dist/wesnoth-phone-data.zip app/src/main/assets/gamedata.zip
cp dist/wesnoth-phone-data.zip.sha256 app/src/main/assets/gamedata.zip.sha256
bash ./gradlew :app:assembleDebug -PphoneAbis="$abis"
