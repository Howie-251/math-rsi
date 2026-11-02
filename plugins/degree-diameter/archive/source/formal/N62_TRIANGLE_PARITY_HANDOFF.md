# Actual n62 parity checkpoint — 2026-10-11

New compiled modules: `DegreeDiameter/N62TriangleParity.lean` and `DegreeDiameter/N62OppositeParity.lean`. Dedicated audits: `ReviewN62TriangleParity.lean` and `ReviewN62OppositeParity.lean`. Shared entrypoint and STATUS were not changed by this worker.

`n62_triangle_count_even` proves `Even (G.cliqueFinset 3).card` from the original arbitrary finite graph, maximum degree eight, actual diameter at most two, and card(V)=62. `G.cliqueFinset 3` is Mathlib's genuine finite set of unordered three-vertex cliques. There is no defect simplicity or supplied involution hypothesis.

The concrete map `triangleMateSet G T` contains exactly the vertices outside T with actual defect entry one from some member of T. The previously checked six exact repeat rows identify its forward and reciprocal images. `n62_triangle_mate_set_properties` proves preservation of genuine triangles, disjointness, and involutivity; `n62_triangle_mate_set_ne` proves absence of fixed triangles. `Finset.sum_involution` over ZMod 2 proves evenness, also covering the empty triangle set.

The optional `n62_unit_nonedge_pair_count_even` proves evenness of the actual finite set `unitNonedgePairs G`, under the additional explicit assumption `∀ x y, defectMatrix G x y ≤ 1`. Actual nonnegativity and zero diagonal are derived from the original graph, so this is the intended simple-defect case. `oppositePair G P` is the genuine set of common neighbors of both vertices of P. Every unit-repeat nonedge has exactly two common neighbors. Those two vertices cannot be adjacent, by the previously proved original-edge defect bound; simplicity forces their reverse common-neighbor set to be exactly P. This gives a second fixed-point-free involution and the opposite-pair four-cycle parity count without Walk API or an abstract cycle certificate.

Successful commands, each exit 0, using LEAN_NUM_THREADS=3 and RAYON_NUM_THREADS=3:

```bash
lake build DegreeDiameter.N62TriangleParity
lake env lean ReviewN62TriangleParity.lean
lake build DegreeDiameter.N62OppositeParity
lake env lean ReviewN62OppositeParity.lean
```

Actual evidence:

- `logs/n62-triangle-parity-build.log`
- `logs/n62-triangle-parity-type-axiom-audit.log`
- `logs/n62-opposite-parity-first.log`
- `logs/n62-opposite-parity-type-axiom-audit.log`

All five audited parity/involution theorems use only propext, Classical.choice, and Quot.sound. No sorry, new axiom, native_decide, or artifact hash was introduced. The first triangle-parity compiler attempt had two local simp/API errors; the named successful build is the corrected source. The opposite-pair module succeeded on its first build. One harmless deprecated Finset lemma-name warning remains in TriangleParity.

The remaining bridge to the simple-defect exclusion is actual finite incidence counting. A compact sufficient identity is

    2 * (unitNonedgePairs G).card + 6 * (G.cliqueFinset 3).card = 186.

All actual ordered unit-defect pairs number 62*3=186 by the derived row sums. Each unordered unit-repeat nonedge contributes two ordered pairs. Each actual triangle contributes six ordered adjacent pairs, with unique coverage since an original edge has defect at most one. Combining this identity with the two compiled evenness theorems gives the contradiction. That identity and final simple-defect exclusion are NOT claimed here. Universal order-62 exclusion remains open. Parent workflow owns entrypoint integration, status updates, and cross-family source review.
