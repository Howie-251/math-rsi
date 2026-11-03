# Complete certificate for flag/layer-edge absorption

Let G be the author's literal 760-vertex, 1520-edge, simple 4-regular
diameter-6 graph. The source diameter assertion is inherited from the
author's supplied verification. It is not rechecked during preparation.

Choose a present original point–line incidence edge e and a present
inserted-layer edge f. The original and layer labels are disjoint, so
their four endpoints T are distinct. Put F={e,f}. Delete F and add a
new vertex x adjacent to T, obtaining H. Each cut endpoint loses one
edge and gains one, and x has degree four. Therefore H is simple and
4-regular, with 761 vertices and 1522 edges.

## Exact new-root condition

For every old vertex v, the distance from v to the set T is unchanged
by deleting F. A shortest path to its first encounter with T contains
no edge internal to T, and both cut edges are internal to T. Hence

    dist_(G-F)(v,T) = dist_G(v,T),
    dist_H(x,v) = 1 + dist_G(v,T).

It follows that every old vertex is at distance at most 6 from x if
and only if the closed radius-5 neighborhood R5_G(T) is all V(G).
The source-neighborhood test is exact, despite deletion of the two
edges. It does not certify old–old distances after the simultaneous
deletions.

## Complete old–old coverage from a bounded root set

Let Q be the closed radius-2 neighborhood R2_G(T) in the original G.
If old vertices a and b are both outside Q, their distance in G to
every endpoint in T is at least 3. Any a-to-b path using a cut edge
must therefore have length at least 3+1+3=7. Since G has diameter at
most 6, an a-to-b path of length at most 6 exists and cannot use F.
That path survives in H.

Thus every potentially damaged old–old pair has an endpoint in Q.
Checking BFS in the actual modified H from all roots in Q, against
all vertices of H, and checking the new root x covers every pair.
This is a complete diameter certificate, not sampling. Each source
vertex has at most 1+4+4*3=17 vertices in its radius-2 ball, so

    |Q union {x}| <= 4*17+1 = 69.

The producer must construct the actual modified adjacency for each
candidate. No inference from individual cut criticality or from an
unmodified old distance matrix replaces these root checks. Once the
exact source R5_G(T) test succeeds, a separate x BFS is logically
redundant, but may be retained as part of that same complete check.

## Frozen scope

Preparation checks the actual author literal: point labels 0..363,
line labels 364..727, layer labels 728..759. There are 1424 current
point–line incidence edges, 64 point/line–layer edges, and 32 layer
edges. Every layer vertex has one point, one line, and two layer
neighbors. Its layer components are cycles of lengths 8,8,16.
Restoring its recorded subdivided flags after removing the layer
recovers a 728-vertex, 1456-edge, 4-regular bipartite incidence literal.
No generalized-hexagon incidence geometry or automorphism group is
reconstructed.

The frozen list is the full product of the 1424 present original
incidence edges and 32 present layer edges, hence 45568 candidates.
It does not include deleted original flags, two arbitrary original
edges, two layer edges, or other changes to the layer. A failure of
this list would exclude precisely this specified absorption family
on the fixed author source, not arbitrary (4,6) graphs of order 761.
