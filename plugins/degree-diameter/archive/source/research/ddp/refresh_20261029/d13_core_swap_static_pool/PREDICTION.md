# Frozen three-candidate static construction test

2026-10-29, before new radius computations.

Take precisely indices0,8,17 from `../d13_core_swap_extension_signature/CORE_SWAP_FIXED_PERIPHERAL_CANDIDATES.json`: swap the saved core split labels in the original S_i and leave peripheral guard IDs fixed. Prediction: these three new, individually capacity-legal and nontrivially distinct sets may preserve original B0 core R4 coverage; any failure must separately report core and peripheral omissions. This is a testable conjecture, not a consequence of a full-source automorphism. Index37 is a superset of original S_0 and is excluded as dominated without a ball computation.

Read original `d13_D5_h9_transfer/source51417.edges` once, retaining its324451 old edges. Run exactly one multi-source BFS through distance4 for each of the three sets. Save R3/R4 and core/peripheral omissions; the same distances provide set-distance compatibility with all40 cached original S_i and between the three new sets. Inherit original40 independent B0 R4 and old-old compatibility without recomputing them.

Only fully covering new sets enter the static pool, each allowed once. Original40 sets are also allowed once. Enumerate every potentially improving choice: nonempty new subset A and old drop set D with |D|≤|A|−1. Check all old-port loads against13−degree_B0, all selected old/new set-distance bounds≤3, and each new vertex degree≤13. Examine total cardinality in descending order43,42,41, so the first accepted family is a proven maximum over this exact0/1 pool. If no improving family exists, the inherited40 remains optimal for this pool.

On a hit, save literal neighborhood family, new subset and dropped old indices, expected n/m, and the complete graph rebuilt as B0 edges plus each selected neighborhood. Do not describe removal of old final helpers as retention of all edges of current51457. Parent performs independent acceptance. No solver, new guard, other candidate, old S_i BFS, source-D5 all-root BFS, or enlarged search. One worker,≤5CPU, one original-source read and at most3 R4 computations.
