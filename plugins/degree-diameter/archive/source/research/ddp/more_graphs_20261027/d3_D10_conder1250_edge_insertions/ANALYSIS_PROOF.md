# Exact family scope for anchored edge insertions

The input is the bound, zero-based official `../d3_D10_current1250_source/source1250.edges`: simple cubic, 1250 vertices and 1875 edges. Its published diameter 10 and edge transitivity are inherited from Conder C1250.2; no source diameter or automorphism computation is repeated. Let the anchored edge be `e0={0,1}`.

## A: one edge subdivision

Replace an edge `{u,v}` by `u-x-v`. The new graph has 1251 vertices, 1876 edges, x of degree 2, and all old vertices of degree 3. Every automorphism carrying one source edge to another extends to an isomorphism between the corresponding subdivisions. The published single edge orbit therefore makes the one anchored case complete for this operation, although it does not make the resulting graph vertex-transitive.

For every old t the exact new-root distance is

`d_new(x,t)=1+min(d_G(u,t),d_G(v,t))`.

Indeed a shortest route to t from whichever old endpoint gives the minimum never needs to begin by traversing the removed edge: switching to the other endpoint would shorten it. Thus the new root passes radius 10 exactly when `R9_G(u) union R9_G(v)=V(G)`.

Every old-old source geodesic uses the subdivided edge at most once, so replacing that edge increases its length by at most one. New-root distances are at most 11 by the displayed formula. Therefore the whole subdivision has diameter at most 11. A genuine pair at distance greater than 10 proves exact diameter 11. In particular, passing the new-root test alone is not enough to claim diameter 10: an old-old distance can increase from 10 to 11.

## B: two cut edges and an adjacent pair of new helpers

Choose two distinct source edges e,f. Delete them, introduce a,b with edge a-b, and allocate the four deleted-edge endpoint occurrences into two unordered groups A,B of size two. Add spokes from a to A and b to B. Occurrences, rather than a set of endpoints, matter when e and f share a vertex.

For disjoint edges there are exactly three unordered 2+2 partitions, all simple. For adjacent edges `{u,v},{v,w}`, each helper must receive one occurrence of v. This leaves exactly one distinct simple partition, `A={u,v},B={v,w}`, up to swapping the helper labels. Allocating both occurrences of v to one helper would introduce a repeated spoke and is invalid. In every valid case all old degrees return to 3 and each new helper has degree 3. The order is 1252 and the size is `1875-2+4+1=1878`.

For any unordered source-edge pair, edge transitivity can send either chosen member to e0; it sends the other to one of the remaining 1874 edges and preserves the endpoint partition. Thus anchoring e0 loses no case in this exact operation. Four remaining edges meet e0 and 1870 are disjoint, so the complete anchored list has `4*1+1870*3=5614` distinct helper-unlabeled cases before any additional source symmetries. This is a logical count, not an edge enumeration performed by this proof task. It does not claim all 5614 graphs are pairwise nonisomorphic.

Let H be the source after deleting e and f. For any old target t, allowing infinity if necessary, the exact formulas are

`d_new(a,t)=min(1+d_H(A,t),2+d_H(B,t))`,

`d_new(b,t)=min(1+d_H(B,t),2+d_H(A,t))`.

Any shortest route from a that reaches b can replace its prefix by the direct a-b edge; after its last departure from a or b it lies entirely in H. This proves both the lower bound and attainability. Shared old pins cause no exception. The two new roots pass radius 10 exactly when

`R9_H(A) union R8_H(B)=V(H)` and `R9_H(B) union R8_H(A)=V(H)`.

Their mutual distance is one. Old-old distances still need separate checking because two source edges were deleted; passing both new-root conditions does not preserve those distances automatically. A negative witness in this two-cut family must not be assigned the subdivision's upper bound 11. Unless the producer establishes a separate bound or completes all distances, its global diameter remains unknown.

The family completeness statements use only the inherited source edge transitivity and the explicitly defined operations. They do not assume bipartiteness, an unbound Petersen-cover coordinate system, or that these graphs are Cayley. No edge pair, endpoint partition, candidate graph, or BFS was enumerated by this analysis.
