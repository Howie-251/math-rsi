# Proof Package: heavy cross repeats consume global slack

## Claim

For an original legal order-$59$ graph with exact N15 at every zero-triangle vertex, let $N$ be its nonzero vertices, $Z$ its zero vertices, $m=|N|$, and $T$ its triangle count. Let $K$ count unordered defect edges of weight two with one endpoint in $N$ and one in $Z$. Then

$$K\le R_{NZ}\le2(4m-3T-59),$$

where $R_{NZ}$ is the part of the global heavy-capacity slack supported on nonedges between $N$ and $Z$, defined below.

As a further consequence, if $T=7$ and $m=21$, then at least one nonedge between two vertices of $N$ must have positive defect. Equivalently, the branch in which all such defect entries vanish is impossible.

## Status and scope

PROVABLE AS STATED, pending independent review. This is a general charging lemma and one bounded consequence for the seven-triangle case. It does not exclude the remaining branch with positive nonedge defect inside the twenty-one-vertex core. The proof uses exact N15, ordinary support transport, the global slack identity, and, only for the final consequence, the established fourth- and fifth-trace identities.

## Notation and dependencies

Use the actual defect $B=A^2+A-7I-J$ of the $8$-regular original graph. Let $t(v)$ count triangles through $v$. Its nonedge defect budget is $6-2t(v)$. For $n\in N$ and $z\in Z$ with $n\not\sim z$, put

$$q(n,z)=|N_G(n)\cap N_G(z)\cap Z|,$$

$$r(n,z)=B_{nz}-\binom{q(n,z)}2-\mathbf1_{\{B_{nz}=2\}}.$$

The common-zero-neighbor lemma gives $q(n,z)\le2$. The pointwise proof in `zero_heavy_global_capacity_20261011.md` gives $r(n,z)\ge0$. In fact $r(n,z)\in\{0,1\}$. Define

$$R_{NZ}=\sum_{n\in N}\sum_{z\in Z\setminus N_G(n)}r(n,z).$$

It is part of the nonnegative slack in that theorem, so

$$R_{NZ}\le\sum_{n\in N}R_n\le2(4m-3T-59).\tag{1}$$

The support-transport fact used below is this: at any root $v$, adjacent zero vertices in its positive defect support have equal weight and form an isolated edge of the full support; an isolated zero support vertex has neighbors in nonzero support of total row weight equal to its own weight. This follows from

$$\sum_{w\sim x}B_{vw}=B_{vx}\qquad(x\in Z,\ B_{vx}>0),\tag{2}$$

which is proved from exact N15 and $AB=BA$ in `nonzero_support_transport_20261011.md`.

## Proof of the general charging bound

**Step 1. A heavy cross repeat supplies a unit of slack.** Fix $B_{nz}=2$ with $n\in N,z\in Z$. If $q(n,z)\le1$, then $r(n,z)=1$; charge this defect edge to its own term.

Otherwise $q(n,z)=2$. Its three common neighbors consist of two zeros $x,y$ and one nonzero vertex $v$. Each pair $v,x$ and $v,y$ is a nonedge with at least the two common neighbors $n,z$. Adjacency is impossible because, for example, $v\sim x$ would make the triangle $n,v,x$ at a zero vertex. Thus both $B_{vx}$ and $B_{vy}$ are positive and belong to $\{1,2\}$.

They cannot both be two. If they were, their total weight four would exhaust the nonedge defect budget at $v\in N$, forcing $t(v)=1$ and exactly those two heavy nonedge repeats. The nonzero positive support of row $v$ would then consist of its two adjacent triangle partners, each of weight one. Applying (2) at $x$ forces $x\sim y$, because its two triangle partners can supply at most one unit of weight to a zero vertex. But $x,y$ are both adjacent to $n$, so this would create a triangle at a zero vertex.

Therefore at least one, say $B_{vx}$, equals one. Its common neighbors are exactly $n,z$, one nonzero and one zero. Consequently $q(v,x)=1$ and $r(v,x)=1$. Charge the original heavy edge $\{n,z\}$ to this light term.

**Step 2. The charges are distinct.** A charge to a heavy term is its own source edge, so these charges are distinct. A light charged pair $\{v,x\}$ has exactly one nonzero common neighbor $n$ and exactly one zero common neighbor $z$. Hence it uniquely determines its source heavy edge $\{n,z\}$. Different source heavy edges cannot select the same light term. Heavy and light charged terms are also disjoint. Thus the charging is injective, proving

$$K\le R_{NZ}.$$

