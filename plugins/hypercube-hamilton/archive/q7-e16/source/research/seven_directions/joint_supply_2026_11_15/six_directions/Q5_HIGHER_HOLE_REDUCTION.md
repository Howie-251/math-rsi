# Two remaining auxiliary levels suffice for all balanced Q5 endpoints

2026-11-01. ARIS proof-writer. Conditional reduction, not a proof of A8,
A10, or full P6. Independent review pending.

## Claim and notation

For $t\ge1$, let $A_{2t}$ mean: every matching of $K(Q_5)$ with hole counts
$(t-1,t+1)$ has a cycle on precisely $Q_5-v$ for every specified majority
hole $v$, containing the matching and using only short new edges. Either
global parity can be the majority. Full $A_2,A_4,A_6$ are established imports.
The exact additional obligations are $A_8$ (hole counts $3,5$) and $A_{10}$
(hole counts $4,6$), with arbitrary required edges and arbitrary majority v.

If A8 and A10 hold, then:

1. Every feasible $A_{2t}$ holds, with any number of holes.
2. Every matching of $K(Q_5)$ with balanced holes has a Hamilton path from
   any free root to any opposite-parity target, covered or free, containing
   the matching and using only short new edges.
3. Every matching of $K(Q_5)$ with balanced holes has a Hamilton cycle
   extension using only short new edges.

These are conditional auxiliary consequences, not assertions that the
remaining Q6 cut configurations all reduce to these local inputs.

## 1. Finite geometric fact

Every set of five vertices of one parity in $Q_5$ has at least eleven
neighbors. Hence every five vertices of one parity and every six vertices
of the other parity contain a short edge between the sets.

The first statement is a finite assertion on $\binom{16}{5}=4368$ sets
for one parity. `q5_higher_hole_reduction_geometry.py` enumerates those
sets, unions the five coordinate neighbors of each vertex, and records
the full histogram. Its minimum is eleven; translation by a coordinate
unit supplies the other parity. An independent checker must re-enumerate
this small universe before treating the fact as accepted evidence.

## 2. Reduction of every larger avoid-one input

Suppose $t\ge6$ in an $A_{2t}$ instance. There are at least five minority
holes and at least six majority holes other than $v$. Section 1 gives a
short edge between these sets. Add it to the matching; $v$ stays free,
and both hole counts decrease by one. Repeat until $t\le5$. The terminal
instance is covered by A2/A4/A6/A8/A10. Its cycle contains the original
matching, omits precisely $v$, and every added matching edge was short.
Thus it has the required scope relative to the original instance.

## 3. Balanced endpoints and cycles

Let $P_m$ be the endpoint assertion for $m$ holes of each parity, and let
$C_m$ be the corresponding full-cycle assertion. Fink's arbitrary perfect-
matching extension theorem supplies $C_0$.

Inductively assume $C_{m-1}$. For $P_m$, let $r$ be a free root and $y$
an opposite-parity target. If $y$ is free, add the possibly long auxiliary
edge $ry$; apply $C_{m-1}$ to this arbitrary complete-graph matching, then
delete $ry$. All surviving new edges are short.

If $y$ is covered, write $h=F(y)$ and set

$$ F'=(F\setminus\{yh\})\cup\{hr\}. $$

Its holes have counts $(m-1,m+1)$, with the majority parity that of $y$;
$y$ is now free. Apply $A_{2m}$ from Section 2, avoiding $y$. In the
resulting 31-cycle replace the required auxiliary edge $hr$ by $h-y-r$
and delete the temporary edge $yr$. This yields a Hamilton $r$--$y$ path,
restores the original edge $yh$, and removes the only new auxiliary edge.
Thus $P_m$ holds.

To obtain $C_m$, take any free root and any short neighbor as target in
$P_m$, then close that Hamilton path by the short edge between its ends.
This closes the induction. For $m=16$ the matching is empty, so the
covered-target branch (which would call the infeasible A32) never occurs;
the free-target branch uses $C_{15}$. All other covered-target calls have
feasible majority counts at most sixteen.

## 4. Exact new geometry sizes, not matching counts

Normalize the forbidden majority vertex to $0$. For A8, the other majority
holes are four even vertices Z and the minority holes are three odd vertices W.
For A10 the corresponding sizes are five and four. If a short Z-W edge
exists, add it to reduce to the predecessor A theorem without covering 0.

The producer's complete nonadjacent domains have 2700 A8 geometries and
55 A10 geometries. No such domain remains for A12 or larger; the geometric
fact above supplies an analytic explanation for all larger feasible sizes.
These are marked hole configurations, not matchings. Each unresolved
configuration must still be proved for every arbitrary complete-graph matching
on its covered vertices. The separate A8 writer is investigating the 160
geometries without a delta-1/2/3 cut; those transfers and that residual
classification are not imported as proved by this document.

## Status

The implications above are PROVABLE AFTER EXTRA ASSUMPTIONS A8 and A10,
and acceptance of the explicitly finite five-neighbor fact. A8 and A10
remain open. None of the complete 10--18-hole Q6 layers is closed here.
