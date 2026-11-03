The frozen loop-completion prediction was supported for both actual sources. This is a different statistic from the ordinary 81-bin partition previously rejected for 15552; that historical failure remains unchanged.

For actual (15,4) n15552/m116316, all 15552 rows passed with 81-label bins (192 bins). For actual (15,5) n102060/m765045, all 102060 rows passed with 243-label bins (420 bins). At each original degree-14 vertex, the calculation adds one virtual count in its own source bin. Every completed row then has exactly five target bins with multiplicity three, and all vertices of each source bin have the same completed target-bin signature.

The first source has 648 virtual-loop vertices in 24 controllers; the second has 810 in 30 controllers. RESULT.json records the complete quotient relation table, loop-controller counts and labels of every virtual-loop vertex for each source. The files were read once each: the existing 15552 header edge list and the existing 102060 CSR. Source adjacency was never changed.

One process used 0.565593974 CPU seconds. No distances, balls, BFS, solver or new graph were computed. This certifies the specified loop-completed equitable five-by-three partitions only; it does not yet identify affine line charts or prove a new construction. No other block sizes or relabelings were tried.

Evidence: PREDICTION.json, run.py and RESULT.json. Historical ordinary-partition evidence remains at ../d15_D4_current15552/REPORT.md and SOURCE_PROFILE.json.
