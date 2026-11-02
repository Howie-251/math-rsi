# An internal double-path vertex: exact local template

Date: 2026-10-13. Exploratory parallel derivation, writer-checked; not a
new accepted main workflow or a nonexistence theorem.

## Claim, imports and notation

The necessary structure below is **PROVABLE AS STATED**. A contradiction
from the existence of an internal double-path vertex is **NOT CURRENTLY
JUSTIFIED**.

Let $A$ be the actual adjacency matrix of a simple $8$-regular,
diameter-two graph on $61$ vertices, and let $B=A^2+A-7I-J$. Import the
accepted conclusions that $B$ is symmetric, nonnegative integral, has
zero diagonal and row sum $4$, has entries in $\{0,1,2\}$, and that
$D=\{\{x,y\}:B_{xy}=2\}$ is a path forest. The last import is
[DOUBLE_DEFECT_CYCLE_OBSTRUCTION.md](DOUBLE_DEFECT_CYCLE_OBSTRUCTION.md).
The adjacent-double case remains open, as recorded in
[ADJACENT_DOUBLE_REPEAT_LOCAL.md](ADJACENT_DOUBLE_REPEAT_LOCAL.md).

Assume $u,v,w$ are consecutive vertices of a $D$ path. Thus

$$B_{v*}=2e_u^T+2e_w^T. \tag{1}$$

For distinct vertices write $\mu(x,y)=|N_A(x)\cap N_A(y)|$; throughout,

$$\mu(x,y)=1+B_{xy}-A_{xy},\qquad AB=BA. \tag{2}$$

The proof uses the row budget at $v$, then its complete radius-two
partition and the $(v,x)$ commutation equations. A final lemma derives
coherent adjacency along a whole double path. No auxiliary graphs are
enumerated and no solver is used.

## 1. The two double edges are nonedges of the original graph

If $A_{uv}=1$, equation (2) gives two distinct common neighbours of
$u,v$. Each forms a triangle on $uv$ and hence gives a positive defect
entry in row $v$. Neither common neighbour is $u$ or $v$, whereas (1)
leaves only $w$ as a possible positive-defect endpoint. Two distinct
common neighbours cannot both be $w$. Therefore

$$A_{uv}=A_{vw}=0. \tag{3}$$

Put $T=N_A(v)$, so $|T|=8$. Any edge within $T$ would give a triangle
at $v$, and therefore a positive defect entry from $v$ to a member of
$T$. Equations (1),(3) forbid this. Thus $T$ is independent.

Define

$$U=T\cap N_A(u),\quad W=T\cap N_A(w),\quad r=|U\cap W|.$$

Equation (2) gives $|U|=|W|=3$. If $x,y\in T$ are distinct, their
common neighbour $v$ accounts for the baseline one. The only other
vertices capable of having two neighbours in $T$ are $u,w$: all
other vertices outside $T\cup\{v,u,w\}$ have exactly one by (1),(2).
Consequently, as a weighted matrix with zero diagonal,

$$B[T]=A(K_3[U])+A(K_3[W]). \tag{4}$$

## 2. Six possible endpoint types

Set $\epsilon=A_{uw}$ and $\beta=B_{uw}$. We have $\beta\le1$, since
$\beta=2$ would create a triangle in $D$. The $(v,x)$ entry of $AB=BA$
is the useful exact identity

$$\sum_{t\in T}B_{tx}=2(A_{ux}+A_{wx}). \tag{5}$$

At $x=u,w$ it gives $\sum_{t\in T}B_{tu}=\sum_{t\in T}B_{tw}=2\epsilon$.
If $\epsilon=1$, these two units exhaust each endpoint's remaining
defect budget after its double edge to $v$. In particular $\beta=0$.
Then (2) gives $\mu(u,w)=0$.

Let $Z=V(G)\setminus(\{v,u,w\}\cup T)$, of size $50$, and put
$h=|Z\cap N_A(u)\cap N_A(w)|$. All common neighbours of $u,w$ lie in
$T\cup Z$, whence

$$r+h=1+\beta-\epsilon. \tag{6}$$

Thus every actual graph is in one of the following six necessary types:

| $\epsilon$ | $\beta$ | $r$ | $h$ |
|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 |
| 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 2 |
| 0 | 1 | 1 | 1 |
| 0 | 1 | 2 | 0 |

This table does not assert that every type is realizable.

## 3. Eight parent classes and small exceptional attachment sets

Every $z\in Z$ has exactly one neighbour in $T$. Let $Z_t$ be the
class with parent $t\in T$, and define
$k_t=1_{t\in U}+1_{t\in W}$. Degree eight at $t$ gives

$$|Z_t|=7-k_t. \tag{7}$$

