# Conditional subdivision-root coverage at odd bipartite diameter

Let G be a connected bipartite graph of odd diameter D=2k+1. Subdivide any edge `{u,v}` by a new vertex x, obtaining G'. Then for every old target t,

`d_G'(x,t)=1+min(d_G(u,t),d_G(v,t)) <= D`.

For the equality, choose an endpoint minimizing its old distance to t. A shortest path from that endpoint cannot start with the removed edge, because the other endpoint would then be one step closer. It cannot use that edge later, because the shortest path is simple and cannot revisit its starting endpoint. Thus a minimizing path avoids the removed edge and is still available after subdivision. Conversely, every simple x-to-t path starts at u or v and thereafter avoids x, giving the lower bound.

Exactly one of u,v lies in the same bipartition class as t. Its distance to t is even and at most the odd number D, hence at most D-1. This proves the inequality.

Edge transitivity is unnecessary for this new-root statement. If it is separately established, it reduces all single-edge subdivisions to one graph up to isomorphism. Old-old distances can still increase by one when all shortest routes use the subdivided edge; therefore automatic new-root coverage does not prove that the whole graph retains diameter D. The general source-path replacement bound is D+1.

For the actual Exoo600 source, parity union-find proves non-bipartiteness. This lemma is conditional and is not a diameter certificate or an exclusion for any Exoo600 subdivision. No candidate or distance search was run.
