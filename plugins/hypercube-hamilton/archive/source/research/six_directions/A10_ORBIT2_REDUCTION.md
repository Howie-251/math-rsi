# A10 orbit 2: strict reduction to 2,366,577 canonical matching inputs

Date: 2026-11-01. ARIS proof-writer package; independent review pending.

## Original claim

Let $F$ be any matching of the complete graph on $V(Q_5)=\{0,\ldots,31\}$
with holes

$$H=\{0,3,5,6,8,15,23,25,26,28\}.$$

There is a simple cycle on $Q_5\setminus\{0\}$ containing $F$, with
all edges outside $F$ short. The claim is unchanged under coordinate
permutations of the marked geometry, which has 20 distinct images.
Required edges may be arbitrary long edges, including same-parity edges.

## Status

**PROVABLE AS STATED, as a complete candidate proof relative to the
explicit positive cycle files below; fresh acceptance remains pending.**
The analytic reduction and finite canonical input domain are complete,
and positive 31-cycle records have been produced for every one of the
2,366,577 inputs. Independent verification of all those records and
fresh semantic review of the proof are pending at this writing.
Producer success by itself is not an independent acceptance, and no
sample success is used as a universal assertion.

The analytic partial theorem is: the claim holds unless
$C=\{16,17,18,20,24,27,29,30\}$ is closed under $F$. In that exceptional
case the claim reduces exactly to the finite canonical family specified
below. No extra assumption is silently imposed on the original claim.

## Assumptions, notation, and dependency map

The numerical even holes are the majority class
$\{0,3,5,6,15,23\}$, and the odd holes are $W=\{8,25,26,28\}$.
Put $Z=\{3,5,6,15,23\}$. For a cut bit $b$, let $A$ be its zero
face and $B$ its one face. Write $F_A,F_B$ for internal matching
edges, $C_{\mathrm{cross}}$ for crossing edges, $c$ for their number,
and $X_A,X_B$ for their endpoint sets. A mirror across the cut is
$\bar t=t\oplus b$.

The imported results are GQ4-avoid from `Q4_GENERAL_AUGMENTATION.md`
and the exact Q4 T15 classification from `Q4_T15_CLASSIFICATION.md`.
The four-candidate bridge construction proved in Steps 1--2 of
`A10_FIRST_ORBIT_ANALYTIC_CLOSURE.md` was independently accepted in
`A10_FIRST_ORBIT_REVIEW.md`. We state and justify its use below; no
full A10 or other unresolved orbit is a dependency.

The new finite domain generator is `A10_ORBIT2_canonical_generator.cpp`.
The separate geometry and Burnside checker is
`A10_ORBIT2_geometry_counts_check.py`. Neither performs a cycle search.

## Proof strategy and analytic reduction

### Step 1. The cut at bit 16 has four candidate T15 bridges

At $b=16$, the original holes in $A$ are the five majority holes
$0,3,5,6,15$ and the minority hole $8$. The original holes in $B$
are the singleton majority hole $a=23$ and the three minority holes
$25,26,28$. The mirrors of the four available majority holes in $A$
are

$$M=\{19,21,22,31\}.$$

They are all originally covered and are exactly the four short
neighbors of $23$ within $B$. Every pair $Y=\{w,z\}\subset M$ may
be selected for bridges from its original hole mirrors $t,s$ in $A$.
After consuming $t,s$, the target-face holes are three majority and
one minority, including the forbidden hole $0$, so GQ4-avoid applies
to every artificial port pairing. Compression on $B$ leaves its
original singleton hole $23$, its original three minority holes,
and the two selected minority bridge holes. This is exactly T15,
with the selected pair avoided. Its only possible obstruction is
the edge $pq$ on the complementary pair $M\setminus Y$.

### Step 2. A nonfixed failed pair restricts the original matching

For clarity, the sufficient bridge rule used here has no crossing
threshold or hidden port hypothesis. Put $T=X_A\cup\{t,s\}$,
$d=|T|/2$, and

$$G=F_B\cup C_{\mathrm{cross}}\cup\{tw,sz\}.$$

The vertices of $T$ have degree one; only $w,z$ have degree two in
$B$, and each leads through a bridge to $T$. Thus $G$ is a path
forest. Its $T$--$T$ components define an endpoint matching $P$.
The other components meeting $T$ have distinct roots in $T$ and
terminals in $B$.

