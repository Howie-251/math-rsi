# Independent review: full-Q5 near-balanced rows and exact higher-hole census

Verdict: **PASS, relative to the explicitly accepted imports**, for the stated
row theorem, predecessor reductions, and all four exact census/raw domains.
This does not close any complete 12/14/16/18-hole layer or full P6.
Review independence is same-family; semantic acceptance remains provisional.
Fresh reviewer: `/root/higher_q5_nearbalanced_review`, user-selected
GPT-6.1-sol / high, overriding the skill's default route.

The frozen manifest SHA-256 is
`1278b483dd4cb90c376caa8deca167b3512aefef3d8ce9475f5f7747f1c81fab`.
All 38 file hashes and byte lengths in it were checked, totalling 250792846
bytes. No producer proof, census, raw, or state file was modified.

## Exact statements and dependency ledger

For every k in {6,7,8,9}, every short Q6 matching M with 2k holes,
every free root u, and every opposite-parity target v (free or covered),
normalize u to even 0 by translation. Let Z be its other k-1 even holes
and W its k odd holes. If Z union W is independent, each target-facing
coordinate cut satisfying b=a>=1 or b=a+1 proves the endpoint assertion.
For b=a+2 the assertion holds provided there exists a source in W intersect
A outside {v, mirror(u)}. All final newly added edges must be short.
This is an assertion about **every realizing short matching**, not one
matching selected for a hole geometry.

Dependencies: accepted uniform transfer plus the established five-direction
free-root endpoint theorem; accepted full Q5 balanced endpoints/cycles and
imbalance-two avoid-one; and, only for the predecessor reductions, the
complete preceding hole layer. These imply cut sufficiency; the independent
geometry census then partitions an enlarged domain. No dependency returns
from these new Q6 rows to their Q5 inputs, and no missing higher predecessor
is silently supplied by the census.

The Q5 import is exactly the accepted consequence in
Q5_A10_FULL_REVIEW.md F08-F15: balanced endpoints m=1,...,16 from every
free root to every opposite-parity target, balanced cycles m=0,...,16,
and imbalance-two holes (t-1,t+1), t=1,...,15, avoiding every specified
majority hole in both orientations. Required local edges may be arbitrary
complete-graph edges. The zero-hole cycle uses its explicit perfect-matching
import. These ranges do not come from extrapolating small numerical rows.

TEN_HOLE_FULL_REVIEW.json has final PASS and the pinned hash
`72c6f693b4f8bee6376edcbd132235d7985436f6ebbad8a19dade0d5326f643d`.
Consequently predecessor reductions for k=6 are available relative to the
accepted imports. For k=7,8,9, those reductions remain conditional on the
complete 12/14/16-hole theorem respectively. The cut theorem on its stated
independent geometries has no such predecessor hypothesis.

## Mathematical micro-claim audit

