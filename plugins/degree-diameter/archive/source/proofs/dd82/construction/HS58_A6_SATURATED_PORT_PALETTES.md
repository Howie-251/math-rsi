# HS58 a6: saturated zero-cycle port constraints

Date: 2026-10-12. This pure argument shares all four zero-set cases
and all 56 addition matchings in
`HS58_SATURATED_DISJOINT_ALL_ADDITIONS.md`. It excludes the subcase
in which both deleted edges have identical port pairs at their two
ends. It does not exclude all saturated a6 candidates.

Use D={01,10-11}, and write B0,B1,B10,B11 for its four two-element
port sets. The deleted edges themselves have no replacement old
two-step path: their endpoints have no additions and Q is triangle
free. Thus B0 intersects B1 and B10 intersects B11. Put
X=B0 union B1 and Y=B10 union B11, each of size two or three.
The four double-neighbor points are zeros, and each eight-cycle in
the cited theorem has one alternating half zero and the other half
ordinary positive.

## An exact two-list condition on each cycle

An ordinary vertex t in singleton cell T_p has no addition and one
port. Its original two-step route to tau(p) was broken, and neither
endpoint of that pair has an addition. Its port must therefore belong
to B_tau(p). Meanwhile each singleton zero q has precisely eight
neighbor-port slots, so every ordinary neighbor's label must avoid
both labels in B_s(q), and all six ordinary labels must differ.

When an L half is zero, a positive T10 point has neighboring zeros
from T0 and T1. Its label belongs to B11 minus X. A positive T11
point similarly uses B10 minus X. The four positive points form a
cyclic sequence through their intervening zeros, and consecutive
labels in this sequence must differ. Their lists alternate between

\[
U=B11\setminus X,\qquad V=B10\setminus X.
\]

For these constraints alone a coloring exists exactly when U and V
are nonempty and |U union V|>=2. Necessity is immediate. Conversely
choose distinct u in U and v in V and alternate them. The same
statement for an R-zero half uses U=B1 minus Y and V=B0 minus Y.
This is an exact local condition, not sufficiency for all zero rows:
each singleton zero still needs four further ordinary labels outside
T, and each double zero needs all eight labels from its nine slots.

For a mixed zero set both conditions apply. They imply |X intersect
Y|<=1. If either X or Y has size two, they further imply the
intersection is empty, because the corresponding identical two-port
sets would otherwise leave at most one available list color.

## Both equal endpoint pairs cannot complete H

Suppose B0=B1=X and B10=B11=Y, now with |X|=|Y|=2. Whichever half
of the first cycle is zero, its two lists coincide. The local condition
requires two colors in the other pair after removing the first, hence
X and Y must be disjoint. Let W be the four other new vertices.

Every positive retained Q neighbor of a deletion endpoint p has its
label in B_tau(p), by the broken-route argument above; zeros contribute
none. Therefore when B_p=B_tau(p), direct and old-intermediate reach
from p adds no labels outside that pair. It follows that both X and
Y must dominate H: every vertex outside either pair has an H neighbor
in that pair. In particular each w in W has at least one X neighbor
and one Y neighbor, and H[X,Y] is an edge cover of its four vertices.

Let k be the number of cycles choosing their L half as zeros. A
positive half whose two lists are the same two colors must alternate
those colors, twice each. Each color of X consequently occurs at
least 2+2(2-k)=6-2k times among old ports: twice at the deletion
endpoints and twice for each R-zero cycle's positive half. Each color
of Y occurs at least 2+2k times. Exact new degrees imply

\[
d_H(x)\le2+2k\ (x\in X),\qquad
d_H(y)\le6-2k\ (y\in Y).
\]

If k=0, both X degrees are at most two. They already need at least
one edge each to Y, leaving at most two incidences to the four
vertices of W, although X must dominate all four. This is impossible.
The case k=2 is symmetric. It remains to consider k=1, when all four
palette vertices have H degree at most four.

There are eleven H edges. Write r=e_H(W,X union Y), c=e_H(X,Y),
and e for all remaining edges. Domination gives r>=8 and c>=2.
Thus the only possibilities are (c,r,e)=(3,8,0),(2,9,0),(2,8,1).
Every H bad pair involving W, or having one endpoint in X and one
in Y, is forbidden: ordinary old vertices have only one port, and
the only multiple-port sets are X and Y themselves.

If (c,r,e)=(3,8,0), label the missing cross edge x1-y1. Every W
vertex has exactly two neighbors, one in each pair. For it to reach
the other two palette vertices within two steps, its type must be
either {x0,y0} or {x1,y1}. Vertices of these two types have disjoint
neighborhoods and are a forbidden bad pair. Hence all four have one
type, making the corresponding palette degrees at least five,
contrary to the degree bound.

For c=2, the cross edges must form a perfect matching, say x0-y0
and x1-y1. Call {x0,y1} and {x1,y0} the off-matching types.

If r=9,e=0, exactly three W vertices have degree two and the fourth
has degree three. Each degree-two vertex must have an off-matching
type in order to reach the other palette vertices. The three must
have the same type, since opposite types are a bad pair. Say this
type is {x0,y1}. The other missing cross pair x1-y0 must have a
common W neighbor, necessarily the fourth vertex, which thus meets
x1 and y0 and also one of x0,y1. That last palette vertex now has
three neighbors among the first three W vertices, one at the fourth,
and its cross-matching edge: degree five, a contradiction.

Finally take r=8,e=1. All W vertices initially have one neighbor in
each palette. If the extra edge is inside X or inside Y, an on-
matching type still cannot reach the other vertex of the opposite
palette. All W types must therefore be off-matching. Opposite types
remain a forbidden bad pair, so all four have the same type, forcing
a palette degree at least five.

If the extra edge joins two W vertices s,t, the other two W vertices
must be off-matching and must have the same type, say {x0,y1}.
To cover the missing cross pair x1-y0, one of s,t must have type
{x1,y0}. Its neighborhood is {x1,y0,the other W endpoint}, which
is disjoint from the neighborhood {x0,y1} of either untouched W
vertex. This is again a forbidden bad pair. All possibilities fail.

Thus no complete a6 extension can have both B0=B1 and B10=B11.
This conclusion uses H freely with eleven edges, not a proposed
auxiliary graph, a flow failure, or an auxiliary catalog.

## Precise remaining obligation

The argument leaves endpoint patterns in which at least one deleted
edge has different but intersecting port pairs. For example the
formal pattern B0={a,b}, B1={a,c}, B10={d,e}, B11={d,f}, with six
distinct labels, satisfies both mixed-zero two-list conditions and
the two required deleted-edge intersections. It has not been shown
to admit the remaining zero-row colors, exact new degrees, an H with
eleven edges, or complete pair coverage. Those joint constraints,
rather than either equal-palette case, are the remaining construction
obligation. No SAT, flow, or new enumeration was used in this proof.
