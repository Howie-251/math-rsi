# The original graph on heavy endpoints is a constrained two-fold lift

## Claim and status

**PROVABLE AS STATED.** New paper derivation awaiting independent review.
For an actual legal order-62 graph with connected repeat support, let
$D$ be the set of $2d$ heavy endpoints. The heavy-mate involution is an
automorphism of $G[D]$. The graph $G[D]$ is a two-fold lift of a simple
graph $F$ on its $d$ heavy pairs, has no triangles or four-cycles, and
has maximum degree at most four.

Writing $m=|E(F)|$, the following bounds hold:

| $d$ | $1$ | $3$ | $5$ | $7$ | $9$ |
|---|---|---|---|---|---|
| Upper bound on $m$ | $0$ | $3$ | $6$ | $11$ | $17$ |
| Upper bound on $|E(G[D])|=2m$ | $0$ | $6$ | $12$ | $22$ | $34$ |

These restrict the remaining heavy configurations but do not exclude
any of the five values of $d$ or prove a complete order-62 contradiction.

## Assumptions and notation

Use the actual connected-repeat order-62 setting:

$$A\mathbf1=8\mathbf1,\qquad B=A^2+A-7I-J,\qquad
B\mathbf1=3\mathbf1,\qquad AB=BA.$$

The established reductions imply that $G$ is triangle-free, all repeat
entries are at most two, every double repeat is D1, and
$d\in\{1,3,5,7,9\}$. These consequences and their source chain are
collected in `CONNECTED_REPEAT_REDUCTION.md`.

For each heavy endpoint $x\in D$, let $h(x)$ be its heavy mate and
$a(x)$ its unit mate. The exact repeat row is

$$B_x=2e_{h(x)}+e_{a(x)}.\tag{1}$$

The D1 local results make $h$ a fixed-point-free involution on $D$,
put $a(x)$ outside $D$, and give $a(x)\ne a(h(x))$.
The common neighbors of $x,h(x)$ are precisely their generated unit
triangle, disjoint from $D$ by `GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`.
In particular a heavy pair is an original nonedge and has no common
neighbor in $D$.

Let the heavy pairs be indexed by $1,\ldots,d$. Write $r_i$ for the
common degree in $G[D]$ of the two endpoints in pair $i$; equality of
these degrees is proved below. Let $Q=A[D]$ and let $H$ be the
permutation matrix of $h$ on $D$.

## Strategy and dependency map

Commutation at two heavy endpoints separates into an even term and a
binary term, forcing the involution symmetry. The actual common-neighbor
counts then exclude four-cycles and give a sum-of-squared-degrees bound.
At equality, the signed adjacency matrix on the antisymmetric part of
the two-fold lift satisfies a particularly restrictive quadratic
identity. That identity removes the extremal edge counts for
$d=5,7,9$.

The proof uses actual repeat rows and common-neighbor counts. The
maximum-degree-four statement additionally uses the complete unit row
at root label $4$ in `D1_MATCH_C4_TRANSPORT_REFINEMENT.md`. No graph
enumeration or solver is used.

## 1. Commutation gives the heavy-mate automorphism

For any $x,y\in D$, the $(x,y)$ entry of $AB=BA$ and (1) give

$$
2A_{x,h(y)}+A_{x,a(y)}
=2A_{h(x),y}+A_{a(x),y}.
\tag{2}
$$

The difference of the even terms is divisible by two, while the
difference of the final binary terms belongs to $\{-1,0,1\}$. Thus
both differences vanish:

$$
A_{x,h(y)}=A_{h(x),y},\qquad
A_{x,a(y)}=A_{a(x),y}=A_{y,a(x)}.
\tag{3}
$$

These equalities also hold when $x=y$ or $x=h(y)$; no distinctness
was used in separating the terms. Replacing $y$ by $h(y)$ gives

$$A_{xy}=A_{h(x),h(y)}.$$

Hence $h$ is an automorphism of $G[D]$, $QH=HQ$, and the two endpoints
of each heavy pair have equal internal heavy degree. The second
identity in (3) is a further reciprocity constraint on original
adjacency between heavy endpoints and their unit mates.

## 2. The lift structure, short-cycle restrictions, and maximum degree

Between two different heavy pairs, involution symmetry makes the
original adjacency block have the form

$$\begin{pmatrix}p&q\\q&p\end{pmatrix},\qquad p,q\in\{0,1\}.$$

The case $p=q=1$ is impossible: the two endpoints of either heavy
pair would have heavy endpoints as common original neighbors. Thus
the block is zero or one of the two perfect-matching matrices. There
are no original edges inside a heavy pair. Define the simple graph
$F$ on heavy pairs by placing an edge exactly when the corresponding
block is a perfect matching. This proves the two-fold lift description,
with $\deg_F(i)=r_i$ and $|E(G[D])|=2|E(F)|=2m$.

