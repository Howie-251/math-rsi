# Independent literal acceptance prediction

Frozen on 2026-11-01 before reading the candidate contents.

This is one independent check of the single literal edge table
`research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq35_spread24/graph_d24_D3_n6160.edges`.
Expected order is 6160, edge count 73920, maximum degree at most 24, and diameter
exactly 3. This acceptance does not inherit any old-source diameter result.

The checker will read the stated header and every literal edge, require all
endpoints in 0..6159, reject loops and duplicate unordered edges, construct both
directions of every edge, verify reciprocal adjacency, and calculate the complete
degree histogram. It will then run ordinary queue BFS independently from every
one of the 6160 roots in that same literal graph. Each root must reach all 6160
labels at distance at most 3. This also establishes connectedness. Because
6160 > 24^2 + 1 = 577, the maximum-degree-24 radius-2 counting bound excludes
diameter at most 2; a PASS therefore establishes exact diameter 3.

If any condition fails, save a concrete header/count/edge/vertex or root-target
counterexample without modifying the candidate. Save the checker source, receipt,
summary, actual root count, per-root coverage, and process CPU. One worker, at most
30 CPU seconds for the acceptance run. Stop after this one complete candidate
check; do not rerun the 6144 source or the 4336 graph.

The only graph-data input is this literal edge table. Do not read producer
PARAMETERS, SOURCE_CHECK, EXTENSION_STEPS, RESULT, generator/code, proof, cached
coverage, or old-source-6144 materials. No solver, Lean, install, hash, checksum,
manifest, or public record claim.
