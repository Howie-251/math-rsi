# HS58 a5: zero-set pairing for saturated disjoint deletions

Date: 2026-10-12. This is a necessary local assembly rule, not an HS
completion theorem. Let Q be HS50, D={xy,zw} two disjoint original
edges, and A five added original nonedges. Assume an eight-regular,
diameter-two extension by eight new vertices, and assume all four
deletion endpoints P={x,y,z,w} have their maximal two ports.
This saturation holds, for example, whenever the auxiliary H has
exactly four pairs at distance greater than two: four endpoint port
pairs must supply those four distinct required pairs.

Put tau(x)=y, tau(y)=x, tau(z)=w, tau(w)=z. Since the endpoints in P
are full, A avoids P. Every other old vertex has p_t=1-a_t>=0, so A
is a five-edge matching. Its ten endpoints form the zero-port set Z;
all vertices outside P union Z have one port. For q in Z, write q'
for its partner under A and S(q)=N_Q(q) intersect P.

## The exact partner condition

Every q in Z has seven Q neighbors and the zero-port old neighbor q'.
If it had no Q neighbor in P, these old intermediates could supply at
most seven new labels. Thus S(q) is nonempty. It contains at most one
endpoint of each deleted edge: adjacency to both would make a Q
triangle. Consequently |S(q)| is one or two.

If t belongs to S(q), the unique original Q two-step route from q
to tau(t) is q-t-tau(t), and it is broken by D. Vertex q has no new
neighbor, while tau(t) has no added edge. The only possible replacement
old route is q-q'-tau(t), forcing tau(t) in S(q'). Applying the same
argument to q' proves the exact equality

\[
S(q')=\tau(S(q)).                                     \tag{1}
\]

Therefore the chosen zero vertices must have equal cardinalities in
each pair of cells S and tau(S), and every added edge must pair those
opposite cells. Such a paired pair q,q' is automatically an original
nonedge: if qq' were in Q, any t in S(q) would give the four-cycle
t-q-q'-tau(t)-t in Q.

## The zero set is Q-independent

If |S(q)|=1, its seven Q neighbors consist of one two-port deletion
endpoint and six vertices with at most one port each. The total of
eight available port slots must cover all eight new labels. Any zero
among those six vertices would reduce the count to at most seven.
Hence a one-endpoint-neighbor zero vertex has no Q neighbor in Z.

Now consider two zero vertices with two endpoint neighbors each. If
their S sets overlap, an edge between them makes a triangle with a
shared endpoint. If the sets are disjoint, they select opposite
endpoints of each deleted edge. An edge between them then makes a
four-cycle through either deleted original edge, just as above.
Both possibilities are forbidden. Together with the one-neighbor
case, this proves Q[Z] is independent.

## Two-neighbor cells and a Q cross-edge

There are only four possible two-element cells:
{x,z}, {x,w}, {y,z}, {y,w}. Each contains at most one old vertex,
because two vertices of HS have at most one common neighbor.
Thus at most four zero vertices can have |S|=2. In particular at
least six of the ten zero vertices have |S|=1. These are bounds on
necessary inputs, not an assertion that all four cells can be selected.

If there is a Q cross-edge between the two deleted edges, relabel so
that it is xz. Then none of the four two-neighbor cells can contain a
zero vertex:

* {x,z} has no common neighbor, since xz is a Q edge and Q has no triangle.
* The unique common neighbor of x,w is z, using the original edges
  xz and zw. It is in P, so it cannot be a zero vertex outside P.
* Similarly the unique common neighbor of y,z is x, using xy and xz.
* A zero vertex in {y,w} would, by (1), need an added partner in the
  empty {x,z} cell.

This proves the entire claim without assuming that those cross-pair
common neighbors lie outside P. In this case all ten zero vertices
have exactly one deletion-endpoint neighbor; their cells occur in
balanced x/y and z/w pairs.

## What the rule supplies to a construction

A saturated disjoint-D construction must choose ten Q-independent
vertices outside P from these nonempty endpoint-neighborhood cells,
with each S and tau(S) cell equally populated. The five added edges
pair opposite cells. The pairing creates valid original-nonedge
additions and repairs the old zero-to-endpoint paths used to derive
(1). It does not by itself cover all old pairs or supply the eight
new labels at each zero vertex; those remain attachment conditions.

For each zero with |S|=1, its one two-port endpoint neighbor and six
ordinary one-port Q neighbors must partition the eight new labels
without repetition. This is an explicit local port obligation that
can be applied while assigning attachments, instead of independently
choosing five arbitrary added old edges. No new graph enumeration or
solver was used to establish these requirements.
