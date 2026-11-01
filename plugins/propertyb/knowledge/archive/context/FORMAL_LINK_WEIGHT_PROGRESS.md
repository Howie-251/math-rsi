# Profile-specific link weight certificates

`formal/Aris4Math/LinkWeightCertificates.lean` is frozen and built successfully on 2026-10-06. Twelve axiom audits include all eight corrected centers and the generic semantic transfer. Every audit reports only `propext`, `Classical.choice`, `Quot.sound`.

The finite `IncidentWeightBound` checks compare forward-plus-reverse weights only for profile types with a possible distinct actual pair. In a shared type, two actual distinct edges imply multiplicity at least two; the module proves this from `TableRealization`, rather than assuming it. Type comparisons and rational identities use `decide +kernel`; no actual hypergraph enumeration is performed.

The conclusions are genuine deletion inequalities for `directedBadPairs H (vertices j)`, with bookkeeping weights given by `Numeric.pairWeight` of actual `positionType`s:

| Theorem | Center | Required degree |
|---|---:|---:|
| `v21_d7_deduction_11` | 11 | 7 |
| `v22_67_deduction_12` | 12 | 7 |
| `v22_77_deduction_11` | 11 | 7 |
| `v22_77_deduction_12` | 12 | 7 |
| `v23_66_deduction_11` | 11 | 6 |
| `v23_66_deduction_12` | 12 | 6 |
| `v23_677_deduction_12` | 12 | 7 |
| `v23_677_deduction_13` | 13 | 7 |

Each theorem assumes actual pair coverage, an actual `RealizesProfile`, a real locked index with the stated position, and its degree. P8 supplies the count of bad pairs; the result is `Numeric.deduction` bounded by the actual sum of distinct deleted directions.

For the last 23-point center, the actual fibers for `[11,13]` and `[12,13]` have cardinality one each. Their union has at most two actual edges and creates at most one exceptional unordered pair. The proof allows that pair to be bad and to have zero weight. The remaining guaranteed slot contributes at least `3/323`.

`ProfileDeletion.lean` will provide the uniform all-position deletion family. Endpoint/pair probability aggregation and branch existence remain in other modules; these certificates do not assert the full theorem.

Evidence: `.aris/traces/proof-checker/2026-10-06_run08/lean-link-weights-build.log` and matching metadata.
