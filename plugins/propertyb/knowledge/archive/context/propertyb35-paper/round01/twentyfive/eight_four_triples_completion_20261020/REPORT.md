# Independent finite verification for eight positives and four negative triples

## Result and scope

The two requested finite obligations for [EIGHT_POSITIVE_FOUR_TRIPLES_REPAIR](../../../../../proofs/propertyb35/EIGHT_POSITIVE_FOUR_TRIPLES_REPAIR.md) passed an independent standard-library implementation:

1. All86 old five-positive graph representatives satisfy the new **distinct target-pair** blocker bound strictly. The smallest margin is nine, at old orbit66.
2. The complete maximum-degree-four five-label domains with two-matching counts $M_2=7,8$ have respectively1020 and1395 labeled vectors, in11 and22 true $S_5$ orbits. Every one of the2415 labeled vectors has direct three-point transversal count equal to its independent32-term inclusion-exclusion count. Their minima are18 and21.

No original hypergraph was enumerated. The old86 completeness result is reused exactly as authorized; its graph domain was not regenerated or enlarged for the first obligation. The second obligation generates only the two specified matching-count levels. The old gate and its data remain untouched.

Exact source and complete rows: [REPLAY.py](REPLAY.py), [REPLAY.json](REPLAY.json). The full run returned `PASS` in0.135 seconds on this machine; timing is descriptive, not part of the proof.

## 1. Common representation and independent candidate reconstruction

Let $A_0,\ldots,A_4$ be five positive four-sets whose maximum positive occurrence is at most two. Their labels are graph vertices. Every actual point occurring in two sets is one edge, with parallel edges retaining different point identities. A point occurring in just one set is private to its label. With edge multiplicities $m_{ij}$ and graph degrees $d_i\le4$, reconstruction gives

* $m_{ij}$ distinct points carrying label mask $\{i,j\}$;
* $4-d_i$ distinct private points carrying label mask $\{i\}$.

The reconstruction uses multiplicities from the graph vector, not saved candidate lists. Each label appears on exactly four points. For $k=3,4$, the direct count enumerates $k$-point subsets and tests whether the union of their label masks is all five labels.

Independently, inclusion-exclusion counts the same family by

$$C_k=\sum_{S\subseteq[5]}(-1)^{|S|}
\binom{u(S)}k,\qquad
u(S)=|\{x:\operatorname{mask}(x)\cap S=\varnothing\}|.$$

Terms with $u(S)<k$ are zero. This32-term formula depends only on point masks, whereas direct counting checks actual point subsets.

## 2. Why the top-distinct-target bound is valid

Fix a three-point $x$ in the original eight-positive family. Let $\mathcal C$ be the four-point transversal family of the five positives avoiding $x$. Write $r,b$ for the numbers of negative triples and quadruples containing $x$. Their original indexed occurrence budget gives $r+b\le4$.

Each negative triple containing $x$ has a two-point target in the other coordinates. A target outside the reconstructed union has no event. Repeated targets do not enlarge the **union** of blocked candidates. If

$$h(F)=|\{C\in\mathcal C:F\subseteq C\}|\quad(|F|=2)$$

and the values for distinct pairs are sorted $h_1\ge h_2\ge\cdots$, the union blocked by these $r$ indexed triples has size at most

$$S_r=\sum_{i=1}^r h_i.$$

This remains valid with repeated negative indices: there are at most $r$ different effective targets, and all extension counts are nonnegative. It is essential here to sum counts of different pairs, rather than repeat the largest count $r$ times.

Let $g_3$ be the maximum extension count of a specified three-point subset. The other at-most $4-r$ negative triples and the $b$ negative quadruples containing $x$ each block at most $g_3$ candidates. Each negative quadruple avoiding $x$ blocks at most one. Thus the complete blocker bound is

$$S_r+(4-r)g_3+b g_3+(17-b),
\qquad0\le r\le4,\quad0\le b\le4-r.\tag{1}$$

The implementation reconstructs every $C\in\mathcal C$, increments all six actual point-pair counters and all four point-triple counters, sorts the distinct pair values, and evaluates all15 integer $(r,b)$ cases in(1). It checks the saved old $C_4$ both by direct subsets and by inclusion-exclusion. All86 comparisons are strict.

The two illustrative rows are:

| Old orbit | $C_4$ | Four largest distinct-pair extensions | $g_3$ | Largest(1) | Margin |
|---:|---:|---|---:|---:|---:|
|2|178|46,22,22,22|13|138|40|
|66|189|46,46,46,22|13|180|9|

At orbit2 the maximum is at $(r,b)=(1,3)$; at orbit66 it is at $(3,1)$. The minimum margin over the entire86 is nine. Complete per-row targets, worst cases and all15 budget comparisons are in the JSON.

The imported old domain is $\Delta\le4$, $4\le E\le8$, $1\le M_2\le6$, with5307 labeled inputs in86 orbits. Its original two complete generation methods and $S_5$ quotient proof remain the coverage source. This replay uses all86 representatives, not just the seven formerly nonstrict rows.

