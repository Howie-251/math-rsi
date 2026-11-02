# Excluding the remaining five-matching-fiber quotient by the existing bridge screen

The later [two-matrix analytic exclusion](VARIABLE_001223_OBLIGATION.md)
and [local hub obstruction](VARIABLE_HUB_LOCAL_ASSEMBLY.md) exclude the
remaining 26 matrices after this proof; see
[the integrated frontier](SIX_FIBER_EQUITABLE_MODEL_FRONTIER.md).

Date: 2026-10-12. This proof reuses the completed general bridge enumeration.
No new quotient, interface, graph, or SAT enumeration is required or run.
The earlier variable-degree enumeration record is left unchanged.

## Claim and the precise quotient

There is no eight-regular diameter-two graph with an equitable partition
into six ten-vertex fibers having internal degrees

$$d=(1,1,1,1,1,3)$$

and cross-degree matrix

$$Q=\begin{pmatrix}
0&0&0&3&3&1\\
0&0&3&1&2&1\\
0&3&0&2&1&1\\
3&1&2&0&0&1\\
3&2&1&0&0&1\\
1&1&1&1&1&0
\end{pmatrix}.\tag{1}$$

This is orbit 3, of size sixty under degree-preserving relabeling, in
[the saved quotient verification](../../../computations/dd82/construction/six_fiber_variable_internal_run/verification.json).
The claim permits different interfaces on every pair, different internal
matchings, and an arbitrary internal cubic graph in fiber 5.

Let $F_{ab}$ have source fiber $a$ as its rows and target fiber $b$ as its
columns, so $F_{ba}=F_{ab}^T$. Let $S_a$ be the actual internal matching
matrix for $a=0,1,2,3,4$.

## The exact local equations needed

For a hypothetical graph, put

$$B=A^2+A-7I_{60}-J_{60}.$$

Diameter two makes $B$ entrywise nonnegative. Its quotient under this
partition is $D=R^2+R-7I_6-10J_6$, where $R=\operatorname{diag}(d)+Q$.
For (1) the saved, directly checked matrix is

$$D=\begin{pmatrix}
4&0&0&0&0&1\\
0&0&4&0&0&1\\
0&4&0&0&0&1\\
0&0&0&0&4&1\\
0&0&0&4&0&1\\
1&1&1&1&1&0
\end{pmatrix}.\tag{2}$$

In particular $D_{aa}=0$ for $a=1,2,3,4$, so the corresponding diagonal
blocks of $B$ vanish. Define the oriented cubic interfaces and the bridge

$$Z_i=F_{30},\qquad Z_j=F_{12},\qquad Y=F_{32}.$$ 

Each $Z$ has row and column sums three; $Y$ has row and column sums two.
Fiber 3 has, besides $Z_i,Y$, exactly two degree-one external interfaces,
to fibers 1 and 5. Their returning products and $S_3^2$ are all identity
matrices. Thus its zero diagonal defect block gives

$$S_3+YY^T+Z_iZ_i^T=J_{10}+4I_{10}.\tag{3}$$

The same calculation in fiber 2, whose cubic interface is $F_{21}=Z_j^T$,
gives

$$S_2+Y^TY+Z_j^TZ_j=J_{10}+4I_{10}.\tag{4}$$

Finally, with $W=F_{14}$, the exact equation in fiber 1 is

$$S_1+WW^T+Z_jZ_j^T=J_{10}+4I_{10}.\tag{5}$$

Equation (5) will be used only to locate $S_1$ in the primal leave of
$Z_j$. No exact diagonal equation is assumed for fiber 0: its diagonal
defect row sum is four.

## Embedding these actual interfaces into the completed local domain

The local equivalence proved in
[D1_LOCAL_CONFIGURATION_CATALOG.md](D1_LOCAL_CONFIGURATION_CATALOG.md)
applies to (3) and (5). It makes both $Z_i$ and $Z_j$ incidence matrices
of linear combinatorial $(10_3)$ configurations, and places $S_3$ and
$S_1$ in their respective primal cubic leaves. Equation (4) places $S_2$
in the dual leave of $Z_j$.

In detail, the off-diagonal bound on $Z_iZ_i^T$ forbids a pair of points
from lying in two common columns. This also forbids two columns from
sharing two points, so the dual configuration is linear as well. Thus
the dual leave of $Z_i$ is one of the dual leaves in the complete ten-type
catalogue, even though its actual internal matching $S_0$ need not belong
to that leave.

Every one of the ten dual leaves has a perfect matching. The already
saved [local interface catalogue](../../../computations/dd82/construction/d1_10_3_catalog/local_interfaces.json)
lists their respective matching counts as

