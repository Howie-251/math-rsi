---
type: experiment
node_id: exp:ddp-wave5-affine-flag80-trade
title: "AG(2,4) rainbow trade80旗标控制器"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave5/affine_flag80_trade/REPORT.md; research/ddp/breadth_20261027_wave5/affine_flag80_trade/best.edges; research/ddp/breadth_20261027_wave5/affine_flag80_trade/best.independent_check.json; research/ddp/breadth_20261027_wave5/affine_flag80_trade/best.json; research/ddp/breadth_20261027_wave5/affine_flag80_trade/best.labels.json; research/ddp/breadth_20261027_wave5/affine_flag80_trade/controller_0.json; research/ddp/breadth_20261027_wave5/affine_flag80_trade/controller_1.json; research/ddp/breadth_20261027_wave5/affine_flag80_trade/controller_2.json; research/ddp/breadth_20261027_wave5/affine_flag80_trade/controller_3.json; research/ddp/breadth_20261027_wave5/affine_flag80_trade/controller_4.json; research/ddp/breadth_20261027_wave5/affine_flag80_trade/controller_5.json; research/ddp/breadth_20261027_wave5/affine_flag80_trade/controller_6.json; research/ddp/breadth_20261027_wave5/affine_flag80_trade/controller_7.json; research/ddp/breadth_20261027_wave5/affine_flag80_trade/exact_cover.json; research/ddp/breadth_20261027_wave5/affine_flag80_trade/run.py; research/ddp/breadth_20261027_wave5/affine_flag80_trade/terminal.json"
added: 2026-10-27T07:55:17Z
tags: ["ddp", "method-ledger"]
---

# AG(2,4) rainbow trade80旗标控制器

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** controller

**目标与阶数：** (12,4)；L=5832；controller n=80；条件性n=6480（未据此计纪录）

**距目标的证据：** 实际D=5，目标D=4；普通无序坏对=208；saved_controller_only;hypothetical_lift_not_generated；8图宽证书全部失败；最佳图普通D5/208坏对，其他7图未普通BFS。

**其他指标（保持原计数类型）：**
```json
{
  "controllers_generated": 8,
  "best_wide_missing_ordered_pairs": 784,
  "other7_actual_D": null,
  "large_lift_generated": false
}
```





**原始证据：** [research/ddp/breadth_20261027_wave5/affine_flag80_trade/REPORT.md](../../research/ddp/breadth_20261027_wave5/affine_flag80_trade/REPORT.md)；[research/ddp/breadth_20261027_wave5/affine_flag80_trade/best.edges](../../research/ddp/breadth_20261027_wave5/affine_flag80_trade/best.edges)；[research/ddp/breadth_20261027_wave5/affine_flag80_trade/best.independent_check.json](../../research/ddp/breadth_20261027_wave5/affine_flag80_trade/best.independent_check.json)；[research/ddp/breadth_20261027_wave5/affine_flag80_trade/best.json](../../research/ddp/breadth_20261027_wave5/affine_flag80_trade/best.json)；[research/ddp/breadth_20261027_wave5/affine_flag80_trade/best.labels.json](../../research/ddp/breadth_20261027_wave5/affine_flag80_trade/best.labels.json)；[research/ddp/breadth_20261027_wave5/affine_flag80_trade/controller_0.json](../../research/ddp/breadth_20261027_wave5/affine_flag80_trade/controller_0.json)；[research/ddp/breadth_20261027_wave5/affine_flag80_trade/controller_1.json](../../research/ddp/breadth_20261027_wave5/affine_flag80_trade/controller_1.json)；[research/ddp/breadth_20261027_wave5/affine_flag80_trade/controller_2.json](../../research/ddp/breadth_20261027_wave5/affine_flag80_trade/controller_2.json)；[research/ddp/breadth_20261027_wave5/affine_flag80_trade/controller_3.json](../../research/ddp/breadth_20261027_wave5/affine_flag80_trade/controller_3.json)；[research/ddp/breadth_20261027_wave5/affine_flag80_trade/controller_4.json](../../research/ddp/breadth_20261027_wave5/affine_flag80_trade/controller_4.json)；[research/ddp/breadth_20261027_wave5/affine_flag80_trade/controller_5.json](../../research/ddp/breadth_20261027_wave5/affine_flag80_trade/controller_5.json)；[research/ddp/breadth_20261027_wave5/affine_flag80_trade/controller_6.json](../../research/ddp/breadth_20261027_wave5/affine_flag80_trade/controller_6.json)；[research/ddp/breadth_20261027_wave5/affine_flag80_trade/controller_7.json](../../research/ddp/breadth_20261027_wave5/affine_flag80_trade/controller_7.json)；[research/ddp/breadth_20261027_wave5/affine_flag80_trade/exact_cover.json](../../research/ddp/breadth_20261027_wave5/affine_flag80_trade/exact_cover.json)；[research/ddp/breadth_20261027_wave5/affine_flag80_trade/run.py](../../research/ddp/breadth_20261027_wave5/affine_flag80_trade/run.py)；[research/ddp/breadth_20261027_wave5/affine_flag80_trade/terminal.json](../../research/ddp/breadth_20261027_wave5/affine_flag80_trade/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定parallelclass、lex前8个rainbow exact-cover、固定B次序与方向

**正向保证：** self、相邻、NB2端点全部由宽证书覆盖；全部A/B边具有rank-good四步替代

**仍未完成：** 其他远端controller pairs未覆盖；未排全部rainbow trade。

**启发与重启依据：** 需要新的全局几何覆盖步骤，不能靠追加exact-cover解/方向/次序。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

