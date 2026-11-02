# Nine-deletion extensions: the eight-III-plus-EE branch is impossible

## Claim and status

Status: **complete candidate paper argument, using 84 small family checks; independent review pending**.

Let an order-58 graph of maximum degree 8 and diameter at most 2 use the 57 labeled Brown vertices and one additional vertex. It cannot delete exactly nine Brown edges consisting of one edge from each of eight distinct all-internal triangles and one external–external edge.

This closes the previously unresolved extra-EE subcase with eight destroyed III triangles. It does not exclude all nine-deletion extensions: the six-III and seven-III branches remain open here. It proves no upper bound for arbitrary order-58 graphs.

## Setup and degree-resource lemma

Use the notation and exact Brown graph facts of `BROWN_EIGHT_DELETE_OBSTRUCTION.md`: $C$ has 8 degree-7 vertices, $I$ has 21 degree-8 vertices with no $C$ neighbor, and $E$ has 28 degree-8 vertices. Each $I$ vertex has four $I$ neighbors and belongs to exactly two III triangles. Each $E$ vertex has two $C$ neighbors and three $I$ neighbors. Each old edge lies in at most one triangle.

The proposed extension is 8-regular. If $d_v$ counts old deletions at $v$, its deficit is $d_v+[v\in C]$. Let $S$ be the new vertex's eight old neighbors. Write $j=|S\cap I|$, $e=|S\cap E|$, and let $\sigma$ count remaining new old–old incidences available at $S$ after connecting its vertices to the new vertex.

In the present branch, the only deficient $E$ vertices are the two endpoints of the deleted EE edge, each with deficit 1; every $C$ vertex has deficit 1. Thus their inclusion in $S$ provides no spare incidence. Every deficient $I$ vertex has deficit 1 or 2, and

$$\sigma=|\{i\in S\cap I:d_i=2\}|.$$

There are $j+e$ vertices of $C$ outside $S$. At most $2e$ are reached using retained old edges from $S\cap E$. Hence at least $\max(0,j-e)$ of the $\sigma$ new incidences at $S$ are required to reach $C$. In particular

$$j\le e+\sigma.$$

After meeting that necessary $C$ demand, at most $\sigma-\max(0,j-e)$ new incidences can reach previously unreached $I$ vertices. Each such incidence covers at most one new $I$ vertex. This permits arbitrary added edges; no matching assumption about those new edges is made.

## The selected III triangles cover either 20 or 21 points

Each internal vertex initially lies in four triangles and must lose at least one old triangle, since an order-58 candidate has at most three triangles per vertex. Eight III deletions plus one EE deletion can cover at most one further internal vertex outside the III union. Thus the eight selected III triangles cover at least 20 of the 21 points of $I$.

The exact small checker `computations/dd82/construction/brown_r9_eight_iii_facts.py` enumerates the $\binom{14}{8}$ triangle subsets. It finds 14 covering all 21 points and 42 covering exactly 20. Its additional family facts used below are checked directly against the complete Brown edge list, without enumerating edge choices or graphs.

## Case 1: all 21 internal points are covered

For every one of these 14 families, the three points belonging to two selected III triangles form one of the selected III triangles themselves. A point can have deletion degree 2 only if both of its selected incident triangles delete an edge containing it. The single deleted edge in this central triangle contains only two points. Therefore at most two internal points can have deletion degree 2, and $\sigma\le2$.

Since $e\le2$, the $C$ demand gives $j\le e+2\le4$. The retained old closed $I$-neighborhood of an internal point in $S$ has size $5-d_i$. Each external point covers at most three $I$ points. Including any remaining new incidences, the total reachable $I$ count is at most

$$5j-\sum_{i\in S\cap I}d_i+3e+\sigma-\max(0,j-e)
=4j+3e-\max(0,j-e).$$

For $j\ge e$ this is $3j+4e\le20$; for $j<e$ it is at most $4+6=10$. It cannot cover all 21 internal points.

## Case 2: exactly 20 internal points are covered

