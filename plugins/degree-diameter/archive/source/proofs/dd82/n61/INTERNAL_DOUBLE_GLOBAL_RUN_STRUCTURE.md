# Global witnesses and neighborhood structure of the double-path forest

> 2026-10-18有界对齐后的研究处置：本稿仍是未接受草稿。其全部内部双路径作用域已被旧[3,3]四轨道RAW覆盖；不继续作为新构造或SAT研究方向。保留正文供证据增强需要时参考，不把RAW升级为已认证不存在。见 [新旧61对齐](../../../research-wiki/DD82_OLD_NEW61_ALIGNMENT_20261018.md)。

Date: 2026-10-13. **PROVABLE AS STATED; writer-checked pure deduction.**
This is a new global structural derivation after the internal-double
computation loop closed. It is not a fresh proof audit, external acceptance,
new solver mechanism, or order61 exclusion. No computation or old check was
run. Parallel writer reasoning contributed the witness/run deductions;
that collaboration is not an independent acceptance receipt.

## Target, invariant object and assumptions

The target is a simultaneous structural description of **all** internal
vertices of the complete double-defect forest and their actual original
neighborhoods. The invariant object is the relation between an internal
double vertex and its common original neighbors across its two double
neighbors. Every statement below is exact; there is no approximation.

Let $A$ be the actual adjacency matrix of a simple degree-eight,
diameter-two graph on $61$ vertices and let $B=A^2+A-7I-J$.
Import the established actual-defect baseline and path forest from
[CONNECTED_TRIPLE_EXCLUSION.md](CONNECTED_TRIPLE_EXCLUSION.md) and
[DOUBLE_DEFECT_CYCLE_OBSTRUCTION.md](DOUBLE_DEFECT_CYCLE_OBSTRUCTION.md):
$B$ is symmetric, nonnegative integral, zero-diagonal, row-four, with
entries at most two, and $D=\{xy:B_{xy}=2\}$ is a path forest.

Use the exact local identities in
[INTERNAL_DOUBLE_PATH_LOCAL.md](INTERNAL_DOUBLE_PATH_LOCAL.md), the
endpoint nonadjacency from
[INTERNAL_DOUBLE_ENDPOINT_ADJACENCY_EXCLUSION.md](INTERNAL_DOUBLE_ENDPOINT_ADJACENCY_EXCLUSION.md),
and the universal $h=0$ theorem in
[INTERNAL_DOUBLE_COMMON_ATTACHMENT_EXCLUSION.md](INTERNAL_DOUBLE_COMMON_ATTACHMENT_EXCLUSION.md).
Their reviewed computational dependencies are inherited, not repeated.

Write $N(x)=N_A(x)$ and $\mu(x,y)=|N(x)\cap N(y)|$ for distinct vertices.
Then $\mu(x,y)=1+B_{xy}-A_{xy}\le3$ and $AB=BA$.
Let $\mathcal I$ be the set of vertices internal to components of $D$.
For $v\in\mathcal I$, name its two $D$ neighbors $u,w$ and define
$$C_v=N(u)\cap N(w),\qquad r_v=|C_v|.$$
Universal $h=0$ gives $C_v\subseteq N(v)$ and $r_v\in\{1,2\}$.
Put $\mathcal I_j=\{v\in\mathcal I:r_v=j\}$ for $j=1,2$ and
$\mathcal W=\bigcup_{v\in\mathcal I}C_v$.
The vertices of $C_v$ are called the witnesses of $v$ in this note.

The strategy is saturated rows $\to$ disjoint witness sets $\to$ exact
neighborhood defect matrices $\to$ the induced defect graph on all
witnesses. The run description follows from that global structure.

## Claim

1. For every $v\in\mathcal I$ and every original vertex $c$,
   $$c\in C_v\quad\Longleftrightarrow\quad
     \operatorname{supp}(B_{c*})\subseteq N(v). \tag{1}$$
   The sets $C_v$ for distinct internal vertices are pairwise disjoint.
2. If $v\in\mathcal I_1$, its unique witness is isolated in $D$.
   If $v\in\mathcal I_2$, its two witnesses form an isolated edge
   component of $D$ and are nonadjacent in $A$. Distinct centers use
   distinct witnesses and hence distinct such edge components.
