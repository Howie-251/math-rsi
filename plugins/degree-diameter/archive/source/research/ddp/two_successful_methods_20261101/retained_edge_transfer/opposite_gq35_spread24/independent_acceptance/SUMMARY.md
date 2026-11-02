# Independent literal acceptance: PASS

Order 6160, literal edges 73920, maximum degree 24; degree histogram `{"24":6160}`.

Checked 6160 roots by ordinary queue BFS in this candidate's complete literal adjacency. Minimum radius-three coverage: 6160. Eccentricity histogram: `{"3":6160}`. Per-root counts are saved in ALL_ROOTS.tsv.

The header, edge count, endpoint ranges, simplicity, reciprocal undirected adjacency, and degree bound all passed. Every one of the 6160 roots reached every one of the 6160 vertices within three steps, proving connectedness and diameter at most 3. Since 6160 > 24^2+1 = 577, the degree-24 diameter-two counting bound excludes diameter at most 2. The graph therefore has exact diameter 3. No source diameter was inherited.

One worker; acceptance CPU 1.080653 seconds (user 1.072649, system 0.008004); wall 1.071038 seconds; CPU budget 30 seconds.

Graph data read: only graph_d24_D3_n6160.edges. No producer PARAMETERS, SOURCE_CHECK, EXTENSION_STEPS, RESULT, generator/code, proof, coverage cache, or old-source-6144 materials were read. The 6144 source and 4336 graph were not rerun. No solver, Lean, install, hashes, checksums, manifests, or public record claim.

Saved ALL_ROOTS.tsv contains exactly 6160 rows, in label order 0..6159; all rows record reached=R3=6160 and eccentricity=3. Compiler CPU: 1.134173 seconds; compilation plus acceptance CPU: 2.214826 seconds, within 30 seconds.