$$6,6,6,6,8,6,6,9,7,11.$$

Choose any such matching $T$ in the dual leave of $Z_i$. It is a virtual
parameter used solely to select a state in the finite domain. It is **not**
identified with $S_0$, and no edge of the hypothetical graph is changed.
The two states are

$$i=(Z_i,S_3,T),\qquad j=(Z_j,S_1,S_2).\tag{6}$$

The endpoints of $Z_i$ and $Z_j$ are the four distinct fibers $3,0,1,2$.
Their point and block labels may therefore be normalized independently
to the catalog representatives. The transformed matchings in (6) are
among the retained leave matchings. These are states among the completed
531-state input of
[D1_GENERAL_BRIDGE_EXCLUSION.md](D1_GENERAL_BRIDGE_EXCLUSION.md).
The classification dependency is exactly the one stated in that proof;
it is not replaced here by a new classification claim.

Moreover (3) and (4) say precisely that $Y$ is an allowed degree-two bridge
from the primal side of state $i$ to the dual side of state $j$. The
completed enumeration includes every such incidence-column labeling,
through all compatible two-factor cycle isomorphisms. The unused virtual
matching $T$ does not occur in either (3) or (4).

## The actual degree-one pair supplies the forbidden left witness

Consider the oriented pair $3\to1$. Its direct interface

$$M=F_{31}$$

is a permutation matrix. Among intermediate fibers other than 3 and 1,
only fiber 2 and the hub 5 contribute a two-step route:

$$F_{32}F_{21}=YZ_j^T,\qquad N=F_{35}F_{51}.$$ 

The matrix $N$ is a permutation, being the product of the two actual
hub matchings. Fiber 0 contributes zero because $q_{01}=0$; fiber 4
contributes zero because $q_{34}=0$. Including the direct edge and the
two endpoint-fiber contributions gives exactly

$$M+S_3M+MS_1+YZ_j^T+N=J_{10}.\tag{7}$$

To justify equality, its row capacity is $1+1+1+6+1=10$; diameter two
requires every one of the ten target coordinates to be reached. Equally,
(7) follows from the zero block $D_{31}=0$ in (2).

Hence the actual matching $M$ would satisfy

$$J-YZ_j^T-M-S_3M-MS_1=N\ge0.\tag{8}$$

This is exactly the **left** local matching domain in the completed
general bridge screen for the state pair (6) and bridge $Y$. The actual
residual route through hub 5 need not have the interpretation of a route
around a same-side triangle: that screen imposed only nonnegativity of
the residual, equivalently that it be some permutation matrix.

## Why the saved single-side zero is sufficient

The existing [complete result](../../../computations/dd82/construction/d1_general_bridge_run/search.json)
records 80,092 base alignments, representing 4,278,652 state--bridge
choices, and separately records

$$\texttt{left\_M\_feasible\_bridges}=0.$$

This is stronger than a zero count of bridges feasible on both sides.
The [actual search source](../../../computations/dd82/construction/d1_general_bridge_search.cpp)
tests the left domain using only the source primal matching, target primal
matching, $Y$, and $Z_j$. It tests the right domain separately. Its grouped
left count multiplies the number of left witnesses by the number of
source dual matching choices, which is positive for all ten types.
Therefore the recorded zero really excludes every left domain, regardless
of the virtual matching $T$.

In particular this argument does not require a right matching between
fibers 0 and 2, does not require actual $S_0$ to be a leave matching, and
does not impose any triangle-closure or homogeneous-permutation condition.
Equation (8) contradicts the independently empty left domain already
exhausted by the general screen. This excludes all sixty labeled matrices
in orbit 3 without any additional enumeration.

## Resulting boundary

The twelve-matrix orbit with the same internal-degree tuple was already
excluded by the five-cycle determinant argument in
[SIX_FIBER_VARIABLE_INTERNAL_DEGREE.md](SIX_FIBER_VARIABLE_INTERNAL_DEGREE.md).
Together, the two proofs exclude every surviving necessary quotient with
$d=(1,1,1,1,1,3)$.

Of the 98 matrices from the complete nonuniform quotient screen, the
remaining unexcluded domains are exactly:

* 2 labeled matrices, one orbit, with $d=(0,0,1,2,2,3)$;
* 24 labeled matrices, one orbit, with $d=(1,1,1,1,3,3)$.

Thus **26 labeled necessary quotients in two orbits remain**. This is not
an exclusion of all nonuniform equitable partitions or arbitrary graphs
on sixty vertices. This note adds a mathematical reduction using existing
files only; no solver, graph search, new enumeration, or new review agent
was run.
