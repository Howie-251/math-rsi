# Full Q5 A10 and all-hole Q5 consequences: independent review

2026-11-01. ARIS proof-checker `/root/a10_final_rank_review`, user-selected
`gpt-6.1-sol / high`; **same-family / provisional**.

**PASS relative to the final accepted local imports.** Full Q5 A10 holds
for every arbitrary K(Q5) matching with hole counts 4:6, either majority
parity, and every specified majority hole v: a simple 31-cycle omitting
exactly v contains the matching and has only short edges outside it.
Together with the already accepted A8 and established A2/A4/A6/perfect-
matching imports, this establishes all feasible Q5 imbalance-two avoid-one
inputs and every balanced-hole Q5 endpoint/cycle assertion described below.
Full Q6/P6 and complete ten-hole covered targets remain **OPEN**.

## Final imports and deterministic evidence

The reviewed assembly is `Q5_A10_FULL_CLOSURE.md`. The exact inputs are
bound in the JSON sidecar, including these final PASS reports:

| Import | Exact scope used |
|---|---|
| Q5_A8_FULL_REVIEW | Arbitrary complete-graph matching, 3:5 holes, every majority omission |
| A10_FIRST_ORBIT_REVIEW | Full arbitrary-matching theorem for 30 marked geometries |
| A10_ORBIT2_REVIEW | Full arbitrary-matching theorem for 20 marked geometries; analytic cases plus complete 2366577-input positive-certificate remainder |
| A10_ORBIT3_UNIVERSAL_REVIEW | Full arbitrary-matching theorem for five marked geometries, from verified forests and universal matrix rank |
| Q5_HIGHER_HOLE_REDUCTION_REVIEW | Conditional A8+A10 reduction, established A2/A4/A6/C0 imports and finite neighborhood fact |

The last-orbit review was finalized PASS before the present assembly gate.
All 114 applicable recorded hash comparisons pass. Final reports, their
audited sources, final evidence, and the assembly are pinned. I imported
the earlier accepted large matching/cycle verifications without rerunning
their 2366577 records or other preceding large certificates. Historical
pending/open statements inside frozen earlier reports describe their old
scope; the present reports discharge the additional obligations separately.

New `Q5_A10_FULL_REVIEW_check.py` independently enumerates each odd four-set
W and then every five-set Z among its nonzero even nonneighbors. This
constructs exactly the normalized no-augmentation domain and gives 55
members. Adjacent coordinate swaps independently generate the three orbits
from the displayed representatives. Their sizes are 30,20,5; they are
pairwise disjoint and their union equals the newly enumerated domain.
This does not assume any original short-matching realizability restriction.
Adjacency from the omitted vertex 0 to a minority hole is allowed.

For the consequence step the new checker also independently enumerates all
4368 five-subsets of each parity. Their neighborhood-size histograms agree:
11:16, 13:1040, 14:1440, 15:1312, 16:560. Thus the minimum 11 and the
opposite-parity pigeonhole bound are verified again.

## Canonical statements and proof obligations

Write A(2t) for every arbitrary matching with (t−1,t+1) holes admitting a
short-added cycle on Q5−v for every marked majority hole v, in either parity.
The accepted feasible range is t=1,...,15. For balanced m:m holes, all
m=1,...,16 have a spanning path from every free root r to every target of
opposite cube parity, free or covered. Every m=0,...,16 has a spanning
cycle extension. At m=0 the endpoint assertion is vacuous; the cycle is
the explicitly imported arbitrary perfect-matching theorem C0.

