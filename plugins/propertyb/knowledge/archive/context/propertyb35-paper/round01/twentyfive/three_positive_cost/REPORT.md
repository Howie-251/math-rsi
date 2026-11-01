# Three positive four-sets: a direct repair theorem

A deterministic counting proof closes the three-positive-set repair gate for the24-point, one-red-exterior, d(G)=35 branch. No local table is needed in the proof. Independent finite Venn replay confirms the counts; it is supplementary verification rather than a substitute for the argument. The result here forces all five centers to have at least four positive edges. The later four-set gate and complete one-red-exterior conditional closure are in `FOUR_REPAIR_GATE.md` and `ONE_RED_EXTERIOR_DG35_CLOSURE.md`; no unconditional24-point closure is asserted.

## 1. Abstract signed-set lemma

Let A_1,A_2,A_3 be four-element sets. Let an indexed negative family have n_t sets of size t, t=1,…,4. Suppose

9n_1+4n_2+n_3≤24.

Then some R of size at most3 hits every A_i and contains no negative set.

The claim needs no positive overlap assumption, per-point degree bound or hypergraph realization.

Proof. Let F be the distinct points appearing as negative singletons and q=|F|≤n_1. The budget gives n_1≤2, hence q≤2. Replace A_i by U_i=A_i−F; each has size at least4−q and at most4. No U_i is empty. Replacing n_1 by q weakens the budget, so it is sufficient to use

9q+4p+t≤24,

where p=n_2 and t=n_3 retain their indexed edge counts. Duplicate negative pairs or triples cannot help the blocker; retaining their indices only enlarges these counts.

A point in all three U_i repairs immediately. Assume their triple intersection is empty. Every two-point transversal of U_1,U_2,U_3 must itself be a negative pair if no repair exists. Call their number P; thus p≥P. Write T for the number of inclusion-minimal three-point transversals. Such a triple contains no two-point transversal. Therefore the P forced negative pairs cover none of these T triples. Every additional negative pair covers at most4 of the triples in the cases below, and a negative triple covers at most one. Negative sets of size4 cover none of the candidates. We now exhaust q=0,1,2.

For the small intersection classification, a point in U_i∩U_j together with each point in the third set supplies at least4−q two-point transversals. If there are two such intersection points in the same pair of sets, this supplies at least2(4−q) different pairs. If they lie in different pairwise intersections, the two collections overlap in at most the pair joining those two points, so there are at least2(4−q)−1 pairs. There is no triple-intersection point under the standing assumption.

**q=0.** The budget implies p≤6. Hence there is at most one pairwise-intersection point: two would force at least7 pairs. If the sets are pairwise disjoint, T=64. A negative pair covers at most4 of these triples, so failure needs

64≤4p+t≤24,

a contradiction. Otherwise there is exactly one intersection point, between two of the sets, and the third set is disjoint from them. It gives P=4 forced pairs. The minimal three-point transversals choose one point from each of the three disjoint parts of sizes3,3,4, so T=36. No forced pair covers these triples; each other pair covers at most4. Thus failure requires

36≤4(p−4)+t≤24−16=8,

using4≤p≤6. Again this is impossible.

**q=1.** Now p≤3. Two pairwise-intersection points would give at least5 forced pairs, so there is at most one. If the sets are pairwise disjoint, T is their size product and is at least27. Each pair covers at most4 triples, giving

27≤4p+t≤24−9=15,

impossible. If there is exactly one intersection point, the third set must have size3, since all its points create forced pairs and p≤3. Thus P=p=3. The minimal triple candidates use the two exclusive parts, each of size at least2, and the third set of size3: T≥12. All negative pairs are already forced pairs and cover none of these triples. But t≤3, a contradiction.

**q=2.** The budget gives p≤1. Any pairwise intersection would create at least2 forced pairs, so all three sets are disjoint. There are at least8 triple candidates. Their coverage by negative pairs and triples is at most4p+t≤24−18=6, fewer than8, so some triple candidate is unblocked.

These contradictions prove the lemma. Every candidate constructed avoids F. No negative singleton can lie in it; negative pairs and triples were explicitly accounted for; negative four-sets cannot be contained in a candidate of size at most3. ∎

## 2. Actual24-point caller

Take the actual critical interface of `../CRITICAL_SMALL_BLOCKERS.md`: H is pair-covering, five-uniform on24 points, δ≥7, G is its unique all-red bad edge, d(G)=35, and r is the sole red exterior point. All five G vertices have degree7. For each g∈G let A_g be its positive four-set family, m_g its size, and let n_t(g) count the original edges avoiding g with exactly t blue vertices.

The common repeated-pair row theorem gives

9n_1(g)+4n_2(g)+n_3(g)≤24.

The previously proved m≤2 repair lemma shows that noncolorability requires m_h≥3 at every G center h. If a center g has exactly three positive four-sets, the squared-cost hypothesis of the abstract lemma applies directly. Its repair colors H. Therefore

**m_h≥4 for all five centers, and c=Σ_h m_h≥20.**

The conclusion is conditional on one red exterior point and d(G)=35. It does not establish that this initial-state normalization is always available, does not assert the squared-cost bound24 for d(G)=36, and does not yet contradict c≥20.

