# Fixed deletion proof check — 2026-10-18

**Same-family provisional review: the concrete contradiction is correct.**
It excludes every monotone degree-at-most-8, diameter-at-most-2 completion
of this saved 58-vertex induced graph, with deletion set

`D = {8,16,21,22,23,27,28,31,51,52,54,56,63,64,69}`.

This is one fixed deletion set, not all polarity73 deletion sets and not
all graphs of order 58. No arbitrary SAT neighbor choices are assumed.

Independently parsed `../../geometry.edges` and the `deleted` field of
`deletion_candidate.json`, rebuilt the induced graph G₀, and checked the
following neighborhoods directly (original labels):

| Vertex | N in G₀ |
| --- | --- |
| 0 | {65,66,67,68,70,71,72} |
| 1 | {9,17,25,33,41,49,57} |
| 2 | {5,13,29,37,45,53,61} |
| 5 | {2,10,18,26,34,42,50,58} |
| 61 | {2,15,19,30,32,45,49,60} |

Vertices 5 and 61 already have degree 8, so their neighborhoods cannot
change in a monotone completion. Vertex 0 has degree 7 and is neither
adjacent to nor joined by a length-two path to either of them. Its single
possible new neighbor must therefore belong to
`N(5) ∩ N(61) = {2}`. Thus edge 0–2 is forced in every completion.

After adding **only** this forced edge, both endpoints have degree 8 and
fixed neighborhoods

- `N(0) = {2,65,66,67,68,70,71,72}`;
- `N(2) = {0,5,13,29,37,45,53,61}`.

These sets are disjoint. Vertex 1 still has degree 7; it is nonadjacent to
both 0 and 2, and its current neighborhood meets neither fixed set. To
repair both distances using its at most one additional edge, its new
neighbor would have to lie in `N(0) ∩ N(2) = ∅`, a contradiction. This
particular witness uses only the maximum-degree and diameter conditions;
it does not need the general regularity theorem. Edge 43–53 is unnecessary.

Also read `../analyze_fixed_candidate.py` for scope correctness. It reads
only D from the screen candidate, preserves all induced edges, and applies
necessary forced edges before reevaluating saturated neighborhoods. Its
general degree-tight rule uses the inherited fact that target orders
58/59 must be 8-regular. Its result explicitly limits exclusion to the
saved deletion set and otherwise returns `FORCING_UNDECIDED`. No scope or
soundness defect was found in this bounded check.

The independent calculation above executed no solver and did not call the
analysis script. `completion.py`, historical proofs and other candidates
were not reviewed or run.
