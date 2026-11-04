# Closing the canonical A4 family by flexible endpoints

Date: 2026-11-01. Proof status at initial writing: complete argument relative
to the listed finite certificates and prior inputs; independent audit pending.
The claim here is full Q5 A4, not full Q6 P6. The 8--18-hole P6 levels remain
open even if this proof and its dependencies are accepted.

## Claim

**A4.** For every matching $F$ of $K(Q_5)$ with exactly four holes of parity
counts 3 and 1, and every prescribed majority-parity hole $v$, there is a
cycle through exactly $V(Q_5)\setminus\{v\}$ containing every edge of $F$,
with all edges outside $F$ short.

By R1A in `A4_SINGLE_GEOMETRY_REDUCTION.md`, it remains to prove the claim
when the holes are $a=0,v=1,b=14,t=22$, with $v=1$ forbidden. That reduction
is already independently reviewed and does not assume A4. Original edges
of $F$ remain completely arbitrary, including same-parity long edges.

## Dependencies

- R1A and its Q4 inputs: `A4_SINGLE_GEOMETRY_REDUCTION.md`,
  `Q4_CORE_AND_A4_SPLIT.md`, with their corresponding audit reports.
- Q4 A4_4 and NC_4 from the latter document. A4_4 is a separately certified
  four-dimensional theorem, not an invocation of the present Q5 A4 claim.
- Complete Q4 avoided-circle tables below, independently verifiable by
  explicit positive circles and exhaustive short perfect completions for
  every negative instance.
- The finite completion accounting below. Its entire search space is
  characterized by inverse maps, not by random sampling of Q5 matchings.

## 1. Complete Q4 two-hole tables

For $h=1,7$, consider every perfect matching of the 14 vertices
$V(Q_4)\setminus\{0,h\}$. A successful instance has a Hamilton circle on
those 14 vertices, containing the matching, with short new edges.

There are $13!!=135135$ instances for each $h$. Each record of
`q4_distance1_avoided_table.bin` or `q4_distance3_avoided_table.bin` contains
the 16-byte mate array and a 14-vertex circle, or an all-255 marker for a
negative instance. `verify_q4_avoided_table.py` checks every matching and
complete bijective rank coverage, as in the preceding Q4 proof package.
It checks every positive circle directly. For a negative, every allowed
vertex already has one required matching edge, so every possible extending
circle must add a short perfect matching disjoint from the required one.
The checker enumerates all such short perfect matchings by matching the
seven even vertices to the seven odd vertices, and verifies that every
union has more than one connected component. Thus the negative judgment
does not rely on the producer's Hamilton search.

| holes | positive | negative | negative with half-layer | negative without half-layer |
|---|---:|---:|---:|---:|
| $0,1$ |135084|51|15|36|
| $0,7$ |135082|53|45|8|

Coordinate permutations take these tables to every pair $0,y$ with $y$ odd.
Let $\mathcal B_y$ denote the corresponding complete set of negative
matchings. The tables and permutations therefore decide the extension
question for every matching with holes $0,y$, for all eight odd $y$.

## 2. A path criterion and its exact inverse

Let $L$ be a matching of $K(Q_4)$ with exactly the holes $0,d$, where
$d\ne0$. For an odd vertex $y\ne d$, write $k=L(y)$ and define

$$T_y(L)=L-yk+dk.$$

This is a matching with precisely the holes $0,y$. If it is not in
$\mathcal B_y$, its certified 14-circle contains $dk$. Delete $dk$ and
append the original edge $ky$, producing a path from $d$ to $y$ on exactly
$Q_4\setminus\{0\}$. The path contains $L$ and all new edges are short.
The edge $ky$ may be long but is an original required edge of $L$.

Conversely, such a path must use $yk$ as its final edge, since $y$ is
covered by $L$. Deleting $y$ and adding $dk$ gives the corresponding
14-circle of $T_y(L)$. The newly added $dk$ is a required edge of $T_y(L)$,
so it need not be short. Thus this criterion is an equivalence.

For fixed $y$ and $d\notin\{0,y\}$ it has an exact inverse. Given
$T\in\mathcal B_y$, let $k=T(d)$ and set

$$L=T-dk+yk.$$

Then $L$ has holes $0,d$ and $T_y(L)=T$. Every bad pair $(L,y)$ is obtained
this way, with no missing matching. The target $y=d$ is separately excluded.

## 3. Finite completion lemma

Let $P$ be any matching on the 15 vertices $Q_4\setminus\{0\}$, with
uncovered vertex set $X$ of odd size $c$. In the intended application $P$
is the internal A matching and $X$ is its crossing-port set.

