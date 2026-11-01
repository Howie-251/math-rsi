# Complete new mixed-gate pass: two higher traces, missing P3+K2 or3K2

## Result and exact scope

The new [seven positives / two positive triples / one negative triple theorem](../../../../../../proofs/propertyb35/SEVEN_MIXED_TWO_SMALL_ONE_TRIPLE_REPAIR.md) covers all previously stopped cases in this necessary P-side selector. A fresh complete run returned:

| Missing graph | High-trace-pair orbits | Retained necessary J inputs | Nongated inputs |
|---|---:|---:|---:|
|$P_3+K_2$|49|516812|0|
|$3K_2$|34|732883|0|
|Total|83|1249695|0|

The run completed in1.418 seconds and has status `COMPLETE_NECESSARY_P_DOMAIN_PASS`. All83 orbit rows finished, and each row's accepted-tag counts sum to its retained inventory count. No exterior sets, external layouts or original hypergraphs were enumerated.

Source and full per-high-orbit counts are [RUN_TWO_SMALL.py](RUN_TWO_SMALL.py) and [RUN_TWO_SMALL.json](RUN_TWO_SMALL.json). The new theorem's main statement and proof were read before the run. **The anticipated extension allowing four positive triples with no negative triples was not used.**

The prior pilot source and its first failed P inventory were read. Its generation/selection implementation was reused as the starting code, then the two shapes were rerun from their first high-trace orbit with the new gate. No prior numerical acceptances, completed orbit counts or witness output were used as the result of this new run. This is a complete fresh deterministic run, not a second independently written generator; a separately implemented domain/gate replay remains a distinct verification step. The old pilot and evidence are unchanged.

## 1. Conditional whole-branch statement

**Candidate finite-selection theorem.** Let $H$ be a simple five-uniform hypergraph on24 vertices, with35 edges, pair coverage, minimum degree at least seven, no all-seven-degree edge and seven high points $P$. Suppose exactly three edges are contained in P. Let F be their missing-pair graph and C their common intersection. Assume exactly two other edges have P-traces of size at least three, and both traces avoid C. If F is $P_3+K_2$ or $3K_2$, then H has Property B.

The complete actual-input proof below uses only the stated finite P-side selector and previously proved generic repair gates. The finite domain passed in this run. This report does not by itself claim independent-generator or designated cross-model acceptance, nor does it claim the full $m(5)\ge36$ result.

## 2. Actual P inventory and the complete necessary domain

All P points have degree eight and all17 exterior points have degree seven: the seven high points exactly use the seven units of total degree excess above seven. The absence of an all-seven-degree edge makes P a hitting set.

An internal edge is $P-e$ for one of the three distinct missing pairs $e\in F$. Normalize the two shapes as

$$P_3+K_2:\quad F=\{01,12,34\},\ C=\{5,6\},$$

$$3K_2:\quad F=\{01,23,45\},\ C=\{6\}.$$

Write $D=P-C$, and denote the two actual higher traces by $T_1,T_2\subseteq D$. Each has size three or four. Their P traces may be equal because the distinct original edges can have different exterior parts. Put

$$c_v=3-d_F(v),\quad h_v=|\{i:v\in T_i\}|,\quad
n_2=11-|T_1|-|T_2|,\quad n_1=30-n_2.$$

The actual nontop pair traces form a loopless multigraph J on P with exactly $n_2\in\{3,4,5\}$ indexed edges. Let $s_v=d_J(v)$. Actual singleton counts are

$$u_v=8-c_v-h_v-s_v\ge0.\tag{1}$$

Actual coverage of the17 exterior points by the star of v gives the second capacity bound

$$s_v\le15-4c_v-\sum_{i:v\in T_i}(|T_i|-1).\tag{2}$$

Indeed the complete exterior capacity of the noninternal star is

$$4u_v+3s_v+\sum_{i:v\in T_i}(5-|T_i|)
=32-4c_v-s_v-\sum_{i:v\in T_i}(|T_i|-1)\ge17.$$

