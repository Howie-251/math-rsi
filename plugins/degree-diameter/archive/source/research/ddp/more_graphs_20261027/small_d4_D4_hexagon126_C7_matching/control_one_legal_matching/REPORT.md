# One first legal mixed matching: route-complementarity control

This is a single degree/girth control, selected without a D4 objective. Deterministic DFS chooses the lowest unmatched orbit and ascending eligible selector IDs, enforcing the cached exact self/pair girth conflicts. It found its first legal mixed matching after10 DFS nodes and342 selector trials: variables1,151,279,399,494,577,630,674,689. There are7 cross-part orbit pairs and2 within-part pairs. No second matching was chosen.

The complete graph control126.edges has126vertices,252edges, all degree4, retains every189sourceedge and passes a fresh no-cycle-of-length<=5 check. Connectedness and diameter upperbound6 are inherited from the retained connectedD6source. No source D6 check or full control diameter BFS was run.

From root0, all161 nonbacktracking prefixes of lengths0..4 were enumerated once, classified by their0/1/2 new matching edges. Immediate backtracks can be removed, so these endpoint sets are complete for the stated short-route questions. The closedB2 has17vertices, supporting B2 protection.

Among80 oldfar targets, exact0M covers0, exact1M covers39 and exact2M covers15. The1M/2M overlap is10, leaving5 targets exclusively reachable with2M:6,32,73,98,100. For target6 the actual path is0--37--38--25--6, with edge kinds M,G,G,M. Complete0/1M prefix enumeration finds no short0/1M route to that target, so the exclusive-two-M prediction is supported in this control.

The root0 R4 union has90vertices and misses36. These are one-root states, not ordinary unordered badpairs. It implies D>=5, while the retainedsource implies D<=6; exactD is unknown. The control is not a new record and does not refute the full matching family. The other17 representative roots were not checked. Worker process CPU was0.083566 seconds plus0.000475754 driverCPU; no solver or BFS was invoked. No score, seed, endpoint adjustment or second object followed this result.

The parent classified the saved exclusive targets using the known source D6 and parity:4 have old distance6 in the same part, and1 has old distance5 across parts. See ROUTE_COMPLEMENTARITY_SUMMARY.json; no graph or traversal was added for this classification.
