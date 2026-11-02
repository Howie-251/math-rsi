# The type-one center graph has no four-cycle

## Claim and status

**PROVABLE AS STATED:** in the connected-repeat setting of
`CONNECTED_REPEAT_TRIANGLE_WITNESS_REFINEMENT.md`, the graph of type-one
unit triangles and their centers has no component isomorphic to $C_4$.
Together with the prior necessary component list, every component is
therefore one of

$$K_1,\qquad K_2,\qquad P_3,\qquad P_4.$$

This is a new strengthening awaiting independent review. The path
$P_4$ is not excluded here; its exact local configuration is recorded
below to distinguish the remaining case from the excluded cycle.

## Assumptions and notation

Use an actual order-62, degree-eight, diameter-two graph with connected
positive support of $B=A^2+A-7I-J$. The graph is triangle-free, all
double repeats are D1, and generated triangles meet no other unit
triangle. For distinct vertices,

$$|N_G(r)\cap N_G(s)|+A_{rs}=1+B_{rs}. \tag{1}$$

A type-one unit triangle $T$ has exactly one common original neighbor,
its center $c(T)$. The centers are distinct for distinct triangles.
If $T=\{x,y,z\}$ has center $a$ and its additional pair witnesses
are $r_{xy},r_{yz},r_{zx}$, its complete repeat row is

$$B_a=e_{r_{xy}}+e_{r_{yz}}+e_{r_{zx}}. \tag{2}$$

Each additional witness is adjacent to exactly its indicated two
vertices of $T$. These facts are proved in
`CONNECTED_REPEAT_UNIT_TRIANGLE_PATTERNS.md`.

