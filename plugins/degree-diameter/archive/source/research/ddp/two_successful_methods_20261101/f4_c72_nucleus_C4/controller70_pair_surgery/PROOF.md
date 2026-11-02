# Exoo72 adjacent-pair deletion plus crossmatching: all4320 controllers fail

## Exact operation and result

For each of the180 edges u<v of the saved Exoo72 source, remove u,v. Write
A=N(u)\{v} and B=N(v)\{u}, each of size4. Add one of the24 perfect matchings
between A and B, retaining every other edge. This gives4320 parameter
assignments, not necessarily4320 distinct graphs. Every resulting graph is
on70 vertices and has175 edges; simplicity and5regularity follow from the
verified boundary structure and were also checked literally on all312
survivors of the first necessary gate.

No assignment has controller diameter≤3. The initial precise same-side gate
rejects4008; the312 survivors each have an explicitly saved root and target
not connected within3 in the new70controller. A stronger structural
explanation below excludes all4320 at once using the source's saved unique
three-step cross pairs. No fiber graph, rank-map model or SAT call is reached.

The exclusion concerns exactly this source and this operation. It is not
an exclusion of arbitrary70vertex5regularD3 controllers or of(22,3) graphs.

## Why the first same-side cut is valid, including existing routes

Let H=G−{u,v}. The actual source has no triangles or4cycles. For every one
of180 source edges, the data confirms A and B are disjoint and A∪B has no
old edges. Also, any two distinct vertices on one side have no common
neighbor in H: the old common neighbor u or v was removed, and another
would make a4cycle in G. These2160 adjacency-intersection checks are saved
in STRUCTURAL_CROSS_OBSTRUCTION.json; they are not old source-diameter BFS.

Define D[i,j] to mean that A_i and B_j have a common old neighbor in H. For
matching σ, a new path of length≤3 from A_i to A_j either already lies in H
or uses exactly one matching edge, at its first or last step. A matching
edge in the middle would require an old edge between two boundary vertices;
two matching edges cannot be used consecutively on a simple path, or with
one intervening old boundary edge. Hence the exact condition is

    existing_H_distance(A_i,A_j)≤3
      OR D[j,σ(i)] OR D[i,σ(j)].

The B-side condition is symmetrically

    existing_H_distance(B_i,B_j)≤3
      OR D[σ⁻¹(i),j] OR D[σ⁻¹(j),i].

The existing_H term is essential. Across the180 deleted edges,1512 same-side
pairs already have a length≤3 alternative in H; they were retained, rather
than rejected by an overly strong D-only cut. BOUNDARY_CERTIFICATE.json
saves every D matrix, every existing-route Boolean and the first failing
pair for each rejected matching. The independent logical derivation above
uses actual structural facts, not an assumption that the source's former
two-step route was unique.

## Actual finite progression

`preflight.py` checks all4320 operations with that exact necessary gate:

- 3072 first fail an A-side pair;
- 936 first fail a B-side pair;
- 312 survive all12 same-side pair obligations.

One rejected matching's targeted new-adjacency pair check confirms that its
predicted missing≤3 route is indeed absent. No full70controller check is
needed for those4008 failures.

`check_survivors.py` constructs only the312 boundary survivors as literal
simple5regular70vertex graphs. For each, new-controller radius3 checks stop
as soon as a missing target appears. All fail, at dense-label roots0..8;
SURVIVOR_OUTCOMES.json records the actual removed pair, matching, first bad
root, unreachable target and root coverage. These are new-controller
acceptance tests, not a rerun of Exoo72's known D3 status.

Preflight and survivor checking together measured0.165369792CPU, single
worker, within20CPU. No new controller reaches the unique-route map gate,
so conic24/general120 domain models are not generated for these operations.

## Stronger reason: one boundary vertex needs two direct matching edges

Take a cross pair A_i,B_j whose unique old path of length≤3 is

    A_i → u → v → B_j.

There is no alternative path of length≤3 in H. If this pair is not itself
an added matching edge, no other matching edge can repair it in≤3:

1. A path using no matching edge would be an already absent H route.
2. A matching edge in the middle of a three-step path is impossible because
   A∪B has no old edge.
3. If the matching edge is first, it goes A_i→B_σ(i). For σ(i)≠j the remaining
   at most2 old steps would connect two distinct B vertices, which have no
   old edge or H common neighbor. The last-edge case is the same argument
   for two distinct A vertices.
4. Two matching edges in a simple path of length≤3 would need an intervening
   old edge within A∪B, or immediately backtrack along the same matching
   edge. Neither gives a new short path.

Therefore every unique old cross pair centered on u-v must be repaired by
that exact direct matching edge.

The already saved Exoo unique-route ledger contains3 such distinct cross
pairs on24 source edges,6 on132 edges, and9 on24 edges. More strongly,
**every one of the180 source edges has at least two of these pairs sharing
one boundary vertex.** A perfect matching gives that vertex only one new
edge, while repairing both pairs would require degree at least2 in the
matching. This is impossible.

STRUCTURAL_CROSS_OBSTRUCTION.json saves, for every source edge, two actual
unique endpoint pairs sharing one A or B vertex, their complete old
three-word witnesses and the required2-versus-available1 matching degree.
It reuses the existing route ledger; no controller distances or shortwords
are recomputed in this explanatory step. Its measured CPU is0.028433571.

The numerical sequence above remains recorded as actually executed. The
later structural proof is an explanation and stronger reusable decision,
not a claim that the earlier312 checks were skipped.

## Decision changed by the result

Crossmatching does replace a selected former A-u-v-B route by one edge, but
it cannot replace all unique cross routes sharing that same endpoint. The
observed failure is a simultaneous-route incompatibility, not merely a
small decline in total radius3 coverage. Stop the whole Exoo72 adjacent
two-vertex deletion plus crossperfectmatching family; no map scaling,
offset, port relabeling or SAT solve can repair a controller that already
has this topology obstruction.

Other source controllers, other boundary rewirings, same-side edges or
different deletion operations are not covered by this proof and were not
automatically dispatched. The target4480vertex22degree graph was never
generated. New full graphs:0; new Lean:0; solver calls:0; active handles:0.
