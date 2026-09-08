/* SPDX-License-Identifier: GPL-2.0-or-later */
#pragma once

#include <array>
#include <string_view>

namespace phone {
// Wire IDs shared with PhoneControls.java. Keep existing IDs stable.
inline constexpr std::array<std::string_view, 14> actions = {
	"cycle", "recruit", "undo", "endturn", "zoomin", "zoomout",
	"objectives", "save", "recall", "unitlist", "leader", "describeunit",
	"preferences", "quit"
};

constexpr bool valid_action(int action)
{
	return action >= 0 && static_cast<unsigned>(action) < actions.size();
}
} // namespace phone
