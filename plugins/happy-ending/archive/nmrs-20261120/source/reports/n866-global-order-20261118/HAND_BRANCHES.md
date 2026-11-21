<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# Hand-checked shared-label branches and exact attainment

2026-11-18. Paper calculation only, written in the assigned directory. No new
[Operational connection details omitted from this publication excerpt.]
review or acceptance is claimed. Earlier sealed evidence is unchanged.

## Input and conventions

The frozen271-row survivor in
`../n866-joint-label-order-20261117/appendix9plus/transport-merge/delivery/nine-holes.json`
has holes

```
1268 1358 1378 1478 1567 2345 2456 2457 3467.
```

All other four-subsets of [8] are occupied. A word w1w2w3w4 has column heights
`(w4-4,w3-3,w2-2,w1-1)`. An actual earlier/later pair u<v has its one common
label in I(v) minus I(u). Blue triples require strictly increasing first label
coordinates, and red triples require strictly increasing second coordinates.
Thus nonincrease of second coordinates forces blue, and nonincrease of first
coordinates forces red. Every displayed inclusion chain has its actual order
fixed by inclusion. Paths below have five vertices, and both colors with the
same first and last vertices give weak8.

Sections 1--3 use only admissible shared labels; Section 4 additionally requires
the ORIGINAL, complete, exact incoming-rank ideal assignment. That additional
condition does not survive arbitrary deletion or compression without proof.

## 1. First shared label: remove its fourth-column choices

Set

```
A=1356 (2,2,1,0)   B=1357 (3,2,1,0)   C=1367 (3,3,1,0)
U=1467 (3,3,2,0)   V=2367 (3,3,1,1)   E=3568 (4,3,3,2)
F=3578 (4,4,3,2)   G=3678 (4,4,4,2)   H=5678 (4,4,4,4).
```

The incomparable U,V have singleton directed differences:
U before V forces label (4,1), whereas V before U forces label (3,2).
These are alternative actual chronologies, not two freely chosen pair labels.

Let P be the actual label of U<E. Its exact domain is
`{(1,4),(3,3),(4,1),(4,2)}`. If P is (4,1) or (4,2), the blue path is

```
A, B, C, U, E.
```

Its four labels are `(1,3),(2,3),(3,2),P`, with nonincreasing second
coordinates. The red path with the same endpoints is

```
A, 2356, 3456, 3567, E.
```

Its labels belong successively to
`{(4,1)}`, `{(3,2),(4,2)}`, `{(1,3),(2,3),(3,3)}`, `{(1,4)}`.
Their first coordinates are nonincreasing, independently of all choices.
All these states are occupied. Therefore any avoiding realization of this
61-state input must have

```
P in {(1,4),(3,3)}.
```

## 2. The P=(1,4) branch

If P=(1,4), the blue path is

```
U, E, F, G, H.
```

Its labels are `(1,4),(2,4),(3,4),(4,3 or 4)`, again with nonincreasing
second coordinates. Put Z=2567=(3,3,3,1). The pair U<Z has exact domain
`{(3,3),(4,1)}`. If its label T is (4,1), the red path is

```
U, Z, 3567, 4567, H,
```

with labels `(4,1),(4,2),(4,3),(s,4)` for s in {1,2,3,4}.
The final difference4567->5678 is the ENTIRE fourth row, not a singleton.
The red path is still forced because its first coordinates4,4,4,s are
nonincreasing. Hence this conditional branch is
excluded, and P=(1,4) requires T=(3,3).

## 3. The P=(3,3), V before U branch

Suppose P=(3,3) and the actual incomparable order is V<U. There is a red path

```
C, V, U, E, F,
```

whose labels are `(4,1),(3,2),(3,3),(2,4)`. Their first coordinates are
nonincreasing. Let Q be the shared label of 1368<2378. Its exact domain is
`{(2,4),(4,1)}`. If Q=(2,4), the blue path with the same endpoints is

```
C, 1368, 2378, 2578, F.
```

Its labels are `(1,4),(2,4),(3,2 or 3),(4,2)`, with nonincreasing second
coordinates. Therefore P=(3,3), V<U requires Q=(4,1).

### Additional U before V branch, independent of P

The parent supplied the following further branch, which is checked here
directly by its state differences. The parallel lead subsequently
confirmed this path calculation by hand; no external acceptance is
claimed. If the actual order is U=1467<V=2367, there is a forced red5

