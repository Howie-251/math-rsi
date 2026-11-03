# The cubic thirty-vertex half in the remaining matching-fiber model

Date: 2026-10-12. This bounded analysis strengthens the necessary half-graph
conditions and rejects three explicit candidates. It does **not** exclude
the general degree-one-fiber family or produce a valid sixty-vertex graph.

## Exact starting point

Use the unique quotient and notation in
[SIX_MATCHING_FIBERS_QUOTIENT.md](SIX_MATCHING_FIBERS_QUOTIENT.md).
Its degree-one interfaces form two quotient triangles. Order the vertices
by these two thirty-point halves and write

\[
A=\begin{pmatrix}C&X\\X^T&D\end{pmatrix}.
\]

Here C and D are simple cubic graphs. Each has an equitable partition
into three ten-point fibers with quotient J_3: one internal matching and
one matching to each other fiber. The zero-one matrix X has row and column
sums five. Since the defect matrix A^2+A-7I-J is zero on either diagonal
half, a successful construction necessarily satisfies

\[
XX^T=G(C):=7I_{30}+J_{30}-C^2-C,\qquad
X^TX=G(D).                                                   \tag{1}
\]

These are necessary conditions; they do not replace the remaining
off-diagonal coverage inequalities or X's prescribed fiber blocks.

## Consequences checked directly

* **Connectedness.** A disconnected cubic C has a vector perpendicular
  to the all-one vector with eigenvalue three. On that vector G(C) has
  eigenvalue 7-9-3=-5, contradicting (1).
* **Girth at least five.** For distinct u,v,
  G(C)_{uv}=1-C_{uv}-(C^2)_{uv} is nonnegative. Adjacent vertices therefore
  have no common neighbor, and nonadjacent vertices have at most one.
* **Spectral interval.** On the perpendicular complement of the all-one
  vector, positive semidefiniteness gives 7-lambda^2-lambda >= 0.
  Combining its lower endpoint with the cubic bound lambda >= -3 gives

  \[
  -3\le\lambda\le r:=\frac{\sqrt{29}-1}{2}=2.192582\ldots .    \tag{2}
  \]

  The main eigenvalue of G(C) is 25. Quotient J_3 also forces at least
  two zero eigenvalues of C, independently of any numerical computation.
* **Two-fiber cycle types.** On any two fibers each vertex has one
  internal and one interface edge. These edge types alternate around
  every cycle. An even number of interface edges is required to return
  to the starting fiber, so each cycle length is divisible by four.
  Excluding four-cycles leaves exactly C_20 or C_8 disjoint union C_12.

The same conclusions hold for D.

## A concrete design obligation stronger than positive semidefiniteness

By the girth statement, each vertex has three vertices at distance one
and six at distance two. Thus

\[
G(C)=5I+H_C,
\]

where H_C is the twenty-regular graph joining pairs at distance at least
three in C. Equation (1) says that each column of X is a five-point set
whose members are pairwise at distance at least three in C. Each far pair
belongs to exactly one such set. Equivalently, the 300 edges of H_C must
be partitioned into thirty copies of K_5, with every vertex in five
blocks. There is also the dual requirement using D and X^T.

The original quotient adds information to this block design: each column
of X has three entries in one C-fiber, two in a second, and zero in the
third, with the orientations prescribed by the degree-three and degree-two
quotient matchings. Finding a positive semidefinite G(C) alone does not
construct these zero-one blocks.

## Why the low moments and the interval alone do not close the problem

There is an explicit cubic thirty-vertex graph meeting all the generic
girth and spectral conditions: the duad-syntheme incidence graph, also
called the Tutte-Coxeter graph. Its fifteen point vertices are the
two-subsets of a six-element set; its fifteen line vertices are the
partitions of that set into three pairs. Incidence means containment.

Let N be its 15 by 15 incidence matrix and K the graph on pairs joining
disjoint pairs. Then NN^T=3I+K. If U is the 6 by 15 unsigned incidence
matrix of pairs versus their elements, then

\[
UU^T=4I+J_6,\qquad K=J_{15}+I-U^TU.
\]

