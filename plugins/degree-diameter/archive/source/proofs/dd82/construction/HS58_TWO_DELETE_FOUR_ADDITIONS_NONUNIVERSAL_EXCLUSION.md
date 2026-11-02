# HS58: all nine nonuniversal auxiliary types at two deletions and four additions

Date: 2026-10-12. All nine nonuniversal H types in the completed
[four-addition auxiliary domain](HS58_TWO_DELETE_FOUR_ADDITIONS_AUXILIARY_DOMAIN.md)
are impossible for every placement of the old edits. This note proves
the nine type exclusions mathematically. Completeness of the list of
nine types is the separate finite auxiliary classification; no SAT
result or fixed old-core experiment is needed for the arguments here.
The two universal types 1 and 6 are outside this note's conclusion.

Let Q be HS50, D its two deleted edges, A four added original nonedges,
and M=Q-D+A. Put r_x=d_D(x), a_x=d_A(x), and let B_x be the new-neighbor
set of old x. Regularity gives |B_x|=1+r_x-a_x>=0. The auxiliary H has
eight vertices and nine edges. Every vertex outside the endpoints of
D has either one port and no added incident edge, or zero ports and
one added incident edge. More than one addition at such a vertex is
impossible.

The exact representatives and labels used below are those in
[enumeration.json](../../../computations/dd82/construction/hs58_two_delete_four_add_auxiliary_run/enumeration.json).
Their bad-pair graphs K(H), consisting of the new pairs at H-distance
greater than two, have the following forms:

| Type IDs | K(H) | Additional geometry used |
| --- | --- | --- |
| 5,7 | K1,4 | Its four leaves are independent in H. |
| 9,10 | K1,4 | H has exactly one edge among its four leaves. |
| 4,11 | C4 | The bad-pair support and its H-neighbors are recorded below. |
| 2,3,8 | K1,3 | Its three leaves have degree one in H and share one H hub. |

## Two reusable old-core facts

**Retained positive neighbor.** If xy is deleted, x and y have no
incident added edges, and t is a retained Q neighbor of x outside
the deletion endpoints with positive port, then

\[
B_t\subseteq B_y.                                      \tag{1}
\]

Indeed, t has a singleton port and no added edge. Its unique Q path
of length at most two to y is t-x-y, destroyed by deleting xy. Neither
t nor y meets A, so no added edge can occur in a replacement old path
of length one or two. They need a common new neighbor, giving (1).
The same conclusion holds when x does meet A: the argument needs
only that the outer endpoints t,y do not meet A.

**Adjacent deletions with all endpoint ports maximal.** If D={xy,xz}
and A is a nonempty matching avoiding x,y,z, no completion exists,
regardless of H. Write Z for the endpoints of A, all of which have
zero ports. A vertex q in Z adjacent in Q to x loses its unique old
two-step paths to both y and z. Its only added neighbor q' must be a
Q neighbor of both y and z to repair them. Their unique Q common
neighbor is x, which is not in Z: contradiction. Thus Z avoids N_Q(x).

If q in Z is a Q neighbor of y, the lost pair q-x requires q's added
partner to be a Q neighbor of x, contradicting that same conclusion.
The argument is identical for z. Hence no vertex of Z has a Q neighbor
among x,y,z. Now choose any q in Z. Its old neighbors are its seven Q
neighbors and its added partner. The latter has zero ports; the seven
Q neighbors lie outside the deletion endpoints and each have at most
one port. Therefore q reaches at most seven new vertices in two steps.
It needs eight and has no direct new edge. This proves the fact.

When all deletion endpoints have their maximal ports 1+r_x, the added
edges automatically form just such a matching outside them. Thus this
fact applies to every saturated adjacent-deletion case below.

## Four bad-star types: 5,7,9,10

Write u for the center of K1,4 and L={a,b,c,d} for its four leaves.
Four bad-star edges force all deletion-endpoint port capacities to be
maximal, by the same elementary clique count used at three additions:
four K2 cliques must each contribute one edge, or one K3 must
contribute two edges and two K2 cliques one each. All endpoint ports
contain u. A is therefore a matching avoiding the deletion endpoints.
Adjacent D is already impossible by the preceding old-core fact.

