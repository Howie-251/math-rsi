---
type: experiment
node_id: exp:ddp-wave2-two-orbit128-search
title: "Q64双轨道128实际14phase有限试验"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave2/two_orbit128_search/REPORT.md; research/ddp/breadth_20261027_wave2/two_orbit128_search/best.edges; research/ddp/breadth_20261027_wave2/two_orbit128_search/best.independent_check.json; research/ddp/breadth_20261027_wave2/two_orbit128_search/best.json; research/ddp/breadth_20261027_wave2/two_orbit128_search/first.cpp_calibration.json; research/ddp/breadth_20261027_wave2/two_orbit128_search/first.python_calibration.json; research/ddp/breadth_20261027_wave2/two_orbit128_search/first_expected.txt; research/ddp/breadth_20261027_wave2/two_orbit128_search/inputs.json; research/ddp/breadth_20261027_wave2/two_orbit128_search/rules.txt; research/ddp/breadth_20261027_wave2/two_orbit128_search/run.json; research/ddp/breadth_20261027_wave2/two_orbit128_search/search.terminal.json; research/ddp/breadth_20261027_wave2/two_orbit128_search/terminal.json"
added: 2026-10-27T08:25:51Z
tags: ["ddp", "method-ledger"]
---

# Q64双轨道128实际14phase有限试验

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (6,3)；L=120；candidate_graph_or_family n=128；条件性n=128（未据此计纪录）

**距目标的证据：** 实际D=4，目标D=3；普通无序坏对=928；saved_explicit_graph；bestD4/928；所有预定phase完成后停止。

**其他指标（保持原计数类型）：**
```json
{
  "representative_deficit_sum": 29,
  "translation_factor_to_unordered": 32,
  "legal_score_evaluations": 13422
}
```





**原始证据：** [research/ddp/breadth_20261027_wave2/two_orbit128_search/REPORT.md](../../research/ddp/breadth_20261027_wave2/two_orbit128_search/REPORT.md)；[research/ddp/breadth_20261027_wave2/two_orbit128_search/best.edges](../../research/ddp/breadth_20261027_wave2/two_orbit128_search/best.edges)；[research/ddp/breadth_20261027_wave2/two_orbit128_search/best.independent_check.json](../../research/ddp/breadth_20261027_wave2/two_orbit128_search/best.independent_check.json)；[research/ddp/breadth_20261027_wave2/two_orbit128_search/best.json](../../research/ddp/breadth_20261027_wave2/two_orbit128_search/best.json)；[research/ddp/breadth_20261027_wave2/two_orbit128_search/first.cpp_calibration.json](../../research/ddp/breadth_20261027_wave2/two_orbit128_search/first.cpp_calibration.json)；[research/ddp/breadth_20261027_wave2/two_orbit128_search/first.python_calibration.json](../../research/ddp/breadth_20261027_wave2/two_orbit128_search/first.python_calibration.json)；[research/ddp/breadth_20261027_wave2/two_orbit128_search/first_expected.txt](../../research/ddp/breadth_20261027_wave2/two_orbit128_search/first_expected.txt)；[research/ddp/breadth_20261027_wave2/two_orbit128_search/inputs.json](../../research/ddp/breadth_20261027_wave2/two_orbit128_search/inputs.json)；[research/ddp/breadth_20261027_wave2/two_orbit128_search/rules.txt](../../research/ddp/breadth_20261027_wave2/two_orbit128_search/rules.txt)；[research/ddp/breadth_20261027_wave2/two_orbit128_search/run.json](../../research/ddp/breadth_20261027_wave2/two_orbit128_search/run.json)；[research/ddp/breadth_20261027_wave2/two_orbit128_search/search.terminal.json](../../research/ddp/breadth_20261027_wave2/two_orbit128_search/search.terminal.json)；[research/ddp/breadth_20261027_wave2/two_orbit128_search/terminal.json](../../research/ddp/breadth_20261027_wave2/two_orbit128_search/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 14个通过phase，各固定三段邻域/两次kick；非全部Q64参数穷尽

**正向保证：** two-orbit作用代表根数与全图计数相符

**仍未完成：** 代表根deficit29不是928无序坏对。

**启发与重启依据：** 该有限profile停止，不能以余预算加kick。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

