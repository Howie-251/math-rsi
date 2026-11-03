# Two explicit HS58 seeds and the cancelled completion calls

Date: 2026-10-12. This record concerns the actual HS50 labeling supplied by
`hs_augmentation.base()`, with

\[
D=\{01,10\!:\!11\},\qquad A=\{25\!:\!26,35\!:\!41,2\!:\!4\}.
\]

Here a colon only separates the endpoints of an edge. Let the modified old
graph be \(M=Q-D+A\). The two auxiliary graphs are types 2 and 3 of
[the auxiliary-domain note](HS58_TWO_DELETE_THREE_ADDITIONS_AUXILIARY_DOMAIN.md).
Their labels are \(0,\ldots,7\), expanded to vertices \(50,\ldots,57\).
The center of their bad-pair star is \(u=3\) and \(u=1\), respectively.
Fix

\[
B_0=\{u,4\},\quad B_1=\{u,5\},\quad
B_{10}=\{u,6\},\quad B_{11}=\{u,7\}.
\]

The six endpoints of \(A\) have no new neighbors; the remaining 40 old
vertices have one each. After the fixed double ports, the required singleton
column capacities are respectively

\[
(2,5,6,3,6,6,6,6),\qquad(2,2,6,6,6,6,6,6).
\]

The generator pairs the sorted singleton vertices with the sorted list of
colors repeated to these capacities. It performs no optimization. Both
expanded seeds are simple graphs on 58 vertices with 232 edges and degree
eight at every vertex. The independent BFS verifier reports diameter three
and **106 bad pairs for each seed**. Every bad pair, its distance, and its
empty common-neighbor set are saved in the corresponding verification JSON.
These seeds are failed constructions, not target graphs.

## A fixed-core obstruction visible in actual labels

The actual old neighbors of vertex 0 in \(M\) are

\[
N_M(0)=\{4,25,30,35,40,45\}.
\]

Vertices 4,25,35 have zero ports. Vertices 30,40,45 have singleton ports.
For every \(t\in\{30,40,45\}\), the pair \(1,t\) is nonadjacent in \(M\)
and has no common old neighbor, as directly checked from the saved old
edge set. In any successful completion, this old pair must therefore share
a new neighbor. Consequently its singleton color satisfies
\(B_t\subseteq B_1=\{u,5\}\).

Now consider length-at-most-two routes from old vertex 0 to the new bad-star
leaves \(4,5,6,7\). Its direct attachment reaches leaf 4. A route through an
old neighbor reaches at most leaf 5, because the other three old neighbors
have no ports. A route through either of its two new neighbors \(u,4\)
reaches none of the other three bad-star leaves: in both auxiliary graphs
\((N_H(u)\cup N_H(4))\cap\{4,5,6,7\}=\varnothing\).
Thus new vertices 56 and 57 cannot be reached from 0 within two steps.

This contradicts complete coverage for the stated fixed old core and
double-port assignment, independent of all 40 singleton choices and their
column capacities. The deterministic seeds choose colors 6 and 7 at old
vertices 40 and 45 instead; their actual failed pairs include \((1,40)\)
and \((1,45)\), both at distance three. The saved witness records this
tradeoff explicitly.

The planned two attachment SAT calls were cancelled **before either was
started** following this analytic obstruction. No CNF, solver result, or
UNSAT certificate is claimed. The broader two-deletion/three-addition
argument is separate; this record itself proves only the fixed-core scope
specified above.

## Artifacts and actual resources

- [Generator](../../../computations/dd82/construction/hs58_two_delete_three_add_seeds.py).
- [Run result](../../../computations/dd82/construction/hs58_two_delete_three_add_seeds_run/result.json).
- [Type 2 complete seed](../../../computations/dd82/construction/hs58_two_delete_three_add_seeds_run/type2/seed.json),
  [edge list](../../../computations/dd82/construction/hs58_two_delete_three_add_seeds_run/type2/seed.edges),
  [full BFS result](../../../computations/dd82/construction/hs58_two_delete_three_add_seeds_run/type2/seed.verification.json),
  [failure witness](../../../computations/dd82/construction/hs58_two_delete_three_add_seeds_run/type2/failure_witness.json).
- [Type 3 complete seed](../../../computations/dd82/construction/hs58_two_delete_three_add_seeds_run/type3/seed.json),
  [edge list](../../../computations/dd82/construction/hs58_two_delete_three_add_seeds_run/type3/seed.edges),
  [full BFS result](../../../computations/dd82/construction/hs58_two_delete_three_add_seeds_run/type3/seed.verification.json),
  [failure witness](../../../computations/dd82/construction/hs58_two_delete_three_add_seeds_run/type3/failure_witness.json).

Generation and the small direct witness checks used 0.004991111 parent CPU
seconds; the two independent BFS subprocesses used 0.059038 CPU seconds.
Total measured wall time was 0.070688259 seconds. Solver runs and solver CPU
time were both zero. No graph search was performed and no job remains active
from this task.

## Deterministic refinement covering every old-old pair

The subsequent authorized refinement kept both initial seeds unchanged and
solved only a small bipartite capacity-matching problem. The actual modified
old graph has 16 bad old-old pairs. Two are the deleted edges themselves,
whose endpoint ports already intersect in \(u\). The other 14 have one
singleton endpoint and one fixed double-port endpoint; there are no bad
old pairs involving a zero-port endpoint or two singleton endpoints.

For each singleton old vertex \(w\), intersect the fixed sets \(B_y\) over
these bad pairs \((w,y)\). This gives its allowed color domain, or all eight
colors if there is no constraint. These constraints are equivalent to full
old-old coverage for this actual core and the prescribed double ports.
Each required color-capacity unit is then treated as a right vertex of a
bipartite graph. A deterministic alternating-path matching covers all 40
singleton vertices in both auxiliary cases, while using every capacity
unit exactly once.

The two additionally expanded graphs retain 58 vertices, 232 edges, and
degree eight everywhere. Independent BFS gives:

| Auxiliary type | Bad old-old pairs | Bad new-new pairs | Bad old-new pairs | Diameter |
|---|---:|---:|---:|---:|
| 2 | 0 | 0 | 83 | 3 |
| 3 | 0 | 0 | 82 | 3 |

Both have the predicted actual failures \((0,56)\) and \((0,57)\), with
distance three and no common neighbor. These remain failed constructions;
the capacity matching is neither a search over graph neighborhoods nor an
attempt to minimize their remaining bad pairs.

The [refinement source](../../../computations/dd82/construction/hs58_two_delete_three_add_old_cover.py)
and [result](../../../computations/dd82/construction/hs58_two_delete_three_add_seeds_run/old_cover/result.json)
save all 16 old bad pairs, their classifications, every allowed domain,
capacities, and final singleton assignments. Complete expanded objects are
saved for
[type 2](../../../computations/dd82/construction/hs58_two_delete_three_add_seeds_run/old_cover/type2.seed.json)
and
[type 3](../../../computations/dd82/construction/hs58_two_delete_three_add_seeds_run/old_cover/type3.seed.json),
with corresponding `.edges` and `.verification.json` files containing the
entire edge sets and independent BFS witnesses.

The one-second parent CPU limit was respected: actual parent CPU was
0.005170480 seconds, independent BFS child CPU was 0.060285 seconds, and
wall time was 0.069039065 seconds. No SAT call was made. The broader analytic
closure is recorded separately in
[HS58_TWO_DELETE_THREE_ADDITIONS_EXCLUSION.md](HS58_TWO_DELETE_THREE_ADDITIONS_EXCLUSION.md);
these fixed-label examples are nonessential illustrations of its coverage
obstruction.