A completion consists of a root $d\in X$ and a perfect matching $D$ on
$X\setminus\{d\}$. Put $L=P\cup D$, which has exactly holes $0,d$.
There are

$$T_c=c(c-2)!!$$

distinct completions, using $(-1)!!=1$. Call an odd target $y$ available
for that completion when $y\ne d$ and $T_y(L)\notin\mathcal B_y$.

The following exact finite facts hold:

1. Either a completion makes target 7 or 11 available, or $P$ belongs to
   the finite stall class counted below.
2. For a stall with $c=1$ or $c=3$, at least four distinct odd targets are
   available for some completion (the completion may depend on the target).
3. For a stall with $c=5$ or $c=7$, there is a set $G$ of four odd vertices,
   disjoint from $X$, such that **every** target $y\in G$ is available for
   **every** completion, including every choice of root $d\in X$.
4. There are no stalls for $c\ge9$.

Here is the full counting certificate:

| $c$ | $|P|$ | $T_c$ | candidate partials | stall partials | available-target sizes on stalls |
|---:|---:|---:|---:|---:|---|
|1|7|1|256|256|4,5,6|
|3|6|3|1372|210|4|
|5|5|15|3048|42|4, all completions|
|7|4|105|3596|2|4, all completions|
|9|3|945|2366|0|—|
|11|2|10395|808|0|—|
|13|1|135135|84|0|—|
|15|0|2027025|1|0|—|

The last row is included to state the finite lemma on all partial matchings;
the actual canonical Q5 cut has at most 13 crossing edges.

### Why this enumeration is complete

First apply the inverse in Step 2 to the two target tables $\mathcal B_7$
and $\mathcal B_{11}$. The latter is the permutation of $\mathcal B_7$
swapping coordinates 2 and 3. For each of the 53 table entries and each
of its 14 covered vertices $d$, recover $L$, and test the other target.
This gives exactly 256 near-perfect inputs $(d,L)$ for which both fixed
targets are unavailable, among all $15\cdot135135=2027025$ inputs.
The case $d=7$ or $d=11$ is included: that target is unavailable by equality,
and the other is tested. See `a4_single_crossing_exceptions.py/.json`.

For each size $|P|=(15-c)/2$, enumerate all subsets of the 256 seven-edge
matchings $L$, keeping a count of how many bad completions contain each
subset $P$. Any stall must occur in this enumeration: if every completion
is bad, it is a subset of at least one bad completion. Each counted
near-perfect matching has a unique free root $d$ besides 0, so it counts
exactly one of the $T_c$ completions. A partial matching is a stall exactly
when its count is $T_c$. No assumptions about the unenumerated Q5 matching
or its crossing bijection are made.

For each stall, use the inverse of Step 2 for all eight odd targets, with
all 14 possible covered roots $d$ in each negative table entry. Count
those bad near-perfect matchings containing $P$. If $y\in X$, also count
the $(c-2)!!$ completions whose root is $d=y$. The target is available for
some completion precisely when the total bad count is less than $T_c$;
it is available for every completion precisely when the count is zero.
`a4_completion_endpoint_probe.py/.json` performs this accounting and records
every stall, port set, and target count. For all 42 five-port and both
seven-port stalls, the four listed available targets have count zero and
lie outside $X$. These are the quantified properties used below.

## 4. Transfer setup in the canonical Q5 family

Split Q5 on coordinate 0. Let $A$ be the odd integer labels, with the sole
hole $v=1$, and $B$ the even labels, with holes $0,14,22$. Identify each
face with $Q_4$ by $z\mapsto\lfloor z/2\rfloor$. In these local coordinates,
$v$ is 0 in A and the B holes are $0,7,11$.

Write $F_A,F_B$ for internal matchings, $C$ for the crossing matching, and
$X_A,X_B$ for their local port sets. Counting either side gives

$$2|F_A|+c=15,\qquad2|F_B|+c=13,$$

so $c=|C|$ is odd and $1\le c\le13$. Crossing edges may be arbitrary long
required edges. They define a bijection between $X_A$ and $X_B$.

Apply the finite completion lemma to $P=F_A$, $X=X_A$. A completion $(d,D)$
and an available odd target $y$ give a path $W$ on $A\setminus\{v\}$,
from local $d$ to local $y$, containing $F_A\cup D$ and only short new
edges. Delete $D$, attach every original crossing edge of $C$ at its A
port, and attach the short coordinate-0 bridge between the two copies of
$y$. The following two forms of this transfer suffice.