The eight class sizes are therefore $r$ copies of $5$, $6-2r$ copies
of $6$, and $2+r$ copies of $7$, summing to $50$.

Let $P=N_A(u)\cap Z$ and $Q=N_A(w)\cap Z$. Their sizes are both
$5-\epsilon$, and $|P\cap Q|=h$.

If $\epsilon=0$, (5) and nonnegativity give $B[T,u]=B[T,w]=0$.
For any $t\in T$, the common neighbours of $u,t$ lie exactly in
$P\cap Z_t$. Equation (2) therefore yields

$$|P\cap Z_t|=1-1_{t\in U},\qquad
|Q\cap Z_t|=1-1_{t\in W}. \tag{8}$$

In particular $P,Q$ are transversals of the five parent classes outside
$U,W$, respectively. Their labels or overlap are not independently fixed.

If $\epsilon=1$, the sets $U,W$ and the sets $P,Q$ are disjoint.
Writing $\rho_t=B_{ut}$ and $\sigma_t=B_{wt}$, we instead obtain

$$\begin{aligned}
|P\cap Z_t|&=1-1_{t\in U}-1_{t\in W}+\rho_t,\\
|Q\cap Z_t|&=1-1_{t\in U}-1_{t\in W}+\sigma_t,\\
\sum_{t\in T}\rho_t&=\sum_{t\in T}\sigma_t=2.
\end{aligned} \tag{9}$$

Here the additional common neighbour of $u,t$ is $w$ precisely when
$t\in W$, explaining the extra term. These residual defect vectors
remain variable.

There is also a strong uniform rule on the majority of $Z$. For
$z\in Z_t$, let $e(z)=A_{uz}+A_{wz}$. Counting its actual neighbours
and its common neighbours with $x\in T$ gives

$$\begin{aligned}
d_Z(z)&=7-e(z),\\
B_{xz}&=d_{Z_x}(z)+1_{x\in U}A_{uz}+1_{x\in W}A_{wz}
             -1+1_{x=t},\\
\sum_{x\in T}B_{xz}&=2e(z).
\end{aligned} \tag{10}$$

If $z\notin P\cup Q$, then $e(z)=0$ and nonnegativity forces
$B[T,z]=0$. Hence

$$d_{Z_x}(z)=1-1_{x=t}. \tag{11}$$

Such a vertex has no neighbour in its own parent class and exactly one
in each of the other seven classes. There are $40+h$ such vertices
when $\epsilon=0$, and $42$ when $\epsilon=1$. The remaining at most
ten vertices have the exact, but less uniform, constraints (10).

## 4. Coherence along an entire double path

First, every adjacent double edge is an isolated edge component of $D$:
if either endpoint had another double neighbour, section 1 would
forbid that original adjacency. Thus every edge of any $D$ path of
length at least two is an original $A$ nonedge.

More strongly, let $v_0,\ldots,v_m$ be a $D$ path, with $m\ge2$, and
write $a_{ij}=A_{v_i v_j}$. Then $a_{ij}$ depends only on $|i-j|$:
the principal submatrix on the path is symmetric Toeplitz.

For $1\le r,s\le m-1$, the two defect rows are saturated by their
path neighbours. Commutation therefore gives

$$a_{r-1,s}+a_{r+1,s}=a_{r,s-1}+a_{r,s+1}. \tag{12}$$

Define $E_{ij}=a_{i+1,j+1}-a_{ij}$ for $0\le i,j\le m-1$.
For $0\le i<j\le m-1$, applying (12) at $(r,s)=(i+1,j)$ yields
$E_{ij}=E_{i+1,j-1}$. When $j-i\ge2$, this reduces the index gap by
two. The terminal diagonal case has $E_{ii}=0$. The terminal gap-one
case also has $E_{i,i+1}=0$, because both consecutive-path adjacencies
$a_{i+1,i+2}$ and $a_{i,i+1}$ are zero. Symmetry handles $i>j$.
Thus $E=0$, proving the assertion without imposing an automorphism
on the original graph.

## Precise remaining obligation

Sections 1–3 retain all endpoint cases and yield a complete vertex
partition with prescribed parent incidences, attachment counts, and
many exact cross-class neighbour counts. They do **not** determine
the graph on $Z$, the residual defect ports, or the simultaneous
common-neighbour counts of all pairs in $Z$; those still have to arise
from the same original $A$. Equation (11) alone is not a matching-cover
construction, because class sizes differ and the exceptional vertices
remain present. No complete candidate or contradiction has been obtained.

The Toeplitz conclusion constrains adjacency only within a double path;
it does not extend that path to a cycle, make the whole graph circulant,
or settle the adjacent-double branch. This is one short application of
the project's formula-derivation/proof-writer mathematical workflow;
there was no solver, external call, or auxiliary enumeration.
