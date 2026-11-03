# False twins at order 58: an exact eight-fibre construction

Every 58-vertex degree-eight diameter-two graph containing a pair of
false twins has the exact construction below: two twins, their eight
independent common neighbours, and eight independent six-vertex fibres
joined pairwise by perfect matchings. Conversely, the displayed matching
coverage conditions are sufficient to construct such a target.

For the f=9 branch of an order-seven automorphism, this representation
reduces to three permutations A,B,C of six coordinates. A normalized
necessary hub condition has exactly 10,080 ordered triples, all saved
by the one authorized domain-preparation run. No outer-fibre coverage
or graph-distance search was performed in this task. Neither the general
false-twin family nor the f=9 branch is excluded by this note.

## 1. Deriving the eight independent fibres from an arbitrary target

Let G be simple, have order 58, maximum degree at most eight, and diameter
at most two. Any vertex of degree at most seven has a radius-two ball
of size at most 1+8·7=57, so G is eight-regular. Its adjacency matrix A
satisfies

\[
 B=A^2+A-7I-J_{58}\geq0,\qquad B_{xx}=0,
 \qquad B\mathbf1=(64+8-7-58)\mathbf1=7\mathbf1.
\]

Suppose u,v are false twins: they are distinct, nonadjacent, and have
the same neighbour set S, of size eight. They have eight common
neighbours, so B_uv=7. This exhausts the row budget at both u and v.
For s∈S, the adjacent pair u,s therefore has

\[
 0=B_{us}=|N(u)\cap N(s)|=|S\cap N(s)|.
\]

Thus S is independent. Put R=V(G)\({u,v}∪S), of size 48. For x∈R,
the nonadjacent pair u,x has B_ux=0, giving

\[
 |S\cap N(x)|=1.
\]

Label S={s_0,...,s_7}. Each s_i has neighbours u,v and six vertices of
R. The sets G_i=N(s_i)∩R consequently partition R into eight sets of
size six.

For distinct s_i,s_j, their common neighbours include u,v, so
B_(s_i,s_j)≥1. The other seven vertices of S already use the full
row budget seven at s_i. Hence B_(s_i,x)=0 for every x∈R.
If x∈G_i, adjacency to s_i gives

\[
 0=B_{s_i x}=|N(s_i)\cap N(x)|=|G_i\cap N(x)|,
\]

since x is adjacent to neither u nor v. Therefore G_i is independent.
For j≠i, nonadjacency to s_j gives

\[
 0=B_{s_j x}=|G_j\cap N(x)|-1.
\]

Every vertex of G_i has exactly one neighbour in every other G_j.
Each pair of fibres is thus joined by a perfect matching. The induced
graph on R is a matching cover of K8, specified by 28 arbitrary
permutations of six coordinates before imposing the remaining coverage.

## 2. The exact converse and its complete coverage obligation

Choose eight disjoint labelled sets G_i={x_(i,a):0≤a<6}, eight further
vertices s_i and two vertices u,v. Add edges u s_i and v s_i, join s_i
to all of G_i, and join each pair G_i,G_j by a chosen perfect matching.
Add no other edges. The graph is simple, has 58 vertices and

\[
 16+48+\binom82\cdot6=232
\]

edges, and every vertex has degree eight. The vertices u,v are false
twins with common neighbour set {s_i}.

Use row-source matching matrices Q_ij, so the (a,b) entry equals one
when x_(i,a) is joined to x_(j,b). Then Q_ji=Q_ij^T, and matrix product
Q_ik Q_kj counts paths with the first step from i to k and the second
from k to j. For i≠j the complete one- and two-step path-count matrix is

\[
 K_{ij}=Q_{ij}+\sum_{k\ne i,j}Q_{ik}Q_{kj}. \tag{1}
\]

There are no additional two-step routes through the s vertices or
through u,v: vertices in different fibres have different parents, and
neither is adjacent to the twins. Nor is there an internal-fibre route.
The direct matching and six intermediate fibres give row and column
sums seven in K_ij.

All different-fibre pairs are covered exactly when K_ij≥J6, equivalently

\[
 K_{ij}-J_6\quad\text{is a permutation matrix for every }i\ne j. \tag{2}
\]

Indeed this difference is integral with row and column sums one, so
entrywise nonnegativity makes it a permutation matrix.

Every other vertex pair is automatically at distance at most two:
two vertices of the same G_i share s_i; the s vertices share u,v;
each twin reaches R through its parent; and s_i reaches a vertex of
G_j, j≠i, through that vertex's unique neighbour in G_i. The remaining
pairs are edges or the twin pair itself. Thus (2) is both necessary and
sufficient for the complete constructed graph to be a target. This is
a two-way representation, not just a necessary local condition.

## 3. Exact coordinates for the f=9 order-seven branch

[CYCLIC7_EIGHT_ORBITS58_SEED.md](CYCLIC7_EIGHT_ORBITS58_SEED.md), Section 1,
proves that an order-seven automorphism with nine fixed vertices has
fixed induced graph K1,8. Write its centre as h and its fixed leaves
as u,v,ℓ_0,...,ℓ_5. The two leaves u,v attach to the same nonfixed
seven-orbit T={s_t:t∈Z7}; every other nonfixed orbit is attached to
exactly one of the other six fixed leaves. Hence

\[
 N(u)=N(v)=\{h\}\cup T.
\]

In the false-twin representation, S is exactly {h}∪T. The fibre with
parent h is

\[
 G_\infty=\{\ell_0,\ldots,\ell_5\},
\]

whose six vertices are individually fixed. Each other fibre G_t has
parent s_t, and the automorphism sends G_t to G_(t+1). Each G_t contains
one point from each of the six remaining nonfixed seven-orbits.

