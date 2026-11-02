# Exact diameter-three constraints for one hub and seven cut edges

Assume the producer-bound source G is simple, 14-regular, of order 1141 and diameter at most 3. Choose a matching M of size 7. Let S be its 14 endpoints, H=G-M, and add a new hub h adjacent to every vertex of S. Call the resulting graph K. It is simple and 14-regular, of order 1142 and size `7987-7+14=7994`. This is a perfect matching only on the selected set S, not on the odd-order source. No graph, source-distance cache, edge enumeration, or solver was used for this note.

## Exact distance identities

For every old t,

`d_H(S,t)=d_G(S,t)`.

To prove this, take a shortest G-path starting at whichever point of S minimizes the distance to t. It cannot contain a deleted edge: both ends of every deleted edge are in S, so starting instead at the endpoint after that edge would give a strictly shorter S-to-t path. Hence a minimizing path survives in H.

Every shortest path in K uses h at most once. Therefore, for distinct old p,q,

`d_K(p,q)=min(d_H(p,q),2+d_G(p,S)+d_G(q,S))`,

and for the new root,

`d_K(h,t)=1+d_G(S,t)`.

The formulas remain valid if H is disconnected. Independently shortest H-prefixes and suffixes give a walk through h; deleting repetitions can only shorten it, which suffices for the upper bound in the first identity. The converse follows by splitting a shortest path at h.

Consequently the new hub covers all old vertices within three steps exactly when `R2_G(S)=V(G)`. The condition for an old pair to have a route through h of length at most three is exactly

`[p in S and q in N_G[S]] or [q in S and p in N_G[S]]`.

Here N_G[S] is the closed one-neighbourhood, including S itself. Thus a three-step hub route needs at least one endpoint to be a pin. Two nonpins cannot be repaired through h within three steps. If both endpoints are pins, the route p-h-q has length two.

Using the SOURCE closed neighbourhood is sound. If a claimed edge q-r to a selected pin r was itself deleted, q is also a selected pin; the pair is then already repaired by the two-step hub route. No cut-graph neighbourhood variable is needed.

## Which old pairs require constraints?

All pairs of original distance at most two are automatically within three in K:

- If an original edge survives, its endpoints stay adjacent. If it is deleted, both endpoints are pins and the hub replaces it in two steps.
- A two-edge source path can lose at most one edge, since M is a matching. Replace that one edge by its two-step route through h, producing a path of length at most three.

Thus only source pairs with `d_G(p,q)=3` need old-old constraints. Every source path of length at most three for such a pair is a three-edge geodesic. A shortest old route in H exists within three exactly when at least one such source geodesic loses no edge.

For a geodesic `p-u-v-q`, the possible intersections with M are

`empty, {pu}, {uv}, {vq}, {pu,vq}`.

A middle cut cannot coexist with either neighbouring cut. Two cuts on this path must be its first and last edges; in that case p,q are both pins and are repaired in two steps. A single middle cut, with both endpoints nonpins, gives only the four-step replacement p-u-h-v-q; it does not repair this pair within three. A first or last cut is not automatically repaired either: one pin endpoint still needs the other endpoint to lie in the closed one-neighbourhood of S.

The following classification is necessary and sufficient for every original distance-three pair:

| Endpoint membership | Exact condition |
|---|---|
| p,q both in S | Always covered, by p-h-q. |
| p in S, q not in S | Either q is in N_G(S), or at least one source three-edge geodesic survives. |
| q in S, p not in S | Symmetric condition. |
| p,q both outside S | At least one source three-edge geodesic survives; a hub route cannot help. |

There are useful exact simplifications inside these cases:

1. If p is a pin and q lies outside N_G[S], the last two edges of every geodesic `p-u-v-q` survive: v cannot be a pin, since it is adjacent to q. Only the first edge can be deleted. Hence this case fails exactly when every source three-geodesic starts with the unique matching edge incident with p. Two distinct first ports already prevent this failure. Reverse the statement when q is the pin.
2. If neither endpoint is a pin, the first and last edges cannot be cut. Put `F_pq=E_G(N_G(p),N_G(q))`; its edges correspond exactly to the source three-geodesics. The pair survives exactly when at least one edge of F_pq is outside M. Thus failure in this case is precisely `F_pq subset M`. In particular a nonmatching F_pq, or one with more than seven edges, cannot all be deleted by M. These are conditional mathematical observations, not new source statistics.