3. For $c\in C_v$, its entire original neighborhood is independent
   in $A$. On its eight neighbors the only positive defect entries are
   $$B_{uv}=B_{vw}=2,\qquad B_{uw}=r_v-1. \tag{2}$$
   In particular $D[N(c)]$ is the three-vertex path $u,v,w$ together
   with five isolated vertices.
4. The whole induced weighted graph $B[\mathcal W]$ has the following
   exact components. Each $D$ component on $k\ge4$ vertices produces
   a unit-weight path on the $k-2$ witnesses of its ordered internal
   vertices. A three-vertex component with $r=1$ produces one isolated
   witness, and one with $r=2$ produces an isolated double edge. There
   are no additional positive entries between these pieces.

These are constraints on the complete forest, not just one selected
triple. For example, $|\mathcal I_1|$ is at most the number of isolated
vertices of $D$, and $|\mathcal I_2|$ is at most the number of isolated
$D$ edges whose endpoints are original nonneighbors.

## Proof

### 1. Exact rows and global disjointness

Fix an internal vertex $v$ with double neighbors $u,w$, and write
$T=N(v)$, $U=T\cap N(u)$, $W=T\cap N(w)$. The inherited local facts are
$$B_{v*}=2e_u^T+2e_w^T,\quad |U|=|W|=3,\quad
  C_v=U\cap W,\quad B[T]=A(K_3[U])+A(K_3[W]), \tag{3}$$
and $T$ is independent in $A$.

For any original vertex $c$, actual commutation at $(v,c)$ gives
$$\sum_{t\in T}B_{tc}=2(A_{uc}+A_{wc}). \tag{4}$$
If $c\in C_v$, the right side is four. Symmetry, nonnegativity and
row sum four force the entire row of $c$ to be supported in $T$.
Conversely, such row support makes the left side four, so both binary
adjacencies on the right are one, proving (1).

For $c\in C_v$, equation (3) gives its whole row more explicitly:
for every $z\ne c$,
$$B_{cz}=1_{z\in N(v)}(A_{uz}+A_{wz}). \tag{5}$$
There are four unit neighbors when $r_v=1$. When $r_v=2$, there is
one double neighbor (the other shared vertex) and two unit neighbors.
These rows already total four, so there are no outside entries.
Consequently a witness has at least three distinct positive-defect
neighbors, is $D$-isolated in the first case, and has just the other
witness as its $D$ neighbor in the second. The two latter witnesses
lie in the independent set $T$ and therefore are original nonneighbors.

