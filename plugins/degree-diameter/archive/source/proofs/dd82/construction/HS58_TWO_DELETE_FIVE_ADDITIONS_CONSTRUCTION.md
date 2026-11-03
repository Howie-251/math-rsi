# HS58 two-delete/five-add construction step and the type-14 query

Date: 2026-10-12. One complete addition-switch pass produced actual
58-vertex, 232-edge, eight-regular graphs in 22 of the 67 retained
auxiliary types. The best has 74 bad pairs and diameter three, so no
target graph was found. One subsequent full joint query for the
actual type-14 auxiliary graph returned **checked UNSAT**, with only
the two HS deletions and that auxiliary graph fixed.

## Concrete generation domain

The input was exactly the 40 saved complete graphs in
[the a4 switch result](../../../computations/dd82/construction/hs58_two_delete_four_add_switch_run/result.json).
For each input, the program exhausts switches

\[
\{x(50+a),y(50+b)\}\longmapsto\{xy,(50+a)(50+b)\},
\]

where x,y are distinct old vertices, a,b distinct new vertices, xy
is an original HS nonedge absent from the input, and ab is absent
from H. Thus each output still has exactly the original deleted
edges D={(0,1),(10,11)}, now five old nonedge additions, and ten H
edges. Every degree remains eight.

The program encountered 25,373 valid switches. Of these, 23,582
belong to the 67 isomorphism types retained by the existing a5
mathematical screen. An exact eight-vertex graph isomorphism maps
each admitted H to its stored representative; the actual map is
saved with every selected complete graph. This is a classification
of generated H graphs, not another auxiliary-domain enumeration.

The constructed type IDs are
2,3,7,8,9,11,12,13,14,19,20,25,26,27,28,35,36,50,53,54,59,60.
The output keeps each type's best graph and, when different, its
best graph that already covers all old-old pairs. There are 27
saved full edge tables. The independent adjacency-list BFS verifier
read every saved graph, checked all degrees are eight, and saved
every bad pair and its exact distance. All 27 have diameter three.

Artifacts:

* [Switch source](../../../computations/dd82/construction/hs58_two_delete_five_add_switch.py).
* [Complete counts, maps, sources, and resources](../../../computations/dd82/construction/hs58_two_delete_five_add_switch_run/result.json).
* [Best complete graph, type 54](../../../computations/dd82/construction/hs58_two_delete_five_add_switch_run/type54.best.json)
  and its [independent BFS](../../../computations/dd82/construction/hs58_two_delete_five_add_switch_run/type54.best.verification.json).

## The best graph's concrete failure

The type-54 graph has 74 bad pairs, all old-new; every old-old and
new-new pair is already within distance two. Its five old additions
are

```
(2,4), (3,16), (5,24), (25,26), (35,41).
```

This fixed old core cannot be repaired by changing attachments
alone. Old vertex 3 has zero ports and old neighbors
{2,4,16,28,33,38,43,48}. Their port counts are
0,0,0,1,1,1,1,1, summing to five. Since 3 has no new neighbor,
it can reach at most five new vertices by any attachment assignment
with this old core, instead of the required eight. Five other zero
vertices have analogous strict port-sum deficits.

The saved
[failure analysis](../../../computations/dd82/construction/hs58_two_delete_five_add_switch_run/type54.best.analysis.json)
contains all zero-row capacity witnesses, exact direct/old/new route
label sets at every old vertex, and all old pairs repaired through
the current attachments. The
[analysis source](../../../computations/dd82/construction/hs58_two_delete_five_add_analysis.py)
also records these data for the selected type-14 seed.

A stronger, separate analytic observation prevented a needless
type-54 solver query. The two deleted edges have no Q cross-edge
between their endpoints. H's three bad pairs form a star with center
u and three leaves L, and H[L] has only one edge. Covering three bad
pairs forces at least three deletion endpoints to have full pairs
{u,a}. One deleted edge therefore has both endpoints full, with
different leaves a,b and a third required leaf c elsewhere. Both
full endpoints have no added incident edge. Every positive ordinary
retained neighbor of either endpoint must have its label in the
deleted partner's port pair, to repair the old unique path destroyed
by the deletion. There is no other deletion-endpoint Q neighbor.
Hence the endpoints can reach c only through H edges ac and bc.
This needs two edges in H[L], a contradiction. No type-54 CNF or
solver run was launched: its query CPU use is zero.

