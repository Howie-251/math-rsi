# Two construction case studies: an actionable HS obstruction and redesign

Date: 2026-10-11. Scope: construction of orders 58–61, maximum degree 8,
diameter at most 2. This note does not address n62 or Lean.

## Primary sources actually read

| Source | Reading and specific mechanism | Local originals |
| --- | --- | --- |
| Benjamin Przybocki, John Mackey, Marijn J. H. Heule, Bernardo Subercaseaux, *Doubly Saturated Ramsey Graphs: A Case Study in Computer-Assisted Mathematical Discovery*, arXiv preprint 2604.21187 | §1.2, §3. Small instances suggested a restricted circulant family; dedicated search supplied further instances; rewriting isomorphic distance sets exposed a uniform rule. Their construction is not a DD82 construction. | [PDF](../../../literature/dd82/arxiv_2604.21187.pdf), [extracted text](../../../literature/dd82/arxiv_2604.21187.txt) |
| Ryosuke Mizuno, *New lower bounds for the degree/diameter problem via interaction with a browser-accessible LLM*, arXiv preprint 2606.15860 | §2.2, §4, §5, Appendix A. A controller supplies routes and an independent affine chart makes each route cover a whole fiber. A stalled controller search was redesigned using a small voltage base. The concrete improvements concern (12,5) and (16,5). | [PDF](../../../literature/dd82/arxiv_2606.15860.pdf), [extracted text](../../../literature/dd82/arxiv_2606.15860.txt) |

Canonical sources: <https://arxiv.org/abs/2604.21187> and
<https://arxiv.org/abs/2606.15860>. Both original PDFs were downloaded, then
extracted with pypdf. The ARIS arXiv metadata helper returned an empty list for
the identifier query; the original PDFs and arXiv HTML were available directly.
No bibliographic absence is inferred from that helper result. The existing wiki
query pack was checked first; its paper list did not contain these two items.

The useful transfer is to make the remaining component obligation explicit,
then test whether it can exist. In the present HS proposal this produces a
complete mathematical obstruction, rather than a new random seed. The theorem
below is a derivation in this session, not a result asserted in either paper.

There is also an immediate limitation on transplanting Mizuno's construction:
an exact-NB-2 controller, with the paper's requirement on all ordered pairs,
cannot be a nonempty simple graph. A length-two closed walk from c to c is
necessarily c,u,c and immediately backtracks. Thus setting s=2 in that
proposition cannot solve our problem, regardless of the field or chart. A
diameter-two adaptation would need a different same-fiber coverage rule.

## Theorem: no order 58–61 target contains an induced HS graph

Let Q be the Hoffman–Singleton graph, with 50 vertices, degree 7, no triangles,
and exactly one common neighbor for every nonadjacent pair. There is no simple
graph G on 58, 59, 60, or 61 vertices with maximum degree at most 8, diameter at
most 2, and an induced subgraph isomorphic to Q.

In particular this rules out every proposed construction which preserves all
old HS adjacencies and nonadjacencies and attaches each old vertex to one new
vertex. It is a family exclusion, not a global exclusion of any target order.

### Reduction to a partition

Every such G is 8-regular: if a vertex had degree at most 7, its ball of radius
two would contain at most 1 + 7 + 7·7 = 57 vertices. Put k = |G| − 50 and let H
be the induced graph on its k new vertices. Every old vertex has exactly one
new neighbor, giving fibers F_a, a in V(H), of sizes

    s_a = 8 − d_H(a),              sum_a s_a = 50.

Empty fibers are allowed. Two distinct new vertices cannot share an old
neighbor, so H itself must have diameter at most two. In particular H is
connected, has maximum degree at most 8, and

    |E(H)| = 4k − 25.

For x in F_a and b != a with ab not an edge of H, the old–new pair (x,b) must
have an old intermediate neighbor in F_b. Thus the seven old neighbors of x
must meet each of the

    m_a = k − 1 − d_H(a) = k − 9 + s_a

mandatory fibers. There are only

    r_a = 7 − m_a = 16 − k − s_a

