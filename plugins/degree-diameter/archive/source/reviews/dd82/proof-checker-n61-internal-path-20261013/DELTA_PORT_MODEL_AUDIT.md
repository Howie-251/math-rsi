# Reused delta: shared-parent ports and complete original-graph model

Date: 2026-10-13. Reviewer: `/root/internal_path_proof_check`.
**Final verdict: PASS for both declared mathematical inputs, modulo
the explicit inherited reductions.** This is an explicitly reused,
same-family, provisional mathematical
review. It does not extend the original fresh two-manuscript receipt
or convert any later delta into fresh or external acceptance.

## Shared-two-parent proof: reviewed input and obligations

Read directly in full after author stability:
`proofs/dd82/n61/INTERNAL_DOUBLE_SHARED_TWO_PORTS.md`, lines 1–161.
Its local type is exactly `(epsilon,beta,r,h)=(0,1,2,0)`.
The actual-A local template and defect baseline are inherited from the
original audit; the separate endpoint-exclusion delta is not silently
relabelled as a new proof here. The present port argument does not need
to repeat those exclusions because it states its local type explicitly.

Frozen obligations for this proof:

| ID | Obligation | Disposition |
|---|---|---|
| S01 | Five-element ordinary blocks, exact P/Q parents, unique unit endpoint ports in Z | Discharged by the local class sizes, transversals, h=0 and remaining row budget |
| S02 | Endpoint common-neighbor equations (3), P/Q independence and simultaneous opposite-set/ordinary port alternatives | Discharged by actual neighborhood partitions and parity of the internal degree sum |
| S03 | Shared-parent saturated rows forbid all P/Q edges into Z_a,Z_b and exclude ports there | Discharged by the local color-degree identity and equation (3) |
| S04 | Equations (7)–(10), including both c-row counts and symmetric d-row count | Discharged by counting the same actual interfaces from both sides and spending c's remaining two defect units |
| S05 | Exactly three port configurations and the claimed P/Q matchings | Discharged by S02, S04 and all individual cross-degrees in (3) |
| S06 | Exact B[P],B[Q] zero/single-unit-edge alternatives | Discharged by the actual `(u,p)` commutation identity, row sums and support on the actual neighbors of x/y |
| S07 | All residual identities (13), including their uniqueness conclusion | Discharged by actual commutation at ordinary points and attachment points, retaining the extra endpoint-adjacency term |

The dependency chain is `local template -> S01 -> S02 -> S03 ->
S04 -> S05 -> S06`; S07 uses S01, S03 and the same commutation identities.
There is no circularity, new asymptotic condition or probabilistic claim.

## Counterexample-first checks of the port proof

- A port in its own attachment set would make the sum of internal
  degrees equal one. The parity argument removes this possibility
  before P/Q independence is used; neither independence is assumed.
- Opposite-set ports and ordinary ports cannot be mixed: the two
  evaluations of `e_A(P,Q)` have indicators with identical base four.
- A neutral ordinary port and coincident ports are not discarded by
  naming. The c/d equations require one port in each of two disjoint
  ordinary classes unless the opposite-set alternative applies.
- The one common-parent or one common-attachment cases from the
  previous notes do not enter this proof. Here U and W overlap in
  exactly a,b, while P and Q are disjoint by the expressly stated type.
- A putative double entry in B[P] would violate equation (11), whose
  right side is binary. A single-edge conclusion does not follow
  merely from total weight; the proof also checks the row bound and
  confines its two endpoints to the actual two neighbors of x.
- The A[P,Q] matching is not forced to preserve neutral parent labels.
  The port proof states this freedom explicitly.
- For ordinary z=x or z=y, the residual equation's diagonal adjacency
  is zero. No distinct-pair common-neighbor identity is misapplied
  there: equation (13) is a matrix commutation identity.

## Exact mathematical checks of the port proof

Every shared-parent class has size five and no attachments. The c/d
classes have size six with exactly one attachment each; each neutral
class has size seven with one P and one Q attachment. Therefore every
ordinary block has size five. Each endpoint spends three defect units
on v and the other endpoint, and has zero defect to T. Its remaining
unit is necessarily at a unique point of Z, proving equation (2).

