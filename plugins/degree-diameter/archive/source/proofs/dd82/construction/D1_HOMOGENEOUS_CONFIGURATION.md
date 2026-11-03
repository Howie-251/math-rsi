# The cyclically homogeneous configuration family has no left q1 completion

Date: 2026-10-12. This is one complete, bounded computation for a specified
subfamily of the surviving six-fiber quotient. It does **not** exclude the
general d1 model. No complete sixty-vertex graph was produced in this run.

## Precisely the family tested

Index the six fibers by $L_a,R_a$, $a\in\mathbb Z_3$, with ten coordinates
per fiber. Choose one of the ten supplied cubic incidence matrices $Z$
from the [configuration/interface catalog](../../../computations/dd82/construction/d1_10_3_catalog/local_interfaces.json).
All three $L_aR_a$ interfaces equal this same $Z$. All three
$L_aR_{a+1}$ interfaces equal a common degree-two matrix $Y$; the remaining
three left-right interfaces are empty. The internal matchings are a
common $S_L$ on the left and a common $S_R$ on the right. Require

$$S_L+YY^T+ZZ^T=J+4I,\qquad
S_R+Y^TY+Z^TZ=J+4I.\tag{1}$$

Each $S_L$ or $S_R$ is any perfect matching of its corresponding leave,
as listed in the local catalog. Finally the three oriented interfaces
$L_a\to L_{a+1}$ equal one permutation matrix $M_L$, and the three
$R_a\to R_{a+1}$ equal one permutation matrix $M_R$. Reverse directions
are transposes. These common-coordinate and common-permutation requirements
are restrictions on the family, not conclusions about arbitrary d1 graphs.

## Every compatible Y is generated

Put $C_L=\operatorname{leave}(Z)-S_L$ and
$C_R=\operatorname{leave}(Z^T)-S_R$. Equation (1) says

$$YY^T=2I+C_L,\qquad Y^TY=2I+C_R.$$

Every column of $Y$ has two ones, so it represents an edge of $C_L$.
There are ten columns and ten edges, and no two columns can represent
the same edge, since off-diagonal entries of $YY^T$ are at most one.
Thus the columns are exactly the edges of $C_L$. Their labeling by
the ten right coordinates is an isomorphism from $C_R$ to the line graph
of $C_L$. Conversely every such isomorphism supplies a compatible $Y$.

Both factors are unions of cycles. Consequently their cycle-length
multisets must agree. For each length $\ell$ occurring $c_\ell$ times,
pair the components arbitrarily, and choose a rotation and either
orientation on each cycle. This produces exactly

$$\prod_\ell (2\ell)^{c_\ell}c_\ell!$$

matrices for each compatible pair $(S_L,S_R)$. The
[preparation code](../../../computations/dd82/construction/d1_homogeneous_configuration_prepare.py)
implements precisely these pairings, rotations, and reflections. It checks
degree two on both sides, absence of duplicate $Y$ within each matching
pair, and all one hundred entries of each equation in (1) for every
generated matrix.

The resulting counts for configuration numbers 1 through 10 are

$$7200,720,720,7200,968,936,936,1584,1296,3100,$$

totaling **24,660**. These counts agree with the independently calculated
cycle-automorphism totals. The preparation took 1.290959167 CPU seconds;
its results are [recorded here](../../../computations/dd82/construction/d1_homogeneous_configuration_run/preparation.json).

## Exact q1 equation and exhaustive local search

For $L_a\to L_{a+1}$, the direct edge, paths through the two endpoint
fibers, the remaining left fiber, and the common right neighbor give

$$M_L+S_LM_L+M_LS_L+(M_L^T)^2+YZ^T=J.\tag{2}$$

The corresponding right equation has $S_R,M_R$ and fixed product $Z^TY$.
The direction of the square in (2) follows because both steps through
$L_{a-1}$ are opposite the chosen cyclic orientation.

Write $S_L[u,s(u)]=1$, $M_L[u,m(u)]=1$, and $R=J-YZ^T$.
Each product entry of $YZ^T$ is at most one: an entry at least two would
give two columns sharing both a row of $Y$ and a row of $Z$, contradicting
the off-diagonal disjointness of $Y^TY$ and $Z^TZ$ in (1).
Hence $R$ is a zero-one matrix with row and column sums four.

Equation (2) requires the four distinct targets

$$m(u),\quad m(s(u)),\quad s(m(u)),\quad m^{-2}(u)\tag{3}$$

to be exactly the support of row $u$ of $R$. In particular an arrow
$u\mapsto v$ is allowed only if

$$R_{u,v}=R_{s(u),v}=R_{u,s(v)}=1.$$

It cannot have $u=v$, since then $M_L$ and $(M_L^T)^2$ overlap. Two
assigned arrows cannot satisfy $m(s(u))=s(m(u))$, because the middle
two terms in (3) would overlap. If $u\mapsto v\mapsto w$ is already
assigned, the inverse-square term forces $R_{w,u}=1$ and must be disjoint
from every already determined one of the other three targets in row $w$.
All these restrictions are necessary; none assumes a converse.

The [C++ search](../../../computations/dd82/construction/d1_homogeneous_configuration_search.cpp)
backtracks over these allowed arrows, choosing an unassigned row with the
fewest unused targets and enforcing the stated restrictions. Distinct
column targets enforce bijectivity. A complete assignment would be
checked against all ten exact four-target equalities (3). Thus no possible
solution of (2) is discarded without violating a necessary condition.
The right search is called only after a left solution exists.

## Actual completed result

The single invocation processed **24,660 of 24,660** inputs, with
**24,804 backtracking nodes**, zero complete permutation leaves, and
**zero left q1 solutions in every configuration type**. It stopped because
the finite family was exhausted, not because the CPU limit was reached.
The [full result](../../../computations/dd82/construction/d1_homogeneous_configuration_run/search.json)
records `complete: true` and `stop_reason: complete_family`.

Actual process CPU was **0.109783 seconds**, wall time **0.110905 seconds**,
and peak resident memory **7,488 KiB**, with one thread. The
[runner](../../../computations/dd82/construction/d1_homogeneous_configuration_run.py)
used a ten-second internal CPU cap, an eleven-second operating-system
soft limit, and a 4 GiB address-space limit;
[resource values](../../../computations/dd82/construction/d1_homogeneous_configuration_run/resources.json)
and the complete generated input table are retained.

Because no left solution exists, the right solver and full-graph expansion
were never reached. Their zero counters do not assert that all isolated
right equations were independently searched. There is no candidate edge
list, best bad-pair score, or BFS witness to report.

For reference, a pair of local solutions would still have needed the
following additional equations, followed by independent graph BFS:

$$M_LY+M_L^TZ+ZM_R^T+YM_R=J\qquad(q=0),$$
$$Y+S_LY+YS_R+M_LZ+ZM_R\ge J\qquad(q=2),$$
$$Z+S_LZ+ZS_R+M_L^TY+YM_R^T\ge J\qquad(q=3).$$

The conclusion is exactly that the common-$Z$, common-$Y$, cyclically
homogeneous $M_L/M_R$ construction specified above has no completion
among the ten supplied configuration types and all their leave matchings.
It does not close independent high-degree interfaces or independent
matchings around the quotient triangles. No additional variant or
second search invocation was run.