```
U, V, 2467, 2567, 2678.
```

Its labels are `(4,1),(3,2),(3,3),(s,4)` with s in {1,2,3}; their first
coordinates are nonincreasing. All states on this path are occupied.
The shared pair1468<1578 has exact difference

```
L(1468,1578) in {(2,4),(3,3)}.
```

If its actual label is (2,4), the blue5 with the same endpoints is

```
U, 1468, 1578, 1678, 2678,
```

whose labels are `(1,4),(2,4),(3,4),(4,1)`. Their second coordinates are
nonincreasing. Thus every avoiding realization with U<V must have
L(1468,1578)=(3,3), independently of P. This is a conditional label
restriction, not elimination of the whole U<V chronology branch.

The SAME forced red5 also gives a second, distinct true-label restriction.
The pair U=1467<1568 has exact difference

```
S=L(1467,1568) in {(1,4),(3,3)}.
```

Indeed I(1568)=(4,3,3,0). If S=(1,4), the blue5 is

```
U, 1568, 1578, 1678, 2678,
```

with labels `S,(2,4),(3,4),(4,1)`. Their second coordinates4,4,4,1
are nonincreasing, giving weak8 with the already established red5
`U,V,2467,2567,2678`. Therefore

```
U<V implies BOTH
L(1468,1578)=(3,3) and L(1467,1568)=(3,3).
```

These are two DIFFERENT actual pairs, simultaneously constrained in the
inclusion chain `1467<1468<1568<1578`. Each conclusion comes from its
explicit same-end red5/blue5 alternatives. Neither is inferred by fixing
the middle entries of a packet whose first and last colors differ. These
two valid interleaved-pair labels must not be confused with the different,
withdrawn pairs in the following record.

### Universal conditional clauses, with exact occupied supports

The last two conclusions are not specific to the selected61-state vector.
Let an arbitrary weak8-free actual input have the admissible shared
ideal-difference labels and color-growth interface. It suffices that the
following NINE distinct state words are all occupied:

```
S={1467,2367,2467,2567,2678,1468,1568,1578,1678}.
```

If its actual chronology has U=1467 before V=2367, the forced red5 and
the two alternative blue5 paths above prove BOTH label conclusions.
No occupancy condition on any other word of the70-state chart is used.
No unmentioned incomparable-pair chronology is fixed; in particular the
red and blue paths do not require an arbitrary relative order between
their different internal vertices. All inclusion orders and the one
assumption U<V are inherited from one physical input.

More precisely, each SINGLE conclusion needs only EIGHT occupied states:

```
S1={1467,2367,2467,2567,2678,1468,1578,1678},
S2={1467,2367,2467,2567,2678,1568,1578,1678}.
```

With o_W the occupancy bit, O_UV the single actual direction bit meaning
U before V, and L_{a,b}^{c} the shared one-hot label bit for cell c, the
two universally necessary clauses are

```
( OR_{W in S1} not o_W ) OR not O_UV OR L_{1468,1578}^{(3,3)},
( OR_{W in S2} not o_W ) OR not O_UV OR L_{1467,1568}^{(3,3)}.
```

Under occupancy of the relevant endpoints the two pair domains are
respectively `{(2,4),(3,3)}` and `{(1,4),(3,3)}`. Thus the same constraints
may equivalently be written with the final literal replaced, respectively,
by `not L_{1468,1578}^{(2,4)}` and `not L_{1467,1568}^{(1,4)}`.
The eight-state supports above contain all five red-path vertices and
all five relevant blue-path vertices; their two common endpoints account
for the total of eight.

These are reusable necessary constraints on overlapping slices sharing
the same owners, chronological direction and pair labels. They use only
the admissible growth interface and the same-end weak8 prohibition, not
the exact terminal-pair attainment assumptions of Section4. Neither
clause is an unconditional occupancy-only hole row: it permits the other
actual direction V<U and, in the U<V direction, enforces a label instead
of contradicting occupancy. No new entire-budget hole bound follows from
these clauses alone. This paper statement supplies their semantic proof;
no new SAT encoding, RUP/DRAT proof or checker run is claimed.

### Occupied transpose image and occupied reversed-complement eight-state image

The genuine transpose T(W)=rho8([8] minus W), with rho8(t)=9-t,
has the following complete dictionary for the nine-state support:

