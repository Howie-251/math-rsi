# Q5 A6 by four-dimensional transfers and a zero-imbalance exception

Date: 2026-11-01. ARIS proof-writer draft. Status: a complete proposed
proof relative to the listed imported results and explicit finite positive
certificates; independent proof-checker review PENDING. This is not a
claim that full Q6 P6, or even all eight-hole P6, has been proved.

## Claim and notation

**A6.** Let $F$ be any matching of the complete graph $K(Q_5)$ with
exactly six uncovered vertices (holes), two of one parity and four of
the other. For each specified hole $v$ in the larger class, there is a
cycle on exactly $Q_5-v$ containing $F$, all of whose edges outside $F$
are edges of $Q_5$ (short edges).

Call the two-hole parity $E$ and the four-hole parity $O$. These names
may be interchanged by translation. Required edges of $F$ may be long
or join vertices of the same parity. No argument assumes otherwise.

In a coordinate cut let $A$ contain $v$, and let $B$ be the other face.
Use global parity labels on both faces. Let $H_A,H_B$ be the original
holes, $F_A,F_B$ the internal required edges, $C$ the crossing required
edges, $c=|C|$, and $X_A,X_B$ their endpoint sets. A crossing edge need
not be short. For a vertex $t$ let $\bar t$ denote its short neighbor
across the cut, not its required partner. Write
$\delta=|H_A\cap O|-|H_A\cap E|$.

## Dependencies and proof map

1. Full Q5 A4: `CANONICAL_A4_CLOSURE.md`, audited in
   `CANONICAL_COMPLETION_REVIEW.md`.
2. Q4 N14 (two same-parity holes, avoid one), A4_4, NC_4, and the
   general GQ4-avoid/GQ4-cycle consequences in
   `Q4_CORE_AND_A4_SPLIT.md` and `Q4_GENERAL_AUGMENTATION.md`.
3. Q4 T44 (four same-parity holes, avoid any two),
   `Q4_TWO_AVOIDED_TRANSFER.md`, reviewed in `Q4_TWO_AVOIDED_REVIEW.md`.
4. Previously audited two-hole optional-short-edge union bounds L15/L18,
   and the four-hole extensions in Section 2 below.
5. The new alternate-endpoint positive certificates in Section 3.
6. The complete residual hole geometry census in Section 4, followed by
   explicit transfer proofs for every cut and the exceptional geometry.

All circle/path extension inputs preserve required edges and add only
short edges. Artificial edges used to encode paths may be arbitrary;
each such edge is removed or expanded in the final construction.

## 1. Preprocessing and transfer conventions

If any minority hole is adjacent to a majority hole other than $v$,
add that short edge and invoke Q5 A4, avoiding $v$. Henceforth assume
there is no edge between the two minority holes and the three other
majority holes. In particular a mirror of a minority hole cannot be
an original nonforbidden majority hole, and a mirror of a nonforbidden
majority hole cannot be a minority hole.

Deleting a nonempty matching $D$ from a cycle leaves disjoint paths
whose endpoints are the endpoints of $D$. If two endpoints of a removed
edge are rejoined while at least one other gap remains, this does not
create a closed component. More generally, restoring any proper subset
of the removed edges by internally disjoint paths still leaves a path
forest. Attaching original crossings at distinct free ports and a short
bridge at a distinct chosen hole preserves this property, except for
explicit duplicated B-side bridge vertices treated below.

Compressing the resulting disjoint paths means replacing each path by
an artificial edge on its two endpoints. After a single B-side cycle
containing these artificial edges has been obtained, replacing each edge
by its path gives one cycle. Its internal vertices are pairwise disjoint
and outside the B-side cycle. This is the expansion used below.

## 2. Four-hole optional-edge bounds

For a matching $L$ of $K(Q_4)$ let its optional-edge union be the set of
short edges outside $L$ occurring in at least one extending cycle of the
specified vertex set. No simultaneous prescription of these edges is
asserted.

**O15.** With one minority and three majority holes, avoiding any specified
majority hole, the optional-edge union has at least 15 elements.
If a short pair of free vertices can be added without using the forbidden
hole, add it and apply the already audited same-parity two-hole L15
bound. Its optional edges are still outside the original matching.
Otherwise translate the minority hole to 0. The two nonforbidden odd
holes have weight three. By a coordinate permutation they are 7 and 11.
The forbidden odd hole has three orbits under their stabilizer, represented
by 1,4,13. The three `q4_four_spectrum_A_*.bin` files give all $10395$
matchings for each representative with cycles certifying a union of size
at least 15.

