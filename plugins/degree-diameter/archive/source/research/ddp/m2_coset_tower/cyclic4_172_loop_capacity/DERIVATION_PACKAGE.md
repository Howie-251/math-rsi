# Four cyclic orbits with internal cycle edges: exact symbolic capacity

## Target

Classify every connected four-vertex undirected voltage multigraph of degree
seven, allowing loops of degree contribution two. Its voltage group is
the additive field F43, so its lift has 172 vertices. Compute, for each
ordered base-vertex pair, the number of distinct linear forms represented
by walks of length at most three. A necessary condition for diameter at
most three is at least 43 forms in each of the sixteen slots.

The output is a complete base classification and a necessary capacity
filter, not an enumeration of voltage assignments or a graph construction.

## Status

COHERENT AS STATED. All 91 connected base isomorphism types were computed.
52 pass the necessary filter, including 48 with loops. No lift was generated.

## Invariant Object

For fixed base vertices i,j, let F_ij be the set of F43 coefficient vectors
of all directed base walks i to j of length at most three. A vector has one
coordinate for each of the fourteen undirected base edges. A chosen
orientation contributes +1 and its reversal contributes -1. The invariant
used for filtering is the cardinality |F_ij|, not the number of walks.

## Assumptions

- The four base vertices denote four free C43 vertex orbits, each of size 43.
- Each nonloop base edge is one matching between its two orbits.
- A base loop with nonzero voltage z lifts to the edges x to x+z in its
  orbit. Since 43 is odd, this is a 43-cycle and contributes degree two.
- All voltage variables are initially independent elements of F43.
- Simplicity of a chosen lift must be imposed separately: loop voltages
  are nonzero; distinct loops at one vertex have voltages unequal up to
  sign; distinct parallel nonloop edges have different voltages when
  oriented in the same direction.
- The underlying nonloop support is connected. This is necessary for a
  connected lift, but does not by itself make every voltage assignment
  connected.

## Notation

The loop multiplicities are l_0,...,l_3. The six cross multiplicities are
ordered as (m01,m02,m03,m12,m13,m23). They satisfy

    2 l_i + sum_{j != i} m_ij = 7.

Thus 0 <= l_i <= 3 and there are exactly fourteen undirected base edges.
Each edge e has two darts 2e and 2e+1, including when it is a loop. The
inverse of a dart d is d xor 1. The tree gauge fixes three nonloop edge
voltages to zero; the other eleven edge voltages remain free.

## Derivation Strategy

First solve the degree equations without any voltage restrictions. Then
take the lexicographically least image under all 24 vertex permutations.
For each connected representative, enumerate the short walks by darts,
deduplicate their actual coefficient vectors modulo 43, and compare the
counts with the same vectors restricted to the eleven gauge coordinates.

## Derivation Map

1. Degree equations reduce the labeled base enumeration to four loop
   counts and two cross multiplicities.
2. S4 canonicalization removes only base-vertex relabelings.
3. Removing immediately reversed darts preserves every short endpoint
   reachable by a voltage walk.
4. Summing signed edge variables is the exact lifted displacement in C43.
5. Restricting a fixed-endpoint coefficient vector to the non-tree
   coordinates does not create collisions.
6. Each coefficient vector evaluates to at most one field value, giving
   the necessary cardinality bound 43.

No approximation occurs in these six steps. Treating a passing base as
promising is an interpretation, not a sufficiency theorem.

## Main Derivation

### 1. Complete labeled enumeration

Write r_i = 7 - 2 l_i. Choose a=m01 and b=m02. The remaining four values
are forced:

    c = m12 = (r0+r1+r2-r3)/2 - a - b,
    m03 = r0-a-b,
    m13 = r1-a-c,
    m23 = r2-b-c.

All r_i are odd, so the displayed half-integer expression is integral.
For every l in {0,1,2,3}^4, enumerate
0 <= a <= min(r0,r1) and 0 <= b <= min(r0-a,r2), and retain precisely the
nonnegative solutions. Every labeled degree solution appears exactly
once, since its l,a,b are recovered from that solution.

This gives 1270 labeled solutions. Exactly 48 have disconnected nonloop
support; 1222 remain. Canonicalization under S4 gives 91 connected types.
For every type, the program also checks that its number of labeled
occurrences equals its number of distinct S4 images. There are 7 types
without loops and 84 with at least one loop.

### 2. Walk enumeration and its orientation requirement

There are seven outgoing darts at every base vertex. A length-k walk
without immediate reversal therefore has 7*6^(k-1) choices for k>=1.
Each root has 1+7+42+252=302 enumerated walks of lengths zero through three.

Only the exact inverse dart is forbidden. In particular, a loop may be
used twice or three times in the same direction; these produce 2z and
3z and must be retained. Returning along a different parallel edge is
also retained. Banning a repeated undirected edge ID would be incorrect.

An immediate reverse pair has total displacement zero and may be deleted
without changing either endpoint. Repeating this deletion leaves a walk
already in the enumerated range. Thus the restriction loses no endpoint
reachable within three steps.

### 3. Exact linear-form equality

For each walk w define c(w) in F43^14 by its signed traversal counts.
Its lifted displacement for an assignment z is exactly c(w) dot z.
Distinct words may have identical c(w), because the voltage group is
abelian. The program deduplicates the vectors, not only the words or their
base endpoints. Coefficients are explicitly reduced modulo 43.

