# Weighted parent coverage excludes the quotient of sizes 8, 24, 30

## Claim

No actual legal order-62 graph has repeat-support components $C,K,L$
with sizes $8,24,30$ and original-graph component quotient

$$R=\begin{pmatrix}2&6&0\\2&1&5\\0&4&4\end{pmatrix}.\tag{1}$$

The order of rows and columns is $C,K,L$; $r_{UV}$ counts original
neighbors in $V$ of each vertex of $U$.

## Status

**PROVABLE AS STATED.** New paper proof awaiting independent review.
It completes the previously partial argument in
`THREE_COMPONENT_8_24_30_REDUCTION.md`; the spectral classification and
the proposed simplicity of $B[K]$ from that note are not dependencies
of this shorter proof.

This excludes the specified actual quotient. It does not certify the
separate quotient enumeration or exclude all order-62 graphs.

## Assumptions and dependencies

Use the actual order-62 identities

$$
A\mathbf1=8\mathbf1,\qquad B=A^2+A-7I-J,\qquad
B\mathbf1=3\mathbf1,\qquad AB=BA,
\tag{2}
$$

where $B$ is nonnegative, symmetric, integral, and zero on the diagonal.
For distinct vertices,

$$c_G(u,v)+A_{uv}=1+B_{uv}.\tag{3}$$

Components mean components of the positive support of $B$. Their
equitability for $A$ is proved in `GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`,
Section 3. Use two additional established consequences of the actual
graph reductions:

1. Every original triangle belongs to a closed six-vertex repeat
   component, by `TRIANGLE_PAIRING_SIMPLE_REPEAT_EXCLUSION.md`,
   Sections 1--4.
2. Repeat entries three are excluded. Every double edge is D0 or D1;
   a D0 heavy component has size four. For a D1 heavy component $H$
   and its generated-triangle component $J$, Section 4 of
   `GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md` gives $r_{HH}\ge4$ if $H=J$,
   and $r_{HJ}\ge4$, $r_{JH}\ge3$ if $H\ne J$.

Since none of the component sizes in (1) is six, the first consequence
makes $G$ triangle-free in this quotient case. Thus $B_{uv}=0$ on every
original edge. The second consequence makes $B[C]$ simple. A double
edge in $C$ cannot be D0, since $|C|=8\ne4$. If it were D1, its
generated-triangle component would be one of $C,K,L$. These choices
respectively contradict $r_{CC}=2<4$, $r_{KC}=2<3$, and $r_{CL}=0<4$.
Thus no double edge lies in $C$. No D1 minimum-size lemma is needed.

## Notation

Let $D=A[C]$ and $X=A[C,K]$. Since $r_{KK}=1$, $G[K]$ is a perfect
matching. Write $p(v)$ for the original matching partner of $v\in K$,
and $P=A[K]$ for its matching matrix. Each $v\in K$ has the parent pair

$$F(v)=N_G(v)\cap C,\qquad |F(v)|=2.$$

## Proof strategy and dependency map

The actual cross-block identity rules out an eight-cycle in $G[C]$.
In the remaining two-four-cycle case, it makes matching partners in
$K$ have simultaneously opposite parent pairs. Simplicity and
connectedness of $B[C]$ then fix the repeat weights required at the
opposites of a zero-repeat parent pair. Commutation requires repeat
weight two covering each opposite vertex. Their only possible common
representative has repeat weight zero, contradicting the total row
budget three.

## Proof

### 1. Closed parent neighborhoods and the original matching

There are no original $C$--$L$ edges and no repeat $C$--$K$ edges.
The $(C,K)$ block of the actual matrix identity is therefore

$$DX+XP+X=J.\tag{4}$$

For a fixed $v\in K$, equation (4) says that the closed
$G[C]$-neighborhoods of the two vertices of $F(v)$ are disjoint,
and that their complement in $C$ is exactly $F(p(v))$.

