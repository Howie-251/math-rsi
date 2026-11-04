# T15 same-face positive-crossing progress

Date: 2026-11-01. Proof-writer package. Assurance: same-family/provisional;
no global closure ledger changed. The unrestricted T15 and P6 remain open.

## Claim and status

**PROVABLE AS STATED, conditional on the audited Q4 theorems imported below:**
Let $F$ be an arbitrary complete-graph matching on $V(Q_5)$ whose six
uncovered vertices all lie in a coordinate face $A$, with one minority
hole $a$ and five majority holes $H$. Fix distinct omitted holes $v,w\in H$.
Write $B$ for the other face, $C$ for the required crossing edges, and
$c=|C|>0$. Identify both faces with the same $Q_4$ by deleting the cut
coordinate. Then a 30-cycle omitting exactly $v,w$, retaining every edge
of $F$, and using only short edges outside $F$, exists under either of:

1. A completion $D$ pairing the crossing ports in $A$ exists such that
   $F_A\cup D$ does not have the Q4 forced-triangle obstruction.
2. There is no usable minority-majority adjacent hole pair, the two
   omitted holes neighbor $a$, $N_A(a)-\{v,w\}=\{p,q\}$, and the A crossing
   port set is exactly $\{p,q\}$ (so $c=2$).

This document also proves an exact reduction: after the imported adjacent
hole augmentation and the already proved zero-crossing case, every
same-face input not covered above has $pq\in F_A$ and $c\in\{2,4,6,8\}$.
Those remaining fixed-$pq$ cases are **NOT CURRENTLY JUSTIFIED** here.

## Assumptions, notation, and dependencies

A short edge has XOR a coordinate unit; required edges may be long and
same-parity. $F_A,F_B$ are the internal restrictions, $X_A,X_B$ are the
crossing port sets, and $C$ is an arbitrary bijection $X_A\to X_B$.
Because there are ten covered A vertices, $c$ is even and $2\le c\le10$.
The number of B ports is the same, and $F_B$ covers exactly their complement.

Imports are the audited exact theorem in `Q4_T15_CLASSIFICATION.md`,
Q4 complete-perfect-matching Hamilton-cycle extension (Fink), the audited
complete distance-3 opposite-hole table `q4_distance3_avoided_table.bin`,
and T44_5 for the adjacent usable-hole augmentation. The opposite-hole
table has $135135$ matchings, $135082$ positive circles, and exactly $53$
negative matchings. Its exhaustiveness and negative correctness are
imported from `Q4_PERFECT_ENDPOINT_ABUNDANCE.md` and its independent audit;
the present script does not independently re-prove that import.

Dependency map: Q4 T15 and Fink imply Claim 1; finite A positive paths
and exhaustive Q4 opposite-hole negatives imply Claim 2; elementary
pairing selection gives the remaining-case reduction. No T15 or P6
conclusion is imported into its own proof.

## Proof 1: safe completion

Take such a $D$. The Q4 T15 theorem gives a 14-cycle on
$A-\{v,w\}$ containing $F_A\cup D$. Delete $D$ and attach every original
crossing edge. Since $c>0$, $D$ is nonempty, so deleting it cuts the circle
into disjoint paths. Their B endpoints are precisely $X_B$, each occurring
once, and their interiors partition all 14 retained A vertices. Contract
these paths to a matching $R$ on $X_B$. Then $F_B\cup R$ is a perfect
matching on $B$. Fink gives a Hamilton 16-cycle through it. Expand $R$.
The expansion is a single simple circle: its contracted circle is simple,
and path interiors are disjoint and outside B. It has $16+14=30$ vertices.
All artificial D edges were deleted; all R edges were expanded; all
remaining new edges are short. All original matching edges remain.

## Proof 2: normalize the two-port triangle residual

If an available hole $b\in H-\{v,w\}$ neighbors $a$, add the short edge
$ab$ and apply T44_5 to its four remaining same-parity holes, omitting
$v,w$. Thus assume that no such $b$ exists.

A common XOR translation and coordinate permutation on both faces put
$a=0$ and the three available majority holes at $7,11,13$. The omitted
pair lies in one of the four complete orbit representatives
$(1,2),(2,4),(1,14),(2,14)$, as proved in the imported Q4 classification.
A triangle obstruction is possible only for the first two. For $(1,2)$,
$(p,q)=(4,8)$; for $(2,4)$, $(p,q)=(1,8)$. Claim 2 assumes the A ports
are $p,q$. The artificial completion is the single edge $pq$; the original
$F_A$ is a perfect matching of the other eight nonhole vertices. Hence
there are exactly $7!!=105$ possible original A matchings per representative.

For every one of those $210$ inputs, for every
$z\in D_3=\{7,11,13,14\}$, and for either choice of $p$ or $q$ as the first
endpoint of $pq$ encountered from 0, the new finite certificate contains
a simple 14-vertex $0$--$z$ path through $F_A\cup\{pq\}$, omitting
exactly $v,w$ and using only short new edges. The script generates all
$105$ matchings directly by pairings and validates all $1680$ positive
paths. Failed DFS queries are never used to justify a negative result.

## Proof 3: exact B compression and lifting

