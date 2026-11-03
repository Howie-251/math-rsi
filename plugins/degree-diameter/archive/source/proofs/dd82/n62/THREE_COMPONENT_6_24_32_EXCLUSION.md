# Parent-pair cycles exclude the three-component quotient of sizes 6, 24, 32

## Claim

No actual legal order-62 graph has three repeat-support components
$H,K,L$ with sizes $6,24,32$ and original-graph component quotient

$$
R=\begin{pmatrix}
0&8&0\\
2&2&4\\
0&3&5
\end{pmatrix}.
\tag{1}
$$

The order of rows and columns is $H,K,L$; $r_{CD}$ counts neighbors
in $D$ of each vertex in $C$. The proof in fact needs only the first
row, the first two entries of the second row, and $|K|\ne6$.

## Status

**PROVABLE AS STATED.** New paper proof awaiting independent review.
This excludes one actual-graph quotient. It neither certifies the
exhaustiveness of the separate three-component enumeration nor excludes
the other quotient possibilities or all order-62 graphs.

## Assumptions and notation

Let $G$ be an actual finite simple graph of order $62$, maximum degree
eight, and diameter at most two. Use the established regularity and
repeat identities

$$
A\mathbf1=8\mathbf1,\qquad B=A^2+A-7I-J,
\qquad B\mathbf1=3\mathbf1,
$$

where $B$ is nonnegative, symmetric, integral, and zero on the diagonal.
For distinct vertices $u,v$,

$$c_G(u,v)+A_{uv}=1+B_{uv}.\tag{2}$$

Components mean components of the positive support of $B$. Their
equitability for $A$ is the actual-graph result in
`GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`, Section 3.

Use the triangle-pairing theorem in
`TRIANGLE_PAIRING_SIMPLE_REPEAT_EXCLUSION.md`, Sections 1--4: every
original triangle has a distinct mate triangle, and their six vertices
form a closed connected component of $B$. Indeed each vertex has its
two unit repeat neighbors within its own triangle and one matching unit
repeat neighbor in the other triangle; those entries exhaust its row.
This theorem applies to arbitrary actual repeat matrices and does not
assume that $B$ is simple or use triple-repeat elimination.

For each $v\in K$, define its **parent pair**

$$P(v)=N_G(v)\cap H.$$

By (1), $|P(v)|=2$, $G[H]$ is independent, every neighbor of a vertex
of $H$ lies in $K$, and every vertex of $G[K]$ has degree two.

## Proof strategy and dependency map

1. The exact cross-component common-neighbor identity makes the parent
   pairs of each $K$-vertex and its two $K$-neighbors partition $H$.
2. The repeat row sum on the six-point independent component supplies
   a parent pair represented by exactly one vertex of $K$.
3. Following three consecutive edges inside the degree-two graph
   $G[K]$ forces that uniquely represented pair to return after three
   steps. Thus $G[K]$ contains an original triangle.
4. Triangle pairing puts that triangle in a six-vertex repeat component,
   contradicting the size of $K$.

No small-component classification, D1 minimum-size theorem, double-edge
count, or finite enumeration is required.

## Proof

### 1. Three parent pairs partition the six-point component

Fix $v\in K$, and let $v_-,v_+$ be its two distinct neighbors in
$G[K]$. For each $h\in H$, the components are distinct, so $B_{hv}=0$.
Moreover $N_G(h)\subseteq K$. Consequently (2) gives

$$
\mathbf1_{h\in P(v_-)}+\mathbf1_{h\in P(v_+)}
=c_G(h,v)=1-\mathbf1_{h\in P(v)}.
\tag{3}
$$

Thus a vertex $h$ of $P(v)$ lies in neither neighboring parent pair,
and every other vertex of $H$ lies in exactly one of those two pairs.
It follows that

$$P(v),\ P(v_-),\ P(v_+)\text{ are a disjoint partition of }H.\tag{4}$$

### 2. At least one parent pair occurs exactly once

Choose any $h_1\in H$. Its repeat row has total weight three and
is supported inside $H\setminus\{h_1\}$, a set of size five. Since
the entries are nonnegative integers, at least one $h_2$ in that set
satisfies $B_{h_1h_2}=0$.

The two vertices are nonadjacent because $G[H]$ is independent.
Equation (2) says they have exactly one common neighbor, denoted $v_0$.
Every common neighbor lies in $K$, since all neighbors of $h_1$ lie
there. As each vertex of $K$ has exactly two $H$-neighbors, this proves

$$
P(v_0)=\{h_1,h_2\},\qquad
P(v)=P(v_0)\text{ for }v\in K\Longrightarrow v=v_0.
\tag{5}
$$

### 3. The uniquely represented pair forces a triangle

Choose a $K$-neighbor $v_1$ of $v_0$. Let $v_2$ be the other
$K$-neighbor of $v_1$, so $v_2\ne v_0$. The three vertices
$v_0,v_1,v_2$ are distinct, and (4) at $v_1$ gives

$$P(v_0)\sqcup P(v_1)\sqcup P(v_2)=H.$$

Let $v_3$ be the other $K$-neighbor of $v_2$, distinct from $v_1$.
Applying (4) at $v_2$ gives

$$P(v_1)\sqcup P(v_2)\sqcup P(v_3)=H.$$

Taking the complement of $P(v_1)\cup P(v_2)$ in these two
partitions yields $P(v_3)=P(v_0)$. By (5), $v_3=v_0$. Hence

$$v_0v_1,\quad v_1v_2,\quad v_2v_0\in E(G),$$

and the three distinct vertices form an original triangle entirely
inside $K$.

### 4. The repeat component cannot have size twenty-four

The triangle-pairing theorem puts this original triangle in a closed
connected six-vertex repeat component. Since one of its vertices lies
in the component $K$, that six-vertex component must equal $K$.
This contradicts $|K|=24$, proving the claim.

## Structural interpretation and scope

Equation (4) also means that the parent-pair labels repeat with period
three along each cycle of the degree-two graph $G[K]$. A uniquely
represented pair therefore forces a cycle of length three. The proof
uses only the local length-three walk and does not require enumerating
those cycles.

The six-vertex repeat component need not be classified as a triangular
prism or $K_{3,3}$ for this exclusion. In particular, simplicity of its
repeat matrix, exclusion of D0 components, and the new D1 minimum size
fourteen are unnecessary dependencies. The triangle-pairing component
has original internal degree two; it is a separate consequence of an
original triangle, not an assumption that all unit repeat triangles are
generated or that $G$ is triangle-free.

The diagnostic
`computations/dd82/n62/three_component_quotients.py` and its JSON output
motivated the candidate (1). This proof assumes that specific actual
quotient and does not use the diagnostic's enumeration as a proof step.
The other three-component quotients remain outside the scope of this
paper. Independent review of the new exclusion is outstanding.
