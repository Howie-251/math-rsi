# Eight mixed positives, at most two triples

Status: complete local repair proof, subject to the stated imported five-label lemmas and ordinary deterministic-program trust. This is not a new global Property B conclusion or an external review acceptance.

Canonical theorem: [EIGHT_MIXED_TWO_SMALL_EIGHTEEN_REPAIR.md](../../../../../../proofs/propertyb35/EIGHT_MIXED_TWO_SMALL_EIGHTEEN_REPAIR.md).

The exact statement is eight indexed positive sets of sizes three/four, at most two positive triples, at most20 indexed negative quadruples, no other negative sizes, ground at most18, total signed occurrence at most7. No padding is used.

Low positive occurrence is covered by the canonical occurrence-charge bound 129964805/143327232. Occurrence at least4 is analytical. After fixing a three-occurrence point, the old all-four and one-triple five-label domains are reused unchanged. The only new domain has capacities(3,3,4,4,4), edge count2..7 and matching count1/2. Matching count at least3 is solved by C3>=5; matching count0 is solved analytically by36 candidates versus at most32 blocked.

Two generators, one assigning edges and one assigning forward vertex stars, produce exactly the same837 labelled multigraphs. Quotient only by S2 x S3 preserving triple/four label classes gives94 orbits. Direct C4 enumeration and32-term inclusion-exclusion agree on every representative. Minimum C4 is81; the universal negative blocker bound is68. Actual triple extension maxima were additionally checked by an independent missed-label intersection computation; the minimum actual margin is13. All vectors, sizes, sets, orbit sizes, counts and margins are in CHECK.json. CPU about0.07seconds locally.

The bounded computation reconstructs five intersecting sets, not complete hypergraphs. The canonical proof supplies the full graph-domain coverage, orbit transport and original signed repair interface. It does not assume a particular P-side inventory or automatically assert that any remaining original branch has these signed parameters. No P6 selector rerun was performed in this task.
