# Independent review of the ten-hole theorem with both endpoints free

2026-11-01. Fresh reviewer `/root/ten_hole_free_closure_audit`, user-selected
`gpt-6.1-sol`, reasoning `high`. The user route overrides the ARIS
proof-checker skill's model/effort default. Review assurance is
**same-family / provisional**; no formal or cross-family acceptance is claimed.

**Verdict: PASS relative to the explicitly imported, accepted theorems.**
For every short 27-edge matching M of Q6, every free root u and every free
opposite-parity target v, a Hamilton u–v path containing M exists with all
new edges short. The finite coverage obligation is independently discharged.
There are no open mathematical gaps in this exact both-free-endpoint claim.
Covered targets at ten holes, the complete 12–18-hole layers, unrestricted
T15 and full P6 are outside the verdict.

The audited proof SHA256 is
`eae99ab5636bf70135779cc4fcd63b1b77ecb52a115f204d93a2a204e0973243`.
The unified-transfer source has SHA256
`75f481593ecff17f888102e687c0c669f8dd96cdd5ce953434fb93de644df0ed`;
its final independent report is PASS, not pending, at this review's emission.
The proof draft's statements that review is pending are historical metadata.
No production proof or main state was edited.

## Import boundary and acyclic dependency map

The proof imports the complete eight-hole endpoint theorem, including a
covered target; the accepted unified conditional transfer with its eight
ten-hole basic rows; exactly the 24 complete marked T15 cores named in the
proof; and the Q4-rich-gluing consequence for a split T15 geometry, including
zero original crossings. These are semantic mathematical imports with their
whole arbitrary-complete-graph-matching quantifiers, not conclusions inferred
from geometry counts. Their underlying large matching certificates are not
rerun here.

The reviewer read the complete ten-hole assembly and unified transfer, the
exact eight-hole theorem and final review, and the complete Q4-rich-gluing
argument and final review. The complete-core registry is checked against the
fixed labeled representatives and the final eight-hole review's registry;
the multi-core review scopes explicitly cover their indicated IDs and both
marked omissions. All relevant reports are PASS. The frozen import manifest
contains 33 theorem/review file hashes, all checked again by the new checker.
The three direct imported sources match their final reports' audited hashes;
the named core reports also match the final eight-hole audit's bindings.

The dependency direction is Q4/published base inputs → Q5 local endpoint,
cycle and marked-core theorems → unified transfer; separately the accepted
complete eight-hole theorem → endpoint-symmetric augmentation. Those branches
plus the independently regenerated geometry coverage imply this ten-hole
both-free theorem. No upstream node invokes this result, ten-hole covered
targets, a higher-hole layer, or full T15/P6. Reading a prior audit as the
explicit source of an imported theorem does not replace the new coverage
check of the ten-hole candidate.

## Quantifiers, symbols and obligation ledger

M is a matching of 27 short edges on the 64 Q6 vertices; u,v are distinct
uncovered vertices of opposite parity. After translating u to 0, Z is a
four-element nonroot even-hole set and W a five-element odd-hole set with
v in W. For a coordinate i, A is the face containing v and B its complement;
a and b count Z and W in A. S is a two-element bridge-source set, m the
unique final B minority hole, and Y the marked pair of bridge mirrors.
The final local geometry consists of m, three included majority holes and
two omitted majority holes. A core ID refers to the index in the fixed
`t15_analytic_geometry.json` residual-orbit representative list, not a
mutable current-core ledger.

| ID | Location | Obligation and discharge |
|---|---|---|
| H01 | L9–11, L53–57 | Every short edge covers one vertex of each parity, so the holes split 5:5. Translation and coordinate permutation preserve shortness, matching containment, freedom, specified endpoints and Hamilton paths. Translation can reverse global parity; the normalized root is even. |
| H02 | L38–44 | For a hole edge xy other than uv, adding xy gives a short 28-edge matching. At least one of u,v remains free, since covering both would require the edge uv. Root the full eight-hole theorem at that endpoint and target the other, which has opposite parity even when covered. Reversal restores the stated order. The augmented edge can remain in the output. |
| H03 | L46–51 | If xy=uv, the augmented matching has eight free vertices. Choose any one as r and any short neighbor s. They have opposite parity, so the full eight-hole theorem applies whether s is covered or free. In a simple Hamilton r–s path with 64 vertices, rs cannot already be an edge: adjacent endpoints would otherwise give a path of length one or a vertex repetition. Since r is free, rs is also not required by M+uv. Adding it gives a single Hamilton cycle containing M+uv. Deleting uv leaves the requested path and deletes no edge of the original M. |
| H04 | L53–57 | H02–H03 remove every configuration containing any adjacent pair of holes, including root or target adjacency. In the remaining domain all ten holes are independent. The odd target has weight 3 or 5 and can be normalized to 7 or31. These reductions cover every matching; no realizability filter is needed. |
| H05 | L61–66 | All eight rows agree exactly with the accepted unified transfer at k=5. In its odd-consumption cases a≥1 ensures the bridge selection condition. All original crossing counts are covered, including zero by its five-direction import. |
| H06 | L70–73 | In row(3,2), choose two distinct nonroot even A holes. The unified formula s=a+1−b=2 gives B counts(1,5). The unique B member of Z is the minority, B's three W vertices are included, and the two source mirrors are the omissions. These are exactly the transfer's final holes even if the original root lies in B, since that root is consumed by tagged closure. |
| H07 | L74–77 | In row(1,4), t=b−a−1=2 gives B counts(5,1). Sources are selected among W∩A excluding v and the mirror of root. Four sources with at most two exclusions leave at least two. Full ten-hole independence actually excludes the root-mirror odd hole already. The unique W∩B vertex is the minority and the three Z∩B vertices are the included majority. The omitted pair is again the source mirrors. |
| H08 | L70–81 | Every source is free and the two mirrors are distinct. No mirror coincides with an included hole: this would be an adjacent original hole pair. Root mirror is explicitly excluded in H07 and impossible by parity in H06. Independence also keeps the minority distinct. Hence the marked projection has exactly six distinct holes with the intended roles. |
| H09 | L79–82 | XOR by the B minority makes its cut bit zero for every B vertex, and deleting that coordinate is a genuine Q5 isomorphism. It takes minority to0 and majority to odd labels. The checker verifies every such map on all384 face/minority pairs, including all pairwise distances. It transports the omitted pair as a marked pair, without interchanging roles with included vertices. |
| H10 | L20–28, L81–84 | Reconstruct all120 five-coordinate permutations of each of the exact24 accepted marked representatives. The resulting1600 geometries are backed by complete arbitrary-K(Q5)-matching theorems. Separately accept exactly the stated geometric split condition: a coordinate has two of the five majority holes on its one-face and separates the omitted pair. This invokes the accepted split theorem for all crossing counts. |
| H11 | L88–106 | A fresh exhaustive C++ census chooses every admissible even quadruple, then every odd quadruple besides the specified target, requiring independence also from root0. It evaluates all six cuts, all basic rows, and all legal source pairs in the two T15 rows until a valid witness is found. Every eligible geometry is discharged, as quantified in the displayed assertion. A second Python enumeration reverses the parity order and independently confirms both complete-domain totals. |
| H12 | L83–84, L111–114 | The cut/bridge/core witness depends only on the hole geometry. Its local input holds for every arbitrary compressed matching arising from every realizing original short M. Therefore finite geometry coverage combines with the transfer's universal matching quantifier. Expansion retains every original edge, and auxiliary edges are removed or expanded; only short new edges survive. H02–H04 plus H05–H11 cover all inputs of the exact theorem. |

