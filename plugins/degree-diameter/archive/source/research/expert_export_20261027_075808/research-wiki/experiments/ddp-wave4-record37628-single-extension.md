---
type: experiment
node_id: exp:ddp-wave4-record37628-single-extension
title: "37628→37629纪录图单点全R4覆盖有限试验"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave4/record37628_single_extension/REPORT.md; research/ddp/breadth_20261027_wave4/record37628_single_extension/independent_cover_check.json; research/ddp/breadth_20261027_wave4/record37628_single_extension/result.json; research/ddp/breadth_20261027_wave4/record37628_single_extension/run.stderr.txt; research/ddp/breadth_20261027_wave4/record37628_single_extension/source_profile.json; research/ddp/breadth_20261027_wave4/record37628_single_extension/terminal.json"
added: 2026-10-27T07:55:17Z
tags: ["ddp", "method-ledger"]
---

# 37628→37629纪录图单点全R4覆盖有限试验

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-cover-profile

**目标与阶数：** (11,5)；L=37628；条件性n=37629（未据此计纪录）

**距目标的证据：** best仍漏115个new-old目标，独立multi-source覆盖检查MATCH；未展开新图。

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 37628,
  "source_known_D_upper_bound": 5,
  "coverage_uncovered_vertices": 115,
  "profiles": 8,
  "neighbor_cap": 11,
  "eight_means": "initial profiles, not pins cap",
  "all_coordinates_mutable": true,
  "expanded_graph_generated": false
}
```





**原始证据：** [research/ddp/breadth_20261027_wave4/record37628_single_extension/REPORT.md](../../research/ddp/breadth_20261027_wave4/record37628_single_extension/REPORT.md)；[research/ddp/breadth_20261027_wave4/record37628_single_extension/independent_cover_check.json](../../research/ddp/breadth_20261027_wave4/record37628_single_extension/independent_cover_check.json)；[research/ddp/breadth_20261027_wave4/record37628_single_extension/result.json](../../research/ddp/breadth_20261027_wave4/record37628_single_extension/result.json)；[research/ddp/breadth_20261027_wave4/record37628_single_extension/run.stderr.txt](../../research/ddp/breadth_20261027_wave4/record37628_single_extension/run.stderr.txt)；[research/ddp/breadth_20261027_wave4/record37628_single_extension/source_profile.json](../../research/ddp/breadth_20261027_wave4/record37628_single_extension/source_profile.json)；[research/ddp/breadth_20261027_wave4/record37628_single_extension/terminal.json](../../research/ddp/breadth_20261027_wave4/record37628_single_extension/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 全部2504可接旧点R4球；8个起始profile，每个greedy补至11邻居并扫一轮全部坐标

**正向保证：** old-old距离不增；单点D5完整条件恰为所选R4球覆盖全部旧点；度预算通过

**仍未完成：** 覆盖miss不是已展开图的全源无序坏对；有限profile不排其他邻居集。

**启发与重启依据：** 不增加seed/坐标轮数；8是起始profile数，绝非8邻居上限，firstpin也可替换。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

