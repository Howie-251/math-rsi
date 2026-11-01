# M=65 avoided-link experiment

The six-uniform avoided-link quotas improve the existing 1–3-lock certificates. They close the complete v=39 triple class and, with root's new degree≤12 triple selection, the complete v=37 triple class. They do not by themselves prove m(6)≥66.

Every lock center receives every avoidance subset R of the other locks, including R=empty (whole pool) and R=all other locks (singleton-type pool). The minimum weighted true bad-pair count is computed jointly, using integer cell capacities, with no duplicate deduction. See PROOF.md for the full valid formula and real-input requirements.

| Test | Profiles | Evaluations | Strict after refinement | Remaining | CPU seconds |
|---|---:|---:|---:|---:|---:|
| Original pilot domain, fixed positions/degrees | 195 | 195 | 105 | 90 | 0.50 |
| Remaining multi-lock profiles, center±3 / all degree orders | 79 | 8582 | 19 additional | 60 within these 79 | 28.80 |
| New v37 degree 8…12 triple domain | 70 | 320 | 70 | 0 | 1.00 |
| Independent complete-cell integer replay of new v37 | 70 | 210 centers / 621579 vectors | 70 | 0 | 0.34 |

The first two rows leave 71 of the original 195 profiles uncertified: v32/33 zero-lock (2), v34–36 single-lock (9), v37 old pair domain (4), v40 triple (21), v41 triple (31), v42/43 triple (4). This is a finite necessary-profile count, not a count of actual hypergraphs or distinct counterexample classes. Root has separate improvements replacing several of these domains.

At the original fixed layout, exactly seven prior failures are rescued: all four v39 triple failures, two v40 triples, and one v41 triple. In the v39 class the worst bound over all 40 profiles is 9314827/9345105<1.

For the new v37 triple selection, 68 profiles pass with selected consecutive positions (17,18,19), allowing degree-label permutations. Both all-degree-12 profiles use selected positions (15,16,17): tri=0 gives 5767609/5856840<1, and tri=1 gives 446447131/453905100<1. The worst bound over all 70 profiles is 2458/2465<1, at degrees [11,12,12], tri=0, ordered [12,12,11] at (17,18,19). Independent replay validates every selected certificate using full rectangular integer enumeration rather than the optimized forced-core method.

All comparisons use exact rational/integer arithmetic. Floating-point decimals occur only as display fields. There was no Lean work, whole-hypergraph enumeration, original manuscript edit, v2 access, or external model call. The total measured new CPU use is approximately 30.64 seconds. No cross-family or formal theorem review is implied.

Reproduction from project root:

```sh
python3 context/propertyb-m6-66-20261029/avoided/verify.py
python3 context/propertyb-m6-66-20261029/avoided/positions.py
python3 context/propertyb-m6-66-20261029/avoided/v37_three.py
python3 context/propertyb-m6-66-20261029/avoided/replay_v37.py
```

Exact evidence: RESULTS.json, POSITIONS.json, V37_THREE.json, REPLAY_V37.json. PROOF.md records the formulas, coverage dependencies and scope limits.
