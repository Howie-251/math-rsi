# Proof Package: excluding the twenty-vertex core at seven triangles

## Claim

Let $G$ be an original legal order-$59$ graph: simple and undirected, of maximum degree at most $8$, with every two distinct vertices joined by a path of length at most $2$. Assume exact N15 at every zero-triangle vertex: its actual defect row has weights $2,2,1,1$, and the induced graph on its support consists exactly of the two equal-weight matching edges.

Let $N$ be the vertices lying in triangles, $Z=V(G)\setminus N$, $m=|N|$, and $T$ the number of triangles. The case

$$T=7,\qquad m=20$$

is impossible. Consequently, any graph under these hypotheses with exactly seven triangles has $m=21$, and its seven triangles are vertex-disjoint.

## Status

PROVABLE AS STATED. Complete paper derivation, pending independent review. This strengthens the global heavy-capacity theorem by excluding its first equality case. The proof uses the exact N15 support condition, the previously derived equality consequences, elementary support transport, and the four-cycle trace identity. The fifth-trace congruence and the provisional split into nine or nineteen heavy nonzero rows are unnecessary for the contradiction.

## Assumptions and notation

The graph is $8$-regular by the ordinary root count. Its actual defect matrix is

$$B=A^2+A-7I-J,$$

which is symmetric, nonnegative, has zero diagonal and row sum $6$, and commutes with $A$. For a vertex $v$, let $t(v)$ denote its triangle count. The sum of its defect entries on true neighbors is $2t(v)$; its nonedge defect budget is therefore $6-2t(v)$.

The global heavy-capacity theorem in `zero_heavy_global_capacity_20261011.md` gives

$$59\le4m-3T,\qquad m\ge20,\qquad T\ge7.$$

Under $T=7,m=20$, equality holds. Its exact nonnegative-slack identity supplies the following facts, where common-neighbor counts always refer to the actual graph:

1. Every pair of distinct vertices has at most two zero common neighbors.
2. A light defect edge between zeros has no nonzero common neighbor.
3. A heavy defect edge between zeros has exactly one nonzero common neighbor.
4. If $n\in N$ and $y\notin N_G[n]$, then, with $q=|N_G(n)\cap N_G(y)\cap Z|$,
   $$B_{ny}=\binom q2+\mathbf1_{\{y\in Z,\ B_{ny}=2\}}.\tag{1}$$

In particular, a light defect edge between $N$ and $Z$ has exactly two zero common neighbors and no nonzero common neighbor. A heavy defect edge between $N$ and $Z$ has exactly two zero common neighbors and exactly one nonzero common neighbor.

## Proof strategy and dependency map

1. Equality rules out every positive defect on a nonedge between two nonzero vertices.
2. The seven triangles on twenty vertices consist of one pair sharing a single vertex and five disjoint triangles. This fixes all positive defect entries inside $N$.
3. A hypothetical heavy repeat between $N$ and $Z$ forces two heavy zero repeats at another nonzero root. Support transport forces these two zeros to be adjacent, contradicting their common neighbor.
4. With no such heavy repeats, every nonzero row has six unit entries. The resulting fourth trace gives a nonintegral four-cycle count.

## Proof

**Step 1. There are no nonedge repeats within $N$.** Suppose that distinct, nonadjacent $n,y\in N$ have $B_{ny}>0$. Equation (1) has no indicator term, and $q\le2$. Thus $B_{ny}=1$ and $q=2$. Let $z,w\in Z$ be the two zero common neighbors of $n,y$.

The vertices $z,w$ are nonadjacent: an edge between them would produce a triangle containing a zero vertex. They have the two common neighbors $n,y$, so $B_{zw}\ge1$. N15 at $z$ gives $B_{zw}\in\{1,2\}$. If it is $1$, equality fact 2 is violated, since $n$ is a nonzero common neighbor. If it is $2$, equality fact 3 is violated, since $n$ and $y$ are distinct nonzero common neighbors. Both alternatives are impossible. Therefore

$$B_{ny}=0\quad\text{for every nonedge }\{n,y\}\subseteq N.\tag{2}$$

**Step 2. The triangle support inside $N$.** The total triangle-vertex incidence is $3T=21$, while $|N|=20$. Each vertex in $N$ occurs at least once. Thus one vertex occurs in exactly two triangles, and the other nineteen occur in exactly one. The two triangles through the exceptional vertex share only that vertex; sharing another vertex would give a second vertex with triangle count at least two. The remaining five triangles are pairwise vertex-disjoint and disjoint from these two.

