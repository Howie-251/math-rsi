# Ruskey–Savage Q7: every matching extends

[Six-domain index](../README.md#ruskeysavage-q6) · [Bilingual public reader](../../development/homepage-redesign-20261105/site/q7.html) · [v6 changes](../../docs/V6_CHANGES.md) · [Hamilton plugin](../../plugins/hypercube-hamilton/README.md)

**The complete R7 author working proof covers every ordinary short-edge matching in the 128-vertex $Q_7$, of any size from 0 to 64, including empty and perfect matchings.** A Hamilton cycle contains all its prescribed edges. The source project accepted this working proof on **2026-11-19**, with status `sound-modulo-imports · same-family · provisional`. External peer review is pending; there is no Lean formalization.

## From dense layers to every matching

1. **E36:** every $Q_7$ matching with at least 46 edges extends to a Hamilton cycle retaining all its edges.
2. **Maximality bound:** double counting alone gives at least 45 edges in every inclusion-maximal $Q_7$ matching. **E38** excludes exactly 45, yielding at least 46; this lower bound does not depend on the older dense-layer theorems. The E38 directional argument reduces a hypothetical maximal 45-edge matching to legal pairs of 19-hole faces; none satisfy the necessary directional conditions.
3. Add free cube edges to any original matching $M$ until it is inclusion-maximal, obtaining $N\supseteq M$. Apply E36 to $N$. Its Hamilton cycle retains every edge of $N$, hence every edge of $M$.

The reduction preserves all original edges: it does not flip or discard them, nor take an arbitrary 46-edge subset of a larger matching.

[Detailed guide and 26 source appendices](https://github.com/lisresearchgroup/math-rsi/blob/main/plugins/hypercube-hamilton/knowledge/q7-closure-proof.md) · [Archive and recomputation commands](https://github.com/lisresearchgroup/math-rsi/blob/main/plugins/hypercube-hamilton/archive/q7-closure/README.md)

## Evidence and verification scope

- **Complete source argument:** the author package connects E36, E38 and the edge-preserving maximal extension. Its internal acceptance is same-family/provisional, modulo the stated imports.
- **Actual local recomputation:** two original C++ programs were compiled and run on Mac. They count **35,360 legal single faces** and reconstruct **18,237,120 ordered face pairs**. **Zero pairs satisfy the directional necessary conditions** for a maximal 45-edge matching. These are face/pair counts, not numbers of matchings or coverage percentages.
- **Whole-proof review boundary:** some large older-layer certificates are absent from the supplied lightweight package, and the complete imported chain was not replayed end to end. Local E38 recomputation does not replace that replay or external peer review. No Lean proof is supplied.

## Fixed releases and current maintenance

| Entry | Scope at that snapshot |
| --- | --- |
| Q6 / v3 | Every matching in $Q_6$; the checked A10 replay rebuilds 1,024 forests and 1,048,576 connectivity bits with rank 1,024. The prescribed-endpoint $P_6$ path theorem, with published lifting results, gives the at-most-six-direction consequence in arbitrary dimension. |
| [v5](../../docs/V5_CHANGES.md) | Every $Q_7$ matching with at least 57 edges; additional 56-edge structural families. |
| [Fixed v6](https://github.com/lisresearchgroup/math-rsi/tree/v6) | Complete E16: every $Q_7$ matching with at least 56 edges, across all five 16-hole parity-gap classes $\mu\in\{0,1,2,3,4\}$. |
| v6 `main` follow-up · 2026-11-20 | Full R7 author working proof covering all matching sizes, accepted in the source project on 19 November; bounded Mac E38 recomputation as above. |

**Research provenance:** MathRSI **v3 with local adaptations** was adopted in the original project; v5/v6 absorb methods and results. This is not a claim that a published v6 run generated the proof. The older English manuscript in the package proves only the ≥57-edge result and is retained as historical material, not as the full R7 proof.

## Methods and remaining questions

The earlier layers retain controlled auxiliary pairings, cross-split theorem reuse, hard-remainder probes and joint orbit/symbolic-face models. The final closure couples the dense-layer theorem with a global obstruction to small maximal matchings, then returns to arbitrary inputs through monotone edge addition.

Free-root Hamilton paths $P_7$, seven-direction lifting in higher-dimensional cubes and the general dimension-$n$ Ruskey–Savage conjecture remain open. The established $Q_6$ theorem is unchanged; the at-most-six-direction consequence uses the prescribed-endpoint $P_6$ path theorem and published lifting results.

[Historical E16 archive](../../plugins/hypercube-hamilton/archive/q7-e16/README.md) · [v6 release implementation](../../development/evolution/v6-c4free-rs7-20261117/EVOLUTION.md) · [v5 implementation](../../development/evolution/v5-q7-20261114/EVOLUTION.md)
