# Each subdivided external edge has only one short controller route

The stated prediction is supported on all240 saved cutpairs, not assumed from the initial proposal. CUT_PAIR_PREDICTION.json precedes the check; check_cut_pairs.py reads CASES.json only. Each of80 controllers has3 cutpairs, and every pair has exactly the single length2 path v_i-w_i-r_i and zero length3 walks. The test counts all length3 walks, not only nonbacktracking ones. CPU0.001872806 seconds; no new controller, lift, BFS, matrix search or solver was run.

## Bound source facts

In the actual30-controller, every vertex lies in one designated triangle and one externalC5. Each triangle meets three distinct externalC5s. The saved source NB3 table has zero on every directed adjacent slot, hence in particular on each selected external edge. For an adjacent pair, any length3 walk not backtracking would be counted there.

The selected external edge v_i-r_i is in no triangle. This also follows from the two-factor geometry: the oldtriangle of v_i meets three different C5s, while v_i and r_i lie on one C5; a common neighbor arising from an external edge or a triangle edge would violate either that separation or the fact the external component is an induced five-cycle within its own factor. Equivalently the saved actual triangle list is complete and all designated triangles are vertex-disjoint; the selected edge is not among them.

Because v_i-r_i is removed, a surviving old-only3walk between these endpoints could not use that edge. Such a walk in the old graph would be nonbacktracking: a backtrack in a length3 walk from v_i to r_i repeats the direct edge v_i-r_i. The original NB3 count is zero, so no old-only3walk remains.

## Structural proof for the new controller

The six chosen old endpoints v_0,r_0,v_1,r_1,v_2,r_2 are distinct, since the three cuts lie in different C5s. Each endpoint v_i and r_i therefore has precisely one neighbor in the new triangle, namely w_i.

A two-step path through an old middle vertex would already make a source triangle on the old external edge; there is none. The only new common neighbor is w_i. Thus the unique2path is v_i-w_i-r_i.

Consider a3walk with a new vertex in an internal position. Its old endpoints force an endpoint-adjacent new vertex to be w_i.

- If both internal positions are new, the walk would have form v_i-w_i-w_j-r_i. The last edge would require w_j=w_i because r_i has only one new neighbor; then the middle edge would be a forbidden selfloop.
- If only the first internal vertex is new, its next old vertex must be v_i or r_i, the only old neighbors of w_i. The final step would require respectively the deleted edge or a selfloop.
- The case with only the second internal vertex new is symmetric.
- A walk with no internal new vertex is an old-only walk, already excluded above.

Hence there is no3walk of any kind from v_i to r_i. These arguments apply to every choice in the complete80-setting rule and explain the observed(1 two-walk,0 three-walk) count for all240 cutpairs.

## Full lift obstruction, including arbitrary maps and offsets

Let q>1. Put q^3 vertices over each controller vertex, allow edges only over controller edges, and assume each fiber vertex has at most q neighbors across each incident controller edge. There are no additional edges inside a fiber or between nonadjacent controller fibers.

Fix any lifted vertex above v_i. Any walk of length<=3 to the fiber above r_i projects to a controller walk of that length. There is no direct edge and no length3 walk; the only possible projection is v_i-w_i-r_i. It has at most q*q=q^2 lifted endpoints. Since q^2<q^3, at least q^3-q^2 points in that target fiber remain outside R3.

This uses only branching counts, not linearity, a field characteristic, matrices, invertibility, projective directions, common affine centers, or zero offsets. It therefore excludes all q-point-per-arc affine-line maps and arbitrary affine offsets over these80 controllers, as well as arbitrary relations satisfying the same branching bound. It is strictly stronger than failure of a full-rank single-word certificate.

For the intended q4 target it prevents full64-point coverage of a cut target fiber; no2112-point lift was generated. It does not exclude arbitrary2112-point graphs, other controllers, extra internal-fiber edges, or rules with a different projected support.

## Consequence for any next controller surgery

Adding a new triangle between subdividing vertices can create routes between different cutedges, but cannot repair the endpoint pair of each individual edge when both old endpoints attach to the same unique subdividing vertex. Protecting all old controller pairs requires explicitly repairing these endpoint pairs as well.

A future rule must first supply a genuine length3 controller route between each cut pair, or enough distinct shorter routes to overcome the q^2 capacity limit. The same-vertex attachment topology above cannot do that merely by changing the internal graph on the new vertices. No such new rule has been generated or tested in this task.
