# Independent verification of the complete 31–33-point branches

**PASS (same-family / provisional).** The selection and coverage arguments in `../small31_33/REPORT.md` are sound under the declared upper-level minimal-counterexample and conditional-permutation imports. The complete necessary domain has 143 local types. Independent reconstruction and exact probability replay pass for every type, with largest bound
\[
163866331/163881900<1.
\]
The run took 0.213476 CPU seconds and approximately 0.216 wall seconds. There is no new Lean or external-model review here, and this local audit alone does not assert $m(6)\ge67$.

## 1. The component support bounds are valid

For a family of distinct five-sets, use its intersection graph. Different components have disjoint vertex supports. A connected component with $t$ sets and $e$ intersecting pairs has $t-1\le e\le\binom t2$.

The random-order independent-set argument and Cauchy–Schwarz give an integer independence lower bound $\lceil t^2/(t+2e)\rceil$. Its independent five-sets have disjoint supports, hence force five times that many support points.

Fix a spanning tree in the component. The $r=e-t+1$ non-tree edges can each be destroyed by choosing one of their endpoints. The union of these chosen endpoints has size at most $r$, so the induced graph on the remaining vertices is a forest on at least $t-r$ vertices. Its larger bipartition class has size at least $\lceil(t-r)/2\rceil=\lceil(2t-e-1)/2\rceil$. This also gives a valid support lower bound after multiplication by five. If this expression is nonpositive it has no effect on the maximum with the positive first bound.

For $t\ge2$, distinct five-sets force support at least six. If the support were at most ten, each five-set would have at most one distinct disjoint partner: none when the support is below ten, and only its complement on a ten-point support. Thus the nonedge graph has maximum degree at most one and at most $\lfloor t/2\rfloor$ edges. When $\binom t2-e>\lfloor t/2\rfloor$, support at most ten is impossible and support is at least eleven. This establishes every term of the proposed component bound $u(t,e)$.

An actual component partition therefore has union size at least the sum of its $u(t,e)$ values. Minimizing over all numerical component partitions, including unrealizable ones, preserves the lower-bound direction. Allowing unused intersection-edge budget also preserves it. Therefore the minimum budget $q_*(f,N)$ accepted by this relaxation is a valid necessary number of intersecting pairs for any actual family of $f$ distinct five-sets supported on at most $N$ points.

The independent program uses a different dynamic program: bottom-up knapsack on **exact** total component edge counts, initialized only at the zero-family/zero-edge state. Taking prefix minima afterward gives the at-most-budget relaxation. It searches budgets starting at zero, rather than starting at the submitted older ceiling bound. All 125 exported entries for $0\le f\le24$, $28\le N\le32$ agree exactly. Every search accepts within the independent budget range $0\ldots80$; this cutoff does not omit any smaller budget or affect an accepted minimum.

The actual link of a lock vertex contains distinct five-sets because the original hypergraph is simple. Consequently the new quota applies to each link used in the certificate. Selecting the cheapest admissible unordered trace cells up to this quota is a lower bound on the same actual nonnegative bad-pair cost and hence gives a valid probability subtraction.

## 2. Complete 31-point selection

Pair coverage implies minimum degree at least six, and the average-degree budget gives minimum degree at most twelve. A minimum vertex of degree six through eleven gives the six complete one-lock types.

When the minimum is twelve, total degree 396 leaves only 24 excess units above the baseline $31\cdot12=372$. If there were at most six twelve-degree vertices, at least 25 vertices would have degree at least thirteen and the sum would be at least 397. Thus there are at least seven twelve-degree vertices. Fix one, $x$. Its codegree excess is
\[
\sum_{y\ne x}(\lambda_{xy}-1)=5\cdot12-30=30.
\]
If each of six other twelve-degree vertices had codegree at least seven to $x$, those six partners alone would contribute at least 36 excess. Hence some actual partner has codegree $1\ldots6$. The six two-lock types in this interval have multiplicities
\[
\ell_3=\lambda,\quad\ell_1=\ell_2=12-\lambda,\quad\ell_0=42+\lambda.
\]
Both vertices are actual and distinct; no unproved low-codegree selection is imposed externally.

## 3. Complete 32-point selection, including the harmonic wedge

Here minimum degree is seven through twelve. For a minimum vertex $x$ of degree $d\le11$, at least $n=62-5d>0$ distinct partners have codegree one. If all such partners had degree above $t=d+\lfloor(396-32d)/n\rfloor$, then the minimum-degree baseline plus these partners would give degree sum above 396. Thus an actual unit partner exists with degree in the entire enumerated interval:

| $d$ | Unit-neighbor lower bound $n$ | Partner degree range |
|---:|---:|---|
|7|27|7–13|
|8|22|8–14|
|9|17|9–15|
|10|12|10–16|
|11|7|11–17|

This is 35 two-lock types.

For minimum twelve, the excess above twelve is twelve. The twelve-degree set $R$ therefore has at least twenty members, and every other degree is between thirteen and twenty-four. A vertex in $R$ has codegree row sum 60 on 31 partners and excess 29, so has at least two unit neighbors. A unit pair within $R$ is the passing degree pair $(12,12)$. A unit neighbor of degree fourteen through twenty-four gives one of eleven other passing pair types. If neither case occurs, **every** unit neighbor of every $r\in R$ has degree thirteen. Let $B$ consist of these actual neighbors. Then $|B|\le12$, and every $r\in R$ has positive degree $u_r$ in the unit-pair bipartite graph; every $b\in B$ has positive degree $t_b$.

