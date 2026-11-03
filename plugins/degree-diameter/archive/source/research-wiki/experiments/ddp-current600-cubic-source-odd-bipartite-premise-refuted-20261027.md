---
type: experiment
node_id: exp:ddp-current600-cubic-source-odd-bipartite-premise-refuted-20261027
title: "(3,9) Exoo600 actualsource is non-bipartite: proposed subdivision premise not met"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d3_D9_current600_source/SOURCE_REPORT.md; research/ddp/more_graphs_20261027/d3_D9_current600_source/SOURCE_PROFILE.json; research/ddp/more_graphs_20261027/d3_D9_current600_source/source600.author.adj; research/ddp/more_graphs_20261027/d3_D9_current600_source/source600.edges; research/ddp/more_graphs_20261027/d3_D9_current600_source/CONDITIONAL_SUBDIVISION_LEMMA.md"
added: 2026-10-27T23:28:32Z
tags: ["ddp", "method-ledger"]
---

# (3,9) Exoo600 actualsource is non-bipartite: proposed subdivision premise not met

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (3,9)；L=600；条件性n=601（未据此计纪录）

**距目标的证据：** Actualsource600/900 full3regular is non-bipartite by exact parity union-find; first conflict edge215-465. No graft tested. The false premise does not imply all grafts fail.

**其他指标（保持原计数类型）：**
```json
{
  "status": "PRIMARY_LITERAL_BOUND_NO_DISTANCE_BFS",
  "n": 600,
  "m": 900,
  "simple": true,
  "undirected": true,
  "degree_histogram": {
    "3": 600
  },
  "connected_by_union_find": true,
  "bipartite": false,
  "bipartite_check": "exact parity union-find over all900edges; no graph-distance traversal",
  "first_parity_conflict_edge": [
    215,
    465
  ],
  "source_labels": "implicit rows0..599, neighbours already0-based",
  "first_row": [
    345,
    539,
    441
  ],
  "normalized_edge_schema": "header600 900; then900 sorted0-based edges",
  "reported_source_D": 9,
  "reported_source_kind": "Exoo voltage graph; actual voltage recipe not supplied by current description",
  "source_D_scope": "inherited from current primary description",
  "edge_transitivity": null,
  "vertex_transitivity": null,
  "source_BFS": 0,
  "candidate_graphs": 0,
  "candidate_search": 0,
  "profile_CPU_seconds": 0.002494766999999995,
  "primary_description": "https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g9.html",
  "primary_literal": "https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD9/Exoo_600.txt",
  "official_sage_link_status": "page links adjD7/600_exoo_SageMath.txt, which returns404; no substitute script assumed",
  "new_lower_bounds": 0,
  "new_graphs": 0,
  "ordinary_bad_pairs_measured": false,
  "predicate_prediction": "BIPARTITE_SOURCE_PRECONDITION_REFUTED",
  "new_all_source_BFS_calls": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d3_D9_current600_source/SOURCE_REPORT.md](../../research/ddp/more_graphs_20261027/d3_D9_current600_source/SOURCE_REPORT.md)；[research/ddp/more_graphs_20261027/d3_D9_current600_source/SOURCE_PROFILE.json](../../research/ddp/more_graphs_20261027/d3_D9_current600_source/SOURCE_PROFILE.json)；[research/ddp/more_graphs_20261027/d3_D9_current600_source/source600.author.adj](../../research/ddp/more_graphs_20261027/d3_D9_current600_source/source600.author.adj)；[research/ddp/more_graphs_20261027/d3_D9_current600_source/source600.edges](../../research/ddp/more_graphs_20261027/d3_D9_current600_source/source600.edges)；[research/ddp/more_graphs_20261027/d3_D9_current600_source/CONDITIONAL_SUBDIVISION_LEMMA.md](../../research/ddp/more_graphs_20261027/d3_D9_current600_source/CONDITIONAL_SUBDIVISION_LEMMA.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Exact current primary Exoo600 literal only. Degree/connectivity/parity checks, no distance BFS or modified graph. Bipartite-odd-diameter premise false; symmetry not bound.

**仍未完成：** Actual600 voltage/symmetry recipe and any non-bipartite graft remain untested. This is not a family nonexistence result.

**启发与重启依据：** Do not transplant the bipartite oddD automatic newroot argument to this source or substitute distinct Conder600 census graphs. A non-bipartite coverage mechanism or recovered actual voltage/symmetry structure would be a substantive new entry; no automatic edge/helper ladder.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