For disjoint D={xy,zw}, the endpoint ports, after naming L, are

\[
B_x=\{u,a\},\quad B_y=\{u,b\},\quad
B_z=\{u,c\},\quad B_w=\{u,d\}.
\]

Choose x so that its private label a is isolated in H[L]. Such a label
exists in all four types: H[L] is empty or has only one edge. The
ordinary retained neighbors of x contribute only u or b by (1).
The vertex x can be a Q neighbor of at most one of z,w, since zw is
an original Q edge and Q has no triangles. Thus old intermediates
and direct attachments reach at most three of the four labels L.
An H step from u reaches no element of L, by the definition of the
bad star; an H step from a reaches no other member of L by its choice.
One required new leaf is therefore missed.

This excludes types 5,7,9,10 for both deletion shapes.

## Two bad-cycle types: 4 and 11

Covering the four edges of K(H)=C4 again saturates all endpoint
capacities. In the adjacent case a three-vertex clique can cover at
most two C4 edges, with the two other cliques contributing at most one
each. Equality forces the center's three ports to be three vertices
of the bad cycle, and both other port pairs to be its remaining bad
edges. The disjoint case assigns the four bad edges to the four
endpoint pairs. In particular all deletion-endpoint ports are
contained in the bad-cycle vertex set T, and A avoids these endpoints.

For any deletion endpoint x, direct new neighbors lie in T. Old
intermediates in the deletion endpoints also contribute only T.
Every other positive old neighbor has a singleton port in a deleted
partner's B set by (1), again in T. Therefore **all new labels outside
T must be supplied by one H step from B_x**.

For type 4, T={4,5,6,7}. All four are H leaves adjacent to hubs 0 or 1.
Consequently no deletion endpoint can reach new vertices 2 or 3.

For type 11, T={1,2,6,7}, and its complement is {0,3,4,5}. Among T,
only 1 has H-neighbors 4 and 5; only 2 has H-neighbor 3; and only
6 or 7 has H-neighbor 0. Covering all four complementary labels
requires B_x to contain 1,2 and at least one of 6,7. But the two-edge
deleted graph always has a degree-one endpoint, whose maximal B set
has size two. That endpoint cannot supply these three distinct
required entrances. This excludes type 11 as well.

## Three-edge bad stars: the precise saturation alternatives

For types 2,3,8 write K(H)=K1,3 with center u and leaves L={a,b,c}.
All three leaves have degree one in H, share a hub h, and are pairwise
nonadjacent in H. The center u has H-degree respectively 1,3,2.
The sets {u,a,b,c,h} and N_H(u) are disjoint in all three representatives;
their sizes give the bounds used below. In particular an
H step from u or from a member of L supplies no other member of L.

First suppose D is disjoint. Covering the three bad pairs requires
three distinct deletion endpoints with full pairs {u,a},{u,b},{u,c};
all three avoid A. Two of these endpoints, say x,y, belong to one
deleted edge, and carry different private leaves a,b. Two disjoint
Q edges have at most one Q cross-edge between their endpoint pairs:
two cross-edges would make a triangle if they share an endpoint, or
a four-cycle if they do not. Hence at least one of x,y, say x, has
no Q neighbor in the other deleted edge's endpoints.

Every old neighbor of x is therefore ordinary, since x avoids A and
xy was deleted. Its positive neighbor ports lie in {u,b} by (1).
Direct attachments at x supply only a from L, and H supplies no
additional label of L. The third leaf c is missed. This closes all
three types for disjoint D, without specifying the fourth endpoint's
ports or whether A touches it.

Now let D={xy,xz}, with x the shared endpoint. The two leaf endpoints
can cover at most two bad-star edges in total. Thus x must cover at
least one. There are exactly three alternatives:

1. All three deletion endpoints have their full port sizes 3,2,2.
2. The center has two ports, meets A once, and the two leaf endpoints
   are full. Their three pairs cover the three distinct bad-star edges.
3. The center is full and covers two bad-star edges; one leaf endpoint
   is full and covers the third; only the other leaf endpoint can meet
   A, once or twice.

