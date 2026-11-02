# Fixed multiplicity-six production: 166650 vertices, maximum degree 70

The complete `graph_d70_D3_n166650.edges` contains 166650 vertices and
5544000 edges. Its immutable source is the accepted 160050-vertex,
5121600-edge, 64-regular graph in `../graph_d64_D3_n160050.edges`.
The accepted 161150-vertex edge file and its neighborhoods were not read.
All 5121600 original source edges are retained.

The fixed base centers are the 22 cubic-coset points paired with the
original 50 spread lines. The point order is
`(1,t,t^3+k,-t^2)` for k=0,2,4 and t=0,...,6, then `(0,0,1,0)`;
the spread index j=0,...,49 varies inside each point. Base center
`50*i+j` has original source label `400*pointID[i]+spread[j]`.
`PARAMETERS.json` contains all 22 points, their source point IDs, the
original spread labels, and all 1100 base-center labels in order.
`BASE_CENTERS.json` binds every saved center field to that recipe.

Each base center is copied six times. With copy=0,...,5 outside the base
order, clone index `1100*copy+50*i+j` has label `160050+clone_index`.
Its only neighbors are the 64 literal neighbors of its base center in the
original 160050-vertex source. There is no new-to-new edge, and neighborhoods
are never taken from the evolving graph. This first copy has the accepted
65-degree recipe by the label formula, without rereading the 65-degree file.

The producer parsed all 5121600 literal source edges, checked strict simple
order and every source degree 64, and extracted all 1100 base neighborhoods.
Each was compared entry by entry with the frozen geometric formula. For a
flag center the raw self-pair is omitted and the actual original source
bonus owner is included. All 1100 literal neighborhoods contain 64 different
vertices. Their load is at most 1, and their union contains 70400 source
vertices. These are actual production checks, rather than assumptions from
the older graph's acceptance.

For every added clone the producer checked that each of its 64 pins had
received exactly `copy` previous clone edges. Those pins therefore change
degree from `64+copy` to `65+copy`. Each full copy layer visits every one
of the 70400 used pins exactly once. `PREFIX_LOADS.csv` records all 6600
steps, including labels, before/after pin degrees and accumulated new-edge
counts. At the final step, 70400 source vertices have added load 6 and
89650 have load 0. Every new vertex has degree 64. Hence the final degree
histogram is `64:96250,70:70400`, and

    m = 5121600 + 6600*64 = 5544000.

The 422400 added edge pairs were sorted, checked distinct, and merged with
every original source edge. Each emitted pair was checked to satisfy u<v
and strict lexicographic order. The complete output was closed before its
final filename was published.

Every current prefix has diameter at most 3 by actual short-walk lifting.
Collapse a clone to its original source center and an old vertex to itself.
For two endpoints with collapsed source vertices a,b, use the accepted
source's diameter-three bound. A source path of length 2 or 3 lifts by
replacing its first and last endpoints with the chosen old or new vertices;
the interior vertices remain in the original source. If a=b, any source
neighbor w gives a two-edge walk through old vertex w. This also handles
two copies of the same center. If a,b are adjacent, use the three-edge walk
through old vertices b,a. These walks remain within every prefix containing
their endpoints, including all previous clones. The center map need not be
injective, and the 231 adjacent base-center pairs cause no difficulty.
Equivalently, the next clone's pins cover the complete current prefix
within radius 2 by these walks. This is the existing generic full-source-
neighborhood clone argument, not 6600 literal current-R2 checks or BFS runs.

The complete graph therefore has diameter at most 3. Since 166650 exceeds
the elementary maximum-degree-70 diameter-two bound `1+70+70^2=4971`, its
diameter is exactly 3, subject to independent acceptance of the complete
literal binding. No new diameter claim is inferred from an untested root
histogram.

The additional falsifiable prediction in `PRED.json` remains untested by
this producer. It predicts 132 new roots with distance counts
`1,64,3191,163394` and 6468 with `1,64,3254,163331`. Each clone has five
other copies of its center at distance 2; clones of distinct base centers
have no shared source neighbor and are at distance 3 by the preceding
walk argument. The predicted exact old-vertex layer counts are for the
fresh independent checker to verify, and are not reported here as observations.

`PRED.json` preceded production. The one worker used 2.180334343 measured
CPU seconds including preparation, compilation and the sole production
run, below the 30-second budget. Compilation used 1.169502 CPU seconds;
the producer child used 0.994703 CPU seconds. `BUILD_RUN.json`,
`RESULT.json` and `TERMINAL.json` give the actual result and terminal state;
`produce.cpp` and `run_production_once.py` give the complete production code.
There was no BFS, solver, Lean compilation, install or hash operation.
Fresh independent full-file acceptance and a concrete Lean instance are
separate root tasks. Accepted counts, original graphs, caches, Wiki and
STATE were not changed by this producer. The root's bounded public
comparison located 164500; global-record status and priority remain pending.
