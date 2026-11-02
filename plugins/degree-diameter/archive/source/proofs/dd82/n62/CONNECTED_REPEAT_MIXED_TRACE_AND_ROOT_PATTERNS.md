# Mixed trace, five-cycles, and unresolved three-unit root patterns

## Claim and status

**PROVABLE AS STATED:** the mixed-trace identity, port bound, and necessary
root-pattern classification below. This new paper note awaits independent
review. The stronger claim that the mixed trace vanishes is **NOT CURRENTLY
JUSTIFIED**.

Assume an actual legal order-62 graph whose repeat support is connected.
Let $d$ count double-repeat pairs and let $c_5$ count unoriented simple
cycles of length five in the original graph. Then

$$
\tau:=\operatorname{tr}(AB^2)=10c_5+8d-25048,
\qquad
0\le\tau\le248-24d+2L_3,
\tag{1}
$$

where $L_3$ is the number of vertices whose three unit repeat neighbors
are all heavy endpoints. In particular $L_3\le\lfloor2d/3\rfloor$.
For $d=9$, these formulas give $2498\le c_5\le2502$.

Positive mixed trace can occur only at the three-unit rows classified
in Section 5. No contradiction to all five listed local patterns is
proved here, and none is asserted to extend to an actual graph.

## Assumptions and notation

Use the actual identities

$$A\mathbf1=8\mathbf1,\qquad B=A^2+A-7I-J,\qquad
B\mathbf1=3\mathbf1,\qquad AB=BA,$$

with $B$ symmetric, nonnegative, integral, zero-diagonal, and at most two.
Assume connected positive repeat support, as in
`CONNECTED_REPEAT_REDUCTION.md`. Triangle pairing and the D0 component
theorem imply that $G$ is triangle-free and all double repeats are D1.
Use the established consequences

$$d\in\{1,3,5,7,9\},\qquad c_4=(93+d)/2.$$

Let $D$ be the $2d$ heavy endpoints and let $S$ be the union of their
generated unit-repeat triangles. The global disjointness theorem gives
$|S|=3d$, $D\cap S=\varnothing$. Put

$$W=V(G)\setminus(D\cup S),\qquad |W|=62-5d.$$

For each $w$, write $N_B(w)=\{v:B_{wv}>0\}$ and define its weighted
original-edge count inside the repeat neighborhood by

$$
m_B(w)=\sum_{\{u,v\}\subseteq N_B(w)}A_{uv}B_{wu}B_{wv}.
\tag{2}
$$

Every vertex outside $D$ has three distinct unit repeat neighbors.
For $w\in W$, write $m(w)$ for the ordinary number of original edges
among those three vertices, and let

$$\ell(w)=|N_B(w)\cap D|,\qquad
L_3=|\{w\in W:\ell(w)=3\}|.$$

## Strategy and dependencies

Expand the exact repeat polynomial to calculate $\tau$ in terms of
original five-cycles. Then use the explicit D1 rows to show that heavy
and generated vertices make zero contribution, and that heavy neighbors
of every remaining row are isolated in its induced original graph.
Finally classify the possible intersections of the three parent pairs
at a row with positive contribution. The last step identifies the
unresolved configurations instead of assuming $\tau=0$.

The required local rows and nonedges are in
`D1_MATCH_HARD_BRANCH_REDUCTION.md` and
`D1_MATCH_C4_TRANSPORT_REFINEMENT.md`; disjointness and the port
placement are in `GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`. No claim that
all unit repeat triangles are generated is used.

## 1. Exact mixed-trace expansion

Put $Q=A^2+A-7I$, so $B=Q-J$ and $Q\mathbf1=65\mathbf1$. Since
$AJ=8J$ and $J^2=62J$,

$$
\begin{aligned}
\operatorname{tr}(AB^2)
&=\operatorname{tr}(AQ^2)-2\operatorname{tr}(AQJ)
  +\operatorname{tr}(AJ^2)\\
&=\operatorname{tr}(A^5)+2\operatorname{tr}(A^4)
 -13\operatorname{tr}(A^3)-14\operatorname{tr}(A^2)
 +49\operatorname{tr}(A)-33728.
