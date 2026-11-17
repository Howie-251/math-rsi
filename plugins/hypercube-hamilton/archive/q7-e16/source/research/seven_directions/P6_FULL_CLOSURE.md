# P6: arbitrary short matchings with a prescribed free root

2026-11-02. ARIS proof-writer final-assembly submission. Acceptance requires
the independently checked dependencies below; this document alone does
not certify a pending layer.

## Exact theorem

For every matching M subset E(Q6), every vertex u not covered by M,
and every vertex v whose Hamming parity differs from u, there is a
Hamilton path from u to v that contains every edge of M.

Only M is required to consist of cube edges. The theorem does not assert
the analogous property for arbitrary complete-graph matchings on64 vertices.
Intermediate long edges in the local proofs are auxiliary requirements
whose use and removal have been checked in the imported constructions.

## Layer inputs

Every layer below has the same prescribed-endpoint quantifiers: arbitrary
original short matching of the indicated size, every free root, and every
opposite-parity target, whether free or covered.

| Uncovered vertices | Matching edges | Proof and acceptance gate |
|---:|---:|---|
|2|31|GENERAL_NEAR_PERFECT.md, N10; GENERAL_NEAR_PERFECT_REVIEW|
|4|30|FOUR_HOLE_FULL.md; FOUR_HOLE_SOL_HIGH_REVIEW|
|6|29|SIX_HOLE_CLOSED.md; SIX_HOLE_CLOSURE_CONSEQUENCES_REVIEW|
|8|28|EIGHT_HOLE_FULL_CLOSURE.md; EIGHT_HOLE_FULL_REVIEW|
|10|27|TEN_HOLE_FULL_CLOSURE.md; TEN_HOLE_FULL_REVIEW|
|12|26|TWELVE_HOLE_FULL_CLOSURE.md; TWELVE_HOLE_FULL_REVIEW|
|14|25|FOURTEEN_HOLE_FULL_CLOSURE.md; FOURTEEN_HOLE_FULL_REVIEW|
|16|24|SIXTEEN_EIGHTEEN_FULL_CLOSURE.md; SIXTEEN_EIGHTEEN_FULL_REVIEW|
|18|23|SIXTEEN_EIGHTEEN_FULL_CLOSURE.md; SIXTEEN_EIGHTEEN_FULL_REVIEW|

For the two-hole input, a short near-perfect matching leaves one hole of
each parity. N10's target-parity condition is therefore exactly the desired
opposite-to-root condition. The other rows have their full endpoint scopes
explicitly stated and independently checked. Historical reports saying
that later layers were then open are not assumptions of their own scoped
theorems. The final checker must distinguish those scope boundaries from
genuinely undischarged conditions.

## Root-preserving reduction to these layers

The accepted ROOTED_RANGE_REVIEW checks ROOTED_MAXIMAL_18_HOLES.md,
relative to the explicit Havel--Krivanek1982 Theorem2 input: every
inclusion-maximal matching in the full Q6 has at least24 edges.
This imported theorem is distinct from a maximum-cardinality matching
statement. Its complete original classification proof is a literature
input, not a new claim proved by the present computation.

Extend the given M by cube edges in Q6 minus{u} until an inclusion-maximal
matching L of that graph is reached. This is a finite process, preserves
M subset L, and keeps u free. If every neighbor of u is covered by L,
then L is maximal in the full Q6, so |L|>=24. Otherwise choose an uncovered
neighbor a of u. The matching L+ua is maximal in the full cube: an edge
still having both endpoints free would lie in Q6 minus{u} and could already
have been added to L. The imported theorem gives |L|+1>=24, hence |L|>=23.
The temporary edge ua is used only to prove this inequality; it is not
retained in the prescribed matching L.

Since u remains free, |L|<=31. Thus the number of uncovered vertices of L
is one of2,4,6,8,10,12,14,16,18. Apply the corresponding complete layer
theorem to L with the same u and v. This is legitimate even if v was free
in M but became covered while extending M, because every layer allows
covered targets. The resulting Hamilton u-v path contains L, and hence
contains M. This proves P6.

## Acceptance and reproducibility boundary

The final full-P6 reviewer must check that all nine layer scopes and the
rooted range input are formally accepted, all live proof/report/certificate
hash bindings agree, every earlier conditional premise used by a layer is
discharged, and the dependency graph is acyclic. In particular, the order
is full12=>full14=>full16=>full18, with no use of a later layer to justify
an earlier one. The local finite certificates are complete positive
families and exact actual-domain partitions; pilot samples or deficient
matrices are not sufficient proof premises.

The proof is relative to the explicitly identified literature theorems
and independently checked finite certificates. Its audit assurance is
same-family/provisional, and it has not been verified by Lean or another
proof assistant. No novelty, peer-review, publication or stronger
arbitrary-complete-graph Q6 claim is made here.