remaining neighbor slots. If F_a is nonempty, r_a >= 0; this also holds when
s_a=0. Therefore 0 <= s_a <= 16−k. Connectivity gives s_a <= 7 as well.

### A necessary collision inequality

Write q_x(b) = |N_Q(x) intersect F_b| and let I be the number of HS edges with
both endpoints in the same fiber. Since adjacent HS vertices have no common
neighbor and nonadjacent HS vertices have exactly one, double counting gives

    sum_x sum_b binom(q_x(b),2) = sum_a binom(s_a,2) − I.       (1)

For x in F_a, first reserve one neighbor in each mandatory fiber. Distributing
the r_a remaining neighbors creates at most binom(r_a+1,2) equal-color pairs:
concentrating them all on one occupied color maximizes this convex sum. If
there are no mandatory colors the stronger bound binom(r_a,2) applies, so the
stated bound remains valid. Also F_a itself is not mandatory, hence
q_x(a) <= r_a and 2I <= sum_a s_a r_a. Applying these bounds to (1) proves

    sum_a s_a(s_a−1) <= sum_a s_a r_a(r_a+2).                   (2)

Equivalently, with t = 16−k,

    0 <= sum_a f_k(s_a),
    f_k(s) = s[(t−s)(t+2−s) − (s−1)].                         (3)

No SAT result is needed for this inequality or the cases below.

### k = 8 (order 58)

H is connected with 8 vertices and 7 edges, so it is a tree. A tree of diameter
at most two is a star. Its fibers therefore have sizes 1,7,7,7,7,7,7,7. Here

    sum_a f_8(s_a) = 1·(7·9) + 7·7·(1·3−6) = −84,

contradicting (3). This excludes the proposed K_{1,7} controller.

### k = 9 (order 59)

First H must have a universal vertex. Suppose otherwise. A degree-one vertex
would force its neighbor to be universal because H has diameter two, so the
minimum degree is at least two. The degree sum is 22, so some vertex v has
degree two. Let its neighbors be u,w. Its two-ball has size at most
1+d_H(u)+d_H(w), hence their degree sum is at least 8. The other seven vertices
have degree at least two, so that sum is also at most 22−14=8. Equality implies
that every other vertex has degree exactly two.

If both d_H(u),d_H(w) >= 3, their sum is 8 and each is at most 5. Every one of
the other seven degree-two vertices must then be adjacent to both u and w:
using a degree-two neighbor would make its neighbor-degree sum at most 7.
This forces d_H(u),d_H(w) >= 7, a contradiction. Otherwise the degrees of u,w
are 2 and 6. All eight degree-two vertices must be adjacent to the unique
degree-six vertex, also impossible. Thus H has a universal vertex.

The universal vertex has degree 8 and hence an empty fiber. For every remaining
fiber, 0 <= s <= 7, and

    f_9(s) − (175−31s) = (s−5)^2(s−7) <= 0.

There are eight remaining fibers summing to 50. Consequently

    sum_a f_9(s_a) <= 8·175 − 31·50 = −150,

again contradicting (3).

### k = 10 (order 60)

Here 0 <= s <= 6. For every integer in this interval,

    f_10(s) − (120−25s) = (s−4)(s−5)(s−6) <= 0.

Thus sum_a f_10(s_a) <= 10·120−25·50 = −50. This excludes every possible
controller H, including the proposed Petersen controller (all fiber sizes 5).

### k = 11 (order 61)

Here 0 <= s <= 5, and

    f_11(s) − (80−20s) = (s−4)^2(s−5) <= 0.

Thus sum_a f_11(s_a) <= 11·80−20·50 = −120. This finishes all four orders.

## Concrete next design obligation

The obstruction identifies what has to change: a successful HS-based proposal
must modify old adjacencies. Merely changing H, repartitioning the same 50
vertices, adding symmetry breaking, or running the same partition model longer
cannot succeed at these orders.

