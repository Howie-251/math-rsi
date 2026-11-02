# HS58: the auxiliary domain at two deletions and four additions

Date: 2026-10-12. This completed finite screen concerns exactly two
original HS50 edge deletions, exactly four original-nonedge additions
among the old vertices, and eight new vertices. It provides a complete
necessary domain for the new-vertex graph H, consisting of eleven
isomorphism types. It does not test or assert an HS completion of any
type. The earlier
[three-addition exclusion](HS58_TWO_DELETE_THREE_ADDITIONS_EXCLUSION.md)
was read as prior evidence and was not recomputed.

## Candidate-preserving conditions

Write r_x for the old deleted degree and a_x for the added degree at
an old vertex x. An order-58 graph of maximum degree eight and diameter
two is eight-regular, so its new-neighbor port count is

\[
p_x=1+r_x-a_x,\qquad \sum_xp_x=50+4-8=46.
\]

The eight new vertices therefore induce exactly (64-46)/2=9 edges.
Let K(H) have as edges all unordered pairs whose H-distance exceeds
two, including disconnected pairs. Each such pair needs a common old
neighbor. Only endpoints of the two deleted edges can have more than
one new neighbor. Consequently the following tests preserve every
possible completion:

* For disjoint deletions, K(H) must be covered by four cliques of order
  at most two. At the auxiliary-only level this is exactly b<=4, where
  b=|E(K(H))|.
* For adjacent deletions, K(H) must be covered by one clique of order
  at most three and two cliques of order at most two. At this level it
  is exactly the existence of a three-element set U containing at
  least b-2 edges of K(H). In particular b<=5, but that count alone
  is not the test.

The program applies the latter condition to all 56 three-element sets.
It does not assume that every surviving abstract port cover embeds in
HS50, and it does not impose additional old-core or attachment rules.

## Complete enumeration and exact isomorphism compression

The source
[hs58_two_delete_four_add_auxiliary.cpp](../../../computations/dd82/construction/hs58_two_delete_four_add_auxiliary.cpp)
visits every nine-edge subset of the 28 possible pairs on labeled
vertices 0,...,7, in increasing bit-mask order. There is no degree,
topology, or symmetry pruning of this input domain. Each graph's full
set K(H) is computed directly from its adjacency rows and their unions
over neighbors.

The environment had no nauty/geng installation. For each previously
unseen surviving isomorphism type, the program instead generates all
8!=40,320 vertex permutations and records every resulting labeled
graph in that type's orbit. A subsequent surviving graph is classified
by membership in those explicitly generated orbits. Thus two graphs
are merged exactly when a vertex permutation identifies them. This
does not use the unicyclic AHU procedure from the earlier eight-edge
screen. The first encountered member of an orbit has the minimum
edge-mask encoding because the enumeration order is increasing.

The run checks orbit-size times automorphism-group-order equals 40,320
for every type. On complete termination it also checks each orbit size
equals its observed labeled multiplicity, and that the orbit union
equals the entire surviving labeled domain.

Actual output files are:

* [enumeration.json](../../../computations/dd82/construction/hs58_two_delete_four_add_auxiliary_run/enumeration.json):
  completion status, all counts, the full bad-pair histogram, and all
  representative data.
* [representatives.json](../../../computations/dd82/construction/hs58_two_delete_four_add_auxiliary_run/representatives.json):
  a reusable copy of the eleven final representatives, with all edges,
  all bad pairs, degree sequences, both compatibility flags, actual
  labeled multiplicities, and adjacent-budget cover witnesses.
* [resources.json](../../../computations/dd82/construction/hs58_two_delete_four_add_auxiliary_run/resources.json)
  and [compilation.json](../../../computations/dd82/construction/hs58_two_delete_four_add_auxiliary_run/compilation.json):
  separately measured resources for the screen and compilation.
* [hs58_two_delete_four_add_auxiliary_run.py](../../../computations/dd82/construction/hs58_two_delete_four_add_auxiliary_run.py):
  the launcher, pinning one CPU, with an internal 9.8-CPU-second stop
  and OS CPU limits of 10/11 seconds for the screen.

The one screen completed all binom(28,9)=6,906,900 inputs, reporting
complete=true and stop_reason=complete_domain. Both deletion budgets
retained exactly the same 48,160 labeled graphs, comprising eleven
isomorphism types. Screen CPU time was 0.878992 seconds and wall time
0.884967 seconds, with exit code zero. Compilation separately used
0.975041 CPU seconds and 0.984025 wall seconds. No additional graph
enumeration, solver, or optimization was run. The optional streamed
enumeration.representatives.jsonl contains discovery-time snapshots;
its then-zero accumulated multiplicities are not the final counts.
Use either final JSON file above for assembly or counts.

