---
type: experiment
node_id: exp:ddp-controller31-triangle-overlap2760-20261027
title: "31三角重叠扩张2760完整指定族"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave4/controller31_triangle_extension/REPORT.md; research/ddp/breadth_20261027_wave4/controller31_triangle_extension/all_candidate_summaries.json; research/ddp/breadth_20261027_wave4/controller31_triangle_extension/best.independent_check.json; research/ddp/breadth_20261027_wave4/controller31_triangle_extension/best_raw_coverage.json; research/ddp/breadth_20261027_wave4/controller31_triangle_extension/first_calibration.json; research/ddp/breadth_20261027_wave4/controller31_triangle_extension/inputs.json; research/ddp/breadth_20261027_wave4/controller31_triangle_extension/passers.json; research/ddp/breadth_20261027_wave4/controller31_triangle_extension/terminal.json"
added: 2026-10-27T08:25:49Z
tags: ["ddp", "degree12", "diameter3", "scoped-failure", "method-ledger"]
---

# 31三角重叠扩张2760完整指定族

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** controller

**目标与阶数：** (12,3)；L=810；controller n=31；条件性n=837（未据此计纪录）

**距目标的证据：** 实际D=4，目标D=3；普通无序坏对=15；saved_controller_only;hypothetical_lift_not_generated；raw passers0；best controllerD4/15，requiredNB3缺34有序对。

**其他指标（保持原计数类型）：**
```json
{
  "candidates": 2760,
  "raw_passers": 0,
  "required_NB3_missing_ordered_pairs": 34
}
```

**既有原文指标：** 345 source vertex pairs times8 specified insertions;2760 distinct labelled simple quartic graphs.2280 have11 triangles,480 have12. Raw NB3 necessary-coverage passers0. Best31/62/4regular:ordinaryD4,bad unordered15;required NB3 ordered misses34, all rows independently checked.



**原始证据：** [research/ddp/breadth_20261027_wave4/controller31_triangle_extension/REPORT.md](../../research/ddp/breadth_20261027_wave4/controller31_triangle_extension/REPORT.md)；[research/ddp/breadth_20261027_wave4/controller31_triangle_extension/all_candidate_summaries.json](../../research/ddp/breadth_20261027_wave4/controller31_triangle_extension/all_candidate_summaries.json)；[research/ddp/breadth_20261027_wave4/controller31_triangle_extension/best.independent_check.json](../../research/ddp/breadth_20261027_wave4/controller31_triangle_extension/best.independent_check.json)；[research/ddp/breadth_20261027_wave4/controller31_triangle_extension/best_raw_coverage.json](../../research/ddp/breadth_20261027_wave4/controller31_triangle_extension/best_raw_coverage.json)；[research/ddp/breadth_20261027_wave4/controller31_triangle_extension/first_calibration.json](../../research/ddp/breadth_20261027_wave4/controller31_triangle_extension/first_calibration.json)；[research/ddp/breadth_20261027_wave4/controller31_triangle_extension/inputs.json](../../research/ddp/breadth_20261027_wave4/controller31_triangle_extension/inputs.json)；[research/ddp/breadth_20261027_wave4/controller31_triangle_extension/passers.json](../../research/ddp/breadth_20261027_wave4/controller31_triangle_extension/passers.json)；[research/ddp/breadth_20261027_wave4/controller31_triangle_extension/terminal.json](../../research/ddp/breadth_20261027_wave4/controller31_triangle_extension/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 345不同triangle/C5点对×8指定插入，2760不同标号quartic图

**正向保证：** 全部候选simplequartic；完整实际三角计数11/12均未漏

**仍未完成：** 没有patternCSP或837图；只排这指定插入族。

**启发与重启依据：** 该族停止，不排一般31控制器。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

