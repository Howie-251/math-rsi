# HS58 with two old deletions: no universal auxiliary vertex

Date: 2026-10-12. The new argument below excludes a universal vertex
in the eight-vertex auxiliary graph whenever at least five old
nonedges are added. It does not assume any particular arrangement of
the other auxiliary edges or of the two deleted HS edges. Combined
with the existing results for at most four additions, it excludes
universal auxiliary vertices at every addition count. No nonuniversal
auxiliary graph is addressed here, and no computation is used.

## Setting and the zero-port identity

Let Q be HS50. Delete exactly two original edges D, add a original
nonedges A among the old vertices, and add eight new vertices. Suppose
the resulting graph G is eight-regular and has diameter two. Write
M=Q-D+A for the old graph, H for the new graph, and B_x for the new
neighbors of an old vertex x. Set

\[
r_x=d_D(x),\qquad a_x=d_A(x),\qquad
p_x=|B_x|=1+r_x-a_x\ge0.
\]

Thus sum_x r_x=4, sum_x a_x=2a, and sum_x p_x=54-2a.
Let Z={x:p_x=0}, z=|Z|, and E=sum_x max(p_x-1,0). Counting ports
relative to one port per old vertex gives

\[
z=E+2a-4.                                           \tag{1}
\]

Assume H has a universal vertex c. Its H-degree is seven, so it has
exactly one old neighbor v. In particular p_v>=1. A zero-port old
vertex q can reach c within two steps only through v: q has no new
neighbor that could serve as an intermediary. Consequently

\[
Z\subseteq N_M(v),\qquad
z\le d_M(v)=8-p_v\le7.                             \tag{2}
\]

Equations (1)-(2) immediately give a<=5. This already excludes every
a>=6 without further properties of Q.

## Five additions force at most one excess port

Now a=5. Equations (1)-(2) imply z=E+6<=7, so E is zero or one.
Moreover p_v cannot exceed one: if p_v>=2, then E>=1 and z>=7,
whereas d_M(v)=8-p_v<=6. Thus

\[
p_v=1,\qquad a_v=r_v.                               \tag{3}
\]

For a zero-port vertex x, one has a_x=1+r_x. Write
r(Z)=sum_(x in Z)r_x. The total added degree on Z is therefore
z+r(Z), while the total added degree outside Z is 10-z-r(Z).

### No excess port

If E=0, every positive-port vertex has exactly one port and z=6.
A zero-port vertex has eight old neighbors and can reach new
vertices only through those neighbors. Covering all eight new
vertices requires all eight old neighbors to have positive ports.
In particular A has no edge with both endpoints in Z.

Every A incidence at Z must then be paired with an incidence outside
Z. But the two available totals are

\[
\sum_{x\in Z}a_x=6+r(Z),\qquad
\sum_{x\notin Z}a_x=4-r(Z),
\]

and the former is larger. This is impossible.

### One excess port

If E=1, there is a unique vertex t with p_t=2, all other positive
ports equal one, and z=7. By (3), t is different from v. Equation
(2) is an equality, so Z=N_M(v).

Let q belong to Z, and let k_q be its number of zero-port neighbors
in M. Its eight old neighbors supply at most

\[
8-k_q+\mathbf 1_{\{qt\in E(M)\}}
\]

ports. Hence diameter two forces k_q<=1, and whenever k_q=1,
the edge qt belongs to M.

Let e_ZZ and e_PP count the edges of A internal to Z and its
complement, respectively. Subtracting the added-degree totals on
the two sides gives

\[
2(e_{ZZ}-e_{PP})
=(7+r(Z))-(3-r(Z))=4+2r(Z).
\]

Thus e_ZZ>=2+r(Z)>=2. Since every zero-port vertex has at most one
zero-port M neighbor, these e_ZZ edges have distinct endpoints.
At least four distinct vertices q of Z therefore have a zero-port
old neighbor. Each must also be adjacent to t in M, and all are
adjacent to v. It follows that

\[
|N_M(v)\cap N_M(t)|\ge4.                            \tag{4}
\]

HS50 has at most one common Q neighbor for any distinct pair. Every
M common neighbor of v,t that was not a Q common neighbor requires
an added edge incident to v or t. Deletions cannot increase the
number. Therefore

\[
|N_M(v)\cap N_M(t)|\le1+a_v+a_t.
\]

Using p_v=1 and p_t=2 gives a_v=r_v and a_t=r_t-1, so the last
bound is r_v+r_t. The two distinct vertices v,t have combined
deleted degree at most three in a simple graph with only two edges:
combined degree four would require both edges to join the same
pair. Thus

\[
|N_M(v)\cap N_M(t)|\le r_v+r_t\le3,
\]

contradicting (4). This argument allows r_v=0; it does not assume
that the center's old neighbor is a deletion endpoint.

## Connection to the earlier addition counts

The degree count gives |E(H)|=5+a. For a<=1 this is less than seven,
so H cannot have a universal vertex at all. The remaining smaller
counts are excluded by the existing proofs:

* a=2: [two-addition exclusion](HS58_TWO_DELETE_TWO_ADDITIONS_EXCLUSION.md).
* a=3: [universal auxiliary case](HS58_TWO_DELETE_THREE_ADDITIONS_UNIVERSAL_H.md).
* a=4: universal type 1 in the
  [integrated four-addition proof](HS58_TWO_DELETE_FOUR_ADDITIONS_EXCLUSION.md), and
  universal type 6 in the
  [center neighbor in W](HS58_FOUR_ADD_UNIVERSAL_TYPE6_V_IN_W.md) and
  [remaining endpoint closure](HS58_FOUR_ADD_UNIVERSAL_TYPE6_ENDPOINT_REDUCTION.md)
  arguments. The complete chain and this new a>=5 argument have been
  read and checked by the root agent. External C17/delta review remains
  unfinished after Google authentication errors; it is not recorded
  as accepted.

Together these arguments rule out a universal H for exactly two
deleted HS edges and any number of old nonedge additions. The new
a>=5 proof is independent of the small-H catalog, the type-6 solver
run that returned UNKNOWN, and all actual seed graphs.
