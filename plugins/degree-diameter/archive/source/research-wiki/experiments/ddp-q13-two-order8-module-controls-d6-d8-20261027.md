---
type: experiment
node_id: exp:ddp-q13-two-order8-module-controls-d6-d8-20261027
title: "q13 two order8-action controls: both137904-vertex degree6 graphs have D9"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q13_D8_controls/REPORT.md; research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q13_D8_controls/PREDICTION.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q13_D8_controls/RESULT.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q13_D8_controls/terminal.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q13_D8_controls/probe.cpp"
added: 2026-10-27T20:53:04Z
tags: ["ddp", "method-ledger"]
---

# q13 two order8-action controls: both137904-vertex degree6 graphs have D9

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (6,8)；L=80050；candidate_graph_or_family n=137904

**距目标的证据：** 实际D=9，目标D=8；Both simple/connected6regular137904/413712, global exactD9; identity R8 missing1762/1624. Both controls terminal,0hit/unknown/untried.

**其他指标（保持原计数类型）：**
```json
{
  "actual_new_graphs": 2,
  "inherited_graphs": 0,
  "complete_identity_BFS": 2,
  "source_D7_BFS_repeated": 0,
  "exact_global_D_per_control": [
    9,
    9
  ],
  "identity_R8_missing_per_control": [
    1762,
    1624
  ],
  "ordinary_bad_pair_count_units": "Not measured; root missing targets stored separately",
  "native_CPU_seconds_per_control": [
    0.010722,
    0.010853
  ],
  "compile_and_native_child_CPU_seconds": 0.8116359999999999,
  "new_lower_bounds": 0,
  "prediction": "REFUTED",
  "UNKNOWN": 0,
  "untried": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q13_D8_controls/REPORT.md](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q13_D8_controls/REPORT.md)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q13_D8_controls/PREDICTION.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q13_D8_controls/PREDICTION.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q13_D8_controls/RESULT.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q13_D8_controls/RESULT.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q13_D8_controls/terminal.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q13_D8_controls/terminal.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q13_D8_controls/probe.cpp](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q13_D8_controls/probe.cpp)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Exactly two frozen q13 matrices with source H48 phases, chi17=5, B_normal=(0,1), C_normal=(0,2). Two new actual Cayley graphs; one complete identity BFS each, no inherited q13 graph.

**仍未完成：** Other field, action, voltage, phase and vector choices outside the stated finite family are not excluded. This is not a general degree/diameter upper bound.

**启发与重启依据：** Order8 action relations and six true inverse-paired generators preserve the group and degree, but did not ensure D8. Stop these two controls; any future experiment must change a coverage-relevant rule and have separate authorization.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

