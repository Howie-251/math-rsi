# p29_both: complete finite result

Status: **COMPLETE_NO_SOLUTION**. All 2 skeletons and 1,414,562 raw assignments were visited; 1,365,784 legal assignments were fully scored. Child CPU time: 20.044099 seconds.

The complete best has quotient `(6, 1, 4)` and variables `(27, 20, 3, 7)` in coordinate order `('b_x', 'd_x', 's_x', 't_x')`. Its two-root missing counts are `(12, 14)`, totaling 26.

Independent generic BFS from all 696 vertices confirms a simple, connected 5-regular graph with 696 vertices, 1740 edges, **diameter 6** and **4,524 unordered pairs beyond distance 5**. See [best.independent_verify.json](best.independent_verify.json) and [search.best.edges](search.best.edges).

The final cursor is skeleton 2, assignment 0, beyond the complete input. This is a finite-family negative result. The exact scope and combined 120 CPU second budget are described in [the batch report](../SEARCH_REPORT.md).
