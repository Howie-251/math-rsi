# Fixed-source matching-to-cycle surgery

Starting only from the saved balanced322 172-point graph, remove two parallel matchings between one pair of orbits and replace them with one cycle inside each endpoint orbit. Each vertex loses and gains exactly two neighbors. Nonzero cycle voltages are represented by1..21, since opposite voltages yield the same undirected cycle overF43.

The complete scope is ten choices of removed matching pair times21 squared, hence4410 actual graphs. All4410 were evaluated by complete BFS from the four translation-orbit representatives,17640 root runs total. No candidate improves the source258 bad pairs or has diameter3.

The sole saved minimum has473 bad unordered pairs,root deficits6/7/6/3,diameter4. It removes source edge indices0/2 between orbits0/1 and adds cycle voltages13/17. This is the capacity-best two-loop topology up to base-vertex relabeling. Its full14 voltage coordinates and602 edges are saved inbest.json/best.edges.

Root independently reconstructed the saved edges and checked all172 roots once: simple connected7-regular,D4,ordered distance histogram172/1204/7052/20210/946. See best.independent_check.json. SearchCPU1.413101311 seconds,independent finalCPU0.002978697 seconds. No restart,pendingempty.

This closes only these4410 modifications of one fixed source. It does not exclude arbitrary voltages of the resulting topology or other172-point graphs. The subsequent separately authorized full-coordinate profile is ../cyclic4_172_loop_search/; its source was this saved graph after an explicit gauge relabeling.