This is the full equality test for these linear forms on unrestricted
F43 assignments. Legal assignments can cause additional value collisions;
the capacity count does not assume those collisions absent.

### 4. Gauge normalization and why it does not overmerge

Choose any three nonloop edges forming a spanning tree T. Relabel each
fiber by x' = x+p_i. For an oriented edge i to j its voltage becomes
z'_e = z_e+p_j-p_i. The potentials p_i can successively set all three
tree voltages to zero. Loop voltages do not change. Parallel differences,
loop nonzeroness, and unequal-up-to-sign loop conditions are preserved.

Let B be the oriented incidence matrix. If two walks have the same
ordered endpoints, their coefficient difference c satisfies Bc=0. If
their restrictions to the eleven non-tree coordinates are equal, c is
supported on T. The incidence columns of a tree are linearly independent
over F43, hence c=0. Conversely, identical full vectors have identical
restrictions. Thus, for each fixed endpoint slot, raw-form equality is
equivalent to equality after deleting the tree coordinates.

Loops have zero incidence columns, but none is in T; their variables are
not deleted. The program checks equality of raw and gauged cardinalities
in all 91*16=1456 slots. No coefficient vectors from different endpoint
slots are merged.

### 5. Necessary capacity and exact coverage conditions

At a fixed legal voltage assignment z, put

    E_ij(z) = {c dot z : c in F_ij} subset F43.

Every vertex in orbit i has distance at most three to every vertex in
orbit j exactly when E_ij(z)=F43. Translation of all fiber coordinates
is an automorphism, so these sixteen conditions are equivalent to
diameter at most three for the lift. In particular, |F_ij|>=43 is
necessary for every slot. The condition is not sufficient.

An equivalent concrete set formula is useful for implementation. Let
V_ij be the set of voltages on darts i to j; set V_ji=-V_ij, and
V_ii={+z,-z : loops at i}. With union as addition and Minkowski sum as
multiplication, the exact short-route matrix is

    E = I union V union V^2 union V^3,

where I_ii={0} and I_ij is empty for i!=j. These are set operations, not
ordinary matrix counts. This formula may include immediate reversals;
they add no values beyond the reduced-walk sets above. Reversal also
gives E_ji=-E_ij and |F_ji|=|F_ij|; the code checks all sixteen slots.

## Remarks and Interpretation

### Results and ranking

52 bases pass: 4 without loops and 48 with loops. Ranking is by larger
minimum capacity, then larger total of the sixteen capacities, then
canonical key. This is only a reproducible capacity ranking and is not
a success-probability estimate.

The old balanced 322 base is still the unique highest-ranked base, with
minimum capacity 68. The best loop bases have minimum capacity 61.
Consequently this calculation gives a new structural input but no
evidence that loop bases have a larger symbolic coverage margin.

### Concrete change from 322

Use the original 322 labeling with cross multiplicities
(3,2,2,2,2,3) and no loops. Its capacity matrix is

    83 68 74 74
    68 83 74 74
    74 74 83 68
    74 74 68 83.

The top loop base, ID 21, has l=(0,0,1,1) and cross multiplicities
(3,2,2,2,2,1). It replaces two of the three 2--3 matchings by one loop
at vertex 2 and one at vertex 3. Every degree remains seven. Its matrix is

    79 68 74 74
    68 79 74 74
    74 74 61 85
    74 74 85 61.

The 2-to-3 capacity rises from 68 to 85, whereas the self-orbit
capacities fall from 83 to 79 or 61. Its first bottlenecks are therefore
the two loop-bearing self-orbits, not the single remaining 2--3 matching.

If the two loop voltages are a,b and the 2--3 edge voltage is c, routes
using only those two base vertices already include

    {c+m*a+n*b : |m|+|n|<=2}

in the 2-to-3 slot. These are thirteen distinct symbolic forms, although
their evaluated field values may collide. In the 2-to-2 slot, both
+/-a (one step) and +/-b (three steps via the other orbit) occur; this
uses the abelian identity c+/-b-c=+/-b. The exact requirements remain
E_ij=F43 simultaneously, with all simplicity constraints imposed.

The other minimum-61 loop base, ID 67, has a loop at every vertex and
cross multiplicities (1,1,3,3,1,1). Its self capacities are all 61;
cross capacities are 68 or 77. It has a different distribution of loop
variables and is not implied feasible by having the same minimum.

## Boundaries and Non-Claims

- This class covers simple seven-regular graphs admitting a specified
  semiregular C43 action with four vertex orbits. Because the odd-order
  group has no edge reversal of order two, internal edge orbits are
  represented by loops and every edge orbit has size 43.
- It does not cover arbitrary 172-vertex graphs or arbitrary symmetries.
- Capacity failure excludes the corresponding base for this C43 lift
  and D3 target. Capacity passage supplies no graph and no new lower bound.
- No actual voltage tuple, lifted adjacency, or BFS was evaluated.
- Old base directories, reports, wiki, and HTML were not changed.

## Open Risks

There is no unresolved step in the stated enumeration or capacity bound.
The substantive open problem is simultaneous evaluation onto all 43
values in every slot under the legal-voltage constraints. This computation
does not resolve that problem for any of the 52 surviving bases.

The local formula-derivation skill was read and used to separate exact
identities from the candidate interpretation. The proof-checker skill was
also read; this bounded derivation is not represented as a completed
external proof audit or formal proof. A parallel paper check confirmed
the tree-incidence argument and loop legality; no additional computation
was delegated.
