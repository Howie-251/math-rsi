# HS58 with two original deletions and three additions is impossible

Date: 2026-10-12. There is no maximum-degree-eight, diameter-two graph
obtained from HS50 by deleting exactly two original edges, adding exactly
three original nonedges among the old vertices, and adding eight new
vertices. This covers all placements of the edits, with no automorphism
or embedding classification. The proof is mathematical: the auxiliary
classification has an analytic proof, and no finite search result or
candidate graph is needed for the exclusion.

Together with [the addition budget](HS58_TWO_DELETE_ADDITION_BUDGET.md)
and [the two-addition exclusion](HS58_TWO_DELETE_TWO_ADDITIONS_EXCLUSION.md),
this proves that an extension with **exactly two HS deletions requires
at least four old-old additions**. No case with four or more additions
is considered here, and no arbitrary order-58 graph is excluded.

## Setup and the three auxiliary cases

Let Q be the Hoffman–Singleton graph. Let D be its two deleted edges,
A the three added nonedges, and M=Q-D+A the actual old graph. If B_x is
the new-neighbor set of old vertex x, regularity gives

\[
|B_x|=p_x=1+r_x-a_x,\qquad
r_x=d_D(x),\quad a_x=d_A(x),\qquad
\sum_xp_x=48.
\]

The eight new vertices induce a graph H with eight edges. Define K(H)
to have the new-vertex pairs whose H-distance exceeds two as its edges.
Each such pair requires a shared old neighbor. Only endpoints of D can
have more than one new neighbor, so K(H) is covered by four cliques
of order at most two when D is disjoint, or by cliques of orders at
most three, two, two when D is adjacent.

The analytic classification in
[HS58_TWO_DELETE_THREE_ADDITIONS_AUXILIARY_DOMAIN.md](HS58_TWO_DELETE_THREE_ADDITIONS_AUXILIARY_DOMAIN.md)
then leaves exactly the following three H types:

1. K1,7 with one edge between two leaves.
2. A triangle containing a degree-six hub, one pendant leaf at another
   triangle vertex, and four leaves at the hub.
3. A four-cycle containing a degree-six hub, with four leaves at the hub.

Type 1 is excluded for all edit placements by
[HS58_TWO_DELETE_THREE_ADDITIONS_UNIVERSAL_H.md](HS58_TWO_DELETE_THREE_ADDITIONS_UNIVERSAL_H.md).
That proof uses the unique old neighbor of the universal new vertex,
the existing seven-point domination lemma for Q minus one vertex, and
the port contradiction r_v+2<=z<=a_v<=r_v. Its coverage bound explicitly
includes the one additional route supplied by the extra leaf edge.

It remains to exclude types 2 and 3. In both, K(H) is exactly a K1,4.
Write u for its center and L={a,b,c,d} for its four leaves. These four
vertices are also degree-one vertices of H with the same H neighbor,
the degree-six hub h. In particular,

\[
N_H(u)\cap L=\varnothing,\qquad
N_H(q)\cap L=\varnothing\quad(q\in L).                \tag{1}
\]

Thus a new attachment to u or to one of these four leaves cannot
reach any other member of L in one further H step. The statements
are about both explicit auxiliary types, not merely their bad-pair
counts.

## Saturated pair coverage fixes the endpoint ports

For disjoint D, each endpoint has at most two ports and can cover at
most one edge of K1,4. All four endpoints must therefore have two
ports, contain u, and supply the four distinct leaves of L bijectively.

For adjacent D, the shared endpoint has at most three ports and can
cover at most two edges of K1,4. The other two endpoints each cover
at most one. Covering all four edges forces all three maxima: the
shared endpoint contains u and two leaves of L; the other endpoints
contain u and one of the two remaining leaves each.

In either case every deletion endpoint has its full possible port
size 1+r_x, so a_x=0 there. Outside these endpoints r_x=0, and
p_x=1-a_x>=0 forces a_x<=1. Consequently **A is a three-edge matching
avoiding every endpoint of D**. Its six endpoints have zero ports;
every other old vertex outside D has exactly one port and no added
incident edge.

This is an equality consequence of covering all four bad new pairs.
It is not an additional restriction imposed on the candidate domain.

