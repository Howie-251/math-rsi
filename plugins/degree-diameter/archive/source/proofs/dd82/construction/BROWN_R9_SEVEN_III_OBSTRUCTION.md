# Nine-deletion Brown extensions: both seven-III branches

## Claim and status

Status: **complete candidate mathematical reduction plus two exact finite necessary-condition checks; independent review pending**.

Suppose an order-58 graph of maximum degree at most 8 and diameter at most 2 uses the 57 labeled Brown vertices and one new vertex. It cannot delete exactly nine Brown edges and destroy exactly seven distinct III triangles.

Both possible internal union sizes, 19 and 21, are covered below. The checks search only the new vertex's eight-neighbor set, with a small amount of deletion data and optimistic repair budgets. They do not run SAT or enumerate the added-edge graph. This document alone does not establish a ten-deletion lower bound; that requires combining every other nine-deletion branch and obtaining independent review.

## 1. Common graph facts and coverage budget

Use the complete Brown graph and the classes $C,I,E$ from `BROWN_EIGHT_DELETE_OBSTRUCTION.md`. Each internal vertex lies in four old triangles and must lose at least one, because an order-58 candidate has at most three triangles at a vertex. With exactly seven distinct III triangles destroyed, at most two IEE triangles can be destroyed by the remaining deletions. Consequently the seven selected III triangles cover at least 19 of the 21 internal points.

The exact triangle-family enumeration in `brown_r9_eight_iii_facts.json` gives:

* 42 seven-III families cover 19 points;
* no such family covers exactly 20 points;
* two families cover 21 points, and are partitions of $I$.

These are all possible seven-III branches.

Let $d_v$ be the old deletion degree. The extension is 8-regular, so the positive deficit at an old vertex is

$$k_v=d_v+[v\in C].$$

Let $S$ be the new vertex's eight old neighbors. Then $S\subseteq\{v:k_v>0\}$, and after adding the new-vertex edges the number of new old–old edge incidences available at $S$ is exactly

$$\sigma(S)=\sum_{s\in S}(k_s-1).$$

For the actual retained old graph, every point outside its closed neighborhood of $S$ requires a new old–old edge from $S$. Each such added incidence can reach at most one new point at distance two from the new vertex. Therefore

$$57-\left|S\cup N_{\mathrm{retained}}(S)\right|\le\sigma(S)$$

is a necessary condition. It need not be sufficient: targets may have insufficient degree, edges must be new, and other vertex-pair distances remain to be checked. Those omissions only relax the condition used for exclusion.

## 2. Union size 19: isolate the only possible repeated endpoints

For each of the 42 families, exactly two internal points $R=\{r_1,r_2\}$ lie in two selected III triangles. Those two points lie in a unique selected central triangle $T_0$. Removing $T_0$ from the selected family leaves six disjoint III triangles covering 18 internal points. These properties follow by the small incidence checks used in the source; they are also the $P_3$ plus four isolated vertices form of the selected-triangle intersection graph.

By the six-III family fact proved and checked in `BROWN_R9_SIX_III_OBSTRUCTION.md`, the three points outside those six triangles form another III triangle. Exactly one of these three is the third point of $T_0$; the other two, say $m_1,m_2$, are the points not covered by the seven selected triangles. In particular $m_1,m_2$ are adjacent.

There must be exactly one further deleted IEE edge at each $m_i$. The two external-neighbor sets $N(m_i)\cap E$ are disjoint: a shared external neighbor would create a second triangle on $m_1m_2$. Hence the extra deletions have endpoints in the two disjoint five-point sets

$$H_i=\{m_i\}\cup(N(m_i)\cap E),$$

and each is one of the six edges in that pair of IEE triangles.

The six noncentral III deletions form a matching. Their endpoints are disjoint from the two $H_i$. The central deletion is the only source of repeated endpoints. Thus the only vertices that can have $d_v=2$ are $r_1,r_2$, and every other positive deficit is 1. In particular the total spare incidence count is at most 2.

### Known-deletion cases

First choose the deleted edge of $T_0$. If it is $r_1r_2$, it meets two of the six noncentral III triangles. Fix the deleted edge in both, giving $3^2=9$ cases. If it joins one $r_i$ to the third central point, it meets just one noncentral triangle; fixing that triangle's deleted edge gives 3 cases for each of the two choices. Thus each family has exactly

