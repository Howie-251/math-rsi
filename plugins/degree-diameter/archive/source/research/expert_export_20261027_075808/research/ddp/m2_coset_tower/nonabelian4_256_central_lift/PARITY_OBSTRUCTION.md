# Central-lift obstructions from small path sets

A quotient target must be reached with both central bits. Counting two distinct base walks does not check this: the walks can induce the same affine central-bit form, and even two genuinely different forms can impose equations that conflict across targets. The cheap candidate-preserving test is therefore **joint GF2 consistency**, followed by propagation after restricting to its solution space.

This note concerns the fixed Q64 four-orbit K4 base with weights `01:3,02:3,03:2,12:2,13:3,23:3`. It supplies necessary conditions and a sufficient criterion for the special case where all unresolved slots have at most two distinct forms. It does not exhibit a new quotient-D3 counterexample in this particular family and does not claim that the abstract examples below have been realized by a tested quotient candidate.

## Coordinates and the exact local requirement

Let `c=(16,0)` generate the center of Q64. The quotient is D32 with rotations modulo 16. Use the canonical representative `h_e^0=(a_e,p_e)`, where `0<=a_e<16`, and write every lifted free-edge voltage as

`h_e=h_e^0 c^(z_e)`, with `z_e` in GF2.

The free-edge order is `[1,2,4,5,7,8,9,10,11,12,13,14,15]`; tree edges `[0,3,6]` have bit zero. For an oriented walk w, compute its canonical Q64 product using the true Q64 inverse for reversed edges. Its central bit is

`f_w(z)=alpha_w + v_w dot z`.

Here `alpha_w` is the rotation bit 4 of the canonical product, and `v_w` records occurrences of each free edge modulo two. Reversing an edge does not change its coefficient in v because c is central of order two. Repeated edge occurrences cancel in v when even. Their canonical-product contribution to alpha must still be computed correctly.

Group the walks of length at most three by `(root base vertex, target base vertex, quotient group element)`. There are 512 such slots over the four roots. For a slot s let F_s be its set of distinct pairs `(alpha,v)`. Exact duplicates are discarded; different base walks with the same pair do not give another possible central value.

The slot is covered in the Q64 lift exactly when

`{f(z): f in F_s} = {0,1}`.

With a reference form `f_0`, this is the clause

`OR_(f != f_0) [ (v_f+v_0) dot z = 1+alpha_f+alpha_0 ]`.

Zero quotient paths fail already at quotient reachability. One distinct affine form fails central coverage for every assignment. If F_s contains `(alpha,v)` and `(alpha+1,v)`, the slot is covered for every assignment. Two other distinct forms impose the single necessary and sufficient equation

`(v_1+v_2) dot z = 1+alpha_1+alpha_2`.

An arbitrary pair must **not** be selected and forced when a slot has three or more forms. For example `{0,u,v}` only requires `u OR v`; imposing `u=1` would lose valid assignments with `(u,v)=(0,1)`.

## Joint consistency and inexpensive propagation

Stack all two-form equations in one GF2 system `A z=b`. Also include original-graph simplicity constraints: two parallel base edges with the same canonical quotient voltage must have opposite lift bits,

`z_e+z_f=1`,

with a tree-edge bit interpreted as zero. Three such parallel edges are immediately impossible, since only two distinct full voltages lie over one quotient voltage; equivalently their three pairwise inequalities XOR to `0=1`.

Perform ordinary GF2 elimination. A row combination with zero coefficient mask and right-hand side one is an explicit obstruction to **every** central lift of this fixed quotient. This is valid field elimination because these are central bits, unlike the earlier Z/32 rotation-coordinate system.

If the system is consistent, write `z=z_0+B t` and reduce every remaining slot form to

`(alpha+v dot z_0) + (B^T v) dot t`.

Deduplicate again. A previously large path set may collapse to one or two effective forms. Reject a one-form slot, remove an automatically complementary slot, add any new two-form equation, and repeat. Every restriction follows from a necessary condition, so this propagation preserves all actual D3 lifts. At most 13 independent equations can be added. No new graph or root BFS is needed for this test.

If every slot is automatic or has at most two forms and the joint system is consistent, this condition is also sufficient for a D3 lift satisfying the parallel-edge simplicity conditions: any solution supplies both central values in every quotient slot from each of the four roots. In the general case, consistency of the forced subsystem is only necessary. The remaining clauses must still be checked by the full central-lift method.

One additional safe simplification is to test whether a slot's all-equal equations are inconsistent on the current solution space. Such a slot is automatically covered even without an explicit complementary pair. If they are consistent with codimension at least two, do not replace their disjunction by a chosen linear equation. This is the boundary between the inexpensive forced-equation stage here and the full bad-affine-subspace criterion handled separately.

## Precise obstruction mechanisms

These small systems explain what a path-count test leaves unchecked:

