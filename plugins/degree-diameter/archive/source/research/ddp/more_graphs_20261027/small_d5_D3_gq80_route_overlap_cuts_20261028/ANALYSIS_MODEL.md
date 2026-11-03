# GQ80 paired matchings with route-overlap integer cuts

This preparation reuses the saved W(3,3) geometry, incidence edges, all 1560 binary variables, 80 perfect-matching degree equations, and 1080 exact far-pair cover constraints from `breadth_20261027_wave11/gq80_paired_matchings`. That original one-call 15-second MILP ended UNKNOWN with no incumbent. Its files are unchanged. No geometry was regenerated and no graph BFS was performed.

For either 40-vertex side, let C(x) be its 13-element closed collinearity set. Distinct x,y have |C(x)∩C(y)|=4, hence A=C(y)\C(x) has size 9, while Z=V\(C(x)∪C(y)) has size 18. Suppose the own-side perfect matching P selects xy. The 27 same-side targets outside C(x) must all be reached in at most three steps. The routes whose own-side matching step is first cover at most A (9 targets). The routes whose opposite-side matching step is in the middle cover at most 4*3=12 far targets: four incident lines can each relay to at most three points outside C(x), and the dual statement is identical for line roots. Therefore at least six targets in Z must instead be reached by the own-side matching step last, so at least six edges run from C(x) to Z in P.

For every unordered potential edge xy and both ordered root choices x and y, append the conditional integer inequality

`sum(P_uv : u in C(root), v in Z) - 6 P_xy >= 0`.

If P_xy=1, the preceding counting argument proves the row. If it is zero, the row is trivially nonnegative. Since C(root) and Z are disjoint, its 13*18 positive variables represent 234 distinct edges, and P_xy is outside that positive set. The constraints neither preselect edges nor restrict graph symmetries. There are 780 potential edges times two roots times two sides = 3120 new rows.

The complete prepared model has 1560 binary variables, 4280 rows (80 degree, 1080 exact cover, 3120 new valid integer cuts), and 780600 nonzero coefficients (47400 inherited plus 733200 new). `overlap_cuts.json` saves all ordered-root cut supports. `full_model.csc.npz`, `lower.npy`, and `upper.npy` save the exact solver input. `prepare_model.py` only constructs these files, without importing a solver.

The primary prediction is existence of a complete degree-5 diameter-at-most-3 graph on 80 vertices from these two arbitrary matchings, compared with baseline 72. UNKNOWN is not a refutation. No separate LP was run to ask whether the old LP solution violates a new row; that secondary question remains unmeasured.

The one future production call is prepared in `worker.py` and `driver.py`: zero feasibility objective, all binary variables, one thread, 45 seconds of solver time, and an aggregate 55-CPU-second budget including measured model preparation (the worker hard limit subtracts that preparation). It exports a rounded incumbent only after checking every original and new row and its simple 5-regular 80/200 edge table. Full 80-source BFS is reserved for the parent upon an actual exported candidate. No solver was invoked during this preparation; execution waits for the parent's paper confirmation.
