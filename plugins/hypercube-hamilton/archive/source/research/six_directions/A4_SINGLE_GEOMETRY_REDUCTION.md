# Q5 A4 reduces to one remaining hole-geometry orbit

Date: 2026-11-01. Status: reductions and positive finite certificates;
independent review pending at initial writing. The remaining orbit is NOT
proved. Full A4 and full P6 remain NOT CURRENTLY JUSTIFIED.

## Claim R1A

Relative to the already established Q5 N14, Q4 N14_4 and NC_4, and the explicit
Q4 optional-edge certificates below, it suffices to prove A4 for the following
single hole-geometry family:

$$F\text{ is any matching of }K(Q_5),\quad
V(Q_5)\setminus V(F)=\{0,1,14,22\},\quad v=1.$$

The required result is a 31-vertex circle avoiding 1, preserving all of $F$,
with all new edges short. There are still all perfect matchings of the
other 28 vertices to handle in this family; reducing the geometry does not
enumerate or solve those matchings.

## L15/L18: optional short edges in Q4 circles

For a fixed matching $L$ and a specified extension type, define its optional
edge set $\mathcal E(L)$ to consist of short edges outside $L$ that occur
in at least one valid circle of that type. Each edge may have a different
witness circle. No simultaneous-prescription property is claimed.

**L15.** If $L$ has two same-parity holes and one specified forbidden hole,
then $|\mathcal E(L)|\ge15$ for its 15-vertex circles avoiding that hole.

**L18.** If $L$ has two opposite-parity holes, then $|\mathcal E(L)|\ge18$
for its full 16-vertex Hamilton circles.

For L15, translate the forbidden hole to 0 and normalize the other to 3 or
15. For L18, translate either hole to 0 and normalize the other to 1 or 7.
These are the complete distance orbits in $Q_4$. Each representative has
$13!!=135135$ matchings. The four files `q4_spectrum_A_3.bin`,
`q4_spectrum_A_15.bin`, `q4_spectrum_B_1.bin`, `q4_spectrum_B_7.bin`
give all matchings and, for each, a list of valid circles whose optional
edge union reaches the claimed lower bound.

Each record is a 16-byte mate array, one byte giving the number of circles,
then that many 15-vertex (type A) or 16-vertex (type B) circles. The verifier
`verify_q4_spectrum_certificates.py` checks every circle, the optional short
edge union, and complete matching-rank coverage, using the bijection proved
in `Q4_CORE_AND_A4_SPLIT.md`. In total 540540 matching records and 2448249
circle witnesses pass. Only positive witnesses are used: the proof does not
need an assertion that the producer enumerated all possible circles.
The separate exact-spectrum diagnostic programs are not proof dependencies.

## Z0: zero-crossing good cuts

Let $F$ have A4 holes $a,b,t,v$, with minority $a$ and forbidden majority
$v$. Suppose a coordinate cut has holes $v,b$ in side $A$, holes $a,t$ in
side $B$, and no matching edge crosses it. Then Q5 A4 holds.

Each face is a $Q_4$. The internal matching $F_A$ has exactly the same-parity
holes $v,b$; $F_B$ has exactly the opposite-parity holes $a,t$. Use the natural
identification of the two faces along the cut coordinate to regard their
short edges as elements of a common 32-edge $Q_4$ edge set. L15 and L18 give
optional edge sets of sizes at least 15 and 18. Their sum exceeds 32, so
their intersection is nonempty. Let $xy$ in $A$ and its mirror $x'y'$ in
$B$ be an edge of this intersection.

Choose a 15-circle $C_A$ avoiding $v$ and containing $F_A\cup\{xy\}$, and a
16-circle $C_B$ containing $F_B\cup\{x'y'\}$. Both chosen edges are optional,
so deleting them does not lose any edge of $F$. Join the resulting two
paths by the short crossing edges $xx'$ and $yy'$. The result is a single
circle through all vertices except $v$, containing $F$ and only short new
edges. This proves Z0.

Combining Z0 with the positive-crossing S4D lemma in
`Q4_CORE_AND_A4_SPLIT.md` proves:

**S2D.** Any coordinate cut with majority holes $v,b$ on one side and
minority $a$ and remaining majority $t$ on the other suffices for A4,
regardless of the number of crossing matching edges.

## S3D: a cut isolating the minority hole always suffices

Assume neither $ab$ nor $at$ is short; otherwise add that short edge to $F$
and apply the already established Q5 N14 to finish A4. Suppose a coordinate
cut has majority holes $b,t,v$ in side $A$ and minority hole $a$ in side $B$.
Let $C$ be the crossing matching, with port sets $X_A,X_B$ and size $c$.
Counting covered vertices of $A$ gives $2|F_A|+c=13$, so $c$ is positive odd.

