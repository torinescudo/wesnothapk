/* SPDX-License-Identifier: GPL-2.0-or-later */
package org.wesnoth.Wesnoth;

import java.io.File;
import java.io.IOException;

/** API 23-compatible file operations confined to the app's game-data directory. */
final class GameDataFiles {
    private GameDataFiles() {}

    static File resolve(File root, String name) throws IOException {
        if (name.isEmpty() || new File(name).isAbsolute() || name.contains("\\")) {
            throw new IOException("Invalid game-data path: " + name);
        }
        File result = new File(root, name).getCanonicalFile();
        String boundary = root.getCanonicalPath() + File.separator;
        if (!result.getPath().startsWith(boundary)) {
            throw new IOException("Path escapes game-data directory: " + name);
        }
        return result;
    }

    static void deleteTree(File root) throws IOException {
        if (!root.exists()) return;
        deleteWithin(root.getCanonicalFile(), root.getCanonicalFile());
    }

    private static void deleteWithin(File root, File entry) throws IOException {
        File canonical = entry.getCanonicalFile();
        // Delete links themselves; do not recurse through aliases or cycles.
        if (!canonical.equals(entry.getAbsoluteFile())) {
            if (!entry.delete()) throw new IOException("Cannot delete link " + entry);
            return;
        }
        if (!canonical.equals(root) && !canonical.getPath().startsWith(root.getPath() + File.separator)) {
            throw new IOException("Refusing to follow a path outside game data");
        }
        if (entry.isDirectory()) {
            File[] children = entry.listFiles();
            if (children == null) throw new IOException("Cannot list " + entry);
            for (File child : children) deleteWithin(root, child);
        }
        if (!entry.delete()) throw new IOException("Cannot delete " + entry);
    }
}
