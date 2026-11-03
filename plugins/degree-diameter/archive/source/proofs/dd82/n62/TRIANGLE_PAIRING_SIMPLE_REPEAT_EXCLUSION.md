# Triangle pairing excludes every simple repeat matrix at order 62

## Theorem and status

For an actual finite simple graph on 62 vertices with maximum degree at most
eight and diameter at most two, its triangles admit a fixed-point-free pairing.
Consequently their number T is even. If the exact repeat matrix
B=A²+A−7I−J is simple, such a graph is impossible.

This paper proof passed fresh independent PASS24 and Gemini B15 review. The triangle-pairing
theorem does not assume that B is simple or use triple-repeat elimination.
The last exclusion covers both simple-repeat templates S_TOUCH and S_DISJOINT.
It does not exclude the five double-repeat templates.

## Actual graph identities

G is eight-regular, because a vertex of degree at most seven reaches at most
1+7+7·7=57 vertices in two steps. The exact B is symmetric, nonnegative
integral, has zero diagonal and row sum three, and commutes with A. For x≠y,

    c(x,y)+Axy=1+Bxy.

The identity 2t(x)=sum_{y~x} Bxy≤3 gives t(x)≤1. All triangles are therefore
vertex-disjoint, and each original edge belongs to at most one triangle.

Fix a triangle T0={r,a,b}. Its incident triangle edges have B weight one.
Every v∈T0 therefore has a unique additional repeat neighbor f(v), with
weight one. It is different from the other two triangle vertices and from v.
It is not adjacent to v: the two triangle edges already use the full even
incident-edge repeat budget 2t(v)=2.

## 1. Each repeat mate is outside the whole triangle neighborhood

We need the following consequence of the saturated-row S_TOUCH contradiction:

    f(v) has no original neighbor in T0.            (1)

Here is why that contradiction applies without a global simple-B assumption.
Suppose v=r and w=f(r) is adjacent to a. Since r,w are nonadjacent and
Brw=1, they have exactly two common neighbors. One is a; call the other c.
The point c lies in N(r), differs from a, and cannot equal b: otherwise wab
would be a second triangle at a and b. The only original edge inside N(r)
is ab, as r lies in precisely its one triangle.

The complete root repeat row is {a,b,w}, all of weight one. Thus every other
nonneighbor y of r has Bry=0 and exactly one common neighbor with r; w alone
has two, namely a,c. Relative to this root, the actual parent structure is
exactly S_TOUCH, with triangle edge ab and exceptional parent set {a,c}.

The proof in S_TOUCH_SATURATED_ROW_EXCLUSION.md uses no global bound Bxy≤1.
Its three saturated rows are forced by row sum three and nonnegative integer
entries: two or three specified unit lower bounds exhaust the available
weight. Its remaining steps use only the actual parent sets, at most one
triangle at a vertex, and AB=BA. It therefore gives the same contradiction
for this actual parent structure. This proves (1) for r, and symmetrically
for a and b. A repeat mate also cannot be a vertex of T0, by its definition.

Thus all three mates lie outside T0∪N(T0).

## 2. The three mates are distinct

Suppose f(r)=f(a)=w. The (r,w) entry of AB has the contribution A_ra B_aw=1.
Hence (AB)rw≥1.
The complete repeat row of r is {a,b,w}, so

    (BA)rw=Aaw+Abw+Aww=0

by (1) and absence of loops. This contradicts commutation. Therefore
F={f(r),f(a),f(b)} has three distinct vertices.

Write 1_S for the actual indicator vector of a vertex set S. Since the
repeat rows of the three triangle vertices are exactly their two partners
and their distinct mates, symmetry gives the vector identity

    B 1_T0 = 2 1_T0 + 1_F.                         (2)

## 3. Commutation forces F itself to be a triangle

Let C=N(T0)\T0, with set union understood. Every vertex outside T0 has at
most one neighbor in T0: adjacency to two would give a second triangle at
those triangle vertices. Consequently

    A 1_T0 = 2 1_T0 + 1_C.                         (3)

The sets C,F,T0 are pairwise disjoint by (1). Apply A to (2), B to (3),
and equate using AB=BA. Substitution gives

    4 1_T0 + 2 1_C + A 1_F
      = 4 1_T0 + 2 1_F + B 1_C,

or equivalently

    B 1_C = 2 1_C - 2 1_F + A 1_F.                (4)

For any v∈F, the left side is nonnegative. The right side is

    -2 + |N(v)∩F|.

Since F has exactly three vertices and has no loop, this neighbor count is
at most two. It must equal two. Every vertex of F is adjacent to both other
vertices of F, so F is an actual triangle in G.

## 4. This is a pairing of all original triangles

Each v∈F now has two unit repeat entries along its triangle edges in F,
and its already established unit repeat entry to the unique corresponding
vertex of T0. These exhaust its repeat row. Therefore applying the mate
construction to F returns exactly T0. Also F≠T0 since the sets are disjoint.

Thus the map T0↦F is a fixed-point-free involution on the finite set of all
actual triangles. Its orbits have size two, proving that the total triangle
count T is even. The empty triangle set satisfies the same conclusion.

## 5. A simple repeat matrix gives the opposite parity

Now additionally suppose B has only entries zero and one. Its row sum three
on 62 vertices gives 93 unordered repeat edges. Exactly 3T are original
triangle edges. On an original edge, the common-neighbor count is at most
one, so it contributes zero to choose(c(x,y),2). On a nonedge, a repeat
entry one gives exactly two common neighbors and contributes one; an entry
zero gives one common neighbor and contributes zero. Hence the standard
opposite-pair count of four-cycles is

    2 C4 = sum_{unordered x,y} choose(c(x,y),2)
         = 93 - 3T.

The left side is even, so T is odd. This contradicts the even T proved
above, excluding every original order-62 graph with simple repeat matrix.

## Scope and remaining connection

The proof uses exact matrix and graph counting identities; it uses no solver
run, no search non-hit, no independent matrix relaxation and no finite type
enumeration. The prior S_TOUCH proof is its only nontrivial local dependency.

With the separately recovered triple-repeat elimination, every remaining
order-62 candidate must have a double repeat and belongs to D0_MATCH,
D0_EDGE_BIN, D0_EDGE_BOUT, D1_MATCH or D2_MATCH. The previous seven-template
classification remains a valid coverage statement; both simple-repeat cases
are now contradicted if this proof is accepted. Lean implementation and
independent review are separate pending work, and arbitrary order62 remains
open until the five double-repeat templates are excluded.

Current formal status: actual triangle pairing/parity and the full simple-B exclusion compile with standard axioms; see formal/N62_SIMPLE_EXCLUSION_HANDOFF.md. B16 reviewed the pairing/parity source; B17 reviews the final incidence module. Other branch papers and the D0-to-D1 outlet supersede the original remaining-range paragraph above.
