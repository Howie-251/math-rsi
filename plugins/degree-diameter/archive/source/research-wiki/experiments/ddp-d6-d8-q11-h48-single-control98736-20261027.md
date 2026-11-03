---
type: experiment
node_id: exp:ddp-d6-d8-q11-h48-single-control98736-20261027
title: "(6,8)q11源比率单控制：98736六价Cayley实际D9"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q11_D8_control/REPORT.md; research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q11_D8_control/PREDICTION.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q11_D8_control/RESULT.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q11_D8_control/RECIPE.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q11_D8_control/probe.cpp; research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q11_D8_control/run.py"
added: 2026-10-27T20:51:14Z
tags: ["ddp", "method-ledger"]
---

# (6,8)q11源比率单控制：98736六价Cayley实际D9

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (6,8)；L=80050；candidate_graph_or_family n=98736；条件性n=98736（未据此计纪录）

**距目标的证据：** 实际D=9，目标D=8；实际connectedCayley图identity完整BFS；lefttranslations为全图一个轨道，所以ecc9=全D9。；唯一控制D8预测REFUTED，无positive edgefile，不扩大q11参数。986为fixedroot-target缺项，非普通无序全图坏对。

**其他指标（保持原计数类型）：**
```json
{
  "q": 11,
  "group_order": 98736,
  "m": 296208,
  "simple": true,
  "connected": true,
  "root_BFS": 1,
  "root_R8_missing": 986,
  "distance_histogram": [
    1,
    6,
    30,
    150,
    736,
    3568,
    15429,
    44655,
    33175,
    986
  ],
  "source_BFS_repeated": 0,
  "new_edgefile_exported": false,
  "separate_from_D7_2625": true,
  "native_CPU_seconds": 0.007772,
  "compile_CPU_seconds": 0.708840925,
  "total_batch_CPU_seconds": 0.7186196559999999,
  "baseline_date": "2026-10-27",
  "baseline_provenance": "Parentprovided80050/currenttable refresh separatelyownedbyroot."
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q11_D8_control/REPORT.md](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q11_D8_control/REPORT.md)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q11_D8_control/PREDICTION.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q11_D8_control/PREDICTION.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q11_D8_control/RESULT.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q11_D8_control/RESULT.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q11_D8_control/RECIPE.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q11_D8_control/RECIPE.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q11_D8_control/probe.cpp](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q11_D8_control/probe.cpp)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q11_D8_control/run.py](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/field_module_lift/q11_D8_control/run.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 唯一F11²×C17⋊H48控制；χ17α5，alpha[[7,5],[1,4]]/beta[[0,10],[1,10]]，sourceH/c17parts固定；A_V0,B_V(0,1),C_V(0,2)=2B。trueinverse由新群重算。actual98736/296208/simple/undirected6reg connected，一根BFS全n访问，R8漏986/ecc9。

**仍未完成：** Otherq11normalsettings or general(6,8)graphs notexcluded.

**启发与重启依据：** 保持sourceC=2B和H/χ关系仍不足D8；停止单控制。原q7/q8/q9±2625D7族是另一授权范围，不能把本case混入。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

