# Q5 balanced eight-hole cycle closure: independent review

2026-11-01. ARIS proof-checker, reviewer `/root/higher_hole_transfer_audit`,
user-specified `gpt-6.1-sol / high`. Assurance: **same-family / provisional**.

**PASS relative to established K6 and the accepted partial A8 theorem.**
Every arbitrary K(Q5) matching with four holes of each parity has a Hamilton
cycle containing it and using only short new edges. The proof requires
neither full A8 nor A10. The finite980-geometry assertion and every supplied
positive witness were independently verified.

This accepts K8 cycles. It does not establish paths to every prescribed
covered target, full A8, any complete higher-hole Q6 layer, or full P6.
No production proof or main state was modified.

## Fixed inputs and exact imports

The submitted files are `Q5_K8_CLOSURE.md`, `q5_k8_geometry.py`, and
`q5_k8_geometry.json`. Their fixed hashes are:

| File | SHA256 |
|---|---|
| Q5_K8_CLOSURE.md |5e6ec0fdb9114d49ae5cc69dad1044e083b43216a39ea37601f9fa759f50bc68|
| q5_k8_geometry.py |17db8c4d4b08aeb1de46e71b2ca650d26032c86d5e7b0af604cce29896b724fb|
| q5_k8_geometry.json |ce2ca2dda5d00ac9a5f5f0aff0a221286352cf8d6308b90185e7267667a7d5b8|

K6 is the full balanced-six-hole cycle theorem in
`A6_AND_EIGHT_FREE_CLOSED.md`, accepted through `A6_CLOSURE_REVIEW.md/.json`.
Its required matching edges are arbitrary complete-graph edges.

The second import is only the precise partial theorem accepted in
`A8_PARTIAL_REVIEW.md/.json`: every arbitrary K(Q5) matching with3 minority
and5 majority holes, with specified majority omitted hole v, has the
required31-cycle if there is an augmenting short hole edge avoiding v or
a cut containing v with majority-minus-minority imbalance1,2,3. The theorem
allows both numerical parity orientations and all original crossing counts,
long or same-parity matching edges and arbitrary crossing partners.

The partial proof source is fixed at SHA256
`3133642eb22daa30c48253dcd97a3a808e8f3169a4c3256af8240ae0f8bd2a5f`;
its final PASS JSON is fixed at
`1b63584b3cf81c6dc3533cea0fedef60bd8d8d8ed1d7a847ca765326e0dda81f`.
Their current bytes and the report's recorded source hash were checked.
The partial report and its statement were read; no unresolved A8 orbit or
new double-bridge claim is imported.

## Proof-obligation ledger

The canonical assertion is: for every matching F on the32 Q5 vertices whose
uncovered set has exactly4 even and4 odd vertices, there exists a simple
32-cycle C with F subset E(C) subset F union E(Q5). The construction may
select its own free r and adjacent covered y after seeing the holes.

