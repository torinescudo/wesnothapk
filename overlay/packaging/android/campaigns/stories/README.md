# Authoring the Crónicas de la Brasa y la Marea

One module per campaign (`alba.py`, `sira.py`, `iria.py`, `maura.py`, `nerea.py`,
`darian.py`), one `CAMPAIGN` dict each, one `dict(...)` per chapter. These files
are the source of truth: `build_campaigns.py` generates the WML, the maps and the
manifest from them, so hand edits to `data/campaigns/**` are overwritten.

    python -m stories            # structural check and beat counts
    python -m stories --strict   # fails when a chapter is below the authoring bar

## Campaign fields

| field | meaning |
| --- | --- |
| `key` | module name, also the map and music prefix |
| `title`, `hero`, `companion`, `companion_type` | shown in the launcher, the campaign list and the first chapter |
| `race`, `recruit`, `enemy` | recruit lists and the opposing faction key used by the generator |
| `length` | short duration label for the campaign menu |
| `premise`, `ending` | narration framing the whole campaign (≥ 120 characters) |
| `chapters` | authored episodes in play order |

## Chapter fields

| field | meaning |
| --- | --- |
| `title`, `goal`, `biome`, `antagonist` | chapter name, objective kind, map family, opposing leader name |
| `opening` | story-screen prose, ≥ 240 characters |
| `intro` | `[(speaker, line), ...]` played as the chapter opens |
| `events` | `[(trigger, [(speaker, line), ...]), ...]` played mid-scenario |
| `victory` | `[(speaker, line), ...]` played before the closing narration |
| `protected` | `(name, unit_type)` for escort and rescue goals, otherwise `None` |
| `resolution` | closing narration for the chapter, ≥ 140 characters |

`goal` is one of `conquer`, `survive`, `escape`, `escort`, `rescue`, `beacons`.
`biome` is one of `forest`, `coast`, `harbor`, `cave`, `quarry`, `plains`,
`mountain`, `ruins`, `islands`.

Triggers accepted in `events`:

* `turn N` — the start of turn N
* `time limit` — the last two turns
* `enemy leader defeated` — immediately after the opposing leader dies
* `village captured` — the first village the player takes
* `half strength` — when the protected character is first wounded
* `beacon lit N` — after the Nth beacon or objective point is reached

## Speakers

`narrator`, `hero`, `companion`, `antagonist` and `protected` are units the
generator already places or controls, so they speak with their own portrait and
name. Any other name is a character who speaks through a portrait image message:
write the name exactly as it should appear on screen. Keep names short and
consistent inside a campaign, and reuse one spelling for a recurring character.

## The bar a chapter has to clear

Measured against mainline scenarios (`compare_with_mainline.py`):

* `intro` ≥ 12 beats, at least 3 scripted `events`, `victory` ≥ 4 beats
* ≥ 22 authored beats in total per chapter
* `opening` ≥ 240 characters, `resolution` ≥ 140 characters

Write the lines the way the existing chapters do: dialogue that carries the
chapter's conflict, gives the antagonist a reason, and leaves the tactical
objective understandable on a phone screen. Lines are read in a small dialog box
while the player is also watching the map, so keep each beat to one or two
sentences.
