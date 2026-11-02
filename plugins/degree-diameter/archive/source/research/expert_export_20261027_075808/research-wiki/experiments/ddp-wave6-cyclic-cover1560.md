---
type: experiment
node_id: exp:ddp-wave6-cyclic-cover1560
title: "120点D3源的普通C13覆盖"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave6/cyclic_cover1560/REPORT.md; research/ddp/breadth_20261027_wave6/cyclic_cover1560/best.edges; research/ddp/breadth_20261027_wave6/cyclic_cover1560/best.independent_check.json; research/ddp/breadth_20261027_wave6/cyclic_cover1560/best_parameters.json; research/ddp/breadth_20261027_wave6/cyclic_cover1560/capacity.json; research/ddp/breadth_20261027_wave6/cyclic_cover1560/capacity.py; research/ddp/breadth_20261027_wave6/cyclic_cover1560/first_incremental_calibration.json; research/ddp/breadth_20261027_wave6/cyclic_cover1560/forms.txt; research/ddp/breadth_20261027_wave6/cyclic_cover1560/full_capacity.py; research/ddp/breadth_20261027_wave6/cyclic_cover1560/run_search.py; research/ddp/breadth_20261027_wave6/cyclic_cover1560/search.cpp; research/ddp/breadth_20261027_wave6/cyclic_cover1560/search_result.json; research/ddp/breadth_20261027_wave6/cyclic_cover1560/self_capacity.json; research/ddp/breadth_20261027_wave6/cyclic_cover1560/terminal.json; research/ddp/breadth_20261027_wave6/cyclic_cover1560/tree_gauge.json"
added: 2026-10-27T07:55:17Z
tags: ["ddp", "method-ledger"]
---

# 120点D3源的普通C13覆盖

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (6,5)；L=1518；candidate_graph_or_family n=1560；条件性n=1560（未据此计纪录）

**距目标的证据：** 实际D=6，目标D=5；普通无序坏对=31655；saved_explicit_graph；所有槽容量通过；最佳1560图D6、31655个>5无序对，有限profile失败。

**其他指标（保持原计数类型）：**
```json
{
  "missing_root_target_sheet_states": 4870,
  "ordered_bad_pairs": 63310,
  "translation_factor": 13,
  "proposals": 4000
}
```





**原始证据：** [research/ddp/breadth_20261027_wave6/cyclic_cover1560/REPORT.md](../../research/ddp/breadth_20261027_wave6/cyclic_cover1560/REPORT.md)；[research/ddp/breadth_20261027_wave6/cyclic_cover1560/best.edges](../../research/ddp/breadth_20261027_wave6/cyclic_cover1560/best.edges)；[research/ddp/breadth_20261027_wave6/cyclic_cover1560/best.independent_check.json](../../research/ddp/breadth_20261027_wave6/cyclic_cover1560/best.independent_check.json)；[research/ddp/breadth_20261027_wave6/cyclic_cover1560/best_parameters.json](../../research/ddp/breadth_20261027_wave6/cyclic_cover1560/best_parameters.json)；[research/ddp/breadth_20261027_wave6/cyclic_cover1560/capacity.json](../../research/ddp/breadth_20261027_wave6/cyclic_cover1560/capacity.json)；[research/ddp/breadth_20261027_wave6/cyclic_cover1560/capacity.py](../../research/ddp/breadth_20261027_wave6/cyclic_cover1560/capacity.py)；[research/ddp/breadth_20261027_wave6/cyclic_cover1560/first_incremental_calibration.json](../../research/ddp/breadth_20261027_wave6/cyclic_cover1560/first_incremental_calibration.json)；[research/ddp/breadth_20261027_wave6/cyclic_cover1560/forms.txt](../../research/ddp/breadth_20261027_wave6/cyclic_cover1560/forms.txt)；[research/ddp/breadth_20261027_wave6/cyclic_cover1560/full_capacity.py](../../research/ddp/breadth_20261027_wave6/cyclic_cover1560/full_capacity.py)；[research/ddp/breadth_20261027_wave6/cyclic_cover1560/run_search.py](../../research/ddp/breadth_20261027_wave6/cyclic_cover1560/run_search.py)；[research/ddp/breadth_20261027_wave6/cyclic_cover1560/search.cpp](../../research/ddp/breadth_20261027_wave6/cyclic_cover1560/search.cpp)；[research/ddp/breadth_20261027_wave6/cyclic_cover1560/search_result.json](../../research/ddp/breadth_20261027_wave6/cyclic_cover1560/search_result.json)；[research/ddp/breadth_20261027_wave6/cyclic_cover1560/self_capacity.json](../../research/ddp/breadth_20261027_wave6/cyclic_cover1560/self_capacity.json)；[research/ddp/breadth_20261027_wave6/cyclic_cover1560/terminal.json](../../research/ddp/breadth_20261027_wave6/cyclic_cover1560/terminal.json)；[research/ddp/breadth_20261027_wave6/cyclic_cover1560/tree_gauge.json](../../research/ddp/breadth_20261027_wave6/cyclic_cover1560/tree_gauge.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定120源、树gauge、两starts各2000单边电压提案

**正向保证：** 14400槽符号容量19–49≥13；保留simple6regular

**仍未完成：** 代表4870缺状态未闭，不等于无序坏对。

**启发与重启依据：** 本profile停止，不加底图/层数/seed。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