**O18.** With two holes of each parity, the full-cycle optional-edge union
has at least 18 elements. If there is a short free pair, add it and use
the opposite-parity two-hole L18 bound. Otherwise normalize even holes
to $0,z$, where $z=3$ or 15. If $z=15$, their neighbors exhaust all odd
vertices, impossible. If $z=3$, the only two odd vertices nonadjacent to
both are 13,14. The file `q4_four_spectrum_balanced.bin` covers all
$10395$ matchings with holes $0,3,13,14$.

Producer `q4_four_hole_spectrum.cpp` stores a mate array, a cycle count,
and explicit cycles. Checker `verify_q4_four_hole_spectrum.py` checks
all 41580 records and 160549 cycles, matching rank coverage, vertex sets,
required edges and every new edge. The two-hole bounds cover the cases
with respectively two same-parity or two opposite-parity holes.

## 3. Alternate endpoint lemma B4

Let $L$ be an arbitrary matching of $K(Q_4)$ with holes $v,b,z,d$, where
$v,b$ have one parity and $z,d$ the other. Suppose $z$ is not adjacent
to $b$. There is a path on exactly $Q_4-v$, starting at $d$, ending at
some vertex of the parity of $d$ other than $z$, containing $L$ and
using only short new edges.

Translate $v$ to 0. Normalize the ordered triple $(b,z,d)$ by all 24
coordinate permutations. There are exactly 196 ordered configurations
and 13 orbits, listed in `q4_balanced_avoid_path_orbits.json`. Each has
$11!!=10395$ matchings of the other twelve vertices. The files
`q4_balanced_avoid_path_b_z_d.bin` have one 31-byte record for every
matching: sixteen mate bytes (255 for holes), followed by the fifteen
path vertices. All 135135 rows are positive.

`verify_q4_balanced_avoid_path.py` independently regenerates the full
196-configuration orbit cover, verifies a bijective matching rank cover
in every file, and checks every path, both endpoints, every required
edge, and shortness of all remaining edges. Thus search completeness is
not needed: exhaustive explicit positive witnesses prove B4.

## 4. Complete geometry cover

Translate one minority hole to 0. The other has weight 2 or 4, so a
coordinate permutation sends it to 3 or 15. The three nonforbidden
majority holes are any three odd vertices nonadjacent to both minorities;
$v$ is any remaining odd vertex. This lists 728 configurations for $z=3$
and 260 for $z=15$, totaling 988. It is a complete cover, not a minimal
orbit list.

`a6_cut_cover.py` enumerates precisely these choices and the five values
of $\delta$. Choosing a cut with $\delta=2,3,4,1$, in that preference
order, leaves exactly two configurations with no such cut:

$$H_E=\{0,3\},\quad (v,H_O\setminus\{v\})=
(1,\{14,22,26\})\text{ or }(2,\{13,21,25\}).$$

Swapping coordinates 0 and 1 interchanges these exceptions. In each,
all five values of $\delta$ are zero. Sections 5--8 cover the selected
cuts; Section 9 covers the exception. Only 988 hole sets are enumerated:
the transfer proofs apply to every arbitrary matching with those holes.

## 5. A cut with delta two

Then $A$ has imbalance two and $B$ is balanced. The number $c$ is even,
because each face has an even number of original holes.
If $c>0$, pair $X_A$ into $D$. GQ4-avoid gives an A-side cycle avoiding
$v$ and containing $F_A+D$. Delete $D$, attach all crossings, and
compress to $R$ on $X_B$. The matching $F_B+R$ has exactly $H_B$ as
holes, hence GQ4-cycle gives its full B-side cycle. Expand $R$.

If $c=0$, write $|H_A\cap E|=k$. Here $k=0$ or 1. The only alternative
$k=2$ would put two minority and all four majority holes in one Q4;
two minority vertices have at least six odd neighbors, so three odd
nonforbidden holes cannot all avoid them. This contradicts preprocessing.
Thus the A holes have counts $(0,2)$ or $(1,3)$ and the B holes have
counts $(2,2)$ or $(1,1)$. The A optional union has size at least 15,
the B union at least 18. Identify both faces with Q4; its 32 edges force
these unions to intersect. Choose corresponding optional edges in one
A cycle avoiding $v$ and one full B cycle, delete them, and add the two
short crossing edges between corresponding endpoints. The result is a
single cycle on $Q_5-v$, preserving all required edges.

## 6. A cut with delta three

Here $A$ has either three majority holes and no minority, or four
majority holes and one minority. There are at least two nonforbidden
majority holes in $A$. Their B mirrors are distinct minority-parity
vertices covered by $F$. The count $c$ is odd, hence positive.
If $c=1$, choose a hole $t$ whose mirror $w$ is not the unique B port.
If $c\ge3$, choose any such $t$.

