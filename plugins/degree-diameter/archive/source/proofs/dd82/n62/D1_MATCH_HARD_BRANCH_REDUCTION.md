# D1_MATCH reduces to a persistent asymmetric branch

## Claim and limitation

For an actual order-62, maximum-degree-eight, diameter-two graph, a D1_MATCH root has the structure proved below. In particular, its heavy repeat remains D1_MATCH when rooted at its other endpoint; the potential D0_MATCH reroot is impossible. The two unit mates of the heavy endpoints are distinct nonadjacent vertices, have no repeat between them, and have exactly one common neighbor.

This is a rigorous local reduction, **not an exclusion of D1_MATCH**. It uses the triangle-pairing theorem from `TRIANGLE_PAIRING_SIMPLE_REPEAT_EXCLUSION.md` and the D0_MATCH component theorem from `D0_DOUBLE_COMPONENTS_AND_D1_OUTLET.md`. It uses no N15 assumption, no independently assigned matrix, and no finite search.

## Actual graph notation

The graph is 8-regular. Its actual matrix

    B = A² + A − 7I − J

is symmetric, nonnegative integral, has zero diagonal and row sum three, and commutes with A. For distinct vertices,

    c(u,v) + A_uv = 1 + B_uv.

Every vertex belongs to at most one original triangle. The triangle-pairing theorem has the following useful consequence: every positive B entry connects two vertices with the same triangle status. Indeed, the B component of any triangle vertex is precisely its paired triangular prism, all of whose vertices lie in triangles. In particular, a positive B neighbor of a triangle-free vertex is triangle-free.

Fix a D1_MATCH root 0. Its independent neighborhood is X={1,...,8}. The exceptional outside vertices satisfy

    P(w)={1,2,3},   P(a)={1,4},   w not adjacent to a.

Every other outside vertex has a unique parent in X. Write C_i for its class. Then

    |C1|=5,   |C2|=|C3|=|C4|=6,   |Ci|=7 for i≥5.

The fixed rows and entries are

    B0 = 2e_w + e_a,
    B1 = e2 + e3 + e4,
    B12 = B13 = B23 = B14 = 1,

and all other distinct X-pair entries vanish. Vertices 0,w,1,2,3 are triangle-free: 0 by the template, w by its nonadjacent double repeat, 1 by its complete nonadjacent repeat row, and 2,3 because their two fixed nonadjacent unit entries leave less than the two units needed for a triangle. The triangle-pairing consequence makes 4 and a triangle-free as well.

## 1. Three exceptional unit endpoints

The five ordinary neighbors of w consist of exactly one point W_i in each C_i, i=4,...,8. To see this, w has no neighbors in C1,C2,C3, because each would form a triangle through w and its parent. It is nonadjacent to a. Each of labels 4,...,8 requires a common neighbor with w, and only an ordinary point in its own class can supply one. The five available neighbors therefore supply exactly one each. In particular, B_wi=0 for every i∈X.

Let W={W4,...,W8}. The remaining unit endpoint of w is an outside vertex r:

    Bw = 2e0 + e_r.

At (1,w), commutation reads

    2 = (BA)_1w = (AB)_1w
      = 2 + B_aw + sum_{x∈C1} B_xw.

Hence B_aw=0 and w has no repeats in C1. At (0,a), commutation gives

    sum_{i∈X} B_ia = 2A_wa = 0.

Thus all B_X,a entries vanish. At (1,a) it then gives

    1 = 1 + sum_{x∈C1} B_xa,

so a has no repeats in C1 either.

For every ordinary y, the complete row of 1 gives

    B_wy + B_ay + sum_{x∈C1} B_xy
      = 1_{y∈C2∪C3∪C4}.                         (1)

Here the term B_0y vanishes. Since row a has exactly two units left after B_a0=1, equation (1) proves that r and the two other endpoints p,q of a are distinct ordinary points in C2∪C3∪C4, all with unit weight:

    Ba = e0 + e_p + e_q.                          (2)

In particular B_ar=0. The vertex r is triangle-free by the triangle-pairing consequence and B_wr=1.

## 2. The C4 position reroots to D0 and is impossible

