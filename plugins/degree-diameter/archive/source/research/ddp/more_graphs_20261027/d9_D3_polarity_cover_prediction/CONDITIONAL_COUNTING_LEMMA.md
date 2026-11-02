# Conditional obstruction for the585-point source: NOT YET APPLIED

Status: conditional deduction only. Actual585 source/degree/port/block-system hypotheses are being independently tested; do not report a theorem about the source until those tests or an inherited authoritative proof establish them. This does not settle N(9,3).

Hypotheses on the old max9,D3 graph G:
- P consists of65 degree8 vertices, every other vertex T has degree9, |T|=520.
- Distinct ports in P have old distance3; each t in T has exactly one neighbor p(t) in P.
- For each t define S(t)=P intersect R2_G(t). The520 sets S(t) form a3-(65,9,1) design. Thus each port occurs72 times, each pair9 times, and each triple once.

Claim, conditional on these hypotheses: no finite connected max9,D3 graph can contain G while preserving all of its old edges and adding at least one vertex. This excludes arbitrary helper graphs and arbitrary added old-old edges, not merely one-star choices. It does not exclude edge deletions or unrelated graphs.

Why old-old additions cannot help. Every old core vertex is saturated, every port has one free slot. Take a shortest new-to-port path of length<=3 and its last new vertex; its first old vertex q must be a port whose free slot is consumed by this new-old edge. If its final port p differs from q, the remaining old segment has length<=2. It cannot use an added port-port edge at q (q has no slot), or after one old step (no two ports have an original common neighbor). All-original length<=2 is forbidden by dist(P,P)=3. Consequently each port must have its own new neighbor. All65 free slots are then consumed, so no added old-old edge can occur.

Let H be the induced graph on all new vertices and choose a vertex x of minimum H-degree r,0<=r<=9. It attaches to a<=9-r ports A. Each H-neighbor has H-degree>=r and hence attaches to at most9-r ports. The union B of their port attachments has size<=r(9-r).

For an old core target t, any <=3 path from x must either enter old G directly at A and then use at most2 old edges, or go via an H-neighbor to B and use one old edge. Therefore t must satisfy S(t) intersects A, or p(t) lies in B. No alternative short route has been discarded.

Bonferroni through triples, using the actual3-design, bounds the first class by
 U(a)=72a-9*C(a,2)+C(a,3).
This polynomial is increasing for0<=a<=9. The second class contains at most8|B| targets, because each port has8 old core neighbors. Thus all reachable old core targets number at most U(9-r)+8*r*(9-r). The table below is strictly less than520 in every row.

|r|a upper bound|U(a)|neighbor-star upper bound|total bound|
|---:|---:|---:|---:|---:|
|0|9|408|0|408|
|1|8|380|64|444|
|2|7|350|112|462|
|3|6|317|144|461|
|4|5|280|160|440|
|5|4|238|160|398|
|6|3|190|144|334|
|7|2|135|112|247|
|8|1|72|64|136|
|9|0|0|0|0|

Maximum462, leaving at least58 core targets unreachable from a minimum-H-degree new vertex. Contradiction. The key hypothesis is the exact port2-neighborhood3-design, not spare counts alone.

Prediction/test: acquire or reuse current primary585 graph; verify the three hypotheses using only necessary local neighborhoods and triple counts, without rerunning old all-source diameter. If any hypothesis fails, preserve the failed prediction and do not apply this lemma. If already answered in the sole Wiki, inherit that answer and do not recount it as new. If the hypotheses hold, avoid starting an arbitrary helper search on this source and prioritize constructions that change old edges or use another source.
