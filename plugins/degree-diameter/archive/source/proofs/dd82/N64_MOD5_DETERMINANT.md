# No order 64 graph: a determinant obstruction over F_5

## Claim and status

There is no finite simple undirected graph on 64 vertices with maximum degree at most 8 in which every distinct pair is adjacent or has a common neighbor.

Status: complete paper proof, independently recomputed within the current research collaboration; external review and Lean implementation are separate obligations. This file does not claim a compiled theorem. It supplies an alternative implementation route for the order 64 exclusion already proved over the rationals in `FOUNDATIONS.md`; it does not determine the full extremal value or exclude any of orders 58 through 63.

## Assumptions and notation

All matrices are derived from the same alleged original graph. Initially, $A$ is its integer adjacency matrix, $I$ is the identity matrix, $J$ is the all-one matrix, and

$$B=A^2+A-7I-J.$$

After the matching structure of $B$ is obtained over the integers, the proof reduces every matrix entry to the field $\mathbf F_5$. The same letters denote these reduced matrices. The change of scalars is explicit; no nonnegative-order argument is used over the finite field.

## Proof strategy and dependencies

The root ball count forces regularity. The actual defect has nonnegative integer entries and row sum one, hence is a fixed-point-free involution matrix. A short polynomial identity produces an integer matrix whose square has an explicitly computable determinant. A basis made from pair sums and pair differences, together with a rank-one determinant identity proved below, evaluates that determinant as the nonsquare $3\in\mathbf F_5$.

Only elementary graph counting, matrix multiplication, determinant multilinearity and arithmetic in $\mathbf F_5$ are needed. No graph spectral classification, rational irreducibility argument, floating-point computation, solver result or historical conditional branch is used.

## Proof

**1. The graph is 8-regular, and its defect is a matching matrix.** For any vertex $v$, the one-or-two-edge path property gives

$$64\le 1+\deg(v)+7\deg(v)=1+8\deg(v).$$

Since $\deg(v)\le8$, this forces $\deg(v)=8$. Consequently $A\mathbf1=8\mathbf1$ and $AJ=JA=8J$.

The matrix $B$ is symmetric. Its diagonal entries are $8-7-1=0$. If $u\ne v$, then

$$B_{uv}=|N(u)\cap N(v)|+A_{uv}-1\ge0,$$

by the actual path property. Finally,

$$B\mathbf1=(8^2+8-7-64)\mathbf1=\mathbf1.$$

Each row of this nonnegative integer matrix therefore contains exactly one entry equal to one and all other entries zero. Let $\pi(v)$ be the position of that one. Symmetry implies $\pi(\pi(v))=v$, and the zero diagonal implies $\pi(v)\ne v$. Thus the 64 vertices are partitioned into 32 disjoint pairs, and

$$B^2=I,\qquad BJ=JB=J.$$

Also $AB=BA$, because $B$ is a polynomial in $A$ minus $J$, and $AJ=JA$.

**2. A polynomial square identity.** Define

$$X=I+B,\qquad D=A(I+B)+I=AX+I.$$

Since $B^2=I$, we have $X^2=2X$. Since $AB=BA$, we also have $AX=XA$. Therefore, initially over the integers,

\[
\begin{aligned}
D^2
 &=A^2X^2+2AX+I\\
 &=2(A^2+A)X+I\\
 &=2(7I+J+B)(I+B)+I\\
 &=2\bigl(8(I+B)+2J\bigr)+I\\
 &=17I+16B+4J.
\end{aligned}
\]

The fourth line uses $(7I+B)(I+B)=8(I+B)$ and $J(I+B)=2J$. Every displayed identity survives entrywise reduction modulo 5.

**3. The pairing basis over $\mathbf F_5$.** Label the 32 pairs as $\{p_i,q_i\}$, $1\le i\le32$. In the vector space $\mathbf F_5^{64}$ define

