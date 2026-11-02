# Fixed H9 core: the entire ordinary-clone packing has optimum63

The frozen macro prediction is supported by an exact integer certificate: **the fixed41636-point core admits at most63 ordinary full-neighborhood clones**, and the author's existing63 clones attain that bound. Every graph in this fixed-core, one-batch ordinary-clone template therefore has at most41699 vertices. This is below the saved(12,5) lower bound42342 by643 vertices, and below the strict-improvement target42343 by644. No further clone optimization is useful for crossing that target.

This result concerns the total capacity of the whole clone mechanism on this core, not an improvement of a few points or a graph bad-pair score. No LP or MILP was needed.

## Prediction and source scope

PREDICTION.json was saved before the core support computation. It proposed that all legal ordinary-clone batches on the fixed core have fewer than707 clones, the number required for41636->42343. A feasible707-clone assignment would have refuted it. The check instead established the sharp maximum63.

The core is the author witness with7959 split fibers and280 additional H3 copies, with its63 final padding twins removed. Its split set, colors, H3 copies, all core vertices, and every core edge remain fixed. Existing Wiki/source scope was checked through wave3/hexagon_partial_fold_scout/REPORT.md and THEOREM_SCOPE_REVIEW.md; none of the closed monotone split cone, four region MILPs, or wave4 global state search was rerun.

The primary source's Lemma2.2 (Section2.3, paper page3, local text lines122-135) allows any nonnegative integer number of ordinary twins of each core vertex, with no new-new edges. Every clone has exactly its prototype's entire old core neighborhood. If the connected core has D<=5, this construction preserves D<=5: two clones of the same prototype have distance2; different prototypes at distance>=2 use the old route's inner vertices; clones of adjacent prototypes use a3-step route. The inherited partial-fold/copy theorem supplies the core's global D5 guarantee. This task did not reprove the geometric input or run an all-source BFS.

## Exact recovery and clone packing

The saved author edge table contains41699 vertices. The last63 IDs are padding twins, consistent with the witness ordering and earlier recovered degree data. Taking the induced subgraph on IDs0..41635 gives41636 vertices and237006 edges. Every removed pad's old neighborhood was checked to equal the neighborhood of its specified core prototype. The recovered degrees match the previous structure_check.json exactly:

| core degree | vertices |
|---:|---:|
| 10 | 5950 |
| 11 | 13720 |
| 12 | 21966 |

The total unused core degree is25620. That total alone is too weak: dividing by the allowed clone degree11 gives2329, which does not settle the707 target. The bottleneck is where these slots occur.

For every core vertex v introduce a nonnegative integer t_v. With A the core adjacency and d_u its degree, the complete packing is

    maximize sum_v t_v
    subject to sum_{v in Ncore(u)} t_v <=12-d_u, for every core vertex u,
               t_v >=0 integer.

New clones themselves have degree d_v<=12, so the displayed old-vertex budgets give the remaining degree conditions. They are sufficient as well as necessary for this frozen one-batch model.

If v has a saturated neighbor u with d_u=12, u's zero budget forces t_v=0. This eliminates41510 of the41636 prototype variables. The remaining126 prototypes all have degree11. Every one has an old neighbor with deficit1, so0<=t_v<=1. The sum of these individual bounds already gives126<707, which decides the macro question without any solver.

clone_packing.json lists every allowed prototype, its complete old neighborhood and individual bound, all1008 nonempty remaining budget rows, and the author's feasible clone assignment. forbidden_prototypes.json gives a saturated-neighbor witness for every eliminated prototype. This is the full core domain, including H3 vertices and their existing copies, without an orbit or region restriction.

## A sharp63-row certificate

The cheap row-cover calculation finds63 old vertices u, each with deficit1, whose packing constraints are exactly

    t_a + t_b <=1.

Their63 prototype pairs partition all126 allowed prototypes: each variable appears exactly once. Summing gives sum_v t_v<=63. Thus this is a direct integer upper bound, also valid for the fractional relaxation, with no numeric solver tolerance or uncertified infeasibility inference.

The author pad list chooses exactly one prototype from each pair. Its63 clones satisfy every one of the complete core budgets, and their neighborhoods exactly reproduce the source pad edges. Therefore the upper bound is attained: the integer and fractional packing optima are both63, and the existing41699 author graph already maximizes this fixed-core ordinary-clone mechanism.

All allowed prototypes and the sharp constraints are listed below. Each row's two prototype IDs are the only nonzero clone variables in that old vertex's degree budget; every other prototype was forced zero. The author column gives its one chosen clone.

