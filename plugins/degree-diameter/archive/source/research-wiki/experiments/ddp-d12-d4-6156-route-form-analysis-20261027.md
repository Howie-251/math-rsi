---
type: experiment
node_id: exp:ddp-d12-d4-6156-route-form-analysis-20261027
title: "6156对照：19形式容量预测被反驳，发现R2筛选可放宽"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/RESULT.json; research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/PENCIL_APPLICABILITY.json; research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/NUMERIC_WORD_TABLES.json"
added: 2026-10-27T18:21:15Z
tags: ["ddp", "method-ledger"]
---

# 6156对照：19形式容量预测被反驳，发现R2筛选可放宽

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (12,4)；L=6156；条件性n=6480（未据此计纪录）

**距目标的证据：** 实际chart reduced4共108：100rank4、8rank3，与作者badwords一致。G4+even至少23不同形式，x0形式容量最小2277>20×81，故不是简单局部19容量上限。原同一voltage向量mod19证书全覆盖，mod20 strict与wide各漏54controller槽，x0 word-image缺3708 endpoints；未构造6480图。

**其他指标（保持原计数类型）：**
```json
{
  "reduced4_words": 108,
  "rank4_words": 100,
  "rank3_words": 8,
  "min_full_certificate_forms": 23,
  "min_x0_form_incidence_capacity": 2277,
  "local19_capacity_prediction": "REFUTED",
  "fixed_voltage_profiles": 2,
  "mod20_strict_missing_controller_slots": 54,
  "mod20_wide_missing_controller_slots": 54,
  "mod20_x0_word_image_missing_endpoints": 3708,
  "count_type": "wordimage/sourcezero endpoint diagnostics, not unorderedbadpairs",
  "CPU_seconds": 0.011393669,
  "graph_generated": false,
  "BFS": 0,
  "voltage_grid_assignments": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/RESULT.json](../../research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/RESULT.json)；[research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/PENCIL_APPLICABILITY.json](../../research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/PENCIL_APPLICABILITY.json)；[research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/NUMERIC_WORD_TABLES.json](../../research/ddp/more_graphs_20261027/d12_D4_current6156/route_capacity_analysis/NUMERIC_WORD_TABLES.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 实际chart reduced4共108：100rank4、8rank3，与作者badwords一致。G4+even至少23不同形式，x0形式容量最小2277>20×81，故不是简单局部19容量上限。原同一voltage向量mod19证书全覆盖，mod20 strict与wide各漏54controller槽，x0 word-image缺3708 endpoints；未构造6480图。

**仍未完成：** No complete newgraph in this finite experiment; unrelatedrules and finalLean remain open.

**启发与重启依据：** 旧Mizuno pencil引理对任意reduced2word适用，不要求其为最短路；作者程序只豁免最短dist2，故20..27 strict-filter无passer不等于图族数学排除。新检验应只改有证明依据的I∪R2∪G4 admissibility，并先冻结zero-triangle差异切片，不重旧strict负范围。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

