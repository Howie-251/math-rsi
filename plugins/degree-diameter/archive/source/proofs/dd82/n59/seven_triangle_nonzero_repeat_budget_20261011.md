# Proof Package: the remaining nonzero-repeat budget at seven triangles

## Claim and status

Assume an original legal order-$59$ graph with exact N15 at every zero-triangle vertex. Suppose $T=7$ and $m=21$, so the seven triangles are vertex-disjoint. Let $N$ be their vertex set and $Z$ the other $38$ vertices. Let

$$W=\sum_{\substack{\{u,v\}\subseteq N\\u\not\sim v}}B_{uv}$$

be the weighted sum over unordered nonedges in $N$, and let $K$ count heavy defect edges between $N$ and $Z$.

The following necessary conditions hold:

1. $1\le W\le6$ and $2W+K\le12$.
2. If $W=5$, the positive nonedge defect graph on $N$ consists of a unit triangle and two further distinct unit edges. In particular, every such defect entry is one.
3. If $W=6$, this defect graph consists of two unit triangles sharing at most one vertex. All cross repeats are light and have no nonzero common neighbor. The two possible incidence patterns are narrowed further in the last section below.

Status: PROVABLE AS STATED, pending independent review. The statements are necessary conditions on one original graph. No graph realizing them is constructed, and $W\le4$ and the surviving unit-edge patterns at $W=5,6$ are not excluded.

## Assumptions, notation, and dependencies

Use the actual defect $B=A^2+A-7I-J$. Every nonzero vertex has triangle count one, has two unit defect entries at its triangle partners, and has nonedge defect budget four. Every zero row has weights $2211$ and the exact induced matching prescribed by N15.

For a nonedge $u,v\in N$, let $q_{uv}$ be its number of zero common neighbors. It is at most two. Define

$$R_{NN}=2\sum_{\substack{\{u,v\}\subseteq N\\u\not\sim v}}
\left(B_{uv}-\binom{q_{uv}}2\right).$$

The factor two counts both root orientations. Let $R_{NZ}$ be the cross slack defined in `heavy_cross_repeat_slack_20261011.md`. That proof gives $K\le R_{NZ}$.

For $i=0,1,2$, let $l_i$ count light defect edges between zeros having exactly $i$ nonzero common neighbors. For $i=1,2,3$, let $h_i$ count heavy defect edges between zeros having exactly $i$ nonzero common neighbors. Every heavy such edge has at least one nonzero common neighbor. The global slack identity becomes

$$8=l_1+2l_2+2h_2+4h_3+R_{NN}+R_{NZ}.\tag{1}$$

This is the identity in `zero_heavy_global_capacity_20261011.md`, with its light-neighborhood count equal to $l_1+2l_2$ and heavy multiplicity excess equal to $h_2+2h_3$.

The repeat-free case $W=0$ was excluded in `heavy_cross_repeat_slack_20261011.md`, including the possible isolated light supports. Thus $W\ge1$ here.

We use the exact support-transport theorem and the trace identities

$$8C_4=6\cdot59+s-12T,\qquad
\sum_{n\in N}e_n+T\equiv4\pmod5,$$

where $s=\sum_{v,w}B_{vw}^2$ and $e_n=Q_2(n)-\sum_wB_{nw}^2+5$. All these quantities refer to the actual graph.

## 1. Exact pair counting and the bound $W\le6$

Let $P$ count unordered nonedge pairs in $N$ having exactly two zero common neighbors. Each such pair determines its unique unordered pair of zero common neighbors. Conversely, two zeros having $i$ nonzero common neighbors determine $\binom i2$ such pairs in $N$. Their nonzero common neighbors are pairwise nonadjacent, since an edge between them would create a triangle at a zero vertex. N15 bounds the zero pair's total common-neighbor count by three. Therefore

$$P=l_2+h_2+3h_3.\tag{2}$$

The definition of $R_{NN}$ gives exactly

$$W=P+\frac12R_{NN}.\tag{3}$$

Substitution of (2)--(3) into (1) yields the useful exact relation

$$8=2W+l_1-2h_3+R_{NZ}.\tag{4}$$

In particular,

$$2W+K+l_1\le8+2h_3.\tag{5}$$

Equation (1) gives $h_3\le2$, and (2)--(3) give $W\ge3h_3$. Therefore

$$2W+K\le12,\qquad W\le6.$$

These inequalities do not assume that zero repeat supports at nonzero roots are fully paired.

## 2. What equality $W=6$ forces

If $W=6$, (4) and $h_3\le2$ force

