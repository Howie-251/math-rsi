# Independent review of the Q6 root2 certificate

The reviewed CNF has 832 variables and 4422 clauses. An independent reconstruction of its clauses agrees exactly as a multiset with `star_q6_def0_root2_flushed.cnf`. This review did not rerun the large proof. The existing C# checker output reports all 291482 additions verified, including the empty clause.

## Exact mathematical statement

There is no C4-free subgraph of Q6 with a specified parity class P such that exactly one P vertex has degree 2, all other P vertices have degrees in {3,4,5}, and the total number of P-rooted full three-stars is 160. There is no restriction on the degrees of the opposite parity class in this CNF.

Here a full three-star with root v and direction triple T means that all three edges from v in T are present. There are 160 three-dimensional faces in Q6. In a C4-free graph, each such face contains at most one full star rooted in P: two distinct same-parity vertices of Q3 have distance two, and the two full stars would contain all four edges of the square on their two differing coordinates. Consequently total P-stars 160 is equivalent to exactly one such star per Q3.

The normalization is exhaustive. Translate the unique degree-2 root to 0; this sends its specified parity class to even parity, regardless of its original parity. Permute the six coordinates to send its two selected directions to 0 and 1. Cube automorphisms preserve degrees, C4-freeness, and full-star counts. Conversely an assignment to the normalized model describes precisely such a normalized graph.

## CNF equivalence

The 192 edge variables correspond bijectively to the edges of Q6. The other 640 variables are the 32 even roots times the 20 direction triples. Each star variable is equivalent to the conjunction of its three incident edge variables, using three forward binary clauses and one reverse clause. These contribute 2560 clauses.

There are 240 negative four-edge clauses, exactly one for each square. Every Q3 has one four-star positive clause and six pairwise negative clauses; these contribute 160 and 960 clauses. The six root units fix its degree-2 neighborhood to directions 0 and 1. For each of the other 31 even roots, all fifteen positive clauses on four of its six incident edges require at least three selected edges, while the single all-negative six-edge clause forbids degree six. These contribute 496 clauses. The degree clauses were independently checked on all 64 possible six-edge assignments.

Thus 2560 + 240 + 160 + 960 + 6 + 496 = 4422, with no further mathematical hypothesis encoded.

## Checker soundness review

Each RUP call starts with an empty assignment, then inserts the current unit clauses and the negations of the proposed clause. A directly conflicting insertion witnesses inconsistency. The two-watched-literal loop scans a clause precisely when a watched literal becomes false. It either finds another nonfalse literal to watch, or makes the remaining watched literal true, or detects conflict. Clause rearrangement only permutes literals. Resetting assignments between calls does not invalidate the watched-literal invariant. Deleted nonunit clauses become null and stale watch entries are discarded; multiplicities of unit clauses are retained separately.

Every accepted RUP addition is logically implied by the active database. The database initially consists of original CNF clauses. Keeping original clauses despite deletion requests is sound, since they are axioms throughout. By induction, all subsequently accepted additions are consequences of the original formula. Deleting a derived clause changes available unit propagation, but cannot invalidate this implication invariant.

For the final empty clause only, the checker may reconstruct the database from the original CNF and every previously validated addition, ignoring their deletions. It reads only proof lines strictly preceding the current empty clause. All of these additions already satisfy the induction invariant. A unit-propagation conflict in their union therefore proves the original CNF unsatisfiable. This fallback is sound; it is not circular and does not assume the current empty clause. It broadens the accepted deletion convention rather than accepting an unvalidated lemma.

The parser checks a final zero, rejects embedded zeros, removes duplicate literals, checks literal ranges for inputs/additions, and counts input clauses. An accepted tautological clause is harmless. Proof deletions lacking a matching active clause are ignored, which also cannot invent a logical consequence. No soundness defect was identified in the reviewed code. The small tests are supporting checks, not a formal verification of the C# implementation.

## Independent checks and scope

`root2_certificate_independent_audit.py` reconstructed the CNF, checked its exact clause multiset, verified the local degree truth table, checked that the proof ends with an empty clause, and matched both SHA256 hashes against the solver and checker metadata.

`rup_small_tests.ps1` ran ten synthetic cases. The checker accepted a direct contradiction, a proof whose final step needs restoration of a deleted previously validated clause, and retention of deleted original axioms. It rejected a false empty clause in a satisfiable formula, a non-RUP unit clause, a missing terminator, an embedded zero, an out-of-range addition, a proof lacking an empty clause, and an attempted contradiction made using a tautology. All outcomes matched expectations.

CNF SHA256: `8f90783e2358a9b13da75de7bd551fb7da8768827c6318864072674687efc801`.

Proof SHA256: `68442c125083a2e27487e9d8808846ccf0fce58422540c33af7b9000dccc58bb`.

The Windows native stream flushing and byte writes do not alter the mathematical encoding. The reviewed proof hash agrees across the files and metadata, and the parser rejects truncated clauses. The existing checker result for the full artifact reports 291482 accepted additions and 257226 deletions in 94.264 seconds. This review establishes the encoding and checks the certificate-verifier reasoning independently. It is not a report that the project's full-proof verification service approved ex(Q7,C4) <= 304.
