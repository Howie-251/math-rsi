---
type: experiment
node_id: exp:ddp-wave7-signed-double340
title: "170源的signed double加vertical matching"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave7/signed_double340/REPORT.md; research/ddp/breadth_20261027_wave7/signed_double340/RESULT.json; research/ddp/breadth_20261027_wave7/signed_double340/distance3_paths.json; research/ddp/breadth_20261027_wave7/signed_double340/mechanism_parameter_screen.json; research/ddp/breadth_20261027_wave7/signed_double340/obstruction.independent_check.json; research/ddp/breadth_20261027_wave7/signed_double340/obstruction.json; research/ddp/breadth_20261027_wave7/signed_double340/screen.py; research/ddp/breadth_20261027_wave7/signed_double340/source.edges; research/ddp/breadth_20261027_wave7/signed_double340/source.raw.edges; research/ddp/breadth_20261027_wave7/signed_double340/source_check.json; research/ddp/breadth_20261027_wave7/signed_double340/source_distances.json; research/ddp/breadth_20261027_wave7/signed_double340/source_download.json; research/ddp/breadth_20261027_wave7/signed_double340/terminal.json"
added: 2026-10-27T08:25:53Z
tags: ["ddp", "method-ledger"]
---

# 170源的signed double加vertical matching

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** capacity

**目标与阶数：** (8,3)；L=253；条件性n=340（未据此计纪录）

**距目标的证据：** 源0→50唯一三路，只给一个sheet；全部signings理论上恰D4。未生成340图。

**其他指标（保持原计数类型）：**
```json
{
  "proven_all_family_D": 4,
  "ordinary_bad_unordered_lower_bound": 10260,
  "unique3_unordered_source_pairs": 5130,
  "graphs_generated": 0
}
```





**原始证据：** [research/ddp/breadth_20261027_wave7/signed_double340/REPORT.md](../../research/ddp/breadth_20261027_wave7/signed_double340/REPORT.md)；[research/ddp/breadth_20261027_wave7/signed_double340/RESULT.json](../../research/ddp/breadth_20261027_wave7/signed_double340/RESULT.json)；[research/ddp/breadth_20261027_wave7/signed_double340/distance3_paths.json](../../research/ddp/breadth_20261027_wave7/signed_double340/distance3_paths.json)；[research/ddp/breadth_20261027_wave7/signed_double340/mechanism_parameter_screen.json](../../research/ddp/breadth_20261027_wave7/signed_double340/mechanism_parameter_screen.json)；[research/ddp/breadth_20261027_wave7/signed_double340/obstruction.independent_check.json](../../research/ddp/breadth_20261027_wave7/signed_double340/obstruction.independent_check.json)；[research/ddp/breadth_20261027_wave7/signed_double340/obstruction.json](../../research/ddp/breadth_20261027_wave7/signed_double340/obstruction.json)；[research/ddp/breadth_20261027_wave7/signed_double340/screen.py](../../research/ddp/breadth_20261027_wave7/signed_double340/screen.py)；[research/ddp/breadth_20261027_wave7/signed_double340/source.edges](../../research/ddp/breadth_20261027_wave7/signed_double340/source.edges)；[research/ddp/breadth_20261027_wave7/signed_double340/source.raw.edges](../../research/ddp/breadth_20261027_wave7/signed_double340/source.raw.edges)；[research/ddp/breadth_20261027_wave7/signed_double340/source_check.json](../../research/ddp/breadth_20261027_wave7/signed_double340/source_check.json)；[research/ddp/breadth_20261027_wave7/signed_double340/source_distances.json](../../research/ddp/breadth_20261027_wave7/signed_double340/source_distances.json)；[research/ddp/breadth_20261027_wave7/signed_double340/source_download.json](../../research/ddp/breadth_20261027_wave7/signed_double340/source_download.json)；[research/ddp/breadth_20261027_wave7/signed_double340/terminal.json](../../research/ddp/breadth_20261027_wave7/signed_double340/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定170源全部edge signings，全部加fiber内matching

**正向保证：** 原≤2距离对可由一次vertical补另一sheet；原D3保证所有lift点对≤4

**仍未完成：** 只排固定base签名族，不排一般340图。

**启发与重启依据：** 必须使唯一三路能分支，换sign不够。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