| Original W | T(W) |
|---|---|
|1467|1467|
|2367|1458|
|2467|1468|
|2567|1568|
|2678|4568|
|1468|2467|
|1568|2567|
|1578|3567|
|1678|4567|

All nine image words are occupied in the selected input. T preserves actual
chronology, transposes every shared cell label, and interchanges the two
colors. Thus if1467<1458, the image of the forced red path is the forced
BLUE path

```
1467,1458,1468,1568,4568.
```

The two alternative RED paths are, respectively,

```
1467,2467,3567,4567,4568,
1467,2567,3567,4567,4568.
```

The first becomes red if L(2467,3567)=(4,2), the undesired transpose of
(2,4); its other domain cell is (3,3). The second becomes red if
L(1467,2567)=(4,1), the undesired transpose of (1,4); its other domain
cell is again (3,3). Therefore the occupied transpose support gives

```
1467<1458 implies
L(2467,3567)=L(1467,2567)=(3,3).
```

Each individual conclusion has its corresponding eight-state image
support, obtained by transposing S1 or S2. This is the transported
conditional admissible-label theorem, not a claim that the selected
occupancy vector is globally transpose invariant.

For D(W)=rho8(W), corresponding to the ideal anti-automorphism
I -> rho4([4]^2 minus I), use ONLY the eight-state support S2 here.
Its full word dictionary is

| Original W | D(W) |
|---|---|
|1467|2358|
|2367|2367|
|2467|2357|
|2567|2347|
|2678|1237|
|1568|1348|
|1578|1248|
|1678|1238|

All eight image words are occupied. D reverses the interpreted chronology
and sends a cell (x,y) to(5-x,5-y). For any original I<J, the image pair
is read from D(J) to D(I), and its difference is exactly the rotated
original difference. Reversing each path and both coordinate values
preserves the original color-growth inequalities; the path colors do
not interchange. The trigger U<V becomes2367<2358. The conclusion
L(1467,1568)=(3,3) becomes

```
2367<2358 implies L(1348,2358)=(2,2),
```

conditional on occupancy of exactly
`{1237,1238,1248,1348,2347,2357,2367,2358}`.
For a direct hand replay, the forced RED path is

```
1237,2347,2357,2367,2358,
```

with labels `(s,1),(2,2),(2,3),(1,4)`, s in {2,3,4}.
Their first coordinates are nonincreasing. The alternative BLUE path is

```
1237,1238,1248,1348,2358.
```

The last pair has exact domain `{(2,2),(4,1)}`. Its undesired choice
(4,1) makes the four labels `(1,4),(2,1),(3,1),(4,1)`, with nonincreasing
second coordinates, and hence gives weak8 with that red path. Only(2,2)
remains. This direct replay also verifies the transported word and label
orientations without assuming any reversal of true longest-path ranks.
No exact-attainment property is transported by this argument.

Withdrawal record: proposed additional conclusions
`L(1467,1578)=(3,3)` and `L(1578,2678)=(3,4)` were withdrawn by their
proposer before incorporation. They do NOT follow from a packet with
different first and last colors: first B and last R allow BBBR, BBRR,
BRRR; first R and last B allow RRRB, RRBB, RBBB. Those two proposed label
equalities are not used here and must not be imported as forced labels.

These branches do NOT cover the input. In particular U<V, P=(3,3) remains
open subject to the two additional label restrictions just stated; the
Q=(4,1) alternative remains open, and P=(1,4), T=(3,3) remains
open. No new universal cover row, hole lower bound, or exclusion of all61
occupied states follows from Sections 1--3.

## 4. Exact terminal-pair attainment: a separate original-input obligation

Write the TRUE pair rank as sigma(u,v)=(b(u,v),r(u,v)), where b+1 and r+1
are the maximum blue and red path vertex counts ending in the SAME last
pair (u,v). In the no-blue6/no-red6 setting these coordinates are in [4].
For the exact state I(v)=downarrow{sigma(u,v):u<v}, sigma(u,v) belongs to
I(v) minus I(u). If that difference is a singleton {(i,j)}, then the actual
sigma(u,v) equals (i,j). It therefore attains BOTH a blue (i+1)-vertex path
and a red (j+1)-vertex path ending in (u,v). Their starting vertices need
not agree: this is not by itself a same-end weak8 certificate.