Combining with (1) proves the general claim. $\square$

## Consequence: the repeat-free nonzero core at seven triangles is impossible

Suppose $T=7,m=21$, and additionally suppose

$$B_{uv}=0\quad\text{for every nonedge }\{u,v\}\subseteq N.\tag{3}$$

All seven triangles are vertex-disjoint because they have $21$ triangle incidences on $21$ nonzero vertices. Every nonzero root has exactly two positive defect entries in $N$, both unit entries at its adjacent triangle partners. Its nonedge defect budget four lies entirely in $Z$.

**Step 3. Row shapes and possible isolated light repeats.** Its zero-repeat pattern is initially $22$, $211$, or $1111$. Pattern $211$ is impossible: its lone heavy zero repeat cannot be paired with another heavy zero repeat, and an isolated heavy zero repeat cannot receive total weight two from an independent subset of the unit triangle edge. Pattern $22$ has its two zero repeats paired, by (2).

Let $a$ be the number of $22$ roots. The other $21-a$ roots have pattern $1111$. For such a root $n$, let $p_n\in\{0,1,2\}$ be the number of paired edges among its four zero support vertices. There are $4-2p_n$ isolated zero repeats. Put

$$b=\sum_{n\text{ of type }1111}(2-p_n).$$

Thus there are exactly $2b$ isolated light zero repeats, counted with their nonzero roots. Every such repeat has a nonzero common neighbor with its root, namely its unit support neighbor supplied by (2). Its defect is one, so it has fewer than two zero common neighbors and contributes one to $R_{NZ}$.

**Step 4. These isolated-light terms are disjoint from heavy charges.** There are $K=2a$ heavy cross repeats. Charges to heavy terms are already disjoint from isolated light terms. Consider a charge arising from a heavy repeat $n,z$ with common neighbors $v,x,y$ as in Step 1. Root $n$ has type $22$, and its zero support pair is isolated in the full support. Thus $z$ is adjacent to neither triangle partner of $n$. Since $v$ is its nonzero common neighbor with $n$, the edge $n,v$ is not a triangle edge.

The charged light pair $v,x$ has exactly the common neighbors $n,z$. By (3), the only positive nonzero support vertices of root $v$ are its triangle partners; $n$ is not one of them because $n,v$ is not a triangle edge. Consequently $x$ has no neighbor in the positive nonzero support of row $v$. Equation (2) forces it to have a zero support neighbor, so this charged light repeat is paired, not isolated.

The $2a$ injective heavy charges and the $2b$ isolated-light terms are therefore disjoint. The total slack at $T=7,m=21$ is eight, giving

$$2a+2b\le R_{NZ}\le8,\qquad a+b\le4.\tag{4}$$

**Step 5. The trace congruences contradict (4).** The row square sum is

$$s=38\cdot10+10a+6(21-a)=506+4a.$$

The fourth-trace identity $8C_4=6\cdot59+s-12T$ gives

$$8C_4=776+4a,$$

so $a$ is even.

For the fifth-trace remainder $e_n=Q_2(n)-\sum_vB_{nv}^2+5$, support transport gives $e_n=0$ for type $22$ and $e_n=4-p_n$ for type $1111$. Indeed their positive nonzero support is a unit edge, and the zero matching contribution is respectively four or $p_n$. Therefore

$$\sum_{n\in N}e_n=42-2a+b.$$

The identity from `matching_zero_global_trace_obstruction_20261011.md` gives $\sum_{n\in N}e_n+T\equiv4\pmod5$, hence

$$b\equiv2a\pmod5.\tag{5}$$

By (4), the only possible even values of $a$ are $0,2,4$. If $a=2$, (5) requires $b\equiv4\pmod5$, incompatible with $0\le b\le2$. If $a=4$, it requires $b\equiv3\pmod5$, incompatible with $b=0$. Thus $a=0$, and (4)--(5) give $b=0$.

But $a=0$ means every one of the $21$ nonzero roots has four light zero repeats, giving $84$ light defect incidences between $N$ and $Z$. N15 allows at most two light endpoints at each of the $38$ zeros, so there can be at most $76$ such incidences. This contradiction excludes (3). $\square$

## Boundaries and remaining work

At $T=7,m=21$, the general lemma gives $K\le8$. The further exclusion proves that some positive nonedge defect inside $N$ is necessary. That remaining defect is constrained by the same total slack eight, but is not excluded here. The conditional argument explicitly accounts for isolated light support vertices; assuming all $1111$ zero supports are paired would be unjustified without that accounting.
