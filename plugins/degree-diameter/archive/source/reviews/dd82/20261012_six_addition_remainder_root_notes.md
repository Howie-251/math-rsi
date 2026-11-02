# Root review: six-addition remainder and tight external rows

Date: 2026-10-12, current phase began 06:46:53 UTC.

Read the complete small-excess and seven-addition proofs, saturated
56-template generator and joint encoder, actual result JSON and
independent LRAT log. The 56 selectors preserve all templates in the
four analytically complete zero sets; all B and H entries are free,
degree ordering only permutes new labels, and every pair has the exact
direct-or-common-neighbor disjunction. The actual formula has 10699
variables and 35325 clauses; solver and checker both exited 20, the
checker recorded s VERIFIED. No broad UNKNOWN input was upgraded.

The small-excess proof additionally received an independent agent's
read-only check of every old-path repair and equality case, with no
gap found. Root checked the seven-addition deleted-edge E=2 branches
separately: m=1 forces the independent union T+U, R=1 forces the
positive added partner into Z, and m=R=0 uses l<=h_t*h_u with l<=2
to force the same union. E=3 fills twelve matching endpoints into
T+U; the thirteenth zero then has two zero neighbors but at most one
unit of excess supply. The adjacent (2,1) proof counts the possible
common neighbors against the sole nonfull deletion leaf's additions
and forces a<=5. The integrated domain is exactly a=6, disjoint D,
E=2 on one whole deleted edge or E=3 on three full endpoints.

Read the complete Petersen tight-row proof, actual completion result,
and independent checker log. A four-target external row leaves six
missing targets and exactly six cubic-internal route slots. Thus all
six slots must avoid the four external targets and be distinct. The
stated forbidden internal edges follow with no girth hypothesis.
For the prior 186-pair skeleton, three recorded rows leave vertex 9
only one allowed internal neighbor. For the repaired 286-pair skeleton,
the four degree-three allowed rows force four distinct neighbors at
vertex 50. Each argument excludes arbitrary cubic internal completion
of its own fixed external skeleton. It does not exclude arbitrary
external matchings. The new 14988-clause formula and 1631-byte proof
have one completed independent verified LRAT check.

These are local mathematical and computational checks. C17 and its two
authorized retries previously failed authentication, with no verdict.
No external review or Lean acceptance is inferred from these checks.

## Final two branches, checked around 07:18 UTC

Read both complete new files HS58_A6_THREE_FULL_EXCLUSION.md and
HS58_A6_TWO_FULL_EXCLUSION.md. In both arguments an ordinary positive
old endpoint has no A edge. Thus a replacement old path to a nonfull
endpoint can only use that endpoint's single A edge; the exceptional
ordinary neighbor is counted by an actual HS common-neighbor intersection.
There is no omitted direct-A or A-A repair. The repeated singleton label
at ordinary neighbors counts distinct old vertices, additional to its
nonfull endpoint, so the bound on the auxiliary degree is valid even if
two singleton labels coincide.

For E3, root checked k<=2/0/1 in the three geometries, the at most one
exception after accounting for epsilon, and the retained full-neighbor
port-pair intersection in the cross-at-nonfull case. The resulting reach
bounds are 7/6/7, with all new labels and H variable.

For E2, root originally derived the extension of that count and had two
independent agents check it. Both found no gap. The q_v and q_w exceptions
must be kept distinct; the proof does so. In the cross geometry, the two
nonfull endpoints can be exchanged, so the endpoint being bounded has no
full neighbor and the cross edge meets the other. This gives reach at most
6; the no-cross bound is 7. The proof does not use the number of internal
matching edges and closes its full-deleted-edge E2 pattern for every a.

The complete theorem is now HS58_TWO_DELETE_ARBITRARY_ADDITIONS_EXCLUSION.md:
a successful specified-HS-base58 construction requires at least three
original deletions, even with arbitrary original-nonedge additions and
arbitrary attachments/H. This uses the earlier documented finite and checked
CNF dependencies; the final two branches are pure. The attempted necessary
E2 old-template diagnostic is not part of the proof. Its planned new SAT,
seed generation and independent enumeration were cancelled before execution.
No arbitrary58 or global optimum conclusion follows.

## Final Petersen domain repair and new coset constructions

Read PETERSEN_ALLOWED_PETERSEN_DOMAINS.md and
PETERSEN_JOINT_P_DOMAIN_REPAIR.md, actual final completion result and
independent checker log. The final six domain sizes are all nonzero;
the unique fiber-3 Petersen graph is an output of the complete catalog,
not a chosen fixed internal graph. In the four displayed uncovered cross
pairs the exact two internal-edge alternatives force four different
neighbors at vertex1. This explanation retains the Petersen hypothesis;
unlike the preceding degree-only obstructions it does not assert
arbitrary cubic completion is impossible. The actual 14982-clause query
has one verified 1263-byte LRAT certificate. This fixed-external repair
chain is ended.

Read both full coset enumerators and actual preparation/search results.
The S5/A5xC2 source generates gH and inverse-paired H-suborbits, verifies
representative independence, and partitions the complete unordered-pair
set into regular symmetric loop-free blocks. Its increasing-index
subsets have exactly the independent generating-function counts1281/1999.
The A6 source explicitly generates all360 even permutations from its
supplied generators, checks each H order6 and sixty gH, and computes
unordered-pair orbits directly by group generators. Both models partition
all1770 pairs; their degree-eight domains each contain exactly7 unions.
Root reads are source-and-output checks, not reruns of either search.

The transitivity-based radius-two search is exact; each actual best graph
has a separate full BFS. Actual maxima are52,51,48,48 vertices in a closed
two-ball, with240,270,360,360 bad pairs. All3294 declared unions have been
visited. No validity claim depends only on degree/edge count.

Root supplied the elementary A6 order-six stabilizer classification and
the constructing agent independently checked it. Inversion of a single
three-cycle requires two transpositions to be even; an involution swapping
two three-cycle supports would be odd. The two proposed odd centralizers
correct S6 conjugacies to A6 conjugacies. Root additionally checked all
order-two stabilizers for S5/A5xC2: unenumerated types admit regular A5 and
are covered by the already-complete Cayley exclusion. Thus the unified
TRANSITIVE60_S5_A5C2_A6_EXCLUSION.md covers all degree-sixty transitive
actions by those three groups, but not all vertex-transitive graphs.
