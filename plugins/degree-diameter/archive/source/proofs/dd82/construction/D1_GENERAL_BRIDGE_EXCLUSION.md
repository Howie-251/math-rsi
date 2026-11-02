# General degree-one six-fiber model: complete bridge obstruction

Date: 2026-10-12. Status: computer-assisted family exclusion, using the
published complete classification of combinatorial (10_3) configurations
and the two finite screens identified below. This is not an exclusion of
arbitrary sixty-vertex graphs, an independently checked SAT certificate,
or a Lean theorem. No additional search or rerun is part of this note.

## Claim and first reduction: the original equitable model

There is no simple eight-regular diameter-two graph on sixty vertices
admitting an equitable partition into six fibers of size ten, each
inducing a perfect matching.

Let Q be its symmetric cross-degree matrix. The capacity and row-square
arguments in
[SIX_MATCHING_FIBERS_QUOTIENT.md](SIX_MATCHING_FIBERS_QUOTIENT.md)
reduce the off-diagonal row multisets to
(3,3,1,0,0), (3,2,2,0,0), and (3,2,1,1,0).
The complete [quotient source](../../../computations/dd82/construction/six_matching_fibers_quotients.py)
and [actual result](../../../computations/dd82/construction/six_matching_fibers_quotients.json)
screen all 6210 labeled symmetric matrices in that proved domain.
The 120 capacity survivors form one orbit under permutation of the six
fiber labels. Thus the fibers can be named L_a,R_a, a in Z/3Z, with

\[
q(L_a,R_a)=3,\quad q(L_a,R_{a+1})=2,\quad q(L_a,R_{a-1})=0,
\]

and a degree-one triangle on each side. This quotient reduction concerns
arbitrary interfaces of the specified degrees; it imposes no cyclic
action on the ten vertices or any homogeneous interface assumption.

## Second reduction: the full finite local input

