# P3: the prescribed second direction repair transfers the tight-route deficit

Status: controlled finite route-linear diagnostic complete; no two-edge graph generated or scored here. All15 nonzero branch directions on the one prescribed second edge were inspected. Every direction that repairs37<->63 damages other original unique4 slots. Per the fixed stop rule, this diagnostic closes without a third edge, more directions, full graph score, BFS, or solver.

## Feedback used to choose the second variable

Root already generated and independently checked the selected first-edge graph: fixed edge0->18 has b3, reverse_b9. It is connected8-regular on1152 vertices, actual D5 with13424 unordered pairs at distance>4, compared with the source's12384. The local predictions were exact: base0->10 had no missing fiber pair among all256, and37->63 plus its reverse each had128 missing ordered fiber pairs. The cached result is actual_prediction_check.json and its saved distances; this task did not repeat its BFS.

The fixed bad path is37-18-0-36-63. Its first two undirected edges belong to the repaired AACA path0-18-37-64-10. The first unshared edge is therefore0<->36, whose forward B relation is36->0. Only that edge's branch vector is varied. All matrices, zero offsets, all other143 branch relations including the first changed edge, and their inverse conventions are retained. This is a second finite diagnostic inside the existing edge-local construction model.

For every trial b, the reverse direction0->36 uses T_B^-1*b. The unchanged forward matrix has columns[14,4,8,9], inverse columns[12,7,2,4]. AACA does not traverse this second edge and was explicitly checked to stay rank4 for every trial.

## Frozen selection and predictions

The selection rule requires both37->63 and63->37 to return to rank4, then minimizes the total number of rank-deficient original unique4 ordered slots, then chooses the smallest integer b. It selects second_b1 and reverse_b12. Eight directions repair37<->63; the minimum remaining damage is4, attained by b1 and b8, with b1 selected by the tie break.

The repaired routes have columns:

- 37->63: [7, 4, 6, 11], rank4.

- 63->37: [10, 4, 6, 1], rank4.

The four damaged directed slots, two reverse pairs, are:

| source->target | unique route | columns after first change | columns after second change | rank | missing per input | ordered missing pairs |
|---|---|---|---|---|---:|---:|
| 2->36 | 2-38-19-0-36 | [3, 2, 15, 11] | [3, 2, 15, 12] | 4->3 | 8 | 128 |
| 26->68 | 26-36-0-19-68 | [6, 13, 10, 3] | [6, 5, 10, 3] | 4->3 | 8 | 128 |
| 36->2 | 36-0-19-38-2 | [6, 12, 14, 3] | [15, 12, 14, 3] | 4->3 | 8 | 128 |
| 68->26 | 68-19-0-36-26 | [14, 15, 13, 8] | [14, 15, 6, 8] | 4->3 | 8 | 128 |

Each slot has exactly one controller walk of length at most4. Its route image from a fixed fiber input has2^rank outputs, so a rank3 route misses8 of16 targets per input. The selected modification would therefore have512 ordered missing tight fiber pairs, or256 unordered pairs across fibers2/36 and26/68. These are exact local predictions, not a measured total bad-pair score of a two-edge graph. The old first-edge damaged pair37/63 is repaired, and the previously repaired0/10 slot remains fully covered.

## All15 second-edge trials

| second forward b | reverse b | repair37<->63 | total damaged tight ordered slots |
|---:|---:|:---:|---:|
| 1 | 12 | yes | 4 |
| 2 | 7 | yes | 12 |
| 3 | 11 | no | 2 |
| 4 | 2 | no | 12 |
| 5 | 14 | yes | 10 |
| 6 | 5 | yes | 6 |
| 7 | 9 | no | 8 |
| 8 | 4 | yes | 4 |
| 9 | 8 | no | 10 |
| 10 | 3 | no | 10 |
| 11 | 15 | yes | 12 |
| 12 | 6 | yes | 6 |
| 13 | 10 | no | 8 |
| 14 | 1 | no | 12 |
| 15 | 13 | yes | 10 |

## What this changes in the construction rule

This test was aimed at a specific prediction: a direction change outside the already repaired AACA route could restore the damaged tight route while preserving the first repair. That prediction is partly supported:37/63 can be restored and0/10 remains full. The stronger desired outcome, restoration without new tight deficits, is false for every one of the15 second-edge directions.

Thus a repair rule that checks only the chosen deficient slot is insufficient: in this concrete source, restoring it transfers rank loss to other unique-route pairs. A later construction retaining such changes must coordinate the affected tight-route directions jointly and preserve all468 necessary rank conditions, before treating local repairs as progress toward whole-graph coverage. This observation does not authorize or launch a new coupled search.

The proved finite exclusion is limited to first edge0->18 fixed at b3, second edge36->0 ranging over these15 nonzero vectors, and every other relation retained. Nonrepairing trials still fail the original37/63 tight route; all repairing trials have other deficient tight routes. Hence no trial in this specified15-choice slice can achieve D4. This is not the whole15-by15 two-edge parameter product, not all choices of a second edge, and not the general edge-local family. No claim is made about a generated two-edge graph's diameter or total bad count.

## Artifacts and stopping point

second_edge_analysis.json contains all15 full diagnostics, all468 rank arrays per direction, complete repair columns and damage records, exact local missing-pair predictions, and the fixed selection rule. analyze_second.py reproduces only this linear calculation. CPU time was 0.035942 seconds under a hard1-CPU-second process limit. Full graph generations0, scores0, BFS0, solver0, new seeds0, new lower bounds0.

The stop rule is met: all repair directions still damage tight slots. No two-edge graph is requested, no third edge is considered, and no cached distance computation is repeated. Existing first-step observed data remain in actual_prediction_check.json and controlled_distances.u8.bin for reuse.
