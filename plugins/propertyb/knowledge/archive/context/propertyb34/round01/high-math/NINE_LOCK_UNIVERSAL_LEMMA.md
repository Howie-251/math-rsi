# A reusable nine-lock coloring criterion on at most 25 vertices

## Claim and status

Let $H$ be a simple five-uniform hypergraph on at most $25$ vertices with exactly
$34$ edges. Suppose it contains nine distinct vertices $s_1,\ldots,s_9$ such
that every pair among them has codegree one, $d(s_i)=6$ for $i\le5$, and
$d(s_i)=7$ for $i>5$. Then $H$ has Property B.

**PROVABLE AS STATED**, as a paper corollary of the complete $q=5$ table in
`CANDIDATE_TWENTYFIVE.md`. Global pair covering is not assumed.

## Proof

### 1. Pad to 25 vertices

Adjoin isolated vertices until the vertex set has size $25$. This preserves
the edge count, simplicity, five-uniformity, selected degrees, and selected
codegrees. A proper coloring of the enlarged hypergraph restricts to one of
the original hypergraph.

### 2. The bad-pair quotas do not require pair covering

For a chosen center, its link is a family of $d$ distinct four-element sets in
a universe of size $M$. For each universe vertex $y$, write $r_y$ for the number
of link sets containing it, and let $b$ count unordered intersecting link pairs.
Then
$$4d-M\le\sum_y(r_y-1)_+
 \le\sum_y\binom{r_y}{2}
 =\sum_{\{E,F\}}|E\cap F|\le3b.$$
The last bound holds because distinct four-element link sets intersect in at
most three elements. Hence
$$b\ge\max\left(0,\left\lceil\frac{4d-M}{3}\right\rceil\right).$$
No assumption that the link covers the universe has been used.

Apply this with $M=24$ for the total link and with $M=16$ for the subfamily of
edges whose trace on the nine locks is exactly the center. These are precisely
the total and nested pure quotas used by the $q=5$ certificates. Actual slots,
their capacities, and both directed weights have the same meanings after
isolated padding.

### 3. Use the complete local table

The unit codegrees on the nine locks ensure their multi-point traces partition
all lock pairs, with each multi-point trace occurring once. Selected degrees
and the $34$ edges determine the singleton and empty counts. Thus the input
belongs to one of the complete $11,692$ colored $q=5$ profiles.

Every profile has a strict exact probability certificate. The largest bound is
$12869/12870<1$; every retained witness has independent labelled-injection A/B/C
replay. The general probability bound and quotas from Step 2 apply to this
actual hypergraph even though the added vertices are isolated. Therefore a
successful permutation and proper coloring exist. Restricting the coloring
proves the original claim. $\square$

The relevant sources are `V25_NINE_Q5_CATALOGUE.json`,
`V25_NINE_Q5_BOUNDS.json`, and `FULL25_COVERAGE_AUDIT.json`. This criterion is a
separate conditional lemma; applying the pair-covering 25-vertex theorem
directly to an isolated padding would be invalid.
