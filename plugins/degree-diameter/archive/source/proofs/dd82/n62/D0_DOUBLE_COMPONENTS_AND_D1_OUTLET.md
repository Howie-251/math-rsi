# D0 double repeats close in four-vertex components

## Statements and current scope

In an actual order-62, degree-at-most-eight, diameter-at-most-two graph:

1. A D0_MATCH root forces a closed four-vertex component of B, a cycle with
   alternating weights 2 and 1. Its four vertices are independent in G.
2. A D0_EDGE_BOUT root forces the same closed weighted component; G induces
   its two opposite matching edges.
3. Using the separately proved triple-repeat, simple-repeat, D2 and BIN
   exclusions and the triangle-pairing theorem, every remaining original
   graph has a D1_MATCH root. Thus a complete D1 exclusion would suffice
   to finish the order-62 paper argument.

These paper deductions passed fresh independent PASS32 and Gemini B16 review. D1 is not excluded here.

## Shared D0 notation

Let B=A²+A−7I−J be the actual nonnegative integral, symmetric row-sum-three
matrix, commuting with A. The root 0 has independent neighbors X={1,...,8}.
Vertices w,a have parent sets S={1,2,3} and {4,5}; all other Y vertices have
one parent. The complete root row is B0=2e_w+e_a. Vertex w is triangle-free,
since its nonadjacent double repeat leaves only one unit of incident-edge
budget, which must be even.

For each i∈S, the two other points j,k of S have B_ij=B_ik=1. All other
off-diagonal entries from i into X are zero by the fixed parent sets.
Thus there is a unique unit endpoint c_i∈Y with

    B_i=e_j+e_k+e_{c_i}.                           (1)

No independent matrix assignment is used in these statements.

## 1. D0_MATCH

Here w is not adjacent to a. Its five Y-neighbors are all ordinary
single-parent points, and their parents avoid S because w is triangle-free.
Each label in X\S needs a common neighbor with w, so these five points
supply exactly one point in each of C4,...,C8. Hence B_wx=0 for x∈X.
The third unit endpoint b of row w lies in Y:

    B_w=2e_0+e_b.                                 (2)

We first exclude b=a. If b=a, then at (i,a) the product AB has contributions
B_0a+B_wa=2, whereas (BA)_ia=A_ja+A_ka+A_{c_i a}=A_{c_i a}≤1.
Thus b≠a and B_wa=0.

Still at (i,a), nonnegativity now gives

    1≤(AB)_ia=(BA)_ia=A_{c_i a},

so a is adjacent to every c_i. In particular c_i≠a. Also c_i≠w because
B_wi=0. At (c_i,w), equation (2) and c_i∈Y give

    (AB)_{c_i w}=A_{c_i b},
    (BA)_{c_i w}≥B_{c_i i} A_iw=1.

Thus b is also adjacent to every c_i. Moreover the right side includes
sum_{h∈S}B_{c_i h}, so that sum is at most one. It already contains the
unit at i. Therefore c_1,c_2,c_3 are distinct: equality c_i=c_j would
give two distinct unit summands.

The pair a,b has at least these three common neighbors. Therefore

    B_ab=c(a,b)+A_ab−1≥2+A_ab.

Row a already has B_a0=1 and has total three. It follows that A_ab=0,
B_ab=2, and its complete row is e_0+2e_b. Symmetry and (2) then force
the complete row at b to be 2e_a+e_w. Together with the root row, this is
the closed weighted cycle

    0 --2-- w --1-- b --2-- a --1-- 0.             (3)

All six possible G edges among these four vertices are absent: root 0
is nonadjacent to Y vertices w,a,b; w is nonadjacent to a by this branch,
and to b because it is triangle-free with positive B_wb; a,b were just
shown nonadjacent. This proves the first assertion.

## 2. D0_EDGE_BOUT

Here w is adjacent to a, and its third repeat b is a root-neighbor label
outside S∪{4,5}, canonically b=6. Again B_w=2e_0+e_b.

At (i,w), (AB)_iw=2A_i0+A_ib=2 and, using (1),
(BA)_iw=A_jw+A_kw+A_{c_i w}=2+A_{c_i w}. Thus c_i is nonadjacent to w.
At (0,c_i), the left product contains B_i,c_i=1 and the right product is
2A_w,c_i+A_a,c_i=A_a,c_i. Therefore a is adjacent to c_i.
At (c_i,w), the same calculation as above gives b adjacent to c_i.
Since c_i is an ordinary Y point, its parent is b.

The (0,c_i) equality now gives exactly sum_{x∈X}B_{x,c_i}=1. Hence the
three points c_i are distinct. The pair a,b is nonadjacent because b is
not a parent of a, and has these three common neighbors. The row budget
again forces B_ab=2, B_a=e_0+2e_b and B_b=2e_a+e_w, giving (3).

In this case G has exactly the two edges 0b and wa within the four points.
The other four pairs in (3) are nonadjacent by the template and by b's
choice outside the parents of a. This proves the second assertion.

## 3. Why a D1 root must remain

Invoke the separate recovered triple-repeat exclusion, so all B entries
are at most two. Let d be its number of unordered double edges and T the
number of original triangles. The row sum gives total unordered weight93;
there are 93−2d unit edges, exactly 3T of them original triangle edges.
Counting opposite pairs in four-cycles gives

    2 C4 = (93−2d−3T) + 3d = 93+d−3T.

The independently proved triangle pairing makes T even. Consequently d
is odd, and in particular positive. This also agrees with the separately
proved simple-B exclusion.

Suppose there were no D1_MATCH root. Choose an arbitrary double edge and
one endpoint as root. The recovered root-template reduction applies to
this choice: the triangle-free double root has one triple-parent point
and one double-parent point. Their intersections give D0, D1 or D2;
when disjoint and adjacent the extra repeat endpoint gives BIN or BOUT.
D2 and BIN are separately impossible, and D1 is absent by supposition.
Thus the chosen double edge lies in a D0_MATCH or D0_EDGE_BOUT template.

By the two assertions above it belongs to a closed component (3), which
contains exactly two double edges. Distinct such components are disjoint:
all four rows are exhausted, so there is no positive B edge leaving them.
As every double edge was arbitrary, all double edges are partitioned into
two-element groups. This makes d even, contradicting its odd parity.

Therefore every actual surviving order-62 graph has a D1_MATCH root.
This is an existence-of-representative reduction, not an assertion that
all roots are D1, or that D0 components individually cannot exist. It does
not remove the triple-repeat elimination's separate finite-check dependency,
and it does not yet supply a Lean proof of the classification or this outlet.
