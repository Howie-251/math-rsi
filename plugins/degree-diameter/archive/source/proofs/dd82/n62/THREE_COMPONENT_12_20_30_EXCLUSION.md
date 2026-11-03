# The component quotient on 12, 20, and 30 vertices is impossible

## Claim

An actual 62-vertex graph of maximum degree eight and diameter at most two
cannot have exactly three components of the positive support of its repeat
matrix, of sizes $(12,20,30)$ and original-graph quotient

$$R=\begin{pmatrix}3&0&5\\0&2&6\\2&4&2\end{pmatrix}.$$

This is a conditional exclusion of this specific quotient. It does not
establish that the separate finite enumeration of three-component
quotients is exhaustive, exclude a one-component repeat matrix, or settle
the order-62 problem.

## Status

**PROVABLE AS STATED:** new paper proof, awaiting independent review.
No numerical eigenvalue calculation, graph enumeration, or solver result
is used in the proof.

## Assumptions and notation

Let $A$ be the adjacency matrix of the actual graph and

$$B=A^2+A-7I-J.$$

Use the established order-62 reductions: $A$ is eight-regular; $B$ is
nonnegative, symmetric, has zero diagonal and row sum three; $AB=BA$;
all repeat entries are at most two; every double repeat is either D0 or
D1. A D0 double belongs to a closed four-vertex component. A D1 double
has its heavy component of size at least fourteen. An original triangle
belongs to a closed six-vertex repeat component by triangle pairing.

The heavy-component lower bound uses the chain ending in
`D1_TWELVE_SIXTEEN_PARTNER_EXCLUSION.md`, together with the other
size-twelve exclusions cited there. Component equitability and the
matrix conventions are those of `GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`.

Assume for contradiction the displayed quotient. Denote its components
by $C,D,E$, of sizes $12,20,30$, respectively. Put

$$P=A[C,C],\qquad Z=A[E,E],\qquad X=A[C,E],\qquad B_C=B[C,C].$$

Thus $P$ is the adjacency matrix of a cubic simple graph on twelve
vertices, $Z$ is the adjacency matrix of a two-regular simple graph,
and $X$ is a zero-one matrix with row sum five and column sum two.

## Proof strategy and dependency map

1. The component sizes exclude original triangles and double repeats
   inside $C$, so $P$ is connected and triangle-free and $B_C$ is the
   adjacency matrix of a connected cubic simple graph.
2. Regard the columns of $X$ as edges of a weighted graph on $C$.
   Commutation and a trace inequality force this auxiliary graph to be
   connected.
3. Its unsigned incidence matrix then has a kernel of dimension at most
   one. The cross-block graph identity forces every nonprincipal
   eigenvalue of $P$ to be at most one, including the possible kernel
   direction.
4. An exact trace-polynomial identity rules out such a triangle-free
   cubic graph on twelve vertices.

## Proof

### 1. The internal graph on twelve vertices is connected

There is no component of size six, so triangle pairing shows that the
whole original graph is triangle-free. There is no component of size
four, so no double repeat is of type D0. A double repeat inside $C$
would therefore be D1, contrary to the heavy-component lower bound
$|C|=12<14$. Consequently $B_C$ is a zero-one matrix. By its definition
as a whole repeat component, it is connected and has row sum three.

For distinct $u,v\in C$, the actual common-neighbor identity gives

$$|N_G(u)\cap N_G(v)|+A_{uv}=1+(B_C)_{uv}\le2. \tag{1}$$

In particular, the graph with adjacency matrix $P$ has no two vertices
with three common neighbors. Each connected component of a simple
cubic graph has even order at least four. A four-vertex cubic graph is
$K_4$, which has triangles. A triangle-free cubic graph on six vertices
must be $K_{3,3}$: if $v$ has independent neighbors $a,b,c$, each of
$a,b,c$ must be joined to both remaining vertices, exhausting all
degrees. The resulting graph has two vertices with three common
neighbors, contrary to (1). Thus every component of $P$ has at least
eight vertices. Since $P$ has twelve vertices, it is connected.

### 2. The auxiliary weighted graph from the columns of $X$

Every column of $X$ has two distinct ones and hence specifies an
unordered pair of vertices of $C$. Let $F$ be the loopless weighted
graph in which a pair's weight is its multiplicity among these thirty
columns. Its adjacency matrix is

$$W=XX^T-5I. \tag{2}$$

Indeed the diagonal of $XX^T$ is five and its off-diagonal entries count
the specified pairs. The matrix $W$ is symmetric and nonnegative with
zero diagonal and row sum five.

Since $A[C,D]=0$, the $C,C$ block of the actual graph identity is

$$P^2+P+XX^T=7I+J+B_C.$$

Substituting (2) gives

$$W=2I+J+B_C-P^2-P. \tag{3}$$

The $C,C$ block of $AB=BA$ gives $PB_C=B_CP$, because $B$ has no
entries between distinct components. Both $P$ and $B_C$ are regular,
so both commute with $J$. Equation (3) therefore shows that $W$
commutes with both $P$ and $B_C$.

