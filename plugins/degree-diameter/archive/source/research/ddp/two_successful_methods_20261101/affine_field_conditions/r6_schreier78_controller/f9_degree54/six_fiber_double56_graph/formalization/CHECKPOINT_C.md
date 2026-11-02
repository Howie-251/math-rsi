# Final U6/57834 concrete target and separate Audit

All4new modules actually exit0: Definitions, Inputs, Exact, separate Audit. `formal/DegreeDiameter/Portfolio/F9SixFiberDouble56Exact.lean:21` proves

```lean
Fintype.card Vertex = 57834 ∧ (∀ v, graph.degree v ≤ 56) ∧
  DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
```

`final_claim : FinalClaim` is also closed. Both original targets have no user certificate premise and use only propext, Classical.choice, Quot.sound. The separate Audit imports Exact, prints the actual graph/center/label and target type/body, checks the source-label/owner/load/oldWalk bridges, and prints final axioms. Explicit DiameterAtMost printing contains `@SimpleGraph.Walk.length`.

The carrier is literally Fin56862⊕Fin972 with explicit `label : Vertex ≃ Fin57834`. BaseIndexFin486decomposes as Fin6×Fin81; CloneIndexFin972as Fin2×Fin486. The closed labels give baseIndex=81*uIndex+9*a+b, cloneIndex=486*copy+baseIndex, source center729*U[uIndex]+a+9*b+81*GF9mul(4,a), and newlabel56862+cloneIndex. U remains exactly[0,1,2,3,9,15]. The graph body is precisely `FullNeighborhoodClones.graph F9Graph56862.graph center`, using the original56862source, never the current55graph or an evolving center neighborhood.

The new reusable `sourcePlaneMap_injective` is closed for every actual controller and port. It transports equality through the actual source dart inverse and the controller0matrix into the already proved55pinMap_injective. No field/inverse-basis check is repeated. Therefore `common_plane_pin_index_unique` needs only the selected controller target double-index injection; it does not require equal charts and may be reused for a separately authorized global fiber set. The actual U6target injection and36same-zero chart facts are kernel checked. These give base load≤1; projection of adjacent clone indices to Fin2gives load≤2. No center independence or owner-injectivity assumption is used. Source degree≤54and the closed original source WalkD3/nonD2combine with the existing clone Walk/collapse lemmas to close the target.

Production already closed the1587762-edge file before this Lean scope and immediately handed it to fresh independent acceptance. That acceptance actually binds all1535274old edges,52488new edges and972immutable fullN54rows, with0new-new edges, old load0:30618/2:26244anddegree54:31590/56:26244. Its972new-root BFS histograms all match[1,54,2478,55301]; it ran0old R3BFS and did not repeat old field/controller checks. The new lightweight `INPUT_BINDING_CHECK.json` compares all972typed producer/independent rows by explicit j, correctly permitting the independent interleaved physical row order. Formalization reads0large edgefiles and runs0BFS; no Lean ASCII-parser theorem is claimed.

All Lean attempts total14.534063CPU, including the2retained elaboration failures. Recipe binding uses0.017030CPU, giving14.551093measured compiler-plus-binding CPU, safely below300. One compiler worker and60CPU module hard limits were used. Old54/55/generic sources and oleans were only imported, never edited or recompiled. All local tasks are terminal.

Root's confirmed published-source guarantee57568is266below57834within the bounded comparison; global record and priority are unconfirmed. The U6instance is preserved. The separate given-U7finite interface and root's broader controller-packing question do not alter this target, and no U7graph was produced here. Accepted counts and A/B/freshC remain root owned.

Authoritative receipt: `FINAL_COMPILE_RESULT.json`; actual final import/type/body/axiom output: `F9SixFiberDouble56Audit.log`.
