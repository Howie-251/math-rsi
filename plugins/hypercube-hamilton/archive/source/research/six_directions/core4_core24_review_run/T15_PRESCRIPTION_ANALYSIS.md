# T15 prescription analysis: exact equivalence and universal factors

Date: 2026-11-01. Local proof package; no project-wide status is changed.

## Claim

The original T15 statement remains: for every matching $F$ of $K(Q_5)$
with holes $\{a,x,y\}\cup B$, where $a$ is even and $x,y$ and the three
members of $B$ are odd, there is a cycle on $Q_5-\{x,y\}$ containing $F$
and having only short edges outside $F$. Original matching edges may have
arbitrary length and parity.

This package proves three narrower statements:

1. For every eligible ordered pair $(y,z)$, with $z\in B$ and
   $d(y,z)=2$, and every $p\in N(y)\cap N(z)$, the A4 cycle prescription
   is exactly equivalent to a T15 cycle with the extra prescribed edge $pz$.
2. In the preprocessed case $N(a)\cap B=\varnothing$, each one of these
   prescriptions has a spanning simple cycle factor, uniformly for all $F$.
   The factor need not be connected.
3. T44_5 gives a Hamilton $a$--$z$ path on $Q_5-\{x,y\}$ for every
   $z\in B$, preserving $F$. A precisely oriented local pattern suffices to
   close one such path.

## Status

**PROVABLE AS STATED** for Claims 1--3, relative to the explicitly imported
CF1 and T44_5 below. The universal connected prescription and full T15 are
**NOT CURRENTLY JUSTIFIED**. No strict counterexample to either is claimed.

## Assumptions and notation

$N(v)$ denotes the five short neighbors of $v$. A cycle factor is a simple
spanning 2-regular graph, possibly disconnected. A prescribed new edge must
be short; an original edge in $F$ need not be short.

The preprocessed case is sufficient for T15: if $az$ is short for some
$z\in B$, apply T44_5 to the matching $F+az$, whose holes are the other
four odd holes, avoiding $x,y$. The added edge is short.

The roles of $x,y$ can be exchanged. The elementary geometry proved in
`T15_EDGE_PRESCRIPTION_REDUCTION.md` guarantees at least one eligible
ordered pair: at most two vertices of a fixed parity can be at distance
four from both $x$ and $y$, whereas $|B|=3$.

## Proof strategy and dependency map

1. Suppress or expand one degree-two vertex to prove an exact equivalence.
2. Import CF1 from `A4_SPANNING_FACTOR.md`, audited in
   `A4_FACTOR_REVIEW.md`, then apply the same suppression to its factors.
   CF1 depends on a complete 65,535-subset geometry certificate and a
   matching-independent Hall loss bound. It is a universal statement about
   arbitrary complete-graph matchings, rather than a matching sample.
3. Import T44_5 from `T44_Q5_CLOSURE_DRAFT.md`, with its accepted scope
   recorded in `T44_Q5_CLOSURE_REVIEW.md`. Delete one auxiliary edge.

Neither the proofs below nor these dependencies import full P6.

## Proof

### 1. Fixed-prescription equivalence

Fix an eligible $(y,z,p)$ and put $L=F+yz$. Its four holes are $a,x$ and
the other two members of $B$. The following statements are equivalent:

* There is a 31-cycle $C$ on $Q_5-x$ containing $L$ and $yp$, with every
  edge outside $L$ short.
* There is a 30-cycle $D$ on $Q_5-\{x,y\}$ containing $F$ and $pz$, with
  every edge outside $F$ short.

In the forward direction the two edges at $y$ are exactly $yz,yp$. Replace
the path $z,y,p$ by the edge $zp$. Because $C$ is one cycle of length 31,
$zp$ cannot already be an edge of $C$: otherwise $p,y,z$ would themselves
form the entire cycle. Suppression gives a simple cycle of length 30.
The edge $zp$ is short by the choice of $p$, and every edge of $F$ remains,
since $y,z$ were holes of $F$.

In the reverse direction replace $zp$ in $D$ by $z,y,p$. The new vertex
$y$ was absent from $D$, so expansion produces a simple 31-cycle. The
only newly introduced edges are the required edge $yz$ of $L$ and the
short edge $yp$. These two operations are inverse.

Thus even the fixed-$p$ strong prescription is a concrete optional-edge
extension question on the original T15 target graph. The weaker sufficient
global obligation is exactly

$$\forall F\ \exists (y,z,p)\ \exists D:
\quad z\in B,\ d(y,z)=2,\ p\in N(y)\cap N(z),\quad pz\in E(D),$$

where the ordered forbidden vertex $y$ may be either member of the
specified avoided pair. Replacing the two existential choices by universal
quantifiers is a stronger assertion, not a consequence of this reduction.

### 2. Each fixed prescription has a simple spanning cycle factor

