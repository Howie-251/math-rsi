# T15 / T44_5 analytic notes — DRAFT

Date: 2026-11-01. ARIS proof-writer working package. This file records proved
partial statements and exact limitations of particular transfers. It does not
change any project-wide theorem status. Independent proof-checker review of
this new package has not been performed.

## Claim and status

The original targets are unchanged:

* **T15:** For every matching $F$ of $K(Q_5)$ with one even and five odd
  holes, and every prescribed pair $x,y$ of odd holes, there is a cycle
  on $V(Q_5)\setminus\{x,y\}$ containing $F$, with only short new edges.
* **T44_5:** The same conclusion holds for four holes of one parity,
  avoiding any prescribed pair of those holes.

For the partial theorem proved below, the proof-writer status is
**PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION**: assume that at least one of
the specified good coordinate cuts has a positive crossing count. The
cell-parity test below is a matching-independent sufficient condition for
this extra assumption. This classification refers to this proof package,
not to the ultimate truth or status of either original target.

## Assumptions and notation

All original required edges may be arbitrary complete-graph edges. A
crossing required edge may cross several coordinates and need not be short.
A short edge is an edge of the cube. A hole is a vertex not covered by $F$.

In a coordinate cut $Q_5=A\cup B$, put $F_A,F_B$ for the internal required
matchings and $C$ for the crossing required matching. Let $c=|C|$, with
endpoint sets $X_A,X_B$. Global parity is used on both faces. Reversing all
parity labels on a face has no effect on any cited parity-count condition.

Imported inputs are the audited Q4 GQ4-avoid/GQ4-cycle consequences in
`Q4_GENERAL_AUGMENTATION.md`, Q4 T44 in
`Q4_TWO_AVOIDED_TRANSFER.md`, and Fink's arbitrary-perfect-matching
extension theorem on Q4. The Q4 optional-edge bounds O15 and L15 are used
only for the optional zero-crossing criterion, and are documented in
`A6_CLOSURE_DRAFT.md` and its dependencies.

## Strategy and dependency map

1. Close two forms of positive-crossing cut by a one-face cycle, deletion
   of artificial port pairs, compression of the other face, and expansion.
2. Force one such cut to have positive crossing count by parity inside
   cells of a multiple-coordinate partition.
3. Enumerate the normalized hole geometries to quantify this partial
   coverage; the enumeration does not range over required matchings.
4. Isolate the exact missing extension statements in two tempting but
   invalid shortcuts.

## 1. Positive-crossing split lemma

Suppose $x\in A$, $y\in B$, the holes in each face have majority excess
two, and each prescribed avoided hole belongs to that face's majority
class. If $c>0$ is even, the desired 30-cycle exists.

**Proof.** Pair $X_A$ arbitrarily into an artificial matching $D$.
The holes of $F_A\cup D$ are precisely the original holes of $A$.
GQ4-avoid gives a cycle on $A\setminus\{x\}$ containing $F_A\cup D$.
Since $D$ is nonempty, deleting $D$ produces a path forest, each of whose
endpoints is a distinct member of $X_A$. Every component is nontrivial:
two deleted matching edges cannot be consecutive around a cycle, and a
single deleted edge leaves the rest of the cycle as a path.

Attach the original crossing edge at every port. The resulting paths
have endpoint set $X_B$, and pairwise disjoint interiors partitioning
$A\setminus\{x\}$. Compress these paths to a matching $R$ on $X_B$.
The matching $F_B\cup R$ has exactly the original B holes, so GQ4-avoid
gives a cycle on $B\setminus\{y\}$ containing it. Expanding every edge
of $R$ gives a single cycle on $Q_5\setminus\{x,y\}$. All original
crossing and internal required edges have been restored; all other
surviving edges are short. The artificial edges of $D$ were deleted and
those of $R$ were expanded. $\square$

In both applications below, each face has an even number of original
holes, so $2|F_A|+c=16-|H_A|$ implies even $c$. Thus positive $c$ is
automatically at least two.

## 2. Positive-crossing same-face lemma

Suppose both prescribed avoided holes lie in $A$, the original A holes
are exactly four vertices of one parity, the original B holes are
balanced, and $c>0$. Then the desired 30-cycle exists.

