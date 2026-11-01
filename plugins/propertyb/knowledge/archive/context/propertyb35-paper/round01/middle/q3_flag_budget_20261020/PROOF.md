# A common flag budget for the Γ-degree-three exceptions

## Actual scope and the finite local input

Let H be a hypothetical non-B A2/A3 input on21 vertices with35 distinct five-edges: it covers point-pairs, has a unique degree-six point, exactly two or three degree-seven points, all other degrees at least eight, and global high-degree excess Σ_v max(d_H(v)−9,0)≤4. Import the already supplied strong-pair reduction λuv≤4. Define Γ on the35 original edges by adjacency when intersection size is not one, and let nj count original edge pairs intersecting in j points. Let τ=Σ_{uv} C(λuv−1,2), which is nonnegative because of pair covering.

The existing [complete qΓ=3 direct-repair diagnosis](../three_nonunit_direct_repair_20261020/PROOF_CHECK.md) represents an original Γ-degree-three edge F by the three exceptional traces T1,T2,T3⊆F; all other31 original edges meet F once, with actual attachment counts ai summing to31. Its completed91-trace-orbit/119-attachment tail analysis, filtered by minimum degree six, at most one degree-six point and selected high excess at most four, leaves83 necessary attachment keys on16 trace orbits. If an actual input lies outside that tail, the already strict direct-coloring entry colors H. Thus every degree-three F in the present non-B input must lie in that83-key domain.

For such F define

\[
f_F=\sum_{1\le i<j\le3}\binom{|T_i\cap T_j|}{2}.
\]

This counts a point-pair in F and an unordered pair of its three exceptional neighbors containing that pair. It is invariant under relabeling F and under permuting the exceptional original edges, including equal traces with different original edge indices.

Direct exact evaluation of all83 keys finds only one zero-flag key, represented by

\[
(T_1,T_2,T_3)=(3,13,22),\qquad
(a_0,\ldots,a_4)=(6,6,7,6,6),
\]
\[
(d_0,\ldots,d_4)=(9,9,10,8,8).
\tag{1}
\]

The traces are {0,1},{0,2,3},{1,2,4}, so their sizes are(2,3,3) and pairwise intersections have size one. The degree formula is the actual identity di=1+ai+#{j:i∈Tj}. This key has exactly one degree-ten point, two degree-eight points and two degree-nine points. The other82 keys all have fF≥1. [SOURCE_AUDIT.json](SOURCE_AUDIT.json) retains every scored key, not merely the zero-key count; CHECK.py independently computes the same scores by summing over point-pairs instead of trace-pair intersection sizes.

## A joint bound on the number of degree-three edges

Let z3 be the number of original edges with Γ-degree exactly three. Divide these into positive-flag and zero-flag edges.

A positive-flag edge F contains a point-pair P that also belongs to two distinct exceptional original neighbors. Thus λP≥3. The number of such original F is at most the total number of original-edge/point-pair incidences with λP≥3:

\[
\#\{F:q_\Gamma(F)=3,\ f_F\ge1\}
\le\sum_{P:\lambda_P\ge3}\lambda_P
\le3\tau.
\tag{2}
\]

The last termwise inequality holds because λP=3 gives3=3C(2,2), and λP=4 gives4≤3C(3,2)=9. Point-pairs of codegree one or two contribute to neither side of this charge. This is a shared budget on the same H: an original edge may have several flags, but it is counted only once on the left, while the incidence sum safely overcounts it. No flags are chosen independently for different edges.

Every zero-flag edge has the actual pattern(1). It has exactly one exceptional Γ-neighbor intersecting it in two points. Counting endpoints of the n2 original intersection-two pairs gives at most2n2 such zero-flag edges. Also let h10, b8 and c9 be the numbers of original points of degree exactly ten, eight and nine. Their total edge incidences respectively give

\[
\#\{F:q_\Gamma(F)=3,\ f_F=0\}
\le10h_{10},\quad\le4b_8,\quad\le\left\lfloor\frac{9c_9}{2}\right\rfloor.
\]

The factors4b8 and floor(9c9/2) use two points of each degree in every such original F, not two independently selected copies. Combining these simultaneous necessary bounds with(2) proves

\[
\boxed{z_3\le3\tau+
\min\left(2n_2,10h_{10},4b_8,
\left\lfloor\frac{9c_9}{2}\right\rfloor\right).}
\tag{3}
\]

Without the degree-class resource refinements the weaker bound z3≤3τ+2n2 follows. No assertion about the presence or absence of a codegree-four pair inside a degree-three edge is needed.

## Fixed-count degree-box capacity; no DP

Retain the preceding necessary-source imports3≤qΓ(F)≤29 from the generic minimum-degree-three repair and edge-critical singleton-neighbor lower bound. These imports, along with the n4≤13 paper-local structural cap, are the scope of the frozen5813-source aggregate domain used below; this note does not re-prove their earlier local theorem imports.

