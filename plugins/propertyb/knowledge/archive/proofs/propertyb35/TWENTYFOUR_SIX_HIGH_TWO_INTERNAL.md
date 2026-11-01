# Twenty-four points: six high points and two internal edges

Let H be a finite simple five-uniform hypergraph on24 vertices, with at most35 edges, pair coverage and minimum degree at least7. Put P={v:d(v)>7}. Suppose |P|=6, no edge of H consists of five degree-seven vertices, and exactly two edges of H are contained in P. Then H has Property B.

No restriction on the noninternal P-trace sizes is imposed. The proof uses actual partial colorings and a seven-case excess budget; it does not enumerate hypergraphs or create a free higher-trace inventory.

## 1. The complete actual trace budget

Six high points and minimum degree7 give5|H|≥7·24+6=174. Since |H|≤35, necessarily |H|=35. The total degree excess over7 is7, so the P degrees are one9 and five8. Write h for the unique degree-nine point. All18 points of L=V−P have degree7.

P hits every edge. Indeed an edge avoiding P would consist entirely of degree-seven points, contrary to the hypothesis. Thus every P-trace is nonempty.

The two different internal five-edges are P−{a} and P−{b} for distinct a,b∈P. Set C=P−{a,b}, of size4. A C point belongs to both internal edges; a,b each belong to one. Since the P degree sum is49,

Σ_(e∈H)(|e∩P|−1)=49−35=14.

The two internal edges use8 units. There is no other trace of size5, since that would be another internal edge. If n_j counts noninternal size-j traces for j=2,3,4, then

n_2+2n_3+3n_4=6.

The singleton-trace count is N_1=33−n_2−n_3−n_4. The complete list is:

| n_2 | n_3 | n_4 | N_1 |
|---:|---:|---:|---:|
|6|0|0|27|
|4|1|0|28|
|3|0|1|29|
|2|2|0|29|
|1|1|1|30|
|0|3|0|30|
|0|0|2|31|

For example the list follows by n_4=0,1,2 and then n_3=0,…,floor((6−3n_4)/2), with n_2 forced. Repeated higher P-traces at different original edges keep their indices.

## 2. Actual signed constraints and the repair results used

We choose a single point q∈C blue and every other P point red in each branch below. Both internal edges are then proper. A noninternal higher trace containing q has both fixed colors and is proper; a missed triple gives its exterior pair as a negative constraint, and a missed four-trace gives its exterior singleton. Pair traces incident with q are proper; the others give negative exterior triples. The private singleton-trace edges of q give positive exterior four-sets, and all other private edges give negative exterior four-sets.

Let k be the number of higher-trace indices containing q, and s its pair-trace degree. The private positive count is exactly

m=d(q)−2−k−s.

The private negative-four count is N_1−m. For each resulting signed system the positive and negative source edges are disjoint, so every outer point's combined indexed occurrence is at most7. There is no omitted zero-P edge, because P hits H.

We use these proved facts:

- [Five-positive signed repair](FIVE_POSITIVE_SIGNED_REPAIR.md), Corollary A: at most five positive four-sets, at most four negative triples and at most28 negative four-sets, with occurrence at most10, are repairable.
- Its strengthened Corollary B: at most five positives of sizes3 or4, at most two negative triples and at most28 negative four-sets, with occurrence at most10, are repairable. The two-negative-triple version is proved directly there; its padding allowance raises at most10 original occurrences to at most14.
- [Five small positive sets](FIVE_SMALL_POSITIVE_ZERO_TRIPLE.md): at most five positives of size at least2 and negative four-sets only, with combined occurrence at most7, are repairable, without a negative-count bound.
- [Six-positive, six-negative-triple repair](SIX_POSITIVE_SIX_TRIPLES_REPAIR.md): at most six positive four-sets, at most six negative triples and at most35 negative four-sets, with occurrence at most7, are repairable on any finite ground set. Its proof is entirely analytic.

If a negative pair or singleton is met by a chosen forbidden exterior point, keep that point blue. Delete the forbidden point from each positive set and discard every negative constraint containing it. One forbidden point leaves positive sizes3 or4; two leave sizes at least2. Occurrence only decreases. A discarded negative is already avoided; it must not be replaced by a smaller negative remainder.

A repaired R⊆L will be colored red, with all other exterior points blue. Hitting every positive constraint prevents its source edge from being all blue; not containing any negative constraint prevents its source edge from being all red. Edges already proper under the fixed P colors stay proper. This is the actual link from each repair to a coloring of H.

## 3. Pure pair traces

For(n_2,n_3,n_4)=(6,0,0), C has four points and only one point of all P has degree9. Choose any degree8 point q∈C, of which there are at least three, and color it blue. Let s be its number of pair-trace source edges. Both internal edges are proper, and every pair trace through q is mixed and proper.

The exact signed counts are

m=8−2−s=6−s positive four-sets,
6−s negative triples,
27−m negative four-sets.

Each is nonnegative because it counts actual source edges. No higher trace occurs and P hits every edge, so these are all remaining monochromatic risks. The exterior indexed occurrence bound is7 by §2. The six-positive repair theorem therefore colors this entire inventory, without a matching, attachment, star or local graph classification. A standalone form is [the single-blue-point short proof](TWENTYFOUR_SIX_HIGH_TWO_INTERNAL_PURE_PAIR_SHORT.md).

## 4. Exactly one higher trace

First suppose n_3+n_4=1, and let T be its P-trace. If an eight-degree point q lies in C∩T, choose it blue. Then

m=8−2−1−s=5−s≤5.