### 4.1 The occupied singleton pair 1357 -> 2357

Let a=1357=(3,2,1,0) and b=2357=(3,2,1,1). Inclusion forces a<b and the
singleton difference is {(4,1)}. Hence there is a true blue5

```
p, q, z, 1357, 2357,
```

in this actual input. All three p,q,z physically precede a. Every member of
the16-corner Boolean family obtained by adding the four cells
`(1,4),(2,3),(3,2),(4,1)` to I(a) contains I(a); the14 retained corners in
`../n866-overlap-order-20261118/DIAMOND_INTERFACE.md` therefore all occur at
or after a. Consequently p,q,z are three distinct actual points OUTSIDE
that14-corner domain, for every common chronological order.

Along this attained blue5 the first coordinates of the four pair labels
are exactly1,2,3,4. In particular sigma(z,a) has first coordinate3. Column3
of I(a) has only height1, so

```
sigma(z,1357)=(3,1).
```

Since this cell is absent from I(z), column3 of I(z) is zero; the ideal
condition also makes column4 zero. Equivalently the word of z begins12.
All15 chart candidates and their status in the selected input are

```
1234 1235 1236 1237 1238
1245 1246 1247 1248
1256 1257 1258
1267 [1268 hole] 1278.
```

These are14 occupied candidates after the difference-cell test alone.
Exact attainment gives a further essential filter: sigma(z,a)=(3,1)
attains a blue4 ending in (z,a). Its preceding pair has first coordinate2,
so I(z) must contain a cell in column2. Hence w3>=4. The FINAL necessary
list for this role has exactly nine occupied chart candidates:

```
1245 1246 1247 1248 1256 1257 1258 1267 1278.
```

Of these, five are proper subideals of I(a), forcing their actual order
before a: `1245 1246 1247 1256 1257`. The other four are incomparable:

```
1248 1258 1267 1278.
```

They are candidates only in the chronology branches where they precede a.
No claim is made that each candidate actually attains the required rank.

### 4.2 Color dual and an available red5 pair

True grid transpose interchanges the colors and sends a=1357 to itself,
but sends b=2357 to1358. Since1358 is a HOLE here, the formal dual pair
1357->1358 is not available in this input. It must not be inserted as an
occupied pair. Were it occupied with exact ranks, it would force red5
ending in that pair and an immediately preceding pair of rank (1,3).

There is an actual occupied red dual-type singleton pair

```
1457=(3,2,2,0) -> 1458=(4,2,2,0),
```

