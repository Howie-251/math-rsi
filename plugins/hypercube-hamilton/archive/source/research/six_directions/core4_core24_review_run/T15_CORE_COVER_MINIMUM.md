# Minimum number of orbit cores for the current a2b1 reduction scheme

Date: 2026-11-01. This is finite proof-planning accounting, not a Hamilton
path existence theorem. It concerns only selecting whole T15 geometry
orbits in the current (a,b)=(2,1) transfer; other proof strategies may
avoid any of these auxiliary obligations.

The independently checked `eight_t15_core_map.json` lists all available
T15 orbit choices for each of the 65920 R8-covered hole geometries having
an a2b1 cut. There are 41 used core orbits but only 34 distinct choice
sets. Core numbers refer to the zero-based `residual_orbits` list in
`t15_analytic_geometry.json`; they are not intrinsic mathematical labels.

Sixteen singleton choice sets force these sixteen cores in any cover
that uses this scheme:

    0,1,2,4,5,8,10,13,14,15,19,23,24,27,50,53.

Discard every choice set already meeting those sixteen. The remaining
eleven constraints fall into seven disjoint variable groups:

| remaining group | required choice sets | one sufficient choice |
|---|---|---:|
| {6,7,9} | {6,7}, {7,9} |7|
| {18,21,25,26} | {18,26}, {21,26}, {25,26} |26|
| {30,34,41,44,46} | {30,41,44}, {34,44,46} |44|
| {31,43} | {31,43} |31|
| {32,42} | {32,42} |32|
| {35,45} | {35,45} |35|
| {49,51} | {49,51} |49|

The seven groups are disjoint from each other and from the sixteen
forced cores. Each needs at least one selected member. Thus every such
cover has size at least 16+7=23. The listed choices meet every remaining
constraint with exactly seven additions, proving a cover of size 23
and its optimality WITHIN THIS REDUCTION SCHEME.

This does not claim that 23 separate new theorems are logically necessary:
one general lemma might prove multiple cores, another transfer might avoid
them, and matching-specific choices may be finer than whole geometry orbits.
It does not address the 207 parent geometries having no a2b1 cut, or the
higher-hole P6 layers. None of these 23 T15 core theorems is declared
proved by the set-cover argument.
