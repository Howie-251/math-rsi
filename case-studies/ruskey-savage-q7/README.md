# Ruskey–Savage Q7: dense matchings and complete E16 closure

[Six-domain index](../README.md#ruskeysavage-q6) · [Bilingual reader](../../development/homepage-redesign-20261105/site/q7.html) · [v6 changes](../../docs/V6_CHANGES.md) · [v5 changes](../../docs/V5_CHANGES.md) · [Hamilton plugin](../../plugins/hypercube-hamilton/README.md)

**Every matching of at least 56 edges (at most 16 holes) in the 128-vertex Q7 extends to a Hamilton cycle containing all its prescribed edges.** The earlier Q6 theorem still covers every matching in Q6; imported results also give the at-most-six-direction application in arbitrary dimension. Q7 deepens that same research domain across `v5` ($\ge 57$ edges) and `v6` (complete E16, $\ge 56$ edges).

## Results and open scope

| Input family | Established scope |
| --- | --- |
| Q7 matchings with at least 58 edges (E12) | Complete dense layers, providing algebraic construction tools for sparser layers. |
| Q7 matchings with at least 57 edges (E14) | Complete theorem (`v5`), combining the 14-hole assembly and all denser layers. |
| Q7 matchings with at least 56 edges (E16) | **Complete theorem (`v6`)**, combining adjacent-hole augmentation with all five independent 16-hole parity-gap classes $\mu \in \{0,1,2,3,4\}$ (parity/weight bounds exclude $\mu \ge 5$). Whole-proof audit: `PASS · same-family · provisional · sound-modulo-imports`. |
| Layers $\le 55$ edges (18–38 holes), full Q7, P7 and seven-direction extension | **Open.** |

A matching with $m$ edges has $128-2m$ unmatched vertices, or holes. Here $\mu$ is the minimum, over the seven coordinate splits, of the absolute difference between the two parity hole counts. Completed $\mu$ classes do not represent equal fractions of the remaining problem. The $\ge 56$-edge theorem retains every edge of the actual matching.

## Reusable mathematical methods

- **Control the auxiliary pairing (`v5`):** Choose a legal donor pairing so the actual compressed successor has the cross-edge interface required by the next proof step, then expand return bridges to restore all prescribed original edges.
- **Count the actual compatible pool & reuse theorems across splits (`v5`):** Count source fibers inside the true non-adjacent pool, and consume new theorems across known legal coordinate splits before dispatching residual work.
- **Gate splits on the hardest remainder & pair orbit bases with symbolic small faces (`v6`):** Probe candidate splits on the hardest open branch before adoption; combine the parameterized $Q_6$ $\Delta=2$ double bridge, the 41-orbit $Q_6$ $A_8$ theorem, joint even/odd CNF+DRUP pairs for $\mu=3$, and $S_6$ large-face independent-hole tables (`189` rows for $\mu=0$, `23` rows for $\mu=1$) paired with symbolic small-face holes after removing five incompatible inner-axis ordering constraints (`100,055 - 5 + 1 = 100,051` constraints).

## Research provenance and evidence

**Run: MathRSI v3 (local adaptation) + hardest-remainder E16 closure. Methods feed v5 and v6.** During `v6` maintenance, all 261 in-repo E16 files and all 290 bundled baseline imports (`7.98 MB`) passed byte and SHA-256 verification; [`check_e16_bundle.py`](../../plugins/hypercube-hamilton/archive/q7-e16/check_e16_bundle.py) recomputed the 189-row $\mu=0$ large-face table and ran four zero-dependency geometry/plan checkers (`MU0` $a=0$ census and plans, `MU0` $a=1,2$ orbits, and $Q_6$ $A_8$ 41-orbit census) alongside the `v5` S3/S2_STRONG, T63 target04 and $Q_6$ A10 checks. Ten large `.cnf`/`.drup` files (`532.49 MB`, up to `201.55 MB` `even.drup`) remain in the external `R-S-n=7(2).rar` archive and are recorded in [`INVENTORY.json`](../../plugins/hypercube-hamilton/archive/q7-e16/INVENTORY.json) (hashes identify external files and do not substitute for DRAT-trim replay).

[v6 implementation & checks](../../development/evolution/v6-c4free-rs7-20261117/EVOLUTION.md) · [E16 curated archive](../../plugins/hypercube-hamilton/archive/q7-e16/README.md) · [Earlier v5 implementation](../../development/evolution/v5-q7-20261114/EVOLUTION.md).
