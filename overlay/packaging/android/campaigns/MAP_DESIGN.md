# Map design: what a quality map is made of

The generator used to fill a grid with noise. These are the rules the maps have
to satisfy instead, measured against the mainline campaigns with the same code
(`map_preview.py` to look at them, `compare_with_mainline.py` to count them).
Numbers are medians over 5 mainline maps (Heir to the Throne 01, Son of the Black
Eye 01, Liberty 01, The South Guard 01, Dead Water 01, Rise of Wesnoth 01) and
12 generated ones.

## What the measurements say

All numbers come from `compare_with_mainline.py`, so they reproduce with one
command on the reconstructed tree. "before" is the maps as first generated,
"after" is what the rules below produce.

| property (tool field) | mainline | before | after |
| --- | ---: | ---: | ---: |
| map tiles | 932 | 540 | 1341 |
| distinct terrain codes per map | 34.5 | 7 | 51.5 |
| villages per map | 14 | 10 | 15 |
| road tiles per map | 60 | 43.5 | 101 |
| mean village-to-village distance | 4.38 | 4.05 | 5.78 |
| largest one-blob share of a base terrain | 0.139 | — | 0.113 |
| tiles with no like neighbour | 0.0813 | 0.1306 | 0.1681 |
| villages cut off from the main landmass | 689 | 1 | 0 |

So the problem was never size or village count: it was that the maps were too
uniform and too empty of structure. Two rows need a word: the isolated-tile
ratio is the one axis where we are *worse* than mainline (0.17 against 0.08) —
the edge roughening that gives the coasts inlets also leaves more single-tile
breaks — and mainline's cut-off villages are naval maps where that is the point.

## The rules

1. **Terrain in masses and in details.** Big shapes first (the coast, the ridge,
   the forest belt), then break each mass with features of a different family:
   a hill in the plain, a clearing in the forest, a sand shelf in the water. The
   largest cluster of any family should stay under half of that family's tiles,
   which is where mainline sits.
2. **A road network, not spokes.** Every keep, village and objective is on the
   road graph, and the graph has branches and loops: one arterial between the
   keeps, secondaries to villages, and short spurs to lookouts. Target roughly a
   tenth of the map's tiles on roads, which is the mainline density.
3. **Villages in places, not on the shoulder of the road.** A village belongs
   against a feature: a forest edge, a hill foot, a bay, a bend in the river. At
   most a third of them should touch a road, and they should sit a good five to
   seven tiles apart, which is where defensible settlements actually are.
4. **Every objective reachable from both keeps**, on walkable ground, and no
   village on its own island unless the scenario is about the sea. The generator
   proves this and retries with another seed when it fails.
5. **Readability at a glance.** The keep pair is symmetric in the layout family
   (opposite corners, opposite edges, north/south), the objective markers sit on
   the road graph, and the interesting terrain is between the armies rather than
   behind them.

## How this is enforced

- `mapgen.py` builds the map in passes (landform, relief, detail, rivers, roads,
  villages) and rejects its own output when rule 4 fails.
- `validate_campaigns.py` checks row widths (the engine rejects ragged maps),
  terrain codes against `data/core/terrain.cfg`, village count, and reachability.
- `compare_with_mainline.py --gate` keeps the counts above the mainline floor.

## Not covered here

Tactical balance (is the map fun to fight over) and the art of hand-drawn maps:
both need playtesting and a human eye. The rules above are what can be built and
checked repeatedly.
