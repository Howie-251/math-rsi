# Eight positive four-sets with four negative triples: bounded diagnosis

## Conclusion

The requested strengthening to **exactly eight positive four-sets, at most four negative triples, at most17 negative four-sets, total indexed occurrence at most seven and ground size at most17** is not proved by the current eight-positive argument. Its low-positive-occurrence branch is strict, but three other numerical steps cease to be strict. This is a failure of those sufficient counts, not a counterexample to the proposed lemma.

The unchanged [eight-positive proof](../../../../../proofs/propertyb35/EIGHT_POSITIVE_FOUR_SET_REPAIR.md) and its86 old five-graph representatives were read. No new graph domain, original hypergraph domain, negative-placement table or q3 computation was generated. The original gate and main proof files are untouched.

## 1. Branches that immediately remain strict

For maximum positive occurrence at most two, the occupancy bound is

$$4(7/16)^3+17(7/16)^4=\frac{62769}{65536}<1.$$

If a point $x$ has positive occurrence at least six, fixing it leaves at most two positive four-sets; their16 three-point candidates cannot all be negative triples, since every obstructing triple contains $x$ and its remaining degree budget is at most one. The cases with zero or one remaining set use at most two points.

For positive occurrence five, the disjoint-three remainder still has64 candidates, with at most $4\cdot4+2=18$ blocked. If it has an intersection, four three-point candidates containing $x$ exceed the at-most-two remaining negative occurrences at $x$; the original global bound of three triples is unnecessary there.

For positive occurrence four and a disjoint-four remainder, the256 five-point candidates have separate union bound

$$4\cdot16+17\cdot4=132<256.$$

The intersection remainder at positive occurrence four can also be completed using degree accounting and the existing small-positive gate. In the old notation, $t$ forced triples $\{x,y,z\}$ leave two disjoint variable sets of size $a=4-t$. Necessarily $t\le3$, since $x$ already has four positive occurrences. If $r$ further triples contain $x$ and $b$ negative quadruples contain $x$, then $r+b\le3-t=a-1$. The remaining triples avoiding $x$ block at most one candidate each, giving

$$ar+(4-t-r)+b=a+(a-1)r+b.$$

For $a=4,3,2$ this is at most13,7,3, strictly below $a^2=16,9,4$. If $a=1$, $t=3$ saturates $x$'s degree budget. The only possible additional blocker of the sole four-point candidate is a triple $\{y,u,v\}$; all four triples then contain $y$. Forbid $y$ and keep $x$ red. All negative triples disappear and no negative quadruple contains $x$. The remaining at-most-four positive sets have sizes three or four, and the small-positive zero-triple repair lemma applies. Thus this high-occurrence branch is not the principal obstacle.

## 2. Where the fixed-three-point proof no longer transfers unchanged

Fix a positive three-point $x$. Let $r,b$ be the numbers of negative triples and quadruples containing $x$. The actual indexed budget remains

$$r+b\le4.$$

### Three-point transverse candidates

When the remaining five positive sets have maximum occurrence two, the old graph formula gives $C_3\ge2M_2$. The new separate blocker bound for those three-point transversals, after adjoining $x$, is

$$4r+(4-r)+b\le8+2r\le16.$$

The old stopping rule $M_2\ge7\Rightarrow C_3\ge14$ is therefore insufficient. $M_2\ge9$ is sufficient by this estimate, but the cases $M_2=7,8$ are not disposed of by that original rule. They are outside the old86-graph domain $1\le M_2\le6$; no new domain for them was generated.

### Zero-matching triangle

The old star family has at least175 four-point transversals and still survives. For a triangle, the old proof guarantees only80. The five-point candidate blocker estimate becomes

$$16r+4(4-r)+4b+(17-b)
=33+12r+3b\le81.$$

Thus $80>81$ fails. This bound ignores overlap between blockers and their degree usage in the variable groups. The failure does not assert that81 distinct candidates can actually be blocked.

### The old86-graph four-point candidate step

