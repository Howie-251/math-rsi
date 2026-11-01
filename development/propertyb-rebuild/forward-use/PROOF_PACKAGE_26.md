# Proof Package: excluding 26 vertices

## Claim
Let $H=(V,E)$ be a finite simple $5$-uniform hypergraph. Assume every pair of distinct vertices belongs to some edge and $|E|\le33$. Then $|V|\ne26$. In fact $|V|\le25$.

## Status
PROVABLE AS STATED.

## Assumptions
The only special assumption is pair coverage. This is a conditional structural lemma; it does not by itself prove Property B for all hypergraphs with at most $33$ edges. For the standard minimum-vertex non-Property-B reduction, pair coverage follows by merging an uncovered pair and pulling back a coloring.

## Notation
Write $v=|V|$, $m=|E|$, $d(x)=|\{e\in E:x\in e\}|$, and $\lambda(x,y)=|\{e\in E:x,y\in e\}|$ for distinct vertices.

## Proof Strategy
Count incidences with a fixed vertex first, retaining integer degrees, then count all vertex-edge incidences.

## Dependency Map
1. Pair coverage gives $\lambda(x,y)\ge1$.
2. $5$-uniformity gives $\sum_{y\ne x}\lambda(x,y)=4d(x)$ and $\sum_xd(x)=5m$.
3. Integer rounding conflicts with the edge budget at $v\ge26$.

## Proof
**Step 1.** Fix $x\in V$. Count pairs $(e,y)$ with $x,y\in e$ and $y\ne x$. Every incident edge contributes exactly four such pairs, while every $y\ne x$ occurs in at least one by pair coverage. Hence
$$4d(x)=\sum_{y\ne x}\lambda(x,y)\ge v-1.$$

**Step 2.** If $v\ge26$, then $d(x)\ge\lceil25/4\rceil=7$ for every $x$. Consequently
$$\sum_{x\in V}d(x)\ge7v\ge182.$$

**Step 3.** Counting vertex-edge incidences in the other order gives
$$\sum_{x\in V}d(x)=\sum_{e\in E}|e|=5m\le165,$$
contradicting Step 2. Therefore $v\le25$, which excludes $26$. $\square$

## Why the coarse bound does not suffice
Summing the unrounded inequality $4d(x)\ge v-1$ gives $v(v-1)\le20m\le660$. At $v=26$ its left side is $650$, so it permits $26$. Retaining the integer rounding at each vertex gives the stronger necessary condition $v\lceil(v-1)/4\rceil\le5m$, which excludes it.

## Corrections or Missing Assumptions
None for the conditional claim above. Pair coverage is not a premise that can be silently added to an arbitrary original hypergraph.

## Open Risks
No missing mathematical connection in this short incidence proof. The arithmetic $26\cdot7=182>165=5\cdot33$ is also executed in `diagnose_scope.py` and retained in `SCOPE_RESULTS.json`. No Lean construction or external review was performed.
