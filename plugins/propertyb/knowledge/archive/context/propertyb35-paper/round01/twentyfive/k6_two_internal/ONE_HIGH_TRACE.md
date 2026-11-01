# Six high points, two internal edges, exactly one higher noninternal trace

Use the same actual24-point35-edge hypotheses as the pure-pair theorem: H is simple, pair-covering, δ≥7, P={d>7} has size6, and no edge is full-seven. Consequently P hits every edge, its degree pattern is one9 and five8, and its complement L consists of18 degree-seven points. The two internal edges are P−{a},P−{b}, with common C=P−{a,b} of size4.

Assume exactly one noninternal edge has P-trace T of size j∈{3,4}; all other noninternal traces have size1 or2. All cases of this one-higher-trace branch are now colored below. The complete two-internal-edge theorem, including every higher-trace inventory, is [TWENTYFOUR_SIX_HIGH_TWO_INTERNAL.md](../../../../../proofs/propertyb35/TWENTYFOUR_SIX_HIGH_TWO_INTERNAL.md).

The two internal edges use8 of the total14 units of multitrace excess. T uses j−1 of the remaining6, so the number of pair-trace edges is7−j: four if j=3 and three if j=4. The private singleton-trace edge count is

35−2−1−(7−j)=25+j,

namely28 or29. Let s_q count pair-trace incidences at q.

## 1. An eight-degree point in C∩T colors H

If q∈C∩T has degree8, color q blue and all other P points red. Both internal edges and the higher-trace edge are proper. Pair-trace edges incident with q are also proper. The private positive four-set count is

m=8−2−1−s_q=5−s_q≤5.

The remaining pair traces give7−j−s_q≤4 negative triples. Private edges at all other P points give25+j−m negative four-sets, at most27: for j=3, s_q≤4 implies m≥1; for j=4, s_q≤3 implies m≥2.

All signed constraints come from disjoint indexed original edge families and every exterior point has degree7. Corollary A of [FIVE_POSITIVE_SIGNED_REPAIR.md](../../../../../proofs/propertyb35/FIVE_POSITIVE_SIGNED_REPAIR.md) applies, with its justified padding allowance for at most five positives. P hitting every original edge ensures that no zero-P or opposite-sign bad event is omitted. Therefore H is colorable.

For j=4, |C∩T|≥2, and at most one C point has degree9; thus such an eight-degree q always exists.

For j=3, |C∩T|≥1. The only way to have no eight-degree point in the intersection is that the unique degree-nine point h lies in C and

T={h,a,b}.

This follows directly from |P−C|=2 and |T|=3, without a local trace enumeration.

## 2. The exceptional triple trace

Suppose T={h,a,b} with h∈C the unique nine-degree point. Color h blue, the other P points red. The two internal edges and the higher-trace edge are proper. The private positive-four count is now

m=9−2−1−s_h=6−s_h.

If s_h≥1, then m≤5, at most4−s_h≤3 negative triples remain, and the private negative four-set count is28−m≤26. The same five-positive repair theorem colors H.

For s_h=0 the exact signed system is:

- six positive four-sets, from the six private h-edges;
- four negative triples, from all four pair-trace edges;
-22 negative four-sets, from the other private edges;
- ground L of size18 and total indexed occurrence at every point at most7.

There is no negative pair: the unique higher-trace edge already contains both fixed P colors and gives no constraint. No freedom to replace these signs or add new vertices is assumed.

There is also an actual coverage fact. The six positive four-sets and the exterior two-set of the higher-trace edge collectively cover all18 exterior points, by pair coverage with h. Hence the union of the six positive four-sets has size at least16, so their repeated-incidence surplus is at most24−16=8. The higher-trace exterior two-set is an already proper source edge, not a new signed constraint; at either of its points, positive-plus-negative occurrence is at most6 rather than7. These strengthenings are recorded as actual input facts. Section A of [SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md](../../../../../proofs/propertyb35/SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md) now proves that the six-positive/four-negative-triple/22-negative-four system is repairable without needing those strengthenings.

Thus every one-higher-trace shape is colored, including the exceptional six-positive interface. The counted interface came from the same actual H; its repair theorem applies to a larger signed-set class and does not require a converse hypergraph realization claim.

`ONE_HIGH_TRACE_CHECK.py/json` verifies all70 labeled location/trace-set choices for j=3,4 under the two roots h∈C or h∉C, identifies exactly the exceptional T, and checks the signed integer counts for every possible selected-center pair-trace degree. It enumerates no outer edges.
