# The new order-59 candidate has a closed 24-state neutral component

The complete neutral component of the previously constructed graph with
26 bad pairs contains exactly **24 labelled graphs**. Exhausting every
unrestricted two-edge-switch neighborhood of these graphs finds no
strict improvement. Consequently, no sequence of switches with
nonincreasing bad-pair count can improve this particular seed.

The seed is
`computations/dd82/construction/twin59_neutral_component_run/component.path2.edges`,
obtained by the path recorded in `TWIN59_NEUTRAL_COMPONENT.md`.
All 24 graphs are simple, eight-regular, have 59 vertices and 236 edges,
and have independently checked unordered distance histogram

$$\{1:236,\qquad 2:1449,\qquad 3:26\}.$$

Thus none is a diameter-two construction.

## One bounded episode

The move removes two edges on four distinct vertices and inserts either
other pairing, provided both inserted edges were absent. Every such
simple-graph switch is allowed; fiber structure and route multiplicity
place no restrictions on the moves.

The deterministic algorithm performs BFS among graphs at the current
bad-pair count, resetting the level upon the first strict improvement.
Exact deduplication uses an ordered set of sorted labelled edge sequences.
The declared limits were 1000 stored states across all levels, 10 CPU
seconds and 20 strict improvements. No random, worsening or annealing
moves are used.

| Quantity | Result |
|---|---:|
| Initial and final bad-pair count | 26 |
| Stored states, all fully expanded | 24 |
| Valid switches from each state | 40825 |
| Total evaluated switches | 979800 |
| Strict improvements | 0 |
| Neutral neighbors of each state | 6 |
| Edges of the connected neutral state graph | 72 |
| Internal search CPU time | 0.429590 seconds |
| Threads / maximum resident memory | 1 / 8552 KiB |

The evaluated-switch total counts transitions from each source state,
not globally distinct neighbor graphs. The 24 retained states are
distinct. The run stopped because the neutral component was completely
closed, with no lower-count exit; no resource cap was reached.

To justify the consequence, suppose a nonincreasing switch path first
reached a graph with fewer than 26 bad pairs. Every preceding graph
would have exactly 26 bad pairs, hence would belong to the enumerated
neutral component. The first decreasing move would therefore be a
lower-count neighbor of one of its 24 states, contrary to the complete
neighborhood enumeration.

## Reconstruction and independent checks

The verifier replays every stored parent/switch record and checks all
24 sorted edge sequences are distinct. It independently performs BFS
from every vertex of every reconstructed graph, saving all bad pairs
with distances, common-neighbor lists and both endpoint neighbor lists.
It also independently counts the legal switches from each graph.

Comparing the 24 edge sets reconstructs a connected, six-regular neutral
state graph. Its neutral degrees match the energy-26 counts in every
complete neighborhood histogram. All histogram totals match the legal
switch counts, and no histogram contains a value below 26. These checks
reuse the original neighborhood scores; they do not rerun the 979800
candidate-scoring experiment.

The seed's separate structural record reports 21 bad-pair endpoints,
with current vertices 41 and 54 each incident to seven bad pairs. It has
one triangle and maximum common-neighbor count five. These are
descriptive failure data, without imposing any conditional N15 bound.

## Files and scope

The run directory is
`computations/dd82/construction/twin59_nonworsening_levels_run/`:

- `episode.json`: all parent/switch records, per-state histograms and level statistics;
- `expanded_states.json`: complete edge lists for all 24 states;
- `verification.json`: reconstruction checks, neutral adjacency and all BFS witnesses;
- `episode.log` and `episode.resources.json`: stopping and resource records.

The source and wrapper are
`computations/dd82/construction/twin59_nonworsening_levels.cpp` and `.py`;
the independent verifier is `twin59_nonworsening_levels_verify.py`.
From the project root, reproduction commands are:

```sh
g++ -O3 -std=c++17 computations/dd82/construction/twin59_nonworsening_levels.cpp -o computations/dd82/construction/twin59_nonworsening_levels.bin
python computations/dd82/construction/twin59_nonworsening_levels.py
python computations/dd82/construction/twin59_nonworsening_levels_verify.py
```

This closes only the nonincreasing unrestricted-switch component of the
fixed labelled seed. It does not exclude paths that first increase the
bad-pair count, other seeds, or any order-59 target graph. No additional
repair experiment was performed after component closure.
