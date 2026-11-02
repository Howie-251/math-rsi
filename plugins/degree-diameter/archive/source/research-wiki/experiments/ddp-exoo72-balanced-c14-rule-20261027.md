---
type: experiment
node_id: exp:ddp-exoo72-balanced-c14-rule-20261027
title: "Exoo72整体循环规则：84点失败如解析预测，固定放大规则关闭"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d5_exoo72_extension/REPORT.md; research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/CYCLIC_REPORT.md; research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/CYCLIC_PREDICTION.json; research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/CYCLIC_RULE.json; research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/CYCLIC_CAPACITY.json; research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/CYCLIC_RESULT.json; research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/C14.edges"
added: 2026-10-27T15:27:58Z
tags: ["ddp", "method-ledger"]
---

# Exoo72整体循环规则：84点失败如解析预测，固定放大规则关闭

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (5,3)；L=72；candidate_graph_or_family n=84

**距目标的证据：** Exactcyclicorbitroot endpoints onlythroughradius3;D>=4,exactDnotcomputed.；完整84点210边simpleconnected5regular图，六轨道代表R3遗漏12/13/11/13/13/12；root0自纤维准确缺2/6/8/12。D至少4、精确D未知，无普通全图坏对数。

**其他指标（保持原计数类型）：**
```json
{
  "candidate_graphs_generated": 1,
  "new_lower_bounds": 0,
  "diameter_lower_bound": 4,
  "representative_root_R3_missing": [
    12,
    13,
    11,
    13,
    13,
    12
  ],
  "root0_self_missing": [
    2,
    6,
    8,
    12
  ],
  "prediction": "SUPPORTED",
  "raw_min_route_capacity": 14,
  "free_min_form_capacity": 14,
  "literal_min_form_capacity": 12,
  "source_BFS": 0,
  "candidate_BFS": 0,
  "CPU_seconds": 0.0031486240000000026
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d5_exoo72_extension/REPORT.md](../../research/ddp/more_graphs_20261027/d5_exoo72_extension/REPORT.md)；[research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/CYCLIC_REPORT.md](../../research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/CYCLIC_REPORT.md)；[research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/CYCLIC_PREDICTION.json](../../research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/CYCLIC_PREDICTION.json)；[research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/CYCLIC_RULE.json](../../research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/CYCLIC_RULE.json)；[research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/CYCLIC_CAPACITY.json](../../research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/CYCLIC_CAPACITY.json)；[research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/CYCLIC_RESULT.json](../../research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/CYCLIC_RESULT.json)；[research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/C14.edges](../../research/ddp/more_graphs_20261027/d5_exoo72_extension/source_analysis/C14.edges)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Sixbase topology+two sharedhalfturn matchings;14crossvoltages frozenbalanced integers. OneC14lift generated;symbolicbounds separatelyforfreevoltagesandliteralrule.

**仍未完成：** 一般(5,3)超过72仍未解；此受限范围不是全题，完整Lean实例0。

**启发与重启依据：** 源h6用偶数偏移补位；C14的h7重复已有奇数偏移。固定balanced偶数lift>72全闭；自由电压m>=16由raw14容量排除，自由C14仍开放且未搜索，不自动进入难点solver。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