whose difference is {(1,4)}. Hence an actual red5 ends in this pair. If z'
is its third vertex, sigma(z',1457) has second coordinate3; row3 of I(1457)
contains only (1,3). Thus sigma(z',1457)=(1,3), I(z') has first-column
height at most2, and its word is a four-subset of [6]. The complete15-word
list is

```
1234 1235 1236 1245 1246 1256
1345 1346 1356 1456
[2345 hole] 2346 2356 [2456 hole] 3456.
```

These are13 occupied candidates from the difference-cell test alone.
Attainment of red4 ending in (z',1457) also forces a preceding incoming
pair at z' with second coordinate2. Thus I(z') has height at least2, and
the preceding upper bound makes its height EXACTLY2: its word ends6.
The FINAL necessary list has exactly nine occupied candidates:

```
1236 1246 1256 1346 1356 1456 2346 2356 3456.
```

The six beginning with1 are proper subideals of I(1457);
2346,2356,3456 are incomparable and require the appropriate actual order.
Every z' candidate is outside the14-corner
family because all corners have first-column height at least3. Unlike
Section4.1, it has NOT been shown that the first two vertices of this red5
are outside that family: 1457 is not its common bottom a.

### 4.3 General simultaneous predecessor test

For a TRUE rank sigma(u,v)=(i,j), if i>1 some actual z<u satisfies

```
chi(z,u,v)=blue and b(z,u)=i-1.
```

Likewise, if j>1 some actual z'<u satisfies

```
chi(z',u,v)=red and r(z',u)=j-1.
```

Proof: take a longest path attaining that coordinate, remove its last
vertex v, and use strict coordinate growth to get equality, rather than
only a lower bound, for the preceding pair. Equivalently the true ranks
satisfy the exact recurrences

```
b(u,v)=max({1} union {1+b(z,u): z<u and chi(z,u,v)=blue}),
r(u,v)=max({1} union {1+r(z,u): z<u and chi(z,u,v)=red}).
```

For any collection of outgoing pairs of one u, all these predecessor
requirements use the SAME actual incoming pair label sigma(z,u) and the
SAME chronological triple color. For a required first coordinate k the
candidate cell lies in column k of I(u) minus I(z); for a required second
coordinate l it lies in row l of that same difference. Distinct required
first coordinates require distinct incoming pairs, as do distinct required
second coordinates. A blue requirement k and a red requirement l can use
one incoming pair only if the common label is (k,l), that cell is in the
appropriate difference, and the relevant triple colors are compatible.
This is a necessary joint assignment test, not a claim that passing the
test constructs true ranks.

The packet axiom gives a useful counting supplement. Every monochromatic
path is monochromatic on all of its three-vertex subsets: first close
consecutive four-packets (equal first and last entries force the middle
entries equal), and induct on the span of a triple. Therefore a blue path
and a red path ending in the same pair (u,v) cannot share any earlier
vertex z, since the triple (z,u,v) would have both colors. Attaining
sigma(u,v)=(i,j) thus needs at least i+j-2 DISTINCT actual predecessors of
u: i-1 on the blue prefix and j-1 on the red prefix.

Every such predecessor z must satisfy I(u) minus I(z) nonempty. Hence if
the occupied candidates that can physically precede u number less than
i+j-2, that exact pair-rank choice is impossible. Joint chronology and
shared-label constraints can only shrink this candidate set. As a small
example, the singleton ideal1235 has only the empty ideal1234 as a possible
predecessor: every other nonempty ideal contains1235. A true rank (2,2)
on an outgoing pair from1235 is therefore impossible, despite passing the
coordinate-width/height test below. This rejection is simultaneous, rather
than choosing the same predecessor independently for its two colors.

One cheap consequence, applicable to every true pair rank, is

```
b(u,v) <= width(I(u))+1,
r(u,v) <= height(I(u))+1,
```

where width is the largest nonempty column index and height is column1's
height (both zero for the empty ideal). A coordinate above1 requires the
preceding pair of coordinate one smaller, whose cell lies in I(u).
Consequently the necessary domain for an actual edge u<v can be reduced to
`(I(v) minus I(u)) intersect ([width(I(u))+1] x [height(I(u))+1])`.
This is an ORIGINAL exact-state condition; arbitrary admissible assignments
need not obey it. Applying it to sigma(z,a) and sigma(z',1457) gives exactly
the width2 and height2 filters used above.

There is also the simpler maximal-cell attainment: each maximal cell of
I(u) must be the actual rank of some incoming pair, by the definition of
the down-closure. Different maximal cells require different predecessors.
For a=1357 the maximal cells are (1,3),(2,2),(3,1), so at least three distinct
actual predecessors of a are required, all outside the14-corner family.
The last demand agrees with the explicit z in Section4.1. Candidate words
for these three incoming labels respectively obey

```
(1,3): w4=6;
(2,2): w3<=4, w4>=5;
(3,1): w1=1,w2=2,w3>=4,
```

in addition to actual occupancy and chronology. For (2,2), the lower
bound records width and height at least1 and is not a sufficient
realization criterion; in particular1235 is further excluded by the
two-distinct-predecessor test just proved. These demands cannot be
re-solved with different labels for the same physical predecessor.

## 5. Global signed occupancy rows and a further backward step

Let o_W be1 when state word W is occupied in the ORIGINAL complete exact
state assignment, and0 otherwise. Section4.1 does not require the selected
nine-hole mask for its deduction. In the full70-state chart it proves the
signed occupancy inequality

```
sum_{4<=a<b<=8} o_{12ab} >= o_{1357}+o_{2357}-1.
```

There are TEN summands globally:
`1245 1246 1247 1248 1256 1257 1258 1267 1268 1278`.
Only nine are occupied in the selected vector, because1268 is a hole.
The inequality asserts existence of an actual attaining predecessor among
these summands when both endpoint states are occupied; it does not assert
that every occupied summand has the required true incoming pair rank.
This is a global exact-state signed row, not an unsigned admissible-slice
cover row and not a consequence already supplied by the271-row matrix.

For the actual red singleton pair1457->1458, the same argument gives

```
sum_{1<=a<b<c<=5} o_{abc6} >= o_{1457}+o_{1458}-1.
```

Again there are ten global summands, and nine are occupied in this vector:
2456 is the missing one. The formal transpose with trigger
o_{1357}+o_{1358}-1 is also valid in the original exact domain, but its
trigger is inactive here because1358 is absent.

One can trace back one further true blue predecessor without making any
new chronological assumption. Suppose the z actually selected in the
attained blue5 is u=124b, with 5<=b<=8. Its ideal heights are
`(b-4,1,0,0)` and sigma(u,1357)=(3,1). On an attaining blue4 ending in
that pair, let t be the vertex immediately before u. Its true pair rank
sigma(t,u) has first coordinate2. Column2 of I(u) has height1, hence

```
sigma(t,u)=(2,1),
t=123b' for some 5<=b'<=8.
```

Indeed omission of (2,1) makes column2 of I(t) zero, so the word begins123;
attainment of the preceding blue3 requires a nonempty first column,
excluding1234. Thus the four possible words are1235,1236,1237,1238, all
occupied here. Necessarily t<u. If b'<=b this order is forced by ideal
inclusion; if b'>b the ideals are incomparable and the attaining path
selects the t<u branch. This conclusion is conditional on u REALLY
playing the attained predecessor role, not on o_{124b}=1 alone.

## 6. Mixed four-packets on the two true incoming arms

Suppose x<y<v<w occur in the two different-color arms attaining a true
last pair (v,w). Monochromatic-path closure gives opposite colors for
chi(x,v,w) and chi(y,v,w). In the packet order

```
chi(x,y,v), chi(x,y,w), chi(x,v,w), chi(y,v,w),
```

the last two entries differ. Since the packet has at most one color
change, its first three entries must agree. Therefore

```
chi(x,y,v)=chi(x,y,w)=chi(x,v,w).
```

This uses the ACTUAL interleaving of the arms, so overlapping slices must
reuse these same four colors. It does not identify the starts of the two
attaining paths.

### A single exact pair is not an eight-point obstruction

Take six marked points in ANY common order, three marked blue and three
marked red, then append v,w. For every three-subset, color it by the mark
of its earliest point. That earliest point is always one of the six
marked points, since only v,w follow them.

For any x<y<z<t, the complete packet is

```
c_x, c_x, c_x, c_y,
```

where c_x and c_y are the marks of x and y. Thus this is a full ordered
rank-3 signotope, with one common chronological order and all triples
defined, for every interleaving of the six marks.

For a monochromatic path, every vertex except its last two must carry
that color. A blue path therefore has at most3+2=5 vertices, and a red
path also has at most5. Taking the three blue marked points in their
actual order and then v,w gives blue5; the analogous three red points
give red5. These are attained maxima at the same last pair, so the TRUE
rank is

```
sigma(v,w)=(4,4).
```

Any path of at least three vertices has the color of its first vertex.
Hence paths with a common first vertex and lengths at least three cannot
have opposite colors. In particular there is no common-end blue5/red5,
and the full8-point signotope has no weak8 (both path lengths are at
most5, so a length sum of10 would require precisely5+5). The mixed-arm
identity above holds throughout this construction.

More generally, interleave i-1 blue marks and j-1 red marks arbitrarily,
then append v,w, using the same earliest-mark triple rule. The true pair
rank is (i,j), with attained blue(i+1) and red(j+1) ending in that pair.
This last generalization asserts the exact ranks and packet property;
it does not assert no-weak8 for unrestricted i,j.

This construction is an actual full signotope with recomputable exact
pair ranks. It does NOT claim realization of any prescribed chart words
for its point ideals or extension to the selected61-state input. It
shows why one exact last pair, its two attaining arms, and their mixed
four-packets alone do not refute the input. A successful strengthening
must connect different common pairs or the actual occupied ideal states
and their simultaneous attainment requirements.

## Scope at stopping point

The paper calculation supplies explicit conditional same-end path certificates,
the nine-candidate external blue predecessor list, the nine-candidate external red
predecessor list, global signed rows, a joint exact-attainment interface,
and the exact8-point limitation example. It does not close
the remaining61-state input. It does not refute the admissible14-corner
example: that example explicitly does not assert exact terminal-ideal
realization. Exact attainment is usable only after binding to the original
full actual input or a proved complete exact reassignment, not as a new
admissible-slice axiom or as an automatically transportable cover row.
