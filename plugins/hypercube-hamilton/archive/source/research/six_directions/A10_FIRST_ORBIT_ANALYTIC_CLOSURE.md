# A10 first residual orbit: closure from an odd closed intersection

Date: 2026-11-01. ARIS proof-writer package; fresh independent review pending.

## Claim

Let $F$ be any matching of the complete graph on $V(Q_5)=\{0,\ldots,31\}$
whose hole set is exactly

$$H=\{0,3,5,6,8,15,16,23,25,26\}.$$

There is a simple cycle on exactly $V(Q_5)\setminus\{0\}$ containing
every edge of $F$, with all edges outside $F$ short. The same statement
holds for every coordinate permutation of this marked geometry, giving
30 normalized hole geometries.

The original majority holes are the six even vertices
$\{0,3,5,6,15,23\}$, the minority holes are the four odd vertices
$\{8,16,25,26\}$, and the specified forbidden majority hole is $0$.
Required matching edges are arbitrary, including long edges and edges
whose endpoints have the same parity.

## Status

**PROVABLE AS STATED**, relative to the certified Q4 inputs below.
This is one specified ten-hole Q5 orbit; it is not the full A10 theorem
and does not by itself close a Q6 P6 layer. This new proof is awaiting
independent proof-checker review.

## Assumptions, notation, and dependency map

Write $Z=\{3,5,6,15,23\}$ and $W=\{8,16,25,26\}$. The proof assumes
only the exact hole set and that $F$ is a matching; there is no additional
condition on its edges. For this hole geometry, no $z\in Z$ is short-adjacent
to any $w\in W$, as the accompanying checker verifies directly.

For a cut bit $b$, let $A=\{x:x\mathbin\&b=0\}$ and $B=Q_5\setminus A$.
Let $F_A,F_B$ be the internal matchings, $C$ the original crossing
matching, $c=|C|$, and $X_A,X_B$ its endpoint sets. The short mirror
of $t\in A$ is $\bar t=t\oplus b$. We use global parity on both faces.

The only extension theorems imported are:

1. GQ4-avoid from `Q4_GENERAL_AUGMENTATION.md`: a matching with hole
   excess two has a face cycle avoiding any specified majority hole.
2. The exact Q4 T15 classification from `Q4_T15_CLASSIFICATION.md`:
   with one singleton-parity hole $a$ and five opposite-parity holes,
   avoiding two of the latter is possible unless both avoided holes
   are neighbors of $a$ and the edge between the other two neighbors
   belongs to the matching.

Both apply to arbitrary complete-graph matching edges and introduce
only short edges. We reproduce the bridge argument needed to use them.
No Q5 A8 or full A10 theorem is a dependency. The geometry checker is
`A10_first_orbit_geometry_check.py`.

## Proof strategy

At each of two cuts, four candidate bridge mirrors form the four short
neighbors of the singleton hole in $B$. Selecting any two yields a T15
completion problem. If every selection fails, the covered vertices
outside this four-set form a closed matching set. The two cuts give
closed eight-sets with a five-vertex intersection, impossible for a
matching covering every vertex of that intersection.

## Proof

### Step 1. A sufficient rule for any of the selected bridge pairs

Suppose a cut $A,B$ has five majority holes and one minority hole in
$A$, and one majority hole $a$ and three minority holes in $B$.
Let $M$ be the four short neighbors of $a$ within $B$, all of which
are covered in the original matching and are mirrors of the four
majority holes of $A$ other than $0$. Choose any pair $Y=\{w,z\}\subset M$
and use their mirror holes $t,s$ in $A$ as bridges. Put
$\{p,q\}=M\setminus Y$.

Removing $t,s$ from the original $A$ holes leaves three majority holes
and one minority hole, with majority excess two and $0$ still free.
The crossing count $c$ is even because

$$2|F_A|+c=16-6=10.$$

Let $T=X_A\cup\{t,s\}$ and $d=|T|/2=(c+2)/2$. Build the graph

$$G=F_B\cup C\cup\{tw,sz\}.$$

