# Final A10 orbit: independent universal-proof review

2026-11-01. Reviewer `/root/a10_final_rank_review`; user-selected
`gpt-6.1-sol / high`. ARIS proof-checker; **same-family / provisional**.

**PASS, relative to the explicit published matching-connectivity rank
theorem.** Every arbitrary eleven-edge matching whose uncovered set is
H={0,1,2,4,8,15,23,27,29,30} has a simple cycle on exactly Q5−0 containing
the matching, with all other edges short. The five coordinate images pass.
Neither the completeness of the 17496-record spectrum nor any enumeration
of original matching inputs is a premise of this acceptance.

## Primary import and exact domain

I independently opened the [author repository manuscript](https://pure.tue.nl/ws/portalfiles/portal/99596886/1211.1506.pdf)
and checked its abstract/introduction (PDF pages 1,3), Theorem 3.4 and
Corollary 3.5 (PDF page 9). The repository cover identifies the publication
as Cygan–Kratsch–Nederlof, JACM 65(3), Article 12 (2018),
[DOI 10.1145/3148227](https://doi.org/10.1145/3148227).

The full matrix indexes every perfect matching of the complete graph on
an even number t of labelled vertices; it does not impose bipartiteness,
parity or cube adjacency. The displayed corollary gives GF(2) rank
2^(t/2−1). Its proof explicitly factors the full matrix through 2^(t/2−1)
columns. For t=22 this supplies exactly the upper bound 1024 needed here.
Relabelling the covered vertex set by 0,...,21 preserves the matrix.
The separate real-rank result for a bipartite restriction mentioned in
the introduction is not the imported result. Online text extraction
confirmed the displayed formula; the screenshot request returned a cache
error and was not used as evidence. This is a declared theorem import,
not a claim to have newly proved its technical appendix.

## Independent deterministic checks

New `A10_ORBIT3_UNIVERSAL_REVIEW_check.py` imports or executes no producer
code. It independently checks all 1024 selected forests: twenty distinct
short edges, no vertex 0, degree one at each of the 22 covered vertices,
degree two at each of the nine included holes, acyclicity by DSU, and
eleven components each with exactly two endpoints. Component endpoint
pairings equal their stored matching records. Every selected record also
matches its indexed source record. Each of the 1024 columns is a valid
perfect matching on the exact covered set.

All 1,048,576 matching-connectivity bits are recomputed by unioning both
matchings in DSU and counting components, independently of the producer's
alternating-walk routine. Every bit equals the saved matrix; it contains
158674 ones. Column-first Gaussian elimination using Python integers,
row swaps and elimination below each lowest-column pivot gives exact
GF(2) rank 1024. The producer's saved pivots, combinations, basis
construction and elimination implementation are not used for this rank.
All manifest byte counts and SHA256 values pass, as do all hashes in
the spectrum FROZEN file. The latter binds context without accepting its
full-spectrum exhaustion claim. New evidence and input hashes are pinned
in the adjacent review JSON.

## Proof obligations and dependency graph

| ID | Obligation and discharge | Result |
|---|---|---|
| U01 | Fixed holes and arbitrary complete-graph matching domain coincide with the 22-terminal matrix domain. | PASS |
| U02 | Each selected positive witness is an admissible short forest and compresses to its recorded row matching; independently checked for all 1024. | PASS |
| U03 | Every selected column is valid; every saved entry has the intended labelled-union connectivity meaning. | PASS |
| U04 | Exact independent elimination proves 1024 restricted rows independent. Restriction independence implies independence of the complete rows. | PASS |
| U05 | Published upper bound applies to the full matrix, so these 1024 rows span its entire row space. | PASS |
| U06 | Every original F column is nonzero: cyclically link the second endpoint of each F pair to the first endpoint of the next pair. Eleven disjoint resulting pairs give one alternating 22-cycle. | PASS |
| U07 | If all selected rows vanished at F, all their linear combinations would vanish there, contradicting U05–U06. Thus at least one legal forest row connects to this arbitrary F. | PASS |
| U08 | Compressing and expanding vertex-disjoint paths preserves connectedness, and adds precisely the nine internal holes. The expanded graph has 31 vertices of degree two. | PASS |
| U09 | A common compressed pair is a separate labelled two-edge component, impossible in a connected union on 22 vertices. In particular no direct forest edge can duplicate F. The expanded graph is simple and connected, hence a single 31-cycle. | PASS |
| U10 | All introduced physical edges belong to the checked short forest. Arbitrary long or same-parity edges in F are retained unchanged. | PASS |
| U11 | Coordinate permutations fix 0 and preserve required edges, shortness, vertex set and simplicity. The marked last orbit has five members (also independently reconstructed in the full assembly audit). | PASS |
| U12 | No A8, earlier A10 orbit or P6 theorem is invoked; the dependency DAG is acyclic and universal quantifier order is retained. | PASS |

DAG: imported rank upper bound + valid 1024 forests/columns + independently
full-rank restriction -> complete-row spanning -> nonzero at every F column
-> connected matching union -> simple 31-cycle expansion. No limit,
probability or asymptotic interchange is present.

## Adversarial checks and scope

I specifically tested the possible failure modes of a disconnected
degree-two union, doubled matching pairs, a direct forest edge already
required by F, a compressed hole pair equal to F, a cycle component hidden
inside S, rank computed in the wrong field, a bipartite-only rank import,
and independence restricted to columns being mistaken for spanning without
a full-matrix upper bound. DSU uses every terminal; forest acyclicity and
exact degrees are checked; every successful matrix entry has disjoint pair
sets; the proof explicitly excludes duplicate-pair components. The exact
GF(2) rank and verified full-domain import settle the algebraic concerns.
No counterexample or unresolved proof obligation remains in this scope.

This review accepts only the last five-geometry A10 orbit. The 17496-spectrum
exhaustiveness, full A10 assembly and Q5 consequences are separate claims.
Full Q6/P6 and the complete ten-hole covered-target theorem remain OPEN.
No producer proof, frozen data or main state was modified.
