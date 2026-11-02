---
type: experiment
node_id: exp:ddp-h9-d12-ninepin-saturated-deletion-20261027
title: "删除唯一饱和Q-line pin并补三anchor：完整42397图"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/REPORT.md; research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/RESULT.json; research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/first_hit.json; research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/anchor_complementarity.json; research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/coreguard_prediction_check.json; research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/generator_dry_run.json"
added: 2026-10-27T14:08:25Z
tags: ["ddp", "method-ledger"]
---

# 删除唯一饱和Q-line pin并补三anchor：完整42397图

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (12,5)；L=42342；candidate_graph_or_family n=42397

**距目标的证据：** 实际D=5，目标D=5；Accepted by complete actual selectedR4 and currentdegree production induction from42396; no new allsourceBFS.；1完整图42397/m245877，pool43删13863，anchors3881/22612/41614；45visited=1hit+44limited，81未试，不判整族失败。32.002577父+child CPU，编译未单独计入。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs_generated": 1,
  "new_lower_bound_mathematically_verified": false,
  "represented_in_main_family": true,
  "actual_new_graph_order": 42397,
  "source_n": 42396,
  "deleted_saturated_pin": 13863,
  "raw_candidates": 126,
  "selected": 64,
  "visited": 45,
  "limited_unknown": 44,
  "unattempted_total": 81,
  "production_parent_and_child_CPU_seconds": 32.002577,
  "compile_CPU_separately_measured": false,
  "missing_core_before_anchors": 39,
  "missing_extra_before_anchors": 47,
  "complete_selectedR4_missing": 0,
  "ordinary_allsource_BFS_executed": 0,
  "Lean_complete": false
}
```



**从属变体：**
```json
[
  {
    "order": 42397,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/REPORT.md](../../research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/REPORT.md)；[research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/RESULT.json](../../research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/RESULT.json)；[research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/first_hit.json](../../research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/first_hit.json)；[research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/anchor_complementarity.json](../../research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/anchor_complementarity.json)；[research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/coreguard_prediction_check.json](../../research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/coreguard_prediction_check.json)；[research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/generator_dry_run.json](../../research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/generator_dry_run.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Current42396,126 original ten-pin sets with exactlyone saturated pin; freeze first64,visit45 before production budget. Remove saturated pin,add at mostthree freeoldanchors; no assumption that ninepins retain geometric corecoverage.

**正向保证：** Actual wholegraphR4 covered all42396 vertices, olddegrees remain<=12, newdegree12.；Deleted13863 remained full and was not reinserted.；Saved masks:3881 covers all39 missingcore vertices;22612 and41614 have7 and12 private-extra targets.

**仍未完成：** Complete concrete Lean instances remain unfinished. Earlier failures are scoped to their actual bases; no family maximality claim.

**启发与重启依据：** FullQline containment is sufficient, not necessary. Removing a saturated pin can work with three anchors; actual global coverage decides. One large-hole case has a unique coreguard, so corehole count alone does not decide difficulty.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

