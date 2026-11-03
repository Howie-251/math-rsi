# PSL25/unipotent-C5: fixed60 profile completed without a hit

The single authorized scope is complete: all60 external valence5 orbitals combined with the fixed valence1 matching were degree6 on1560 vertices, and none had full radius5 from the root. Total production CPU was0.319778456 seconds, including0.071286395 seconds of new-action preparation. There was no restart, field/subgroup followup or failed-graph export.

## Exact construction and checked scope

Reuse the saved GF25=F5[u]/(u^2-2) implementation, encoded a+5b. Recover the same7800 cached PSL matrices as the saved1950 C4 representatives multiplied by their saved4 stabilizer elements; the old elements() enumerator and old graphs were not run.

Set H={[[1,t],[0,1]]:t in F5}. Vertices are the1560 right cosets gH. Left multiplication by U(1),U(u),W supplies the new-action permutations; their root orbit contains all1560 vertices. The fixed matching is the unordered-pair G-orbit of {H,SH}, S=diag(2,3). An outside involution T supplies the valence5 unordered-pair orbit of {H,TH}; union gives degree6,4680 edges. These parameters define a candidate, not a successful D5 graph.

All frozen structural counts matched: |N_G(H)|=100,20 normalizer cosets;325 group involutions,25 in N and300 outside; the external involutions split into60 H-conjugacy classes of size5 with distinct root neighborhoods. The five involution matching cosets are one N-conjugacy orbit of the selected matching. Thus varying the matching within those five choices introduces no additional case when all60 outside classes are allowed: N conjugation preserves H and permutes those classes.

Every candidate's unordered-edge orbits were expanded under the three left permutations, checked simple and degree6 at every vertex, and scored by exact root R5. Since that same action is transitive and preserves each orbital, one full root would imply the whole graph has diameter at most5. The first new candidate received the authorized one-root ordinary R5 calibration, which matched the bitset set exactly. No old graph BFS, all-source BFS, old group regeneration or expanded independent group audit occurred.

## Failed prediction and actual coverage

P1 predicted that at least one candidate would reach all20 normalizer cosets within5. This is REFUTED: their normalizer reach ranges from2 to15. Outside-normalizer reach ranges from10 to1510 of1540.

The16 best cases (indices13,14,15,16,18,19,20,21,23,24,25,26,28,29,30,31) each reach1525 of1560 vertices. They miss5 normalizer cosets and30 outside cosets, total35. Hence even the best result is not only a far-outside coverage defect: the normalizer part remains incomplete as well. No new smaller bad-pair objective or matrix tuning is proposed.

Full per-case coverage is in cases.json; coverage_summary.json records the11 distinct coverage profiles. These are root radius5 missing-vertex counts, not unordered graph bad pairs. No actual diameter is reported for failed or possibly disconnected candidates. No lower bound, new complete graph, review or Lean result is claimed.

## Decision

Stop this fixed PSL25/C5 valence5-plus-normalizer-matching branch. The result excludes the frozen60 profiles (and their five equivalent matching placements) at the requested D5 target. It does not exclude other subgroups, orbital profiles, altered actions or general degree6 graphs. No automatic continuation is scheduled.

Artifacts: PREDICTION.json, PLAN.md, run.py, inputs.json, prepare.json, profile8.json, first_calibration.json, cases.json, coverage_summary.json, RESULT.json and terminal.json.
