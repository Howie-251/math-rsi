# Complete fixed-rule obstruction: AFY70 → cubic72

2026-11-01. `EXHAUSTIVE_FIXED_RULE_NO72`. This is a finite exclusion for one fixed source and one explicitly specified operation, not an exclusion of cubic72/D5 graphs.

The inherited source is `research/ddp/more_graphs_20261027/cubic_D6_twofold70/source70.edges`, n70/m105/cubic/D5, credited by its existing SOURCE.json to I. Alegre, M. A. Fiol and J. L. A. Yebra and the official D5 adjacency. No source-validity or diameter5 BFS was repeated. The old ordinary two-cover (D6) and three-cover (D7) exclusions concern different graph operations. A limited report/Wiki check located no prior completed identical three-cut rule.

## Exact rule and complete enumeration

Choose three distinct old edges having six distinct endpoints. Delete them. Split their endpoints into two triples A and B, add vertices70 and71, join70 to A and71 to B, and add no70–71 edge or any other edge. Each of the six old endpoints loses one edge and gains one; all other old degrees remain3; each new degree is3. Thus every tested configuration has72 vertices and105−3+6=108 edges and is simple cubic by construction.

`gate.cpp` enumerates edge indices i<j<k from the complete105-edge literal list and rejects exactly the endpoint intersections. There are166390 matching triples. Sort each six-endpoint set, require its smallest endpoint to belong to A, and enumerate all size3 subsets A satisfying that requirement. This gives C(5,2)=10 representatives, exactly once each up to swapping the two new vertices. No source automorphism or heuristic pruning discards configurations. Therefore166390×10=1663900 configurations cover the whole stated operation.

For each actual modified72-vertex adjacency, compute the closed radius5 set from helper70 using successive bitset frontiers. If any OLD vertex is missing, diameter≤5 is impossible. If all70 old vertices are reached, also require vertex71 to be reached. Only a configuration passing these tests would be checked from helper71 and then from every old root. These tests operate on the actual final adjacency, including paths through either helper.

## Actual exhaustive result

| First failing condition | Configurations |
|---|---:|
| helper70 fails to reach some old vertex within5 | 1663872 |
| helper70 reaches all old vertices, but helper71 is not within5 | 28 |
| helper71-to-old test entered | 0 |
| old-old test entered | 0 |
| complete diameter≤5 hit | 0 |

The28 remaining configurations have helper distance exactly6: all three B pins are old vertices and hence each is within5 of helper70; if any were within4 then71 would be within5. Thus all three are at distance5 and appending their edge to71 gives distance6. This explanation does not require an additional BFS beyond the recorded radius5 data.

Every configuration has a witnessed type of pair outside radius5 before an old-old check is needed. Therefore no actual complete72-root batch was run, and none is claimed. The all-pair test is present in the code for a genuine surviving candidate, but no candidate reaches it.

## Corrected route prediction

The original proposed old-host R4 cover criterion is too strong to use without qualification. A route can be

`helper70 — a — b — helper71 — c — target`,

where a∈A, b,c∈B and a–b,c–target are retained old edges. It has length5 even if the old-only route from A to target exceeds4. The experiment therefore allows this collaboration and never uses source-only R4 failure to discard a configuration.

As a diagnostic only, the inherited source has closed R4 ball size46 at each of its70 vertices. In23072 configurations both original-source triple unions cover70 old vertices;120232 have exactly one such cover and1520596 have neither. Even the original-source covers are optimistic: deleting the chosen edges can break routes. These counts are neither a source-D5 revalidation nor the exclusion proof; the actual modified graph radius5 tests provide the obstruction.

## Cost and boundary

One compile and one complete execution: compile1.380910CPU seconds, numerical gate0.442339, measured runner-plus-children total1.863956, inside the20CPU budget. Brief preceding file preparation/report reads were not individually metered; the runner reserved one CPU second for them and final receipts. No timeout or sampling was needed. Process/session is terminal, no seeds or continuation planned.

No graph hit, new parameter, Lean instance, graph download, field/rank check, solver, remote review, install or hash was produced. The stopped scope does not cover a different70-point source, adjacent helpers, nonmatching cuts, additional old-old edge repairs, or general cubic72/D5 existence. Do not extend this finite NO to any of those rules.

Evidence: PRED.md, BUDGET.json, gate.cpp, run_once.py, compile.log, gate.log, RESULT.json, TERMINAL.json. The executable is only a local reproducible build product.
