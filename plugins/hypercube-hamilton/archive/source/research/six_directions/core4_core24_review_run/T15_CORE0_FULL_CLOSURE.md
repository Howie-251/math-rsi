# Complete T15 core 0 by boundary-pairing exclusion

Date: 2026-11-01. ARIS proof-writer. Candidate full core-0 proof;
fresh independent semantic and finite-input audit pending.

## Exact claim

Let F be any matching of K(Q5) with holes {0,1,2,7,11,13}. There is a
simple 30-vertex cycle on Q5-{1,2} containing every edge of F and with
all new edges short. This includes every cube-automorphic image of the
marked geometry. Original matching edges may have arbitrary length and
parity. Full T15 and full eight-hole P6 remain separate open targets.

Cut coordinate 1 (zero-based). Identify both faces with Q4 by deleting
that coordinate. The one-face A has holes {0,3,5}, of even local parity;
omit 0_A. The zero-face B has holes {0,7,1}; omit 1_B. All labels below
are these common local labels. Write internal matchings F_A,F_B,
crossings C, port sets X_A,X_B, and c=|C|. Both faces have 13 originally
covered vertices. Hence c is odd and 1<=c<=13.

## Dependencies and strategy

1. Q4 N14, at its previously audited arbitrary-complete-graph scope.
2. The complete audited Q4 balanced four-hole tables: holes {0,7,z,1},
   omit z,1, where z=3 or 5. Each has exactly three negative matchings
   and 10392 positive matchings. The z=5 table is obtained from z=3
   by interchanging coordinates 1 and 2. `T15_BALANCED_BRIDGE_REVIEW`
   audited all positive certificates and all negative short completions.
3. `THREE_MATCHINGS_DISCONNECTION.md` and its finite N6/N8 basis.
4. `T15_R3_SMALL_CROSSING_PROGRESS.md`, including full B enumeration
   and the 810810 complete residual positive cycle certificates, for c=1,3.
5. `t15_core0_r3_c5_inverse.py/.json`: complete two-negative-family
   inverse accounting for the only remaining c=5 port configuration.

The new part is not a count of many A matchings. It uses the fact that
N14 can be applied for **every** artificially chosen boundary matching.
A small forbidden output set can therefore be ruled out by deliberately
choosing the auxiliary matching to disconnect every forbidden output.

## 1. Boundary pairings supplied by N14

Choose a bridge label z in {3,5}, and let w be the other one. Put
E=X_A union {z}. For every perfect matching D on E, F_A union D has
exactly the two even holes 0,w. N14 supplies a 15-cycle on A-0 containing
that matching. Delete D. Its path components form a spanning forest
with endpoint set E and some induced perfect pairing R on E.

The multigraph R union D is connected: compressing each forest path
in the original 15-cycle produces exactly this alternating cycle.
Conversely, any later manipulation of the compressed paths records
their interiors for expansion; these interiors are disjoint and exhaust
A-0. All new surviving path edges are short, since all D edges are deleted.

Attach every original crossing and the new short bridge z_A z_B.
There are two distinct cases.

### Internal bridge mirror

If z_B is not a port, it is internally covered by F_B, since it is not
one of its original holes. Attaching the crossings and the bridge maps
the endpoints E bijectively to X_B union {z_B}. Join the resulting
path pairing to F_B and suppress the degree-two vertex z_B.
The result is a matching L with holes {0,7,1,z}. The suppressed vertex
has one internal F_B neighbor and one port neighbor, which are distinct;
therefore no cycle or loop is created.

For this fixed F_B and crossing bijection, the map R -> L is injective.
Indeed, in L identify the partner of the internal vertex k=F_B(z).
Replace its incident edge kq by kz,zq, remove the other fixed F_B edges,
and pull all port labels back through C. This recovers R uniquely.
Consequently at most three possible R give negative L, one for each
negative entry of the exact balanced table. Every positive L expands
its 14-cycle to a 30-cycle by restoring z_B and the 15 A vertices.

### Occupied bridge mirror

If z_B is a port, set d=C^{-1}(z_B). The vertex z is an A original hole,
so d!=z. For c>=3 prescribe zd in D, and write D={zd} union D', where
D' is any perfect matching on X_A-{d}.

Replace the deleted edge zd of the N14 cycle by the path
z_A--z_B--d_A, whose first edge is short and whose second is the original
crossing. Delete D'. Because D' is nonempty, this leaves a path forest,
not a closed component. Attach all the other original crossings.
Its endpoints are X_B-{z_B}, and its interiors cover (A-0) union {z_B}.
Let Q be its endpoint pairing, pulled back to X_A-{d}.

Here Q union D' is connected: it is obtained by compressing paths in
the same single cycle after replacing zd. The B matching obtained by
adding the transported Q to F_B has holes {0,7,1,z}. This map Q -> L
is injective, because F_B is fixed and disjoint from the port endpoints.
At most three Q are negative. A positive 14-cycle expands to the same
30-vertex conclusion, with no remaining auxiliary edges.

