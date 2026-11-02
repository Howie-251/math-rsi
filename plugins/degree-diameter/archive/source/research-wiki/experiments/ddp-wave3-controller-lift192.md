---
type: experiment
node_id: exp:ddp-wave3-controller-lift192
title: "原6点base的C4×C8电压192控制器"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave3/controller_lift192/REPORT.md; research/ddp/breadth_20261027_wave3/controller_lift192/base_words.json; research/ddp/breadth_20261027_wave3/controller_lift192/best.edges; research/ddp/breadth_20261027_wave3/controller_lift192/best.independent_check.json; research/ddp/breadth_20261027_wave3/controller_lift192/best.labels.json; research/ddp/breadth_20261027_wave3/controller_lift192/capacity.json; research/ddp/breadth_20261027_wave3/controller_lift192/first_calibration.json; research/ddp/breadth_20261027_wave3/controller_lift192/input.txt; research/ddp/breadth_20261027_wave3/controller_lift192/search_output.json; research/ddp/breadth_20261027_wave3/controller_lift192/terminal.json"
added: 2026-10-27T08:25:51Z
tags: ["ddp", "method-ledger"]
---

# 原6点base的C4×C8电压192控制器

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** controller

**目标与阶数：** (12,5)；L=42342；controller n=192；条件性n=46656（未据此计纪录）

**距目标的证据：** 实际D=6，目标D=5；普通无序坏对=144；saved_controller_only;hypothetical_lift_not_generated；best controller ordinaryD6/144；exactNB5缺2752有序对。

**其他指标（保持原计数类型）：**
```json
{
  "representative_NB5_misses": 86,
  "exact_NB5_missing_ordered_pairs": 2752,
  "proposals": 200000
}
```





**原始证据：** [research/ddp/breadth_20261027_wave3/controller_lift192/REPORT.md](../../research/ddp/breadth_20261027_wave3/controller_lift192/REPORT.md)；[research/ddp/breadth_20261027_wave3/controller_lift192/base_words.json](../../research/ddp/breadth_20261027_wave3/controller_lift192/base_words.json)；[research/ddp/breadth_20261027_wave3/controller_lift192/best.edges](../../research/ddp/breadth_20261027_wave3/controller_lift192/best.edges)；[research/ddp/breadth_20261027_wave3/controller_lift192/best.independent_check.json](../../research/ddp/breadth_20261027_wave3/controller_lift192/best.independent_check.json)；[research/ddp/breadth_20261027_wave3/controller_lift192/best.labels.json](../../research/ddp/breadth_20261027_wave3/controller_lift192/best.labels.json)；[research/ddp/breadth_20261027_wave3/controller_lift192/capacity.json](../../research/ddp/breadth_20261027_wave3/controller_lift192/capacity.json)；[research/ddp/breadth_20261027_wave3/controller_lift192/first_calibration.json](../../research/ddp/breadth_20261027_wave3/controller_lift192/first_calibration.json)；[research/ddp/breadth_20261027_wave3/controller_lift192/input.txt](../../research/ddp/breadth_20261027_wave3/controller_lift192/input.txt)；[research/ddp/breadth_20261027_wave3/controller_lift192/search_output.json](../../research/ddp/breadth_20261027_wave3/controller_lift192/search_output.json)；[research/ddp/breadth_20261027_wave3/controller_lift192/terminal.json](../../research/ddp/breadth_20261027_wave3/controller_lift192/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定base/group，八starts×25000单坐标提案；非全部电压空间

**正向保证：** 沿原144结构移植校准；32fiber平移作用使代表缺86×32=2752

**仍未完成：** 所有exactNB5槽仍未闭，未生成46656提升。

**启发与重启依据：** 父profile停止，不扩group/sheet/base。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

