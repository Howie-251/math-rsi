---
type: experiment
node_id: exp:ddp-wave2-sl23-c8-biorbit384-d5
title: "SL2(F3)×C8双轨道2+2模板"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave2/sl23_c8_biorbit384_d5/REPORT.md; research/ddp/breadth_20261027_wave2/sl23_c8_biorbit384_d5/BEST_QUOTIENT_WITNESS.json; research/ddp/breadth_20261027_wave2/sl23_c8_biorbit384_d5/CAPACITY.json; research/ddp/breadth_20261027_wave2/sl23_c8_biorbit384_d5/capacity.raw.json; research/ddp/breadth_20261027_wave2/sl23_c8_biorbit384_d5/capacity_input.txt; research/ddp/breadth_20261027_wave2/sl23_c8_biorbit384_d5/sl23.json; research/ddp/breadth_20261027_wave2/sl23_c8_biorbit384_d5/terminal.json"
added: 2026-10-27T08:25:51Z
tags: ["ddp", "method-ledger"]
---

# SL2(F3)×C8双轨道2+2模板

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** capacity

**目标与阶数：** (4,5)；L=364；条件性n=384（未据此计纪录）

**距目标的证据：** 最大最小fiber容量5<8，全固定模板排除；未开实际图profile。

**其他指标（保持原计数类型）：**
```json
{
  "quotient_triples": 13824,
  "capacity": 5,
  "required_states": 8,
  "graphs_generated": 0
}
```





**原始证据：** [research/ddp/breadth_20261027_wave2/sl23_c8_biorbit384_d5/REPORT.md](../../research/ddp/breadth_20261027_wave2/sl23_c8_biorbit384_d5/REPORT.md)；[research/ddp/breadth_20261027_wave2/sl23_c8_biorbit384_d5/BEST_QUOTIENT_WITNESS.json](../../research/ddp/breadth_20261027_wave2/sl23_c8_biorbit384_d5/BEST_QUOTIENT_WITNESS.json)；[research/ddp/breadth_20261027_wave2/sl23_c8_biorbit384_d5/CAPACITY.json](../../research/ddp/breadth_20261027_wave2/sl23_c8_biorbit384_d5/CAPACITY.json)；[research/ddp/breadth_20261027_wave2/sl23_c8_biorbit384_d5/capacity.raw.json](../../research/ddp/breadth_20261027_wave2/sl23_c8_biorbit384_d5/capacity.raw.json)；[research/ddp/breadth_20261027_wave2/sl23_c8_biorbit384_d5/capacity_input.txt](../../research/ddp/breadth_20261027_wave2/sl23_c8_biorbit384_d5/capacity_input.txt)；[research/ddp/breadth_20261027_wave2/sl23_c8_biorbit384_d5/sl23.json](../../research/ddp/breadth_20261027_wave2/sl23_c8_biorbit384_d5/sl23.json)；[research/ddp/breadth_20261027_wave2/sl23_c8_biorbit384_d5/terminal.json](../../research/ddp/breadth_20261027_wave2/sl23_c8_biorbit384_d5/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定group及2+2分配全部13824个SL quotient triples

**仍未完成：** 不排其他生成元组成、群或非同模板图。

**启发与重启依据：** 需改变quotient短路容量。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

