# Two avoided vertices in Q4 and minority-isolating A4 cuts

Date: 2026-11-01. Status: finite certificates and reductions; independent
review pending at initial writing. Q5 A4 and full P6 remain unproved.

## T44: four same-parity holes, two prescribed avoided holes

Let $L$ be an arbitrary matching of $K(Q_4)$ with four holes, all of the same
parity. For any two prescribed holes $x,y$, there is a cycle through exactly
$V(Q_4)\setminus\{x,y\}$, containing every edge of $L$, with only short new
edges. Thus this is a 14-vertex cycle, including the other two holes.

Translate $x$ to 0. The other holes then are even. Permute coordinates to
take $y$ to 3 or 15, covering its possible distances two and four. For each
choice, the remaining two holes are any unordered pair of the remaining six
even vertices, giving 15 configurations. Each of the 30 configurations has
$11!!=10395$ perfect matchings of its 12 covered vertices.

The files `q4_two_avoided_p_b_t.bin` contain all these matchings and a
14-cycle for each. Every 30-byte record contains a 16-byte mate array
(255 denotes holes), followed by the 14 cycle vertices. The independent
checker `verify_q4_two_avoided_certificates.py` verifies the matching, the
cycle and its required/new edges, and complete bijective matching-rank
coverage as defined in `Q4_CORE_AND_A4_SPLIT.md`. All 311850 records pass.
No Hamilton-search completeness or negative result is relied on. This proves
T44 by explicit exhaustive positive certificates and the stated symmetries.

## S1D: minority-isolating cuts

Consider a Q5 A4 matching $F$ with minority hole $a$ and majority holes
$b,t,v$, where $v$ is forbidden. Suppose a coordinate cut has all three
majority holes in side $A$ and $a$ in side $B$. Let $w$ be the short neighbor
of $a$ across this cut. Assume $w\notin\{b,t,v\}$, and suppose either

1. $w$ is covered by an internal edge of $F_A$; or
2. $w$ is a crossing endpoint and the crossing matching has at least three
   edges.

Then the full Q5 A4 conclusion holds for $F$.

Let $C$ be the crossing matching, with endpoint sets $X_A,X_B$ and size $c$.
Since side $B$ has exactly one hole, $2|F_B|+c=15$, so $c$ is odd and positive.
Choose a perfect matching $D$ on $X_B\cup\{a\}$; an additional choice in
case 2 is specified below. Then $F_B\cup D$ is a perfect matching of $K(B)$.
By Fink's perfect-matching extension theorem it has a Hamilton circle with
only short new edges. Delete the nonempty matching $D$ to obtain disjoint
nontrivial paths with endpoints $X_B\cup\{a\}$. Attach the original edges of
$C$ at $X_B$, and attach the new short bridge $aw$ at $a$.

### Case 1: internal partner at the bridge endpoint

The resulting paths have distinct endpoints $X_A\cup\{w\}$, and interiors
partition $B$. Compress them to a matching $R$ on this endpoint set. Its
unique overlap in covered vertices with $F_A$ is $w$. Write $k=F_A(w)$
and $d=R(w)$. The matching

$$L=(F_A\setminus\{wk\})\cup(R\setminus\{wd\})\cup\{kd\}$$

has precisely the four holes $b,t,v,w$, all of the same parity because
$w$ is opposite to the minority hole $a$. All listed edges are disjoint:
$k$ is internal to $F_A$, $d\in X_A$, and none is a hole. Apply T44 to
avoid $v,w$ and obtain a cycle on $A\setminus\{v,w\}$. Expand $kd$ into
the original edge $kw$ followed by the transferred $w$--$d$ path. Expand
every other edge of $R$. This restores $w$, all of $B$, all original edges
of $F$, and gives a single circle through $Q_5\setminus\{v\}$.

### Case 2: a crossing partner at the bridge endpoint

Let $x\in X_B$ be the original partner of $w$. Choose $D$ to contain $ax$;
pair the remaining $c-1$ ports arbitrarily. Because $c\ge3$, $D$ has at
least two edges. In the B circle with $D$ removed, the vertices $a,x$ lie
in different path components: deleting $ax$ alone leaves an $a$--$x$
path containing every other edge of $D$, so deleting one more of those
edges separates $a$ from $x$.

After attaching $aw$ and the original $xw$, those two different paths join
at $w$ into a single path. No cycle is created. All resulting paths have
distinct endpoints $X_A\setminus\{w\}$ and disjoint interiors partitioning
$B\cup\{w\}$. Compress them to a matching $R$ on $X_A\setminus\{w\}$.
Now $L=F_A\cup R$ has the four same-parity holes $b,t,v,w$. Apply T44 avoiding
$v,w$ and expand $R$. The expanded circle restores $w$ and $B$, preserves
$F$, and uses only short new edges. This proves case 2 and S1D.

The excluded crossing case $c=1$ cannot be inserted into this proof: then
$D=\{ax\}$ and the two attachments close a separate B-side circle. A
different argument would be needed; no conclusion is asserted for it here.

## G2D: two coordinates shared by all majority holes suffice

Normalize $a=0$. If $b,t,v$ have at least two common 1-coordinates, then
every matching with these holes satisfies Q5 A4.

Choose two such coordinates $i,j$. For each, the minority-isolating cut has
an odd positive crossing count. The bridge endpoint $w_i=2^i$ (respectively
$w_j=2^j$) is not a hole, because the majority holes have both coordinates
equal to one. Thus each endpoint is either internally matched in its
majority side, or is a crossing endpoint. S1D solves the input unless both
cuts have exactly one crossing edge and that edge meets the respective
$w_i,w_j$.

Suppose both cuts have this exceptional form. Write the unique crossing
edges as $e_i,e_j$. If they are the same edge, it must be $w_iw_j$, connecting
cells 10 and 01 in the $(i,j)$ split. No matching edge then leaves cell 00.
That 8-vertex cell has exactly one hole, $a$, so it cannot match its seven
other vertices internally. This is a contradiction.

If $e_i\ne e_j$, then $e_i$ cannot cross coordinate $j$, whose unique
crossing edge is $e_j$. Consequently $e_i$ runs from cell 10 to cell 00;
the same reasoning makes $e_j$ run from cell 01 to cell 00. No matching
edge leaves cell 11. That cell has exactly the three holes $b,t,v$, so it
cannot match its five other vertices internally. This is again a
contradiction. Therefore at least one cut satisfies S1D, proving G2D.

## Scope together with G4D

In the 770 normalized residual Q5 hole configurations ($a=0$, unordered
nonadjacent $b,t$, distinct odd forbidden $v$), G4D from
`Q4_CORE_AND_A4_SPLIT.md` covers 255 and G2D covers 120, with intersection
30. Their union therefore covers all matchings in 345 configurations;
425 configurations remain outside these two geometry-only sufficient
conditions. S4D and S1D can additionally handle individual matchings in
that remaining domain when their crossing conditions hold.

These counts are neither matching counts nor a minimal orbit classification.
The full Q5 A4 statement, and hence the unconditional full six-hole P6
reduction, remains open. All other remaining P6 hole levels also remain open.
