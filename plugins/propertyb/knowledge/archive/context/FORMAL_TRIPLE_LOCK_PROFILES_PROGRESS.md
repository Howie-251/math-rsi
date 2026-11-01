# Actual 23-point three-lock type table

`formal/Aris4Math/TripleLockProfiles.lean` is frozen and successfully built on 2026-10-06. Four explicit axiom audits (`counts_677`, `position_fiber_count`, `realizes_677`, `realizes_677_of_vertices`) report only `propext`, `Classical.choice`, and `Quot.sound`.

The input is an actual simple five-uniform hypergraph on 23 points with 32 edges and three distinct chosen points. Their degrees are 6, 7, 7; every pair has codegree one; no edge contains all three. `threeVertices` embeds these actual points as indices 0, 1, 2, and `threePositions` locks them at one-based positions 11, 12, 13.

The proof partitions actual edges by the eight subsets of the three lock indices. `sum_all_counts`, `sum_degree_counts`, and `sum_codegree_counts` derive the total, three degree equations, and three pair-codegree equations. The no-triple assumption forces the eighth fiber to zero. The resulting linear equations give exact counts:

| Position type | Count |
|---|---:|
| empty | 15 |
| [11] | 4 |
| [12] | 5 |
| [13] | 5 |
| [11,12] | 1 |
| [11,13] | 1 |
| [12,13] | 1 |

The enumeration is only of eight label sets, not of hypergraphs or permutations. Canonical sorted-position lists are proved injective, giving `position_fiber_count`. The final `realizes_677_of_vertices` concludes the actual `RealizesProfile` for `Numeric.v23_677` directly from the structural hypotheses.

The source theorem contains no arbitrary type-count assumptions, `sorry`, new axioms, or `native_decide`. Parent-owned `TwentyThree.lean` applies the structural selection theorem, this realized profile, the actual link-deletion certificates, and the probability bridge.

Evidence: `.aris/traces/proof-checker/2026-10-06_run08/lean-triple-profiles-build.log` and matching metadata.
