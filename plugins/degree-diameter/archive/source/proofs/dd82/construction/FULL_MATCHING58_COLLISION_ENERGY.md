# Exact collision energy for the full false-twin58 construction

This changes the objective of a single bounded construction search, not
the graph domain. All 21 free S6 interfaces may change; only the seven
root identities and the false-twin scaffold are retained. No HS50 core,
group action or additional entrywise bound is frozen. Parent mechanism:
`dd82-v3-f9-c7-20261013-0749`. The parent read the complete source and
authorized its one batch, which has now completed. **F improved from 84
to 57, but the lowest-F graph has 51 bad pairs; no target was found.**

For every unordered fibre pair i<j, the full route-count matrix is

\[
K_{ij}=Q_{ij}+\sum_{k\ne i,j}Q_{ik}Q_{kj}.
\]

Each of its six rows is a nonnegative integer vector with sum seven.
Define the energy over all 28·6=168 rows by

\[
F=\sum_{i<j,a}\left[\sum_b\binom{K_{ij}(a,b)}2-1\right]
 =\frac12\sum_{i<j,a,b}(K_{ij}(a,b)-1)(K_{ij}(a,b)-2).
\]

The identity follows rowwise from the row sum seven and six columns.
For every nonnegative integer K, (K−1)(K−2)/2 is nonnegative, vanishing
exactly at K=1 or 2. Hence F≥0, and F=0 holds exactly when every row
contains one two and five ones. By the full matching-cover representation,
this is equivalent to every pair of graph vertices being at distance at
most two. In particular, this is an exact zero-target objective, with no
chosen mixture of unrelated scores.

More explicitly, each K=0 contributes one and each K≥3 contributes
binom(K−1,2), giving

\[
F=\operatorname{bad\_pairs}
  +\sum_{i<j,a,b:\,K_{ij}(a,b)\ge3}\binom{K_{ij}(a,b)-1}{2}.
\]

Thus F directly penalizes the observed collapse of many routes onto one
target. In the actual input graph, the bad block is K16=6I+Q16 with Q16
a derangement. The 162 other rows have energy zero; the six bad rows
have four zeros and a six, hence energy 4+binom(5,2)=14 each. The input
therefore has F=84 and 24 bad pairs. This agrees with the saved edge table.

The new source
[full_matching58_collision_anneal.cpp](../../../computations/dd82/construction/full_matching58_collision_anneal.cpp)
uses real graph edges to evaluate K(u,v)=A_uv+|N(u)∩N(v)| for cross-fibre
pairs and then computes F. It separately retains the ordinary full-graph
bad count. All 315 single-interface transposition moves remain available;
the acceptance rule uses F alone, and temporary increases in F or bad
count are permitted. The seed is `2026101302`, the temperature is the
same 2.5-to-0.15 schedule over each 250,000 proposals, and reheating never
resets the graph or random generator. The starting graph is the saved
24-bad-pair graph, not a new fixed-core restriction.

Each strict new minimum of F saves its complete graph and both scores.
A separate best-bad graph is tracked over every evaluated proposal,
including proposals rejected by the F acceptance rule; equal bad counts
prefer smaller F only for saving, without changing acceptance. The full
edge set, 28 permutations, seed, discovery iteration and row-energy
histograms are retained. Final lowest-F and lowest-bad graphs receive
independent BFS; identical edge sets are checked only once, and an
unchanged initial graph reuses its existing independent BFS with exact
edge equality recorded.

The wrapper
[full_matching58_collision_anneal_run.py](../../../computations/dd82/construction/full_matching58_collision_anneal_run.py)
separates preparation from the single run. Preparation compiled the source
on CPU 1 and checked all 315 seed switches: degree/gauge preservation,
reversibility, agreement between actual common-neighbour F and both
permutation-route formulas, and agreement of the independent bad-count
calculation. This self-check did not optimize or rerun BFS. Compilation
used 1.002212 child CPU seconds; the check used 0.006686 child CPU seconds
(0.004264 inside C++). Evidence is in
[preparation.json](../../../computations/dd82/construction/full_matching58_collision_anneal_run/preparation.json).

The sole executed episode had a 60 CPU second process cap, 59 seconds of
internal search, a 150 second wall cap, one pinned CPU (CPU 1), and no
restarts or further batches. Energy zero stops immediately for independent
BFS. A positive result is only a failed complete graph; the search does
not enumerate the family and cannot prove its exclusion. The parent owns
the final same-thread Gemini review and project-state updates.

## Actual single-batch result

The process stopped normally at the internal CPU budget. It evaluated
10,302,792 proposals, accepted 233,755, including 81,097 increases of F,
and made no restart. Search child CPU was 59.006576 seconds and wall time
60.229333159 seconds. Its lowest F was 57, with 51 bad pairs. Its lowest
bad count remained 24 at F=84, attained by the unchanged starting graph.
The final current graph had F=127 and 114 bad pairs; saved minima were
retained separately. No second batch or extra seed was run.

The actual lowest-F complete graph is
[candidate.best_energy.json](../../../computations/dd82/construction/full_matching58_collision_anneal_run/candidate.best_energy.json)
with plain
[edge table](../../../computations/dd82/construction/full_matching58_collision_anneal_run/candidate.best_energy.edges).
It includes all 28 matchings, the discovery iteration and row-energy
histograms. Every earlier strict energy minimum also has a complete saved
graph. One independent BFS run confirmed 58 vertices, 232 edges, all
degrees eight, diameter three and 51 bad pairs. The full list is in
[candidate.best_energy.verification.json](../../../computations/dd82/construction/full_matching58_collision_anneal_run/candidate.best_energy.verification.json).
That separate process used 0.031950 CPU seconds and 0.066141319 wall
seconds. The best-bad edge set was directly compared with the previously
verified initial graph and was identical, so its existing 24-pair BFS
evidence was reused instead of recomputed. Exact resources and both
verification paths are recorded in
[resources.json](../../../computations/dd82/construction/full_matching58_collision_anneal_run/resources.json).
The saved route rows have energy histogram 0:126, 1:36, 2:3, 5:3; their
maximum-entry histogram is 2:165 and 3:3. In particular no K entry is now
four or greater: the old sixfold route concentration was actually removed.
The six units F−bad=6 are the remaining excess-collision penalties.

The one authorized failure-structure check removed the same original
labels {0,8,46,47,48,49,50,51} from the lowest-F graph. The remaining
50 vertices still have 175 edges and degree seven, but their common
neighbour counts are now:

| Pair type | Common-neighbour count: number of pairs |
| --- | --- |
| Adjacent | 0:157; 1:18 |
| Nonadjacent | 0:129; 1:813; 2:105; 3:3 |

For example, nonadjacent original vertices 10 and 25 have common neighbours
34 and 40. Thus **the previously identified induced HS50 core is broken**.
Only this fixed vertex set was checked; no claim is made that every
possible HS50 core is absent. The reproducible check is
[full_matching58_collision_core_check.py](../../../computations/dd82/construction/full_matching58_collision_core_check.py),
with its data in
[best_energy.prior_core_check.json](../../../computations/dd82/construction/full_matching58_collision_anneal_run/best_energy.prior_core_check.json).
It used 0.001384629 CPU seconds and 0.001386207 wall seconds, with no new
candidate generation, optimization or BFS.

The changed objective therefore produced a real complete graph outside
the prior fixed HS50 core and reduced its exact collision energy. It did
not improve the minimum bad-pair count or solve the general false-twin58
construction problem. This heuristic result gives no family exclusion.
Gemini review of this final outcome is the parent's round-4 obligation;
no further search is authorized or launched in this episode.
