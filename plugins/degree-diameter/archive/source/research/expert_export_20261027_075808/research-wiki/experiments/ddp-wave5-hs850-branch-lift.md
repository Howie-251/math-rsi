---
type: experiment
node_id: exp:ddp-wave5-hs850-branch-lift
title: "HS50×C17固定非均匀分支template"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave5/hs850_branch_lift/REPORT.md; research/ddp/breadth_20261027_wave5/hs850_branch_lift/SCREEN.json; research/ddp/breadth_20261027_wave5/hs850_branch_lift/obstruction.json; research/ddp/breadth_20261027_wave5/hs850_branch_lift/screen.py; research/ddp/breadth_20261027_wave5/hs850_branch_lift/terminal.json"
added: 2026-10-27T07:55:17Z
tags: ["ddp", "method-ledger"]
---

# HS50×C17固定非均匀分支template

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** capacity

**目标与阶数：** (12,3)；L=810；条件性n=850（未据此计纪录）

**距目标的证据：** 非邻fiber≤3端点至多12<17，指定整个template不可能D3。

**其他指标（保持原计数类型）：**
```json
{
  "capacity": 12,
  "required_states": 17,
  "parameter_assignments": 0,
  "graphs_generated": 0
}
```





**原始证据：** [research/ddp/breadth_20261027_wave5/hs850_branch_lift/REPORT.md](../../research/ddp/breadth_20261027_wave5/hs850_branch_lift/REPORT.md)；[research/ddp/breadth_20261027_wave5/hs850_branch_lift/SCREEN.json](../../research/ddp/breadth_20261027_wave5/hs850_branch_lift/SCREEN.json)；[research/ddp/breadth_20261027_wave5/hs850_branch_lift/obstruction.json](../../research/ddp/breadth_20261027_wave5/hs850_branch_lift/obstruction.json)；[research/ddp/breadth_20261027_wave5/hs850_branch_lift/screen.py](../../research/ddp/breadth_20261027_wave5/hs850_branch_lift/screen.py)；[research/ddp/breadth_20261027_wave5/hs850_branch_lift/terminal.json](../../research/ddp/breadth_20261027_wave5/hs850_branch_lift/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定branch位置和大小(4,2,2,1,1)，六参数及同位置同大小常数替换

**正向保证：** 任意六参数均定义simple12regular；两平移轨道；self及相邻fiber完整覆盖

**仍未完成：** 不排改变branch位置/大小或其他HS提升。

**启发与重启依据：** 必须改变非邻fiber容量；不能继续六参数赋值。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