Let Z_a:L_a -> R_a denote the degree-three interface. The exact
same-fiber equation makes Z_a the point-block incidence matrix of a
linear combinatorial (10_3) configuration. The complete catalogue
dependency and its explicit data are described in
[D1_LOCAL_CONFIGURATION_CATALOG.md](D1_LOCAL_CONFIGURATION_CATALOG.md).
The primary source is Betten, Brinkmann and Pisanski, *Counting symmetric
configurations v_3*, Discrete Applied Mathematics 99 (2000), 331-338,
[Table 1](https://doi.org/10.1016/S0166-218X(99)00143-2).
The ten-type count concerns abstract incidence configurations, with
point-preserving isomorphisms, not merely the nine geometrically
realizable types. The two supplied ten-example tables were compared
locally; that comparison checks their transcription, while completeness
is inherited from the cited classification.

The three Z interfaces have disjoint endpoints, so independent relabeling
of their six fibers normalizes each Z to one of the ten representatives.
Both internal matchings remain free: choose S_L in the primal cubic
leave and S_R in the dual cubic leave of the selected Z. A **state** is
the full triple (Z,S_L,S_R). The
[actual local-interface catalogue](../../../computations/dd82/construction/d1_10_3_catalog/local_interfaces.json)
gives 531 such states on the fixed representatives. All are retained in
[states.json](../../../computations/dd82/construction/d1_general_bridge_run/states.json),
including their full Z row masks and both matching permutations.

For two consecutive states i,j, write their residual two-factors as
F_Li and F_Rj. A degree-two bridge Y:L_i -> R_j must be the point-edge
incidence matrix of F_Li, with column labels identifying its line graph
with F_Rj. Such matrices exist precisely when the two factors have the
same cycle type. For a cycle type with c_l cycles of length l, the number
of distinct labeled matrices is

\[
                     \prod_l(2l)^{c_l}c_l!.
\]

The complete reasoning, all column-label freedom, and the orientation of
the eventual global equations are in
[D1_GENERAL_CONFIGURATION_ASSEMBLY.md](D1_GENERAL_CONFIGURATION_ASSEMBLY.md).
In particular, normalizing Z does not also fix every internal matching
to one common matrix.

## The bridge necessary condition, without triangle closure

For each state pair and compatible Y, define

\[
R_L=J-YZ_j^T,\qquad R_R=J-Z_i^TY.
\]

These are zero-one matrices with row and column sums four. To see the
first zero-one assertion directly, the two columns in a row of Y are
adjacent in F_Rj and hence form a noncollinear pair in the dual
configuration Z_j. Their two three-point neighborhoods in Z_j are
disjoint. For the second, the three points of a Z_i block are pairwise
nonadjacent in F_Li, so their two-edge incidence supports in Y are
disjoint. The implementation checks these disjoint unions explicitly.

A successful global graph would have a degree-one matching M_L from
L_i to L_j and one M_R from R_i to R_j. Each must satisfy, with the
corresponding source and target internal matchings,

\[
N=R-M-S_{\rm source}M-MS_{\rm target}\ge0.                 \tag{1}
\]

Since every row and column sum of the right side is one, N must be a
permutation matrix. In a full graph N is the route through the third
same-side fiber. This screen **does not** impose that route's product
with the other two matchings: it only asks for some M satisfying (1),
independently on the two sides. In particular, it does not impose
N=(M^T)^2, forbid M(u)=u, restrict the cycles of M, or reuse the special
constraints from the already closed homogeneous family.

For a proposed value M(u)=v, the complete support requirements are

\[
             R_{u,v}=R_{S_{\rm source}(u),v}
                    =R_{u,S_{\rm target}(v)}=1.
\]

The search assigns a permutation using precisely these domains and
distinct columns. The only additional exclusion is

\[
M(S_{\rm source}(u))\ne S_{\rm target}(M(u)),
\]

which prevents S_source M and M S_target from occupying the same cell.
The other pairs of permutation matrices are automatically disjoint
because the two S matrices are fixed-point-free matchings and M is
bijective. Hence every rejected branch violates (1), and every full
assignment surviving the branches satisfies (1). At a full assignment,
the code additionally recomputes N using integer subtraction and checks
its nonnegativity and all row and column sums. It asks for the first
local witness only; failure exhausts the full local M domain.

## Exact enumeration and the observed zero

The [compact preparation](../../../computations/dd82/construction/d1_general_bridge_prepare.py)
writes ten Z matrices and their primal/dual leave choices, rather than
millions of matrices. The
[C++ screen](../../../computations/dd82/construction/d1_general_bridge_search.cpp)
generates all Y matrices by every length-compatible cycle pairing, every
rotation, and both orientations of each cycle.

The enumeration groups equal work. Fix configuration types i,j, the
primal matching of i, the dual matching of j, and Y. The left condition
then depends only on the still-free primal matching of j, while the
right condition depends only on the still-free dual matching of i.
The program checks these two finite lists separately. This base Y
represents
|PM(dual_i)| times |PM(primal_j)| complete state-Y bridges. The feasible
full bridges are exactly the Cartesian product of the two feasible
lists. Thus grouping does not discard any state pair or Y labeling.

The sole [bounded run](../../../computations/dd82/construction/d1_general_bridge_run.py)
completed, with
[actual result](../../../computations/dd82/construction/d1_general_bridge_run/search.json)
`complete=true` and the following full-domain counts:

| Cycle type | Base Y alignments | Complete state-Y bridges | Left M feasible | Right M feasible |
| --- | ---: | ---: | ---: | ---: |
| (10) | 32000 | 1788020 | 0 | 0 |
| (3,3,4) | 576 | 28224 | 0 | 0 |
| (3,7) | 4116 | 162624 | 0 | 0 |
| (4,6) | 9600 | 921984 | 0 | 0 |
| (5,5) | 33800 | 1377800 | 0 | 0 |
| Total | 80092 | 4278652 | 0 | 0 |

The total and each cycle-type count agree exactly with the independently
calculated expected domain sizes. Statistics for every ordered pair of
configuration types are also saved. The screen made 1157968 local
existence calls and visited 1163728 backtracking nodes. Measured process
CPU time was 0.121869 seconds on one CPU, with exit status zero; see
[resources.json](../../../computations/dd82/construction/d1_general_bridge_run/resources.json).
The authorized limit was ten CPU seconds, with an internal stop at 9.8
seconds to preserve a partial result if needed; it was not reached.

The [witness file](../../../computations/dd82/construction/d1_general_bridge_run/search.witnesses.jsonl)
is empty because there are no surviving bridges. Had a bridge survived,
its two complete state IDs, Y, and first M/N witness on each side would
have been saved. The program would not have supplied all local M
solutions or asserted their compatibility around a triangle.

Every original graph in the claimed equitable model must survive the
quotient reduction, configuration normalization and at least one of
these necessary bridges. The complete bridge domain is empty, already
on either single-side matching condition. This closes the stated
general degree-one six-fiber family. No three-state cycle assembly was
launched, and no conclusion about arbitrary sixty-vertex graphs follows
without a separate theorem forcing this equitable partition.