## 3. What the finite diagnostic checked

`PROFILE.py` first enumerated the seven Venn-cell counts for three four-sets with positive repeated-incidence surplus≤5. There are65 labeled count families. Six have equal positive sets and are excluded for a simple original hypergraph at one center, leaving59. Marking the forbidden vertices by cell counts with |F|≤2 gives1023 cases. All fail to admit a blocking negative-pair/triple collection under the two budgets. Runtime was0.067 seconds; only112 cover-recursion calls were made.

The cover recursion was unnecessary: `COARSE_BOUND.py` confirms that every surviving budget is already excluded by the number of triple candidates minus the sum of the largest possible pair gains. There were112 budget comparisons and no exceptions. This observation led to the direct proof in §1, which is stronger because it does not assume surplus≤5 and needs only the squared-cost inequality. The original profile additionally imposed3n_1+2n_2+n_3≤12; its numerical scope is retained accurately.

`REPLAY.py` is an independent standard-library check. It does not import any profile/model source, use a solver or run a set-cover recursion. It enumerates all5^7 seven-cell count vectors directly, checks the three4-incidence equations, marks F using actual vertex subsets, and obtains minimal transversals from the Cartesian product U_1×U_2×U_3. It checks the elementary intersection classification and, for every permissible integer p, the inequality

T−(p−P)K > min(24−9q−4p,12−3q−2p),

where K is the actual maximum number of minimal triple candidates containing a pair. Complete output:65 raw families,59 simple families,2437 actual-vertex F cases,331 integer budget comparisons, all strict with minimum gap2. Runtime0.120 seconds. Both the counting argument and replay retain q=|F|≤n_1; they do not silently identify distinct forbidden points with indexed singleton edges.

Reproduce with:

```sh
python3 context/propertyb35-paper/round01/twentyfive/three_positive_cost/REPLAY.py
```

`COST_ONLY_REPLAY.py/json` also repeats the independent check with only9q+4p+t≤24, removing the supplemental linear constraint. It verifies the same2437 actual forbidden-set cases and331 integer budgets, all strict with minimum gap2, in0.122 seconds.

No actual H was enumerated. No floating infeasibility, unverified solver status, external model opinion or new lock inventory is used in the theorem.

## 4. Boundary of the three-set lemma

The next genuine obligation is the m≥4 plateau. The c≥20 conclusion strengthens the small-negative incidence budget to≤8 at a center with the other four m_h≥4, but repairs may now require four blue points and can be blocked by the many genuine negative four-sets, including those other-center positive edges. The three-set proof does not remove them. The subsequent `FOUR_REPAIR_GATE.md` and `ONE_RED_EXTERIOR_DG35_CLOSURE.md` resolve this plateau under the same a=1,d(G)=35 conditions. They do not prove the unconditional24-point branch.

## 5. Bounded four-positive pilot, not a completed gate

`FOUR_COMPLEXITY.py/json` only counts the real low-overlap domain. With four positive four-sets, the seven-degree24-point repeated-incidence budget5 means

Σ_(nonempty Venn cells C) (|C|−1)μ_C≤5.

Recursing only over the11 nonsingleton cells under this small budget gives822 labeled count families,798 with four different sets. Their |F|=0,1,2 cell markings number798,5206,17389. This0.006-second count is not a probability screen or a coloring theorem.

`FOUR_PILOT.py/json` then tests only five explicit geometries (four disjoint sets; one point common to all four; that common point plus two pair intersections; five distinct pair-intersection points; and disjoint pair-overlap groups of sizes3 and2). In each, F is empty, or consists of the one/two vertices of greatest positive multiplicity. This is15 stated inputs, not the full23393-mark domain. All15 are excluded by the following necessary blocker inequalities in0.039 seconds.

After the m3 theorem, every other center has at least4 positive edges, so the selected center's small-negative incidence budget is≤8. With q=|F|≤n_1≤2 and p=n_2,t=n_3, use

9q+4p+t≤24, 3q+2p+t≤8, n_4≤28−q−p−t.

Let T_j count the inclusion-minimal free transversals of size j. If T_1>0 there is a repair. Otherwise P=T_2 distinct pairs must be negative pairs. None lies in a larger minimal transversal. Let K_23,K_24 be the largest numbers of minimal3- or4-transversals containing one pair, and K_34 the analogous maximum for a triple. At least

L_3=max(0,T_3−(p−P)K_23)

negative triples must be used for remaining minimal3-transversals. These triples cannot lie in minimal4-transversals. Consequently a blocker must satisfy t≥L_3 and

T_4≤(p−P)K_24+(t−L_3)K_34+28−q−p−t.

The pilot checks every nonnegative integer(p,t) under the displayed budgets, with p≥P, and all15 inputs violate this necessary condition or already have a free singleton. The program saves the sets, F, candidate counts, occupancy maxima and exact count gaps. No actual incidence realization is inferred from a surviving inequality, and no such survivor was seen among these15 inputs.

This favorable pilot suggests a bounded count screen may be worthwhile, but it does not prove the full four-positive gate. Even a completed m4 gate would still require handling the possibility that all five centers have m=5; it cannot be silently applied to only four of a center's five required positive sets.