Suppose $pq\notin F_B$ and some terminal lies outside $\{p,q\}$.
If $p,q$ are both rooted terminals, add the edge between their roots
to $P$, otherwise add nothing, obtaining a matching $J$. The number
of terminal roots is $2d-2|P|$, which is even and exceeds the number
zero or two accounted for by the potential obstruction pair. Hence
$|J|<d$. Complete $J$ to a perfect matching $D$ on $T$, and use
GQ4-avoid to get an $A\setminus\{0\}$ cycle containing $F_A\cup D$.
After deleting $D$, contract its remaining paths to the matching $Q$
on $T$. The multigraph $Q\cup D$ is one cycle, while $Q\cup J$ is
acyclic because $J$ is a proper subset of $D$.

Attaching $G$ cannot close a component, because that would give a
cycle in $Q\cup P$. Its compressed matching $L$ on $B$ has holes
exactly the original $B$ holes and $w,z$. It does not contain $pq$:
if an endpoint is in a component not meeting $T$, its unchanged
original partner excludes $pq$; if both are rooted terminals, a
compressed $pq$ path together with the extra prescribed edge of
$J$ would be a cycle in $Q\cup J$. T15 gives a $B\setminus Y$ cycle
containing $L$, and expansion gives the required global cycle.
Every suppressed vertex is restored once; all original edges survive,
and every other edge is short.

Consequently, if the global cycle does not exist, every selected
pair with nonfixed obstruction $pq\notin F_B$ satisfies

$$X_B\subseteq M,\qquad
F_B(y)\in M\text{ for each internally matched selected }y\in Y.\tag{1}$$

A port outside $M$ or an internal bridge partner outside $M$ would
be exactly the forbidden terminal in the sufficient rule. This
justification handles every port/internal mixture.

### Step 3. All six choices force the closed eight-set

Of the six complementary-pair obstruction edges, at most two can
belong to the original matching. For any $x\in M$, the three bridge
pairs containing $x$ have complementary obstruction edges lying
entirely in the other three vertices of $M$. A matching on those
three vertices contains at most one edge. Hence at least two nonfixed
bridge choices contain $x$.

If no global cycle exists, apply (1) to these nonfixed choices.
There is at least one such choice, giving $X_B\subseteq M$; and
every vertex of $M$ is selected in one, so every internal matching
partner of a vertex of $M$ lies in $M$. All other covered vertices
of $B$ must therefore be paired among themselves. They are exactly

$$C=\{16,17,18,20,24,27,29,30\}.$$

Thus $C$ is closed under $F$. This proves the partial theorem.

### Step 4. Exact unsymmetrized exceptional family

Write

$$D=V(Q_5)\setminus(H\cup C)
=\{1,2,4,7,9,10,11,12,13,14,19,21,22,31\}.$$

Every exceptional matching is uniquely the disjoint union of a perfect
matching on $C$ and one on $D$. Conversely every such union is an
actual matching with the exact original hole set and with $C$ closed.
There are $7!!=105$ matchings on $C$, $13!!=135135$ on $D$, and hence

$$105\cdot135135=14,189,175$$

actual matching inputs in this exceptional family. The reduction
does not claim they are all counterexamples or all successful; it
identifies exactly the family left by the analytic sufficient rule.

### Step 5. Symmetry and complete canonical generation

Let $G_0$ be the six coordinate permutations of the three low bits,
fixing the bits of values 8 and 16. Each fixes the marked hole geometry,
$C$, and $D$, and preserves arbitrary required edges and short edges.
These are in fact the full six-element coordinate stabilizer of the
marked geometry; the checker regenerates all 120 coordinate permutations
to verify this and the marked orbit size 20.

Represent a matching by its list of unordered endpoint pairs, with
smaller endpoint first and the pairs sorted lexicographically. The
generator enumerates all 105 matchings on $C$. Retain the least member
of each $G_0$ orbit, giving 23 representatives. For a retained $F_C$,
let $G_C\subseteq G_0$ be its stabilizer. Enumerate all 135135 matchings
$F_D$ on $D$, retaining exactly those lexicographically least under
$G_C$. Write the actual matching $F_C\cup F_D$ for each retained pair.

This covers every exceptional input: first use $G_0$ to take its
$C$ matching to a retained representative; then use that representative's
stabilizer to take its $D$ matching to a retained representative. It
also has no repeated full orbits: two different canonical $C$ matchings
cannot be related by $G_0$, while two canonical $D$ matchings in the
same $C$ block cannot be related by $G_C$ unless they are identical.
The recursive pairing enumeration itself has no repetitions, since
it always pairs the least unpaired vertex with each possible partner
and recurses on the remainder.

