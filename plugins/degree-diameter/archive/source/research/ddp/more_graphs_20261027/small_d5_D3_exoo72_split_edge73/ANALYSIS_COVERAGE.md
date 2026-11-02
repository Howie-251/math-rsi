# Exoo72 balanced split plus one absorbed edge: diameter-three gate

Status: **VALID paper specialization; no candidate or new ball computation**. This operation adds two endpoint ports to a split, so the old plain-split exclusion is not its exclusion. The analogous diameter-four proof is `../small_d4_D4_bhakar104_split_edge105/ANALYSIS_COVERAGE.md`.

The inherited source G is the accepted five-regular 72-vertex diameter-three graph. Existing literals are `research/ddp/more_graphs_20261027/d3d4_transfer/source72.implicit_adj.txt` (72 rows, zero-based, no header) and `research/ddp/more_graphs_20261027/d5_exoo72_extension/root_cover_preflight/source.edges`. The scout found no persisted full distance matrix or radius-two cache; this paper does not assume one exists or compute one. The source's previous diameter acceptance is reused.

## Operation and capacity change

Write N_G(v)=A disjoint-union B, |A|=2 and |B|=3. Replace v by adjacent children u,w, with u-A and w-B. Delete an old edge x-y whose endpoints lie outside the closed B1_G(v), and add u-x,w-y. All other old edges are retained. The clean endpoint domain makes all added edges distinct and new.

The result has 73 vertices and 182 edges. Its degree histogram is one vertex of degree four (u) and 72 vertices of degree five. The old plain split gave the smaller child degree three and its buddy degree four, so its radius-three bound was 1+3+11+44=59<73. With the two ports the smaller child has degree four and all four neighbours have degree at most five, giving the necessary bound 1+4+16+64=85>73. This removes that particular capacity obstruction; it does not prove coverage or diameter three.

## Exact two-new-root criterion

For every t with d_G(v,t)=3 let

    F_v(t)={z in N_G(v): d_G(z,t)=2}.

Define

    E_A={t in S3_G(v): F_v(t) intersect A is empty},
    E_B={t in S3_G(v): F_v(t) intersect B is empty}.

Then the two new children are each within distance three of the whole new graph **if and only if**

    E_A subset B2_G(x),
    E_B subset B2_G(y).

This is an exact test with old closed radius-two balls, not an optimistic substitute for deleting v and x-y. In particular it supports a complete finite preflight over legal oriented old edges after fixing v and A/B.

Let K be G with vertex v and edge x-y deleted, and put P=A union {x}, Q=B union {y}. For an old target t,

    d_new(u,t)=min(1+d_K(P,t),2+d_K(Q,t)).

Any path to the buddy w can use u-w immediately instead of an indirect prefix; a path avoiding w leaves u once and otherwise lies in K. Hence this distance formula is exact, with the symmetric formula for w.

First consider d_G(v,t)<=2. Its source geodesic lifts after splitting with at most one additional buddy step, so it has length at most three. In the clean endpoint domain x,y outside B1_G(v), such a geodesic cannot use x-y. More generally, even if one allowed any non-v-incident cut edge, that edge could only occur as the second edge of a length-two geodesic; the new root reaches its exit endpoint directly or via its buddy in at most two steps. Thus all old near targets are safe for both new roots, including the possible cut damage.

Now take d_G(v,t)=3. Every old neighbour z of v has d_G(z,t)>=2, so the buddy's old B branch cannot cover t in its remaining one step. The u-root condition therefore reduces to

    t in B2_K(A) union B2_K(x) union B1_K(y).

Since a shortest old path starting at x and using x-y uses that edge first,

    B2_K(x) union B1_K(y)=B2_(G-v)(x).

A path of length at most two ending at this far target cannot pass through v. On S3_G(v), the right hand side is therefore exactly B2_G(x).

Similarly, an old A-to-t two-geodesic avoids v. If it is lost at x-y, it contains x, and its suffix places t in B2_G(x) already. Thus, on this far layer,

    B2_K(A) union B2_G(x)=B2_G(A) union B2_G(x).

This is precisely the displayed E_A condition. Exchanging A/B and x/y proves the E_B condition. Finally u,w are adjacent, so they cover one another automatically.

## A gate pass is not an old-old proof

For full acceptance, it suffices to run actual modified radius-three checks from the old root set

    S=[N_G(v) union B1_G({x,y})] minus {v},

and include the two children if not accepted through the exact gate. Both balls in this expression refer to the unchanged source.

If old p,q are outside S, a source path of length at most three cannot use v: each endpoint has old distance at least two from v, so such a path would have length at least four. It cannot use x-y either: both endpoints are outside the closed endpoint balls, giving length at least 2+1+2=5. A source path of length at most three is consequently retained verbatim. All other old pairs have a root in S, so the modified checks are complete, not symmetry samples.

There are five vertices in N_G(v). The closed radius-one balls of adjacent x,y have union size at most (5+1)+(5+1)-2=10. Hence |S|<=15, and the two children bring the complete root count to at most17. Remove v from the entire set before interpreting old roots, then treat its new u label separately.

The first testable question is whether any legal oriented edge has x covering the full E_A loss set and y the full E_B loss set. If no such edge exists over the frozen operation, the new-root stage closes that operation without constructing candidates. If one passes, its old-old distances remain a separate obligation handled by the preceding complete root set. No solver, enumeration, graph, actual diameter or ordinary bad-pair result is claimed here, and neither the earlier matching-insertion tests nor the plain split result is imported as an exclusion of this changed rule.
