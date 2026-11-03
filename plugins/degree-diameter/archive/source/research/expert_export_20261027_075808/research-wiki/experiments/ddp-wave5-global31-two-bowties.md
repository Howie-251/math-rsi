---
type: experiment
node_id: exp:ddp-wave5-global31-two-bowties
title: "31点两bowtie quartic控制器全局交换"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave5/global31_two_bowties/REPORT.md; research/ddp/breadth_20261027_wave5/global31_two_bowties/best.independent_check.json; research/ddp/breadth_20261027_wave5/global31_two_bowties/best.json; research/ddp/breadth_20261027_wave5/global31_two_bowties/compile.json; research/ddp/breadth_20261027_wave5/global31_two_bowties/first_calibration.json; research/ddp/breadth_20261027_wave5/global31_two_bowties/inputs.json; research/ddp/breadth_20261027_wave5/global31_two_bowties/run.py; research/ddp/breadth_20261027_wave5/global31_two_bowties/search.cpp; research/ddp/breadth_20261027_wave5/global31_two_bowties/terminal.json"
added: 2026-10-27T07:55:17Z
tags: ["ddp", "method-ledger"]
---

# 31点两bowtie quartic控制器全局交换

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** controller

**目标与阶数：** (12,3)；L=810；controller n=31；条件性n=837（未据此计纪录）

**距目标的证据：** 实际D=4，目标D=3；普通无序坏对=7；saved_controller_only;hypothetical_lift_not_generated；raw passers=0；最佳controller普通D4/7坏对，required NB3缺18有序对。

**其他指标（保持原计数类型）：**
```json
{
  "required_NB3_missing_ordered_pairs": 18,
  "raw_passers": 0,
  "legal_proposals": 600000,
  "ordinary_scope": "31controller only"
}
```





**原始证据：** [research/ddp/breadth_20261027_wave5/global31_two_bowties/REPORT.md](../../research/ddp/breadth_20261027_wave5/global31_two_bowties/REPORT.md)；[research/ddp/breadth_20261027_wave5/global31_two_bowties/best.independent_check.json](../../research/ddp/breadth_20261027_wave5/global31_two_bowties/best.independent_check.json)；[research/ddp/breadth_20261027_wave5/global31_two_bowties/best.json](../../research/ddp/breadth_20261027_wave5/global31_two_bowties/best.json)；[research/ddp/breadth_20261027_wave5/global31_two_bowties/compile.json](../../research/ddp/breadth_20261027_wave5/global31_two_bowties/compile.json)；[research/ddp/breadth_20261027_wave5/global31_two_bowties/first_calibration.json](../../research/ddp/breadth_20261027_wave5/global31_two_bowties/first_calibration.json)；[research/ddp/breadth_20261027_wave5/global31_two_bowties/inputs.json](../../research/ddp/breadth_20261027_wave5/global31_two_bowties/inputs.json)；[research/ddp/breadth_20261027_wave5/global31_two_bowties/run.py](../../research/ddp/breadth_20261027_wave5/global31_two_bowties/run.py)；[research/ddp/breadth_20261027_wave5/global31_two_bowties/search.cpp](../../research/ddp/breadth_20261027_wave5/global31_two_bowties/search.cpp)；[research/ddp/breadth_20261027_wave5/global31_two_bowties/terminal.json](../../research/ddp/breadth_20261027_wave5/global31_two_bowties/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 一个架构，3固定fresh starts各200000合法交换；不排全部31图

**正向保证：** 逆一致端口局部规则可由18pattern实现；全图搜索允许外部端口交换

**仍未完成：** raw覆盖未过，因此未调用后续pattern CSP，未生成837图。

**启发与重启依据：** 须有新的raw可行controller架构，不追加同架构起点。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

