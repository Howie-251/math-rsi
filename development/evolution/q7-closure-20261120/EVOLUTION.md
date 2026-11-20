# Seven-dimensional matching extension · November 20, 2026

The November 19 research package gives a working proof for every matching of the seven-dimensional cube. Earlier public milestones were 57 prescribed edges at v5 and 56 at the fixed v6 tag. This update enters the ongoing v6 workflow on `main`. The source project records local adoption of MathRSI v3. The newer release numbers describe when the reusable methods reached MathRSI.

[Detailed mathematical proof and 26 appendices](../../../plugins/hypercube-hamilton/knowledge/q7-closure-proof.md) · [Source map](../../../plugins/hypercube-hamilton/SOURCE_MAP.md)

## Where the proof changed the workflow

Once the dense theorems covered every matching with at least 46 edges, a proof for each smaller size would have repeated work. Starting with the actual prescribed matching, add disjoint cube edges until no more can be added. A cycle containing the resulting matching still contains the original one. A counting argument forces such a terminal matching to have at least 45 edges. This leaves exactly one size of **maximal** matching outside the dense theorem. The separate E38 calculation excludes it and completes the implication.

The route, proof and verification skills now ask for a terminating operation that preserves the input requirements, a bound on its possible terminal objects and the exact domain of the theorem that accepts them. For a theorem covering just one size, a larger terminal object would still require a proof. These checks let the workflow stop generating intermediate layers once it can return a witness for every original input.

[Shared proof workflow](../../../base/skills/mathrsi-prove/references/actual-input-coverage.md#密层结论返回后先比较保留原要求的终端域)

## What belongs to the hypercube plugin

- Across a cut, the second face must accept the pairing actually produced by paths through the first face, with the original ports, partners and prescribed edges attached. The plugin records how a shared partition and an Euler tour can supply compatible labeled controls.
- In the 46-edge layer with minimum absolute directional imbalance two, the proof bounds the cost of unavailable or conditional choices on the same candidate grid. A failing 10-by-10 grid would cost at least 200, whereas the row and column budgets sum to at most 184. This permits unknown cases without treating them as successful calls. The integration checked the arithmetic against the supplied weight summaries. Its older source column table is listed as omitted.
- An alternating-path flip can establish a necessary structural condition even if it removes prescribed edges. To finish the target theorem, the proof returns to the original matching and uses the inclusion-preserving completion above. A Hamilton cycle for the flipped matching alone need not contain the original edges.

[Domain methods and concrete failure cases](../../../plugins/hypercube-hamilton/skills/mathrsi-hypercube-hamilton/references/q7-closure-methods.md)

## What a reader can reproduce

The portable E38 replay compiles both original C++ enumerators. One uses cube symmetries and the other enumerates raw face pairs. The geometric checker recovers the actual faces and signed imbalances, compares the complete weighted histograms, and checks the frozen outputs. The two counts refer to different universes: 35,360 individual faces, and 18,237,120 ordered cross-independent face pairs. The minimum maximum absolute imbalance in the four cases is 9, 11, 11 and 11. Each exceeds the necessary cap of 7.

The upstream audit classifies the full theorem as a working proof with imported results. The lite package omits some earlier rank and enumeration payloads. Access to the final replay alone therefore establishes only the finite E38 exclusion. Independent external refereeing and a full Lean formalization remain outstanding. The seven-dimensional prescribed-endpoint path theorem and dimension-independent extension with seven active directions remain separate questions.

[Replay and recorded results](../../../plugins/hypercube-hamilton/archive/q7-closure/README.md) · [Earlier dependency inventory](../../../plugins/hypercube-hamilton/archive/q7-closure/verification/DEPENDENCIES.json)
