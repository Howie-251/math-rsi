# Critical low-edge repair and a two-point small-negative transversal

## Claim and status

The new small-positive theorem gives a useful **conditional repair interface**. It does not currently give coverage of the 24-point minimum-degree-seven branch. Two precise issues remain: the actual signed occurrence need not be at most seven, and minimizing the blue exterior actually precludes a two-point small-negative transversal at every seven-degree center of a hypothetical non-B input.

The conditional interface, the blue-minimal obstruction and its private-edge packing consequences below are **PROVABLE AS STATED**. The proposed conclusion that some center and initial coloring must satisfy the interface is **NOT CURRENTLY JUSTIFIED**. No non-B hypergraph is constructed or asserted here.

## Assumptions and notation

Let $H$ be a simple five-uniform, point-pair-covering hypergraph on $24$ vertices, with minimum degree at least seven and $M\in\{34,35\}$ edges. Let $G\in H$ be an actual edge. Assume a proper coloring of $H-G$ with $G$ all red has been selected. The initial red and blue sets are $P$ and $B$, with $G\subseteq P$, $b=|B|$. This section does not assume that $P-G$ has size one.

For $g\in G$, its indexed positive family consists of

$$\mathcal A_g=\{e-\{g\}:e\in H,\ g\in e,\ e-\{g\}\subseteq B\}.$$

Every positive set has size four; write $m_g=|\mathcal A_g|$. Every original edge $f$ avoiding $g$ contributes the nonempty negative set $B_f=f\cap B$. Its size is between one and four, since $H-G$ is proper. The small-negative family $\mathcal N_g^{\le3}$ retains the indices $f$ with $|B_f|\le3$. Let $F_g$ denote the **set of distinct points** whose singleton occurs in this family. Thus $|F_g|$ is not the number of indexed negative singleton edges.

A repair is a set $R\subseteq B$ meeting every member of $\mathcal A_g$ and containing no negative set. It colors $H$ by flipping $g$ blue and the points of $R$ red. Edges containing $g$ that are not positive remain proper automatically. This is the actual signed interface in [CriticalLowEdgeRepair](../LOW_EDGE_REPAIR_INTERFACE.md).

## 1. The exact small-transversal interface

Suppose $m_g\le5$. Suppose the small-negative family has a transversal $F\subseteq B$ of size at most two. Forbid the points of $F$ from the repair. Each positive four-set then retains at least two points. Discard every negative set meeting $F$: it is already avoided. **Do not shorten a negative set by deleting its points in $F$.** All retained negative sets have size four.

If the resulting indexed positive and negative families have total occurrence at most seven at each remaining active point, [FIVE_SMALL_POSITIVE_ZERO_TRIPLE](../../../../../proofs/propertyb35/FIVE_SMALL_POSITIVE_ZERO_TRIPLE.md) applies and gives a repair. This includes $m_g=0$, when the empty repair suffices.

Here the degree condition is a real hypothesis. In the unfiltered actual signed system define

$$o_g(x)=|\{e\in H:g,x\in e,\ e-\{g\}\not\subseteq B\}|.$$

Positive source edges and negative source edges are disjoint, and every incident edge of $x\in B$ belongs to exactly one of the positive, negative or ignored classes. Therefore

$$a_g(x)+b_g(x)=d_H(x)-o_g(x).\tag{1}$$

A sufficient degree compensation is $o_g(x)\ge d_H(x)-7$ at every active point. Forbidding $F$ and discarding the already avoided or otherwise irrelevant negative sets may further reduce occurrences, so (1) is a sufficient pre-filter check, not a necessary post-filter check. Neither $d(G)=35$ nor $d(G)=36$ bounds every exterior degree by seven: the total excess is seven when $M=35$, and an exterior degree can be as large as fourteen.

## 2. Blue-minimal private edges force many singleton blockers

Now choose the initial proper coloring of $H-G$, keeping $G$ red, with the **fewest blue points**. Each $x\in B$ then has an actual private edge $Q_x\in H-G$ with

$$Q_x\cap B=\{x\}.\tag{2}$$

Otherwise changing only $x$ to red would preserve properness of $H-G$. These witnesses cannot be identified with the unique-red witnesses of a different, red-minimal coloring.

For any $g\in G$, set $U_g=\bigcup\mathcal A_g$ and let $a_g(x)$ count its indexed positive memberships. If $x\in U_g-F_g$, every singleton-blue edge through $x$, including $Q_x$, must contain $g$: one avoiding $g$ would put $x$ in $F_g$. The private edge $Q_x$ is different from all positive source edges, since it has one blue point and those have four. Thus

$$\lambda(g,x)\ge a_g(x)+1\quad(x\in U_g-F_g),$$

whereas $\lambda(g,x)\ge a_g(x)$ on $U_g\cap F_g$. All other pair repetitions are nonnegative, because $H$ covers every pair. The full repetition row is $4d_H(g)-23$. Hence

$$4d_H(g)-23
\ge \sum_{x\in U_g}(\lambda(g,x)-1)
\ge 4m_g-|U_g\cap F_g|.$$

We have proved the useful common-source inequality

$$|U_g\cap F_g|\ge 4m_g-(4d_H(g)-23).\tag{3}$$

This needs no signed-occurrence cap and no assumption about the number of red exterior points.

