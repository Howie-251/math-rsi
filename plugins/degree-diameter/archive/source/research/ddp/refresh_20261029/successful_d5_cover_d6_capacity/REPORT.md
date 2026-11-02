# Three accepted D5 sources: ordinary-cover D6 obstruction

All three requested D6 cover directions are excluded. These are necessary-route obstructions for every ordinary cover of the specified literal source, not failures of chosen voltage assignments.

| Accepted literal source | Required sheets to exceed saved D6 bound | Actual witness (root, target) | NB walks through length 6 | Excluded sheets for D≤6 |
|---|---:|---|---:|---|
| 37631, max degree 11 | 5 | (0, 13489) | 4 | all k≥5 |
| 42402, max degree 12 | 9 | (42324, 796) | 8 | all k≥9 |
| 51457, max degree 13 | 11 | (49949, 1574) | 2 | all k≥3, hence all k≥11 |

The exact witness counts by lengths 0,…,6 are respectively `[0,0,0,0,1,1,2]`, `[0,0,0,0,1,1,6]`, and `[0,0,0,0,1,1,0]`. No prospective cover order is counted as an actual graph.

## Why the obstruction is sufficient

Let π:G̃→G be an ordinary k-sheet graph cover. Choose any lift r̃ of a tested base root r. Every shortest path from r̃ projects to a nonbacktracking base walk: consecutive inverse base arcs must lift to consecutive inverse arcs by the local bijection, contradicting shortestness. Each base walk starting at r has exactly one lift starting at r̃. Therefore the number of points in π⁻¹(t) reachable within D steps is at most the number of nonbacktracking walks from r to t of lengths 0,…,D. A count less than k makes D(G̃)≤D impossible. This does not require a regular/deck-Galois cover or a regular source. Length 0 is included for t=r.

The computation uses exact integer arc messages. If c_l(v,w) counts length-l walks ending with v→w, then `c_(l+1)(v,w) = sum_u c_l(u,v) − c_l(w,v)`. There is no truncation or saturation. Immediate reversal is excluded; other repeated vertices/edges and non-tailless closed walks remain counted, as required.

## Actual tested roots and self-fiber counts

Each literal was loaded once. Requested roots were 0, the smallest minimum-degree vertex, and n−1, deduplicated. Each source stopped at its first failing root; the last-added vertices were not tested.

| Source | Tested root | Minimum NB≤6, first target | Root self-fiber NB≤6 | Exact closed counts, lengths 0,…,6 |
|---|---:|---|---:|---|
| 37631 | 0 | 4, target 13489 | 357 | 1,0,0,0,2,14,340 |
| 42402 | 0 | 13, target 18371 | 1257 | 1,0,0,0,102,6,1148 |
| 42402 | 42324 (degree 7) | 8, target 796 | 767 | 1,0,0,0,42,2,722 |
| 51457 | 0 | 15, target 1451 | 799 | 1,0,0,0,30,18,750 |
| 51457 | 49949 (degree 7) | 2, target 1574 | 209 | 1,0,0,0,0,2,206 |

These minima are over every target at the listed root, not over untested source roots. The obstructions occur at other fibers; no claim that a source has only the empty short closed walk is made.

## D5 consequence from the same accumulation

Already at root 0, the three sources have a target with exactly one NB walk through length 5: targets 102, 53, and 191 respectively. Each witness has exact counts `[0,0,0,0,0,1]` through length 5. Hence every nontrivial ordinary cover (k≥2) of each of these exact accepted sources fails diameter at most 5. This used existing intermediate counts, not extra roots or another run.

## Scope and accounting

The targeted old-scope check is recorded in `PREDICTION.md`; it found no prior completion of this gate for these final accepted graphs. Actual source paths, degrees, all per-root minima and witnesses are in `RESULT.json`. No public base graph was substituted for an accepted extended source. The inherited source D5 certificates were not rerun.

One execution: three literal reads, five DP roots, worker CPU 0.123602 s; compilation plus execution 0.838358 s, within 10 CPU seconds. No source diameter BFS, cover graph, voltage assignment, solver, random proposal, restarted computation, or additional source. `TERMINAL.json` has no pending work. This closes ordinary covers of these exact sources at the stated sheet thresholds; changed base adjacency, branched maps, and different constructions are outside the result.
