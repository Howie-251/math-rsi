# Deflating the 24 order-59 states produces an order-58 graph with 21 bad pairs

Complete deletion-and-repair enumeration over the 24 saved order-59
states gives a minimum of **24 bad pairs**. A subsequent bounded
unrestricted two-edge-switch episode finds a graph with **21 bad pairs**
and stops at that first improvement. Independent all-source BFS confirms
the resulting graph is simple, eight-regular, has 58 vertices and 232
edges, and has unordered distance histogram

$$\{1:232,\qquad 2:1400,\qquad 3:21\}.$$

It remains a failed diameter-three candidate, not a new lower bound.

## Complete deflation choices

The input contains all 24 complete graphs in
`computations/dd82/construction/twin59_nonworsening_levels_run/expanded_states.json`.
Their neutral component is documented in `TWIN59_NONWORSENING_LEVELS.md`;
that order-59 search was not rerun.

For every input graph and every vertex $v$, delete $v$ and enumerate all
$7!!=105$ perfect matchings on its eight former neighbors. Reject a
matching if any proposed edge already exists. Otherwise its four edges
restore degree eight at every affected vertex. The edge count is
$236-8+4=232$, and simplicity follows from the rejection test.

| Quantity | Count |
|---|---:|
| Input labelled graphs | 24 |
| Vertex-deletion / repair choices | 148680 |
| Choices rejected for an existing repair edge | 1080 |
| Valid choices scored | 147600 |
| Minimum bad-pair count | 24 |
| Choices attaining that minimum | 360 |

These are counts of choices, without deduplicating resulting graphs.
The full global and per-source histograms are saved in `deflation.json`.
The exhaustive enumeration used 0.090745 internal CPU seconds.

The first minimizing choice uses source node 0 and deletes vertex 41 in
the current order-59 numbering. Its repair edges, in that same numbering,
are

$$\{(3,12),(28,29),(39,46),(42,54)\}.$$

After deletion, labels above 41 decrease by one. The original order-60
vertex 41 was already absent, so the second deleted vertex corresponds
to original order-60 vertex 42. The complete minimizing graph is saved
as `deflation.best.edges` and `.json`. Its independent distance histogram
is $\{1:232,2:1397,3:24\}$.

## One bounded nonincreasing episode

Starting from this new order-58 graph, deterministic BFS retains graphs
with 24 bad pairs and stops at the first smaller value. The move set is
all simple, degree-preserving two-edge switches, with exact deduplication
by an ordered set of sorted edge sequences. The declared limits are 100
stored states and 5 CPU seconds. The implementation uses $n=58$ and the
58-bit live-vertex mask.

The first strict improvement occurs after 38453 valid switch evaluations,
within the partially expanded starting neighborhood. The search stores
24 states: 23 neutral graphs including the seed and one improved graph.
It uses 0.017625 internal CPU seconds. No state is fully expanded, and no
resource cap is reached. The two C++ processes together use 0.116162 CPU
seconds including process overhead, on one thread.

The improving switch, in the new order-58 numbering, is

$$\{(39,45),(42,49)\}\longmapsto\{(39,42),(45,49)\},$$

reducing the bad-pair count from 24 to 21. In source order-59 labels it
removes $(39,46),(43,50)$ and adds $(39,43),(46,50)$. Thus it changes one
new repair edge and one surviving source edge; it goes beyond the
preceding fixed-source deletion-and-perfect-matching choices.

The new graph is `component.path1.edges` and `.json`. Its neighborhood
was not explored. Neither the initial neutral component nor a local
minimum at 21 has been certified.

## Checks and reproduction

The independent Python verifier accounts for all 148680 choices and
recomputes the existing-edge rejection counts. It reconstructs the
minimizing graph directly from its source, deleted vertex and repair,
then reconstructs every retained switch state and checks exact
distinctness. All 24 retained order-58 states receive independent
all-source BFS checks, with full bad-pair witnesses saved. The original
C++ scores and the BFS results agree.

All outputs are under
`computations/dd82/construction/twin59_to_58_deflation_run/`:

- `deflation.best.edges`, `.json`, `.verification.json`: the minimizing deflation;
- `component.path1.edges`, `.json`, `.verification.json`: the 21-bad-pair endpoint;
- `deflation.json`: exhaustive choice counts and histograms;
- `component.json`: exact parent/switch records and partial expansion histogram;
- `episode.expanded_states.json`, `verification.json`: all retained graphs and BFS checks;
- log files and resource records for both runs.

From the project root, the commands are:

```sh
g++ -O3 -std=c++17 computations/dd82/construction/twin59_to_58_deflation.cpp -o computations/dd82/construction/twin59_to_58_deflation.bin
g++ -O3 -std=c++17 computations/dd82/construction/twin58_deflated_neutral_component.cpp -o computations/dd82/construction/twin58_deflated_neutral_component.bin
python computations/dd82/construction/twin59_to_58_deflation.py
python computations/dd82/construction/twin59_to_58_deflation_verify.py
```

The complete finite statement concerns only the 148680 specified
deflation choices. The subsequent episode is a successful first-improving
path, with no nonexistence conclusion for order 58 and no further search
after the 21-bad-pair endpoint.
