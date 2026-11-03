# HS58 universal type 6: the unique center neighbor is an addition endpoint

Date: 2026-10-12. This pure argument closes the type-6 branch v in W
under the equality reduction stated below. It uses no computation.
The good-ordinary-leaf exclusion and equality reduction are dependencies
established in the universal-case sections of
[HS58_TWO_DELETE_FOUR_ADDITIONS_EXCLUSION.md](HS58_TWO_DELETE_FOUR_ADDITIONS_EXCLUSION.md).
The separate v outside W branch is not considered here.

## Imported equality case and port sets

Let Q be HS50, D two deleted original edges, A four added original
nonedges, and M=Q-D+A. The new-vertex graph H is a star with center c
and two disjoint extra leaf edges. Its other three leaves are ordinary:
their only H neighbor is c. Let v be the unique old neighbor of c,
and W the endpoint set of A. Assume v belongs to W.

The good-leaf reduction states that every ordinary leaf's old-neighbor
set meets W. The total leaf-port incidence in W is

\[
|W|+\sum_{x\in W}r_x-8-1\le3,
\]

where r_x=d_D(x), the 8 subtracts the total added degree, and the 1
subtracts the unique center port at v. As there are three ordinary
leaves, equality forces the following premises:

* |W|=8, so A is a four-edge matching.
* All endpoints of D lie in W.
* The three leaf ports in W are the three distinct ordinary labels.

For x in W, its new-neighbor count is p_x=1+r_x-1=r_x. Vertices of W
outside the deletion endpoints have zero ports. Every vertex outside
W has one port. Since v has the center port, v is a deletion endpoint;
its remaining r_v-1 ports are ordinary leaves. These facts make the
port sets of distinct deletion endpoints disjoint.

For use below, a deleted original edge cannot have an old two-step
route consisting of two original edges, because Q has no triangle.
Two added edges cannot constitute a two-step route, because A is a
matching. Thus if the endpoint port sets are disjoint, repairing a
deleted edge requires an original retained edge from one endpoint to
the other endpoint's added partner. An original deleted edge cannot
itself be added back, since A consists of original nonedges.

## Disjoint deletions

There are four positive-port vertices P in W, namely the four deletion
endpoints, and four zero-port vertices Z=W minus P. Every old vertex
has at most one port. A zero-port vertex has eight old neighbors and
can reach new vertices only through them. To reach all eight new
vertices, all eight old neighbors must have positive ports. Therefore
no edge of A pairs two vertices of Z. Its four edges match Z and P
bijectively.

Vertex v carries only c. Each of the other three vertices of P carries
one ordinary leaf. For such a vertex x, its direct and H-mediated
routes cover its own leaf and c, and its added old neighbor has zero
ports. Its six retained Q neighbors must therefore supply the other
six leaf labels. Each can supply at most one leaf label, so none can
have zero ports. Consequently these three ordinary-port deletion
endpoints have no Q neighbor in Z.

Take the deleted edge not incident to v. Both endpoints have ordinary
ports and added partners in Z. Their port sets are disjoint, and the
only possible old repairs would require a Q edge from an endpoint to
Z. No such edge exists. This contradicts diameter two.

## Adjacent deletions with an addition between deletion endpoints

Write D={xy,xz}, with x the shared endpoint, and P={x,y,z}. The other
five vertices Z=W minus P have zero ports. If A has an edge within P,
it can only be yz: the other two pairs are original edges. The matching
then gives x a partner s in Z.

To repair deleted xy, the potential old route through the added edge
yz would use the deleted edge xz. Hence its only possible old repair
is x-s-y, forcing sy in Q. Similarly repairing xz forces sz in Q.
The original edges xy,xz and these two forced edges create the
four-cycle x-y-s-z-x in Q. This is impossible in HS50. This argument
applies whether v=x or v is one of y,z.

## Adjacent deletions with no addition between deletion endpoints

Every vertex of P now has an added partner in Z.

If v=x, the port sets are B_x={c,alpha}, B_y={beta}, B_z={gamma},
where alpha,beta,gamma are the three distinct ordinary leaves. For
either y or z, the added neighbor contributes no port, and the direct
and H routes reach only its own leaf and c. Its six retained Q neighbors
must supply the other six leaf labels. Those neighbors are outside P:
x is deleted as a neighbor, and y,z are nonadjacent in Q because they
already have common neighbor x. Each retained neighbor has at most
one port. Thus neither y nor z has a Q neighbor in Z.

The original nonadjacent pair y,z has unique common Q neighbor x,
and both edges of that path were deleted. It is not directly added
in the present case, and its port sets are disjoint. The only possible
new old two-step routes use the added partner of y or z, both in Z.
The necessary Q adjacency to the other endpoint is impossible. Thus
y,z remain farther than two steps apart.

Finally suppose v=y, exchanging y,z if needed. Then B_y={c}, B_x
contains two ordinary labels, and B_z contains the third. Vertex x
must reach the five other leaves through its five retained Q neighbors;
vertex z must reach the six other leaves through its six retained Q
neighbors. Their added partners have zero ports, and their ordinary
ports give no additional H leaf routes. Each retained Q neighbor is
outside P and has at most one port. Both demands therefore force all
those neighbors to have positive ports. In particular neither x nor
z has a Q neighbor in Z.

The deleted edge xz has disjoint port sets and added partners in Z.
Its only possible old repairs require precisely such a Q adjacency.
This is again impossible.

These cases exhaust adjacent and disjoint D and every possible v in W.
Subject to the stated good-leaf/equality reduction, no type-6 completion
has its unique center neighbor among the addition endpoints.
