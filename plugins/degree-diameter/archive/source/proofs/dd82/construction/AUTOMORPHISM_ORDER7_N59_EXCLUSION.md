# Any 59-vertex target has no automorphism of order seven

2026-10-12. Pure proof for arbitrary finite simple undirected graphs; no
vertex-transitivity or prescribed construction is assumed. This does not
exclude order 59 itself.

Let Gamma have 59 vertices, maximum degree eight and diameter at most two.
The radius-two bound at a vertex of degree d is 1+8d, so every vertex has
degree eight. With adjacency matrix A, put B=A^2+A-7I-J. Then B has zero
diagonal, nonnegative integer entries and row sum six. For a nonadjacent
pair x,y its entry is |N(x) intersect N(y)|-1. These identities are the
same as in [the 60/61 proof](AUTOMORPHISM_PRIME_60_61_OBSTRUCTION.md), with
row sum six instead of five or four.

Suppose g has order seven. Its fixed set F has size f congruent to 3
modulo 7, hence is nonempty. The induced graph H on F has every vertex
degree either one or eight: an eight-element neighbourhood under g is
either entirely fixed or consists of one fixed point and a seven-cycle.
Since Gamma is connected and g is nonidentity, an edge from F to its
complement exists. Its endpoint u in F has H-degree one; write a for its
unique neighbour in H.

Call a nonadjacent pair of fixed vertices exceptional if it has no fixed
common neighbour. Its common-neighbour set is g-invariant and has size
between one and seven, so an exceptional pair has exactly seven common
neighbours in one nonfixed orbit. Consequently its B entry is six and
exhausts the entire B row at either endpoint. Every fixed vertex therefore
has at most one exceptional partner. All other fixed pairs have distance
at most two in H.

The H-ball of radius two around the leaf u has exactly 1+deg_H(a) vertices,
at most nine. At most one further vertex of F can be exceptional with u.
Thus f is at most ten. Together with f congruent to 3 modulo 7, this leaves
f=3 or f=10.

If f=3, every H-degree is one (degree eight is impossible), contradicting
the degree-sum parity for three vertices.

If f=10, deg_H(a)=8, since otherwise the preceding bound gives f at most
three. Let v be the sole vertex other than a not adjacent to a. The eight
neighbours of a include u. Because u has only neighbour a, the pair u,v
is exceptional. Vertex v is adjacent to neither a nor u, so its H-degree
is at most seven and therefore exactly one. Let b be its neighbour.
Then b is distinct from u,a,v and is adjacent to a and v. Its H-degree
must consequently be eight. Since b is not adjacent to the leaf u, it is
adjacent to every other vertex besides itself and u.

There are six vertices w outside {u,a,v,b}. Each is adjacent to both a
and b, so must have H-degree eight. But w is adjacent to neither leaf u
nor leaf v, and hence has H-degree at most seven. This is a contradiction.

Both possible fixed-set sizes are impossible, proving that g cannot
exist. The proof depends only on the exact repetition budget, connectivity
and the orbit sizes of an order-seven permutation.

Local review status: independently checked by cyclic_lift58_60 on
2026-10-12. The exceptional-pair budget, the leaf-ball bound, and both
fixed-set cases are sound. In particular, the common-neighbour upper
bound seven follows from B having nonnegative entries and row sum six.
No enumeration, solver call, external review or Lean claim is attached.
