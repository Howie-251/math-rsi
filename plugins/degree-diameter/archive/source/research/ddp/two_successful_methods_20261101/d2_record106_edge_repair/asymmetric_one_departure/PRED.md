# One departure from the source C7 pin-set shape

Recorded before the only process starts. The prior invariant-pin-set paper
obstruction motivates two new, fixed noninvariant S11 shapes:

* A: remove min(O) from a seven-orbit O and add five fixed vertices:
  14*C(8,5)=784 representatives.
* B: take O, three fixed vertices, and min(Q) from another free orbit Q:
  14*C(8,3)*13=10192 representatives.

The verified source C7 action justifies these representatives. It imposes no
invariance on the internal rewiring. Total10976, with no further pattern,
phase, source or timer. Prediction: this smallest change of orbit shape may
produce a pin set passing closed domination and frozen-cross-degree bounds;
actual private-route and degree constraints may still rule it out. A found
solution must be returned as a complete107-vertex candidate for fresh root
acceptance, not silently counted as a new graph.

For fixed S only old G[S] changes; add z adjacent exactly to S. Each selected
v has a_v frozen outside neighbors and new internal degree between
L_v=max(0,9-a_v) and U_v=10-a_v. A selected-v/outside-u pair is already safe
if its frozen direct edge or a common outside neighbor exists. Otherwise
require an internal edge v-w to some w in S intersect N_G(u). Both-selected
pairs use z; both-outside old routes retain their two edges even when the
middle is selected. z-to-outside requires source closed domination. Thus
these positive coverage clauses plus degree bounds are exact for this rule.

Only propagation and a bounded finite DFS on55 internal edges are allowed.
Propagate coverage units, upper-degree saturation, lower-degree impossibility,
and forced remaining lower-degree edges. Global node cap200000. Stop at the
first candidate, or on total CPU/node cap. Unvisited/unsolved representatives
remain UNKNOWN. Exhaustive NO is allowed only if all10976 representatives
are rejected by exact gates or fully explored finite trees.

Prior case CPU10.711203943/20. This single-worker batch has at most6 CPU
seconds including imports, input preparation, compilation, failures, search
and receipt writing. No old6253-variable MILP, solver, graph-distance BFS,
source D2/common-neighbor full verification, automorphism search/refinement,
field/rank/Lean, web, graph changes outside the returned candidate, or root
and Wiki modifications.
