# Source650 critical-middle necessary gate

The complete necessary-condition calculation does **not** exclude the fixed one-hub family. Of 2,080 FF edges, 1,952 have a critical matching of size 9, 126 have size 8, and 2 have size 7. Every FP edge (1,040) and PP edge (130) has critical matching size 0. The prediction that all FF edges are forbidden is therefore refuted; 128 FF edges remain unexcluded by this gate. No new graph, source distance BFS, modified-graph BFS, or solver was run.

The fixed proposed rule deletes 1–5 old edges from the actual degree10/D3 graph on 650 vertices, then adds one hub adjacent to every distinct endpoint S of the deleted edges, with |S|≤10. All other old edges remain; no other new edges are allowed. Its target is n651/max10/D3, beyond saved lower bound 650. The source is the cached Delorme graph with Pelekhaty adjacency, maintained at https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD3/n650d10k3.txt . Its published D3 is inherited, not rechecked.

## Exact calculation and meaning

STRUCTURE_ROOT.json supplies the already verified P130/F520 partition and the 65 pairs sharing their eight F-neighbors. These are F-neighborhood twin pairs, not an unproved claim of identical complete neighborhoods. Root also supplied the endpoint closed-R2 port-union upper bounds FF40/FP24/PP8. Those structure and R2 computations were reused without repetition.

The producer computed exact ordinary walk matrices A² and A³, with row sums 100 and 1000. For a central old edge u–v, it builds the bipartite graph on L=N(u)\{v} and R=N(v)\{u}. A pair p,q is critical exactly when p≠q, p and q are nonadjacent, A²[p,q]=0 and A³[p,q]=1. Thus its unique length≤3 old route is p–u–v–q.

After deleting u–v, that pair must meet S: if neither endpoint meets S, every route through the sole new hub has length at least four, and no surviving old route of length≤3 exists. A size9 critical matching uses 18 distinct physical old vertices outside u,v, requiring at least nine additional S vertices beyond u,v. This contradicts |S|≤10, so each of the 1,952 size9 edges is rigorously forbidden. The producer explicitly checked physical distinctness for every size9 matching; it does not confuse duplicate left/right labels with independent vertices.

The first remaining FF edge is (1,9), with maximum matching 8 and 53 critical pairs. A size7 example is (16,132), with 38 critical pairs. Their complete neighbor lists, critical masks and maximum matchings are in EDGE_CRITICAL_MATCHINGS.jsonl. All 3,250 old edges were processed, with no untested or unknown edges.

Had all FF cuts been forbidden, the inherited FP/PP bound would imply that five cuts expose at most 5×24=120 of the 130 P vertices within two old steps of S, making hub D3 impossible. Because 128 FF edges survive, that conditional argument cannot close the actual family. A matching smaller than nine is only failure of this rejection criterion, not a feasible insertion.

## Cost, scope and stop

Native calculation: 0.028830 CPU seconds; native process: 0.030475; compile: 0.784837; Python driver: 0.001418. Root's separate reused structure/R2 calculation was 0.026185 CPU seconds. The native hard limit was 10 CPU seconds and the finite analysis completed normally.

Actual new order, diameter and ordinary unordered bad-pair count are null: no modified graph was produced. This batch closes its necessary-data task, not the whole proposed insertion family. The remaining question is whether a choice of at most five cuts using the 128 unexcluded FF edges can meet the joint critical-pair and hub-coverage constraints; no such search is authorized or run here. Arbitrary 651-vertex graphs, additional helper vertices, omitted endpoint spokes, and other rewiring rules are not excluded.

Reproduce this calculation with `python research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/run.py` from the project root. The source is read once. The binary walk-count schema is in WALK_COUNT_SCHEMA.json; RESULT.json and terminal.json record the completed finite scope.
