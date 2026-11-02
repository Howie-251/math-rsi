# Saturated rows exclude D0_EDGE_BIN at order 62

## Theorem and scope

No actual order-62 graph with maximum degree eight and diameter at most two
realizes D0_EDGE_BIN. This complete paper argument passed fresh independent review (PASS9; reviews/dd82/proof-checker-n62-bin-20261011). Cross-family B16 review is pending.
It does not rely on SAT, global repeat simplicity, or the triple-repeat
elimination inside this branch.

Use the actual matrices A and B=A²+A−7I−J. The original graph is
eight-regular; B is symmetric nonnegative integral with zero diagonal,
row sum three, and AB=BA. Every vertex is in at most one triangle.

The root 0 has independent neighbors X={1,...,8}. The exceptional vertices
w,a have parent sets {1,2,3} and {4,5}, respectively, and w is adjacent to a.
Every other Y vertex has one parent. The branch's additional repeat neighbor
b of w is one of {4,5}, canonically b=4. Thus the complete rows are

    B0=2e_w+e_a,       Bw=2e_0+e_b.                (1)

This complete Bw row is part of the already derived D0_EDGE_BIN template,
not an independently assigned matrix. Equivalently it follows from its
fixed local choice Bwb=1 and the row sum. In particular b∈X and a~b.

## One more saturated row

Choose i=1 and let j=2,k=3. Within X, the parent sets give
B_ij=B_ik=1 and every other off-diagonal entry of row i on X is zero.
The original pairs in X are all nonedges. Row sum three therefore supplies
a unique further unit repeat endpoint c, lying in Y:

    Bi=e_j+e_k+e_c.                               (2)

The endpoint c is different from 0 (B_i0=0), from i (zero diagonal), and
from all of X (the fixed common-neighbor counts just stated). It is also
different from w: row w in (1) has no positive entry at i. The original
neighborhood of i is {0,w} union Ci, where Ci is its singleton-parent class.

## Three entries of the commutation identity

At (i,w), row (1) gives

    (AB)iw=2 A_i0+A_ib=2,

because i and b are distinct members of the independent X. Row (2) gives

    (BA)iw=A_jw+A_kw+A_cw=2+A_cw.

Thus A_cw=0.

At (0,c), the left side has contribution A_0i B_ic=1. The complete root
row in (1) gives the right side

    (BA)0c=2 A_wc+A_ac=A_ac.

Consequently A_ac=1. In particular c≠a.

At (c,w), the complete row of w gives

    (AB)cw=2 A_c0+A_cb=A_cb,

since c∈Y. The right side has contribution B_ci A_iw=1, so A_cb=1.
Together with A_ab=1, this makes a,b,c a genuine triangle and implies
B_bc≥1.

Return to entry (0,c). Both i and b are neighbors of 0, and they are
distinct. Therefore

    (AB)0c ≥ A_0i B_ic + A_0b B_bc ≥ 2,

while its right side is still A_ac=1. This contradicts AB=BA.

## Remaining range

The proof closes exactly D0_EDGE_BIN. It uses the actual parent data and
the actual additional repeat endpoint prescribed in that template. It
does not exclude D0_EDGE_BOUT, whose endpoint b lies outside {4,5}; there
the step a~b is unavailable. Other branch exclusions have separate proofs
and reviews. No Lean implementation of this branch is claimed here.
