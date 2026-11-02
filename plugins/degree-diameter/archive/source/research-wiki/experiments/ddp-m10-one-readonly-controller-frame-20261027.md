---
type: experiment
node_id: exp:ddp-m10-one-readonly-controller-frame-20261027
title: "M10 read-only A1/B7 central-pair frame reaches236/240 controller states and is rejected"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d14_D4_current9720_source/m10_readonly_capacity/REPORT.md; research/ddp/more_graphs_20261027/d14_D4_current9720_source/m10_readonly_capacity/ANALYSIS_PREDICTION.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/m10_readonly_capacity/ANALYSIS_RESULT.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/m10_readonly_capacity/ANALYSIS_check.py; research/ddp/more_graphs_20261027/d14_D4_current9720_source/m10_readonly_capacity/CONTROLLER_WORD_CERTIFICATE.json"
added: 2026-10-27T22:41:00Z
tags: ["ddp", "method-ledger"]
---

# M10 read-only A1/B7 central-pair frame reaches236/240 controller states and is rejected

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** controller

**目标与阶数：** (16,4)；L=16384；条件性n=19440（未据此计纪录）

**距目标的证据：** The -Iphasebudgetcoversall10, butcomplete341widewords withremainingplainbudgetreach236/240states. MissingSL2matrices-Xa,-Xa^-1 eachatcentralphases3/7. CompletefiberD4impossibleforthisoneframe; broaderM10phasefamilynotexcluded.

**其他指标（保持原计数类型）：**
```json
{
  "controller_order": 240,
  "controller_word_states_reached": 236,
  "minimum_reached_phases_per_SL2": 8,
  "widewords": 341,
  "frames": 1,
  "BFS": 0,
  "fiber_evaluations": 0,
  "new_graphs": 0,
  "CPU_seconds": 0.004616718999999998,
  "prediction": "REFUTED",
  "conditional_order_gap_above_savedL": 3056,
  "separate_guaranteed_transform": {
    "source": [
      13,
      5,
      51457
    ],
    "transformation": "CartesianproductK2",
    "target": [
      14,
      6
    ],
    "guaranteed_order": 102914,
    "saved_publicL": 824124,
    "shortfall": 721210,
    "graphs_generated": 0
  }
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d14_D4_current9720_source/m10_readonly_capacity/REPORT.md](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/m10_readonly_capacity/REPORT.md)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/m10_readonly_capacity/ANALYSIS_PREDICTION.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/m10_readonly_capacity/ANALYSIS_PREDICTION.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/m10_readonly_capacity/ANALYSIS_RESULT.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/m10_readonly_capacity/ANALYSIS_RESULT.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/m10_readonly_capacity/ANALYSIS_check.py](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/m10_readonly_capacity/ANALYSIS_check.py)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/m10_readonly_capacity/CONTROLLER_WORD_CERTIFICATE.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/m10_readonly_capacity/CONTROLLER_WORD_CERTIFICATE.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** ExactlyoneG=SL2(3)xC10 framea=(Xa,1),b=(Xb,7),plainprojectedsteps+/-1,+/-4. Exact<=4 controllerwordimages only; no fibergraph/BFS/phasebatch. Separate arithmeticcheckofaccepted13D5graphCartesianK2doesnotbeat14D6baseline.

**仍未完成：** OtherM10phase/generatorrulesareunresolved; no claimofgeneraldegree16diameter4exclusion.

**启发与重启依据：** Passingonecentrephasecapacitydoesnotguaranteefullcontrollercoverage. Thisoneauthorizedframehasnoactualnewgraphanddoesnotjustify4-slotrepairoraphasegrid. Restart requires a new global route basis; ordinary research remains within the existing user authorization.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

