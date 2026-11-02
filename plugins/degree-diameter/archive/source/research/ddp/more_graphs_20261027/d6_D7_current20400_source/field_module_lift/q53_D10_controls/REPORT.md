# Two fixed q53 degree6 / diameter10 controls — complete, no hit

Both specified semidirect Cayley graphs have **exact diameter 11**, so neither improves N(6,10). Each is simple, connected, degree6, order 2,292,144, with 6,876,432 edges. The prediction that at least one would have D≤10 was refuted. Only these two controls were executed; both reached terminal results, with no unknown or unattempted control.

The first alpha matrix [[49,10],[6,4]] gives 5,596 vertices outside the identity R10; the first is vertex335. The second [[3,38],[41,50]] gives 6,886 outside R10; the first is vertex86. These are **single-root target counts**, not unordered bad-pair counts. Complete distance histograms and actual new inverse generators are in RESULT.json. No failed edge-list artifact was exported.

The group and literal adjacency are specified in MODEL.json. In both cases the normal module is F53², with a C17 coordinate and H48 written beta^u alpha^v. The beta action is [[0,52],[1,52]], alpha acts by the chosen matrix, and its C17 action remains multiplication by5. Positive generators are A=(0,0;0;0,1), B=(0,1;1;1,12), C=(0,2;5;2,11). The projective relation C_normal=2B_normal is retained. This constructs new groups rather than treating the new matrices as automorphisms of the old 20,400-vertex graph.

MATRIX_VALIDITY.md/json records the prior small-matrix verification: T1²=23I, T2²=30I, the two scalar squares are −1, T has order8, beta has order3, and T beta T^-1=beta^-1. The native producer used the new semidirect inverse formula and checked all three two-sided inverse pairs and six distinct nonidentity generators. Those facts establish a simple undirected 6-regular Cayley graph. One complete identity BFS per graph reached all 2,292,144 vertices; left multiplication is transitive and preserves right-step edges, so its eccentricity is the exact global diameter. This did not repeat the source D7 BFS or the chi5/chi6 quartic experiments.

The producer uses implicit right-product neighbors and O(n) distance/queue arrays, without a 2809² addition table or a stored full adjacency. Native CPU was 0.241240 seconds; total driver, compile and child CPU was 1.049406 seconds, below the 5-second budget. Reproduce with `python run.py` in this directory. `PREDICTION.json` is the frozen pre-execution prediction, `checkpoint.json` is terminal.

The finite scope is closed: exactly q53, these two matrices, chi17=5 and the prescribed B/C normal vectors. No other q53 vectors, matrices, fields, or arbitrary graphs are excluded. No additional search follows this no-hit result.
