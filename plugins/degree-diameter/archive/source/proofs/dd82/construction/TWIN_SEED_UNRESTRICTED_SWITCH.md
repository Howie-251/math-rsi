# Unrestricted two-edge switches of the new twin-HS seeds

The deflated order-$59$ candidate improves from $28$ to $27$ bad pairs by
one unrestricted degree-preserving switch. Its complete next neighborhood
has no strict improvement. The order-$60$ seed with $20$ bad pairs has no
improving unrestricted switch; its best distinct neighbor has $22$ bad
pairs. None of these graphs has diameter two.

## Exact experiment scope

The inputs are the new seeds
`computations/dd82/construction/twin60_deflate59_run/candidate.best.edges`
and
`computations/dd82/construction/petersen_all_matchings_run/candidate.best.edges`.
This is not a rerun of the old $50$-bad-pair seed or its matching-only
neighborhoods.

For each unordered pair of vertex-disjoint edges $ab,cd$, the program
tries both replacements $ac,bd$ and $ad,bc$. A replacement is rejected
exactly when an added edge already exists. No fiber, route-cap, triangle,
or other structural restriction is imposed. Every accepted switch gives
a simple eight-regular graph, and every distinct simple graph obtainable
by one nontrivial two-edge switch appears once: its two removed edges and
two added edges uniquely identify that switch.

For order $59$, every full neighborhood is scored and the best strict
improvement is selected, breaking ties by the fixed lexicographic edge
iteration. The limit was ten accepted steps or ten CPU seconds. It stopped
naturally after one accepted step. Equal-energy moves were not followed.
For order $60$, only the requested single full neighborhood was checked.

## Complete neighborhood outcomes

| Current graph | Distinct valid switches | Best neighboring bad-pair count | Number attaining it | Decision |
|---|---:|---:|---:|---|
| $59$ vertices, $28$ bad pairs | $40825$ | $27$ | $1$ | Accept the unique improving switch |
| $59$ vertices, $27$ bad pairs | $40826$ | $27$ | $7$ | Stop strict descent; ties remain |
| $60$ vertices, $20$ bad pairs | $42440$ | $22$ | $5$ | No improving switch |

The complete energy histograms, rejected-alternative counts and chosen
moves are in `twin_seed_unrestricted_switch_run/deflated59.json` and
`twin_seed_unrestricted_switch_run/twin60.json`.
For an eight-regular graph with $m=4n$ edges, the number of unordered
vertex-disjoint edge pairs is
$\binom{m}{2}-n\binom{8}{2}$. The independent verifier checks this count,
the two alternatives per disjoint pair, and the histogram totals against
every completed neighborhood record.

## The actual order-59 improvement and departure from the fiber moves

The deflation deleted original vertex $41$; the current label $v\ge41$
corresponds to original label $v+1$. In original order-$60$ labels, the
accepted switch removes

$$\{38,46\},\ \{45,50\}$$

and adds

$$\{38,45\},\ \{46,50\}.$$

The removed edge $\{38,46\}$ was one of the deflation repair edges. The
other removed edge $\{45,50\}$ was an original edge of the order-$60$
seed. Thus the improvement edits the surviving original graph as well as
the repair, going beyond the completed deletion-plus-neighbor-matching
family whose minimum was $28$.

These changes involve two different original fiber pairs. Original
vertices $45$ and $46$ change their numbers of neighbors in the different
fibers. No internal fiber edge changes. This is an actual improvement
obtained by releasing the single-matching restriction, although the graph
still has $27$ uncovered pairs.

The saved order-$59$ local-minimum graph has $236$ edges and exact distance
histogram

$$\{1:236,\quad2:1448,\quad3:27\}.$$

The saved equal-energy neighbor also has $27$ bad pairs and was retained
as a witness only; it was not accepted as a descent step.

For the order-$60$ seed, the saved best neighbor removes $\{40,53\}$ and
$\{41,59\}$ and adds $\{40,59\}$ and $\{41,53\}$. This particular best
move is itself within one matching, despite all unrestricted moves being
considered. Its distance histogram is

$$\{1:240,\quad2:1508,\quad3:22\}.$$

## Saved objects and independent verification

The output directory is
`computations/dd82/construction/twin_seed_unrestricted_switch_run/`.
It contains:

- `deflated59.step1.edges`: the genuinely improved $27$-bad-pair graph;
- `deflated59.best_distinct_neighbor.edges`: a $27$-bad-pair neighbor of the terminal graph;
- `twin60.best_distinct_neighbor.edges`: the $22$-bad-pair neighbor;
- corresponding complete graph `.json` and `.verification.json` files;
- neighborhood reports, full histograms, execution logs and resource records;
- `verification.json`, combining the independent checks and original-label traces.

`twin_seed_unrestricted_switch_verify.py` independently reads the expanded
edge files, reconstructs adjacency sets, replays every saved change, and
runs BFS from every vertex. Every bad pair is saved with its distance,
common-neighbor set, and both neighbor lists. The verifier also records
which original fiber degree profiles change and whether a move is a
single-matching transposition.

The deterministic enumerator and reproducible wrapper are
`twin_seed_unrestricted_switch.cpp` and `.py`. The retained order-$59$ run
used $0.027939$ internal CPU seconds and the order-$60$ run $0.015327$;
both used one thread and under $9$ MiB maximum resident memory. The
limits were not approached.

## Boundary of the conclusion

The $27$-bad-pair graph is a local minimum for strict single-switch descent,
with seven equal-energy neighbors. The $20$-bad-pair order-$60$ seed is a
strict minimum in its single-switch neighborhood. No larger switch radius,
plateau exploration, unrestricted nonexistence claim, or new legal graph
is established by this experiment.
