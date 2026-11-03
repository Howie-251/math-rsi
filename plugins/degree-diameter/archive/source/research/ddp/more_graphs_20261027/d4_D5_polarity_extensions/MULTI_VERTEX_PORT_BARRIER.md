# Fixed H3 host: at least14 helpers after the13-tree capacity closure

This is a consequence of the actual shared port data, not a search or a general impossibility theorem for(4,5). The host is the natural364-point/714-edge polarity graph, whose28 degree3 vertices are its only free old ports at maximum degree4. Distinct ports are at distance exactly5: the saved R4 data excludes every other port, and the inherited host has diameter5.

Consider a diameter-at-most5 extension retaining all host edges, adding no old-old edges, and placing new-old edges only where the degree4 limit permits. At most one new edge can meet each old port.

Every one of the28 ports must receive a new neighbor. Otherwise, from any new vertex to an unattached port p, take the last entry into the old host along the path. It enters at a different port q. The remaining old segment has length at least5, in addition to the entering edge, so the path is longer than5.

The subgraph H induced by the new vertices must be connected. A path between different components of H must cross the old host between two distinct attached ports. Such a passage costs at least1+5+1=7. A port cannot join two new components because it has only one free slot. Thus two different H components would contradict diameter5.

With k new vertices, H has at least k-1 edges. Counting degrees of new vertices gives

    4k >= 28 + 2|E(H)| >= 28 + 2(k-1),
    hence k >= 13.

Therefore this entire old-edge-preserving, no-new-old-old-edge extension class has no solution with1..12 new vertices. The single365 and two-root366 failures are instances of this common port-spacing obstruction. At k13 equality forces all28 ports to be used, H to be a tree, and every old and new vertex to have degree4; it would be a377-vertex graph.

The subsequent finite cached-mask probe in helper13_tree_probe/REPORT.md now excludes this entire k13 case. Every helper leaf has3 attached ports. Every helper must be at H-distance≤4 from each such leaf, or its attached old port cannot be reached within5; a detour through two old ports costs≥7. Thus H has diameter≤4.

Writing the tree as a center with b≤4 branches and k_i≤3 second-level leaves gives1+b+Σk_i=13. For b3, k=333. For b4 with any k_i3, a leaf in that branch has15 foreign leaf-cell interiors that must be covered solely by its own R4 triple. Actual exhaustive3276-triple masks give good(T)=∅ in every case, excluding both forms. The sole remaining form is b4,k=2222. Its leaf tripleT and parent portp must cover18 foreign cell interiors through R4(T)∪R3(p). Actual exhaustive81900(T,p) masks again give good(T,p)=∅ uniformly. R2 cells partition the host, so other-helper contributions cannot fill these foreign interiors.

Consequently a successful extension within this stated class would now require at least14 helpers. No14-helper construction or search was initiated. Added old-old edges, deleted host edges, different hosts and arbitrary(4,5) graphs remain outside this result; no arbitrary377-point graph is excluded.

Evidence: source_and_single/PORT_BINDING.json; source_and_single/PORT_BALLS.json; source_and_single/PORT_CLASSES.json; two_root/RESULT.json; helper13_tree_probe/{CAPACITY.json,PARENT_PORT_CAPACITY.json,REPORT.md}. The initial degree barrier was a paper deduction; the later3276+81900 checks reused existing masks with no new BFS.
