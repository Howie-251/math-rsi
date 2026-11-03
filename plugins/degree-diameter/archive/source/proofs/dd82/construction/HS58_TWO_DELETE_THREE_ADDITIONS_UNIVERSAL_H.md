# HS58: two deletions, three additions, and a universal auxiliary vertex

Date: 2026-10-12. This pure mathematical argument excludes the branch
with exactly two original HS edges deleted, exactly three original
nonedges added among the old vertices, and a universal vertex in the
eight-vertex auxiliary graph. It uses no enumeration or graph search.
It does not by itself address auxiliary graphs without a universal
vertex.

## The exact auxiliary and port structure

Write Q for HS50, D for its two deleted edges, A for the three added
nonedges, and M=Q-D+A for the actual old graph. Put r_x=d_D(x),
a_x=d_A(x), and p_x=1+r_x-a_x. Any hypothetical order-58,
maximum-degree-eight, diameter-two graph is eight-regular, so p_x is
its old-new degree and

\[
\sum_xp_x=50+4-6=48,\qquad |E(H)|=8.
\]

If H has a universal vertex c, its seven incident edges leave exactly
one further edge. Thus H is K1,7 with one extra edge between two of
the leaves. Call those two leaves special and the other five ordinary.
The ordinary leaves each have seven old neighbors; the special leaves
have six each. Vertex c has exactly one old neighbor, denoted v.

Let L_x be the set of the seven new leaf labels attached to old x.
Then |L_x|=p_x-[x=v]. In particular, p_v>=1 and

\[
a_v\le r_v.                                           \tag{1}
\]

If p_x=0, x cannot reach c through a new intermediate vertex. Its only
possible two-step route to c is x-v-c, so xv must be an edge of M.

## Some ordinary leaf avoids all addition endpoints and v

Let W be the endpoint set of A. We have |W|<=6 and sum_(x in W)a_x=6.
The number of distinct leaf labels touching W union {v} is at most
their total incidence count there. If v is outside W, this count is

\[
|W|-6+\sum_{x\in W}r_x+r_v\le |W|-2\le4.
\]

If v belongs to W, it is

\[
|W|-7+\sum_{x\in W}r_x\le |W|-3\le3.
\]

There are five ordinary leaf labels, so at least one of them, say l,
has a seven-point old neighbor set S avoiding both W and v.

For each old vertex other than v, reaching this ordinary leaf requires
being in S or having an M neighbor in S. Thus S closed-dominates M-v.
No added edge touches S, so S also closed-dominates Q-v. The existing
[seven-point domination lemma](HS59_SPARSE_AUXILIARY_REMAINDER.md)
gives exactly two possibilities:

\[
S=N_Q(v),\qquad\text{or}\qquad
S=N_Q(x)\text{ with }\operatorname{dist}_Q(x,v)=2.      \tag{2}
\]

## The distance-two option still cannot cover seven leaves

Suppose S=N_Q(x) in the second case of (2). Every retained Q neighbor
of x carries l and is outside W, hence has at most r_y additional
leaf labels. The set N_Q(x) is independent. Each deleted edge not
incident to x has at most one endpoint there, while the r_x deleted
edges incident to x contribute no retained neighbor. Consequently

\[
\left|\bigcup_{y\in N_{Q-D}(x)}L_y\right|
 \le1+\sum_{y\in N_{Q-D}(x)}r_y\le3-r_x.
\]

Direct leaf attachments at x contribute at most 1+r_x-a_x labels.
Every added neighbor y has a_y>=1, so its leaf count is at most
p_y<=r_y. Direct and old-intermediate routes therefore reach at most

\[
4-a_x+\sum_{y\in N_A(x)}r_y                         \tag{3}
\]

leaf labels. For a_x=0,1,2,3, this is at most 4,5,5,5 respectively:
a single vertex has deleted degree at most two, two distinct vertices
have combined deleted degree at most three, and the entire deleted
degree sum is four.

Here the extra edge in H must also be counted. Since x is not v, it
does not attach to c. Its H-mediated routes can add at most one leaf
outside L_x, namely the partner of a special leaf it carries. Hence
even after this extra contribution, x reaches at most six of the
seven leaf labels. This contradicts diameter two.

The second option in (2) is impossible. We have proved

\[
S=N_Q(v),\qquad N_Q(v)\cap W=\varnothing.              \tag{4}
\]

## Zero ports force the final contradiction

Let z be the number of old vertices with p_x=0 and define the total
positive excess above one port by

\[
E=\sum_x\max(p_x-1,0).
\]

Because every p_x is a nonnegative integer and their sum is 48,

\[
E-z=48-50=-2,\qquad z=E+2.                          \tag{5}
\]

By (4), every s in N_Q(v) has a_s=0 and p_s=1+r_s. Therefore

\[
E\ge\sum_{s\in N_Q(v)}r_s\ge r_v.                  \tag{6}
\]

All these neighbors have positive ports, and v has the center port,
so a zero-port old vertex lies outside N_Q(v) union {v}. Nevertheless
it must be adjacent to v in M to reach c. Such an adjacency cannot be
an original HS edge; it must be one of the a_v added edges incident
to v. Thus z<=a_v. Combining this fact with (1), (5), and (6) yields

\[
r_v+2\le E+2=z\le a_v\le r_v,
\]

the required contradiction. No endpoint-pattern enumeration is needed.

For completeness, (4) and domination also imply that no deleted edge
can join N_Q(v) to a distance-two vertex: that vertex would lose its
unique neighbor in S, and no added edge touches S. Thus the proposed
deleted-edge restriction to v-S and distance-two-to-distance-two edges
is valid, but the port contradiction above closes the branch without
using that further restriction.

This result covers every embedding of the two deletions and three
additions when H has a universal vertex. Any extension to other H
shapes requires a separate argument or finite classification; none is
claimed here.
