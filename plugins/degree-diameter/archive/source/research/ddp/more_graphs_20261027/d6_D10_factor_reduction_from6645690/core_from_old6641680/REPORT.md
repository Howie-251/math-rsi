# Old6641680 seed: both small-core necessary gates pass; target batches not run

The actual available primary is the **old6641680** Cayley recipe, not current6645690. The current graph's small algebraic recipe remains unbound; see the source agent's `../../d7_D10_current6645690_source/VERSION_GAP.md`. No factorization-based current-source model was substituted. The old seed uses AUTHOR LEFT law, normal83021=61*1361, phase80 and action4400. Its exact primary files and arithmetic receipts are linked in the combined raw input.

The fixed core keeps F1361/action317 and phase80, giving108880 vertices. Positive normal/phase darts are `(824,38),(625,3),(1089,58)`, with true inverse darts `(1057,42),(769,77),(951,22)`. The retained involution is **(1109,40)**, not zero. `CORE_INPUT.json` preserves both original and projected labels.

| Necessary rule | Full core BFS | Required radius missing | Minimum raw count | First minimum (phase,normal) |
|---|---|---|---|---|
| Remove h: degree6 / targetD10 | all108880 reached; exactcoreD9 | 0 outsideR10 | 67 | (17,395) |
| Keep h: degree7 / targetD9 | all108880 reached; exactcoreD8 | 0 outsideR9 | 81 | (31,684) |

Both minima exceed the13-lift threshold. Exact raw prefix totals, including identity, are14648437 through length10 for degree6 and14108774 through length9 for degree7. The complete endpoint multiplicities are saved as the two `.u64le.bin` arrays; `RAW_COUNTS_SCHEMA.json` gives their encoding. Histograms and depth totals are in `RESULT.json` and the two rule JSON files. DP retained the original inverse-letter map, even if projected labels could coincide; it never merged words based on their core endpoints. The code checks that positive raw support equals the corresponding complete BFS-radius support.

These are **core results only**. They are necessary for the proposed1415440-vertex lifts and do not prove target coverage. The exactcoreD9/D8 values must not be recorded as target diameters. The original6641680 source was not BFS-reproduced; the only two BFS runs here were the authorized108880-core runs. No13-component image, target graph, target BFS, solver or225-setting family was evaluated.

The paper-only `../ANALYSIS_GATE_METHOD.md/json` proves the source, gate, normalization and conditional-connectivity scope. All valid F13 actors are1,12,5,8. The trivial actor has183 nonzero projective normal classes; each of three nontrivial actors has14, giving225 representatives **per rule**, with h smallnormal0 forced when kept. The now-proved core generation supplies that paper's onto-core premise. This complete small-normal question is saved, not executed; no zero-hit or UNKNOWN result is attributed to those225 settings.

Native work used 0.054323 CPU seconds; whole native-process usage was 0.056097, compilation 1.027350, driver 0.002397. Aggregate observed CPU is below30. After compilation the native hard limit was28 CPU seconds, within the total30CPU budget; one worker, exit0, completed checkpoint2/2, no live session remains.

The target batches are **not started and deferred under the user's small-degree/small-diameter priority**. This is not an infeasibility claim. A future explicit choice may reopen the saved finite target question, but no large batch or different template is dispatched now. Source/version audit, the two gates and the paper normalization form one family record.
