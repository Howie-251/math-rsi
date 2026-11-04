# A6 closure: independent mathematical review

Date: 2026-11-01. Reviewer requested: GPT-6.1-sol, high, through the ARIS
proof-checker workflow. Review independence: **same-family**. Semantic acceptance:
**provisional**. Result: **PASS relative to the explicitly imported results**.
No FATAL, CRITICAL, MAJOR, or MINOR mathematical issue was found. The proof,
certificates, and project proof state have not been changed by this review.

## Exact scope and statement

For every matching F of the complete graph on the 32 vertices of Q5 with
exactly six unmatched vertices, of parity counts 2 and 4, and for each specified
hole v of the four-hole class, there exists a simple cycle with vertex set
Q5 minus v containing every edge of F; every edge of the cycle outside F is a
Q5 edge. F is permitted arbitrary long and same-parity edges. This review
establishes this A6 statement modulo the listed previous extension theorems
and certified finite inputs. It does not establish full Q6 P6 or close the
R8-covered residual or any higher hole level.

The audited source is `A6_CLOSURE_DRAFT.md`. Its hash and every directly
checked dependency hash are recorded in `a6_closure_independent_check.json`.
The separate machine verdict is `A6_CLOSURE_REVIEW.json`.

## Evidence and dependency DAG

The proof has the following acyclic dependencies:

* The preprocessing edge uses imported full Q5 A4, audited in
  `CANONICAL_COMPLETION_REVIEW.json` (PASS).
* Q4 N14_4, A4_4, N10_4, NC_4 and K4_4 come from
  `Q4_CORE_AND_A4_SPLIT.md`, audited in `Q4_CORE_REVIEW.json` (PASS).
  `Q4_GENERAL_AUGMENTATION.md` derives GQ4-avoid/path/cycle from these and the
  perfect-matching extension theorem. These general consequences were also
  directly reviewed here: the short augmentation preserves the specified free
  root/avoided hole, and the geometric bound supplies every required edge.
* T44 is imported from `Q4_TWO_AVOIDED_TRANSFER.md`, audited in
  `Q4_TWO_AVOIDED_REVIEW.json` (PASS).
* O15/O18 use the old two-hole optional-edge bounds and four new four-hole
  spectra. B4 uses the thirteen new alternate-endpoint path certificates.
  The fresh independent `A6_FINITE_INPUTS_REVIEW.md/.json` was actually read,
  its PASS result inspected, and all its certificate and source hashes checked.
  It verifies 717255 matchings and 2743933 positive path/cycle witnesses,
  including the old two-hole spectrum dependencies. It proves the geometric
  orbit cover separately from matching coverage; it imports no producer code.
* Sections 5--9 use only these inputs and path surgery. The geometry census
  selects among these sections. No step uses A6 or an A6 consequence as an input.

Existing Q4/A4/T44 direct audited-input hashes were also recomputed against
their respective PASS reports. Historical descriptions of other, then-open
results in those older reports do not add hypotheses to their Q4 statements.
The ultimate perfect-matching extension theorem is an explicit external
import, not reproved in this audit. No external web fact is needed here.

## Definitions and global invariants

E/O denote global minority/majority parity, not local parity coordinates in
each face. Every coordinate identification with Q4 preserves equality and
opposition of parity, which is sufficient for every imported theorem. The
mirror bar(t) is the short neighbor across the cut and is never silently
identified with the required partner. Ports are covered by original crossing
edges and cannot be original holes or internal-matching endpoints.

All artificial edges are temporary matching edges. Every one is deleted,
suppressed, or expanded. The interiors expanded in the final B cycle are
pairwise disjoint, and absent from that B cycle. In particular a bridge vertex
that becomes an interior is explicitly avoided on the B side. Original crossing
edges can be long; they are retained required edges. All genuinely new bridges
and optional edges are short. These facts establish both simplicity and the
required-edge/new-edge distinction of the final cycle.

Deleting a nonempty matching D from a simple cycle produces a path forest.
Restoring a proper subset of D by pairwise internally disjoint replacement
paths preserves a path forest: contraction yields a proper subgraph of the
original cycle. If xy is one deleted D edge and at least one other D edge is
deleted, x and y lie in different resulting components. These are exactly the
separation facts used in the port cases. For a spanning path, deleting any
nonempty set of its edges separates its two original endpoints.

## Obligation ledger: every case and application

