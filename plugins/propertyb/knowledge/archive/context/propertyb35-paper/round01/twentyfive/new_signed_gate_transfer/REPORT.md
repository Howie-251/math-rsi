# New signed repair gates on 25 points with at least three six-degree points

## Scope and conclusion

The new repair gates give an exact small interface for three six-degree points on one actual edge, but do not yet cover that full branch. Its two missing properties are a suitable initial coloring and control of its small negative sets; the signed occurrence bound also needs actual verification. The structural obstruction to blue minimization persists at a unit six-degree center.

There is one new complete **conditional** result: a unit six-degree center on a source edge of total degree at most37 can be repaired whenever the source coloring has exactly one exterior red point. This applies conditionally to every $r_6=3$ source edge through a six-degree point, and to a suitable two-low source edge when $r_6=4$. A frozen actual $r_6=3$ example shows that the one-exterior-red hypothesis cannot be guaranteed even when all three lows are on the source edge.

Standing assumptions are a simple five-uniform pair-covering $H$ on25 vertices and35 edges, minimum degree six. There are $r$ six-degree points, every other point has degree at least seven, and

$$\sum_{d(v)>7}(d(v)-7)=r.$$

Every six-degree point $z$ satisfies $\lambda(z,x)=1$ for all $x\ne z$, since its six incident edges supply exactly24 pair incidences.

The existing [GLOBAL_MIXED_REDUCTION](../GLOBAL_MIXED_REDUCTION.md), [q3 raw-bound scope](../MIXED_THREE_SIX_UNIT8.md) and [branch coverage](../../../BRANCH_COVERAGE.md) remain unchanged. No q3 DP, alternative layout or new lock table was run.

## 1. Three collinear lows give five actual disjoint positive blocks

Let $K=\{z_0,z_1,z_2\}$ consist of six-degree points on a common edge $G$. Write $Q=G-K$, $W=V-G$. Any other edge through one selected low contains no other point of $G$: each such pair is already covered by $G$. At each low, the other five edges therefore have four-point parts forming a partition of the20-point set $W$.

The edges meeting $K$ are exactly $G$ and these15 distinct other star edges; hence the edge family $H_0$ avoiding $K$ has19 edges. It is colorable by the already proved small-edge Property B result. That fact does not prescribe colors at $Q$, the high points, or any required negative-set sizes.

Choose one low $g\in K$ blue and the other two red. Start with a proper coloring of $H_0$ on $V-K$. Fix all initially red nonlow vertices and allow only initially blue vertices to turn red. The common edge $G$ is already proper because its low points have both colors.

The correct signed system is:

* Positive sets are the four-point blocks of the blue-low star that are initially all blue. There are at most five; they are pairwise disjoint and lie in $W$.
* Negative sets are the initially blue portions of all ten other red-low star edges and all19 edges of $H_0$.

An empty negative set means the chosen initial state cannot be repaired in this direction. Properness of $H_0$ excludes empty negatives from $H_0$, but does **not** exclude an initially all-red red-low star edge. This must be checked separately.

The $H_0$ edges need only the negative sign **because they are initially proper**: changing blue points red cannot create an all-blue edge. Starting without that proper source coloring would instead require both signs for every zero-low edge. Deleting that positive risk from a fresh coloring argument would be incorrect.

All future repairs may be restricted to the union $U$ of the positive blocks. A negative set not contained in $U$ is then automatically avoided. This is a legitimate simplification, not a deletion of its only relevant monochromatic sign.

## 2. Exact occurrence and the genuinely missing gate hypotheses

For $x\in U$, the unique original edge containing $g,x$ is its positive star edge. All other incident edges avoid $g$ and supply negative constraints before inactive ones are discarded. Hence

$$a_x+b_x=d_H(x)\qquad(x\in U)\tag{1}$$

in the unfiltered source system. Thus six- and seven-degree active points satisfy the required occurrence cap, but an active high point need not. The unit property gives no ignored-edge compensation on a positive block.

A safe option is to forbid all initially blue high points from the repair. Delete them from positives and discard, rather than shorten, every negative meeting them. The remaining active points have degree at most seven, so total signed occurrence is at most seven. However a positive block may shrink below size two; when $r=3$, there are at most three high points, and a block containing all three could shrink to a singleton. This possibility has not been excluded by the actual unit-star structure.

After these safe operations, the exact sufficient alternatives are:

1. At most five positive sets of sizes two to four, no negative singleton or pair, and at most one negative triple: apply [five small positives / one triple](../../../../../proofs/propertyb35/FIVE_SMALL_POSITIVE_ONE_TRIPLE.md).
2. At most four positive sets of size at least two, no negative singleton or pair, and at most three negative triples: apply [four small positives / three triples](../../../../../proofs/propertyb35/FOUR_SMALL_POSITIVE_THREE_TRIPLE_REPAIR.md).
3. At most six positive **four-sets**, no negative singleton or pair, at most six negative triples and at most35 negative four-sets: apply [six positives / six triples](../../../../../proofs/propertyb35/SIX_POSITIVE_SIX_TRIPLES_REPAIR.md). The unshrunk one-blue-low source has at most five positives and29 negative source edges, but the no-small-negative and occurrence hypotheses still need verification.

