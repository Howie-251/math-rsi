# A8: a sufficient double-bridge criterion controlling the T15 obstruction

Date: 2026-11-01. ARIS proof-writer draft; independent review pending.

## Claim

Let $F$ have the original A8 hole counts and satisfy the residual
nonadjacency condition of `A8_PARTIAL_PROOF_PACKAGE.md`. Take a coordinate
face $A$ containing the forbidden majority hole $v$ and two distinct holes
$t,s\ne v$. Let $B$ be the other face and put $w=\bar t,z=\bar s$.
Assume:

1. The vertices $w,z$ are covered by $F$.
2. Removing $t,s$ from the original $A$ holes leaves majority excess two.
3. The original $B$ holes together with $w,z$ consist of one singleton
   parity hole $a$ and five holes of the other parity; $w,z$ belong to
   that five-hole class.

The graph criterion in Step 2 below suffices for the A8 conclusion.

## Status

**PROVABLE AS STATED**, relative to GQ4-avoid and the Q4 T15 classification.
This is a sufficient criterion, with no claim that all remaining matching
instances satisfy it. In particular, a fixed original edge between the
two remaining neighbors of $a$ may prevent its use.

## Notation, assumptions, and dependency map

Use $F_A,F_B,C,c,X_A,X_B$ as in the partial package. Put
$T=X_A\cup\{t,s\}$ and $d=|T|/2$. Assumption 2 implies $|T|$ is even.
GQ4-avoid is used on $A-v$. The exact Q4 T15 classification in
`Q4_T15_CLASSIFICATION.md` is used on $B$ avoiding $w,z$. The argument
does not assume T15 is universally positive.

## Proof strategy and proof

### Step 1. A graph recording the part outside the target face

Define $G$ with edges

$$F_B\cup C\cup\{tw,sz\}$$

and include its isolated original $B$ holes. The $A$ vertices of $G$
are exactly $T$, each of degree one. Every covered $B$ vertex except
$w,z$ has degree one; $w,z$ each have degree two. Thus every nontrivial
component is a path: a cycle could use only degree-two vertices $w,z$,
but $G$ is simple and has no cycle on two vertices. There are no repeated
edges here, since $t,s$ are original holes and the original matching has
no edge incident to them.

Each component with both endpoints in $T$ gives an artificial edge on
its two endpoints. These edges form a matching $P$ on $T$. There are at
most two such components. Indeed each must contain $w$ or $z$, because
all other $B$ vertices have degree one. Each other component meeting $T$
has a unique endpoint in $B\setminus\{w,z\}$; call that endpoint a
terminal, and call its unique corresponding vertex of $T$ its root.

### Step 2. The sufficient criterion

If at least one of $w,z$ is not adjacent to $a$ in $B$, set $J=P$.
Otherwise let $p,q$ be the two neighbors of $a$ in the $Q_4$ face $B$
other than $w,z$. Require

$$pq\notin F_B.\tag{1}$$

If both $p,q$ are terminals of components meeting $T$, let their roots
be $u,r$ and set $J=P\cup\{ur\}$. Otherwise set $J=P$.
The roots of terminal components are disjoint from all endpoints of
$P$, so $J$ is a matching in all cases. The sufficient criterion is

$$d>|J|.\tag{2}$$

This criterion is inspectable from $F$ and the selected bridges without
searching for any $A$-face cycle. In the case where (1) is needed,
$c\ge6$ implies (2), because $d=(c+2)/2\ge4$ and $|J|\le3$;
the condition (1) is still required even for such large $c$.

### Step 3. Choice of the target-face cycle

Complete $J$ to a perfect matching $D$ on $T$. By assumption 2 the
matching $F_A\cup D$ has hole excess two, with $v$ in its larger class.
GQ4-avoid gives a cycle $K$ on $A-v$ containing $F_A\cup D$.
Delete $D$. The resulting path forest pairs the vertices of $T$ by a
matching $S$, where an edge of $S$ stands for an entire remaining path
of $K$. As a multigraph, $S\cup D$ is one cycle: it is obtained by
contracting those paths in the original cycle. This remains true when
$d=1$, in which case its two edges are parallel.

Since $P\subseteq J\subset D$ and $|J|<d$, the multigraph
$S\cup P$ contains no cycle. Otherwise it would already contain the
unique cycle of $S\cup D$, forcing every edge of $D$ to belong to $P$.
Consequently attaching $G$ to the uncompressed $A$ paths produces no
closed component. Its nontrivial components are paths with endpoints
in $B\setminus\{w,z\}$ and interiors containing all of $A-v$ and both
$w,z$. Compress them, retaining isolated original $B$ holes, to a matching
$L$ on $B$ with hole set exactly $H_B\cup\{w,z\}$.

### Step 4. Excluding the T15 obstruction

If at least one of $w,z$ is not a neighbor of $a$, the T15 obstruction
does not hold, independent of $L$, so proceed to Step 5.

In the other case, the T15 obstruction is exactly $pq\in L$.
The vertices $p,q$ are original covered vertices: they cannot be original
$B$ holes because every original hole of their parity is nonadjacent to
the singleton opposite-parity original hole $a$, by residual
nonadjacency. They are not $w,z$, so each has degree one in $G$.

A component of $G$ with both endpoints in $B$ is a single edge of $F_B$:
any longer such path would require traversing $w$ or $z$, whose other
incident bridge leads to an endpoint in $T$. Thus, if $p$ or $q$ belongs
to a component not meeting $T$, it remains paired with its original
partner in $L$. Condition (1) then prevents $pq\in L$.

It remains to consider the case where $p,q$ are both terminals with
roots $u,r$. Here $ur\in J\subset D$. If expansion and compression
produced an edge $pq\in L$, the portions between roots would give an
$u$--$r$ path in $S\cup P$. Adding the edge $ur$ gives a cycle in
$S\cup P\cup\{ur\}$. But $P\cup\{ur\}=J$ is a proper subset of $D$
by (2), so this multigraph is a proper subgraph of the single cycle
$S\cup D$ and cannot contain a cycle. This contradiction proves
$pq\notin L$.

### Step 5. Completion

Assumption 3 gives exactly the hole pattern of Q4 T15, with avoided
holes $w,z$. Step 4 excludes its necessary and sufficient obstruction,
so T15 gives a simple cycle on $B\setminus\{w,z\}$ containing $L$.
Expand all its compressed edges. The expanded paths restore every
vertex of $A-v$, both bridge vertices, and every original edge of $F$,
and all other edges used are short. The result is the desired cycle on
$Q_5-v$.

## Corrections or missing assumptions

The criterion is not necessary. Its failure is not a counterexample to
A8 or to other choices of bridges or cuts. In particular $d=|J|$ only
blocks this method of keeping a spare gap; it does not rule out a more
flexible target-face construction.

## Open risks

This proof is unreviewed. It has not been used to count or close the
remaining four A8 residual orbits. Universal coverage would require an
additional argument over all arbitrary matchings, or a complete finite
positive certificate package for the cases left by this criterion.
