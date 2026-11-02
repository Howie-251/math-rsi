---
type: experiment
node_id: exp:ddp-wave2-triangle-bowtie32-controller
title: "32点三角端口控制系统固定有限合成"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/REPORT.md; research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/best.capacity.json; research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/best.edges; research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/best.independent_capacity_check.json; research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/best.independent_check.json; research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/best.json; research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/first.cached.txt; research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/first.capacity.txt; research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/first.edges; research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/first.score.json; research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/first_calibration.json; research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/inputs.json; research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/inputs.txt; research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/preparation_attempts.json; research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/process.json; research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/production_terminal.json; research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/run.json; research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/starts.jsonl; research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/terminal.json"
added: 2026-10-27T08:25:51Z
tags: ["ddp", "method-ledger"]
---

# 32点三角端口控制系统固定有限合成

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** controller

**目标与阶数：** (12,3)；L=810；controller n=32；条件性n=864（未据此计纪录）

**距目标的证据：** 实际D=4，目标D=3；普通无序坏对=4；saved_controller_only;hypothetical_lift_not_generated；best controllerD4/4普通坏对；容量U缺量324、14个有序不足槽。

**其他指标（保持原计数类型）：**
```json
{
  "capacity_deficit_ordered": 324,
  "capacity_insufficient_ordered_slots": 14,
  "proposals": 800000,
  "large_lift_generated": false
}
```





**原始证据：** [research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/REPORT.md](../../research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/REPORT.md)；[research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/best.capacity.json](../../research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/best.capacity.json)；[research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/best.edges](../../research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/best.edges)；[research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/best.independent_capacity_check.json](../../research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/best.independent_capacity_check.json)；[research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/best.independent_check.json](../../research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/best.independent_check.json)；[research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/best.json](../../research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/best.json)；[research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/first.cached.txt](../../research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/first.cached.txt)；[research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/first.capacity.txt](../../research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/first.capacity.txt)；[research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/first.edges](../../research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/first.edges)；[research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/first.score.json](../../research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/first.score.json)；[research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/first_calibration.json](../../research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/first_calibration.json)；[research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/inputs.json](../../research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/inputs.json)；[research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/inputs.txt](../../research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/inputs.txt)；[research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/preparation_attempts.json](../../research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/preparation_attempts.json)；[research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/process.json](../../research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/process.json)；[research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/production_terminal.json](../../research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/production_terminal.json)；[research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/run.json](../../research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/run.json)；[research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/starts.jsonl](../../research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/starts.jsonl)；[research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/terminal.json](../../research/ddp/breadth_20261027_wave2/triangle_bowtie32_controller/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定三角骨架+external2factor，8starts各100000提案；32是33的共享三角结构跟进

**正向保证：** simplequartic及固定三角边/externaldegree保持；优化U=I+3A+9A²+27A³完整必要上界

**仍未完成：** U≥27也非实际fiber覆盖；本次未达必要条件，未生成提升图。

**启发与重启依据：** 三角端口骨架已收束，不追加31/34/seed；不排整个控制器族。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

