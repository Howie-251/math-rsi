# HS58 a=4 joint encoding: read-only scope and preservation check

Date: 2026-10-12. The read-only review found no candidate-preservation
gap in
[hs58_two_delete_four_add_joint.py](../../../computations/dd82/construction/hs58_two_delete_four_add_joint.py).
No generator, solver, certificate checker, or auxiliary enumeration
was rerun for this review.

## Exact scope

The original old graph is the 50-vertex HS graph from hs_augmentation.base.
The deleted original edges are fixed to {(0,1),(10,11)}. The fixed
auxiliary graph, on local new labels 0,...,7, has edges

\[
02,03,04,05,06,07,12,13,26.
\]

Its local label a denotes global vertex 50+a. This is catalog type 8:
the canonical representative maps to this labeling by
(0,1,2,3,4,5,6,7) -> (0,2,1,3,6,4,5,7).
Its bad pairs are 14,15,17 in the actual local labeling.

The encoded family allows every choice of exactly four original
nonedges to add and every old-new attachment set, subject to the
required graph properties. It fixes neither seed additions nor seed
attachments. The source reads only the seed's deletion and auxiliary
edge lists; normalization is empty. The conclusion is confined to
this fixed D and labeled H. No orbit argument covering other deletion
placements or auxiliary types is asserted here.

## Primary variables and degrees

The actual encoding.json contains 1,050 addition variables, exactly
the complement of the 175 original HS edges among the binom(50,2)
old pairs. It contains all 400 attachment variables in a 50 by 8 array.
The 1,450 primary IDs are distinct and exactly 1,...,1450. These
facts were checked against the saved metadata without regenerating
the encoding.

The edge function returns true on the 173 retained original edges,
false on the two deleted original edges, the corresponding variable
on every original nonedge, and the corresponding B variable on every
old-new pair. In particular, an original deleted edge cannot be
reintroduced as an addition. New-new edges are exactly the fixed H.

For old vertex x the exact-cardinality equation is

\[
\sum_{y:xy\notin E(HS)} A_{xy}+\sum_a B_{xa}
 =8-d_{HS-D}(x)=1+d_D(x).
\]

Thus addition endpoints and their reduced port budgets are handled
jointly, including additions touching deletion endpoints. Each new
column has exact sum 8-d_H(a), and the total number of selected
addition variables is exactly four. These are precisely the degree
equations for this fixed family. Restricting to eight-regular graphs
loses no order-58 target: a vertex of degree at most seven can reach
at most 1+7+7*7=57 vertices within distance two.

## All distance clauses and helper semantics

For each of the binom(58,2) unordered pairs x,y, the source encodes

\[
E_{xy}\ \lor\ \bigvee_{z=0}^{57}(E_{xz}\land E_{zy}).
\]

Loops are false. Only pairs already covered by a fixed edge or two
fixed edges are skipped. Boolean constants are tested with Python
identity checks, so the positive variable numbered 1 is not mistaken
for the Boolean constant true. Every remaining conjunction is either
simplified by a constant or represented by a fresh variable with all
three clauses expressing equivalence to AND.

Consequently old-old routes through two added edges or through a new
vertex, old-new routes using an added edge or an H edge, and new-new
routes through an old vertex are all present. No deleted-edge-only
repair rule, port saturation, endpoint restriction, or auxiliary
structural lemma is imposed as an extra clause.

The imported generic functions add_iff_and, unary_thresholds, and
enforce_exact were read at their actual source in
context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/code/n62/n62_ab_cnf.py.
The unary recurrence represents each prefix threshold in both
directions, and enforce_exact requires threshold k and forbids
threshold k+1. Only these generic helpers and the emitter are used;
no n=62 graph constraints enter this instance. Every target graph in
the stated family extends to the auxiliary variables by its true
thresholds and true path conjunctions. Conversely a satisfying
assignment expands to a simple eight-regular graph in that family
covering every vertex pair within two steps.

## Actual saved result and its interpretation

The saved
[encoding.json](../../../computations/dd82/construction/hs58_two_delete_four_add_joint_run/encoding.json)
records 32,437 variables and 102,312 clauses, agreeing with the actual
input.cnf header. There are 26 old-old, 400 old-new, and three new-new
coverage clauses; 1,224 pairs are already covered by fixed edges.
These counts total 1,653=binom(58,2).

The saved
[result.json](../../../computations/dd82/construction/hs58_two_delete_four_add_joint_run/result.json)
records one CaDiCaL run, exit code 20, using 0.354425 CPU seconds and
0.367881 wall seconds. The actual
[certificate_check.log](../../../computations/dd82/construction/hs58_two_delete_four_add_joint_run/certificate_check.log)
identifies this input.cnf and proof.lrat, reports the same CNF counts,
and ends with s VERIFIED. Its recorded exit code is 20, CPU time
0.023120 seconds, and wall time 0.025737 seconds. The resulting saved
status is CHECKED_UNSAT. This review read those existing records; it
did not replay the certificate checker.

Together with the source-preservation check, this is a computer-assisted
exclusion of the fixed D/H family stated above, with all four additions
and all 400 attachments free. The subsequently obtained analytic
closure of disjoint-deletion K1,3 cases is a separate, broader result;
this experiment is corroborating evidence and need not be a dependency
of that mathematical proof. No arbitrary order-58 exclusion is claimed.
