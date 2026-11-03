---
type: experiment
node_id: exp:ddp-wave7-shortcut-matching-scout
title: "650层结构与加matching降径参数准备"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave7/shortcut_matching_scout/REPORT.md; research/ddp/breadth_20261027_wave7/shortcut_matching_scout/RESULT.json; research/ddp/breadth_20261027_wave7/shortcut_matching_scout/old_distance5_pairs.txt; research/ddp/breadth_20261027_wave7/shortcut_matching_scout/source650_distances.u8; research/ddp/breadth_20261027_wave7/shortcut_matching_scout/three_orbit_distance_vectors.json"
added: 2026-10-27T07:55:18Z
tags: ["ddp", "method-ledger"]
---

# 650层结构与加matching降径参数准备

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (6,4)；L=441；条件性n=650（未据此计纪录）；从属目标：[{'Delta': 5, 'D': 3, 'savedL': 72}, {'Delta': 5, 'D': 4, 'savedL': 252}, {'Delta': 6, 'D': 4, 'savedL': 441}, {'Delta': 7, 'D': 4, 'savedL': 684}, {'Delta': 8, 'D': 4, 'savedL': 1100}]

**距目标的证据：** 恢复500/125/25三层及87800旧D5无序对；full500作用不容许invariant perfectmatching。

**其他指标（保持原计数类型）：**
```json
{
  "old_D5_unordered_pairs": 87800,
  "matching_search": false
}
```



**从属变体：**
```json
[
  {
    "target_degree": 5,
    "target_D": 3,
    "source_degree": 4,
    "source_D": 4,
    "source_n": 104,
    "target_saved": 72,
    "target_moore": 106,
    "strictly_bigger": true,
    "not_over_moore": true,
    "parameter_pass": true
  },
  {
    "target_degree": 5,
    "target_D": 4,
    "source_degree": 4,
    "source_D": 5,
    "source_n": 364,
    "target_saved": 252,
    "target_moore": 426,
    "strictly_bigger": true,
    "not_over_moore": true,
    "parameter_pass": true
  },
  {
    "target_degree": 6,
    "target_D": 4,
    "source_degree": 5,
    "source_D": 5,
    "source_n": 650,
    "target_saved": 441,
    "target_moore": 937,
    "strictly_bigger": true,
    "not_over_moore": true,
    "parameter_pass": true
  },
  {
    "target_degree": 7,
    "target_D": 4,
    "source_degree": 6,
    "source_D": 5,
    "source_n": 1518,
    "target_saved": 684,
    "target_moore": 1814,
    "strictly_bigger": true,
    "not_over_moore": true,
    "parameter_pass": true
  },
  {
    "target_degree": 8,
    "target_D": 4,
    "source_degree": 7,
    "source_D": 5,
    "source_n": 2810,
    "target_saved": 1100,
    "target_moore": 3201,
    "strictly_bigger": true,
    "not_over_moore": true,
    "parameter_pass": true
  }
]
```

**原始证据：** [research/ddp/breadth_20261027_wave7/shortcut_matching_scout/REPORT.md](../../research/ddp/breadth_20261027_wave7/shortcut_matching_scout/REPORT.md)；[research/ddp/breadth_20261027_wave7/shortcut_matching_scout/RESULT.json](../../research/ddp/breadth_20261027_wave7/shortcut_matching_scout/RESULT.json)；[research/ddp/breadth_20261027_wave7/shortcut_matching_scout/old_distance5_pairs.txt](../../research/ddp/breadth_20261027_wave7/shortcut_matching_scout/old_distance5_pairs.txt)；[research/ddp/breadth_20261027_wave7/shortcut_matching_scout/source650_distances.u8](../../research/ddp/breadth_20261027_wave7/shortcut_matching_scout/source650_distances.u8)；[research/ddp/breadth_20261027_wave7/shortcut_matching_scout/three_orbit_distance_vectors.json](../../research/ddp/breadth_20261027_wave7/shortcut_matching_scout/three_orbit_distance_vectors.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 27格来源和Moore筛后选固定650源；本目录没有matching搜索

**正向保证：** old-old≤4加边后保持；完整必要判定含1或2条matching边

**仍未完成：** 无明确全对称匹配规则；源远端尚未缩短。

**启发与重启依据：** 已进入独立shortcut650有限profile；不是另一独立方法。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

