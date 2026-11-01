# The bounded three-low eight-unit gate: exact scope and a repair alternative

The raw eight-unit gate is not uniformly strict for three degree-six and five degree-seven locks. A nonstrict trace inventory is genuinely realizable by a25-point,35-edge hypergraph of spectrum6³,8³,7¹⁹ with no seven-degree K5. Thus discarding that inventory through a necessary condition on the three six-degree stars is impossible. This does not refute Property B or the conditional coloring statement Gate(8,3); it identifies a limitation of the present raw permutation criterion.

## Complete domain, bounded computation and exact unfinished scope

All65 complete unit-eight clique families and all56 unordered three-low markings were reconsidered. If B is the multitrace family, h_i=7−inc_B(i), and L is the low triple, the actual singletons are h_i−1_{i∈L}, while empty is38−|B|−Σh_i. Only nonnegative inventories are retained. The complete domain has64 uncolored families,2968 marked inputs and915 exact low-set-preserving orbits.

`MIXED_THREE_SIX_UNIT8_SCREEN.py/json` tests inherited q=2 positions on the actual q=3 counts rather than assuming monotonicity. It also uses46 distinct consecutive/previous fixed layouts. The full screen took4.253 seconds and gave2494 strictly covered labels;474 labels in130 orbits remained.

The bounded exact subset-position DP processed125 of those130 orbits in28.124 elapsed seconds, then stopped. Of these,110 orbits are strict and15 remain nonstrict. No later DP was run for the five unprocessed orbits. Across the original screen and processed witnesses there are2894 labels in895 orbits with strict layouts. The15 processed nonstrict orbits represent52 labels; the five unprocessed orbits represent22 labels. These three label counts sum to2968. `MIXED_THREE_SIX_UNIT8_STATUS.py/json` binds the source records and lists every residual and unfinished orbit.

The unprocessed roots are60 with low{2,5,7} or{5,6,7};62 with{5,6,7};63 with{4,5,6};64 with{3,4,5}. Their label multiplicities are6,1,1,4,10. They are not asserted to be either strict or nonstrict under optimized layouts.

Among the completed nonstrict examples are core4 low{0,3,5}, reported optimum19739/19448; core15 low{0,1,2},185/182; and core16 low{0,2,7},68127/68068. The original exact engine is `context/propertyb34/round01/high-math/subset_position_dp.py`. Its state is the current position and set of previously placed locks; a transition places either a remaining lock or an unlocked point. The pointwise bound depends only on that state and choice, so Bellman minimization exhausts every lock order and placement for this specified raw/total/pure-quota bound. On the recorded optimum layouts the corrected and raw values coincide. Every returned witness has its25 rows replayed by that engine's independent row routine. This is not an independent reimplementation of the DP optimum, and no independent full2968-input strict replay is claimed.

The ordinary finite colorability theorem Gate(8,3) remains open here. Completing the last five computations would not resolve the already witnessed failure of a universal strict raw bound, so no extra lock or free-point domain has been introduced.

## A real no-K5 realization of core15

Use points5x+y for(x,y)∈F5² and the30 standard affine lines. Add

{3,4,11,12,13}, {5,4,14,15,16}, {6,9,17,18,19},
{7,9,10,20,21}, {8,10,22,23,24}.

These are five distinct non-lines. The six-degree points are exactly0,1,2, the eight-degree points4,9,10, and all other points are seven-degree. The seven-degree support graph is4K4+K3, hence has no K5. The red set

{1,2,3,4,5,6,10,14,15,19,20,21}

properly colors all35 edges.

Choose the actual unit locks I=(0,1,2,3,5,6,7,8). The first four lie on one affine line and the last four on a parallel line. The affine30-line trace family consists of two four-traces15 and240, all16 cross pairs, one singleton at each lock and four empty traces. Each added edge contributes exactly one of the five seven-degree singleton traces. Thus the full actual trace inventory is exactly core15, low labels{0,1,2}, not just the same degree vector or moment data.

The three six-degree stars have the following common free-point witness. Their shared edge has trace15 and free part{4}; this supplies the cell(15,15,15) once. The remaining16 free points give sixteen cells in the product of the remaining five edges of each star, with every cell used once. Each star's free block sizes are4,3,3,3,3, and the three one-dimensional marginals agree. The explicit cells, all original edges and every free-point assignment are in `MIXED_THREE_SIX_UNIT8_REALIZATION.json`.

