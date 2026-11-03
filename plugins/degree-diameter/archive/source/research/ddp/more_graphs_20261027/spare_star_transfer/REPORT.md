# Complete spare-star rule: neither actual source has a legal false twin

The complete scans of the actual51417-point degree13 and94186-point degree14 sources found zero fullopen-neighborhood spare stars. The existence prediction is refuted. Completed-scan CPU totaled approximately0.6784s, with no BFS, coverage optimizer, hash, new graph or shared Wiki/HTML/ZIP update.

The exact rule is: choose an old vertexv such that every vertex of its complete open-neighborhoodN(v) has degree strictly below the cap. Add a new pointz joined to exactlyN(v), retaining all old edges. Its degree isdeg(v), the old neighbors each consume one free slot, and its routes to every oldx≠v reuse the old shortestv→x route after replacing its first point byz. The pairz,v has distance2. Thus a valid sourceD≤5 would give a complete newD≤5 graph without arbitrary setcover.

The current method ledger was checked before the scans. Existing entries cover these source bindings, degree filters, geometry pools, rare-degree subsets and bounded arbitraryfree-point coverage. The observed degree14 false-twin pair is not a prior complete spare-star scan. The older degree12 core-clone analyses concern a different actual host and a different neighborhood restriction, so these two fullsource scans did not repeat them.

| Actual source | Edge count | Vertices scanned | Legal prototypes | Minimum saturated neighbors | Vertices attaining minimum |
|---|---:|---:|---:|---:|---:|
| degree13, n51417 | 324451 | 51417 | 0 | 1 | 91 |
| degree14, n94186 | 657452 | 94186 | 0 | 9 | 20 |

All degree13 saturated-neighbor counts are1..13, with histogram{1:91,2:310,3:322,4:370,5:333,6:1303,7:3949,8:6053,9:10323,10:8853,11:11768,12:4041,13:3701}. The degree14 histogram is{9:20,10:242,11:1824,12:8858,13:27334,14:55908}. Every actual vertex is covered, not only an initially selected class.

Source51417 used its ordinaryn/m header. Source94186 has a commented "# n m" header; the initial parse stopped at that header before reading any edges, then the parser was corrected. The already completed51417 result was reused rather than scanned again. The corresponding JSON results record the full source bindings and histograms; uint8 files save the saturated-neighbor count for each vertex in label order.

This closes only the exactcompleteN(v), old-edge-preserving false-twin insertion rule on these two fixed source graphs. It does not close proper-neighborhood changes, edge deletions, rewiring, or arbitrary target graphs. No removal of one or two saturated neighbors or approximate-star search followed.

The same pure local interface is documented in INTERFACE.md and was sent to the expert fetching the degree15 source, for one cheap scan only after its actual complete source binding. No new source download was initiated here.