## A retained neighbor with one port must repair a specific old pair

We will use the following consequence of the actual edited old graph.
Suppose xy is a deleted edge and t is a retained Q neighbor of x,
outside the endpoints of D, with p_t>0. Then t has one port and no
incident edge of A, while y also has no incident edge of A by saturation.

Because Q has no triangle, t and y are nonadjacent in Q. Their unique
common Q neighbor is x. Deleting xy destroys their unique Q path of
length at most two. No added edge can restore a one- or two-step old
path: every edge on such a path is incident to at least one of its
endpoints t,y, and neither endpoint has an incident added edge.
Thus the actual graph M still does not cover this old pair within
two steps. It must instead be repaired by a common new neighbor:

\[
B_t\cap B_y\ne\varnothing.
\]

Since B_t is a singleton, this says

\[
B_t\subseteq B_y.                                   \tag{2}
\]

Zero-port retained neighbors contribute no new labels and need not
be classified for the argument. In particular, we do not assume that
deletion-only old-pair requirements remain valid when either old
endpoint has an added edge; (2) is used only after both endpoints
have been proved untouched by A.

## Adjacent deletions miss two required new leaves

Let D={xy,xz}. The forced port pattern, after naming the four bad leaves,
is

\[
B_x=\{u,a,b\},\qquad B_y=\{u,c\},\qquad B_z=\{u,d\}.
\]

The old neighbors of x in M are exactly its five retained Q neighbors;
x has no additions, and both deleted neighbors y,z are absent. Each
retained neighbor t lies outside the endpoints of D. If it has a
positive port, applying (2) to both xy and xz yields

\[
B_t\subseteq B_y\cap B_z=\{u\}.
\]

Zero-port neighbors contribute nothing. Hence routes from x through
an old intermediate can reach no label of L. Direct attachments reach
only a,b from L. By (1), H-mediated routes from B_x reach no further
label of L. Therefore x cannot reach c or d within two steps. This
excludes adjacent D in both remaining auxiliary types.

## Disjoint deletions miss at least one required new leaf

Let D={xy,zw}. The forced port pattern is

\[
B_x=\{u,a\},\quad B_y=\{u,b\},\quad
B_z=\{u,c\},\quad B_w=\{u,d\}.
\]

Again x has no added old edge, so its old neighbors are exactly its
retained Q neighbors. For each such neighbor t outside the deletion
endpoints, either it has zero ports or (2) gives
B_t subseteq {u,b}. Thus these neighbors supply at most the bad leaf b.

Of the other deleted edge's endpoints z,w, at most one is a Q neighbor
of x: adjacency to both would form a triangle with the original HS
edge zw. These possible retained endpoint neighbors therefore supply
at most one of c,d. The deleted neighbor y is not adjacent to x in M,
and x's direct ports supply only a from L. By (1), the H routes from
{u,a} supply no further member of L.

Consequently x reaches at most three of the four required bad leaves:
a, possibly b, and at most one of c,d. At least one of c,d is farther
than two steps from x. This excludes disjoint D in both remaining
auxiliary types.

## Scope and evidence boundary

Two distinct deleted HS edges are either adjacent or disjoint, so the
two arguments above close types 2 and 3 without classifying their old
embeddings. The separate universal-vertex proof closes type 1, and the
analytic auxiliary classification covers every H. This proves the
stated full two-deletion/three-addition exclusion.

The earlier auxiliary screen's 2,688 labeled survivors for each port
budget remain unchanged as raw necessary-domain counts: 168 of type 1,
1,680 of type 2, and 840 of type 3. Their later exclusion is mathematical
and is not retroactively recorded as a different screen output.

The separately generated fixed-core full graphs and their BFS failures
are illustrative construction attempts, not dependencies of this proof.
Their planned CNF/SAT runs were cancelled before launch. No new solver,
enumeration, or graph optimization was used for the integrated theorem,
and no four-addition research is part of this note.

C16 read the complete classification, universal case and integrated
proof, accepting the stated scope. Root independently checked these
files and all retained-neighbor routes. Raw response and disposition:
reviews/dd82/20261012_C16_*.
