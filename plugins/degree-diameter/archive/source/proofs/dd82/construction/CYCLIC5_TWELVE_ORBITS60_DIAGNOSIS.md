# Twelve cyclic orbits of length five: seed diagnosis and construction domain

The bounded diagnosis did **not** find an automorphism of cycle type
5^12 in the actual 20-bad-pair seed. It also did **not** prove that none
exists. All automorphisms preserving each of its original six Petersen
fibres were tested and contain no such element; the unrestricted
automorphism enumeration was stopped at its CPU limit. Thus no voltage
description of this particular seed has yet been established.

Source:
[cyclic5_twelve_orbits60_diagnose.py](../../../computations/dd82/construction/cyclic5_twelve_orbits60_diagnose.py).
Actual result:
[diagnosis.json](../../../computations/dd82/construction/cyclic5_twelve_orbits60_run/diagnosis.json).

## Actual input and bounded test

The input is
[petersen_all_matchings_run/candidate.best.edges](../../../computations/dd82/construction/petersen_all_matchings_run/candidate.best.edges),
the complete 60-vertex, 240-edge, eight-regular graph whose saved independent
verification has twenty bad pairs. It is **not** the older
three-permutation C5-symmetric seed with fifty bad pairs in
[PETERSEN_SIX_FIBERS.md](PETERSEN_SIX_FIBERS.md). The existence of a cyclic
symmetry in that older restricted construction says nothing about this
new input.

The installed environment has NetworkX 3.4.2. The checks found no pynauty,
igraph, dreadnaut, labelg or geng executable/module; no software was
installed.

First, each of the 120 automorphisms p of the first ten-vertex Petersen
fibre was transported to fibre i through the actual 0--i matching M0i:

\[
 p_i=M_{0i}\,p\,M_{0i}^{-1}.
\]

Every graph automorphism preserving all six original fibres individually
must have this form, because it must preserve their unique matching
interfaces. Each transported permutation with all cycles of length five
was checked directly against all 240 original edges. None passed. This
is a complete test only of that fibre-preserving subgroup.

The second stage used NetworkX GraphMatcher on the full sixty vertices,
with the number of bad pairs incident to a vertex as a preserved color.
That color is a graph invariant, so it does not exclude any automorphism;
no Petersen-fibre label was imposed in this stage. It returned two
automorphisms before the stop and found no element of cycle type 5^12.
The automorphism iterator did not finish, so this is an UNKNOWN result
for the full graph.

The single episode used 4.599840525 CPU seconds and 4.603985924 wall
seconds, with one CPU, a five-CPU-second hard limit and 1 GiB address-space
limit. It performed no optimization, SAT call or full BFS rerun. There
is no running job.

## Exact complete construction domain if a C5 action is chosen

Independently of whether this particular seed has the symmetry, take
vertices (a,t), where 0≤a<12 and t∈Z5, with the common translation
(a,t)↦(a,t+1). All invariant simple undirected graphs are unions of the
following disjoint edge orbits:

- For a<b and d∈Z5, select or omit the matching
  {(a,t),(b,t+d)} for all t. There are binomial(12,2)·5=330 such orbits.
- For each a and s∈{1,2}, select or omit the five-cycle edges
  {(a,t),(a,t+s)} for all t. There are 12·2=24 such orbits.

These 354 orbits each have five edges and partition all 1770 unordered
vertex pairs. Hence a 240-edge invariant graph selects exactly 48 of
them. If x_abd records a selected matching and y_as a selected internal
cycle, the exact degree-eight constraints are

\[
 \sum_{b<a,d}x_{bad}+\sum_{b>a,d}x_{abd}
       +2y_{a1}+2y_{a2}=8\qquad(0\leq a<12).
\]

Any binary choice satisfying these twelve constraints produces an
explicit simple 60-vertex, 240-edge, eight-regular graph. No original
Petersen internal graph or six-fibre interface is fixed. This is a
different domain from the old three-permutation construction; it also
differs from the previously investigated cyclic lifts with two, three
or four large vertex orbits.

For an exact coverage formulation, let D_ab⊆Z5 be the selected shifts
from orbit a to orbit b. Then D_ba=−D_ab; D_aa is a union of the pairs
{±1}, {±2} selected by y. The targets reachable from (a,0) in one or two
steps in orbit b have shifts

\[
 C_{ab}=D_{ab}\cup\bigcup_{c=0}^{11}(D_{ac}+D_{cb}).
\]

Diameter at most two is exactly C_ab=Z5 for a≠b, and
Z5\{0}⊆C_aa for a=b. These conditions refer to the same complete
expanded graph and allow internal and external edge orbits to vary
together. They define a possible future construction experiment; none
was run in this diagnostic.

## Precise remaining seed obligation

An actual permutation of cycle type 5^12 preserving the input edge set
is still needed before claiming that this seed lies in the 354-variable
domain. The existing twenty bad pairs involve twenty vertices, an
automorphism-invariant set. A possible further reduction is to use
automorphisms of the induced graph on this set together with its bad-pair
relation: if the other forty vertices have pairwise distinct neighbour
sets in the invariant set, their images would be uniquely determined.
That proposed uniqueness and reduction were not evaluated in this
episode; no further time was silently added to the capped search.

A subsequent separately authorized diagnostic found ten neighbour-pair
classes of size four, so the proposed unique lifting is unavailable. It
also exported the distinct old 50-bad seed's verified C5 voltages; see
[the endpoint and old-seed report](CYCLIC5_TWELVE_ORBITS60_ENDPOINT_AND_OLD_SEED.md).
