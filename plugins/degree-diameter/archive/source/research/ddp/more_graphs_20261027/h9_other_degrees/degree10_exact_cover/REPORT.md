# Degree10 fixed-fold exact cover: one LP and one MIP, no incumbent

Status: **UNKNOWN_NO_INCUMBENT_WINDOW_CLOSED**. The complete fixed-source one-new-vertex model was submitted once. No feasible10-pin set was returned, and no infeasibility proof was obtained. This is not an exclusion of the family and is not a new graph result. The task has no active solver or continuation.

## Exact scope and input reuse

The source is the nonregular33397-point H9 fold with166425 edges. Its only available old vertices at degree cap10 are the364 H3 points:28 have degree6 and336 have degree7; all33033 generic vertices already have degree10. A new point preserving every old edge can choose only these364 pins and can choose at most10 of them.

The preceding bounded-ball pass computed the complete closed R4 ball of each available pin once and saved degree10_radius4.u64.bin. Their union covers every source vertex; there are no uniquely forced pins. A cheap uniform hard-target bound required at least9 pins, which did not decide the10-pin limit. This exact task reused that matrix and performed no BFS.

There is one binary x_a for each of the364 available pins. Every one of the33397 target rows requires sum_(a whoseR4contains target)x_a>=1, and sum_a x_a<=10. No pin is fixed, and no unproved group symmetry, orbit reduction, random start or local repair is used. Identical coverer rows were removed without changing feasibility, leaving26117 coverage inequalities. model.json preserves the target-to-row mapping, representative targets and literal pin order; unique_cover_rows.u8.bin preserves every complete364-bit row.

## LP result and exact lower-bound check

One single-thread HiGHS LP minimized sum x_a over the nonnegative cover relaxation. It terminated optimal with objective9.036789297658839, using14.614467 CPU seconds. The upper bound x_a<=1 was unnecessary for this relaxation because any entry exceeding1 can be clipped to1 without violating a0/1 unit-right-hand-side cover inequality.

An exact integer dual was retained and independently recomputed from the saved packed rows: nonnegative target-row weights sum to9036606; each pin's weighted column load is at most1000000. Therefore any cover has

    sum x_a >=9036606/1000000 >9.

So an integral feasible cover would require at least10 pins. This does not exclude10. The integer loads were recomputed using integer arithmetic, not accepted solely from the LP's floating objective. This is a scoped covering-matrix certificate, not a universal degree-diameter bound.

## The one MIP window

The binary feasibility model used zero objective, all364 binary variables, the complete deduplicated coverage matrix and the cardinality cap10. SciPy milp/HiGHS ran with one solver thread and a whole-process hard CPU limit120 seconds. Its time limit was set from the remaining budget after LP/preparation, leaving room to return and save status. There was exactly one MIP call, with no seed or extra window.

It returned time limit reached, primal status None, no incumbent. Measured MIP CPU was101.389955 seconds; measured total process CPU including preparation and LP was116.546768 seconds, within120. HiGHS completed internal stopping after its configured remaining-time value; the whole-process hard limit remained active. There is no returned binary witness and no certified UNSAT conclusion.

## Decision and artifacts

The fixed-source10-pin possibility remains open. The result only says the one complete MIP window did not decide it; it is not evidence that all10-pin choices fail. No sample was added and no reduced-bad-count candidate was selected. The separate degree11 Q-line work is an independent parameter task, not a reason to relabel this UNKNOWN.

PREDICTION.json freezes the question before solving. LP_result.json and MIP_result.json preserve statuses and measured costs. integer_dual.json proves the lower bound10 over the complete reused matrix. model.json and unique_cover_rows.u8.bin define the exact model; production.log, run.py, driver.py, RESULT.json and terminal.json preserve execution and final scope.

No graph generated; no new BFS; no new lower bound; no active handle. A future continuation would need explicit new mathematical or solver justification, not another automatic window.