Assume $N(a)\cap B=\varnothing$. Fix *any* eligible $(y,z,p)$.
For $L=F+yz$, its two nonforbidden majority holes are the two members of
$B-\{z\}$, and neither is adjacent to $a$. Thus it falls in the
nonadjacent branch required by CF1. The edge $yp$ is an allowed short edge
outside $L$: $y$ is matched only to $z$ in $L$, and $p$ has opposite parity.
CF1 therefore gives a simple spanning 2-factor $J$ on $Q_5-x$ containing
$F+yz+yp$.

Here $p\ne a$, since $p$ is adjacent to $z\in B$. Consequently $p$ is
covered by $F$. It already has its $F$ edge and the edge $py$ in $J$.
There cannot be an edge $pz$ in $J$: it would give $p$ degree three,
because $pz\notin F$ as $z$ is a hole of $F$. Hence $y$ is not in a
triangle of $J$. Suppressing $y$ produces a **simple** spanning 2-factor
$J'$ on $Q_5-\{x,y\}$ containing $F+pz$. It preserves the number of
components. Expansion is inverse, also on factors under these hypotheses.

This proves the universal quantification

$$\forall F\ \forall (y,z,p)\ \exists J':
\quad J'\text{ is a simple spanning 2-factor containing }F+pz.$$

It proves neither that one such factor is connected nor that an arbitrary
chosen factor can be merged. In particular Hall feasibility of the
prescribed edge is already settled; the remaining issue is connectedness.

The exclusion of a triangle above matters: without preprocessing one can
have $p=a$, which has no required $F$ edge. A general factor could then
contain the triangle $p,y,z$; suppressing $y$ would create a doubled edge.
The cycle equivalence in Step 1 is valid without preprocessing because a
31-cycle cannot have a separate triangle component.

### 3. Exact form of the remaining completion problem

Still assume preprocessing. For any target factor $J'$ put $H=J'-F$.
The new degree is two at the four included holes $a$ and $B$, and one at
every covered vertex. These four holes are independent in the cube:
members of $B$ have the same parity, and none is adjacent to $a$.
Every component of $H$ containing a hole is therefore a two-edge path
centered at that hole. Its two ends are covered vertices and have degree
one in $H$. These four paths are disjoint. The remaining 18 covered
vertices are nine isolated edges of $H$.

Thus $H$ always consists of exactly four two-edge paths and nine single
edges, with 17 short edges in total. The completion problem can equivalently
be stated as choosing these paths and edges, disjoint from $F$, such that
$F\cup H$ is connected; under a fixed prescription, require $pz\in H$.

Contracting the 13 edges of $F$ gives a 2-regular multigraph on 17 vertices
(the 13 contracted pairs and the four holes). It has no loops, since $H$
avoids $F$, but it may have parallel edges. Connectivity of this
multigraph is exactly connectivity of $J'$. CF1 establishes that at least
one such completion exists for every eligible prescribed $pz$; it supplies
no connectivity conclusion about this multigraph.

### 4. T44 supplies every hole-to-hole Hamilton path

Fix $z\in B$ and add the auxiliary edge $az$ to $F$. This is a matching
whose holes are the four odd vertices $x,y$ and $B-\{z\}$. T44_5 gives a
30-cycle on $Q_5-\{x,y\}$ containing $F+az$. Delete $az$ to obtain a
Hamilton path from $a$ to $z$ containing $F$, with every new edge short.
The edge $az$ need not be short: it was prescribed as an auxiliary matching
edge and is deleted before the path is used. This proves the assertion for
every choice of $z$, including the preprocessed case.

For completeness, a precise one-rotation sufficient condition is as follows.
Orient such a path $P$ from $a$ to $z$. Suppose consecutive vertices $v,w$
occur in this order, $vw\notin F$, and the following adjacency conditions
hold:

$$v\in N(z),\qquad w\in N(a).$$

Then delete $vw$ and add $vz,wa$. The two resulting path components have
endpoints $a,v$ and $w,z$. The new edges join $v$ to $z$ and $w$ to $a$,
so their union is one spanning cycle. Both new edges are short and the
deleted edge is outside $F$. This closes T15 for that particular path.

The order $v,w$ is essential. If the order is $w,v$, the same operation
closes each path component separately and yields two cycles. No argument
here proves that a path with the required ordered pattern always exists.

## Corrections or missing assumptions

There is no new universal connected-prescription proof in this package.
The exact missing lemma is that, for every preprocessed T15 matching $F$,
at least one eligible prescribed $pz$ admits a **connected** completion
$F\cup H$ of the form in Step 3. Requiring this separately for every
eligible $p$ is a potentially unnecessary strengthening.

## Open risks

* The factor result imports CF1's complete finite geometry certificate;
  it is not presented as a purely analytic proof of that certificate.
* T44_5 is imported at its audited scope for arbitrary $K(Q_5)$ matchings.
* The ordered rotation criterion is sufficient only. Failure of this
  criterion for some chosen path would not refute T15.
* Full T15, the connected A4 optional-edge strengthening, and full P6
  retain their previous open status.
