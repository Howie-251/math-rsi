# Complete T15 core8: fresh proof review

Verdict: **PASS, same-family / provisional**, relative to the explicit Q4 N14
and balanced-table imports. No open FATAL, CRITICAL, MAJOR, or MINOR
mathematical issue was found. This review covers core8 only.

Reviewer: `gpt-6.1-sol`, reasoning `high`, fresh context, task
`/root/t15_core8_complete_audit`. These are the requested actual settings;
the ARIS proof-checker skill's nominal Astra/ultra settings were overridden
by the user. Instruction source:
`F:/c4free-hypercube-main/ARIS/skills/skills-codex/proof-checker/SKILL.md`.
No cross-family semantic acceptance is claimed. No theorem or production
source was edited, and no parent proof state or ledger was updated.

## Precisely accepted statement

For every matching F of the complete graph on Q5 whose uncovered vertices
are exactly {0,1,2,7,13,31}, there exists a simple cycle with vertex set
Q5 minus {1,2}, containing every edge of F, whose remaining edges have
Hamming distance one. Original edges have no length or parity restriction.
Transporting the whole construction proves all cube-automorphic images
with their transported marked omissions.

The imported assumptions are Q4 N14 in its complete-graph matching scope
and the complete audited balanced tables. I read their precise statements
and the prior balanced-bridge review, and checked exact hash agreement of
both N14 binary representatives and all thirteen balanced tables with that
review. Those imports were not reproved from scratch in this audit.

## Obligations and hypothesis discharge

The acyclic dependency graph is: imported N14 -> A cycle and connected
boundary pairing; imported balanced tables -> B positive/negative outputs;
complete inverse families + disconnected blockers -> large-crossing
closure; complete B spectra -> small-crossing exception lists; fully
verified positive certificates -> all remaining original inputs. No T15,
eight-hole, or P6 conclusion enters an upstream assumption.

| Obligation | Independent assessment |
|---|---|
| Marked geometry | Swapping bits 0 and 1 sends the holes to {0,1,2,7,14,31}, preserves {1,2} as a set, and preserves cube edges. Under A=2v+1, B=2v, the holes are A:{0,3,15}, B:{0,1,7}, with omissions A:0, B:1. |
| Crossing domain | Each face has thirteen original covered vertices. Thus 13-c is nonnegative even, giving exactly c=1,3,5,7,9,11,13. No zero or even case is omitted. |
| N14 application | X_A and bridge z are disjoint free vertices for F_A. Any perfect matching D on X_A union {z} completes F_A to seven edges with exactly the same-parity holes 0 and w, where w is the other bridge. The prescribed omitted vertex is 0. |
| Connectedness | Deleting nonempty D from the simple N14 cycle leaves vertex-disjoint spanning paths. The endpoint pairing R and D form a connected multigraph after path contraction, including doubled edges where appropriate. |
| Internal mirror | The B mate k of z is internally covered, whereas q is a crossing port; hence k differs from q. Suppression at z replaces kz and its attached path by kq, giving a matching on exactly the twelve nonhole balanced vertices. This inverse is unique once the oriented edge kq and original F_B are specified. |
| Occupied mirror, c>=3 | d=C inverse(z) is an A covered port, different from hole z. Prescribe zd in D. Replace zd by the short bridge and original crossing through z_B, and delete D'. Since D' has (c-1)/2>=1 edges, this breaks a single simple cycle into paths, without a surviving closed component. Their remaining endpoints are exactly X_B minus {z}. |
| Complete inverse accounting | Enumerating every negative L, every occupied-mode m-edge subset, and every internal-mode oriented kq and (m-1)-edge subset yields every forbidden output and no additional unsupported output. The reconstructed families equal every saved family exactly. |
| Blocking implication | Pulling a blocker through the arbitrary crossing bijection preserves connectivity. Every forbidden output has disconnected union with this blocker, while N14 supplies a connected union. Therefore the supplied output is positive. Absence from all inverse families also guarantees positivity. |
| Larger crossings | All c>=7 families have explicit checked blockers. Every internal c=5 family does too. The occupied c=5 null families are one for bridge 3 and two for bridge 15; their intersection is exactly J={(2,4),(5,6),(9,11),(10,13)} with ports S={3,8,12,14,15}. |
| Three-crossing realizability | On E=X_A union {z}, every D has some realizable R with connected D union R. There are three possible R. A singleton realizable set {R0} is impossible by choosing D=R0, whose two doubled edges have two components. Thus at least two R are realizable for each fixed A matching and bridge. |
| B spectra | The graph checker uses the same three original endpoint pairings R, transports them through C, and adds F_B. It rejects loops and all closed components, then traces every remaining path. Its graph has degree two at z and degree one at every other allowed B vertex. A successful trace yields exactly the balanced matching required for expansion. |
| Small-crossing closure | At c=1, the unique R is realizable; only 22 B matchings have no admissible bridge. At c=3, every nonexceptional B/bijection input has at least two admissible R on one bridge, intersecting the at-least-two realizable set. Exactly 10 B matchings, each for all six bijections, have no admissible R; these are exactly J union {e} for e in the ten two-subsets of S. |
| Residual domains | The input lists equal independently retraced exceptions, with no duplicate. For each B case the domain consists of every A port c-subset, every perfect matching on its complement, and every crossing permutation. No restriction on original long edges is introduced. |
| Expansion | The positive balanced cycle has fourteen B vertices and omits z,1. The path interiors consist of fifteen A vertices and z_B, pairwise disjoint and outside that B support. Expanding all compressed edges produces one simple 30-cycle. Suppressed original kz is restored. |
| Auxiliary-edge elimination | Every artificial D edge is deleted or replaced by the occupied bridge/crossing detour. Every compressed edge is expanded. Original F_A,F_B and crossing edges survive. All added uncompressed edges are cube edges. |