| ID | Obligation and hypothesis discharge | Result |
|---|---|---|
| A01 | Short minority--nonforbidden-majority hole edge preserves v and reduces holes 2:4 to 1:3; Q5 A4 applies to the augmented arbitrary matching. | PASS |
| A02 | After preprocessing, every mirror of a selected nonforbidden majority hole, or minority hole, is covered whenever the opposite-side forbidden v cannot occur there. | PASS |
| A03 | GQ4-avoid augmentation uses two smaller-class holes and three larger-class holes excluding v when m>=2. The Q4 neighbor bound supplies a short pair. | PASS |
| A04 | GQ4-path augmentation retains the free root; the opposite target is allowed to become covered by N10_4/K4_4. Balanced m=0 is separately handled by the perfect-matching theorem in GQ4-cycle. | PASS |
| A05 | GQ4-cycle closes a Hamilton path from a free root to a short neighbor; the endpoint edge cannot already belong to a 16-vertex simple path. | PASS |
| A06 | O15 augmentation does not use the forbidden hole and its old optional union is a subset of the new union. Residual four-hole orbits and witnesses pass finite review. | PASS |
| A07 | O18 augmentation preserves balanced holes; residual holes reduce to 0,3,13,14. Its witness unions pass finite review. | PASS |
| A08 | B4 has exact four distinct holes, ordered root and excluded endpoint, and b nonadjacent to z. Full 196-configuration/13-orbit cover and all arbitrary matchings pass finite review. | PASS |
| A09 | Geometry normalization: translation sends a minority hole to 0, the second has weight 2 or 4; permutations send it to 3 or 15. This preserves arbitrary F and v. | PASS |
| A10 | Nonforbidden majority triples run over all odd vertices nonadjacent to both minority holes; v is every remaining odd vertex. Exactly 728+260=988 normalized cases result. | PASS |
| A11 | The five cuts select delta 2,3,4,1 whenever available; exactly two normalized cases remain and all their deltas are zero. | PASS |
| A12 | For any cut, 2|F_A|+c=16-|H_A| fixes parity of c. The proof never restricts parity or length of crossing edges. | PASS |
| A13 | Delta2,c>0: arbitrary pairing of X_A fills ports, leaving H_A of excess2; GQ4-avoid applies. Deleted D is nonempty. | PASS |
| A14 | Delta2,c>0: transferred R is a matching on all X_B, disjoint from F_B, leaving exactly balanced H_B. GQ4-cycle and expansion apply. | PASS |
| A15 | Delta2,c=0: k=2 contradicts the Q4 neighbor bound; k=0,1 give A holes (0,2)/(1,3), B holes (2,2)/(1,1). | PASS |
| A16 | Corresponding optional unions of cardinality >=15 and >=18 in a 32-edge Q4 intersect. Each independently supplies a cycle containing the chosen edge; no simultaneous prescription is assumed. Deletion and two short mirror edges merge the cycles. | PASS |
| A17 | Delta3: A counts (0,3)/(1,4) give at least two eligible t, with covered mirrors. c odd; at c=1 an eligible mirror distinct from the sole port exists. | PASS |
| A18 | Delta3: pairing X_A plus t leaves A excess2 and retains v; GQ4-avoid applies to every chosen D. | PASS |
| A19 | Delta3 internal w: R(w)=q is a B port while F_B(w)=k is internal, so k!=q. Suppressing w gives a genuine matching with holes H_B plus w, of minority excess2; avoiding w and expansion restore it once. | PASS |
| A20 | Delta3 port w: prescribe tx in D; c>=3 implies another gap. The two attachments through w restore just that gap, so the transferred graph stays a forest. B holes become H_B plus w; GQ4-avoid applies. | PASS |
| A21 | Double bridge: the two remaining A holes have the same parity and include v. Filling X_A,t,s leaves exactly those holes, so N14_4 applies. | PASS |
| A22 | Every prescribed D edge has disjoint endpoints. The w-z internal-pair prescription ts applies only when p=0, so it cannot conflict with port prescriptions. | PASS |
| A23 | For p port bridge vertices, |D|=(c+2)/2>p in all three allowed cases, so restoring the p port gaps leaves a forest. Its endpoint and interior sets are exactly the sets asserted in the proof. | PASS |
| A24 | In F_B+R only the 2-p internal bridge vertices have degree2. A closed component can only be the two-vertex parallel w-z component, requiring both F_B and R to contain w-z. If w-z is required, ts in D and another gap separate its ends, forbidding that R edge. | PASS |
| A25 | Suppression consequently gives a loop-free disjoint matching; all four holes H_B,w,z have the same parity. T44 avoids w,z. Each original/port/internal bridge vertex appears exactly once upon expansion. | PASS |
| A26 | Delta4 offers three covered mirror vertices. Mixed status gives case2; all internal gives an unpaired pair; all ports or two ports has even c>=4 and gives case3. No c=2 all-port option is omitted. | PASS |
| A27 | Delta1,k=0 would put two minority and three nonforbidden majority holes in B, contradicting Q4 geometry. Thus k=1 or2; c is positive odd. | PASS |
| A28 | For each root d and pairing D of other ports, adding dy leaves A holes of majority excess2 and keeps v free. Deleting dy from its GQ4-avoid cycle supplies exactly the claimed spanning d--y path. | PASS |
| A29 | Delta1 internal mirror w: delete D (possibly empty), attach crossings and y-w, and suppress w. The transferred graph is a forest; B holes H_B plus w have majority excess2. | PASS |
| A30 | Delta1 port mirror and c>=3: choose its partner as root d; nonempty D separates d,y before rejoining them at w. Avoiding w in B and expansion apply. | PASS |
| A31 | Delta1,k=2,c=1: the two distinct minority-hole mirrors cannot both be the sole port, so one is internal. | PASS |
| A32 | Delta1,k=c=1,d majority: A4_4 applies to the 3:1 holes v,b,d;y. At free d its two distinct cycle neighbors are minority, so one z!=y exists; deleting dz gives the required A path. | PASS |
| A33 | Delta1,k=c=1,d minority: B4 inputs are (v,b,z_input=y,d_input=d). Preprocessing proves b nonadjacent to y; B4 ends at z_out!=y of minority parity, with z_out!=d by path simplicity. | PASS |
| A34 | Both endpoint cases: q=bar(z_out)!=w. If q is an original hole, consuming it balances H_B; otherwise suppressing q leaves H_B plus q of majority excess2 and avoids q. Neither suppression collides with F_B, and expansion restores all vertices. | PASS |
| A35 | Exceptional geometry: on cuts j=2,3,4, t=0,s=3 leave two same-parity A holes including v, and two majority B holes. Both mirrors are covered; the double-bridge hypotheses hold except exactly the stated c=0 paired or c=2 two-port forms. | PASS |
| A36 | If all three cuts are bad, no F edge leaves S. Hence the 13 covered vertices of S would have to pair internally, an odd-cardinality contradiction. This proves existence of a good cut for every arbitrary matching F, without enumerating those matchings. | PASS |
| A37 | The second normalized exception is the image under the coordinate 0/1 swap. Translation/permutation transport the cycle back for every original hole set and every specified majority v. | PASS |
| A38 | The final cycle contains exactly 31 vertices, all F edges, and only short edges outside F. Both quantifiers, arbitrary F and each majority v, are retained. | PASS |

