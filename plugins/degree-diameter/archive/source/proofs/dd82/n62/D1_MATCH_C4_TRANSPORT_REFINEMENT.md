# The C4 transport refinement of the hard D1 branch

## Scope

Assume the actual order-62 graph and the normalized hard D1 notation established in `D1_MATCH_HARD_BRANCH_REDUCTION.md`. This note proves additional exact support restrictions. It does not exclude the branch.

Use the complete rows

    B0=2e_w+e_a,       Bw=2e0+e_r,
    B1=e2+e3+e4,      B2=e1+e3+e_b,      B3=e1+e2+e_c,
    Ba=e0+e_p+e_q,    Br=e_w+e_s+e_t,

where r∈C2, p,s∈C3, q∈C4. The ordinary neighborhoods of w and a are

    W={W4,...,W8},
    U={u2,u3,A5,...,A8},

respectively. These sets are disjoint. We already know b∈W, c∈U∩(C5∪...∪C8), a and r are nonadjacent with unique common neighbor c, r≠u2, p≠u3, q≠W4, and all positive B neighbors of a triangle-free vertex are triangle-free. Labels 1,2,3,4 and a,r,b,c are triangle-free.

Write B_{S,y}=sum_{x∈S}B_xy. The established transport equations are

    B_C2,y = [y∈C1∪C3] + A_by − [y=r],
    B_C3,y = [y∈C1∪C2] + A_cy − [y=r]             (1)

for ordinary y. Both A and B between C2,C3 are perfect matchings. Internally B[C2] is empty and B[C3] consists of one unit edge v1v2, where {v1,v2}=N(c)∩C3. Neither v_i is u3 or the unique original C3-neighbor of r.

## 1. The complete row at label 4

The row of 4 already contains B41=1. Its other positive endpoints are ordinary vertices: its remaining X entries vanish, B40=0, B4w=0, and B4a=0.

At (4,a), commutation gives

    (AB)_4a = B0a + B_aa + B_C4,a = 1+0+1 = 2,
    (BA)_4a = 1 + sum_{y≠1} B4y A_ya.

Thus the residual weight of row 4 on the ordinary neighbors U of a is exactly one. The residual row sum is two; integrality rules out a single double entry and gives two distinct unit endpoints f,g. Exactly one, call it f, lies in U.

For the other endpoint g, the root identity

    sum_{i∈X}B_iy=2A_wy+A_ay

and B4g=1 force adjacency to w or a. Since g∉U, it lies in W. Hence

    B4=e1+e_f+e_g,   f∈U,   g∈W.                 (2)

The endpoint g differs from W4: positive B4g would otherwise lie on an original edge incident with triangle-free vertex 4. Similarly f is not in C4. Since each U point has total X-repeat weight one, f≠c (whose X-repeat is already at 3). The endpoint b may or may not equal g.

At (2,4), commutation gives

    B_4,C2 = A_b4 = [b=W4].

Since g∈W lies outside C2 and U has only the point u2 in C2,

    f=u2 if and only if b=W4.                    (3)

At (3,4), commutation gives B_4,C3=A_c4=0. Thus f≠u3.

## 2. No repeat crosses from C3 to C4

Since f≠c, equation (2) gives B4c=0. Also 4 and c are nonadjacent, while a is adjacent to both. They therefore have exactly that common neighbor. In N(4)={0,a}∪C4 this implies

    N(c)∩C4 is empty.

Now equation (1) gives B_C3,y=A_cy=0 for each y∈C4. Nonnegativity proves the full block vanishes:

    B(C3,C4)=0.                                 (4)

In particular B_pq=0.

The original edges between C3 and C4 form a five-edge matching, missing u3 in C3 and W4 in C4. Indeed B4,C3=B3,C4=0; for x∈C3 the common-neighbor equation with 4 gives d_C4(x)=1−[x=u3], and for y∈C4 the equation with 3 gives d_C3(y)=1−[y=W4].

## 3. The sole internal repeat edge in C4

