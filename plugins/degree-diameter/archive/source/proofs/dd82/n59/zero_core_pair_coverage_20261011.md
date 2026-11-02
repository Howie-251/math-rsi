# Proof Package: at least seventeen triangle-bearing vertices under N15

## Claim

Let $G$ be a simple undirected graph on $59$ vertices with maximum degree at most $8$ and diameter at most $2$. Assume the N15 condition at every vertex lying in no triangle: its actual defect row has exactly two entries equal to $2$ and two entries equal to $1$, and its support induces the two equal-weight matching edges. Let $N$ be the vertices lying in at least one triangle, $m=|N|$, and $T$ the number of triangles. Then

$$m\ge17,\qquad T\ge6.$$

A more general necessary inequality established below is

$$\binom m2\le40m-531.$$

## Status

PROVABLE AS STATED, conditional on the stated global zero-row N15 hypothesis and the zero-neighbor lemma in `independent_zero_common_neighbors_20261011.md`. Complete paper derivation; independent review pending. This is a theorem about actual graphs and their actual defect matrix, not a claim that all legal graphs satisfy N15.

## Assumptions and notation

The ordinary Moore root count makes $G$ $8$-regular: a vertex of degree at most $7$ could reach at most $1+7+7\cdot7=57$ vertices in two steps. Set $Z=V(G)\setminus N$, and let $d_N(v)=|N_G(v)\cap N|$ for every vertex $v$. Write $e_N$ for the number of edges of $G[N]$.

The predecessor's zero-neighbor lemma, using N15, the heavy-endpoint lemma, and exact zero-support transport, gives

$$d_N(z)\ge2\qquad(z\in Z).\tag{1}$$

Every vertex of $N$ also has at least two neighbors in $N$, namely the other vertices of one of its triangles. Consequently

$$2\le d_N(v)\le8\qquad(v\in V(G)).\tag{2}$$

## Proof strategy and dependency map

1. The predecessor's heavy-endpoint and transport argument gives (1).
2. Regularity counts the total of $d_N$ across all $59$ vertices.
3. A chord bound for $\binom d2$ bounds all two-step connections between vertices of $N$.
4. Diameter two requires coverage of every pair of vertices in $N$. Every triangle contributes three duplicated connections, which must be subtracted.
5. The resulting inequality excludes $m=15$ and $m=16$; the simpler edge count already excludes $m\le14$.

## Proof

**Step 1. Basic edge counts.** Counting incidences with vertices in $N$ gives

$$\sum_{v\in V(G)}d_N(v)=8m.$$

From (2), $8m\ge118$, so the integer $m$ is at least $15$. Counting edges between $N$ and $Z$ using (1) gives

$$8m-2e_N=e(N,Z)\ge2(59-m),$$

and therefore

$$e_N\le5m-59.\tag{3}$$

Every vertex of $N$ occurs in at least one triangle, so counting triangle-vertex incidences also gives

$$3T\ge m.\tag{4}$$

**Step 2. Total two-step coverage of the core.** For $2\le d\le8$,

$$\binom d2\le1+\frac92(d-2),\tag{5}$$

because the right side minus the left side equals $(d-2)(8-d)/2$, which is nonnegative. Applying (5) to (2), then summing, yields

$$\sum_{v\in V(G)}\binom{d_N(v)}2
\le59+\frac92(8m-118)
=36m-472.\tag{6}$$

**Step 3. Pair coverage and exact triangle duplication.** Each edge of $G[N]$ covers one unordered pair in $N$. Each length-two path whose endpoints belong to $N$ covers one such pair and is counted once by the middle vertex in $\sum_v\binom{d_N(v)}2$. Every pair in $N$ is covered because $G$ has diameter at most $2$.

For an adjacent pair $\{r,s\}\subseteq N$, its direct edge supplies the first cover, and every common neighbor supplies a further cover. The total number of such further covers over adjacent pairs is exactly $3T$: each triangle contributes its three choices of an edge and the opposite vertex, and every such configuration is a triangle. Consequently these $3T$ covers can all be removed without leaving any pair uncovered. Thus

$$\binom m2\le e_N+\sum_{v\in V(G)}\binom{d_N(v)}2-3T.\tag{7}$$

Equivalently, (7) follows from the exact identity

$$e_N+\sum_v\binom{d_N(v)}2
=\binom m2+\sum_{\{r,s\}\subseteq N}B_{rs},$$

where $B=A^2+A-7I-J$, because the defect sum over edges in $G[N]$ is $3T$, while its remaining terms are nonnegative. Every triangle is entirely contained in $N$ by definition.

**Step 4. Excluding the two smallest possible cores.** Substitution of (3), (4), and (6) into (7) gives

$$\binom m2\le (5m-59)+(36m-472)-m=40m-531.\tag{8}$$

At $m=15$, (8) asserts $105\le69$; at $m=16$, it asserts $120\le109$. Both are false. Step 1 gives $m\ge15$, so $m\ge17$. Finally $m\le3T$ implies $T\ge6$. $\square$

## Scope and open risks

No computation, matrix relaxation, triangle classification, short-cycle exclusion, or H5 qualification is used in the new counting argument. Its only N15-dependent input is the predecessor's lemma that each zero vertex has at least two nonzero neighbors. The result excludes all cases with at most five triangles under global zero-row N15. It does not establish N15 for arbitrary order-$59$ graphs, exclude six or more triangles, or close H5 or the degree-diameter problem. Paper proof review and any formalization remain separate work.
