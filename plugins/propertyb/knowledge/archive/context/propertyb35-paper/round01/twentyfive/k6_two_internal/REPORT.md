# Six high points, two internal edges, six pair traces: structural selection

The pure-six-P2 branch is now completely colored. The broader six-high-point/two-internal-edge theorem, including all higher traces, is now [TWENTYFOUR_SIX_HIGH_TWO_INTERNAL.md](../../../../../proofs/propertyb35/TWENTYFOUR_SIX_HIGH_TWO_INTERNAL.md); the source below retains its pure-pair scope. The canonical proof is [TWENTYFOUR_SIX_HIGH_TWO_INTERNAL_PURE_PAIR.md](../../../../../proofs/propertyb35/TWENTYFOUR_SIX_HIGH_TWO_INTERNAL_PURE_PAIR.md). The structural selection leaves four star degree placements; the seven-mixed and exact eighteen-point eight-mixed repair theorems cover all four. This remains a pure-pair-trace result, not a theorem for noninternal three- or four-point P-traces. The selection proof uses a matching and two attachment counts; the multigraph profiles are supplementary checks, not a classification of hypergraphs.

## 1. Actual input

Let H be a24-point,35-edge, simple pair-covering five-uniform hypergraph of minimum degree7. Let P={v:d(v)>7} be a hitting set of size6. Its degrees are(9,8,8,8,8,8), and L=V−P consists of18 seven-degree points. Assume exactly two edges are contained in P and, among all remaining edges, exactly six have P-trace size2 and27 have P-trace size1. No larger noninternal P-trace is assumed in this pure-P2 branch.

Label P={0,1,2,3,4,5} so the two internal edges are P−{4} and P−{5}. Let C={0,1,2,3} be their common four points, and write a=4,b=5. The six indexed pair traces form a loopless multigraph J on P; parallel edges correspond to different original H edges. Let s_v=d_J(v). A C point belongs to two internal edges and an a/b point to one; write c_v=2 or1 accordingly. The exact private single-trace count is

u_v=d_H(v)−c_v−s_v,

with Σ_vu_v=27. Pair coverage of a,b requires at least one ab pair trace, because neither internal edge contains both.

For a C point p, its noninternal edges must cover all18 outer neighbors. Thus4(d_H(p)−2)−s_p≥18. This is a necessary bound, not a substitute for the actual outer set structure. The profiles retain it, but the final structural selection below does not need any unstated outer independence.

## 2. A single-blue center whenever some C degree is at least2

If some p∈C has s_p≥2, color p blue and all other P points red. Both internal edges are proper. Every pair-trace edge containing p is already proper; all other pair traces give at most6−s_p≤4 negative triples. The u_p private edges of p give positive four-sets, with

u_p=d_H(p)−2−s_p≤5.

This also includes the nine-degree case s_p=2: it has exactly five positives and four negative triples. The correct sufficient threshold is s_p≥2 for both degree8 and degree9, not the stronger s_p≥3 at the nine-degree point.

All other private edges give27−u_p≤27 negative four-sets. Positive and negative indices come from different original edges. Each outer point's combined occurrence is at most its original degree7. Corollary A of [FIVE_POSITIVE_SIGNED_REPAIR.md](../../../../../proofs/propertyb35/FIVE_POSITIVE_SIGNED_REPAIR.md), allowing at most five positives with proved padding slack, gives a repair. If u_p=0 the empty repair suffices. Since P hits every original edge, there is no omitted zero-P edge or opposite-color constraint. This is a genuine coloring of H.

Hence the only remaining actual case has

**s_p≤1 for every p∈C.**

## 3. A matching plus attachments, not a free multigraph table

Under this condition the edges of J inside C form a matching of size z∈{0,1,2}. Every C vertex outside this matching is either isolated or has its unique edge attached to a or b. Let k_a,k_b be the two attachment counts and k=k_a+k_b. The remaining pair traces are ab edges, whose multiplicity is

