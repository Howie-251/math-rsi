# A forced eight-point repeat structure in the quotient of sizes 8, 24, 30

## Claim and status

**PROVABLE AS STATED: the structural reduction below.** The full exclusion
of this quotient is **NOT CURRENTLY JUSTIFIED**. This new paper note
awaits independent review.

Suppose an actual legal order-62 graph has repeat-support components
$C,K,L$ with sizes $8,24,30$ and original-graph quotient

$$R=\begin{pmatrix}2&6&0\\2&1&5\\0&4&4\end{pmatrix}.\tag{1}$$

Then $G[C]$ consists of two four-cycles. With the notation below,
$B[C]$ has a specified eight-vertex simple cubic structure, and $B[K]$
has no double entries. Thus every double repeat lies in $L$. These facts
do not yet exclude a D1 heavy edge in $L$ whose generated triangle lies
in $K$ or in $L$.

## Assumptions and dependencies

Use the actual order-62 identities

$$A\mathbf1=8\mathbf1,\qquad B=A^2+A-7I-J,\qquad
B\mathbf1=3\mathbf1,\qquad AB=BA,$$

with $B$ nonnegative, integral, symmetric, and zero on the diagonal.
For distinct vertices, $c_G(u,v)+A_{uv}=1+B_{uv}$.

Use component equitability from `GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`.
Use the established triple-repeat exclusion and the D0/D1 classification
of double edges. A D0 heavy component has size four; every D1 heavy
component has size at least fourteen, conditional on the source chain
ending in `D1_TWELVE_SIXTEEN_PARTNER_EXCLUSION.md`. Therefore the
eight-vertex component $C$ has only unit repeat entries.

The triangle-pairing theorem in
`TRIANGLE_PAIRING_SIMPLE_REPEAT_EXCLUSION.md` puts every original
triangle in a closed six-vertex repeat component. None of the three
components in (1) has size six. Thus $G$ is triangle-free in this
specific quotient case. In particular $B_{uv}=0$ on every original
edge. This is a derived property of (1), not an all-vertex assumption
made for arbitrary order-62 graphs.

## Strategy

The actual cross-block identity fixes how the two $C$-parents of a
$K$-vertex transform under its unique original neighbor in $K$. This
rules out an eight-cycle in $G[C]$ and sharply restricts $B[C]$ in the
two-four-cycle case. A norm identity rules out one of the two resulting
sign-matrix possibilities. Finally, commutation transports the small
repeat rows to $K$ and excludes every double entry there.

## 1. Parent pairs and the original matching in $K$

By (1), $G[K]$ is a perfect matching. Write $p(v)$ for the original
matching partner of $v\in K$, and put

$$P(v)=N_G(v)\cap C,\qquad |P(v)|=2.$$

Let $D=A[C]$, let $X=A[C,K]$, and let $P=A[K]$ also denote the
matching matrix when used in matrix expressions. The $(C,K)$ block
of the actual identity is

$$DX+XP+X=J.\tag{2}$$

Indeed there are no original $C$--$L$ edges and no repeat $C$--$K$
edges. For a fixed $v\in K$, equation (2) says that the closed
$G[C]$-neighborhoods of its two parents are disjoint and that their
complement in $C$ is exactly $P(p(v))$.

## 2. The original induced graph on $C$ cannot be an eight-cycle

The graph $G[C]$ is two-regular and triangle-free. Since it has eight
vertices, it is either an eight-cycle or two four-cycles.

Suppose it is an eight-cycle. Disjoint closed neighborhoods require
the two parents of each $v\in K$ to have cyclic distance three or
four. At distance three, the two complementary vertices are adjacent
on the eight-cycle. They would both neighbor $p(v)$ and form an
original triangle with it. This is impossible.