Finally, every P-pair not covered by an internal edge or either higher trace must occur as a J edge. Singletons cannot cover such a pair.

The domain retains every J satisfying(1),(2) and these required-support tests. These conditions are necessary, and can retain inventories with no actual exterior realization; that only enlarges the tested domain safely. No converse realization assertion is made.

### High-trace orbit coverage

For $P_3+K_2$, D has five vertices, with15 possible three-/four-subsets and120 unordered two-trace multisets. The automorphism group of the missing graph on D has four elements: independent path reversal and isolated-edge reversal. Applying every such automorphism to every two-trace multiset and taking its least image gives exactly49 orbits.

For $3K_2$, D has six vertices, with35 possible trace sets and630 unordered two-trace multisets. The matching automorphism group has48 elements: permute the three missing edges and independently reverse their endpoints. The same direct quotient gives exactly34 orbits.

The code does not assume these orbit lists. It enumerates all permutations of D, retains exactly those preserving F, forms every unordered trace pair with repetition, and computes its canonical image. Permuting isolated C vertices has no effect on the trace pairs; J is subsequently enumerated with all seven labels, so no C permutation quotient is needed for completeness.

### Pair-trace multiset coverage

For each trace-pair representative, J is enumerated as every multiset of exactly $n_2$ among the21 unordered P-pairs. Its unique sorted repeated-index sequence is generated by `combinations_with_replacement`. The raw counts for $n_2=3,4,5$ are

$$\binom{23}3=1771,\quad\binom{24}4=10626,\quad
\binom{25}5=53130.$$

Each sequence uniquely specifies all multiplicities and all J degrees. Only(1),(2) and required P-pair support are filtered. This proves that every actual labeled inventory over the normalized high traces is retained.

The completed domain by trace sizes is:

| Missing graph | Sizes | High orbits | Necessary J inputs |
|---|---|---:|---:|
|$P_3+K_2$|3,3|22|413208|
|$P_3+K_2$|3,4|19|98437|
|$P_3+K_2$|4,4|8|5167|
|$3K_2$|3,3|13|621430|
|$3K_2$|3,4|12|103650|
|$3K_2$|4,4|9|7803|

## 3. Exact blue-pair witness and all original edge types

For a retained inventory, examine all21 P-pairs $\{i,j\}$. A pair is eligible when it is not a missing edge of F and it meets both $T_1,T_2$. Color i,j blue and the other five P points red.

Every internal edge contains a blue point, since otherwise its missing pair would be $\{i,j\}$. It also has at least three red points. Both higher traces contain blue, and their size at least three ensures they contain red as well. Thus all these edges are already proper.

Put $S=s_i+s_j$ and $k=m_J(i,j)$. The complete unresolved signed family on the actual17-point exterior has counts

$$\begin{aligned}
m_4&=16-c_i-c_j-h_i-h_j-S,\\
m_3&=k,\\
t&=n_2-S+k,\\
b&=n_1-m_4.
\end{aligned}\tag{3}$$

Blue singleton traces give $m_4$ positive four-sets. The k all-blue pair traces give positive triples. The all-red pair traces give t negative triples, and red singleton traces give b negative four-sets. Other pair traces have both colors and stay proper. These are all original edge types because P hits every edge. Both higher traces are proper already, so no negative singleton or pair is silently dropped.

Different signed indices come from different original edges. Every exterior point has original degree seven, hence its total signed occurrence is at most seven. The repair gates below therefore have their common degree hypothesis justified by the actual H.

The deterministic witness routine scans eligible blue pairs lexicographically and returns the first whose four counts in(3) meet a listed gate. Every retained inventory has such a pair in the complete new run. On returning its repair R, color R red and the other exterior points blue. Positive edges gain red, negative edges retain blue, and already proper internal/higher/mixed-pair edges keep their P colors. This is a proper coloring of every original edge.

## 4. Gate predicates and the new gate's precise role

All statements below have total indexed occurrence at most seven. Exact-count gates are used only with their exact counts; no positive padding is performed.