One precise redesign is to delete old edges and spend the released degree on
additional old–new incidences. Let A' be the 50-by-50 adjacency matrix after
those deletions, B the 50-by-k old–new incidence matrix, and H the auxiliary
adjacency matrix. The complete, jointly realizable obligations are:

    A'1 + B1 = 8·1,                 H1 + B^T1 = 8·1;
    A' + (A')^2 + BB^T > 0          off diagonal;
    B + A'B + BH > 0                at every entry;
    H + H^2 + B^TB > 0              off diagonal.

These three coverage lines respectively handle old–old, old–new, and new–new
pairs. They must hold for the same A', B, H. Unlike the excluded construction,
B may have row sums above one, so B^TB can supply new–new coverage and H need
not have diameter two on its own.

If exactly e HS edges are deleted and no old edges added, then

    |E(old,new)| = 50 + 2e,          |E(H)| = 4k − 25 − e.

Each deleted old edge uv supplies a particularly restrictive finite design
obligation before any search: because Q has girth five, each of the 13 pairs

    {u,v},  {v,x} for x in N_Q(u)\{v},
             {u,y} for y in N_Q(v)\{u}

loses its only old path of length at most two. Under a deletion-only old graph,
each such pair must have intersecting rows of B. With only the edge uv deleted,
rows u,v have size two and the twelve neighbor rows have size one. Thus the
six neighbors of u other than v must choose their attachment from B_v, and
the six neighbors of v other than u from B_u, with B_u intersect B_v nonempty.
This is an explicit repair obligation, not an assurance that such a repair
exists. For multiple deletions the same intersection requirements remain
necessary, with possibly larger row sizes and additional lost paths.

A bounded next experiment can therefore choose a deletion pattern, propagate
these forced row intersections, and solve the remaining three coverage
conditions jointly. If it fails, preserve the actual conflicting port or
intersection constraints. Do not resume arbitrary partition search in the
family excluded above. Alternatively choose a different base that does not
retain an induced HS subgraph.

## Record for the parent/wiki owner

The primary literature reading is complete for the requested sections. The
new mathematical outcome is the four-order induced-HS obstruction above. It
has a self-contained counting proof and does not depend on metadata retrieval,
the papers' computational certificates, or a solver status. No graph with
more than 57 vertices was constructed by this subtask. No global target order
was excluded. Root owns wiki integration and any independent proof review.

## Addendum: deletion-only HS extensions to order 58

Independent short check requested by root later on 2026-10-11. Suppose exactly
t HS edges are deleted, no old–old edges are added, and eight new vertices are
introduced. Let D be the deleted-edge graph, r_v its degrees, and B_v the set
of new neighbors of old vertex v. Regularity gives |B_v|=1+r_v and

    m = |E(H)| = 7−t,                  0 <= t <= 7.

Every pair of new vertices must be covered by an H edge, a two-step H walk, or
a shared old neighbor. Consequently

    28 <= m + sum_a binom(d_H(a),2) + sum_v binom(1+r_v,2)
       <= m(m+1)/2 + 2t + binom(t,2)
        = 28 + t(t−6).                                      (4)

Here the number of pairs of incident edges in any simple graph with e edges
is at most binom(e,2), and
sum_v binom(1+r_v,2)=2t+sum_v binom(r_v,2). This establishes the stated bound
without requiring the deleted graph to be a forest. In particular t=1,...,5
are impossible; t=0 was already excluded above. Only t=6,7 remain in this
deletion-only order-58 family.

### t=6: the proposed normal form is forced

All inequalities in (4) are equalities. Thus every pair of deleted edges
intersects. A triangle-free simple graph with six pairwise intersecting edges
is a six-edge star. Let x be its center, l_1,...,l_6 its leaves, and w the
seventh, retained HS neighbor of x. There is exactly one H edge. The set B_x
has seven vertices; call it S, and call the eighth new vertex z. Each B_li has
two vertices, and all other old vertices have one new neighbor.

The center covers precisely the 21 pairs inside S. The six leaf pairs and
the unique H edge must cover the seven remaining pairs z–S, exactly once each.
After relabeling S={a_1,...,a_7}, therefore

    B_x = S,           B_li = {z,a_i} (i=1,...,6),
    E(H) = {{z,a_7}}.

