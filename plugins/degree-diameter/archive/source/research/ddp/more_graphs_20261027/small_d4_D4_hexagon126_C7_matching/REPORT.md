# Hexagon126 C7 matching: UNKNOWN solver, supported route control

The sole exact-model SAT call returned **UNKNOWN with no witness**. It did not return SAT or UNSAT, and it does not exclude this matching family. A separately authorized first legal matching supplied a useful route control, not a new record.

| Stage | Actual result |
|---|---|
| Source | Official LCF126 graph:126 vertices,189 edges,degree3. Girth12/D6 inherited from the primary description. |
| Exact model | 696 matching selectors;60066 total variables and178695 clauses. One60-second CaDiCaL call, exit0, no model. |
| Control graph | 126 vertices,252 edges,degree4,girth at least6. Root0 R4 covers90 and misses36. |
| Control diameter | Connectedness and D<=6 inherited from the retained source; root0 failure gives D>=5. Exact D is unknown. |
| New lower bounds | 0. |

## Source and model scope

The source is bound directly to the primary LCF recipe. The earlier single8CPU GraphMatcher attempt between local triad labels and LCF labels remained UNKNOWN, with no mapping and no retry. It is a source-history gap, not a graph failure or a fabricated isomorphism.

The explicit shift v->v+18 preserves all189 source edges and has18 orbits of size7, nine per bipartition. One source-cache pass traversed126 roots only through depth4: layers1,3,6,12,24 and B4 size46. There are5040 old-far unordered pairs,3024 across parts and2016 within parts. This is actual radius-cache work; no full source-D6 BFS was repeated.

The prepared model exactly restricts C7-equivariant perfect matchings to old-distance>=5 edges and forbids all new4/5 cycles. Its696 selectors include3 self-conflict units. There are10230 pair conflicts, of which1842 duplicate degree constraints, leaving8388 new clauses. Canonicalization gives1125 unordered pair orbits:81 fixed old-B2 claims,108 unsupported false claims and936 Y variables. The720 old-far pair rows test all126 middle vertices, using58434 shared AND witnesses. Closed-B1 supports retain direct matching edges, and true auxiliary claims require real paths. MODEL_SCOPE.md and CODE_REVIEW.md give the exact scope and implementation review.

The paper one-M bound was corrected from64 to76/74. The original prediction and correction are preserved; no such numeric bound was encoded as a cut.

## The one solver call

The command was the existing CaDiCaL with -t60 on model.cnf, PID3706828, execsession59781. It used60.012343 CPU seconds and60.037328 wall seconds, exiting0 without a model or SAT/UNSAT status. No wall guard fired. There was no proof log, second call, changed seed or reencoding.

A pre-exec driver-limit error occurred before CaDiCaL started: inherited hardCPU10 prevented the child from setting65. The driver was corrected to soft10/hard75. PRESTART_FAILURE records zero actual solver executions for that failed start; it is not a second numerical window. The resource-receipt label was corrected accordingly, with no change to the model or execution.

## One legal matching, chosen without a D4 objective

The control DFS selected the first legal mixed matching by lowest unmatched orbit and ascending selector ID. It stopped after10 nodes and342 selector trials, with7 cross-part orbit pairs and2 within-part pairs. The literal graph preserves all189 source edges and passes degree and short-cycle checks. No second object was selected.

One root0 enumeration of all161 nonbacktracking prefixes through length4 gave B2=17. Among80 old-far targets, zero-M routes cover0, one-M routes39 and two-M routes15. The one-M/two-M overlap is10. Five targets are reachable only with two matching edges:6,32,73,98,100. The path0--37--38--25--6 has edge types M,G,G,M. Existing endpoint sets prove that no zero-M or one-M route reaches6 within4.

The saved [route summary](control_one_legal_matching/ROUTE_COMPLEMENTARITY_SUMMARY.json) splits the5 exclusive targets into4 old-distance6 same-part targets and1 old-distance5 opposite-part target. This shows which two route classes receive new coverage. It does not establish complete coverage. Root0 still misses36 vertices; these are root states, not unordered bad pairs. No other17 representative roots or full global diameter were computed.

The control used0.083566 workerCPU plus0.000475754 driverCPU. Counted source-cache, preparation, solver and control CPU is61.800251118, below the90-second batch budget. The old8CPU isomorphism attempt has its own historical budget. The tiny failed pre-exec start was not individually CPU-timed and is not invented as zero.

## Final state

The family remains UNKNOWN. B2 protection and exclusive two-M coverage are supported by the actual control, while joint D4 existence has neither a witness nor a certified exclusion. One family row combines source history, exact preparation, the single solver call and the control; these are not separate methods. This batch stops without a new matching, endpoint rule, representation, seed or SAT window.


补充类型对照：只读已存endpointsets，two-M独占的5点为6、32、73、98、100；结合源已知D6和奇偶二分，分别是4个旧距6同部目标、1个旧距5跨部目标。完整差集/交集在control_one_legal_matching/ROUTE_COMPLEMENTARITY_SUMMARY.json，未新增图或遍历。当前公开(4,4)基线104的本轮实读记录在BASELINE_PRIMARY_RECEIPT.json。本批停止追加数值；在既有Goal授权内，后续有具体新覆盖问题、有效规则改变或有用运行反馈时可自主另定有界批次，不需用户逐次批准。
