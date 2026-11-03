# The remaining nonuniform (1,1,1,1,3,3) matrix obligation

Later status: this entire quotient is now excluded by the
[local hub obstruction](VARIABLE_HUB_LOCAL_ASSEMBLY.md), accepted in C14.
The matrix derivation below is preserved as its earlier construction obligation.

Date: 2026-10-12. This bounded derivation simplifies the exact equations
and proves a spectral restriction on both cubic fibers. It does not
exclude this quotient or prove a repartition into Petersen fibers.
No enumeration, solver, graph search, or new review agent was used.

## Quotient and simultaneous normalization

The input is orbit 4 in
[the actual quotient verification](../../../computations/dd82/construction/six_fiber_variable_internal_run/verification.json):

\[
d=(1,1,1,1,3,3),\qquad
Q=\begin{pmatrix}
0&0&1&3&1&2\\
0&0&3&1&2&1\\
1&3&0&2&0&1\\
3&1&2&0&1&0\\
1&2&0&1&0&1\\
2&1&1&0&1&0
\end{pmatrix}.
\]

Write every oriented interface with source vertices as rows. The five
degree-one interfaces 04,34,45,15,25 form a spanning tree on the six
fibers. Successively relabeling a child fiber along this tree makes all
five interface matrices identity matrices simultaneously. This uses
only legitimate fiber relabelings.

In these coordinates put

\[
Z=F_{03},\quad W=F_{12},\quad
Y=F_{05},\quad V=F_{14},\quad T=F_{23},\quad
M=F_{02},\quad N=F_{13}.
\]

Z,W have row and column sums three; Y,V,T have row and column sums two;
M,N are permutation matrices. The internal graphs of fibers 0,...,3
are matching matrices S_0,...,S_3, and those of fibers 4,5 are symmetric
simple cubic adjacency matrices C_4,C_5.

This gauge leaves only two nonidentity degree-one interfaces. It does
not allow Z and W also to be fixed independently to catalogue matrices
without tracking the induced changes to the identity tree. They remain
arbitrary row/column labelings of configurations below.

## Four exact diagonal blocks and the configuration input

For B=A^2+A-7I-J, the four diagonal blocks B_ii, i=0,...,3, vanish.
The resulting identities are

\[
\begin{aligned}
S_0+YY^T+ZZ^T&=J+4I,\\
S_1+VV^T+WW^T&=J+4I,\\
S_2+TT^T+W^TW&=J+4I,\\
S_3+T^TT+Z^TZ&=J+4I.                         \tag{1}
\end{aligned}
\]

Thus Z and W are linear combinatorial (10_3) incidence matrices, with
both primal and dual internal matchings in their respective leaves.
All four statements follow from the exact local equivalence in
[D1_LOCAL_CONFIGURATION_CATALOG.md](D1_LOCAL_CONFIGURATION_CATALOG.md).
The three two-factors represented on the row side by Y,V,T, and their
column-side line graphs, must be compatible with the actual labels in
(1). This provides finite local input without fixing the matrices to the
previously excluded homogeneous Petersen interface.

## All exact off-diagonal zero blocks

The seven off-diagonal zero blocks of the defect quotient are precisely
01,04,15,24,25,34,35. Their equations in the tree gauge are

\[
\begin{aligned}
I+S_0+C_4+Z+Y&=J, & &(04)\\
I+S_3+C_4+Z^T+N^TV&=J, & &(34)\\
I+S_1+C_5+W+V&=J, & &(15)\\
I+S_2+C_5+W^T+M^TY&=J, & &(25)\\
I+M^T+T+W^TV&=J, & &(24)\\
I+N^T+T^T+Z^TY&=J, & &(35)\\
MW^T+ZN^T+V^T+Y&=J. & &(01)                 \tag{2}
\end{aligned}
\]

Each product has the source/target orientation indicated by the original
fiber labels. For example, the 24 routes use middle fibers 0,1,3,5 and
give M^T,W^TV,T,I respectively. The 35 routes use 0,1,2,4 and give
Z^TY,N^T,T^T,I. Thus no direct route or possible intermediate fiber is
missing from these capacity-ten equations.

Two useful eliminations follow immediately:

\[
\begin{aligned}
C_4&=J-I-S_0-Z-Y,\\
C_5&=J-I-S_1-W-V.                             \tag{3}
\end{aligned}
\]

