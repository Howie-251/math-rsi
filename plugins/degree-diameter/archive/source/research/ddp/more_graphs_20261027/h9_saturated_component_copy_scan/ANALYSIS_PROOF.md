# Saturated-component copying: sufficient whole-graph rule

Status: **VALID sufficient construction theorem; no component scan or BFS performed by this paper**.

Let G be a simple graph with maximum degree at most Delta and diameter at most five. Let C be a complete connected component of the induced graph on the saturated vertices {v:deg_G(v)=Delta}. Require:

1. The induced graph G[C] has internal diameter at most three.
2. Every c in C has at least one neighbour outside C.
3. Every outside vertex x satisfies |N_G(x) intersect C| <= Delta-deg_G(x).

Keep every old edge. Add a disjoint copy C', copying every internal edge and connecting c' to exactly the old outside neighbours of c. No edge is added from C' directly to old C.

Each new c' has the same degree as c, namely Delta. Old vertices in C gain nothing; an outside x gains exactly |N_G(x) intersect C| edges, which fits its actual current deficit by condition3. Distinct new labels and source simplicity give no loops or duplicate edges. If s=|C| and e_C is the number of internal edges, the new order is n+s and the number of added edges is Delta*s-e_C.

Old-old distances do not increase. For a new c' and an old target t outside C, take a shortest source c-to-t path. Copy its internal prefix until its first exit from C, use the shared old boundary edge, and retain the remaining old path verbatim. This has the same length at most five, even if the remaining old path re-enters C.

For a new c' and old t in C, move inside C' to t' in at most three steps, then use t'-x-t through any outside neighbour x of t. The total is at most five. Two new points in the same C' are connected internally in at most three steps. These cases exhaust all vertex pairs, proving diameter at most five without any old-graph distance computation or full R4 test.

The internal diameter is essential: distance at most three through old vertices outside C would not certify a path inside C'. Completeness of the saturated component ensures every boundary vertex is unsaturated, but does not ensure enough slots when it is adjacent to several C vertices. The multiplicity/deficit check remains mandatory. This theorem is sufficient; failure of one premise does not exclude a different copy or cooperation rule. Each later application must use the actual accepted current graph and current boundary deficits; no simultaneous unchecked batch or inclusion of unsaturated vertices is authorized here.

## The proposed degree12 P3 is already load-blocked

The existing paired-clone cache `../h9_paired_full_neighborhood_clone_rule/BINDING_RESULT.json` binds saturated vertices28565 and36331 in current42402. Both have the saturated neighbour27674, so they belong to the same saturated component whether or not that component is exactly a P3.

Their shared old neighbours3467,6041,12679,24577,29213 and36095 each have degree11 and therefore only one cap12 slot. All six are unsaturated, hence outside the full saturated component. Copying that component would add at least two incident edges to each of them, violating condition3. Expanding the saturated component cannot absorb these unsaturated boundary vertices. Thus the particular component containing both proposed leaves is already blocked by saved data; no new lookup of the centre's neighbours or radius calculation is needed for that conclusion.

This does not exclude other saturated components in the same graph or the other assigned sources. The producer's one finite five-source component scan is separate numerical work. This paper does not invent a result for that scan or trigger an unsaturated-component variant.

Evidence: the parent-frozen component rule and existing accepted D5 source receipts; the degree12 counterexample uses only the saved paired-clone BINDING_RESULT, not a repeated source scan. Paper execution: zero graphs, components enumerated, BFS, R4 calls or solvers.
