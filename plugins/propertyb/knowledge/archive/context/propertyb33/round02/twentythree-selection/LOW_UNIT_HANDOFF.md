# 23-point one-low, all-unit interfaces

Date: 2026-10-13. Project: `aris4math`. Both interfaces below have explicit module builds and independent import audits. They supplement the completed r=0 branch in `HIGH_BRANCH_HANDOFF.md`.

## Actual high-pair exclusion

`Aris4Math.ThirtyThree.TwentyThreeLowUnitFiveComplete.propertyB_of_high_pair`

Inputs are the actual `Simple5Hypergraph (Fin 23)`, pair covering, exactly 33 edges, at least 17 vertices of degree seven, an actual vertex x of degree six with unit codegree to every degree-seven vertex, and distinct degree-seven y,z with codegree at least three. The conclusion is `PropertyB H`. It has no selected locks, trace profile, catalog certificate or numerical bound as an input.

Codegree at least four invokes `TwentyThreeHighPair`. In the codegree-three case, `TwentyThreeDefectSelection.exists_mixed_five_of_high_three` produces five distinct actual locks. Their degrees are (6,7,7,7,7), pair 12 has codegree three, and only pair 34 may have another nonunit codegree. If that codegree is at least four, `TwentyThreeHighPair` applies again. Otherwise pair covering puts it in 1..3.

The locks are reordered to (old3,old4,old1,old2,old0), with the degree-six lock now at index4. Every large trace contains a unit-codegree pair, hence has multiplicity at most one. The actual pair budgets put the Boolean large-trace family into the already kernel-checked 55-family maximal catalog. `TwentyThreeLowUnitFiveCatalog.classify` covers all three values of the remaining pair codegree, obtaining one of 75 representatives and an explicit label permutation. The actual singleton, pair and empty upper counts reconstruct the entire actual multiplicity vector using `MultiLockRecovery.actual_recovered`. Relabeling preserves actual counts. The caller supplies these counts directly to the parent's `TwentyThreeLowUnitFiveBare.propertyB_of_counts`.

Files owned or checked here:

- `formal/Aris4Math/ThirtyThree/TwentyThreeLowUnitFiveCatalog.lean`: parent-generated catalog, explicit build checked here; 151 admissible labeled inputs, 75 representatives.
- `formal/Aris4Math/ThirtyThree/TwentyThreeLowUnitFiveComplete.lean`: actual trace and selection caller, 215 lines.

The parent owns `TwentyThreeLowUnitFiveBare.lean`; it was built before these checks and was not modified here.

## Actual six-lock matching normalization

`Aris4Math.ThirtyThree.TwentyThreeLowUnitSixSelection.exists_locks`

Inputs:

- actual `Simple5Hypergraph (Fin 23)`, pair covering, exactly 33 edges;
- `H.sixVertices.card = 1`;
- a degree-six vertex x whose codegree with every degree-seven vertex is one;
- every distinct degree-seven pair has codegree at most two.

Output:

```lean
∃ e : Fin 3, ∃ w : Fin 6 ↪ Fin 23,
  (∀ i, H.degree (w i) = TwentyThreeLowUnitSixCatalogData.degreeData i) ∧
  (∀ i j, i ≠ j → H.codegree (w i) (w j) =
    TwentyThreeLowUnitSixCatalogData.pairDegree e i j)
```

Thus indices 0..4 have degree seven, index5 degree six; e=0,1,2 specifies zero, one or two disjoint pairs of codegree two, at canonical positions 01 and 23. All other distinct pairs have codegree one.

`exists_six_locks_low_unit_of_count` supplies the actual six locks and shows that each of the five high locks has at most one nonunit neighbor among the other high locks. Pair covering and the supplied upper bound restrict each high-high codegree to 1 or 2. The module defines ten Boolean bits from these actual codegrees and proves their exact correspondence to a symmetric local relation. The resulting graph has maximum degree one.

The finite classification includes all 2^10 assignments, retaining exactly 26 matchings (one empty, ten one-edge, fifteen two-edge). `matching_complete` proves coverage in the kernel; `normalized` verifies an explicit permutation for every retained matching. These permutations are the parent's stable S5 permutations fixing label5. The embedding is the composition of the selected actual embedding with the chosen permutation. `permutation_degrees` proves that this reindexing preserves the degree vector.

The output does not assume the six locks, a matching or a representative profile. The further actual trace recovery, 243 representative classification, and probability exclusions belong to the parent's six-lock caller.

## Executed acceptance

All commands run from `formal/` with the project's pinned `.tools/elan` environment.

- `lake build Aris4Math.ThirtyThree.TwentyThreeLowUnitFiveCatalog`: PASS, 1004 jobs, new module 525 seconds. Log: `low-unit-five-catalog-build.log`.
- `lake build Aris4Math.ThirtyThree.TwentyThreeLowUnitFiveComplete`: PASS, 1013 jobs, new module 3.0 seconds. Log: `low-unit-five-complete-build.log`.
- `lake build Aris4Math.ThirtyThree.TwentyThreeLowUnitSixSelection`: PASS, 973 jobs, new module 19 seconds. Log: `low-unit-six-selection-build.log`.
- `lake env lean ../context/propertyb33/round02/twentythree-selection/LowUnitFiveImportAudit.lean`: independent import, original Bool-coloring caller, exported type and five transitive axiom audits. Log: `low-unit-five-import-audit.log`.
- `lake env lean ../context/propertyb33/round02/twentythree-selection/LowUnitSixSelectionImportAudit.lean`: independent import, expanded original degree/codegree interface and four transitive axiom audits. Log: `low-unit-six-selection-import-audit.log`.

The audited conclusions use only `propext`, `Classical.choice`, `Quot.sound`; `actual_related` uses the subset `propext`, `Quot.sound`. Source scans of the three modules changed/checked here found no `sorry`, `admit`, new `axiom`, or `native_decide`.

First short compilation logs remain as diagnostic history; their earlier errors are superseded by the explicit successful builds and independent import logs. In particular, an error-bearing temporary `#print axioms` output is not acceptance evidence.

These are Lean kernel and interface results. This agent performed no Grok/Gemini calls; cross-family review is coordinated by the parent. Interpretive review by this agent remains same-family/provisional. The parent owns total T33 assembly and completion claims.
