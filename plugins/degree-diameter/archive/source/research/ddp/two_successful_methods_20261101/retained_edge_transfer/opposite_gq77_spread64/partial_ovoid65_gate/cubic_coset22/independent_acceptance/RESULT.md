# Independent acceptance: PASS

The complete literal `graph_d65_D3_n161150.edges` was independently read and accepted: **161150 vertices, 5192000 edges, maximum degree65, exact diameter3**.

- The candidate's entire old-old body is exactly the source's5121600 literal edges, in the same strict lexicographic order. The full candidate has proper endpoints, strict order, and no repeated edge.
- For every i=0,...,1099, newlabel160050+i has exactly the64 neighbors of its specified old center in the immutable source graph. Neighborhoods were independently recovered from the source edge file. There are70400 added edges and0 new-new edges.
- Every old pin load was counted and bound individually: load0:89650, load1:70400, maximum1. The actual degree histogram is64:90750 and65:70400.
- Ordinary queue BFS was actually run from all1100 new roots; each reaches all161150 vertices within3, and0 old roots were run. Distance0/1/2/3 histograms:22 roots have(1,64,3186,157899), and1078 have(1,64,3249,157836). Every individual root is recorded in `NEW_ROOT_BFS.csv`.
- All-pairs diameter-at-most3 follows from the inherited accepted source theorem and the full-neighborhood clone lemma in `PLAIN_PROOF.md`. Its adjacent-center path has length3; the1100 centers actually induce231 source edges. The order bound for degree65 and diameter2 is4226, proving the diameter is exactly3.

The10-root BFS pilot used0.034380 CPU seconds and predicted5.859821 CPU seconds for the validator. Actual measured compile+validation+driver total is6.747941293 CPU seconds; summary postprocessing adds0.005828474, giving **6.753769767 CPU seconds /120**, one worker, one compile, no budget extension. The actual validator internal total is5.763262 CPU seconds, with3.679689 spent in BFS. No solver, installation, download, hash, old-source reconstruction, old-root BFS, or Lean compilation was performed.

This is mathematical and literal acceptance. It inherits the already closed source concrete Lean theorem; it does not claim that a new concrete Lean instance for161150 has been compiled. It makes no public world-record or priority claim.
