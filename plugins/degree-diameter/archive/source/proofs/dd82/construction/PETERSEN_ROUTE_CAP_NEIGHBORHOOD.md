# Complete two-transposition neighborhood of the 50-bad-pair seed

## Result and exact scope

The saved graph `petersen_six_fibers.best.edges` is the unique minimum within
its radius-two matching-transposition neighborhood among final graphs
satisfying the necessary route cap. It has $50$ uncovered pairs; every
distinct cap-feasible neighbor has at least $57$. Among distinct graphs
reached by exactly two transpositions, the minimum is $64$.

The neighborhood allows transpositions in **all fifteen** inter-fiber
matchings. The six internal Petersen graphs and the fiber partition stay
fixed. Every one of the $675$ first moves was expanded, including those
whose intermediate graph violates the cap. No annealing or SAT was run.
This is a complete bounded neighborhood result, not an exclusion of the
six-fiber family or arbitrary order-$60$ graphs.

## Why the final cap is necessary

For a source in one fiber and a different target fiber there are exactly
$11$ direct-or-two-step route slots to ten targets: one direct, three from
each endpoint's internal Petersen graph, and four from the other fibers.
If every target is reached, exactly one target is reached twice and the
other nine once. Thus a valid target graph necessarily satisfies

$$A_{uv}+|N(u)\cap N(v)|\le2$$

for every cross-fiber pair $u,v$. We impose this only on the final graph
being evaluated. Within a fiber the Petersen paths already give exact
coverage, and external perfect matchings cannot add common neighbors to a
same-fiber pair.

## Enumeration and completeness

A move chooses one of $15$ matchings and two of its $10$ source coordinates,
then exchanges their matched targets. There are
$15\binom{10}{2}=675$ choices. Applying all $675^2=455625$ ordered pairs
covers every graph at matching-transposition distance at most two, after
also including the seed and all single moves.

The full double loop performs no first-move cap pruning. It found $2775$
cap-feasible ordered double moves. Of these, $825$ have a cap-violating
first move; these would have been omitted by an incorrectly pruned search.
This count includes reversals returning to the seed, so it does not assert
that all $825$ represent new endpoints inaccessible through another order.

Duplicate endpoints can be counted without hashes. Moves in different
matchings commute and are canonically ordered by matching index. Two
disjoint transpositions in one matching are canonically ordered by their
source pair. For two overlapping transpositions, their product is a
three-cycle: exactly one factorization starts with the two smallest of its
three moved coordinates. Equal transpositions return to the seed.
Consequently the number of distinct double endpoints is

$$1+\binom{15}{2}\binom{10}{2}^2
+15\left(3\binom{10}{4}+2\binom{10}{3}\right)=225676.$$

Single moves have odd total permutation parity and cannot equal a double
endpoint. Thus the radius-two neighborhood has $225676+675=226351$ distinct
graphs, including the seed. The program's canonical counters equal these
closed-form counts.

## Complete outcome counts

The recomputed single-move list matches the earlier root enumeration
entry for entry: $50$ cap-feasible moves, with $25$ producing $57$ bad pairs
and $25$ producing $66$.

The distinct cap-feasible double endpoints, including the seed, have this
histogram:

| Bad pairs | 50 | 64 | 65 | 71 | 72 | 73 | 74 | 78 | 80 | 82 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Distinct graphs | 1 | 225 | 50 | 125 | 25 | 350 | 25 | 50 | 50 | 125 |

There are $1026$ such double endpoints, and $1076$ cap-feasible graphs in
the full radius-two neighborhood including single moves. The sole graph
with $50$ bad pairs is the original seed. Therefore no diameter-two graph
occurs anywhere in this neighborhood, even when the intermediate graph is
allowed to violate the route cap.

## Saved candidates and independent verification

The best distinct neighbor exchanges source coordinates $0,5$ in the
matching from fiber $0$ to fiber $2$. It is a simple $60$-vertex $8$-regular
graph with $240$ edges and distance histogram

$$\{1:240,\quad2:1473,\quad3:57\}.$$

The best distinct double neighbor additionally exchanges source coordinates
$2,7$ in the same matching. Its distance histogram is

$$\{1:240,\quad2:1466,\quad3:64\}.$$

The independent Python verifier reads the saved edge lists, reconstructs
ordinary adjacency sets, performs BFS from every vertex, and saves every
bad pair together with its common-neighbor set and both neighbor lists.
It also replays the saved transpositions from the seed and independently
checks all cross-fiber route counts. Both candidates satisfy the cap but
fail diameter two.

## Reproduction and resources

Files under `computations/dd82/construction/`:

- `petersen_route_cap_neighborhood.cpp` and `.bin`: exhaustive enumerator;
- `petersen_route_cap_neighborhood.py`: reproducible execution wrapper;
- `petersen_route_cap_verify.py`: independent graph and move-replay checks;
- `petersen_route_cap_two_switches.json`, `.log`, `.resources.json`;
- `petersen_route_cap_two_switches.best.edges`, `.best.verification.json`;
- `petersen_route_cap_two_switches.best_double.edges`, `.best_double.verification.json`;
- `petersen_route_cap_two_switches.verification.json`: combined check report.

From the project root:

```bash
g++ -O3 -march=native -std=c++17 -Wall -Wextra computations/dd82/construction/petersen_route_cap_neighborhood.cpp -o computations/dd82/construction/petersen_route_cap_neighborhood.bin
python computations/dd82/construction/petersen_route_cap_neighborhood.py
python computations/dd82/construction/petersen_route_cap_verify.py
```

The retained enumeration used one thread, $0.156095$ internal CPU seconds
($0.159329$ total child CPU seconds), and $8536$ KiB maximum resident memory.
The wrapper enforces a $20$-CPU-second hard limit and $4$ GiB address-space
limit. An initial complete pass took $0.153488$ CPU seconds; the retained
pass added the separate best-double artifact and process-specific resource
accounting. No search budget extension was needed.