These alternatives include a full center that covers just one bad
pair with an additional hub or other nonbad label: then both leaf
endpoints must be full, so it is in alternative 1. A center with at
most one port covers no bad pair and is impossible. Touching the
center and a leaf endpoint, or both leaf endpoints, also leaves fewer
than three possible bad-pair witnesses. Thus no port case is omitted.

Alternative 1 is excluded by the adjacent full-port old-core fact,
including the apparent hub-port escape just mentioned.

In alternative 2, name the port pairs
B_x={u,a}, B_y={u,b}, B_z={u,c}. The center's one added neighbor is
ordinary with zero ports. Every positive retained old neighbor t of
x must repair both lost pairs t-y,t-z, forcing B_t={u}. Zero-port
neighbors contribute nothing. Neither direct nor H routes from
{u,a} reach b or c, so this alternative is impossible.

## The one affected leaf endpoint

In alternative 3, name the fixed full ports

\[
B_x=\{u,a,b\},\qquad B_y=\{u,c\},
\]

and let z be the only deletion endpoint allowed to meet A. If it does
not, this is already alternative 1. Otherwise a_z is one or two.
Each added neighbor q of z is ordinary and has zero ports; q's only
added neighbor is z.

Such a q cannot be a Q neighbor of x. Otherwise the old pair q-y
loses its unique Q route q-x-y; its only added route could use q-z,
but y and z are nonadjacent in Q and y has no addition. Vertex q
has no new port, so no repair is possible. Thus

\[
N_A(z)\cap N_Q(x)=\varnothing.                       \tag{3}
\]

The deleted old pair x-z therefore has no replacement old route of
length at most two: x has no additions, and none of z's added
neighbors is a Q neighbor of x. It must have intersecting ports.
If a_z=2, then B_z is empty and we have a contradiction immediately.

Suppose a_z=1. Write q for its unique added neighbor and B_z={l}.
The same deleted-pair argument gives

\[
l\in B_x=\{u,a,b\}.                                \tag{4}
\]

Every positive retained old neighbor of x has color in B_y={u,c}
by (1), and zero-port neighbors contribute nothing. Hence all new
vertices reachable from x lie in

\[
\{u,a,b,c,h\}\cup N_H(u).
\]

For types 2 and 8 this has at most six and seven vertices respectively,
so both are excluded. Only type 3, where d_H(u)=3 and u has old
capacity 8-3=5, needs one further argument.

Consider the five retained Q neighbors t of x. A positive t has
color u or c. If its color differs from l, the pair t-z has no shared
new neighbor, and its only replacement old route is t-q-z. Hence
t must be a Q neighbor of q.

If t has zero ports, its added partner t' is also ordinary and zero:
the only addition meeting a deletion endpoint is z-q, and q is not
in N_Q(x) by (3). Repairing t-y requires t' to be a Q neighbor of y.
That partner cannot also be a Q neighbor of z, since y,z have unique
Q common neighbor x and t' is not x. Repairing t-z therefore again
requires t to be a Q neighbor of q.

Distinct Q vertices x,q have at most one common Q neighbor. Thus at
least four of the five retained neighbors t are positive and have
color exactly l. Together with (4) and their color restriction {u,c},
this forces l=u. Vertices x,y,z already all carry u, and the four
additional retained neighbors now do too. This requires at least
seven old incidences at u, exceeding its capacity five in type 3.

All alternatives are impossible. Types 2,3,8 are therefore excluded
for adjacent D as well as disjoint D.

## Result and actual computation boundary

The six four-bad-pair types and all three three-bad-pair types are
closed. The nine type proofs use exact old one/two-step route repairs,
port capacities and the explicit H neighborhoods; they impose no
unproved HS automorphism normalization.

The catalog's raw 48,160 labeled survivors and eleven isomorphism
types are unchanged. The present theorem removes the nine nonuniversal
types after that necessary screen; it does not alter its recorded
counts. The separately completed fixed-D, free-addition type-8 UNSAT
experiment is consistent with this theorem but is not its completeness
argument. Neither a new solver nor any new enumeration was run for
this proof.
