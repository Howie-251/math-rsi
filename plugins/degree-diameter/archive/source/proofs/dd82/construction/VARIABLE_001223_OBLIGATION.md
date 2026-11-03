# The (0,0,1,2,2,3) quotient is impossible

Date: 2026-10-12. This is a direct matrix and route-count contradiction.
It uses no new enumeration, no configuration classification, no graph
search, and no assumption about repartitioning the graph.

## Claim and normalization

There is no simple eight-regular diameter-two graph admitting an equitable
partition into six ten-vertex fibers with

$$d=(0,0,1,2,2,3),\qquad
Q=\begin{pmatrix}
0&1&3&0&3&1\\
1&0&3&3&0&1\\
3&3&0&0&0&1\\
0&3&0&0&2&1\\
3&0&0&2&0&1\\
1&1&1&1&1&0
\end{pmatrix}.\tag{1}$$

This represents orbit 1, containing two degree-preserving labeled
matrices in
[the completed variable-degree quotient screen](../../../computations/dd82/construction/six_fiber_variable_internal_run/verification.json).

Write $F_{ab}$ for the interface matrix with rows in fiber $a$ and columns
in fiber $b$. Undirectedness gives $F_{ba}=F_{ab}^T$.
Each interface between the hub fiber 5 and an outer fiber is a perfect
matching. Fix coordinates on fiber 5 and independently relabel each
outer fiber by its matched hub neighbor. Then

$$F_{a5}=F_{5a}=I_{10}\qquad(0\le a\le4).\tag{2}$$

Let $S,T,U,P$ be the internal adjacency matrices on fibers $2,3,4,5$,
respectively. They have degrees $1,2,2,3$ and zero diagonal. Fibers 0 and 1
have no internal edges. Define

$$X=F_{02},\quad Y=F_{04},\quad Z=F_{12},\quad W=F_{13},
\qquad K=J_{10}-I_{10}.$$

All four displayed interface matrices are zero-one with every row and
column sum three. The degree-one interface $F_{01}$ and degree-two
interface $F_{34}$ are unrestricted; the equations used below do not
depend on their values.

## Four exact route equations

The quotient defect matrix for (1) is

$$D=(\operatorname{diag}(d)+Q)^2+\operatorname{diag}(d)+Q
-7I_6-10J_6
=\begin{pmatrix}
3&1&0&0&0&1\\
1&3&0&0&0&1\\
0&0&4&0&0&1\\
0&0&0&3&1&1\\
0&0&0&1&3&1\\
1&1&1&1&1&0
\end{pmatrix}.$$

In particular the four pairs $(0,4),(2,4),(1,3),(2,3)$ have zero defect.
Their complete direct and two-step route matrices are as follows:

| Oriented pair | Direct and endpoint-fiber contributions | Other intermediate fibers | Total row count |
| --- | --- | --- | ---: |
| $0\to4$ | $Y+YU$ | Hub contributes $I$; fibers 1, 2, 3 contribute zero | $3+6+1=10$ |
| $2\to4$ | Zero, since $q_{24}=0$ | Fiber 0 contributes $X^TY$; hub contributes $I$; fibers 1, 3 contribute zero | $9+1=10$ |
| $1\to3$ | $W+WT$ | Hub contributes $I$; fibers 0, 2, 4 contribute zero | $3+6+1=10$ |
| $2\to3$ | Zero, since $q_{23}=0$ | Fiber 1 contributes $Z^TW$; hub contributes $I$; fibers 0, 4 contribute zero | $9+1=10$ |

Each matrix must be entrywise at least $J_{10}$ to give diameter two.
Because its row sum is exactly ten, it equals $J_{10}$. Consequently

$$Y(I+U)=K,\qquad X^TY=K,\tag{3}$$
$$W(I+T)=K,\qquad Z^TW=K.\tag{4}$$

These equations allow arbitrary interfaces, with no symmetry relation
between $X,Y,Z,W$ imposed in advance.

## The equations force two diagonal matchings

The matrix $K=J_{10}-I_{10}$ has eigenvalues $9$ once and $-1$ nine times,
so it is invertible. The first equation in (3) therefore makes $Y$
invertible. Since $Y$ has both row and column sum three,

$$YJ=JY=3J,\qquad YK=KY.$$

Its inverse also commutes with $K$. Thus the two equations in (3) give

$$X^T=KY^{-1}=Y^{-1}K=I+U.\tag{5}$$

Likewise (4) makes $W$ invertible, and $W$ commutes with $K$. Hence

$$Z^T=KW^{-1}=W^{-1}K=I+T.\tag{6}$$

Since $T$ and $U$ have zero diagonal, both $X^T$ and $Z^T$ have diagonal
entries equal to one. These are consequences of coverage, not additional
matching assumptions.

## The hub block now has too many routes to one target

For the pair $2\to5$, the direct route is $I$. A path whose intermediate
vertex is in fiber 2 contributes $S$, and one whose intermediate vertex
is in fiber 5 contributes $P$. The other possible intermediate fibers
are 0 and 1, contributing $X^T$ and $Z^T$ respectively by (2).
Fibers 3 and 4 contribute zero. Its complete route matrix is therefore

$$C=I+S+P+X^T+Z^T.\tag{7}$$

Every row of $C$ sums to

$$1+1+3+3+3=11.$$

But (5)--(6), and the zero diagonals of $S,P,T,U$, give

$$C_{uu}=1+0+0+1+1=3\qquad\text{for every coordinate }u.$$

Diameter two requires the other nine entries in row $u$ to be at least
one as well, forcing that row sum to be at least $3+9=12$. This contradicts
the actual row sum eleven. Here $C_{uu}$ refers to different vertices in
fibers 2 and 5 with the same normalized coordinate; it is a cross-fiber
target and must be covered just like the other nine targets.

Thus (1) is unrealizable, and its entire two-matrix orbit is excluded.
No repartition theorem is needed.

## Updated scope

The complete variable-degree screen in
[SIX_FIBER_VARIABLE_INTERNAL_DEGREE.md](SIX_FIBER_VARIABLE_INTERNAL_DEGREE.md)
left 98 labeled matrices in four orbits. Its twelve-matrix five-cycle
orbit was excluded there. The sixty-matrix orbit with the same
$d=(1,1,1,1,1,3)$ tuple was excluded in
[VARIABLE_D1_FIVE_ONE_BRIDGE_EXCLUSION.md](VARIABLE_D1_FIVE_ONE_BRIDGE_EXCLUSION.md).
The present proof excludes the two-matrix $(0,0,1,2,2,3)$ orbit.

Exactly **24 labeled necessary quotients in one orbit**, with internal
degrees $(1,1,1,1,3,3)$, remain unexcluded from that nonuniform screen.
No claim about that orbit or arbitrary sixty-vertex graphs is made here.
