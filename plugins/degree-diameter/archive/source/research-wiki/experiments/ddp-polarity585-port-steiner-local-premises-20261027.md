---
type: experiment
node_id: exp:ddp-polarity585-port-steiner-local-premises-20261027
title: "实际585源的65ports构perfect1code，520个R2块为Steiner3-(65,9,1)"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/REPORT.md; research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/PREDICTION.json; research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/SOURCE.json; research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/RESULT.json; research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/BLOCKS.json; research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/PORT_R2.json; research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/check.py"
added: 2026-10-27T19:13:48Z
tags: ["ddp", "method-ledger"]
---

# 实际585源的65ports构perfect1code，520个R2块为Steiner3-(65,9,1)

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (9,3)；L=585；candidate_graph_or_family n=585；条件性n=586（未据此计纪录）

**距目标的证据：** 三项事前局部结构预测全部支持，提供counting引理所需actual premises；设计导出点重数72/对重数9/三元重数1。局部数据是结构证据，非新图/全图坏对结果。

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 585,
  "source_m": 2600,
  "source_reported_D": 3,
  "source_D3_inherited": true,
  "degree_histogram": {
    "8": 65,
    "9": 520
  },
  "ports": 65,
  "nonports": 520,
  "R2_neighborhoods_expanded": 65,
  "closed1_cover_multiplicity_histogram": {
    "1": 585
  },
  "distinct_S_blocks": 520,
  "S_block_size": 9,
  "triples": 43680,
  "triple_multiplicity_histogram": {
    "1": 43680
  },
  "design_replications": {
    "point": 72,
    "pair": 9,
    "triple": 1
  },
  "CPU_seconds": 0.050057111999999994,
  "source_all_root_BFS": 0,
  "helpers_searched": false,
  "new_graphs": 0,
  "independent_method_count_note": "Two records in one port-code extension mechanism; source data and theorem are not two independent construction methods."
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/REPORT.md](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/REPORT.md)；[research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/PREDICTION.json](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/PREDICTION.json)；[research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/SOURCE.json](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/SOURCE.json)；[research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/RESULT.json](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/RESULT.json)；[research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/BLOCKS.json](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/BLOCKS.json)；[research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/PORT_R2.json](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/PORT_R2.json)；[research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/check.py](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/check.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 复用已保存actual585/2600源及65degree8/520degree9既有分区；仅65次R2邻域展开与43680triples计数。65closed1balls对585点覆盖重数均1；R2(p)与ports交仅自身；520个S(t)均9点且各异，全43680triples各一次。未重全源D3/BFS或旧replication/helper试验。

**仍未完成：** Local scan alone does not prove arbitrary graph upperbound; complete old-edge-retaining obstruction is the linked theorem in the same mechanism.

**启发与重启依据：** 用实际port-R2三设计而非图名几何类比支撑全体helper计数；source全D3继承已知事实，承重排除只需已验local separation/code/design，不再跑source allpairs。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

