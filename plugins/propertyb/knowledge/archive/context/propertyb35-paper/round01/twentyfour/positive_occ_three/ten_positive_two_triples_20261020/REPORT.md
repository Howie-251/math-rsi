# Ten positives / two negative triples: bounded structural diagnosis

Target: exactly10 indexed positive four-sets on at most18 points, at most two negative triples and18 negative four-sets, total indexed occurrence at most seven. No complete general theorem or signed counterexample is claimed here. No seven-label catalogue or negative-layout search was generated.

## Closed occurrence range: some point occurs at least four times

The positive total is40, so maximum positive occurrence≤2 is in fact impossible on18 points. Its usual probability bound2(7/16)³+18(7/16)⁴=27097/32768<1 is valid but unnecessary for this exact input size.

If some point x occurs at least five times, fixing it red leaves at most five unhit positive four-sets on at most17 points. The five-remaining-positive proof in [NINE_POSITIVE_JOINT_NEGATIVE_REPAIR](../../../../../../proofs/propertyb35/NINE_POSITIVE_JOINT_NEGATIVE_REPAIR.md), AppendixA, only uses those five positives, exterior size≤17, original t≤3,t+b≤20 and x-negative occurrence≤3. Our t≤2,t+b≤20 and x-negative occurrence≤2 are stronger. It therefore applies directly when five remain. It does not need the original total to be nine. If fewer than five remain, the same fixed-point candidate arguments apply directly without padding: at most two easy; three disjoint give64 four-red candidates against at most2·4+2 blockers; four disjoint give256 five-red candidates against2·16+18·4=104; with intersections two fixed red points leave at most two groups, and the AppendixA kernel budgets are only stronger here.

For positive maximum exactly four, fix ax=4. Six positives remain.

- If they have maximum occurrence≤2, their union is at most17 and their intersection multigraph has six labels, maxdegree4 and E≥7. The nine-positive theorem §§5–6, including the already complete981-orbit census/76 rational certificates/integer exception, uses **only this six-positive representation**, original t≤3,t+b≤20, x-negative≤4 and each outside negative occurrence≤7−remaining-positive-frequency. Our t≤2,t+b≤20,x-negative≤3 meets these hypotheses. Thus the whole six-remaining-max2 branch transfers without a new domain.
- If a point y meets at least three of the remaining six, fix x,y red; at most three positive fours remain, avoiding both kernel points. x/y original positive occurrences are at least4/3, so their total negative incidence is at most3+4≤8. The nine-positive AppendixB n≤2 proof uses only up to three such remaining groups, the joint kernel capacity≤8 and at most three original negative triples. Here the number n of negative triples containing both x,y is automatically≤2, so its delicate n=3 star-swapping case is not used. The original x/y positive labels need not be disjoint: their being already hit is sufficient, and all budget estimates remain upper bounds. For fewer than three groups, after forbidding the n third points, two disjoint groups give at least(4−n)² candidates, greater than its pair-blocker bounds5,4,2 for n0,1,2; intersecting/one-group cases are immediate. Hence this branch also transfers.

Thus **all inputs with maximum positive occurrence at least four are closed by existing actual sublemmas**. This is not a claim that the ten-positive theorem is closed.

## Genuine remaining maximum-three structure

Let n1,n2,n3 count points of positive occurrence1,2,3. Forty positive incidences on at most18 points imply

n3≥4,  n1≤n3−4.

Each three-point is represented by its support triple of positive labels among the10 labels; every label belongs to at most four such triples. A point y remains a three-point after fixing another three-point x exactly when these support triples are disjoint. Therefore the ability to choose x with a remaining three-point is exactly the existence of two disjoint positive-label support triples.

Such a pair cannot be assumed. `CHECK.py/json` gives10 explicit positive fours on18 points whose four three-star supports are

{0,1,2}, {0,3,4}, {0,5,6}, {0,7,8}.

They all meet label0. Every choice of a three-point x leaves a seven-positive family of maximum occurrence≤2. This is a positive-only input, not a signed counterexample; it shows that a universal selection of two disjoint three-stars is false under the stated positive assumptions.

If the three-star support family is pairwise intersecting, its size is at most10: fix one support triple e; every other support meets it, and the total remaining label capacity on e is at most3(4−1)=9. Combined with n3≥4, this is a real smaller structural interface: an intersecting three-uniform multi-family of4..10 triples on10 positive labels, each label capacity≤4, together with n1≤n3−4. Repeated support triples remain distinct actual points and consume capacity. It is stricter than a free seven-label graph and may be a better route than a general seven-label table.

Fixing a three-point x leaves seven positive fours with U≤17. In the no-remaining-three-point branch their intersection multigraph satisfies Δ≤4 and E=28−|U|∈[11,14]. The old six-label981 catalogue cannot be applied to seven labels.

Moreover, a seven-label short-transversal strategy is not automatic: take two disjoint doubled triangles on six labels and a seventh isolated label. This has Δ4,E12,U16, yet **zero three-point and zero four-point transversals**. Its minimum transversals have five points; there are576 five-point transversals. The reason is that each triangle needs two shared points and the isolated positive four-set needs a fifth point. The explicit represented sets and exact small counts are in `CHECK.json`.

This graph is not asserted to extend to an unresolved original ten-positive input or to any signed counterexample. It does establish that a proof using only the relaxed seven-label conditions Δ4,E≥11,U≤17 cannot presume a useful C3/C4 candidate family. Any such strategy must retain extra information from the three positive sets hit by x or allow larger candidate sizes with the real shared capacities.

## Narrow unresolved obligations

The remaining target maximum is exactly three. Its two natural subbranches are:

1. Two disjoint three-star support triples exist: fixing the two centers leaves **four**, not three, unhit positive four-sets, with original kernel negative budget≤8 and original t≤2,b≤18. The subsequent [surviving-three-point subtheorem](FOUR_REMAINING_HIGH_THREE_REPAIR.md) now covers all n0,1,2 whenever the four positives after forbidding the common-negative-triple third points still have a three-point. The n2 case reselects the red kernel and returns to n0, rather than mishandling singleton residual positives. Thus the current unresolved portion of this kernel route has maximum positive occurrence at most two **after those forbidden points are removed**; its residual pair/triple/four negative risks still cannot be dropped or handed to a gate that forbids only triples/fours.
2. Every pair of three-star support triples intersects: every chosen x leaves a max2 seven-label graph, but its graph is coupled to an intersecting4..10 support-triple system and the original40-incidence/18-point budget above. The seven-label relaxed domain alone can have no C4 candidates, so either this coupling must be used or larger candidates analyzed.

No new enumeration was opened. The two tiny positive-only witnesses were checked deterministically; they identify invalid shortcuts, not failure of the proposed signed gate. A later actual P6 caller must still establish that its particular signed system satisfies whichever strengthened sublemma is eventually proved. No claim about all186 residual inputs or all141 target signatures is made here.
