# Independent literal acceptance: PASS

`PRED.json` was frozen before the two literal edge inputs were read. The sole graph inputs were the accepted `../../graph_d25_D3_n7242.edges` source and the new `../graph_d26_D3_n7531.edges` candidate. No producer pins, parameters, proof, results, generator, or packing cache was read or used.

The candidate header and actual edge count are **7531 vertices / 97750 unordered edges**. It is simple and undirected, with maximum degree **26**. Its degree histogram is **degree 25: 306 vertices, degree 26: 7225 vertices**.

The candidate's old-old edge set is exactly the source's **90525 edges**: **0 missing and 0 extra**. The **289 new vertices**, labels **7242..7530**, each have degree **25** and only old neighbors. There are **7225 old-new edges** and **0 new-new edges**.

Fresh ordinary C++ queue BFS through radius 3 was run on the complete 7531-vertex candidate from **all 289 new roots**. Every new root reached **all 7531 vertices**, with zero missing targets. Individual records are in `roots.tsv`; their distance-2 shell sizes range from 417 to 441, and distance-3 shell sizes range from 7064 to 7088.

**No old root BFS was rerun.** The old-old distance bound at most 3 is inherited from the source accepted independently in the immediately preceding task, because all source edges are retained. The 289 new-root checks cover all pairs involving a new vertex, so the whole candidate is connected and has diameter at most 3. Its diameter is **exactly 3**, since maximum degree 26 allows at most 1+26+26·25=677 vertices within distance 2 of a root, and 7531>677.

The one-worker checker used **0.064811000 CPU seconds**, including 0.054645000 seconds of literal parsing/comparison/setup and 0.010166000 seconds for all 289 new-root BFS checks. Compilation plus checker child CPU was **1.224059000 seconds**; each process had a 30-second CPU hard limit. See `ACTUAL_CPU.json` and `RUN.json`.

Saved evidence: `check_literal.cpp`, `PRED.json`, `INDEPENDENT_ACCEPTANCE.json`, `roots.tsv`, `ACTUAL_CPU.json`, `RUN.json`, `SUMMARY.json`, and compiler/checker stdout and stderr. No graph was repaired; no other graph, solver, Lean, installation, hash, checksum, or public-record claim was involved.
