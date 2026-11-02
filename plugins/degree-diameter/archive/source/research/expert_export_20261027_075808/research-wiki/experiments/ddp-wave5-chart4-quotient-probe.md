---
type: experiment
node_id: exp:ddp-wave5-chart4-quotient-probe
title: "F3⁴通用四步chart：108词满秩"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave5/chart4_quotient_probe/RESULT.json"
added: 2026-10-27T07:55:17Z
tags: ["ddp", "method-ledger"]
---

# F3⁴通用四步chart：108词满秩

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** word-rank

**目标与阶数：** (12,4)；L=5832；条件性n=5913（未据此计纪录）

**距目标的证据：** 108/108约化长度四词rank4；正向结果。

**其他指标（保持原计数类型）：**
```json
{
  "rank_words_total": 108,
  "rank4_words": 108,
  "minimum_controller_order_to_exceed": 73
}
```





**原始证据：** [research/ddp/breadth_20261027_wave5/chart4_quotient_probe/RESULT.json](../../research/ddp/breadth_20261027_wave5/chart4_quotient_probe/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 保存F3⁵ chart公共不变线的四维商；局部线性规则，不是整图

**正向保证：** 任意quartic exact-NB4 controller C可条件性给81|C|点、degree12、D≤4

**仍未完成：** 尚缺≥73点合格controller；不能沿用原72的pencil修补到此quotient chart。

**启发与重启依据：** 有明确控制器结构与覆盖证书时才值得继续；不要把局部满秩当新下界。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

