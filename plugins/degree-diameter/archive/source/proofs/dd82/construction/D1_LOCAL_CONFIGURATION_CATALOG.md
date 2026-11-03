# Exact local reduction to ten combinatorial configurations

Date: 2026-10-12. This is a complete parametrization of one same-fiber
equation in the general degree-one-fiber model. It is not a classification
of compatible sixty-vertex graphs.

## Equivalence

Let S be the adjacency matrix of a perfect matching on ten points. Let Y
and Z be ten-by-ten zero-one matrices with row and column sums two and
three respectively. The local equation from
[SIX_MATCHING_FIBERS_QUOTIENT.md](SIX_MATCHING_FIBERS_QUOTIENT.md) is

\[
                   S+YY^T+ZZ^T=J+4I.                         \tag{1}
\]

For distinct points p,q the three nonnegative entries on the left sum to
one. In particular, no pair appears in two columns of Z. Its ten columns
are therefore ten distinct triples, every point is in exactly three
triples, and two triples meet in at most one point. This is precisely a
combinatorial configuration (10_3), with no geometric realization
requirement. Write ZZ^T=3I+T. Then T is its simple six-regular collinearity
graph, and its leave L=K_10-T is a simple cubic graph.

Similarly, the columns of Y are ten distinct unordered pairs: a repeated
pair would make an off-diagonal entry of YY^T at least two. These columns
form the edge set of a simple two-regular graph F, and YY^T=2I+F.
Equation (1) is consequently equivalent to

\[
                         L=S+F.                              \tag{2}
\]

Conversely, start with any combinatorial (10_3) configuration, let Z be
its point-block incidence matrix, choose any perfect matching S in its
cubic leave L, and set F=L-S. Label F's ten edges arbitrarily and take Y
to be its point-edge incidence matrix. All row/column degrees are correct,
and substituting YY^T=2I+F and ZZ^T=3I+T proves (1).

Thus the complete one-sided local data are: a (10_3) configuration, a
perfect matching in its leave, and the relevant point/column labels.
For a prescribed standard S one may relabel the points to carry the
chosen matching to S. Those relabelings and both sets of column labels
remain meaningful when interfaces are glued to other fibers.

No hidden connectedness hypothesis is needed. In a linear configuration
of degree and block size three, any point sees six distinct other points,
so each incidence component contains at least seven points. A ten-point
configuration cannot split into two such components.

## Classification source and its exact scope

The primary computational classification is Betten, Brinkmann and
Pisanski, *Counting symmetric configurations v_3*, Discrete Applied
Mathematics 99 (2000), 331-338,
[DOI 10.1016/S0166-218X(99)00143-2](https://doi.org/10.1016/S0166-218X(99)00143-2).
The [author-posted full text](https://www.researchgate.net/publication/223111487_Counting_symmetric_configurations_v3)
defines isomorphisms as point bijections carrying blocks to blocks.
Table 1, page 333, gives ten configurations at v=10, all ten self-dual
and self-polar, and none disconnected. The text reports independent
computations by two programs through v=16. This is a classification of
abstract incidence structures, not only straight-line configurations,
and is not a count taken modulo an additional identification with duals.

For explicit data, Anton Betten's official
[Orbiter user's guide](https://www.math.colostate.edu/~betten/orbiter/users_guide.pdf),
Section 12.6, printed/PDF page 536, includes the complete `10_3.inc` table.
It has been extracted from the actual downloaded PDF into
[the local catalogue](../../../computations/dd82/construction/d1_10_3_catalog/10_3.inc),
with the [original PDF page](../../../computations/dd82/construction/d1_10_3_catalog/orbiter_manual_page536.pdf)
preserved. Each number 10p+b indicates incidence between point p and block b.

A second full table, with different numbering, appears in Grunbaum's
author-hosted *Configurations of Points and Lines* draft,
[Table 2.2.7](https://faculty.washington.edu/moishe/branko/CfsPts%26LinesFinal%20pdf%20files/Chapter%202.pdf),
page 2.2.6. Its ten triple lists are stored in
[10_3_grunbaum.json](../../../computations/dd82/construction/d1_10_3_catalog/10_3_grunbaum.json).
Table 2.2.1 distinguishes ten combinatorial types from nine realizable
by real straight lines; the fourth combinatorial type must be retained
for our incidence-matrix problem.

Completeness here is inherited from the stated published classification.
The local comparison checks transcription and agreement of the two
supplied catalogues; it does not independently enumerate all configurations.
The [actual two-color Levi comparison](../../../computations/dd82/construction/d1_10_3_catalog/verification.json)
confirmed no duplicates within either table and a bijection between them.
Orbiter entries 1 through 10 correspond respectively to Grunbaum entries
8,5,10,9,4,3,7,1,2,6; every point and block map is saved. This single check
took 6.917921 CPU seconds on one CPU under a ten-second limit.

## Actual local expansion

The root agent's
[local-interface generator](../../../computations/dd82/construction/d1_local_configuration_interfaces.py)
used the Grunbaum representatives and listed every perfect matching in
each primal and dual leave. The
[actual output](../../../computations/dd82/construction/d1_10_3_catalog/local_interfaces.json)
contains 71 primal choices and 71 dual choices, with (1) checked exactly
for every generated S,Y,Z. In Grunbaum order the primal matching counts
are 6,6,6,6,8,6,6,9,7,11. The recorded runtime is 0.009206 CPU seconds.

These are matching choices on the ten fixed representatives, not 71
interfaces up to isomorphism, not 142 distinct global choices, and not
sixty-vertex solutions. The actual remaining global obligations include
using each interface consistently at both endpoints, all degree-zero and
degree-one exact cross-coverage equations, and the degree-two and
degree-three coverage inequalities. The local catalogue supplies finite
input for those obligations without fixing the previously excluded common
Petersen-based interfaces.
