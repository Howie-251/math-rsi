# Complete twelve-hole Q6 prescribed-endpoint theorem

2026-11-02. ARIS proof-writer assembly. Independent finite and final
assembly acceptance gates must pass before ledger closure.

## Exact theorem

Let M be any matching of26 cube edges in Q6. For every prescribed vertex
u uncovered by M and every prescribed opposite-parity vertex v, whether
free or covered, there is a Hamilton u--v path containing every M edge.
All added physical edges are cube edges. This is the complete twelve-hole
level of P6, not merely the two-free-endpoint case.

## Accepted predecessor and free-target branch

The complete ten-hole theorem is accepted in
`TEN_HOLE_FULL_REVIEW.json`, with both free and covered opposite targets.
The whole twelve-hole FREE-target branch is separately accepted in
`TWELVE_HOLE_FREE_REVIEW.json`. That proof covers adjacent-hole reduction,
normalization, all independent geometries and its final47 witnesses.
It therefore remains here to consider v covered by M.

Translate u to0 and permute coordinates so that v is1,7 or31. Let Z
be the five other even holes and W the six odd holes. If any z in Z
and w in W are adjacent, add zw to M. The resulting27-edge matching
still leaves u free and v covered; the full ten-hole theorem supplies
the required path, which also contains M. Otherwise Z union W is
independent. Root-to-W adjacency is deliberately retained.

## Exact covered-geometry reduction chain

The independently exhaustive initial census and cut theorem in
`HIGHER_Q5_FULL_REVIEW.json` leave7,820,116 covered-target records after
the near-balanced cuts. All subsequent records use original normalized
labels Z5 then W6, with the target marked. Every accepted positive
geometry is sufficient for EVERY realizing original matching, not a
sampled matching or favorable endpoint choice.

| independent acceptance gate | covered records remaining |
|---|---:|
|HIGHER_Q5_FULL_REVIEW.json|7,820,116|
|HIGHER_Q5_FULL_REUSE_REVIEW.json|348,236|
|HIGHER_Q5_FULL_T37_APPLICATION_REVIEW.json|215,243|
|TWELVE_NEW_TYPES_APPLICATION_REVIEW.json|37,405|
|TWELVE_NEW_FORCED_HALL_REVIEW.json|29,370|
|TWELVE_EXTRA_TYPES_REVIEW.json|1,281|
|TWELVE_EXTRA_FORCED_REVIEW.json|235|

Each gate verifies the actual sources, marked omissions, local input
scope and exact record-set complement. The Hall gate removes7,483
geometries using explicit covered-neighborhood deficiency certificates;
those geometries cannot be realized by an original short matching.
It also combines552 valid forced-input successes by an exact disjoint
union. No other matching-realizability exclusion is presumed.

The final235 records all have v=31 and W=N(0). Under coordinate
permutations fixing0 and31 they form six orbits of sizes30,60,60,10,15,60.
The exact six representatives, already independently checked, are the
Z sets listed in `TWELVE_STAR_MAXIMAL_A_REDUCTION.md`. Hence it remains
to prove the theorem for every realizing matching in those six cases.

## Last235: finite A witnesses and universal B gluing

Use the conditional reduction in `TWELVE_STAR_MAXIMAL_A_REDUCTION.md`,
with its separate mathematical acceptance gate
`TWELVE_STAR_MAXIMAL_A_REVIEW.json`. Split along bit32; A contains0 and31.
For each original matching the internal A matching L is a short matching
of the fixed26-vertex covered graph G, containing all five forced
internal vertices T=mirror(Z). Add short edges to reach an inclusion-
maximal L* on G. The reduction proves that a positive A witness for L*
lifts back to L by treating all added edges as completion edges. It
explicitly handles an actually crossing target that becomes internally
matched only during this auxiliary maximalization.

The finite positive premise is supplied by
`TWELVE_STAR_MAXIMAL_A_FINITE_PROOF.md` and must be independently
accepted in `TWELVE_STAR_MAXIMAL_A_FINITE_REVIEW.json`. Its exact six
complete maximal-matching domains have sizes

629747,598097,598067,598037,598067,598037,

total3,620,052. Every input has a witness consisting of an actual opening
choice q,t,w,b and a legal short forest P on A minus {0,31}. The forest
has the required degrees, contains q-t, and its labelled union with
the modified internal matching L*' is acyclic. Its balanced opposite-
parity endpoint set admits a completion matching joining all path
components into one cycle. This is an individual positive finite
certificate for each maximal matching. A rank8031 arbitrary-matching
opening theorem is neither asserted nor needed.

The finite gate must independently establish both parts: complete
domain coverage (legal maximal inputs, uniqueness and an independently
computed total) and every selected forest/compatibility witness.
Producer search completion or agreement with a producer count alone
does not discharge this gate.

In the actual gluing, q is an original even crossing port and t was
originally internally A-covered. Deleting q-t makes room for q's original
crossing and the new short t-to-mirror(t) bridge. The latter consumes
an original B hole, while three unit-source bridges create the three
marked B omissions. The resulting B input is an exact forced-T17 class.
Its two obstruction endpoints remain originally internally B-covered,
nonports and outside all suppressed conflicts, so their forbidden
same-parity pair cannot be present in the compressed matching.

The local B classifications are accepted via
`Q5_T17_RANK_BATCH_REVIEW.json`, `TWELVE_EXTRA_FORCED_REVIEW.json` and
`TWELVE_STAR_B_REVIEW.json`; each finite witness must identify its
actual marked B input under a common cube automorphism. No unrestricted
T17 conclusion is used. Expanding the resulting B cycle produces one
cycle on Q6 minus {u,v}, preserving the original matching with v-h
temporarily replaced by w-h. The reduction allows this auxiliary edge
to be a virtual crossing if h=63. Delete w-h and attach the short edges
u-w and h-v. The result is the required Hamilton u--v path, preserving
the actual original v-h and every other original M edge.

Every maximal A input is covered by the finite premise, every original
internal matching extends to one of them, and every resulting B matching
is covered uniformly by its exact local theorem. Thus all235 remaining
geometries are covered. Combining this with the accepted covered chain,
the predecessor reduction and the accepted free-target branch proves
the exact theorem.

## Acceptance boundary and remaining P6 work

This assembly may be marked accepted only after the conditional
reduction, complete finite premise and final independent assembly all
have finalized PASS reports with their frozen sources verified. At that
point the complete2/4/6/8/10/12-hole levels are closed relative to their
explicit imports and deterministic certificates. Complete14/16/18-hole
levels and full P6 remain OPEN; twelve-hole closure alone is not Q6.
Assurance remains same-family/provisional and not formal verification.