Suppose no $b$-centered wedge has endpoints of codegree at most two. For each edge $rb$, the other $t_b-1$ members of $N(b)$ then have codegree at least three with $r$. All nonunit partners have codegree at least two, whereas exactly $u_r$ unit partners have codegree one. Hence
\[
60=\sum_{z\ne r}\lambda_{rz}\ge62-u_r+(t_b-1),
\]
which gives $t_b\le u_r-1$. Both counts are positive, so $1/t_b>1/u_r$. Summing this strict inequality over all bipartite edges gives
\[
|B|=\sum_{rb}1/t_b>\sum_{rb}1/u_r=|R|,
\]
contradicting $|B|\le12<20\le|R|$. Thus an actual degree-thirteen center and two distinct twelve-degree endpoints exist, with both center pairs unit and the endpoint pair of codegree $\lambda\in\{1,2\}$. The triple trace has multiplicity $\tau\in\{0,1\}$; these four types are exactly those reconstructed independently. If the earlier unit-pair case was excluded then the wedge endpoint codegree cannot be one, but retaining this additional type only enlarges the necessary domain harmlessly.

## 4. Complete 33-point selection, including the degree-nine exception

The minimum is seven through twelve. The same minimum/unit-partner budget argument gives:

| $d$ | Unit-neighbor lower bound | Partner degree range |
|---:|---:|---|
|7|29|7–12|
|8|24|8–13|
|9|19|9–14|
|10|14|10–14|
|11|9|11–14|
|12|4|12–12|

Take a minimum-degree actual unit neighbor of $x$. The passing pair domain consists of every interval value except degree fourteen at $d=9,10,11$. Therefore in an exceptional case all actual unit neighbors of $x$ have degree at least fourteen.

For $d=9$, at least nineteen such neighbors cost at least $19\cdot5=95$ of the 99 excess degree units above the baseline nine. Twenty would cost 100, so there are exactly nineteen. The other thirteen partners are nonunit, and their total codegree excess is exactly $45-32=13$, forcing each to have codegree two. The fourteen vertices outside the nineteen unit neighbors, including $x$, have at most four excess degree units in total, so at least ten of them have degree nine. In particular a distinct second degree-nine vertex exists, lies outside the unit-neighbor set, and has codegree exactly two to $x$. The independently replayed special pair bound is $101147/103385<1$.

For $d=10,11$, let $u$ be the actual number of unit neighbors, at least $n=64-5d$. If $h$ of them have degree strictly above fourteen, their degree cost above the baseline $d$ is at least $u(14-d)+h$. Thus the number of degree-fourteen neighbors is
\[
u-h\ge(15-d)u-(396-33d)\ge(15-d)n-(396-33d),
\]
namely at least four for $d=10$ and three for $d=11$. This handles any $u\ge n$, and provides two distinct actual degree-fourteen unit neighbors. Their mutual codegree $\lambda$ is at least one by coverage and at most fourteen by degree. Their triple intersection $\tau$ is zero or one because both center pairs have codegree one. The only further nonnegativity restriction is $13-\lambda+\tau\ge0$, yielding exactly 27 necessary trace types for each $d$. This is a complete local classification, including the possible endpoint-degree-fourteen/common-codegree-fourteen type.

## 5. Domain reconstruction and exact independent replay

The independent program rebuilds every local trace dictionary by subtracting pair/triple incidence multiplicities from the prescribed actual degrees, then uses the remaining edge count as the empty trace. The necessary domain is reconstructed from the proved degree intervals and selection branches; the submitted generator and quota routines are never imported. Comparing full branch/vertex-count/trace-dictionary keys verifies equality of the complete domain, with no omitted or duplicate row.

| Branch | Number of types | Largest independent exact bound |
|---|---:|---:|
|31, minimum six through eleven|6|119429/120060|
|31, two twelve-degree vertices|6|6587228/6653325|
|32, minimum seven through eleven|35|12601627/12606300|
|32, minimum twelve, pair cases|12|163866331/163881900|
|32, minimum twelve, wedge cases|4|1483427/1520760|
|33, ordinary adaptive pair cases|25|825843/827080|
|33, minimum nine special pair|1|101147/103385|
|33, minimum ten, two fourteen-degree neighbors|27|54619477/54627300|
|33, minimum eleven, two fourteen-degree neighbors|27|3147356/3151575|
|Total|143|163866331/163881900|

Each submitted successful position vector is checked to be distinct and within the actual vertex range. Its probability is independently computed using the pre-existing falling-factorial uniform-injection kernel extracted from the older independent checker. This uses neither the submitted binomial-weight probability implementation nor a stored probability value in the calculation. Every resulting rational value equals the submitted value exactly and is strictly below one.

**Precise quota scope:** `certificate.py` imports `diagnose.strengthened`, which installs the stronger **complete-link-pool** quota. Its import of `avoided.triple` does not install `avoid_delete`, because that patch is guarded by `if __name__ == '__main__'`. Accordingly these 143 rows use the new component quota on the complete link pool, rather than an additional joint avoided-lock minimization. The independent replay matches this actual implementation. The report's assertion that the same component lemma can apply to avoided subfamilies is mathematically valid, but such extra strengthening is not needed for these rows.

Reproduce from the project root:

```sh
python3 context/propertyb-m6-67-progress-20261029/independent31_33/check.py
```

`CHECK.json` contains all 125 independent quota entries, the complete reconstructed intervals and every independently replayed probability. Acceptance here is confined to these three branches and the declared mathematical imports.