**Proof.** The same port pairing $D$ fills every A crossing port. Apply
Q4 T44 to $F_A\cup D$, avoiding both prescribed A holes. Delete $D$,
attach $C$, and compress the resulting paths to $R$ on $X_B$.
The matching $F_B\cup R$ has balanced original holes. Apply GQ4-cycle
and expand $R$. This restores all original edges and all vertices except
the two prescribed avoided holes. $\square$

For T44_5 the B face in this lemma has no original holes, so Fink also
suffices. For T15 it has one hole of each parity.

## 3. Explicit geometric description of the good cuts

For T15, short-edge augmentation reduces to the case where the minority
hole, translated to $0$, is nonadjacent to all three included majority
holes $s,t,u$. This preprocessing uses T44_5 and is therefore only a
conditional reduction until that target is supplied. The direct lemmas
above themselves do not require the preprocessing or T44_5 in dimension
five.

Let $x,y$ be the prescribed avoided holes, and let $r_j$ be the number of
the five odd holes whose coordinate $j$ is one. With the minority at $0$:

* A split good cut is exactly a coordinate with $r_j=2$ and
  $x_j\ne y_j$. The zero face contains one even and three odd original
  holes; the one face contains two odd original holes.
* A same-face good cut is a coordinate with $r_j=4$ and $x_j=y_j=1$.
  Its one face contains four odd original holes; its zero face has one
  original hole of each parity.

For T44_5 translate a prescribed avoided hole to $0$ and write the other
as $y$, with included holes $s,t$. All four holes are then even. A split
good cut is exactly

$$j\in\operatorname{supp}(y)\cap\operatorname{supp}(s\mathbin\oplus t).$$

A same-face good cut is exactly a coordinate at which all four holes
are zero. These criteria follow by counting the original holes on each
side, not by assumptions about $F$.

## 4. Cell-parity theorem

Let $I$ be any collection of good coordinate cuts of either type. Fixing
the coordinates in $I$ partitions $Q_5$ into cells, each of size
$2^{5-|I|}$. If any cell contains an odd number of vertices covered by
$F$, then at least one cut in $I$ has positive crossing count. Therefore
the corresponding target conclusion holds for this matching.

**Proof.** If every cut in $I$ had crossing count zero, every edge of
$F$ would preserve every coordinate in $I$. Thus every required edge
would lie in a single cell. Each cell's covered vertices would then be
partitioned into pairs by its internal matching, giving an even count.
This contradicts the stated odd cell. Sections 1 or 2 now apply to a
positive-crossing cut. $\square$

This proof applies without change to long edges: it is the absence of
edges crossing the selected cuts that confines them to cells.

## 5. Independent geometry census

`t15_analytic_geometry.py` regenerates the following numbers and writes
`t15_analytic_geometry.json`. It uses integer bits, all 120 coordinate
permutations, and direct cell-hole counts. No Hamilton search is involved.

For T15, normalize the minority hole to $0$. There are eleven odd
nonneighbors of $0$, so choose the three included holes in $\binom{11}{3}$
ways and the avoided pair from the remaining thirteen odd vertices in
$\binom{13}{2}$ ways. This gives $12870$ configurations.

| Split good cut exists | Same-face good cut exists | Configurations |
|---|---|---:|
| no | no | 3240 |
| no | yes | 2600 |
| yes | no | 4390 |
| yes | yes | 2640 |

The $3240$ configurations with neither kind of cut form 54 coordinate
permutation orbits. Applying Section 4 to all available good cuts forces
a positive good cut in $2700$ of the $12870$ configurations. Thus all
required matchings in these $2700$ normalized configurations satisfy
T15, using only the listed Q4 imports. This is a geometry-level count,
not a matching count or an assertion that the other configurations fail.

For T44_5 normalize the second avoided hole to $3$ or $15$, according as
the avoided pair has distance two or four. There are $\binom{14}{2}=91$
included pairs in each normalized case.

* For $y=15$, all 91 pairs admit a split good cut. Section 4 forces a
  positive good cut for 55 pairs.
