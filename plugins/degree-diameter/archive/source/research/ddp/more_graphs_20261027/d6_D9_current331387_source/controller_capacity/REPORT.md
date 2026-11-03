# Six-dart phase capacity through length nine

The frozen prediction was that every phase has at least 6959 nonbacktracking words of length at most nine. It is supported: the exact minimum is **58581**, first attained at phase **23**. All minimum phases are `[23, 26]` and the maximum is 61067. The complete 49 endpoint counts, each depth's endpoint counts, and the depth-nine phase/last-dart counts are in `RESULT.json`.

The fixed phases are `[1,36,45,48,13,4]`, in the order three positive darts followed by their inverses. The inverse-index map is `[3,4,5,0,1,2]`. This is the parent/scout-bound phase normalization `j'=2j mod49` of source positive phases `[25,18,47]`. No source field law was approximated: this diagnostic deliberately retains only phase addition modulo 49.

The dynamic-programming state is `(phase,last_dart)`, with last index 6 denoting none only at the empty prefix. At a step, append any of the six darts except the inverse of the last one. Python unbounded integers count multiplicities; no word list is materialized. Counts by length zero through nine are `[1, 6, 30, 150, 750, 3750, 18750, 93750, 468750, 2343750]`.

The exact total, including identity, is

`1+6*(1+5+...+5^8)=2929687`.

The value 2929686 counts only nonempty prefixes and is one less than the usual Moore ball count. This arithmetic observation is not a source graph verification.

The whole DP worker used 0.027244 CPU seconds, including interpreter/setup and output, under a three-second RLIMIT_CPU hard limit. One worker, one run, no compilation. The process exited successfully and no handle remains active. `PREDICTION.json`, `count_dp.py`, `run.py`, `worker.log`, `RESULT.json`, and `terminal.json` retain the experiment.

The source scout supplied the next compatible prime 6959 before the prediction and run were frozen. The minimum 58581 passes its necessary raw route-count gate, but many distinct projected words may attain the same field endpoint. This is neither a complete field-image certificate nor a diameter result. No field image, source/new graph, BFS, parameter embedding, or solver was evaluated here. Any subsequent target experiment remains a separate, explicitly authorized producer task within the same source family.