Its $A$ vertices are precisely $T$, each of degree one. Only $w,z$
have degree two in $B$; each is incident to a bridge leading to $T$.
Thus $G$ is a path forest. A closed component would have to pass
through a degree-two bridge vertex and then its degree-one neighbor,
which cannot occur in a cycle.

Let $P$ be the matching of endpoint pairs in $T$ given by components
with both endpoints in $T$. Every other component meeting $T$ has a
unique terminal in $B$ and a unique root in $T$. There are
$2d-2|P|$ such roots. Suppose $pq\notin F_B$ and there is a terminal
outside $\{p,q\}$. If both $p,q$ are terminals rooted in $T$, add the
edge between their roots to $P$, obtaining $J$; otherwise put $J=P$.
This is a matching on $T$. With $e=|J|-|P|\in\{0,1\}$, the even
number $2d-2|P|$ is strictly greater than $2e$. Hence $d>|J|$.

Complete $J$ to a perfect matching $D$ on $T$. The matching
$F_A\cup D$ has the original $A$ holes except $t,s$, so GQ4-avoid
gives a cycle $K$ on $A\setminus\{0\}$. Remove $D$. Contracting
each remaining path gives another matching $Q$ on $T$, with the
multigraph $Q\cup D$ one cycle. Because $J$ is a proper subset of
$D$, the subgraph $Q\cup J$ is acyclic.

Attach $G$ to the paths of $K-D$. A closed component would induce a
cycle in $Q\cup P\subseteq Q\cup J$, which is impossible. Compress
the resulting paths to a matching $L$ on $B$. Its holes are exactly
the original four $B$ holes together with $w,z$. Its suppressed
interiors contain every vertex of $A\setminus\{0\}$ and both $w,z$.

The obstruction edge $pq$ is absent from $L$. If an endpoint belongs
to a component of $G$ not meeting $T$, it keeps its original partner
from $F_B$, and $pq\notin F_B$ excludes the edge. Every such $B$--$B$
component is a single original edge: a longer path would have to
traverse a bridge vertex and end in $T$. If both endpoints are
rooted terminals, a compressed $pq$ edge would give a path between
their roots in $Q\cup P$. Adding the prescribed extra edge of $J$
would produce a cycle in $Q\cup J$, again impossible.

Now $L$ has singleton majority hole $a$ and five minority holes,
including the prescribed avoided pair $w,z$. Both are neighbors of
$a$, and the two remaining neighbors are $p,q$. T15 applies because
$pq\notin L$. It gives a cycle on $B\setminus\{w,z\}$ containing $L$.
Expand all compressed paths to obtain a single cycle on
$Q_5\setminus\{0\}$. All original required edges survive, and all
other edges are short. Each suppressed vertex is restored exactly once.

We have proved a sufficient rule that holds for every crossing count
and every mixture of port and internal bridge vertices.

### Step 2. Consequences of failure of all six bridge pairs

Assume, for contradiction, that no required global cycle exists.
For a pair $Y\subset M$ whose complementary edge $pq$ is not in
$F_B$, Step 1 says there is no terminal outside $\{p,q\}$. It follows
that

$$X_B\subseteq M,\qquad
F_B(y)\in M\text{ whenever }y\in Y\text{ is internally covered in }B.\tag{1}$$

Indeed, a crossing port outside $M$ is a nonbridge terminal outside
$\{p,q\}$. An internally covered selected bridge with partner outside
$M$ has that partner as such a terminal. These account for all possible
paths rooted in $T$ leading outside the allowed terminal pair.

There are six bridge pairs, one for each two-subset of the four-set
$M$. The associated fixed-obstruction edge is its complementary pair.
A matching can contain at most two such complementary edges, and if
two occur they are disjoint. Thus at least four bridge choices are
nonfixed, so at least one choice gives the port condition in (1).

