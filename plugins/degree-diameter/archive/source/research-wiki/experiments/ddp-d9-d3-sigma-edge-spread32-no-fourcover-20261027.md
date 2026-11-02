---
type: experiment
node_id: exp:ddp-d9-d3-sigma-edge-spread32-no-fourcover-20261027
title: "固定σ的32条旧coreedge：最大仅2块端口互不交，无四spread"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/sigma_edge_spread/PREDICTION.json; research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/sigma_edge_spread/REPORT.md; research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/sigma_edge_spread/RESULT.json; research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/sigma_edge_spread/SIGMA_EDGES.json; research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/sigma_edge_spread/COMPATIBILITY.json; research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/sigma_edge_spread/check.py; research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/sigma_edge_spread/compatibility.py"
added: 2026-10-27T19:23:22Z
tags: ["ddp", "method-ledger"]
---

# 固定σ的32条旧coreedge：最大仅2块端口互不交，无四spread

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (9,3)；L=585；candidate_graph_or_family n=585；条件性n=586（未据此计纪录）

**距目标的证据：** 四spread存在预测被反驳：exactcover0，17搜索节点完整穷尽。更强同mask结构：144对不交，但没有任意三块两两不交，因此最大兼容块数恰2。条件586 graft没有输入，未生成。

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 585,
  "source_m": 2600,
  "sigma_old_core_edges": 32,
  "port_union_size": 16,
  "intersection_ports": 2,
  "port_pair_universe": 32,
  "port_pair_mask_size": 8,
  "exactcover4_passers": 0,
  "exactcover_nodes": 17,
  "disjoint_mask_pairs": 144,
  "pair_intersection_histogram_in_port_pairs": {
    "0": 144,
    "2": 160,
    "3": 192
  },
  "maximum_pairwise_disjoint_masks": 2,
  "scan_exactcover_CPU": 0.001002951,
  "compatibility_CPU": 0.000267263,
  "newgraphs": 0,
  "BFS": 0,
  "new_aut_search": false
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/sigma_edge_spread/PREDICTION.json](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/sigma_edge_spread/PREDICTION.json)；[research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/sigma_edge_spread/REPORT.md](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/sigma_edge_spread/REPORT.md)；[research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/sigma_edge_spread/RESULT.json](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/sigma_edge_spread/RESULT.json)；[research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/sigma_edge_spread/SIGMA_EDGES.json](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/sigma_edge_spread/SIGMA_EDGES.json)；[research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/sigma_edge_spread/COMPATIBILITY.json](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/sigma_edge_spread/COMPATIBILITY.json)；[research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/sigma_edge_spread/check.py](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/sigma_edge_spread/check.py)；[research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/sigma_edge_spread/compatibility.py](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/sigma_edge_spread/compatibility.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定实际585源及已验sigma(p0 fixed)。原2600edges中32条{v,sigma(v)}coreedges均有S交2/并16非p ports，且并为8sigma-portpairs。只对这32 masks作完整exactcover4，无新图/BFS/aut。

**仍未完成：** No general(9,3) exclusion; other source/generator rules outside this fixed conditional construction remain unresolved.

**启发与重启依据：** 局部sigma-edge确有合适16port覆盖量，但四块不能同时协调；不能把每块容量16与四倍64当整体覆盖。仅关闭此固定sigma的32edge四spread规则，不推全586或全部9D3无望，不改换sigma/块族续搜。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

