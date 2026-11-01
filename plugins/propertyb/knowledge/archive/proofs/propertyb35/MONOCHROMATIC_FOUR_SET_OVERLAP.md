# Monochromatic four-set overlap on nineteen points

Let $S$ be a set of nineteen points, colored uniformly with ten red and nine blue points. Let $A_1,\ldots,A_m$ be distinct four-element subsets of $S$. For a fixed color let $E_i$ be the event that $A_i$ is monochromatic in that color, and put
$$
D_m=\sum_{i=1}^m |E_i|-\left|\bigcup_{i=1}^m E_i\right|,
$$
where event sizes count the $\binom{19}{9}=92378$ equally likely colorings.

Then:

- For six red four-set events, $D_6\ge1595$.
- For seven red four-set events, $D_7\ge2035$.
- For seven blue four-set events, $D_7\ge616$.

These bounds require only that the four-sets are distinct. They require neither a partition nor independence. For either color, adding events cannot decrease $D_m$, so the respective bounds also apply when more sets are present.

## Two event inequalities and the intersection budget

For any spanning tree $T$ on the event indices,
$$
D_m\ge\sum_{ij\in T}|E_i\cap E_j|. \tag{1}
$$
Indeed, in a coloring where exactly $k$ events occur, the tree induced on their indices has at most $k-1$ edges if $k>0$ and zero if $k=0$. Summing this pointwise inequality proves (1). Any prescribed forest can be extended to a spanning tree.

Write
$$
S_2=\sum_{i<j}|E_i\cap E_j|,\qquad
S_3=\sum_{i<j<k}|E_i\cap E_j\cap E_k|.
$$
The third-order Bonferroni inequality gives
$$
D_m\ge S_2-S_3. \tag{2}
$$
If a point $v$ occurs in $r_v$ of the four-sets, then
$$
\sum_{i<j}|A_i\cap A_j|
=\sum_v\binom{r_v}{2}
\ge\sum_{v:r_v>0}(r_v-1)
=4m-\left|\bigcup_i A_i\right|\ge4m-19. \tag{3}
$$
Call an index pair **heavy** when its four-sets intersect in at least two points. Distinctness bounds all pair intersections by three.

## Red events

Each red event has size $\binom{15}{9}=5005$. If $|A_i\cap A_j|=j$, then
$$
|E_i\cap E_j|=\binom{11+j}{9},
$$
which for $j=0,1,2,3$ gives respectively $55,220,715,2002$.

If some pair intersects in three points, putting that pair into a spanning tree gives
$$
D_6\ge2002+4\cdot55=2222,\qquad
D_7\ge2002+5\cdot55=2277. \tag{4}
$$
Assume henceforth that all pair intersections have size at most two. Let $h$ count heavy pairs and $u$ count pairs intersecting in exactly one point. Then
$$
u+2h\ge4m-19,\qquad
S_2=55\binom m2+165u+660h. \tag{5}
$$
For any three four-sets, inclusion-exclusion gives
$$
|A_i\cup A_j\cup A_k|
=12-|A_i\cap A_j|-|A_i\cap A_k|-|A_j\cap A_k|
 +|A_i\cap A_j\cap A_k|.
$$
If the three indices contain $k$ heavy pairs, their union has at least $9-k$ points. Their joint red-event size is consequently at most $10,55,220,715$ for $k=0,1,2,3$, respectively. In particular, for $h=0$ or $h=1$,
$$
S_3\le10\binom m3+45h(m-2). \tag{6}
$$
Combining (2), (5), and (6) gives

| $m$ | $h$ | lower bound on $u$ | lower bound on $S_2$ | upper bound on $S_3$ | lower bound on $D_m$ |
|---:|---:|---:|---:|---:|---:|
| 6 | 0 | 5 | 1650 | 200 | 1450 |
| 6 | 1 | 3 | 1980 | 380 | 1600 |
| 7 | 0 | 9 | 2640 | 350 | 2290 |
| 7 | 1 | 7 | 2970 | 575 | 2395 |

### Six red events

If there are at least two heavy pairs, any two distinct heavy graph edges form a forest. Taking them in (1), then completing with three edges, gives
$$
D_6\ge2\cdot715+3\cdot55=1595. \tag{7}
$$
The case of exactly one heavy pair already gives $1600$. It remains to improve the no-heavy row of the table. If $u\ge6$, (2) gives
$$
D_6\ge825+165\cdot6-200=1615.
$$
If $u=5$, form the simple graph of the five index pairs whose four-sets intersect. A triple of indices with zero or one graph edge has union of size at least eleven and cannot all be red. A triple with two graph edges has union of size at least ten, so its joint red-event size is at most one. A graph triangle has joint event size at most ten.