Each alternative is a complete actual coloring implication. None of these missing hypotheses follows just from the three real partitions. Those same partitions were already realized by the frozen nonstrict core15 example; they cannot provide a contradiction excluding that inventory.

For completeness, if one normalizes a proper $H-G$ source coloring by minimizing its number of blue points, the obstruction becomes stronger. At a unit center $g$, each point of a positive four-block has a singleton-blue private edge. That private edge cannot contain $g$, since the unique $g,x$ edge is the positive four-block. Thus every point of every positive block is a negative singleton. If the positive family is nonempty, a one-direction repair is completely blocked; if it is empty, flipping $g$ alone already succeeds. Blue minimization cannot supply the desired small-negative gate at a six-degree center that still needs repair.

## 3. A new one-exterior-red conditional lemma

**Lemma.** Let $H$ be as in the standing assumptions. Suppose an actual edge $G$ contains a six-degree point $g$, has degree sum $D_G\le37$, and $H-G$ has a proper coloring with $G$ all red and exactly one red exterior point. Then $H$ has Property B.

**Proof.** The positive four-sets at $g$ are subblocks of its actual star partition and hence are pairwise disjoint. All original edges avoiding $g$ give nonempty negative sets of sizes one through four, with indexed counts $n_1,\ldots,n_4$. There are at most $35-6=29$ such edges. The degree cap on exterior points need not be seven and is not used here.

The general one-red squared-cost inequality in [CRITICAL_SMALL_BLOCKERS](../CRITICAL_SMALL_BLOCKERS.md) gives

$$9n_1+4n_2+n_3\le4(D_G-d(g)-25+2)=4(D_G-29)\le32.\tag{2}$$

Here is its direct source accounting. Put $S=G-\{g\}$ and let $r$ be the unique exterior red point. The sum of pair-repetition rows of $S$ is $4(D_G-6-24)$. For an edge avoiding $g$ with blue part of size $t$ and $\varepsilon=\mathbf1_{r\in e}$, its $S$ part has size $h=5-t-\varepsilon$. It contributes $h(h-1)+h\varepsilon\ge(4-t)^2$ to directed $S$--$S$ and $S$--$r$ incidences. The original edge $G$ already supplies the baseline of every directed $S$--$S$ pair. Only the four $S$--$r$ baseline incidences must be added to the repetition budget. This gives $4(D_G-6-24)+4=4(D_G-29)$ as in (2).

If there is no positive set, flip $g$ alone. Otherwise choose independently and uniformly one point from each disjoint positive four-set. A negative $t$-set has probability at most $4^{-t}$ of being contained in the selected union: it has probability zero if it uses a point outside those blocks or two points of one block. By (2), $n_1\le3$ and

$$\begin{aligned}
\sum_{t=1}^4 n_t4^{-t}
&\le\frac{n_1}{4}+\frac{32-9n_1}{64}+\frac{29}{256}\\
&\le\frac34+\frac5{64}+\frac{29}{256}
=\frac{241}{256}<1.
\end{aligned}$$

Some selection is a repair, proving the lemma. ∎

When $r=3$, any edge through a six-degree point has $D_G\le6+4\cdot7+3=37$, so the lemma applies **if its one-exterior-red source exists**. When $r=4$, the unique actual edge through any two low points has $D_G\le2\cdot6+3\cdot7+4=37$, with the same conditional conclusion. No assertion here supplies that source coloring.

## 4. The actual core15 example forbids the one-red normalization

Use the unchanged actual $35$-edge example in [MIXED_THREE_SIX_UNIT8_REALIZATION.json](../MIXED_THREE_SIX_UNIT8_REALIZATION.json). Its three low points are $0,1,2$ and their common edge is $G=\{0,1,2,3,4\}$. The four affine parallel lines

$$\{5,6,7,8,9\},\quad\{10,11,12,13,14\},\quad
\{15,16,17,18,19\},\quad\{20,21,22,23,24\}$$

are original edges avoiding $G$, and are mutually disjoint. Every proper coloring of $H-G$ with $G$ red must put a red exterior point on each. It therefore has at least four red exterior points. The hypothesis of the new conditional lemma fails for **every** such source coloring in this actual example, although the example itself is colorable.

[CHECK.py](CHECK.py) verifies these four real edges, their disjointness, all three unit-star partitions, and the exact cost32 arithmetic. It also records one fixed proper $H_0$ coloring with all high points red and a valid nonempty positive block at center two; after removing inactive negatives that block has no active negative constraint and a direct one-point repair. This demonstrates a valid actual interface only, not new branch coverage. [CHECK.json](CHECK.json) reports `PASS`.

## 5. Stopping boundary

The new gates reduce a legitimate one-blue-low repair to small-negative sizes/counts and active high-point exclusion. The real unresolved step is choosing the initial proper $H_0$ coloring (or another source coloring) so that these conditions hold. Unit stars alone give disjoint positives, but blue-minimal private edges can force all their points to be singleton blocked, and a red-exterior-one reduction is impossible in a known real three-low example.

No new unconditional $r\ge3$ branch is claimed. The old q3 raw optimum failures, real realizations and unprocessed orbits are untouched. This report introduces neither a free-pivot table nor whole-hypergraph enumeration.
