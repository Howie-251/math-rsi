# T33: completed kernel proof and original-statement audit

Updated 2026-10-13. The positive T33 statement has now been accepted by the pinned Lean kernel through the actual new Main and an unconditional independent import. The original target is:

> Every finite simple five-uniform hypergraph with at most33 edges has a Boolean coloring in which each edge contains both colors.

The equivalent lower bound is m(5)≥34. The delivered theorem does not assert equality m(5)=34. The named `lake build Aris4Math.ThirtyThree.Main` completed successfully with 1138 jobs, followed by a successful independent original-statement audit. This report records the formal result and its execution evidence; overall delivery status is recorded separately in `../final-audit/PROOF_CHECK_STATE.json`.

## Actual completed exports

Source `formal/Aris4Math/ThirtyThree/TwentyThreeComplete.lean` assembles all six structural branches into

```lean
Aris4Math.ThirtyThree.twenty_three_propertyB
  (H : Simple5Hypergraph (Fin 23))
  (cover : H.PairCovering) (edges33 : H.edges.card = 33) : PropertyB H
```

The r=1 subassembly chooses its actual degree-six vertex and splits between a nonunit seven-degree partner and the complementary all-unit condition. The full degree split covers r=0,1,2,3 and r≥4. Every branch theorem is imported as an actual proof; no branch oracle remains.

Source `formal/Aris4Math/ThirtyThree/Main.lean` supplies this theorem to the existing complete finite reduction/assembly and exports:

```lean
Aris4Math.propertyB_of_at_most_thirty_three : Target33
Aris4Math.two_colorable_of_at_most_thirty_three
Aris4Math.non_propertyB_edges_ge_thirty_four
```

`Target33` quantifies over arbitrary finite vertex types and all actual simple five-uniform hypergraphs with edge count≤33. The top-level theorem has no pair-covering, vertex-count, degree, profile, table, probability-bound or `RemainingGoal` premise. All these internal conditions are supplied by proved reductions and actual callers.

## Independent spelling of the original statement

`formal/ReviewAudit33.lean` imports the new Main and proves a statement written without the project's target/hypergraph aliases in its input:

```lean
∀ (V : Type u) [Finite V] (E : Finset (Finset V)),
  (∀ e ∈ E, e.card = 5) → E.card ≤ 33 →
  ∃ c : V → Bool, ∀ e ∈ E,
    1 ≤ (e.filter fun x => c x = true).card ∧
    (e.filter fun x => c x = true).card ≤ 4
```

It also checks that each edge actually contains a true-colored vertex and a false-colored vertex, and proves the equivalent lower bound for an uncolorable bare edge set. The audit prints the concrete definitions, actual exported types, and eight transitive-axiom dependencies. All eight depend only on `propext`, `Classical.choice`, `Quot.sound`.

This is a separate import and independent spelling on the same machine. It uses the same constructed mathematical proof, and does not claim another person's review, a second proof or replication on another machine.

## Executed commands and outcomes

The following commands ran in `formal/` after selecting the project-local toolchain:

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
```

| Command | Exit | Evidence | Reported wall time |
|---|---:|---|---:|
| `lake env lean -o .lake/build/lib/lean/Aris4Math/ThirtyThree/TwentyThreeComplete.olean Aris4Math/ThirtyThree/TwentyThreeComplete.lean` | 0 | `twenty-three-direct.log` | 3.656750166 s |
| `lake env lean -o .lake/build/lib/lean/Aris4Math/ThirtyThree/Main.olean Aris4Math/ThirtyThree/Main.lean` | 0 | `main-direct.log` | 9.438417791 s |
| `lake env lean ReviewAudit33.lean` | 0 | `original-statement-import-audit.log` | Not separately recorded; the first tool wait yielded after10.002720625 s, final resumed result exited0. |
| `lake build Aris4Math.ThirtyThree.Main` | 0; 1138 jobs | `main-build.log`, `main-build.meta.json` | 12.506869832985103 s |
| `lake env lean ReviewAudit33.lean` after named build | 0 | `original-statement-post-build-audit.log`, `original-statement-post-build-audit.meta.json` | 12.1003973329789 s |

The wall times are the tool's reported values for these invocations, not a claim about total project build cost. The many supporting finite classifications and exact formulas were checked in their own source builds.

`ENVIRONMENT.txt` records the actual Lean version and the manifest's resolved Mathlib revision: Lean4.24.0, Mathlib `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. Machine-readable command/exit/scope metadata is `EXECUTION_SUMMARY.json`.

The default `lake build` target remains the original T32 `Aris4Math.Main`. The successful new-result build explicitly used

```sh
lake build Aris4Math.ThirtyThree.Main
```

The named build started at 2026-10-13 07:41:36 UTC and succeeded. The post-build audit started at 07:42:00 UTC and succeeded; its output is identical to the earlier independent original-statement audit, including all eight standard-three-axiom results. This was a managed incremental build using the pinned dependency cache and already built modules. Its 12.51 seconds are the final invocation's wall time, not the cost of constructing all supporting modules from scratch. No clean build or second-machine reproduction is claimed.

## Source and review map

The obligation DAG, mathematical skeleton and exact hypothesis origins are in `../final-audit/PROOF_SKELETON.md`. `INTERFACE_MAP.md` identifies each actual finite-branch API. `SOURCE_IMPORT_CLOSURE.txt` lists the project modules reachable from the new Main. The source scan found no proof-placeholder or `native_decide` use in that closure; the two plain-text occurrences of the English word “admit” were documentation prose. The actual transitive-axiom output is the acceptance evidence for the theorem dependency chain.

Earlier `TwentyThreeConditionalCaller.lean` and `FinalStatementConditionalCaller.lean` in the sibling `twentythree-selection/` directory were interface probes with explicit assumptions. They are retained as development history and are superseded for acceptance by the actual Main/import logs above.

Fresh final C reviews from Grok (`grok-4.7-build/xhigh`) and Gemini (CLI-selected `gemini-3.8-flash-high/high`, fresh retry1) both returned valid content without identifying a substantive gap in their actual reading scopes. They read sources and recorded outputs; neither ran Lean. The first Gemini C call failed and is not counted as acceptance. Raw replies and scope/correction records are in `../reviews/`. Any build-pending wording in those submitted-snapshot reviews is superseded by the execution evidence above.

The fresh proof-checker read the complete mathematical draft and identified two minor expository bookkeeping errors, both corrected with the exact diff reviewed. The frozen-input `WARN` and same-family/provisional status remain recorded; no mathematical gap was identified in the corrected proof. HTML fidelity review passed with offline desktop and phone checks, also marked same-family/provisional. The final reading edition is `PROOF_PACKAGE_33.html` at the project root, sourced from `proofs/propertyb33/PROOF_PACKAGE.md`. Formal audit and human reproduction instructions are in `../final-audit/PROOF_AUDIT.md` and the root `HANDOFF_FOR_REVIEW_33.md`.

The original T32 Main, statement, proof state and claim have not been replaced or weakened.