For $1\le M_2\le6$, $4\le E\le8$, the old complete graph domain remains available unchanged. With $|U|\le16$, the old specified-pair/triple extension bounds are46 and13. The new blocker expression is

$$46r+13(4-r)+13b+(17-b)
=69+33r+12b\le201.$$

The old minimum $C_4=178$ is not enough. This is the main precise mismatch with the previously strict $178>168$ comparison.

To see whether simply using exact extension maxima could repair it, [the bounded check](EIGHT_FOUR_TRIPLES_DIAGNOSIS_CHECK.py) reconstructed only the same86 old representatives. It counted $C_4$ and, separately, the maximum number of those candidates containing a specified pair or triple. Every reconstructed $C_4$ agreed with both old saved counts, including the independent inclusion-exclusion count.

All old representatives with $E\ge5$ are strict by this refined check: $|U|\le15$ gives extension maxima at most42 and12, and the blocker bound is at most185, while their saved minimum $C_4$ is196. Exactly seven old $E=4$ representatives remain nonstrict:

| Old orbit id | $C_4$ | Pair / triple maximum | New separate blocker bound | Difference |
|---:|---:|---|---:|---:|
|0|190|46 /13|201|$-11$|
|2|178|46 /13|201|$-23$|
|4|200|46 /13|201|$-1$|
|20|188|46 /13|201|$-13$|
|34|187|46 /13|201|$-14$|
|49|193|46 /13|201|$-8$|
|66|189|46 /13|201|$-12$|

These are not feasible blocking configurations: the check maximizes each negative event separately and ignores joint degree and overlap restrictions. No negative-placement search was performed.

Finally, the original branch where the remaining five positives themselves have a three-point also needs an additional argument. Replacing three by four negative triples changes its displayed bound to

$$2a+s(a-2),\qquad0\le s\le a,$$

which can equal $a^2$ at $a=4,3,2$ and need not be strict at $a=1$. The previous single equality transfer for three triples cannot simply be cited as the full new branch. The new five-small-positive/one-triple theorem may help with degree-saturated equality transfers, but that is not a complete argument recorded here.

## 3. Actual missing-star B/C2 inputs have more structure than this generic gate

In the intended [seven-high, three-internal source](../../../../../proofs/propertyb35/TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_PARTIAL.md), choose a common point $q\in C$ and a common high-trace leaf $u$ as the two blue high points. For the stated B/C2 choice, the actual signed input is eight positive four-sets, four negative triples and17 negative four-sets on the17 seven-degree exterior points. Positive source edges and negative source edges are disjoint, so the occurrence cap seven is justified.

The eight positives split into two **actual** four-set families, one at $q$ and one at $u$. The point $q$ has four private singleton-trace edges and one relevant pair-trace edge with three exterior points. Pair coverage of $(q,L)$ therefore forces

$$\left|\bigcup_{i=1}^4 A_{q,i}\right|\ge17-3=14.$$

The leaf $u$ has four private singleton-trace edges and two relevant three-trace edges, each with two exterior points. Pair coverage gives

$$\left|\bigcup_{i=1}^4 A_{u,i}\right|\ge17-4=13.$$

Equivalently, within the $q$ side the16 positive incidences have union deficit at most two, and within the $u$ side deficit at most three. The generic eight-positive proof discards this split and these two strong within-side restrictions. They are legitimate inputs for a future tailored repair; they do not enlarge the generic ground size or automatically remove the seven $E=4$ representatives. No such removal is claimed.

## 4. Exact stopping boundary

[EIGHT_FOUR_TRIPLES_DIAGNOSIS_CHECK.json](EIGHT_FOUR_TRIPLES_DIAGNOSIS_CHECK.json) records the exact low-occurrence fraction, all86 reused rows and the seven nonstrict comparisons. Runtime for the old-domain count was below one second. The diagnosis is complete at the requested boundary: the stronger generic lemma is unresolved; the original theorem remains intact; the actual B/C2 pair of four-set union bounds is recorded for the root agent's next decision.
