---
type: experiment
node_id: exp:ddp-current-d6d7-20400-source-recipe-gap-20261027
title: "(6,7)20400当前Cayley源：报告F5²半直积群，缺三逆对实际生成元"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d6_D7_current20400_source/REPORT.md; research/ddp/more_graphs_20261027/d6_D7_current20400_source/PREDICTION.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/RESULT.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/20400_d6D7_SageMath.author.txt; research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/six_generators/REPORT.md; research/ddp/more_graphs_20261027/d6_D7_current20400_source/normal425_cover/REPORT.md"
added: 2026-10-27T19:58:36Z
tags: ["ddp", "method-ledger"]
---

# (6,7)20400当前Cayley源：报告F5²半直积群，缺三逆对实际生成元

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (6,7)；L=20400；known_source_or_recovery n=20400

**距目标的证据：** Primary报告n20400,m61200,6reg,D7,Autorder20400/CayleyTrue，结构(C5xC5):(C3:(C17:C16))、center1；这反驳PSL2(16)xC5猜测。代码由实际Adeg6D7打印此报告但label误写deg16D4。没有三组inversepair或normalform/action矩阵，代数recipe尚未绑定。

**其他指标（保持原计数类型）：**
```json
{
  "reported_order": 20400,
  "reported_edges": 61200,
  "reported_degree": 6,
  "reported_D": 7,
  "reported_Aut_order": 20400,
  "reported_center_order": 1,
  "source_graph_decoded": false,
  "Sage_bytes": 170269,
  "actual_source_BFS": 0,
  "candidate_graphs": 0,
  "parameter_search": 0,
  "complete_Cayley_recipe": false,
  "initial_factorization_guess": "REFUTED_BY_PRIMARY_REPORTED_CENTER",
  "current_recipe_gap_resolved": true
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d6_D7_current20400_source/REPORT.md](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/REPORT.md)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/PREDICTION.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/PREDICTION.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/RESULT.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/RESULT.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/20400_d6D7_SageMath.author.txt](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/20400_d6D7_SageMath.author.txt)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/six_generators/REPORT.md](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/six_generators/REPORT.md)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/normal425_cover/REPORT.md](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/normal425_cover/REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 只唯一Wiki与官方currentD7描述/小Sage代码阅读；当前Rithwik20400不同于formerComellas20319。Sage170269bytes内嵌sparse6 graph但未解码/执行/解析，无单独20k edgefile下载、BFS或候选。

**仍未完成：** The historical missing-generator gap is resolved by later rootedWL/six_generators/normal425_cover actual recovery. New larger graphs and fullLean remain open.

**启发与重启依据：** 阶数因子不足以识别Cayley群；先取得实际3inversepairs或regularAut身份邻居绑定，才讨论修改参数保relation/degree/connected。此缺项不排family；不代用20319旧配方或盲扫新群。 Later actual recovery now supplies all six regular-action generators and a validated48-base C5^2 x C17 voltage recipe; do not repeat this missing-recipe diagnosis as the current state.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

