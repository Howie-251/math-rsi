---
type: experiment
node_id: exp:ddp-d11-d4-one-switch-absorption679-20261027
title: "(11,4)paired-switch补路679项：原反例修好但仍无完整图"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d11_D4_current3645/absorbed_switch_probe/REPORT.md; research/ddp/more_graphs_20261027/d11_D4_current3645/absorbed_switch_probe/RESULT.json"
added: 2026-10-27T18:32:57Z
tags: ["ddp", "method-ledger"]
---

# (11,4)paired-switch补路679项：原反例修好但仍无完整图

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** (11,4)；L=3645；条件性n=3646（未据此计纪录）

**距目标的证据：** 在先前47个newroot通过候选中，只取firstbadpair端点处存在的copy-switch，得35组；Smax必要界剪2个子集，其余679全测。541新根不足、138新根通过但旧旧D4反例，0图/未试/UNKNOWN。代表original127确将3352–2244修成经newx两步路，但66–1863仍>4。

**其他指标（保持原计数类型）：**
```json
{
  "switch_groups": 35,
  "necessary_bound_pruned_subsets": 2,
  "candidates_evaluated": 679,
  "newroot_fail": 541,
  "newroot_pass": 138,
  "oldpair_fail": 138,
  "modified_roots_BFS": 1677,
  "max_old_roots": 41,
  "old_R3_balls_reused": 1964,
  "new_R3_balls": 29,
  "CPU_total": 2.744826601,
  "newgraphs": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d11_D4_current3645/absorbed_switch_probe/REPORT.md](../../research/ddp/more_graphs_20261027/d11_D4_current3645/absorbed_switch_probe/REPORT.md)；[research/ddp/more_graphs_20261027/d11_D4_current3645/absorbed_switch_probe/RESULT.json](../../research/ddp/more_graphs_20261027/d11_D4_current3645/absorbed_switch_probe/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 在先前47个newroot通过候选中，只取firstbadpair端点处存在的copy-switch，得35组；Smax必要界剪2个子集，其余679全测。541新根不足、138新根通过但旧旧D4反例，0图/未试/UNKNOWN。代表original127确将3352–2244修成经newx两步路，但66–1863仍>4。

**仍未完成：** This finite result does not resolve generalgraph construction or completeLean.

**启发与重启依据：** 这说明新增wholepairedswitch能补一类路线却没同时修全部旧路；固定F3+最大free子集规则已闭，不追新badpair再加switch。与旧两edge范围分开。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

