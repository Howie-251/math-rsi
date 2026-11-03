# Balanced split plus an absorbed old edge: exact root gate

Status: **VALID paper reduction; no candidate evaluated**. This is a different operation from the closed plain adjacent-split family. The source is the previously accepted simple four-regular 104-vertex diameter-four graph. Existing files are `research/ddp/breadth_20261027_wave2/sources/bhakar104.edges`, `bhakar104_distances.json`, and `bhakar104_check.json`. This analysis performs no source BFS, new distance computation, candidate enumeration or solver call.

## Operation and degree conditions

Fix v with N_G(v)=A disjoint-union B and |A|=|B|=2. Replace it by adjacent children u,w. Retain u-A and attach w-B. Choose an oriented old edge x-y with x,y!=v, delete x-y, and add u-x and w-y. For simplicity and degree four, require x not in A and y not in B; x in B or y in A is allowed. All other old edges are retained.

The frozen production batch uses the cleaner subfamily x,y outside the closed old B1_G(v), so these nonduplication conditions hold automatically. Its source-side preparation reports no triangles and 192 eligible unordered outside edges for every v, hence 104*3*2*192=119808 planned settings. Those are inherited preparation counts, not an enumeration performed by this analysis. The proof applies to the wider legal nonincident-edge operation, but no experiment on that wider family is claimed.

The two children have degree 2+1+1=4. Every old neighbour of v receives its replacement child edge, and x/y replace their deleted x-y incidence by one new edge. The graph has 105 vertices and 210 edges, with all degrees four. These counts do not prove diameter four.

Let O=V(G) minus {v} and let K=G-v-x-y, where the last notation means deleting the **edge** x-y, not its vertices. Put P=A union {x}, Q=B union {y}. The exact distance from u to any old target t is

    d_new(u,t) = min(1+d_K(P,t), 2+d_K(Q,t)).

The symmetric expression holds for w. A shortest path visiting the other child can use u-w immediately: any indirect prefix to that child is longer and can be replaced. Otherwise it leaves its initial child once and stays in K. Thus these formulae include all root paths, including paths that would have reached the buddy through old vertices.

## The exact gate using only the original cached matrix

For an old far target t with d_G(v,t)=4, define its geodesic first-neighbour support

    F_v(t)={z in N_G(v): d_G(z,t)=3}.

This set is nonempty. Define the loss sets

    E_A={t in S4_G(v): F_v(t) intersect A is empty},
    E_B={t in S4_G(v): F_v(t) intersect B is empty}.

Equivalently all first supports of a target in E_A lie in B, and conversely. They include the singleton first-support obstructions that defeated a plain split, while allowing all other support multiplicities.

For every legal operation above, the two new children are within distance four of every vertex **if and only if**

    E_A subset B3_G(x),
    E_B subset B3_G(y).

The balls in this test are in the original graph G. The statement is exact despite deleting v and x-y; it is not an optimistic use of an undeleted source cache.

To prove it, first take t with d_G(v,t)<=3. Lift a source geodesic after splitting v. It gains at most the one buddy step, hence has length at most four unless it uses the deleted x-y edge. If it uses x-y, that edge is at position j>=2, since it is not incident to v. Its remaining suffix has length at most 3-j<=1 and avoids v and the cut edge. From u, reach the suffix's initial endpoint by u-x of length one or u-w-y of length two; from w use w-y or w-u-x. Thus the damaged geodesic is replaced by a route of length at most two plus one, at most three, for either new root. All old targets at distance at most three are therefore automatically safe for both new roots.

Now let d_G(v,t)=4. Neither B nor any other old neighbour of v reaches t in at most two old steps, so the buddy's old B branch cannot cover t from u. The exact root formula reduces to

    t in B3_K(A) union B3_K(x) union B2_K(y).

Every shortest old walk from x that uses the deleted x-y edge uses it first. Consequently

    B3_K(x) union B2_K(y) = B3_(G-v)(x).

For this far target, an old walk of length at most three ending at t cannot pass through v. Hence its membership in B3_(G-v)(x) is exactly membership in the cached B3_G(x).

Likewise, source A-to-t walks of length three avoid v. If such a walk is lost when x-y is deleted, it contains x, so its suffix shows d_G(x,t)<=3. That target was already absorbed by the endpoint-port term. Therefore

    B3_K(A) union B3_G(x)
    = B3_G(A) union B3_G(x)       on S4_G(v).

This proves the u condition. The w condition follows by exchanging A/B and x/y. The children themselves are adjacent, completing the exact root statement.

## Strong finite search interface

For each v and unordered 2+2 partition, form from the saved matrix

    X={x in O minus A: E_A subset B3_G(x)},
    Y={y in O minus B: E_B subset B3_G(y)}.

The first constructive question is whether any oriented existing non-v edge goes from X to Y. If none exists, the whole operation for that split is excluded at the new-root stage. If none exists for any v/split, the complete stated operation is excluded without building a candidate or computing modified distances.

The concrete proposed coverage prediction is that such a legal oriented edge exists for at least one split, so the two new ports repair both entire loss classes. This is a proposed gate-level claim, not a tested fact or a claim of full diameter four. Ordinary split failure does not answer it: the added endpoint ports are exactly the new coverage terms.

## Old-old distances require a separate complete check

Passing the root gate does not preserve old-old diameter automatically. For instance a source four-geodesic p-a-v-b-q, with a in A and b in B and both endpoints at old distance two from v, can become a five-walk after splitting. Thus checking only R1_G(v) roots would be incomplete.

A complete sufficient set of modified BFS roots is

    S = [B2_G(v) union B1_G({x,y})] minus {v},

together with the two children if not already accepted by the exact root theorem. Both balls here are closed balls in the original graph. If old endpoints p,q lie outside S, any old path of length at most four cannot pass through v (it would need at least 3+3 steps), and cannot use x-y (it would need at least 2+1+2). Such a source path is retained verbatim. Every other old-old pair has a root in S and is handled by its actual modified radius-four check.

There are at most sixteen non-v vertices in B2_G(v). Since x-y is an edge, the two closed radius-one balls have union size at most eight. Thus |S|<=24, and including u,w needs at most 26 roots. Remove v from the **entire** union if it is a neighbour of x or y, then add its new u label explicitly; this avoids confusing the deleted old vertex with a surviving old root. No symmetry sampling is involved.

The source diameter-four acceptance is inherited. A candidate passes overall only after the legal degree/edge checks, the exact two-root gate, and the complete affected-old-root checks. No global existence, actual diameter, failed graph or ordinary bad-pair count is reported by this paper task.