Pair $X_A\cup\{t\}$ into $D$. The holes of $F_A+D$ have imbalance two;
GQ4-avoid supplies a cycle avoiding $v$.
If $w$ is internal to $F_B$, delete $D$, attach $C$ and bridge $tw$,
and compress to $R$ on $X_B\cup\{w\}$. With $k=F_B(w)$ and $q=R(w)$,
replace $wk,wq$ by $kq$. This is a matching with holes $H_B\cup\{w\}$,
whose minority-parity excess is two. GQ4-avoid on B avoids $w$.
Expand $kq$ via $kw$ and the transfer path, and expand the other R edges.

If $w\in X_B$, choose $D$ to contain $tx$, where $x$ is its original
crossing partner. Since $c\ge3$, there is another edge of $D$. Deleting
$D$ separates $t$ and $x$ into different paths. Attaching $tw,xw$ rejoins
those paths through $w$, and creates no circle. The compressed matching
$R$ has endpoints $X_B-\{w\}$ and interiors $A-v$ together with $w$.
Now $F_B+R$ has holes $H_B\cup\{w\}$. Apply GQ4-avoid avoiding $w$
and expand. Both cases give the required 31-cycle.

## 7. Double-bridge transfer and delta four

Suppose two distinct original holes $t,s$ in A, neither $v$, have the
same parity, and their mirrors $w=\bar t,z=\bar s$ in B are covered.
Suppose the remaining A holes are exactly two same-parity vertices,
including $v$, and the original B holes are exactly two vertices of the
parity of $w,z$. In particular $c$ is even. The following conditions
each suffice for A6:

1. Both $w,z$ are internal to $F_B$, and either $wz\notin F_B$ or $c\ge2$.
2. Exactly one of $w,z$ is a crossing port (necessarily $c\ge2$).
3. Both are ports and $c\ge4$.

Pair $X_A\cup\{t,s\}$ into $D$, choosing it as follows. For each bridge
whose B endpoint is a port, include the edge joining its A hole to the
original A partner of that port. These prescribed edges are disjoint.
For case 1 with $wz\in F_B$, instead prescribe $ts\in D$. Complete the
remaining pairs arbitrarily. N14_4 gives an A cycle avoiding $v$.

Let $p\in\{0,1,2\}$ be the number of bridge endpoints that are ports.
Delete $D$, attach all original crossings and the bridges $tw,sz$.
At each port bridge vertex two segments join. This restores a prescribed
D edge by a two-edge path; since $|D|=(c+2)/2>p$, at least one gap remains
and the transferred graph is a path forest. Its interiors partition
$A-v$ and the $p$ port bridge vertices. Its endpoints are the other
B ports and the $2-p$ internal bridge vertices. Compress to $R$.

In $F_B+R$, the only vertices of degree two are the internal bridge
vertices. Suppress them along their components to get a matching $L_B$.
There is no closed component: the only possible one would require both
bridge vertices to be internal and $wz$ to be an edge of BOTH $F_B$ and
$R$. When $wz\notin F_B$ this cannot occur. When $wz\in F_B$, the chosen
$ts\in D$ and $|D|\ge2$ place $t,s$ in different path components after
deletion, so $wz\notin R$ as well. With zero or one internal bridge
vertex a cycle cannot occur, since every other vertex has degree at most
one. The holes of $L_B$ are exactly $H_B\cup\{w,z\}$, four vertices of
one parity. T44 gives a B cycle avoiding $w,z$. Undo all suppressions and
expansions. Each avoided bridge vertex is restored exactly once, together
with all of $A-v$, and every original edge is retained.

For $\delta=4$, all four majority holes lie in A and both minority holes
in B. The three nonforbidden majority holes offer three covered mirror
vertices. Choose two for this transfer. If at least two are ports and
$c\ge4$, use case 3. If there is a port and an internal vertex, use case 2.
If all three are internal, at most one pair is an edge of $F_B$, so
choose an unpaired pair and use case 1. The only remaining possibility
is that all three are ports, which implies even $c\ge4$. Thus every
delta-four input is covered.

## 8. A cut with delta one

Write $k=|H_A\cap E|$, so $|H_A\cap O|=k+1$. The value $k=0$ is
impossible: B would have two minority and three majority holes, all
nonforbidden, contrary to the Q4 neighbor bound and preprocessing.
Thus $k=1$ or 2. The crossing count $c$ is odd and positive.

For any minority hole $y\in A$, any root port $d\in X_A$, and any pairing
$D$ of $X_A-\{d\}$, add the auxiliary edge $dy$ to $F_A+D$. Its holes
have majority excess two and include $v$. GQ4-avoid gives a cycle on
$A-v$ containing $dy$. Deleting $dy$ gives a spanning $d$--$y$ path
containing $F_A+D$ with only short new edges. This holds for EVERY root
port and EVERY pairing D.