## One joint type-14 completion query

The chosen complete seed is
[type14.old_covered.json](../../../computations/dd82/construction/hs58_two_delete_five_add_switch_run/type14.old_covered.json).
It has 79 bad pairs, all old-new. Its fixed old core has several
zero-row capacity bounds equal to seven rather than eight. The
query therefore leaves every original-nonedge addition and every
attachment free, instead of freezing these failed additions.

The only structural choices fixed in this query are the actual HS
labeling, D={(0,1),(10,11)}, and the following labeled H:

```
01,02,04,05,06,07,12,13,34,35.
```

This is a5 catalog type 14. The CNF has all 1,050 possible old
nonedge additions and all 400 old-new edges as primary variables.
It enforces exactly five additions, degree eight at all 58 vertices,
and distance at most two for every pair. There is no label
normalization and no mathematical shortcut used as an extra clause.

Of the 1,653 unordered vertex pairs, fixed edges already cover 1,225.
The CNF explicitly imposes the remaining 26 old-old, 400 old-new,
and two new-new requirements. All path conjunctions are defined in
both directions. The final input has 33,345 variables and 105,994
clauses.

A proposed blanket bad-pair degree-sum shortcut was withdrawn before
this query: a deleted partner can carry added edges, which can repair
some broken old paths and invalidate a naive restriction of all
neighbor labels to its port set. That unproved shortcut was neither
used to filter the construction pass nor encoded in the CNF. Any
subsequent repaired mathematical argument is independent of this
certificate.

CaDiCaL returned UNSAT, and the existing LRAT checker returned
`s VERIFIED` with exit code 20. The result excludes all choices of
the five old additions and all attachments for **this exact fixed
D and H**. It does not exclude arbitrary positions of D, all HS
automorphism orbits, every type-14 completion, or the whole a5 family.

* [Joint source](../../../computations/dd82/construction/hs58_two_delete_five_add_joint.py).
* [Exact encoding and variable maps](../../../computations/dd82/construction/hs58_two_delete_five_add_joint_run/encoding.json).
* [CNF](../../../computations/dd82/construction/hs58_two_delete_five_add_joint_run/input.cnf),
  [LRAT proof](../../../computations/dd82/construction/hs58_two_delete_five_add_joint_run/proof.lrat),
  and [verification log](../../../computations/dd82/construction/hs58_two_delete_five_add_joint_run/certificate_check.log).
* [Solver and checker result/resources](../../../computations/dd82/construction/hs58_two_delete_five_add_joint_run/result.json).

## Actual resources and construction obligation

The construction pass was pinned to one CPU. Search and H mapping
took 1.965040 CPU seconds and 1.984082 wall seconds. Total parent
CPU including output preparation was 2.013054 seconds; independent
BFS children used 0.780212 CPU seconds. The complete generation and
verification wall time was 2.859878 seconds. Concrete failure
analysis used 0.004779 CPU seconds.

CNF preparation used 0.140697 CPU seconds and 0.156334 wall seconds.
The single query had a 20 CPU-second, 4 GiB memory, 128 MiB proof-file
budget. Actual solver use was 1.902329 CPU seconds and 1.970385 wall
seconds. LRAT verification used 0.083424 CPU seconds and 0.086262
wall seconds. There was no rerun and no retained solver state.

The concrete next assembly obligation is to choose an old core whose
zero-port vertices each have at least eight incident neighbor ports,
while simultaneously repairing every old pair whose unique HS route
was deleted. These are necessary constraints on the additions before
color assignment; satisfying old-old coverage in a complete seed
alone did not ensure adequate old-new coverage. Further narrowing by
subsequent mathematics or a newly authorized residual query must be
recorded separately, without changing this completed experiment's
input or scope.

The later repaired no-cross argument and the separately authorized
type-3 residual query are recorded in
[HS58_TWO_DELETE_FIVE_ADDITIONS_TYPE3_JOINT.md](HS58_TWO_DELETE_FIVE_ADDITIONS_TYPE3_JOINT.md).
That additional input and certificate are separate from the completed
type-14 run above.
