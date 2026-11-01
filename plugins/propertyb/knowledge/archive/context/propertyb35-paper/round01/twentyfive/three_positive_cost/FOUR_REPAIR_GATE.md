# Four-positive repair gate with a shared degree budget

The complete local gate below is strict. It concerns four four-sets and their negative blockers; it does not enumerate hypergraphs. Its actual consequence in the one-red-exterior24-point d(G)=35 interface is that every G center must have five positive edges. That remaining case is not removed here.

## 1. Local signed-set statement

Let A_1,…,A_4 be four distinct four-element sets, with repeated-incidence surplus

16−|A_1∪⋯∪A_4|≤5.

Let an indexed negative family have at most28 nonempty sets of sizes1,…,4. Write n_t for its indexed size-t counts and assume

9n_1+4n_2+n_3≤24,

3n_1+2n_2+n_3≤8.

Let a_x count membership in the four positive sets and b_x membership in the indexed negative sets. For every subset U of the positive union assume the common incidence budget

Σ_(x∈U)(a_x+b_x)≤7|U|+7.

Then some R, of size at most4, meets every A_i and contains no negative set.

A complete exact finite verification of this local statement is given in §§2–4. The shared incidence hypothesis is essential to this test: the cost-only version has an explicit blocking signed-set model in `FOUR_FIRST_RESIDUAL.md`.

## 2. General integer count certificate

Let F be the distinct negative-singleton points lying in the positive union, q=|F|. Since n_1≤2, q≤2. Put U=(∪A_i)−F and A_U=Σ_(x∈U)a_x. Restrict candidate repairs to inclusion-minimal transversals of the four sets contained in U. Every such transversal has size at most4: choose one point in each positive set and remove redundant points. Let T_j be the number of these candidates of size j.

If T_1>0, there is a repair. Otherwise let P=T_2. Each of these pairs must occur as a negative pair in a failed repair system. A minimal candidate of size3 or4 contains none of these forced pairs.

Discard negative sets not contained in any candidate, retaining q distinct singleton edges that define F only for the budgets. Let p,t be the indexed numbers of the remaining useful negative pairs and triples. The weakened necessary constraints are

p≥P,

9q+4p+t≤24, 3q+2p+t≤8.

The number of useful negative four-sets is at most28−q−p−t. Duplicate indices cause no difficulty: they consume budget without increasing the number of candidates covered.

For one pair let K_23,K_24 be the maximal numbers of minimal3- and4-candidates containing it. Let K_34 be the maximal number of minimal4-candidates containing one triple. These maxima are computed over all subsets of U of the indicated sizes, so no independence or compatibility of their maximizers is assumed. At least

L_3=max(0,T_3−(p−P)K_23)

indexed negative triples are needed for the minimal3-candidates left after the nonforced negative pairs. Each of these triples is itself a minimal transversal and cannot lie in a minimal4-candidate. Consequently t≥L_3, and at least

L_4=max(0,T_4−(p−P)K_24−(t−L_3)K_34)

useful negative four-sets are needed. Therefore every blocker necessarily satisfies both

L_4≤28−q−p−t,

2p+3t+4L_4≤7|U|+7−A_U.

The second inequality is the shared degree step: every useful negative set is entirely in U, so its full size contributes to the same U-incidence sum. Positive and negative incidences cannot be given independent degree budgets. Ignoring any other negative edges weakens the inequality and is safe.

All formulas use nonnegative integers. Once the positive four-set family and F are fixed, only p=0,…,4 and t=0,…,8 can occur. The exact certificate checks that every such(p,t) violates one of these necessary conditions.

## 3. Complete positive/F domain

Label the four positive edges1,…,4. For each nonempty C⊆{1,2,3,4}, let μ_C count vertices belonging to exactly those A_i. Then

Σ_(C∋i)μ_C=4 for each i,

Σ_C(|C|−1)μ_C≤5.

Conversely any nonnegative integer solution gives exactly such a four-set family, up to a vertex permutation within the cells. Each nonsingleton cell has weight |C|−1≥1, so only a small finite domain remains. The singleton cell counts are recovered uniquely from the four degree-four equations. Exclude two equal positive sets, because the statement requires distinct sets.

There are822 labeled solutions before this exclusion and798 after it. No permutation of the four positive labels is factored out. The forbidden set F has at most two vertices. Permutations within each Venn cell carry any F to its canonical representative determined by the counts |F∩cell|; thus all actual forbidden choices are represented. These markings total23393:798 with q=0,5206 with q=1 and17389 with q=2. Individual unknown vertex degrees do not obstruct this transport: the hypothesis used by the gate is the uniform subset sum bound7|U|+7, which is invariant under relabeling.

