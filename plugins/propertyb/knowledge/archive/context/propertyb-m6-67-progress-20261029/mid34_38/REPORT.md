# Middle domain 34–38: actual minimum-neighbor choice

## Target and status

The target remains $m(6)\ge67$: every finite simple six-uniform hypergraph with at most $66$ edges has Property B. The original target is **NOT CURRENTLY JUSTIFIED** by this package. This package proves a sharper actual lock-selection lemma and records exact conditional probability certificates. No full vertex-count segment is closed.

Assume the imported minimal-counterexample reduction: the same actual hypergraph has $v$ vertices, exactly $66$ edges, covers every pair, and has degree sum $396$. The lock-conditioned permutation failure bound, all edge-type weights, the common avoided-link bad-pair vector and the two possible three-unit-lock traces are imported from `context/propertyb-m6-66-20261029/PROOF_M6_GE66.md`, §§3–4, with the budget reset to $66$. The present arithmetic reuses its probability kernel and is not an independent implementation.

## Lemma 1: selecting successive minimum-degree unit neighbors

Let $x$ have actual minimum degree $d$, put

$$E_x=5d-(v-1),\qquad n=v-1-E_x=2(v-1)-5d>0.$$

Let $A=\{y\ne x:\lambda_{xy}=1\}$, and choose $y\in A$ with minimum degree $e$. Then

$$d\le e\le d+\left\lfloor\frac{396-vd}{n}\right\rfloor.$$

Put

$$t=n-1-\bigl(5e-(v-1)\bigr).$$

If $t>0$, one can choose $z$ having unit codegree with both $x$ and $y$, with actual degree $f$ satisfying

$$e\le f\le e+\left\lfloor\frac{396-vd-n(e-d)}t\right\rfloor.\tag{1}$$

**Proof.** Pair coverage gives $\sum_{u\ne x}(\lambda_{xu}-1)=E_x$. Thus at most $E_x$ vertices have codegree at least two with $x$, and $r=|A|\ge n$. All vertices of $A$ have degree at least $e$, all other vertices have degree at least $d$, and therefore $396\ge vd+r(e-d)\ge vd+n(e-d)$. This proves the bound on $e$.

Within $A\setminus\{y\}$, at most $5e-(v-1)$ vertices have codegree at least two with $y$. Consequently the actual common unit pool $B$ has size at least $r-1-(5e-(v-1))\ge t$. Choose its minimum-degree member $z$, of degree $f$. Since $B\subset A$, we have $f\ge e$. The degree sum gives

$$396\ge vd+r(e-d)+|B|(f-e)\ge vd+n(e-d)+t(f-e),$$

which is precisely (1). All three points are distinct and the three actual codegrees are one. ∎

This is stronger than choosing an arbitrary low-degree unit neighbor and then charging all unused vertices only at degree $d$. It does not assert the existence of a third unit point when $t\le0$.

## Conditional probability certificates

`adaptive.py` implements Lemma 1 with the old avoided-subset quota. `adaptive_component.py` replaces each avoided-subset quota by the component-support bound from `../small31_33/diagnose.py`, always constraining the same actual integer bad-pair vector. Its generic function is `quota(f,N)`, where $f$ is the number of distinct five-element links and $N$ is their maximum support size.

The component-support relaxation is as follows. In a connected component of the link intersection graph with $a$ vertices and $b$ edges, an independent set has size at least

$$\alpha\ge\max\left(\left\lceil\frac{a^2}{a+2b}\right\rceil,
\left\lceil\frac{2a-b-1}{2}\right\rceil\right).$$

The first bound is Caro–Wei plus Cauchy–Schwarz. For the second, fix a spanning tree, remove one endpoint of each of the $b-a+1$ remaining edges, and take a larger bipartition class of the induced forest. The component support is at least $5\alpha$, and at least $6$ if $a\ge2$ because the five-element sets are distinct; an isolated link has support $5$. Components have disjoint supports. The finite dynamic program relaxes over every possible component size and edge count, so a computed lower support greater than $N$ excludes that many or fewer bad pairs. It is only a necessary relaxation, and is combined with the preexisting $\lceil(5f-N)/4\rceil$ bound.

