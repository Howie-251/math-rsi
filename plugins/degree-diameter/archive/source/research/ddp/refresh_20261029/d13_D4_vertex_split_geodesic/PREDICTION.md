# Frozen adjacent single-vertex split gate on the literal 6804 source

Use only `research/ddp/more_graphs_20261027/d13_D4_current6804/source6804.edges`, whose complete source recipe is saved beside it. A targeted query of this source's experiment directory and corresponding ledger records found no prior single-vertex-split/geodesic-support test; the two matching-hub branches are different and remain stopped.

Operation: replace one vertex v by adjacent vertices v_A and v_B, assigning each of its 13 original neighbors to exactly one side A or B. All other adjacency is unchanged. The degree cap 13 requires 1<=|A|,|B|<=12. This task checks only the necessary distance gate and never generates a changed graph.

For each old target t at distance 4 from v, let S_v(t) be the set of neighbors that can be the first step of an old shortest v--t path. Both split vertices can be within distance 4 of t only if S_v(t) meets both A and B. A path that first uses v_A--v_B would contract to an old path of length at most 3, contradicting d_G(v,t)=4. Conversely, a supported first step gives an old shortest route on its assigned side. Targets at old distance at most 3 can be reached from the other side using the new joining edge, so this test exactly addresses the two new-root radius constraints; old-old distances remain a separate question.

Thus a singleton support rejects every partition of that root. If no singleton occurs, test all 2^12=4096 partitions modulo exchanging A and B, fixing the first sorted neighbor in A. Save all passing partitions, without treating them as full diameter-4 graphs.

All 6804 roots are represented by the 81 vertices with controller identity and fiber codes x=0..80. Indeed every source edge is a right-controller-symbol transition with a fiber rule independent of the controller. Left multiplication L_h(g,x)=(hg,x) preserves each edge, including the central plain matching. Taking h=g^-1 sends any root (g,x) to (e,x) and transports every partition and support set. No claim about the full automorphism group is needed.

Prediction: the distance-4 support constraints may close this whole adjacent single-vertex-split family; no success is assumed. For each of the 81 representative roots, perform one BFS through radius 4, propagating the bitwise union of all shortest-path first steps. A singleton is a decisive witness; otherwise the complete Property-B check decides the root gate. If a partition passes, notify the parent before any changed-graph work.

Budget: one worker, at most 10 CPU seconds. No candidate graph, candidate BFS, additional source, different split operation, solver, or hub continuation is authorized.
