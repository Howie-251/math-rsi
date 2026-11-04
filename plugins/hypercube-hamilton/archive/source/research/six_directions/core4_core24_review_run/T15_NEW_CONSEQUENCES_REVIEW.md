# Independent scoped audit: new T15 consequences

Date: 2026-11-01. Reviewer: fresh delegated agent `/root/t15_new_consequences_audit`.
Actual reviewer spawn: model `gpt-6.1-sol`, reasoning effort `high`,
`fork_turns=none`, as explicitly specified by the user and relayed by the parent.
This user-directed route overrides the skill's default reviewer model/effort.
Protocol: ARIS proof-checker, scoped to the parent's requested artifacts.
Semantic review independence: **same-family**. Acceptance: **provisional**.
No cross-family overlay was performed. Deterministic certificate verification is
reported separately from semantic proof acceptance. This report changes no
project-wide status and proves neither full T15 nor P6.

Verdict: **PASS within the declared scope, modulo explicit imports**. The
same-face zero-crossing proof is sound relative to T44_5. The eight-hole
accounting is independently correct as geometry accounting; interpreting its
7,820 covered rows as universally solved requires the separate eight-core
theorem audit. No new core theorem is inferred from the counts.

## Inputs and independence

Read the complete `T15_SAMEFACE_ZERO_CROSSING.md`, its checker source,
`eight_after_single_face_cores.py`, and `T15_PRESCRIPTION_ANALYSIS.md`.
The new `T15_NEW_CONSEQUENCES_REVIEW_check.py` imports no producer or earlier
checker. It reads four A-path binaries and two complete Q4 circle binaries
directly. It independently checks exact supports, mandatory-edge retention,
shortness, matching universes, and negative short-completion exhaustion.
Saved check summaries and input hashes are comparison targets, not proofs.

For the new geometry accounting the only generating inputs are
`remaining_eight_after_a1b4_{1,7,31}.bin` and
`t15_analytic_geometry.json`. All 120 Q5 coordinate permutations are generated
to assign orbit IDs, and overlapping source orbits with different IDs are
rejected. The producer's `eight_t15_core_map.json` is **not** read to generate
choices. Its hash is checked only because the producer claims it as provenance.
This audit takes the raw previous remaining bins as its scoped starting set;
it does not re-prove that the earlier a1b4 elimination is complete.

Exact SHA-256 hashes of all reviewed proof and data inputs, including the
new checker itself, are in the companion check JSON. T44_5 and CF1 import
documents are checked against their current PASS review hashes. Their complete
proofs and transitive dependencies are explicit imports, not reaudited here.

## Proof-obligation ledger: same-face zero crossings