## Two delicate steps checked in detail

For double suppression, F_B+R should be viewed as a multigraph with the two
edge sources retained. Every vertex besides the internal bridge vertices has
degree at most one. Thus a cycle requires both internal bridge vertices, and
with only those two degree2 vertices it must be a parallel two-edge component.
When w-z is not an F_B edge there is no such component. When w-z is an F_B
edge, c>=2 and ts belongs to D, so deleting another D edge separates t,s;
the attachments therefore cannot produce R edge w-z. Each remaining component
has two distinct degree1 endpoints and can be compressed to an ordinary
matching edge. This also proves that suppressing two adjacent internal bridge
vertices creates no loop or repeated endpoint. T44 is applied only after this
check, with exactly the four advertised same-parity holes.

For the all-zero exception, set S={x: popcount(x>>2)<=1}. If x in S and r
outside S are joined by a matching edge, some j in {2,3,4} has r_j=1,x_j=0:
otherwise the support of r in these bits would be contained in that of x.
In a bad cut with c_j=0 such an edge is forbidden. In the other bad form
the B endpoint r has to be 2^j or 2^j+3, both inside S. This contradiction
is independent of the length of xr. The set has 16 vertices and exactly
holes 0,1,3. Therefore 13 covered vertices would all have mates inside S,
which is impossible. The paired-edge condition of the c_j=0 form is not even
needed for this final barrier argument; its zero-crossing condition suffices.

## Independent deterministic checks and counterexample pass