| ID | Obligation and discharge |
|---|---|
| H01 | Translation by u preserves shortness, matching membership and opposite endpoint parity. Coordinate permutations fixing 0 act transitively on odd targets of each weight 1,3,5, represented by 1,7,31. No matching symmetry beyond transporting every realizing M is assumed. |
| H02 | If the original crossing count c=0, M uses at most five directions. Invoke the explicitly accepted **five-direction free-root endpoint theorem for the original Q6 instance**, including a covered target. This is a distinct import, not an application of a Q5 endpoint theorem across disconnected faces. Its explicit provenance is HIGHER_HOLE_UNIFIED_TRANSFER.md and EIGHT_HOLE_CONDITIONAL_REDUCTION_DRAFT.md lines39,108-110. |
| H03 | For c>0, let pE,pO count even/odd A crossing ports. Short internal M_A gives 16-a-delta-pE=16-b-pO, hence pE-pO=b-a-delta. Also c congruent to a+b+delta modulo2. These give all completion pairing parities. |
| H04 | Row b=a>=1 consumes one even source z in Z intersect A, which exists because a>=1. If delta=1, r=u and pair X_A plus z; if delta=0, r=z and pair X_A. In both cases the unconsumed holes are exactly (b,b), with the even r free. |
| H05 | Row b=a+1 consumes no source. If delta=1, r=u and pair all X_A; if delta=0, pE-pO=1 so an even crossing port r exists and pair X_A minus r. The resulting holes are exactly (b,b), with b>=1. |
| H06 | Row b=a+2 consumes one odd source w. With delta=1 pair X_A plus w and r=u. With delta=0, pE-pO=2 so an even port r exists; pair (X_A minus r) plus w. The resulting holes are exactly (a+1,a+1). |
| H07 | All sources are original holes, distinct from ports and the free root. In rows H04-H05 only even vertices can be consumed, so odd v remains legal. In H06 the source condition explicitly excludes free v. A covered target may itself be paired by D; the local endpoint theorem permits covered targets and after deleting D the temporary isolated crossing target is legal. |
| H08 | In H06, for covered v only mirror(u) can be forbidden, whereas b=a+2>=2, so a source exists. For fully independent holes mirror(u) is not a hole, and excluding free v leaves a source. Under only Z union W independence and a=0,b=2 one must retain the explicit exception; the proof and census do so in their appropriate domains. |
| H09 | A source mirror y cannot be an original crossing port: its short crossing partner would be the source itself, which was free. Independence excludes opposite-parity nonroot holes at y. An even source has an odd mirror, different from u; an odd source excludes mirror(u). Thus y is internally B-covered. |
| H10 | Delete D from the A Hamilton path and attach physical crossings and the possible source bridge. All attachments use distinct B vertices. With delta=1, c>0 and completion parity force D nonempty, so the true endpoint segments are different. With delta=0, u was unattached. Adding the unique tagged uv joins components without making a cycle. The accepted D-empty boundary therefore remains valid. |
| H11 | Compress the A-interior paths to arbitrary matching T on B. Its endpoints are X_B plus the possible y and, if delta=0, u. There is only one possible conflict y with M_B. Its original mate h is internally covered, is neither a crossing port nor u, and has parity opposite to y; hence h is outside all T endpoints. The conflict is a path with pendant h, not a cycle. Suppressing y retains all required edges as a recorded path and preserves the tag. |
| H12 | The actual B holes after suppression are (H_B minus u) union {y}, or H_B minus u if no source. For b=a they are (k-a-1,k-a+1), with exactly odd majority y omitted. For b=a+1 they are (k-a-1,k-a-1), no omissions. For b=a+2 they are (k-a,k-a-2), with exactly even majority y omitted. No fictitious hole count is substituted for the constructed matching. |
| H13 | Every A balanced parameter is positive and <=9, within 1,...,16. B balanced parameters are 0,...,8; imbalance-two t is 1,...,8, within 1,...,15. Zero-hole B cycles are explicitly covered. Face parity relabeling can interchange parity classes and is allowed by the imported both-orientation statement. |
| H14 | Arbitrary D/compressed matching edges, including long/same-parity edges, satisfy the arbitrary-K(Q5) imports. The theorem is universal over that auxiliary matching, so no matching feasibility or sampled matching argument enters. Expanding all recorded paths restores every original required edge and every actual vertex exactly once. D is deleted, compression expanded, and the unique tag deleted. Every surviving newly introduced physical edge is short. |
| H15 | Covered predecessor reduction: any Z--W short edge is disjoint from u and covered v. Adding it gives a short matching with 2k-2 holes and unchanged free root, so complete P(k-1) applies. Root adjacency is not removed in this domain. |
| H16 | Free predecessor reduction, xy different from uv: adding any short hole edge leaves at least one of u,v free. Apply P(k-1) rooted at that free endpoint and reverse if necessary. The added edge is short relative to M. The other endpoint is permitted to be covered. |
| H17 | Free predecessor reduction, xy=uv: add uv, choose any remaining free r and any short neighbor s. P(k-1) supplies a Hamilton r--s path containing augmented M. The edge rs is not already on this 64-vertex simple path because it joins its endpoints. Add it to close a simple Hamilton cycle and delete uv. Since both u,v were originally free, no original required edge is deleted. This uses the full preceding theorem for either root parity and both target statuses. |
| H18 | Thus any free-target input not handled by the conditional predecessor step has fully independent holes, including root--W nonadjacency. This discharges the exceptional source condition H08 in the reduced census. It does not license that reduction at 14/16/18 without their missing predecessor. |

The independent Python boundary checker verifies all 1994 feasible
positive-crossing face-population cases for these rows: completion parity,
even-port availability, positive balanced A holes, exact B populations,
all local theorem ranges, and nonempty D when u lies in A.

Adversarial cases explicitly examined: a=b=0 (excluded because no even
source); a=0,b=2 with two forbidden odd sources (explicit source hypothesis
is necessary); a free v consumed as a source (forbidden); an odd source
whose mirror is u (forbidden); a mirror that is a crossing port (impossible
by shortness); a covered crossing target temporarily isolated after D
deletion (handled); D empty (only the accepted delta=0 boundary); a
tag-carrying conflict path (suppression records the tag); zero B holes
(perfect-matching cycle import); rs already in the Hamilton path
(impossible); and adding uv then accidentally deleting an original edge
(uv originally joins two holes). No counterexample or open obligation was
found within the stated scope. There are no asymptotic, analytic, or
probabilistic interchanges to justify.