Having several source three-geodesics is not by itself sufficient: they may all share a deleted first edge, or their middle edges may themselves form a selected matching. A unique-three-path constraint is only one necessary subcase.

## Exact lazy linear formulation

Use the producer's notation: binary y_e selects a deleted source edge, and binary x_v indicates that v is a pin. Impose

`sum_e y_e=7`, and `x_v=sum_{e incident with v} y_e` for each old v.

The second equality, together with binary x_v, enforces the matching and binds its endpoint set exactly. The hub-root constraints are

`sum_{v in R2_G(t)} x_v >= 1` for every old t.

For a failed source distance-three pair p,q, let P_pq be ALL its source three-geodesics. Add one auxiliary r_P for each P, and auxiliaries a_pq,b_pq, all in the interval [0,1], with

`r_P <= 1-y_e` for every edge e of P;

`a_pq <= x_p`, `a_pq <= sum_{v in N_G[q]} x_v`;

`b_pq <= x_q`, `b_pq <= sum_{v in N_G[p]} x_v`;

`sum_{P in P_pq} r_P + a_pq + b_pq >= 1`.

These upper bounds and the final covering inequality are already an exact existential formulation for integer x,y. If no old path survives and neither hub condition holds, every auxiliary is forced to zero. If a surviving path or a valid hub route exists, set its auxiliary to one and the row is feasible. Lower reification bounds are unnecessary; the auxiliaries need not be binary and are not claimed to equal semantic route indicators in every feasible auxiliary assignment. Their only purpose is to certify existence of a valid route. All paths and neighbourhoods must be from the fixed source, not from whichever routes happened to survive the current matching.

A reliable compact NECESSARY cut for a distance-three pair is

`sum_{e in F_pq} y_e <= |F_pq|-1+x_p+x_q`.

It enforces a surviving middle edge when both endpoints are nonpins, and becomes vacuous if either endpoint is a pin. For a unique geodesic with middle edge uv this reduces to `y_uv <= x_p+x_q`. This compact inequality alone does not handle the one-pin/first-edge obstruction and is not a replacement for the exact route OR above.

## Sparse first-port cut from the existing route-diversity cache

For source `d_G(u,t)=3`, define `H_u(t)={v in N_G(u):d_G(v,t)=2}`. This is the set of first ports of all source three-geodesics, not a neighbourhood in the cut graph H. If `H_u(t)={v}`, the following sparse inequality is valid:

`y_uv <= sum_{s in N_G[t]} x_s`.

If y_uv is one, u is a pin and every old route of length at most three from u to t loses its first edge. The exact old-pair condition therefore requires a hub route. Since u is already a pin, this is equivalent to t belonging to the closed one-neighbourhood of S, exactly the positive right-hand side. If t itself is a pin it is included in that closed neighbourhood and is repaired by u-h-t. When y_uv is zero the inequality is vacuous; it is not claimed to cover other ways the pair could fail.

Thus, conditional on choosing this cut edge, the row exactly captures that pair's remaining route requirement. It needs no auxiliary and contains one edge variable plus the 15 pin variables of the source closed neighbourhood. The same statement applies at the other endpoint. Existing unique-first-port data may supply these rows directly; no new path computation or large matrix is required by this note. This strengthens the middle-edge-only necessary constraints without mistaking them for a complete model.

A lazy loop may inspect a proposed matching in the actual modified graph and add the displayed globally valid row for a failing pair. A previously added row does not depend on that particular matching. Passing all newly tested pairs is not a complete graph claim until every old pair is covered; source distances at most two and hub pairs are handled by the proved reductions. No separate unverified 'unique3 implies everything' rule is used.

The complete criterion for this exact family is: the matching/degree constraints, closed R2 coverage for h, and the exact old-pair route OR for every source distance-three pair. Together they are necessary and sufficient for K to have diameter at most three. This does not establish feasibility or infeasibility of the model. No numerical experiment was performed here.
