# Complete verification for the fixed two-edge absorption rule

Let G be the author's current 3645-vertex graph, with 20044 edges, maximum
degree 11 and diameter at most 4. Its diameter bound is inherited from the
author's published graph and verification; preparation does not recheck it.
Let F consist of the two selected existing point–host edges, and T be their
four distinct endpoints. Let U be the seven current vertices of degree 10.
All vertices of T have degree 11 and T is disjoint from U. Put S = T union U.
Form H by deleting F and adding a new vertex x adjacent to all eleven
vertices of S. Then H has 3646 vertices and 20053 edges, and maximum degree
11. This degree assertion follows directly: each endpoint of F loses and
gains one edge; each vertex of U gains one edge; x has degree 11.

## New-root coverage uses the original adjacency exactly

For every old vertex v,

    dist_(G-F)(v,S) = dist_G(v,S).

Every edge of F has both endpoints in S. A shortest path from v to its
first encounter with S cannot use such an edge. This gives a shortest
v-to-S path in G-F, while removing edges cannot decrease the distance.
Consequently

    dist_H(x,v) = 1 + dist_G(v,S).

Thus x is within distance 4 of every old vertex exactly when the closed
radius-3 neighborhood of S in G is all of V(G). The existing exact
seven-free-port radius-3 cache covers 2902 vertices and misses 743, all in
the original 3444 labels. A candidate therefore passes the new-root test
exactly when the original radius-3 neighborhoods of T cover these 743
vertices. Reusing this cache does not reuse distances in a modified graph.

## A bounded root set checks every old–old pair

Let Q be the closed radius-1 neighborhood of T in the original G. There
are at most 4*(11+1) = 48 vertices in Q. Suppose both old vertices a,b lie
outside Q. Every a-to-T and b-to-T path in G has length at least 2.
Any a-to-b path using an edge of F therefore has length at least
2+1+2 = 5. Since G has diameter at most 4, an old path of length at most 4
exists and cannot use F; it survives in H. Hence all possibly damaged
old–old pairs have at least one endpoint in Q.

It follows that BFS in the actual modified H from every root in Q and
from x, checking all H vertices at distance at most 4, proves the entire
diameter bound. This is complete pair coverage, not a sample of roots.
If the new-root radius-3 test has already been established by the first
lemma, its BFS is mathematically redundant; it may be retained once by
the producer as the same complete check. Every candidate must use its
own two deleted edges and actual modified adjacency. Two individually
safe cuts need not be jointly safe, and no such assumption is made.

## Frozen source rule and its limits

The original 3444-vertex base is reconstructed only by restoring the
author's logged deletions with both labels below 3444. It has 18942
edges and is 11-regular. No geometry or old distance matrix is rebuilt.
Each of the 164 spread twins has exactly the same ten original
point-copy neighbors as a unique original spread-line copy. This
equality binds the original alternative hosts. For every base point
p=0,...,819, each copy 2p and 2p+1 independently selects its original
spread twin or this original spread-line copy. Only candidates whose
two cut edges are still present in current G are retained.

The original base identifies hosts; it does not certify current route
coverage. The current source has undergone 201 insertions and deletions.
Both the source radius-3 gate and modified-graph root checks remain
necessary. Used base points are included when another host edge remains.
The 201 logged insertions use 199 distinct base points. No candidate has
been evaluated by the preparation script.

The preceding negative all-free-port result concerns preservation of
all source edges. The present construction deletes two actual edges and
therefore lies outside that closed scope. A failure of the frozen list
would concern this specific original-host, two-edge absorption family;
it would not exclude arbitrary rewiring or arbitrary maximum-degree-11
graphs of order 3646.
