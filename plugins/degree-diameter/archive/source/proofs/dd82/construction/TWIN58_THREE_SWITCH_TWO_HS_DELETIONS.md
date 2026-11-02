# Genuine three-edge switches with at least two net HS deletions

Date: 2026-10-12.

One complete genuine three-edge-switch neighborhood of the new
HS-derived order-58 seed was checked, retaining only endpoints with at
least two net deleted original HS edges. Its minimum is **24 bad pairs**,
attained by 15 endpoints. Thus this neighborhood does not improve the
21-bad-pair source. The selected minimizing graph is independently
verified and itself has an obstructed fixed old core.

## Input and exact move domain

The source is
`computations/dd82/construction/twin59_to_58_deflation_run/component.path1.edges`.
It is the new graph distinguished from the earlier Brown seed in
`TWIN58_NONWORSENING_LEVELS.md`. The Brown program's matching-generation
and exact score-update method are reused; the Brown seed is never
loaded or searched.

For each unordered triple of pairwise disjoint seed edges, consider
perfect matchings on its six endpoints. There are 15 matchings:

- one retains all three original edges;
- six retain exactly one original edge and therefore perform only a two-edge switch;
- eight retain no original edge and perform a genuine three-edge switch.

Only the last eight are in this declared domain. Their symmetric
difference with the original matching is one alternating six-cycle.
The enumeration does **not** claim to include two-edge switches. Added
edges must be absent from the seed. No intermediate graph or
intermediate two-switch score is constrained: only the final endpoint
is evaluated.

The reference HS50 is the original induced graph on order-60 labels
$0,\ldots,39,50,\ldots,59$ in
`petersen_all_matchings_run/candidate.best.edges`. The source has one
missing HS edge. The new one-deletion exclusion motivates retaining
only final graphs with at least two missing reference HS edges.

## Complete enumeration and verification

| Quantity | Count |
|---|---:|
| Edge triples visited | 2054360 |
| Pairwise disjoint triples | 1698699 |
| Legal genuine three-edge switches | 9492773 |
| Rejected for fewer than two net HS deletions | 109246 |
| Eligible endpoints scored | 9383527 |
| Minimum eligible bad-pair count | 24 |
| Endpoints attaining the minimum | 15 |

The single run completed in 1.21007 internal CPU seconds under its
declared ten-second cap, using one thread and 8400 KiB maximum resident
memory. It stopped after exhausting the domain, not at a resource limit.

The exact score update uses only pairs incident to the six changed
vertices. Every other vertex retains its entire neighbor set, so pairs
with both endpoints outside the six vertices retain their adjacency
and common neighbors. If $S$ is the six-vertex set and $M(u)$ the bad
partners of $u$, the number of bad pairs incident to $S$ is

$$\sum_{u\in S}|M(u)|-\frac12\sum_{u\in S}|M(u)\cap S|.$$

Subtracting this expression before the edit and adding it afterward
gives the full new score. The program cross-checked 144 such scores
against a complete distance-two calculation during the run.

The independent verifier replays the selected edit and performs
all-source BFS directly on its edge file. It also independently checks
the 15 matching patterns and the disjoint-triple count. The latter
follows by counting independent triples in the line graph:

$$\binom{232}{3}-1624\cdot230+232\binom{14}{2}
 -(58\binom83+5)=1698699.$$

Here the final term uses the source's five triangles. No second
candidate-scoring enumeration was performed.

## Selected minimizing graph and old-core failure

Use original order-60 labels below; original vertices 41 and 42 are
absent. The selected edit removes

$$\{(0,55),(3,12),(9,14)\}$$

and adds

$$\{(0,9),(12,55),(3,14)\}.$$

Its net missing HS edges are exactly $(0,55),(50,55)$, and its old
non-HS additions are

$$\{(0,9),(3,14),(12,55),(28,29),(38,55)\}.$$

It is simple, eight-regular, has 58 vertices and 232 edges, and its
independent distance histogram is

$$\{1:232,\qquad2:1397,\qquad3:24\}.$$

Relative to the source it repairs two bad pairs, retains nineteen and
introduces five. Complete witnesses are saved.

Its old induced graph has zero-port vertices
$3,9,12,14,28,29,38$. The old pairs $(9,55),(14,55),(28,55)$ are still
nonadjacent with no common old neighbor. Since one endpoint is
saturated, these pairs remain uncovered in every completion that keeps
this old induced graph.

For zero-port vertices 3 and 29, the sum of their old neighbors'
auxiliary-port capacities is only seven, below the eight auxiliary
vertices that must be reached. Each therefore contributes at least one
additional old–auxiliary bad pair. The other zero-port capacity sums
are 9, 8, 8, 8, 9 for vertices 9, 12, 14, 28, 38 respectively.

Consequently every attachment/auxiliary-only completion retaining this
selected old core has **at least five bad pairs**. Meeting the necessary
two-deletion threshold does not make this core completable. This
observation is specific to the saved minimizing graph; it is not a
claim about arbitrary two-deletion cores or arbitrary order-58 graphs.

## Files and reproduction

The directory
`computations/dd82/construction/twin58_three_switch_two_hs_deletions_run/`
contains `neighborhood.json` with complete histograms and edit trace,
`neighborhood.best.edges` and `.json`, the full BFS witnesses in
`neighborhood.best.verification.json`, and the fixed-core checks in
`neighborhood.best.old_core_obstruction.json`. It also contains
`verification.json`, the process log and resource record.

From the project root:

```sh
g++ -O3 -std=c++17 computations/dd82/construction/twin58_three_switch_two_hs_deletions.cpp -o computations/dd82/construction/twin58_three_switch_two_hs_deletions.bin
python computations/dd82/construction/twin58_three_switch_two_hs_deletions.py
python computations/dd82/construction/twin58_three_switch_two_hs_deletions_verify.py
```

No further search was run from the 24-bad-pair endpoint. The source's
21 bad pairs remain the better recorded value; neither graph is a
diameter-two target.
