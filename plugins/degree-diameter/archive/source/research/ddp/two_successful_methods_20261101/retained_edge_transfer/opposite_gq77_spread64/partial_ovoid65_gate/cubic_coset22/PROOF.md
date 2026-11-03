# Produced fixed 161150-vertex graph: formula and producer evidence

The completed `graph_d65_D3_n161150.edges` has 161150 vertices and 5192000
edges. It retains the entire accepted 160050-vertex, 5121600-edge,
64-regular source and appends 1100 vertices. Clone `160050+i` is adjacent
exactly to the 64 neighbors of `CENTERS.json[i].center` in the immutable
160050-vertex source. There is no clone-to-clone edge. The original source
center order is k=0,2,4, then t=0,...,6 within each k, then infinity;
each point is paired with the original 50 spread indices in order.

The algebraic set consists of `(1,t,t^3+k,-t^2)` for those three offsets,
and `(0,0,1,0)`. For the source alternating form with nonzero factor 2
removed, pairing two finite points gives `(t-s)^3+(l-k)`. Cubes are
0,1,6; distinct offset differences are 2,3,4,5. Distinct finite points
therefore never have zero pairing, and their pairing with infinity is 1.
The one finite precheck also verified all actual point/line incidences and
all 604450 pairs of the 1100 source neighborhoods. The partial-ovoid
condition and spread uniqueness are exactly the hypotheses used by the
existing `OvoidSpreadCloneCapacity.load_le_one` lemma.

The producer subsequently read every one of the 5121600 literal source
edges, checked its simple strict order and every source degree 64, and
extracted the complete literal neighborhoods of the 1100 saved centers.
Each sorted literal neighborhood equaled its expected formula neighborhood.
The formula includes the actual source bonus vertex for a flag center,
in place of its raw self-pair. The table preparation checked all 1100 saved
center rows against the frozen geometry, point order and spread order.
Thus the new edges use the accepted source's actual neighborhoods, rather
than an evolving neighborhood or a differently ordered recipe.

The 70400 new edges load exactly 70400 distinct source vertices once each;
the other 89650 source vertices receive no new edge. Hence old degrees
are 65 at 70400 vertices and 64 at 89650 vertices. Every new vertex has
degree 64. The complete graph degree histogram is consequently
`64:90750,65:70400`. Its edge count is `5121600+1100*64=5192000`.
The producer sorted the added pairs and merged them with every original
source pair, checking strict lexicographic `u<v` order while writing.
It closed the complete file before publishing its final name.

For the diameter bound, collapse every clone to its source center and fix
two resulting source endpoints a,b. If a=b, a source neighbor w gives a
two-edge walk from either lifted endpoint through old vertex w to the other.
If a,b are adjacent, the old vertices b,a give the three-edge walk
`lift(a),b,a,lift(b)`. If the source distance is 2 or 3, keep the internal
source vertices and replace the first and last endpoints by their lifted
vertices; both required end edges exist by the full-neighborhood rule.
This covers old and new endpoints alike. The accepted source has diameter
at most 3 and no isolated vertex, so every new point pair has distance at
most 3. This is the existing `FullNeighborhoodClones.diameterAtMost`
argument; it does not assume independent centers. In particular the 231
K2 components among centers require no edge between clones. The order
161150 exceeds the elementary diameter-two bound `1+65+65^2=4291`, so
the diameter is exactly 3.

`PRED_PRODUCTION.json` preceded the run. `BUILD_RUN.json` measures
2.032453389 total CPU seconds, including preparation, compilation and
production, below the 60-second budget on one worker. Compilation used
1.125590 CPU seconds and the producer child used 0.897069 CPU seconds.
The actual producer result and final terminal state are in `RESULT.json`
and `TERMINAL.json`; the complete source is `produce.cpp` with its one-run
driver `run_production_once.py`. Production ran once, without BFS, solver,
Lean compilation, installation or hashes. Fresh independent complete-file
readback and any concrete Lean instance remain root-owned tasks; producer
PASS is not an independent acceptance or a certified global record.
