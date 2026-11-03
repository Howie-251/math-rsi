# Two improved parameters and 38 complete graph examples

The strongest independently checked graphs prove

- **N(11,5) ≥37631**, compared with the official source value37628.
- **N(12,5) ≥42377**, compared with the official source value42342.

The official diameter-five description was refreshed in this turn on2026-10-27; its Dhar_37628 and Dhar_42342 sections still give those source values. This is a comparison with the checked public lower bounds, not an optimality or publication-acceptance claim.

## The complete families

For maximum degree11, retain all205296 edges of Dharunish Yugeswardeenoo's37628-point graph and use the three saved complete neighbor lists, in order. This gives graphs of orders37629,37630,37631, with205296+11j edges for j=1,2,3.

For maximum degree12, retain all245217 edges of the author's42342-point graph and use the35 saved complete neighbor lists, in order. This gives every order42343 through42377, with245217+12k edges for k=1,...,35. The first was the original42343 result, two further steps gave42345, and32 more steps gave42377.

These are38 complete examples at two parameter pairs. Different orders guarantee that these38 graphs are distinct. The examples share a geometric construction mechanism; their number is not a count of independent methods or improved parameter pairs.

## Complete coverage at each step

For each step let B be the actual graph before the new vertex z is added, and let A be the saved complete neighbor set. No old vertex or edge is removed. Each vertex in A has old degree strictly below its degree cap, the members of A are distinct, and |A| is11 or12 respectively.

Root independently recomputed the complete multi-source radius4 cover of A **in B before z or any future vertex was added**. Every existing vertex was covered. Thus for every old x there is a∈A and an old B-walk from a to x of length≤4; prepending z--a gives distance≤5. All old--old routes are preserved. There is only one new vertex per step, so no separate pair of newly introduced vertices remains unchecked. This proves the entire family by induction from the independently checked first graphs.

This argument does not infer that prefixes have diameter5 merely by deleting vertices from the largest graph. Every prefix has its own complete earlier-graph coverage check. In particular, the intermediate graphs37630 and42344 were checked by this route certificate, rather than being mislabeled as separate all-source BFS runs.

The saved independent all-source BFS checks from expanded edge lists include:

| Graph | Edges | Maximum degree | Exact diameter | BFS roots | Bad/unreachable unordered pairs |
|---|---:|---:|---:|---:|---:|
| 37629 | 205307 | 11 | 5 | 37629 | 0/0 |
| 37631 | 205329 | 11 | 5 | 37631 | 0/0 |
| 42343 | 245229 | 12 | 5 | 42343 | 0/0 |
| 42345 | 245253 | 12 | 5 | 42345 | 0/0 |
| 42377 | 245637 | 12 | 5 | 42377 | 0/0 |

All are simple and connected. The most recent strongest checks used4 workers:37631 took10.2909 wall/41.0824 CPU seconds;42377 took15.1431 wall/60.4583 CPU seconds. The checker reads the expanded edge list and does not share the search's reachability cache.

For every family prefix, the order is above the relevant radius4 Moore bound:12222 for degree11, and17569 for degree12. Therefore its diameter is exactly5, since its proved upper bound is5.

## Generation and attribution

`delivery/families.json` stores every literal new-vertex label and complete neighbor set. `delivery/family_generator.py` deterministically generates any requested family prefix from the saved original source adjacency. The strongest graph files and independent check results remain in their original research directories.

The complete public base graphs belong to **Dharunish Yugeswardeenoo**, using the partial-fold and duality foundation of **Rishabh Rajiv**. The new work is these explicit extensions, recovered geometric attachment rules, bounded complete searches and finite verification. Source selection/geometry is not a premise that can replace checking the actual graph.

## Remaining formal scope

The generic Lean single-vertex extension and parent/depth certificate soundness theorems compile. The complete concrete graph instances and old-source diameter proofs have not yet been assembled in Lean. Thus this is a mathematically verified construction family with pending formalization, not a completed formal Goal. The user's latest instruction puts active work back on finding further graph examples; the existing formal sources and certificate data are retained.