The higher-trace edge is proper. There are at most n_2−s≤4 negative triples, and the private negative-four count is at most27: for the triple case n_2=4,N_1=28 and m≥1; for the four-trace case n_2=3,N_1=29 and m≥2. Corollary A repairs H.

A four-trace has at least two C points, so it always contains such an eight-degree q. A triple has at least one C point. If it has no eight-degree C point, necessarily h∈C and T={h,a,b}. Choose q=h. Its positive count is m=9−2−1−s=6−s. When s≥1 this is at most5, there are at most3 negative triples, and the private negative-four count is at most26; Corollary A applies.

When s=0, the exact system is six positive four-sets, four negative triples and22 negative four-sets, with occurrence7. The six-positive theorem in §2 applies. This closes both one-higher-trace inventories, including the exceptional degree-nine point.

## 5. Two higher four-traces

Here(n_2,n_3,n_4)=(0,0,2), N_1=31. Choose an eight-degree q∈C in one of the four-traces, possible because that trace contains at least two C points.

If q is in both, there are m=4 positive four-sets, no negative triple or smaller constraint, and27 private negative four-sets; Corollary A applies.

If q misses the other four-trace, there are m=5 positives and26 private negative four-sets. The missed four-trace contributes one negative singleton. Forbid its point. The remaining five positives have sizes3 or4 and all remaining negatives are four-sets, at most26. Corollary B applies. This closes the two-four-trace inventory without requiring a common C point.

## 6. One higher four-trace and one higher triple

Here(n_2,n_3,n_4)=(1,1,1), N_1=30. Choose an eight-degree q∈C in the four-trace.

If q also lies in the triple, both higher edges are proper. Then m=4−s≤4, at most1−s≤1 negative triple remains, and there are at most27 private negative four-sets. Corollary A applies.

Otherwise the missed higher triple gives one negative pair. We have m=5−s≤5, at most1−s≤1 negative triple from the pair-trace edge, and at most26 private negative four-sets. Forbid one point of the negative pair, and apply Corollary B to the positive3/4 sets. This closes the mixed higher-trace inventory.

## 7. Two higher triples

Here(n_2,n_3,n_4)=(2,2,0), N_1=29. If either higher triple contains an eight-degree point q∈C, choose that q blue.

If q lies in both, m=4−s≤4, at most2−s≤2 negative triples remain, and at most27 private negative four-sets remain. Corollary A applies.

If q lies in exactly one, m=5−s≤5, and the missed higher triple gives one negative pair. There are at most2−s≤2 negative triples and at most26 private negative four-sets. Forbid one endpoint of the negative pair. Corollary B, with its two-negative-triple allowance, applies.

If neither higher triple has an eight-degree C point, their C-intersections must both be{h}, so h∈C and both indexed P-traces are{h,a,b}. Choose q=h. Both higher edges are proper. Now m=9−2−2−s=5−s≤5, at most2−s≤2 negative triples remain, and at most26 private negative four-sets remain. Corollary A applies. Repeated P-traces are allowed here; the original edges retain their different exterior parts and indices.

## 8. Three higher triples

Here(n_2,n_3,n_4)=(0,3,0), N_1=30. Suppose an eight-degree q∈C belongs to at least one higher triple, and choose it blue. If k∈{1,2,3} higher indices contain q, then

m=8−2−k=6−k≤5.

Exactly3−k≤2 higher triples are missed and give negative exterior pairs. Choose one forbidden point from each such pair, forming a set F of size at most2. Every missed-pair constraint is avoided. Remove F from each positive four-set; each remains of size at least2. There are no pair-trace negative triples. All remaining negatives are private four-sets, at most30−m≤27. The five-small-positive theorem repairs the reduced system, with occurrence at most7. Its R avoids F and hence repairs all original constraints.

If no higher triple contains an eight-degree C point, all three indexed P-traces are{h,a,b}, with h∈C. Choose q=h. All higher edges are proper, m=9−2−3=4, and the only negatives are26 private four-sets. Corollary A applies.

This closes the last inventory.

## 9. Conclusion and checks

The seven trace inventories of §1 are exhaustive and each has been colored. Every fixed P coloring makes both internal edges proper, every missed higher edge is explicitly retained as a small negative and then avoided, and the final signed repair accounts for every other original edge. Therefore H has Property B.

The actual source-edge occurrence bound is always7; the five-positive corollaries use their proved padding slack to reach the abstract bound14, and the small-positive theorem uses no padding. No counting of hypothetical H realizations is used. The pure-pair case now uses §3's single-blue-point argument; all six higher-trace inventories use the direct choices above. The former matching-and-attachment proof and its exact replays remain valid alternative evidence, but they are not dependencies of this proof.

The compact check [HIGH_TRACE_CALLER_CHECK.py](../../context/propertyb35-paper/round01/twentyfive/k6_two_internal/HIGH_TRACE_CALLER_CHECK.py) restores all stated private counts and negative-triple counts from the seven excess patterns and selected degree/higher-incidence/pair-incidence parameters. [FIVE_SMALL_CHECK.json](../../context/propertyb35-paper/round01/twentyfive/k6_two_internal/FIVE_SMALL_CHECK.json) records the strict numerical branches of the two additional repair lemmas. Their mathematical proofs are in the cited canonical sources. The general random-transversal proof and its new double-point budget are independent of the original hypergraph and retain negative indices. This complete branch proof uses only general probability inequalities and analytic candidate counts, with no finite graph catalogue dependency.

This theorem closes exactly the24-point, six-high-point, two-internal-edge branch under the stated pair-cover/minimum-degree/no-full-seven hypotheses. It does not assert coverage of one or three internal edges, seven high points, or arbitrary noncritical H lacking those structural hypotheses.
