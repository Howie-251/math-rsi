The primary fixedspace prediction was supported on both actual sources. Each self-controller relation has a3-dimensional27-point free subspace in the original coordinates. This exactly matches all648/810 original-free cache labels, rather than only a subset inferred from the compact recipe.

For each normalized relation y=B*x+t*v, use Q_v=I-v*e_j^T with v_j=1. The recorded B is Q_v-valued, so Q_v(B-I)=B-Q_v; the implementation checks this matrix identity, computes its RREF/kernel, enumerates all27 kernel points, and compares their literal labels with the original-free ball-cache labels for that controller.

Actual15552 has24 loop controllers, producing24 zero singleton groups and312 nonzero plus/minus pair groups:336 disjoint groups partition all648 ports. Actual102060 has30 loop controllers, producing30 singletons and390 pairs:420 groups partition all810 ports. Every controller has13 normalized projective directions. The old canonical selfline is exactly one, leaving12 other directions and576/720 additional actual ports outside the old canonical domain.

Both source*_FREE_DIRECTION_GROUPS.json interfaces contain source n/m/D, bin size, full kernel matrices and bases, all13 directions, group costs/pins, and zero-based original-ball row indices. Selector variables are one-based. The existing cache label order is retained explicitly. neg_local_offsets and the formula a*q+x→a*q+neg_local_offsets[x] specify global inversion; all certified arc constants are zero, so it preserves every relation and deletion of virtual loops.

One worker used0.063390872 CPU seconds. It read only original-free cache labels, skipped the R3 ball contents, and did not read/OR R4 balls. No new balls, source BFS, cached target OR, solver or graph computation was run. The expanded direction interface supplies a new complete inversion-invariant free-port model; its target coverage or graph existence is not certified here and belongs to the producer.

Evidence: PREDICTION.json, run.py, RESULT.json, source15552_FREE_DIRECTION_GROUPS.json, source102060_FREE_DIRECTION_GROUPS.json. RAW_ANALYSIS_FIELDS.json supplies merge fields for the two existing source Wiki records, not new method rows.