For `z in Z_t`, counting common neighbors against `N(u)=U union P`
gives `1[t in U]+d_P(z)=1+1[z=x]-1[z in P]`, and likewise for w.
On P, summing this equation gives `sum_P d_P=1[x in P]`, so parity
forces x outside P and every P internal degree zero. The Q proof is
identical. On the opposite attachment sets, exactly the exceptional
q0 or p0 parent lies in U or W, yielding the constant four in both
cross-edge counts. Thus ports are either both in the opposite sets
or both ordinary.

The a/b defect rows are saturated within T. For any attachment, the
local color-degree formula at a or b reduces to its number of A
neighbors in the corresponding shared-parent class; that number is
zero. Applying equation (3) to an ordinary vertex in either class
then excludes both ports there.

For c and P, `B_cp=d_Zc(p)`. Counting the interface from
`Z_c={q0} union O_c` gives `1[x=q0]+1[x in O_c]` exactly. For c and
Q, `d_Zc(q)=1+B_cq-1[q=q0]` sums to `4+sum_Q B_cq`. From Z_c, q0
has no Q neighbor by independence, and the five ordinary points
contribute `5+1[y in O_c]`. Hence the remaining Q defect sum is
`1+1[y in O_c]`. The full c row already has unit entries at a,b
and zero entries at u,v,w and ordinary vertices, so its two remaining
units give equation (9). Exchanging the entire stated endpoint roles
gives equation (10), with no additional assumption.

In the opposite-set branch these equations force x=q0,y=p0. In the
ordinary branch they force exactly one port in O_c and one in O_d;
they cannot coincide. Equation (3) gives cross-degree one at every
attachment in the first case, and in the other cases gives degree
zero at p0,q0 and one at each neutral-parent attachment. This proves
the three matching descriptions with all permitted matchings free.

For p in P, `(AB)_{u,p}` has only `B_cp+sum_P B_p'p` remaining from
the U and P terms. `(BA)_{u,p}=A_xp`, since p is adjacent to neither
v nor w. Therefore every B[P] row has sum at most one, and a positive
row is supported at a P vertex adjacent to x. Summing the equation
gives total ordered B[P] weight `d_P(x)-1[x in Z_c]`. Equation (3)
at x, using the already proved exclusions of P,Z_a,Z_b, gives
`d_P(x)=2-1[x in Z_c]`. Thus the ordered total is zero or two.
In the latter case x has exactly two P neighbors; the one unit edge
must join them. The endpoint exchange gives the Q conclusion. These
are exactly the three table rows.

At an ordinary z, all U defect terms and its original adjacencies
to v,w vanish, leaving `sum_P B_pz=A_xz`. At q in Q, the additional
original adjacency to w contributes one and the only remaining U
defect term is B_cq, giving `sum_P B_pq=1+A_xq-B_cq`. The analogous
p equation retains B_dp. Nonnegative integer entries summing to a
binary value yield the stated unique unit defect neighbor on ordinary
vertices. All equations concern the same actual A and B.

The shared-parent proof has seven of seven obligations discharged,
with no issue. It remains a necessary representation of an unresolved
branch, not a realizability certificate or an exclusion.

## Complete model specification

Read `proofs/dd82/n61/INTERNAL_DOUBLE_FULL_GRAPH_DESIGN.md` completely,
initially 286 lines. The author then confirmed the sole final change:
section5 explicitly separates exceptional-only T–Z counters from
endpoint counters on all 50 Z vertices. The corrected section was read
directly; the stable reviewed document has 289 lines. No source code,
emitted constraint file, solver execution or external call was reviewed.

The three-case reduction is inherited from the earlier three-exclusion
delta, with its actual reused provisional status. The port theorem above
is a separately checked refinement of the third case. The complete model
need not encode every proven port consequence to retain full coverage;
the two reviewed inputs are not conflated into one exclusion theorem.

Frozen model obligations:

