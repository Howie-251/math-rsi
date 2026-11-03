# A surviving order62 graph has connected repeat support

## Claim and status

Let G be an actual finite simple graph on62 vertices of maximum degree
at most eight and diameter at most two. Its repeat matrix
B=A²+A−7I−J has connected positive support.

Consequently G is triangle-free, every double repeat is of D1 type,
and the number d of double-repeat pairs belongs to

    {1,3,5,7,9}.

This is a paper reduction with explicitly bounded exact quotient
classifications, not an exclusion of all order62 graphs. The
classifications are external integer computations, not Lean-certified
enumerations. Individual proofs, computation and integration retain
separate audit scopes. Gemini B22 accepted the original integration and
B24 accepted the shorter component-count dependency. The triple-repeat
import now uses the analytic replacement accepted in B28; the separate
finite component-quotient classifications still remain external checks.

## 1. Restrict the number of components

Write c for the number of connected components of the positive support
of the actual B, not of the original graph. Apply the reviewed general
triple-repeat exclusion in TRIPLE_REPEAT_ANALYTIC_COMPONENT_EXCLUSION.md,
D0/D1 classification and odd-double parity.
They give B≤2 and at least one D1 pair.

For a selected D1 pair, let H be its heavy component and K the component
of its generated unit repeat triangle. The earlier
D1_COMPONENT_MINIMUM_SIZES.md, Sections1–5, gives |H|,|K|≥12.
GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md gives the equitable original-graph
quotient R and

    R²+R=10I+1 nᵀ,    c+2 tr(R)=17.

Thus c is odd. SHORT_COMPONENT_COUNT_BOUND.md proves c≤9 using only
those earlier twelve-point lower bounds. Briefly, H=K gives internal
degree at least4 and the trace bound directly. Otherwise packing gives
c≤11. If c=11, balance and the nonnegative common-neighbor budget
force |H|=|K|=12 and r_HK=r_KH=4. The other components are eight fours
and one six. Writing alpha=r_HH, their total outward degree from H is
4−alpha, while their common-neighbor budget is2−alpha². Balance with
sizes at most6 makes the latter at least the former, forcing
alpha²−alpha+2≤0, impossible. Oddness then gives c≤9.

The paper THREE_COMPONENT_EXCLUSION.md excludes c=3, leaving

    c ∈ {1,5,7,9}.                                      (1)

General triple-repeat exclusion, D1 existence from
D0_DOUBLE_COMPONENTS_AND_D1_OUTLET.md Section3, and the earlier
H,K≥12 proof are genuine dependencies. Triple exclusion now retains only
the recovered analytic Steps1–3 and the raw-input quotient trace identity;
its former finite matrix table is not needed. The later chain excluding
twelve-point components to reach H,K≥14 is no longer needed here.
Their removal from the separate c3 proof does not remove these retained
imports from the general bound on c.

## 2. Exact quotient classification for c=5,7,9

For each c in {5,7,9}, every actual component quotient satisfies:

- positive even sizes n_i≥4 with sum62;
- nonnegative integer entries and row sums8;
- n_i r_ij=n_j r_ji;
- r_ii<n_i, since the original graph is simple;
- trace(R)=(17−c)/2;
- R²+R=10I+1 nᵀ.

The classification is implemented in
computations/dd82/n62/component_quotient_search.py and saved in
component_quotients_5.json, component_quotients_7.json and
component_quotients_9.json. The independent checker is
check_large_component_quotients.py with its separately saved output.

The finite objects are integer quotients of at most nine components,
not original62-vertex adjacency matrices. Here is the coverage argument.

First enumerate all sorted even size partitions of62 with each part
at least4. Their counts for c=5,7,9 are respectively221,201,94.
For a fixed size vector n and a row i, balance implies

    r_ij=(n_j/g_ij)t_ij,
    r_ji=(n_i/g_ij)t_ij,
    g_ij=gcd(n_i,n_j),  t_ij≥0.

All entries are bounded by the row sum8. Thus the generator enumerates
every possible off-diagonal row and its balanced column using finite
integer ranges. The diagonal is the remaining row sum and is retained
only when it is below n_i, at most the total trace, and satisfies

    r_ii²+r_ii+Σ_{j≠i} r_ij r_ji=n_i+10.                 (2)

