---
type: experiment
node_id: exp:ddp-q53-two-module-controls-degree6-d10-20261027
title: "F53² two order8-action controls: both 2,292,144-vertex Cayley graphs have exact D11"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/REPORT.md; research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/PREDICTION.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/RESULT.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/MODEL.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/MATRIX_VALIDITY.md; research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/MATRIX_VALIDITY.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/probe.cpp; research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/run.py; research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/checkpoint.json"
added: 2026-10-27T20:51:14Z
tags: ["ddp", "method-ledger"]
---

# F53² two order8-action controls: both 2,292,144-vertex Cayley graphs have exact D11

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (6,10)；L=1394189；candidate_graph_or_family n=2292144

**距目标的证据：** 实际D=11，目标D=10；Both simple connected 6regular n2292144/m6876432; exact global D11 by Cayley transitivity and complete identity BFS. Root R10 missing targets5596/6886 respectively; both controls complete, no hits/unknown/untested. No failed graph edge export and no new lower bound.

**其他指标（保持原计数类型）：**
```json
{
  "actual_controls": 2,
  "identity_full_BFS_count": 2,
  "global_D_per_control": [
    11,
    11
  ],
  "root_R10_missing_per_control": [
    5596,
    6886
  ],
  "first_root_witnesses": [
    335,
    86
  ],
  "native_CPU_seconds": 0.24124,
  "total_parent_children_CPU_seconds": 1.049405686,
  "new_lower_bounds": 0,
  "prediction": "REFUTED",
  "ordinary_bad_count_units": "Root missing targets are separate from unordered bad pairs"
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/REPORT.md](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/REPORT.md)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/PREDICTION.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/PREDICTION.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/RESULT.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/RESULT.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/MODEL.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/MODEL.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/MATRIX_VALIDITY.md](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/MATRIX_VALIDITY.md)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/MATRIX_VALIDITY.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/MATRIX_VALIDITY.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/probe.cpp](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/probe.cpp)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/run.py](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/run.py)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/checkpoint.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q53_D10_controls/checkpoint.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Exactly the two frozen q53 alpha matrices, beta=[[0,-1],[1,-1]], chi17(alpha)=5, source H48 phases and c coordinates, B_normal=(0,1), C_normal=(0,2). Two complete actual implicit Cayley models and identity BFSs; no source D7 BFS.

**仍未完成：** Other generators/matrices/modules and arbitrary N(6,10) constructions are not excluded.

**启发与重启依据：** Matching source normal-action order8 and retaining C=2B kept the algebraic relations and degree but did not guarantee D10. This closes the two explicit controls only; no automatic field/vector/matrix expansion or bad-target tuning.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

