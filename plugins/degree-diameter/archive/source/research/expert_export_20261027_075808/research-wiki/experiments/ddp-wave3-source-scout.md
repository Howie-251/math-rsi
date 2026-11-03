---
type: experiment
node_id: exp:ddp-wave3-source-scout
title: "通用F3⁵五步chart与180/186控制器固定群筛"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave3/source_scout/THEOREM_SCOPE_REVIEW.md; research/ddp/breadth_20261027_wave3/source_scout/route_chart_controller180/REPORT.md; research/ddp/breadth_20261027_wave3/source_scout/SCOUT.json; research/ddp/breadth_20261027_wave3/source_scout/chart_check.json; research/ddp/breadth_20261027_wave3/source_scout/route_chart_F3_5.json; research/ddp/breadth_20261027_wave3/source_scout/route_chart_controller180/RESULT.json; research/ddp/breadth_20261027_wave3/source_scout/route_chart_controller180/group.json; research/ddp/breadth_20261027_wave3/source_scout/route_chart_controller180/mixed_involutions/RESULT.json; research/ddp/breadth_20261027_wave3/source_scout/route_chart_controller186/RESULT.json"
added: 2026-10-27T07:55:16Z
tags: ["ddp", "method-ledger"]
---

# 通用F3⁵五步chart与180/186控制器固定群筛

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (12,5)；L=42342；条件性n=42525（未据此计纪录）

**距目标的证据：** 324/324词rank5且逆一致；尚无≥175点quartic exact-NB5控制器。

**其他指标（保持原计数类型）：**
```json
{
  "rank5_words": 324,
  "minimum_controller_order": 175
}
```



**从属变体：**
```json
[
  {
    "id": "A5xC3-180",
    "hypothetical_lift_n": 43740,
    "scope": "全部13296个四元inverse-closed S",
    "actual_sets_checked": 11931,
    "two_noninvolution_inverse_pair_sets": 3321,
    "mixed_onepair_twoinvolutions": 8610,
    "four_involution_sets_disconnected": 1365,
    "best_exactNB5_endpoints_two_pair": 163,
    "best_exactNB5_endpoints_mixed": 162,
    "all_scope_excluded": true,
    "actual_D": null
  },
  {
    "id": "F31:C6-186",
    "hypothetical_lift_n": 45198,
    "scope": "仅2926个二非对合逆对组成",
    "actual_sets_checked": 2926,
    "all_scope_excluded": true,
    "other_compositions_open": true,
    "actual_D": null
  }
]
```

**原始证据：** [research/ddp/breadth_20261027_wave3/source_scout/THEOREM_SCOPE_REVIEW.md](../../research/ddp/breadth_20261027_wave3/source_scout/THEOREM_SCOPE_REVIEW.md)；[research/ddp/breadth_20261027_wave3/source_scout/route_chart_controller180/REPORT.md](../../research/ddp/breadth_20261027_wave3/source_scout/route_chart_controller180/REPORT.md)；[research/ddp/breadth_20261027_wave3/source_scout/SCOUT.json](../../research/ddp/breadth_20261027_wave3/source_scout/SCOUT.json)；[research/ddp/breadth_20261027_wave3/source_scout/chart_check.json](../../research/ddp/breadth_20261027_wave3/source_scout/chart_check.json)；[research/ddp/breadth_20261027_wave3/source_scout/route_chart_F3_5.json](../../research/ddp/breadth_20261027_wave3/source_scout/route_chart_F3_5.json)；[research/ddp/breadth_20261027_wave3/source_scout/route_chart_controller180/RESULT.json](../../research/ddp/breadth_20261027_wave3/source_scout/route_chart_controller180/RESULT.json)；[research/ddp/breadth_20261027_wave3/source_scout/route_chart_controller180/group.json](../../research/ddp/breadth_20261027_wave3/source_scout/route_chart_controller180/group.json)；[research/ddp/breadth_20261027_wave3/source_scout/route_chart_controller180/mixed_involutions/RESULT.json](../../research/ddp/breadth_20261027_wave3/source_scout/route_chart_controller180/mixed_involutions/RESULT.json)；[research/ddp/breadth_20261027_wave3/source_scout/route_chart_controller186/RESULT.json](../../research/ddp/breadth_20261027_wave3/source_scout/route_chart_controller186/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 原文通用chart；Cayley控制器子试验为从属有限群范围，不是独立新大类

**正向保证：** 任意合格逆标号controller C给243|C|点、degree12、D≤5

**仍未完成：** ordinaryD≤5不足以代替exactNB5；chart正向结果不等于新图。

**启发与重启依据：** 仅有明确新控制器结构/路由覆盖才继续，不排队换群。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