Consequently K has spectrum 6^1,(-3)^5,1^9, and the cubic incidence
graph has exact spectrum

\[
3^1,\quad2^9,\quad0^{10},\quad(-2)^9,\quad(-3)^1.
\]

Its corresponding G has spectrum 25^1,1^{10},5^9,7^{10}, which is
positive definite. In particular, the usual trace conditions
tr(C)=0, tr(C^2)=90, tr(C^3)=0 and tr(C^4)=450, together with at least
two zero eigenvalues and (2), admit an actual graph. No contradiction
from those conditions alone is possible.

This graph nevertheless **cannot have the required J_3 partition**.
If such a partition existed, every line would see all three point colors.
Double-counting incidences shows each point color contains five duads.
Two same-color duads must intersect, since disjoint duads lie on a common
syntheme. Every intersecting family of five edges of K_6 is a star:
if two edges ab and ac are present and the common endpoint a is not in
all edges, then bc is present and every edge must belong to that triangle,
which allows only three edges. But two distinct full stars share an edge,
so three stars cannot partition the fifteen duads. This proves the
partition obstruction without a graph catalogue or coloring search.

## Exact published range used here

Cioaba, Koolen, Nozaki and Vermette prove the spectral order bound in
Theorem 2.3 of *Maximizing the order of a regular graph of given valency
and second eigenvalue*, SIAM J. Discrete Math. 30 (2016), 1509-1525.
Their Table 1 gives v(3,2)=30, and the paragraph following Table 2 states
that the Tutte-Coxeter graph is the unique graph meeting that bound,
with uniqueness referenced to Brouwer-Cohen-Neumaier, Theorem 7.5.1.
The primary paper is [arXiv:1503.06286v2](https://arxiv.org/pdf/1503.06286),
Theorem 2.3 on printed page 5 and the uniqueness statement on printed
page 9.

Applied to our connected graph of **exactly thirty vertices**, this result
and the preceding partition obstruction strengthen (2) to

\[
                    2<\lambda_2(C)\le r.                    \tag{3}
\]

This citation does not say that every smaller cubic graph with second
eigenvalue at most two is Tutte-Coxeter. Proposition 2.9 and Table 3 of
the same paper extend some maximum-order bounds to larger eigenvalue
thresholds; they do not supply a classification of all thirty-vertex
graphs in (3). No such classification or stronger gap is asserted here.

## Explicit partition-bearing graphs rejected exactly

For k=2,4,7, take GP(15,k), with vertices a_i,b_i for i modulo 15 and
edges a_i a_{i+1}, b_i b_{i+k}, a_i b_i. Give both a_i and b_i color
i modulo three. This is a genuine three-fiber J_3 partition.

The [generator and exact checker](../../../computations/dd82/construction/d1_half_cubic_examples.py)
saves all edges, the coloring, and an integer vector w for each graph in
[its actual result](../../../computations/dd82/construction/d1_half_cubic_examples.json).
For every stored vector sum(w)=0, and direct integer substitution gives:

| Half graph | Girth | Diameter | w^T G(C) w |
| --- | ---: | ---: | ---: |
| GP(15,2) | 5 | 6 | -24304 |
| GP(15,4) | 7 | 5 | -2346 |
| GP(15,7) | 5 | 6 | -23706 |

Thus none can be completed to X in (1), regardless of the choice of D.
Numerical eigenvectors were used once to discover these integer witnesses;
the saved rejection calculation uses integer arithmetic only. The actual
generator/checker run took 0.002034 CPU seconds on one CPU with a ten-second
CPU limit. It constructed four named graphs and performed exact checks;
there was no graph enumeration, SAT call, or sixty-vertex search.

## Remaining precise gap

No C with both the required J_3 partition and (3) has been produced or
excluded by this bounded analysis. Even finding one would leave the
specified K_5 decomposition, compatible D, zero-one X and the original
off-diagonal coverage obligations. The general degree-one-fiber model
therefore remains open. The earlier fixed Petersen-based Y/Z/S interface
obstruction is not being extended to these arbitrary interfaces.