The c=3 pairing distinction is essential: Step 2 occupied blockers are
pairings on the two-vertex boundary X_B minus {z}; Step 3 instead counts
the three pairings R on the four original A endpoints X_A union {z}.
The verifier implements Step 3's latter semantics, including the possible
identification of the bridge endpoint and an occupied B port. It does not
count the smaller post-detour boundary as three possibilities. Both
arguments are valid and are not substituted for one another.

## Full finite verification and independence

I compiled `verify_t15_core8_residual.cpp` and `verify_t15_core8_B.cpp`
afresh with `g++ -O3 -std=c++17`, with assertions enabled. All generated
executables, exception lists and rerun outputs are isolated under
`core8_full_review_run/`. I reviewed both verifier implementations rather
than accepting their saved PASS fields.

| c | B cases | A partial matchings | Crossings per A/B input | Checked records |
|---:|---:|---:|---:|---:|
| 1 | 22 | 135135 | 1 | 2972970 |
| 3 | 10 | 270270 | 6 | 16216200 |
| 5 | 1 | 135135 | 120 | 16216200 |
| Total | | | | 35405370 |

All 1,982,700,720 certificate bytes were reread. Each record supplies its
own thirteen required edges and thirty cycle vertices. The checker verifies
the exact matching support, B-case identity, crossing count, cycle support,
vertex distinctness, all required edges, and shortness of every other edge.
Exact EOF excludes incomplete or trailing records. All three fresh reports
equal their saved verification reports.

Coverage is independent of the producer's recursive skip-or-pair traversal
and DFS/memo search. The verifier obtains an index directly from the
matching in each certificate. The c-subset rank is sum binomial(p_i,i+1)
on positions among thirteen allowed A vertices. These ranks exhaust
0 through binomial(13,c)-1, as separately exhaustively checked for all three
c. On a remaining set of 2k vertices, choosing the least vertex's partner
at index j partitions the matchings into 2k-1 disjoint blocks, each of size
(2k-3)!!. The recurrence j*(2k-3)!! plus the residual rank therefore proves
the matching rank bijective by induction, with empty rank zero and (-1)!!=1.
The crossing permutation uses ordinary factorial ranks, separately checked
on every permutation for c=1,3,5. B cases have distinct internal matchings;
their complementary port sets are consequently determined uniquely.
The mixed-radix formula combines precisely these four bijections.

The bitmap rejects any repeated input index, requires every bit filled,
and checks the exact expected record count. Consequently no producer
enumeration bug, reordering, duplicate cycle witness, or missing input can
be hidden by the positive count. The checker source belongs to the submitted
package; its independence is algorithmic from search and producer order,
and this fresh audit independently reviewed and reran that code. It is not
claimed to be a cross-family implementation.

Six deliberately damaged small files (empty, partial record, duplicate
record, invalid cycle vertex, required matching loop, and one valid record
without remaining coverage) were all rejected with nonzero exit status.
This also confirms the freshly compiled executable's assertions are active.

The B checker retraced all 135135 c=1 inputs and 1621620 c=3
B/bijection inputs. Full histograms equal both saved reports and producer
histograms; regenerated exception lists equal the residual B lists exactly.
The blocker checker was rerun from copied raw tables and copied explicit
blockers, reconstructing every inverse family and checking disconnectedness
of each explicit blocker against every negative output. All reports agree.
The fresh supplement independently validates geometry, exception relations,
rank components, hash bindings, and all cross-report equalities. All
manifest input hashes match the current files.

## Counterexample attempts and scope

Counterexample attempts targeted occupied c=1 loops, occupied c=3 repeated
labels, doubled boundary edges, c=13 empty internal matchings, a disconnected
compressed component, the single c=5 common null family, confusion between
the two c=3 pairing domains, and omission/duplication in certificate coverage.
The proof explicitly handles or excludes each possibility. No mathematical
counterexample or unclosed proof obligation was found. The only inequalities
used are finite counts and the elementary two-of-three intersection;
there are no limiting interchanges, probabilistic modes, or asymptotic
uniformity claims to audit. Artificial-edge versus original-edge roles stay
consistent throughout.

The optional parent recount was read-only: filtering the already audited
base rows using the current accepted extra-core set reproduces exactly
5927 remaining configurations, by target 1/7/31: 1495/2162/2270, including
50 without an a2b1 route. The existing residual binaries equal that row
filter byte-for-byte. If core8 is subsequently integrated, the same row
filter would leave 3101, by target 775/1136/1190. This report does not
perform integration or independently reprove the base geometry census.

This PASS accepts the complete core8 statement relative to its listed
imports, with same-family/provisional assurance. It establishes neither
the other T15 cores, full T15, the complete eight-hole layer, nor P6.
Machine-readable input hashes and rerun evidence are in
`T15_CORE8_FULL_REVIEW.json` and `core8_full_review_run/fresh_supplement.json`.

## Metadata correction after parent integration

The optional 5927-row parent recount above records the background snapshot
at the original review, dated 2026-11-01T10:59:37.859249+00:00. The precise
earlier sampling time was not separately logged. Its ledger, three current
residual binaries, and base geometry file are background context, not core8
theorem dependencies. Their original hashes and recount results are retained
under `context_snapshot_hashes` and `context_snapshot_metadata`. They have
been removed only from the theorem's `audited_input_hashes` namespace.
Later acceptance of core8 or other cores changes these parent state files
without affecting this core8 proof. All actual proof, certificate, import,
checker and verification-report hashes remain binding and were rechecked
after this classification correction. The PASS verdict and proof are
unchanged. This correction did not modify the parent ledger.