* For $y=3$, 73 pairs admit a split good cut. The other 18 pairs form
  exactly three orbits, of six pairs each, represented by
  $\{s,t\}=\{5,9\},\{5,29\},\{12,20\}$. The first of these has a
  same-face good cut; the last two have neither kind. Section 4 forces
  a positive good cut for 16 of all 91 pairs.

The three-orbit assertion also follows directly: failure of every split
cut means $s,t$ agree on coordinates zero and one. On the remaining
three coordinates, they differ at two positions. When their first two
bits are $00$ or $11$, their remaining patterns are two distinct
nonzero even patterns; these give the $\{12,20\}$ orbit. When their
first two bits are $01$ or $10$, the odd remaining patterns form either
a pair of unit vectors or a unit vector and $111$, giving respectively
$\{5,9\}$ and $\{5,29\}$. Swapping the avoided vertices by translation
through $3$ identifies the two choices of first-two-bit pattern in each
case. Coordinate permutations of the last three bits finish the stated
classification.

## 6. A proved but limited zero-crossing criterion

In the split lemma with $c=0$, let $S_A,S_B$ be the unions of short edges
outside the internal required matchings occurring in valid face cycles
avoiding their prescribed hole. Project both sets into the same Q4.
If $S_A\cap S_B\ne\varnothing$, choose witnessing face cycles, delete
the common projected edge in both, and add the two corresponding short
crossing edges. This gives the desired 30-cycle and preserves $F$.

For the T15 split type, O15/L15 imply $|S_A|,|S_B|\ge15$. For the T44_5
split type, L15 gives the same bounds. If at least three of Q4's 32
short edges are excluded from both sets, then

$$|S_A|+|S_B|\ge30>32-3,$$

so the required intersection exists. Common excluded edges include
projected short original edges present in both internal matchings. If
the two forbidden face vertices project to adjacent Q4 vertices, the
edge joining those projections is another common excluded edge. Count
only distinct excluded edges.

The bounds $15+15$ alone do not force intersection among 32 edges.
The main investigator's richer-spectrum computations may remove this
zero-crossing limitation once their separate certificates and checker
are supplied; those new certificate claims are not used in this file.

## 7. Genuine obstructions to shortcuts

### Q4 T15 cannot simply be imported

`q4_six_two_avoided_results.json` contains failures for Q4 with one
minority and five majority holes, avoiding two prescribed majority
holes. Thus a cut placing all six T15 holes in one face cannot be
closed by asserting a dimension-four version of the full target.

### Opposite-parity two-fault perfect-matching extension is false

A tempting one-bridge transfer on a cut with one majority hole in one
face and three in the other can require a circle extending an arbitrary
perfect matching of $Q_4\setminus\{a,b\}$, with $a,b$ of opposite
parity. That general extension assertion is false. One explicit example,
with omitted vertices $0,1$, is

$$F=\{23,45,67,89,(10)(13),(11)(14),(12)(15)\},$$

where $ab$ denotes the unordered pair $\{a,b\}$, and parentheses
separate vertices with two-digit labels. More unambiguously, its edge
list is

$$\{\{2,3\},\{4,5\},\{6,7\},\{8,9\},\{10,13\},\{11,14\},\{12,15\}\}.$$

Every vertex is already covered by $F$, so any extending circle would
need a disjoint short perfect matching as its added edges. Independent
bipartite recursion gives exactly four such short perfect matchings;
their unions with $F$ have component-size pairs $(4,10),(8,6),(10,4),
$(10,4)$, respectively. None is connected.

The existing checker `verify_q4_opposite_avoided_obstructions.py` verifies
this example independently by enumerating short perfect completions, and
its JSON reports four completions with two components each. This is an
obstruction to that auxiliary universal lemma, not a T15 or T44_5
counterexample. A specialized transfer would have to exploit additional
structure of its induced matching rather than invoke the false lemma.

## Open risks and exact remaining work for this route

1. Review the new positive-crossing and cell-parity package independently.
2. Audit richer spectrum intersection certificates before importing them
   into the zero-crossing split step.
3. Handle good-cut-free geometries and same-face zero-crossing inputs by
   additional transfers, or by other constructions.
4. Never identify absence of one of these sufficient cuts with failure
   of the original cycle target.