* New gate: $m_4+m_3\le7$, $m_3\le2$, $t\le1$, with arbitrary b. These positives are all3/4 sets, exactly within [SEVEN_MIXED_TWO_SMALL_ONE_TRIPLE_REPAIR](../../../../../../proofs/propertyb35/SEVEN_MIXED_TWO_SMALL_ONE_TRIPLE_REPAIR.md).
* Four-small gate: $m_4+m_3\le4$, $t\le3$, arbitrary b, by [FOUR_SMALL_POSITIVE_THREE_TRIPLE_REPAIR](../../../../../../proofs/propertyb35/FOUR_SMALL_POSITIVE_THREE_TRIPLE_REPAIR.md).
* Five-small gate: $m_4+m_3\le5$, $t\le2$, arbitrary b, by [FIVE_SMALL_POSITIVE_TWO_TRIPLES_REPAIR](../../../../../../proofs/propertyb35/FIVE_SMALL_POSITIVE_TWO_TRIPLES_REPAIR.md). Its at-most-three positive pair condition is met with zero positive pairs here.
* Pure-four-set gates: $m_3=0$ and either $(m_4,t,b)\le(5,10,32)$, $(6,6,35)$, or $(7,4,22)$, using respectively [five](../../../../../../proofs/propertyb35/FIVE_POSITIVE_TEN_TRIPLES_REPAIR.md), [six](../../../../../../proofs/propertyb35/SIX_POSITIVE_SIX_TRIPLES_REPAIR.md), or [seven](../../../../../../proofs/propertyb35/SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md) positives.
* Exact eight-four-set gates: $m_3=0,m_4=8$, and either $t\le4,b\le17$ ([new eight gate](../../../../../../proofs/propertyb35/EIGHT_POSITIVE_FOUR_TRIPLES_REPAIR.md)) or $t\le3,b\le20$ ([old eight gate](../../../../../../proofs/propertyb35/EIGHT_POSITIVE_FOUR_SET_REPAIR.md)). Ground17 is justified.
* The source retains the prior seven/eight mixed predicates. They receive no acceptances in this run after the new gate is placed first, but they are unchanged valid predicates. No gate requiring four positive triples with t zero is present.

Acceptance counts, using the source's fixed priority, are:

| Gate tag | $P_3+K_2$ | $3K_2$ |
|---|---:|---:|
|new seven-mixed/two-small/one-T|149149|201812|
|five-small/two-T|5042|76604|
|six-four/six-T|64317|157476|
|seven-four/four-T|162455|191587|
|eight-four|135804|105314|
|four-small/three-T|45|90|
|Total|516812|732883|

These tags depend on scan priority and are not disjoint structural classes independent of that priority. They do give a full acceptance partition of this run, and their total is checked for every high-trace row.

As a concrete connection to the old stop, the inventory

$$F=\{01,12,34\},\quad T_1=013,\quad T_2=124,
\quad J=2\cdot02+04+23+56$$

has eligible blue pair02 with $m_4=4,m_3=2,t=1,b=21$. The new theorem directly accepts these six positive3/4 sets, including the two positive triples; it needs no negative-quadruple bound or geometric intersection assumption. This is exactly the former unresolved necessary inventory, rather than a new unconstrained example replacing it.

## 5. Transport and acceptance boundary

Every actual missing $P_3+K_2$ or $3K_2$ graph can be labeled as in Section2. Apply an automorphism of its D support to put its unordered high-trace pair in the canonical orbit; carry all original J labels along that same map. The necessary degree, capacity and support conditions remain true, so the normalized J occurs in the enumerated domain. Retrieve a blue pair via(3), then invert the P relabeling. This preserves actual P colors, all source-edge indices, signed sizes and the applicable repair theorem. Section3 returns the actual proper coloring of H.

The record proves full computational coverage of this necessary selection domain under the stated repair lemmas, and gives the complete actual caller. It does not claim that all retained inventories are realizable, or that a new generic gate follows from the numerical counts. The underlying old and new repair proofs, independent-generator replay, and designated cross-model review remain separately identifiable dependencies.
