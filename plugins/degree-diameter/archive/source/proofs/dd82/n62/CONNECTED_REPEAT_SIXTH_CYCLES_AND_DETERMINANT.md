# Sixth-cycle parity and an arithmetic square constraint in the connected case

## Claim and status

**PROVABLE AS STATED:** the exact identities and arithmetic consequences
below. This new paper note awaits independent review. They do not yet
exclude any of the remaining values $d\in\{1,3,5,7,9\}$.

For an actual legal order-62 graph with connected repeat support, let
$c_j$ be the number of unoriented simple original cycles of length $j$,
let $u$ be the number of unit triangles in $B$, and put
$\tau=\operatorname{tr}(AB^2)$. Then

$$
\boxed{u=2c_6+5c_5+16d-37076},\qquad
\boxed{4c_6+\tau+24d-49104=2u}.
\tag{1}
$$

In particular $u\equiv c_5\pmod2$.

There is also a nonzero odd integer $S$ such that

$$
\boxed{\det(29I+4B)=41S^2},\qquad
S=\frac{\det(2A+I)}{17}.
\tag{2}
$$

If $\kappa(B)$ is the integer weighted spanning-tree count of the
repeat graph, this implies

$$
\boxed{S^2\equiv39\kappa(B)\pmod{41}},\qquad
\boxed{\kappa(B)\equiv(15S)^2\pmod{41}}.
\tag{3}
$$

Thus the weighted spanning-tree count must be zero or a quadratic
residue modulo $41$. A further necessary congruence is

$$\boxed{\det(3I+B)\equiv10S^2\pmod{17}}.\tag{4}$$

## Assumptions and notation

Use the actual connected-repeat reduction and its hypotheses:

$$
A\mathbf1=8\mathbf1,\quad B=A^2+A-7I-J,\quad
B\mathbf1=3\mathbf1,\quad AB=BA,
$$

where $B$ is nonnegative, integral, symmetric, zero-diagonal, and at
most two. The original graph is triangle-free, every double repeat
is D1, $d\in\{1,3,5,7,9\}$, and

$$c_4=(93+d)/2.$$

These are the actual-graph consequences in
`CONNECTED_REPEAT_REDUCTION.md`. The separate preceding note
`CONNECTED_REPEAT_MIXED_TRACE_AND_ROOT_PATTERNS.md` supplies

$$\tau=10c_5+8d-25048.$$

The new argument below also derives all additional traces directly
from the same matrix identity. It does not modify either source.

A weighted spanning tree uses the positive repeat-support edges and
has weight equal to the product of their entries in $B$. The positive
integer $\kappa(B)$ is the sum of those weights over spanning trees.
Its weighted Laplacian is $3I-B$.

## Strategy

Count nonbacktracking closed walks of length six to express
$\operatorname{tr}(A^6)$ in terms of $c_4,c_6$. Expand the exact
polynomial for $B^3$ and compare it with the unit-triangle count.
Separately, complete the square in the actual matrix identity and
apply the determinant formula for a rank-one perturbation. Reduction
modulo $41$ then connects the square identity to the weighted
matrix-tree theorem.

## 1. The sixth adjacency trace

For a triangle-free regular graph of degree $r$ and order $n$,

$$
\operatorname{tr}(A^6)
=nr(5r^2-6r+2)+48(r-1)c_4+12c_6.
\tag{5}
$$

Here is a direct derivation to fix all coefficients. Let $F_j$ count
nonbacktracking walks of length $j$ between ordered endpoints. The
matrices obey $F_1=A$, $F_2=A^2-rI$, and
$F_j=AF_{j-1}-(r-1)F_{j-2}$ for $j\ge3$. Expansion gives

$$
F_6=A^6-(5r-4)A^4
 +3(r-1)(2r-1)A^2-r(r-1)^2I.
$$

A length-six nonbacktracking closed walk in a triangle-free simple
graph is either a simple six-cycle, or a four-cycle traversed after
one initial edge and followed by that edge in reverse at the end.
The latter walk is allowed because nonbacktracking is imposed only
at consecutive steps, not across the chosen starting point. These
two types contribute respectively $12c_6$ and $8(r-2)c_4$ to
$\operatorname{tr}(F_6)$. To see the classification, a shortest
closed segment within such a walk is a simple cycle of length at
least four. If it has length six, the whole walk is that cycle.
If its length is four, the remaining two steps must close by the
single initial/final edge; placing a two-step return anywhere in the
interior would violate nonbacktracking. A length-five cycle cannot
be closed by one additional edge in a simple graph.

Substitute $\operatorname{tr}(A^2)=nr$ and
$\operatorname{tr}(A^4)=nr(2r-1)+8c_4$ into this expression for
$\operatorname{tr}(F_6)$. Rearrangement yields (5).

For $n=62$, $r=8$, and $c_4=(93+d)/2$, equation (5) becomes

$$\boxed{\operatorname{tr}(A^6)=151528+168d+12c_6}.\tag{6}$$

## 2. The cubic repeat trace and cycle parity

Every repeat triangle in the present D1-only case has all three
weights equal to one. Indeed, a triangle containing a double edge
$0w$ would have to use its unit mate $a$ as its third vertex, but the
complete D1 rows give $B_{wa}=0$. Hence

$$\operatorname{tr}(B^3)=6u.\tag{7}$$

Put $Q=A^2+A-7I$, so $B=Q-J$ and $Q\mathbf1=65\mathbf1$. Its cube is

$$
Q^3=A^6+3A^5-18A^4-41A^3+126A^2+147A-343I.
$$

The all-ones correction contributes