The graph $G[D]$ is triangle-free because $G$ is. It has no four-cycle
either. Opposite vertices in such a cycle would have two common heavy
neighbors. If they are a heavy pair, this contradicts the generated
triangle description. Otherwise their mutual repeat entry is zero:
by (1), a heavy endpoint has no heavy repeat neighbor except its mate.
The actual identity $c_G(x,y)+A_{xy}=1+B_{xy}$ then gives
$c_G(x,y)\le1$, again a contradiction.

For the degree bound, normalize a D1 root at any $x\in D$, with its
eight original neighbors labelled $1,\ldots,8$. Labels $1,2,3$ form
its generated unit triangle and cannot be heavy endpoints. The C4
transport refinement gives the complete row
$B_4=e_1+e_f+e_g$ with three distinct unit entries, so label $4$ is
not heavy either. At most labels $5,6,7,8$ lie in $D$. Therefore

$$0\le r_i\le4.\tag{4}$$

For an equivalent sign description, choose one endpoint in each heavy
pair. Give an edge of $F$ sign $+1$ if its lift joins the chosen
endpoints and sign $-1$ if it crosses the choices. Every base triangle
or four-cycle must have negative sign product; a positive product
would lift to original triangles or four-cycles. This is a necessary
condition, not a sufficient realizability criterion.

## 3. A squared-degree bound from actual common neighbors

Count unordered pairs of vertices of $D$ having a common neighbor in
$D$. Triangle-freeness excludes adjacent pairs, and generated-triangle
separation excludes heavy pairs. Every other pair has at most one
common heavy neighbor, by the preceding common-neighbor argument.
Thus

$$
\sum_{v\in D}\binom{\deg_{G[D]}(v)}2
\le\binom{2d}{2}-|E(G[D])|-d.
$$

The left side is $2\sum_i\binom{r_i}{2}$, while
$|E(G[D])|=2m$ and $\sum_i r_i=2m$. Rearrangement gives

$$\boxed{\sum_{i=1}^d r_i^2\le2d(d-1)}.\tag{5}$$

At equality, every nonadjacent, nonmate pair of heavy endpoints has
exactly one common heavy neighbor. Therefore the full matrix identity
on $D$ becomes

$$Q^2+Q=\operatorname{diag}(\deg_{G[D]}-1)+J-H.\tag{6}$$

Its diagonal entries are the internal heavy degrees, and its
off-diagonal entries encode precisely the common-neighbor counts just
specified.

## 4. Equality forces a signed quadratic identity

Consider the subspace spanned by $e_x-e_{h(x)}$, one basis vector for
each chosen heavy-pair representative. Since $Q$ commutes with $H$,
this subspace is invariant. The restriction of $Q$ in this integer
basis is the symmetric signed adjacency matrix $Z$ of $F$: its
nonzero off-diagonal entries are $+1$ or $-1$, and its diagonal is zero.

On this subspace $H=-I$ and $J=0$, so (6) becomes

$$\boxed{Z^2+Z=\operatorname{diag}(r_1,\ldots,r_d)}.\tag{7}$$

The left side commutes with $Z$. Consequently

$$Z\operatorname{diag}(r_i)=\operatorname{diag}(r_i)Z.$$

For an edge $ij$ of $F$, $Z_{ij}\ne0$, and the corresponding entry
forces $r_i=r_j$. Hence, whenever equality holds in (5), edges of
$F$ can join only vertices of equal degree. Every connected component
of $F$ is regular.

## 5. The five numerical edge bounds

For $d=1$, the simple graph $F$ has no edge. For $d=3$, simplicity
gives $m\le3$.

For $d=5$, inequality (5) gives $\sum r_i^2\le40$. Cauchy's inequality
and $\sum r_i=2m$ imply $4m^2\le200$, hence $m\le7$. If $m=7$,
five nonnegative integers summing to $14$ have sum of squares at least
$40$, with equality only for the multiset

$$\{3,3,3,3,2\}.$$

This follows by repeatedly replacing two degrees differing by at least
two by two closer integers, which strictly decreases their squared
sum. Thus equality holds in (5), and Section 4 forbids any edge from
the unique degree-two vertex to a degree-three vertex. It has no other
degree-two vertex to neighbor, a contradiction. Hence $m\le6$.

For $d=7$, inequality (5) gives $\sum r_i^2\le84$, and Cauchy's
inequality gives $m\le12$. If $m=12$, the same integer balancing
argument shows that the minimum squared sum is $84$, attained only
by