Crucially, the selected nonfixed bridge pairs cover every candidate.
To prove this, fix $x\in M$. There are three bridge pairs containing
$x$. Their three complementary edges are precisely the three edges
on the other three vertices $M\setminus\{x\}$. A matching on three
vertices contains at most one edge. Therefore at least two of these
three bridge pairs are nonfixed, and in particular $x$ is selected
in a nonfixed pair. Applying (1) to a nonfixed pair containing each
$x$ shows that every internally covered vertex of $M$ has its partner
in $M$. This explicitly allows two simultaneous disjoint fixed
obstruction edges; it does not assume there is at most one.

Consequently every covered vertex of $B\setminus M$ is matched within
$B\setminus M$. It cannot be a port, by $X_B\subseteq M$, and cannot
be matched to $M$, whose internally matched vertices all have partners
in $M$. Thus

$$C_B=(B\setminus M)\setminus H$$

is closed under the original matching $F$.

### Step 3. Verify and apply the cut at bit 8

For $b=8$, the holes in $A$ are the majority holes $0,3,5,6,23$ and
the minority hole $16$. The holes in $B$ are the singleton majority
hole $a=15$ and the three minority holes $8,25,26$.

The four available majority holes in $A$ have mirrors

$$M_8=\{11,13,14,31\}.$$

They are all covered in the original matching, and they are exactly
the four short neighbors of $15$ within $B$. Thus every hypothesis
of Steps 1--2 holds. The absence of a global cycle forces the covered
eight-set

$$C_8=\{9,10,12,24,27,28,29,30\}$$

to be closed under $F$.

### Step 4. Verify and apply the cut at bit 16

For $b=16$, the holes in $A$ are the majority holes $0,3,5,6,15$ and
the minority hole $8$. The holes in $B$ are the singleton majority
hole $a=23$ and the three minority holes $16,25,26$.

The four available majority holes in $A$ have mirrors

$$M_{16}=\{19,21,22,31\}.$$

They are covered and exactly the four short neighbors of $23$ within
$B$. Steps 1--2 therefore force the covered eight-set

$$C_{16}=\{17,18,20,24,27,28,29,30\}$$

to be closed under $F$.

### Step 5. The closed intersection has impossible odd size

The intersection of two closed matching sets is closed. For any
vertex in the intersection, its unique original matching partner
must belong to each of the two sets. Here

$$C_8\cap C_{16}=\{24,27,28,29,30\}.$$

These are five originally covered vertices, all distinct from every
hole. A closed set of covered vertices is partitioned into two-element
matching edges and must have even cardinality. Its cardinality here
is five. This contradiction refutes the assumed absence of a global
cycle and proves the claimed extension for every matching with holes $H$.

### Step 6. The 30 marked geometries

Every coordinate permutation fixes $0$ and preserves parity, short
edges, arbitrary matching edges, and the asserted cycle condition.
Generating all 120 coordinate permutations gives exactly 30 distinct
marked pairs $(\pi Z,\pi W)$. Transfer the cycle back by the inverse
permutation. This proves the same conclusion throughout this orbit.

## Verification

Run `D:\anaconda\python.exe A10_first_orbit_geometry_check.py` in this
directory. The checker verifies the exact hole counts at both cuts,
the four candidates and their short-neighbor identities, all six
complementary T15 obstruction edges per cut, both closed-set identities,
their odd covered intersection, and the 30-element marked orbit.

It also checks the nonfixed-choice covering property against all ten
possible restrictions of a matching to a four-element candidate set:
the empty matching, six single-edge matchings, and three two-edge
matchings. It enumerates no full Q5 matching instances and performs
no Hamilton-cycle search. Output is `A10_first_orbit_geometry_check.json`.

## Corrections or missing assumptions

None for the stated marked orbit. The two-fixed-obstruction case was
explicitly handled in Step 2. The proof uses no assertion that all
four-candidate T15 choices are simultaneously nonfixed.

## Open risks and remaining scope

Fresh independent semantic review of this new proof is pending.
The checker verifies the finite geometry and choice facts; the global
matching argument is the analytic proof above. This package proves
only the specified 30 normalized ten-hole geometries, and it changes
neither earlier frozen A8 files nor the main progress ledger.