$$f_i=\mathbf e_{p_i}+\mathbf e_{q_i},\qquad g_i=\mathbf e_{p_i}-\mathbf e_{q_i}.$$

These 64 vectors are a basis because 2 is invertible in $\mathbf F_5$ and

$$\mathbf e_{p_i}=(f_i+g_i)/2,\qquad \mathbf e_{q_i}=(f_i-g_i)/2.$$

Directly from the pair permutation,

$$Bf_i=f_i,\qquad Bg_i=-g_i.$$

Moreover,

$$Jf_i=2\sum_{j=1}^{32}f_j,\qquad Jg_i=0.$$

Thus, in the ordered basis $f_1,\ldots,f_{32},g_1,\ldots,g_{32}$, the matrix $D^2=17I+16B+4J$ is block diagonal with blocks

$$33I_{32}+8J_{32}\quad\text{and}\quad I_{32}.$$

This is an explicit change of basis, not an assumption about the spectrum of the original graph. Conjugation by an invertible matrix preserves the determinant, so

$$\det(D^2)=\det(33I_{32}+8J_{32})\quad\text{in }\mathbf F_5.$$

**4. Rank-one determinant calculation.** For every positive integer $m$ and scalars $a,b$ in a field,

$$\det(aI_m+bJ_m)=a^{m-1}(a+mb).$$

Here is a direct proof requiring no division by $a$. Write column $j$ as $a\mathbf e_j+b\mathbf1$ and expand by multilinearity. Terms choosing $b\mathbf1$ from at least two columns vanish because they have equal columns. The term choosing no such column is $a^m$. Each of the $m$ terms choosing it from exactly one column is $ba^{m-1}$: the determinant of the identity matrix with column $j$ replaced by $\mathbf1$ equals one, by expanding that column in the standard basis. The sum is the claimed expression.

Applying this to the first block gives, in $\mathbf F_5$,

\[
\begin{aligned}
\det(D^2)
 &=33^{31}(33+32\cdot8)\\
 &=33^{31}\cdot289\\
 &=3^{31}\cdot4\\
 &=2\cdot4\\
 &=3.
\end{aligned}
\]

The penultimate numerical fact is $3^{31}=3^{4\cdot7+3}=(3^4)^7 3^3=2$ in $\mathbf F_5$.

**5. Contradiction.** Determinant multiplicativity gives

$$\det(D^2)=\det(D)^2.$$

But the squares in $\mathbf F_5$ are exactly $0,1,4$, whereas Step 4 gives $\det(D^2)=3$. This is impossible. Hence the alleged order 64 graph does not exist. $\square$

## Integer interpretation and arithmetic correction

The same pair-sum and pair-difference basis is valid over $\mathbf Q$. Applying Steps 3 and 4 there yields the integer equality

$$\det(D)^2=\det(D^2)=17^2\,33^{31}.$$

Its reduction modulo 5 is $3$, not $2$: the factor $17^2$ contributes $4$, while $33^{31}$ contributes $2$. Both routes give the contradiction. If one first divides by the invertible square $17^2$ in $\mathbf F_5$, the equivalent statement is $(\det(D)/17)^2=2$. The proof above uses the full determinant and the nonsquare $3$ throughout.

## Formalization interface and remaining scope

A Lean implementation can use the original-graph regularity and defect identities, extract the 32 transposition pairs from the integral row-one condition, reduce to `ZMod 5`, and implement the explicit pairing basis and determinant formula. It needs neither an arbitrary diagonalization theorem nor the rational quadratic-extension argument used in the earlier paper proof. The extraction of a pair indexing, matrix change of basis and determinant transport still need their actual formal proofs; this document does not treat those bridges as already compiled.

The new identity and finite-field route were proposed by the coordinating agent and independently expanded and checked here. The only correction was the full determinant's residue, from 2 to 3. No external mathematical source or computation certificate is required for the displayed proof.