Thus every parent pair is antipodal. Every one of the six $K$-neighbors
of a given $c\in C$ also neighbors its antipode $c'$. The pair $c,c'$
therefore has at least six common neighbors. But it is nonadjacent,
so the repeat identity gives $c_G(c,c')=1+B_{cc'}\le4$, since a repeat
row has sum three. This is a contradiction.

Hence $G[C]$ consists of two four-cycles. Label their vertices
$a_0,a_1,a_2,a_3$ and $b_0,b_1,b_2,b_3$ in cyclic order, with indices
modulo four. Write $o(a_i)=a_{i+2}$ and $o(b_j)=b_{j+2}$ for opposite
vertices.

## 3. The cross-repeat matrix on the two four-cycles

No two closed neighborhoods in one four-cycle are disjoint. Equation
(2) therefore makes every parent pair have the form $\{a_i,b_j\}$,
and

$$P(p(v))=\{o(a_i),o(b_j)\}\quad
\text{if }P(v)=\{a_i,b_j\}.\tag{3}$$

Two adjacent vertices in the same four-cycle have no common neighbor:
they have none in that four-cycle, no $K$-vertex has both as parents,
and they have no neighbors in $L$. Their repeat entry is zero. Two
opposite vertices have exactly their two common neighbors within the
four-cycle, so their repeat entry is one.

Let $M_{ij}=B_{a_i b_j}$. Since $B[C]$ is simple, $M$ is a binary
$4\times4$ matrix; every row and every column has sum two. If $m_{ij}$
counts the $K$-vertices with parent pair $\{a_i,b_j\}$, the exact
common-neighbor identity gives

$$m_{ij}=1+M_{ij}.\tag{4}$$

The partner bijection (3) implies

$$M_{i+2,j+2}=M_{ij}.\tag{5}$$

Each row of $M$ selects one vertex from each opposite pair of columns.
For otherwise its two ones occur at $b_j,b_{j+2}$. Equation (5) then
gives the same two ones in row $a_{i+2}$. Together with the two opposite
repeat edges, these four vertices form a closed unit $K_4$ in $B$,
contradicting connectedness of the eight-vertex repeat component.
The corresponding statement holds for every column, by the same
argument with the two four-cycles exchanged.

On vectors antisymmetric at opposite vertices, encode $M$ by the
$2\times2$ sign matrix

$$T_{ij}=M_{ij}-M_{i,j+2}\in\{-1,1\},\qquad i,j\in\{0,1\}.$$

The restriction of $B[C]$ to this four-dimensional subspace is

$$\begin{pmatrix}-I_2&T\\T^T&-I_2\end{pmatrix}.\tag{6}$$

The only determinant possibilities are $\det T=0$ or $|\det T|=2$.

## 4. The rank-one sign matrix is impossible

Suppose $\det T=0$. We can write $T=uv^T$ with both $u,v$ having
two entries in $\{-1,1\}$. In (6), the vector with coordinates
$(u,-v)$ has eigenvalue $-3$. Expanded to opposite-antisymmetric
coordinates on $C$, and extended by zero outside $C$, it gives a
vector $f$ with

$$Bf=-3f,\qquad f|_C\in\{-1,1\}^{8},\qquad
\mathbf1^Tf=0,\qquad \|f\|^2=8.$$

On opposite-antisymmetric vectors, the adjacency matrix of each
four-cycle is zero. Thus $A[C]f=0$. There are no $C$--$L$ edges,
so $Af$ is supported entirely on $K$. Commutation gives
$B(Af)=-3Af$.

For a connected nonnegative symmetric repeat matrix of row sum three,
its $-3$ eigenspace is zero if its support is not bipartite, and otherwise
is spanned by the vector with signs $+1,-1$ on its two parts. This is
the equality case of

$$g^T(3I+B)g=\frac12\sum_{x,y}B_{xy}(g_x+g_y)^2,$$

as also proved in Section 6 of `GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`.
Consequently the integral vector $Af|_K$ is either zero or an integer
multiple $q$ of such a sign vector. In either case

