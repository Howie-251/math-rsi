---
type: experiment
node_id: exp:ddp-wave5-heisenberg729-capacity
title: "UT3(F9)五逆对Cayley完整机制容量"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave5/heisenberg729_capacity/REPORT.md; research/ddp/breadth_20261027_wave5/heisenberg729_capacity/RESULT.json; research/ddp/breadth_20261027_wave5/heisenberg729_capacity/check_capacity.py; research/ddp/breadth_20261027_wave5/heisenberg729_capacity/terminal.json"
added: 2026-10-27T08:25:52Z
tags: ["ddp", "method-ledger"]
---

# UT3(F9)五逆对Cayley完整机制容量

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** capacity

**目标与阶数：** (10,3)；L=650；条件性n=729（未据此计纪录）

**距目标的证据：** 投影秩不足4则断连；满秩五类关系的central fiber容量为6/6/6/1/1，均<9。

**其他指标（保持原计数类型）：**
```json
{
  "relation_lines": 121,
  "all_short_words": 1111,
  "maximum_obstructing_fiber_capacity": 6,
  "required_states": 9,
  "parameter_assignments": 0,
  "graphs_generated": 0
}
```





**原始证据：** [research/ddp/breadth_20261027_wave5/heisenberg729_capacity/REPORT.md](../../research/ddp/breadth_20261027_wave5/heisenberg729_capacity/REPORT.md)；[research/ddp/breadth_20261027_wave5/heisenberg729_capacity/RESULT.json](../../research/ddp/breadth_20261027_wave5/heisenberg729_capacity/RESULT.json)；[research/ddp/breadth_20261027_wave5/heisenberg729_capacity/check_capacity.py](../../research/ddp/breadth_20261027_wave5/heisenberg729_capacity/check_capacity.py)；[research/ddp/breadth_20261027_wave5/heisenberg729_capacity/terminal.json](../../research/ddp/breadth_20261027_wave5/heisenberg729_capacity/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** UT3(F9)任意五个inverse generator pairs；全部projection关系weight

**正向保证：** 121条关系线及1111短词微小检查吻合；形式容量允许独立B_ij，故为真实参数的上界

**仍未完成：** 不排不同生成元配额、其他群或一般729点图。

**启发与重启依据：** 需改变central-fiber路径容量；不搜索域参数或seed。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

