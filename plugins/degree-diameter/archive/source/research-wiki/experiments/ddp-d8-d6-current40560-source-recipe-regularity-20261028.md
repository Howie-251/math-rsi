---
type: experiment
node_id: exp:ddp-d8-d6-current40560-source-recipe-regularity-20261028
title: "(8,6)40560官方配方全8正则：保边增点无spare接口"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d8_D6_current40560_source/SOURCE_NOTES.md; research/ddp/more_graphs_20261027/d8_D6_current40560_source/PROVENANCE.json"
added: 2026-10-28T00:14:45Z
tags: ["ddp", "method-ledger"]
---

# (8,6)40560官方配方全8正则：保边增点无spare接口

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (8,6)；L=40560；条件性n=40561（未据此计纪录）

**距目标的证据：** Currentpublic40560 sourceD6 inherited; authorrecipe-only regularity deduction, no literalprofile or BFS.；旧39216个8regular点经1344flag细分degree不变；每新点2old+3K4+3external=8，故作者定义source全8regular、recipe边数162240/free0。固定保边star/wholeN/proxy入口无旧port，直接停止。

**其他指标（保持原计数类型）：**
```json
{
  "source_order_author_recipe": 40560,
  "source_edges_derived_recipe": 162240,
  "source_regular_degree_derived_recipe": 8,
  "free_vertices_recipe_implied": 0,
  "literal_profile": false,
  "literal_downloaded": false,
  "source_BFS": 0,
  "new_experiments": 0,
  "candidate_graphs": 0,
  "solver": 0,
  "baseline_date": "2026-10-28",
  "source_credit": "DharunishYugeswardeenoo,7October2026; current literal republished inNishantBhakar Zenodo23691325 catalog"
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d8_D6_current40560_source/SOURCE_NOTES.md](../../research/ddp/more_graphs_20261027/d8_D6_current40560_source/SOURCE_NOTES.md)；[research/ddp/more_graphs_20261027/d8_D6_current40560_source/PROVENANCE.json](../../research/ddp/more_graphs_20261027/d8_D6_current40560_source/PROVENANCE.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 仅当前官方H7+40560配方及cap8保全部旧边append适用性；未下载literal或运行actualprofile。

**仍未完成：** General larger(8,6)graphs and differentconnectionchanges not excluded; currentliteral numbering was not bound.

**启发与重启依据：** 正则性可从精确配方直接证明时，不重复下载/profile。此为既有技巧的source适用性记录，不新增方法；不同连接机制或真正有spare的新source另论，本轮不转删边。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

