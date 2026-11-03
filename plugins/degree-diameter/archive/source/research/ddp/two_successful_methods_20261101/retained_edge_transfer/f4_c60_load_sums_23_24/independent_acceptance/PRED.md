# Independent literal acceptance prediction

Prepared before reading graph contents or producer results on 2026-11-01.

Scope: one bounded independent acceptance of the proposed undirected graph with
order 4336, size 48320, maximum degree at most 23, and diameter exactly 3.
The supplied prior acceptance of the 3840-vertex, 38400-edge, degree-20 source
and its diameter-3 proof is trusted; no old-root distance calculation is repeated.

Only these graph data files may be read by this checker:

- `research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/graph_d20_D3_n3840.edges`
- `research/ddp/two_successful_methods_20261101/retained_edge_transfer/f4_c60_load_sums_23_24/graph_d23_D3_n4336.edges`

Expected PASS conditions, all checked directly from literal edge pairs:

1. Both headers and literal edge counts agree with the stated orders and sizes;
   all endpoints are in range; neither file has loops or repeated undirected edges.
2. The candidate adjacency is undirected, has maximum degree at most 23, and its
   complete degree histogram is independently calculated.
3. Candidate edges with both labels below 3840 are exactly the 38400 source edges,
   including every source edge and no extra old-old edge.
4. There are exactly 496 new labels, 3840 through 4335. Every new vertex has degree
   20 and has only old neighbors; there are no new-new edges.
5. An ordinary queue BFS from each of the 496 new roots, in the complete literal
   4336-vertex graph, reaches every label within three steps. The checker reports
   all 496 roots and their covered counts, and runs zero old-root BFS traversals.
   These traversals also establish connectedness directly.

Under these checks, old-old distances at most 3 follow from the already accepted
source and preservation of all its edges. New-old and new-new distances at most 3
follow from the 496 literal BFS traversals. Since 4336 > 23^2 + 1 = 530, the usual
degree-23 radius-2 counting bound excludes diameter at most 2, so the diameter is
exactly 3. This is graph validity only, with no claim about public records.

If a condition fails, record a concrete edge, vertex, root-target pair, or count
counterexample and stop; do not modify the producer graph. If the candidate is
not present, prepare the checker and report READY without polling.

One worker, at most 20 CPU seconds per acceptance invocation; actual process CPU
and the number of BFS roots will be recorded. No solver, Lean, package install,
hash, checksum, artifact manifest, generator/recipe/owner inspection, coverage
cache, or matrix certificate is used. Reports are confined to this directory.
