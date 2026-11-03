---
type: experiment
node_id: exp:ddp-wave8-insertion171
title: "170→171：删三条matching边并连六端点"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave8/insertion171/REPORT.md; research/ddp/breadth_20261027_wave8/insertion171/fallback.edges; research/ddp/breadth_20261027_wave8/insertion171/fallback.independent_check.json; research/ddp/breadth_20261027_wave8/insertion171/fallback_predictions.json; research/ddp/breadth_20261027_wave8/insertion171/paths.txt; research/ddp/breadth_20261027_wave8/insertion171/run.py; research/ddp/breadth_20261027_wave8/insertion171/search.cpp; research/ddp/breadth_20261027_wave8/insertion171/search_result.json; research/ddp/breadth_20261027_wave8/insertion171/source_b2.txt; research/ddp/breadth_20261027_wave8/insertion171/terminal.json"
added: 2026-10-27T08:25:53Z
tags: ["ddp", "method-ledger"]
---

# 170→171：删三条matching边并连六端点

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (7,3)；L=170；candidate_graph_or_family n=171；条件性n=171（未据此计纪录）

**距目标的证据：** 实际D=4，目标D=3；普通无序坏对=79；saved_explicit_graph；全部新根三球不满，最少仍漏11；指定整族无D3。保存fallbackD4/79不是全族坏对最优。

**其他指标（保持原计数类型）：**
```json
{
  "raw_edge_triples": 34930665,
  "legal_three_edge_matchings": 32846935,
  "newroot_capacity_passers": 0,
  "minimum_newroot_missing": 11,
  "formal_full_candidate_checks": 0,
  "fallback_new_old_bad": 11,
  "fallback_old_old_bad": 68,
  "proven_all_family_D": 4
}
```





**原始证据：** [research/ddp/breadth_20261027_wave8/insertion171/REPORT.md](../../research/ddp/breadth_20261027_wave8/insertion171/REPORT.md)；[research/ddp/breadth_20261027_wave8/insertion171/fallback.edges](../../research/ddp/breadth_20261027_wave8/insertion171/fallback.edges)；[research/ddp/breadth_20261027_wave8/insertion171/fallback.independent_check.json](../../research/ddp/breadth_20261027_wave8/insertion171/fallback.independent_check.json)；[research/ddp/breadth_20261027_wave8/insertion171/fallback_predictions.json](../../research/ddp/breadth_20261027_wave8/insertion171/fallback_predictions.json)；[research/ddp/breadth_20261027_wave8/insertion171/paths.txt](../../research/ddp/breadth_20261027_wave8/insertion171/paths.txt)；[research/ddp/breadth_20261027_wave8/insertion171/run.py](../../research/ddp/breadth_20261027_wave8/insertion171/run.py)；[research/ddp/breadth_20261027_wave8/insertion171/search.cpp](../../research/ddp/breadth_20261027_wave8/insertion171/search.cpp)；[research/ddp/breadth_20261027_wave8/insertion171/search_result.json](../../research/ddp/breadth_20261027_wave8/insertion171/search_result.json)；[research/ddp/breadth_20261027_wave8/insertion171/source_b2.txt](../../research/ddp/breadth_20261027_wave8/insertion171/source_b2.txt)；[research/ddp/breadth_20261027_wave8/insertion171/terminal.json](../../research/ddp/breadth_20261027_wave8/insertion171/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定170源所有三条两两不接旧边，共32846935合法matching

**正向保证：** 所有旧≤2点对保持≤3；S旧二步支配等价新根三步全覆盖；所有候选理论D≤4

**仍未完成：** 不排其他171图或不同插入结构；formal unique/full候选筛实际调用0。

**启发与重启依据：** 须改变插入结构，不能继续同三边族；fallback79不能当全族最小坏对。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

