# Two q13 order8-action controls — complete, no D8 graph

Both actual graphs have n=137904, m=413712, are simple connected 6-regular, and have **exact global diameter9**. The target was (6,8), saved baseline80050. The frozen prediction that restoring the source normal alpha action to order8 would give at least one D8 graph was refuted.

These were two newly constructed graphs, with one complete identity BFS each; no q13 result was inherited and the old source D7 BFS was not repeated. Left multiplication acts transitively on each right-step Cayley graph, so the identity eccentricity is the global diameter. The two identity R8 complements contain1762 and1624 targets respectively. Those are root-to-target counts, not ordinary unordered bad-pair counts.

The finite scope is exactly q13 with beta=[[0,12],[1,12]], chi17(alpha)=5, normal B=(0,1), C=(0,2), and the fixed source H48 phases/C17 coordinates. The alpha matrices are [[8,6],[1,5]] (square5I) and [[9,5],[1,4]] (square8I). Actual generator/inverse IDs and distance histograms are in RESULT.json; probe.cpp supplies the graph rule and inverse checks. The prediction and literal matrices are preserved in PREDICTION.json.

Native times were0.010722 and0.010853 CPU seconds; the recorded compile-and-native child total was0.811636 CPU seconds. Both controls completed, zero untried/unknown, zero new lower bounds. This batch is closed with no free-vector or extra-field search. The result does not exclude other q13 generators or modules; restoring action order alone was insufficient here.
