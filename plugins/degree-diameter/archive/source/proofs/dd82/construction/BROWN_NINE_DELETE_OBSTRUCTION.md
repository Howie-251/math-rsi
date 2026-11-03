# Brown57 extensions require at least ten old deletions

## Claim and status

Complete candidate paper assembly, pending independent review of this assembly and the new seven-III finite checks.

Any graph of maximum degree at most eight and diameter at most two on the 57 labeled Brown vertices and one new vertex deletes at least ten edges of the fixed Brown graph. It also adds exactly as many old-old edges as it deletes. This is a bound on modifications of the fixed Brown graph, not nonexistence of arbitrary order58 graphs. No Lean theorem is claimed.

The reviewed papers `BROWN_EXTENSION_OBSTRUCTION.md` and `BROWN_EIGHT_DELETE_OBSTRUCTION.md` exclude at most eight deletions. Here we exclude exactly nine.

## 1. Exhaustive triangle count split

Use the explicit Brown graph, classes $C,I,E$, and finite facts stated in `BROWN_EIGHT_DELETE_OBSTRUCTION.md`: sizes 8,21,28; each $C$ has degree seven and neighbors only in $E$; each $E$ has two $C$ and three $I$ neighbors; each $I$ has four $I$ neighbors. There are 14 III triangles and 42 IEE triangles. Each $I$ lies in two of each type; every old edge lies in at most one triangle. Old edge types are II, CE, IE, EE.

Suppose nine old edges are deleted. The order58 candidate is 8-regular, by the original root bound. Let $x$ be the new vertex and $S=N(x)$, so $|S|=8$. Counting total edges gives exactly nine added old-old edges.

Every $i\in I$ must lose at least one old triangle: it started in four, and the order58 root repeat budget seven permits at most three. If $a,b$ count distinct destroyed III and IEE triangles, then

$$a+b\le9,\qquad 3a+b\ge21.$$

Therefore $6\le a\le9$. The following cases cover every deletion set:

* $a=6$: excluded by `BROWN_R9_SIX_III_OBSTRUCTION.md`, including its 14-family finite domination check.
* $a=7$: excluded by `BROWN_R9_SEVEN_III_OBSTRUCTION.md`, including both possible union sizes 19 and 21 and their exact finite checks.
* $a=8$: choose one deleted edge from each of the eight distinct III triangles. One extra edge remains, of type II, CE, IE, or EE.
* $a=9$: all nine deletions are II edges, one from each of nine distinct III triangles.

The remainder handles every $a=8$ extra type and $a=9$.

## 2. Common degree and reachability budget

Let $d_v$ be the deletion degree, $k_v=d_v+[v\in C]$ the deficit to eight, and

$$j=|S\cap I|,\quad e=|S\cap E|,\quad
\sigma=\sum_{s\in S}(k_s-1).$$

Only positive-deficit vertices can lie in $S$. There are exactly $\sigma$ available added old-old incidences at $S$. If retained old edges from $S$ cover at most $h$ of the $j+e$ absolute points outside $S$, at least $\max(0,j+e-h)$ added incidences are needed to reach those points. Every remaining added incidence can reach at most one additional internal point from $x$.

For an internal point with $d_i^0$ deleted II edges, its retained original closed neighborhood covers at most $5-d_i^0$ internal points. These are upper bounds on unions, so overlaps only decrease coverage.

## 3. Every all-II nine-deletion pattern

This handles $a=9$ and the II-extra case at $a=8$ (and would also handle any smaller feasible $a$ with all deletions II).

Choose $a$ base deleted edges from the distinct destroyed III triangles. Since no IEE triangle is destroyed, those triangles cover all 21 internal points. Their $3a$ vertex incidences therefore have exactly $R=3a-21$ repetitions; each internal point lies in at most two III triangles. Base deletion degrees are at most two, and at most $R$ vertices can have degree two. Thus the total number of spare incidences after the base deletions is at most $R$.

Each of the remaining $9-a$ II deletions creates at most two additional spare incidences. Consequently

$$\sigma\le R+2(9-a)=a-3\le6.$$

