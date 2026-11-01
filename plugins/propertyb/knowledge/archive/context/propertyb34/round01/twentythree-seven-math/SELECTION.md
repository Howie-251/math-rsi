# 23 vertices, minimum degree seven: six-point selection

Status: exact selection lemma; probability classification and global realization remain candidates under review. H has 23 vertices, 34 five-element edges, and covers every pair. Let L be its r >= 14 vertices of degree seven. Write w(x,y)=lambda(x,y)-1 >= 0. For each x in L, the sum over all other vertices is exactly 6, hence its sum over L is at most 6. The previously verified strong-codegree branch handles lambda >= 4 between vertices of L.

Choose a six-element S subset L minimizing W=sum_{pairs in S}w. Put d_S(x)=sum_{z in S-x}w(x,z). For y in L-S, swapping x for y cannot decrease W, so

    d_S(y) >= d_S(x) + w(x,y).

Let b be the sum of weights from S to L-S. Summing this inequality over y gives

    (r-6) d_S(x) + sum_{y outside S} w(x,y) <= b.

The five other vertices of S each have total weighted degree at most 6 in L, while x has total degree d_S(x)+sum_outside w(x,y). Thus

    b <= 30 + d_S(x) + sum_outside w(x,y) - 2W.

Cancel to obtain the exact selection inequality

    (r-7) d_S(x) + 2W <= 30.             (1)

Averaging W over all six-subsets also gives W <= floor(90/(r-1)), hence W<=6. Since W >= d_S(x) and r>=14, (1) forces d_S(x)<=3. If some degree equals 3, it forces W<=4. Therefore every H selects either six points of maximum internal weighted degree at most 2, or six points of maximum degree 3 and total weight at most 4.

This selection has no three-color class-size restriction. It is stronger than the earlier route that only guaranteed six points when r>=16.

## Equality candidate, W=6 and maximum degree 2

All six internal degrees equal 2. Every y in L-S must have d_S(y)>=3: otherwise the swap inequality gives d_S(y)>=2, but any positive incident weight raises the lower bound to at least 3. Since the cut has total weight at most 36-12=24, r<=14. Thus r=14, all eight outside low-degree vertices have d_S(y)=3, each of the six selected vertices has total low-degree weighted degree 6, and no weight from S to a high-degree vertex is positive. Each positive weight from S to an outside low-degree vertex is 1.

For any positive cut edge xy, swapping x for y preserves W=6. The replacement set is still a global W-minimizer. By (1), every vertex of the replacement set has internal degree at most2, hence exactly2. If z is another S-neighbor of y, its new internal degree is 2-w(x,z)+1=2, so w(x,z)=1. Consequently the three S-neighbors of every outside low-degree vertex form an ordinary triangle.

Every selected vertex has four cut neighbors. Therefore S consists of two disjoint ordinary triangles A,B; the eight outside vertices split into Y_A,Y_B of size4 according to their S-neighborhood. Let y,z be distinct members of Y_A. Swap a in A with y. Relative to the new minimizing set S', the vertex z is still outside and has positive weight to both vertices of A-a. Its three S'-neighbors must form a triangle, hence its third neighbor is y and w(y,z)=1. This holds for every y,z in Y_A, and similarly Y_B. Thus A union Y_A and B union Y_B are two disjoint ordinary K7 components in the weighted nonunit graph. All14 vertices have weighted degree6 within these components, saturating the global budget, so every remaining pair involving one of these14 vertices has lambda1. In particular all pairs from the14 degree7 points to the9 degree8 points have lambda1.

This is a complete graph-theoretic equality reduction, not yet an exclusion of this possible pair-codegree pattern by the hypergraph probability argument.

## Numerical classification so far

Six internal weighted degrees <=2: the complete extension generator found 725 trace orbits after pruning already-strict five-point projections. 530 have a strict pure-quota bound. The first 120-layout-order joint run adds 84, leaving111. Their weighted graphs are exclusively: 2K2+2K1 (11), K3+3K1 (6), K3+K2+K1 (48), 3K2 (29), and 2K3 (17). All weights shown are1. The full720-order refinement adds33 strict certificates and leaves78 profiles; the five graph shapes are unchanged. Independent exact replay has passed all1478 retained pure certificates (including the209 equality extensions) and all175 retained joint certificates. The separate max-degree3/W<=4 branch has9 weighted graph shapes,66 surviving trace profiles, all strict with maximum4809/4862; its independent replay also passed. See SIX_DEGREE_TWO_CANON.json and SIX_RESIDUES.json.
