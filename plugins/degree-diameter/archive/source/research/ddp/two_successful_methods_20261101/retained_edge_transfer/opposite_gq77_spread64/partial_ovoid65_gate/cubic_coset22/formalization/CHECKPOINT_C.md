# Final kernel checkpoint: exact161150 instance

All24new Lean modules are complete and exited0: Definitions,20 finite-input chunks, Inputs, Exact, and separate Audit. `GQ77Cubic22Clone65Exact.lean:38` proves the closed theorem

```lean
Fintype.card Vertex = 161150 ∧
  (∀ v, graph.degree v ≤ 65) ∧
  DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
```

`final_claim : FinalClaim` is also closed. Neither theorem accepts a user certificate or any remaining finite hypothesis. Both depend only on propext, Classical.choice, Quot.sound. The source no-isolates proof and old bounded-Walk equivalence have the same standard three axioms. The separate Audit imports only Exact, checks the label and load bridges, prints the actual theorem type and body and FinalClaim, and prints all final axioms. Explicit printing of `DiameterAtMost` shows `SimpleGraph.Walk.length`; the diameter assertion is the existing actual bounded Walk predicate.

The graph definition, printed by Audit, is exactly `FullNeighborhoodClones.graph OppositeGQ77Spread.graph center`: old-old adjacency is retained; old-new adjacency tests the immutable source center; new-new adjacency is False. It is on literal carrier `(Fin160000⊕Fin50)⊕Fin1100`, with explicit `label : Vertex ≃ Fin161150`. `clonePair` gives k=50*i+j in the original point/spread order, and the closed label lemmas give all original labels and new160050+k labels. `ovoid_unique` is proved by the actual22owner and3200line-position kernel checks; the source's completed spread uniqueness supplies hS. The generic load bound needs no center independence assumption or injectivity premise.

The completed external binding reads the actual literal files. It checks all1100ordered centers, all70400immutable64-neighbor source pin entries, and every one of5192000final edges against the source-plus-clones formula. All5121600old edges are retained exactly, and0new-new edges occur. This external ASCII binding is not represented as a Lean parser theorem and runs0BFS; the fresh numerical1100new-root acceptance is a separate root task.

Measured Lean child CPU for all attempts is98.887887seconds. This includes the initial terminated preparation attempt0.823873, the naturally successful broad import3.272812 before import narrowing, and an earlier successful Audit2.471005 before refining explicit Walk visibility. All history receipts/logs remain. Final narrower Definitions2.640816, Inputs2.473647, Exact2.482152, final Audit2.443765; maximum finite chunk4.670195. External binding9.924844CPU plus measured final generation gives108.816773accountedCPU, safely within the600CPU total budget. Every compiler invocation had45CPU hard limit and at most two workers ran concurrently.

No old module, old generic file, old graph, or old compiled cache was edited or recompiled. No native computation oracle, unproved axiom, installation, checksum, solver, or additional BFS was used. The only graph instance is the fixed O22 cubic-coset recipe. Root best-located public guarantee remains160750, so161150 is400larger within that located comparison; global record and priority are unconfirmed. New-scope external A/B/C reviews are separately root coordinated.

Authoritative result: `FINAL_COMPILE_RESULT.json`; binding: `INPUT_BINDING_CHECK.json`; final actual import/type/body/axiom output: `GQ77Cubic22Clone65Audit.log`. No further local compiler or numerical task is running.