## Eleven explicit auxiliary types

All representatives use labels 0,...,7. An expression ij denotes the
unordered edge {i,j}. Every row passes both deletion-pattern budgets.

| ID | All nine edges of H | Degrees in label order | All bad pairs | Labeled multiplicity |
|---|---|---|---|---:|
| 1 | 01,02,03,04,05,06,07,12,13 | 7,3,2,2,1,1,1,1 | none | 840 |
| 2 | 01,02,03,05,06,07,12,13,14 | 6,4,2,2,1,1,1,1 | 45,46,47 | 3360 |
| 3 | 02,03,04,05,06,07,12,13,14 | 6,3,2,2,2,1,1,1 | 15,16,17 | 1120 |
| 4 | 01,02,03,06,07,12,13,14,15 | 5,5,2,2,1,1,1,1 | 46,47,56,57 | 2520 |
| 5 | 01,02,04,05,06,07,12,13,23 | 6,3,3,2,1,1,1,1 | 34,35,36,37 | 840 |
| 6 | 01,02,03,04,05,06,07,14,23 | 7,2,2,2,2,1,1,1 | none | 840 |
| 7 | 01,02,03,05,06,07,12,14,23 | 6,3,3,2,1,1,1,1 | 34,45,46,47 | 6720 |
| 8 | 01,03,04,05,06,07,12,14,23 | 6,3,2,2,2,1,1,1 | 25,26,27 | 6720 |
| 9 | 01,02,03,04,06,07,14,15,23 | 6,3,2,2,2,1,1,1 | 25,35,56,57 | 10080 |
| 10 | 02,03,04,05,06,07,14,15,23 | 6,2,2,2,2,2,1,1 | 12,13,16,17 | 5040 |
| 11 | 03,04,05,06,07,12,14,15,23 | 5,3,2,2,2,2,1,1 | 16,17,26,27 | 10080 |

Types 1 and 6 have universal vertex 0. Their two extra leaf edges are
incident or disjoint, respectively; together they represent 1,680
labeled graphs. Types 2,3,8 have bad graph K1,3, centered at labels
4,1,2 respectively, and represent 11,200 labeled graphs. Types 5,7,9,10
have bad graph K1,4, centered at labels 3,4,5,1 respectively, and
represent 22,680 labeled graphs. Types 4 and 11 have bad graph C4 and
represent 12,600 labeled graphs.

Among all 6,906,900 inputs there are 89,040 graphs with exactly five
bad pairs. None passes the adjacent-deletion cover test. The final
coincidence of the two surviving domains is a result of the complete
screen, not an assumption that the two budget tests are equivalent
for arbitrary auxiliary graphs.

## Immediate port consequences for the four-bad-pair types

For types 4,5,7,9,10,11, the bad graph is triangle-free with four
edges, either C4 or K1,4. Under disjoint D all four endpoint cliques
must cover one distinct required pair, so every deletion endpoint has
its full two ports. Under adjacent D a three-vertex clique covers at
most two required pairs because the bad graph is triangle-free. The
other two endpoint cliques each cover at most one. Covering all four
therefore forces full port counts 3,2,2, with no required-pair overlap
between the three covers.

In either deletion pattern p_x=1+r_x at every deletion endpoint,
hence no addition touches one. At every other old vertex, r_x=0 and
nonnegative p_x=1-a_x forces a_x<=1. Thus in all six four-bad-pair
types, the four added old edges must form a matching entirely outside
the endpoints of D.

For the K1,4 types, all deletion endpoint port sets contain the bad
star's center. In the disjoint case they pair it with its four leaves
bijectively. In the adjacent case the deleted-edge center carries it
and two leaves, and the other endpoints carry the remaining two
leaves separately. For a C4 type with adjacent D, the three-port set
must cover two adjacent edges of the bad cycle; the other two port
sets cover its remaining edges. These are concrete necessary patterns
for old-core assembly. The K1,3 types have a spare pair slot, so this
full-port conclusion has not been imposed on them.

No type in this new four-addition domain is excluded by this screen.
An HS completion still has to satisfy every old-old, old-new, and
new-new distance condition with the actual edited old graph.
