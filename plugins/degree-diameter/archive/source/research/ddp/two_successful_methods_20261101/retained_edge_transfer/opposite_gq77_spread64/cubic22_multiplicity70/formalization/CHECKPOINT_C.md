# A70 final closed instance

All4new modules and their separate Audit actualexit0, first attempt: Definitions2.100205CPU, Inputs1.992804, Exact2.536904, Audit2.372201. Total measured Lean child CPU9.002114; the two lightweight recipe-binding attempts add0.111096CPU, giving9.113210measuredCPU within300. One worker,60CPU per-module hard limits. All local tasks are terminal.

`formal/DegreeDiameter/Portfolio/GQ77Cubic22Clone70Exact.lean:21` proves the closed theorem

```lean
Fintype.card Vertex = 166650 ∧ (∀ v, graph.degree v ≤ 70) ∧
  DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
```

`final_claim : FinalClaim` is also closed. Both have no user certificate premises and depend only on propext, Classical.choice, Quot.sound. Separate `formal/GQ77Cubic22Clone70Audit.lean` imports Exact, checks the label/load/source/oldWalk bridges, prints the actual final type and body and FinalClaim, and prints all axioms. Its explicit `DiameterAtMost` output contains `@SimpleGraph.Walk.length`, so D3 is the actual bounded Walk predicate.

The carrier is literally `(Fin160000⊕Fin50)⊕Fin6600`, with explicit `label : Vertex ≃ Fin166650`. `clonePair : Fin6600 ≃ Fin6×Fin1100`; the center is `center65(pair.2)`, and `label_new_copy` gives160050+1100*copy+50*i+j. The graph body is exactly `FullNeighborhoodClones.graph OppositeGQ77Spread.graph center`; the source is the original closed160050graph, never the161150graph. All endpoints used by clone adjacency belong to that original source and new-new adjacency is False.

The new `load_le_six` uses the already proved base load≤1 to inject the adjacent clone-index subtype into its `Fin6` copy coordinate. Thus old degree≤64+6, while every new clone has source-center degree≤64. No source/clone-pair enumeration, center independence, or center injectivity assumption occurs. The source's actual WalkD3/no-isolates/nonD2 and the existing arbitrary-index clone Walk/collapse lemmas close the diameter claims.

`INPUT_BINDING_CHECK.json` and exported `FORMAL_ORDERED_CLONE_RECIPE.csv` compare all6600typed center/label rows with actual producer prefix rows. The fresh independent input recipe has the same O22 values, original spread order, source160050, and copy/base/new-label rule. Its actual `../independent_acceptance/SUMMARY.json` is PASS: all5544000literal edges bound, all6600immutable64-neighborhoods exact, all422400new edges, all5121600old edges retained, and0new-new edges. Formalization only read that actual summary and recipe;0large edgefile reads and0BFS were performed here. No Lean ASCII-parser theorem is claimed.

No old generic, graph, source, or olean changed; old415/24modules were only imported and not recompiled. No native computation oracle or new unproved axiom is used. This is only the fixed six-copy degree70instance. Root bounded best-located guarantee is164500, so166650 is2150larger within that located comparison; global record and priority remain pending. External A/B/C review and accepted-count updates remain root coordinated.

Authoritative receipt: `FINAL_COMPILE_RESULT.json`; actual final import/type/body/axiom output: `GQ77Cubic22Clone70Audit.log`.
