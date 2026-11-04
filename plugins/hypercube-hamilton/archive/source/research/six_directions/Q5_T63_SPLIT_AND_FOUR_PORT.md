# Q5 T63: strict split criteria and the four-port interface

2026-11-01. ARIS proof-writer producer package; independent checker review
is required before acceptance. Existing accepted proofs and ledgers are
unchanged. Full Q5 T63, full ten-hole Q6 and full P6 remain OPEN here.

## Claim and status

The original target T63_5 is: for every arbitrary matching F of K(Q5)
with six holes H of one parity and every prescribed U subset H of size
three, there is a simple 29-cycle on exactly Q5-U containing F and using
only short new edges.

**Original target: NOT CURRENTLY JUSTIFIED.** No verified counterexample
to T63_5 has been found. The following strict sufficient statements and
four-port gluing lemma are **PROVABLE AS STATED relative to their listed
Q4 imports**. The tempting universal one-edge zero-crossing gluing claim
is false; an explicit finite local counterexample and its positive
four-bridge repair are supplied below. This does not refute T63_5.

## Assumptions, notation and dependency map

A coordinate cut has faces A and B. Write F_A,F_B for the original
internal matching edges, C for the original arbitrary crossing edges,
c=|C|, and X_A,X_B for their endpoints. Original matching edges may be
long or join equal parities. A short mirror identification gives the same
four-bit labels to A and B. Thus equal labels are connected by short
bridges. New-edge optionality always means exclusion from the relevant
original face matching; required edges cannot be deleted.

A good split means |H intersect A|=2, |U intersect A|=1 and consequently
|H intersect B|=4, |U intersect B|=2, allowing A,B to be exchanged.
The imported local theorems are accepted Q4 N14 (two same-parity holes,
omit one), Q4 T44 (four same-parity holes, omit two), and the optional
N14 lower-bound certificates accepted by Q4_RICH_GLUING_REVIEW. All permit
arbitrary complete-graph required matchings. The sufficient proof DAG is
these Q4 inputs -> positive-crossing transfer / zero-crossing interface
-> matching-specific T63_5 sufficient conditions. The common-cell parity
argument additionally gives a hole-only universal family. No Q5 A8 or
unproved T63_5 is imported into that chain.

## 1. Positive-crossing good split

**Theorem 1.** A good split with c>0 suffices for the original T63_5
conclusion for this F.

The identity 2|F_A|+c=16-2 implies c is even, so c>=2. Choose a perfect
matching D on X_A. The matching F_A union D has exactly the two original
same-parity holes in A. N14 gives a cycle K_A on A minus its sole marked
omission, containing F_A union D and using only short new edges. Delete
the nonempty matching D. The remaining components are paths with distinct
endpoints X_A, and their interiors partition the other A vertices.
Attach each actual original crossing edge at its A endpoint. Distinct
crossing endpoints give a path forest with endpoints X_B. Compress its
components to a matching R on X_B.

F_B union R is a matching: X_B consists of crossing ports and is disjoint
from F_B's covered vertices. Its holes are precisely the four original
holes in B, of the same parity. T44 supplies a cycle K_B omitting exactly
the two marked B holes and containing F_B union R. Expand every R edge
to its transferred path. These paths have disjoint interiors, and all A
vertices except its marked omission are restored exactly once. The result
is one simple cycle with 15+14=29 vertices, containing every edge of F.
The artificial D edges are gone and compressed edges are expanded; all
surviving new edges are local cube edges. This proves Theorem 1.

## 2. A hole-only universal family from common-cell parity

Let I be the set of all good split coordinates. Partition Q5 by the bits
in I, calling the resulting induced subcubes common cells.

**Theorem 2.** If some common cell contains an odd number of covered
vertices of F, then T63_5 holds for every arbitrary matching with the
marked geometry (H,U).

If no matching edge crossed any coordinate in I, every matching edge
would remain inside one common cell. Its covered vertices would therefore
occur in disjoint pairs in that cell, forcing their number to be even.
An odd cell contradicts this. Consequently some good split has c>0;
Theorem 1 applies. The condition depends only on (H,U), not on the
required matching. Equivalently, a cell of even size has odd covered
count exactly when its hole count is odd. When all five coordinates are
in I the cells are singletons; use covered count directly (a covered
singleton itself is an odd cell).

The producer geometry census covers all binomial(16,6)*binomial(6,3)
=160160 even-hole marked geometries under the 1920 parity-preserving Q5
automorphisms. It finds 135 orbits, 42400 geometries satisfying this
universal sufficient criterion, 91360 other geometries having a good
split, and 26400 with no good split. These counts are diagnostic until
independently checked; the analytic theorem does not depend on them.
An odd translation gives the opposite parity. Root reports that none of
the actual remaining 54222 ten-hole geometries is universally closed by
this criterion alone; no coverage decrement is claimed from it.

## 3. Strict zero-crossing interface

Assume a good split has c=0. Choose any N14 cycle K_A and any T44 cycle
K_B on their prescribed retained vertices, containing their original face
matchings. For t=1 or 2, let D_A,D_B be t disjoint optional short edges
on the respective cycles, with the same projected endpoint set S. Removing
D_A or D_B leaves t paths. Let Q_A,Q_B be their induced endpoint pairings
on S, with separately labelled edges when the endpoints agree.

**Theorem 3 (path-pairing interface).** If the multigraph Q_A union Q_B
is connected, removing D_A,D_B and adding the short mirror bridges at all
vertices of S gives one simple extending 29-cycle on exactly Q5-U.