No external point has positive deficit, so $e=0$. No original edge joins $S$ to an unselected absolute point, so reaching $C$ needs at least $j$ added incidences. Thus $j\le\sigma\le6$.

All deleted edges at internal points are II, and no selected absolute point has an internal neighbor. Hence the number of internal points reachable from $x$ is at most

$$5j-\sum_{i\in S\cap I}d_i+(\sigma-j)=3j\le18,$$

where $\sigma=\sum_{i\in S\cap I}d_i-j$. This cannot reach all 21 points of $I$.

## 4. Eight base III edges and a CE extra

The eight selected triangles cover all $I$, since CE destroys no triangle. Their 24 incidences have exactly three repetitions; hence base spare incidences at $I$ total at most three. The CE deletion creates at most one further spare incidence, at its absolute endpoint. Thus $\sigma\le4$, and $e\le1$.

If its external endpoint belongs to $S$, that point retains only one absolute neighbor. Consequently $h\le e$, and at least $j$ spare incidences are required for $C$. In particular $j\le4$.

Write $\varepsilon_C=1$ if the deleted CE edge's absolute endpoint lies in $S$, and zero otherwise. Then

$$\sigma=\sum_{i\in S\cap I}d_i^0-j+\varepsilon_C.$$

An external selected point has at most three retained internal neighbors, so internal reachability is at most

$$5j-\sum d_i^0+3e+\sigma-j
=3j+3e+\varepsilon_C\le16<21.$$

## 5. Eight base III edges and an IE extra

The eight selected III triangles cover at least 20 internal points, since the extra destroys only one IEE triangle. If they cover 21, their base spare count is at most three and the IE extra creates at most one more. If they cover 20, their base spare count is at most four, and the extra's internal endpoint must be the unique uncovered point; its new deficit is one and creates no spare incidence. Thus in both cases $\sigma\le4$ and $e\le1$.

Old external-to-absolute coverage is at most $2e$, so $C$ requires at least $\max(0,j-e)$ added incidences. Hence $j\le e+\sigma\le5$.

Let $\varepsilon=1$ if the extra's internal endpoint lies in $S$, and zero otherwise. Then

$$\sigma=\sum_{i\in S\cap I}d_i^0+\varepsilon-j.$$

The external endpoint retains two internal neighbors. The extra IE deletion does not reduce any internal point's internal neighborhood. Thus the internal reachability bound is

$$5j-\sum d_i^0+2e+\sigma-\max(0,j-e)
=4j+2e+\varepsilon-\max(0,j-e).$$

If $j\ge e$, this is $3j+3e+\varepsilon\le19$. If $j<e$, then $j=0,e=1,\varepsilon=0$, and the bound is two. Both contradict the required 21.

## 6. Eight base III edges and an EE extra

This is exactly the complete branch excluded by `BROWN_R9_EIGHT_III_OBSTRUCTION.md`. Its finite premises inspect all 14 full-cover families and all 42 twenty-cover families, with two possible EE edges for the unique uncovered point in the latter case. The proof uses the actual retained neighborhoods and spare-incidence budget; it does not assume an arbitrary adjacency completion impossible merely from a solver result.

## 7. Conclusion and finite dependencies

Every nine-deletion pattern belongs to one of the preceding cases and is impossible. The earlier bound excludes fewer deletions. Therefore every such extension requires at least ten old deletions and ten old-old additions.

The finite obligations are scoped to this one explicit Brown graph: basic triangle/degree data; the six-III constrained domination problems; both seven-III relaxed coverage problems; and the eight-III+EE incidence facts. Their sources and complete outputs are named in the corresponding papers. In particular the new seven-III code/source/coverage requires its independent review before this assembly is promoted to an accepted claim.

No existence or nonexistence conclusion about arbitrary58-point graphs follows. A new construction is free to use a different graph or more edits; this bound explains why very small modifications of the fixed Brown witness fail.

## Current review status

Reviewed complete paper assembly: fresh proof-checker-brown9-complete-20261011 PASS28 obligations, with actual finite reruns and independent case enumeration; GeminiB10 accepted. No Lean theorem.
