---
type: experiment
node_id: exp:ddp-wave5-nb4-base-capacity
title: "两个6点基图×C13的exact-NB4必要筛"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave5/nb4_base_capacity/REPORT.md; research/ddp/breadth_20261027_wave5/nb4_base_capacity/RESULT.json; research/ddp/breadth_20261027_wave5/nb4_base_capacity/capacity.py; research/ddp/breadth_20261027_wave5/nb4_base_capacity/terminal.json"
added: 2026-10-27T08:25:52Z
tags: ["ddp", "method-ledger"]
---

# 两个6点基图×C13的exact-NB4必要筛

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** capacity

**目标与阶数：** (12,4)；L=5832；条件性n=6318（未据此计纪录）

**距目标的证据：** 两base各有slot仅8条具名NB4词，8<13；甚至同base任意uniform≥9fiber均不行。

**其他指标（保持原计数类型）：**
```json
{
  "hypothetical_controller_n": 78,
  "required_sheet_states": 13,
  "witness_word_capacity": 8,
  "graphs_generated": 0
}
```





**原始证据：** [research/ddp/breadth_20261027_wave5/nb4_base_capacity/REPORT.md](../../research/ddp/breadth_20261027_wave5/nb4_base_capacity/REPORT.md)；[research/ddp/breadth_20261027_wave5/nb4_base_capacity/RESULT.json](../../research/ddp/breadth_20261027_wave5/nb4_base_capacity/RESULT.json)；[research/ddp/breadth_20261027_wave5/nb4_base_capacity/capacity.py](../../research/ddp/breadth_20261027_wave5/nb4_base_capacity/capacity.py)；[research/ddp/breadth_20261027_wave5/nb4_base_capacity/terminal.json](../../research/ddp/breadth_20261027_wave5/nb4_base_capacity/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 原144机制6base及octahedron两固定base，所有电压赋值；不排其他base

**正向保证：** 具名平行边按真实反走规则处理；完整36槽形式计数

**仍未完成：** 仅阻断这两base；不是普通D4或一般78controller不存在。

**启发与重启依据：** 必须更换路径容量不足的结构，换电压/群不补足8条词。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

