# A bounded nonincreasing episode from the new order-58 graph

Date: 2026-10-12.

The new HS-derived order-58 seed is not isomorphic to the earlier Brown
seed. One declared, bounded nonincreasing two-edge-switch episode finds
no improvement before its CPU limit. The final graph still has **21 bad
pairs**, so it is not a diameter-two construction. Its fixed old induced
graph also has a direct obstruction: changing only attachments and the
auxiliary graph leaves at least six bad pairs.

## Distinct input and actual failure

The input is
`computations/dd82/construction/twin59_to_58_deflation_run/component.path1.edges`,
whose construction and first improvement are recorded in
`TWIN59_TO_58_DEFLATION.md`. Both it and
`computations/dd82/construction/brown58_three_switch.seed.edges` are
eight-regular order-58 graphs with 21 bad pairs, but their direct graph
invariants differ:

| Invariant | New HS-derived seed | Earlier Brown seed |
|---|---:|---:|
| Triangle count | 5 | 56 |
| Maximum common-neighbor count | 5 | 2 |
| Adjacent pairs with a common neighbor | 15 | 168 |

In particular, the triangle count proves nonisomorphism. The complete
common-neighbor histograms and actual bad pairs were saved before the
new search. No Brown search or previous order-59 exploration was rerun.

## Declared episode and stopping scope

The algorithm reuses `twin59_nonworsening_levels.cpp`, adapting the graph
size and live-vertex mask to 58 and the initial bad-pair count to 21.
It expands unrestricted simple-graph, degree-preserving two-edge switches
in deterministic order. Neutral states are traversed by BFS; the first
strict improvement would be saved and start a fresh level. Exact
deduplication uses an ordered set of sorted labelled edge sequences.

The bounds, fixed before execution, were 2000 total retained states,
10 CPU seconds, and 20 strict improvements. The total-state limit is
at least as restrictive as a 2000-neutral-state limit. There are no
random or increasing moves.

| Result | Value |
|---|---:|
| Initial / final bad-pair count | 21 / 21 |
| Retained distinct neutral states | 1127 |
| Completely expanded states | 530 |
| Partially expanded states | 1 |
| Evaluated valid switches | 20810752 |
| Strict improvements | 0 |
| Recorded internal CPU time | 10.0025 seconds |
| Threads / maximum resident memory | 1 / 8528 KiB |

The stop reason is `global_cpu_cap`; the bound is checked every 512
candidate evaluations. No time was added and no subsequent repair
episode was launched. **The neutral component is not closed.** The
evaluation count counts transitions from source states, not globally
distinct neighbor graphs, and supplies no exclusion outside the portion
actually explored.

Every retained graph was reconstructed from its parent and exact switch,
checked for distinctness, and independently tested by all-source BFS.
All 1127 have the recorded 21 bad pairs. Full edge lists for all states
are saved. There are no new improving candidates to verify; the final
graph is identical to the input. Its independent distance histogram is

$$\{1:232,\qquad2:1400,\qquad3:21\}.$$

## A fixed-old-core obstruction from the final graph

For this analysis use original order-60 labels. Original vertices 41
and 42 have been deleted; current order-58 labels below 41 are unchanged,
and labels at least 41 map to the original label plus two.

Let $O=\{0,\ldots,39,50,\ldots,59\}$ be the original HS50 core. The
eight auxiliary vertices are $X=\{40,43,\ldots,49\}$. Relative to that
HS core, the final old induced graph $F$ deletes $(50,55)$ and adds

$$\{(3,12),(9,14),(28,29),(38,55)\}.$$

It has 178 edges. Put $p_u=8-d_F(u)$, the maximum number of auxiliary
neighbors available to an old vertex in any maximum-degree-eight
completion retaining $F$. The port-count distribution is

$$\#\{u:p_u=0\}=7,\quad\#\{u:p_u=1\}=42,\quad
\#\{u:p_u=2\}=1.$$

The zero-port vertices are $3,9,12,14,28,29,38$; vertex 50 has two ports.
The actual graph has 44 old–auxiliary incidences and ten auxiliary edges.
Its 21 bad pairs split as five old–old, fifteen old–auxiliary, and one
auxiliary–auxiliary pair.

**Fixed-core claim.** Any maximum-degree-eight graph retaining $F$ and
these eight auxiliary vertices has at least six bad pairs, irrespective
of its attachments and auxiliary edges.

First, $(9,55),(14,55),(28,55)$ are nonedges with no common old neighbor
in $F$. Vertices 9, 14 and 28 have no auxiliary-neighbor capacity, so
none of these three pairs can acquire a common auxiliary neighbor.
They remain bad pairs in every such completion.

Second, each of the saturated vertices $u=3,12,29$ has

$$\sum_{w\in N_F(u)}p_w=7.$$

Its eight old neighbors include one zero-port vertex and seven one-port
vertices. Since $u$ has no auxiliary neighbors, every path of length at
most two from $u$ to $X$ must use an attachment from an old neighbor of
$u$. Those neighbors have only seven attachment slots in total and
therefore reach at most seven of the eight auxiliary vertices. Thus
each of $3,12,29$ has at least one bad old–auxiliary pair. These three
pairs are distinct and are separate from the three forced old–old
pairs, proving the lower bound six.

In the actual graph these additional three witnesses are
$(3,43),(12,43),(29,43)$. The complete old-neighbor and port data are
saved in `failure_structure.json`. This argument applies only when $F$
is retained; it does not constrain arbitrary changes to old–old edges,
all states in the partially explored component, or other order-58
constructions. It uses no conditional N15 or triangle bound.

## Files and reproduction

All results are in
`computations/dd82/construction/twin58_nonworsening_levels_run/`:

- `seed_comparison.json`: direct invariants separating the two seeds;
- `episode.json`: source, bounds, parent/switch records and expansion histograms;
- `expanded_states.json`: all 1127 complete labelled graphs;
- `verification.json`: independent BFS summaries for every retained state;
- `final.edges`, `.json`, `.verification.json`: final graph and all bad-pair witnesses;
- `failure_structure.json`: exact HS-core edits, partition and obstruction data;
- `episode.log`, `episode.resources.json`: stopping and resource records.

The source is `twin58_nonworsening_levels.cpp`, with the same basename
for its Python runner. From the project root:

```sh
g++ -O3 -std=c++17 computations/dd82/construction/twin58_nonworsening_levels.cpp -o computations/dd82/construction/twin58_nonworsening_levels.bin
python computations/dd82/construction/twin58_nonworsening_levels.py
python computations/dd82/construction/twin58_nonworsening_levels_verify.py
python computations/dd82/construction/twin58_nonworsening_failure.py
```

The independent checks reconstructed saved states and analyzed the final
graph; they did not repeat the 20810752 candidate-scoring evaluations.
