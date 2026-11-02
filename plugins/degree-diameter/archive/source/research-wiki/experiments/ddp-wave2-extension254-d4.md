---
type: experiment
node_id: exp:ddp-wave2-extension254-d4
title: "252→254四matching-edge双点增阶"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave2/extension254_d4/REPORT.md; research/ddp/breadth_20261027_wave2/extension254_d4/best.edges; research/ddp/breadth_20261027_wave2/extension254_d4/best.independent_check.json; research/ddp/breadth_20261027_wave2/extension254_d4/best.json; research/ddp/breadth_20261027_wave2/extension254_d4/first.cpp_calibration.json; research/ddp/breadth_20261027_wave2/extension254_d4/first.expected.edges; research/ddp/breadth_20261027_wave2/extension254_d4/first.independent_calibration.json; research/ddp/breadth_20261027_wave2/extension254_d4/inputs.json; research/ddp/breadth_20261027_wave2/extension254_d4/run.json; research/ddp/breadth_20261027_wave2/extension254_d4/source.edges; research/ddp/breadth_20261027_wave2/extension254_d4/source_check.json; research/ddp/breadth_20261027_wave2/extension254_d4/starts.jsonl; research/ddp/breadth_20261027_wave2/extension254_d4/starts.txt; research/ddp/breadth_20261027_wave2/extension254_d4/terminal.json"
added: 2026-10-27T08:25:51Z
tags: ["ddp", "method-ledger"]
---

# 252→254四matching-edge双点增阶

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (5,4)；L=252；candidate_graph_or_family n=254；条件性n=254（未据此计纪录）

**距目标的证据：** 实际D=5，目标D=4；普通无序坏对=133；saved_explicit_graph；bestD5/133，完成有限批次，不是所有四matching扩张穷尽。

**其他指标（保持原计数类型）：**
```json
{
  "proposals": 80000,
  "legal_trials": 78252
}
```





**原始证据：** [research/ddp/breadth_20261027_wave2/extension254_d4/REPORT.md](../../research/ddp/breadth_20261027_wave2/extension254_d4/REPORT.md)；[research/ddp/breadth_20261027_wave2/extension254_d4/best.edges](../../research/ddp/breadth_20261027_wave2/extension254_d4/best.edges)；[research/ddp/breadth_20261027_wave2/extension254_d4/best.independent_check.json](../../research/ddp/breadth_20261027_wave2/extension254_d4/best.independent_check.json)；[research/ddp/breadth_20261027_wave2/extension254_d4/best.json](../../research/ddp/breadth_20261027_wave2/extension254_d4/best.json)；[research/ddp/breadth_20261027_wave2/extension254_d4/first.cpp_calibration.json](../../research/ddp/breadth_20261027_wave2/extension254_d4/first.cpp_calibration.json)；[research/ddp/breadth_20261027_wave2/extension254_d4/first.expected.edges](../../research/ddp/breadth_20261027_wave2/extension254_d4/first.expected.edges)；[research/ddp/breadth_20261027_wave2/extension254_d4/first.independent_calibration.json](../../research/ddp/breadth_20261027_wave2/extension254_d4/first.independent_calibration.json)；[research/ddp/breadth_20261027_wave2/extension254_d4/inputs.json](../../research/ddp/breadth_20261027_wave2/extension254_d4/inputs.json)；[research/ddp/breadth_20261027_wave2/extension254_d4/run.json](../../research/ddp/breadth_20261027_wave2/extension254_d4/run.json)；[research/ddp/breadth_20261027_wave2/extension254_d4/source.edges](../../research/ddp/breadth_20261027_wave2/extension254_d4/source.edges)；[research/ddp/breadth_20261027_wave2/extension254_d4/source_check.json](../../research/ddp/breadth_20261027_wave2/extension254_d4/source_check.json)；[research/ddp/breadth_20261027_wave2/extension254_d4/starts.jsonl](../../research/ddp/breadth_20261027_wave2/extension254_d4/starts.jsonl)；[research/ddp/breadth_20261027_wave2/extension254_d4/starts.txt](../../research/ddp/breadth_20261027_wave2/extension254_d4/starts.txt)；[research/ddp/breadth_20261027_wave2/extension254_d4/terminal.json](../../research/ddp/breadth_20261027_wave2/extension254_d4/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定252源四条不接边及方向；8starts×10000提案

**正向保证：** 全部候选simple5regular254/635

**仍未完成：** 其他四matching赋值和其他254图仍开放。

**启发与重启依据：** 固定批次停止，不加seed/删边数/source。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

