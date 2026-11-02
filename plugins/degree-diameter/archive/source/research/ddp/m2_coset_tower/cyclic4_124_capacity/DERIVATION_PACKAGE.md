# Four C31 orbits, degree six, diameter-three capacity

## Target

Completely enumerate connected four-vertex undirected pseudographs whose
degrees are six, counting each loop twice. For each base, compute the
distinct F31 linear forms supplied by all walks of length at most three
between every ordered pair of base vertices. The lift has 124 vertices.
Filter by the necessary condition that each of the sixteen sets contains
at least 31 forms. This task does not assign actual field voltages.

## Status

COHERENT AS STATED. The computation completed all 47 connected base types.
25 survive the necessary capacity condition. The K4 double-edge base
222 is highest by minimum capacity, with diagonal 55 and off-diagonal 44.
The tentative diagonal count 61 is corrected to 55 below.

## Invariant Object

For fixed source and target orbits i,j, F_ij is the set of directed
edge-traversal coefficient vectors modulo 31 for walks i to j of length
at most three. The relevant capacity is |F_ij|. It counts different
linear functions of voltage variables, not different words or actual
field values after an assignment.

## Assumptions

- Four free C31 vertex orbits, with vertices (i,x), i in {0,1,2,3},
  x in F31.
- An oriented cross edge i to j with voltage z gives the matching
  (i,x)--(j,x+z); reversal has voltage -z.
- A loop with nonzero voltage z gives a 31-cycle inside its orbit,
  contributing degree two.
- For a simple lift, parallel cross voltages in one orientation must
  differ. Loops at one vertex must have nonzero voltages, pairwise
  unequal up to sign. These are restrictions on future assignments,
  not restrictions that remove symbolic walks.
- The nonloop support of the base is connected.

## Notation

Let l_i be the number of loops at vertex i and let the cross counts be
(m01,m02,m03,m12,m13,m23). Their degree equations are

    2*l_i + sum_{j != i} m_ij = 6.

There are twelve undirected base edges. Each has two distinct directed
darts, also when it is a loop. The inverse dart of d is d xor 1. A
nonloop spanning tree has three edges; fixing those voltages to zero
leaves nine free voltage coordinates.

## Derivation Strategy

Use the exact degree-equation and S4-orbit enumeration from the completed
172-point capacity calculation, with degree six and field order 31.
Recompute all bases and their forms at the new parameters. Keep loop
orientations and all repeated same-way loop traversals. Compare raw
twelve-coordinate forms with the nine-coordinate tree-gauge forms.

The previously read local formula-derivation skill is used to distinguish
exact identities, necessary bounds, and interpretations. This task does
not launch a proof-audit workflow or an actual construction search.

## Derivation Map

1. Degree equations determine the other four cross counts from l_i,
   m01, and m02.
2. Canonicalization under all 24 base permutations preserves all types.
3. Removing immediate inverse darts preserves all short reachable
   endpoints; each root has 1+6+30+150=187 reduced walks.
4. Their signed edge sums are the exact displacement functions in F31.
5. The tree-incidence argument proves gauge does not merge different
   forms with fixed endpoints.
6. Covering all 31 vertices of a target orbit requires at least 31 forms.

These are exact steps, with no approximation. Ranking surviving bases by
their form counts is an interpretation and does not establish existence.

## Main Derivation

### Complete degree and isomorphism enumeration

For l_i in {0,1,2,3}, put r_i=6-2*l_i. Set a=m01 and b=m02. Then

    c = m12 = (r0+r1+r2-r3)/2-a-b,
    m03 = r0-a-b,
    m13 = r1-a-c,
    m23 = r2-b-c.

Enumerate 0<=a<=min(r0,r1) and 0<=b<=min(r0-a,r2), and retain precisely
the solutions whose cross counts are nonnegative. All r_i are even,
so the formula for c is integral. Every labeled solution has a unique
l,a,b and occurs exactly once. Unlike degree seven, degree six allows
r_i=0; these isolated base vertices are rejected by the connectivity
test, rather than being omitted without a test.

There are 670 labeled degree solutions, 142 disconnected and 528
connected. Taking the lexicographically smallest image under S4 gives
47 connected types: 6 without loops and 41 with loops. For every type,
the program checks that its labeled occurrence count equals the size
of its S4 orbit.

### Reduced walks and gauge

Only the exact inverse dart of the preceding step is prohibited. This
gives 1,6,30,150 walks at lengths 0,1,2,3 from each root. Same-way
repeated loop traversal, and returning along a different parallel
edge, remain allowed. All signed coefficient vectors are reduced
modulo 31 and deduplicated separately for each endpoint slot.

