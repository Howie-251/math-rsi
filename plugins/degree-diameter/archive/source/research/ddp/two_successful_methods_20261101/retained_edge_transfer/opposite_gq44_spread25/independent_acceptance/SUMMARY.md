# Independent literal acceptance: PASS

The sole graph input was `../graph_d25_D3_n7242.edges`. `PRED.json` was frozen before inspecting that input. No producer parameters, source checks, extension steps, results, generator, proof, old 7225/6160 source material, or existing cache was read or used.

The literal header and parsed edge count are **7242 vertices / 90525 unordered edges**. The graph is simple and undirected, has no loops or repeated unordered edges, and has degree **25 at every vertex**. A full connectivity BFS reached all 7242 vertices.

A fresh ordinary C++ queue BFS was then run from each of **all 7242 roots** through radius 3. Every root reached **all 7242 vertices**, with zero missing targets. The 7242 individual records are in `roots.tsv`; each records shell sizes at distances 0, 1, 2, and 3, total reached, missing count, and eccentricity. The radius-2 shell ranges from 416 to 480 vertices, and the distance-3 shell ranges from 6736 to 6800 vertices.

The accepted graph has **exact diameter 3**: the complete all-root check proves diameter at most 3, while maximum degree 25 permits at most 1+25+25·24=626 vertices within distance 2 of a root, and 7242>626.

One worker was used, with a 30-second CPU hard limit per compile/check process. Measured checker CPU was **0.243566000 s** (0.026607000 s setup and 0.216959000 s all-root BFS). Compile plus checker child CPU was **1.229532000 s**. See `ACTUAL_CPU.json` and `RUN.json`.

Saved evidence: `check_literal.cpp`, `PRED.json`, `INDEPENDENT_ACCEPTANCE.json`, `roots.tsv`, `ACTUAL_CPU.json`, `RUN.json`, `SUMMARY.json`, and compiler/checker stdout and stderr. No graph repair, other graph instance, solver, Lean, installation, hash, checksum, or public-record claim was made.
