# C60/F4 global-conic domain: complete negative result

The prescribed domain is closed by a necessary rank condition, before any
graph is generated. The complete run was PID2212495, exit0,
**0.084363529 CPU seconds**. It checked all60×60×16=57600 inverse-compatible
projectivity triples. Six satisfy every unique-distance-three forced cell;
none gives a full-rank three-word to all3300 required controller pairs.

| Complete-domain stage | Number |
|---|---:|
| port0/1 paired quotient projectivities |60|
| port2/3 paired quotient projectivities |60|
| port4 projectivities admitting a linear involution lift |16|
| all combined triples |57600|
| triples avoiding every forced bad cell |6|
| triples covering every required pair by rank3 |0|
| rank plus external-pencil solutions |0|
| rank plus every-pencil solutions |0|

No matrix, field, controller or random-seed search followed. Graph count and
BFS count are zero. No3840-point graph is claimed.

## Exact mathematical scope

Fix the saved literal C60 and its inverse ports(1,0,3,2,4). Work over
F4=F2[w]/(w²+w+1), with global directions

\[
L_0=(0,0,1),\ L_1=(1,0,0),\ L_2=(1,1,1),\
L_3=(1,w,w+1),\ L_4=(1,w+1,w).
\]

The excluded class consists of arbitrary invertible **global** linear
matrices T_p with T_inv(p)=T_p⁻¹ and T_p L_p proportional to L_inv(p), using
all four coefficients on each target line. These hypotheses include T4²=I.
They do not require any particular longitudinal/shear entries in the3×3
matrices. All such entries are invisible to the central-turn rank test.

The result does not exclude different matrices on different edges, different
frames at different vertices, directions not forming the specified global
arc, affine offsets, a different controller or a different fiber rule.
No classification of all labeled five-arcs is claimed here.

## Why the finite projectivity domain is complete

Let H_p send L_p to the first coordinate axis. On the two-dimensional
quotient, every possible T_p induces an element Q_p of PGL(2,4). This group
has60 elements; the script enumerates all invertible2×2 matrices modulo
nonzero scalar by normalizing the first nonzero entry. Inverse port charts
give inverse quotient maps. For port4, Q4² is scalar. In F4 every nonzero
element has a unique square root, so every such projectivity can be scaled
to square to I; block-diagonal lift in H4-coordinates then provides a genuine
T4²=I. There are16 such projectivities, including the identity.

For a three-word with central port p, incoming reverse port i and outgoing
port j, invert the last chart. Its noise span has rank equal to

\[
\operatorname{rank}(T_pL_i,L_{\mathrm{inv}(p)},L_j).
\]

This is3 exactly when Q_p maps the projected L_i to a point different from
the projected L_j. It therefore depends only on Q_p. The code precomputes
the required-endpoint bitmask for every good central turn, combines inverse
ports into two paired components and the self-inverse component, and takes
their three-way OR. Longitudinal entries or scalar lifts cannot change this
answer. `PROJECTIVITIES.json` records every candidate and good/bad cells;
`check_once.py` is the complete deterministic enumeration.

## Why full-rank NB3 is necessary here

The literal controller check covers all3300 ordered nonadjacent/equal pairs.
For a distinct nonadjacent endpoint, every length≤3 route is either NB2 or
NB3: a backtrack of length3 would end at an adjacent vertex. The actual word
counts give at most four potentially rank≤2 route images in total. At zero
source coordinate, all images are linear subspaces and contain0. Thus if
every NB3 has rank≤2, their union contains at most1+4(16−1)=61 points.

For a self endpoint, the length-two backtracks give five lines, contributing
at most15 nonzero points. Together with the actual number (at most three) of
rank≤2 NB3 images, the union is again at most61. The code stores the bound
for every pair and confirms its maximum is61. Consequently D≤3 requires a
rank3 NB3 for every required pair. All57600 projectivity triples fail this
necessary condition. This closes the stated graph class, not just a
sufficient full-pencil certificate. Affine constants would destroy the
common-zero count and remain outside this conclusion.

## Adjacent-edge scope correction

Literal ports0,1,4 have no adjacent NB2 or NB3 route, so full pencil coverage
is necessary for them. Ports2,3 lie on triangles and have an extra NB2 route;
they cannot be treated as pure-backtrack edges without another argument.
The implementation records rank-only, external-pencil and all-pencil counts
separately. All are zero already at rank-only, so the negative result does
not rely on the stronger adjacent-pencil claim.

For completeness, a paper-only refinement was obtained: after the forced
cells, a four-plane port2 pencil would have the unique bad perfect matching
(0,0),(1,1),(3,4),(4,2). Put A=L2,B=L3,C=L4,T=T2. This forces
TB∈span(B,C) outside span(B). Its triangle two-step image is
span(T⁻¹A,A), which cannot contain B, since that would force
TB∈span(A,B). It adds at most3 new points to the52-point pencil, still below64.
This refinement was not needed by the complete negative run.

## Execution accounting

One initial invocation PID2206115 stopped in preparing the very first
projectivity because normalization mistakenly selected the first entry
instead of the first nonzero entry. It evaluated **zero** projectivity
triples and produced no graph. The one-line fix preceded the sole complete
enumeration; `PREPARATION_FAILURE.json` retains the failure. Its exact child
CPU was not retained, so0.084363529 is the measured complete-run CPU, not an
invented aggregate including that failed preparation. No scored candidate
was repeated or continued after a timeout.

Inputs/outputs: PREDICTION.md, check_once.py, PROJECTIVITIES.json,
CONTROLLER_WORD_CAPACITY.json, SOLUTIONS.json(empty), RESULT.json and
HANDLE.json. This batch is terminal; no additional matrix or affine-offset
domain is activated by the result.
