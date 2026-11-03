# Independent pre-test attack: arbitrary free-vertex edges

Only the new augmentation model is considered: retain all source and uniform-k
full-neighborhood clone edges, cap Delta=delta+k, allow arbitrary added edges
inside F=(old D)+(all clones), and allow a finite nonempty new helper set B with
arbitrary B-B and B-F edges. The inherited host-code conditions are pairwise
disjoint N_H(C), their union H minus D, D subset C isolated in H[C], and C minus D
a perfect matching. No source, geometry, field, Lean, large graph or previous toy
will be rerun.

Independent prediction: the new route h-clone_a-clone_b-T(b) exists legally at
k2 and invalidates reusing the old fixed-free-adjacency exact-route condition.
It still uses one of the first pin's remaining k-1 spare slots, and therefore
does not exceed the new first-pin bound k+1. For every helper h the bound
M <= (k+1)p_h + sum_{g in N_B(h)}p_g should remain necessary, yielding
M <= floor((delta+2k+1)^2/4) after summation.

Test only one delta1 host consisting of two matching edges with C=all4 old
vertices, D=empty, two clones/class. Add h-clone_0 and a peer edge to clone_2.
Check every vertex degree against Delta3 and actual helper-to-old distances,
with and without that single peer edge. The same gadget at k1 should violate
the first pin's cap. This is a tiny route test, not full-graph D3 or q8 BFS.
No optional exhaustive enumeration is needed if the paper route classification
and this counterexample to the obsolete route condition agree. Total CPU<=5.