| ID | Obligation | Discharge |
|---|---|---|
| SF1 | Universal input domain | Every matching of K(Q5), six exact holes of type 1:5, arbitrary specified two majority omissions, some common coordinate face with no required crossing. Long and same-parity matching edges remain allowed. |
| SF2 | Restrictions | Zero required crossings imply F_B is perfect and F_A has exactly the six holes; no assumption about a favorable matching is added. |
| SF3 | Adjacent preprocessing | For available b adjacent to a, F+ab is a matching with four same-parity holes including the omitted pair. T44_5 applies to precisely these hypotheses. ab is short, so the final cycle has only short edges outside original F. |
| SF4 | Residual normalization | Shared translation sends a to 0, then shared coordinate permutation sends the three available weight-three holes to {7,11,13}. It transports every arbitrary matching and preserves both bridges. |
| SF5 | Marked-geometry coverage | Independent enumeration of all 560 marked root-zero geometries gives 520 adjacent and four disjoint residual orbits of sizes 12,12,4,12, with representative omitted pairs (1,2),(2,4),(1,14),(2,14). |
| SF6 | A14 path coverage | Four files each have 945 distinct valid matchings on their exact ten-vertex support: all 9!! inputs. Directly check 22,260 positive paths, 210 triangular rows, and 3,570 nontriangular rows. |
| SF7 | A endpoint bounds | All nontriangular rows list the six allowed odd endpoints. Every triangular row lists all four distance-three endpoints. No completeness of the list beyond this lower bound is assumed. |
| SF8 | B table coverage | Each opposite-hole table has 135,135 distinct matchings on 14 vertices, exactly 13!!. All 270,166 positive cycles verify. All 51+53 negatives are certified by exhausting disjoint short perfect complements. |
| SF9 | B forward/inverse equivalence | If P(0)=y, a Hamilton endpoint path is impossible. Otherwise remove endpoints 0,y and replace their matching edges by ab; the result is exactly a required 14-cycle problem. The reverse cannot duplicate ab because a 14-vertex path cannot contain the edge joining its endpoints. |
| SF10 | B universal quantifier | Transport all negative tables to the eight odd y. Invert every oriented edge, giving 5,824 instances and 4,708 candidate P. Every nontrivial bad endpoint must produce one of these instances. Outside the candidate set only an odd root partner can fail: at least seven good odd and three good distance-three endpoints remain. |
| SF11 | B endpoint bounds | Independent candidate census gives bad histogram {1:2072,2:2180,3:36,4:420} and good-distance-three histogram {1:420,2:276,3:2212,4:1800}; hence at least four good odd endpoints and one good distance-three endpoint for all P. Translation handles all roots. |
| SF12 | Endpoint intersection | In the eight-element local odd universe, six A endpoints and at least four B endpoints intersect in at least two. In triangular rows, A contains every distance-three endpoint and B contains at least one. The same q is therefore available in both faces. |
| SF13 | Two-bridge simplicity and support | A14 and B16 have disjoint vertex supports and distinct endpoints 0,q. Joining corresponding endpoints gives one explicitly traversable 30-cycle, retaining every original edge and omitting exactly v,w. Both bridges are short. |

The dependency DAG is acyclic at this scope: Q4 tables and path witnesses feed
the residual branch; T44_5 feeds only adjacent preprocessing; both feed the
same-face claim. No full Q5 T15 or P6 proposition is used.

Counterexample checks target the vulnerable cases: triangular A rows are
checked directly rather than excluded; trivial B partner endpoints are handled
separately; all negative complementary short matchings are exhausted; marked
geometry orbit overlaps and omissions cause failure. No counterexample or
unresolved semantic gap was found in this scoped theorem. Inputs with required
crossings or holes in no common coordinate face are outside this theorem.

## Independent eight-hole accounting

The checker reads 41,458 distinct previous raw geometries. For each coordinate
it identifies the target face; a cut is eligible exactly when that face has two
Z holes and one W hole. The lone Z hole in the other face becomes the minority
root. Move the two avoided Z holes across the cut, delete that coordinate using
an explicit coordinate list, translate by the root, and identify the resulting
marked Q5 orbit. This reconstructs every choice set from 112,199 eligible cuts.

Using candidate core IDs {13,14,19,31,32,35,37,38} gives:

| Target | Newly covered | Remaining | Remaining without a2b1 |
|---:|---:|---:|---:|
| 1 | 2,610 | 9,385 | 10 |
| 7 | 2,490 | 11,663 | 20 |
| 31 | 2,720 | 12,590 | 20 |
| Total | **7,820** | **33,638** | **50** |

The remaining total is **33,588 with a2b1 + 50 without a2b1**. Each new
`remaining_eight_after_single_face_*.bin` has no duplicate rows and its set is
exactly the independently reconstructed retained set. These are counts of
normalized marked hole configurations, not matchings, automorphism classes of
the entire parent problem, or proved Hamilton paths by themselves. Realizing
matchings are not enumerated here.

After removing the eight candidate cores, the remaining choice patterns force
the eleven singleton cores

    0,1,2,4,5,8,10,15,23,24,27.