No true edge lies in two triangles. On a true edge, its defect equals its number of triangles. Combining this with (2), the positive defect support inside $N$ consists exactly of the triangle edges, each with weight one. In particular, if $t(v)=1$, the nonzero part of its positive support consists of its two triangle partners, of weight one, and those two partners are adjacent.

**Step 3. A transport identity at zero support vertices.** For any root $v$ and any zero vertex $x$ with $B_{vx}>0$, exact N15 at $x$ implies

$$\sum_{w\sim x}B_{vw}=B_{vx}.\tag{3}$$

Indeed, in the positive support of row $x$, the endpoint $v$ has exactly its equal-weight partner as a neighbor. Hence $(BA)_{xv}=B_{xv}$. The matrices $A$ and $B$ commute and are symmetric, so $BA$ is symmetric. Its $(v,x)$ entry is the sum on the left of (3).

A particular consequence needed below is this: if $t(v)=1$ and its nonedge support consists of two zeros $x,y$, both of weight two, then $x$ and $y$ are adjacent. The other positive-support vertices are the two adjacent triangle partners $a,b$ of $v$, each of weight one. Equation (3) at $x$ reads

$$2=2A_{xy}+A_{xa}+A_{xb}.$$

Because $x$ is zero and $a,b$ are adjacent, $A_{xa}+A_{xb}\le1$. Therefore $A_{xy}=1$.

**Step 4. Heavy defect edges between $N$ and $Z$ are impossible.** Suppose that $u\in N$, $z\in Z$, and $B_{uz}=2$. The equality facts give precisely three common neighbors of $u,z$: one nonzero vertex $v$ and two zero vertices $x,y$.

The vertices $v,x$ have the two common neighbors $u,z$. They cannot be adjacent, since $u,v,x$ would then form a triangle containing the zero vertex $x$. Therefore $B_{vx}\ge1$. If $B_{vx}=1$, the light-repeat equality fact would forbid the nonzero common neighbor $u$. N15 at $x$ bounds its positive defect values by two, so $B_{vx}=2$. Applying the same argument to $v,y$ gives $B_{vy}=2$.

The nonedge defect budget of $v$ is $6-2t(v)\le4$, since $v\in N$. These two heavy entries already consume four. Thus $t(v)=1$ and its entire nonedge support is $\{x,y\}$, of weights two. Step 3 forces $x\sim y$. But $x$ and $y$ are both adjacent to $u$, producing a triangle $u,x,y$ containing zero vertices. This is a contradiction. Hence

$$B_{nz}\ne2\qquad(n\in N,\ z\in Z).\tag{4}$$

**Step 5. The fourth trace is impossible.** By (2) and (4), every nonzero row of $B$ has only unit positive entries: triangle edges have weight one, nonedges within $N$ have weight zero, and positive entries toward $Z$ have weight one. Its row sum is six, so its row square sum is also six. Every zero row has square sum $2^2+2^2+1^2+1^2=10$. Consequently

$$s:=\operatorname{tr}(B^2)=20\cdot6+39\cdot10=510.\tag{5}$$

For completeness, the actual fourth-trace identity is

$$8C_4=6\cdot59+s-12T,\tag{6}$$

where $C_4$ counts unoriented simple four-cycles, whether or not they have chords. To obtain it, the defect identity gives $\operatorname{tr}(AB)=6T$ and

$$\operatorname{tr}(A^2B)=s-6T+6\cdot59.$$

Direct substitution of $B$ into the same trace gives

$$\operatorname{tr}(A^2B)=\operatorname{tr}(A^4)+6T-120\cdot59.$$

Thus $\operatorname{tr}(A^4)=126\cdot59+s-12T$. Counting four-step closed walks in an $8$-regular graph gives $\operatorname{tr}(A^4)=120\cdot59+8C_4$, proving (6).

Substituting $T=7$ and (5) into (6) gives

$$8C_4=354+510-84=780,$$

but $780$ is not divisible by $8$. This contradiction excludes $T=7,m=20$.

Finally, if $T=7$, the global theorem gives $m\ge20$ and triangle incidence gives $m\le21$. Excluding $m=20$ forces $m=21$, so all seven triangles are vertex-disjoint. $\square$

## Scope and open risks

The result excludes the entire $T=7,m=20$ equality case, not just either of its provisional row-pattern branches. It leaves $T=7,m=21$ and larger triangle counts open. It does not establish N15 for arbitrary original graphs or close H5. No computation, additional trace congruence, or formalization was used. Independent review of this new exclusion remains pending.
