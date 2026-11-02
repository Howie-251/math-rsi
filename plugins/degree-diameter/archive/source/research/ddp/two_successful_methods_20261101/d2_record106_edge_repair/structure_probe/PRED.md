# Structure that could change the D2 generation rule

Do not rerun source validity, the252 failed anchors or the joint MILP. Use
the already bound source106 and saved critical-edge profiles. Budget5CPU
seconds, within the original whole-case20CPU account.

The eight labels F={7,17,23,34,46,54,59,105} recur in the route constraints.
New falsifiable structural prediction: fixing those eight labels pointwise
leaves an order-seven automorphism, with the other98 labels partitioned
into14 orbits of size7. Refine colors using fixed-label adjacency, propagate
only unique-neighbor-between-color equations, and verify every actual edge
of each complete returned permutation. If propagation is incomplete, report
UNKNOWN rather than pretending to have found a full automorphism. No general
graph-isomorphism search, new controller or solver is authorized here.

Specific route predictions:17 and105 have equal open neighborhoods. The
nonadjacent pair7,12 has exactly those two common neighbors. Removing just
one edge7--17 or7--105 retains the other route; removing both removes both
routes. In the proposed two-repair pattern, new edges64--7 and7--5 restore
the previously missed pair64,5 but cannot repair7,12, since12 is adjacent
to neither64 nor5. Check these controlled routes directly, with no BFS or
full candidate graph generation.

Derive the number of single-common-neighbor pairs by summing the existing
directional critical-target lists and dividing by2. This is a readout of
saved profiles, not a newly predicted count or a source revalidation.

Return the actual orbit/permutation data and route witnesses. A verified
order-seven action would motivate a new symmetry-preserving internal-rewire
construction on a seven-point orbit plus3/4 fixed points; it would not prove
the existing UNKNOWN model feasible or infeasible.
