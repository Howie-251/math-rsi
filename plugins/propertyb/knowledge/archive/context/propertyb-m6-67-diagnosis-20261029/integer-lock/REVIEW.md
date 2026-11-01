# Independent integer lock-selection check

**Result: PASS (same-family / provisional).** Every pair-covering six-uniform hypergraph on 37 vertices with at most 66 edges has three vertices of degree at most 13 whose three pairwise codegrees are exactly one. This is a lock-selection result; it does not prove the full bound $m(6)\ge67$.

The checked background is `context/propertyb-m6-66-20261029/PROOF_M6_GE66.md`, §4, `context/propertyb-m6-66-20261029/NEXT_INCREMENT_NOTE.md`, and `context/propertyb-general/k12-lock-pilot-20261021/DERIVATION_PACKAGE.md`, §4.2. The proof below uses the actual codegrees of the same hypergraph throughout and does not require any probability table or enumerated hypergraphs.

**Lemma 1 (37-point integer selection).** Let $H=(V,E)$ be six-uniform, $|V|=37$, $|E|\le66$, and suppose every two distinct vertices belong to a common edge. Then there are distinct $x,y,z$ with degrees at most 13 and $\lambda_{xy}=\lambda_{xz}=\lambda_{yz}=1$.

**Proof.** For each vertex $x$, counting incidences with its other edge vertices gives
\[
5d(x)=\sum_{y\ne x}\lambda_{xy}\ge36,
\]
so the integer degree satisfies $d(x)\ge8$. Let $L=\{x:d(x)\le13\}$ and $r=|L|$. Since the vertices outside $L$ have integer degree at least 14 and the total degree is at most $6\cdot66=396$,
\[
\sum_{x\in L}d(x)\le396-14(37-r)=14r-122.\tag{1}
\]
In particular $L\ne\varnothing$ (otherwise $14\cdot37\le396$).

Define the simple conflict graph $G$ on $L$ by joining $x,y$ exactly when $\lambda_{xy}\ge2$. Pair coverage implies every $\lambda_{xy}-1\ge0$, hence
\[
\deg_G(x)\le\sum_{y\in V\setminus\{x\}}(\lambda_{xy}-1)=5d(x)-36.
\]
A uniformly random ordering of $L$ has an independent set consisting of the vertices appearing before every neighbor. Its expected size is $\sum_{x\in L}1/(1+\deg_G(x))$. Consequently,
\[
\alpha(G)\ge\sum_{x\in L}\frac1{1+\deg_G(x)}
\ge\sum_{x\in L}\frac1{5(d(x)-7)}.\tag{2}
\]
Every relevant degree is an integer in $\{8,9,10,11,12,13\}$. For every such integer,
\[
\frac1{5(d-7)}-\frac{14-d}{60}
=\frac{(d-10)(d-11)}{60(d-7)}\ge0.\tag{3}
\]
The sign uses integrality: no integer lies strictly between 10 and 11. Summing (3) and applying (1) gives
\[
\alpha(G)\ge\frac{14r-\sum_{x\in L}d(x)}{60}
\ge\frac{122}{60}=\frac{61}{30}>2.
\]
Since $\alpha(G)$ is an integer, it is at least three. An independent triple has pairwise codegree below two, and pair coverage makes each codegree at least one. This proves the claim. $\square$

**Exact arithmetic check.** A Python `Fraction` computation checked all six degree values, the displayed factorization, and the final strict rational inequality. Its full output is `check.json` in this directory.

| $d$ | $1/[5(d-7)]$ | $(14-d)/60$ | Difference | $(5d-35)(14-d)$ |
|---:|---:|---:|---:|---:|
|8|1/5|1/10|1/10|30|
|9|1/10|1/12|1/60|50|
|10|1/15|1/15|0|60|
|11|1/20|1/20|0|60|
|12|1/25|1/30|1/150|50|
|13|1/30|1/60|1/60|30|

**Lemma 2 (general integer denominator criterion).** Let $H$ be a pair-covering $k$-uniform hypergraph on $v\ge2$ vertices, $k\ge2$, with at most $M$ edges. Write
\[
a=k-1,\qquad b=v-2,\qquad \delta=\left\lceil\frac{v-1}{k-1}\right\rceil.
\]
Choose an integer $D\ge\delta$, and suppose $Z=(D+1)v-kM>0$. Define the positive integer
\[
Q=\max_{d\in\{\delta,\ldots,D\}}(ad-b)(D+1-d).
\]
Then the largest set of degree-at-most-$D$ vertices having all pairwise codegrees one has size at least $Z/Q$. In particular there are at least $s$ such vertices whenever $Z>(s-1)Q$.

**Proof.** For $L=\{x:d(x)\le D\}$, the same degree budget gives $L\ne\varnothing$ and
\[
\sum_{x\in L}(D+1-d(x))\ge Z.
\]
The same conflict graph argument gives $1+\deg_G(x)\le ad(x)-b$. These denominators are positive because $ad(x)\ge v-1$, so $ad(x)-b\ge1$. For every permitted integer degree, the definition of $Q$ gives
\[
\frac1{ad-b}\ge\frac{D+1-d}{Q}.
\]
Summation and the random-order independent-set argument prove $\alpha(G)\ge Z/Q$. Pair coverage converts independence into unit codegree. $\square$

The finite maximum in Lemma 2 is a concave quadratic in $d$: its real vertex is $d_*=(a(D+1)+b)/(2a)$. Thus its integer maximum is attained at the permitted integer(s) nearest $d_*$ (or an interval endpoint when the vertex lies outside). For $k=6,v=37,D=13$, the vertex is $10.5$ and $Q=60$ at $d=10,11$, giving exactly Lemma 1. Equivalently, (3) is the affine line through the two consecutive integer reciprocal values at 10 and 11; it is below all other integer samples even though it lies above the reciprocal curve between these two points.

**Scope.** The earlier continuous identity $20Z-2T^2=-2(5(D+1)-72)^2-2$ remains correct. Its failure only concerns that sufficient continuous bound; the integer improvement above repairs this particular selection obligation. No new lower-bound theorem, full numerical domain, Lean verification, or cross-family approval is asserted here.