| ID | Obligation | Disposition |
|---|---|---|
| M01 | Exactly three necessary local types cover every actual internal-double target | Discharged modulo the specifically inherited three-exclusion reductions |
| M02 | Canonical U,W and class sizes preserve every ordered endpoint pair | Discharged by independent relabeling of intersection, one-sided and neutral parent categories |
| M03 | Fixed P/Q labels and the shared neutral class preserve every prescribed overlap | Discharged by remaining neutral-parent permutations and independent permutations inside each class |
| M04 | Same-class ordinary zeros and shared-parent saturation zeros are necessary | Discharged by the local ordinary rule and actual B[T] row saturation |
| M05 | Exactly seven five-point reference matchings can be fixed when r>0 | Discharged by actual degree-one interfaces and independent unused ordinary-block permutations; no such normalization is applied when r=0 |
| M06 | Shared-attachment extra zeros and beta-one P/Q independence are necessary | Discharged by actual defect saturation and triangle contributions to actual endpoint rows |
| M07 | Free-pair and edge totals are algebraically consistent | Discharged: 1086/870/800 free A bits, 74 core-touching edges and 170 total Z edges |
| M08 | Every original vertex has degree eight and the fixed core has the stated actual defect identities | Discharged by exact class/attachment degrees and direct fixed-neighborhood counts |
| M09 | All1830 original pairs have genuine direct-edge/two-edge coverage | Discharged at specification level by actual third vertices and full AND equivalence with faithful constants |
| M10 | Short defect counters and all row/column budgets equal actual-A quantities | Discharged, with endpoint counters explicitly covering all50 Z points |
| M11 | Shared-attachment exact coverage constraints are necessary | Discharged by its actual row saturation, with at most49 other Z vertices |
| M12 | Omitting generic all-Z-pair defect-upper counters preserves coverage and sound original-graph decoding | Discharged because all genuine target constraints are retained and all vertices/pairs still satisfy exact degree and diameter-two semantics |

All twelve model obligations are discharged. Dependencies run from the
inherited local reductions through labeling and exact counting to the
coverage implication. M12 does not use a solver outcome, and the claimed
three-input decision remains hypothetical until actual checked results.

## Model counterexample probes and exact coverage check

**All three types and compatible labels.** The parent-category sizes
allow the specified U,W labels for any actual ordered pair. A P point
and a Q point can coincide only over a neutral parent. With h=1, the
neutral parent carrying that point can be named first using an untouched
neutral-category permutation; with h=0 no coincidence is imposed.
Inside each class, the one or two distinguished attachments can be
labeled before its ordinary vertices. These choices do not fix any
unrelated matching or invoke a graph automorphism.

The potentially troublesome `r=0,h=1` case is retained separately:
its shared-attachment class has six ordinary points and receives no
five-point reference normalization. For r>0, every ordinary block has
five points. A shared parent has all four defect units in T. At any
exceptional z, the actual color-degree formula reduces to
`0=B_cz=d_Zc(z)`, since `e_z=1` and its parent is not c. Thus no
attachment can meet the shared reference class. The ordinary color
rule consequently gives degree one on both sides between that class
and every other ordinary block. Each is a genuine perfect matching.
After arbitrarily labeling the reference five points, the still-unused
permutation of each other ordinary block makes its one matching the
identity. Exceptional labels stay fixed. Only the seven reference
interfaces are normalized; a second set of matching identities is
not assumed. All other ordinary-block interfaces remain variable.

**Additional zeros and counts.** For h=1, the shared attachment s
has `sum_T B_ts=4`, so its entire row is supported on T. In particular
its original edge to u has zero defect; any edge from s to another
P point would supply a triangle and positive defect on that edge.
The Q argument is the same. There are exactly eight other distinct
attachments, all outside s's parent class, so the eight new zero
pairs are distinct from the already fixed same-class pairs. For
beta=1, two adjacent P points would require two positive additional
endpoint-row entries beyond weights two at v and one at w. Only
one unit remains, so P is independent; likewise Q. Their h=0 sets
are disjoint and contribute twenty distinct zero pairs.

The sum of within-class pair counts is
`10r+15(6-2r)+21(2+r)=132+r`. Exactly `2+r-h` same-class pairs
can remain, namely the two distinct attachments in nonshared neutral
classes. Thus ordinary same-class zeros leave `1095-h` candidate
Z pairs. For r>0 the ten attachments avoid each shared size-five
class, adding `50r` zeros. The reference blocks fix `7*25=175`
different ordinary-to-ordinary pairs; the beta-one independence adds
twenty attachment-to-attachment zeros. The supports of these sets
are disjoint. These calculations yield precisely 1086,870,800.
The reference blocks contain 35 fixed edges. The eleven-point core
touches `8+6+50+10=74` edges, counting a shared attachment's two
distinct endpoint edges separately. The Z-degree sum is `350-10=340`,
so there are 170 Z edges and 244 total edges. The remaining free-edge
counts 170,135,135 are consistent.

