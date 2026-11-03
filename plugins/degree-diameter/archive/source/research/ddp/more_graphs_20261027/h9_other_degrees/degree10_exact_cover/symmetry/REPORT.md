# Degree10 coverer symmetries: only one verified involution

The frozen prediction that the specified coordinate symmetries would reduce the 364 pins to a few orbits was refuted in this tested collection. All 5616 SL3(F3) matrices and the single J were tested against the exact 26117 distinct coverer rows. Only the identity and A=[[2,1,2],[0,1,1],[0,0,2]] pass. J fails at row0. This collection does not include every JA product or the full hypergraph automorphism group.

For each candidate we compute the actual projective permutation on the calibrated 364 H3 pin coordinates, check bijectivity, try 16 fixed row probes with early rejection, then test every row for surviving candidates. Both passing permutations map all 26117 rows bijectively onto the original rowset. Their full column permutations, matrices, candidate rejection records and explicit row image maps are saved in RESULT.json and verified_row_maps.u16.bin. No geometric extension to the whole graph is assumed.

The nonidentity permutation is an involution. BFS using only verified generators gives exactly 192 pin orbits: 20 singletons and 172 pairs. The generated verified group has order2. The native run used 0.154927 CPU seconds and 58311 exact rowset membership tests. This is at most a factor2 reduction, not a useful few-case split.

For completeness orbit_cases.json records a lossless 192-case disjunction. Any nonempty feasible cover has an earliest selected orbit. A verified generated permutation transports one selected member to its representative while preserving the hypergraph, cardinality and all orbits. In that case fix that representative selected and all earlier orbits unselected. Do not independently orient the 172 pairs: the verified action is one simultaneous involution.

No MIP was started, no new graph was generated and no full graph distance BFS was run. N10 exact10-pin feasibility remains UNKNOWN from the earlier time-limited solve. This weak symmetry entry is stopped. A separately authorized new coordinate action is studied in the sibling symmetry_g2_root directory; these SL3 results are retained unchanged as evidence of this collection's scope.
