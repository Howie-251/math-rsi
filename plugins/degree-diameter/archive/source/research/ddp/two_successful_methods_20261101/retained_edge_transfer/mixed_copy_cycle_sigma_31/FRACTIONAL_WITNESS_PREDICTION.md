# Diagnostic prediction after the one full MILP timed out

The actual one-shot MILP returned UNKNOWN with no integer incumbent after
95.395974 child CPU seconds, including matrix/imports. It is terminal and
will not be restarted. At most24.604026CPU remain in the original120CPU
model batch. This separate diagnostic is capped at5CPU, with no new solver
or second graph/hole/peer pattern.

Predict that R={585*x+y: x0..14, y in the original B-neighbors of b0=0}
has120 labels, all among the130 freed degree30 vertices, and that every
actual G0 target has at least7 vertices of R in its closed radius2 ball.
The reason is the polarity2-support interface and the complete fifteen
A-coordinate fiber over each of the eight nonabsolute B-neighbors.

If true, the explicit rational assignment x[h,u]=1/7 for all six helpers
and u in R, zero otherwise, satisfies the entire LP relaxation. Every
helper uses120/7<26 pins fractionally, every used old pin gets6/7<=1 load,
and all coverage inequalities have integer numerator

    |closedB2(v) intersect R|+5|closedB1(v) intersect R| >=7.

The helper weighted-sum symmetry rows are equalities. No optimization or
floating-point certificate is needed: check these integer counts on the
actual prepared G0 and save each target separately, including all copies.
The own-B2>=7 prediction and the full-model numerator>=7 prediction are
reported separately if one fails. A fractional witness is not a graph or
an integer solution.

If supported, the shortage is not aggregate LP capacity. The next algorithm
should use the small A-support coloring/cover obligations and shared endpoint
slots to find a genuine six-way allocation, rather than spend another budget
solving this large symmetric root LP. If refuted, keep exact missed targets
and do not assert LP feasibility. No old585 R2/Steiner/BFS/field/Lean or
portfolio verification is repeated, and no graph/parameter/Lean is added.
