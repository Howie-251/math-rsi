# Global five-cycle and route budgets for the girth-five GQ80 family

Verdict: the proposed global identities are **VALID**, but this analysis does **not** establish a global overlap lower bound exceeding the available budget. The girth-five family remains open unless the separate producer supplies a complete witness or a separately justified exclusion. This paper task runs no solver, graph generation, BFS, matching enumeration or numerical experiment.

The inherited model is the incidence graph of W(3,3), with40 points,40 lines and160 incidence edges, plus noncollinear point perfect matching P and nonintersecting line perfect matching Q. Mixed four-cycles are prohibited. These are exactly the girth-at-least-five restrictions in ../girth5_cnf_20261028/ANALYSIS_GIRTH_SCOPE.md. No commuting-adjacency, automorphism or matching symmetry is assumed.

## 1. The a sums and the exact number of five-cycles

Let C(x) be the13-point closed collinearity set of a point x and let Sx=C(x) minus{x}. Define a_x as the number of P edges having both endpoints in Sx. A selected noncollinear point edge has exactly four common collinear roots in W(3,3). It therefore contributes one to a_x at exactly four roots. There are20 selected point edges, so

    sum over the40 point roots of a_x =20*4=80.

The dual identity holds for line roots and Q. Thus the average a is2 on each side. This is an identity for noncollinear/nonintersecting matchings, not a fresh diameter obstruction.

A simple five-cycle must contain an odd number of internal matching edges. It cannot contain three matching edges and two incidence edges: a simple cycle cannot have two consecutive matching edges, since each vertex has only its unique matching mate. Three matching edges cannot be separated cyclically by only two incidence edges. Five matching edges alone are also impossible. Thus every five-cycle contains exactly one matching edge and four source incidence edges.

Every selected noncollinear P edge closes exactly four source length-four geodesics, one through each common collinear root. This gives80 five-cycles containing a P edge. Every Q edge gives four dual cycles, another80. Hence

    total number of five-cycles =160.

For a fixed point root x, cycles in which x is an endpoint of its own P edge number4. Cycles in which x is the middle point of a four-incidence path around another P edge number a_x. Cycles whose matching edge is on the line side number4: for each of the four lines L through x, Q(L) is disjoint from L, and the GQ point-line axiom gives exactly one length-four incidence path from L to Q(L) containing x. No such cycle is counted twice because the two Q-matched lines cannot both contain x. Therefore

    five_cycles_through(x)=8+a_x.

The dual formula holds for each line root. These counts agree globally: each side has400 vertex-cycle incidences and all80 vertices have800=5*160. Again, the average10 five-cycles per vertex is a consistency identity, not a new contradiction.

## 2. Exact route families and an explicit excess decomposition

Fix x on the point side and its mate y=P(x). Among the27 original noncollinear points, y is already adjacent to x. The remaining target set is

    T_x = points minus(C(x) union{y}),  |T_x|=26.

All routes of length at most3 to T_x have exactly one matching edge and two incidence edges. They are precisely these three types:

* Matching first: A_x=C(y) minus(C(x) union{y}), with exactly8 distinct endpoints.
* Matching last: B_x=P(Sx) minus C(x), with exactly12-2a_x distinct endpoints. The2a_x images remaining in Sx come from internal P edges. Neither x nor y can be an image here, since x and y are matched to one another.
* Opposite matching in the middle: for each L through x use Q(L). It has exactly three points noncollinear with x. None is y, because that would produce a prohibited mixed four-cycle with the edge xy. Thus there are exactly12 such routes as a multiset R_x. Their endpoints need not be distinct across the four matched lines.

Let Rbar_x be the support of that relay multiset. Define three nonnegative integers

    b_x = |A_x intersection B_x|,
    d_x =12-|Rbar_x|,
    c_x = |Rbar_x intersection(A_x union B_x)|.

Then b_x is overlap between the two own-side families, d_x counts repeated relay endpoints, and c_x counts relay endpoints already covered by either own-side family. Triple intersections are correctly counted: b_x and c_x each contribute one, as required for three routes to a single endpoint. More than one relay to that endpoint contributes through d_x.

The number of route occurrences is32-2a_x and their endpoint union has size

    |A_x union B_x union Rbar_x|=32-2a_x-(b_x+c_x+d_x).

Writing delta_x=26 minus this union size, the exact relation is

    E_x := b_x+c_x+d_x =6-2a_x+delta_x.

Thus complete same-side D3 coverage is equivalent to delta_x=0, or

    E_x=6-2a_x.

In particular a_x<=3 is necessary. It does not guarantee coverage. Summing the exact formula over one40-root side and using sum a_x=80 gives

    sum E_x =80 + sum delta_x.

A diameter-three completion has exactly80 ordered repeat excess on each side, not merely a bound inferred from averages. Failure pairs reverse, so sum delta_x is even. A proof of sum E_x>=82 on either side would exclude the family. No such stronger inequality has been proved here; rewriting it as a deficit identity alone does not prove a deficit exists.

## 3. Avoid rediscovering an existing overlap cut

The weaker P-only consequence is

    2a_x+b_x<=6.

It is not new. Put Z_xy=points minus(C(x) union C(y)), the18-point set in the earlier mate-conditioned overlap proof. Once P(x)=y,

    |P(C(x)) intersection Z_xy|=12-2a_x-b_x.

Therefore 2a_x+b_x<=6 is exactly the previous requirement that this number be at least6. It is a rewriting of the saved3120 overlap cuts. The unconditional a_x<=3 constraint follows by dropping b_x>=0. This paper does not count that rewriting as a new constraint or new method.

What remains coupled between P and Q is the need to achieve

    d_x+c_x=6-2a_x-b_x

at every point and line root simultaneously, under the involution equations and all mixed-rectangle prohibitions. The first two terms are constrained by the actual concurrency and intersections of the four Q-images of the pencil through x; the separate a average supplies no lower bound that forces an excess.

## 4. Concrete unresolved question and stopping decision

At a root with a_x=3, full coverage requires b_x=c_x=d_x=0. Thus its8 own-first endpoints,6 own-last endpoints and12 relay endpoints must form an exact disjoint partition of all26 targets. Once P is chosen, the first two pieces are fixed; the four Q-image lines must have12 distinct far endpoints, all outside that fixed14-point union. A forced overlap at even one such root kills that completion. This is a precise local route-complementarity question to test if a later controlled construction has an actual reason to focus there. It is not a complete exclusion strategy, because the average2 does not force any a_x=3 root.

More generally a putative D3 completion has520 unordered nonmate far pairs on each side and560 unordered route occurrences. Only40 extra occurrences are available; at least480 pairs per side would have exactly one length-three route. This is another conditional consequence of the same budget, not an independent obstruction.

The numerical profile a_x=2 and E_x=2 for every root is consistent with all the displayed scalar sums and with ten five-cycles per vertex. This is only an arithmetic budget profile, not an actual graph or matching counterexample. It demonstrates why the validated counts alone do not give the desired contradiction: an additional geometric or involution-compatibility argument must rule out simultaneous equality. No such argument is supplied here.

The next mathematical target, if later justified, is a forced lower bound on the Q-relay collision term after the own-side matching is fixed, rather than another average, five-cycle recount, or unrestricted seed scan. This task ends at that exact gap and does not request another solver or numerical experiment.
