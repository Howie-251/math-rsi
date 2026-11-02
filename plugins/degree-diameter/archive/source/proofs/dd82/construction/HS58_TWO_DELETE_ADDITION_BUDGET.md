# HS58 with two HS deletions: the first possible addition budget

Date: 2026-10-12. Pure necessary-condition proof; no enumeration, solver,
graph search or new candidate was used. With exactly two original HS
edges deleted, a diameter-two order-58 extension requires **at least two
old-old additions**. If there are exactly two additions, the eight new
vertices must induce **K1,7**. This specifies a remaining construction
domain; it does not assert that the domain has a completion.

Subsequent status: [the domination argument](HS58_TWO_DELETE_TWO_ADDITIONS_EXCLUSION.md)
excludes the remaining two-addition star domain, and
[the integrated three-addition proof](HS58_TWO_DELETE_THREE_ADDITIONS_EXCLUSION.md)
excludes all three-addition auxiliary types. Thus exactly two HS
deletions now require **at least four old-old additions**. The derivation
below is retained as the auxiliary-star reduction used in those proofs.

## Degree and pair budgets

Let Q be the 50-vertex, seven-regular Hoffman–Singleton graph. Delete
two distinct edges D from E(Q), and add a distinct edges A from the
nonedges of Q. Add eight new vertices. All graphs are simple. Write
r_v=d_D(v), a_v=d_A(v), and let B_v be the new neighbors of old vertex v.

A maximum-degree-eight, diameter-two graph on 58 vertices is
eight-regular: a vertex of degree at most seven would reach at most
1+7+7*7=57 vertices within distance two. Consequently

\[
p_v=|B_v|=1+r_v-a_v\ge0,\qquad
\sum_vp_v=54-2a,\qquad |E(H)|=5+a.                 \tag{1}
\]

Only the endpoints of D can have p_v greater than one. The number of
new-new pairs that can have a common old neighbor is at most

\[
P=\sum_v\binom{p_v}{2}
 \le\sum_v\binom{1+r_v}{2}
 =\begin{cases}5,&\text{D has adjacent edges},\\
               4,&\text{D has disjoint edges}.
   \end{cases}                                      \tag{2}
\]

The possible upper port sizes are (3,2,2) in the adjacent case and
(2,2,2,2) in the disjoint case. Additions can only decrease these sizes;
all other old vertices have at most one port. No restriction on the
positions or shared endpoints of the added edges is used.

For m=|E(H)|, at most m+sum_x binom(d_H(x),2) new pairs are covered
inside H. The latter sum counts pairs of incident H edges and is at
most binom(m,2). If a<=1, then m<=6 and

\[
28\le m+\binom m2+P\le6+15+5=26,
\]

a contradiction. Thus a>=2. This extends the previously recorded
[no-addition exclusion](HS58_TWO_DELETE_NO_ADDITIONS.md) only to the
additional a=1 case; no old deletion-only experiment is repeated.

## At two additions, the auxiliary graph is a star

Now let a=2, so H has eight vertices and seven edges. If H were
disconnected, one component and its complement would supply at least
1*7=7 unordered cross-component pairs. None has an H path of length at
most two; all would need shared old neighbors, contradicting P<=5.
Hence H is connected and is a tree.

In a tree, the direct-edge pairs and the pairs having a two-edge path
are disjoint, and each two-edge path has a unique middle vertex.
Therefore the number of pairs at H-distance greater than two is

\[
b(H)=28-7-\sum_x\binom{d_H(x)}2.
\]

By (2), b(H)<=5, so the sum of degree binomials is at least sixteen.
If the maximum degree were at most five, put x_v=d_H(v)-1. Connectedness
gives x_v>=0, sum_v x_v=6, and x_v<=4. Convexity concentrates these six
units as (4,2,0,...,0), yielding

\[
\sum_v\binom{d_H(v)}2\le\binom52+\binom32=13,
\]

a contradiction. Thus the maximum degree is six or seven.

Degree seven gives K1,7. Degree six forces the degree sequence
(6,2,1,1,1,1,1,1). The two nonleaf vertices must be adjacent; the tree
is the double-star with five leaves at one center and one at the
other. Its five bad pairs join the lone leaf to the five opposite
leaves, forming a K1,5 on the new labels.

If D is disjoint, (2) supplies at most four shared-old pair witnesses,
which cannot cover these five pairs. If D is adjacent, only three old
vertices can supply pairs, with port sizes at most 3,2,2. A port set
of size p contains at most p-1 edges of the required K1,5: it must
contain that star's center, after which its remaining vertices supply
at most p-1 leaves. Thus these three sets cover at most 2+1+1=4 of
the required pairs. The double-star is impossible in both cases.

Therefore **H=K1,7 whenever a=2**. The proof uses neither an HS
automorphism reduction nor an assumption on whether old additions
restore particular deleted old paths.

## Exact remaining attachment domain

For a future construction at this first possible budget, choose any
two HS deletions D and any two non-HS additions A, and form the actual
old adjacency matrix M=A_(Q-D+A). Require the port sizes in (1) to be
nonnegative. Label the new star center 0 by a permutation of the eight
new labels; no old labeling is fixed by this normalization.

The remaining binary 50-by-8 matrix B must have row sums p_v, center
column sum one, and each of its seven leaf column sums seven. These
column sums total fifty, as required by (1). With H the star adjacency,
the exact remaining coverage conditions are

\[
M_{uv}+(M^2)_{uv}+(BB^T)_{uv}\ge1\quad(u\ne v),
\qquad B+MB+BH\ge J_{50,8}.                         \tag{3}
\]

New-new coverage already follows from the star. Together with the
stated binary matrices and degree equations, (3) is necessary and
sufficient for a full graph in this fixed two-deletion/two-addition
domain to have diameter two. This is the exact domain subsequently
excluded by the linked domination argument.

In particular, old-pair intersection requirements must be computed
from the actual matrix M. An added old edge can restore a deleted
one- or two-step route, so it is not valid to impose every
deletion-only thirteen-pair obligation without checking the additions.
No complete order-58 construction or exclusion of all a>=2 cases
is claimed.