`MIXED_THREE_SIX_UNIT8_REALIZATION.py` verifies the exact trace equality, all degrees, every covered pair, global unit codegrees at the three lows, the seven-degree components, the displayed proper coloring, and all three simultaneous free-point partitions. It passed in0.005 seconds. Therefore every sound necessary linear inequality on those partitions must be satisfied by this inventory; a partition-only contradiction for core15 cannot exist.

## Three collinear lows: a sufficient one-direction repair lemma

The following conditional lemma is a possible alternative to raw free-pivot enumeration. It uses `proofs/propertyb35/RANDOM_TRANSVERSAL_REPAIR.md` and keeps the zero-low edges correctly in the argument.

Let z0,z1,z2 be six-degree points on a common edge e0. Their three stars each have six edges. Since each low is globally unit, their pairwise common edge is always e0; all other low-star edges are disjoint from e0 outside their own low point. Write Q=e0\{z0,z1,z2}, W=V\e0, and H0 for the edges avoiding all three lows. There are19 edges in H0. For each low, its other five edges have four-point exterior parts partitioning W.

Take a proper coloring of H0 in which both points of Q are blue. Fix z0,z1 blue and z2 red. Allow only initially blue points to be turned red; initially red points and Q remain fixed. Let A be the outside four-set of each initially all-blue edge through z0 or z1 other than e0. These are positive constraints. A point occurs in at most two A's because the two blue-low stars are partitions, and every A has size4.

For each edge of H0, and each of the other five edges through z2, take its initially blue exterior part as a negative constraint B. An H0 edge has no initially all-blue possibility because the starting H0 coloring is proper; turning blue vertices red cannot create a blue monochromatic edge. The positive family therefore needs only the blue-low star edges. Conversely, all H0 edges still appear as negative constraints, so a new red monochromatic zero-low edge is not omitted. Negative sets containing a blue point of Q are automatically safe: Q is in no positive A and is never flipped. Empty negative sets must be excluded by the initial-coloring hypothesis.

Let N be the number of remaining, indexed active negative constraints after discarding those containing Q. All five z2-star constraints are in W. For q1,q2∈Q, every edge through either point other than e0 avoids the selected lows. Hence the number of H0 edges meeting Q is exactly

d(q1)+d(q2)−λ(q1,q2)−1,

and

N=25−d(q1)−d(q2)+λ(q1,q2) ≤17.

For the inequality: if one Q point has degree6, λ=1 and N≤14; if one has degree7 and neither has degree6, its row4 gives λ≤5 and N≤16; if both degrees are at least8, λ≤min(d(q1),d(q2)) gives N≤25−max(d(q1),d(q2))≤17. In core15 one Q point is seven-degree, so the stronger N≤16 applies.

**Conditional repair conclusion.** If every active B has at least three points, at most eight indexed B's have size3, and all others have size at least4, then H is colorable.

Indeed choose independently one uniform point from each A and let R be their union. The occupancy lemma gives q_x≤p=1−(3/4)²=7/16 and

Pr(some active B⊆R) ≤17p⁴+8(p³−p⁴)=65513/65536<1.

One choice of R hits all A and contains no active B. Flip precisely R to red. Every blue-low edge is proper, every red-low edge and every H0 edge avoids becoming all red, and H0 cannot become all blue. The common edge e0 was fixed with both colors. Thus all original35 edges are proper. ∎

The genuine missing step is a uniform choice of the initial proper H0 coloring with Q blue and the stated active-negative size/count conditions (or a sharper nonuniform/pair-occupancy estimate). The known small-edge Property B theorem colors H0, but it does not supply these additional properties. They are not assumed automatic.

## Why applying uniform occupancy directly from scratch is insufficient

Fix the same three low colors but start all other points uncolored. The correct positive family is the ten blue-low four-sets **and all nineteen zero-low five-edges**. The correct negative family is the five red-low four-sets and the same nineteen zero-low five-edges. A zero-low edge must carry both signs.

Under uniform selection from every positive set, a point x∈W belongs to two four-set positives and d(x)−3 five-set positives. Thus

q_x=1−(3/4)²(4/5)^{d(x)−3} ≥89/125

because d(x)≥6. The five red-low four-set constraints alone then contribute at least

5(89/125)⁴=62742241/48828125>1

to the single-point occupancy sufficient bound. Thus that direct uniform implementation cannot prove a universal result for this collinear-low situation. It does not invalidate nonuniform distributions, the point-pair occupancy correction, or the one-direction repair interface above. The initial proper coloring is what removes zero-low blue constraints legitimately; simply dropping them from a fresh-coloring calculation would be unsound.