$$\|Af\|^2=24q^2\quad\text{for some }q\in\mathbb Z.\tag{7}$$

On the other hand, the actual matrix identity and $\mathbf1^Tf=0$
give $(A^2+A)f=4f$. Taking its inner product with $f$, and using the
disjoint supports of $f$ and $Af$, yields

$$\|Af\|^2=4\|f\|^2=32.$$

This contradicts (7). Thus $|\det T|=2$.

After permuting opposite pairs and exchanging the vertices within
them, the remaining sign matrix and cross-repeat matrix may be taken as

$$
T=\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad
M=\begin{pmatrix}
1&1&0&0\\
1&0&0&1\\
0&0&1&1\\
0&1&1&0
\end{pmatrix}.
\tag{8}
$$

The within-four-cycle repeat entries are still exactly the two
opposite matchings. Formula (8) specifies $B[C]$ completely up to
the stated relabeling.

## 5. There are no double repeat entries inside $K$

Because $B$ is block diagonal on its support components, commutation
on the $(C,K)$ block gives

$$B[C]X=XB[K].\tag{9}$$

For $v\in K$ with parents $a_i,b_j$, its right-hand side means that
the weighted parent coverage of all repeat neighbors of $v$ is the
vector $B[C]\mathbf1_{\{a_i,b_j\}}$.

If $M_{ij}=1$, this coverage vector has no coordinate exceeding one.
To check this, its coordinates at $a_i,b_j$ are one; those at their
opposites are one, because the opposite entry in that row or column of
$M$ is zero; every other coordinate is a single binary $M$ entry.
A double repeat neighbor would contribute two at each of its two
parents, which is impossible. Thus $v$ has no double repeat.

If $M_{ij}=0$, the coverage vector has value two exactly at
$o(a_i),o(b_j)$, value zero at $a_i,b_j$, and values at most one
everywhere else. Hence any putative double repeat mate of $v$ must
have parent pair $\{o(a_i),o(b_j)\}$. By (4)--(5), that label occurs
exactly once. By (3), its unique vertex is $p(v)$, the original matching
partner of $v$. But $B_{v,p(v)}=0$, since $G$ is triangle-free. This
also rules out a double repeat at $v$.

All repeat neighbors of a vertex of $K$ lie in $K$. We have therefore
proved that $B[K]$ is simple. With simplicity already established for
$B[C]$, every double repeat of $B$ lies in $L$.

## 6. Remaining exact incidence structure and obstruction

There are sixteen parent-pair labels $\{a_i,b_j\}$. The eight positions
where $M_{ij}=1$ each have two representatives in $K$; the other eight
positions each have one, totaling $24$ vertices. Their original perfect
matching maps every label to its simultaneous opposite label.

Write $Y=A[K,L]$. Every $K$-vertex has five $L$-neighbors, and every
$L$-vertex has four $K$-neighbors. The $(C,L)$ block of the actual
identity gives

$$XY=J_{8\times30}.\tag{10}$$

Thus the parent pairs of the four $K$-neighbors of each $L$-vertex form
a perfect matching on the eight vertices of $C$. The $(K,L)$ block is

$$PY+YA[L]+Y=J_{24\times30},\tag{11}$$

where $A[L]$ is four-regular. Relations (8)--(11), along with the actual
internal identities, remain necessary constraints.

They do not yet supply a contradiction. In particular, two vertices of
$L$ can share three $K$-neighbors and use distinct representatives of
the same doubled parent-pair label as their fourth neighbors. Therefore
three common $K$-neighbors cannot be promoted to four merely by the
perfect-matching coverage in (10). This is a concrete remaining
possibility, not an assertion that it lifts to a graph.

The D1 component possibilities after this reduction are a heavy edge
in $L$ with its generated triangle in $K$, or both in $L$. No exclusion
of those possibilities is claimed. The separate three-component
enumeration is only diagnostic motivation; this note assumes (1) and
does not certify that enumeration or address other component counts.
