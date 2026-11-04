# Independent fourteen-hole Hall and complete free-target review

**PASS.** All 8,623 explicit Hall certificates are valid. Their exact
complement has 3,923 covered-target records and zero free-target records.
Together with the finalized near-balanced, registry-reuse and cached-local
applications, this proves the entire fourteen-hole free-target branch:
for every short 25-edge matching in Q6 and every prescribed pair of
opposite-parity uncovered endpoints u,v, there is a Hamilton u--v path
containing the matching, using only short new physical edges.

This does not prove the covered-target branch, full fourteen holes, or
full P6. The 3,923 retained geometries are unresolved sufficient-route
residues; their realizability is not asserted. The 8,623 excluded geometries
cannot occur as exact holes of an original matching, rather than being
counterexamples to Hamilton extension.

Reviewer `/root/twelve_hole_final_assembly_review`, user-selected GPT-6.1-sol
/ high, applies ARIS proof-checker independently of the Hall producer.
The explicit model route overrides skill defaults. Assurance remains
same-family/provisional relative to named accepted imports, without Lean
or cross-family formal verification. No producer or main-state file changed.

## Direct Hall proof and finite gate

A short matching with fourteen holes has seven holes of each parity and
25 covered vertices of each parity. Let E,O be the actual covered even
and odd sets. Every vertex of E must be paired bijectively with a distinct
vertex of O at cube distance one. If a nonempty S subset E has its entire
covered odd neighborhood T=N(S) intersect O strictly smaller than S, the
partners of S would give an injection S into T, a contradiction. This is
a direct finite counting proof, independent of any matching solver.

The fresh `FOURTEEN_HALL_REVIEW_check.py` imports no producer module and
executes no producer checker or search. It validates all 18 manifest-bound
hashes and sizes, reads the six thirteen-byte source streams and validates
all 12,546 records: sorted unique Z6/W7, correct parity and range, root
exclusion, nonroot hole independence, exact covered/free target status,
and full hole independence for free-target records. It checks unique
records within each target/status domain and seven holes per parity.

Each of the 8,623 little-endian `<BBIQQ` records is independently parsed.
The target/status must identify an actual input stream, the source index
must be in range and unused, and the S mask must encode a nonempty subset
of the actual covered even vertices. The checker generates every one of
the six cube neighbors of every vertex of S, intersects with the actual
covered odd set, and requires exact equality with the stored T mask.
It then checks the strict deficiency. No omitted neighbor or diagnostic
solver verdict can certify an exclusion.

The independently obtained witness-size histogram is 7,996 certificates
with (|S|,|T|)=(1,0), and 627 with (25,24). Indices are unique within each
marked source domain, which prevents duplicate certificates from inflating
the deletion count. Deleting exactly these indices in original source
order reproduces all six output streams byte for byte, including empties.

| Target/status | Input | Verified exclusions | Exact remaining |
|---|---:|---:|---:|
|1 covered|3105|2265|840|
|1 free|0|0|0|
|7 covered|3613|2425|1188|
|7 free|18|18|0|
|31 covered|5810|3915|1895|
|31 free|0|0|0|
|Total|12546|8623|3923|

## Complete free-target assembly and hypothesis ledger

