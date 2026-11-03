# Four regular nonabelian orbits: D64 and Q64 capacity

## Target and status

**COHERENT AS STATED; both finite phase ranges completed.** The graph
mechanism has four vertex orbits of size 64, degree eight, and target
diameter three. Its potential order 256 exceeds the requested saved
(8,3) comparison value 253, but no graph or new lower bound is supplied
by this capacity calculation.

The task enumerates every normalized phase assignment for two fixed
groups, without assigning their Z32 coordinates. Both groups have
8192 phase masks. D64 has 1953 capacity survivors; Q64 has 7930.

The local formula-derivation skill's distinction between exact algebra,
necessary capacity, and interpretation is used here. This is not a
new proof-audit workflow, external review, or formal proof artifact.

## Groups and exact inverse rules

Use the common notation G_epsilon with epsilon=0 for D64 and epsilon=1
for the generalized quaternion group Q64. Elements are (x,s), with
x in Z/32Z and s in {0,1}, and

    (x,s)(y,t) = (x+(-1)^s*y+16*epsilon*s*t, s xor t).

For epsilon=0 this is the stated dihedral semidirect product. For
epsilon=1 it is the normal form r^x*j^s with
r^32=e, j^2=r^16, and j*r*j^(-1)=r^(-1), giving the generalized
quaternion group of order 64.

The inverse formula is

    (x,s)^(-1) = (-(-1)^s*x+16*epsilon*s, s).

Thus even-phase inverse is (-x,0). Odd-phase inverse is (x,1) in D64,
and (x+16,1) in Q64. Treating the quaternion odd-phase elements as
self-inverse would produce the wrong symbolic collisions.

All translation arithmetic is over Z32, not a field. No projective
normalization, division by arbitrary coordinates, or field scaling
has been used.

## Graph and labels

Vertices are (i,g), for i=0,1,2,3 and g in G_epsilon. A base edge e
oriented from i to j with voltage h_e gives

    (i,g) -- (j,g*h_e) for every g.

There are no loops in the base. Cross multiplicities are

    (m01,m02,m03,m12,m13,m23)=(3,3,2,2,3,3).

Each base vertex has degree eight, with sixteen undirected base edges
in total. Matchings in the same endpoint class must have distinct
group voltages for the lift to remain simple and eight-regular.
For fixed phases, equal phases require distinct x coordinates;
different phases are already distinct. The identity is allowed on
a cross edge. Future assignments must impose this legality condition.

Left multiplication by any k in G_epsilon, simultaneously on all four
orbits, is an automorphism because k*(g*h_e)=(k*g)*h_e. Hence the four
roots (i,e) represent every graph vertex. This symmetry is proved for
nonabelian groups and does not require commutative voltages.

## Gauge and complete normalized input range

Changing coordinates inside orbit i by g'=g*k_i changes a voltage to

    h'_e = k_i^(-1)*h_e*k_j.

Choose tree edge IDs 0,3,6, respectively one matching in classes
01,02,03. With k_0=e, solve successively along the tree to make those
three voltages the identity. Every original voltage assignment has
such a normalized representative. Conversely, all thirteen remaining
voltages are unrestricted group elements in this tree gauge.

This transformation changes phases as well as coordinates: if k_i
has phase q_i, then p'_e=q_i xor p_e xor q_j. It would be incorrect to
delete tree translation columns while leaving arbitrary original tree
phases unchanged. The implementation works directly in the normalized
tree-identity system, so it never makes that deletion.

The edge ordering is:

    01: 0,1,2; 02: 3,4,5; 03: 6,7;
    12: 8,9; 13: 10,11,12; 23: 13,14,15.

The thirteen free edges, in both bit and coordinate order, are

    [1,2,4,5,7,8,9,10,11,12,13,14,15].

Phase mask bit k gives the phase of free edge k in this list. Every
mask 0,...,8191 is evaluated exactly once in each group. There is no
extra quotient by edge permutations, base permutations, or conjugacy.
These are complete marked normalized phase ranges, not counts of
nonisomorphic graphs.

## Exact short-word coefficient rule

For each fixed phase mask, a short word's translation coordinate has
the affine form

    c + sum_{k=0}^{12} a_k*z_k  (mod32),

with c=0 in D64 and c in {0,16} in Q64. Its final phase is also recorded.
Each forward dart is 2e and its inverse is 2e+1.

Suppose the current phase is s, the next edge has phase p, and rev is
zero for a forward dart and one for its inverse. The coefficient of
that edge variable added by the step is

    (-1)^s                         if rev=0,
    (-1)^(s+p+1)                   if rev=1.

The phase then becomes s xor p. In Q64, writing c=16*c_bit, update

    c_bit ^= p & (s xor rev),

