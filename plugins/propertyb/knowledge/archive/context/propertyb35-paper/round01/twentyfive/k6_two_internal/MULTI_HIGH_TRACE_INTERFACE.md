# Multiple higher traces with two internal P edges

The complete result is now [TWENTYFOUR_SIX_HIGH_TWO_INTERNAL.md](../../../../../proofs/propertyb35/TWENTYFOUR_SIX_HIGH_TWO_INTERNAL.md). Its two-negative-triple five-set lemma and five-size-at-least-two lemma remove the limitations of the sufficient callers recorded here; this interface note is not the current remaining-branch list.

Use the actual six-high-point setting of the pure-pair theorem:24 vertices,35 simple five-edges, pair coverage, minimum degree7, no full-seven edge, six high points P with degrees(9,8,8,8,8,8), and exactly two internal edges P−{a},P−{b}. Put C=P−{a,b}, |C|=4. P is a hitting set, and L=V−P consists of18 degree-seven points.

Let n_j count noninternal traces of size j, j=2,3,4. The remaining multitrace excess gives

n_2+2n_3+3n_4=6.

With at least two higher traces, the only possible(n_2,n_3,n_4) are

(0,0,2), (1,1,1), (2,2,0), (0,3,0).

Higher-trace multiplicities retain their original edge indices, even if their P-traces coincide. For q∈C let h_q count its higher-trace incidences and s_q its pair-trace incidences. A single-blue q gives

m=d(q)−2−h_q−s_q

private positive four-sets. Pair traces avoiding q give negative triples. A missed higher triple gives a negative exterior pair; a missed higher four-trace gives a negative exterior singleton. A higher trace containing q is already proper.

Every use below retains these small negative constraints explicitly. If a single negative singleton or pair is avoided by forbidding a vertex x in R, delete x from each positive four-set, giving sizes3 or4, and discard entire negative constraints containing x. Do not shrink and keep a forbidden-point negative constraint. This operation preserves occurrence bound7. The five-positive Lemma B with its stated padding slack applies when at most one negative triple remains.

## 1. A common C point always suffices for multiple higher traces

If some q∈C belongs to every higher trace, choose it blue. Since there are at least two higher traces, even the nine-degree case has m≤9−2−2=5. All higher edges are proper; at most n_2≤2 negative triples remain. The private negative-four count is at most27, by substituting the four inventory patterns above. Thus five-positive Lemma A repairs H.

No eight-degree restriction is needed in this multiple-higher-trace common-intersection case. In particular any nonempty C∩(intersection of all higher traces) is sufficient.

## 2. Two higher four-traces: complete subbranch

Each four-trace has at least two C points, so choose an eight-degree q∈C in one of them. If it belongs to both, §1 applies. Otherwise the other four-trace gives exactly one negative singleton. There are no pair traces and no higher triples. The private positive count is8−2−1=5, and the private negative-four count is31−5=26. Forbid the singleton point. Five positives now have sizes3 or4, there are no negative triples, and there are at most26 negative four-sets. Five-positive Lemma B repairs H.

Hence the full(n_2,n_3,n_4)=(0,0,2) subbranch is colored, without assuming a common C point.

## 3. One higher four-trace and one higher triple: complete subbranch

Choose an eight-degree q∈C in the four-trace; such a point exists. If it also lies in the triple, all higher edges are proper and §1 applies. Otherwise the triple gives one negative exterior pair. There is one pair trace, so at most one negative triple arises from it. The private positive count is5−s_q≤5, and private negative-four count is30−(5−s_q)≤26. Forbid one endpoint of the negative pair and apply five-positive Lemma B to the resulting positive3/4 system, with at most one negative triple. Thus(n_2,n_3,n_4)=(1,1,1) is also colored.

## 4. Two higher triples and two pair traces: useful sufficient callers

A common C point is handled by §1. Even without such a point, it suffices that a C point q lying in exactly one higher triple has s_q≥1. Its degree may be8 or9: then m≤9−2−1−1=5. The other higher triple gives one negative pair, while only2−s_q≤1 pair traces give negative triples. The private negative-four count is at most26. Forbid one endpoint of the negative pair and apply five-positive Lemma B.

Thus a remaining necessary configuration in this inventory must have disjoint nonempty C-intersections of the two higher triples, and every C point in their union must have pair-trace degree zero. This is a precise structural boundary, not a claim that such parameters extend to H. Without an incidence relation between the missed higher-trace exterior pair and the two pair-trace exterior triples, merely forbidding one point need not reduce the two negative triples to the one allowed by Lemma B.

## 5. Three higher triples and no pair traces: useful sufficient caller

If a C point q occurs in at least two higher triples, choose it blue. There are at most five private positives, no pair-trace negative triples, and at most one missed higher triple. If none is missed, Lemma A applies. If one is missed, forbid one endpoint of its negative exterior pair and apply Lemma B. The private negative-four count is at most27.

The remaining necessary configuration has each C point in at most one higher triple. Their three nonempty C-intersections are therefore pairwise disjoint. Since |C|=4, their size multiset is(1,1,1) or(2,1,1). In the first case all triples contain a,b. In the second case the unique two-C trace contains one of a,b and the other two triples contain both, so all three share that same missing point. This common point lies outside C, and coloring it blue alone leaves one of the two internal P edges red. Thus the single-blue common-C caller is genuinely unavailable in these remaining configurations. A two-blue or other repair argument is still needed here.

## 6. Scope

The statements above are direct actual-H coloring callers using the canonical five-positive repair lemmas and one forbidden exterior point. No higher-trace inventory table, outer-pivot enumeration or realizability claim is used. They completely color the two inventories containing higher four-traces and give explicit sufficient conditions and remaining structures for the two-triple and three-triple inventories. They do not claim the full two-internal-edge branch with arbitrary higher traces is closed.