$$\{4,4,4,3,3,3,3\}.$$

Again equality holds in (5). Each of the three degree-four vertices
could neighbor only those three vertices, so it would have degree at
most two. This contradiction gives $m\le11$.

For $d=9$, inequality (5) gives $\sum r_i^2\le144$, so $m\le18$.
Equality $m=18$ in Cauchy's inequality forces all nine degrees to be
four, and (7) becomes

$$Z^2+Z=4I_9.$$

The polynomial $t^2+t-4$ is irreducible over the rationals, since its
discriminant $17$ is not a square. An integer matrix satisfying this
polynomial has its two conjugate eigenvalues with equal multiplicity:
its rational characteristic polynomial is a power of
$t^2+t-4$. Its dimension must therefore be even. The dimension here
is nine, a contradiction. Hence $m\le17$.

Multiplying these five bounds by two gives the claimed edge bounds
for $G[D]$.

## 6. Base distance separates heavy vertices from other generated triangles

Let $D_i$ be heavy pair $i$, and let $S_i$ be its generated triangle.
For different indices $i,j$, if their distance in $F$ is one or two,
then

$$\boxed{E_G(D_i,S_j)=\varnothing}.\tag{8}$$

At distance one, each $x\in D_i$ is adjacent to one endpoint
$y\in D_j$. Since $y$ is adjacent to every vertex of $S_j$, an
additional original edge from $x$ to $S_j$ would create a triangle.

At distance two, lifting a base path gives an original path
$x,z,y$ with $x\in D_i$, $z\in D_k$, $y\in D_j$, where the three
base indices are distinct. If $x$ were adjacent to $s\in S_j$,
then $x,y$ would have the two distinct common neighbors $z,s$.
They are nonmate heavy endpoints, so $B_{xy}=0$ and the actual
common-neighbor identity allows at most one common neighbor. This
proves (8).

Suppose additionally that $F$ has diameter at most two, meaning that
every distinct pair of base vertices is joined by a path of length
at most two. Then the only original edges from $D$ into
$S=\bigcup_i S_i$ are the six edges between each $D_i$ and its own
$S_i$. If $W=V(G)\setminus(D\cup S)$, degree counting gives

$$\boxed{|E_G(D,W)|=10d-4m}.\tag{9}$$

Indeed the degree sum on $D$ is $16d$, original edges within $D$
consume $4m$, and original edges from $D$ to $S$ consume $6d$.

There is a further conditional consequence when $d=9$. Each generated
triangle has three distinct external unit repeat ports. In the
normalized D1 rows these are $4,b,c$; port $4$ is originally adjacent
to one heavy endpoint and port $b$ to the other. No port is heavy,
by the established absence of repeat edges from $D$ to $S$.
Under the diameter-two assumption, (8) prevents $4,b$ from belonging
to another generated triangle. They lie outside their own generated
triangle by construction. Thus both lie in $W$.

Let $e_B(S,W)$ count positive repeat edges between these sets; all
have weight one. The two ports just identified give $e_B(S,W)\ge18$.
There are exactly $3d=27$ external repeat incidences from $S$.
Every repeat edge between distinct generated triangles uses two of
them, so $e_B(S,W)$ is odd. Therefore

$$e_B(S,W)\ge19.$$

Here $|W|=62-5d=17$, and the heavy unit mates give exactly $2d=18$
repeat edges between $D$ and $W$. Summing the repeat rows on $W$
therefore yields

$$2e_B(W)+18+e_B(S,W)=3\cdot17=51,$$

where $e_B(W)$ counts unordered repeat edges inside $W$. These are
unit edges because $W$ contains no heavy endpoint. Consequently

$$\boxed{e_B(W)\le7\quad\text{if }d=9\text{ and }\operatorname{diam}(F)\le2}.
\tag{10}$$

Equations (9)--(10) are conditional statements; no diameter bound for
the unknown base graph $F$ has been proved here. Original edges in
(8)--(9) and repeat edges in (10) are different relations.

## Remaining scope

The heavy-mate symmetry and the extremal exclusions are new necessary
conditions. They neither force a particular heavy-pair quotient nor
exclude the current values of $d$. The heavy-port multigraph in
`CONNECTED_REPEAT_HEAVY_PORT_CLOSURE.md` records unit-mate incidence
and is a different graph from the simple original-adjacency quotient
$F$ used here; no identification between them has been assumed.

The sign conditions on short base cycles, the reciprocal adjacency
identity (3), the conditional separation bounds, and the remaining
non-extremal cases may constrain their interaction further, but no
such completion is asserted. No search,
solver, or new formal axiom is used. Independent review of the present
paper is outstanding.
