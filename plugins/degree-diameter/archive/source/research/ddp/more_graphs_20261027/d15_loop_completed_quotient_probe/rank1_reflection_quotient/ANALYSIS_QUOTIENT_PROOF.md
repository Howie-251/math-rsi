# Rank-one reflection automorphism quotient: conditional proof

The proposed gate and degree/diameter argument are valid for the stated controller-fixed linear reflection class. This is a quotient of the complete old graph, not an induced subset. This paper performs no numeric gate, graph construction or BFS.

In each source space V=F3^4 the five individually preserved kernel lines have one rank4/support3 configuration. The three circuit lines span P of dimension2. A linear involution preserving each line acts on its vector by a sign. Applying it to the unique three-term dependency forces the same sign on all three lines. In a rank-one reflection, the minus eigenspace has dimension1, so this two-dimensional plane must have sign plus. The remaining two intrinsic axes are eigenlines, and exactly one must have sign minus. Hence there are exactly two such local reflections. For either minus axis u, the other four kernels span a fixed hyperplane; normalize its annihilator ell by ell(u)=1 and set R=I-2*u*ell. Rescaling u changes no R. This completeness does not extend to arbitrary involutions, controller permutations or affine maps.

Write a completed source arc a->b as y=B*x+<v>, with B rank3, kernel the input-port line and Q_v*B=B. A choice R_a,R_b preserves this relation exactly when

    R_b*v is in <v>, and Q_v*R_b*B = B*R_a.

The first condition preserves the noise line. The second says that the image of B*x differs from B*R_a*x only by that noise. These conditions are necessary and sufficient for the entire three-neighbor relation, not a sample of its edges. Two local choices per controller and binary forbidden state pairs therefore give an exact2SAT gate for this reflection class. Self-arc repeated variables must be handled as the resulting unit or tautological clauses; a returned assignment must be rechecked on all960 arcs. The source translations are zero. Deleted virtual loops are preserved under a vertex permutation, so a valid relation automorphism is an automorphism of the actual simple source as well.

The degree reduction requires a further observation. Let lambda_in and lambda_out be the signs on the input-kernel and output-noise lines of an accepted arc. B induces an isomorphism between the corresponding three-dimensional quotients, intertwining R_a and R_b. Consequently

    det(R_a)/lambda_in = det(R_b)/lambda_out.

Both full determinants are minus one, so the signs agree. Every controller has exactly one minus input port, and that port therefore has minus output noise at its target. For this target reflection, im(R_b-I)=<v>. Every affine neighbor line B*x+<v> is invariant under R_b, even if x itself is not fixed. On its three points the involution has one fixed point and one two-cycle, hence at most two orbit classes. The other four ports give at most three classes each. Thus every source orbit has at most2+4*3=14 neighbors in the simple quotient. Deleting loops and duplicate edges only lowers degree.

One representative suffices to compute an orbit's quotient neighbor set: the other representative's neighbors are its automorphic images and belong to exactly the same target orbits. Without the verified automorphism this representative construction and degree argument would not be justified.

Each rank-one reflection fixes3^3=27 of the81 vertices in its controller. The remaining54 form27 pairs, giving54 quotient vertices per controller. Across192 controllers this gives5184 fixed source vertices and exactly10368 source orbits. For any two quotient classes choose source representatives and a source path of length at most4. Projecting the path and deleting repeated orbit stays gives a quotient path no longer than4. Thus the old D4 bound transfers automatically once the actual quotient is constructed correctly. An induced-subgraph D4 argument was unavailable for the earlier36-point rule; this quotient argument retains every projected path.

If the gate is SAT and the actual graph checks pass, the resulting simple undirected graph has order10368 and maximum degree at most14. The original source diameter is inherited, not revalidated. ExactD4 follows from the degree14/D3 Moore bound1+14+182+2366=2563<10368. The supplied current target baseline9720 would then be exceeded. A returned assignment or orbit count alone is not an exported verified target graph; the producer still checks actual degrees and the new quotient as assigned.

If2SAT is UNSAT, it excludes this complete two-choice-per-controller reflection class only. No different involution, controller action, partition or field is automatically tried. Actual gate outcome, orbit map and graph validation belong to their producer receipts and are not invented here.

Inherited completed gate: all3840 endpoint-state pairs produce1812 distinct clauses and the exact2SAT instance is UNSAT. Aggregate CPU is0.445824661. No SAT assignment was returned, so no post-SAT arc recheck, orbit map or quotient graph was generated. A separate consequence in ANALYSIS_DEGREE_NECESSITY.md uses the already saved nonloop zero-allowed arc5 to exclude maximum14 even for non-automorphic partitions from this same two-choice family. It explicitly uses both representatives' source neighbors. Neither this paper nor that strengthening runs a new numeric test.
