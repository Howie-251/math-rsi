# Actual n62 simple-defect exclusion — 2026-10-11

Completed module: `DegreeDiameter/N62SimpleExclusion.lean`. Dedicated audit: `ReviewN62SimpleExclusion.lean`. Shared entrypoint and STATUS remain owned by the parent workflow and were not changed by this worker.

The final universe-polymorphic original-graph theorem is:

```lean
no_n62_simple_defect_graph
    (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G)
    (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62)
    (hsimple : ∀ x y, defectMatrix G x y ≤ 1) : False
```

The defect matrix is the actual integer `A*A+A-7I-J` of this same arbitrary graph. Its nonnegativity is derived, so the explicit entry upper bound is exactly the simple-defect subcase. No count, row template, triangle pairing, cycle certificate, or parity premise is supplied to the final theorem.

`n62_simple_repeat_incidence` proves the actual finite identity

    2 * (unitNonedgePairs G).card + 6 * (G.cliqueFinset 3).card = 186.

The proof uses genuine unordered two-point sets and Mathlib's genuine unordered three-cliques. Each two-point set contributes exactly two ordered off-diagonal pairs. Each triangle contributes exactly six. Distinct two-point sets have disjoint off-diagonals; distinct triangles also have disjoint off-diagonals, by the already derived unique neighborhood triangle edge. The nonadjacent and adjacent unions are disjoint and exactly cover the actual ordered B=1 pairs. Nonnegativity, the explicit upper bound one, and all 62 actual row sums of three give exactly 186 ordered pairs. The two previously compiled evenness theorems then yield the contradiction by integer arithmetic.

Actual validation, each exit 0, with LEAN_NUM_THREADS=3 and RAYON_NUM_THREADS=3:

```bash
source ../.tools/lean-env.sh
export LEAN_NUM_THREADS=3 RAYON_NUM_THREADS=3
lake build DegreeDiameter.N62SimpleExclusion
lake env lean ReviewN62SimpleExclusion.lean
```

Successful evidence:

- `logs/n62-simple-exclusion-build-second.log` — successful module build, 9.3 seconds.
- `logs/n62-simple-exclusion-type-axiom-audit.log` — exact actual definitions, both exported theorem types, both transitive-axiom reports, and a raw original-graph caller compiled successfully.

Both exported results depend only on `propext`, `Classical.choice`, and `Quot.sound`. Source inspection found no sorry, native_decide, or new axiom. Earlier unsuccessful compiler logs preserve two Ne.symm elaboration repairs and one self-rewriting simp issue, fixed by pointwise sum_congr; they are not claimed as validation. No hash or checksum was generated.

This closes the formal simple-defect exclusion, including the actual incidence bridge left open in N62_TRIANGLE_PARITY_HANDOFF.md. It does not exclude graphs with an entry at least two, prove the remaining double-repeat cases, determine N(8,2), or change the certified global bound. Cross-family final-source review and shared entrypoint/status integration remain the parent's workflow responsibilities. No known n63–65 proof was developed or rebuilt deliberately.
