---
type: experiment
node_id: exp:ddp-wave7-shortcut650
title: "固定650源加全局perfectmatching降径"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave7/shortcut650/REPORT.md; research/ddp/breadth_20261027_wave7/shortcut650/MODEL.md; research/ddp/breadth_20261027_wave7/shortcut650/best.F.edges; research/ddp/breadth_20261027_wave7/shortcut650/best.edges; research/ddp/breadth_20261027_wave7/shortcut650/best.independent_check.json; research/ddp/breadth_20261027_wave7/shortcut650/best_score.json; research/ddp/breadth_20261027_wave7/shortcut650/first_proposal_calibration.json; research/ddp/breadth_20261027_wave7/shortcut650/initial0.F.edges; research/ddp/breadth_20261027_wave7/shortcut650/initial0_row_pairs.json; research/ddp/breadth_20261027_wave7/shortcut650/initial1.F.edges; research/ddp/breadth_20261027_wave7/shortcut650/initial1_construction.json; research/ddp/breadth_20261027_wave7/shortcut650/model_check.json; research/ddp/breadth_20261027_wave7/shortcut650/run.py; research/ddp/breadth_20261027_wave7/shortcut650/search.cpp; research/ddp/breadth_20261027_wave7/shortcut650/search_result.json; research/ddp/breadth_20261027_wave7/shortcut650/terminal.json"
added: 2026-10-27T08:25:53Z
tags: ["ddp", "method-ledger"]
---

# 固定650源加全局perfectmatching降径

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (6,4)；L=441；candidate_graph_or_family n=650；条件性n=650（未据此计纪录）

**距目标的证据：** 实际D=5，目标D=4；普通无序坏对=31918；saved_explicit_graph；最佳图D5、31918个>4无序对；不排其他全局matching。

**其他指标（保持原计数类型）：**
```json
{
  "old_bad_unordered_pairs": 87800,
  "legal_proposals": 10000
}
```





**原始证据：** [research/ddp/breadth_20261027_wave7/shortcut650/REPORT.md](../../research/ddp/breadth_20261027_wave7/shortcut650/REPORT.md)；[research/ddp/breadth_20261027_wave7/shortcut650/MODEL.md](../../research/ddp/breadth_20261027_wave7/shortcut650/MODEL.md)；[research/ddp/breadth_20261027_wave7/shortcut650/best.F.edges](../../research/ddp/breadth_20261027_wave7/shortcut650/best.F.edges)；[research/ddp/breadth_20261027_wave7/shortcut650/best.edges](../../research/ddp/breadth_20261027_wave7/shortcut650/best.edges)；[research/ddp/breadth_20261027_wave7/shortcut650/best.independent_check.json](../../research/ddp/breadth_20261027_wave7/shortcut650/best.independent_check.json)；[research/ddp/breadth_20261027_wave7/shortcut650/best_score.json](../../research/ddp/breadth_20261027_wave7/shortcut650/best_score.json)；[research/ddp/breadth_20261027_wave7/shortcut650/first_proposal_calibration.json](../../research/ddp/breadth_20261027_wave7/shortcut650/first_proposal_calibration.json)；[research/ddp/breadth_20261027_wave7/shortcut650/initial0.F.edges](../../research/ddp/breadth_20261027_wave7/shortcut650/initial0.F.edges)；[research/ddp/breadth_20261027_wave7/shortcut650/initial0_row_pairs.json](../../research/ddp/breadth_20261027_wave7/shortcut650/initial0_row_pairs.json)；[research/ddp/breadth_20261027_wave7/shortcut650/initial1.F.edges](../../research/ddp/breadth_20261027_wave7/shortcut650/initial1.F.edges)；[research/ddp/breadth_20261027_wave7/shortcut650/initial1_construction.json](../../research/ddp/breadth_20261027_wave7/shortcut650/initial1_construction.json)；[research/ddp/breadth_20261027_wave7/shortcut650/model_check.json](../../research/ddp/breadth_20261027_wave7/shortcut650/model_check.json)；[research/ddp/breadth_20261027_wave7/shortcut650/run.py](../../research/ddp/breadth_20261027_wave7/shortcut650/run.py)；[research/ddp/breadth_20261027_wave7/shortcut650/search.cpp](../../research/ddp/breadth_20261027_wave7/shortcut650/search.cpp)；[research/ddp/breadth_20261027_wave7/shortcut650/search_result.json](../../research/ddp/breadth_20261027_wave7/shortcut650/search_result.json)；[research/ddp/breadth_20261027_wave7/shortcut650/terminal.json](../../research/ddp/breadth_20261027_wave7/shortcut650/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 两固定starts各5000合法matching switches；允许打破初态对称性/远距限制

**正向保证：** 旧1625边全保留；新增325条perfectmatching；全部原≤4点对保持；评分包括两条新匹配边路径

**仍未完成：** 所有LL/LB/LH/BB/BH/HH层对仍有缺项。

**启发与重启依据：** 该profile停止，需不同覆盖结构，不追加HH修补或seed。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