The resulting file contains exactly 2,366,577 orbit representatives.
An independent Burnside count corroborates this number. The identity
fixes $14,189,175$ complete exceptional matchings; each of the three
transpositions fixes $9\cdot375=3375$, and each of the two 3-cycles
fixes $3\cdot27=81$. Therefore

$$\frac{14,189,175+3(3375)+2(81)}6=2,366,577.$$

For each generated pair, the full matching orbit has size
$6/|\operatorname{Stab}_{G_C}(F_D)|$. The generator sums these orbit
sizes to $14,189,175$, providing a further coverage count.

### Step 6. Exact saved input format and remaining certificate obligation

The frozen file is `A10_ORBIT2_canonical_inputs.bin`, with
2,366,577 records of 22 bytes, totaling 52,064,694 bytes. Its SHA-256 is
`f75459b8203101f4001f34855c80cff46a53cb63ccaff6666b87fb90215129c9`.

Each record contains eleven actual original matching edges as pairs
of unsigned bytes: first the four edges of $F_C$, then the seven edges
of $F_D$. Both sublists have lexicographically sorted unordered endpoint
pairs. There are no artificial edges, omitted matching edges, covered
holes, or additional constraints hidden in these records.

The 23 canonical $C$ blocks are ordered lexicographically. Within
each block the $D$ order is the least-unpaired-vertex recursive pairing
order, filtered by the stabilizer test. Per-block counts, stabilizer
sizes, and weighted orbit counts are saved in
`A10_ORBIT2_canonical_counts.json`.

To finish verification of the original theorem it is enough to check
the supplied 31-cycle for each saved record has vertex set $Q_5\setminus\{0\}$,
containing all eleven recorded required edges and having every other
edge short. The covering proof in Step 5 transports such a certificate
to every exceptional matching; Steps 1--3 handle every nonexceptional
matching. All positive records have now been produced in three contiguous
chunks, each with 53 bytes per record: the original 22 input bytes followed
by the 31 cycle vertices.

| input interval, zero-based and half-open | certificate file | positive records | unknown or exhausted |
|---|---|---:|---:|
| $[0,800000)$ | `A10_ORBIT2_chunk_0.bin` | 800000 | 0 |
| $[800000,1600000)$ | `A10_ORBIT2_chunk_800000.bin` | 800000 | 0 |
| $[1600000,2366577)$ | `A10_ORBIT2_chunk_1600000.bin` | 766577 | 0 |

The corresponding `.json` producer summaries report those counts.
The proof requires an independent verifier to check every record,
its alignment to the original input, exact cycle vertices, required
edge containment, and shortness of all new edges. That independent
verification is being run separately. Conditional on those explicit
checks, every canonical exceptional input has a positive certificate,
and Steps 1--5 prove the original orbit claim.

## Why the other ordinary face-circle templates do not finish the proof

At bit 8, $A$ has five majority holes and no minority holes. Consuming
three majority holes would give a valid target-face GQ4-avoid input,
but the other face would have a T17 pattern: one free majority hole
$15$ and seven minority holes, with three prescribed avoided bridge
vertices. All four candidate mirrors are the four neighbors
$\{11,13,14,31\}$ of $15$ in that face. Avoiding any three leaves
the original free vertex $15$ with only one available short neighbor.
Because it has no required edge, a simple cycle would need two distinct
short neighbors there. This is impossible for every matching.

At bits 1, 2, and 4, $A$ has two majority and three minority holes.
Consuming all three minority holes gives two majority holes in $A$,
but creates another T17 pattern in $B$. The original free singleton
holes are respectively $25,26,28$; the avoided bridge triples are
respectively $\{9,27,29\},\{10,27,30\},\{12,29,30\}$. Each triple
removes three of that singleton's four face neighbors. The same degree
obstruction applies. These facts invalidate only those fixed transfer
templates, not the original Q5 claim. T63 must not be applied to these
one-versus-seven hole patterns.

## Verification and open risks

`A10_ORBIT2_geometry_counts_check.py` verifies exact face geometry,
the closed-set identity, the four degree-obstruction templates, all
coordinate stabilizers, the 105 and 135135 matching domains, their
fixed-point counts for Burnside, the 23 canonical $C$ orbits, the
saved binary size and hash, and the stated total counts. Its output
is `A10_ORBIT2_geometry_counts_check.json`.

The generator's canonical coverage argument is Step 5; independent
review should inspect both that argument and its implementation.
The checker verifies geometry and domain counts, not positive cycles.
The original orbit remains open until the whole positive certificate
domain and this reduction have fresh independent acceptance. No
earlier frozen A8/A10 proof or main ledger was edited.
