# Frozen static-pool calibration

2026-10-29, before the new distance computation.

Prediction: the 40 literal neighborhoods of accepted vertices 51417,…,51456 in the accepted final graph all independently R4-dominate original B0 on labels 0,…,51416, and every pair of neighborhoods has B0 set-distance at most 3. If true, all 40 are a feasible incumbent for a future static joint repacking model, with their actual old-port usage. This calibration produces no new graph or record and does not authorize joint optimization.

Old-scope check: the ledger entry `ddp-d13-singlefault-star-guard-mechanism-20261027` explicitly records a single original-B0 control (prototype3962 with saturated pin6216 deleted), and says the other39 were not recomputed on original B0. The continuation REPORT verifies the successive current graphs, which does not imply independent original-B0 coverage. No completed 40×B0 static gate was found in the targeted ledger/current-source/refresh scope check. Thus the full present calibration is new; the old successful sequence remains accepted regardless of this prediction.

Read only once:
`research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/continuation/graphs/graph_d13_D5_n51457.edges`.

Recover B0 by removing the final40 vertices. Check actual old-old edge count324451, extra incidence count412, no new-new edges, and397 distinct used old ports. Extract each S directly from the literal edge list. The inherited B0 D5 proof is not rerun.

Exactly40 multi-source BFS computations on B0, one for each S, truncated after distance4. Record old-target missing count/first witness. The same distance array computes distances to every other S, giving the780 unordered compatibility conditions d_B0(Si,Sj)≤3 without further BFS. Distances not found by depth4 are recorded as greater than4, not as exact values. Do all40 even if the prediction fails; a failure only means a static independent model omits earlier-added helper routes.

Check old-port multiplicity against B0 degree budget13; preserve all412 actual incidences and usage by vertex. One worker, at most5CPU seconds including compilation/preparation. No source-diameter BFS, newly constructed graph, joint MIP/SAT, pool expansion, guard search, or old current-R4 recheck.

## Authorized follow-up: multiplicities of these exact40 sets only

2026-10-29, appended before the multiplicity calculation. The static calibration has completed with all40 independent R4 covers and all780 compatible pairs. Test the concrete possibility of adding at least41 vertices by duplicating these same neighborhoods, without generating a new neighborhood.

For each saved S_i choose an integer k_i≥0. For every used old vertex v impose `sum_(i:v in S_i) k_i ≤ c_v`, where `c_v=13−degree_B0(v)` is already saved in `RESULT.json`. The known all-one vector has total40. Each extra vertex attaches to exactly S_i; repeated copies have mutual distance2 through any common neighbor, while distinct-set copies inherit set-distance≤3. Together with original-B0 R4 domination and the port inequalities this is a sufficient actual graph construction rule, not only a relaxed score.

First calculate `UB_i=min_(v in S_i)c_v` and test whether any set can be added directly to the all-one incumbent using its saved residual capacities. If every UB_i=1, total≤40 proves this exact40-set multiplicity pool closed immediately. If any direct duplicate is feasible, save its literal multiplicity vector and notify root before graph generation. Otherwise, only one existing integer-packing solver call with these40 variables may be used, at most5CPU seconds (or one existing SAT call limited5seconds); no install, new graph read, BFS, new pattern, second call, or pool expansion. Any total≥41 is delivered as construction parameters for root's generation/independent acceptance; infeasibility or UNKNOWN applies only to this fixed pool.
