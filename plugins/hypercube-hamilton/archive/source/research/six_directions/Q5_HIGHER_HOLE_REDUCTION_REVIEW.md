# Conditional Q5 higher-hole reduction: independent review

2026-11-01. ARIS proof-checker; reviewer `/root/higher_hole_transfer_audit`.
User-requested `gpt-6.1-sol / high` overrides the skill default. This is a
separate input review and does not replace the unified-transfer review.
Assurance: **same-family / provisional**.

**PASS: the conditional reduction is correct relative to A8, A10 and the
explicit established local imports.** The required finite neighborhood fact
and all supplied geometry data have been independently reconstructed.
A8 and A10 themselves remain **OPEN**. No complete higher-hole Q6 layer or
full P6 is established here.

## Reviewed input and fixed imports

The declared inputs are `Q5_HIGHER_HOLE_REDUCTION.md`,
`q5_higher_hole_reduction_geometry.py`, and its adjacent `.json`. Their
fixed SHA256 values are in the review JSON. The producer was read but was
neither imported nor executed by the independent checker.

The required established inputs are A2/N14, A4, A6, and Fink's arbitrary
perfect-matching full-cycle extension theorem C0. The explicit N14
statement in `TWO_ODD_HOLES_TRANSFER.md` and the underlying argument in
`GENERAL_NEAR_PERFECT.md` allow arbitrary matching edges and either
specified same-parity hole to be omitted. Full A4 is the exact claim in
`CANONICAL_A4_CLOSURE.md`; full A6 is the exact claim in
`A6_CLOSURE_DRAFT.md`, with accepted later reviews. These are not restricted
to short, bipartite or sampled matching inputs. The perfect-matching theorem
is a declared external import with short new edges, not newly reproved.

Four imported reports were checked for PASS, with sixteen comparisons of
relevant current source hashes against their accepted recorded hashes.
All agree. No large preceding certificate was rerun.

## Canonical claims and dependency graph

Assume the full A8 and A10 statements for every arbitrary K(Q5) matching,
every indicated marked majority hole, and either majority parity. Then
for every feasible t=1,...,15, A(2t) holds. In addition, for every m=1,...,16,
every matching with exactly m holes of each parity has the asserted
Hamilton path from each free root to each opposite-parity target, free or
covered, and a Hamilton cycle extension with short new edges. Balanced
m=0 has the imported cycle theorem; its free-root endpoint assertion is
vacuous.

Dependency DAG: finite neighborhood fact + A2/A4/A6/A8/A10 -> all feasible
avoid-one statements; C0 -> P1 -> C1 -> P2 -> ... -> P16 -> C16, with
each Pm also using the already obtained A(2m) only when feasible. No edge
of this dependency graph uses the desired higher balanced assertion to
establish its own avoid-one input. No Q6 higher layer is used.

## Obligation ledger

