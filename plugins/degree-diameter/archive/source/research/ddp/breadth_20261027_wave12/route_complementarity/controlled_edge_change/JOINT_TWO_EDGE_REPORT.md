# P4 joint two-edge diagnostic: simultaneous direction choice still cannot preserve all tight routes

Status: complete exact225-assignment route-linear diagnostic, with no feasible assignment. No two-edge graph was generated, no full-graph score or BFS was computed, and no new seed or third edge was considered. The earlier GQ branch remains paused.

## Falsifiable question and fixed scope

The preceding sequential test first fixed edge0->18 at b3 and then changed edge36->0 to repair37<->63; this moved rank loss to other tight routes. The current question was whether simultaneous choice of both branch vectors could avoid that propagation. Both vectors now range independently over all15 nonzero F2^4 codes. Every matrix, every zero offset, and all other142 edge branch vectors remain fixed at cachedbest68. Reverse relations always use their actual inverse matrix times the forward branch vector.

The exact acceptance condition is AACA rank4 for target0->10, together with rank4 on all468 cached unique4 ordered controller slots. AACA uses the first changed edge but not the second. If any assignment passed, the fixed rule would choose the lexicographically first pair and root would generate exactly that graph. None passed, so no graph parameters were selected or exported.

## Exact finite result

- All225 assignments completed.
- Exactly28 of the468 tight paths traverse at least one of the two prescribed undirected edges. The other440 have unchanged columns and retain baseline rank4 for every assignment.
- Eight first-edge vectors give AACA rank4; with15 second-edge vectors each, this is120 target-repairing assignments.
- None of those120 preserves all468 tight ranks.
- The smallest damage count subject to target rank4 is2 directed slots. The lexicographic diagnostic minimizer is(bfirst,bsecond)=(3,3), with reverse codes(9,11). Its second vector equals the original B vector, so this is the already measured first-edge-only modification; it is not a new candidate. Its two deficient slots are37->63 and63->37, both rank3.

The complete joint minimum by first-edge vector is:

| first b | smallest damaged directed tight slots over all15 second b | second b attaining that minimum |
|---:|---:|---|
| 2 | 12 | 3 |
| 3 | 2 | 3 |
| 6 | 10 | 3, 8 |
| 7 | 4 | 3 |
| 10 | 6 | 3 |
| 11 | 8 | 3 |
| 14 | 12 | 3, 8 |
| 15 | 2 | 3 |

For each of the eight first vectors that repairs AACA, the original second vector b3 is already a damage minimizer. The second edge therefore cannot improve this tight-rank damage count anywhere in this complete prescribed joint slice. This statement is a reduction of the saved225 diagnostics, not a new search or a claim about arbitrary paired edges.

## Meaning for the prediction and next rule

The hypothesis that joint choice on these same two edges can repair the target while retaining every original unique4 fiber route is false within this fixed225-assignment slice. Each accepted target-repairing assignment has a rank-deficient unique route, hence misses exactly16-2^rank targets per fiber input for that slot. An assignment whose AACA stays rank3 also cannot give whole-graph D4: the unchanged DCC route has rank3, and at source coordinate0 with all offsets0 their linear images both contain0 and cannot cover all16 targets.

Thus this full prescribed slice cannot achieve D4. The conclusion is limited to these two edges, fixed matrices and other branch vectors, and zero offsets. It does not exclude the general edge-local family, other selected edges, matrix changes, nonzero offsets, or coordinated changes on a larger dependency set. No such extension is launched.

The test changes the next decision: changing the order from greedy to joint on this edge pair does not resolve its direction conflict, so continuing along the same local propagation chain has no support from these data. Any separately authorized follow-up would need a new concrete mechanism for preserving the tight-route directions rather than merely revisiting their decision order. At the current stop, no third edge or new graph is requested.

## Artifacts and cost

joint_two_edge_analysis.json saves all225 vector pairs, target columns/rank, complete damage records with paths and columns, affected-slot indices, the exact selection rule, and the no-feasible terminal result. analyze_joint.py reproduces only this diagnostic. It traverses the28 affected cached routes per assignment; the untouched440 slots are covered by the explicit path-independence argument. CPU time was 0.035967 seconds under a hard1-CPU-second process limit. Graphs0, whole-graph scores0, BFS0, solvers0, new lower bounds0. No original or controlled graph BFS was repeated.
