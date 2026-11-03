# Nine-deletion Brown extensions: the six-III branch

## Claim and status

Status: **complete candidate reduction plus a small exact finite domination check; independent review pending**.

Suppose an order-58 graph of maximum degree at most 8 and diameter at most 2 uses the 57 labeled Brown vertices and a new vertex. If it deletes exactly nine Brown edges, those deletions cannot destroy exactly six distinct all-internal III triangles.

This is one edit-distance branch exclusion. The seven-III branches remain open in this document. It does not prove that every extension needs ten deletions, or that arbitrary order-58 graphs are impossible.

## 1. Six III triangles force nine disjoint deletion blocks

Use the vertex classes $C,I,E$ and the finite Brown graph facts from `BROWN_EIGHT_DELETE_OBSTRUCTION.md`. In particular $|C|=8$, $|I|=21$, $|E|=28$; each internal vertex belongs to two III triangles and two IEE triangles, while every old edge lies in at most one triangle.

Every internal point must lose at least one old triangle: it starts with four, whereas an order-58 candidate permits at most three. Let $a,b$ count distinct destroyed III and IEE triangles. With nine deletions,

$$a+b\le9,\qquad3a+b\ge21.$$

If $a=6$, both inequalities force $b=3$ and equality in the internal coverage count. Thus:

* the six selected III triangles are disjoint and cover 18 internal points;
* the other three internal points $M$ each belong to one of the three additionally destroyed IEE triangles;
* all nine deletions lie in those nine distinct triangles, exactly one edge per triangle. There are no CE deletions or additional deletions in an already destroyed triangle.

The already recorded triangle-coverage histogram gives exactly 14 such six-III families. Direct enumeration of the 14 III triangles further verifies that $M$ itself is always another III triangle. This assertion is checked by the finite program used below, rather than assumed from the count alone.

For distinct $m,m'\in M$, their external-neighbor sets are disjoint. If an external point were adjacent to both, it would create a second triangle on the old edge $mm'$, whereas every Brown edge belongs to at most one triangle. Each $m$ has four external neighbors, so the three sets have total size 12.

For each $m$, the graph on $H_m=\{m\}\cup(N(m)\cap E)$ consists of its two IEE triangles sharing $m$. Its six edges are exactly the choices for the single extra deletion which destroys a triangle at $m$.

The six selected III vertex sets and the three sets $H_m$ are pairwise disjoint. Each of the nine old deletions lies entirely inside its own block. Therefore the nine deleted edges form a matching. In particular every deleted-edge endpoint has deletion degree 1, and no vertex of $C$ is incident to a deletion.

## 2. The new vertex's neighbors must dominate the old graph

The proposed order-58 graph is 8-regular by the original root bound. Let $S$ be the eight old neighbors of its new vertex $x$. After the nine matching deletions, every positive old degree deficit is exactly 1: this holds both for the old degree-7 points of $C$ and for the degree-8 endpoints of deleted edges.

Connecting any $s\in S$ to $x$ uses its sole deficit. Consequently no added old–old edge is incident to any point of $S$. Any old point outside $S$ must therefore be adjacent to a point of $S$ through a retained original Brown edge, in order to lie at distance 2 from $x$.

Thus $S$ dominates the Brown graph after deletion, and in particular dominates the original Brown graph before deletion. Testing domination before deletion is a relaxation and is enough for an obstruction if it already has no solution.

All possible members of $S$ lie in the set

$$W=C\cup I\cup\bigcup_{m\in M}(N(m)\cap E),\qquad |W|=8+21+12=41.$$

In each of the nine blocks, at most two points can belong to $S$, since only the two endpoints of that block's deleted edge have a deficit. If two are selected, they must be adjacent in the original graph, and they are precisely that edge's endpoints. These block restrictions are necessary, independent of which old edges are ultimately added.

We have reduced the branch to the following finite statement, with no added-edge variables:

> For each of the 14 six-III families, there is no set $S\subseteq W$ of size 8 which dominates the original Brown graph, selects at most two points from every deletion block, and selects an adjacent pair whenever it selects two points from a block.

## 3. Exact finite domination check

Source: `computations/dd82/construction/brown_r9_a6_domination.cpp`.

Results: `computations/dd82/construction/brown_r9_a6_domination.json`.

The program reads the complete edge list `brown57.edges`, reconstructs $C,I,E$, lists the 14 III triangles, and enumerates all six-triangle subsets whose union has size 18. It checks that the three omitted internal points form an III triangle, that the nine blocks are disjoint, and that the candidate set has size 41.

For each family it searches for $S$ using only unsigned 64-bit set operations and integer counts. A state consists of the chosen set, the available candidates, the already dominated vertices, and the number of selected points. The search is exhaustive for the following reasons:

1. A chosen vertex contributes its closed original neighborhood to the dominated set.
2. After the first choice in a block, other points in that block which are not its neighbors are removed. After the second choice, all remaining points in that block are removed. These are exactly the necessary block restrictions.
3. If some vertex remains undominated, choose one having the fewest available dominators. Every completing dominating set must choose at least one such candidate. Branches choose the first selected candidate in increasing label order, excluding only the previously tried candidates in subsequent branches. Thus no possible selected subset is lost or counted through a different ordering.
4. If all vertices are dominated before eight choices, the program continues by considering the remaining available candidates in increasing order until it has chosen exactly eight. It does not discard a smaller dominating set whose allowed extension could satisfy the size requirement.
5. Two upper-bound tests prune a branch: fewer than the required number of candidates remain, or the sum of the largest remaining individual coverage gains is less than the number of uncovered vertices. The latter sum overcounts overlaps, so it is an optimistic bound and cannot discard a feasible covering set.
6. At depth eight, the program checks the complete dominated bit mask. No numerical approximations or solver status are involved.

The program includes a later test for choosing deletion partners without destroying domination, but **no dominating eight-set reaches that test**. The result therefore proves the stronger relaxed finite statement above; no correctness assumption about that later filter is needed for the obstruction.

The numbers of visited search states in the 14 families were

$$83,85,83,84,93,83,81,87,91,83,84,83,84,85,$$

for a total of **1,189 nodes**. Every family had zero dominating eight-sets. The single-process run was bounded by 30 seconds and exited successfully. It called no SAT solver and enumerated no added-edge completions or candidate order-58 graphs.

For reproducibility, a future check can compile and invoke the source with the edge-list path:

```text
g++ -O3 -std=c++17 brown_r9_a6_domination.cpp -o brown_r9_a6_domination
timeout 30s ./brown_r9_a6_domination brown57.edges
```

Combining this exact finite fact with Sections 1 and 2 excludes the six-III branch.

## 4. Limits and the next missing branch

This result replaces the apparent $14\cdot3^6\cdot6^3$ deletion-pattern enumeration with fourteen constrained domination problems, each requiring fewer than one hundred search states. The triangle data and block constraints preserve every original graph in this branch.

The seven-III possibilities are different: their selected triangles can cover 19 or 21 internal points, and repeated deletion endpoints can provide spare incidences at $S$. The matching/no-new-edge-at-$S$ argument above must not be reused there without establishing its hypotheses for a particular subcase.

No Lean implementation is supplied. An independent checker should review the reduction to the nine disjoint blocks, the dominance relaxation, and the search-cover argument before promoting this candidate branch result.