Every port in S belongs to both original cycles, hence is not omitted in
either face. On deleting the optional matching, its degree in its face
becomes one; each mirror bridge restores degree two. Other degrees stay
two. The retained original paths have disjoint interiors. Contracting all
these paths and the mirror identification reduces component connectivity
to Q_A union Q_B. If that multigraph is connected, the full graph is
connected and 2-regular, hence one simple cycle. No required edge was
deleted; all added mirror bridges are short. The vertices are unchanged
from the disjoint two local cycles, so the total is 29.

For t=1 the two edges of Q_A union Q_B are parallel and connected. This
is the usual single-common-optional-edge gluing. For t=2, connectedness is
equivalent to Q_A != Q_B: distinct perfect matchings on four ports form
one alternating 4-cycle; identical pairings form two parallel 2-cycles.
This criterion checks simultaneous occurrence of the two deleted edges
in actual local cycles. Optional-edge unions alone do not establish it.

The special square interface has D_A and D_B as different perfect
matchings of the same short square. This is sufficient only when the
actual surviving path pairings differ as above; a square in two separate
optional unions is not itself a valid certificate.

## 4. One-edge gluing fails for an explicit local pair

In shared Q4 labels, let A's required edges be

    (1,11),(2,9),(4,6),(5,14),(7,12),(8,10),(13,15).

Its holes are {0,3}, and 0 is omitted. Let B's required edges be

    (0,8),(3,10),(4,12),(5,13),(6,15),(7,9).

Its holes are {1,2,11,14}, with {1,2} omitted. These face hole parities
are opposite in local labels, hence equal globally when B uses bit16.
This is a legitimate zero-crossing T63_5 instance with global holes
{0,3,17,18,27,30} and omissions {0,17,18}.

The fresh Python contraction enumerator in
`Q5_T63_four_bridge_example.py` lists exactly five A cycles and one B
cycle up to reversal. It contracts each required edge to an oriented
two-vertex unit and retains each nonomitted hole as a singleton unit.
Every admissible cycle uses all units exactly once; after fixing the
orientation of the first required unit, reversal covers every remaining
orientation. The enumerator tries every remaining unit and orientation
whose joining edge is short, and checks the closing short edge. This is
a finite exhaustive argument for this local cycle domain, not a failed
Hamilton search. All six explicit cycles and their optional unions are
stored in `Q5_T63_four_bridge_example.json`; the two full unions are
disjoint. Thus no choice of the local cycles permits single-edge gluing
by deleting only optional edges. This refutes that proposed gluing lemma,
not the original global cycle theorem.

There is nevertheless a four-port repair. Take the A cycle

    1,11,10,8,9,2,6,4,5,14,15,13,12,7,3

and B cycle

    0,8,10,3,11,9,7,5,13,15,6,14,12,4.

Delete A edges (10,11),(8,9), and B edges (8,10),(9,11). The common port
set is {8,9,10,11}. A's surviving pairing is {(8,10),(9,11)}; B's is
{(8,9),(10,11)}. They differ, so Theorem 3 applies. The resulting global
cycle, explicitly verified for original-edge containment and shortness, is

    1,3,7,12,13,15,14,5,4,6,2,9,25,23,21,29,31,22,30,28,20,16,24,8,10,26,19,27,11.

## 5. Controlled next finite interface domain

The completed producer-only Q4 rich probe treats all 311850 canonical T44
matching inputs already present in the accepted T44 positive tables. For
304872 inputs it stores explicit cycles whose optional-edge union has
size at least 18. N14's accepted positive optional union has size at least
15. Such pairs intersect since 18+15>32, so single-edge gluing works.
The remaining 6978 canonical T44 inputs have stored union below 18 and
are the only exceptions needing a further interface check. Their counts
by stored union size are 8:60, 12:426, 13:224, 14:652, 15:988, 16:1632,
17:2996. The high/low division uses positive lower bounds; no exact upper
bound is needed to cover all inputs.

A separate complete Q4 unit enumeration reconstructs the true N14
optional unions for its two standard hole representatives, totaling
270270 inputs. Before any pair comparison, discard pairs with union-size
sum greater than 32. Expanding each low T44 record under the 192
opposite-parity transforms then gives an upper bound around 5.3e8 scalar
mask comparisons, sharply below the blind matching Cartesian product.
Deduplicating equal marked T44 states and equal N14 union masks reduces
this further. Every remaining disjoint-union pair can then be tested for
the simultaneous two-edge path-pairing interface from Theorem 3. The
mathematical target is a complete positive certificate per exception;
failure of this interface would leave the general zero-crossing theorem
OPEN and would not refute T63_5.

These probes are producer evidence and have not passed an independent
proof-checker. In particular no universal zero-crossing gluing conclusion,
full T63_5 theorem, or new ten-hole coverage is asserted by their existence.

## Corrections, blockers and open risks

The Q4 T63 degree obstruction does not directly lift to Q5: deleting three
vertices leaves at least two short neighbors at every retained vertex,
whereas the Q4 obstruction requires only one remaining neighbor already
used by a required edge. Also at most one vertex can neighbor all three
same-parity omitted vertices, since distinct cube vertices have at most
two common neighbors. These observations rule out that particular local
argument only; they are not a proof against other counterexamples.

Theorem 1 still needs c>0. Theorem 2 handles only its stated odd-cell
family. Theorem 3 needs actual simultaneous cycle/interface witnesses.
General zero-crossing N14/T44 gluing and geometries with no good split
remain open. No failed or sampled search is presented as a negative
certificate for the original T63_5 claim.