$$
\operatorname{tr}(-3Q^2J+3QJ^2-J^3)
=62(-3\cdot65^2+3\cdot65\cdot62-62^2)
=-274598.
$$

Using triangle-freeness, simplicity, and the already established traces

$$
\operatorname{tr}(A^5)=10c_5,\quad
\operatorname{tr}(A^4)=7812+4d,\quad
\operatorname{tr}(A^2)=496,
$$

we obtain

$$
\operatorname{tr}(B^3)
=\operatorname{tr}(A^6)+30c_5-72d-373984.
$$

Combining this with (6)--(7) gives

$$6u=12c_6+30c_5+96d-222456,$$

which is the first formula of (1). Substituting the mixed-trace identity
gives its second formula. Reduction modulo two yields

$$\boxed{u\equiv c_5\pmod2}.\tag{8}$$

If the nongenerated unit-triangle clusters consist of $s$ single
triangles and $k$ diamonds, the cluster description in
`CONNECTED_REPEAT_UNIT_TRIANGLE_PATTERNS.md` gives $u=d+s+2k$.
Since $d$ is odd, (8) then says

$$\boxed{c_5\equiv1+s\pmod2}.\tag{9}$$

This last interpretation uses that separate cluster result. Equation
(8) does not require it.

For completeness, another exact mixed trace follows without a walk
classification:

$$
\boxed{\operatorname{tr}(A^2B^2)=1860+28d+6u-\tau}.
\tag{10}
$$

Indeed $A^2=7I+J+B-A$, $\operatorname{tr}(B^2)=186+4d$,
$\operatorname{tr}(JB^2)=558$, and (7) apply. This is an identity,
not an additional independent nonnegativity theorem.

## 3. Completing the square gives an integer-square determinant

Let $M=2A+I$. Then

$$29I+4B=M^2-4J,\qquad M\mathbf1=17\mathbf1.\tag{11}$$

The integer determinant of $M$ is odd because $M\equiv I\pmod2$;
in particular $M$ is invertible. Its integer characteristic polynomial
has the integer root $17$, so $17$ divides $\det M$. Thus

$$S=\det M/17$$

is a nonzero odd integer. The rank-one determinant formula applied
to (11), together with $M^{-2}\mathbf1=\mathbf1/289$, gives

$$
\begin{aligned}
\det(29I+4B)
&=\det(M)^2\bigl(1-4\mathbf1^TM^{-2}\mathbf1\bigr)\\
&=\det(M)^2\left(1-\frac{248}{289}\right)
=41S^2.
\end{aligned}
$$

This proves (2) directly from the actual graph identity. Connectedness
of $B$ is not needed for this determinant equality itself.

## 4. The weighted spanning-tree congruence

Connectedness of the repeat support makes $3$ a simple eigenvalue of
$B$. Write

$$q(x)=\det(xI-B)/(x-3).$$

This is a monic integer polynomial of degree $61$. If
$\mu_1,\ldots,\mu_{61}$ are the other repeat eigenvalues, the
weighted matrix-tree theorem gives

$$q(3)=\prod_{i=1}^{61}(3-\mu_i)=62\kappa(B).\tag{12}$$

The determinant identity says

$$S^2=\prod_{i=1}^{61}(29+4\mu_i).$$

This product is an integer polynomial expression in the coefficients
of $q$. Reducing that expression modulo $41$, where $29\equiv-12$,
gives

$$
S^2\equiv4^{61}\prod_i(\mu_i-3)
=-4^{61}q(3)
\equiv39\kappa(B)\pmod{41}.
$$

For the last coefficient, $4^{61}\equiv4\pmod{41}$ and
$-4\cdot62\equiv39\pmod{41}$. Since $39\equiv11^2$ and
$11^{-1}\equiv15\pmod{41}$, division by $11^2$ gives the second
congruence in (3).

Reducing (2) modulo $17$ gives (4): its left side is
$4^{62}\det(3I+B)\equiv-\det(3I+B)$, and its right side is
$7S^2$. Thus $\det(3I+B)\equiv10S^2\pmod{17}$.

## 5. Equivalent characteristic-polynomial identity

Let $p(t)=\det(tI-A)/(t-8)$. The original graph is connected, so this
is the monic integer polynomial of its $61$ nonprincipal eigenvalues.
On $\mathbf1^\perp$, $B=A^2+A-7I$. Consequently

$$\boxed{q(t^2+t-7)=-p(t)p(-1-t)}.\tag{13}$$

For each nonprincipal adjacency eigenvalue $\lambda$, the paired
factor on the right is
$(t-\lambda)(t+1+\lambda)=t^2+t-\lambda^2-\lambda$; the minus
sign accounts for the odd degree $61$. Formula (13) is another exact
way to express the same spectral relation. It is not an assertion
that a proposed repeat matrix automatically admits an original graph.

## Remaining obstruction and scope

The parity condition (8) restricts the parity of the five-cycle count
using a repeat-triangle statistic that was previously separate from
it. The determinant conditions restrict the entire repeat matrix,
not just its number of double edges. Neither result currently
contradicts any of $d=1,3,5,7,9$.

The open variables include the nongenerated repeat triangles, the
positive mixed-trace root patterns, and the weighted spanning-tree
count of the unknown connected repeat graph. A fixed value of $d$
does not determine these quantities in the arguments above. Treating
the square condition as automatic for every cubic repeat candidate,
or treating the cycle parity as an exclusion without a further bound,
would be unjustified.

No repeat graphs were enumerated, no solver was run, and no claim of
an original graph realization or a complete order-62 contradiction is
made. Independent review of this note remains outstanding.