## Independent exhaustive census and exact raw-set verification

HIGHER_Q5_FULL_REVIEW_check.cpp is an independent W-first implementation.
For each k it enumerates every k-subset W of the 32 odd vertices. It removes
all neighbors of W from the 31 nonzero even vertices, then enumerates every
(k-1)-subset Z of the remaining vertices. This enumerates each Z,W pair
exactly once, and enumerates precisely Z union W independent. Pruning when
too few eligible even vertices remain is sound because adding W vertices
can only shrink that set. This reverses the producer's Z-first algorithm.

For each pair and each of the three targets it records target status,
then the free root-adjacent branch before any cut. For every other record
it checks all six target-facing actual faces using bitmask populations.
A successful row is exactly b>=1 and a<=b<=a+2. Source existence is
automatic here: covered-target b=a+2 by H08, or free-target root adjacency
was excluded before testing. The independent implementation does not use
the old K>=7 eligible-only shortcut or producer counts to classify records.

The exhaustive totals are 166914212 distinct Z,W geometries and 500742636
target-marked records. Every eligible, predecessor-adjacent, known-cut and
residual count agrees exactly with the manifest and all four producer JSONs.

Each of the 24 frozen raw files was then read completely. Every record
has the exact byte width 2k-1, increasing nonzero even Z, increasing odd W,
the correct target status, Z--W independence, no conditional root-adjacent
free branch, and no successful cut in any of the six coordinates. Complete
records are strictly lexicographically increasing, proving no duplicates.
EOF also checks there is no partial trailing record. In each file the raw
record count equals the independently enumerated residual count. Therefore
raw is a subset of the independently defined finite residual, has no
duplicates, and has equal cardinality; **the two sets are exactly equal**.
This is a full coverage proof, not a producer-hash or count-only check.
In total 20088984 raw records were individually validated.

| Holes | Covered residual v1/v7/v31 | Covered total | Free residual v1/v7/v31 | Free total |
|---:|---|---:|---|---:|
|12|2364029 / 2632038 / 2824049|7820116|0 / 80622 / 107984|188606|
|14|2760900 / 3125851 / 3365650|9252401|0 / 94182 / 137860|232042|
|16|725370 / 834303 / 912495|2472168|0 / 15786 / 27060|42846|
|18|22260 / 27735 / 30810|80805|0 / 0 / 0|0|

No matching-realizability filter is used. Every original matching in the
reduced domain induces one of the enumerated geometries, so enumeration
of unrealizable geometries enlarges the domain safely. Conversely a raw
record is not a negative extension certificate and counts no individual
matching. These are labeled geometry counts, not automorphism orbit counts.

Reproduction: compile the independent C++ source with g++ -std=c++17 -O3
-mpopcnt; run it with arguments [this directory] k for k=6,7,8,9, saving
stdout to HIGHER_Q5_FULL_REVIEW_k{k}.json; then run the independent Python
checker. The C++ opens only raw producer files for reading and writes only
stdout. The Python writes HIGHER_Q5_FULL_REVIEW_check.json.

## Accepted scope and remaining work

Twelve-hole reduced residuals are exactly covered7820116/free188606 after
the now-available complete ten-hole predecessor reduction and these rows.
They are initial near-balanced-filter residuals; they precede reuse of
other accepted marked registries, T63/T44 or other local inputs. They are
not a final count of difficult or unproved matching cases.

The same exact numerical partition holds at 14/16/18, but interpreting
its root-adjacent free bucket as solved requires the corresponding complete
preceding layer. In particular the empty eighteen-hole free residual does
not prove the full eighteen-hole free theorem while sixteen-hole closure
is missing. No full12/full14/full16/full18 theorem is accepted here.
No unrestricted multiple-omission local input, no new T37 theorem and no
full P6 assertion follows from this audit. The producer's illustrative
T37 rows give holes (3,7), two majority omissions, and 22 complementary
endpoints, consistent with a rank1024 target; no such certificate is
provided or assumed in this package.

The audit has zero open FATAL/CRITICAL/MAJOR issues for its declared scope.
The deterministic census and raw-domain checks are complete. Mathematical
acceptance remains same-family/provisional relative to the named imports;
the accepted upstream large certificates were not regenerated here.
