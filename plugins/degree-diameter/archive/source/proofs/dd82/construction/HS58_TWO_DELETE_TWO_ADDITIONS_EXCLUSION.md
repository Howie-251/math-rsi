# HS58 with two original deletions and two additions is impossible

Date: 2026-10-12. Pure mathematical family exclusion. There is no
maximum-degree-eight, diameter-two graph obtained from HS50 by deleting
exactly two original edges, adding exactly two original nonedges among
the old vertices, and adding eight new vertices. No enumeration,
automorphism reduction, solver, or graph search is used.

Combined with [the addition budget](HS58_TWO_DELETE_ADDITION_BUDGET.md),
this means a construction with exactly two HS deletions would require
**at least three old-old additions**. Cases with three or more additions
are not addressed here.

## Setup and the unique center attachment

Let Q be the Hoffman–Singleton graph, D the two deleted edges, A the two
added nonedges, and M=Q-D+A the actual old graph. Put

\[
r_x=d_D(x),\qquad a_x=d_A(x),\qquad
p_x=1+r_x-a_x.
\]

Regularity forces p_x to be the number of new neighbors of x. Thus
p_x>=0 and sum_x r_x=sum_x a_x=4. The preceding budget proof forces
the graph on the eight new vertices to be K1,7. Let c be its center.
Its old degree is one, so write v for its unique old neighbor. Each new
leaf has seven old neighbors. Let L_x be the set of new leaves attached
to old vertex x. Then

\[
|L_x|=p_x-[x=v].                                      \tag{1}
\]

For each old x other than v, every new leaf must be in

\[
L_x\ \cup\ \bigcup_{y\in N_M(x)}L_y.                 \tag{2}
\]

Indeed, x has no edge to c, and an H path from an attached new leaf
cannot reach a different leaf in one further step. Only v can use c
as the intermediate vertex to reach every leaf.

In particular, if p_x=0 then the pair (x,c) requires xv in E(M). This
zero-port condition is necessary but the stronger argument below does
not require enumerating its possible endpoint patterns.

## At least three leaves avoid all addition endpoints and v

Let W be the set of endpoints of the two added edges. Thus |W|<=4,
sum_(x in W) a_x=4, and a_x=0 outside W. Call a new leaf good if its
seven old neighbors avoid W union {v}.

The number of leaves that are not good is at most the total number of
leaf incidences on W union {v}. If v is outside W, (1) gives

\[
\sum_{x\in W}|L_x|+|L_v|
=|W|-4+\sum_{x\in W}r_x+r_v\le |W|\le4.             \tag{3}
\]

If v is in W, the corresponding total is

\[
\sum_{x\in W}|L_x|
=|W|-5+\sum_{x\in W}r_x\le |W|-1\le3.               \tag{4}
\]

Multiple occurrences of the same leaf only decrease the number of
distinct affected labels. Since there are seven leaves, at least three
are good.

## Apply the existing seven-point domination lemma

Fix a good leaf l and let S be its seven old neighbors. By (2), S
closed-dominates M-v: each old vertex other than v is either in S or
has an M neighbor in S. Since S avoids W, no added edge has an endpoint
in S. Consequently this domination also holds in Q-v. Moreover v is
not in S.

The seven-point domination lemma in
[HS59_SPARSE_AUXILIARY_REMAINDER.md, section 2](HS59_SPARSE_AUXILIARY_REMAINDER.md)
therefore applies exactly as stated. It says that a seven-element
subset of Q-v closed-dominating Q-v is either

\[
S=N_Q(v),\qquad\text{or}\qquad
S=N_Q(x)\text{ for an }x\text{ at Q-distance two from }v. \tag{5}
\]

This lemma uses only the HS girth-five and unique-common-neighbor
properties; no assertion about the altered old graph is substituted
for its Q-v hypothesis.

## A distance-two neighborhood cannot supply a good leaf

Suppose S=N_Q(x), where dist_Q(x,v)=2. In particular x is not v, so
(2) must supply all seven leaf labels at x. Every retained Q neighbor
of x belongs to S, carries l, and lies outside W. Its port number is
therefore 1+r_y. Since N_Q(x) is independent, each deleted edge not
incident to x has at most one endpoint in N_Q(x). The r_x deleted
edges incident to x have their opposite endpoints removed from the
retained-neighbor set. Hence

\[
\sum_{y\in N_{Q-D}(x)}r_y\le2-r_x.
\]

The retained Q neighbors all share the same leaf l, so their union of
leaf labels has size at most

\[
1+\sum_{y\in N_{Q-D}(x)}r_y\le3-r_x.                 \tag{6}
\]

Direct attachments at x contribute at most p_x=1+r_x-a_x leaves.
Every added neighbor y has a_y>=1, so it contributes at most
p_y=1+r_y-a_y<=r_y leaves. Combining these bounds, the union in (2)
has size at most

\[
4-a_x+\sum_{y\in N_A(x)}r_y.                        \tag{7}
\]

There are only two added edges. If a_x=0, (7) is at most four. If
a_x=1, its one added neighbor has r_y<=2, giving at most five. If
a_x=2, the two added neighbors are distinct, and their combined
deleted degree is at most three: two distinct vertices cannot both
have degree two in a simple graph with only two edges. Again (7) is
at most five. All cases fall short of seven.

Thus the second option in (5) is impossible. **Every good leaf has
old neighborhood exactly N_Q(v).**

## The remaining port count contradicts three good leaves

At least three distinct good leaves now attach to every one of the
seven vertices in N_Q(v), requiring at least 21 leaf incidences there.
But N_Q(v) is independent, so the two deleted edges supply at most
two deleted-degree incidences in this set. Consequently

\[
\sum_{y\in N_Q(v)}|L_y|
=\sum_{y\in N_Q(v)}p_y
\le7+\sum_{y\in N_Q(v)}r_y\le9,
\]

contradicting 21<=9. This proves the claimed two-deletion/two-addition
exclusion for every actual placement of the four edited edges.

The proof uses old-new coverage and exact port counts. It does not
impose deletion-only old-pair intersection constraints after additions
have potentially restored those paths. No remaining construction
domain survives at this precise edit budget.

Root and C15 read the full proof, the preceding budget, and the imported
domination lemma. C15 accepted the stated scope; raw response and root
disposition are saved in reviews/dd82/20261012_C15_*.
