The full actual-source matroid prediction passed: all960 B matrices have rank3 and one-dimensional input kernels; at each of192 controllers the five kernel representatives span rank4 and have a unique dependence of support3. This is a different intrinsic subset rule, not a change of basis intended to repair the failed projective5-frame.

The three dependent lines span an intrinsic2-plane P_a, and the other two kernel lines are independent axes. The saved direct-sum basis has rank4. Selecting P_a+{+e1,-e1}+{+e2,-e2} gives exactly36 original points per controller, independent of the displayed basis of P_a, the axes' signs, or their order. The complete label pool contains6912 distinct original15552-source labels.

LABEL_POOL.json saves each controller's five kernels, unique relation, ternary/axis port indices, P basis, axis representatives, all36 offsets and labels, and all960 typed directed quotient arcs. source_vertex_ids.txt is the ascending original-label list; its zero-based position is the proposed induced-graph label. PROFILE.json retains the complete192-controller profile.

The optional type-pair statistic warns against inheriting a degree claim: there are192 axis→axis,384 ternary→ternary,192 ternary→axis and192 axis→ternary directed quotient arcs. Thus not all endpoints have matching types. The producer must compute the actual induced adjacency and maximum degree before a13D4 candidate can exist; neither degree nor diameter follows merely from the label count.

One worker used0.071742091 CPU seconds. No source distance check, induced edge generation, new graph, BFS or solver was run. The source subset is ready for the root's separately authorized induced-degree gate and only then a distance test. Target6912 would exceed the saved13D4 public6804 baseline, but no new graph or record is claimed here.

Evidence: PREDICTION.json, run.py, PROFILE.json, RESULT.json, LABEL_POOL.json and source_vertex_ids.txt.
