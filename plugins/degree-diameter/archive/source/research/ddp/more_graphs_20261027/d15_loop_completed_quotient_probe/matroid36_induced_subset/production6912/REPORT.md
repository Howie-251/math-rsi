# Fixed mixed-alphabet induced graph: D4 prediction refuted

The unique prescribed subset produced a simple graph with 6912 vertices and 22896 edges. The actual degree range is 1..11, so the maximum-degree-at-most-13 prediction is supported. The diameter-at-most-4 prediction is refuted by the first checked root.

The subset is the exact ascending label vector supplied in ../source_vertex_ids.txt, comprising the intrinsic 36-point sets at all 192 controllers. Every edge of the old literal with both endpoints selected was retained; no edge was removed from this induced graph or added to it. New label is the zero-based position in that vector. The source edge file was read once; the old source's diameter was not recomputed and was not used to infer the induced diameter.

New root 0 is old source label 1. Its closed R4 contains 1296 vertices, with layer sizes [1, 6, 35, 208, 1046], leaving 5616 vertices outside. The first missed vertex is new label 4, old source label 9. This is a counterexample to D4 for this fixed graph; its exact global diameter, connectivity, and unordered bad-pair count were not computed. The remaining 6911 roots were unnecessary after this counterexample.

The actual degree histogram is {'1': 48, '2': 720, '3': 48, '4': 1152, '5': 1104, '6': 144, '7': 1392, '10': 1920, '11': 384}. Mixed endpoint port types prevent assuming that the attractive local count 3*3+2*2 is attained; even though this graph passes the degree gate, its connections do not preserve the old graph's four-step coverage.

This closes only the one fixed original-F3 C36 induced-subset rule. No alternative basis, subset, size, field, edge deletion, or seed was attempted. It does not exclude other graphs for (13,4), nor does it change any delivered lower bound.

Production aggregate CPU was 0.585443188 seconds including compilation, generation, and the one new-root R4 traversal. Driver PID was 2050254; the synchronous execution completed successfully. The input label gate used a separate prior 0.071742091-CPU run; combined gate plus production CPU is 0.657185279, below the 30-second budget. There were zero solver calls, zero old-source BFS traversals, one generated graph, one tested candidate, and no pending work.

Files: PREDICTION.json, INPUT.json, DEGREE_PROFILE.json, CASE.json, RESULT.json, TERMINAL.json, run.py, radius4.cpp, and the complete graph_induced_n6912.edges. Coordinate and degree hypotheses are recorded in ../ANALYSIS_SET_DEGREE.md and the intrinsic label pool.