Since $G[C]$ is two-regular, triangle-free, and has eight vertices,
it is either an eight-cycle or two four-cycles. Suppose it is an
eight-cycle. The two parents of $v$ must have cyclic distance three
or four for their closed neighborhoods to be disjoint. At distance
three, the complementary parent pair $F(p(v))$ consists of adjacent
vertices, creating an original triangle with $p(v)$. Hence all parent
pairs would be antipodal. Every one of the six $K$-neighbors of a
vertex $c\in C$ would also neighbor its antipode $c'$, giving
$c_G(c,c')\ge6$. However, the nonadjacent pair satisfies
$c_G(c,c')=1+B_{cc'}\le4$ by the repeat row sum. This contradiction
excludes the eight-cycle.

Thus $G[C]$ consists of two four-cycles. Label their vertices
$a_0,a_1,a_2,a_3$ and $b_0,b_1,b_2,b_3$ in cyclic order, with indices
modulo four. Write $o(a_i)=a_{i+2}$ and $o(b_j)=b_{j+2}$.

### 2. Parent pairs and the cross-repeat matrix

No two closed neighborhoods in a four-cycle are disjoint. Therefore
every parent pair has the form $\{a_i,b_j\}$, and (4) gives

$$F(p(v))=\{o(a_i),o(b_j)\}
\quad\text{when }F(v)=\{a_i,b_j\}.\tag{5}$$

Two adjacent vertices within one four-cycle have no common neighbors:
they have none inside $C$, no $K$-vertex has both as parents, and they
have no neighbors in $L$. Their repeat entry is zero. Two opposite
vertices have exactly their two common neighbors inside that four-cycle,
so their repeat entry is one.

Let

$$M_{ij}=B_{a_i b_j},\qquad
m_{ij}=|\{v\in K:F(v)=\{a_i,b_j\}\}|.$$

Simplicity of $B[C]$ makes $M$ binary. The opposite repeat edge already
uses one unit in each row, so every row and every column of $M$ has
sum two. Counting common neighbors of $a_i,b_j$ gives

$$m_{ij}=1+M_{ij}.\tag{6}$$

The matching bijection (5) implies $m_{i+2,j+2}=m_{ij}$, and hence

$$M_{i+2,j+2}=M_{ij}.\tag{7}$$

Each row of $M$ contains one one in each opposite pair of columns.
For otherwise its two ones occur at $j,j+2$. Equation (7) gives those
same two ones in row $i+2$. The vertices
$a_i,a_{i+2},b_j,b_{j+2}$ then induce a unit $K_4$ in $B$: the two
opposite repeat edges and all four cross entries have weight one.
Their repeat rows are exhausted, making this a closed four-vertex
component, contrary to the size and connectedness of $C$.

Interchanging the two four-cycles proves that every column also has
one one in each opposite pair of rows. Consequently,

$$M_{i,j+2}=1-M_{ij},\qquad
M_{i+2,j}=1-M_{ij}.\tag{8}$$

### 3. A zero cross-repeat entry requires four units from a row of sum three

Every row of $M$ has two zeros. Choose $i,j$ with $M_{ij}=0$.
By (6), there is exactly one $v\in K$ with

$$F(v)=\{a_i,b_j\}.$$

Equations (6)--(7) also say that the opposite parent pair
$\{o(a_i),o(b_j)\}$ occurs exactly once. By (5), its unique
representative is $p(v)$. Since $v,p(v)$ form an original edge in the
triangle-free graph,

$$B_{v,p(v)}=0.\tag{9}$$

Commutation on the $(C,K)$ block, using block diagonality of $B$,
gives

$$B[C]X=XB[K].\tag{10}$$

Define two sets of $K$-vertices by

$$U=\{w\in K:o(a_i)\in F(w)\},\qquad
V=\{w\in K:o(b_j)\in F(w)\}.$$

The $(o(a_i),v)$ entry of (10), the opposite repeat edge, and (8)
give

$$
\sum_{w\in U}B_{vw}
=B_{o(a_i),a_i}+B_{o(a_i),b_j}
=1+M_{i+2,j}=2.
\tag{11}
$$

At $(o(b_j),v)$, the same identity gives

$$
\sum_{w\in V}B_{vw}
=B_{o(b_j),a_i}+B_{o(b_j),b_j}
=M_{i,j+2}+1=2.
\tag{12}
$$

A vertex belongs to $U\cap V$ precisely when its parent pair is
$\{o(a_i),o(b_j)\}$. We have proved that
$U\cap V=\{p(v)\}$, whose repeat weight from $v$ is zero by (9).
Weighted inclusion-exclusion now gives

$$
4=\sum_{w\in U}B_{vw}+\sum_{w\in V}B_{vw}
=\sum_{w\in U\cup V}B_{vw}+B_{v,p(v)}
\le\sum_{w\in K}B_{vw}=3.
$$

The final equality holds because $K$ is the repeat component containing
$v$. This contradiction proves the claim.

## Scope and remaining dependencies

The contradiction uses the actual weighted repeat rows; it makes no
assumption that $B[K]$ is simple. No spectral classification, finite
case enumeration, SAT or LP computation, or graph-realizability claim
is used. The proof needs only the global D1 incidence bounds, not a
D1 minimum-size lemma.

The source chain for triangle pairing, triple-repeat exclusion, D0/D1
coverage, and the global D1 incidence bounds remains explicit above. The
three-component quotient diagnostic is only the motivation for (1)
and is not a proof step. Other quotients and other component counts
remain outside this paper. Independent review of the new exclusion
is outstanding.