Put E=|E(Γ)|=595−n1. For a fixed possible integer m=z3, exactly m original edges have Γ-degree three and the remaining k=35−m have degrees in{4,…,29}. Their excess above four is

\[
X=2E-3m-4k.
\]

The fixed-count box is infeasible unless0≤X≤25k. Otherwise write X=25a+b,0≤b<25. Since g(q)=f(34−q) is discrete convex, filling degrees at the endpoints4 and29 maximizes its sum. More explicitly, transferring one unit between two interior degrees toward the extremes cannot decrease the convex objective. Consequently the maximum over this degree-sum relaxation is

\[
B(E,m)=m f(31)+a f(5)+f(30-b)+(k-a-1)f(30)
\tag{4}
\]

when a<k, and m f(31)+k f(5) when a=k (then b=0). These are the degree multiset3^m,29^a,(4+b),4^(k−a−1), with the partial entry omitted in the all-saturated case. There is no claim that the multiset is realizable by a graph or H.

If Z is the right side of(3), the actual m is one of the integers0,…,min(Z,35). Thus

\[
P\le\max_{0\le m\le\min(Z,35)\atop0\le X\le25(35-m)}B(E,m).
\tag{5}
\]

This checks at most36 scalar formulas; it is not a graph-degree DP. We take the minimum with every saved P bound, then reallocate the same capacities and weights from the existing moment filter. All previously excluded keys remain excluded because P never increases.

## Complete frozen-domain results

The input is precisely all5813 keys from [the conditional critical re-sieve](../a2_a3_joint_moment_frontier_20261020/CONDITIONAL_CRITICAL_RESIEVE.md). The two modes give:

|q3 bound used|Degree-labeled survivors|Distinct moment keys|n4 range|τ range|Minimum surviving L−2722720|
|---|---:|---:|---|---|---:|
|3τ+2n2|4534|3245|0–13|0–28|8|
|Full bound(3)|3805|2825|0–13|0–28|8|

The first count agrees exactly with the parent's independent4534 count. All sixteen degree spectra still have survivors. Per-spectrum counts are:

|a7|a8|High-excess partition|Pair resource only|All four resources|
|---:|---:|---|---:|---:|
|2|7|empty|37|22|
|2|8|1|63|60|
|2|9|1+1|110|109|
|2|9|2|155|100|
|3|5|empty|63|39|
|3|6|1|109|101|
|3|7|1+1|155|153|
|3|7|2|221|148|
|3|8|1+1+1|221|221|
|3|8|1+2|281|259|
|3|8|3|460|333|
|3|9|1+1+1+1|291|285|
|3|9|1+1+2|388|379|
|3|9|1+3|582|528|
|3|9|2+2|474|341|
|3|9|4|924|727|

The largest remaining family is the last spectrum, with727 aggregate keys. A closest witness after all resources is in spectrum6,7²,8⁹,9⁸,11 (W=652,e=2):

\[
(n_0,n_1,n_2,n_3,n_4)=(35,518,0,34,8),\quad\tau=10.
\]

Since n2=0 and h10=0, its zero-flag allowance is zero and Z=30. The degree-box maximizer uses m=30, one degree29, one degree23 and three degree4 entries, giving

\[
P\le30f(31)+f(5)+f(11)+3f(30)=12658.
\]

Its middle capacities are(1155,13849,0,476,32); the maximizing allocation is(0,12150,0,476,32), with L=2722728, a margin of eight above the strict repair threshold. This is an exact relaxation witness, not a realization or a non-B hypergraph. It explains why the joint q3 flag budget alone is still insufficient to close these spectra.

## Evidence and independent full-key replay

[FILTER.py](FILTER.py) computes the83 source scores, verifies the unique zero-flag key, and re-filters the5813 saved inputs in both modes using the explicit fixed-count formula(4). [RESULT.json](RESULT.json) records every per-spectrum count and extremal witness. The two SURVIVORS files retain all4534/3805 surviving full keys and allocations. Measured CPU0.090931 seconds.

[CHECK.py](CHECK.py) independently reconstructs the83 scores by point-pair enumeration. For each possible m it builds an explicit35-entry degree list, distributes X units subject to the degree29 cap, checks the degree count/sum/bounds, and computes f by five-group pair products rather than the discovery's closed formula. On every5813 source it then recomputes the greedy middle allocation and exact objective. Every surviving full key agrees in both modes, and all sixteen per-mode counts agree. [CHECK.json](CHECK.json) is PASS, CPU0.702723 seconds.

The mathematical contribution is the common original-H budget(3); the finite re-sieve is only a necessary-domain diagnosis. The local83-tail import, earlier source/critical imports and n4 bound have not been silently upgraded or replaced. No original-H, free-set, negative-layout or new DP search was performed. This is same-family/provisional checking, not an A2/A3 or global Property-B closure claim.
