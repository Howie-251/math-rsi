# Independent verification of v34/minimum10 and the complete 34-point interface

**PASS (same-family / provisional).** The new 34-point/minimum-ten proof in `../34_min10/PROOF.md` has no identified mathematical gap. Its complete 40-type necessary domain was independently reconstructed and every recorded actual layout reproduced with exact independent injection probabilities and component quotas. All bounds equal the submitted rational values and are strictly below one; the maximum is $413127/413540$.

The older 34-point/minimum-seven-or-eight adaptive domain was also completely reconstructed and independently replayed using its actual older quota version. All eleven rows match exactly and are strict; their maximum is $619799/620310$. The final run took approximately 0.157 CPU seconds.

Together with the already checked minimum-nine and minimum-eleven branches, this completes the actual-input interface for **all 34-point inputs** under the shared minimal-counterexample, component-support and conditional-permutation probability imports. This does not assert the full $m(6)\ge67$ result, a new Lean verification, or external-model acceptance.

## 1. Complete minimum-ten selection

Fix the same actual finite simple six-uniform hypergraph on 34 vertices, with 66 edges, pair coverage and minimum degree ten. Total degree is 396.

If there are two ten-degree vertices, choose them. Their actual codegree lies in $1\ldots10$, giving exactly the ten necessary pair types
\[
\ell_3=\lambda,\quad\ell_1=\ell_2=10-\lambda,\quad\ell_0=46+\lambda.
\]
All ten exact pair bounds are strict. Otherwise fix the unique ten-degree vertex $x$; every other vertex then has degree at least eleven. If $x$ has an eleven-degree unit-codegree partner, the additional type $(10,11,1)$ is strict, with value $370673/372186$ at positions $(16,17)$.

It remains to assume every actual unit-codegree partner of $x$ has degree at least twelve. Let $u$ be the number of these actual partners. Pair coverage gives
\[
\sum_{y\ne x}(\lambda_{xy}-1)=50-33=17,
\]
so there are at least $33-17=16$ unit partners. The degree baseline is $10+33\cdot11=373$, leaving 23 excess units. Each unit partner consumes at least one such unit, so
\[
16\le u\le23. \tag{1}
\]
There are $33-u$ nonunit partners. Their degree excess above eleven is at most $23-u$, because unit partners already consume at least $u$. Consequently at least
\[
(33-u)-(23-u)=10
\]
nonunit partners have degree exactly eleven.

The same nonunit partners each consume at least one of the 17 codegree-excess units. The remaining number is
\[
17-(33-u)=u-16\le7.
\]
Thus at most seven nonunit partners can have codegree at least three with $x$. Among the at least ten eleven-degree nonunit partners, at least three therefore have codegree exactly two. Choosing any two of those three gives distinct actual vertices $y,z$ with
\[
(d(x),d(y),d(z))=(10,11,11),\qquad
\lambda_{xy}=\lambda_{xz}=2.
\]
There is no independence assumption between the degree budget and the codegree budget: the intersection lower bound uses the same actual partner set. All inequalities were also checked over every permitted integer $u=16,\ldots,23$.

## 2. Complete triple-trace domain

Write $\lambda=\lambda_{yz}$. Coverage and endpoint degrees give $1\le\lambda\le11$. The triple intersection multiplicity satisfies $0\le\tau\le\min(2,\lambda)$. All actual trace counts follow uniquely:
\[
\ell_7=\tau,\quad\ell_3=\ell_5=2-\tau,\quad
\ell_6=\lambda-\tau,
\]
\[
\ell_1=6+\tau,\quad\ell_2=\ell_4=9-\lambda+\tau,
\quad\ell_0=38+\lambda-\tau.
\]
Only the endpoint singleton restriction $9-\lambda+\tau\ge0$ further restricts the stated ranges. There are two types at $\lambda=1$, three each at $\lambda=2,\ldots,9$, two at $\lambda=10$, and one at $\lambda=11$, giving $2+8\cdot3+2+1=29$ types.

The independent program reconstructs these 29 dictionaries directly from the actual degree and codegree specifications, adds the ten repeated-ten-degree pair dictionaries and the one $(10,11,1)$ pair, and checks that its complete key set equals the submitted 40-row set with no duplicate keys. It also checks every actual degree/codegree marginal, triple multiplicity and chosen position vector.

## 3. Exact independent probability replay and quota scope

The replay uses the pre-existing independent falling-factorial uniform-injection probability formula extracted from the older independent checker. It imports neither the new submitted probability generator nor its quota implementation.

The component quota is independently supplied by the already audited bottom-up exact-edge component knapsack in `../independent31_33/check.py`. This is the strengthened **three-bound** version: random-order/Cauchy–Schwarz, feedback-vertex/forest, and unique-complement support at least eleven. For 37 of the 40 rows, independent complete-link-pool cheapest-cell deduction exactly reproduces the certificate.