These constructions apply to every arbitrary crossing bijection; no
shortness assumption is made on original C, F_A or F_B.

## 2. All c>=7, and an internal mirror when c=5

For an internal mirror the boundary set E has size c+1. When c>=5 this
size is even and at least six. Apply the three-matchings disconnection
lemma to the at most three forbidden R. Choose D whose union with every
forbidden R is disconnected. Section 1 and N14 produce an R with
connected R union D. It cannot be one of the forbidden R. This gives a
positive L and finishes the construction.

For an occupied mirror at c>=7, the boundary of Q has size c-1>=6.
Apply the same lemma to the at most three forbidden Q to select D'.
Then invoke N14 with {zd} union D'. The resulting Q has connected
Q union D' and is therefore positive. It expands as in Section 1.

Thus every c>=7 input is closed, and for c=5 an input is closed if
either 3_B or 5_B is internally covered.

## 3. The remaining c=5 case: both mirrors are ports

Suppose {3,5} is a subset of X_B, which has size five. For bridge z,
any compressed matching is L=F_B union Q_B, where Q_B pairs the four
ports X_B-{z}. Thus Q_B consists of two edges, F_B consists of four,
and their vertex supports are disjoint.

If even one such compression can be negative, its F_B must be obtained
from one of the three negative L entries by choosing two L edges for
Q_B and deleting them. The port set is then {z} union V(Q_B). Since
the other bridge mirror w is also a port, the chosen two edges must
cover w. Conversely these choices enumerate all possible negative
compressions for this bridge, independently of the A forest.

There are precisely 15 distinct (X_B,F_B) candidates for z=3, and 15
for z=5. `t15_core0_r3_c5_inverse.py` enumerates every choice explicitly
from the complete negative tables, including the coordinate permutation
for z=5. The two sets have empty intersection. This is a small finite
exhaustion, not a sampling statement.

Therefore, for the actual (X_B,F_B), at least one bridge z has no
possible negative compressed matching at all. For that bridge choose
any D' on the four remaining A ports, add zd and use Section 1.
The resulting forest is valid and its compressed L must be positive.
This closes every c=5 input.

## 4. Three crossings

For each bridge there are three possible pairings of the four endpoints
X_A union {z}. At least two are realizable by Section 1: if only R0 were
realizable, choosing D=R0 would force R0 union D disconnected, contrary
to N14. This is the two-of-three lemma, independent of any A enumeration.

For fixed B partial matching and crossing bijection, test the three
pairings for each bridge. After mapping A ports through C, join the
compressed paths to F_B. Reject a loop or closed component at the bridge
mirror; otherwise suppress that mirror and use the exact balanced table.
This determines the admissible pairing sets purely on B.

The complete enumeration in `verify_t15_r3_small_B.cpp` generates all
binomial(13,3)*9!!=270270 B partial matchings and all 6 partner orderings.
For all 1621620 inputs there is a bridge with at least two admissible
pairings among its three possibilities. It independently traces graph
components and reads the original binary negative tables; it does not
reuse the producer's suppression formula. The resulting full histograms
and checks are recorded in `t15_r3_small_B_independent.json` and
`t15_r3_small_verification.json`.

For that bridge, its at-least-two realizable A pairings and at-least-two
admissible B pairings intersect. Choose their common pairing and expand
the positive B 14-cycle. This closes all c=3 cases.

## 5. One crossing

For c=1 the A endpoint set has two vertices, so its unique pairing is
realizable by N14. The same complete B enumeration checks all
13*11!!=135135 partial matchings. Only six have no admissible bridge.
Their exact lists are in `T15_R3_SMALL_CROSSING_PROGRESS.md`; the
independent graph checker agrees with the producer and the search inputs.

For each of these six fixed B inputs, enumerate each of the 13 A port
choices and all 10395 internal pairings of its other twelve covered
vertices. All 810810 resulting full Q5 matchings have explicit 30-cycle
certificates in `t15_r3_small_core0_c1_residual.bin`.
The independent verifier reconstructs every required matching in this
entire domain, checks it equals the recorded one, and checks exact cycle
support, vertex uniqueness, containment of all thirteen required edges,
shortness of every other edge, record count and absence of trailing data.
All checks pass. Search caps play no role in the proof: every input has
a verified positive certificate, with no UNKNOWN or omitted input.

The certificate uses the isomorphic global labels 2v+1 for A and 2v
for B. It omits precisely 1,2, representing 0_A,1_B. This coordinate
insertion preserves all local and cross-face short adjacencies; transport
back to the original cut gives the stated core-0 marked geometry.

## Conclusion and independent-audit boundary

The only possible crossing counts are 1,3,5,7,9,11,13. Sections 2--5
cover all of them and every arbitrary internal matching and partner
bijection. The exact core-0 theorem follows once the explicit finite
inputs and dependency applications above pass fresh independent review.

This proof does not rely on the large A port-spectrum producer counts,
the alternative cut's c2 or c4 research, or any random Q5 experiment.
No claim of full T15, complete eight-hole P6, or full P6 is made.
