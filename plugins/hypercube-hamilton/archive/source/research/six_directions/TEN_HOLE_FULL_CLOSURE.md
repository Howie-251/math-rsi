# Full ten-hole Q6 endpoint extension: assembly candidate

2026-11-01. ARIS proof-writer. Final assembly acceptance pending.

## Original theorem

Let $M\subseteq E(Q_6)$ be any 27-edge matching. For every uncovered
vertex $u$ and every vertex $v$ of opposite parity, covered or free,
there is a Hamilton $u$--$v$ path containing every edge of $M$.
No constraint on the prescribed target is added.

## Status and explicit outstanding imports

The free-target branch, the independent-hole reduction and the earlier
covered-target coverage chain are already accepted. The final covered
assembly below additionally requires independent acceptance of the new
actual T15 rank batch and of the T17 unrestricted/forced-obstruction
rank inputs with a proved root-not-obstruction transfer. Those candidate
imports must not be treated as accepted merely because their producer
matrices have full rank. The main ten-hole flag stays false until a
separate final assembly review accepts all these dependencies and the
exact final union.

## 1. Free targets and normalization of covered targets

When $v$ is free, apply `TEN_HOLE_FREE_CLOSURE.md`, accepted by
`TEN_HOLE_FREE_REVIEW.json`. This covers every realizing short matching
and every free opposite-parity endpoint pair.

For the remaining case $v$ is covered. Translate by $u$ to put the
free root at zero; the target then has odd weight. Permuting coordinates
puts it at $v\in\{1,7,31\}$. Write the other even holes as $Z$, $|Z|=4$,
and the odd holes as $W$, $|W|=5$. If some short edge joins $Z$ to $W$,
add that edge to $M$. The root remains free. The accepted full eight-hole
endpoint theorem supplies a Hamilton path to the same covered target
containing this enlarged matching, hence containing $M$.

It therefore suffices to handle $Z\cup W$ independent, with the target
outside the holes. These are marked hole geometries; each positive
geometry statement must cover every short matching realizing it.

## 2. Accepted complete reduction to 4096 marked geometries

The independent domain and exact filtering accepted in the following
reviews reduce the full normalized covered-target universe to the
listed frozen residual. No probabilistic matching sample is used.

| accepted review | exact remaining covered-target geometries |
|---|---:|
| `TEN_HOLE_COVERED_PARTIAL_REVIEW.json` | 91225 |
| `Q5_A8_CONSEQUENCES_REVIEW.json` | 54222 |
| `TEN_COVERED_T63_SPLIT_REVIEW.json` | 41306 |
| `TEN_COVERED_Q5_ENDPOINT_REVIEW.json` | 41236 |
| `Q5_T26_RANK_BATCH_REVIEW.json` | 4096 |

The first review accounts for the complete 145248180 normalized
covered-target geometries before its reductions. Each subsequent review
uses the exact frozen residual of its predecessor and validates actual
cut/bridge witnesses and exact remaining sets. The final three files are
`Q5_T26_RANK_BATCH_REVIEW_remaining_v1.bin`, `_v7.bin`, `_v31.bin`, with
910, 1476 and 1710 nine-byte records. Their order and hashes are bound
by the final T26 review.

Every route handles an original empty crossing set by the explicit
five-direction endpoint import. Positive-crossing transfers use complete
local statements for arbitrary compressed matchings, preserve every
original required edge, and restore precisely the marked suppressed
vertices. These quantifiers were checked in the respective reviews.

## 3. Final finite union required for acceptance

On these exact 4096 records the new candidate routing is:

- 2598 records have an actual T17 projection with an unrestricted
  positive 2048-rank certificate among ten marked orbits.
- 1036 further records have only forced-obstruction T17 projections,
  but each has an actual projection whose two obstruction vertices
  exclude the global root. The seven local 1024-rank certificates
  cover precisely the local matchings avoiding that obstruction edge.
  `Q5_T17_RANK_ROOT_NOT_OB_TRANSFER.md` supplies the required completion
  choice: if both obstruction vertices are crossing ports, prescribe
  the edge between their A partners in the deleted completion matching.
  A tagged A cycle has at least two deleted gaps, or the tagged A path
  only acquires a B-root leaf, so those ports cannot be paired by one
  transferred component. The parity of the bridge mates excludes every
  other way to create the obstruction. The target-port and root-side
  cases are included in that lemma and require independent acceptance.
  The original internal matching's absence of that edge alone does not
  suffice.
- The 462 records with no T17 projection are covered by the new T15
  rank batch. Its larger positive set has 2346 records, which may
  overlap the preceding T17 routes.

An independent final checker must establish this union by exact sets,
not by adding the overlapping totals. The expected per-target partition
is $(570,220,120)$ at target 1, $(918,396,162)$ at target 7, and
$(1110,420,180)$ at target 31. Each row sums to its accepted input count.
Every actual projection must preserve the marked omissions under one
common cube automorphism, and every application of the forced local
input must discharge the obstruction-avoidance hypothesis.

These final route counts are recorded here as required verification
obligations until the independent route and union reviews pass. They
do not independently assert that any missing lemma has been proved.

## 4. Conclusion after the final verification gate

Once all final local inputs, the root-not-obstruction transfer and the
exact union in Section 3 are independently accepted, every normalized
covered-target geometry is positive by Sections 1--3. Invert the
normalization to recover every original $M,u,v$. Combining with the
already accepted free-target branch proves the original full ten-hole
theorem, with no narrowed matching or target quantifier.

Even after that gate, this theorem is one Q6 hole level. The complete
12/14/16/18-hole obligations and full P6 remain open. No full-P6 flag
may be inferred from this assembly alone.