The mirror $w=\bar y$ has majority parity and is covered in B. If it is
internal, delete D, attach crossings and $yw$, compress to R, and repair
the unique overlap at $w$ as in Section 6. The resulting matching has
holes $H_B\cup\{w\}$ of majority excess two. GQ4-avoid avoiding $w$
and expansion finish the construction.

If $w$ is a port and $c\ge3$, choose $d$ to be its original partner.
Now D is nonempty. Deleting D separates the two ends $d,y$ of the A path;
attaching $dw,yw$ joins different path components at $w$. Compress on
$X_B-\{w\}$ and apply GQ4-avoid to $F_B+R$ avoiding $w$. Its holes are
again $H_B\cup\{w\}$.

When $k=2,c=1$, choose a minority hole whose mirror is not the unique
port, and use the internal case. The only remaining case has $k=c=1$
and the unique minority hole $y$ mirrored at the unique port $w$.
Let $d$ be the unique A port; the holes of $F_A$ are $v,b,y,d$, where
$v,b$ have majority parity. Preprocessing says $y$ is not adjacent to b.

If $d$ has majority parity, A4_4 gives a cycle on $A-v$ containing $F_A$.
At its free vertex $d$ both incident cycle edges are short. Their two
neighbors have minority parity; choose a neighbor $z\ne y$ and delete
$dz$. This gives an A path from $d$ to $z$ avoiding $v$.
If $d$ has minority parity, B4 gives exactly such a path, with endpoint
$z$ of minority parity and $z\ne y$. In both cases $z\ne d$ as well.

Attach the original crossing $dw$ and the new bridge $z\bar z$ to this
path. Because $z\ne y$, its mirror $q=\bar z$ is not the unique B port w.
It has majority parity and hence is either an original majority hole
or internally covered. Compress to the edge $wq$.
If q is a hole, $F_B+wq$ has balanced holes, so GQ4-cycle applies.
If q is internally covered, suppress q through its $F_B$ edge and $wq$;
the resulting matching has holes $H_B\cup\{q\}$ of majority excess two.
GQ4-avoid avoids q. Expanding restores the A path and q and completes
the construction in all delta-one cases.

## 9. The all-zero exceptional geometry

It suffices by the stated coordinate swap to handle

$$H_E=\{0,3\},\quad H_O=\{1,14,22,26\},\quad v=1.$$

For each coordinate $j\in\{2,3,4\}$, put its zero face in A. It contains
the minority holes $t=0,s=3$, the forbidden hole 1, and exactly one other
majority hole. B contains exactly two majority holes. The two bridges
from $0,3$ have endpoints $w_j=2^j,z_j=2^j+3$. These have majority parity
and are covered. Consequently Section 7 applies unless the cut has one
of these two exceptional forms:

- $c_j=0$ and $w_jz_j\in F_B$;
- $c_j=2$ and its B port set is exactly $\{w_j,z_j\}$.

Indeed even $c_j$ and the three cases in Section 7 exhaust all other
possibilities, including an internal required edge $w_jz_j$ when $c_j>0$.

Suppose all three cuts have one of these exceptional forms. Let S be the
vertices whose last three bits (coordinates 2,3,4) have weight at most
one. Then $|S|=4(1+3)=16$. Its original holes are exactly $0,1,3$;
the other three holes $14,22,26$ each have two of those bits set.
No edge of F can leave S. To see this, take an edge from $x\in S$ to
$r\notin S$. At some coordinate $j\in\{2,3,4\}$ the outside endpoint r
has bit 1 and x has bit 0. If $c_j=0$ the edge is impossible. Otherwise
the B port r must equal $w_j$ or $z_j$, each of which has only ONE set
bit among those three coordinates, contradicting $r\notin S$.
Thus F would match the 13 covered vertices of S entirely within S,
which is impossible for a matching. At least one of the three cuts is
therefore nonexceptional, and its double-bridge transfer proves A6.

## Conclusion and remaining scope

Preprocessing and the complete 988-configuration cover reduce every A6
input to Sections 5--9. These sections give cycles through exactly
$Q_5-v$, preserving arbitrary original edges and adding only short ones.
Subject to independent audit of this argument and the new finite inputs,
the A6 proof is complete relative to the declared prior results.

`EIGHT_HOLE_CONDITIONAL_REDUCTION_DRAFT.md` separately explains the
consequence for all free-target eight-hole Q6 inputs and some covered
targets. Its covered residual R8-covered remains a genuine obligation.
Neither A6 nor that conditional reduction alone closes full eight-hole
P6, and the higher 10--18-hole levels also remain open.
