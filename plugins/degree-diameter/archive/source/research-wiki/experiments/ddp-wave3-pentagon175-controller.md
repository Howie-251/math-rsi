---
type: experiment
node_id: exp:ddp-wave3-pentagon175-controller
title: "35个C5固定骨架的175控制器"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave3/pentagon175_controller/REPORT.md; research/ddp/breadth_20261027_wave3/pentagon175_controller/best.edges; research/ddp/breadth_20261027_wave3/pentagon175_controller/best.independent_check.json; research/ddp/breadth_20261027_wave3/pentagon175_controller/best.json; research/ddp/breadth_20261027_wave3/pentagon175_controller/best.labels.json; research/ddp/breadth_20261027_wave3/pentagon175_controller/first_calibration.json; research/ddp/breadth_20261027_wave3/pentagon175_controller/first_expected.txt; research/ddp/breadth_20261027_wave3/pentagon175_controller/inputs.json; research/ddp/breadth_20261027_wave3/pentagon175_controller/production_terminal.json; research/ddp/breadth_20261027_wave3/pentagon175_controller/run.json; research/ddp/breadth_20261027_wave3/pentagon175_controller/starts.txt; research/ddp/breadth_20261027_wave3/pentagon175_controller/terminal.json"
added: 2026-10-27T08:25:51Z
tags: ["ddp", "method-ledger"]
---

# 35个C5固定骨架的175控制器

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** controller

**目标与阶数：** (12,5)；L=42342；controller n=175；条件性n=42525（未据此计纪录）

**距目标的证据：** 实际D=6，目标D=5；普通无序坏对=315；saved_controller_only;hypothetical_lift_not_generated；best controller ordinaryD6/315；exactNB5缺2696有序对。

**其他指标（保持原计数类型）：**
```json
{
  "exact_NB5_missing_ordered_pairs": 2696,
  "proposals": 40000
}
```





**原始证据：** [research/ddp/breadth_20261027_wave3/pentagon175_controller/REPORT.md](../../research/ddp/breadth_20261027_wave3/pentagon175_controller/REPORT.md)；[research/ddp/breadth_20261027_wave3/pentagon175_controller/best.edges](../../research/ddp/breadth_20261027_wave3/pentagon175_controller/best.edges)；[research/ddp/breadth_20261027_wave3/pentagon175_controller/best.independent_check.json](../../research/ddp/breadth_20261027_wave3/pentagon175_controller/best.independent_check.json)；[research/ddp/breadth_20261027_wave3/pentagon175_controller/best.json](../../research/ddp/breadth_20261027_wave3/pentagon175_controller/best.json)；[research/ddp/breadth_20261027_wave3/pentagon175_controller/best.labels.json](../../research/ddp/breadth_20261027_wave3/pentagon175_controller/best.labels.json)；[research/ddp/breadth_20261027_wave3/pentagon175_controller/first_calibration.json](../../research/ddp/breadth_20261027_wave3/pentagon175_controller/first_calibration.json)；[research/ddp/breadth_20261027_wave3/pentagon175_controller/first_expected.txt](../../research/ddp/breadth_20261027_wave3/pentagon175_controller/first_expected.txt)；[research/ddp/breadth_20261027_wave3/pentagon175_controller/inputs.json](../../research/ddp/breadth_20261027_wave3/pentagon175_controller/inputs.json)；[research/ddp/breadth_20261027_wave3/pentagon175_controller/production_terminal.json](../../research/ddp/breadth_20261027_wave3/pentagon175_controller/production_terminal.json)；[research/ddp/breadth_20261027_wave3/pentagon175_controller/run.json](../../research/ddp/breadth_20261027_wave3/pentagon175_controller/run.json)；[research/ddp/breadth_20261027_wave3/pentagon175_controller/starts.txt](../../research/ddp/breadth_20261027_wave3/pentagon175_controller/starts.txt)；[research/ddp/breadth_20261027_wave3/pentagon175_controller/terminal.json](../../research/ddp/breadth_20261027_wave3/pentagon175_controller/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 四starts各10000外2factor交换提案；不排整个C5骨架

**正向保证：** 每点C5保证self有NB5闭路；simplequartic逆标号一致

**仍未完成：** 其他ordered pair的exactNB5未闭，未生成42525图。

**启发与重启依据：** profile停止，不追加starts/group。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

