# Map design: what a quality map is made of

The generator used to fill a grid with noise. These are the rules the maps have
to satisfy instead, measured against the mainline campaigns with the same code
(`map_preview.py` to look at them, `compare_with_mainline.py` to count them).
Numbers are medians over 5 mainline maps (Heir to the Throne 01, Son of the Black
Eye 01, Liberty 01, The South Guard 01, Dead Water 01, Rise of Wesnoth 01) and
12 generated ones.

## What the measurements say

| property | mainline | generated before | generated after | what it means |
| --- | ---: | ---: | ---: | --- |
| largest same-terrain cluster, share of its own tiles | 0.45 | 0.69 | 0.42 | masses now break up the way mainline maps do |
| tiles with no like neighbour | 0.044 | 0.015 | 0.073 | textured edges instead of smooth blobs |
| road tiles | 89 | 43.5 | 103 | roads now lace the land |
| road share of the map | 0.107 | 0.03 | 0.076 | arterials, branches and verges |
| villages | 14 | 14.5 | 14.5 | parity |
| villages touching a road | 0.33 | 0.83 | 0.15 | settlements sit at features now |
| mean village-to-village distance | 5.8 | 4.05 | 7.2 | spread out like defensible places |
| villages cut off from the main landmass | 0 | 0 | 2 | two island chapters, by design |

So the problem was never size or village count: it was that the maps were too
uniform and too empty of structure.

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
