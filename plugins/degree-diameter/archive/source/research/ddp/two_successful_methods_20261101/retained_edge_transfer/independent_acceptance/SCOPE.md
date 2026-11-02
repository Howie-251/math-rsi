# Two terminal graphs: independent literal-edge acceptance

Prepared before execution, 2026-11-01. This is the same-family ARIS research-review / proof-checker task. Its deterministic checks can support acceptance; subjective research assessments remain provisional.

The complete numerical run has one Python standard-library worker, a 45 CPU-second hard limit, and a 44 CPU-second profiling alarm for a clean incomplete result. No installation, upgrade, search, checksum, archive test, or rerun of the old 3,750 BFS roots is authorized here.

The only graph inputs are these literal edge lists, with paths relative to the repository root:

- `research/ddp/refresh_20261029/f5_full_d20_D3/graph_d20_D3_n3750.edges`: previously accepted 3,750 vertices / 37,500 edges.
- `research/ddp/two_successful_methods_20261101/retained_edge_transfer/graph_d21_D3_n3900.edges`: target 3,900 vertices / 40,500 edges / maximum degree at most 21.
- `research/ddp/two_successful_methods_20261101/retained_edge_transfer/graph_d22_D3_n4125.edges`: target 4,125 vertices / 45,000 edges / maximum degree at most 22.

The old `INDEPENDENT_VALIDATION.json` is used only for its existing overall full-root D3 PASS, root count, and graph-identity fields. No production recipe, generator, coordinate formula, cached ball, or earlier BFS distance array is used by the checker. Project instructions and the new handoff define the evidence boundary.

For every edge list, parse the actual header and every edge row, require the advertised n and m, check endpoint labels, loops and duplicate unordered edges, reconstruct symmetric adjacency, and check degrees. An edge row denotes one unordered edge; this encoding is not a directed adjacency-list format.

For each new graph, verify that all 37,500 literal old edges survive with the same labels. Run an independent, three-layer BFS from every newly labeled vertex (150 roots 3750..3899, or 375 roots 3750..4124), using that terminal graph's full literal adjacency. Require every such BFS to reach every terminal vertex. Save every checked root's layer sizes, reached count and eccentricity, or the first counterexample.

The distance proof is exhaustive by pair type. Old-old pairs retain paths of length at most 3 because the old graph has an accepted full-root D3 result and every old edge is retained. Any pair with a new endpoint is covered by a new-root BFS; undirectedness covers both orders. Thus the union proves all terminal pairs have distance at most 3 without repeating old-root BFS. A new-root layer at distance 3 also proves diameter exactly 3.

Only the two named terminal graphs are eligible for this acceptance. Checking 525 new roots across those two graphs does not independently accept 525 construction prefixes. Public maxima for degrees 21 and 22 are unknown in this task, novelty remains pending, no global-record claim is made, and Lean formalization of either new graph remains incomplete. Stop after this acceptance; do not open another search.
