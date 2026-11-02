# Order62 cannot have exactly three repeat-support components

## Claim and status

Let G be any finite simple graph on62 vertices with maximum degree at most
eight and diameter at most two, and let B=A²+A−7I−J be its actual repeat
matrix. Then the positive support of B does not have exactly three
connected components.

This is a paper theorem with one explicitly bounded exact integer
classification. It is not a Lean theorem, a whole-order exclusion, or a
claim that the remaining connected-support case is impossible. The
three individual quotient exclusions have separate proof-checker
receipts; the widened classification and this integration have their
own review scopes. Cross-family review is pending.

## 1. Exact reduction to three integer quotients

Use the actual graph foundations and Section3 of
GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md. The matrix B is symmetric,
nonnegative and integral, has diagonal zero and row sum three, and
commutes with the eight-regular adjacency matrix A. Its support
components form an equitable partition for A.

If there are three components, let their sizes be n=(n1,n2,n3) and
write R for the original-graph quotient, with r_ij counting neighbors in
component j of a vertex in component i. Then

    R has nonnegative integer entries and R 1=8 1;
    n_i r_ij=n_j r_ji;
    R²+R=10I+1 nᵀ;
    tr(R)=7.

The trace is the three-component instance of c+2 tr(R)=17. Equivalently,
the quotient has eigenvalue8 on constants, and its other eigenvalues
are the two conjugate roots of t²+t−10. Their sum is−1.

Each component size is a positive even integer. Indeed, three times
its order is twice the sum of its unordered repeat-edge weights. In
particular n_i≥2, without any bound on individual repeat entries.

The finite classification is implemented and independently checked in:

- computations/dd82/n62/three_component_quotients.py and its saved JSON
  are the original diagnostic with n_i≥4.
- computations/dd82/n62/check_three_component_quotients.py and
  three_component_quotients_check.json check the wider domain n_i≥2
  and compare its complete result to the three original candidates.

Here is the precise finite search, sufficient to reproduce the check.
Enumerate all45 nonnegative integer triples with sum8 and form every
ordered triple of these rows. Retain trace7. Exactly9108 matrices remain.
For each, compute the exact integer matrix Q=R²+R−10I. Retain it only
when its three rows are equal to a positive even vector n and edge
balance n_i r_ij=n_j r_ji holds. Its row sum is automatically62, so
n1+n2+n3=62. Finally quotient by all six simultaneous permutations of
component sizes, rows and columns. The result is exactly18 labelled
matrices in the following three orbits:

| Sizes | R |
|---|---|
| (6,24,32) | [[0,8,0],[2,2,4],[0,3,5]] |
| (8,24,30) | [[2,6,0],[2,1,5],[0,4,4]] |
| (12,20,30) | [[3,0,5],[0,2,6],[2,4,2]] |

Every actual quotient satisfies all filters and therefore appears in
this list up to relabelling. No surviving quotient is assumed to be
realizable. This is a small quotient classification, not an enumeration
of original62-vertex graphs. The saved checker is external exact
evidence; its classification has not been certified by the Lean kernel.

## 2. Local dependencies used in the exclusions

The following previously proved actual-graph facts are used.

1. Every original triangle belongs to a closed connected six-vertex
   repeat component consisting of it and its mate triangle. See
   TRIANGLE_PAIRING_SIMPLE_REPEAT_EXCLUSION.md, Sections1–4.
   This statement does not require B to be simple.
2. Every actual double-repeat pair is either D0, in a closed
   four-vertex repeat component, or D1. See
   D0_DOUBLE_COMPONENTS_AND_D1_OUTLET.md and the actual-graph
   construction formalized in N62DoubleRoot.lean. The local
   classification does not require a global B≤2 assumption.
3. For a D1 pair, write H for its heavy component and K for the
   component containing its generated unit triangle. If H=K,
   then r_HH≥4. Otherwise r_HK≥4 and r_KH≥3.
   These are the local incidence bounds of
   GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md, Section4. In the D1 root
   notation, the generated parents1,2,3 and the additional parent4
   belong to K, while 0,w,a belong to H and all neighbor1.
   Thus the bounds come from actual vertex incidences.

Within any of the three listed quotients, a repeat entry3 is already
impossible: it exhausts the rows of its two endpoints, making them a
closed component of size2. None of the listed sizes is2. Consequently
one may use B≤2 in these cases without invoking the separate recovered
triple-repeat finite classification.

## 3. Excluding each possible quotient

### Sizes6,24,32

