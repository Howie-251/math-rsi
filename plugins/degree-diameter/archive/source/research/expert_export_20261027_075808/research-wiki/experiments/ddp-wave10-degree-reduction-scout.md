---
type: experiment
node_id: exp:ddp-wave10-degree-reduction-scout
title: "170/253高次数源的spanning删边降度：全部边已被唯一三路强迫"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave10/degree_reduction_scout/REPORT.md; research/ddp/breadth_20261027_wave10/degree_reduction_scout/RESULT.json; research/ddp/breadth_20261027_wave10/degree_reduction_scout/source170_to_degree6.json; research/ddp/breadth_20261027_wave10/degree_reduction_scout/source170_to_degree6.forced_edges.json; research/ddp/breadth_20261027_wave10/degree_reduction_scout/source253_to_degree7.json; research/ddp/breadth_20261027_wave10/degree_reduction_scout/source253_to_degree7.forced_edges.json; research/ddp/breadth_20261027_wave10/degree_reduction_scout/screen.py"
added: 2026-10-27T07:58:08Z
tags: ["ddp", "method-ledger"]
---

# 170/253高次数源的spanning删边降度：全部边已被唯一三路强迫

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** necessary-capacity-screen

**目标与阶数：** 多目标：source170_to_degree6→[6, 3]／L=120；source253_to_degree7→[7, 3]／L=170（逐变体，不合成一个距离）

**距目标的证据：** no_new_graph_generated；170源全部595边与253源全部1012边均属于某条唯一距离3路径，若保持D3则每条都必须保留；根0等所有顶点的必保度分别7/8，超过目标6/7。两项均在必要条件处停止，未生成降度候选。

**其他指标（保持原计数类型）：**
```json
{
  "object_level": "theoretical_fixed_source_filter",
  "graph_generated": false,
  "source_count": 2,
  "CPU_seconds": 0.08116758700000001,
  "pruning_profiles": 0,
  "matching_searches": 0,
  "BFS_runs": 0
}
```



**从属变体：**
```json
[
  {
    "id": "source170_to_degree6",
    "target_Delta": 6,
    "target_D": 3,
    "savedL": 120,
    "n": {
      "actual": null,
      "hypothetical": 170
    },
    "actual_D": null,
    "actual_D_scope": "no_reduced_candidate;source_D3_only",
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "source_n": 170,
    "source_degree_histogram": {
      "7": 170
    },
    "source_known_D": 3,
    "order_margin": 50,
    "minimum_edges_that_must_be_deleted": 85,
    "unique3_unordered_pairs": 5130,
    "forced_edge_count": 595,
    "all_source_edges_forced": true,
    "forced_degree_histogram": {
      "7": 170
    },
    "status": "ALL_SPANNING_MAXDEGREE_SUBGRAPHS_BLOCKED",
    "scope": "All spanning subgraphs of this exact source graph, with arbitrary edge deletions; no added edges, vertex deletions, or rewiring.",
    "source": "research/ddp/breadth_20261027_wave7/signed_double340/source.edges",
    "source_validation_reused": "research/ddp/breadth_20261027_wave7/signed_double340/source_check.json",
    "graph_generated": false
  },
  {
    "id": "source253_to_degree7",
    "target_Delta": 7,
    "target_D": 3,
    "savedL": 170,
    "n": {
      "actual": null,
      "hypothetical": 253
    },
    "actual_D": null,
    "actual_D_scope": "no_reduced_candidate;source_D3_only",
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "source_n": 253,
    "source_degree_histogram": {
      "8": 253
    },
    "source_known_D": 3,
    "order_margin": 83,
    "minimum_edges_that_must_be_deleted": 127,
    "unique3_unordered_pairs": 9108,
    "forced_edge_count": 1012,
    "all_source_edges_forced": true,
    "forced_degree_histogram": {
      "8": 253
    },
    "status": "ALL_SPANNING_MAXDEGREE_SUBGRAPHS_BLOCKED",
    "scope": "All spanning subgraphs of this exact source graph, with arbitrary edge deletions; no added edges, vertex deletions, or rewiring.",
    "source": "context/DD_PORTFOLIO_START_20261026/baselines/d8_D3_known.edges",
    "source_validation_reused": "context/DD_PORTFOLIO_START_20261026/validation/d8_D3.json",
    "graph_generated": false
  }
]
```

**原始证据：** [research/ddp/breadth_20261027_wave10/degree_reduction_scout/REPORT.md](../../research/ddp/breadth_20261027_wave10/degree_reduction_scout/REPORT.md)；[research/ddp/breadth_20261027_wave10/degree_reduction_scout/RESULT.json](../../research/ddp/breadth_20261027_wave10/degree_reduction_scout/RESULT.json)；[research/ddp/breadth_20261027_wave10/degree_reduction_scout/source170_to_degree6.json](../../research/ddp/breadth_20261027_wave10/degree_reduction_scout/source170_to_degree6.json)；[research/ddp/breadth_20261027_wave10/degree_reduction_scout/source170_to_degree6.forced_edges.json](../../research/ddp/breadth_20261027_wave10/degree_reduction_scout/source170_to_degree6.forced_edges.json)；[research/ddp/breadth_20261027_wave10/degree_reduction_scout/source253_to_degree7.json](../../research/ddp/breadth_20261027_wave10/degree_reduction_scout/source253_to_degree7.json)；[research/ddp/breadth_20261027_wave10/degree_reduction_scout/source253_to_degree7.forced_edges.json](../../research/ddp/breadth_20261027_wave10/degree_reduction_scout/source253_to_degree7.forced_edges.json)；[research/ddp/breadth_20261027_wave10/degree_reduction_scout/screen.py](../../research/ddp/breadth_20261027_wave10/degree_reduction_scout/screen.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 只检查两个固定源的同顶点集任意spanning删边子图；170源降maxdegree6、253源降maxdegree7；不许新增边、删点或重连。

**正向保证：** 两源已知D3验证复用；本次不重复source BFS。；每条强迫边都有局部邻集唯一三路证书；证书所需路径的完整性以外不使用搜索结果。

**仍未完成：** 纯spanning删边无解；不排除允许加边、删点、重连或更换源的其他机制。

**启发与重启依据：** 降degree前先查唯一短路强迫边图的最大度；同源只删边不能靠matching优化修复，不能追加该删边profile。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