Label its vertices x_(t,a) by their unique matching neighbour ℓ_a in
G_∞. Since ℓ_a is fixed, the automorphism sends x_(t,a) to x_(t+1,a).
Thus all seven matchings G_∞--G_t become the identity simultaneously.
This is a legitimate fibre-coordinate choice, not an additional
restriction. In arbitrary coherent transported coordinates they would
all be one constant matching, removable by this coordinate change.

The explicit action is therefore

\[
 g(h)=h,\quad g(u)=u,\quad g(v)=v,\quad g(\ell_a)=\ell_a,
 \quad g(s_t)=s_{t+1},\quad g(x_{t,a})=x_{t+1,a}.
\]

It has cycle type 1^9 7^7: the orbit T and the six cycles indexed by a
are nonfixed. This describes the f=9 structural branch in actual vertex
coordinates. The previously saved numerical seed in the cited note is
the **f=2** branch, and is not an f=9 example.

Invariance now makes every outer matching depend only on the fibre
difference. Set

\[
 P_1=A,\quad P_2=B,\quad P_3=C,\quad
 P_4=C^T,\quad P_5=B^T,\quad P_6=A^T.
\]

Use Q_(t,t+d)=P_d and Q_(∞,t)=I. The seven unordered outer pairs at each
cyclic distance 1,2,3 are distinct and exhaust the 21 outer pairs;
the reverse directions use transposes. Together with the seven fixed
identity matchings this specifies all 28 interfaces. There are exactly
three free S6 parameters in this representation. Conversely any such
triple constructs a full 58-vertex eight-regular graph with the stated
f=9 action; it is a target precisely when the conditions below hold.

## 4. Four six-by-six coverage conditions

For the fixed fibre to any outer fibre, equation (1) becomes

\[
 K_\infty=I+A+A^T+B+B^T+C+C^T. \tag{3}
\]

For outer distance d∈{1,2,3}, the path through the fixed fibre contributes
I, and the five other outer fibres contribute the sum

\[
 K_d=I+P_d+\sum_{e\in\mathbb Z_7\setminus\{0,d\}}P_eP_{d-e}. \tag{4}
\]

The remaining distances give transposes. Explicitly, in the row-source
matrix convention,

\[
\begin{aligned}
 K_1&=I+A+BA^T+CB^T+(C^T)^2+B^TC+A^TB,\\
 K_2&=I+B+A^2+CA^T+C^TB^T+B^TC^T+A^TC,\\
 K_3&=I+C+AB+BA+C^TA^T+(B^T)^2+A^TC^T.
\end{aligned}
\]

Each matrix has row and column sums seven. The full graph is a target
if and only if K_∞−J and each K_d−J, d=1,2,3, are permutation matrices.
Checking entrywise positivity K≥J is equivalent. No other point-pair
obligation remains outside these four matrices.

## 5. Normalized hub domain and complete preparation mechanism

Let F=K_∞−J. If the hub condition holds, F is a symmetric permutation
matrix. Its a-th diagonal entry is twice the number of A,B,C fixing a:
the I and J diagonal entries cancel. Since a permutation entry is zero
or one, every such count is zero. Thus A,B,C are derangements and F has
zero diagonal. It is a perfect matching on the six coordinates.

The same coordinate permutation in all eight fibres conjugates A,B,C
and F, preserves the identity interfaces, and is a full-graph
relabelling. Therefore we may normalize

\[
 F=(01)(23)(45),\qquad
 A+A^T+B+B^T+C+C^T=J-I+F. \tag{5}
\]

All targets in the f=9 branch have a representative satisfying this
normalization. Remaining coordinate symmetries are not quotiented out.

There are 265 derangements of six coordinates. Enumerate ordered A,B
from this set and form

\[
 L=J-I+F-(A+A^T+B+B^T).
\]

If any entry is negative, no C can complete the equation. Otherwise L
is symmetric, has zero diagonal and row sum two. It is the adjacency
matrix of a loopless degree-two multigraph. Every component is either
a double edge on two vertices or a simple cycle of length at least
three. A double edge gives exactly one permutation two-cycle; a simple
cycle gives exactly its two orientations. These choices produce all,
and only, C with C+C^T=L. There are at most four such C, attained for
two three-cycles. This is a complete candidate-preserving domain
generator, with at most 265²·4=280,900 triples before its actual count.

The authorized preparation was run once in
[false_twins58_f9_domain_prepare.py](../../../computations/dd82/construction/false_twins58_f9_domain_prepare.py).
It checked all 70,225 ordered pairs and found:

| Residual components | A,B pairs | C choices per pair |
| --- | ---: | ---: |
| 2+2+2 | 112 | 1 |
| 2+4 | 840 | 2 |
| 3+3 | 528 | 4 |
| 6 | 3,088 | 2 |
| Total | 4,568 | 10,080 total triples |

Every one of the 10,080 ordered triples is saved in
[triples.txt](../../../computations/dd82/construction/false_twins58_f9_domain_run/triples.txt),
one row of eighteen integers: the six images of A, then B, then C.
Distinct A,B and distinct component orientations ensure there is no
duplicate ordered triple. Isomorphic complete graphs may still share
this parameter domain; no graph-isomorphism count is claimed.

The preparation completed in 0.338266358 CPU seconds and 0.341856141 wall
seconds, on one CPU with a five-CPU-second cap and 1 GiB address-space
limit. Its exact record is
[result.json](../../../computations/dd82/construction/false_twins58_f9_domain_run/result.json).
It evaluated zero outer coverage matrices, zero full graph distances,
and no SAT instance. These triples satisfy only (5); the three remaining
matrices (4) are the explicit complete construction obligation for a
subsequent separately authorized search.