| ID | Obligation and verification | Result |
|---|---|---|
| H01 | Feasible imbalance-two holes have counts (t-1,t+1), so 1<=t<=15 in Q5; at t=15 two covered vertices remain and arbitrary same-parity matching edges are allowed. | PASS |
| H02 | Independently enumerate all4368 five-subsets in each parity. The least neighborhood size is11 in both. | PASS |
| H03 | For any six vertices of the opposite parity, 11+6>16 forces intersection with that neighborhood. Thus every chosen five minority holes and six nonforbidden majority holes contain a short edge. | PASS |
| H04 | For every t>=6, minority holes number at least5 and majority holes other than v number at least6. The chosen edge covers neither v nor an already covered vertex. Adding it preserves a matching and reduces t by1. | PASS |
| H05 | Repeating ends at t=5; existing t<=5 instances use A2/A4/A6 or the explicit new assumptions A8/A10. The resulting cycle contains all original edges, omits exactly v, and its added requirement edges were all short. | PASS |
| H06 | Balanced Pm free-target case: r,y are distinct free vertices of opposite parity. Adding ry gives an arbitrary matching with (m-1,m-1) holes; C(m-1) applies. Deleting its required ry yields one Hamilton r--y path. | PASS |
| H07 | Covered-target case: r,y,h=F(y) are distinct. Replacing yh by hr leaves a matching, removes r from the holes and adds y, leaving (m-1,m+1) holes oriented toward y. Mate parity is unrestricted and does not affect these counts. | PASS |
| H08 | For m<=15 the exact A(2m) instance is feasible. Its cycle avoids y and contains hr. Replacing hr by h-y-r restores yh; deleting yr yields the required Hamilton path, with no auxiliary edge remaining. | PASS |
| H09 | At m=16 F is empty and every target is free. Only C15 is invoked; the impossible A32 input is never called. No r,y,h coincidence arises in a covered branch. | PASS |
| H10 | For m>=1 a free root exists, and any of its five short neighbors is an allowed opposite-parity target in Pm. A 32-vertex Hamilton path cannot already contain the edge joining its two endpoints; closing it produces a simple cycle with a short added edge. | PASS |
| H11 | The induction uses only C(m-1) to get Pm, then Pm to get Cm, so it terminates at m=16 without circularity. C0 handles perfect matchings separately. | PASS |
| H12 | Normalizing the forbidden vertex to0 by translation makes majority holes even, with exactly t other nonzero even holes and t-1 odd holes. The forbidden vertex may have adjacent minority holes; the census excludes adjacency only between Z and W. | PASS |
| H13 | Independent complete geometry counts are2700 for A8 and55 for A10. For t=6,...,15 there are no such nonadjacent geometries. These are marked holes, not matching-extension evidence. | PASS |
| H14 | Full producer delta histograms and residual coordinate-permutation orbits reconstruct exactly:160 A8 residual configurations in5 orbits and55 A10 configurations in3 orbits. This verifies only geometry statistics, not the delta-based transfer theorem. | PASS |
| H15 | Every original/new-edge distinction is respected: added hole-pair requirements are short, ry is deleted, hr is deleted, yh restored, and the closing root-neighbor edge is short. All conclusions retain arbitrary original required edges. | PASS |
| H16 | The draft keeps A8/A10 conditional and avoids any claim that all Q6 cuts reduce to them. Its conclusions match precisely the conditional claims above. | PASS |

There are no asymptotic, probabilistic, analytic-interchange or limiting
uniformity claims to check.

## Independent finite verification and counterexample attempts

The standalone `Q5_HIGHER_HOLE_REDUCTION_REVIEW_check.py` computes adjacency
by testing all vertex pairs for Hamming distance1. It does not reuse the
producer's bit-mask unions or import its functions. Both parity classes
are independently enumerated, for8736 five-subsets in total. Each gives:

| Neighborhood size |11|13|14|15|16|
|---|---:|---:|---:|---:|---:|
| Five-subsets per parity |16|1040|1440|1312|560|

For geometry enumeration the checker reverses the producer's loop order:
choose Z first, construct its opposite-parity nonneighbors, then choose W.
Every nonzero even t-subset appears once and every allowed W is enumerated
once. This gives complete marked domains rather than selected examples.
For t=4,5 the counts are2700,55. Their residual counts are160,55.
For t=6 through15 all counts are zero. The latter also follows analytically
from H03--H04, independently of computation.

Orbit verification uses a breadth-first traversal under adjacent coordinate
transpositions, which generate the whole stabilizer of0. It does not use
the producer's minimization over precomputed120 coordinate maps. The five
A8 residual orbit sizes are60,20,30,30,20; A10 sizes are30,20,5.
The reported representatives generate disjoint orbits whose union is the
independently enumerated residual. All full delta histograms also agree.
The delta statistic is checked solely as a numerical definition on holes.

The checker tests58 feasible covered-target parity populations over all
m and both root parities, including both mate parities where possible.
Counterexample candidates examined are a maximum-size minority set with
no edge avoiding v; a long or same-parity hr; h=r; temporary edge duplication;
an m=16 covered target; and a Hamilton path already containing its closing
endpoint edge. They are respectively excluded by the exact11+6 bound,
the arbitrary-matching input scope, the free-root condition, omission of y,
the empty-matching condition, and the length of the Hamilton path. No
counterexample was found. The graph operations in H06--H10 provide the
universal proof; finite parity tests do not substitute for that proof.

## Decision and scope limits

All16 proof obligations pass. No issue or proof repair is required.
The finite neighbor fact and reported geometry data are deterministically
verified. Semantic acceptance of the conditional proof remains provisional.

A8 and A10 still require proofs for **every** arbitrary complete-graph
matching on their covered vertex sets and every specified majority hole.
This review neither proves those statements nor accepts the separate delta
transfers under investigation. Complete higher-hole Q6 layers and full P6
remain open. The earlier unified-transfer audit, production proofs and main
claim ledger were not modified.
