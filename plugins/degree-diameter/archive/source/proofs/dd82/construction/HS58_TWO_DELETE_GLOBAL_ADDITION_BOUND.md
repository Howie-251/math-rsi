# HS58 with two old deletions: a global bound on all old additions

Date: 2026-10-12. Without fixing the eight-vertex auxiliary graph,
the addition graph, or any attachments, the counting and HS matrix
identities below prove **at most eight old additions**. The final
sections exclude eight additions too, using the existing saturated
endpoint arguments for the last case. Thus the combined bound is
**a<=7**. This is an upper bound on the addition count, not an
exclusion of the remaining a=6,7 constructions. No graph enumeration
or SAT is used.

## Notation and the zero-port inequality

Let Q be HS50, D two distinct original edges, and A a set of a
original nonedges added on the old vertices. Let M=Q-D+A. Suppose
eight new vertices and arbitrary attachments give an eight-regular
graph G of diameter two. The graph H on the new vertices is arbitrary.
For each old vertex x define

\[
r_x=d_D(x),\quad a_x=d_A(x),\quad
p_x=|B_x|=1+r_x-a_x\ge0.
\]

Here r_x is deleted degree, not the available port budget 1+r_x.
At an ordinary old vertex r_x=0, so a_x<=1. Branching in A can
therefore occur only at the at most four deletion endpoints. The
degree identities give sum p_x=54-2a and |E(H)|=a+5.

Put Z={x:p_x=0}, z=|Z|, and define excess weights
e_x=max(p_x-1,0), with E=sum e_x<=sum r_x=4. Then

\[
z=E+2a-4.                                           \tag{1}
\]

A zero-port vertex q has eight old neighbors and reaches new vertices
only through their attachments. Those neighbors must collectively
supply all eight labels. In particular

\[
d_M(q,Z)\le\sum_{t\in N_M(q)}e_t.
\]

This uses only a necessary count of available ports; it does not
mistake that count for coverage by distinct labels. Summing over q
gives

\[
2e_M(Z)\le\sum_t e_t d_M(t,Z)\le6E.                 \tag{2}
\]

The last bound holds because e_t>0 implies p_t>=2 and d_M(t)<=6.
A sharper available form is
sum_t e_t d_M(t,Z)<=sum_t e_t(7-e_t).

Let r(Z)=sum_(q in Z)r_q and d=e_D(Z). For q in Z,
a_q=1+r_q, so the added degree on Z is z+r(Z). Subtracting the
added degree on its complement shows

\[
e_A(Z)-e_A(V(Q)\setminus Z)=z+r(Z)-a,
\]

and therefore

\[
e_A(Z)\ge a+E+r(Z)-4.                               \tag{3}
\]

Writing m=e_Q(Z), equations (2)-(3) imply

\[
m+a\le4+2E-r(Z)+d\le4+2E.                         \tag{4}
\]

Indeed e_M(Z)=m-d+e_A(Z), while
r(Z)-d=d+e_D(Z,V(Q)\setminus Z)>=0. Ignoring m gives the first
general bound a<=12. The HS restriction on m is substantially stronger.

## HS edge bound and the uniform conclusion a<=8

If Q also denotes its adjacency matrix, its defining common-neighbor
counts give

\[
Q^2=6I-Q+J.
\]

On the subspace perpendicular to the all-one vector its eigenvalues
are 2 and -3. For the indicator of Z, subtracting its constant
component and applying the lower eigenvalue bound gives

\[
2m\ge {7z^2\over50}-3\left(z-{z^2\over50}\right),
\qquad m\ge {z(z-15)\over10}.                       \tag{5}
\]

Combining (1), (4), and (5), every proposed construction must satisfy

\[
{(2a+E-4)(2a+E-19)\over10}+a-4-2E\le0.             \tag{6}
\]

To exclude all a>=9 at once, write a=9+s with s>=0. Ten times the
left side of (6) is

\[
E^2-7E+36+4sE+36s+4s^2.
\]

Its first part is (E-7/2)^2+95/4, and every remaining term is
nonnegative. Thus (6) is impossible for a>=9. No case-by-case H
classification or enumeration of E is required.

## The two exact second-moment identities used at a=8

For any old set Z, let k_t=|N_Q(t) intersect Z| and let
s_2=sum_(q in Z)k_q^2. The HS matrix identity gives

\[
\sum_{t\notin Z}k_t=7z-2m,\qquad
\sum_{t\notin Z}k_t^2=z^2+6z-2m-s_2.                \tag{7}
\]

Two consequences will be useful:

1. If Z is independent and z=14, then
   sum_(t outside Z)(k_t-2)(k_t-3)=6. Every summand is nonnegative
   because k_t is an integer. In particular no outside vertex has
   k_t=6, since its single summand would already be 12.
