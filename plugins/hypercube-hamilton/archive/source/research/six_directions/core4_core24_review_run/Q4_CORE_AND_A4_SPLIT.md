# Four-dimensional core certificates and an unconditional A4 split class

Date: 2026-11-01. Status: finite positive certificates plus mathematical
reductions; independent review pending at initial writing. Full Q5 A4 and P6
remain unproved. None of the claims below assumes Q5 A4 or P6.

## Exact core claims

**N14_4.** Every matching of $K(Q_4)$ with exactly two same-parity holes has a
cycle through all vertices except either prescribed hole, preserving every
matching edge and using only short new edges.

**A4_4.** Every matching of $K(Q_4)$ with exactly four holes of parity counts
3 and 1 has a cycle through all vertices except any prescribed majority-parity
hole, preserving every matching edge and using only short new edges.

All matching edges may be arbitrary pairs of vertices, including same-parity
long edges. A short edge changes exactly one coordinate. Hamilton circles in
these statements have 15 vertices and may include the prescribed long edges.

## Finite proof of N14_4

Translate the prescribed forbidden vertex to 0 by bitwise XOR. The other
hole is a distinct even vertex, at Hamming distance two or four. A coordinate
permutation takes it to 3 or 15 respectively. These automorphisms preserve
short edges, long prescribed edges, and the extension question.

For each representative, all perfect matchings of the other 14 vertices are
covered by a certificate file: `q4_two_hole_3.bin` or `q4_two_hole_15.bin`.
There are $13!!=135135$ such matchings in each representative. Every record
contains the entire mate array and a 15-vertex cycle witnessing the assertion.

The independent checker `verify_q4_extension_certificates.py` checks:

1. The mate array is an involution without fixed points on exactly the
   14 prescribed covered vertices, with precisely the two prescribed holes.
2. The cycle contains all 15 required vertices exactly once, includes every
   matching edge, and has only short edges outside the matching.
3. No perfect matching is omitted or repeated. To certify this without
   depending on the generator's recursion order, compute its rank as follows.
   Remove the least remaining vertex $x$. If its mate has index $i$, starting
   at zero, in the increasing list of other remaining vertices, its rank is
   $i(2k-3)!!$ plus the recursively computed rank of the remaining matching,
   where $2k$ is the number of vertices before removing this pair. Empty
   rank is zero and $(-1)!!=1$. There are $2k-1$ disjoint equal-size blocks,
   so induction proves a bijection with $0,\ldots,(2k-1)!!-1$.
   The checker marks all these ranks and requires each exactly once.

All 270270 records pass. Thus, modulo the transparent finite certificate
verification, the two representatives and symmetry prove N14_4 completely.
This proof does not import the five-dimensional version of N14.

## Finite proof of A4_4

Translate the minority-parity hole to $a=0$. Let $v$ be the forbidden odd
hole and $b,t$ the two remaining odd holes. If $a$ is adjacent to $b$ or $t$,
add that short edge. The resulting matching has two same-parity holes, and
N14_4 proves the required 15-cycle avoiding $v$.

Otherwise $b,t$ are distinct weight-three vertices in $Q_4$. Permuting
coordinates makes their unordered pair $\{7,11\}$. Their supports share
coordinates 0 and 1 and differ in coordinates 2 and 3. The permutations of
the two common coordinates and of the two differing coordinates preserve
this unordered pair. The six possible forbidden odd vertices have exactly
three orbits:

$$\{1,2\},\qquad \{4,8\},\qquad \{13,14\}.$$

Choose representatives $v=1,4,13$. For each, the other 12 vertices have
$11!!=10395$ perfect matchings. Files `q4_four_hole_1.bin`,
`q4_four_hole_4.bin`, `q4_four_hole_13.bin` contain a 15-cycle certificate
for each one. The same independent checker validates the matching, cycle,
and full rank coverage. All 31185 records pass. Together with the adjacent
branch, this proves A4_4.

The five files total 301455 certificates. The search programs' positive
outputs are independently checked; neither a numerical solver's feasibility
judgment nor the completeness of its search is needed for acceptance.

## Derived four-dimensional path inputs

**N10_4.** Let $L$ be an arbitrary matching of $K(Q_4)$ with exactly two holes
$r,s$. For any $y\ne r$ with $p(y)=p(s)$ there is a Hamilton $r$--$y$ path
containing $L$, with all newly added edges short.

If $y$ is free, then $y=s$. Add $rs$ to make a perfect matching of $K(Q_4)$,
apply Fink's perfect-matching extension theorem, and delete $rs$ from the
resulting Hamilton circle. It yields the stated path. This is the only
external extension theorem needed here; it permits arbitrary original edges
of the complete graph and adds short edges.

