# Actual HS58 four-addition constructions and joint completion

Date: 2026-10-12. No diameter-two graph was found. This experiment moves
from the previous complete three-addition seeds to actual four-addition
graphs, then releases all four old additions and all old-new edges in one
specified auxiliary type. It does not classify all placements of two
deleted HS edges.

## Complete construction step

The two inputs are the old-cover seeds in
`computations/dd82/construction/hs58_two_delete_three_add_seeds_run/old_cover/`.
They have 58 vertices, 232 edges, all degrees eight, and respectively
83 and 82 bad pairs, all old-new. Both have

```
D = {(0,1),(10,11)}
A = {(25,26),(35,41),(2,4)}.
```

For each unordered pair of attachment edges `x--(50+a), y--(50+b)`,
require distinct old and new endpoints, an absent original-nonedge `xy`,
and an absent auxiliary edge `ab`. Remove the two attachments and add
`xy` and `ab`. This preserves every degree, the original deletion set,
and simplicity; it changes exactly three old additions to four and eight
auxiliary edges to nine.

The complete stated domains contain 728 and 719 proposals. Every proposal
was expanded and all pairs checked using fresh adjacency bitmasks. Their
minimum bad-pair counts are 81 and 77. For each of the 20 possible labeled
auxiliary-edge additions in each parent, the best complete graph was saved,
giving 40 explicit graphs, each independently checked by the existing
standalone BFS implementation. Every saved graph has degree eight and
diameter three. These poor candidates are not lower-bound progress.

The overall best transition removes `5--57, 24--54` and adds `5--24, 54--57`.
Its 77 bad pairs are all old-new. Its auxiliary graph is catalog type10,
one of the types subsequently excluded by the saturated-port argument.
The best generated graph in a still-open type at selection time is
`parent3_h2_6.json`: 79 bad pairs, all old-new, auxiliary catalog type8.
It removes `3--52,16--56` and adds `3--16,52--56`.

Source: `computations/dd82/construction/hs58_two_delete_four_add_switch.py`.
Actual results and all graphs, edge lists, and full BFS failure records are
under `hs58_two_delete_four_add_switch_run/`. `type_mapping.json` matches
these forty auxiliary graphs to the complete eleven-type catalog by exact
graph isomorphism; it is navigation, not a theorem dependency.

The parent used 0.340211855 CPU seconds, independent BFS children used
1.194971 CPU seconds, and total wall time was 1.621902283 seconds. The
parent CPU cap was ten seconds. No local-search restart occurred.

## Joint completion with all old additions free

The next input retains the same exact labeled D and fixes H from
`parent3_h2_6.json`, but freezes none of its four additions or attachments.
There are 1,050 variables for all original HS nonedges and 400 variables
for all old-new pairs. All 173 nondeleted HS edges are retained; the two
deleted original edges cannot be readded. Exactly four original nonedges
are selected.

For an old vertex x, the exact degree constraint is

`sum(incident addition variables) + sum(B[x,*]) = 8 - d_(Q-D)(x)`.

For each new vertex a, the column sum of B is `8-d_H(a)`. For every pair
not already covered by fixed edges alone, the CNF requires its direct-edge
literal or at least one actual two-edge path. The paths include A-A, A-B,
fixed-A, fixed-B and B-B combinations whenever the endpoints permit them.
Each conjunction is encoded in both directions. There is no symmetry
normalization or fixed attachment.

This gives 32,437 variables and 102,312 clauses. Precisely 1,224 pairs are
already covered by fixed edges; the remaining clauses cover 26 old-old,
400 old-new, and 3 new-new pairs. The counts sum to all 1,653 pairs of a
58-point graph. CNF generation used 0.133411544 CPU seconds and
0.134992272 wall seconds.

The sole ten-CPU-second call returned UNSAT in 0.354425 CPU seconds and
0.367880907 wall seconds. The emitted LRAT proof was checked against that
actual CNF by `lrat-trim --no-trim`; it returned exit20 and `s VERIFIED`,
using 0.023120 CPU seconds and 0.025737245 wall seconds. The result is
**CHECKED_UNSAT for this exact D and labeled H with all four additions and
all attachments free**. No completeness claim for other placements of D
comes from this run, and no solver restart was needed.

Source: `computations/dd82/construction/hs58_two_delete_four_add_joint.py`.
Actual CNF, LRAT, solver/checker logs, variable maps and resource records
are in `hs58_two_delete_four_add_joint_run/`. The separate
[encoding review](HS58_TWO_DELETE_FOUR_ADDITIONS_JOINT_ENCODING_REVIEW.md)
reads the actual source, helper, metadata and checked result; it found no
loss of candidates and did not rerun the solver.

After this call finished, the parallel mathematical derivation excluded
all disjoint-D cases in the three K1,3 auxiliary types, including type8.
That broader argument does not depend on this fixed-placement certificate.
The calculation is retained as the actual construction attempt and its
failure feedback, rather than being relabeled as a global classification.