Let $w$ be the number of adjacent pairs of graph edges and $t$ the number of triangles. A two-edge index triple contributes one to $w$, and a triangle contributes three, so
$$
S_3\le w+7t\le\binom52+7\cdot2=24.
$$
Here a five-edge simple graph has at most two triangles: two triangles not sharing an edge already use six edges; two sharing an edge use a five-edge diamond, which contains precisely those two triangles, so any third requires another edge. Thus
$$
D_6\ge1650-24=1626.
$$
Together with (4) and (7), this proves $D_6\ge1595$.

### Seven red events

If the heavy graph contains a three-edge forest, (1) gives
$$
D_7\ge3\cdot715+3\cdot55=2310.
$$
Otherwise its forest rank is at most two. The cases $h=0,1$ were handled above. When $h\ge2$, the heavy graph, after deleting isolated vertices, is exactly two disjoint edges, a three-vertex path, or a triangle. Indeed, forest rank is the sum of the nontrivial component sizes minus one; rank two permits only two components of size two or one component of size three.

Let $n_2,n_3$ count index triples containing exactly two or three heavy pairs. The joint-event bounds above can be written as
$$
10+45k+120\,1_{k=2}+570\,1_{k=3}.
$$
Each heavy pair belongs to five index triples, so
$$
S_3\le350+225h+120n_2+570n_3. \tag{8}
$$
Using $u\ge9-2h$ gives all remaining cases:

| Heavy graph | $(h,n_2,n_3)$ | $u$ lower bound | $S_2$ lower bound | $S_3$ upper bound | $D_7$ lower bound |
|---|---|---:|---:|---:|---:|
| Two disjoint edges | $(2,0,0)$ | 5 | 3300 | 800 | 2500 |
| Three-vertex path | $(2,1,0)$ | 5 | 3300 | 920 | 2380 |
| Triangle | $(3,0,1)$ | 3 | 3630 | 1595 | 2035 |

The minimum over these cases, (4), the rank-three case, and the $h=0,1$ cases is $2035$. This proves the second assertion.

## Blue events

Each blue event has size $\binom{15}{5}=3003$. For pair intersection size $j=0,1,2,3$,
$$
|E_i\cap E_j|=\binom{11+j}{1+j}=11,66,286,1001.
$$
There are four exhaustive cases for seven events.

If a pair intersects in three points, the spanning-tree bound gives
$$
D_7\ge1001+5\cdot11=1056.
$$
If all intersections have size at most two and there are at least two heavy pairs, put two of them into the tree to obtain
$$
D_7\ge2\cdot286+4\cdot11=616.
$$
If there are no heavy pairs, (3) gives $u\ge9$, and
$$
S_2\ge21\cdot11+55\cdot9=726.
$$
Any three blocks have union of size at least nine; their joint blue-event size is at most one. Hence $S_3\le35$ and $D_7\ge691$.

If there is exactly one heavy pair, $u\ge7$, and
$$
S_2\ge21\cdot11+275+55\cdot7=891.
$$
The five index triples containing that pair have union of size at least eight and joint blue-event size at most eleven. The other thirty triples have joint size at most one. Thus $S_3\le5\cdot11+30=85$ and $D_7\ge806$. The minimum of the four bounds is $616$.

## Additional events and use in a union bound

Adding an event $E$ changes $D_m$ by
$$
|E\cap\bigcup_{i\le m}E_i|\ge0,
$$
proving the asserted monotonicity. If original bad events have been divided into disjoint groups of original-edge indices, each applicable group may replace its sum of event sizes by its own union bound with the deduction proved here. No intersections between different groups are deducted, so these groupwise deductions can be combined without double charging. Establishing the actual grouping remains the responsibility of the caller.

The proof above is analytic. The [independent arithmetic receipt](../../context/propertyb35-paper/round01/root/whole_class_followup_20261020/red_four_union/RESULT.json) and [small checker](../../context/propertyb35-paper/round01/root/whole_class_followup_20261020/red_four_union/CHECK.py) only recompute its binomial constants and integer branches; they do not enumerate four-set families or hypergraphs. The [source derivation](../../context/propertyb35-paper/round01/root/whole_class_followup_20261020/red_four_union/REPORT.md) records the conditional caller arithmetic separately.
