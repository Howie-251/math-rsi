# Six high points, one internal edge: bounded two-higher-trace pilot

## Exact run and stopping point

The requested short pilot was run with the new seven-mixed gate and its verified zero-negative-triple extension, the existing small-positive gates, six-positive/six-triple and seven-positive/four-triple gates, and the dimension-free ten-positive/zero-triple corollary. The17-point eight-four-set gates were **not** used on this18-point exterior.

[PILOT.py](PILOT.py) and [PILOT.json](PILOT.json) save the fresh source and complete first-stop record. Runtime was0.027 CPU seconds. The pilot stopped during the first requested inventory $(n_2,n_3,n_4)=(6,2,0)$, with the unique nine-degree point in C. It did not reach $(5,1,1)$ or either optional three-higher-trace inventory. No original H or exterior set was enumerated; the old P6 canonical proof is unchanged.

The first rejected signature is **not a mathematical obstruction**: one of its blue choices is already accepted by the separately proved exact18-point eight-mixed gate, which was not included in the first list of tested predicates. That distinction is recorded below rather than claiming an unrepairable input.

## Actual input, retained degree-nine position, and necessary P domain

Use $P=\{0,\ldots,5\}$, $C=\{0,\ldots,4\}$ for the unique internal edge, and $a=5$. Let $d_v$ be one nine and five eights. The pilot separates the two genuine degree orbits: nine at0 in C, or nine at a; its high-trace quotient uses only permutations of C preserving that position.

For each requested inventory, higher traces are the appropriate three-/four-subsets of P with $T_1\cap T_2\subseteq\{a\}$. The already closed case with a common C point is not included. The exact actual counts are

$$n_1=24+n_3+2n_4,\quad c_v=\mathbf1_{v\in C},\quad
h_v=|\{i:v\in T_i\}|,\quad
u_v=d_v-c_v-h_v-s_v\ge0.$$

Each J is a multiset of $n_2$ of the15 unordered P-pairs. For the two requested edge numbers the raw multiset counts are $\binom{20}6=38760$ and $\binom{19}5=11628$. The following filters are necessary for actual H:

* If a P-pair is not covered by C or either higher trace, J must cover it.
* The recovered singleton counts $u_v$ are nonnegative.
* Coverage of the18 exterior points gives

$$s_v+\sum_{i:v\in T_i}(|T_i|-1)\le4d_v-18-4c_v.$$

No exterior realization is assumed for each retained necessary inventory.

For a blue P-pair $\{i,j\}$ meeting C and both higher traces, the internal edge and both higher traces are proper. The exact unresolved signed counts are

$$m_4=u_i+u_j,\quad m_3=J_{ij},\quad
t=n_2-s_i-s_j+J_{ij},\quad b=n_1-m_4.$$

The17-point gates are not applicable because the actual exterior has18 points. Positive/negative source indices are disjoint, so D7 is justified by the original18 seven-degree points. There are no omitted zero-P edges: the standing no-all-seven-edge assumption makes P a hitting set. Both higher traces are proper under the eligible blue-pair rule, so no negative singleton/pair is silently deleted.

## First necessary inventory

The first stop has

$$T_1=012,\quad T_2=345,\quad d=(9,8,8,8,8,8),$$

$$J=2\cdot01+02+05+15+25,$$

$$s=(4,3,2,0,0,3),\qquad u=(3,3,4,6,6,4).$$

It satisfies the degree and outer-capacity tests and the necessary P-pair support tests. The complete eligible-blue-pair signatures are:

| Blue pair | $(m_4,m_3,t,b)$ |
|---|---|
|03 or04|$(9,0,2,17)$|
|05|$(7,1,0,19)$|
|13 or14|$(9,0,3,17)$|
|15|$(7,1,1,19)$|
|23 or24|$(10,0,4,16)$|
|25|$(8,1,2,18)$|

Every signature falls outside the first predicate list. But blue05 has **exactly seven positive four-sets and one positive triple, no negative triples and19 negative quadruples**, total indexed occurrence at most seven, on18 points. It therefore meets [EIGHT_MIXED_POSITIVE_EIGHTEEN_REPAIR](../../../../../proofs/propertyb35/EIGHT_MIXED_POSITIVE_EIGHTEEN_REPAIR.md) directly. This uses the correct18-point theorem and is unrelated to applying an inadmissible17-point eight-four-set gate.

Thus the present run supplies only an accurate selector stopping record, not an unresolved mathematical inventory or a whole-inventory claim. Continuing the same P domain with that additional compatible gate would be a distinct authorized run with fresh output; the first-stop record is preserved.
