# F41 reflection branches: completed finite construction check

No degree-5, diameter-at-most-5 graph was found in either prescribed reflection branch. Both finite inputs were exhausted with full two-root scores, not an early-failure score. This is a finite-family result, not a general degree/diameter impossibility result.

## Exact family and normalization

The group is `G=F41 semidirect C8`, with `(x,i)(y,j)=(x+3^i*y,i+j)` and vertex label `layer*328+x*8+i`. The graph has 656 vertices. Internal edges are right multiplication by two inverse-closed elements on each side; cross edges use `S={e,s,t}`. Side 0 is fixed to `A={(0,4),(1,4)}`.

In the mixed branch, `B={(b,beta),(-3^(-beta)b,-beta)}` and the variables are `(b,s_x,t_x)`. In the both-reflections branch, `B={(b,4),(d,4)}` and variables are `(b,d,s_x,t_x)`. Once A has been fixed by common conjugation and scaling, there is no remaining projective reduction: every one of the `41^3` or `41^4` translation tuples is visited, including the all-zero tuple before legality filtering.

The input skeletons and normalization/capacity proofs are in `DERIVATION.md`, `capacity.py`, `capacity_results.json`, and `profile_metadata.json`. The symbolic filter leaves 40 of 50 mixed skeletons and 4 of 6 both-reflection skeletons. Its rejection is necessary: a target quotient fiber with fewer than 41 distinct affine endpoint forms cannot cover its 41 actual vertices. We did not add any residual A-swap, cross-anchor, B-order, or quotient-unit filtering to the translation search.

Legality excludes mixed internal identity or involution, duplicate both-reflection generators, and any collision among `e,s,t`. Repeated quotient residues alone are allowed. The fixed A consists of two distinct nonidentity involutions; its product generates the normal C41. Each supplied skeleton generates the quotient C8. Thus each legal generated graph is simple, connected, and 5-regular.

## Completed counts

| Branch | Skeletons | Raw assignments | Legal fully scored | Illegal | Minimum root miss sum | Best bad unordered pairs |
|---|---:|---:|---:|---:|---:|---:|
| mixed | 40 | 2,756,840 | 2,713,298 | 43,542 | 11 | 1,804 |
| both | 4 | 11,303,044 | 11,027,360 | 275,684 | 6 | 984 |

All **14,059,884** raw assignments were visited, and **13,740,658** legal graphs were fully scored. The remaining **319,226** assignments failed explicit legality checks. Raw and legal totals agree with the independently derived metadata.

For each legal graph the implementation computes radius-5 BFS from vertex 0 and vertex 328. Common left multiplication by G acts transitively within each layer and preserves all right-multiplication edges. Therefore two-root coverage is exactly equivalent to diameter at most 5. If their missing counts sum to `score`, the number of unordered bad pairs is `328*score/2`. Scores include both roots in full even when the first root already fails.

The first minimizers, with group labels `x*8+i`, are:

- **mixed**: quotient `(beta,sigma,tau)=(1, 1, 2)`, variables `(34, 31, 3)`, generators `(A0,A1,B0,B1,s,t)=(4, 12, 273, 135, 249, 26)`, root missing counts `[9, 2]`. The full graph is `complete_mixed.best.edges`.
- **both**: quotient `(beta,sigma,tau)=(4, 1, 3)`, variables `(37, 26, 16, 2)`, generators `(A0,A1,B0,B1,s,t)=(4, 12, 300, 212, 129, 19)`, root missing counts `[2, 4]`. The full graph is `complete_both.best.edges`.

The recorded minimum in each branch is global for its full supplied input. The output does not claim that either saved minimizer is globally best among arbitrary 656-vertex graphs or other graph constructions.

## Regression, measured cost, and terminal state

Before production, four prescribed tiny families over `F5 semidirect C4`, action 2, were compared with an independently generated explicit undirected graph implementation. All 1,500 raw assignments and 980 legal graphs matched on legality counts, complete score histograms, and actual diameter histograms; the independent program had checked all 40 roots of each legal graph. These are implementation controls, not additional research groups.

The negative control regenerated the saved previous F41 inverse-pair graph. Its complete 656-vertex edge set matched exactly and the two root missing counts were `[11,14]`, score 25. See `regression_saved_f41.*` and `regression_calibration.json`.

Two 100,000-assignment calibration slices measured 1.207 and 1.387 CPU seconds and predicted approximately 191.2 CPU seconds for production. The actual sequential production used **192.406995 CPU seconds**; regression and calibration used **2.604094 CPU seconds**, for **195.011089 CPU seconds** before the millisecond-only status-label regression described below. Wall time for production was 192.441959 seconds. The single-core batch stayed inside the authorized cumulative 300-CPU-second limit; it was not restarted or extended.

An independent code read found the group formulas, generator order, legality, all-tuple enumeration, and five-step scoring consistent. It also found a reporting issue confined to positive controls with `STOP_ZERO=0`: complete runs containing solutions had been labeled `COMPLETE_NO_SOLUTION`. The label was corrected to `COMPLETE_WITH_SOLUTIONS`; production uses `STOP_ZERO=1`, so its candidate detection and completed negative outcomes were unaffected. Only the four tiny regression cases were rerun after this correction; production and calibration were not repeated. This took 0.007196 CPU seconds, giving a total search/calibration/regression cost of 195.018285 CPU seconds; see `regression_label_fix.json`.

The terminal state is **COMPLETE_NO_SOLUTION**, with all 44 skeletons complete and no remaining cursor. `complete_mixed.skeleton_results.jsonl` and `complete_both.skeleton_results.jsonl` contain every skeleton's visited/legal counts, exact score histogram, minimum, completed cursor, and CPU time. `production_process.json` records the exact commands, per-process exits and actual CPU usage. `search_reflections.cpp` is the independent search implementation; `run_production.py` is the bounded sequential runner. No random seeds, extra groups, or follow-on searches were used.

## Independent complete-graph verification

An independent Python implementation read each saved edge list, built fresh adjacency, and ran deque BFS from every one of its 656 vertices. It did not use the search generator, group formulas, saved distance matrices, or the two-root inference. Both graphs are simple, connected, 5-regular, have 1,640 edges, and have diameter **6**. The bad unordered pair counts agree exactly: mixed **1,804**, both **984**.

Their two distinguished root distance histograms, at distances 0 through 6, are:

- mixed: `(1,5,20,80,263,278,9)` and `(1,5,20,80,259,289,2)`;
- both: `(1,5,20,80,272,276,2)` and `(1,5,20,80,266,280,4)`.

This independent validation used 0.546521 CPU seconds. Its code and complete results are `reflection_best_independent_bfs.py` and `reflection_best_independent_bfs.json`. Including it, the measured search, calibration, regression and saved-graph verification cost was 195.564806 CPU seconds, below the 300-second allowance. No general conclusion beyond this specified two-orbit family is inferred. All requested calculations have ended.