## 5. Safe transfer when $y\notin X_B$

The resulting path family has distinct endpoints $X_B\cup\{y\}$ and
disjoint interiors partitioning $A\setminus\{v\}$. In particular this
remains true if $y\in X_A\setminus\{d\}$: its incident D edge is removed
from the endpoint of $W$, leaving an isolated A vertex; attaching its
original crossing edge and the new bridge turns it into a two-edge path
with distinct B endpoints. Every other component is a path as well. No
cycle can be formed because the attached B endpoints are all distinct.
Compress the paths to a matching $R$ on $X_B\cup\{y\}$.

If $y=7$ or $11$, it is a B hole and $F_B\cup R$ has the two opposite-parity
holes 0 and the other member of $\{7,11\}$. NC_4 gives a full B circle;
expanding $R$ gives the desired 31-circle.

Otherwise $y$ is odd, is not 0,7,11, and is not in $X_B$. It is internally
covered in B. Set $k=F_B(y)$ and $q=R(y)$. The matching

$$L_B=(F_B\setminus\{yk\})\cup(R\setminus\{yq\})\cup\{kq\}$$

has exactly the holes $0,7,11,y$, of parity counts 1 and 3. Apply A4_4
avoiding $y$. Expand $kq$ into the original edge $ky$ followed by the
transferred $y$--$q$ path, and expand the other R edges. This restores $y$
and all of $A\setminus\{v\}$, preserving every original edge and adding
only short edges. Thus the safe transfer is valid.

## 6. Port transfer with a prescribed root

Suppose $c\ge3$, $y\in X_B$, $y\notin X_A$, and a completion is available
with root $d$ equal to the A partner of the original crossing edge at the
B vertex $y$. Its auxiliary matching $D$ is nonempty.

The path $W$ has endpoints $d$ and $y$ in A. Both are outside $V(D)$:
$d$ was excluded in forming D, and $y\notin X_A$. Every edge of D is
therefore internal to this path. Deleting a nonempty D separates its two
original endpoints into different path components. After attachment, the
original crossing edge at $d$ and the new bridge at the other endpoint
meet at the same B vertex $y$. They concatenate two DIFFERENT components
and do not close a cycle. No other attached B endpoints coincide.

The resulting paths have distinct endpoints $X_B\setminus\{y\}$ and
disjoint interiors partitioning $(A\setminus\{v\})\cup\{y\text{ in B}\}$.
Compress them into a matching $R$. Then $F_B\cup R$ has exactly the holes
$0,7,11,y$. The four holes are distinct because $y\in X_B$, and their
parities are again 1 even and 3 odd. A4_4 avoiding $y$ yields a circle on
$B\setminus\{y\}$. Expanding R restores $y$ and all of $A\setminus\{v\}$,
and yields the required 31-circle. Every crossing edge, including the one
at $d$, is an original edge of F and is preserved.

## 7. Every canonical input admits one of these transfers

If a completion makes 7 or 11 available, choose it and that target. These
vertices are B holes and hence outside $X_B$, so Step 5 applies.

Otherwise we are in a finite stall class. For $c=1$ or $c=3$, at least
four odd targets are available for some completions. At most $c\le3$ of
them lie in $X_B$. Choose one outside $X_B$ and a completion making it
available, and use Step 5.

For $c=5$ or $c=7$, use the four-target set G supplied by the finite lemma.
If some $y\in G$ is outside $X_B$, any completion making it available
gives Step 5. Otherwise $G\subseteq X_B$. Choose any $y\in G$, take its
original crossing partner as root $d$, and choose ANY perfect matching D
on $X_A\setminus\{d\}$. The universal zero-bad-count property ensures this
particular root and completion admit target y. Also $y\notin X_A$ and
$D\ne\varnothing$. All hypotheses of Step 6 hold, proving the result.

There are no stalls for $c\ge9$, so the first branch already handles them.
This exhausts the canonical family and proves A4 by R1A.

## Consequence for the actual P6 goal

The previously audited full six-hole reduction
(`SIX_HOLE_MIXED_AND_GEOMETRY.md`, `SIX_HOLE_COVERED_REDUCTION.md`,
`SIX_HOLE_FREE_REDUCTION.md`) has A4 as its remaining input. Once this
closure proof and its finite checks are accepted, that conditional reduction
becomes a proof for all six-hole short matchings of Q6 and all required
free-root/opposite-target endpoint choices.

This is not the whole of P6. The 8,10,12,14,16,18-hole rooted-maximal levels
are still separate unresolved obligations. The user goal must remain active.