x=6−z−k.

Since2z+k≤4, x≥2+z. Thus the mandatory ab condition holds automatically. These descriptions exhaust every actual J in the remaining branch.

Select two blue P points {p,q}, where p∈C and q∈{a,b}, and require p not to be attached to q. The blue pair is then independent in J, so there are no positive triples. Both internal edges are proper because a five-subset of six points cannot avoid both blue points. Write q' for the other missing point, and let η=1 if the unique nine-degree point lies in {p,q}, zero otherwise.

The number of wholly red pair traces, hence negative triples, is

t=z+k_(q')−s_p.

All remaining pair traces are mixed and already proper. The number of private positive four-sets is exactly

m=u_p+u_q
=13+η−s_p−x−k_q
=7+η+t.

The private negative four-set count is27−m. These are actual indexed source edges, with total occurrence at every outer point at most7.

Thus t=0 gives m≤8 positives and only negative four-sets, covered by the zero-triple eight-positive corollary in `FIVE_POSITIVE_SIGNED_REPAIR.md`. If t=1 and η=0, the input is exactly eight positive four-sets, one negative triple and19 negative four-sets on18 points, covered by [EIGHT_POSITIVE_18_ONE_TRIPLE.md](../../../../../proofs/propertyb35/EIGHT_POSITIVE_18_ONE_TRIPLE.md).

## 4. Direct selection in every nonstar shape

The following cases construct one of these two legal callers.

- z=2: there are no attachments. Choose p in the matching and q among a,b, both avoiding the nine-degree point. Then t=2−1=1 and η=0.
- z=1 and all attachments lie at one missing point q: choose p in the matching. Then t=1−1=0. The same choice applies when there are no attachments.
- z=1 and attachments lie at both a,b: because k≤2, necessarily k_a=k_b=1. Choose q avoiding the nine-degree point and choose p in the matching avoiding it. Then t=1+1−1=1 and η=0.
- z=0 and min(k_a,k_b)=0 with k≤3: take q at the attached endpoint, or either endpoint if k=0, and choose an isolated C point p. Then t=0.
- z=0 and min(k_a,k_b)=1: take q so q' has exactly one attachment, and let p be that attached C point. Then t=1−1=0.
- z=0 and min(k_a,k_b)=2: necessarily k_a=k_b=2. Choose q avoiding the nine-degree point and choose p among the two attachments to q', also avoiding it. Then t=2−1=1 and η=0.

Every chosen point exists: a matching has two or four endpoints, and a pair of attachments has two C endpoints, so a single nine-degree vertex cannot prohibit all choices. The t=0 cases may contain the nine-degree point; their m is then8 rather than7, both within the zero-triple corollary.

The only case not listed is

z=0, k=4, {k_a,k_b}={4,0}.

Here all four C points are attached to one missing point q, and x=2. The exact six pair traces are q0,q1,q2,q3 and two copies of ab. This star shape is handled separately by its four degree placements in §§6–7.

## 5. Complete small checks and exact scope

`PURE_P2_PROFILE.py/json` initially scanned the necessary six-edge trace-multigraph domain, not H. It fixed one compulsory45 edge and distributed the other five traces over the15 pairs. It restored all P1 counts, checked nonnegativity and the outer neighbor-capacity inequality. Its deliberately weaker single-center threshold used s≥3 at a nine-degree C point. The domain left under that older threshold has453 labeled vectors,315 with the nine at C point0 and138 with the nine at missing point4. These453 are **not** the full pure-P2 domain and are not asserted to be actual H realizations.

`REFINED_SELECTION.py/json` applies mutually exclusive priority stages to exactly those453 vectors:

1.177 vectors now have the improved nine-degree s=2 single-blue caller;
2.230 vectors have the zero-triple two-blue caller;
3.42 vectors have exactly eight positive four-sets, one negative triple and19 negative four-sets;
4.4 vectors are the star parameters of §4.

The stages sum to453 and are disjoint in that order. The raw exploratory315/138 and339/114 numbers are not used as final coverage counts.

`SELECTOR_REPLAY.py/json` independently constructs the remaining domain from matchings and attachments. It generates a matching on C, attaches each unused C point to neither/a/b, and restores x=6−z−k copies of ab. There are exactly138 labeled multigraphs for either location-root of the nine-degree vertex. Its276-vector union agrees exactly with the refined subset of the earlier independent15-slot construction. It implements the explicit selections of §4 and verifies230 zero-triple callers,42 exact one-triple callers, and4 stars. No outer edge or negative-constraint layout is enumerated.

The mathematical coverage is §3's matching/attachment description and §4's direct selection, not numerical support counts. The small replay checks those formulas and label choices. The five-positive padding and zero-triple corollary are proved in the canonical signed-repair source; the exact one-triple eight-positive theorem has its separate proof and independent seven-graph replay.

## 6. Exact four star parameters

`STAR_RESIDUALS.json` records all four labeled parameters in the roots nine=0∈C or nine=4∈{a,b}, and star center q=4 or5. All four C points have s=1, the star center has s=6 and the other missing point s=2. Their exact P1 counts and a valid mixed-positive two-blue pilot are:

| Nine-degree point | Star center | P1 counts at0,…,5 | Choose blue | Signed system |
|---:|---:|---|---|---|
|0|4|(6,5,5,5,1,5)|{1,4}|6 positive4 +1 positive3;21 negative4|
|0|5|(6,5,5,5,5,1)|{1,5}|6 positive4 +1 positive3;21 negative4|
|4|4|(5,5,5,5,2,5)|{0,4}|7 positive4 +1 positive3;20 negative4|
|4|5|(5,5,5,5,6,1)|{0,5}|6 positive4 +1 positive3;21 negative4|

There are no negative triples in these displayed two-blue systems. All indexed occurrences are at most7 in any actual H realization. These mixed-positive inputs are not covered merely by the four-set-only zero-triple corollary, and a four-set theorem must not ignore the positive triple. The next section applies the appropriate mixed-set theorems to all four cases. No assertion is made that the four trace parameters are full H constructions. No free outer-pivot domain was opened.


## 7. All four star placements colored

The [seven-mixed signed-repair theorem](../../../../../proofs/propertyb35/SEVEN_MIXED_POSITIVE_ZERO_TRIPLE.md) applies to at most seven positives of sizes3 or4, at most one positive triple, at most21 negative four-sets, and total indexed occurrence at most7. It has no ground-size restriction. Its proof covers a high-occurrence vertex by direct candidate counts and the low-occurrence case by the strict bound57519/65536. All assumptions hold for rows1,2 and4 of the table in §6. The canonical source spells out the actual coloring caller, including the absence of red pair-trace constraints and of zero-P edges. `SEVEN_MIXED_CHECK.py/json` independently checks the rational arithmetic, numerical candidate bounds and all three source-edge counts.

The remaining row has nine-degree point4 equal to star center4, pair traces04,14,24,34,45,45, and P1 counts(5,5,5,5,2,5). Coloring0 and4 blue gives **seven positive four-sets plus one positive triple**, no negative triples and20 negative four-sets, on18 degree-seven outer points. This is eight positives and is not a consequence of the seven-positive theorem. It is exactly the input of [EIGHT_MIXED_POSITIVE_EIGHTEEN_REPAIR.md](../../../../../proofs/propertyb35/EIGHT_MIXED_POSITIVE_EIGHTEEN_REPAIR.md):18 outer points, seven positive four-sets and one positive triple,20 negative four-sets, no negative triples, total indexed occurrence7. That theorem repairs the last placement. Thus the full pure-six-P2 branch is colored; the canonical proof assembles the complete actual-edge argument. `PURE_PAIR_FINAL_CHECK.py/json` restores all276 matching/attachment signed inputs and checks their four repair interfaces, including this final one, without importing the selector source or enumerating outer edges.
