---
type: experiment
node_id: exp:ddp-wave6-affine-linker504
title: "AG(2,3)/K7三层504点全局H交换"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave6/affine_linker504/REPORT.md; research/ddp/breadth_20261027_wave6/affine_linker504/best.edges; research/ddp/breadth_20261027_wave6/affine_linker504/best.independent_check.json; research/ddp/breadth_20261027_wave6/affine_linker504/best_H.edges; research/ddp/breadth_20261027_wave6/affine_linker504/best_score.json; research/ddp/breadth_20261027_wave6/affine_linker504/first_proposal_calibration.json; research/ddp/breadth_20261027_wave6/affine_linker504/run.py; research/ddp/breadth_20261027_wave6/affine_linker504/search.cpp; research/ddp/breadth_20261027_wave6/affine_linker504/search_result.json; research/ddp/breadth_20261027_wave6/affine_linker504/structure.json; research/ddp/breadth_20261027_wave6/affine_linker504/terminal.json"
added: 2026-10-27T07:55:17Z
tags: ["ddp", "method-ledger"]
---

# AG(2,3)/K7三层504点全局H交换

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (6,4)；L=441；candidate_graph_or_family n=504；条件性n=504（未据此计纪录）

**距目标的证据：** 实际D=6，目标D=4；普通无序坏对=17073；saved_explicit_graph；最佳504图D6、17073个>4无序对；有限失败不排全部H。

**其他指标（保持原计数类型）：**
```json
{
  "proposals": 4000,
  "best_relevant_H_short_endpoint_pairs": 698,
  "coarse_necessary": 840,
  "bad_layers": {
    "AB": 2255,
    "AC": 1572,
    "BB": 3575,
    "BC": 6485,
    "CC": 3186
  }
}
```





**原始证据：** [research/ddp/breadth_20261027_wave6/affine_linker504/REPORT.md](../../research/ddp/breadth_20261027_wave6/affine_linker504/REPORT.md)；[research/ddp/breadth_20261027_wave6/affine_linker504/best.edges](../../research/ddp/breadth_20261027_wave6/affine_linker504/best.edges)；[research/ddp/breadth_20261027_wave6/affine_linker504/best.independent_check.json](../../research/ddp/breadth_20261027_wave6/affine_linker504/best.independent_check.json)；[research/ddp/breadth_20261027_wave6/affine_linker504/best_H.edges](../../research/ddp/breadth_20261027_wave6/affine_linker504/best_H.edges)；[research/ddp/breadth_20261027_wave6/affine_linker504/best_score.json](../../research/ddp/breadth_20261027_wave6/affine_linker504/best_score.json)；[research/ddp/breadth_20261027_wave6/affine_linker504/first_proposal_calibration.json](../../research/ddp/breadth_20261027_wave6/affine_linker504/first_proposal_calibration.json)；[research/ddp/breadth_20261027_wave6/affine_linker504/run.py](../../research/ddp/breadth_20261027_wave6/affine_linker504/run.py)；[research/ddp/breadth_20261027_wave6/affine_linker504/search.cpp](../../research/ddp/breadth_20261027_wave6/affine_linker504/search.cpp)；[research/ddp/breadth_20261027_wave6/affine_linker504/search_result.json](../../research/ddp/breadth_20261027_wave6/affine_linker504/search_result.json)；[research/ddp/breadth_20261027_wave6/affine_linker504/structure.json](../../research/ddp/breadth_20261027_wave6/affine_linker504/structure.json)；[research/ddp/breadth_20261027_wave6/affine_linker504/terminal.json](../../research/ddp/breadth_20261027_wave6/affine_linker504/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定A/C/CB与任意simple cubic B层H；只2starts×2000合法H交换

**正向保证：** 全部A-A≤4；samepoint A-C≤3及C-C≤4；intersecting-label C-C≤4；图connected独立于H

**仍未完成：** 跨cell不交标签及B相关远端未闭；best相关端点698<粗必要840。

**启发与重启依据：** 需要全局端点覆盖新结构，不能把坏对下降当接近D4或加seed。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