$$9+3+3=15$$

known-deletion cases, for 630 cases total.

All deletion degrees greater than 1 are now fixed. The remaining noncentral III triangles and the two sets $H_i$ are mutually disjoint blocks. Inside each block exactly one edge will be deleted. Therefore at most two points of that block can lie in $S$; if two are selected, they must be adjacent. Vertices outside $C$, the known deletion endpoints, and these blocks have no deficit and cannot lie in $S$.

For this branch the checker removes only the known edges when computing closed neighborhoods. It ignores all still-unfixed deletions. This can only increase the coverage of $S$, while its spare count is already exact: an unfixed block can create only degree-1 deficits and no spare incidences. If even this relaxed coverage cannot satisfy the inequality in Section 1, no complete deletion pattern can do so.

The complete result is:

| Families | Known-deletion cases | Search states | Surviving eight-neighbor sets |
|---:|---:|---:|---:|
| 42 | 630 | 107,074 | 0 |

Source: `computations/dd82/construction/brown_r9_a7_cover19.cpp`.

Results, including per-family counts: `computations/dd82/construction/brown_r9_a7_cover19.json`.

## 3. Union size 21: fix the two extras before the base matching

In each of the two parallel classes, choose one deleted edge in each selected III triangle as the seven base edges. The actual nine-edge deletion set has two further distinct edges, called extras. An extra II edge must belong to one of the seven selected triangles; an II edge in any other triangle would destroy an eighth distinct III triangle.

The possible extra-edge pool therefore contains:

$$21\text{ II edges}+56\text{ CE edges}+84\text{ IE edges}+42\text{ EE edges}=203\text{ edges}.$$

Choose the unordered pair of distinct extras first. A selected III triangle is affected if it contains an internal endpoint of an extra edge. At most two base triangles are affected: an II extra has both endpoints in one base triangle; an IE extra has one internal endpoint; CE and EE extras have none.

Fix the base deletion in each affected triangle, excluding any edge already chosen as an extra. This preserves every actual deletion set: choosing one base edge from each actual selected triangle leaves two extras in the displayed pool, and its affected base choices appear in this enumeration. Some actual deletion sets may appear more than once, which is harmless for an exclusion.

The two extras and the affected base edges form the known deletion set $K$. The unaffected base triangles remain disjoint three-point blocks with one unknown deleted edge each. They have no vertex incident to a known deletion. All deficit values at known vertices are exact; the only possible unknown deficits are 0 or 1 inside those disjoint triangles.

Starting with the seven-edge base matching, every initial positive deficit is 1. The first extra can create at most one spare incidence: an allowed II edge distinct from its base edge shares exactly one endpoint with that base edge; a CE edge has only its $C$ endpoint initially deficient; an IE edge has at most its internal endpoint initially deficient; an EE edge has neither endpoint initially deficient. The second extra can add at most two more spare incidences. Thus the total spare count is at most 3.

### Eliminating the remaining base-edge choices after selecting S

Let

$$u_K(S)=57-|S\cup N_{G-K}(S)|$$

be the number of uncovered vertices after only the known deletions. Consider an unaffected base triangle $T$.

* If $S\cap T$ is empty, deleting an edge of $T$ does not change coverage from $S$.
* If $|S\cap T|=2$, the deleted edge must join those two selected points. Both remain covered by membership in $S$, and no other point loses an $S$ neighbor.
* If $S\cap T=\{v\}$, the deleted edge must join $v$ to one of the other two triangle points. Choosing partner $w$ causes an additional uncovered point exactly when $w$ has no other neighbor in $S$.

For that last test the original Brown adjacency can be used: no known deleted edge is incident to $w$, by the definition of an unaffected triangle. Thus its number of neighbors in $S$ before the unknown deletion is exactly $|N_G(w)\cap S|$.

Define $h(S)$ to count the unaffected triangles with $S\cap T=\{v\}$ for which **both** possible partners have exactly one neighbor in $S$. Each such triangle necessarily creates one new uncovered point; otherwise a safe partner can be chosen. The targets lie in distinct unaffected triangles, and unknown deletions from another block cannot change their neighbor count. They were initially covered by $v$, so they are not among the vertices counted by $u_K(S)$.