Precisely the three rows with $\lambda=2$ use the maximum over individual avoided-lock quota deductions. The independent implementation enumerates every $R\subseteq S\setminus\{j\}$, computes the actual trace subfamily size $f_R$, obtains the quota with support $33-|R|$, and fills eligible unordered cells in increasing nonnegative exact weight. Taking the maximum of these costs preserves the lower-bound direction for the same actual bad-pair cost. The deductions are not added. The three exact values are:

| $\tau$ | Actual positions | Independent exact bound |
|---:|---|---:|
|0|$(16,17,19)$|742709/744372|
|1|$(16,17,19)$|7433509/7443720|
|2|$(16,17,19)$|927532/930465|

Every row has exact equality to its recorded rational value and is strictly below one. The complete 40-row maximum is $413127/413540<1$. Hence every minimum-ten actual input reaches an applicable strict bound through the complete selection proof above.

## 4. Complete older adaptive domain at minimum seven and eight

For a minimum-degree vertex $x$ of degree $d$, at least
\[
n=2\cdot33-5d=66-5d
\]
partners have codegree one. If all such partners had degree above $d+\lfloor(396-34d)/n\rfloor$, the minimum-degree baseline plus their excess degree would exceed total degree 396. Therefore the actual partner degree can be chosen in the complete ranges
\[
d=7:\ e=7,\ldots,12,\qquad
d=8:\ e=8,\ldots,12.
\]
These are six plus five unit-codegree pair types, exactly the eleven relevant rows in `../mid34_38/ADAPTIVE_COMPONENT.json`. No three-lock branch is required for these two minimum degrees. The program independently reconstructs the domain and verifies exact set equality.

The row labelled degree pair $(7,12)$ assigns lock degrees $(12,7)$ at its recorded positions, and the row labelled $(8,12)$ assigns $(12,8)$. These are valid label permutations of the same actual pair. The replay preserves the **assigned** degrees and slot labels and does not substitute the sorted reporting degrees into the probability formula.

The older adaptive quota differs from the new quota above in two respects. Its component support bound has only the random-order/Cauchy–Schwarz and feedback-vertex/forest terms; it does **not** include the unique-complement eleven-point term. Its deduction solves the joint integer complete-pool/avoid-other-lock constraints, rather than taking their separate-cost maximum. This exact old version was independently reconstructed instead of silently upgrading the recorded evidence.

For a unit-codegree pair, the only positive unordered cells through a lock are its singleton–singleton core, capacity $\binom{d-1}{2}$, and singleton–shared-edge cell, capacity $d-1$. The shared-edge/shared-edge cell has capacity zero. Let their selected integer bad-pair counts be $z_0,z_1$, with old quotas $q_{\rm all}$ and $q_{\rm avoid}$. The exact necessary constraints are
\[
z_0\ge q_{\rm avoid},\qquad z_0+z_1\ge q_{\rm all},
\]
with both natural cell capacities. For every permitted $z_1$, the least-cost core count is
\[
z_0=\max(0,q_{\rm avoid},q_{\rm all}-z_1),
\]
because its weight is nonnegative. Enumerating $z_1=0,\ldots,d-1$ therefore gives the exact joint minimum. This independent implementation uses the old two-bound component DP rebuilt from scratch and the independent injection weights.

All eleven reconstructed old adaptive values equal their stored fractions and are strict, including the $(8,12)$ type. The maximum is $619799/620310$.

## 5. Complete 34-point original-input interface

For any pair-covering 34-point six-uniform hypergraph with total degree 396,
\[
\delta\ge\lceil33/5\rceil=7,\qquad
\delta\le\lfloor396/34\rfloor=11.
\]
Thus the following branches cover every possible actual minimum degree:

| Actual minimum degree | Complete local types | Proof and independent evidence |
|---|---:|---|
|7 or 8|11|This audit, §4; exact old adaptive replay|
|9|27|`../34_min9/REPORT.md`, `CERTIFICATE.json`, previously independently checked|
|10|40|This audit, §§1–3; all forty rows replayed|
|11|9|`../34_min11/REPORT.md`, `CERTIFICATE.json`, root-read proof and two probability implementations|
|Total|87|Complete 34-point local interface|

The program checks the existing minimum-nine and minimum-eleven evidence interfaces and recorded strict values, while this run newly recomputes the forty minimum-ten and eleven older adaptive rows. It does not represent the previously completed branches as newly recomputed again.

No point-count, degree, codegree, quota, or certificate assumption is introduced as an additional hypothesis on the original all-hypergraph problem: pair coverage and the fixed 34-point branch are the declared internal reduction inputs. Every actual input inside this branch is matched to a fully verified necessary local domain and a strict probability bound.

Reproduce from the project root:

```sh
python3 context/propertyb-m6-67-progress-20261029/independent34_min10/check.py
```

`CHECK.json` records all new probability rows, old-version quota inputs, selection budgets and the complete 34-point interface. This is a same-family/provisional local audit with the usual software trust and the shared declared mathematical imports.