There are no analytic interchanges, asymptotic constants, probabilistic modes
or parameter-uniform limits in this finite graph argument.

## Independent exhaustive coverage

New standalone artifacts are `TEN_HOLE_FREE_REVIEW_check.cpp` and
`TEN_HOLE_FREE_REVIEW_check.py`. Neither loads or calls a producer module,
producer census, saved producer residual binary, producer lookup or dynamic
core ledger. The only geometry input is the fixed marked representative list;
the acceptance lookup is regenerated independently. The imports manifest
records theorem scopes and hashes only.

| Target | All independent geometries | Basic eight rows | Complete-core witness | Split witness | Remaining |
|---:|---:|---:|---:|---:|---:|
|7|2,919,186|2,897,100|19,175|2,911|0|
|31|3,575,055|3,549,870|20,586|4,599|0|
|Total|6,494,241|6,446,970|39,761|7,510|0|

For each target the outer enumeration has exactly12,650 eligible even
quadruples. Each permitted odd set containing v is generated once by choosing
its other four elements in increasing order. This proves domain exhaustiveness
and absence of duplicates by construction. Independence between same-parity
holes is automatic in a cube; the code explicitly excludes all even–odd
distance-one pairs, including the root. The independent reverse count first
chooses W and sums the binomial number of allowed even quadruples. It gives
exactly2,919,186 and3,575,055 as well.

The regenerated acceptance lookup has1,600 complete-core orbit images and
31,640 marked split geometries, hence33,240 entries. These counts are merely
lookup accounting, not an assertion that all entries occur in the Q6 input
domain. Every one of the47,271 nonbasic geometries has a concrete witness in
`TEN_HOLE_FREE_REVIEW_witness.tsv`: target, original four Z vertices, original
five W vertices, cut coordinate, two bridge sources, acceptance kind, and
core ID/permutation index or split coordinate. Python independently replays
all47,271 records from their original Q6 coordinates, checks source legality,
hole independence, exact omitted/included roles, actual minority translation
and projection, then verifies the actual representative permutation or split
criterion. It also checks witness geometry uniqueness.

The proof's producer diagnostics56805/51935 concern a larger domain allowing
root–W adjacency. They were not used, nor are those producer counts certified
by this review. They are unnecessary: H02–H03 resolve all root-adjacent input
geometries analytically, and the exact remaining domain is checked from zero.
The minority/included-hole short-augmentation shortcut is not needed by the
new lookup or proof.

## Adversarial checks and validation

The counterexample pass targeted an added hole edge covering exactly one
specified endpoint; uv itself as the only adjacent hole edge; a covered s in
the cycle construction; root in either face; the original target as a bridge
source; a source mirrored to root; identical or role-swapped projected holes;
parity reversal by minority translation; omitted vertices on the same side of
an alleged split; and an acceptance derived from only a sampled matching.
The argument and fresh checks exclude each failure mechanism. In particular,
H03 handles the uv boundary directly, source exclusions are replayed from
original coordinates, and no arbitrary intermediate matching is restricted
to short edges. No counterexample or open gap was found in a used implication.

Validation completed with assertions enabled using `g++ -O3 -std=c++17` and
Python3.14. The final checker succeeded after the independent reverse count,
33 frozen import hash checks and full witness replay were added. Exact source,
lookup, result and witness hashes appear in the check JSON and review JSON.
The review writes only its own new checker, frozen import manifest, positive
witnesses and audit artifacts; no production proof or global state is changed.
