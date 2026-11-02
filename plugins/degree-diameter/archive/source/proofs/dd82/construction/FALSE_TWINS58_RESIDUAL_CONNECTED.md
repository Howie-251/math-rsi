# False-twin order 58: the residual matching cover is connected

Date: 2026-10-13. This proof uses the general false-twin representation;
it assumes no translation symmetry or prescribed matching permutations.

## Claim

Let $G$ be a simple graph on $58$ vertices with maximum degree at most $8$
and diameter at most $2$, containing a pair of false twins. Let $H$ be the
adjacency matrix of its induced graph on the $48$ vertices in eight
six-vertex fibres, as in
[the exact representation](FALSE_TWINS58_EIGHT_SIX_FIBERS.md), Sections 1–2.
Write $D=\operatorname{diag}(J_6,\ldots,J_6)$ and define

$$E=H^2+H-7I-J_{48}+D.$$

Then the graph with adjacency matrix $E$ is connected. On the subspace
$W$ of vectors summing to zero in each fibre, every eigenvalue $\lambda$
of $H$ satisfies

$$
\frac{-1-\sqrt{57}}2<\lambda<\frac{-1+\sqrt{57}}2,
\qquad \lambda\notin(-1,0).
$$

If $E$ is bipartite, its two parts meet every fibre in $3$ vertices each,
and every vertex of $H$ has $3$ neighbours in its own part and $4$ in
the other part. In particular, $H$ has no zero eigenvalue in either case.

## Status

**PROVABLE AS STATED.** This is a structural restriction on the entire
false-twin family, not an exclusion of that family or of order $58$.
No computational search or Lean formalization is used.

## Assumptions and Notation

The representation gives eight independent fibres $F_1,\ldots,F_8$, each
of size $6$, with a perfect matching of $H$ between every pair. For
distinct fibres, diameter-two coverage says that the corresponding block
of $H^2+H-J_{48}$ is a permutation matrix. Within a fibre, distinct
vertices have no common $H$ neighbour, so $H^2$ has diagonal block $7I_6$.
Consequently $E$ is also the adjacency matrix of a simple $7$-regular
matching cover of $K_8$: its diagonal blocks are zero and every
off-diagonal block is a permutation matrix.

All matrices and vector spaces are over the reals unless integrality is
stated. The all-ones matrix has its dimension indicated where needed.
The symbols $t_i$ below count vertices per fibre, not total component sizes.

## Proof Strategy and Dependencies

The matching-cover identities imply that $H$ commutes with $E$. The
$7$-eigenspace of $E$ gives an integer equitable quotient of $H$ on the
components of $E$. An irreducible quadratic constrains its dimension;
four small component-size profiles are then excluded by exact equations.
Only the displayed representation and elementary spectral facts for
connected regular graphs are used.

## Proof

**1. Commutation and connectivity of $H$.** Between two distinct fibres,
both $HD$ and $DH$ have block $J_6$; their diagonal blocks are zero.
Thus $HD=DH=J_{48}-D$. Regularity also gives $HJ_{48}=J_{48}H$,
and therefore $HE=EH$.

Every pair of vertices in distinct fibres is joined by a path of length
at most two inside $H$, by the exact cross-fibre coverage condition.
Vertices in the same fibre can be joined using a vertex in a different
fibre. Hence $H$ is connected.

**2. The component quotient.** Let $C_1,\ldots,C_c$ be the components of
$E$. A perfect matching of $E$ between any two fibres restricts to a
bijection between their intersections with a fixed component. Hence

$$|C_i\cap F_j|=t_i\ge1,\qquad |C_i|=8t_i,\qquad \sum_i t_i=6.$$

The $7$-eigenspace of the symmetric regular matrix $E$ consists precisely
of vectors constant on each $C_i$. Since $H$ commutes with $E$, this
space is $H$-invariant. Thus the number $q_{ij}$ of $H$ neighbours in
$C_j$ of a vertex in $C_i$ does not depend on the chosen vertex.
The quotient $Q=(q_{ij})$ satisfies

$$q_{ij}\in\mathbb Z_{\ge0},\qquad Q\mathbf1=7\mathbf1,
\qquad t_iq_{ij}=t_jq_{ji}.$$

On component-constant vectors, $E$ acts as $7I$, $J_{48}$ acts as
$8\mathbf1t^T$, and $D$ acts as $\mathbf1t^T$. Therefore

$$\boxed{Q^2+Q=14I+7\mathbf1t^T.}\tag{1}$$

The quotient is similar to a symmetric matrix by the weights $t_i$.
Its eigenvalue $7$ is simple because $H$ is connected. On the invariant
space $t^Tx=0$, equation (1) gives eigenvalues among

$$\alpha=\frac{-1+\sqrt{57}}2,\qquad
\beta=\frac{-1-\sqrt{57}}2.$$

These are irrational conjugates, so their multiplicities in the integer
matrix $Q$ are equal. Put $m=(c-1)/2$. Since $1\le c\le6$, it follows that

$$c\in\{1,3,5\},\qquad \operatorname{tr}Q=7-m.\tag{2}$$

**3. Excluding three components of sizes $t=(2,2,2)$.** Here $Q$ is
symmetric. Its total entry sum is $21$, while (2) gives diagonal sum
$6$. Its off-diagonal entry sum would be $15$, whereas symmetry makes
that sum even. This is impossible.

