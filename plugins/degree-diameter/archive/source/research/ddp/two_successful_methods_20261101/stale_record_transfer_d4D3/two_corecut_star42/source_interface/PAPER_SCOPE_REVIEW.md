# Paper scope review: two disjoint cuts and one quartic star

This reviews one proposed modification of a fixed simple quartic graph G with41 vertices,82 edges and diameter at most3. Source identity and older exact scopes are owned by the separate read-only source-interface task; this paper does not read or validate the raw graph. The conclusions below apply once that actual source binding is established.

## Degree and order

A graph with maximum degree4 and diameter≤3 has at most1+d(1+3+9)≤40 vertices if any root has degree d≤3. Thus a42-vertex candidate must be4-regular. Delete two vertex-disjoint old edges, with four endpoints P, and add one new vertex z joined once to each endpoint. Every old endpoint loses and gains one edge; all other old degrees stay4, and z has degree4. The result is42 vertices and82-2+4=84 edges, all4-regular. Simplicity is automatic for the new star. Two cuts sharing an endpoint would leave that endpoint degree3 under this rule, so disjointness is material.

## Exact new-root gate

Put H=G minus the two cut edges, before the star. Every shortest z-to-old path uses z only at its start. Hence

d_new(z,t)=1+d_H(P,t).

Therefore the new root has radius≤3 exactly when the union of the four closed H-balls of radius2 covers all41 old vertices. Deleting edges whose endpoints all lie in P does not change distance from P: choose a closest-seed shortest path in G; any later visit to P could shorten it, so no deleted P–P edge is needed. Thus d_H(P,t)=d_G(P,t), although this identity does not certify old–old pairs.

## Old-pair damage and cooperative repair

For old u,v, the new distance is

min(d_H(u,v), d_H(u,P)+2+d_H(v,P)),

where paths through z use two star edges. In particular, if u and v are both outside P, every route through z has length at least4. Such a pair must retain an H-path of length≤3; the new star cannot repair its destroyed source3-walk within diameter3. If exactly one endpoint is a pin, a star route can repair the pair in≤3 only when the other endpoint is in the closed H-neighborhood of P. This is a concrete loss-of-route condition, not a claim that it fails for every two-cut choice.

Source diameter3 gives a universal upper bound4 for the candidates. Take any old shortest path of length≤3. If it uses no cut it survives. If it uses one cut, substitute two star edges and increase length by at most1. If it uses both disjoint cuts, their occurrences lie at the first and third edges of a3-path; replace the entire segment between its pin endpoints by two star edges, rather than replacing each cut separately. New-to-old distances are≤4 because d_H(P,t)=d_G(P,t)≤3. Thus every such candidate has diameter≤4, and a successful new-root radius3 test is still insufficient to conclude diameter3.

## Exact scope and limits

A complete test of this fixed two-cut rule requires every unordered pair of vertex-disjoint old edges unless an actual source automorphism and orbit binding justify representatives. No vertex transitivity is assumed. An older single-edge subdivision or single-split NO does not exclude this two-cut, four-star operation. Conversely this paper provides no general construction of42 vertices and no strict NO for all cut pairs. It changes no graph, degree bound or public record.

No graph generation, source diameter check, BFS/balls, cut-pair enumeration, field/rank test, solver, Lean, external review, installation or hashing is performed by this paper task. The source-interface metadata is awaited separately; a follow-up source binding should cite that actual receipt without repeating the source validation.