| budget vertex u | allowed prototype a | allowed prototype b | author chosen |
|---:|---:|---:|---:|
| 52 | 25578 | 35072 | 25578 |
| 120 | 12861 | 32044 | 12861 |
| 542 | 23137 | 34966 | 23137 |
| 574 | 28215 | 36185 | 28215 |
| 656 | 2364 | 3819 | 2364 |
| 766 | 2912 | 3886 | 2912 |
| 843 | 5733 | 7715 | 5733 |
| 931 | 5120 | 5349 | 5120 |
| 945 | 28580 | 36402 | 28580 |
| 951 | 30292 | 35617 | 30292 |
| 995 | 20692 | 33965 | 20692 |
| 1055 | 28459 | 36316 | 28459 |
| 1500 | 27939 | 36224 | 27939 |
| 1691 | 26614 | 35372 | 26614 |
| 1715 | 28175 | 36163 | 28175 |
| 1795 | 15403 | 33200 | 15403 |
| 1900 | 29857 | 35564 | 29857 |
| 1913 | 1167 | 1333 | 1167 |
| 2012 | 18530 | 32983 | 18530 |
| 2294 | 6691 | 7844 | 6691 |
| 2445 | 29263 | 36525 | 29263 |
| 2537 | 29095 | 36477 | 29095 |
| 2546 | 29424 | 36609 | 29424 |
| 2579 | 22973 | 35031 | 22973 |
| 2709 | 27790 | 36137 | 27790 |
| 2862 | 5198 | 5359 | 5198 |
| 2876 | 27959 | 36238 | 27959 |
| 3082 | 5546 | 7609 | 5546 |
| 4182 | 17970 | 32722 | 17970 |
| 4573 | 13510 | 32194 | 13510 |
| 5016 | 15591 | 33281 | 15591 |
| 5163 | 17289 | 32566 | 17289 |
| 5210 | 31058 | 35795 | 31058 |
| 5296 | 26599 | 35369 | 26599 |
| 5700 | 21775 | 34717 | 21775 |
| 5706 | 19548 | 33610 | 19548 |
| 6047 | 23984 | 34193 | 23984 |
| 6322 | 20311 | 33837 | 20311 |
| 6345 | 15919 | 33248 | 15919 |
| 6441 | 24436 | 34340 | 24436 |
| 6540 | 704 | 873 | 704 |
| 6566 | 27934 | 36223 | 27934 |
| 6924 | 22709 | 34938 | 22709 |
| 7132 | 31369 | 35926 | 31369 |
| 7518 | 12880 | 32051 | 12880 |
| 8128 | 28190 | 36166 | 28190 |
| 9146 | 10800 | 11987 | 10800 |
| 9205 | 10376 | 11955 | 10376 |
| 9744 | 25160 | 34504 | 25160 |
| 10112 | 25612 | 35085 | 25612 |
| 10180 | 666 | 857 | 666 |
| 10602 | 31243 | 35895 | 31243 |
| 11041 | 27018 | 35412 | 27018 |
| 11092 | 29187 | 36502 | 29187 |
| 11367 | 1542 | 3596 | 1542 |
| 12380 | 39306 | 40496 | 39306 |
| 12589 | 29755 | 36577 | 29755 |
| 13836 | 38946 | 40474 | 38946 |
| 13890 | 5756 | 7728 | 5756 |
| 14475 | 8345 | 8523 | 8345 |
| 16613 | 18127 | 32812 | 18127 |
| 18921 | 37923 | 38021 | 37923 |
| 26068 | 26428 | 35341 | 26428 |

## Decision and limits

The whole fixed-core ordinary-clone route is closed as a way to beat42342. This is stronger than a stopped finite random trial: all legal clone batches in the stated domain obey the explicit63 bound. No new graph or lower bound is claimed; the witness attaining it is the known author graph.

The result does not exclude changing the core split set, colors, H3 copy counts, deleting or rewiring edges, or a different augmentation with a separately proved global routing guarantee. Those are outside this prediction and are not started here. It also does not resurrect any previously stopped H9 search. The feedback changes the mechanism choice: the failure is an exhausted global clone capacity on this core, so extra clone seeds, longer clone runs, or a few clone gains cannot cross the target.

## Artifacts and cost

- PREDICTION.json: hypothesis frozen before support/packing computation.
- core.edges and core_degrees.json: recovered known core and exact deficits, not a new candidate.
- clone_packing.json: all126 allowed variables and the complete reduced integer model.
- forbidden_prototypes.json: saturated-neighbor forced-zero witnesses.
- integer_upper_bound.json and pair_cover_certificate.json: explicit63-row global certificate and author saturation.
- RESULT.json and terminal.json: attained upper bound63 and final order bound41699.
- screen.py: source reading, recovery, support filtering, row cover and exact checks.

Core recovery, support filtering and upper-bound computation took 0.557277 CPU seconds. LP calls0; MILP calls0; BFS calls0; default author verifier calls0; new target graphs0; new lower bounds0. No geometry regeneration, old full-graph distance check, split-state optimization, dependencies, or hashes were performed.
