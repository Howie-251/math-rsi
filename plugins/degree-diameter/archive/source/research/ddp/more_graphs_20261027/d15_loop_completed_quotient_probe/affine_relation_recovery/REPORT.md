The frozen affine-relation prediction passed completely for both actual sources. This resolves their compact affine interface in the specified labels; no alternative coordinates, block sizes or frames were tried.

- Actual (15,4), n15552/m116316: 192 controllers with F3^4 fibres of size81; all960 directed quotient arcs and all77760 arc-input rows match exactly.
- Actual (15,5), n102060/m765045: 420 controllers with F3^5 fibres of size243; all2100 directed quotient arcs and all510300 arc-input rows match exactly.

For a local offset x, the coordinates are its little-endian base-3 digits. Every directed arc has the exact completed relation y=B*x+c+t*v for t=0,1,2. Its direction is normalized at the first nonzero coordinate j. The row0 and basis inputs determine the candidate via Q_v(y)=y-y_j*v, and every literal three-output set was then compared with that candidate. Basis fitting alone was not the acceptance condition.

The original 648 and810 degree-14 points receive their virtual selfloops only during this calculation. The tables reconstruct the original graph by removing outputs whose full vertex label equals the input vertex label; outputs in another controller with the same local offset are retained. Thus the saved tables determine every original adjacency, including all exceptions previously appearing as degree14, with no change to the actual graph.

`source15552_AFFINE_RELATIONS.json` and `source102060_AFFINE_RELATIONS.json` contain every directed arc's B,c,v, pivot, and encoded column values. `generator.py` reconstructs adjacency from either complete table and can export the same source edge set if requested. It was saved without running an extra graph export or distance check.

One worker used0.803465985 CPU seconds, including input reads and both complete recoveries. Each actual source input was read once. No BFS, ball, solver, new graph, or diameter verification was run; published source D4/D5 remains inherited. This is a source-interface result, not a new lower bound or a claim about possible new connections.

Evidence: `PREDICTION.json`, `run.py`, `RESULT.json`, both relation tables, and `generator.py`. The preceding loop-completed equitable check is preserved in `../RESULT.json`; the old ordinary uncompleted partition failure remains unchanged. Independent algebraic review is recorded separately in `ANALYSIS_AFFINE_CERTIFICATE.md/json` when ready.
