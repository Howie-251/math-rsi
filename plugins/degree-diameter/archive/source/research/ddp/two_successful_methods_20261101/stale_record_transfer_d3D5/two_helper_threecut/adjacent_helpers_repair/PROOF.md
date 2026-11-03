# Adjacent-helper repair rule: complete fixed-scope NO

2026-11-01. `EXHAUSTIVE_FIXED_ADJACENT_REPAIR_RULE_NO72`. This is a change of generation rule based on the first experiment's actual failure, using the same inherited AFY70 source and the same cumulative20CPU budget. It is not a continuation of the old nonadjacent-helper enumeration.

## Changed mechanism

The first operation left28 configurations in which helper70 reached all old points, but helper71 was exactly6 away. The new operation puts an edge directly between the helpers. Their degree budget then permits only two old pins each. The two remaining freed old endpoints are repaired by one old-old edge, which may restore a cut but must not duplicate an edge still present after the cuts.

Delete3 vertex-disjoint old edges, choose any2 of their6 distinct endpoints for this repair, and split the other4 endpoints2+2 between helpers70/71. Each old endpoint loses and gains exactly one incident edge; each helper has two old neighbors and the other helper. Thus each configured graph is simple cubic with72 vertices and105−3+1+4+1=108 edges. No other change is permitted in the tested scope.

## Complete enumeration and actual tests

All166390 three-edge matchings of the literal105-edge source list are considered. Each has15 unordered endpoint-repair choices. The40320 choices that duplicate a retained old edge are rejected, leaving2455530 legal repair choices. Restoring any selected cut edge is allowed. For each legal repair, assign the least remaining endpoint to helper70 and choose its partner among the other3 endpoints. This lists all3 unordered2+2 partitions exactly once up to swapping helper labels. Total2455530×3=7366590 labeled operation configurations. Different choices may produce isomorphic or identical final graphs; the finite scope is nevertheless fully covered without an isomorphism assumption.

For each actual modified adjacency, use exact bitset radius5 from helper70, then helper71 if necessary. Since helpers are adjacent, their mutual distance is1. Only when both reach all70 old vertices do old-root radius5 checks begin, stopping at a first missing old target. All these paths may use either helper and the repaired edge; no old-only R4 NO filter is used.

| First failure | Configurations |
|---|---:|
| helper70 cannot reach some old vertex within5 | 7365708 |
| helper70 passes, but helper71 cannot reach some old vertex within5 | 714 |
| both helpers pass, but an old-old pair is farther than5 | 168 |
| diameter≤5 hit | 0 |

This changed rule really fixes the former helper-distance obstruction:168 configurations pass every pair involving a helper. They all still lose old-old distance coverage. The first exact witness is old pair(0,17), with cut edgeIDs[0,5,7], i.e. edges(0,1),(2,56),(3,4); repair(0,4); helper70 pins[1,3], helper71 pins[2,56], and helper edge70–71. In that actual final graph both helper roots cover all old points within5, yet17 is outside the radius5 ball of0. This is a specific old-route failure, not merely a total score.

No configuration reaches a complete all72-root acceptance batch, and none is claimed. Candidate-level old-old tests are entered168 times and each has an actual failing pair before full success. Source validity and source-only D5 BFS are inherited, not rerun; the first rule's source-R4 diagnostic is not recomputed.

## Receipt and stop boundary

One new compile1.323228CPU seconds and one complete numerical execution1.412590CPU seconds; measured new runner-plus-children2.775128. With prior measured1.863956, cumulative measured total4.639084/20CPU. Brief preceding preparation/final notes are not individually metered; the runner reserves one CPU second for them rather than assigning fabricated exact CPU values. Both original sessions are terminal and no processes remain.

Both tested operations now stop. No fourth cut, different source, larger repair class, seed or solver is started. This NO does not exclude general cubic72/D5 graphs, other70-point sources, nonmatching deletions, repair endpoints outside the six freed vertices, or more old-old edge reallocation. No new graph, parameter, Lean instance, field/rank/oldD6 check, install, hash, query or remote review is produced.

Evidence: PRED.md, BUDGET.json, gate.cpp, run_once.py, compile.log, gate.log, RESULT.json, TERMINAL.json; source and original result remain in the parent directory/previous source cache.

## One saved-pair route diagnostic

The original source5-route0–2–56–41–40–17 uses deleted edge(2,56). In the modified graph its replacement0–2–71–56–41–40–17 is a real6-route. Combined with the existing exact R5 failure, the saved old pair is therefore at distance6. Only these two paths were checked against the literal source/operation; no BFS or full rule was repeated. The diagnostic CPU is0.021609 seconds; whole-case measured cumulative CPU becomes4.660693/20.