1. **Duplicate forms.** Two different walks yielding `{u,u}` always have one central value. The number of base walks is two but the number of affine forms is one.
2. **Conflicting two-form slots.** Slots `{0,u}`, `{0,v}`, and `{0,u+v}` require `u=1`, `v=1`, and `u+v=1`. XOR of the three equations is `0=1`. Every slot separately admits central coverage, and each has two genuinely different forms, but no common assignment covers all of them.
3. **Why forced-equation consistency is not a full solver.** Four slots with form sets `{0,u+a,v+b}`, one for each `(a,b)` in GF2^2, respectively forbid the four assignments `(u,v)=(a,b)`. Each slot has three forms, and none alone forces a nontrivial linear equation, but their conjunction is unsatisfiable.

Examples 1–3 are exact algebraic obstruction mechanisms at the lift interface, not claimed saved quotient-D3 candidates from the present K4 family. Thus this task has not settled the proposed walk-count sufficiency statement by producing an actual family counterexample. It does establish the additional conditions that any implementation must check before accepting a lift.

There is a concrete source of duplicate forms within the present Q64 path representation: a closed walk projecting to the quotient identity and its reverse have the same central value, because both possible full voltages, 1 and c, are self-inverse. Counting the two orientations as two independent central alternatives is wrong. The stored example below exhibits precisely this issue.

Conversely, a same-base path to a quotient odd element automatically supplies both lifts: in Q64 the inverse of an odd voltage differs by c, and reversing the path preserves its length. The same holds for a same-base quotient rotation of value 8, whose two lifts 8 and 24 are inverses. This shortcut does not apply to the quotient identity slot: its reversed paths have the same central value.

## Actual two-triangle example from the saved best

The parent supplied the complete closed-walk support **ending at c in the old full lift**: the two undirected triangle supports are `{2,7,12}` on base vertices 013 and `{9,11,15}` on 123. That list alone would not rule out additional walks projecting to the quotient identity but ending at the full identity e. The following saved independent evidence supplies this missing step.

`../nonabelian4_256_search/best.independent_check.json` records a simple 8-regular graph on 256 vertices, with all 256 roots checked, parameter expansion equal to the saved edges, and ordered distance-two count **14,336 = 256*8*7**. Each root has only `8*7=56` nonbacktracking walks of length two, so at most 56 distinct distance-two vertices. Equality of the sum forces equality at every root. Hence no such walk ends at a neighbor and no two end at the same distance-two vertex: the full graph has neither triangles nor four-cycles. Simplicity and full degree 8 also exclude coincident actual parallel-edge voltages. Therefore there is **no nonempty freely reduced closed walk of length at most three with full voltage e**. Immediate edge/reverse-edge backtracks do have value e, but reduce to the empty walk and give only its already counted constant-zero form.

A freely reduced base word projecting to the quotient identity has full voltage either e or c. The independent certificate excludes the nonempty e case, so the parent's complete list of c-ending words now supplies **all nonempty freely reduced quotient-identity supports** of length at most three. Root 0 has only the first triangle support, root 2 only the second; roots 1 and 3 have both. The empty walk is retained separately. Neither the c-path list nor the distance calculation was recomputed here.

Using `../nonabelian4_256_search/best.json`, I evaluated only the two specified canonical products:

- Darts `[4,24,15]`: `(10,0)(6,1)(16,1)=(16,0)`. Its central form is `1+z_2+z_7+z_12`; root 0 therefore forces **`z_2+z_7+z_12=0`**.
- Darts `[19,22,31]`: `(16,1)(1,0)(31,1)=(0,0)`. Its central form is `z_9+z_11+z_15`; root 2 therefore forces **`z_9+z_11+z_15=1`**.

Subscripts here are base-edge IDs. In the fixed 13-free-edge bit order the coefficient masks are respectively **530** and **4416**, with right-hand sides **0** and **1**. The empty walk supplies central bit zero in each identity slot, so covering its central antipode forces the respective triangle form to be one. Reversing a triangle supplies the same form, not a new alternative. The two equations also suffice for the center-antipode slots of roots 1 and 3, which can use both supports.

The stored full voltages satisfy both equations, and their two specified products are `(16,0)`. This demonstrates the actual forcing mechanism, not an inconsistency. The old quotient has diameter four, as established by the parent, so it is **not** a counterexample with a diameter-three quotient and is not a candidate for a central-bit search. No lift assignment was enumerated.

The exact two-product arithmetic and coordinate masks are saved in `PARITY_EXAMPLE.json`; it used 0.000214820 CPU seconds. This bounded task otherwise used paper reasoning and read existing parameters only. It performed zero phase-mask scans, zero base-walk reenumerations, zero candidate searches, zero generated graphs, and zero BFS roots.

## Implementation suggestion

Before any general central-bit search, canonicalize affine forms per slot, remove automatic slots, collect forced equations and duplicate-parallel-edge equations, and run the joint GF2 consistency/propagation pass. Save a zero-mask/right-hand-side-one combination when it fails. If complex clauses remain, pass the residual affine parameterization to the full lift checker rather than declaring success from quotient diameter or path multiplicity. This stage changes no authorized search scope and introduces no extra normalization.
