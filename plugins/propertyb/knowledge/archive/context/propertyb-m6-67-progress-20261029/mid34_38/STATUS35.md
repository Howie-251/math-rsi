# Latest status: minimum-ten branch closed

The final complete candidate is frozen in `PROOF35_MIN10.md` and `CERT35_MIN10.json` (102 accepted rows). The actual codegree-two degree-ten partner and degree-twelve common unit center close the earlier gap. Independent replay is in progress. The prior exploratory report below is retained as history and does not describe the current mathematical frontier.

# 35 vertices: completed minimum-eleven branch and exact remaining minimum-ten obligation

This file supplements the frozen complete `PROOF36_38.md`. The full $m(6)\ge67$ target is unchanged. Root is handling the other 34/35 minimum-degree cases; this package does not claim a complete 35-vertex proof.

## The minimum-eleven case is complete

Assume $v=35$, degree sum $396$, pair coverage, and minimum degree eleven. Set $R=\{x:d(x)=11\}$ and $r=|R|$. Since all other degrees are at least twelve,

$$396\ge11r+12(35-r)=420-r,$$

so $r\ge24$. A point $x\in R$ has at most $55-34=21$ nonunit neighbors. Thus it has a unit neighbor $y\in R$ because $r-1-21\ge2$. For the specified actual unit edge $xy$, the fixed-edge weak-wedge lemma in `PROOF36_38.md` applies:

$$5(d(x)+d(y))=110<2\cdot35+2\cdot24-6=112.$$

Consequently there is an actual three-lock weak wedge with all degrees eleven, two unit pairs and the remaining pair of codegree one or two. Its triple intersection multiplicity is zero or one. `min11_35.py` generates all eight labelled codegree/trace possibilities (all-unit traces are repeated under the irrelevant doubled-pair label; this redundancy is harmless). Every row in `MIN11_35.json` is strict. Thus every actual hypergraph in this minimum-degree case is colorable. ∎

## Two unit arms at minimum degree ten

Let $x$ be an actual minimum-degree point of degree $d=10$. Its actual unit-neighbor set $A$ has size at least

$$n=2(35-1)-5d=18.$$

Choose $y$ of minimum degree $e$ in $A$, then choose $z$ of minimum degree $f$ in $A\setminus\{y\}$. Every other vertex has degree at least $d$, so

$$396\ge35d+(e-d)+(n-1)(f-d).$$

The usual unit-partner bound gives $e\le12$, and therefore

$$e\le f\le d+\left\lfloor\frac{396-35d-(e-d)}{n-1}\right\rfloor.$$

The previously complete adaptive $e=10$ branch is imported from `ADAPTIVE_COMPONENT.json`. For its remaining $e=11,12$ cases, the exact two-arm degree domain is

$$(d,e,f)=(10,11,11),(10,11,12),(10,12,12).$$

Both $xy$ and $xz$ have codegree one, but $\lambda_{yz}$ need not be one. Its complete range is $1\le\lambda_{yz}\le\min(e,f)$. The triple intersection multiplicity $\tau$ is zero or one. The actual multiplicities are

$$\ell_{xyz}=\tau,\quad \ell_{xy}=\ell_{xz}=1-\tau,
\quad\ell_{yz}=\lambda_{yz}-\tau,$$

with singleton multiplicities determined by degrees and the empty multiplicity by the total edge count $66$. Negative tuples are excluded because no actual input can have them.

`two_arms35.py` evaluates all 65 nonnegative trace types with the final component-support quota, testing the maximum of valid avoided-subset deductions. It tries center layouts first, then all three positions in the ten-position window $13,\ldots,22$, with every label order. There are 61 strict types and precisely four failures:

- $(10,11,12)$, $\lambda_{yz}=3$, $\tau=0$ or $1$;
- $(10,12,12)$, $\lambda_{yz}=3$, $\tau=0$ or $1$.

`TWO_ARMS35.json` records each actual layout and exact fraction. `two_arms35_joint.py` further evaluates the exact common integer avoided-subset vector for these four profiles at the specified center layouts. None becomes strict (`TWO_ARMS35_JOINT.json`). These are failed sufficient bounds, not hypergraph counterexamples.

## A reusable actual degree-twelve pool

In the $(e,f)=(11,12)$ case, $y$ is the unique degree-eleven point of $A$, and the other $r_A-1$ unit neighbors have degree at least twelve. Here $r_A=|A|\ge18$. Their baseline degree cost is

$$35\cdot10+(11-10)+(r_A-1)(12-10)=349+2r_A.$$

At most $396-(349+2r_A)=47-2r_A$ of those $r_A-1$ points can have degree at least thirteen. Hence at least $3r_A-48\ge6$ unit neighbors of $x$ have degree exactly twelve.

In the $(e,f)=(12,12)$ case, every point of $A$ has degree at least twelve. Its baseline cost is $350+2r_A$, so at most $46-2r_A$ of them have degree at least thirteen. Thus at least $3r_A-46\ge8$ have degree exactly twelve.

Choose another such degree-twelve unit neighbor $w$, distinct from $y,z$. If $\lambda_{yw}\ne3$, the three-lock type $(x,y,w)$ is among the strict two-arm numerical types. If $\lambda_{zw}\ne3$, the type $(x,z,w)$ is among those same strict types. This invocation depends only on its actual degree/codegree/trace tuple, not on how the three vertices were selected. Therefore an unresolved counterexample forces

$$\lambda_{yw}=\lambda_{zw}=3.$$

It is enough to consider the two four-lock degree tuples

$$(10,11,12,12),\qquad(10,12,12,12),$$

with all three pairs incident to $x$ of codegree one and all three peripheral pairs of codegree three. `degree12_star35.py` generates all 32 nonnegative labelled multiset clique partitions for these two tuples. Fourteen are strict and eighteen remain non-strict in `DEGREE12_STAR35.json`. Even the trace consisting only of pair blocks fails, so merely excluding high traces through $x$ does not resolve this domain.

## Exploratory fourth-lock records

These are auxiliary diagnostics, not ingredients of the frozen 36–38 proof:

- `MIN10_35.json`: an earlier broad weak-wedge domain, `complete=false`, stopped at the CPU cap. It must not be cited as complete.
- `TWO_ARMS35_FOUR.json`: the four remaining two-arm parent types, extended to a fourth point with total new codegree excess at most two; complete 680 types, six non-strict.
- `STAR_FOUR35.json`: a fourth point selected in $A\setminus\{y,z\}$, retaining its unit relation with $x$ and the degree baseline $f$; stopped before the final parent finished and remains `complete=false`.
- `DEGREE12_STAR35.json`: the much smaller actual degree-twelve pool reduction above, complete 32 types, eighteen non-strict.

The exact remaining mathematical obligation at minimum degree ten can therefore be stated using the actual degree-twelve pool and the peripheral codegree-three condition. A stronger joint probability estimate, or a valid structural argument using that pool, is still needed. No new table expansion is proposed here.

The first wide-layout version of the two-arm scan was interrupted and replaced by a center-first implementation; it has no completed evidence file and is not counted as a passed computation. All final status statements above refer to the named completed JSON files.