No actual row is discarded by these tests. Backtracking joins these
complete row domains. Whenever two rows i,j have been selected, both
their balance entries and both ordered off-diagonal equations

    Σ_l r_il r_lj+r_ij=n_j

are determined and checked. A complete selection with the prescribed
trace therefore satisfies every matrix entry of the exact identity;
conversely every actual R follows one branch. Simultaneous permutations
within equal-sized components identify only relabelled copies.

The independent implementation instead generates rows by stars and
bars, checks divisibility directly, and uses forward filtering. It
reproduces every original row domain and the following complete results:

| c | Size partitions | Labelled survivors | Canonical quotients |
|---|---:|---:|---:|
| 5 | 221 | 2 | 1 |
| 7 | 201 | 6 | 1 |
| 9 | 94 | 0 | 0 |

For c=5 the unique size vector and quotient are

    n=(4,8,10,20,20),
    R=[[1,2,5,0,0],
       [1,2,0,0,5],
       [2,0,0,4,2],
       [0,0,2,2,4],
       [0,2,1,4,1]].

For c=7 they are

    n=(4,4,4,10,10,10,20),
    R=[[1,1,1,0,0,5,0],
       [1,1,1,0,5,0,0],
       [1,1,1,5,0,0,0],
       [0,0,2,0,1,1,4],
       [0,2,0,1,0,1,4],
       [2,0,0,1,1,0,4],
       [0,0,0,2,2,2,2]].

No realizability conclusion is drawn from these survivors.

## 3. The two remaining quotients cannot be actual graphs

Apply the uniform lemma in
FIVE_SEVEN_COMPONENT_QUOTIENT_EXCLUSIONS.md: a four-point repeat
component containing an original-graph edge forces a separate closed
six-point repeat component.

For clarity, its actual-graph mechanism is as follows. Triangle pairing
prevents any vertex of the four-point component from lying in an original
triangle; otherwise its repeat component would have size six.
Consequently the repeat entry on the given original edge is zero.
A repeat row of total three has only two other vertices available and
entries at most two, so it contains a double edge. It cannot be D1,
whose established local repeat rows contain six distinct vertices in
its heavy component. It is therefore D0. The D0 component theorem and
its generated-triangle companion theorem force the separate
six-vertex unit prism.

Each displayed quotient has a four-point component of internal original
degree one. It therefore contains an original edge, but neither size
vector contains six. The uniform lemma contradicts both quotients.
Hence c=5 and c=7 are impossible; c=9 was already excluded by the exact
classification. Equation (1) now forces c=1.

## 4. Consequences in the connected-support case

An original triangle would belong to a closed six-point repeat
component by triangle pairing. Since the whole support is connected
and has62 vertices, no original triangle exists.

A D0 double would belong to a closed four-point component, so no D0
double exists either. Every double is therefore D1. Odd-double parity
gives d positive and odd.

The global port bound in GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md is

    15d+9T+2d1≤186,

where T counts original triangles and d1 counts D1 doubles. Here
T=0 and d1=d, so17d≤186. Thus d≤10; combined with oddness this gives

    d ∈ {1,3,5,7,9}.                                   (3)

There are exactly93−2d unit-repeat unordered pairs, since the total
repeat-row weight is186. All positive repeat pairs are original
nonedges because the graph is triangle-free. Each unit pair has two
common neighbors and each double pair has three. Counting opposite
pairs of original four-cycles therefore gives

    number of original four-cycles
      = ((93−2d)+3d)/2
      = (93+d)/2 ∈ {47,48,49,50,51}.                    (4)

Each generated unit repeat triangle belongs to one of the d doubles,
and these triangles are pairwise disjoint. This does not assert that
every unit triangle of B is generated; that remains a separate
structural question.

## Remaining scope

Connected repeat support, triangle-freeness, and (3)–(4) are necessary
conditions for any surviving actual graph. They do not construct such
a graph and do not show that none exists. The arbitrary order62
exclusion and exact N(8,2) remain open. No dedicated reproof of known
orders63–65 is part of this reduction.
