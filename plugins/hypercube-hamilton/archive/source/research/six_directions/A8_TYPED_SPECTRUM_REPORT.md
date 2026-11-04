# A8 orbit 4: the proposed low-gap pairing-spectrum repair is impossible

Date: 2026-11-01. New exploratory result; independent proof-checker review
pending. The earlier frozen proofs and manifests were not modified.

## Claim and status

For the canonical three-bridge setup with original $A$ holes
$\{0,1,2,4,15\}$, forbidden vertex $0$, original $B$ holes
$\{7,11,13\}$, bridge vertices $Y=\{1,2,4\}$, and possible compressed
obstruction edge $0\,8$, every nonfixed low-gap $B$ input has an empty
allowed endpoint-pairing spectrum. Consequently changing the short
spanning forest in $A$ cannot repair any such input while keeping this
fixed bridge and local-completion template.

**PROVABLE AS STATED** by the topology argument below. The computations
provide complete finite corroboration, with an independent verifier
running over the saved inputs. This is not a counterexample to A8 and
does not close any remaining A8 orbit.

## Dependencies and notation

The fixed imported results are the Q4 T63 classification and the
three-bridge transfer, independently accepted in `A8_BRIDGE_INPUTS_REVIEW`.
Let $c\in\{1,3,5\}$ be the crossing count and
$T=X_A\cup\{t_1,t_2,t_3\}$ the $c+3$ endpoints in $A$.
The graph $G$ consists of $F_B$, the original crossing edges, and the
three bridges. Let $P$ be its matching of $T$--$T$ path components.
A component meeting $T$ at one endpoint and $B$ at the other has a
terminal in $B$ and a root in $T$. Put $d=(c+3)/2$.
Let $e=1$ when both $0,8$ are terminals rooted in $T$, and $e=0$
otherwise. Nonfixed low-gap inputs satisfy $0\,8\notin F_B$ and
$d=|P|+e$.

## Proof

The components of $G$ meeting $T$ partition $T$ into pairs belonging
to $P$ and singleton roots of terminal components. Therefore their
number of terminal roots is exactly $2d-2|P|=2e$.

If $e=0$, every endpoint in $T$ belongs to a $T$--$T$ component.
Any proposed $A$ forest pairs all endpoints in $T$ by another matching
$S$. Every vertex of the finite multigraph $S\cup P$ then has degree
two, so it contains a closed component. This closes a component inside
the transferred forest before the other-face cycle can be expanded.

If $e=1$, there are exactly two terminal roots, belonging to $0,8$.
For any endpoint matching $S$, the multigraph $S\cup P$ consists of
some cycles and one path between those two roots. If any cycle occurs,
the transfer is invalid because a closed component has already formed.
If there is no cycle, compression necessarily creates the edge $0\,8$.
This is exactly the necessary and sufficient T63 obstruction. Thus
every possible $S$ fails, independently of which $A$ forest realizes it.
This proves the claim.

## Finite computation and complete domains

The producer is `A8_typed_spectrum.cpp`. It enumerates optional short
edge sets $N$ in $A$ having degree two at $15$, degree zero at $0$,
and degree one at each other vertex. It chooses the two neighbors of
$15$ and then all short perfect matchings on the twelve remaining
vertices. There are exactly 96 distinct patterns. For each original
$F_A$ it keeps only simple path forests $F_A\cup N$ and records their
endpoint pairing mask. Parallel copies of a required edge and an optional
edge are rejected as cycles, so required edges are not counted twice.

For each saved low-gap $B$ input and every crossing bijection, the
producer tries every abstract endpoint pairing, rejects any closed
component, and rejects the compressed $0\,8$ edge. It saves the resulting
mask, which is always zero.

| $c$ | complete $A$ inputs | distinct $A$ spectra | spectrum size range | low-gap $B$ inputs | crossing bijections total | distinct $B$ spectra |
|---:|---:|---:|---|---:|---:|---:|
| 1 | 10395 | 4 | 2--3 | 3780 | 3780 | 1, empty |
| 3 | 17325 | 1843 | 6--15 | 1785 | 10710 | 1, empty |
| 5 | 6930 | 6858 | 16--60 | 105 | 12600 | 1, empty |

The corresponding numbers of original $(F_A,F_B,\text{bijection})$
zero-intersection pairs are 39,293,100; 185,550,750; and 87,318,000.
These counts describe failures of this particular template, not failures
of the original cycle problem. No larger matching search is warranted
to fill a spectrum that the topology forces to be empty.

## Saved certificates and verification

For each crossing count, `A8_typed_c*_A.bin` has 32-byte records: a
16-byte mate array followed by a 128-bit little-endian pairing mask.
Endpoint order is the three bridge holes followed by sorted original
$A$ ports. Pairing ranks are the recursive unordered pairing order
(least unused vertex paired in increasing order).

The corresponding `A8_typed_c*_B.bin` records have $32+c$ bytes: the
16-byte $B$ mate array, the permutation of sorted $B$ ports assigned
to the sorted $A$ ports, and a 128-bit mask. The other result files
record exact counts and representative zero intersections.

`A8_typed_spectrum_verify.py --full-a` independently regenerates the
96 patterns and complete $A$ matching domains, recomputes every $A$
mask using adjacency components instead of the producer's disjoint-set
algorithm, and checks all saved $B$ inputs and crossing permutations.
For $B$ it independently checks the topological premise of the proof:
all endpoint components are paired internally, except possibly exactly
the two roots ending at $0,8$. The output is
`A8_typed_spectrum_verified.json`. The verifier imports neither the
producer nor any Hamilton search routine.

## Remaining obligation

A repair must change the cut, the chosen bridges, the local avoided
vertices, or the type of transferred object. Optimizing the $A$ forest
within this template cannot help. The separate four-cut signatures file
records exact local bad conditions for coordinating the two delta-zero
and two delta-minus-one cuts of the fourth residual orbit; their joint
feasibility has not been settled here.