$$h_3=2,\qquad l_1=R_{NZ}=K=0.$$

Equations (1)--(3) then give

$$l_2=h_2=R_{NN}=0,\qquad P=6.$$

Each of the two heavy zero pairs counted by $h_3$ has three nonzero common neighbors. Its three unordered pairs of nonzero common neighbors contribute a triangle to the nonedge defect graph on $N$. Two such triples cannot share two vertices: that shared pair of nonzero vertices would then have more than two zero common neighbors. The two repeat triangles therefore share at most one vertex.

They already account for six positive nonedge pairs, while the entire weighted budget is $W=6$. Thus all six repeat entries are one and there are no others. Because $R_{NN}=0$, every repeat pair has exactly its two zero common neighbors and no nonzero common neighbor.

Also $R_{NZ}=0$ and $K=0$, so every positive cross repeat has weight one and has two zero common neighbors and no nonzero common neighbor.

## 3. The possible weights when $W=5$

If $W=5$, (4) and $W\ge3h_3$ give

$$h_3=1,\qquad l_1=R_{NZ}=K=0.$$

The three nonzero common neighbors of the unique heavy zero pair counted by $h_3$ supply a positive repeat triangle on $N$. Its baseline unit weights use three of the five available units. The remaining two units may add to these edges or occur on other pairs.

Let

$$F=\sum_{\substack{\{u,v\}\subseteq N\\u\not\sim v}}B_{uv}(B_{uv}-1).$$

In general the row sums and the zero-row squares give

$$s=506+2F+2K.$$

Here $K=0$, so the fourth-trace identity requires $F\equiv0\pmod4$. There are only two ways to distribute the remaining two units consistent with this congruence:

- Increase two distinct edges of the triangle from one to two; then $F=4$.
- Add two distinct unit edges outside the triangle; then $F=0$.

Indeed, adding two to one triangle edge gives $F=6$; a new edge of weight two gives $F=2$; increasing one triangle edge and adding one new unit edge also gives $F=2$. Those possibilities fail the fourth trace.

### The triangle with two doubled edges is impossible

Write its vertices as $u,v,w$, with

$$B_{uv}=B_{uw}=2,\qquad B_{vw}=1.$$

The row at $u$ spends its nonedge budget four inside $N$ and has no zero repeats. Each of $v,w$ spends three inside $N$ and has exactly one unit zero repeat, denoted $x_v,x_w$. Because a single zero support vertex cannot be paired, transport makes it isolated. Since $R_{NZ}=0$, it cannot neighbor a triangle partner of its root. Its only unit nonzero repeat endpoint is the other endpoint of the light edge $v,w$, so

$$x_v\sim w,\quad x_v\not\sim u,
\qquad x_w\sim v,\quad x_w\not\sim u.\tag{6}$$

The three pairs in this repeat triangle have the same two zero common neighbors. The heavy pairs $u,v$ and $u,w$ each have one further common neighbor in $N$; the light pair $v,w$ has none in $N$.

Let $p_{uv}$ count the triangle partners of $u$ adjacent to $v$, and $q_{uv}$ the triangle partners of $v$ adjacent to $u$. Evaluating $AB=BA$ at $(u,v)$ gives

$$p_{uv}=q_{uv}.$$

To check the equality explicitly, row $u$ has only its two unit triangle partners and its two heavy nonzero repeats; the other repeat vertex $w$ is nonadjacent to $v$. Row $v$ has its unit triangle partners, repeats $u,w$ of weights two and one, and the zero repeat $x_v$, which is nonadjacent to $u$ by (6). These are all terms.

The unique nonzero common neighbor of $u,v$ cannot be a triangle partner of both, since their original triangles are vertex-disjoint. Hence $p_{uv}+q_{uv}\le1$, and the equality forces both to vanish. The same argument applies to $u,w$.

Consequently the weighted edge sum on nonzero support is one at each of $u,v,w$, supplied only by its own triangle-partner edge. Their nonzero row square sums are respectively $10,7,7$. Their zero supports contain no paired edge. The transport formula therefore gives

$$e_u=-4,\qquad e_v=e_w=-1.$$

Every other nonzero root has no nonzero nonedge repeat and has four light zero repeats. Since $R_{NZ}=0$, an isolated such repeat could not have a neighbor in its positive nonzero support, so those four zeros are paired. Each of these eighteen roots has remainder two. Thus

$$\sum_{n\in N}e_n=-4-1-1+18\cdot2=30.$$