There are 43 other old vertices. Their remaining attachment capacities are
one at z and six at each a_i. This agrees exactly with root's SAT normal
form. This conclusion is necessary; it does not assert that the remaining
43 assignments exist.

### t=7: only three deleted-edge shapes survive the pair count

Now H is empty. Put W(D)=sum_v binom(r_v,2). Equation (4), before its last
relaxation, gives

    28 <= 14 + W(D),                 W(D) >= 14.              (5)

The deleted graph must have maximum degree at least six. To prove this,
first if its maximum degree is at most three, binom(r_v,2)<=r_v, so W(D)<=14.
Equality would require every nonisolated vertex to have degree three, whereas
their degree sum is 14. Hence W(D)<14 in that case.

If its maximum degree d is four or five, choose a degree-d vertex x and let
R=D−x have 7−d edges. Because D is triangle-free, N_D(x) is independent, and
each edge of R contributes at most one to sum_{v in N_D(x)}d_R(v). Therefore

    W(D) = binom(d,2) + W(R) + sum_{v in N_D(x)}d_R(v)
         <= binom(d,2) + binom(7−d,2) + (7−d).

This is 12 for d=4 and 13 for d=5, again impossible. Since HS has degree
seven, d is six or seven. Up to isolated vertices, the remaining possibilities
are precisely:

| Deleted graph D | W(D) | Total available shared-old pair witnesses |
| --- | ---: | ---: |
| Seven-edge star K_{1,7} | 21 | 35 |
| Six-edge star and one disjoint edge | 15 | 29 |
| Six-edge star with an additional edge from one leaf to a new vertex | 16 | 30 |

Indeed for d=6 the seventh edge cannot touch the center and cannot join two
star leaves because that would create a triangle. It either touches exactly
one star leaf or neither. This is an elementary necessary shape reduction,
not an enumeration of embeddings or a solution of these three cases.

### Forced attachments useful for a subsequent bounded search

**Seven-edge star.** Its center has all eight new neighbors. The seven leaves
have two-element attachment sets L_i. Every two distinct old leaves lost their
unique old two-step path through the center, so the L_i are pairwise
intersecting. A pairwise intersecting family of two-element sets either has a
common element or is contained in the three edges of a triangle; repetitions
are allowed. Each leaf has six retained old neighbors, all with singleton
attachments. Their six attachment labels must be exactly the complement of
L_i in the eight new labels: with H empty these are the only six available
witnesses for those old–new pairs. This supplies a concrete starting design
obligation for each branch.

**Six-edge star plus disjoint edge uv.** The center x has seven new neighbors
S and misses z. The six star leaves and u,v supply eight two-element sets.
At least seven of these sets must contain z, and their partners must cover
all of S. In fact every star leaf's set contains z: otherwise the other seven
two-element sets would be the seven distinct z–S pairs, so the exceptional
leaf's two labels could not intersect all five other star-leaf sets, contrary
to the lost-path obligation. The retained old neighbor w of x must contain z
in B_w because H is empty and (x,z) needs a two-step path. The disjoint edge
may have w as an endpoint, so B_w need not be a singleton. Also B_u and B_v must intersect to
repair the deleted edge uv.

**Six-edge star with extra edge l_1u.** The center misses z as above; l_1 has
three new neighbors, the other five star leaves have two each, and u has two.
The triple B_l1 must contain z: otherwise the six two-element sets could cover
at most six of the seven z–S pairs. All five ordinary star-leaf pairs must
also contain z. If one did not, the other five pairs and the triple would have
to cover the seven z–S pairs exactly once, giving four distinct z-partners on
the other ordinary leaves; the exceptional two-element set could not intersect
all four. Their z-partners, together with the z-partner of B_u if it contains
z, must collectively cover S. The retained
HS neighbor w of x is not a deleted-edge endpoint (triangle-freeness excludes
w=u), so its singleton attachment is forced to z. Finally B_l1 and B_u must
intersect to repair l_1u.

These conditions retain the common realization requirement: the same old
attachments must satisfy every branch and all three coverage matrices. No
claim is made that any of these remaining cases is feasible.
