# Source650: complete forced-pin search for the five-cut hub family

The fixed source650 family is excluded. The finite search completed all 128 possible FF anchors and their 512 left-subset choices: 4 size7 base covers and 274 size8 base covers yielded 2,820 physical endpoint sets after per-anchor deduplication. Of these, 260 covered all 650 old vertices within old distance two. **None admitted a five-edge realization containing its anchor and meeting every deleted edge's critical-pair constraints.** No modified graph or distance BFS was needed or run. The prediction of at least one endpoint set passing both gates is refuted.

The precise family deletes at most five edges from the actual fixed degree10/D3 source on 650 vertices, adds one new hub joined to **all** distinct deleted-edge endpoints S, and retains every other old edge. It allows no other new edges and requires |S|≤10. The target is n651/max10/D3, beyond saved lower bound 650. This is a finite exclusion of that insertion rule, not an upper bound on N(10,3).

## Why the enumeration is complete

The earlier stage found 1,952 FF edges with a size9 critical matching, so none can be cut. The remaining FF edges consist of 126 with matching8 and two with matching7. If no FF edge is deleted, the inherited FP/PP endpoint-R2 port bound gives at most 5×24=120 reachable P vertices, short of P130. Therefore every legal insertion must cut one of these 128 remaining anchors.

Fix such an anchor u–v and let C=S\{u,v}. Every critical pair for that edge must meet C. Its matching lower bound is seven or eight, while |C|≤8. The search enumerates all 512 subsets Lselected of its nine left vertices and forces Rforced to contain every right neighbor of an unselected left vertex. For any valid C, choosing Lselected=C∩L gives C0=Lselected∪Rforced⊆C. Physical IDs, rather than left/right multiplicity, define this union. All 128 actual anchors have disjoint L/R label sets.

If |C0|=8, it is the full C and gives S10. If |C0|=7, it gives S9, and every possible one-vertex enlargement anywhere in the old graph gives all remaining S10 cases. No cover smaller than seven can occur. The enumeration includes the matching7 anchors, isolated-neighbor choices, and extra pins outside L∪R.

Having an FF anchor forces |S|≥9. At most four cut edges have at most eight endpoints, so the cut set must have exactly five edges. On ten endpoints these edges form a perfect matching. On nine endpoints they have degree sequence 2,1,…,1, hence form P3 plus three P2. The code enumerates both shapes, including anchors either inside the P3 or in one of its independent P2 edges. Every proposed cut edge must have all its own critical pairs hit by S. All realizations containing an anchor are enumerated; global deduplication uses sorted five-edge ID tuples only after a complete realization exists.

The old closed-R2 gate uses cached A² and the old adjacency, without recomputing walks or doing BFS. Because every deleted edge lies wholly inside S, a shortest path into S never uses a deleted edge; thus old R2(S) equals R2 in the cut graph. Passing that gate is exactly the hub-to-old distance≤3 condition. Nevertheless, the code retains an actual modified hub check and all 650 old-root checks after a realizable cut set; no set reached that stage.

The complementary paper review by expert_brief_evidence independently confirmed this enumeration and scope before execution. Its ANALYSIS_PROOF files are supplementary references when present; the producer's counts are in RESULT.json.

## Execution and evidence

Native CPU: 0.035215 seconds; native process: 0.036837; compile: 1.214182; driver: 0.035776. The 10-CPU-second native hard limit was not approached. The complete finite result has no unknown or untested anchors, endpoint sets, or graph realizations. ACTUAL_CASES.jsonl is empty because there were no realizable five-cut sets.

Source D3 is inherited; source distance BFS, A²/A³ recomputation, modified-graph BFS, solver calls and generated graphs are all zero. Actual new order, new diameter, and ordinary unordered bad-pair count remain null. No lower bound was improved. The earlier prediction that all FF edges were forbidden remains recorded as refuted; its 128 surviving edges were the input to this complete next stage rather than silently discarded.

Run `python research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/run.py` from the project root to reproduce the fixed finite computation. It reuses the parent directory's EDGE_CRITICAL_MATCHINGS.jsonl and A2.u16le.bin, and the original cached source adjacency. This family is closed: no additional cut, helper, arbitrary omitted-endpoint spokes, or other rewiring rule was tested or excluded.
