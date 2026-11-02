# Actual1141: every balanced vertex split fails the far-first-support condition

All 1,141 source vertices have at least one distance3 target whose geodesics use a single first neighbor. There are 357,347 such ordered source/target pairs among 1,087,886 distance3 ordered pairs. Therefore **no balanced7/7 adjacent-child split of any vertex of this fixed source can produce a D3 graph on 1,142 vertices**. The prediction that at least one vertex would survive the singleton gate is refuted. No split graph, coloring solver or distance BFS was run.

For example, vertex0 has sorted neighbors1..14. Target23 is at old distance3, and all its length3 routes from0 begin with neighbor6 (support mask32). The child not assigned neighbor6 cannot reach23 within three steps. Vertex0 has313 singleton targets in total. VERTEX_FIRST_SUPPORTS.jsonl records a witness and all singleton targets separately for every old vertex.

## Binding and exact necessary calculation

The cached source source1141.header.edges is the previously profiled actual1,141-vertex,7,987-edge,full14regular graph. Its published D3 is inherited from the primary Comellas entry. A fresh read of the main table still gives (14,3)=1,141; CURRENT_MAIN_RECEIPT.json records the primary URL. The exact existing ledger node is ddp-current-d14d3-1141-source-profile-20261027, whose earlier scope was source recovery and the absence of spare degree. It did not cover this split model.

The producer read the source once and computed exact ordinary A²/A³ walk counts, with row sums196/2744. A pair v,t has distance3 precisely when t≠v, A[v,t]=A²[v,t]=0 and A³[v,t]>0. For such a pair, the support H_v(t) consists of those sorted source neighbors u of v with A²[u,t]>0. FIRST_SUPPORTS.u16le.bin stores this14-bit support for every distance3 pair and zero otherwise. Every per-vertex minimum is one, so ELIGIBLE_SPLIT_HYPEREDGES.jsonl is correctly empty.

In the proposed split, two adjacent children partition the14 old neighbors into7+7, giving both children degree8. A distance3 old target can be within three steps of a child only through a neighbor assigned to that child: crossing to its sibling consumes an extra step and would require an old distance≤2 route, contradicting the target's old distance3. Consequently H_v(t) must meet both assigned sets. A singleton can never do so. This closes only this exact fixed-source split family, not arbitrary1,142-vertex (14,3) graphs or other rewiring rules.

## Separate critical-middle model

The same cached matrices were used to analyze all7,987 old edges. For u–v, the13×13 critical graph joins p∈N(u)\{v} and q∈N(v)\{u} exactly when p,q have old distance3 and A³[p,q]=1. In a different proposed rule deleting at most seven edges and adding one hub at every cut endpoint, a matching13 would require13 extra pins beyond u,v, exceeding the hub's14-pin budget. Physical left/right labels would need to be distinct; the code checks that condition whenever matching13 occurs.

Here the maximum matching is only11, attained by the single edge(377,421), whose critical graph has40 pairs. The full matching histogram for sizes0..13 is:

`[458,647,374,128,44,97,690,1880,2053,1307,308,1,0,0]`.

Thus this matching13 necessary test forbids **zero** edges of the second model. No hub graph, endpoint-cover search or solver was run, and no exclusion of that model follows. EDGE_CRITICAL_MATCHINGS.jsonl supplies all physical labels, row masks and maximum matchings for a separately authorized next stage.

## Cost and scope

Native CPU0.176828 seconds; native process0.179011; compile0.921411; driver0.001433; aggregate1.101855. The hard native limit was10 CPU seconds. All vertices and edges were processed, with no unknown or untested entries. Source distance BFS, modified graphs, modified BFS and solver calls are zero. Actual modified order/diameter and ordinary unordered bad-pair count are null; no new lower bound was obtained.

Reproduce with `python research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/run.py` from the project root. CACHE_SCHEMA.json describes the three little-endian uint16 matrices and the JSONL interfaces. This batch stops after the necessary cache; no additional source, helper, split coloring, cut-set search or graph experiment is included.