\end{aligned}
$$

The final constant is
$(-2\cdot8\cdot65+8\cdot62)\operatorname{tr}(J)=-544\cdot62$.
Triangle-freeness gives $\operatorname{tr}(A^3)=0$, and simplicity
gives $\operatorname{tr}(A)=0$. Regularity gives
$\operatorname{tr}(A^2)=62\cdot8=496$.

The length-four closed-walk count is

$$
\operatorname{tr}(A^4)
=62\cdot8(2\cdot8-1)+8c_4=7812+4d.
$$

In a triangle-free simple graph every closed walk of length five is a
simple five-cycle with a starting point and orientation. Indeed any
repeated vertex would split it into shorter closed walks of positive
length; the odd one would have length one or three, both impossible.
Thus $\operatorname{tr}(A^5)=10c_5$. Substitution yields

$$\boxed{\tau=10c_5+8d-25048}.\tag{3}$$

## 2. The local interpretation and zero-contribution vertices

Expanding the trace and using symmetry gives

$$\tau=2\sum_w m_B(w).\tag{4}$$

For a D1 heavy endpoint, its repeat neighborhood consists of its heavy
mate and its unit mate. Those two vertices are nonadjacent in the
original graph, by the normalized D1_MATCH template. Hence its
contribution to (4) is zero.

For a normalized generated triangle $\{1,2,3\}$, the complete repeat
rows are

$$B_1=e_2+e_3+e_4,\qquad
B_2=e_1+e_3+e_b,\qquad
B_3=e_1+e_2+e_c.$$

The first support lies inside the independent neighborhood of the
heavy root. In the second, $b$ is an ordinary single-parent point
whose parent is outside $\{1,2,3\}$; it is therefore nonadjacent
to $1,3$, which are also mutually nonadjacent. In the third, $c$ is
an ordinary single-parent point with parent outside $\{1,2,3\}$,
so $\{1,2,c\}$ is independent as well. Thus every vertex in $S$
also has zero contribution.

Every vertex of $W$ has three unit repeat neighbors, so (4) reduces to

$$\tau=2\sum_{w\in W}m(w).\tag{5}$$

## 3. Heavy-neighbor ports and the upper bound

Every heavy endpoint has one unit mate. The D1 light-mate theorem puts
that mate outside both $D$ and $S$. Consequently

$$\sum_{w\in W}\ell(w)=2d.\tag{6}$$

Moreover every heavy endpoint among the three repeat neighbors of a
vertex $w\in W$ is isolated in their induced original graph. To verify
this, root the D1 structure at that endpoint, denoted $0$. Its unit
mate is $w=a$, with the established complete row

$$B_a=e_0+e_p+e_q.$$

The vertices $p,q$ are ordinary outside points relative to root $0$,
so neither is adjacent to $0$ in the original graph. This proves the
claimed isolation, independently for every heavy neighbor of $w$.

The induced original graph on three vertices is triangle-free, and
its $\ell(w)$ heavy vertices are isolated. Therefore

$$m(w)\le2-\ell(w)+\mathbf1_{\ell(w)=3}.\tag{7}$$

For $\ell=0,1,2,3$, the right side is respectively $2,1,0,0$.
Summing (7), using (5)--(6), gives

$$
\boxed{0\le\tau\le248-24d+2L_3},\qquad
3L_3\le2d.
\tag{8}
$$

## 4. Numerical consequences and the conditional zero-trace case

Combining (3) and (8) gives the following necessary ranges. These are
integer consequences of the proved formulas, not existence claims.

| $d$ | Upper bound on $\tau$ after eliminating $L_3$ | Range for $c_5$ |
|---|---:|---|
| $1$ | $224$ | $2504\le c_5\le2526$ |
| $3$ | $180$ | $2503\le c_5\le2520$ |
| $5$ | $134$ | $2501\le c_5\le2514$ |
| $7$ | $88$ | $2500\le c_5\le2508$ |
| $9$ | $44$ | $2498\le c_5\le2502$ |

