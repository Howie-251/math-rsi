# Former1118 supplies graph annealing, not a transferable algebraic rule

2026-10-27. Disposition: stop this lineage analysis; do not reproduce its score optimizer.

Only the primary PR457 HOW_WE_FOUND_IT.md, how-we-built-it/README.md and sa2_opt.c were downloaded and read. The account is credited to the handle mizopl; this is not evidence of an identity with Ryosuke Mizuno. No1118 or1117 graph was downloaded, parsed or verified, and no source recipe was compiled or executed.

The vertex set is simply an arbitrary explicit input seed plus k new labels. load_seed_graph reads that seed (sa2_opt.c lines136–172); warm_start_insert sets N=N0+k (lines205–212). For the reported run, k=1 and N0=1117. No group elements, geometric coordinates, incidence construction, voltage fibers or parameterized algebraic edge formula is supplied.

The code first greedily deletes seed edges one at a time, retaining a deletion only if its full distance evaluation still has zero violations (lines174–201). It computes(D−1)-balls and greedily connects new vertices to deficient old vertices with maximum marginal coverage and randomized ties (lines214–260). If slots run out it can delete an old edge and attach both endpoints to the inserted vertex (lines262–284).

Repair is general graph modification: adding an edge between deficient vertices near a bad pair (lines353–377), targeted shortcut rewiring starting at line378, and arbitrary random two-switches (lines430–448). The main loop restarts this optimizer and gives near-misses additional temperature schedules (lines595–663). Old-old edges may change, so this is not a monotone single-vertex extension theorem or a preserved global route rule.

HOW_WE_FOUND_IT.md lines5–7 reports an1117 seed with7785 edges,68 degree13 vertices and1049 degree14 vertices; eight redundant-edge deletions gave84 free slots. It reports attaching new vertex1117 to fourteen deficient vertices, initially leaving49 distant pairs, followed by annealing/polishing to zero. The reported1118 output has7809 edges,34 degree13 vertices and1084 degree14 vertices. These are primary author/submission facts, not numbers recomputed here. The search narrative itself is marked contributor text rather than a proof.

The technical changes are a new-vertex loss screen and multi-temperature polishing. They may improve the same heuristic but do not supply a new mechanism for raising the current1141 record. The earlier1117 seed's own origin lies outside these files; it has not been proved devoid of geometry. However, the supplied1118 procedure does not preserve or identify such a structure, so no recursive seed chase is justified from this account.

SOURCE_RECEIPTS.json and the three saved files provide provenance; RESULT.json lists exact code sections and reported metrics. This task produced no graph, BFS, solver call, search run, new dependency or shared Wiki/delivery change. It is terminal.
