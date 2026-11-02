---
type: experiment
node_id: exp:ddp-wave6-lamplighter384-capacity
title: "F2⁶⋊C6 shift/toggle完整参数容量"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave6/lamplighter384_capacity/REPORT.md; research/ddp/breadth_20261027_wave6/lamplighter384_capacity/RESULT.json; research/ddp/breadth_20261027_wave6/lamplighter384_capacity/check_capacity.py; research/ddp/breadth_20261027_wave6/lamplighter384_capacity/phase0_words.json; research/ddp/breadth_20261027_wave6/lamplighter384_capacity/terminal.json"
added: 2026-10-27T08:25:52Z
tags: ["ddp", "method-ledger"]
---

# F2⁶⋊C6 shift/toggle完整参数容量

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** capacity

**目标与阶数：** (4,5)；L=364；条件性n=384（未据此计纪录）

**距目标的证据：** phase0全部≤5词仅30形式<64，因此整个指定参数族不行。

**其他指标（保持原计数类型）：**
```json
{
  "phase0_capacity": 30,
  "required_states": 64,
  "graphs_generated": 0
}
```





**原始证据：** [research/ddp/breadth_20261027_wave6/lamplighter384_capacity/REPORT.md](../../research/ddp/breadth_20261027_wave6/lamplighter384_capacity/REPORT.md)；[research/ddp/breadth_20261027_wave6/lamplighter384_capacity/RESULT.json](../../research/ddp/breadth_20261027_wave6/lamplighter384_capacity/RESULT.json)；[research/ddp/breadth_20261027_wave6/lamplighter384_capacity/check_capacity.py](../../research/ddp/breadth_20261027_wave6/lamplighter384_capacity/check_capacity.py)；[research/ddp/breadth_20261027_wave6/lamplighter384_capacity/phase0_words.json](../../research/ddp/breadth_20261027_wave6/lamplighter384_capacity/phase0_words.json)；[research/ddp/breadth_20261027_wave6/lamplighter384_capacity/terminal.json](../../research/ddp/breadth_20261027_wave6/lamplighter384_capacity/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定四生成元{t,t^-1,a,b}全部delta,u,v，允许t阶12

**正向保证：** 完整1365短词校准delta抵消；351返回phase0词

**仍未完成：** 不排其他ring长度或generator机制。

**启发与重启依据：** 须改变phase0路径容量，不搜mask。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

