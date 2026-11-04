# Independent review: the first A8 residual orbit

2026-11-01. Reviewer `/root/ten_hole_free_closure_audit`, user-selected
`gpt-6.1-sol / high` rather than the ARIS skill default. Semantic assurance
is **same-family / provisional**.

**PASS relative to the explicit GQ4-avoid and Q4 T44 imports.** The stated
delta-four branch works for every arbitrary K(Q5) matching and specified
majority forbidden hole under its exact hole geometry. It closes all60
marked configurations in the first residual orbit of the separately accepted
partial A8 package. Combining the two reports proves2600 of the2700 residual
after-augmentation geometries;100 in four orbits remain open. Neither this
report nor that arithmetic proves full A8 or any complete higher-hole P6
layer. The original partial package and its160-residual accounting are unchanged.

The audited `A8_DELTA4_FIRST_ORBIT.md` SHA256 is
`296d483e95fa6b5d07b5d35f9562fce0a798b1b0876898ea4bc5a5013d947a3f`.

## Exact theorem and imports

Let F be any matching on the32 Q5 vertices with three minority and five
majority holes, and let v be any specified majority hole. Suppose no minority
hole is short-adjacent to a majority hole other than v. Suppose a coordinate
face A containing v contains all five majority holes and exactly one minority
hole. Then a simple cycle on exactly Q5−v contains every edge of F and has
only short edges outside F. All required edges may be long or same-parity.

The nonadjacency hypothesis is the after-augmentation hypothesis. It does
not prohibit adjacency to v, and does not restrict F's required edges.
GQ4-avoid is read in `Q4_GENERAL_AUGMENTATION.md` and accepted in the final
A6 audit; it applies to all imbalance-two hole counts and arbitrary required
edges. Q4 T44 is the explicit four-same-parity-hole, any-two-prescribed-
omissions theorem in `Q4_TWO_AVOIDED_TRANSFER.md`, with its accepted whole
matching-quantifier review. The earlier exhaustive matching certificates are
imported rather than rerun. Thirteen relevant recorded hashes match current
sources/reports. No Q5 T15, Q4 T15, unrestricted A8, or double-bridge theorem
under investigation is imported.

The dependency DAG is Q4 N14/A4 and the already accepted local consequences
→ GQ4-avoid; separately certified Q4 T44 → B completion. These plus the new
two-bridge forest proof imply this geometric branch. The partial-A8 review
is used only to identify and combine the disjoint residual sets, not to
establish the new two-bridge transfer itself.

## Obligation ledger and adversarial review

