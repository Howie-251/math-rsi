# One fixed whole27-plane/controller packing gate

Budget:30 CPU seconds cumulative including all preparation, local new-code
checks, compilation and exactly one deterministic controller search, one
worker. The search has at most25 remaining CPU seconds and stops on first31
packing, complete exclusion, or budget UNKNOWN. No second timer/seed/model.

New falsifiable local prediction: in actual controller0 take exactly
W={(x0,0,x2,x3):xi in F3}, labelsx0+9*x2+27*x3,27 centers. Their full original
simple neighborhoods have size14 or15, lie only in the actual completed
controller targets[0,11,59,79,180], and have maxpinload1. Anyvirtual self-entry
is removed exactly at equal global labels. Do not predict totalpin count.
Compare these27 neighbor sets to the27 corresponding literal source rows,
reading only the initial labels through74, not parsing the full graph.
A local mismatch stops without controller search.

For the paper bridge, retain the old affine Q_v normalization: v_pivot=1 and
B's pivot row zero imply im(B) intersect span(v)={0}. This supplies the missing
premise before using the inherited input-kernel transversality. No old rank,
field, geometry or full-source BFS is recomputed.

If localPASS, extract exactly192 five-target setsT(a) from the saved960-arc
relation table, including all24 self-controller memberships. Search only
whether31 such sets can be pairwise disjoint. A proper greedy coloring of
the compatibility graph bounds each exact clique branch; one deterministic
bitset recursion has a process CPU cap and a node counter. First31 returns
its actualI/T labels; only full exhaustion can return EXACT_NO31. Timeout
returns UNKNOWN and the incumbent, with no broader conclusion.

A found31 gives only conditional n15552+31*27=16389. Root must then check
latestpublic16D4 and separately authorize actual graph/fresh verification.
A negative closes only the whole27-plane plus disjointT rule, not partial
centers, load2 at olddegree14 points, or general(16,4). This batch has zero
newgraph/parameter/Lean counts. No oldscope rerun, external solver, parallel
worker, fieldrank/BFS/Lean/query/paidreview/hash or root-owned file edit.
