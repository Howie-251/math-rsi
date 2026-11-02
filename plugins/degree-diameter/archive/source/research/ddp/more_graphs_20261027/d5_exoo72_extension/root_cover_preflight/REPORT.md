# Exoo72 minimal matching insertion: complete root-cover preflight is empty

The specified73-point operation is completely excluded by its new-root requirement. All832020 three-edge matchings of the fixed Exoo72 source were considered, with all six choices of the endpoint not joined to the new point, giving4992120 operations. None has union of original closed radius2 balls of its five selected endpoints equal to all72 vertices. Since deleting edges cannot enlarge those balls, no operation can give the new point distance at most3 to all old vertices. No old-to-old check or candidate full-graph BFS is needed for this operation. The frozen prediction of at least one root-cover candidate was refuted.

This is not an exclusion of arbitrary73-point graphs, other deletion patterns, other attachment sets or other sources. No candidate graph or new lower bound was produced. The old source diameter3 was not rechecked.

## Source and exact operation

The existing local source is research/ddp/more_graphs_20261027/d3d4_transfer/source72.implicit_adj.txt. It contains72 implicit0based adjacency rows, each of degree5. SOURCES.json in that directory attributes it to Geoffrey Exoo via the maintained UPC Exoo_72.txt source. The preflight converts it once to a canonical180-edge list; source_edges.json records the sorted edge-ID mapping. Only input simplicity, symmetry and degrees are checked, without repeating source BFS.

For a three-edge matching M, let v be one of its six endpoints and let S be the other five. Delete M, add new vertex72, and join it to every vertex of S. The new graph would have73vertices and182edges. The new point and71 old points have degree5; the omitted old endpoint has degree4. Thus degree and parity budgets are valid. Its exact new-root radius3 requirement is

    R2_(G minus M)(S) = V(G).

The necessary inexpensive requirement is R2_G(S)=V(G). It already fails in every finite case, so no after-deletion union needs to be evaluated on a surviving candidate. Exact root-cover count0 follows from this necessary failure, not from thousands of candidate BFS runs.

## Structural simplification

Write uv for the deleted matching edge incident to the omitted vertex v, with u in S. The other two removed edges have both endpoints in S. Deleting any edge internal to a multisource set S does not change its closed radius2 union: if a path from S uses such an edge, restart at its later endpoint, which is itself a seed; if the edge is the last step, its destination is already a seed. The same reasoning works for simultaneous internal deletions. Therefore

    R2_(G minus M)(S) = R2_(G minus uv)(S).

This reduces any exact positive check to one orphan-edge erasure rather than three. The program precomputes original72vertex R2 bitsets and the180 single-edge-erasure R2 tables with literal length0/1/2 unions. No graph BFS is used. Because the original necessary pass count is0, the erased tables are not needed by any surviving case.

## Complete finite enumeration and stored output

The code enumerates a canonical orphan edge and its two possible orientations. It then chooses the other two edges in increasing edge-ID order, requiring all six endpoints distinct. This is a bijection with a three-edge matching and one omitted endpoint. Each matching contributes exactly six operations; the full count4992120/6=832020 is integral. The raw upper bound before disjointness is6*binomial(180,3)=5735160, so this is a small complete finite scope.

For each operation, the five-seed original R2 union is evaluated with two72bit words. Zero unions are full. RESULT.json records exact aggregate, per-omitted-vertex and per-orphan-edge counts. root_cover_candidates.u16.bin is the complete positive output and is empty. Its documented record format would contain the three sorted edge IDs and the omitted vertex, four native16bit integers. There is no first-positive graph or claimed diameter metric.

The initial ten-orphan-edge profile and full computation fit the fixed budget. Native CPU was0.014127seconds, compilation1.541390, and the driver measured1.556940 child CPU seconds in total, below30. All180 orphan edges and every finite operation reached terminal state. There was no solver, candidate or source BFS, old-to-old pair test, alternative insertion, seed, continuation or shared-Wiki update.

The5,3 ledger's W(3,3)80-point paired-matching model remains a different time-limited UNKNOWN experiment and was not resumed. The earlier fixed-source degree/slack screen only noted that Exoo72 is5regular and has no spare degree; this task genuinely changes the graph by deleting a matching. The present operation is now closed at the root-cover stage and should not be restarted merely with a longer window. A later task would need an explicitly different attachment/deletion rule or source.