Using N(4)={0,a}∪C4, equation (2) gives, for every ordinary y,

    B_C4,y = [y∈C1] + A_fy + A_gy − [y=p] − [y=q].    (5)

The pair 4,f is a nonedge with B4f=1 and hence has two common neighbors. One is a, so f has exactly one neighbor in C4. The pair 4,g is also a nonedge with B4g=1, but g is adjacent to neither 0 nor a, so g has exactly two neighbors in C4.

Sum (5) over C4. Its right side is 1+2−1=2. Thus the symmetric nonnegative integral zero-diagonal matrix B[C4] has total entry sum two. It consists of exactly one unordered unit edge.

Nonnegativity at y=q additionally forces q to be adjacent to f or g. This describes a necessary cancellation in (5); it is not a new adjacency between a and q.

## 4. Fully saturated rows on the C3 internal edge

Let y_i∈C2 be the B-perfect-matching mate of v_i. If v_i≠p, let z_i∈C1 be its B-matching mate there. If v_i=p, put z_i=a instead. The original hard-branch matchings and the complete row of a show that these are three distinct unit entries:

    B_vi = e_vj + e_yi + e_zi,   {i,j}={1,2}.    (6)

Indeed one entry is the internal edge, one is the C2 matching, and the third is the C1 matching except at its omitted point p, where B_pa=1 supplies it. All three units exhaust the row. Thus there is no unsaturated exception if p is an endpoint of the internal edge.

As two exact consequences of (6), commutation at (a,v_i) and (r,v_i) yields

    A_q,vi = [y_i=u2],
    A_t,vi = A_r,zi.                             (7)

For the second equality, A_r,y_i=0 because C2 is independent, and A_r,v_j=0 because neither internal-edge endpoint is the original C3-neighbor of r. When z_i=a, the right side is zero; when z_i∈C1, it is one precisely when z_i is the original C1-neighbor of r. In the first equality, neither v_j nor z_i is adjacent to a, while y_i is adjacent to a exactly when it equals u2.

## 5. Light mates of this heavy edge lie in no unit B triangle

The complete row of a is {0,p,q}. No two of these three endpoints are adjacent in the support of B: B0p=B0q=0 from the complete root row, and Bpq=0 by (4). Therefore a lies in no unit B triangle.

Rooting the same heavy edge at w gives another hard D1 representation, as proved in the preceding reduction. Applying this same argument in that representation proves that r also lies in no unit B triangle. This does not assert that arbitrary unit-repeat vertices avoid unit B triangles: the generated triangle {1,2,3} is an explicit counterexample to such an extension.

## 6. Why aggregate cross-block commutation has not given a contradiction

For completeness, one can sum the (C2,C3) block of AB=BA. Let D=C4∪...∪C8, restricted to ordinary vertices. The H=C1 matching terms cancel in total. The internal C3 edge contributes two, and the term through a contributes one. All other uncancelled terms give exactly

    3 + sum_{d∈D∩N(c)} d_C2(d)
      − sum_{d∈D∩N(b)} d_C3(d) = 0.              (8)

This is consistent with the existing identities. Vertex c has three neighbors in D: its other neighbors are a,r,v1,v2 and its root parent. Exactly one of these three D-neighbors lies in W, since c,w are a nonedge with Bcw=0 and hence have one common neighbor. For d∈D∩N(c), the common-neighbor equation with 2 gives d_C2(d)=1−[d∈W]; the potential exceptional point b is not adjacent to c, since both b,c are neighbors of triangle-free r. The first sum in (8) is therefore two.

Vertex b has five neighbors in D: its other neighbors are w,r and its root parent. None lies in W, because that would make a triangle at w. For each d in this five-point set, the common-neighbor equation with 3 gives d_C3(d)=1. Thus the second sum is five, and (8) reads 3+2−5=0.

The unique internal C3 repeat edge is therefore balanced at this aggregate level. Any contradiction must retain additional pointwise support information, for example the saturated rows (6), or use further global structure. No exclusion or parity of heavy edges within each B component has been established here.