Run `D:\anaconda\python.exe a6_closure_independent_check.py` from this directory.
The checker imports neither `a6_cut_cover.py` nor any producer/checker code.
It enumerates all 15 possible nonzero even second minority vertices with the
first at 0, instead of assuming the reduction to the two normal forms. Its
8580 residual rooted geometries all normalize to the claimed cover; the normal
forms have exactly 728 and 260 cases and precisely the advertised two exceptions.
For all z the selected delta counts are 6200,1600,360,400 for delta 2,3,4,1,
and 20 all-zero exceptions (the additional eighteen are relabelings).

The checker also verifies the exceptional face holes and bridge coverage,
computes S and its three holes, and examines all 13*13=169 covered vertex
pairs across its boundary. Every one violates a bad-cut B-port restriction
even when zero-crossing cuts are relaxed to allow both designated ports.
This is a finite check of the barrier implication, not a search over matchings.

Adversarial edge cases checked mathematically include: c=0 in delta2 and in
double bridge; c=1 in both odd branches; c=2 with both bridges ports; the
w-z required internal edge; R and F_B parallel edges; the c=1 root of either
parity; the new mirror being either a hole or internally matched; arbitrary
same-parity crossings; and both all-zero exceptions. The problematic c=2
two-port double-bridge case is correctly excluded by Section 7 and handled
by the exception's global parity contradiction. The problematic c=1 root
mirror is correctly routed to B4/A4_4. No counterexample was found and no
unproved universal conclusion is inferred merely from that search.

There are no asymptotic, analytic interchange, probability-mode, or hidden
constant obligations in this finite combinatorial proof. All 38 obligations
above are discharged relative to their explicit inputs. The semantic verdict
remains same-family/provisional; a cross-family proof overlay is not supplied.

## Consequences after discharging the A6 assumption

At the parent's explicit request, this review also read the previously PASS
`EIGHT_HOLE_CONDITIONAL_REDUCTION_REVIEW.md/.json` and its reviewed draft.
The independent checker now verifies **all** of that report's audited-input,
imported-dependency, and checker-artifact hashes. All agree. The earlier
conditional audit covers 2588364 free-target hole geometries, including its
61 configurations requiring the root-bridge boundary construction. Those
checks are imported here, not falsely reported as having been rerun here.

The local endpoint consequence (called **G6-local here**) has the following
precise statement. For every arbitrary matching F of K(Q5) with 2t holes,
1<=t<=3, let h be its even-minus-odd hole count. If h is -2,0,2, r is a hole,
y!=r, and epsilon(r)+epsilon(y)=h, there is a Hamilton r--y path containing F
and adding only short edges. This is Section 1 of the conditional reduction.
The label distinguishes it from the already existing **G6 geometry
classification** in `SIX_HOLE_MIXED_AND_GEOMETRY.md`.

For completeness the direct proof is short. If y is free, adjoin ry: the
remaining 0,2,4 holes are balanced, and perfect matching/N10/K4 supplies a
full cycle, which can be opened at ry. If y is covered with mate k, replace
yk by kr. The holes replace r by y, so their count is still 2t and imbalance
is h-epsilon(r)+epsilon(y)=2epsilon(y). N14/A4/**now-proved A6** supplies a
cycle omitting exactly y. Delete kr and append original ky. All artificial
edges are removed; y is restored once. This verifies the full root/target
quantifiers, including covered targets and arbitrary same-parity required edges.

**K6** follows: every balanced six-hole arbitrary K(Q5) matching has a Hamilton
path from each free root to every opposite-parity target, free or covered.
It also has a full extending cycle, obtained by choosing a short neighbor of
the free root as target and closing the path. These are universal local lemmas,
relative to the same explicit earlier inputs, rather than sampled claims.

The just-audited A6 exactly matches the new universal assumption of the
conditional reduction, including arbitrary complete-graph matching edges and
each specified majority-hole avoidance. Substitution therefore proves the
**complete Q6 eight-hole FREE-target endpoint theorem**: for every 28-edge
short matching M in Q6 and each two distinct free vertices u,v of opposite
parity, there is a Hamilton u--v path containing M. It also proves all covered
targets satisfying that reduction's preliminary augmentation or nine-row cut
criterion. No stronger consequence is inferred from the previous PASS.

The full eight-hole endpoint theorem still requires **R8-covered**. Its
explicit all-six-directions short-matching witness survives, so this is a
nonempty remaining domain for the present scheme. Full P6 and the 10,12,14,16,18
hole levels remain open. These consequences add no proof dependency cycle:
A6 was proved from Q4 inputs and Q5 A4 before it was substituted downstream.
Their semantic assurance is the same **same-family/provisional** assurance.