**4. Excluding three components of sizes $t=(4,1,1)$.** Write
$q_{12}=a$, $q_{13}=b$ and $q_{23}=q_{32}=d$. Weighted symmetry gives
$q_{21}=4a$ and $q_{31}=4b$, so $a,b\in\{0,1\}$. The row sums and
trace give

$$21-5(a+b)-2d=6.$$

Parity forces $a+b=1$, and then $d=5$. The small-component row with
entry $4$ toward the large component would have entry $5$ toward the
other small component, exceeding its total degree $7$.

**5. Excluding three components of sizes $t=(3,2,1)$.** Weighted symmetry
allows the notation

$$q_{12}=2a,\quad q_{21}=3a,\quad
q_{13}=b,\quad q_{31}=3b,\quad
q_{23}=d,\quad q_{32}=2d,$$

where $0\le a,b\le2$ and $0\le d\le3$. The trace condition becomes

$$5a+4b+3d=15.$$

For $a=0$, reduction modulo $3$ forces $b=0$, giving the forbidden
$d=5$. For $a=1$, it forces $b=1$ and gives $d=2$.
For $a=2$, it forces $b=2$, giving $d=-1$. The sole remaining matrix is

$$Q=\begin{pmatrix}4&2&1\\3&2&2\\3&4&0\end{pmatrix}.$$

But its $(1,1)$ entry in $Q^2+Q$ is $29$, whereas (1) requires
$14+7\cdot3=35$. This excludes the last three-component profile.

**6. Excluding five components.** The only profile is $t=(2,1,1,1,1)$.
Index the large component by $0$, put $a_i=q_{0i}$ for $1\le i\le4$,
and set $A=\sum_i a_i$. The lower-right block $B$ of $Q$ is symmetric,
$q_{i0}=2a_i$, and $q_{00}=7-A$. Formula (2) gives

$$\operatorname{tr}B=A-2.$$

Its row sums are $7-2a_i$, so its off-diagonal entry sum is $30-3A$.
This must be even. Together with $2\le A\le7$, this yields
$A\in\{2,4,6\}$. The $(0,0)$ entry of (1) says

$$ (7-A)(8-A)+2\sum_i a_i^2=28.\tag{3}$$

For $A=2$, the first term alone is $30$. For $A=6$, equation (3)
would give $\sum_i a_i^2=13$, contradicting
$\sum_i a_i^2\equiv\sum_i a_i=6\pmod2$. For $A=4$, it gives
$\sum_i a_i^2=8$. No $a_i$ can exceed $2$, and
$\sum_i a_i(a_i-1)=4$ then forces, up to ordering,
$a=(2,2,0,0)$. Thus $q_{00}=3$ and, for every $j\ne0$,

$$ (Q^2+Q)_{0j}=4a_j+2(B_{1j}+B_{2j})$$

is even. Equation (1) requires this entry to be $7$. This contradiction
excludes five components. Therefore $c=1$, so $E$ is connected.

**7. Spectral consequences.** The fibre-constant subspace is invariant
under both matrices; its orthogonal complement $W$ is also invariant.
On $W$ the matrices $D,J_{48}$ vanish, so

$$E|_W=(H^2+H-7I)|_W.$$

As $E$ is connected and $7$-regular, its eigenvalue $7$ is simple,
carried by the global constant vector, which is not in $W$.
Consequently an eigenvalue $\lambda$ of $H|_W$ satisfies

$$-7\le\lambda^2+\lambda-7<7.$$

The right inequality yields $\beta<\lambda<\alpha$, and the left
yields $\lambda(\lambda+1)\ge0$, proving the stated gap.

**8. The bipartite alternative.** If $E$ is not bipartite, $-7$ is not
an eigenvalue, so $H|_W$ has neither eigenvalue $0$ nor $-1$.
Suppose instead that $E$ is bipartite. A matching between fibres reverses
the bipartition. If the positive part meets fibre $i$ in $r_i$ vertices,
then $r_i=6-r_j$ for every $i\ne j$. Using three distinct fibres gives
$r_i=3$ for every $i$.

Let $z$ be $+1$ on the positive part and $-1$ on the negative part.
It lies in $W$ and spans the simple $-7$-eigenspace of $E$.
Commutation forces $Hz=\lambda z$, where
$\lambda^2+\lambda=0$, so $\lambda\in\{0,-1\}$.
Every coordinate of $Hz$ is a sum of seven numbers in $\{1,-1\}$ and
is odd; hence $\lambda=0$ is impossible. Thus $Hz=-z$, which gives
three $H$ neighbours of the same sign and four of the opposite sign
at each vertex. The only possible $0$-eigenspace of $H|_W$ has thereby
also been excluded. On the fibre-constant subspace $H$ has eigenvalues
$7$ and $-1$, so $H$ is nonsingular. $\square$

## Corrections or Missing Assumptions

None beyond the stated exact false-twin representation and diameter-two
coverage. The proof does not assume any automorphism group or special
form for the $28$ matching permutations.

## Open Risks and Scope

The theorem supplies a necessary structural restriction. Connected
residual covers remain possible at the level of this argument; neither
an actual graph nor a contradiction for the whole false-twin family has
been obtained here. External review and Lean checking are not asserted.
