# Every adjacent single-vertex split of this9720 source fails

All81 controller-identity fiber representatives have an old distance4 target whose shortest paths begin through only one neighbor. This rejects every neighbor partition at each representative before any8192-assignment PropertyB loop is needed. Left controller automorphisms carry the81 representatives to every source vertex, so the entire fixed9720-source adjacent single-vertex split rule is excluded.

The source is Nishant Bhakar's14-regular9720-vertex route-chart graph. This is a new geodesic-support gate on that unchanged source, not a new source diameter validation and not the previous single seven-edge common hub. No candidate graph was constructed.

## Why the singleton is decisive

Let v be the split vertex, and partition its old neighbors into A and B. Keep every edge of G-v, retain v joined to A, add w joined to B, and join v to w. For an old target t with d_G(v,t)=4, let S_t be the first-neighbor support of all length4 geodesics from v to t.

If a length-at-most4 path from either split side uses the new v-w edge, identifying v and w projects it to an old v-to-t walk of length at most3, contradicting d_G(v,t)=4. Therefore each split side needs a length4 route starting with one of its own assigned old neighbors: S_t must meet both A and B.

When S_t is a singleton, one split side lacks that neighbor, so it cannot reach t within4. This argument rejects all partitions of that vertex, including any satisfying the degree limits |A|,|B|≤13. It is independent of whether other old-old distances could be retained.

## Exhaustive source scope

Vertices are(g,x), with g∈SL2(3)×Z5 and x∈F3^4. For every controller element h, the map(g,x)→(h*g,x) preserves adjacency: right multiplication by each controller symbol commutes with left multiplication, and the fiber chart depends only on the symbol. Every(g,x) is therefore the image of(identity,x), without requiring an automorphism between different fiber coordinates.

The81 representatives are the literal labels0 through80. Each received one BFS to depth4, with bitwise OR propagation of all geodesic first-neighbor masks before processing the next distance layer. Every representative has a singleton support. ROOT_RESULTS.jsonl saves one literal singleton witness per root, together with the distance4 target count and distinct support count.

Examples:

| Root | Old distance4 target | Only possible first neighbor |
|---:|---:|---:|
|0|83|398|
|1|82|397|
|2|81|396|

Thus no split of any of the9720 source vertices can give diameter at most4 under this exact adjacent split rule. The result does not exclude other sources, nonadjacent splitting, additional edge rewiring or multiple-vertex changes.

## Execution and saved evidence

PREDICTION.md froze the81-root scope before execution. The previous hub process's in-memory adjacency had not been persisted, so check.cpp reused its already executed recipe-generation block and INPUT.txt to reconstruct the same source. These81 BFS runs served the new complete first-step support calculation; no old-source all-root diameter validation was added.

Completed81/81; singleton rejections81; partition assignments tested0; new graphs0; old-old candidate BFS0; SAT calls0. Native CPU was0.036461 seconds; preparation, compilation and native work together used1.069389204 CPU seconds, below the10CPU budget. No background work or unfinished representative remains.

RESULT.json gives the complete-scope stop state, ROOT_RESULTS.jsonl the81 witnesses, TERMINAL.json the actual resource receipt, and check.cpp/run_once.py the executed implementation. No other split rule, source, seed or matching was tried after this conclusion, and no Wiki/root state file was modified by this worker.