Let $u=C(p)$, $t=C(q)$, and choose one certified A path. Orient its
artificial $pq$ edge so that its root-side port has B partner $u$ and
its endpoint-side port has B partner $t$ (the other orientation exchanges
$u,t$). Delete $pq$, attach the two required crossings, and add the two
short bridges $0_A0_B,z_Az_B$. The two resulting A excursions have B
endpoint pairs $(0,u)$ and $(z,t)$. Their interiors partition the 14 A
vertices. Treat these excursions as two separate abstract edges.

On B form the multigraph consisting of $F_B$ and those two excursion
edges. Every vertex except $0,z$ has degree one, and $0,z$ have degree
two, unless an excursion forms a degenerate loop or a closed component.
Reject a choice if its degree conditions fail or any component is a
circle. Otherwise contract each path component to its endpoint pair,
obtaining a seven-edge matching $T$ with holes $0,z$.

A positive table circle for $T$ on $B-\{0,z\}$ expands to a single
30-circle containing $F_B$, all A path edges except artificial $pq$,
both original crossings and both bridges. Its distinct path interiors
restore exactly $0_B,z_B$ and the 14 A vertices. This proves simplicity,
connectedness, exact support and original-edge retention. The program
uses edge-labelled multigraphs so parallel edges and loops cannot be
silently mistaken for valid path components.

## Proof 4: why only 6360 B candidates suffice

There are $\binom{16}{2}=120$ possible unordered B port sets $Y$.
Fix $z\in D_3-Y$, and order $Y=(u,t)$ with $u\ne0$. Such a choice always
exists. Because both A directions are available, this order imposes no
restriction on the actual crossing bijection.

For this initial choice the B graph in Proof 3 is always a path forest.
If $0\in Y$ then $t=0$ and the two excursions concatenate; otherwise
$0,z$ are internally matched. The following inverse is unique for every
matching $T$ with holes $0,z$. Write $m$ for its mate map.

* If $t=0$, put $b=m(u)$ and
  $F_B=T-\{ub\}+\{zb\}$.
* If $t\ne0$ and $m(u)=t$, put
  $F_B=T-\{ut\}+\{0z\}$.
* If $t\ne0$ and $m(u)\ne t$, put $a=m(u),b=m(t)$ and
  $F_B=T-\{ua,tb\}+\{0a,zb\}$.

These exhaust respectively the original cases $0\in Y$, $F_B(0)=z$,
and $F_B(0)\ne z$. The formulas produce a matching whose exact holes
are Y and invert the compression. Therefore, if the initial T is not
one of the 53 audited negatives, it is positive immediately. Every
remaining original $F_B$ belongs to the inverse images of those 53
negatives. No failed original input can lie outside this finite set.

For each Y the script generates exactly 53 inverse candidates, hence
6360 candidates in total. It tests the four choices of z and both
orders of Y with the exact multigraph compression from Proof 3.
Every candidate has a positive compressed circle; its explicit circle
is saved and checked for exact support, all required edges, and
shortness of every new edge. The output saves all candidates and one
successful choice per candidate. This is an exhaustive negative-inverse
argument for all $135135$ B matchings per port set, not a sample of them.
Combining with the 1680 A witnesses proves Claim 2. Undo the shared
cube automorphism to get the original labelled statement.

## Proof 5: precise remaining cases

For a fixed normalized geometry let $p,q$ be the two nonomitted root
neighbors. The obstruction requires $pq\in F_A\cup D$.
If $pq\notin F_A$ and the two vertices are not both ports, this cannot
hold for any D. If they are both ports and $c\ge4$, pair p with a third
port and q with a fourth, then pair the remaining ports arbitrarily.
This gives $pq\notin D$. If $c=2$, the only forced artificial obstruction
is $X_A=\{p,q\}$, closed in Proofs 2--4. Consequently the sole remaining
positive-crossing obstruction has $pq\in F_A$. Since that edge consumes
two of the ten covered A vertices, $c\le8$. Thus the exact remaining
crossing counts are $2,4,6,8$, with fixed $pq$. They are not proved here.

## Reproduction and open risks

Run `D:/anaconda/python.exe research/six_directions/t15_sameface_positive_c2_check.py`.
It writes `t15_sameface_positive_c2_certificates.json`, with all 210 A
inputs, 1680 positive A paths, 6360 B inverse candidates, their positive
B compressed circles, and input/script hashes. The present proof package
has not received an independent semantic review. Its finite proof is
conditional on the stated imported table's audited completeness.

Diagnostic only: `t15_sameface_positive_probe_extended.py` explores
$c=2$ with $pq\in F_A$ and an artificial pair elsewhere. Some A direction
patterns leave 105 B candidates unresolved by this particular construction.
Those are obstructions to this method, not T15 counterexamples. No claim
about those original inputs follows from the diagnostic failure.

A second implementation, `t15_sameface_positive_c2_independent_check.py`,
reads the saved certificates without importing the producer or DFS. It
independently generates all A inputs and every B negative inverse set,
then verifies exact coverage, 1680 positive A paths and all 6360 positive
B compressed circles. Its JSON reports PASS. This remains a same-agent,
same-family computational cross-check; it is not an independent semantic
review or an independent proof of the imported table's completeness.