The center graph $\Gamma$ has the type-one triangles as vertices;
$T,T'$ are adjacent exactly when $c(T)\in T'$, equivalently when
$c(T')\in T$. Adjacent triangles are disjoint, and two neighbors
of the same vertex are the two triangles of a diamond. The earlier
paper proves that components can only be $K_1,K_2,P_3,P_4,C_4$.

## Strategy

Normalize the two diamonds forced by a center four-cycle. The exact
center rows force both tips of one diamond to have the same two
original neighbors. This contradicts the missing repeat edge between
those tips. For comparison, perform the corresponding normalization
for a four-vertex path and retain only the consequences actually
proved there.

## 1. Normalization of a four-cycle

Suppose $\Gamma$ has a $C_4$ component. Its alternating vertices are
the two triangles of one diamond, and the other two vertices are
the triangles of a disjoint diamond. Write them as

$$T_z=\{x,y,z\},\quad T_w=\{x,y,w\},\qquad
  T_u=\{a,b,u\},\quad T_v=\{a,b,v\},$$

where $x,y$ and $a,b$ are the shared-edge endpoints, while $z,w$
and $u,v$ are the tips. The eight displayed vertices are distinct.

The centers of $T_z,T_w$ both lie in $T_u\cap T_v=\{a,b\}$.
They are distinct, so label $a,b$ so that $c(T_z)=a,c(T_w)=b$.
The centers of $T_u,T_v$ similarly are the two distinct vertices
$x,y$. Label $x,y$ so that

$$\boxed{c(T_z)=a,\quad c(T_w)=b,\quad
  c(T_u)=x,\quad c(T_v)=y.} \tag{3}$$

These two label choices are independent and do not change the
triangles themselves.

The two centers $a,b$ are common original neighbors of $x,y$.
Since $B_{xy}=1$ and $x,y$ are originally nonadjacent, they are the
exact common-neighbor pair:

$$N_G(x)\cap N_G(y)=\{a,b\}. \tag{4}$$

In particular $u\not\sim_G y$ because $u\sim_G x$, and
$v\not\sim_G x$ because $v\sim_G y$, by (3)--(4).

## 2. The exact center rows force a missing repeat

The repeat row of $a$ in its diamond is

$$B_a=e_b+e_u+e_v.$$

As the center of $T_z$, its extra witness for $x,y$ is $b$ by (4).
The two remaining vertices $u,v$ in this row must supply the extra
witnesses for $x,z$ and $y,z$, respectively. Since $u$ is adjacent
to $x$ but not $y$, and $v$ to $y$ but not $x$, the assignment is
forced:

$$u\sim_G z,\qquad v\sim_G z. \tag{5}$$

At the other center,

$$B_b=e_a+e_u+e_v.$$

The same argument for $T_w$, now with $a$ as the extra witness for
$x,y$, forces

$$u\sim_G w,\qquad v\sim_G w. \tag{6}$$

Consequently $z,w$ have the two distinct common original neighbors
$u,v$. Equation (1) then gives $B_{zw}\ge1$. But $z,w$ are the
tips of a unit diamond, so $B_{zw}=0$. A positive repeat between
them would complete a unit $K_4$, which exhausts its four repeat
rows and contradicts connected support on 62 vertices. This is the
required contradiction. Therefore $\Gamma$ has no $C_4$ component.
$\square$

## 3. The four-vertex path has a different forced pattern

Suppose instead that $\Gamma$ has a $P_4$ component. Label its vertices
in path order as

$$T_z,\quad T_u,\quad T_w,\quad T_v,$$

with the same two diamond vertex sets as above. The two internal
centers lie on shared edges, while each endpoint center belongs only
to its one neighboring triangle. After relabeling,

$$\boxed{c(T_z)=u,\quad c(T_w)=a,\quad
  c(T_u)=x,\quad c(T_v)=w.} \tag{7}$$

For example $c(T_z)$ lies in $T_u$ but not $T_v$, so it is the tip
$u$, not a shared-edge endpoint. This is the distinction from (3).

The unit-repeat common-neighbor identities give

$$N_G(x)\cap N_G(y)=\{u,a\},\qquad
  N_G(a)\cap N_G(b)=\{x,w\}. \tag{8}$$

The center row $B_a=e_b+e_u+e_v$ for $T_w$ has extra $x,y$ witness
$u$. Since $b\sim_G x$ and $b\not\sim_G y$ by (7)--(8), its
other two witnesses force $b\sim_G w$ and $v\sim_G y,w$.
The center row $B_x=e_y+e_z+e_w$ for $T_u$ has extra $a,b$ witness
$w$; the other two witnesses similarly force $y\sim_G a,u$ and
$z\sim_G b,u$.

Using these incidences and the uniqueness of each center, the complete
original cross-incidence matrix between the two four-sets is

$$A[\{x,y,z,w\},\{a,b,u,v\}]
 =\begin{pmatrix}
1&1&1&0\\
1&0&1&1\\
0&1&1&0\\
1&1&0&1
\end{pmatrix}. \tag{9}$$

For the zeros not already supplied by (8), $x\not\sim_G v$ follows
because otherwise $T_v$ would have centers $x,w$. An edge $za$ would
give $T_z$ centers $u,a$, so $z\not\sim_G a$. An edge $wu$ would
give $T_u$ centers $x,w$, so $w\not\sim_G u$. Finally $z\not\sim_G v$:
if that edge existed, the tips $u,v$ of the second diamond would
have both $y$ and $z$ as common neighbors, contradicting $B_{uv}=0$.

Each of the two four-sets is independent in the original graph. All
positive diamond repeats are original nonedges. The two missing tip
pairs are also original nonedges, since $z,w$ share the neighbor $b$
and $u,v$ share the neighbor $y$ in the triangle-free original graph.
Thus (9) describes the entire original induced graph on these eight
vertices; it has eleven edges.

There are two additional distinct outside witnesses. Since $u$ is
the center of $T_z$, its row has the form

$$B_u=e_a+e_b+e_p,\qquad p\sim_G y,z.$$

Since $w$ is the center of $T_v$, its row similarly has the form

$$B_w=e_x+e_y+e_q,\qquad q\sim_G b,v.$$

Inspection of (9) and the independent four-sets shows that neither
$p$ nor $q$ is among the eight displayed vertices. Also $p\ne q$:
if they coincided, the edges $p z$, $p b$, and $z b$ would form an
original triangle. Their remaining rows are undetermined.

The other two outside ports, at $z$ and $v$, have not been proved
to lie outside these eight vertices: they may potentially be joined
to each other by a repeat edge. No zero repeat across all pairs of
the two diamonds is assumed here.

## Remaining scope

The contradiction in Section 2 uses the centers at both shared-edge
endpoints of the opposite diamond. Endpoint centers in a $P_4$ lie
at tips instead, and the resulting configuration (9) does not give
the same duplicated common neighbors. The $P_4$ case remains open,
as do $K_1,K_2,P_3$ center components and type-zero unit triangles.
The partial pattern is a necessary condition, not a construction or
an assertion of global realizability.