The final finite domain is generated directly by Lemma 1. Every two-lock row uses its actual multiplicities; every conditional three-lock row tests both complete trace patterns. Exact fractions and the actual successful layout/degree assignment are retained in `ADAPTIVE_COMPONENT.json`. Four consecutive center layouts and all distinct degree orders are tested, stopping once a strict bound is found. For a branch labelled `three_pass`, a non-strict two-lock row is replaced by all its admissible three-lock rows; it is not itself claimed strict.

|$v$|entire minimum-degree cases covered|remaining pool-selection cases|remaining three-lock probability types|
|---:|---|---:|---:|
|34|$d=7,8$|7|0|
|35|$d=7,8$|4|0|
|36|$d=7,8,9$|2|0|
|37|none|0|15|
|38|none|0|12|

Thus the package closes genuine entire minimum-degree subcases at 34,35,36 vertices, but does not close any whole vertex-count segment. The component-support strengthening adds the $v=34,d=8,e=12$ two-lock case; it does not remove the listed 37/38 probability failures.

## Exact remaining obligations

The remaining common-pool selection failures $(d,e)$ are:

- $v=34$: $(9,12),(9,13),(10,12),(10,13),(11,11),(11,12),(11,13)$.
- $v=35$: $(9,12),(10,11),(10,12),(11,11)$.
- $v=36$: $(10,11),(11,11)$.

The final $v=36,d=11$ case is necessarily 11-regular, since $36\cdot11=396$. The current elementary common-neighbor argument does not prove three unit locks there. Allowing the second lock to have codegree at most $2,3,4,5$ gives a natural alternative degree bound, but the tested two-lock probability bounds do not close any new full minimum-degree case (`TWO_NONUNIT.json`).

For $v=38$, every remaining probability failure is the separate-edge trace, with sorted degree triples

$$\begin{gathered}
(8,8,8),(8,8,9),(8,8,10),(8,8,11),\ (8,9,9),(8,9,10),(8,9,11),\\
(8,10,11),(9,9,9),(9,9,11),(9,10,11),(10,10,11).
\end{gathered}$$

All same-original-edge three-lock traces pass on this selected domain. The low triple $(8,8,8)$ still has bound $1040783/1038345>1$ after a separate bounded search over all three positions in the 11-position center window. The corresponding $v=37$ obstruction $(8,11,11)$ remains $7578839/7565085>1$; $v=38,(10,10,11)$ remains $46752722/46725525>1$. These searches retain actual fractions in `LAYOUT_PROBE.json`. They show that simply spreading the tested locks within that window does not solve the three highlighted types, not that no layout or stronger argument can work.

`SUMMARY.json` contains the complete remaining degree and trace inputs and all exact bounds. The outstanding mathematical obligations are either a stronger actual lock-selection argument in the 13 pool failures, or an additional valid joint probability deduction for the 27 three-lock types. A failed sufficient bound is not a non-Property-B counterexample.

## Reproduction and verification limits

Run from the project root:

```sh
python3 context/propertyb-m6-67-progress-20261029/mid34_38/adaptive_component.py
```

The auxiliary scripts are bounded diagnostics, not parts needed for the surviving conditional subcase proof. Total recorded numerical CPU was about 33 seconds across the four diagnostics. No Lean, independent probability reimplementation, external reviewer, whole-target proof or updated global bound is claimed.

## Later continuation: frozen complete branches

The preliminary blockage report above records the first bounded diagnostic. Subsequent actual selection lemmas and fourth-lock extensions completely close the 36,37,38 vertex branches. Their final mathematical assembly is `PROOF36_38.md`, with the exact certificate map in its last section. Independent full-domain and numerical replay by the separate small-domain executor is recorded in `../independent36_38/REPORT.md`; it reports `PASS_WITH_DECLARED_IMPORTS`, including exact agreement on all 5386 four-lock rows. This does not upgrade the entire original target.

The 35-vertex minimum-eleven case has also been closed; its proof and the exact remaining minimum-ten obligation are in `STATUS35.md`. Root owns the other remaining 34/35 cases. Preliminary statement “no full vertex segment closed” above is historical and is superseded by this paragraph.

## Final minimum-ten continuation

The 35-vertex minimum-degree-ten gap is now closed by the actual low codegree-two degree-ten partner and degree-twelve common unit center. The final frozen proof is `PROOF35_MIN10.md`, with 102 successful records in `CERT35_MIN10.json`. It does not use the exploratory fourth-lock failures. Independent verification of this new final branch is pending; the previously completed independent 36–38 replay is unaffected.