Apply THREE_COMPONENT_6_24_32_EXCLUSION.md. The six-point component is
independent and all its original neighbors lie in the24-point component.
Each vertex of the latter has a two-point parent set in the former and
two internal neighbors. Their three parent pairs partition the six
points, so pair labels repeat after three steps.

A zero repeat entry between two of the six points exists by the row
budget. It has a unique common neighbor and hence a uniquely represented
parent pair. The period-three rule forces an original triangle in the
24-point component. Fact1 instead puts that triangle in a six-point
repeat component, a contradiction.

### Sizes8,24,30

Apply THREE_COMPONENT_8_24_30_EXCLUSION.md. None of these components has
size6, so Fact1 gives triangle-freeness of the original graph. There is
no size4 component, so Fact2 rules out D0. A heavy pair in the
eight-point component cannot be D1: its generated component could be
itself,24,or30, but respectively the quotient has internal degree2<4,
reverse degree2<3,or forward degree0<4. Thus its repeat matrix is simple.

The source proves its internal original graph is two four-cycles.
Parent pairs of24-point vertices cross the two cycles; a vertex's
original matching partner has the simultaneous opposite parent pair.
The binary cross-repeat matrix M has row and column sums two.
Connectedness makes each row and column select one point of each
opposite pair.

Choose a zero entry M_ij. Its parent label has a unique representative v,
and the opposite label's unique representative is its matching partner
p(v). Commutation requires repeat-neighbor weight2 covering each opposite
parent. The two weighted sets can intersect only at p(v), where the
repeat weight is zero by triangle-freeness. Their total required
weight4 exceeds the repeat row sum3. This is the source's contradiction.

### Sizes12,20,30

Use the proof in THREE_COMPONENT_12_20_30_EXCLUSION.md with the following
shorter derivation of its initial properties. This explicitly replaces
that paper's use of the stronger heavy-component size bound.

Again Fact1 makes the whole original graph triangle-free and no D0
component is possible. If a double pair lay in the12-point component,
its generated component could be12,20,or30. Fact3 excludes these three
choices because respectively r_CC=3<4, r_CD=0<4,or r_EC=2<3.
There is no triple entry by Section2. Therefore the repeat matrix on
the12-point component is the adjacency matrix of a connected cubic
simple graph.

These are exactly the initial properties used in Sections1–4 of the
source. Write P for the internal original cubic adjacency matrix, Z for
the internal two-regular matrix on30 points, and X for the12-by30
incidence block, with row sum5 and column sum2. The source first makes
P connected using triangle-freeness and the bound of two on common
neighbors. For W=XXᵀ−5I it proves

    W=2I+J+B_C−P²−P,    PX+XZ+X=J.

The weighted graph W is connected: otherwise its component-constant
space is invariant under P and B_C, and the B_C quotient has trace
at most2q but at least3+(11/4)(q−1)>2q.

Connectedness bounds ker(Xᵀ) by one dimension. The second displayed
identity gives every nonprincipal P eigenvalue at most1, including the
possible bipartition-sign kernel direction. Finally P is a triangle-free
cubic graph on12 points, so

    tr P=0,   tr P²=36,   tr P³=0.

The polynomial (t−1)(t+3)² makes all eleven nonprincipal eigenvalues
equal to1 or−3. The zero trace would give multiplicity7/2 for−3.
This contradiction excludes the final quotient.

All three possibilities are impossible, proving the claim.

## 4. Consequence for the remaining component counts

If one additionally uses the reviewed general D1 existence and minimum
size chain, the remaining support-component counts are

    c ∈ {1,5,7,9}.

This consequence uses more dependencies than the three-component theorem.
General D1 existence retains the recovered triple-repeat exclusion.
For a selected D1 pair, both associated components have size at least14.
If they coincide, their internal original degree is at least4, so
c+2 tr R=17 implies c≤9. If distinct, all other components have at
least4 vertices under B≤2, so 28+4(c−2)≤62 gives c≤10.
The same trace identity makes c odd. The theorem above removes c=3.

This does not decide any of c=1,5,7,9. It neither proves full
nonexistence at order62 nor changes the current global bound.

## Evidence boundary

Individual same-family audits: the6-case and original classification
are in proof-checker-n62-three-components-20261011; the12-case is in
proof-checker-n62-12-20-30-20261011; the8-case is in
proof-checker-n62-8-24-30-20261011. The independent widened-domain check
and this dependency simplification must be recorded separately.
Gemini review and Lean certification are not implied by these audits.

