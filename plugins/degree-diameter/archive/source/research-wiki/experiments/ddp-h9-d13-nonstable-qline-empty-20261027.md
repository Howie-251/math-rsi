---
type: experiment
node_id: exp:ddp-h9-d13-nonstable-qline-empty-20261027
title: "(13,5)非稳定线wholeclass：43680闭包也被满度挡住"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d13_D5_h9_transfer/nonstable_qline_pool/REPORT.md; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/nonstable_qline_pool/RESULT.json; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/nonstable_qline_pool/PREDICTION.json"
added: 2026-10-27T17:26:52Z
tags: ["ddp", "method-ledger"]
---

# (13,5)非稳定线wholeclass：43680闭包也被满度挡住

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** (13,5)；L=51417；条件性n=51418（未据此计纪录）

**距目标的证据：** 1120个F3plane中87360个nonstable Q9line occurrences共轭合并为43680次closure实际检查；12960闭包的唯一fixed点free，12096闭包card≤13，但所有closure均有满度pin，合法池0。

**其他指标（保持原计数类型）：**
```json
{
  "nominal_occurrences": 87360,
  "closure_tests": 43680,
  "conjugate_identical_duplicates_skipped": 43680,
  "stable_lines_repeated": 0,
  "degree_feasible": 0,
  "card_atmost13": 12096,
  "CPU_seconds": 0.19877266,
  "BFS": 0,
  "diagnostic_recovery_CPU_seconds": 0.17191,
  "diagnostic_recovery_new_line_experiments": 0,
  "one_saturated_diagnostics": 12,
  "one_saturated_full_pin_counts": {
    "19": 12
  },
  "one_saturated_after_deletion_counts": {
    "18": 12
  },
  "feasible_singlefault_pool": 0,
  "prediction": "REFUTED"
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d13_D5_h9_transfer/nonstable_qline_pool/REPORT.md](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/nonstable_qline_pool/REPORT.md)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/nonstable_qline_pool/RESULT.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/nonstable_qline_pool/RESULT.json)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/nonstable_qline_pool/PREDICTION.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/nonstable_qline_pool/PREDICTION.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 1120个F3plane中87360个nonstable Q9line occurrences共轭合并为43680次closure实际检查；12960闭包的唯一fixed点free，12096闭包card≤13，但所有closure均有满度pin，合法池0。

**仍未完成：** General source extension feasibility remains open; no complete newgraph was generated.

**启发与重启依据：** 只需1个free固定点的预测仍被其余满度pin反驳。12个仅1满pin诊断全部fullsize19，删后18>13，无singlefault生产池；这次0.172CPU恢复诊断不计新line实验。停止该固定scope，不扩其它plane或删多点。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

