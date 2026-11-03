# Independent acceptance: PASS

The completed `../graph_d64_D3_n160050.edges` has 160050 vertices, 5121600 edges, degree exactly 64 at every vertex, and diameter exactly 3.

All literal edges satisfy the independently reconstructed adjacency formula. The literal graph and the formula graph both have degree 64 everywhere; therefore their edge sets agree exactly. Header, edge-line format, endpoint range, u<v, strict sorting, edge counts, and all degrees passed.

The fresh finite geometry check enumerated all 2850 rank-two RREF subspaces, obtaining 400 isotropic eight-point lines on 400 canonical points. Every point has eight incident lines. All 160000 point-line projection obligations passed, including uniqueness on all 156800 nonincident pairs. The 50 ordered GF49 spread lines cover each point exactly once. These full finite premises and the actual reusable short-walk proof establish every old-old, old-new, and new-new pair within three steps; see `PLAIN_PROOF.md`.

Literal queue BFS ran at exactly the 50 new roots 160000..160049. Each reached all 160050 vertices, with distance counts 1,64,3528,156457. No old-root BFS was performed. The all-pairs upper bound is supplied by the full finite-premise argument, not inferred from these 50 runs. Since 160050>1+64+64²=4161, the diameter is exactly 3.

Total measured child CPU, including both compilations, the geometry precheck, and the final literal run: 4.717618 seconds, single worker. The final validator used 1.864207 CPU seconds. No producer source, producer geometry, route cache, prior acceptance, solver, Lean build, hash, or install was used. This is mathematical/literal acceptance; a concrete Lean instance and public priority/global record certification are separate.

Files: `SUMMARY.json` gives the machine-readable outcome and timings; `NEW_ROOT_BFS.csv` gives every root; `INDEPENDENT_GEOMETRY.txt` records canonical point, line, and spread labels; `validator.cpp` is the complete fresh checker; compile and run logs are preserved.
