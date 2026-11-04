# A8: three-bridge sufficient criterion for a delta-minus-one cut

Date: 2026-11-01. ARIS proof-writer draft; fresh independent review pending.

## Claim

Let $F$ be an A8 matching with forbidden majority hole $v$, satisfying
the usual residual nonadjacency condition. Suppose a coordinate face
$A$ containing $v$ has exactly three minority holes $t_1,t_2,t_3$ and
two majority holes. Thus its imbalance is $-1$, and the other face $B$
has three majority holes and no minority holes. Put $w_i=\bar t_i$.
All three $w_i$ are covered and have majority parity. The criterion
below suffices to extend $F$ to the required cycle on $Q_5-v$.

## Status

**PROVABLE AS STATED**, relative to GQ4-avoid and the new finite T63
classification `A8_Q4_T63_CLASSIFICATION.md`, which is itself pending
fresh independent review. No remaining orbit is claimed to satisfy
the criterion universally.

## Notation, assumptions, and dependency map

Use $F_A,F_B,C,c,X_A,X_B$ as before. Here $c$ is odd because $A$ has
five holes. Let $T=X_A\cup\{t_1,t_2,t_3\}$ and
$d=|T|/2=(c+3)/2$. Define

$$G=F_B\cup C\cup\{t_1w_1,t_2w_2,t_3w_3\}.$$

The $A$ vertices are exactly $T$, of degree one. Only the three bridge
vertices $w_i$ have degree two in $B$. Every such vertex is incident
to a bridge ending in $T$; consequently every component of $G$ is a
path. A cycle could not visit any bridge vertex without also visiting
a degree-one endpoint. All other $B$ vertices have degree at most one.

Let $P$ be the matching on $T$ given by the components of $G$ with
both endpoints in $T$. Each consumes at least one bridge vertex, so
$|P|\le3$. A component meeting $T$ with other endpoint in $B$ has
that endpoint as its terminal and its $T$ endpoint as its root.

## Proof strategy and criterion

If the three avoided vertices $w_1,w_2,w_3$ have no common short neighbor
in the face $B$, set $J=P$. Otherwise their common short neighbor $a$
is unique. Indeed two same-parity vertices of $Q_4$ have at most two
common neighbors, so two different common neighbors cannot have three
distinct common neighbors $w_i$. Let $b$ be the fourth neighbor of $a$
in $B$, the unique neighbor not among $w_1,w_2,w_3$.

If $b$ is an original $B$ hole, again set $J=P$; the edge $ab$ cannot
belong to the compressed matching because $b$ remains a hole. Otherwise
require $ab\notin F_B$. If both $a,b$ are terminals of components of
$G$ meeting $T$, with roots $u,r$, set $J=P\cup\{ur\}$. In all other
cases set $J=P$.

The sufficient criterion is

$$d>|J|.$$

Here $J$ is a matching: roots of terminal components are distinct and
are not endpoints of $P$. In particular, when an obstruction edge is
possible and absent from $F_B$, every cut with $c\ge7$ satisfies this
criterion because $d\ge5$ and $|J|\le4$.

## Proof

Complete $J$ to a perfect matching $D$ on $T$. The holes of
$F_A\cup D$ are just the two original majority holes in $A$, including
$v$. GQ4-avoid gives a cycle $K$ on $A-v$ containing this matching.
Deleting $D$ gives a path matching $S$ on $T$ with $S\cup D$ a single
cycle after the paths are contracted. The graph $S\cup J$ has no
cycle, since $J$ is a proper subset of $D$. Attaching $G$ to the $A$
paths therefore produces a path forest with all endpoints in
$B\setminus\{w_1,w_2,w_3\}$. Compressing gives a matching $L$ on $B$
with exactly six majority-parity holes: the three original $B$ holes
and the three bridge vertices.

The T63 classification says that this matching has a cycle avoiding
$w_1,w_2,w_3$ unless it contains $ab$ for the unique possible $a,b$
above. When no common $a$ exists, no obstruction exists. If $b$ is an
original hole, $ab\notin L$ because $b$ is free in $L$.

In the remaining case $a,b$ are original covered nonbridge vertices of
$B$. Each has degree one in $G$. Every component of $G$ with both
endpoints in $B$ is an original edge of $F_B$: any longer path would
have to pass through a bridge vertex and then end in $T$. If one of
$a,b$ is in such a component, its original partner remains its partner
in $L$, and $ab\notin F_B$ excludes the obstruction.

If both are terminals rooted at $u,r$, an edge $ab\in L$ would yield
an $u$--$r$ path in $S\cup P$. Together with $ur\in J$, it would form
a cycle in $S\cup J$, contradicting its acyclicity. Therefore the
compressed matching has no T63 obstruction. Take its T63 cycle,
expand all paths, and restore each bridge vertex and all of $A-v$.
The resulting cycle contains every original required edge and all
new edges are short. This proves the sufficient claim.

## Application and remaining finite obligations

For the fourth residual representative of the original census,

$$v=0,\quad Z=\{15,23,27,29\},\quad W=\{1,2,4\},$$

the cuts at bits $8$ and $16$ both have the required $A$ hole counts.
Their bridges, common neighbor, and possible obstruction edge are:

| cut bit | bridge vertices in $B$ | common neighbor $a$ | fourth neighbor $b$ |
|---|---|---:|---:|
| $8$ | $9,10,12$ | $8$ | $24$ |
| $16$ | $17,18,20$ | $16$ | $24$ |

The two fixed obstruction edges $8\,24$ and $16\,24$ cannot both
belong to the original matching. Therefore at least one of these cuts
has no fixed obstruction. If that cut has at least seven crossings,
the criterion proves the A8 conclusion. It follows that an instance
left by both sufficient tests must have a cut with no fixed obstruction
and at most five crossings. This is a rigorous reduction to small
crossing counts, not a proof that they are all extendable.

## Open risks

The T63 classification and this transfer await independent review.
Cases with $c=1,3,5$ and $d\le|J|$ can require other bridges, other
cuts, or a finite local certificate package. No large matching census
has been run and no full orbit closure is asserted.
