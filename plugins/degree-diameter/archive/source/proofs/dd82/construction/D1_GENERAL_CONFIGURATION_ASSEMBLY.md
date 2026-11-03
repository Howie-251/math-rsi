# Complete finite assembly model for the general degree-one fibers

Date: 2026-10-12. This note defines the entire remaining six-fiber model,
including both ends of every interface. It is a mathematical
parametrization, not a report of an executed enumeration or an exclusion.

The underlying quotient classification is in
[SIX_MATCHING_FIBERS_QUOTIENT.md](SIX_MATCHING_FIBERS_QUOTIENT.md).
The ten incidence representatives and the exact one-sided equivalence are
in [D1_LOCAL_CONFIGURATION_CATALOG.md](D1_LOCAL_CONFIGURATION_CATALOG.md).
Completeness of the ten representatives retains the published
classification dependency stated there.

## Coordinates and independent normalization of the three cubic interfaces

Index fibers by L_a,R_a, with a in Z/3Z. Their internal graphs are
perfect matchings. The degree-one interfaces form a triangle on each
side. Between the two sides, the interface degrees are

\[
q(L_a,R_a)=3,\qquad q(L_a,R_{a+1})=2,\qquad q(L_a,R_{a-1})=0.
\]

All matrices below use source vertices as rows and target vertices as
columns. Reversing an interface transposes its matrix.

Let H_1,...,H_10 be the fixed ten-by-ten incidence matrices from either
verified catalogue, with a consistently chosen numbering. Choose any
ordered triple t_0,t_1,t_2 in {1,...,10} and set

\[
                       Z_a=H_{t_a}:L_a\longrightarrow R_a.
\]

Every original graph in this quotient can be put into this form. The
local equation makes each original degree-three interface a (10_3)
configuration. A point relabeling and a block relabeling carry it to one
of the H_t. The three degree-three interfaces have disjoint endpoints,
so these six fiber relabelings can be made independently. They also
relabel all incident matchings and degree-two interfaces; those data are
allowed to vary below. No symmetry or polarity of H_t is needed.

In particular, after this normalization one must allow the internal
matchings on the six fibers to vary. One cannot simultaneously assert
that all of them remain the same previously fixed matrix S.

## Both leaves, their matchings, and all degree-two interfaces

Define the primal and dual cubic leave matrices

\[
\Lambda^L_a=J+2I-Z_aZ_a^T,\qquad
\Lambda^R_a=J+2I-Z_a^TZ_a.
\]

Choose arbitrary perfect matchings S^L_a in Lambda^L_a and S^R_a in
Lambda^R_a, and put

\[
F^L_a=\Lambda^L_a-S^L_a,\qquad
F^R_a=\Lambda^R_a-S^R_a.
\]

These are simple two-factors. The degree-two interface
Y_a:L_a -> R_{a+1} must satisfy both

\[
Y_aY_a^T=2I+F^L_a,\qquad
Y_a^TY_a=2I+F^R_{a+1}.                                    \tag{1}
\]

The columns of Y_a are precisely the edges of F^L_a. To describe all
column labels without loss, choose a bijection

\[
\phi_a:V(R_{a+1})\longrightarrow E(F^L_a)
\]

which is a graph isomorphism from F^R_{a+1} to the line graph of F^L_a,
and define (Y_a)_{uv}=1 exactly when u is an endpoint of phi_a(v).
Two columns then have a common one exactly when their corresponding
edges meet, proving (1). Conversely, (1) forces precisely this form.

Since the line graph of a disjoint union of cycles has the same cycle
lengths, such a Y_a exists if and only if F^L_a and F^R_{a+1} have the
same cycle type. If that type contains c_l cycles of length l, then the
number of distinct Y_a in the fixed coordinates is exactly

\[
              |\operatorname{Aut}(F^L_a)|
                 =\prod_{l\ge3}(2l)^{c_l}c_l! .             \tag{2}
\]

Indeed, between two isomorphic fixed graphs the isomorphisms form a
torsor for the automorphism group; each phi gives different incidence
columns. The factors account for rotations/reflections within cycles and
permutations of equal-length cycles, including triangles. Thus all
degree-two column-label freedom is included, rather than selecting just
one incidence matrix for each cycle type.

Equations (1) automatically give every same-fiber equation:

\[
S^L_a+Y_aY_a^T+Z_aZ_a^T=J+4I,
\quad
S^R_a+Y_{a-1}^TY_{a-1}+Z_a^TZ_a=J+4I.                       \tag{3}
\]

