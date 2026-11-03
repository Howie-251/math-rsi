# No order 64 graph: a trace obstruction over F_11

## Claim and status

No finite simple undirected graph on 64 vertices has maximum degree at most 8 and the property that every distinct pair is adjacent or has a common neighbor.

Status: complete paper derivation; Lean implementation and independent external review are separate obligations. This is an alternative proof of the order 64 exclusion, not a new extremal bound and not a proof of the full degree/diameter objective. It avoids the pairing basis and determinant calculation in `N64_MOD5_DETERMINANT.md` and the rational spectral argument in `FOUNDATIONS.md`.

## Proof

Suppose that such a graph exists. For every vertex $v$, counting its ball of radius two gives

$$64\le1+8\deg(v).$$

Since all degrees are at most 8, the graph is 8-regular. Let $A$ be its integer adjacency matrix, let $J$ be the all-one matrix, and define the actual integer defect

$$B=A^2+A-7I-J.$$

Then $B$ is symmetric, has zero diagonal, and has nonnegative integer entries: off the diagonal, its entry is the common-neighbor count plus the adjacency indicator minus one. The path property makes this nonnegative. Its row sums are

$$8^2+8-7-64=1.$$

Thus each row has exactly one entry equal to one and all others zero. Symmetry and the zero diagonal imply that these entries form disjoint transposition pairs. In particular,

$$B^2=I,\qquad BJ=JB=J.$$

Regularity also gives $AJ=JA=8J$, hence $AB=BA$.

The graph is triangle-free. Indeed, a triangle through $v$ would make two distinct entries in row $v$ of $B$ at least one, contradicting its row sum one. Therefore every actual edge $uv$ has no common neighbor and satisfies $B_{uv}=0$. It follows directly that

$$\operatorname{tr}(AB)=\sum_{u,v}A_{uv}B_{vu}=0.$$

The identities $\operatorname{tr}(A)=\operatorname{tr}(B)=0$ follow from their zero diagonals.

Now reduce every matrix entry modulo 11 and work entirely over $\mathbf F_{11}$. Define

$$D=A(I+B)+I,\qquad E=\frac{I-B}{2}=6(I-B).$$

The division by 2 is valid in $\mathbf F_{11}$. Before reduction, the commuting identity $AB=BA$ and $B^2=I$ give

\[
\begin{aligned}
D^2
 &=2(A^2+A)(I+B)+I\\
 &=2(7I+J+B)(I+B)+I\\
 &=17I+16B+4J.
\end{aligned}
\]

Modulo 11, $17I+16B=6I+5B=6(I-B)=E$. Also $(I+B)E=0$. Consequently

$$D^2=E+4J,\qquad DE=E,\qquad DJ=17J.$$

The last identity uses $J+BJ=2J$ and $AJ=8J$. For every integer $k\ge0$, induction gives $D^kE=E$ and $D^kJ=17^kJ$. Multiplying $D^2=E+4J$ by $D^k$ therefore gives the complete power formula

$$D^{k+2}=E+4\cdot17^kJ.$$

Taking $k=9$ and then taking traces yields

$$\operatorname{tr}(D^{11})=32+4\cdot17^9\cdot64.$$

Here $\operatorname{tr}(E)=(64-0)/2=32$ and $\operatorname{tr}(J)=64$, with all quantities interpreted in $\mathbf F_{11}$. Since

$$17^9\equiv6^9\equiv2\pmod{11},$$

we obtain

$$\operatorname{tr}(D^{11})\equiv32+4\cdot2\cdot64\equiv32+6\equiv5\pmod{11}.$$

On the other hand, for every square matrix $M$ over $\mathbf F_{11}$,

$$\operatorname{tr}(M^{11})=\operatorname{tr}(M).$$

For completeness, expand the left side as a sum indexed by cyclic strings of 11 matrix indices. Cyclic rotation preserves the product of entries. Because 11 is prime, every nonconstant string belongs to an orbit of size 11, whose total contribution vanishes. Constant strings contribute $\sum_i M_{ii}^{11}=\sum_i M_{ii}$ in $\mathbf F_{11}$. This proves the identity; it is also the finite-field trace Frobenius theorem.

Applying it to $D$ gives instead

$$\operatorname{tr}(D^{11})=\operatorname{tr}(D)
=\operatorname{tr}(A)+\operatorname{tr}(AB)+64
=64\equiv9\pmod{11}.$$

The incompatible residues 5 and 9 give the contradiction. Therefore no original order 64 graph exists. $\square$

## Formalization interface and scope

The necessary formal bridges are the original-graph regularity and integral defect identities; the row-one argument giving $B^2=I$; the explicit triangle-free argument giving $\operatorname{tr}(AB)=0$; reduction to `ZMod 11`; the displayed power induction; and trace Frobenius, available in Mathlib as `Matrix.ZMod.trace_pow_card`. No 32-pair indexing, eigenspace dimension, change of basis or determinant theorem is needed for this route.

This file itself is not a compiled Lean proof. No historical SAT branch or unresolved order from 58 through 63 is removed by it. The finite-field route was proposed by the coordinating agent; its coefficients, trace premises, power recurrence and final residues were independently recomputed here.
