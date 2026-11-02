# Checkpoint B — load-bearing connections

Status: local source implemented; only modules with an exit_code0 build receipt are kernel verified. The configured Gemini B call returned an output-token-limit ERROR without substantive findings; B remains pending, with no automatic repeat.

Read actual source bodies in formal/DegreeDiameter/Portfolio/F4Graph3840{Field,,Routes,Linear,RouteData,Certificates,Diameter}.lean and generator formalization/generate_lean.py, and the original PARAMETERS/generate/PROOF/ROUTE_CERTIFICATE. Do not infer completed Lean compilation from the existence of these files.

The key general reduction additive_ext uses the three-coordinate basis decomposition and F-linear maps. The concrete reverse_matrix proof only needs basis equality and transported direction equality; it does not assume the whole theorem. It establishes the per-dart reverse, including matching port4 with opposite-end inverse matrices, then removes graph symmetrization and bounds each neighborhood by an image of Fin5×F.

For D3, routeForward consists of three actual forward edges; bounded_walk_of_route constructs a real SimpleGraph.Walk, conditional only on the two exact endpoint equations. The final diameter proof supplies both for arbitrary Fin3840 u,v.

For nonadjacent/equal controller layers, controllerWord is read from the3300 saved rank-route certificates. The generated nbInverse is an exact GF4 inverse of the three-column route-noise matrix. nb_basis_valid kernel-checks the composition with that inverse on all three basis vectors for every nonadjacent controller pair. route_noise_add/smul and additive_ext promote the basis equality to every Vec. The final caller uses noise to reach target minus route center.

For adjacent layers, the generated finite decoder chooses before/after backtracks and noise to hit all64 zero-source targets for each300dart. These are local affine certificate calculations, not graph BFS or solver. adjacent_valid kernel-checks the actual three-step vector endpoint. route_before_center/route_after_center use the already-proved per-edge inverses, so the decoder's center is the direct edge's linear action for every source coordinate. The final caller again subtracts that center. The code does not require an unproved projective-plane counting theorem.

Attack the basis-to-all-vector implication, reverse-dart dependence on controller source, exact finite coverage and actual caller hypotheses. No hcertificate or equivalent premise may remain on the final theorem. Distinguish any implementation error in an uncompiled file from a gap in the mathematical reduction.

## Executed compression bridge and current finite state

The graph's original matrixData definition remains unchanged. F4Graph3840FastTables.matrix_eq_fast was kernel compiled (18.91CPU); it proves all300 original matrices equal the selection from25 repeated matrices. Its actual transitive axioms are propext, Classical.choice, Quot.sound. Finite vector checks rewrite with that proved equality, reducing repeated literal expansion without changing graph semantics.

The internal decoder tables are losslessly interned:3600 NB inverse entries select402 distinct matrices, and300 adjacent darts select25 distinct64-target decoder arrays. RouteData compiled in12.18CPU after this representation change. There is no theorem assumption asserting that the decoder works; every actual caller remains checked against routeVec of the original graph.

Current Row00 has been kernel compiled against these compressed definitions (29.27CPU), discharging its55 nonadjacent controller words, their3 basis decodes each, and5×64 adjacent zero-source targets. Remaining independent rows01–59 are being checked in3 workers, each -j1 and at most115CPU; the aggregate reservation bound is2400CPU. The authoritative live state is CERTIFICATE_BATCH_HANDLE.json, and per-module receipts determine which rows have actually passed. No uncompiled row is yet claimed proved.

The now-compiled common decoder-to-all-vectors argument and adjacent route centers are factored into F4Graph3840DecoderInterface.lean. The actual final arbitrary-u,v argument is in F4Graph3840DiameterInterface.lean (kernel compiled1.97CPU): its three local-decoder premises are explicit development interfaces. F4Graph3840Diameter.lean supplies those premises from Certificates, rather than exporting them as inputs to diameterAtMost_three. Read both actual caller and interface. The lower-bound Walk argument is in F4Graph3840Lower.lean (kernel compiled9.32CPU, standard axioms).
