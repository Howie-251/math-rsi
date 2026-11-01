# Four remaining positives: a surviving three-point repairs the whole kernel branch

## Complete subtheorem

In the ten-positive system described below, suppose x,y are positive three-points with disjoint positive-label supports. Let Z collect the third points of all original negative triples containing both x,y. If, after forbidding Z, the four unhit positive sets still have a point z of positive occurrence three, the original signed system repairs. This covers n=0,1,2. It is not asserted merely from the existence of three disjoint positive three-stars: the surviving-point premise includes z∉Z and can fail when a negative triple is{x,y,z}.

## A general small auxiliary gate

On any finite ground set, suppose there are at most four indexed positive sets, each of size at least three, at most one negative pair, at most three negative triples, and any number of negative four-sets. If total indexed occurrence at each point is at most seven, the system repairs.

If there is a negative pair, fix either endpoint f blue. That entire pair constraint is now satisfied; **every** negative constraint containing f is satisfied and removed as an indexed constraint, rather than shortened. Delete f from each positive set; every positive still has size at least two. Other negative constraints retain their original sizes. The total occurrence of every unfixed point does not increase. Apply [FOUR_SMALL_POSITIVE_THREE_TRIPLE_REPAIR](../../../../../../proofs/propertyb35/FOUR_SMALL_POSITIVE_THREE_TRIPLE_REPAIR.md). If there is no negative pair, apply that theorem directly. This proves the auxiliary gate; no ground or negative-four count bound is required.

## Actual two-kernel interface

Consider the proposed ten-positive system on at most18 points, with maximum original positive occurrence three, at most two negative triples and18 negative four-sets, total occurrence seven. Let x,y be three-points whose positive-label support triples are disjoint. Fix x,y red. Exactly four positive four-sets remain, all avoiding x,y. The two kernel points have total negative incidence at most eight.

Let n be the number of original negative triples containing both x,y. Each such index has form{x,y,p}; let Z be its third-point set and fix Z blue. Index counts are retained even when third points repeat. This removes the **whole** negative indices containing Z, while positive sets lose their Z points. For the direct arguments below n is0 or1, so |Z|=n and the four positives still have size at least4−n. The final section handles n=2 by choosing a different kernel before fixing any blue point.

Suppose a point z outside Z still belongs to three of these positive sets. Its original positive occurrence is exactly three, so it belongs to exactly those three remaining original positives. In particular the fourth original positive A avoids z, and all original positives hit by x/y avoid z as well. Write A′=A\Z, m=|A′|≥4−n.

For each a∈A′ the four-point red set{x,y,z,a} hits every original positive. It avoids all negative triples containing both kernels, since those contain a fixed blue point of Z. If any such red set is legal, the repair is complete.

Otherwise select one actual blocking index for each a. The only possible blockers are an original triple containing exactly one kernel and the two points z,a, or the original four-set{x,y,z,a}. Each index blocks at most one a, so the selected m blockers are distinct. If s are triples, then s≤2−n and the other m−s are four-sets. These indices contain z and are disjoint from the n already removed original two-kernel triples. Their kernel incidences total

s+2(m−s)=2m−s.

After discarding these selected blockers, the remaining total kernel-negative incidence is at most

K=8−2n−2m+s≤s,

using m≥4−n. The number of remaining original negative triples is at most2−n−s. Now turn z blue. All selected blockers are satisfied and removed; any other negative index containing z is also entirely removed, only improving both bounds. The four remaining positive sets are shortened by Z∪{z}; each was an original four-set.

## n=0: one possible negative pair is necessary to retain

Here m=4. All four selected blockers contain z, and az=3 gives z-negative capacity at most four. Hence these four indices exhaust its negative capacity: no other negative index contains z. Three original positives become triples and A remains a four-set.

Remaining negative constraints, after the fixed red kernels are removed, have these exact possible origins:

- an original triple with one kernel gives a negative pair;
- an original triple with neither kernel gives a negative triple;
- an original four-set with both kernels gives a negative pair;
- an original four-set with one kernel gives a negative triple;
- an original four-set with neither kernel remains a negative four-set.