Consequently the internal cubic graphs are determined by the other local
data and must satisfy symmetry, zero diagonal and zero-one entries.
In particular Z+Y and W+V are symmetric, and the four nonidentity
summands in each of the first and third equations of (2) have disjoint
support. These are actual constraints; arbitrary cubic choices cannot
be appended afterwards.

Comparing the transpose of 04 with 34, and the transpose of 15 with 25,
also gives

\[
N^TV-Y^T=S_0-S_3,\qquad
M^TY-V^T=S_1-S_2.                              \tag{4}
\]

The two equations 24 and the transpose of 35 eliminate T:

\[
W^TV+M^T=Y^TZ+N,\qquad
T=J-I-M^T-W^TV.                               \tag{5}
\]

Any use of (3) or (5) must still require the resulting matrices to be
zero-one with the prescribed row and column degrees.

## Both cubic fibers are connected and have second eigenvalue at most two

Because V is the incidence matrix of a simple two-factor by (1), write
V^TV=2I+H_4, where H_4 is a simple two-regular graph. Similarly write
Y^TY=2I+H_5. The two remaining diagonal defect blocks then satisfy

\[
C_i^2+C_i+H_i=J+2I+B_{ii}\qquad(i=4,5).       \tag{6}
\]

Each B_ii is a nonnegative symmetric matrix with zero diagonal and every
row sum two, by the saved defect quotient. Its entries need not all be
zero or one: a weight-two edge is allowed. Both H_i and B_ii nevertheless
have operator norm at most two.

Let x be a unit eigenvector of C_i perpendicular to the all-one vector,
with eigenvalue lambda. Equation (6) gives

\[
\lambda^2+\lambda
 =2+x^TB_{ii}x-x^TH_ix\le6.
\]

Therefore -3 <= lambda <= 2. A disconnected cubic graph would have an
eigenvector of eigenvalue three perpendicular to the all-one vector, so
both C_4 and C_5 are connected and satisfy lambda_2 <= 2.

This spectral conclusion does not force either graph to be Petersen.
For example, the pentagonal prism C_5 Cartesian-product K_2 is a
connected cubic graph on ten points with
lambda_2=(1+sqrt(5))/2 < 2; its spectrum follows by adding the cycle
eigenvalues to +1 and -1. It has four-cycles. This example concerns only
the spectral condition, not the full equations (1)-(6).

## The nonzero blocks remain inequalities

The remaining off-diagonal defect row sums are

\[
D_{02}=D_{13}=D_{45}=1,\qquad
D_{03}=D_{05}=D_{12}=D_{14}=D_{23}=2.         \tag{7}
\]

For any such pair i,j, with internal matrices A_i,A_j and oriented
interface F_ij, its exact route-count matrix is

\[
K_{ij}=F_{ij}+A_iF_{ij}+F_{ij}A_j
                    +\sum_{k\ne i,j}F_{ik}F_{kj}.
\]

The remaining obligation is K_ij >= J entrywise, equivalently
B_ij=K_ij-J >= 0. The three row-sum-one B blocks in (7) are permutation
matrices; the five row-sum-two blocks can have entries two. Equations
(1)-(2), (6), and these eight inequalities are necessary and sufficient
for diameter two once the matrices define a simple graph with the
prescribed degrees.

In particular, the actual capacity of the q1 pairs 02 and 13 is eleven.
For the orientation 3 -> 1 one has

\[
N^T+S_3N^T+N^TS_1+T^TW^T+V^T=J+B_{31},      \tag{8}
\]

where B_31 is an unknown permutation matrix. Rearranging leaves
V^T-B_31, which need not be nonnegative. Therefore the previously
exhausted capacity-ten local bridge domain is not a valid substitution
for (8). The same issue applies to 0 -> 2. No exact-bridge zero from
the uniform d=1 model is imported here.

## Precise boundary of this derivation

The tree gauge, eliminations (3)-(5), and cubic spectral bound are proved
necessary restrictions and can be applied to actual candidate data.
The remaining equations are coupled to common labels; separate catalogue
choices do not prove simultaneous realization. No argument above forces
S_0=S_3 or S_1=S_2, makes V^T-B_31 nonnegative, or supplies the vertex
subsets of a Petersen repartition. The zero equations involve sums of
matrix products, rather than the fixed invertible product around an odd
cycle used in the already excluded five-matching-fiber quotient, so that
determinant argument has not been reproduced here. The quotient remains
an open construction obligation at the end of this bounded analysis.