Let $m$ be the one uncovered internal point. The extra EE edge must destroy an IEE triangle at $m$. There are exactly two possible EE edges for that point.

The 42 triangle families and their two EE alternatives have the following exact properties, recorded explicitly in the checker's JSON output:

1. Exactly four internal points $R$ belong to two selected III triangles.
2. Exactly two selected III triangles contain no point of $R$. They are disjoint; write their six-point union as $Z$.
3. The original graph induced on $Z$ consists of those two triangles and one edge between them. Denote that cross-edge's endpoints by $a,b$.
4. No point of $R$ has an old neighbor in $Z$.
5. Neither endpoint of either allowed extra EE edge has an old neighbor in $Z$.
6. Every internal point outside $Z\cup\{m\}$ has at most one old neighbor in $Z$.

The internal point $m$ has deletion degree zero: it lies in no selected III triangle, and the extra deletion is EE. Therefore $m\notin S$.

If $e\le1$, then $\sigma\le4$ and $j\le e+4\le5$. The same general internal-coverage expression from Case 1 is at most $3j+4e\le19$ when $j\ge e$, and is smaller otherwise. Thus only $e=2$ needs consideration.

Put

$$k=|\{i\in S\cap I:d_i=1\}|=j-\sigma.$$

The $C$ budget gives $k\le2$. The number of unused added incidences that can help reach $Z$ is at most $2-k$: when $j\ge2$ this equals $\sigma-(j-2)$; when $j<2$ the available $\sigma=j-k$ is no larger than $2-k$.

Only these $k$ internal points of deletion degree 1 can reach $Z$ through retained old edges or by belonging to $Z$ themselves. Indeed the internal points of deletion degree 2 lie in $R$, the two external points cannot reach $Z$, and $C$ has no old internal neighbors.

An eligible point outside $Z$ has at most one retained old neighbor in $Z$. A point inside $Z$ belongs to exactly one selected III triangle, namely its own isolated triangle. If it has deletion degree 1, that deletion removes one incident edge within that triangle. Its retained closed neighborhood in $Z$ therefore has size 2, except possibly at $a,b$, where it has size 3 because of the cross edge.

For two such internal points, the union of their retained closed neighborhoods in $Z$ has size at most 5. If at least one is not $a$ or $b$, the bound is at most $3+2$. If the two points are $a,b$, their neighborhoods both contain $a,b$, so the union has size at most $3+3-2=4$.

Consequently, for $k=0,1,2$, the old coverage of $Z$ is at most $0,3,5$ respectively. Adding the at most $2-k$ new incidences gives upper bounds

$$2,\quad4,\quad5,$$

all below $|Z|=6$. This contradicts distance at most 2 from the new vertex to every point of $Z$.

Both possible III union sizes are impossible, proving the stated branch exclusion.

## Computation scope and retained exploratory profile

The proof uses only the family checker: 14 full-cover families and 42 twenty-cover families with two EE alternatives each. The graph predicates behind the six assertions are literal adjacency/set tests against `brown57.edges`; the complete records are in `brown_r9_eight_iii_facts.json`.

Before finding the six-point argument, a separate necessary-coverage profile enumerated all $42\cdot3^8=275562$ base II deletion patterns and their two allowed EE alternatives. It then checked 6,144,768 critical $S\cap I$ choices; their maximum upper bound on reachable internal points was 20, with no survivors. Source and results are preserved as `brown_r9_ee_profile.cpp` and `.json`. The process was bounded by 30 seconds on one CPU and exited successfully. It performed no SAT calls and no search over added-edge completions.

That larger profile is now unnecessary for the proof: the 84 family checks and the six-point argument replace it. Its result is not a complete exclusion of all nine-deletion patterns.

## Remaining nine-deletion branches

If $a$ and $b$ count distinct destroyed III and IEE triangles, then $a+b\le9$ and $3a+b\ge21$, so $a\ge6$. The present document addresses the difficult EE subcase when $a=8$ only. The $a=6$ and $a=7$ possibilities still need their own degree-resource or structural argument. In particular no statement that every Brown57 extension requires ten deletions is made here.