The mirrors of $b,t$ in $B$ are distinct, are not $a$ by the nonadjacency
assumption, and are not any other hole. Thus each is either internally
matched in $B$ or belongs to $X_B$. If $c=1$, at most one of the two mirrors
is a crossing port; choose the other, which is internally matched. If
$c\ge3$, choose either mirror. Relabel $b,t$ so the chosen bridge is $tw$
with $w\in B$.

Choose a perfect matching $D$ on $X_A\cup\{t\}$. The matching $F_A\cup D$
has same-parity holes $v,b$, so N14_4 gives a cycle through $A\setminus\{v\}$.
Delete $D$, attach the original crossing edges at $X_A$, and add $tw$ at $t$.
All resulting internal A segments use only original F edges and short new
edges. There are two cases.

If $w$ is internally matched in $B$, the resulting paths have distinct
endpoints $X_B\cup\{w\}$ and interiors partitioning $A\setminus\{v\}$.
Compress them to a matching $R$. Write $k=F_B(w)$ and $d=R(w)$. Then

$$L=(F_B\setminus\{wk\})\cup(R\setminus\{wd\})\cup\{kd\}$$

is a matching of $K(B)$ with exactly the holes $a,w$, of the same parity.
N14_4 gives a cycle on $B\setminus\{w\}$. Expand $kd$ into $kw$ followed by
the transferred $w$--$d$ path, and expand every other edge of $R$. This
restores $w$ and every A vertex except $v$, and proves the desired A4 circle.

If $w\in X_B$, then $c\ge3$ by its selection. Let $x=F(w)\in X_A$ and
choose $D$ to contain $tx$. Since $D$ has at least two edges, deleting it
from the A circle separates $t$ and $x$ into different path components:
after deleting $tx$ alone, the remaining $t$--$x$ path contains every other
edge of $D$. Attaching $tw$ and the original $xw$ concatenates these two
components at $w$, without forming a cycle. All transferred paths now have
distinct endpoints $X_B\setminus\{w\}$, and their disjoint interiors
partition $(A\setminus\{v\})\cup\{w\}$. Compress to a matching $R$ on this
endpoint set. Then $F_B\cup R$ has precisely the same-parity holes $a,w$.
Apply N14_4 to avoid $w$, and expand $R$. This again gives the required A4
circle. Thus S3D is unconditional within the stated hole split.

All original crossing edges may be long; they are retained as original
required edges. Artificial matching edges are removed or expanded, and
the sole added bridge $tw$ is short.

## Proof of R1A: the remaining geometry has one orbit

Translate $a$ to 0, so $b,t,v$ are odd. Adjacent $a$--$b$ or $a$--$t$ cases
were handled above; assume $|b|,|t|\ge3$.

If some coordinate has $v_i=1$ and $b_i\ne t_i$, it is an S2D cut. If
some coordinate has $b_i=t_i=v_i=1$, it is an S3D cut. Therefore an input
not already solved must satisfy

$$\operatorname{supp}(v)\cap
 (\operatorname{supp}(b)\cup\operatorname{supp}(t))=\varnothing.$$

Indeed, at any coordinate where $v_i=1$, differing $b_i,t_i$ would trigger
S2D and two ones would trigger S3D, leaving only two zeros.

The distinct odd vertices $b,t$, each of weight at least three, have support
union of size at least four. As $v$ is nonzero and disjoint from that union
in a five-coordinate cube, the union has exactly four coordinates and
$v$ has exactly the fifth coordinate. Neither $b$ nor $t$ can have weight
five; hence each is a three-element subset of the other four coordinates.
Their missing coordinates there are distinct. A coordinate permutation
takes $v$ to 1 and the unordered pair $\{b,t\}$ to $\{14,22\}$. This proves
the asserted single remaining hole orbit.

In the previous labeled normalization of 770 residual configurations,
exactly $5\binom42=30$ lie in this orbit, and the other 740 are solved by
S2D or S3D. This count measures hole configurations only. The 30 configurations
are isomorphic to one family with arbitrary matching on 28 covered vertices.

## Remaining core

The unsolved core is now the explicitly quantified family in R1A. The
existence of a spanning cycle factor for it is already established by
`A4_SPANNING_FACTOR.md`, but its connectivity is still unproved. The
reduction does not justify declaring Q5 A4 or the full six-hole P6 level
closed. The 8--18-hole levels remain separate obligations.
