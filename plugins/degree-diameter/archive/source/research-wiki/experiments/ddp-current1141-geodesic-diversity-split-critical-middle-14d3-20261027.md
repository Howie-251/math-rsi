---
type: experiment
node_id: exp:ddp-current1141-geodesic-diversity-split-critical-middle-14d3-20261027
title: "Actual1141: all1141 balanced7/7 vertex splits excluded by singleton far-first support"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/REPORT.md; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/PREDICTION.json; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/RESULT.json; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/CURRENT_MAIN_RECEIPT.json; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/CACHE_SCHEMA.json; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/VERTEX_FIRST_SUPPORTS.jsonl; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/ELIGIBLE_SPLIT_HYPEREDGES.jsonl; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/EDGE_CRITICAL_MATCHINGS.jsonl; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/A2.u16le.bin; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/A3.u16le.bin; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/FIRST_SUPPORTS.u16le.bin; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/analyze.cpp; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/run.py; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/RUN_HANDLE.json; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/terminal.json; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/ANALYSIS_PROOF.md; research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/ANALYSIS_RESULT.json"
added: 2026-10-28T00:01:06Z
tags: ["ddp", "method-ledger"]
---

# Actual1141: all1141 balanced7/7 vertex splits excluded by singleton far-first support

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** necessary-condition-analysis

**目标与阶数：** (14,3)；L=1141；条件性n=1142（未据此计纪录）

**距目标的证据：** Complete ordinary A2/A3 cache:1087886 distance3 ordered pairs,357347 singleton first-support pairs; every1141 vertex has minimum support1. This strictly excludes every balanced7/7 split of the source. In the separate edge-freeing model, critical matching maximum11 means matching13 forbids zero old edges; that family is not excluded.

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 1141,
  "source_m": 7987,
  "source_degree": 14,
  "source_D_inherited": 3,
  "source_profile_node": "ddp-current-d14d3-1141-source-profile-20261027",
  "distance3_ordered_pairs": 1087886,
  "singleton_far_first_support_ordered_pairs": 357347,
  "per_vertex_min_support_histogram": [
    0,
    1141,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
  ],
  "first_support_size_histogram": [
    0,
    357347,
    472791,
    202790,
    46216,
    6607,
    868,
    104,
    164,
    283,
    126,
    306,
    225,
    57,
    2
  ],
  "eligible_split_vertices": 0,
  "first_singleton_witness": {
    "v": 0,
    "target": 23,
    "unique_first_neighbor": 6,
    "mask": 32
  },
  "critical_middle_maxmatching_histogram": [
    458,
    647,
    374,
    128,
    44,
    97,
    690,
    1880,
    2053,
    1307,
    308,
    1,
    0,
    0
  ],
  "matching13_forbidden_cut_edges": 0,
  "maximum_critical_matching": 11,
  "unique_maximum_matching_edge": [
    377,
    421
  ],
  "source_distance_BFS_count": 0,
  "modified_graphs": 0,
  "modified_BFS_count": 0,
  "solver_calls": 0,
  "native_CPU_seconds": 0.176828,
  "total_parent_children_CPU_seconds": 1.10185507,
  "prediction": "REFUTED",
  "new_lower_bounds": 0,
  "untested_vertices": 0,
  "untested_edges": 0,
  "ordinary_bad_count_units": "null; ordered geodesic-support counts are not unordered bad pairs"
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/REPORT.md](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/REPORT.md)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/PREDICTION.json](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/PREDICTION.json)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/RESULT.json](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/RESULT.json)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/CURRENT_MAIN_RECEIPT.json](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/CURRENT_MAIN_RECEIPT.json)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/CACHE_SCHEMA.json](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/CACHE_SCHEMA.json)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/VERTEX_FIRST_SUPPORTS.jsonl](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/VERTEX_FIRST_SUPPORTS.jsonl)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/ELIGIBLE_SPLIT_HYPEREDGES.jsonl](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/ELIGIBLE_SPLIT_HYPEREDGES.jsonl)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/EDGE_CRITICAL_MATCHINGS.jsonl](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/EDGE_CRITICAL_MATCHINGS.jsonl)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/A2.u16le.bin](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/A2.u16le.bin)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/A3.u16le.bin](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/A3.u16le.bin)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/FIRST_SUPPORTS.u16le.bin](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/FIRST_SUPPORTS.u16le.bin)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/analyze.cpp](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/analyze.cpp)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/run.py](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/run.py)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/RUN_HANDLE.json](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/RUN_HANDLE.json)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/terminal.json](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/terminal.json)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/ANALYSIS_PROOF.md](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/ANALYSIS_PROOF.md)；[research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/ANALYSIS_RESULT.json](../../research/ddp/more_graphs_20261027/d14_D3_current1141_source/geodesic_diversity_gate/ANALYSIS_RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixed actual1141 source. Model1: split any old vertex into adjacent children with7+7 old neighbors. Model2 necessary cache only: at most7 deleted edges plus one hub joined to all cut endpoints, at most14 pins. No generated graph/solver.

**仍未完成：** Other1142 graphs/rewiring and the separate <=7-cut/all-endpoints one-hub model remain unexcluded. Necessary support passing would never by itself prove D3.

**启发与重启依据：** The child-degree8 Moore bound permits1142 in principle but actual far-geodesic concentration blocks all sourcevertex splits before coloring or graph generation. The same source has much weaker critical-middle matching than source650; a new edge-freeing batch needs an explicit bounded batch with additional joint constraints, not an inference of feasibility from matching<13.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