## 3. Complete new $M_2=7,8$ domain by whole vertex stars

The new domain consists of all loopless five-label multigraph vectors

$$m=(m_{01},m_{02},\ldots,m_{34})\in\mathbb Z_{\ge0}^{10},
\qquad d_i=\sum_{j\ne i}m_{ij}\le4,
\qquad M_2\in\{7,8\},$$

where

$$M_2=\sum_{\substack{\{i,j\},\{u,v\}\text{ disjoint}\\
\{i,j\}<\{u,v\}}}m_{ij}m_{uv}.$$

This implementation uses a different recursion from assigning consecutive graph edges: at vertex $i=0,1,2,3$, it assigns its entire forward star $(m_{i,i+1},\ldots,m_{i,4})$ at once. Its incoming degree is fixed by prior stars. The allowed tuples have sum at most its remaining capacity and give no later vertex total degree exceeding four. At each level, all such integer tuples are traversed. Partial $M_2$ is monotone under adding nonnegative multiplicities, so a branch whose current $M_2>8$ may safely be pruned. No lower-bound, edge-number or other structural filter is used.

Every legal vector chooses exactly one tuple at each successive vertex, so is generated once; conversely each output has nonnegative multiplicities, the degree caps and one of the two required matching counts. The zero-first-star and isolated-vertex possibilities are retained. This proves completeness independently of the root agent's edge-wise generator.

The output has exactly:

| $M_2$ | Labeled vectors | $S_5$ orbits | Minimum direct $C_3$ | Minimum IE $C_3$ |
|---:|---:|---:|---:|---:|
|7|1020|11|18|18|
|8|1395|22|21|21|

The code reconstructs and counts **all2415 labeled inputs** by both methods. It then independently forms each full orbit under all120 label permutations; every transported vector belongs to the generated domain, its candidate count is unchanged, and orbit sizes sum to2415. The complete labeled vectors and all33 representatives are saved.

These minima exceed the16-candidate blocker bound

$$4r+(4-r)+b\le16,$$

so every new input in these two matching levels has a valid four-point candidate after adjoining $x$. For $M_2\ge9$, the existing formula $C_3\ge2M_2\ge18$ gives the same strict conclusion without another finite domain.

The root agent then ran a separate [edge-wise domain implementation](EDGE_DOMAIN_CHECK.py), with [result](EDGE_DOMAIN_CHECK.json): its complete2415-vector set is exactly equal to this forward-star set. It also evaluates the weighted two-matching/missing-vertex-degree formula for $C_3$ on every label, obtaining the same counts as both direct subsets and32-term inclusion-exclusion. This supplies a different generation-order domain equality check and a third counting formula, with no additional object scope.

## 4. Transport back to actual signed constraints

Every actual remaining-five-positive family with maximum occurrence two has the stated multigraph representation. Permuting its five labels, permuting actual parallel-edge points, or permuting private points is a bijection on the reconstructed point set and all transversal subsets. It preserves $C_3,C_4$, the full multiset of distinct-pair extension counts, and $g_3$. Thus(1) and the new matching-level counts transport to the original points, without assumptions on negative-target positions. Points outside the five-set union are never selected; targets using them are automatically avoided.

The old86 domain plus the new $M_2=7,8$ levels are used only in the precise graph branches stated. The remaining branches (a second three-point, zero-matching star/triangle, and larger matching count) are handled analytically in the root's new canonical proof, not folded into this computation.

## 5. Targeted check of the root's two new analytic supplements

The new canonical proof's double-three-point and zero-matching-triangle supplements were read independently after the finite run.

For the double-three-point step, the joint $x,y$ occurrence budget

$$b\le a-s-\max(u,v)$$

correctly counts quadruples that can obstruct the four-point candidates, since they must contain both fixed points. When $s<a$ and $a\ge2$, its resulting bound is strict. In the $a=1$ branches, changing the common point of all forced triples to blue leaves at most one quadruple through the retained red point; that is exactly one new negative triple. The five-small-positive/one-triple theorem therefore has the stated hypotheses. The alternative where the unique quadruple blocks the candidate saturates both fixed points and also leaves at most one negative triple. No claim that every three-point candidate is automatically safe is used.

For the triangle with80 candidates, a nonmaximal pair target leaves at most $3\cdot16+12+17=77$ blocked. Four distinct maximal targets miss the16 candidates from the fifth actual triangle pair. All these remaining candidates share a point $p$ with positive occurrence at least two. The original three-point $x$ is saturated by four negative triples, so no negative quadruple contains $x$. Every obstructing quadruple of a remaining five-point candidate must therefore be its four non-$x$ points and contain $p$. At most five indexed negative quadruples can contain $p$, fewer than16. This gives the claimed strict repair. Duplicate targets only decrease their union and do not evade this argument.

No substantive issue was found in these two supplements within the stated scope. This is same-family mathematical verification plus deterministic local arithmetic, not a new cross-family review or a proof of the full $m(5)\ge36$ goal.