using the phase s before the step. This follows from the inverse's
additional 16*p on a reversed dart and the multiplication cocycle
16*s*p. The sign of 16 is immaterial modulo 32. D64 has no such
constant update.

The producer enumerates every nonbacktracking base walk of length
0,1,2,3: respectively 1,8,56,392 per root, totaling 457. Only the
immediately inverse dart is prohibited; different parallel edges are
kept. Immediate reversal composes to the group identity, so removing
it does not lose a vertex reachable within three steps.

There are four source orbits, four target orbits, and two final phases,
giving thirty-two target slots. For each slot, the producer deduplicates
the full affine form (a_0,...,a_12,c) modulo 32. Different constants
0 and 16 are not merged.

Because the word length is at most three, signed coefficients lie in
[-3,3]. Equality modulo 32 is therefore equivalent to equality of
these signed coefficient vectors; the representation packs each
coefficient plus three into three bits. A separate bit records the
constant. This is an exact storage representation, not a numerical
approximation or an artifact hash.

Two affine forms are identical functions on Z32^13 exactly when their
constants and coefficient vectors agree modulo 32. The constant is
determined at the zero input and each coefficient by the corresponding
unit input; this algebraic argument does not assume a field.

## Necessary capacity and remaining coverage

For every root i, target j, and target phase s, the actual coordinates
reached by short walks must include all 32 residues. Thus at least 32
different symbolic affine forms are necessary in each slot.

For a fixed legal coordinate assignment, actual D<=3 is equivalent
to all thirty-two evaluated sets being Z32. Left G action then gives
coverage from every graph vertex. Symbolic capacity alone does not
imply this simultaneous evaluation property, especially over a ring
with nonunits and assignment-dependent collisions.

## How the nonabelian rule changes the old collisions

Take three distinct matching voltages in one endpoint class,
h_e=(x,p), h_f=(y,q), h_g=(z,r). Over an additive voltage group,
h_e*h_f^(-1)*h_g and h_g*h_f^(-1)*h_e have the same coordinate.
In D64 their coordinates are instead

    x+(-1)^(p+q+1)*y+(-1)^(p+q)*z,
    z+(-1)^(r+q+1)*y+(-1)^(r+q)*x.

For phases (p,q,r)=(0,0,1), these are x-y+z and z+y-x: different
linear forms over Z32. Thus the new mechanism truly separates some
commutative collisions; it is not a relabeled cyclic-voltage seed.

There is an opposing dihedral collision. Any closed walk of odd phase
has value (L,1), which equals its inverse in D64. Reversing the walk
therefore produces the same symbolic form. In Q64 its inverse is
(L+16,1), so the reversed walk supplies a different affine form with
the same coefficient vector and the other constant.

Consequently, in a Q64 self/odd slot all actual reachable coordinates
occur in pairs separated by 16. Covering Z32 in such a slot can be
viewed as covering all residues modulo 16 and then taking both lifts.
This observation does not remove the other slots or establish coverage.

The coefficient part of every fixed walk is the same in D64 and Q64;
only the quaternion constant may differ. Forgetting that constant maps
the Q64 form set onto the D64 form set, proving that each Q64 symbolic
capacity is at least the corresponding D64 capacity.

## Completed finite results

| Group | Phase masks completed | Passing masks | Tight slots among passing masks | Best minimum capacity |
|---|---:|---:|---:|---:|
| D64 | 8192 | 1953 | 3024 | 36 |
| Q64 | 8192 | 7930 | 144 | 52 |

Ranking uses larger minimum slot capacity, then larger total capacity;
the first mask in numeric order breaks a remaining tie. D64's leading
mask is 239, total capacity 1510. Q64's is 1205, total capacity 1804.
These are phase patterns only, not voltage assignments or graphs.

The saved-table comparison confirms Q64's capacity is never smaller in
any of 8192*32 slots. Every one of the 8191 nonzero phase masks gains
capacity in some slot. Q64 adds 5977 passing masks. The all-zero phase
mask gives exactly the same table in both groups and fails because
its odd-phase slots are empty.

Recorded CPU for preparation, compilation, and both capacity runs was
2.365815 seconds. Reading and comparing the two completed tables took
0.331696818 seconds. Thus recorded work here totals 2.697511818 CPU
seconds, within the shared single-worker 120-second budget. No actual
Z32 assignment, graph, or BFS was evaluated.

## Boundaries and next unresolved condition

The complete scope is the phase-capacity stage for the two fixed groups
and this one fixed base. It does not exhaust coordinates, classify
isomorphism types, or exclude either group family. Passing counts and
larger quaternion capacity are not evidence of a verified graph.

The next unresolved condition is actual simultaneous coverage in all
thirty-two slots under distinct parallel group voltages. No actual
search has been started by this task. The older cyclic and other
construction directories were not changed.