## Exact domains for the six remaining matchings

Orient the matchings around each triangle:

\[
M^L_a:L_a\longrightarrow L_{a+1},\qquad
M^R_a:R_a\longrightarrow R_{a+1}.
\]

After fixing the preceding data, form

\[
R^L_a=J-Y_aZ_{a+1}^T,\qquad
R^R_a=J-Z_a^TY_a.                                         \tag{4}
\]

The products subtracted in (4) are exactly the routes through the unique
common opposite-side fiber. Each has row and column sums six. Any entry
larger than one immediately rejects the current data: those two-step
routes already exceed the exact capacity on a degree-one pair. Otherwise
each R is zero-one with row and column sums four.

For a fixed R and internal matchings S_source,S_target, define the finite
domain

\[
\mathcal D(R;S_{\rm source},S_{\rm target})=
\{M\text{ a permutation matrix}:\quad
 N(M):=R-M-S_{\rm source}M-MS_{\rm target}\ \ge0\},           \tag{5}
\]

where the inequality is entrywise. The integer matrix N(M) has every
row and column sum one, so nonnegativity makes it a permutation matrix.
It is uniquely determined by M. Formula (5) is a complete local domain;
it does not assert that each member extends around its triangle.

Choose M^L_a from D(R^L_a;S^L_a,S^L_{a+1}) and M^R_a from
D(R^R_a;S^R_a,S^R_{a+1}). For each side independently impose the three
couplings

\[
             N(M_a)=M_{a-1}^T M_{a+1}^T.                    \tag{6}
\]

The right side is the route from fiber a to fiber a-1 through the reverse
of M_{a-1}, then from a-1 to a+1 through the reverse of M_{a+1}.
Thus (5)-(6) are precisely the six degree-one coverage equations with
possibly different internal matchings at their two ends. The transpose
equations cover the reverse orientations automatically.

## Remaining cross-half equations

For each a, the degree-zero pair L_a,R_{a-1} has exact capacity ten.
Its complete equation is

\[
M^L_aY_{a+1}+(M^L_{a-1})^TZ_{a-1}
 +Z_a(M^R_{a-1})^T+Y_aM^R_{a+1}=J.                         \tag{7}
\]

For the degree-two pair L_a,R_{a+1}, impose

\[
Y_a+S^L_aY_a+Y_aS^R_{a+1}
 +M^L_aZ_{a+1}+Z_aM^R_a\ \ge J.                            \tag{8}
\]

For the degree-three pair L_a,R_a, impose

\[
Z_a+S^L_aZ_a+Z_aS^R_a
 +(M^L_{a-1})^TY_{a-1}+Y_a(M^R_a)^T\ \ge J.                \tag{9}
\]

These matrices count all one-step and two-step routes for their specified
pair of fibers; the row sums are ten, twelve and thirteen respectively.
There are no omitted middle fibers: in (7) all four other fibers
contribute, while in (8) and (9) the two unlisted other fibers have a
zero interface on the required route. Transposes again supply reverse
orientations.

## Sufficiency and preservation of every original candidate

Given any data satisfying the construction rules and (6)-(9), use the
six S matrices as internal edges, the six M matrices on the two
triangles, Z_a and Y_a on the stated cross-half pairs, and zero on the
remaining pairs. All matrices are zero-one; diagonal fiber blocks are
simple matchings; reverse blocks are transposes. This defines a simple
graph on sixty vertices, each of degree 1+1+1+3+2=8.

The local identity (3) covers every distinct pair in a fiber. Equations
(4)-(6) cover every pair in a same-side triangle; (7)-(9) cover every
cross-half pair. Hence this expanded graph has diameter at most two.

Conversely, every eight-regular diameter-two graph with the specified
six-fiber partition has the proved quotient. Independently normalizing
its three Z interfaces gives the chosen H_t. Its internal matchings are
among the leave matchings, its Y matrices are among exactly the
line-graph isomorphisms above, and its actual six M matrices satisfy
(5)-(9) by counting their routes. Thus this finite input definition loses
no member of the general model.

The parametrization may represent a graph several times. No quotient by
automorphisms is required for completeness, and no count of these
parameter choices is a count of graph isomorphism types. The local
71-primal/71-dual matching catalogue is reusable input; this note has
not run the assembly domains, solved their coupling equations, or
excluded the family.