Consequently the minimum number of uncovered vertices over all remaining base deletion choices is exactly

$$u_K(S)+h(S).$$

The necessary condition checked at a leaf is therefore

$$u_K(S)+h(S)\le\sigma(S).$$

No enumeration of all $3^7$ base-edge choices is needed.

The complete result is:

| Parallel classes | Known-deletion cases | Search states | Surviving eight-neighbor sets |
|---:|---:|---:|---:|
| 2 | 145,040 | 5,805,357 | 0 |

The known-deletion cases, grouped by the unordered extra-edge types, are:

| Extras | Cases |
|---|---:|
| II + II | 1,554 |
| II + CE | 4,704 |
| II + IE | 19,152 |
| II + EE | 3,528 |
| CE + CE | 3,080 |
| CE + IE | 28,224 |
| CE + EE | 4,704 |
| IE + IE | 57,204 |
| IE + EE | 21,168 |
| EE + EE | 1,722 |

Source: `computations/dd82/construction/brown_r9_a7_cover21.cpp`.

Results: `computations/dd82/construction/brown_r9_a7_cover21.json`.

The run reached its final line with `families=2`, `cases=145040`, `passes=0`, and `complete=1`. A diagnostic stop after ten survivors is present in the source but was never triggered.

## 4. Completeness of the neighbor-set search

Both programs use the same elementary finite search idea. The state records the selected set $S$, available candidates, currently covered vertices, a set of temporarily ignored targets, and the number of selected points. They use integer counts and 64-bit sets, with no approximate computation.

The candidate set contains every vertex with possible positive deficit. At known vertices the spare weight $k_v-1$ is exact; at still-unfixed blocks it is zero. The sum of all available known spare weights gives an upper bound $M$ on the eventual $\sigma(S)$: at most 2 in union-size-19 cases and at most 3 in union-size-21 cases.

The search selects exactly eight points and enforces the local block restrictions. In the size-19 code, the first selection in a five-point block removes nonadjacent alternatives, and the second removes all remaining block members. In the size-21 code, every unaffected block is a triangle, so only the two-point capacity is needed.

For an uncovered, unignored target $z$, the branches either select a currently available point whose retained closed neighborhood contains $z$, or mark $z$ ignored if fewer than $M$ targets have been ignored. The selecting branches exclude only the earlier choices from subsequent branches, so every possible completing set appears in a branch determined by its first selected dominator of $z$.

To verify that the ignore branch preserves coverage, fix any putative successful set. Follow selecting branches for targets covered by that set and ignore only targets it truly leaves uncovered in the known-deletion graph. Their number is at most $\sigma(S)\le M$. Thus a successful set has a complete search path. A target ignored in some other branch may later become covered; this can cause redundant exploration but does not remove the path just described.

Two safe bounds prune a state:

1. there must be enough available points to reach eight selections;
2. the sum of the largest remaining individual coverage gains, plus the still-unused ignore budget, must reach the number of currently unignored uncovered targets.

The second bound overcounts overlap between neighborhoods, so it is an upper bound on possible coverage and cannot eliminate a successful set. The terminal predicate uses the actual uncovered count and actual spare count of the chosen set, with the additional exact $h(S)$ test in the size-21 branch. Every one of the two runs finished without a surviving terminal set.

These are necessary-condition exclusions. A successful terminal set would only be a candidate for further analysis, not an order-58 graph. Finding no such set is enough for the branch contradiction because every genuine extension would produce one.

## 5. Execution and mathematical boundary

Each program was compiled as C++17 and run as a single process under a 30-second timeout, and each exited successfully. Neither invokes a SAT solver, linear solver, stochastic search, or new-edge completion procedure. The complete source and exact counts are retained; no hash or checksum was generated.

The triangle-family coverage and the search recurrence are explicit finite obligations suitable for independent review or later formalization. No Lean proof is claimed. The six-III branch is treated separately in `BROWN_R9_SIX_III_OBSTRUCTION.md`, and the eight-III-plus-EE branch separately in `BROWN_R9_EIGHT_III_OBSTRUCTION.md`. The remaining assembly of the complete nine-deletion case split belongs in a separate reviewed theorem, rather than being silently inferred from this seven-III result.