Suppose one vertex $c$ belonged to $C_v$ and $C_{v'}$ for distinct
internal vertices. Its at least three distinct positive-defect
neighbors would all belong to $N(v)\cap N(v')$ by (1). The vertex
$c$ itself also belongs to this intersection and is not in its own
defect support. This would give at least four common original neighbors,
contradicting $\mu(v,v')\le3$. Thus all witness sets are disjoint.
The assertions and two injections in claim2 follow.

### 2. A witness's entire neighborhood

Fix $c\in C_v$ again. Every positive defect neighbor of $c$ lies
in $T\setminus\{c\}$, hence is an original nonneighbor of $c$.
If $x\in N(c)$, then $B_{cx}=0$ and the actual identity gives
$\mu(c,x)=0$. Therefore $N(c)$ is independent.

For any $z\ne c$ with $B_{cz}=0$,
$$|N(z)\cap N(c)|=1-A_{cz}\le1. \tag{6}$$
Such a vertex cannot give an additional common neighbor to a pair
of vertices in $N(c)$. Positive defect neighbors of $c$ have the
following complete neighborhoods inside $N(c)$:

- Each point of $U\setminus W$ has defect one to $c$ and already
  has the two neighbors $u,v$ in $N(c)$. These are exactly its two
  neighbors there.
- Each point of $W\setminus U$ has exactly the two neighbors $v,w$
  there, by the same actual common-neighbor identity.
- If $r_v=2$, the other point of $U\cap W$ has defect two to $c$
  and already has all three neighbors $u,v,w$ in $N(c)$. These are
  exactly its three neighbors there.

For a pair in the independent set $N(c)$, the common neighbor $c$
accounts for the baseline one in its actual defect. Equations (5)–(6)
exhaust all other possible common neighbors. There are $3-r_v$
copies of the pair $\{u,v\}$, $3-r_v$ copies of $\{v,w\}$, and
$r_v-1$ copies of the triangle on $\{u,v,w\}$. Since $r_v$ is
one or two, their weighted sum is precisely (2). Every other pair
in the eight-point neighborhood has defect zero. This proves claim3.

### 3. The induced weighted forest on every witness

Let $c\in C_v$ and $d\in C_{v'}$ be distinct witnesses. If
$v=v'$, then there are two witnesses, and (5) gives $B_{cd}=2$.
Now suppose $v\ne v'$.

If $B_{cd}>0$, equation (5) says that $d$ is adjacent to $v$ and
to at least one of its two double neighbors. Thus $D[N(d)]$
contains an edge incident with $v$. By claim3 its only two edges
are the two edges incident with its assigned center $v'$. Therefore
the edge is incident with both $v$ and $v'$, so $v,v'$ are
consecutive internal vertices of the same $D$ component.

Conversely suppose $v,v'$ are consecutive internal vertices. Their
component has at least four vertices, so both centers have one witness.
Name the other double neighbor of $v$ as $u$. The witness $d$ of
$v'$ is adjacent to $v$ and $v'$. It cannot also be adjacent to
$u$: otherwise $D[N(d)]$ would contain the edge $uv$, which is
not one of the two edges of its assigned three-vertex path centered
at $v'$. Equation (5) therefore gives $B_{cd}=1$.

Hence distinct-center witnesses have a positive defect entry exactly
when their centers are consecutive, and that entry is one. A center
with two witnesses lies only in a three-vertex $D$ component, so its
double witness edge has no links to other witnesses. Claim4 follows
for the entire forest simultaneously. This does not assert that
$\mathcal W$ is a closed component of the full defect graph: its
rows generally also have positive entries outside $\mathcal W$.

## Global run consequences

For any original vertex $x$, read the binary word $A_{x,v_i}$ in
the order of each complete $D$ path component. A run means a maximal
nonempty consecutive string of ones within one such word.

Universal $h=0$ forbids the pattern $101$, so runs in the same word
are separated by at least two zeros. A run of length at least four
would make $x$ a witness of two distinct internal centers, contrary
to global disjointness. Thus all runs have length at most three.
Across **all** components together, any vertex has at most one
three-run. If it has one, claim3 says that its remaining five original
neighbors produce five singleton runs; it has no two-run in any
component. A vertex outside $\mathcal W$ has no three-run, so its
induced graph $D[N(x)]$ is a matching together with isolated vertices.

There is also an exact component inventory. For a component on
$k\ge4$ vertices, let $q_j$ count all maximal $j$-runs over the
$61$ original vertex words. Its $k-2$ internal centers each have
one distinct witness, so $q_3=k-2$. Every consecutive D pair is
an original nonedge with exactly three common neighbors. Summing
adjacent pairs of ones and then all ones gives
$$q_2+2q_3=3(k-1),\qquad q_1+2q_2+3q_3=8k.$$
Therefore
$$q_3=k-2,\qquad q_2=k+1,\qquad q_1=3k+4. \tag{7}$$
The same counting on a three-vertex component gives
$(q_1,q_2,q_3)=(13,4,1)$ for its one-witness type and $(14,2,2)$
for its two-witness type. Isolated vertices and two-vertex components
have no internal center and require no witness assignment.

## Scope and remaining obstruction

The new conclusion is the global disjoint witness relation, the exact
defect structure of every witness neighborhood, and the induced unit-
path/double-edge structure of the whole witness set. It couples all
double components and all their internal vertices at once; it is not
another constraint on only the old selected triple or another solver
time limit. No prior UNKNOWN input is reopened here.

This does not prove that an original neighborhood is one interval on
a D path. Even the binary condition alone permits separated runs such
as $111001$; the theorem still permits singleton runs away from the
assigned triple. It also does not make the witness set invariant under
$A$ or $B$, give an equitable component quotient, or settle the remaining
order61 existence problem. No complete contradiction follows from the
counting injections alone. A subsequent proof would have to control
the positive defect entries outside the witness set and the remaining
original incidences, using these exact global structures rather than
assuming closure. Separate proof checking is still required before any
new theorem acceptance is claimed.