If $\tau=0$ were proved, equation (3) modulo ten would force
$d\equiv1\pmod5$. In the established five-value set this leaves only
$d=1$, and then $c_5=2504$. This is a conditional implication;
no proof of $\tau=0$ is supplied.

## 5. Precise local patterns that can still contribute positively

Suppose $m(w)>0$. Then $w\in W$ and its complete repeat row is
$B_w=e_a+e_b+e_c$. All three repeat mates are original nonneighbors
of $w$. For each $z\in\{a,b,c\}$ put

$$P_z=N_G(w)\cap N_G(z),\qquad |P_z|=2.$$

The three parent pairs are distinct. If, for example,
$P_a=P_b=\{h_1,h_2\}$, then $h_1,h_2$ have the three common
neighbors $w,a,b$. They are nonadjacent because they lie in the
independent set $N_G(w)$. The bound $B\le2$ makes them a double pair
whose generated triangle is exactly $\{w,a,b\}$. This would put
$w$ in $S$, contrary to its positive contribution.

An original edge between two of $a,b,c$ requires their parent pairs
to be disjoint: a shared parent would create an original triangle.
Form the simple three-edge graph $F_w$ on $N_G(w)$ whose edges are
$P_a,P_b,P_c$. Because $m(w)>0$, it contains two disjoint edges.
Ignoring isolated vertices, the only possible such three-edge graphs
are a three-edge matching, a two-edge path plus a disjoint edge, and
a three-edge path. Triangle-freeness of $G[\{a,b,c\}]$ gives exactly
the following necessary possibilities:

| Parent-pair graph $F_w$ | Possible positive original graph on $\{a,b,c\}$ |
|---|---|
| Three disjoint edges | One edge, or a two-edge path |
| A two-edge path plus a disjoint edge | One edge, or a two-edge path; every edge joins the mate of the disjoint parent pair to one of the other two mates |
| A three-edge path | Exactly one edge, between the mates corresponding to its two end edges |

These are five cases when the two rows with two possibilities are
split. Any heavy mate must be isolated, so a two-edge path can occur
only when $\ell(w)=0$. A single-edge contribution permits at most
one heavy mate, necessarily the isolated third mate.

One additional description connects a remaining case to nongenerated
unit triangles. In the second row, suppose both possible original
edges occur, say $a\sim b\sim c$, while $P_a,P_c$ share one parent
$h$ and $P_b$ is disjoint from both. The pair $a,c$ has common neighbors
$h,b$. The repeat mates $a,c$ cannot be heavy endpoints, by the
preceding isolation property. They are nonadjacent and have the two
distinct common neighbors $h,b$, so $B_{ac}\ge1$; as neither endpoint
is heavy, $B_{ac}\le1$. Thus $B_{ac}=1$, and $\{w,a,c\}$ is a unit
repeat triangle.
Its three vertices have exactly one common original neighbor, namely
$h$, because $P_a\cap P_c=\{h\}$. This is a type-one nongenerated
unit triangle in `CONNECTED_REPEAT_UNIT_TRIANGLE_PATTERNS.md`, not
an already excluded generated triangle.

## Remaining obstruction to zero mixed trace

Even at a D1 light mate, the current local results leave a concrete
case undecided. Its row is $B_a=e_0+e_p+e_q$, and the heavy endpoint
$0$ is isolated in that repeat neighborhood. Thus

$$m(a)=A_{pq}.$$

The C4 transport paper proves $B_{pq}=0$ and places $p\in C_3$,
$q\in C_4$. It also proves that the original edges between these
classes form a five-edge matching, missing $u_3$ and $W_4$;
$p\ne u_3$ and $q\ne W_4$. These facts do not determine whether
the matching pairs $p$ with $q$. In particular, $B_{pq}=0$ cannot
be read as $A_{pq}=0$.

No actual graph realizing $p\sim q$ or any other positive-contribution
pattern has been constructed. The point is the missing implication:
the established row and matching conclusions have not excluded these
original edges. A proof of zero mixed trace must eliminate all positive
patterns in Section 5, or derive a different identity forcing their
total count to vanish. The trace and port bounds alone do not do so.

No solver, finite graph search, new formal axiom, or assumption that all
unit repeat triangles are generated is used in this note.