There are no remaining original triples with both kernels, by n=0. For s=0,1,2 the shared remaining budgets are K≤s and remaining original triples≤2−s.

|s|Remaining possible small negative constraints|
|---:|---|
|0|No kernel incidence remains; at most two original triples avoiding kernels give N3≤2, N2=0|
|1|Either a single one-kernel original triple gives N2=1 and exhausts both remaining triple and kernel budgets; or no such triple remains, with at most one one-kernel four-set and one kernel-free triple giving N3≤2; a two-kernel four-set is impossible|
|2|No original triple remains. At most one two-kernel four-set gives N2=1, or at most two one-kernel four-sets give N3≤2; their joint kernel cost cannot exceed two|

Thus uniformly N2≤1,N3≤2, with arbitrary N4 and D7. The four positive sets have sizes3,3,3,4, so the auxiliary gate applies.

In particular the s=1 remaining one-kernel original triple must **not** be mistaken for a kernel-free triple: fixing its red kernel produces a negative pair. The explicit origin table and the auxiliary gate cover it. Negative triples that did not block the earlier four candidates are still present whenever allowed by these same residual budgets; none was assumed absent without paying its kernel/triple cost.

## n=1: the same blocker removal closes the whole high-three case

Here m≥3 and s≤1. Since K≤s, for s=0 all remaining negative indices avoid both kernels; at most one original negative triple remains, giving at most one N3. For s=1 there are no remaining original negative triples and K≤1, so no two-kernel negative four-set is possible and at most one one-kernel four-set gives an N3. There is no negative pair in either case.

After Z and z are blue, each of the four positives has size at least two: at most two points were removed from an original four-set. The remaining negative family has at most one triple and otherwise four-sets; D7 is preserved. The four-small-positive theorem therefore applies directly, without invoking the auxiliary gate's stronger positive-size hypothesis. Extra negative indices containing z, if any, were removed as already satisfied and cannot spoil the budget calculation.

## Return to the original signed system

The final red set contains x,y, avoids Z and z, and meets every shortened remaining positive. The original x/y positives were already hit. Original negative triples containing both kernels contain their blue third point; selected blocker edges and any other edge removed on fixing a blue point contain that blue point. Other original negatives are exactly represented by their residual pair/triple/four constraints after removing red kernels, and are avoided by the repair. Shortening or removing indexed constraints does not increase any unfixed point's total occurrence. Thus the argument returns a repair of the original ten-positive system in the stated subbranches.

## n=2: change the kernel and invoke n=0

Both original negative triples contain x,y, so they have third points in Z. The surviving three-point z is outside Z. Consequently neither original negative triple contains z.

The original maximum positive occurrence is three. Since z belongs to three positives unhit by x,y, its original positive support has exactly those three labels, disjoint from the three x labels and the three y labels. Thus x,y,z have three pairwise disjoint positive-label support triples.

Return to the original signed system; do not first fix Z or z blue. Instead fix **x,z red**. The new number n′ of original negative triples containing both new kernel points is zero, because both original negative triples avoid z. The four positive four-sets unhit by x,z include the three original y-star sets and the one remaining tenth positive. Hence y is a three-point in this new four-positive family, and its positive occurrence is still exactly three. There are no forbidden third points for this new n′=0 kernel.

All premises of the already proved n=0/high-three argument now hold with new kernels(x,z) and new three-point y: their original positive counts are three, total negative kernel incidence is at most eight, the negative triple/four budgets remain two/eighteen, and D7 is unchanged. That argument repairs the original system. This closes the entire n=2 high-three subbranch without the singleton residual transformation.

The earlier direct transformation could leave singleton positives; it is retained only as [historical boundary information](HISTORY_N2_BOUNDARY.md). It is not a remaining case of this subtheorem. The max2 families after forbidding Z, and the full ten-positive gate outside the stated surviving-three-point premise, are not covered here.

No new positive graph catalogue, negative-layout enumeration or solver was used. The n0,n1 direct arguments and the n2 kernel change prove the complete subtheorem above, not the full ten-positive gate or the actual P6 residual census.