| ID | Obligation and discharge |
|---|---|
| H01 | Normalize any original free u by translation to0, possibly reversing parity globally. Coordinate permutations send the opposite free v to1,7,31 by its odd distance. These automorphisms preserve short matching containment and Hamilton paths; inverse transport restores the original endpoints. |
| H02 | Every fourteen-hole matching has 25 short edges and seven holes per parity. The source record format Z6/W7 therefore has precisely the original-domain dimensions. No direction-use filter or unproved matching feasibility criterion narrows the domain. |
| H03 | If any two holes x,y are adjacent and xy differs from uv, adding xy leaves at least one of u,v free. Apply the complete twelve-hole endpoint theorem with that endpoint as root, allowing the other endpoint to have become covered. Reverse the path if needed. It contains the original matching. |
| H04 | If the adjacent pair is uv, add uv and choose another remaining free root r. Choose any short neighbor s of r and use full twelve holes to obtain a Hamilton r--s path containing uv, with covered targets allowed. Add rs to close a cycle and delete added uv. The endpoint edge rs cannot already belong to a Hamilton path on64 vertices. Both u,v were originally free, so no original required edge is deleted. This covers the special augmentation boundary. |
| H05 | The remaining free domain may thus assume the entire hole set independent. The accepted HIGHER_Q5_FULL_REVIEW census and near-balanced row theorem cover all other cut cases and leave exactly232042 free records. Legal source exclusions include free target and root mirror; in this independent domain the latter cannot be a hole. The published/accepted local and zero-crossing imports retain their declared scopes. |
| H06 | The historical fourteen-hole predecessor assumption in the near-balanced source is now discharged by finalized TWELVE_HOLE_FULL_REVIEW. This is the full theorem including covered targets, which H03/H04 need. FOURTEEN_REUSE_REVIEW and FOURTEEN_CACHED_REVIEW explicitly bind that final PASS and mark the predecessor condition discharged. No full fourteen-hole theorem is used in a premise. |
| H07 | Final FOURTEEN_REUSE_REVIEW proves every actual selected cut/source construction uniformly over every realizing original short matching, and its exact source complement leaves318 free records:18 at v7 and300 at v31. Its local matchings may be arbitrary complete-graph matchings, so completion/compression edges satisfy the imported quantifiers. |
| H08 | Final FOURTEEN_CACHED_REVIEW accepts exactly20 needed universal local statements and their actual applications. Its exact residual leaves the same18 v7 free records and zero v31 free records. No other383 candidate local-rank claims are imported. Source and output byte streams are hash-bound at both consecutive interfaces. |
| H09 | Every one of those18 actual free records has a strict Hall certificate checked above. Thus no original short matching realizes any remaining free record. Combining all sufficient construction routes with these impossible exact inputs proves the complete free-target theorem, rather than inferring a Hamilton theorem from a failed search. |
| H10 | The covered complement remains840+1188+1895=3923. Hall exclusion says nothing about existence or nonexistence of a Hamilton extension for retained geometries. Consequently full fourteen holes and full P6 remain open. |

The independently checked free chain is:

| Target | Near-balanced residual | Reuse residual | Cached residual | Hall residual |
|---|---:|---:|---:|---:|
|1|0|0|0|0|
|7|94182|18|18|0|
|31|137860|300|0|0|
|Total|232042|318|18|0|

## Source bindings, independence and adversarial checks

The four formal imports HIGHER_Q5_FULL_REVIEW, TWELVE_HOLE_FULL_REVIEW,
FOURTEEN_REUSE_REVIEW and FOURTEEN_CACHED_REVIEW were read at their exact
scopes and checked PASS. All 324 distinct directly declared source/import/
checker bindings in those reports were rehashed successfully. The cached
gate binds the exact finalized reuse report, and both bind the same full12
predecessor hash. The Hall manifest's input streams are the exact cached
gate outputs. Initial census-to-reuse and reuse-to-cached stream hashes
are checked on both sides of every interface; no agreement of counts alone
is used to identify record sets.

Frozen Hall proof SHA256:
`bdd7d357556cd0eb7a66d4dcab21b0e860754092c5ec6e957e64af27124f0fa4`.
The companion JSON binds the actual manifest, evidence, accepted imports
and this independent checker. Large already accepted upstream connectivity
certificates and whole-domain censuses are not rerun. They are explicit
accepted imports, not evidence produced by this new Hall checker.

Counterexample attempts include S containing a hole, wrong parity or empty
S; T omitting covered neighbors or including uncovered ones; non-strict
deficiency; repeated or out-of-range indices; wrong free-target status;
using non-independent free records as the accepted cut domain; residual
reordering or duplicate deletion; a stale predecessor gate; applying only
a two-free-endpoint predecessor after augmentation; the special uv edge;
and treating a retained geometry as a realized matching or counterexample.
The explicit finite checks and H01--H10 discharge these attempts.

The dependency graph is accepted local/transfer theorems and full12 ->
near-balanced fourteen-hole preprocessing -> accepted reuse -> accepted
cached positives -> explicit Hall exclusions -> free-target assembly.
Nothing depends on this Hall conclusion or on full14/P6. All mathematical
obligations are finite or elementary; there are no hidden asymptotic or
limit-interchange conditions. No FATAL, CRITICAL, MAJOR or MINOR issue
remains within the declared scope.