Discard every constraint hit by those eleven. The remaining constraints split
into three disjoint variable groups, disjoint also from the forced cores:

| Variable group | Choice constraints | One sufficient choice |
|---|---|---:|
| {6,7,9} | {6,7}, {7,9} | 7 |
| {18,21,25,26} | {18,26}, {21,26}, {25,26} | 26 |
| {30,34,41,44,46} | {30,41,44}, {34,44,46} | 44 |

Each group needs at least one additional core. Selecting 7,26,44 hits all
remaining constraints. Thus the exact minimum additional **whole-orbit core
cover in the present a2b1 scheme** is 11+3=14. This does not imply fourteen
logically independent theorems are necessary, and it covers only the remaining
a2b1 geometries, not the fifty with no eligible cut. Different reductions or a
general theorem could replace this planning cover.

## Prescription analysis: local semantic review

`T15_PRESCRIPTION_ANALYSIS.md` is sound at its claimed conditional scope:

* For each fixed eligible y,z,p, suppressing y in a 31-cycle replaces z-y-p
  by zp; a pre-existing zp would isolate a triangle in that single cycle.
  The inverse inserts the previously omitted y. This is exact fixed-prescription
  cycle equivalence, without a quantifier upgrade to every prescription from
  a claim that merely some prescription works.
* In the preprocessed case p cannot equal a, because p is adjacent to z in B.
  Consequently p is covered by F. Applying imported CF1 to L=F+yz is valid:
  L has holes a,x,B-minus-z, its two included majority holes are nonadjacent
  to a, and yp is an allowed short edge outside L. In the resulting factor p
  already has its F edge and py, so pz cannot also occur. Suppression is simple
  and preserves component count. This proves factors for every eligible fixed
  prescription, without proving connectedness.
* In the target 30-vertex graph F has 13 edges and four included holes. Since
  those holes are independent after preprocessing, H=J'-F consists of four
  vertex-disjoint two-edge paths centered at holes plus nine isolated edges
  on the remaining 18 covered vertices. It has 17 short edges. Contracting F
  gives a loopless 2-regular multigraph on 17 vertices. Parallel edges are
  allowed; connectivity is preserved by contraction and remains unproved.
* For every z in B, F+az has four same-parity holes, including x,y. Imported
  T44_5 gives the specified 30-cycle; deleting az gives a Hamilton a--z path
  retaining F. az is allowed to be long because it is an auxiliary matching
  edge removed before use.
* The ordered rotation criterion is correct: deleting forward v-w separates
  endpoint pairs (a,v) and (w,z); adding v-z and w-a joins the components into
  one cycle. The reversed order instead closes two components, so it cannot
  be silently substituted. No existence claim for the favorable order is made.

CF1's full geometry/Hall proof is an import. This review checks its application
and the new suppress/expand argument; it does not rerun all 65,535 GF5 subsets.
The project's current authoritative A4 state is the established complete Q5 A4
result in `CANONICAL_A4_CLOSURE.md`, accepted by
`CANONICAL_COMPLETION_REVIEW`. That A4 theorem is not independently reaudited in
this scoped review. The present analysis keeps the **additional prescribed-edge
connected A4 extension** and full T15 open; this is not a claim that ordinary
Q5 A4 remains unproved. The older reduction file is used here only for the
elementary distance-two existence geometry.

## Reproduction and limits

Run from E:/新问题:

    D:/anaconda/python.exe research/six_directions/T15_NEW_CONSEQUENCES_REVIEW_check.py

The check returns PASS. Semantic conclusions remain same-family/provisional.
The eight candidate core theorem is separately reviewed by another fresh
agent and is **not** independently reproved here. Even after accepting that
theorem, the remaining 33,638 configurations are only residual geometry
obligations in this scheme. Full T15, full eight-hole P6, and full P6 remain
unproved. No global ledger or source proof was edited.
