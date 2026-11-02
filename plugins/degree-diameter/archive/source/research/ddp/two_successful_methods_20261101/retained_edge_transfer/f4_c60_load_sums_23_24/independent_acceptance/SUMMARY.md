# Independent literal acceptance: PASS

Candidate: order 4336, 48320 edges, maximum degree 23.

Degree histogram: `{"20":496,"21":64,"22":1472,"23":2304}`; old: `{"21":64,"22":1472,"23":2304}`; new: `{"20":496}`.

Literal old-old edges: 38400; retained source edges: 38400; missing source edges: 0; extra old-old edges: 0; new-new edges: 0.

Ordinary complete-graph BFS roots: 496 new roots, 0 old roots; candidate labels 0..4335.

All 496 new roots reached all 4336 vertices within 3 steps; this also proves connectedness. Both files passed literal header/count/range/simplicity checks. Reciprocal adjacency passed. Every new vertex has degree 20, and every neighbor is old.

The previously accepted source diameter bound and exact preservation of all 38400 old edges give old-old distance at most 3 without rerunning old roots. Combined with the new-root BFS this proves diameter at most 3. Since 4336 > 23^2+1 = 530, degree-23 radius-2 counting excludes diameter at most 2. Therefore the candidate has diameter exactly 3.

One worker; acceptance CPU 0.103144 seconds (user 0.099177, system 0.003967); wall 0.090065 seconds; CPU budget 20 seconds.

Graph data read: only the two literal edge tables named in PRED.md. Producer generator/code, recipe, owner, coverage cache, matrix certificate, GRAPH_RESULT, RECIPE, and TERMINAL were not read. No solver, Lean, installation, hashes, checksums, or artifact manifest. No public record claim.

Compiler CPU across two build attempts: 1.861806 seconds; build plus acceptance CPU: 1.964950 seconds, within the 20 CPU-second budget. The first build reported a C++ name collision; renaming the local JSON string helper fixed it before any graph acceptance run. Build details are in BUILD.txt.
