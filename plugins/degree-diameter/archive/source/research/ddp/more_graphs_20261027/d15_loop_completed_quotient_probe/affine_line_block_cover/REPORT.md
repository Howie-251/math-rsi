The frozen affine-line block-cover certificate was tested completely on both actual sources and returned rawUNSAT in each one-call small CNF. This is a source-row variant, not a new method or a general15-pin exclusion.

|Source|Raw affine lines|Positive unique block masks|Block-union misses|Five-largest-column bound|CNF variables/clauses|SolverCPU|
|---|---:|---:|---:|---:|---:|---:|
|15552 / D4|2808|312|0|290≥192|1872 /3614|0.552736|
|102060 / D5|3510|390|0|915≥420|2340 /4700|0.223832|

Each actual27-point free fixedspace contributes all117 affine lines:13 directions and9 cosets. The column of a line was computed by OR of its three existing original R3/R4 ball masks, then marking only fibres whose every original target bit was present. No single-word rank criterion or approximate coverage replaced this cached test. Equal block masks retained their deterministic first witness at the same conservative cost3. Any selected groups would have been merged to distinct old pins before adding an edge, so overlapping lines would never duplicate a spoke.

Both complete block unions and the elementary at-most5 capacity gates passed. Each source then received exactly one full block-cover plus at-most5 CNF, with CaDiCaL8-second internal wall limit and10/11-second OS CPU limits. Both returned20 without any SAT witness. No proof trace was checked, so these are raw solver UNSAT results. No graph or candidate pin set was exported.

The whole worker used3.856504860 aggregate parent-plus-children CPU seconds, including3.079936860 parent preparation/decode CPU. Configured limits were35 aggregate and10 preparation CPU seconds. Session48313 exited0; RUN_HANDLE and RESULT are terminal. There was no retry, seed, extra time, new ball or source BFS.

Only the sufficient certificate requiring each entire target fibre to be covered by one selected affine line is rejected here. Multiple selected lines might instead combine proper subsets inside the same target fibre; ordinary individual-pin covers and general graphs remain outside this result.

Evidence: PREDICTION.json, run.py, both source*_LINE_BLOCK_MASKS.json files (all raw lines and exact deduplicated columns), source*_RESULT.json, the two CNFs/stdout/stderr, and RESULT.json. RAW_ANALYSIS_FIELDS.json is for merging this variant into the two existing source records. Independent paper review is recorded in ANALYSIS_LINE_CERTIFICATE.md/json when ready.