But $30+7\not\equiv4\pmod5$. This excludes the doubled-edge pattern. Hence $W=5$ has exactly the unit-edge form in the claim.

## 4. Transport narrows both $W=6$ incidence patterns

The following are necessary incidence conditions, not constructions. A zero repeat at a nonzero root with a nonzero repeat endpoint may be isolated: absence of nonzero common neighbors only forbids adjacency to true nonzero neighbors of the root. The argument below explicitly allows adjacency to its nonedge repeat endpoints.

Call a repeat-triangle vertex of nonedge repeat degree two active if its two light zero repeats are isolated. Otherwise those two zeros are paired. A root with no nonzero nonedge repeat has four light zeros, all paired, and remainder two. A repeat-degree-two root has nonzero support square sum four and weighted nonzero support edge sum one; its remainder is one when its zeros are paired and two when they are isolated.

### 4.1 Two vertex-disjoint repeat triangles

Let $q$ be the number of active vertices among these six vertices. Then

$$\sum_{n\in N}e_n=36+q,$$

so the fifth trace gives $q\equiv1\pmod5$.

For a repeat edge $v,w$, let $j_{vw}$ count the isolated zero repeats of root $v$ adjacent to $w$. Transport makes each isolated zero repeat adjacent to exactly one of its two unit nonedge repeat endpoints. The true triangle partners are unavailable because $R_{NZ}=0$.

For an edge of either repeat triangle, evaluating $AB=BA$ gives $j_{vw}=j_{wv}$. The nonzero terms vanish: the two other repeat endpoints within that triangle are nonadjacent in the original graph, and a pair with positive nonedge defect has no nonzero common neighbor. At each vertex the sum of its two $j$ values is either zero or two. Thus a repeat triangle can have zero, two, or three active vertices, but cannot have exactly one.

Across the two triangles, $q\equiv1\pmod5$ and $0\le q\le6$ therefore force $q=6$. All six vertices are active. The degree-two equations on each three-vertex triangle then force

$$j_{vw}=1$$

on every repeat edge in either direction. Thus each repeat root has exactly one light zero repeat adjacent to each of its two repeat partners.

### 4.2 Two repeat triangles sharing one vertex

Write the repeat triangles as $uab$ and $ucd$. The shared root $u$ has repeat degree four and no zero repeats. The four outer roots have repeat degree two and either two paired or two isolated zero repeats.

There are no original edges inside $\{a,b\}$ or inside $\{c,d\}$. Original edges between these two pairs form a matching: two edges incident to the same outer vertex would give a nonzero common neighbor to the opposite repeat pair, which has none. Let $c_0\in\{0,1,2\}$ count these original matching edges, and let $q$ count active outer vertices. The remainder at $u$ is $c_0$, so

$$\sum_{n\in N}e_n=36+c_0+q,
\qquad c_0+q\equiv1\pmod5.\tag{7}$$

Let $c_a\in\{0,1\}$ be the matching degree of $a$, and define $c_b,c_c,c_d$ likewise. Let $j_{au}$ count the isolated zero repeats of root $a$ adjacent to $u$. Since $u$ has no zero repeats, evaluating $AB=BA$ at $(a,u)$ gives

$$j_{au}=c_a.$$

Evaluating it on the repeat edge $a,b$ gives $j_{ab}=j_{ba}$. If $\epsilon_a,\epsilon_b\in\{0,1\}$ indicate activity, transport therefore yields

$$2\epsilon_a-c_a=2\epsilon_b-c_b.$$

The parity of this equality forces $c_a=c_b$ and then $\epsilon_a=\epsilon_b$. The same holds for $c,d$. Thus $c_0=1$ is impossible.

If $c_0=0$, the active count $q$ is one of $0,2,4$, contradicting (7). Hence $c_0=2$. Every outer vertex then has $j_{au}=1$ or its counterpart and is active, so $q=4$. Its other isolated light zero repeat is adjacent to its outer repeat partner.

Therefore this branch requires exactly two original matching edges between the outer pairs, and all four outer roots have two isolated light zero repeats.

## Remaining branches

The present deductions leave:

- $1\le W\le4$, subject to the exact slack equation (4).
- $W=5$: one unit repeat triangle and two additional distinct unit repeat edges.
- $W=6$: either two disjoint unit repeat triangles with the forced isolated-support incidences above, or two sharing a vertex with the forced outer matching and isolated supports above.

These are constraints on the actual graph; no independent matrix assignment or isolated integer template is promoted to a graph witness. No finite computation or formalization was performed. The claims require fresh review before promotion.
