# HS58 a5: remaining-geometry joint encoding check

Date: 2026-10-12. Read-only review of
`computations/dd82/construction/hs58_a5_remaining_joint.py`, its two
actual `encoding.json` files and DIMACS headers, and the called exact
cardinality / conjunction helpers. No CNF regeneration, solver run,
or certificate replay was performed for this review.

No candidate-preservation gap was found in the encoding. Its precise
scope is exactly two fixed original deletions, exactly five original
nonedge additions, an auxiliary H among the 67 retained canonical
representatives, and arbitrary old-new attachments. Combined with
the existing auxiliary reductions and the complete deletion orbits,
this covers the adjacent and cross geometries respectively.

There are 1050 variables for all original nonedges, all 400 old-new
edge variables, 28 H-edge variables, and 67 type selectors. At least
one selector and pairwise at-most-one clauses choose exactly one
type. Its implication clauses fix every H-edge variable to precisely
that representative. Canonicalizing H uses only a permutation of new
vertices; all attachment columns remain free, so it costs no candidate.
The 67-type domain depends on the saved complete auxiliary catalog,
the universal-H exclusion, and the adjacent maximal-port exclusion
for the 17 five-bad-pair types. It is not justified by a solver result.

For each old vertex x, the exact-degree constraint is
\[
\deg_A(x)+|B_x|=8-\deg_{Q-D}(x).
\]
For each new a it is |B^a|+deg_H(a)=8. The additional exact cardinality
requires |A|=5. Deleted original edges remain false; they do not occur
among the nonedge addition variables. The source applies no further
old-vertex or attachment normalization, matching restriction, or
saturated-endpoint condition. In particular the conditional 720
cross-matchings lemma is not used as a general-domain restriction.

For each of the 1653 vertex pairs, a retained original edge or retained
original two-step path suffices to skip its clause. Every other pair
receives the disjunction of its direct edge and every two-edge route
through all 58 potential intermediates. Self edges are false. Old-old
routes include A-A and B-B; old-new routes include A-B and B-H;
new-new routes include B-B and H-H, as well as the direct H edge.
Conjunction variables have the complete three-clause equivalence.
Boolean constants are distinguished by `is True` / `is False`, so
variable 1 is not confused with a constant. Reusing conjunctions and
`set(terms)` removes repeated Boolean alternatives from an OR and
does not impose a route-counting condition.

The imported helper module contributes only generic CNF emission,
exact unary cardinalities, and AND equivalences; its historical n62
graph encoder is never instantiated. The unary recurrence has both
directions and enforces the target threshold and excludes the next.

| Geometry | Fixed D | Variables | Clauses | Fixed-covered pairs | Remaining old-old / old-new / new-new |
| --- | --- | ---: | ---: | ---: | --- |
| Adjacent | {01,04} | 39032 | 128174 | 1200 | 25 / 400 / 28 |
| Cross | {01,23} | 39076 | 128308 | 1199 | 26 / 400 / 28 |

These counts agree between the saved metadata and actual DIMACS
headers.

After the encoding review, the parent's two authorized runs completed.
Their saved `result.json` and `certificate_check.log` were then read
without rerunning either solver or checker. Both report CHECKED_UNSAT,
solver exit 20, checker exit 20, and `s VERIFIED`; each check explicitly
names its corresponding saved `input.cnf` and `proof.lrat` and prints
the same variable/clause header above. Adjacent solver/checker CPU
was 19.536785 / 0.981838 seconds; cross solver/checker CPU was
7.061750 / 0.254257 seconds. The result paths are respectively
`hs58_a5_remaining_joint_run/adjacent/` and
`hs58_a5_remaining_joint_run/cross/` under the construction directory.

The proposed cumulative scope is correct. Every unordered pair of
distinct original edges is exactly one of: adjacent; disjoint with
an original cross edge; disjoint without one. The first two complete
orbits and their free-addition/free-port joint CNFs are covered here
and in `HS58_REMAINING_DELETION_ORBITS.md`. The third is already
closed by `HS58_A5_NO_CROSS_DELETIONS_EXCLUSION.md`, including its
7875-pair orbit, 67-to-1 H reduction, and actual checked type-3 CNF.
Consequently all three geometries with exactly five additions are
excluded. Combining the previously proved addition budget and the
two-, three-, and four-addition exclusions gives: an eight-regular
diameter-two extension of HS50 by eight vertices, deleting exactly
two original edges, must add at least six original nonedges.
This does not assert existence with six additions, cover other
deletion counts, or exclude arbitrary graphs on 58 vertices. The
statement is computer-assisted and this review makes no new claim
of external-review acceptance or completed Lean formalization.
