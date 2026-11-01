# Lean proof of the Property B lower bound

The original target is fully proved in [Aris4Math/Main.lean](Aris4Math/Main.lean): every finite simple 5-uniform hypergraph with at most 32 edges has Property B. Equivalently, every such hypergraph without Property B has at least 33 edges, giving **m(5) ≥ 33** in the [mathematical specification](../FORMAL_SPEC.md).

`Aris4Math.Target` is defined in the root module; its proof is `Aris4Math.propertyB_of_at_most_thirty_two` in `Main`. Import `Aris4Math.Main` to use the result. Two further entry points expose the statement without the `Target` abbreviation:

- `two_colorable_of_at_most_thirty_two`: a Boolean coloring with between one and four red vertices in every edge.
- `non_propertyB_edges_ge_thirty_three`: a non-Property-B hypergraph has at least 33 edges.

These statements quantify over arbitrary finite vertex types. They impose no balance, degree, regularity, pair-covering, or vertex-count assumption. The 19–25 vertex cases and pair-covering condition are proved reductions inside the argument.

## Reproduce the build

From the project root:

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
cd formal
lake build
lake env lean ../.aris/traces/proof-checker/2026-10-06_run09/lean-main-import-audit.lean
```

The default build target is now **`Aris4Math.Main`**. Lean is pinned to 4.24.0; Mathlib is pinned in `lake-manifest.json` to `f897ebcf72cd16f89ab4577d0c826cd14afaafc7` (v4.24.0). The project-local toolchain is in `.tools/elan` at the project root.

The [recorded build](../.aris/traces/proof-checker/2026-10-06_run09/lean-main-build.log) and [separate import audit](../.aris/traces/proof-checker/2026-10-06_run09/lean-main-import-audit.log) both exited successfully. The latter prints the actual definitions and expanded theorem types, then checks the transitive axioms of the finite goal and all three top-level formulations. Each depends only on `propext`, `Classical.choice`, and `Quot.sound`; there is no `sorryAx` or project-specific axiom in this dependency chain.

## Proof organization

`Reduction` and `SmallVertices` prove the reduction from arbitrary finite hypergraphs. `Aris4Math.finite_goal` assembles seven completed branches: `NoLocks` (19), `GlobalPairs` (20), `TwentyOne`, `TwentyTwo`, `TwentyThree`, and `LargeVertices` (24–25). The supporting modules prove structural selection, analytic type classification, actual conditional permutation counts, link-weight deductions, and exact rational bounds. See the [complete verification report](../context/FORMAL_VERIFICATION_PROGRESS.md) for the mapping and evidence.

The proof does not enumerate all hypergraphs, colorings, or permutations. It proves the coverage and counting statements and uses kernel-checked finite arithmetic for explicit profiles and constants. The result relies on Lean's standard logical foundations and the installed Lean/Mathlib toolchain; model review and counterexample searches are supplementary evidence, recorded separately in the [review notes](../context/reviews/research/REVIEW_NOTES.md).

## General RS probability core and 17-uniform pilot

The separate [General/RS/PilotMain.lean](Aris4Math/General/RS/PilotMain.lean) target proves the actual RS recoloring probability bound for every finite simple k-uniform hypergraph, k ≥ 2, and its Property B criterion. It also proves that every finite simple 17-uniform hypergraph with at most 131072 edges has Property B, by applying that same criterion. The initial colors, eligibility bits, full permutation, failure events, and their exact probabilities are connected in the proof.

With the same pinned toolchain, run from `formal/`:

```sh
lake build Aris4Math.General.RS.PilotMain
lake env lean ReviewAuditGeneralRSPilot.lean
```

The second command restates the original finite-vertex coloring claim and the general criterion, prints their definitions, and audits their transitive axioms. Both commands have exited successfully; all seven audited declarations depend only on `propext`, `Classical.choice`, and `Quot.sound`. The default build target remains the original five-uniform `Aris4Math.Main`.

See the [pilot stage report](../context/propertyb-general-lean-pilot/REPORT.md) and [pilot HTML](../PROPERTY_B_GENERAL_LEAN_PILOT.html). Its original [follow-up plan](../context/propertyb-general-lean-pilot/FUTURE_FORMALIZATION.md) has now been implemented in the separate growth-theorem entry below.

## Full growing integer improvement for every k ≥ 17

[General/Growth/Main.lean](Aris4Math/General/Growth/Main.lean) proves `propertyB_of_general_growth`: every finite simple k-uniform hypergraph with at most `rsBudget k + integerGain k (rsBudget k)` edges has Property B. `rsBudget_characterization` proves that this budget is exactly the maximum integer accepted by the paper's precise RS criterion. The maximum, its parameter witness, minimal-counterexample structure and the strict numerical bound are all proved internally. `non_propertyB_edges_ge_general_growth` states the equivalent edge-count lower bound.

```sh
lake build Aris4Math.General.Growth.Main
lake env lean ReviewAuditGeneralGrowth.lean
```

Both commands have exited successfully. The independent audit restates the maximum definition and its global maximality together with the original finite-vertex Bool coloring theorem; all seven queried declarations use only `propext`, `Classical.choice`, and `Quot.sound`. The fixed toolchain and default original five-uniform build target remain unchanged.

See the [full growth stage report](../context/propertyb-general-lean-growth/REPORT.md), [executed verification](../context/propertyb-general-lean-growth/VERIFICATION.json), and [statement-alignment audit](../context/propertyb-general-lean-growth/SEMANTIC_AUDIT.md). The separate literature-comparison theorems D/E remain paper proofs; this target formalizes the growth main theorem C.