For an oriented edge i to j, fiber relabeling x'=x+p_i changes its
voltage to z'_e=z_e+p_j-p_i. Three nonloop tree voltages can be set to
zero. If two fixed-endpoint walk forms agree on the nine non-tree
coordinates, their difference is a circulation supported on a tree.
The oriented incidence columns of a tree are independent over F31,
so the difference vanishes. Loops are never deleted by this gauge.
Thus raw and gauge equality coincide. The program explicitly checks
the resulting cardinalities in all 47*16=752 endpoint slots.

### Exact coverage at an assignment

Given legal voltages z, define E_ij(z)={c dot z:c in F_ij}. Then D<=3
is equivalent to E_ij(z)=F31 for all sixteen ordered slots. Simultaneous
translation x to x+t is an automorphism, so four source representatives
would suffice to verify the entire lift; base S4 symmetry alone does
not justify fewer representatives after assigning voltages.

If V_ij is the set of outgoing dart voltages from i to j, with
V_ji=-V_ij and V_ii the signed loop voltages, the same sets are given by

    E = I union V union V^2 union V^3,

using union and Minkowski sum as the matrix operations. Here I has {0}
on its diagonal and empty off-diagonal sets. Immediate reversals in
this expression add no displacement absent from the reduced-walk sets.
Capacity |F_ij|>=31 is necessary, but it does not guarantee those sets
evaluate onto F31 simultaneously.

### K4 double edges: diagonal 55, off-diagonal 44

For the base with two edges between every pair and no loops, fix a root.
Its self-slot reduced walks are:

- The empty walk: 1 form.
- Two-edge returns using different parallel edges:
  3*2*(2-1)=6 forms.
- Three-edge triangles: 3*2 choices of the two other vertices, with
  2^3 edge choices per triangle, giving 48 forms.

Thus the diagonal is 1+6+48=55. The figure 61 counts six immediately
reversed two-step walks again; all six have zero displacement already
represented by the empty walk. It is not a distinct-form count.

For fixed distinct endpoints i,j, the counts are 2 forms at length one,
8 forms at length two, and 34 at length three. The last number splits as:

- 2 alternating walks i,j,i,j along the two parallel edges;
- 8 walks first reaching j and returning to it through a third vertex;
- 8 walks returning to i through a third vertex before the last edge;
- 16 walks through both other vertices, in either order.

These types have different edge supports; within a type the surviving
edge choices give different coefficients. Therefore no further
symbolic collision occurs: each root has 55+3*44=187 distinct forms.
The exhaustive vector enumeration agrees with this separate count.

The matrix is

    55 44 44 44
    44 55 44 44
    44 44 55 44
    44 44 44 55.

Its minimum 44 is the largest among all 47 bases. At actual voltages,
each off-diagonal set must turn its 44 forms into all 31 values; its
repetition loss must equal 13. Each self-slot has 55 forms and must
have repetition loss 24. The loss is forms evaluated minus distinct
values, not the number of unordered colliding pairs. These statements
are exact coverage criteria, not a construction claim.

## Remarks and Interpretation

25 bases survive: 3 loop-free and 22 with loops. The leading three
minimum capacities are 44 (222, no loops), 42 (cross counts
1,2,3,3,2,1, no loops), and 37 (including a loop-bearing type).
The leading loop type has l=(0,0,1,1) and cross counts
(2,1,3,3,1,0); it has minimum 37 and total capacity 704.

This is a parameter migration of the same four-orbit voltage mechanism,
not another seed of the old graph. The degree changes from seven to six,
the field from F43 to F31, the edge count of the base from fourteen to
twelve, and its free gauge coordinates from eleven to nine. The number
of reduced walks per root changes from 302 to 187 and the target fiber
size from 43 to 31. A successful D3 lift would have order 124, above the
saved (6,3) baseline 120; no such lift is supplied by this calculation.

There is no inference that the migration improves the symbolic margin:
222 has worst-slot ratio 44/31, whereas the old 322 base has 68/43.
Both degree and coverage constraints have genuinely changed, but actual
voltage feasibility remains unresolved here.

## Boundaries and Non-Claims

- Complete only for connected six-regular four-vertex voltage bases
  over C31, including loops and parallel edges.
- No actual field assignment, lifted graph, root BFS, or new lower
  bound was produced.
- No claim about arbitrary 124-vertex graphs or the latest public
  record is made. The value 120 is the saved comparison requested.
- No earlier 172-point, M1, or diameter-five search was rerun or edited.

## Open Risks

The base classification and stated capacity counts are complete. The
remaining mathematical question is whether some legal assignment to a
surviving base covers all 31 displacements in every endpoint slot.

A parallel paper calculation confirmed the 222 diagonal/off-diagonal
counts without another program, graph, or BFS. It was not an external
review or formal certification.
