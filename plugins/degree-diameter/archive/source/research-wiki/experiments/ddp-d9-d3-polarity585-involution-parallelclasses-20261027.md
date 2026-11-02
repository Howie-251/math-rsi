---
type: experiment
node_id: exp:ddp-d9-d3-polarity585-involution-parallelclasses-20261027
title: "585实际对合与九平行类：固定1端口、32对交换，全2600边保持"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/involution_probe/PREDICTION.json; research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/involution_probe/REPORT.md; research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/involution_probe/RESULT.json; research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/involution_probe/sigma.json; research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/involution_probe/PARALLEL_CLASS_IDENTIFICATION.json; research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/FALSE_TWIN_CONSTRAINT.md"
added: 2026-10-27T19:15:33Z
tags: ["ddp", "method-ledger"]
---

# 585实际对合与九平行类：固定1端口、32对交换，全2600边保持

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (9,3)；L=585；known_source_or_recovery n=585

**距目标的证据：** 对合预测支持。另一次只读检查证九parallelclasses恰N(0)及N(a)\{0},a∈N(0)；另八类U+p=N_source(a)。这是可复用source接口/机制支持，非新图或新独立构造方法。

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 585,
  "source_m": 2600,
  "port_count": 65,
  "port_fixed": 0,
  "port_transpositions": 32,
  "fixed_graph_vertices": [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8
  ],
  "edges_checked": 2600,
  "edge_failures": 0,
  "aut_candidates_tested": 1,
  "sigma_CPU": 0.002791158,
  "parallelclasses": 9,
  "derived_lines": 72,
  "parallel_class_check_CPU": 0.00016111,
  "source_BFS": 0,
  "newgraphs": 0,
  "independent_mechanism_count_increment": 0,
  "graft_candidates_run": 0,
  "false_twin_constraint_bound_inherited": 578
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/involution_probe/PREDICTION.json](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/involution_probe/PREDICTION.json)；[research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/involution_probe/REPORT.md](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/involution_probe/REPORT.md)；[research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/involution_probe/RESULT.json](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/involution_probe/RESULT.json)；[research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/involution_probe/sigma.json](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/involution_probe/sigma.json)；[research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/involution_probe/PARALLEL_CLASS_IDENTIFICATION.json](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/involution_probe/PARALLEL_CLASS_IDENTIFICATION.json)；[research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/FALSE_TWIN_CONSTRAINT.md](../../research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/FALSE_TWIN_CONSTRAINT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 从已验Steiner3-(65,9,1)的实际blocks在port0派生8阶affineplane；按N(0)的特殊parallelclass构造唯一parallelogram平移73→86，经block唯一性提升为585置换。实际全图bijection、order2、固定port0及core1..8，其余64ports为32transpositions，2600条边全部保持。无GF8原标签假设、无aut群枚举或BFS。

**仍未完成：** The permutation is verified for the fixed source. It is not a new graph, an independent construction family, a full automorphism-group determination, or a resolution of arbitrary(9,3) graphs.

**启发与重启依据：** 群坐标不可用时，已绑定的blockdesign可给一个确定的几何置换并直接全edge验真。parallelclass+port的pins会复现旧邻域；若graft保该a邻域则出现fullfalse-twins，root已给degree9/D3上界578，作为原graft反驳补证据。原56graft未运行，本轮停止aut方向/再graft，不将此支持row重复成producer反驳node。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

