---
type: experiment
node_id: exp:ddp-wave2-line1664-d4
title: "固定Bhakar104×F2⁴二邻点线关系提升"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave2/line1664_d4/REPORT.md; research/ddp/breadth_20261027_wave2/line1664_d4/capacity.json; research/ddp/breadth_20261027_wave2/line1664_d4/controller_short_walk_witness.json; research/ddp/breadth_20261027_wave2/line1664_d4/root_controller_witness_check.json; research/ddp/breadth_20261027_wave2/line1664_d4/run.json; research/ddp/breadth_20261027_wave2/line1664_d4/scope.json; research/ddp/breadth_20261027_wave2/line1664_d4/terminal.json"
added: 2026-10-27T07:55:16Z
tags: ["ddp", "method-ledger"]
---

# 固定Bhakar104×F2⁴二邻点线关系提升

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** capacity

**目标与阶数：** (8,4)；L=1100；条件性n=1664（未据此计纪录）

**距目标的证据：** 0→32只有唯一三路且无其他≤4walk，至多8<16，指定投影模板统一排除。

**其他指标（保持原计数类型）：**
```json
{
  "capacity": 8,
  "required_states": 16,
  "graphs_generated": 0,
  "source_n": 104,
  "all_walk_witness": [
    0,
    24,
    4,
    32
  ]
}
```





**原始证据：** [research/ddp/breadth_20261027_wave2/line1664_d4/REPORT.md](../../research/ddp/breadth_20261027_wave2/line1664_d4/REPORT.md)；[research/ddp/breadth_20261027_wave2/line1664_d4/capacity.json](../../research/ddp/breadth_20261027_wave2/line1664_d4/capacity.json)；[research/ddp/breadth_20261027_wave2/line1664_d4/controller_short_walk_witness.json](../../research/ddp/breadth_20261027_wave2/line1664_d4/controller_short_walk_witness.json)；[research/ddp/breadth_20261027_wave2/line1664_d4/root_controller_witness_check.json](../../research/ddp/breadth_20261027_wave2/line1664_d4/root_controller_witness_check.json)；[research/ddp/breadth_20261027_wave2/line1664_d4/run.json](../../research/ddp/breadth_20261027_wave2/line1664_d4/run.json)；[research/ddp/breadth_20261027_wave2/line1664_d4/scope.json](../../research/ddp/breadth_20261027_wave2/line1664_d4/scope.json)；[research/ddp/breadth_20261027_wave2/line1664_d4/terminal.json](../../research/ddp/breadth_20261027_wave2/line1664_d4/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定104投影、16fiber、无内部边、每控制边最多两个邻点，含非线性关系放宽

**正向保证：** 完整walk包含反走；源104D4复用

**仍未完成：** 不排其他控制图、内部边、更大branch或一般1664图。

**启发与重启依据：** 须改变投影路线容量；矩阵/seed不能补足。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

