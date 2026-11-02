# Full scope of the fixed 104c split-and-absorb operation

The complete operation is closed for the fixed triangle-free Bhakar104c source: split any vertex v into adjacent children u,w, give them two old neighbors each (A and B), delete one source edge x-y, and add u-x,w-y. Every legal simple output on105vertices fails diameter4. This is not an exclusion of arbitrary105-point graphs.

The new batch already completed all119,808 tuples with x,y outside closed N[v]. It skipped12 outputs inherited from the old saved-Q switch neighborhood, rejected the remaining119,796 by the exact two-child gate, and left none unvisited. One literal graph was expanded only for the recorded two-root calibration. The original RESULT remains the unchanged account of that frozen batch.

It remains to classify source cuts touching N[v]. First require the cut not to meet v. Since the source has no triangles, no two of the four neighbors of v are adjacent. Exactly12 non-v-incident edges touch N(v), each at just one endpoint. For each such cut, one orientation is illegal and the other is an old absorption:

- If x is in A, u-x is already a retained spoke. If y is in B, w-y is already a moved spoke. These are duplicate-edge outputs.
- If x is in B={x,b}, u-x restores the original edge v-x. Relative to the original104-point graph, only edges v-b and x-y are removed, and w joins their four distinct endpoints. This is exactly one of the old20,904 two-disjoint-edge/four-spoke absorptions, all of which failed D4.
- If y is in A, exchange the child roles and labels. The same reduction gives an old two-disjoint-edge absorption. This is a relabeling argument and uses no source vertex-transitivity.

A cut incident to v cannot add a new legal case: depending on orientation, the stated new edges include a selfloop at u or a duplicate buddy edge u-w.

For each of104vertices and3 unordered balanced partitions there are204 non-v-incident source edges and2 orientations:127,296 raw tuples. The outside domain accounts for119,808. The remaining12 edges per partition each give one illegal and one inherited legal orientation:3,744 of each. Thus the legal parameter total is123,552 =119,808 new-batch tuples +3,744 inherited degenerate tuples. These are parameter counts, not counts of distinct graphs. No degenerate case, old neighborhood, graph or BFS was generated for this classification.

Evidence: local RESULT.json; old `breadth_20261027_wave2/extension105_d4/REPORT.md`; SOURCE_SCOPE.md/json and SKIP_SCOPE.md/json. Other source graphs, unbalanced splits, multiple cuts or other surgeries remain outside this conclusion.