| ID | Obligation and discharge |
|---|---|
| D01 | A has six original holes, so2|F_A|+c=10 and c is even,0≤c≤10. The four non-v majority holes have distinct B mirrors of minority parity. Since the only original B holes are minority and cannot be adjacent to these sources, every mirror is covered, either by F_B or a crossing. |
| D02 | If both mirror types occur, select one port and one internal mirror. A crossing exists and even c≥2, so p=1 and d=(c+2)/2≥2. If all internal, select a pair not joined by F_B; at most two of their six pairs can be matching edges. Then p=0,d≥1. If all ports, c≥4; choose any two, p=2,d≥3. These cover every classification, including exactly two candidate ports at c=2 by the mixed choice. Always p<d. |
| D03 | D pairs X_A plus the two source holes t,s. For each selected port mirror, prescribe the edge from its source to its actual original A crossing partner. Those partners are distinct covered A ports, never original holes; prescriptions are pairwise disjoint. The remaining even number of vertices can be paired arbitrarily. D is disjoint from F_A. |
| D04 | F_A+D has exactly one minority and three majority holes in A, including v. GQ4-avoid therefore gives an A−v cycle containing all of F_A and D, permitting all artificial long edges. This local input is valid also at c=0,D={ts}. |
| D05 | Removing D leaves d path components. Each selected port mirror restores exactly its prescribed removed gap through a fresh B vertex. Since only p<d gaps are restored, no circle forms. All other crossing attachments are at distinct endpoints. The resulting forest covers A−v and selected port mirrors internally, with endpoints all unselected B ports and the selected internal mirrors. |
| D06 | Its compressed matching R meets F_B only at selected internal mirrors. With one such mirror a cycle is impossible, since every other vertex has degree at most one. With two such mirrors the only possible closed component would use the edge wz in both matchings. The chosen pair is not an F_B edge, excluding that case. Equivalently, each selected internal mirror's F_B mate is distinct from the other mirror and from every crossing port; the two mates are distinct. Simultaneous suppression therefore yields a genuine matching, no loop or closed component. |
| D07 | Suppression of internal mirrors and consumption of port mirrors leave exactly the two original B holes plus w,z as holes of L. These are four distinct minority-parity vertices. T44 applies to every such arbitrary matching, omitting exactly w,z, without a constraint on compressed edge parity or length. |
| D08 | The B cycle has14 vertices. Expanding its compressed edges restores15 vertices of A−v plus exactly the two omitted bridge mirrors, each once. Those mirrors were either suppressed internal vertices or interior port vertices in the forest. Thus the final cycle has31 distinct vertices, exactly Q5−v. Every original edge of F_A,F_B,C survives; all auxiliary D edges disappear and every compressed edge expands. The new bridges and remaining local optional edges are short. No endpoint tag is required for a cycle conclusion. |
| D09 | For v=0,Z={3,5,6,15},W={8,25,26}, coordinate4 has all five majority holes in its zero face and exactly minority hole8 there. The mirrors of the four candidate sources are19,21,22,31, all covered. Coordinate permutations transport the complete arbitrary matching and forbidden vertex, so all60 marked configurations in its orbit satisfy the theorem. |
| D10 | Independently test the exact face condition on every one of the partial package's160 residual members. Its set is exactly the first60-element orbit. The other four residual orbits are disjoint and have sizes20,30,30,20. Combining with the accepted2540 delta1/2/3 configurations gives2600, leaves100, and does not alter the older package's stated scope. |

There are no asymptotic, analytic interchange or probability-mode claims.
No counterexample or unresolved hypothesis gap was found in any used step.

## Independent finite checks

New standalone `A8_DELTA4_FIRST_ORBIT_REVIEW_check.py` does not import or run
any producer or prior checker. It enumerates220 candidate-mirror classifications
over c=0,2,4,6,8,10, including every partial matching among the four internal
candidates. In every class the advertised selection exists and satisfies p<d.
Outside mates are allowed without a parity/length constraint; selecting an
internal pair not joined together is the only needed restriction.

The checker enumerates all nonempty matchings D of a labeled15-cycle with
d≤6, the complete allowed range from c≤10. All cyclic endpoint orders are
covered. For every possible distinct pair of source endpoints it attaches
original crossing edges to independently named B ports, attaches both mirrors,
and includes the required internal-mirror mate edges before suppressing the
path interiors. It checks exact endpoint sets, degree two at every interior,
and exactly two endpoints in every component. All43,530 both-internal,
37,980 mixed and37,620 both-port proper-gap tests pass. There are360 oriented
two-port/d=2 choices that would restore every gap; those are explicitly
excluded, as the four-candidate selection requires c≥4 for two selected ports.
The c=0 both-internal case is included and passes without a crossing.

For geometry, adjacent coordinate swaps independently expand the representative
to60 configurations. Testing the condition directly on all160 residual members
gives exactly that same set. The check JSON contains a concrete valid coordinate
for every one of the60 geometries, and fixed source and import hashes.

The adversarial pass targeted c=0 with paired internal mirrors, c=2 with two
selected port mirrors, both selected internal mirrors in the same compressed
component, a same-parity original long edge, actual crossing partner distinct
from mirror, all four candidates internal but paired in two F_B edges, and
source/forbidden-hole collisions. The selection rules, matching disjointness
and proper-gap invariant discharge these cases. In particular the potentially
dangerous c=0 pair must be chosen outside F_B, and the c=2 case must use the
mixed choice whenever there are only two candidate ports.

No production proof, old geometry data, prior audit or global state was edited.
Remaining100 geometries are open arbitrary-matching obligations, not negative
examples. Semantic acceptance remains same-family/provisional.
