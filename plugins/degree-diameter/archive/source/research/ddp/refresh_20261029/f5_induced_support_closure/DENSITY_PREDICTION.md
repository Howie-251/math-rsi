# Missing-pencil density gate for the three 19-fiber supports

The true controller-D3 projection rejected the three16-supports but retained three19-supports. Thus the Horn-only all30-fiber inference remains unproved.

New proposed necessary bound: for a retained external controller edge u-v, if either endpoint has a controller neighbor outside the support, at least one of the six backtracking pencil planes is unavailable. Since this external edge has no triangle/two-step route and the source controller has no four-cycle/NB3 alternative, retained endpoints must avoid differences W minus L, where W is that missing plane direction and L the common line direction. Transform the source set by T_p. In each of the five W-cosets, if both endpoint sets are nonempty they must lie in the same L-line, and so their combined size is at most10; if one side is empty, the other has at most25 points. Summing yields n_u+n_v≤125 for arbitrary partial fiber sets, not only whole fibers.

Prediction: each of the three19-supports contains four pairwise disjoint such external edges. Then their eight fiber occupancies sum to at most500 and the other11 fibers to at most1375, giving N≤1875<1921. If no such matching is found, do not infer exclusion from this gate. Static independent attack of the125-point inequality is pending when this prediction is written.

This uses the already saved six-plane complementarity, not a new unverified plane-counting heuristic. Compute only the fixed30-controller and saved three support masks; save each edge and an actual omitted control neighbor as a witness. No source graph, vertex BFS or large solver.