Suppose r∈C4. Its two common neighbors with w are then among W: none of 1,2,3 is adjacent to r. Root the same graph at w. The heavy mate 0 has parents {1,2,3}; the light mate r has two parents disjoint from that triple; also 0 is nonadjacent to r. Thus this is D0_MATCH.

The D0_MATCH component theorem forces the two light mates a and r of the heavy endpoints 0,w to satisfy B_ar=2. This contradicts B_ar=0 from (1). Consequently r∈C2∪C3. Interchanging labels 2 and 3, assume from now on

    r∈C2.                                        (3)

## 3. The two remaining unit rows at labels 2 and 3

Their remaining endpoints are ordinary vertices b,c:

    B2 = e1 + e3 + e_b,
    B3 = e1 + e2 + e_c.                           (4)

They cannot be in X by the fixed parent counts, cannot equal w because B_wX=0, and cannot equal a because B_aX=0. They are nonneighbors of 2,3 respectively since those labels are triangle-free. The (1,2) and (1,3) commutation entries also exclude b,c from C1.

For any ordinary y, commutation at (0,y) gives

    sum_{i∈X} B_iy = 2A_wy + A_ay.                (5)

Thus b,c each belong to W or to the ordinary neighborhood of a. The two sets are disjoint: w,a are a nonedge with B_wa=0 and already have the common neighbor 1, so they have no other common neighbor.

At (2,w) and (3,w), respectively, equations (3)-(4) give

    2 + A_bw = 2 + 1_{r∈C2} = 3,
    2 + A_cw = 2 + 1_{r∈C3} = 2.

Consequently

    b∈W,   c adjacent to a,   c not in W.         (6)

At (2,a), commutation now gives B_a,C2=0: its BA value is 1+A_ba=1, while its AB value is 1+B_a,C2. At (3,a) the corresponding values are 1+A_ca=2 and 1+B_a,C3. Using (1)-(2), this forces

    p∈C3,   q∈C4.                                (7)

## 4. The light mates a,r share exactly c

At (2,r), the BA value is A_br, whereas the AB value is

    B_wr + sum_{x∈C2} B_xr
      = 1 + sum_{x∈C2} B_xr.

Therefore

    r adjacent to b,   B_r,C2=0.                 (8)

The decisive short propagation is the (w,c) entry. Since c is an ordinary outside vertex,

    (BA)_wc = 2A_0c + A_rc = A_rc.

But w is adjacent to 3 and B_3c=1, so (AB)_wc≥1. Hence

    r adjacent to c.                             (9)

Both a and r are adjacent to c. They cannot be adjacent to each other, since a is triangle-free. Since B_ar=0, their common-neighbor equation now shows

    a not adjacent to r,   N(a)∩N(r)={c}.         (10)

Equation (5) at r gives B_X,r=0. Equation (1) gives B_r,C1=0. Finally, at (3,r), commutation and (9) give

    2 = 1 + B_r,C3,

so B_r,C3=1. Together with (8) and the row sum, this yields distinct unit endpoints s,t with

    Br = e_w + e_s + e_t,
    s∈C3,   t∈C4∪C5∪C6∪C7∪C8.                 (11)

There is no double entry at either light mate a or r. Also b≠c, and the two common neighbors of w,r are exactly {2,b}. Relative to root w, the heavy mate 0 therefore has parent triple {1,2,3} and the light mate r has parent pair {2,b}, with intersection one. Thus this reroot remains D1_MATCH.

## 5. The ordinary neighborhoods and the three deficient matchings

The six ordinary neighbors of a consist of exactly one point in each of C2,C3,C5,C6,C7,C8. Indeed, it has no ordinary neighbors in its parent classes C1,C4 because labels 1,4 are triangle-free. For each of the six other root labels, B_ai=0 requires a common neighbor, necessarily in that label's ordinary class, as w is not adjacent to a. There are exactly six available neighbors. Write

    N(a)\X = {u2,u3,A5,A6,A7,A8} =: U.

Equation (10) gives r≠u2. The common-neighbor identity for w,a gives W∩U=∅.

Commutation at (a,w), using their complete repeat rows, gives

    A_ar = A_pw + A_qw.

The left side is zero by (10); p∈C3 cannot be adjacent to w. Consequently q is not adjacent to w, so

    q≠W4.                                        (12)

