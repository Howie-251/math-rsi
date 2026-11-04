# Ten-hole row (4,5) and exact combined residual: independent review

2026-11-01. ARIS proof-checker `/root/a10_final_rank_review`; explicit
`gpt-6.1-sol / high`; **same-family / provisional**.

**PASS relative to the final accepted full Q5 endpoint and uniform transfer
imports.** Row (4,5) uniformly covers 70 additional ten-hole covered-target
geometries, 10/30/30 for targets1/7/31. These additions are disjoint from
the separately accepted marked-T63 additions of12916. The exact combined
remaining domain has12910/12696/15630 records, total **41236 OPEN**.
These are unresolved geometries, not counterexamples. Complete ten-hole
covered targets, remaining complete Q6 layers and full P6 remain OPEN.

## Input gates and scope

The submission is `TEN_COVERED_Q5_ENDPOINT_APPLICATION.md`, with its filter
source, frozen output JSON and remaining files. `Q5_A10_FULL_REVIEW.json`
is final PASS before this review: its accepted consequences include the
balanced five-plus-five-hole Q5 endpoint statement for every arbitrary
complete-graph matching, every free root and opposite-parity target.
`Q5_T63_COMPLETE_SPLIT_REVIEW.json` and
`TEN_COVERED_T63_SPLIT_REVIEW.json` are also final PASS before the combined
gate. Their marked split scope, not unrestricted T63, is the only T63
result used. The uniform-transfer source/review and accepted preceding
54222-record domain are source-bound by current SHA256 comparisons.

The application quantifies over every short Q6 matching realizing each
accepted independent-hole geometry, with free even root u=0 and odd covered
target v. Its geometry test does not select or sample a favorable matching.

## Semantic proof replay

The old transfer's stated b<=3 bound served its limited A-side endpoint
imports. It is not sufficient merely to cite that old numerical statement
for b=5. I replayed its construction with the newly accepted local theorem:

1. In the target-oriented coordinate face A assume (a,b)=(4,5), so every
   nonroot hole lies in A. In the even-consumption construction s=a+1−b=0;
   there are no bridge sources or marked B omissions.
2. For c>0 and u in A, shortness gives even c, hence c>=2. Pair all A
   crossing ports into arbitrary completion D and let r=u. The completed
   A matching has exactly five holes per global parity. D is nonempty.
3. For u in B, port imbalance p_even−p_odd=b−a=1 supplies an even port r.
   Pair all other ports into D, leaving r free. The completed A matching
   again has exactly five holes of each parity. The c=1,D=empty boundary
   is legal. An arbitrary D may create long/same-parity requirements;
   the new full Q5 endpoint theorem explicitly accepts them.
4. In either case the covered odd v is an allowed opposite-parity target.
   Take its Hamilton r–v A path, delete D and attach every original crossing
   edge. Add the labelled temporary tag uv. If u in A, deleting a nonempty
   D separates the two true endpoint segments before tagging. If u in B,
   tagging extends the terminal segment to the previously untouched u.
   Thus the tagged graph is a forest and compresses to a matching T on B.
5. There is no Y conflict set because s=0. T and the original internal B
   matching have disjoint covered endpoints: its ports and B-root were
   previously free. The complete B matching L has hole counts
   (k−a−1,k−b+s)=(0,0). Apply the imported arbitrary perfect-matching cycle
   extension theorem, expand each recorded transferred path, and delete
   the unique tag. Every original edge is restored. All surviving new
   physical edges are short; D and compressed edges do not survive.
6. For c=0 use the explicit established five-direction endpoint input as
   in the accepted transfer. No higher-hole Q6 theorem is used to obtain
   the new Q5 endpoint import or establish this cut application.

This proves the actual new row without extrapolating an unsupported bound.
The proof also includes v being a crossing port and the root-face boundary
cases covered by the accepted tagged-forest construction. There is no
hidden dependence on unproved unrestricted T63 or full ten-hole coverage.

## Independent full scan and exact partition

New `TEN_COVERED_Q5_ENDPOINT_REVIEW_check.py` imports or executes no producer
code. It validates every input record's labels, parity, sorted halves,
distinct holes, free root, covered target and Z–W independence. For every
record it constructs all six actual target-oriented faces as vertex sets
and counts their Z and W intersections. Every qualifying real cut is
recognized. All70 stored producer witnesses agree with this independent
calculation, including their original record indices and minimum cut.

| Target | Accepted input | New Q5 row | New marked T63 | Combined remaining |
|---:|---:|---:|---:|---:|
|1|16920|10|4000|12910|
|7|17022|30|4296|12696|
|31|20280|30|4620|15630|
|Total|54222|70|12916|41236|

Each of the70 newly covered records belongs to the accepted T63 remaining
set. Therefore the two additions have empty intersection, checked by exact
set operations, not inferred from total subtraction. The endpoint-only
remaining domain is54152. Both that domain and the intersection remaining
after both routes are reconstructed in original order, compared byte for
byte and as sets, and checked for duplicates. Every frozen hash matches.
The combined output hashes are:

| Target | SHA256 |
|---:|---|
|1|a13a090fae7b46b71a6e37979c3b9cf84be600db1669937f0bb06c6ec180c8e9|
|7|4bbd08ec437acb296fdb08ef4ae4750ce1e4e3faacc3f24a87db846bedc92586|
|31|1df23351b5be3da9c934ef5e83df12f02cf60ce92375f76554050eecaec598e4|

## Counterexample pass and decision

Reviewed failure candidates were b=5 being outside the former limited
endpoint import, no even crossing root, empty D, accidental tag closure,
arbitrary artificial edges outside a short-only local theorem, an original
B matching conflict, a producer cut with wrong target orientation, overlap
with the12916 accepted additions, and losing residual records through
numeric subtraction. The new endpoint theorem, explicit parameter replay
and exhaustive independent sets/bytes checks exclude these failures.
No open mathematical issue remains in the stated application scope.

The dependency graph is accepted Q5 A8/A10 -> all balanced Q5 endpoints
-> row(4,5); independently accepted marked-T63 application -> its positive
set; exact disjoint union/intersection ->41236 remaining geometries. No
reverse dependency occurs. Semantic assurance remains provisional within
the same model family. Producer/frozen files and main state were not edited.
