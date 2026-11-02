# Semilinear F64: two inverse pairs and two involutions, bounded profile

This file preserves the original bounded-profile decision. The separately
authorized continuation has since completed; [REPORT.md](REPORT.md)
records its full-range results. The original prefix was not repeated.

The authorized **2,000-HH-pass prefix is complete and stopped**. It
visited 2,000 raw inputs, all legal and HH-passing, with **zero BB
passes** and minimum BB missing count **6**. No candidate in the profile
reached the three-root BFS stage, and no D5 graph was found. The complete
41,490,060-input range has **not** been started.

The saved next cursor is **2,000**. Its parameters are type I, first
involution index 0, second-involution orbit index 0, and inverse-pair
indices `(1,703)`. All visited inputs belong to the first type-I branch,
whose two involutions are `(1,0,0)` and `(2,0,0)`. This prefix is not a
representative sample of all 46 normalized branches; zero BB passes here
does not exclude the full family.

## Exact range and machine-list comparison

The group, field, subgroups, labels and graph construction are unchanged
from the checked faithful semilinear tower. The source `engine.hpp`
retains its actual multiplication, inverse, exact BB masks and ordinary
three-root BFS. Generator legality now requires six distinct nonidentity
inverse-closed elements with **exactly two involutions**; the remaining
four elements form two different noninvolutory inverse pairs.

The independent [SCOPE.md](SCOPE.md) gives two complete cases:

| Type | Normalization | Legal inputs | HH passes |
|---|---|---:|---:|
| I | An A21 involution exists; first is `(1,0,0)` or `(1,0,1)`; second has 20 Frobenius2 orbit representatives | 33,774,000 | 31,274,334 |
| II | Both involutions come from the 45 non-A21 involutions; first A21 inverse pair uses the existing six representatives | 7,716,060 | 7,708,176 |
| Total | Both cases | **41,490,060** | **38,982,510** |

Type I enumerates all unordered distinct pairs from the 1,300 true
inverse pairs for each of its 40 first/second-involution choices.
Type II enumerates all C(45,2)=990 involution choices and all 1,299
remaining inverse pairs for each of six first-pair representatives.
No actual inverse pair or involution is repeated within a generator set.

The Frobenius map is `(x,a,e)->(x^2,2a mod21,e)`. Both normalized first
involutions are fixed by it, permitting the second-involution orbit
reduction while the other two inverse pairs range over their complete
list. The original subgroup-preserving rotation conjugation changes a
when e=1; arbitrary scaling of x with fixed a was not used.

Before profiling, the independently generated C++ lists were compared
with the math agent's `normalization_inputs.json`: **all 87 involutions,
both complete lists of 20 second-involution orbit representatives and
every orbit member, and all 45 type-II involutions match exactly**.
The expected input counts also match. `generated_scope.json` preserves
the actual C++ lists, and `prepare.terminal.json` records the comparison.
General valid `(x,0,1)` noninvolutions remain in the actual inverse-pair
table; the old incorrect global a!=0 restriction was not introduced.

The enumeration order is type I first: first-involution index, second
orbit index, then full pair-table indices j<k. Type II then uses first
pair branch, involution-list indices j<k, and the other pair's index in
the 1,299-list with the fixed pair removed. `profile_metadata.json` records
this order and the complete candidate-preservation parameters.

## One actual involution-containing calibration graph

Exactly one new preflight graph was used. Its two involutions are
`(1,0,1)` and `(2,0,0)` and its two inverse-pair representatives are
`(3,3,1)` and `(0,1,0)`.

The source agent independently verified the two involutions, reconstructed
all **11,200 edges** with the actual semilinear multiplication and compared
the complete edge set. It matches the saved `preflight.edges` exactly.
One generic all-source check confirmed a simple connected 7-regular graph
on 3,200 vertices, with **diameter 6** and **368,928 bad unordered pairs**.
Its root misses are **225,255,294**. All 448 individual BB targets and
the seven stored masks agree with independent BFS; BB missing is 33.

The evidence is in `preflight.independent_check.json` and
`preflight.independent_verify.json`. Neither of the old three-pair
preflight graphs was rerun.

## Prefix result and saved representative

The filter sequence is unchanged: actual K-orbit HH coverage, then the
exact `H W3 H union K W1 H union H W1 K` BB condition, then actual
three-root BFS only on BB passes. Both source-head and target-head terms
are retained. The full BFS weighting remains 2,688/448/64; a true zero
score would save the complete graph and stop immediately.

The first prefix input with six missing blocks has cursor **812** and
inverse-pair table indices `(0,813)`. Its six actual generators are

`[(1,0,0),(2,0,0),(0,1,0),(0,20,0),(17,3,1),(62,18,1)]`.

Its seven BB masks are in `profile.best_BB.json`. Only its BB coverage
was scored: no full bad-pair count or diameter is claimed for that
representative. The BB histogram, all 46 branch counters, and exact
next-input parameters are in `profile.terminal.json` and `terminal.json`.

## Measured cost and production decision

Preparation and compilation used **1.944672 CPU seconds**. The independent
new-graph calibration used **0.342636 CPU seconds**, and the independent
normalization-list generation used about 0.0167 seconds. With the bounded
profile, the cumulative charged time is **2.329450 CPU seconds**, within
the authorized 60-second budget, with one search worker.

The profile engine reports 0.017512 seconds setup and only 0.000295
seconds in its 2,000-input loop. Its direct 5.77-second full-frontend
extrapolation is **not reliable at this short timing scale**. No downstream
BB-survivor BFS cost was observed.

For a more useful cost reference, the already completed three-pair run
uses the same group arithmetic and BB/BFS implementation. Scaling its
actual raw-input and BB-stage costs to this new declared range gives
**about 86 CPU seconds for HH plus BB**, with additional actual BFS cost
depending on the unknown number of new BB survivors. The previous run's
three-root BFS cost was about **0.000094 CPU seconds per survivor**.
This is an empirical planning estimate, not a new execution or a runtime
guarantee. `cost_estimate.json` preserves the exact source counters and
calculation.

No complete production run or additional parameter was started. The
profile, cursor and candidate scope are saved for the parent's explicit
production-budget decision.
