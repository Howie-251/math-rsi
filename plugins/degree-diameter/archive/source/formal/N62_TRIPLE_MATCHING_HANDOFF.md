# Actual order-62 triple-repeat exclusive-side matching

Source obligation: `proofs/dd82/n62/RECOVERED_REDUCTION.md`, Step 2. Given only the original graph assumptions and an actual triple entry `defectMatrix G u v = 3`, construct the exclusive original-neighbor sides and their actual perfect matching.

Module: `DegreeDiameter/N62TripleMatching.lean`, importing completed `N62TripleRepeat` unchanged. The actual side is defined by `tripleExclusiveNeighbors G u v = G.neighborFinset u \ commonNeighborVertices G u v`; its proved membership description is `G.Adj u x ∧ ¬ G.Adj v x`.

Implemented:

- The two sides are disjoint from each other, from the actual common-neighbor four-set, and from both endpoints.
- Each side has four vertices and is independent in the original graph. There are no original edges from a side to the common-neighbor four-set.
- `n62_triple_exclusive_opposite_common_card`: an exclusive vertex and the opposite endpoint have exactly one actual common neighbor.
- `n62_triple_cross_neighbors_eq`: that actual common-neighbor set is exactly its original neighbors in the opposite exclusive side.
- `n62_triple_cross_degree_one`, `n62_triple_exclusive_unique_neighbor`: cross degree one and a unique actual cross-side neighbor. Applying the same theorem with reversed endpoints, using actual defect symmetry, gives both directions.
- `tripleExclusiveMate`: selects the already proved unique original neighbor.
- `tripleMatchingEquiv`: constructs an equivalence between the two actual subtype four-sets; `tripleMatchingEquiv_adj_iff` proves that its graph is exactly the original cross-side adjacency relation.
- `n62_triple_exclusive_six_remaining`: deleting the original endpoint and actual matching mate leaves six original neighbors.
- `n62_triple_exclusive_remaining_outside` and `n62_triple_exclusive_exterior_card`: those six vertices lie outside both endpoints, the common-neighbor set, and both exclusive sides, with exact original-neighbor count six there.

All graph-specific exported conclusions use original degree/diameter/order-62 assumptions and the actual triple entry only. No matching, root, row, five-cell, or finite-matrix certificate is supplied as a premise.

Proof connection: use the saturated opposite endpoint row to obtain defect zero between it and an exclusive vertex; their nonadjacency gives exactly one common neighbor. Endpoint neighborhood independence puts that common neighbor on the opposite exclusive side. Uniqueness in both directions constructs inverse mate functions. All cardinalities use actual filtered original-neighbor sets and original degree 8.

Dedicated audit: `ReviewN62TripleMatching.lean`. Actual-input examples check both sides' cardinalities and disjointness, both endpoint exclusions and both unique-neighbor directions, the matching equivalence's exact adjacency interpretation, and the six outside neighbors.

Reproduction:

```bash
cd formal
source ../.tools/lean-env.sh
export LEAN_NUM_THREADS=3 RAYON_NUM_THREADS=3
lake build DegreeDiameter.N62TripleMatching
lake env lean ReviewN62TripleMatching.lean
```

Targeted build exit 0: `logs/n62-triple-matching-second.log` (new module 41s, no new-module warning; existing dependency warnings are replayed). Final dedicated audit exit 0: `logs/n62-triple-matching-type-axiom-audit-final.log`. All 19 audited declarations (17 public theorems plus the mate/equivalence constructions) depend only on `[propext, Classical.choice, Quot.sound]`; all four original-input examples compile. The first build log preserves repaired API/simp/proof-field errors. The initial audit log preserves a repaired subtype-binder annotation error in its equivalence example; neither is a success record.

Remaining: this does not construct the full five-cell quotient, establish repeat separation or the opposite-side repeat block, build the 24-vertex block matrices, or eliminate triple entries. Parent has reported a developing paper route replacing the old finite enumeration; this module supplies actual graph geometry usable by either route and claims no enumeration result. No shared entrypoints/STATUS, existing sources, or order-63–65 sources were changed. Parent owns integration and cross-family review.
