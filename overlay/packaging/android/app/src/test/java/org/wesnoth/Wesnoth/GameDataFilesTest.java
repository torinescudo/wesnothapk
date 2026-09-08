/* SPDX-License-Identifier: GPL-2.0-or-later */
package org.wesnoth.Wesnoth;

import java.io.File;
import java.io.IOException;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.TemporaryFolder;
import static org.junit.Assert.*;

public class GameDataFilesTest {
    @Rule public TemporaryFolder temporary = new TemporaryFolder();

    @Test public void allowsNestedArchiveEntriesWithoutExistingParents() throws Exception {
        File root = temporary.newFolder("gamedata");
        assertEquals(new File(root, "data/core/file.cfg").getCanonicalFile(),
            GameDataFiles.resolve(root, "data/core/file.cfg"));
    }

    @Test public void rejectsTraversalAbsolutePathsAndRootItself() throws Exception {
        File root = temporary.newFolder("gamedata");
        for (String path : new String[] {"", ".", "..", "../saves", "data/../../saves",
                "../gamedata-other/file", "..\\saves", root.getAbsolutePath()}) {
            try {
                GameDataFiles.resolve(root, path);
                fail("Accepted unsafe path: " + path);
            } catch (IOException expected) {
                // Both extraction and patch deletion use this boundary.
            }
        }
    }

    @Test public void clearingGameDataPreservesSiblingSaves() throws Exception {
        File root = temporary.newFolder("gamedata");
        File nested = new File(root, "data/core");
        assertTrue(nested.mkdirs());
        assertTrue(new File(nested, "unit.cfg").createNewFile());
        File save = temporary.newFile("save.gz");
        GameDataFiles.deleteTree(root);
        assertFalse(root.exists());
        assertTrue(save.exists());
        GameDataFiles.deleteTree(root); // Clearing an already absent tree is safe.
    }
}