If $y$ is covered, let $k=L(y)$. The matching
$L'=L-yk+kr$ has same-parity holes $y,s$. N14_4 supplies a 15-cycle avoiding
$y$ and containing $L'$. Delete $kr$ to obtain an $r$--$k$ path on all vertices
except $y$, and append the original edge $ky$. The path now contains all of
$L$ and only short edges outside $L$. The appended edge may be long, but is
an original required matching edge.

**NC_4.** If the two holes of $L$ have opposite parity, $L$ extends to a
Hamilton circle of $K(Q_4)$ with only short new edges. Choose any short
neighbor $y$ of the free root $r$, use N10_4, and close the Hamilton path by
$ry$. Such a spanning path on 16 vertices cannot already contain the edge
between its two endpoints, so this produces a simple circle.

**K4_4.** A balanced four-hole matching of $K(Q_4)$ has a Hamilton path from
any free root $r$ to any vertex $y$ of the opposite parity, preserving the
matching and adding only short edges. If $y$ is free, add the auxiliary
edge $ry$; the remaining holes are opposite, so NC_4 gives a full circle;
delete $ry$. If $y$ is covered with mate $k$, swap $yk$ to $kr$. The four
holes now have counts 3 and 1, with $y$ in the majority. Apply A4_4 avoiding
$y$, delete $kr$, append the original $ky$. Both constructions meet the
specified endpoints and restore all original matching edges.

## S4D: a Q5 A4 class closed without assuming A4

Let $F$ be an arbitrary $K(Q_5)$ matching with holes $a,b,t,v$, where $a$
has the minority parity and the desired circle must avoid $v$. Suppose a
coordinate cut has on one side $A$ exactly the holes $v,b$, on the other
side $B$ exactly $a,t$, and at least one original $F$ edge crosses the cut.
Then the Q5 A4 conclusion holds for $F$.

Let the crossing matching be $C$, with endpoint sets $X_A,X_B$. Since
$|A|=16$ and exactly two vertices of $A$ are globally free, the equality
$2|F_A|+|C|=14$ makes $|C|$ even. Thus it is at least two. Choose any
perfect matching $D$ of the complete graph on $X_A$. Then $F_A\cup D$ has
the same-parity holes $v,b$. N14_4 supplies a cycle on $A\setminus\{v\}$
containing it, with all other edges short.

Delete $D$. Because $D$ is a nonempty matching in a simple circle, the result
is a disjoint family of nontrivial paths, with endpoints exactly $X_A$.
Attach each corresponding original crossing edge of $C$. The paths now
have endpoints $X_B$, disjoint interiors in $A\setminus\{v\}$, and together
cover that entire side. Replace each by a formal edge to get a matching $R$
on $X_B$. No restriction on the length or parity of edges in $C$ or $R$
is imposed; edges of $C$ are original required edges, not new short edges.

The matching $F_B\cup R$ of $K(B)$ has precisely the opposite-parity holes
$a,t$. NC_4 supplies its full Hamilton circle. Expand every $R$ edge into
its corresponding path. This gives a single circle through
$V(Q_5)\setminus\{v\}$, containing $F$ and with every edge outside $F$ short.
All artificial edges $D,R$ have disappeared. This proves S4D.

## G4D: a whole hole-geometry family, with no matching restriction

Normalize $a=0$. If both masks

$$v\mathbin{\&}b\mathbin{\&}\neg t\ne0,
\qquad v\mathbin{\&}t\mathbin{\&}\neg b\ne0$$

are nonzero (all masks restricted to the five cube coordinates), then every
matching with these holes satisfies Q5 A4.

Choose a coordinate $i$ from the first mask and $j$ from the second. The
four holes have distinct $(i,j)$ patterns: $a:00$, $b:10$, $t:01$, $v:11$.
If any matching edge crosses either coordinate cut, that cut has the S4D
hole split, so S4D applies. If no edge crosses either cut, all matching
edges lie within the four 8-vertex $Q_3$ cells. Each cell has exactly one
hole and hence seven covered vertices, impossible for an internal matching.
Therefore at least one cut has crossings, proving the claim.

For normalized residual Q5 geometries ($a=0$, $b,t$ nonadjacent to $a$,
unordered $b,t$, and distinct forbidden odd $v$), there are 770 choices.
Exactly 255 have both masks nonzero, 350 only one, and 165 neither. These
are labeled geometric counts, not isomorphism counts or matching counts.
G4D closes all matchings in the first class. S4D can also close instances in
the one-mask class when a corresponding cut actually has a crossing edge.

## Remaining obligations

The four-dimensional input A4_4 does not by itself prove five-dimensional
A4. The complete remaining transfer for hole configurations outside G4D,
including zero-crossing cases, is not supplied here. A4_4 and K4_4 are now
available for that research; they must not be invoked with an unverified
dimension or endpoint condition. The unconditional full six-hole P6 result
and all remaining 8--18-hole obligations remain open.