Also p≠u3 because B_ap=1 while a is triangle-free. Finally c is in C5∪...∪C8: it is in U, cannot be u3 since B_3c>0 and 3 is triangle-free, and cannot be u2 since r∈C2 is adjacent to c whereas C2 is independent. The location b=W4 has **not** been excluded.

Put H=C1. Each x∈H has exactly one original neighbor in each C_j, j=2,...,8. First x is adjacent to neither w nor a because all three lie in the neighborhood of triangle-free label 1. Equation (5) gives B_X,x=0. The common-neighbor equation with each other root label j then supplies exactly one neighbor in C_j.

For y∈C2∪C3∪C4, its common neighbors with 1 lie among w,a,H, and B_1y=0. Therefore the edges from H into each of C2,C3,C4 are matchings covering all but the following points:

    actual matching: C2 misses u2; C3 misses u3; C4 misses W4.    (13)

Equation (1) shows that the total repeat weight from H into C2∪C3∪C4 is 18−3=15. This exhausts the row sum of the five points of H, so all their positive B entries stay in these three classes. Further, b and c have no original neighbors in H: each has exactly one common neighbor with label 1, already supplied by w or a. At (2,x) and (3,x), for x∈H, equations (4) therefore give

    B_x,C2=1,   B_x,C3=1.

The third unit must lie in C4. In combination with (1), these are also matchings:

    repeat matching: C2 misses r; C3 misses p; C4 misses q.      (14)

The omitted points in the actual and repeat matchings are different in all three classes, by (10), triangle-freeness of a, and (12).

There are also precise matching identities. Let x_r be the unique H-neighbor of r in G, and x_W the unique H-neighbor of W4 in B. At each x∈H, commutation at (w,x) gives

    A_rx = B_W4,x,

so x_r=x_W. Similarly, at (a,x),

    A_px + A_qx = B_u2,x + B_u3,x.                (15)

Thus the multisets of H-mates on the two sides agree. These identities retain multiplicity; they do not assert that their two terms have distinct mates.

## Remaining obligation

The constraints above do not yet force a second heavy edge in the B component of {0,w}, nor contradict a finite graph. In particular, one must not identify the actual matchings (13) with the repeat matchings (14), assume that every vertex is triangle-free, or treat the even number of original triangles as triangle-freeness. A valid completion could exclude this branch directly or prove that each component carrying these heavy edges has an even number of them; the latter would combine with the established odd parity of the total double-edge count.

## Additional transport constraints between C2 and C3

The following deductions sharpen the local interface without completing it.

First, b has exactly one neighbor in C2, namely r, and no neighbor in C3. The pair 2,b is a nonedge with B_2b=1, so it has exactly two common neighbors, already w and r. The pair 3,b is a nonedge with B_3b=0, so its unique common neighbor is already w. Conversely c has exactly one neighbor in C2, namely r, because c is nonadjacent to 2, has B_2c=0, and is adjacent to r. It has exactly two neighbors v1,v2 in C3: the pair 3,c is a nonedge with B_3c=1, and neither 0 nor w is adjacent to c.

For every ordinary y, commutation with rows 2 and 3 gives

    B_C2,y = 1_{y∈C1∪C3} + A_by − 1_{y=r},
    B_C3,y = 1_{y∈C1∪C2} + A_cy − 1_{y=r}.       (16)

Here B_Cj,y denotes sum_{x∈Cj} B_xy. The neighborhood facts just proved imply:

* The restriction of B to C2 has no positive entry.
* The restriction of B to C3 consists of precisely the single unit edge v1v2. Indeed, (16) says its only nonzero internal row sums are one at v1,v2.
* Between C2 and C3, every row on both sides has total B weight one. Thus those B entries form a perfect matching of the two six-point classes, with r matched to s.
* The original edges between C2 and C3 also form a perfect matching: the common-neighbor equation with label 3 for each C2 point, and with label 2 for each C3 point, gives exactly one cross-neighbor.

The two endpoints v1,v2 are different from u3 and from the unique original C3-neighbor of r. Otherwise the triangle-free vertex c would lie on a triangle with a or r, respectively. They have precisely the two common neighbors 3,c, since they are nonadjacent original vertices with B_v1,v2=1.

No equality between the original and repeat perfect matchings has been established. The single internal repeat edge in C3 has not yet been transported into a contradiction with the empty internal repeat graph in C2.
