# Independent all-pair and every-prefix proof: the actual G1 extensions at 90 and 94

The source is the already accepted actual G1, `../graph_d82_D3_n346516.edges`, with 346516 vertices and 14204970 edges. Its mathematical D3 acceptance is inherited from `../independent_acceptance/NOTE.md`; no old-root BFS, source H, finite-field or geometry validation was repeated. This proof uses source graph walks and the fresh literal role-neighborhood binding, not producer neighborhood caches.

## Actual interface bound in this batch

One fresh stream of G1 records its entire sorted edge body and extracts the **complete literal** neighbor set N_c of each first role c=342290+h, h=0,...,4225. The extraction checks that the roles are independent and every N_c is nonempty and lies below 342290, with pairwise disjoint neighbor sets. Their union has 342225 old vertices. The actual role degrees are 65 diagonal roles of degree 80, 4160 off-diagonal roles of degree 81, and the first hub role 4225 of degree 65. The complete template lists are saved in `PARENT_4226_ROLE_ACTUAL_NEIGHBORS.tsv`.

At degree 90 there are r=8 added blocks, and at degree 94 there are r=12. New vertex 346516+4226*copy+h must have exactly N_(342290+h), with copy in 0,...,r-1. Every candidate is streamed once. Old-old edges must match the freshly cached complete G1 body in order. Every new edge must have its old endpoint in the independently extracted N of its new role; its old endpoint must be below 342290. Strict sorted simplicity and the complete actual degree equal to |N_c| then imply equality of the full new neighbor set, rather than just inclusion. Every new vertex is checked, not a representative subset. There are no new-new edges.

These checks bind 33808 new vertices at degree 90 and 50712 at degree 94. All 14204970 parent edges are retained in each. The new edge counts are 2737800 and 4106700, respectively. Labels, headers, body counts, full vertex degrees and degree histograms were actually checked. No graph is obtained by extending the other new target or degree83.

## All pairs have a genuine walk of length at most three

Let x_c be any new copy of source role c.

* Old-old: use an already accepted G1 walk; every source edge remains.
* x_c to an old vertex v different from c: take a shortest G1 walk c-u-...-v, of length at most three, and replace its first edge c-u by x_c-u. The complete literal equality N(x_c)=N_G1(c) supplies the edge. Its interior vertices all remain in G1.
* x_c to its own old center c: choose any u in its nonempty N_c; x_c-u-c has length two.
* Two new copies of the same c: the same nonempty N_c supplies a common old neighbor and a length-two walk.
* Copies x_c and y_d of distinct centers: if a shortest source walk c-...-d has length two or three, replace both endpoints. If the source centers were adjacent, the general route x_c-d-c-y_d would have length three. Here actual source roles are independent with disjoint N, so their source distance is three, and endpoint replacement uses two G1 interior vertices.

Thus every old-old, old-new and new-new pair is covered. No future new copy is an interior vertex. The same argument applies after **any prefix** of the added copies; it does not infer a smaller graph's D3 by deleting vertices from a tested maximum graph. A new copy's entire fixed old N is added when that vertex is introduced.

For degrees, every old vertex belongs to at most one N_c. A prefix of r complete blocks adds load at most r to any old vertex. G1 has maximum degree 82, hence every prefix respects cap 82+r. Every new vertex has degree 65, 80 or 81. The final full literal degree checks establish exact maxima 90 and 94; the histograms are recorded in the per-target results.

## Exact diameter and what BFS measured

For two different source roles c,d, their copied vertices have no common neighbor because N_c and N_d are disjoint, and have no direct edge. The analogous new-hub to first-source-clone pair also has no direct edge and no common neighbor: both complete neighbor sets are two disjoint source-role N sets. Therefore these pairs cannot be at distance at most two. The preceding all-pair proof supplies distance at most three.

Within the authorized preselected last-block hub BFS, actual predecessor paths were

    380323 -- 342225 -- 5265 -- 342290
    397227 -- 342225 -- 5265 -- 342290.

Both were measured as distance three. These are genuine literal-edge paths and provide concrete nonD2 witnesses without any old-root BFS.

Ordinary BFS was run only from 68 preselected last-block new vertices per target: the 65 N80 roles fixed from G1 before either candidate was read, the fixed off roles h1 and h2, and hub h4225. Every measured root reached the entire graph in at most three and matched its saved full histogram prediction. The BFS also checked distance two to the parent same-role representative and every earlier repeated same-role copy. Among new vertices it found r-1 same-role twins at distance two and r*4225 other-role vertices at distance three.

There were **zero old-root BFS runs**. At degree90, 33740 other new roots were unmeasured; at degree94, 50644 were unmeasured. In each case this includes 4158 other off roles in the last block and every root in prior added blocks. Their D3 conclusion comes from the full literal neighbor binding and the walk proof above, not an assumed orbit, field translation, or extrapolation from 68 BFS roots. The three measured histogram distributions likewise describe only the roots actually tested.

## Scope and execution boundary

The fresh single-worker suite finished once with both targets PASS, 9.240740672 CPU seconds within 60, including recorded local preparation, compilation and validator/aggregation. The actual source G1 was parsed once and each candidate once. The suite imported no producer adjacency cache or generation function. It performed no old H/field/geometry/root-BFS/Lean/solver/paid-review work, no hashes and no additional parameter or copy count. Mathematical acceptance is supported for these two complete literal graphs; new Lean, external reviews, release/count updates and public-priority decisions are separate root-owned tasks. This batch changes no root state, Wiki, progress page or frozen archive.
