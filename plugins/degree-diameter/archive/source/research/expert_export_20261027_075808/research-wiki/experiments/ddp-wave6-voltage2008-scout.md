---
type: experiment
node_id: exp:ddp-wave6-voltage2008-scout
title: "Loz–Širáň2008 B/D/T/X原规则门槛筛"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave6/voltage2008_scout/REPORT.md; research/ddp/breadth_20261027_wave6/voltage2008_scout/RESULT.json"
added: 2026-10-27T07:55:17Z
tags: ["ddp", "method-ledger"]
---

# Loz–Širáň2008 B/D/T/X原规则门槛筛

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (?,?)；L=不适用／见变体

**距目标的证据：** 无越线；(8,4)=1100仅追平。未试过的完整T(1,1)例D8超范围。

**其他指标（保持原计数类型）：**
```json
{
  "formulas": {
    "B": "n=mn,degree=s+2l",
    "D": "n=2mn,degree=2l+e",
    "T": "n=3mn,degree=2l+2e",
    "X": "n=4mn,degree=2l+3e"
  },
  "untried_source_example": {
    "n": 3243,
    "Delta": 4,
    "source_reported_D": 8
  }
}
```





**原始证据：** [research/ddp/breadth_20261027_wave6/voltage2008_scout/REPORT.md](../../research/ddp/breadth_20261027_wave6/voltage2008_scout/REPORT.md)；[research/ddp/breadth_20261027_wave6/voltage2008_scout/RESULT.json](../../research/ddp/breadth_20261027_wave6/voltage2008_scout/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 原文给定D3/4/5、degree≤12实例与27格保存门槛比较

**正向保证：** 恢复完整边规则与all ordered base slots voltage coverage条件

**仍未完成：** 概率引理有存在前提，不能倒置为新参数存在证明。

**启发与重启依据：** 需有可验证越线参数和覆盖步骤，不能再开群名队列。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

