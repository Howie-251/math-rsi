# Degree 7, diameter 5: one 2824-vertex voltage profile

No diameter-5 graph was found. The saved best and final graphs are simple, connected, 7-regular, and have diameter 6 under independent all-source BFS. This is a bounded heuristic result, not a nonexistence result for the group or for arbitrary 2824-vertex graphs.

## Construction and baseline

The vertices are two copies of `F353 ⋊ C4`, with multiplication `(x,i)(y,j)=(x+42^i y,i+j)` and labels `x*4+i` within each copy. Since `42²=-1 mod353`, the action has order four. Each side has one noninvolutory inverse pair of internal generators; the cross set has five distinct elements including identity. Thus the complete graph has 2824 vertices and degree seven. The public degree-7, diameter-5 source has 2810 vertices, as read on 2026-10-26 from the [Comellas table](https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html).

The 2810-vertex source was first reconstructed from its actual edge list. The source's displayed operation and displayed generator parameters, when combined literally, did not reproduce that graph. The corrected convention, explicit relabeling, edge equality, and independent all-2810-root distance check are saved in [the recovery notes](m1_d7d5_source/RECOVERY_NOTES.md). This is a known baseline reproduction, not a new bound. The same search implementation accepts the corrected source parameters as a positive control.

## Actual finite run

The [predeclared plan](../../computations/ddp/m1/d7d5_f353/PLAN.md) specifies one group, one seed, one CPU, and 120 CPU seconds. Six annealing segments were fixed before execution; they are parts of this one profile. Common conjugation and scaling normalize each candidate. Complete depth-5 BFS from the two identity roots is exact under the left group action, but the saved edge lists were separately checked from every vertex.

The process ended normally with `BUDGET_EXHAUSTED`: 1,264,612 proposals, 27,047 accepted moves, about 120.003 internal CPU seconds and 120.023 child CPU seconds including setup. No continuation or new seed was started.

|Saved graph|Representative misses|Bad unordered pairs|Independent diameter|
|---|---:|---:|---:|
|Best|124+120=244|172264|6|
|Final|125+135=260|183560|6|

Both have 2824 vertices, 9884 edges, degree exactly seven, and no unreachable pairs. The independent verifier read complete edge lists rather than using the searcher's caches. Its nonzero exit status correctly records failure of the target diameter.

The best parameters are `a=4`, `b=148`, `S=[0,552,116,1,1061]` in the stated `x*4+i` labeling. The best score was reached at about 67.2 CPU seconds. The count of bad unordered pairs agrees with `1412*(244)/2=172264`.

## Consequence

Changing the source's order-five action to an order-four action permits an order above the public threshold, but this run gives no evidence of sufficient five-step coverage. The defect is substantial; a fresh seed alone is not a justified next step. The full source-graph matching augmentation is a separate concrete construction entry, while this profile remains preserved without an automatic continuation.

All parameters, full best/final edge lists, calibration, process termination, and independent BFS JSON files are in `computations/ddp/m1/d7d5_f353/`. No new lower bound, external review, or Lean result is claimed here.
