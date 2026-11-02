---
type: experiment
node_id: exp:ddp-h9-baer13-first-construction-20261027
title: "Baer13折叠blocking邻域：完整新图42398"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/h9_baer_plane_pool/THEOREM.md; research/ddp/more_graphs_20261027/h9_baer_plane_pool/REPORT.md; research/ddp/more_graphs_20261027/h9_baer_plane_pool/RESULT.json; research/ddp/more_graphs_20261027/h9_baer_plane_extensions/REPORT.md; research/ddp/more_graphs_20261027/h9_baer_plane_extensions/RESULT.json; research/ddp/more_graphs_20261027/h9_baer_plane_extensions/first_hit.json; research/ddp/more_graphs_20261027/h9_baer_plane_extensions/independent_first_new_root.json; research/ddp/more_graphs_20261027/h9_baer_plane_extensions/generator_dry_run.json; research/ddp/more_graphs_20261027/h9_baer_plane_extensions/graphs/graph_d12_D5_n42398.edges"
added: 2026-10-27T14:20:17Z
tags: ["ddp", "method-ledger"]
---

# Baer13折叠blocking邻域：完整新图42398

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (12,5)；L=42342；candidate_graph_or_family n=42398

**距目标的证据：** 实际D=5，目标D=5；Complete actual currentR4 induction and one independent fresh-edge-list new-root BFS; no allsource repeat.；13raw Baerpoints foldto11pins; anchor41666 gives full42398graph/m245889/max12/D5. All364 actualmandatory checks covercore41356; firstnewroot independently fromedgefile reachesall42398 within5. 410items=1hit+363coveragefail+46degreeblocked,0UNKNOWN.

**其他指标（保持原计数类型）：**
```json
{
  "new_lower_bound_mathematically_verified": true,
  "improved_parameter_pair": [
    12,
    5
  ],
  "example_orders": [
    42398
  ],
  "example_count": 1,
  "strongest_n": 42398,
  "strongest_m": 245889,
  "raw_pins": 13,
  "folded_pins": 11,
  "anchors": [
    41666
  ],
  "current_source_n": 42397,
  "core_checks": 364,
  "core_counterexamples": 0,
  "independent_roots_checked": 1,
  "last_allsource_order": 42377,
  "new_allsource_executed": false,
  "production_CPU_seconds": 16.312,
  "first_new_root_CPU_seconds": 0.29630095,
  "complete_Lean_instances": 0,
  "Goal_complete": false
}
```





**原始证据：** [research/ddp/more_graphs_20261027/h9_baer_plane_pool/THEOREM.md](../../research/ddp/more_graphs_20261027/h9_baer_plane_pool/THEOREM.md)；[research/ddp/more_graphs_20261027/h9_baer_plane_pool/REPORT.md](../../research/ddp/more_graphs_20261027/h9_baer_plane_pool/REPORT.md)；[research/ddp/more_graphs_20261027/h9_baer_plane_pool/RESULT.json](../../research/ddp/more_graphs_20261027/h9_baer_plane_pool/RESULT.json)；[research/ddp/more_graphs_20261027/h9_baer_plane_extensions/REPORT.md](../../research/ddp/more_graphs_20261027/h9_baer_plane_extensions/REPORT.md)；[research/ddp/more_graphs_20261027/h9_baer_plane_extensions/RESULT.json](../../research/ddp/more_graphs_20261027/h9_baer_plane_extensions/RESULT.json)；[research/ddp/more_graphs_20261027/h9_baer_plane_extensions/first_hit.json](../../research/ddp/more_graphs_20261027/h9_baer_plane_extensions/first_hit.json)；[research/ddp/more_graphs_20261027/h9_baer_plane_extensions/independent_first_new_root.json](../../research/ddp/more_graphs_20261027/h9_baer_plane_extensions/independent_first_new_root.json)；[research/ddp/more_graphs_20261027/h9_baer_plane_extensions/generator_dry_run.json](../../research/ddp/more_graphs_20261027/h9_baer_plane_extensions/generator_dry_run.json)；[research/ddp/more_graphs_20261027/h9_baer_plane_extensions/graphs/graph_d12_D5_n42398.edges](../../research/ddp/more_graphs_20261027/h9_baer_plane_extensions/graphs/graph_d12_D5_n42398.edges)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** All7560 Baer subplanes in each of364F3-center H9flatplanes;410degreelegal foldedsets atsource42397,one sequential completeextension. These are not Qline or partialQline pinsets.

**仍未完成：** Complete Lean remains unfinished; no global optimality or public acceptance claim.

**启发与重启依据：** Retain exact source and finite scope; no same-base restart or unbounded local-score optimization.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