| ID | Obligation and discharge | Result |
|---|---|---|
| F01 | Translate by the specified v. Translation preserves arbitrary required edges and short cube edges, sends v to0 and its parity class to even. | PASS |
| F02 | If a short edge joins a minority hole to a nonforbidden majority hole, adding it preserves a matching, leaves0 free and reduces 4:6 to3:5. Full A8 applies for this very omitted hole. | PASS |
| F03 | The augmentation edge is short relative to the original F, so the resulting cycle retains the exact required new-edge scope. | PASS |
| F04 | Otherwise Z,W are independent across parities, with sizes5,4; no other nonadjacency condition is required. This domain is exactly the independently enumerated55 geometries. | PASS |
| F05 | The three source representatives match the accepted final theorem scopes, with omitted vertex0 and arbitrary11-edge required matchings. | PASS |
| F06 | Coordinate images produce pairwise disjoint30+20+5 sets with exact full union. Transport any original F to its representative and invert the automorphism after applying that theorem. | PASS |
| F07 | Augmentation and no-augmentation are exhaustive, and inverses preserve simplicity, exact31-vertex support, all required edges and shortness of new edges. Thus the marked omission quantifier is universal. | PASS |
| F08 | For t>=6 choose five minority and six majority holes other than v. The neighborhood bound11 forces a short edge because11+6>16. Add it and decrease t; termination at5 invokes full A10. | PASS |
| F09 | All t<=5 bases are established A2/A4/A6/A8/A10. Each newly required augmentation edge is short and v remains free. Feasibility requires t+1<=16, hence t<=15. | PASS |
| F10 | For balanced Pm with free target y, add arbitrary ry, use C(m−1), delete ry. The matching scope permits long auxiliary edges and deletion leaves one spanning r–y path with only short surviving new edges. | PASS |
| F11 | For covered y let h=F(y). Replacing yh by hr leaves a matching on the same covered population with holes (m−1,m+1), majority parity y, independently of h's parity. Distinctness follows since r was free. | PASS |
| F12 | A(2m) avoiding y gives a31-cycle containing hr. Delete hr and attach h–y through the original edge hy; this yields one32-vertex r–y path. This is equivalent to the draft's temporary h–y–r replacement/deletion; no auxiliary long edge survives. | PASS |
| F13 | At m=16 F is empty, so a covered target cannot occur; only C15 is used. The impossible A32 is never invoked. | PASS |
| F14 | Obtain Cm from Pm by choosing any short neighbor of a free root and closing the resulting path. Its endpoint edge cannot already appear in a32-vertex simple Hamilton path, so closure is simple. | PASS |
| F15 | The induction C0→P1→C1→...→P16→C16 is acyclic; avoid-one statements have already been proved independently. No Q6 theorem is imported to establish these Q5 conclusions. | PASS |
| F16 | Final reports and reviewed inputs match all recorded hashes. The last-orbit rank import and finite witnesses are final PASS; no pending certificate or unproved spectrum exhaustiveness is used. | PASS |

The dependency DAG is A8 + three A10 orbit theorems + exact geometry cover
-> A10; finite neighbor fact + A2/A4/A6/A8/A10 -> all feasible A(2t);
then C0 and these A(2t) -> the sequential Pm,Cm induction. The earlier two
A10 orbit proofs do not require full A8/A10; the last one requires neither.
There is no reverse dependency or semantic circularity. No asymptotic,
probabilistic or limit-interchange assertion occurs.

## Counterexample pass and remaining scope

Adversarial candidates examined include a minority hole adjacent only to0,
an odd specified omitted vertex, a long or same-parity required edge,
wrongly marked orbit images, overlapping orbit families, choosing a bridge
through v, a mate h of either parity in the covered-target operation, an
m=16 covered target, an auxiliary edge remaining in the final path, and
closing a path with an edge already in it. Exact domain enumeration,
automorphism transport, final theorem quantifiers, and F01–F15 exclude
these failures. No counterexample or open proof obligation remains.

These accepted Q5 conclusions do not establish Q6 marked multiple-omission
inputs or make a uniform cut transfer automatic. Complete ten-hole covered
targets, complete 12/14/16/18-hole Q6 layers and full P6 remain OPEN. A
particular further Q6 application requires its own audit of cut hypotheses
and complete domain coverage. No producer file or main ledger was modified.
