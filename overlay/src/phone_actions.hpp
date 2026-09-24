/* SPDX-License-Identifier: GPL-2.0-or-later */
#pragma once

#include <array>
#include <string_view>

namespace phone {
// Wire IDs shared with PhoneControls.java. Keep existing IDs stable.
inline constexpr std::array<std::string_view, 15> actions = {
	"cycle", "recruit", "undo", "endturn", "zoomin", "zoomout",
	"objectives", "save", "recall", "unitlist", "leader", "describeunit",
	"preferences", "quit", "moveaction"
};

// Returned to Java when the published snapshot is too old to trust. SDL can stop
// publishing while a dialog holds focus, and "no news" is not "nothing is
// available": the Java side keeps the last state and waits instead of refusing.
inline constexpr int stale_mask = -2;

constexpr bool valid_action(int action)
{
	return action >= 0 && static_cast<unsigned>(action) < actions.size();
}
} // namespace phone
