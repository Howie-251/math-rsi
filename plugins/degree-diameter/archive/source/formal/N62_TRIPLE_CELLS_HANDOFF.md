# Actual order-62 triple-repeat cells and repeat separation

Source obligation: `proofs/dd82/n62/RECOVERED_REDUCTION.md`, Step 2, retained by the analytic triple-repeat exclusion. Starting with the original graph assumptions and an actual triple entry, construct the exclusive eight-set and two actual 24-sets, and prove their repeat separation.

Module: `DegreeDiameter/N62TripleCells.lean`, importing the completed `N62TripleMatching` unchanged. Every graph-specific conclusion takes only `G`, `degreeAtMostEight G`, `diameterAtMostTwo G`, `Fintype.card V = 62`, and the actual hypothesis `defectMatrix G u v = 3`, together with membership/entry hypotheses identifying the vertices concerned. No cell, matrix, equitable-partition, row-sum, or count certificate is supplied.

Implemented:

- `n62_triple_exclusive_repeat_sum`: the actual repeat row of each exclusive-side vertex sums to three over the opposite actual exclusive side. This uses `AB = BA` at the opposite endpoint and the proved saturated endpoint row, then removes the actual common-neighbor set using its proved repeat rows.
- `n62_triple_exclusive_repeat_zero_outside` and `n62_triple_exclusive_repeat_crosses`: the complete actual repeat row is supported on the opposite exclusive side. Reversing the endpoints yields the reverse direction. The actual eight-set `tripleExclusiveVertices` has cardinality eight and is repeat-closed.
- `tripleOuterFiber G u v s = G.neighborFinset s \ {u,v}` and `tripleOuterVertices G u v` as their actual finite union over the common-neighbor four-set. Each fiber has cardinality six; the four fibers are pairwise disjoint, so the union has cardinality 24.
- `n62_triple_outer_outside`: this outer set excludes both endpoints, the common-neighbor set, and both exclusive sides.
- `tripleCommonDegree`: actual original-neighbor count into the common-neighbor four-set. It equals four at the endpoints and one exactly on the outer set. Actual component equitability proves this count is preserved by every positive repeat entry; consequently the outer set is repeat-closed.
- `tripleInnerVertices`: the actual endpoints together with the union of their original neighborhoods. Its cardinality is 14, it is repeat-closed, and it is disjoint from the outer set. `mem_tripleInnerVertices` gives its exact decomposition into endpoints, common-neighbor set, and the two exclusive sides.
- `tripleRemainingVertices`: the actual complement of the inner and outer sets. It has cardinality 24 and is repeat-closed, using symmetry and the two proved closure statements.

Together with the existing endpoint-pair and common-four-set repeat rows, these statements establish separation of the actual five cells of sizes `(2,4,8,24,24)`. The sets are defined directly from original graph neighborhoods, finite unions, and complement; no relabeling or guessed partition is assumed.

Dedicated audit: `ReviewN62TripleCells.lean`, checking all 23 public theorems' types and axiom dependencies and four original-input callers. The callers verify both exclusive crossing directions and the cross-row sum, the concrete cell cardinalities and disjointness, closure of all three newly constructed cells, and the exact level-one characterization of the outer 24-set.

Validation:

```bash
cd formal
source ../.tools/lean-env.sh
export LEAN_NUM_THREADS=3 RAYON_NUM_THREADS=3
lake build DegreeDiameter.N62TripleCells
lake env lean ReviewN62TripleCells.lean
```

Targeted build exit 0: `logs/n62-triple-cells-second.log` (new module 27 seconds). It reports two harmless `unnecessarySimpa` suggestions in the inner-cardinality proof and inherited dependency warnings. Dedicated audit exit 0: `logs/n62-triple-cells-type-axiom-audit.log`. All 23 audited theorems use only `[propext, Classical.choice, Quot.sound]`; all four original-input examples compile. The first-build log records three repaired API/simp errors and is not a success record.

Precise remaining boundary: the full original-graph five-cell neighbor-count matrix is not exported here. In particular the next actual bridge must show U has no original neighbors in E, V has one original neighbor in each exclusive side, and the per-fiber U/V neighbor counts, yielding U internal degree three and V internal degree two. Construction of the actual four-by-four repeat block, its labeling and classification bridge, the 24-vertex matrices, and full triple elimination remain separate obligations. No full triple exclusion or unconditional original order-62 nonexistence is claimed. No shared entrypoint, shared audit, STATUS, existing source, or order-63–65 file was edited. Parent owns integration and cross-family source review.
