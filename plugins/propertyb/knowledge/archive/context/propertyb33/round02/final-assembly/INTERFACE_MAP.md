# T33 final assembly: actual interfaces

Updated 2026-10-13 against EXECUTION_SUMMARY.json. The named managed build `lake build Aris4Math.ThirtyThree.Main` passed with 1138 jobs and exit 0; the subsequent unconditional `lake env lean ReviewAudit33.lean` also passed. The complete Target33 export has no residual branch parameter. Earlier conditional smoke tests and direct compilation are preserved below only as preparation history. This is a local incremental build, not a clean or second-machine reproduction.

## 23-point partition

`TwentyThreeSelection.degree_count_cases` derives the exhaustive partition from the actual incidence budget:

| Number r of degree-six vertices | Actual Property B entry | Input beyond H, pair covering and exactly33 edges | Final recorded status |
|---|---|---|---|
| r = 0 | `TwentyThreeHighComplete.propertyB_of_no_sixes` | `H.sixVertices.card = 0` | Formal build and independent import PASS |
| r = 1, a seven-degree bad partner exists | `TwentyThreeLowBadHighComplete.propertyB_of_low_bad_high` | count1; actual x of degree6, y of degree7; codegree(x,y)≥2 | Formal build and independent import PASS |
| r = 1, all seven-degree partners are unit | `TwentyThreeLowUnitComplete.propertyB_of_low_unit` | count1; actual x of degree6; unit codegree with all degree7 vertices | Formal build and post-build independent import PASS |
| r = 2 | `TwentyThreeTwoLowComplete.propertyB_of_two_sixes` | `H.sixVertices.card = 2` | Direct compile, ordinary Lake build (1018 jobs) and post-build independent import PASS |
| r = 3 | `TwentyThreeThreeLowComplete.propertyB_of_three_sixes` | `H.sixVertices.card = 3` | Complete managed Lake build and post-build independent import PASS |
| r ≥ 4 | `TwentyThreeFourLowComplete.propertyB_of_four_sixes` | `4 ≤ H.sixVertices.card` | Formal build and independent import PASS |

`TwentyThreeComplete.propertyB_of_one_six` obtains the actual degree-six vertex from the nonempty degree-six set. If a seven-degree vertex has codegree≥2 with it, the bad-partner theorem applies. Otherwise degree difference makes the pair distinct, pair covering supplies codegree≥1, and the negated bad-partner predicate gives codegree<2. Thus every such codegree equals1, exactly the all-unit theorem's input.

`Aris4Math.ThirtyThree.twenty_three_propertyB` then invokes the five exhaustive values/ranges of r. The final signature is only:

```lean
(H : Simple5Hypergraph (Fin 23)) →
H.PairCovering → H.edges.card = 33 → PropertyB H
```

## Whole finite domain and original target

Existing `Assembly.finite_goal_of_remaining` covers 19,20,21,22,24,25 with their actual theorems and leaves exactly the23-point input. The new `ThirtyThree/Main.lean` supplies it with `twenty_three_propertyB`. It exports:

- `Aris4Math.ThirtyThree.remaining_goal : RemainingGoal`;
- `Aris4Math.ThirtyThree.finite_goal : FiniteGoal`;
- `Aris4Math.propertyB_of_at_most_thirty_three : Target33`;
- `Aris4Math.two_colorable_of_at_most_thirty_three`, spelling out the original Bool-coloring conclusion;
- `Aris4Math.non_propertyB_edges_ge_thirty_four`, the equivalent lower bound.

The existing `Reduction.target_of_finite_goal` starts with any finite vertex type and at most33 edges. A least-vertex counterexample is pair-covering because merging an uncovered pair would produce a smaller one. Integer degree/incidence counting bounds the vertex count by25; the balanced coloring bound handles up to18. Padding to exactly33 distinct five-sets preserves noncolorability and pair coverage. This supplies all internal hypotheses of the finite branches. The padding proof does not invoke the old T32 main theorem.

The original `Aris4Math/Main.lean`, its T32 exports, and the default Lake target are unchanged. Acceptance of T33 must name `Aris4Math.ThirtyThree.Main` explicitly.

## Independent spelling and checks

`formal/ReviewAudit33.lean` imports the actual new Main and has passed. It independently spells the input as arbitrary `[Finite V]`, a `Finset (Finset V)`, uniform edge size5 and edge cardinality≤33. It checks the original red-count formulation, the literal existence of both Boolean colors in each edge, and the lower-bound formulation. This tests the exported statement against the original object domain without reusing a project-specific target alias in its statement. It is an independent import and spelling on this machine, not a second proof or another person's independent replication.

Preparation checks and final acceptance:

- `context/propertyb33/round02/twentythree-selection/TwentyThreeConditionalCaller.lean`: complete23-point routing with unfinished branch propositions as explicit parameters; passed short compilation.
- `context/propertyb33/round02/twentythree-selection/FinalStatementConditionalCaller.lean`: actual Assembly caller and the independent original statement, with the missing target kept as an explicit parameter; passed short compilation, recorded in `final-statement-conditional-check.log`.
- Actual direct Main compilation and unconditional `lake env lean ReviewAudit33.lean` both PASS, recorded in `main-direct.log` and `original-statement-import-audit.log`. The final named managed build subsequently passed; see `main-build.log` and `main-build.meta.json`. Post-build original-statement audit passed in `original-statement-post-build-audit.log`; all eight audited declarations depend only on `propext`, `Classical.choice`, and `Quot.sound`.

No source file adds an axiom or unfinished-proof placeholder. Grok and Gemini final C responses were both valid and found no substantive issue in their actual static-reading scopes; neither executed Lean. See [review disposition](../reviews/REVIEW_DISPOSITION.md) and [final proof audit](../final-audit/PROOF_AUDIT.md).