We claim that $F$ is connected. Suppose instead that it has $q>1$
components. Let $U$ be the space of vectors constant on each of those
components. For a nonnegative symmetric matrix of row sum five,
its eigenspace at five is exactly this space. Explicitly,

$$f^T(5I-W)f=\frac12\sum_{u,v}W_{uv}(f_u-f_v)^2.$$

Thus $U=\ker(W-5I)$, and commutation makes $U$ invariant under both
$P$ and $B_C$. In particular the partition into $F$-components is
equitable for $B_C$. Let $S$ be the corresponding quotient matrix of
$B_C$. It has integer entries and row sum three. Since $B_C$ is
connected and $q>1$, every part has an edge to another part. Its
constant number of external neighbors is at least one, so every
diagonal entry of $S$ is at most two. Hence

$$\operatorname{tr}S\le2q. \tag{4}$$

On $U\cap\mathbf1^\perp$, equation (3) becomes

$$B_C=P^2+P+3I, \tag{5}$$

because $W=5I$ there and $J=0$. The restriction of the real symmetric
matrix $P$ to this invariant space has real eigenvalues $\lambda$.
For an eigenvector with eigenvalue $\lambda$, (5) gives the
$B_C$-eigenvalue

$$\lambda^2+\lambda+3
  =\left(\lambda+\frac12\right)^2+\frac{11}{4}
  \ge\frac{11}{4}.$$

On the remaining constant direction, $B_C$ has eigenvalue three.
The trace of $S$ is the trace of $B_C|_U$, since the component
indicators are a basis of $U$. Consequently

$$\operatorname{tr}S\ge3+\frac{11}{4}(q-1)>2q,$$

where the last difference is $(3q+1)/4>0$. This contradicts (4),
and proves that $F$ is connected.

### 3. Every nonprincipal eigenvalue of $P$ is at most one

The $C,E$ block of the graph identity, using $A[C,D]=0$ and
$B[C,E]=0$, is

$$PX+XZ+X=J_{12\times30}. \tag{6}$$

Let $v$ be a $P$-eigenvector orthogonal to the all-ones vector, and
write $Pv=\lambda v$. Transposing (6) and applying it to $v$ gives

$$ZX^Tv=-(\lambda+1)X^Tv. \tag{7}$$

If $X^Tv\ne0$, the fact that $Z$ is symmetric of row sum two implies
that its eigenvalues lie in $[-2,2]$. Equation (7) therefore gives

$$-3\le\lambda\le1. \tag{8}$$

It remains to treat $\ker X^T$. For an edge column corresponding to
$\{u,v\}$, the corresponding coordinate of $X^Tf$ is $f_u+f_v$.
Since $F$ is connected, these equations imply either that the kernel
is zero, or that $F$ is bipartite and the kernel is spanned by its
sign vector $f$, taking values $+1$ and $-1$ on the two parts.

In the latter case, the two parts have equal size: weighted degree
counting in the five-regular graph gives five times each part size
as the total weight across the bipartition. Thus $f\perp\mathbf1$.
The transpose of (6) shows that $X^TPf=0$, so the one-dimensional
kernel is invariant under $P$. Write $Pf=\lambda f$. Each row of
$P$ sums three signs, and division by its own sign shows that

$$\lambda\in\{-3,-1,1,3\}.$$

The possibility $\lambda=3$ is excluded because $P$ is connected:
its eigenspace at its degree three consists only of constant vectors,
whereas $f$ is a nonconstant sign vector. The kernel direction
therefore also has eigenvalue at most one.

Together with (8), this proves that the eleven nonprincipal
eigenvalues of $P$ all belong to $[-3,1]$.

### 4. A trace-polynomial contradiction on twelve vertices

Let the eigenvalues of $P$ be $3,\lambda_2,\ldots,\lambda_{12}$.
The graph is simple, cubic, and triangle-free, so

$$\operatorname{tr}P=0,\qquad
  \operatorname{tr}P^2=36,\qquad
  \operatorname{tr}P^3=0.$$

For

$$p(t)=(t-1)(t+3)^2=t^3+5t^2+3t-9,$$

these identities give

$$\operatorname{tr}p(P)=0+5\cdot36+0-9\cdot12=72=p(3).$$

Hence

$$\sum_{i=2}^{12}(\lambda_i-1)(\lambda_i+3)^2=0. \tag{9}$$

Every term in (9) is nonpositive because $\lambda_i\in[-3,1]$.
Each must therefore vanish, so every $\lambda_i$ is either one or
minus three. If $b$ of them are minus three, the other $11-b$ are
one. The zero trace of $P$ would give

$$0=3+(11-b)-3b=14-4b,$$

which requires the noninteger value $b=7/2$. This contradiction
excludes the displayed component quotient. $\square$

## Open risks and remaining scope

The argument needs the established heavy-component lower bound to
exclude double repeats inside $C$, and triangle pairing to establish
triangle-freeness. It does not replace either proof. It supplies no
classification of larger heavy components or of a connected repeat
matrix. Its mathematical proof and dependency use still require an
independent review before being promoted to a reviewed research result.