| ID | Obligation and discharge | Result |
|---|---|---|
| K01 | Any short-adjacent hole pair has opposite parity and disjoint endpoints free for F. Adding it leaves3+3 holes; arbitrary-matching K6 applies. The added required edge is short relative to F. | PASS |
| K02 | If augmentation is impossible, all eight holes are independent. The independently enumerated domain contains every such4+4 set, without a symmetry or realizability restriction. | PASS |
| K03 | For each of980 geometries, the certificate gives r among the holes and y a short neighbor outside every hole. Thus y is covered for every F realizing that geometry. | PASS |
| K04 | Replacing r by y changes holes to3 of r's parity and5 of y's parity. The selected cut contains y and has majority-minus-minority imbalance1,2,3 by the direct global-parity calculation. | PASS |
| K05 | Put h=F(y). The vertices r,y,h are distinct, h is outside all original holes, and hr does not meet any other required edge after yh is removed. F' is a matching with exactly the certified hole set. Mate parity and length are unrestricted. | PASS |
| K06 | All nonforbidden holes of F' are original holes, so original independence ensures no minority--nonforbidden-majority adjacency. The partial A8 cut theorem therefore applies directly, with omitted hole exactly y, for every possible h and every other original matching edge. | PASS |
| K07 | The imported31-cycle avoids y and contains the required auxiliary edge hr. Replacing that edge with h-y-r inserts a new vertex into one cycle, yielding a simple32-cycle. The original yh is restored and yr is short. | PASS |
| K08 | Every other edge of F is retained by F'. The auxiliary hr disappears. The only surviving edges outside F are short imported cycle edges and yr. No shortness or bipartiteness of original F is assumed. | PASS |
| K09 | All40 choices of(r,y) for each independent geometry are checked as ordered pairs: eight roots and five short neighbors. The successful-pair histogram is exactly40:580,18:320,24:80, and all980 stored positive witnesses are valid. | PASS |
| K10 | The selected r,y depend only on the hole geometry; the subsequent mate h may be any of23 other covered vertices. Arbitrary-matching quantification of the partial theorem covers all these possibilities, not one representative matching. | PASS |
| K11 | The acyclic dependency chain is established K6/partial A8 + finite geometry -> K8. Full A8, A10, K8 itself and higher-hole P6 are absent from the used partial theorem's proof. | PASS |
| K12 | The statement concludes a cycle with freely selected construction vertices, without promising a path to an externally prescribed covered target. Its stated scope matches the proof. | PASS |

All twelve obligations are discharged. There is no open severity issue and
no proof modification was required. No analytic interchange, probability,
asymptotic or induction obligation occurs in this proof.

## Independent deterministic checks

`Q5_K8_REVIEW_check.py` imports and executes no producer code. Adjacency is
computed from pairwise Hamming distance. The checker chooses odd four-sets
first, then chooses even four-sets from their complete common nonneighbor
set. This reverses the producer's enumeration. Its exact980-set domain
equals the JSON rows, with no duplicate or missing geometry.

For each geometry it directly forms every new hole set after replacing r
by y, calculates the majority/minority classes and the five actual faces
containing y, and tests the imbalance predicate. All39,200 root-neighbor
pairs are checked;30,880 are successful. The successful-pair histogram is:

| Successful pairs per geometry |18|24|40|
|---|---:|---:|---:|
| Geometries |320|80|580|

Each of the980 stored witnesses is checked independently for root and
neighbor membership, short adjacency, covered-neighbor status, exact cut
and reported imbalance. The stored witness imbalances occur264 times at1,
164 times at2 and552 times at3.

For every stored witness, the checker also lets h range over all23 possible
mates of y, realizes that choice by an arbitrary complete-graph matching,
and checks the replacement has24 distinct covered endpoints and exactly
the prescribed new holes. All22,540 replacement checks pass. This is a
bookkeeping test, not exhaustive enumeration or a test of matching-extension
existence; the universal proof follows from K05--K08 and the imported
arbitrary-matching theorem.

Counterexample attempts targeted a neighboring y that is another hole,
h=r, h another old hole, a required same-parity hr, a wrong omitted vertex,
local/global parity reversal, a bridge y-r already present on the31-cycle,
and a successful-pair count mistaken for all covered targets. Independence,
the free-root and matching conditions, exact marked-cut calculation,
the arbitrary-matching import and omission of y respectively exclude these
failure modes. The final target scope is explicitly kept at K8 cycles.
No counterexample was found.

The independent result JSON records source/dependency hashes and all counts.
The geometry checker and this review do not recertify the large matching
certificates underlying K6 or partial A8.

## Final accepted scope

Full Q5 K8 cycle extension is proved relative to the listed accepted inputs,
with same-family/provisional assurance. Complete prescribed covered-target
balanced-eight-hole endpoints, full A8, A10, complete10--18-hole Q6 layers
and full P6 are not proved by this result. Earlier reviews and the main
claim ledger remain untouched.
