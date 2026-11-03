# HS58: two deleted original edges require at least six old additions

Date: 2026-10-12. This is a computer-assisted exclusion of a specified
augmentation family. It does not exclude arbitrary graphs on 58 vertices.

Let Q be the saved Hoffman–Singleton graph on fifty vertices. Delete exactly
two distinct original edges D, add a set A of original nonedges, and add eight
new vertices, with arbitrary edges among and to the new vertices. If the
resulting graph is eight-regular and has diameter two, then **|A| >= 6**.

The previous [four-addition closure](HS58_TWO_DELETE_FOUR_ADDITIONS_EXCLUSION.md)
and its recorded predecessors exclude |A| <= 4. We close |A| = 5 here.
Degree counting gives ten edges in the eight-vertex auxiliary graph H.

## Complete auxiliary domain and deletion geometries

The [five-addition construction report](HS58_TWO_DELETE_FIVE_ADDITIONS_CONSTRUCTION.md)
records the complete auxiliary classification: all 13,123,110 labeled
eight-vertex ten-edge graphs are screened by necessary endpoint-port budgets,
leaving 89 isomorphism types. Seventeen types require the adjacent-deletion
full-port branch, which the general adjacent full-port lemma excludes; five
have a universal vertex, excluded by
[the universal-H proof](HS58_TWO_DELETE_UNIVERSAL_H_EXCLUSION.md).
The remaining 67 exact representatives are saved without applying the
no-cross-only degree-sum reduction to other deletion geometries.

Every pair of distinct edges of Q lies in exactly one of three domains:

| Geometry | Number of deletion pairs | Representative |
| --- | ---: | --- |
| Adjacent | 1050 | {(0,1),(0,4)} |
| Disjoint, with an original edge between the two endpoint sets | 6300 | {(0,1),(2,3)} |
| Disjoint, without such an edge | 7875 | {(0,1),(10,11)} |

The total is 15,225 = C(175,2). The saved six explicit automorphisms cover
each domain in a single orbit, with all predecessor words saved. The
[remaining-orbit proof](HS58_REMAINING_DELETION_ORBITS.md) covers the first
two; the [no-cross exclusion](HS58_A5_NO_CROSS_DELETIONS_EXCLUSION.md) covers
the third, including its stronger 67-to-1 auxiliary reduction and checked
type-3 certificate. No assumption about the order of the automorphism group
is needed.

## Joint adjacent and cross formulas

For each of the first two representatives the actual encoding leaves all
1050 original-nonedge variables A and all 400 old-new variables B free.
It uses 28 auxiliary-edge variables and exactly one of 67 type selectors.
Each selected type fixes every auxiliary edge and nonedge. Every old and
new vertex has exact degree eight, and |A| is exactly five.

Every pair lacking an already fixed retained-Q path receives its direct-edge
alternative and every two-edge path through all 58 vertices. Both directions
of each AND definition are encoded. This includes paths through added old
edges, old-new edges, and two auxiliary edges. There are no saturated-endpoint,
matching, seed-neighborhood, or additional old-label restrictions.

An arbitrary target is transported by the inverse of its saved Q
automorphism word, then independently relabeled on its eight new vertices
to the canonical H. Because all A and B variables remain free, these maps
preserve the candidate and make the corresponding formula satisfiable.
This is the required direction of the reduction.

The actual source, metadata, inputs, logs and proof files are under
`computations/dd82/construction/hs58_a5_remaining_joint.py` and
`hs58_a5_remaining_joint_run/{adjacent,cross}/`. A separate agent read
the source and actual metadata, called cardinality helpers and result logs:
[encoding review](HS58_A5_REMAINING_JOINT_ENCODING_REVIEW.md).

| Geometry | Variables / clauses | Solver CPU | LRAT checker CPU | Result |
| --- | --- | ---: | ---: | --- |
| Adjacent | 39032 / 128174 | 19.536785 s | 0.981838 s | CHECKED_UNSAT |
| Cross | 39076 / 128308 | 7.061750 s | 0.254257 s | CHECKED_UNSAT |

Each had one 180-CPU-second attempt, 8 GiB address-space limit and 768 MiB
proof-output limit. Both returned before the limits. Each independent
`lrat-trim --no-trim` call named its actual saved CNF and LRAT file, returned
exit 20 and printed `s VERIFIED`. Encoding CPU was 0.162808 and 0.163293 s;
solver wall time was 20.110051 and 7.627698 s; checker wall time was
1.013988 and 0.279922 s. The two solver runs overlapped, so those wall times
must not be summed as elapsed research time. Neither run was restarted.

Combining these two checked contradictions with the no-cross exclusion
closes every deletion geometry at |A|=5. The earlier low-addition results
then establish the stated lower bound of six additions.

## Actual construction feedback and verification status

Before this closure the two remaining geometries also produced complete
58-vertex, 232-edge, eight-regular graphs, independently BFS-checked:
[seed report](HS58_A5_REMAINING_GEOMETRY_SEEDS.md). They have 94 and 72 bad
pairs, respectively, and diameter three. The cross seed improves the saved
bad-pair count within this construction work, but is not a valid target.
Its concrete port-capacity failure and the adjacent seed's broken old paths
are saved; neither failed example substitutes for the joint exclusion.

Root and independent-agent source/proof checks are complete for this
combination. The result is a locally checked mathematical/computational
claim, not a completed external Gemini review or Lean formalization.
The preceding external review requests exhausted their permitted retries
with authentication errors and supplied no verdict. There is no new claim
about arbitrary 58--61 graphs or a lower bound greater than 57.
