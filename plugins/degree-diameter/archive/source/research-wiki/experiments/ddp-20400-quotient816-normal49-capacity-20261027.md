---
type: experiment
node_id: exp:ddp-20400-quotient816-normal49-capacity-20261027
title: "实际816商七步raw容量min111：F7²纤维49未被必要计数排除"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d6_D7_current20400_source/quotient816_capacity/REPORT.md; research/ddp/more_graphs_20261027/d6_D7_current20400_source/quotient816_capacity/PREDICTION.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/quotient816_capacity/RESULT.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/quotient816_capacity/COUNTS.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/quotient816_capacity/count.py"
added: 2026-10-27T20:51:14Z
tags: ["ddp", "method-ledger"]
---

# 实际816商七步raw容量min111：F7²纤维49未被必要计数排除

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** capacity

**目标与阶数：** (6,7)；L=20400；条件性n=39984（未据此计纪录）

**距目标的证据：** minK=111，在(base16,0)/(base32,0)，各len4/6/7 rawcounts=1/19/91。共同纤维size必须≤111，原25校准过；F7²49≤111，容量预测支持但完全不等于39984图存在或D7充分。

**其他指标（保持原计数类型）：**
```json
{
  "quotient_states": 816,
  "normal_source_module_order": 25,
  "hypothetical_F7_squared_order": 49,
  "hypothetical_order": 39984,
  "raw_NB_words": 117187,
  "word_counts_by_length": [
    1,
    6,
    30,
    150,
    750,
    3750,
    18750,
    93750
  ],
  "minimum_K": 111,
  "min_witnesses": [
    {
      "state": 272,
      "target_base": 16,
      "c17": 0,
      "raw_routes": 111,
      "routes_by_depth": [
        0,
        0,
        0,
        0,
        1,
        0,
        19,
        91
      ]
    },
    {
      "state": 544,
      "target_base": 32,
      "c17": 0,
      "raw_routes": 111,
      "routes_by_depth": [
        0,
        0,
        0,
        0,
        1,
        0,
        19,
        91
      ]
    }
  ],
  "original25_check": true,
  "q7_capacity_allowed": true,
  "sufficient_for_cover": false,
  "capacity_metric_unit": "Raw labeled nonbacktracking word multiplicity at quotientendpoint; not actualfibercoverage or ordinarygraphbadpairs",
  "CPU_seconds": 0.034097815,
  "source_graph_parses": 0,
  "graph_BFS": 0,
  "group_or_module_search": false,
  "candidate_graphs": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d6_D7_current20400_source/quotient816_capacity/REPORT.md](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/quotient816_capacity/REPORT.md)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/quotient816_capacity/PREDICTION.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/quotient816_capacity/PREDICTION.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/quotient816_capacity/RESULT.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/quotient816_capacity/RESULT.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/quotient816_capacity/COUNTS.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/quotient816_capacity/COUNTS.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/quotient816_capacity/count.py](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/quotient816_capacity/count.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 复用actual48base×F5²×C17配方，忘a/b得到816state商；从(base0,c17=0)一根完整NB≤7 raw词计数117187，保六labeledports含投影loop/parallel，按recordedreverseport禁立即inverse。只容量，0sourceparse/BFS/新表示/候选。

**仍未完成：** Newnormalmodule representation, connectedness, fullD7coverage and candidateexistence remain open; no generalparameter bound beyond this fixedquotientstepfiber capacity.

**启发与重启依据：** 从actualquotient先决定新module规模是否有路线预算，再谈关系保留表示；此处rawcount允许49，下一H48complement/表示任务须另授权，未自动开始。不同word可能collision，K不是新图/实际覆盖数。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