**Original graph semantics.** All adjacencies touching the core are
fixed consistently. An ordinary point has its parent plus exactly
one neighbor in each other class, totaling eight. An exceptional
point has one parent, e_z endpoint neighbors and `7-e_z` Z neighbors,
also totaling eight. Each core vertex's degree follows from its exact
class/attachment sizes; normalized reference vertices have one parent
plus seven matching neighbors. Optional duplicate degree counters are
therefore unnecessary for the mathematical implication.

All1830 unordered original pairs retain direct-edge or actual common-
neighbor coverage. A two-free-edge witness uses an equivalent AND,
not a one-direction witness variable; fixed-one and fixed-zero cases
retain their literal or constant truth values. Thus every satisfying
model decodes to a simple 8-regular original61 graph of diameter at
most two, regardless of whether generic defect-upper counters are
present. Conversely every actual graph of an inherited allowed type
can be relabeled as proved and can assign every auxiliary its exact
original-A value, satisfying every stated necessary constraint.

The fixed core gives `mu(v,u)=mu(v,w)=3`; each other nonneighbor of
v has one T parent, and T is independent. Hence the actual middle
defect row is exactly the two specified double entries. Its core
constants also give `B_uw=r+h-1=beta`, the exact B[T], and
`B[T,u]=B[T,w]=0`: the latter follows from the one attachment in
every class outside U or W. These facts do not require guessing B.

The T–Z color count and u/w–Z attachment counts in model equation(3)
are the actual common-neighbor identities, including the adjacency
indicator and unique-parent term. At ordinary points only B[T,z]
is forced zero; endpoint defect may be nonzero, as the reviewed port
theorem explicitly demonstrates. The final wording therefore correctly
requires endpoint counts and budgets on all50 Z points. The budgets
use the remaining actual row weight after B[T], the double edge to
v and possible unit uw entry; their right sides are exactly
`4-2(1[x in U]+1[x in W])`, `2e_z`, and `2-beta`. If threshold bits
are used, both equivalences to actual counts are required, as stated.

For a shared attachment s, zero defect to every other Z vertex means
`mu(s,z)+A_sz=1`; it is valid on at most49 distinct pairs, with no
assumption about their adjacency. The possible fixed common-core
witnesses cover `132+r+20-binomial(h,2)` Z pairs, because same-parent
pairs do not overlap same-P/same-Q pairs and the latter intersect
only in pairs of shared attachments. Hence the stated uncovered
counts1073,1072,1071 and loose bound `1073*48=51504` follow.
For h=1, exactly six same-parent and eight same-attachment-endpoint
pairs involving s were already covered, so at most14 additional
exact pair counters require at most672 new conjunctions. These are
algebraic upper estimates only; the approximate implementation-size
paragraph is not a measured or certified emitted size.

Omitting the redundant upper-defect counters for other Z pairs
cannot delete a true target. Full original degree and coverage remain
mandatory, so the omission cannot turn a satisfying assignment into a
non-graph witness either. The inherited entry theorem need not be
implemented as a generic counter at every pair to obtain a complete
necessary model. It remains essential that implementation preserves
the actual original pairs, constants, auxiliary equivalences and short
count scopes; no such source implementation is certified by this review.

## Final combined scope

Both inputs pass their stated mathematical obligations: seven shared-
parent port obligations and twelve full-model obligations, nineteen
in total, with zero open issues. The author's all50 endpoint-counter
clarification was read before closure. The new shared-port theorem,
the previous three exclusions, and the proposed complete model retain
their separate provenance and claims.

The review is reused, same-family and provisional. No manuscript was
edited by this reviewer; no code, solver, graph search, certificate,
external call, old computation, formalization, rendering or digest
was performed. Actual emitted counts and source semantics remain for
their separately authorized implementation review. No branch has been
solved or excluded by this specification review. All three actual
checked contradictions would be needed for a later internal-double
exclusion, and that would still not be an order61 exclusion.
