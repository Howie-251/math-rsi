# Double-defect cycles cannot occur at order 61

Date: 2026-10-13.

## Claim and status

**PROVABLE AS STATED.** Let $G$ be a simple undirected graph of order $61$,
degree $8$ and diameter at most $2$, with adjacency matrix $A$. Its actual
defect matrix cannot be

$$B=A^2+A-7I-J=2A(C_{61}).$$

Consequently, using the established connectedness and entry bounds for the
actual defect matrix, the simple graph

$$D=(V(G),\{\{u,v\}:B_{uv}=2\})$$

is a disjoint union of paths, including isolated vertices.

This is a pure proof. It uses no finite enumeration, norm calculation,
solver, or cyclic-defect-2 theorem. The manuscript is writer-checked;
fresh local and external review are not claimed here.

## Assumptions, notation and strategy

The matrix $A$ always denotes the adjacency matrix of the same original
graph. It is symmetric and binary, has diagonal zero, and has row sum $8$.
Thus $AJ=JA=8J$, and the displayed definition of $B$ gives $AB=BA$.

For the final corollary only, import from
[CONNECTED_TRIPLE_EXCLUSION.md](CONNECTED_TRIPLE_EXCLUSION.md) that the
positive support of $B$ is connected, every row sums to $4$, and all entries
belong to $\{0,1,2\}$. Those results are not reproved here.

The proof first establishes a constant-diagonal commutant lemma for an odd
cycle, then applies an elementary two-step count to the resulting graph.
**Commuting with a cycle alone is not being assumed to imply circulancy.**
The additional constant-diagonal hypothesis is used explicitly.

## 1. Constant diagonal removes the extra cycle commutant

**Lemma.** Let $n\ge3$ be odd, index matrices by $\mathbb Z/n\mathbb Z$, and
let $C=A(C_n)$ have its cycle in the order $0,1,\ldots,n-1$. If a real
matrix $H$ satisfies $HC=CH$ and all its diagonal entries are equal, then

$$H_{i+1,j+1}=H_{ij}\qquad\text{for every }i,j.$$

In particular $H_{ij}=H_{0,j-i}$ is circulant. Symmetry of $H$ is not
needed for this lemma.

**Proof.** Define

$$E_{ij}=H_{i+1,j+1}-H_{ij}.$$

The $(i,j+1)$ entry of $HC=CH$ is

$$H_{ij}+H_{i,j+2}=H_{i-1,j+1}+H_{i+1,j+1}.$$

Rearranging gives

$$E_{ij}=H_{i,j+2}-H_{i-1,j+1}=E_{i-1,j+1}.$$

For fixed $i,j$, choose $t\in\mathbb Z/n\mathbb Z$ with
$2t=i-j$, possible because $n$ is odd. Iterating the last identity gives

$$E_{ij}=E_{i-t,j+t}=E_{k,k},\qquad k=(i+j)/2.$$

The constant diagonal implies $E_{k,k}=H_{k+1,k+1}-H_{kk}=0$. Hence $E=0$,
which proves simultaneous-shift invariance. Repeating that invariance
$-i$ times gives $H_{ij}=H_{0,j-i}$. $\square$

## 2. The all-double cycle gives an impossible original graph

Suppose $B=2C$ after labeling its cycle by $\mathbb Z/61\mathbb Z$.
The identity $AB=BA$ gives $AC=CA$. Since $A$ has constant diagonal zero,
the lemma applies and yields

$$A_{ij}=A_{0,j-i}.$$

Let $S=\{s\in\mathbb Z/61\mathbb Z:A_{0s}=1\}$. The original graph's
degree, zero diagonal and symmetry give, respectively,

$$|S|=8,\qquad 0\notin S,\qquad S=-S.$$

No nonzero element of $\mathbb Z/61\mathbb Z$ equals its negative. We can
therefore write $S=\{\pm a_1,\pm a_2,\pm a_3,\pm a_4\}$ with four distinct
opposite pairs. Every vertex reachable from $0$ in at most two edges lies in

$$
\{0\}\ \cup\ \{\pm a_i:1\le i\le4\}
\ \cup\ \{\pm2a_i:1\le i\le4\}
\ \cup\ \{\epsilon a_i+\eta a_j:
  1\le i<j\le4,\ \epsilon,\eta\in\{-1,1\}\}.
$$

Indeed a two-step walk adds two members of $S$; opposite members cancel,
equal members give $\pm2a_i$, and members from different pairs give the
last set. This union has cardinality at most

$$1+8+8+4\binom42=41.$$

Coincident expressions can only reduce this upper bound. Diameter at most
$2$ would require all $61$ vertices to occur in the union, a contradiction.
Thus $B=2A(C_{61})$ is impossible. $\square$

## 3. Consequence for the double-edge support

Every vertex has degree at most $2$ in $D$, because each incident edge of
$D$ contributes $2$ to its defect-row sum $4$. If $D$ contains a cycle,
each vertex of that cycle has its whole defect row saturated by its two
cycle neighbours. There can be no positive entry of $B$ from a cycle
vertex to any vertex outside the cycle. Connected positive support of $B$
therefore forces the cycle to contain all $61$ vertices and forces
$B=2A(C_{61})$. Section 2 excludes that possibility.

Hence $D$ is acyclic and has maximum degree at most $2$, so each of its
components is a path or an isolated vertex. $\square$

## Boundary

This closes the double-cycle case and proves a structural constraint on
every remaining order-$61$ target. It does not exclude double paths or
prove nonexistence at order $61$. No circulant assumption was imposed on
an arbitrary target: circulancy was derived only under the hypothesis
$B=2A(C_{61})$, using the original adjacency matrix's zero diagonal.

This note applies the project's `formula-derivation` and `proof-writer`
skills under the V3 mathematical adaptation. No shared navigation or wiki
was modified, and no external review is represented as completed.
