// SPDX-License-Identifier: GPL-2.0-or-later
package org.wesnoth.Wesnoth;

/** Stable campaign identifiers shared by the launcher and native arguments. */
final class PhoneCampaigns {
    static final String[] IDS = {
        "CBM_alba", "CBM_sira", "CBM_iria", "CBM_maura", "CBM_nerea", "CBM_darian"
    };

    static boolean contains(String candidate) {
        for (String id : IDS) if (id.equals(candidate)) return true;
        return false;
    }

    private PhoneCampaigns() {}
}
