# Result: spreading the holes broadens routes, but the own-cover batch is UNKNOWN

2026-11-01. Root read the actual base/result/terminal, color model/result/
terminal, route-prediction result and solver log. Session91896 exited0;
the one solver run reached its45-second limit without an integer incumbent.
Total child CPU was49.845277 of60, including imports and mask preparation.
No timer/seed restart or second hole layout was tried.

The geometrical prediction was supported, not merely a total bad-pair count:

|freed old-U pins|actual old groups reached in two steps|
|---:|---:|
|105 nonabsolute-B pins|5 each|
|15 nonabsolute-B pins|8 each|
|10 absolute-B pins|1 each|

This is the intended change from the previous same-column rule's separated
repair blocks. It does not prove that six simultaneous covers can be chosen.

All10070 current G0 targets were represented. Their130-bit radius2 masks
gave8711 unique masks, with8582 minimal retained constraints after exact
subset reduction. A retained-mask subset witness is saved for every old
target. The smallest mask has7 pins. The final model had780 binary color
variables plus one max-load variable,51659 rows and403036 nonzeros.
Although this removes the earlier10500-variable/7349320-nonzero model's
size, the actual solver log still reached16047 LP iterations and zero
branching nodes before its limit. No integer solution or objective optimum
was obtained. This is algorithmic evidence about this batch, not a proof
of infeasibility.

The restricted question was SIX DISJOINT OWN closed-radius2 covers using
the130 freed U vertices. If such a coloring exists, all130 pins can be
assigned, the K6 target has10076 vertices/154530 edges, and each helper
prefix is valid. Its failure/UNKNOWN does not exclude U-only JOINT K6
completions that use another helper's B1 routes, F-pin repairs, another
layout, or general cap31 graphs. The same-column160>156 theorem is not
transferred to this changed geometry.

Pause this own-cover submodel here; retain masks, subset witnesses and the
specific compatible-route question for a future justified algorithm/rule
change. Do not rerun the same timer or start a hole/peer seed ladder.
The next selected production batch is the already audited, still untried
G1 role-copy endpoints90 and94, preserving progress in new parameter
instances while this small-parameter compatibility question remains open.

The new source/base and mask measurements add zero portfolio graphs,
parameters or Lean instances. The old full source was read for construction,
not reverified by source BFS/field/Steiner/cube/old Lean. Current counts
remain148named/39pairs/Lean42 at this disposition; later endpoint
acceptances, if any, are recorded separately. Public priority stays UNKNOWN.
