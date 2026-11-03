# A neutral two-switch path improves the new order-59 candidate to 26 bad pairs

Starting from the independently checked $27$-bad-pair graph, a bounded
neutral-component exploration found the path

$$27\longrightarrow27\longrightarrow26.$$

It stopped at this first strict improvement. The new graph is simple,
eight-regular on $59$ vertices with $236$ edges; independent all-source BFS
gives distance histogram

$$\{1:236,\quad2:1449,\quad3:26\}.$$

It is a failed candidate of diameter three, not a new legal construction.

## Scope and stopping rule

The input is
`computations/dd82/construction/twin_seed_unrestricted_switch_run/deflated59.step1.edges`.
The earlier complete unrestricted neighborhood had seven equal-energy
neighbors, motivating this new finite path exploration.

The search performs deterministic BFS on labelled graphs with exactly
$27$ bad pairs, using all unrestricted simple-graph two-edge switches.
It uses an ordered set of sorted edge sequences for exact deduplication.
No fiber, matching-only, triangle or route-cap restriction is imposed.
The declared limits were $100$ distinct stored states and $5$ CPU seconds,
with immediate exit at the first candidate having fewer than $27$ bad
pairs. No random or annealing moves are used.

The run stored $25$ different graphs: $24$ neutral states and the improved
endpoint. It fully expanded six states and partially expanded the seventh,
evaluating $284797$ valid switches in $0.094413$ internal CPU seconds.
The process used one thread and $8336$ KiB maximum resident memory.
Neither limit was reached. **The neutral component was not closed**, and
the $26$-bad-pair endpoint's neighborhood was not explored.

The previous report retained the start's neutral-neighbor count and one
witness, rather than all seven moves, so this task recovered the complete
start adjacency list. Its full starting histogram matches the previous
complete enumeration exactly. Each later stored state was expanded at
most once.

## Exact successful path

In original order-$60$ labels, with vertex $41$ deleted during deflation:

| Step | Removed edges | Added edges | Bad pairs |
|---|---|---|---:|
| Neutral | $(38,45),(40,53)$ | $(38,40),(45,53)$ | $27$ |
| Improving | $(38,40),(50,55)$ | $(38,55),(40,50)$ | $26$ |

The last step removes original internal Petersen edge $(50,55)$.
Both moves lie outside a single inter-fiber matching transposition.
Thus the improvement also departs from retaining all original internal
Petersen edges; the graph remains simple and eight-regular.

The JSON stores every retained state's parent and switch, the exact path,
per-expansion histograms and whether each expansion was complete. An
independent verifier reconstructs all stored states and confirms their
sorted edge sequences are distinct. It reads both path edge files,
replays both changes, and independently runs BFS from all vertices.
Every bad pair is retained with its distance, common neighbors, and the
two neighbor lists.

## Artifacts and reproduction

The run directory is
`computations/dd82/construction/twin59_neutral_component_run/`:

- `component.path1.edges`, `.json`, `.verification.json`: neutral intermediate;
- `component.path2.edges`, `.json`, `.verification.json`: improved endpoint;
- `component.json`: bounded exploration and full recoverable state/path record;
- `component.log`, `component.resources.json`, `verification.json`.

The source, wrapper and verifier are respectively
`computations/dd82/construction/twin59_neutral_component.cpp`, `.py`, and
`twin59_neutral_component_verify.py`. The C++ source reuses the previously
checked unrestricted-switch primitives through its local include.

This is a successful bounded escape from strict single-switch descent.
It proves neither optimality of the new candidate nor nonexistence of an
order-$59$ target graph.
