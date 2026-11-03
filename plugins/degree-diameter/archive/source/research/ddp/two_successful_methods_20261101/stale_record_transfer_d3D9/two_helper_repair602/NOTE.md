# Exoo600 adjacent-helper repair sample

Actual status: UNKNOWN_10000_SAMPLE_NO_HIT. Tested 10000 distinct configurations to a terminal decision. Both helper roots passed radius9 in 0; 0 of those then failed an old-old pair. Stage counts and first actual counterexamples are in RESULT.json; ATTEMPTS.csv records every sampled configuration. The original600 graph was never distance-validated again.

The prediction that some candidate preserves new-old coverage was not supported in this sample. Old-old testing is only reported for candidates that passed both helper roots. A sample with no hit is UNKNOWN about the full rule. No claim of an exhaustive negative result or a new graph is made without a saved full candidate and root acceptance.

The operation keeps every source vertex cubic: six cut endpoints each lose exactly one edge and gain exactly one via repair or helper. Each helper has two old pins plus the peer edge. The only allowed old modifications are the three cuts and single original nonedge repair. A hit has602 vertices and903 edges. This differs from the old AFY70/D5 source and the Exoo600 branch that stopped solely at a false bipartite premise.

Exact cooperative helper routes and old-old route cases are in PAPER_NOTE.md. Ordinary BFS was performed only on modified602-vertex candidates, with both helpers first; old-labelled BFS rows are final-candidate checks. No source-wide original D9 BFS, symmetry search, solver, Lean, web or review was run.

Budget includes conservative preparation0.2CPU, actual compiler1.056955000 and run child0.116409000, plus driver CPU. Total1.414801274/20CPU, one worker. All processes terminal; fixed seed202611010309, no automatic retry or extension. Root owns acceptance, counts and global documents.
