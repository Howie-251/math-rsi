# Six red four-sets on eighteen points

Let $A_1,\ldots,A_6$ be distinct four-subsets of an eighteen-point set. Choose an eleven-subset $X$ uniformly by counting all $D=\binom{18}{11}=31824$ choices. Write $E_i=\{A_i\subseteq X\}$ and $R=\binom{14}{7}=3432$. Then

\[
 \left|\bigcup_{i=1}^6 E_i\right|\le 6R-2616. \tag{1}
\]

The sets need not cover the eighteen points. There is no hypergraph, degree, or pair-cover assumption in this lemma.

For two distinct sets intersecting in $j=0,1,2,3$ points, the corresponding event intersection has size

\[
 w_j=\binom{10+j}{3+j}=(120,330,792,1716)_j. \tag{2}
\]

For any forest on these six event indices, its pair-event intersections may be subtracted from the sum of the six single-event counts. Pointwise, the induced forest on the occurring events has at most their number minus one edges. We may consequently use any tree, including edges joining disjoint four-sets. We also use the upper Bonferroni bound

\[
 |\bigcup_iE_i|\le 6R-S_2+S_3,\qquad
 S_k=\sum_{|I|=k}|\bigcap_{i\in I}E_i|. \tag{3}
\]

Let $Q_1,Q_2$ have edges when the corresponding four-sets intersect in at least one, respectively at least two, points. The rank of a graph here means its number of vertices minus its number of components, counting isolated vertices. Let $r_1,r_2$ be these ranks.

## 1. Three independent heavy pairs

If $r_2\ge3$, take three edges of a $Q_2$-forest and extend them to a tree on all six indices. By (2) this subtracts at least

\[
 3\cdot792+2\cdot120=2616. \tag{4}
\]

Hence assume $r_2\le2$.

## 2. A pair intersecting in three points

If $r_2=2$, include a three-intersection edge and a second independent $Q_2$ edge, then extend to a tree. The deduction is at least

\[
 1716+792+3\cdot120=2868.
\]

If $r_2=1$, the three-intersection pair is the only edge of $Q_2$. We claim $r_1\ge3$. Otherwise $Q_1$ has at least four components. With six vertices, its nontrivial component sizes are either one pair; two pairs; or one triple. The component containing the three-intersection pair has support at least five points. In the two-pair case, the other pair intersects in exactly one point, and the total support is at least $5+7+4+4=20$. In the one-pair case it is at least $5+4+4+4+4=21$. In the triple case, the third set meets each member of the special pair in at most one point. It therefore adds at least two points to their five-point union, giving total support at least $7+4+4+4=19$. Distinct components have disjoint supports; all three cases contradict an eighteen-point ground set.

Thus a $Q_1$-forest containing the three-intersection pair has at least three edges. Extend three of them to a tree, obtaining deduction

\[
 1716+2\cdot330+2\cdot120=2616.
\]

This settles every case with a three-point intersection.

## 3. All pair intersections at most two

Let $m_1,m_2$ count pairs intersecting in exactly one and two points. The union of the six four-sets has size at most eighteen, so

\[
 m_1+2m_2=\sum_x\binom{d_x}{2}
 \ge\sum_{x:d_x>0}(d_x-1)
 =24-|\bigcup_iA_i|\ge6. \tag{5}
\]

Also

\[
 S_2=15\cdot120+210m_1+672m_2. \tag{6}
\]

We bound triple intersections by the number of one- and two-intersection pairs inside the triple. A triple with no two-intersection pair and $s$ one-intersection pairs has union size at least $12-s$, so its event intersection has size at most

\[
 (0,1,8,36)_s\le12s\quad(s=0,1,2,3). \tag{7}
\]

A triple with exactly one two-intersection pair and $s=0,1,2$ one-intersection pairs has union size at least $10-s$, so its event intersection has size at most

\[
 (8,36,120)_s\le96+12s. \tag{8}
\]

These bounds remain safe if a point belongs to all three sets, since that increases the union size in the inclusion-exclusion formula.

Because $r_2\le2$, the graph $Q_2$ is one of: empty; one edge; two disjoint edges; a three-vertex path; a triangle, together with isolated vertices. These five possibilities exhaust graphs of rank at most two.

### 3.1 No heavy pair

Every pair belongs to four triples. Equations (5)–(7) give

\[
 S_2-S_3\ge1800+(210-48)m_1\ge1800+162\cdot6=2772.
\]

### 3.2 One heavy pair, or two disjoint heavy pairs

No triple contains two heavy pairs. Summing (7)–(8), with every pair again in four triples, gives

\[
 S_3\le384m_2+48m_1.
\]

For $m_2=1$, (5) gives $m_1\ge4$, hence

\[
 S_2-S_3\ge1800+288+162\cdot4=2736.
\]

For two disjoint heavy pairs, $m_2=2$ and $m_1\ge2$, giving

\[
 S_2-S_3\ge1800+576+162\cdot2=2700.
\]

### 3.3 Two heavy pairs forming a path

There is only one triple containing both heavy pairs. If its third pair is disjoint, that triple has event intersection at most (120\), already below the two allowances of (96\). If its third pair intersects in one point, its event intersection is at most (330\), exceeding $2\cdot96+12$ by (126\). Thus in all cases

\[
 S_3\le768+48m_1+126.
\]

For $m_1\ge3$, equations (3) and (6) give deduction at least

\[
 1800+576+162\cdot3-126=2736.
\]

By (5), the only remaining value is $m_1=2$. If the third pair of the heavy path is disjoint, the stronger no-exception calculation gives deduction at least (2700\). Otherwise, one of the two one-intersection pairs closes the path. The special triple contributes at most (330\). There are six other triples containing exactly one heavy pair. In each such triple the closing pair cannot occur; only the other one-intersection pair is available. Each contributes at most (36\). The remaining thirteen triples have no heavy pair and at most two one-intersection pairs, and each contributes at most (8\). Therefore

\[
 S_3\le330+6\cdot36+13\cdot8=650,
 \qquad S_2-S_3\ge3564-650=2914.
\]

### 3.4 A heavy triangle

The unique triple containing all three heavy pairs contributes at most (792\), since its union has at least six points. Nine triples contain exactly one heavy pair; ten contain none. For a triple of the former kind, (8) improves to

\[
 |E_i\cap E_j\cap E_k|\le8+56s\quad(s=0,1,2).
\]

For the latter kind use (7). If $X$ and $Y$ count the incidences of one-intersection pairs in these two classes of triples, then $X+Y=4m_1$; none occurs in the heavy triangle. Hence

\[
 S_3\le792+9\cdot8+56X+12Y
 \le864+224m_1.
\]

As $m_1\le12$,

\[
 S_2-S_3\ge3816+210m_1-864-224m_1
 =2952-14m_1\ge2784.
\]

Every Bonferroni case subtracts at least (2616\), as do the forest cases. This proves (1).

## 4. Adding further red four-sets

For any $a\ge6$ distinct four-sets on the same eighteen points, first apply (1) to six of them. Regard their union event as one event, and add each remaining event in a star centered there. Every new event intersects this union in at least the intersection with one fixed original event, which has size at least (120\) by (2). Thus

\[
 \left|\bigcup_{i=1}^aE_i\right|
 \le aR-2616-120(a-6). \tag{9}
\]

This is a single-event-union argument in one fixed probability space; deductions from incompatible anchors are not added.
