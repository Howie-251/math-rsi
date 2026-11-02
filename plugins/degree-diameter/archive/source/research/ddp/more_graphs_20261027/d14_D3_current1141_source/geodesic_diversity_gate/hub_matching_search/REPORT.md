# Source1141: global seven-matching-edge / one-hub construction model

The single bounded MILP run ended **UNKNOWN, with no incumbent**. HiGHS reported a time limit and primal_status None. No modified graph, new-root BFS, old-root BFS, or lazy counterexample round was executed. The necessary-model-feasibility prediction remains unknown; this is neither a construction nor an infeasibility result.

The fixed operation deletes exactly seven pairwise-disjoint edges from the existing actual1141/7987/full14regular source, then adds vertex1141 adjacent to the fourteen distinct cut endpoints. All other old edges remain. A successful object would be1142/7994/simple14regular/D3, beyond saved lower bound1141. Published source D3 is inherited; the source and its A²/A³/support caches were reused without source distance BFS or walk recomputation.

## Joint model and independent paper check

The initial model has1,141 binary endpoint variables x_v and7,987 binary cut variables y_e. It imposes sum y=7 and x_v=sum of incident y_e at each old vertex, so the cuts form a matching and the hub has fourteen distinct pins. All1,141 old closed-R2 balls must contain a pin. It also contains all173,821 cached unique-three-path critical-middle constraints y_uv≤x_p+x_q. A bounded strengthening adds14,125 unique-first-loss rows: for each directed source edge with singleton far-first support, only its lexicographically first target t is used, giving y_uv≤sum_{s∈N_G[t]}x_s. The complete starting model has9,128 binary variables,190,229 rows and986,560 nonzeros. The objective sum x is the constant14, so it does not optimize bad-pair scores.

debruijn independently proved the following exact lazy condition before the run. Source pairs at distance≤2 remain within distance3 under a matching cut and endpoint hub. For a source-distance3 pair p,q, D3 holds precisely when some old3path survives all cuts, or p is a pin and N_G[q] contains a pin, or the symmetric condition holds. For each old3path P, an auxiliary r_P has upper bounds r_P≤1−y_e for each path edge. Hub auxiliaries satisfy a≤x_p and a≤sum_{s∈N_G[q]}x_s, with b symmetric; the OR is sum r_P+a+b≥1. Auxiliary variables may be continuous in[0,1] because x/y are binary; no lower reification is required. Closed neighborhoods include the endpoint itself. ANALYSIS_D3_CONSTRAINTS.md/json contains this proof and its scope.

The producer would construct and check every incumbent's actual modified graph, collecting at most32 source-distance3 counterexamples to add these exact OR rows. At most ten incumbent rounds were allowed within the same budget. No incumbent was found, so none of this conditional graph verification or lazy generation ran. The prepared native verifier was compiled but never executed.

## Actual execution and stop

Preparation including imports and cache/model construction took0.815519 CPU seconds. There was one solver call, round0; status1 / HiGHS status13, time limit, objective null, no incumbent. The worker's final in-process snapshot was59.491913 CPU seconds. The enclosing process receipt, which includes interpreter exit and all descendants, records **59.627412 CPU seconds**; native verifier compilation was a separate0.761742 CPU seconds. The hard worker limit was60 CPU seconds and the worker exited normally with code0. Solver threads and numerical libraries were restricted to one.

RUN_HANDLE.json and terminal.json are terminal UNKNOWN rather than stale SOLVING states. The saved cursor is round0 with9,128 variables and190,229 rows. Empty INCUMBENT_ROUNDS.json and LAZY_PAIR_CONSTRAINTS.json reflect zero actual candidates and zero lazy pairs, not missing results. RESULT.json, LAST_SOLVER_RESULT.json and PROCESS_RECEIPT.json preserve the actual outcome and cost.

Actual new graph order, diameter and ordinary unordered bad-pair count remain null. No new lower bound or exact exclusion was obtained. Even a future floating MILP infeasibility message would need to be distinguished from a strictly checked exact infeasibility proof; this run did not report infeasibility at all. The batch stops here without more CPU, cuts, helpers, sources or parameter variants.

To reproduce this fixed batch, run `python research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/hub_matching_search/run.py` from the project root. This is a reproduction command, not an automatic continuation request.