2. If z=15, then
   sum_(t outside Z)(k_t-3)^2=10m-s_2<=8m. The inequality follows
   from s_2>=sum_(q in Z)k_q=2m.

These are exact counts for the original Q, not for the edited graph M.

## Eight additions, excess two

Suppose a=8. Equation (4), with m>=0, forces E>=2. If E=2, then
z=14 and equality in (4) forces m=0 and r(Z)-d=0. The latter
implies r(Z)=d=0, so no deletion endpoint is zero-port.

Equations (2)-(3) now force e_M(Z)=6 and
sum_t e_t d_M(t,Z)=12. A single weight-two excess vertex has only
five old neighbors and contributes at most ten, so it is impossible.
There must be exactly two weight-one excess vertices, each with all
six old neighbors in Z.

At least one of them has deleted degree one: a two-edge simple graph
has at most one vertex of deleted degree two. Such a vertex t has
p_t=2 and r_t=1, hence a_t=0. Its six retained Q neighbors all lie
in Z, and its deleted partner lies outside Z. Therefore k_t=6.
This contradicts consequence 1 of (7) for the independent 14-set Z.

## Eight additions, excess three

Now E=3, so z=15. Equation (4) gives 0<=m<=2. The lower bounds in
(2)-(3) give

\[
\sum_t e_t d_M(t,Z)\ge14+2m.                        \tag{8}
\]

Every positive excess vertex lies outside Z. Furthermore
d_M(t,Z)<=k_t+a_t. There are only two possible excess-weight patterns.

If the pattern is (1,1,1), its three vertices have
sum a_t=sum(r_t-1)<=1, because sum r_x=4. Thus (8) implies that their
three Q-neighbor counts sum to at least 13+2m. Their three deviations
from 3 sum to at least 4+2m. Cauchy-Schwarz and consequence 2 of (7)
would require

\[
8m\ge{(4+2m)^2\over3}.
\]

But (4+2m)^2-24m=4((m-1)^2+3)>0, a contradiction.

If the pattern is (2,1), the weight-two vertex is the shared endpoint
of adjacent D and has r=2,a=0. The other excess vertex is a deleted
leaf with r=1,a=0. Let their Q-neighbor counts be k_x,k_y. Equation
(8) gives 2k_x+k_y>=14+2m, hence
2(k_x-3)+(k_y-3)>=5+2m. Weighted Cauchy-Schwarz would require

\[
8m\ge{(5+2m)^2\over5}.
\]

The difference (5+2m)^2-40m=(2m-5)^2 is strictly positive for every
integer m. This is again impossible. These two patterns exhaust E=3.

## Eight additions, excess four

E=4 means every deletion endpoint has its maximal port count and no
addition meets a deletion endpoint. All additions are a nonempty
matching on ordinary zero-port vertices, and z=2a=16.

For adjacent D this is exactly the already proved
“Adjacent deletions with all endpoint ports maximal” obstruction in
[the nonuniversal exclusion](HS58_TWO_DELETE_FOUR_ADDITIONS_NONUNIVERSAL_EXCLUSION.md).
That lemma does not depend on H or on the number of matching additions.

For disjoint D, the zero-set proof in
[the saturated disjoint lemma](HS58_SATURATED_DISJOINT_ZERO_SET.md)
shows Q[Z] is independent. Its argument uses maximal endpoint ports,
the matching A, and the unique old paths, but never uses a=5 or
|Z|=10: one-endpoint-neighbor zero vertices cannot have a Q neighbor
in Z by the port count; two-endpoint-neighbor zero vertices cannot
be adjacent to each other by the forbidden Q triangles or four-cycles.
Thus it applies unchanged to z=16. Equation (5) gives
m>=16/10>0, contradicting independence.

This excludes E=4 and completes the a<=7 bound. The separate
[all-addition saturated study](HS58_SATURATED_DISJOINT_ALL_ADDITIONS.md)
also supplies a self-contained version of the zero-set argument and
stronger bounds for that particular endpoint pattern; those stronger
coordinate bounds are not needed for this last step.

## Remaining joint-construction domain

The proof applies to both adjacent and disjoint positions of D,
arbitrary original-nonedge addition sets A, arbitrary H, and arbitrary
attachments. It imposes no HS automorphism normalization and assumes
no auxiliary universal vertex. It therefore supplies a direct
candidate-preserving restriction for a joint all-A/all-B/all-H input.

Together with the separately completed exclusions for a<=5, only
a=6 or a=7 remain for exactly two original deletions. This note
does not decide either remaining count, does not assert an eight-vertex
H type, and does not certify a full 58-vertex construction. Useful
necessary constraints retained for those inputs are (1)-(4), the
exact row inequality before (2), and the HS moments (7).
