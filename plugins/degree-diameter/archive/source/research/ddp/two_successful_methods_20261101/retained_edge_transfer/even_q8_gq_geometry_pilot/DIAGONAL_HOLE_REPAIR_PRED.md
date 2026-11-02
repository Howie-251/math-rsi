# Pre-test prediction: a small diagonal-hole repair is also insufficient

2026-11-01. Saved before the independent targeted test; actual execution times belong to its receipt. Follow-up to the independently supported one-copy joint-batch barrier. This changes the generation rule: omit some full-neighborhood clones before trying a joint repair. No large one-copy graph or repair is generated.

Fix the accepted filled source, full C=O times spread, diagonal D, cap Delta=delta+1 and exactly one clone for each C except b distinct diagonal centers D_i (1<=b<=5). Keep all source and remaining clone edges. Add exactly t=b+1 mutually connectable helpers, trying for a net increase of one vertex beyond the full-copy order.

**Prediction:** this cannot have diameter3 for either q8 source, for every choice of b distinct diagonal holes in this specified range.

Let I be the omitted ovoid indices, and use spreadowner bijection to identify spread columns with O indices. For a target center c_(i,j) outside both I rows and I columns and off the diagonal, every omitted diagonal neighborhood supplies exactly ONE available old pin within source distance<=2 of c. There are b such pins in total. Geometry reason: one projection of o_i onto the omitted spreadline, and one line through the omitted ovoid point meeting S_j. Their ordered pair is that pin. A freed fill pin has no such route because its column is omitted. Old D pins never reach an off-diagonal center in two steps.

All available old pins have unique adjacent C-center among the omitted diagonal centers, so an extra internal helper step cannot reach this target through an old pin in three total steps. Thus across t=b+1 helpers at least one helper-target pair is missing for every such target.

The number of these target centers is (R-b)(R-b-1). Each existing clone pin can fix at most t+1 helper-target pairs: its base center for its own helper and its mate for that helper and the internally adjacent helpers. Every such clone has only one spare degree. There are at most t*Delta clone-pin edges even if we optimistically ignore all other degree costs. A necessary condition is therefore

    (R-b)(R-b-1) <= (b+1)(b+2)*Delta.

This fails for b=1..5:
balanced R65/Delta82 has b5 LHS3540 >3444;
Payne R64/Delta81 has b5 LHS3422 >3402.
Earlier b have larger LHS and smaller RHS. At b6 this coarse necessary condition no longer excludes a repair: this is NOT an existence claim.

Independent check should attack the path counting, unique spare degree and exact one-old-pin assertion. Targeted test may use actual accepted incidence/ovoid/spread small tables for one selected b5 subset in each source; verify every outside-row/column target has exactly five old-pin routes (one per hole), and no freed fill/D shortcuts. The paper argument must establish arbitrary diagonal subsets, since one selected subset alone does not.

Budget <=15 CPU seconds, no old field/projection rerun, source BFS, big clone graph, Lean, solver or new global search. If supported, reject b<=5 diagonal repairs and prefer a qualitatively different code or retain sufficient unsaturated support; do not automatically launch b6.