For each marking the certificate constructs all minimal candidates, their cardinality counts, K_23,K_24,K_34 and the U-incidence capacity. The stored records and the inequalities of §2 are a complete finite proof of the signed-set statement.

## 4. Actual exact results and independent replay

`FOUR_DEGREE_SCREEN.py/json` checks all798 families and23393 markings. Every marking is strict; no unprocessed state or nonstrict witness remains. Runtime1.464 seconds. The earlier cost-only screen intentionally stopped at the first nonstrict state and remains separately preserved; it is not used as a full result.

`FOUR_DEGREE_REPLAY.py/json` independently verifies the complete domain and arithmetic:

- It generates quadruple, triple and pair Venn-cell multiplicities separately by their surplus weights3,2,1, then restores singleton counts. This differs from the original recursive11-cell generation.
- It enumerates actual zero-, one- and two-vertex F subsets and transports only by their cell multiplicities.
- It generates candidate repairs as free vertex subsets of sizes1,…,4. Such a subset is minimal exactly when its hit mask covers all four positives and every selected point has a private positive set. It does not use the screen's Cartesian-product construction.
- It compares the entire798-family domain, all23393 candidate-count/K/capacity records, and all integer(p,t) conditions. No screen source is imported and no solver is used.

Result: PASS in4.057 seconds. There are691 integer budget comparisons after the elementary singleton/pair/triple requirements. Of these667 fail the negative-edge count condition and24 fail the shared degree condition. The minimum positive degree gap among the latter is13. Only8 marked states need the degree condition; up to the four positive label permutations their free parts are disjoint sets of sizes(3,2,2,2) or(4,2,2,2). No floating-point inequality or solver UNSAT is used.

Reproduce with:

```sh
python3 context/propertyb35-paper/round01/twentyfive/three_positive_cost/FOUR_DEGREE_REPLAY.py
```

## 5. Actual critical-low-G caller

Restrict to a pair-covering five-uniform H on24 points with M≤35, δ≥7, a real G of degree sum35, and an initial coloring whose only bad edge is all-red G and whose only red exterior point is r. This is precisely the conditional interface of `../CRITICAL_SMALL_BLOCKERS.md`; it is not claimed that a=1 is always available.

All G points have degree7. At a chosen center g, positives are the edges containing g, having G-trace{g}, and having four blue exterior points. Negative edges avoid g and retain their full blue parts. They number M−7≤28. The common row bound gives9n_1+4n_2+n_3≤24. The m≤2 repair lemma and the direct m3 theorem in `REPORT.md` show that noncolorability requires m_h≥4 at all five centers.

If some g has exactly four positive edges, their four-sets are distinct by simplicity of H. Pair coverage and the degree-seven row budget give their repeated-positive surplus≤4·7−23=5. The four other centers supply at least16 distinct positive edges, which are actual negative four-edges for g, and each supplies one incidence with S=G−{g}. Thus

3n_1+2n_2+n_3≤35−7−4−16=8.

For any subset U of blue exterior points, total degree has the bound

Σ_(x∈U)d(x)≤7|U|+(5M−7·24)≤7|U|+7.

The positive edges through g and negative edges avoiding g are disjoint original indexed edge families; hence a_x+b_x≤d(x). This supplies the incidence hypothesis of the local gate. Its R is a genuine repair of H. Therefore a non-B initial state in this actual branch cannot have m_g=4.

Each seven-degree center has at most five positive edges. Consequently the actual necessary conclusion is

**m_g=5 at every g∈G, and c=25.**

The proof never treats a center with five positive edges by ignoring its fifth constraint. That case remains separate.

## 6. The rigid m=5 continuation, not yet colored

At every center g the seven incident edges are G, five positive edges, and one remaining edge. Pair coverage of g with r forces that last edge to contain r. Thus every nongroup edge meeting G is either one of the25 positive singleton-trace edges or one of these r-containing edges. Their nonempty G-traces partition G: each g lies in exactly one such trace, so two distinct traces are disjoint and their union is G. Each block has size at most4 because its edge also contains r.

Every edge disjoint from G also contains r, since its initial color is proper and r is the only red exterior point. It follows that every edge other than G and the25 positive edges contains r, and all such edges are distinct. Hence

d(r)=M−26,

which is9 for M=35 and8 for M=34. The remaining total blue excess is at most5 or1, respectively. This is a genuine structural reduction to a partition and a constrained blue incidence system. It is not yet a coloring argument, and this report does not declare the a=1 branch or the original theorem complete.
