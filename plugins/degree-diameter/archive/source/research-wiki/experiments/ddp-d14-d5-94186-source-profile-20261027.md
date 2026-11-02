---
type: experiment
node_id: exp:ddp-d14-d5-94186-source-profile-20261027
title: "(14,5)94186源实际绑定：3685可接点、3700槽"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/REPORT.md; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/SOURCE.json; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/SOURCE_PROFILE.json"
added: 2026-10-27T17:26:52Z
tags: ["ddp", "method-ledger"]
---

# (14,5)94186源实际绑定：3685可接点、3700槽

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (14,5)；L=94186；known_source_or_recovery n=94186

**距目标的证据：** 实际完整边表94186/m657452，degree12:15、13:3670、14:90501，free3685/slots3700。旧Mizuno88452源在相同labels仅111共同边，未恢复纤维映射；数值前缀不能当旧核心。

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 94186,
  "source_m": 657452,
  "degree_histogram": {
    "12": 15,
    "13": 3670,
    "14": 90501
  },
  "free_vertices": 3685,
  "free_slots": 3700,
  "source_allBFS": 0,
  "CPU_seconds": 1.141946663
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/REPORT.md](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/REPORT.md)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/SOURCE.json](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/SOURCE.json)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/SOURCE_PROFILE.json](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/SOURCE_PROFILE.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 实际完整边表94186/m657452，degree12:15、13:3670、14:90501，free3685/slots3700。旧Mizuno88452源在相同labels仅111共同边，未恢复纤维映射；数值前缀不能当旧核心。

**仍未完成：** No third-parameter complete record has been generated in these source/rareclass stages.

**启发与重启依据：** 只继承公开源D5，不重全源。以实际free slots和邻域类型选择覆盖预测，不能照搬原fiber labels。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