**Seven-degree consequence.** If $d_H(g)=7$, (3) gives $|U_g\cap F_g|\ge4m_g-5$. Suppose $H$ were non-B and $\tau(\mathcal N_g^{\le3})\le2$. Every transversal must contain all the distinct singleton points, so $|F_g|\le2$. Formula (3) gives $m_g\le1$. The case $m_g=0$ repairs by flipping only $g$. In the case $m_g=1$, the sole positive four-set has a point $x\notin F_g$; $R=\{x\}$ meets it and contains no negative set. This also repairs $H$. Consequently, in a hypothetical non-B input,

$$\tau(\mathcal N_g^{\le3})\ge3\qquad(d_H(g)=7).\tag{4}$$

More specifically, $m_g=1$ requires all four positive points to be singleton blockers, while for $m_g\ge2$ formula (3) gives

$$\tau(\mathcal N_g^{\le3})\ge |F_g|\ge4m_g-5.$$

Thus the bounds for $m_g=1,2,3,4,5$ are respectively $4,3,7,11,15$. They are necessary conditions under the non-B assumption, not examples attaining them.

For an eight-degree center the repetition row is nine. If its small-negative transversal has size at most two, (3) gives $m_g\le2$. Non-B excludes zero or one as above, so only $m_g=2$ can remain. For $d(G)=36$, the degree pattern is $8,7,7,7,7$; in a blue-minimal hypothetical counterexample, a two-point small-negative transversal could therefore occur only at its unique eight-degree center, with exactly two positives. The signed degree compensation in (1) would still need verification.

## 3. A positive consequence of the same normalization: fewer positives

The private-edge packing inequality in [PRIVATE_EDGE_PACKING](../../../../../proofs/propertyb35/PRIVATE_EDGE_PACKING.md) applies to $H-G$, the red set $P$ and blue set $B$. Write $E=5M-168\in\{2,7\}$. For $p\in P$ the degree in $H-G$ is $D_p=d_H(p)-\mathbf1_{p\in G}$, and

$$4b\le\sum_{p\in P}\left\lfloor\frac{4D_p-b}{3}\right\rfloor.$$

Because all point degrees are at least seven and their total excess is $E$,

$$\sum_{p\in P}D_p\le7(24-b)+E-5.$$

Dropping the floors gives

$$12b\le4\bigl(7(24-b)+E-5\bigr)-(24-b)b,$$

or

$$b^2-64b+652+4E\ge0.\tag{5}$$

On $1\le b\le19$ the left side strictly decreases. At $M=35$, its value at $b=14$ is $-20$, so $b\le13$. At $M=34$, its value at $b=13$ is $-3$, so $b\le12$.

Since $F_g\subseteq B$, (3) now shows that every seven-degree center has $m_g\le4$ in **any** such blue-minimal coloring, without a non-B assumption. An eight-degree center has $m_g\le5$. In particular, blue minimization reduces $d(G)=35$ to five centers with at most four positives each, and $d(G)=36$ to four centers with at most four and one with at most five. This is a genuine reduction, but its abundant singleton blockers prevent the proposed two-point-transversal route at the seven-degree centers.

## 4. Fixed actual input check

[CHECK.py](CHECK.py) reads the frozen actual $24$-point, $35$-edge example in [CRITICAL_SMALL_BLOCKERS_PILOT.json](../CRITICAL_SMALL_BLOCKERS_PILOT.json). It directly verifies simplicity, uniformity, pair coverage, minimum degree seven, $d(G)=35$ and that the displayed initial coloring has $G$ as its only monochromatic edge. It enumerates only subsets of the nine blue points to determine each exact small-negative transversal number. No hypergraph enumeration, solver or new external model is used.

| Center $g$ | Positive count | Exact small-negative $\tau$ | Blue points with unfiltered signed occurrence $>7$ |
|---|---:|---:|---|
|6|1|7|$\{0\}$|
|8|0|7|none|
|15|0|8|none|
|19|0|9|none|
|21|0|8|none|

At $g=6$, point $0$ has $d_H(0)=8$, $o_6(0)=0$ and signed occurrence eight, exactly as (1) predicts. These data show that an arbitrary actual source coloring need have neither a two-point transversal at any center nor the unfiltered signed cap. This example is colorable; the four centers with no positives repair immediately. Its coloring is not asserted to be blue-minimal, red-minimal, or part of an edge-critical non-B example. Thus it does **not** refute the existence of some better initial coloring or center in the critical problem.

The same script independently checks the finite arithmetic exclusion $b\ge14$ in (5). Exact output is [CHECK.json](CHECK.json); execution returned `PASS`.

## 5. Remaining mathematical obligation

The known red-exterior-minimal normalization makes each exterior red point the unique red point of a private zero-$G$ edge. These witnesses have four blue points; they do not themselves give a two-point transversal of the small-negative family. They also do not give the singleton-blue private edges used in (3). The two optimality choices cannot be combined without proof.

The still-open option is to select a **red-minimal or otherwise chosen** initial coloring and a center whose small negatives can be forbidden with at most two points while retaining the required signed degree cap, or to use a different repair criterion that tolerates the forced singleton family in (3). No argument here guarantees that selection. The existing one-red-exterior conditional closure [ONE_RED_EXTERIOR_DG35_CLOSURE](../three_positive_cost/ONE_RED_EXTERIOR_DG35_CLOSURE.md) cannot be extended by assuming that exterior-red count is one.

This report closes the proposed blue-minimal-to-two-transversal implication in the negative direction and records its useful positive-count reduction. It does not close $24\delta_7$ or the full $m(5)\ge36$ goal.
