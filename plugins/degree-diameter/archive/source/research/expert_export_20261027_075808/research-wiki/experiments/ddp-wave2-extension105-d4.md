---
type: experiment
node_id: exp:ddp-wave2-extension105-d4
title: "固定104c→105单点四spoke增阶"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave2/extension105_d4/REPORT.md; research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/REPORT.md; research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/REPORT.md; research/ddp/breadth_20261027_wave2/extension105_d4/best.edges; research/ddp/breadth_20261027_wave2/extension105_d4/best.independent_check.json; research/ddp/breadth_20261027_wave2/extension105_d4/best.json; research/ddp/breadth_20261027_wave2/extension105_d4/first_calibration.json; research/ddp/breadth_20261027_wave2/extension105_d4/first_expected.txt; research/ddp/breadth_20261027_wave2/extension105_d4/inputs.json; research/ddp/breadth_20261027_wave2/extension105_d4/production.json; research/ddp/breadth_20261027_wave2/extension105_d4/run.json; research/ddp/breadth_20261027_wave2/extension105_d4/source.edges; research/ddp/breadth_20261027_wave2/extension105_d4/terminal.json; research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/best.edges; research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/best.json; research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/best.verification_reuse.json; research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/candidates.jsonl; research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/completions.txt; research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/first.expected.edges; research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/first.independent_calibration.json; research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/fixed.edges; research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/inputs.json; research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/run.json; research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/source.edges; research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/terminal.json; research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/best.edges; research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/best.json; research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/best.verification_reuse.json; research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/first.cpp_calibration.json; research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/first.expected.edges; research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/first.independent_calibration.json; research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/inputs.json; research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/run.json; research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/source.edges; research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/terminal.json"
added: 2026-10-27T07:55:16Z
tags: ["ddp", "method-ledger"]
---

# 固定104c→105单点四spoke增阶

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (4,4)；L=104；candidate_graph_or_family n=105；条件性n=105（未据此计纪录）

**距目标的证据：** 实际D=5，目标D=4；普通无序坏对=8；saved_explicit_graph；20904合法候选全部无D4；bestD5/8。两局部跟进也无改善，best复用同一图验收。

**其他指标（保持原计数类型）：**
```json
{
  "raw_source_edge_pairs": 21528,
  "legal_candidates": 20904
}
```



**从属变体：**
```json
[
  {
    "id": "complete-two-edge-switch-neighborhood",
    "scope": "保存best的全部普通单步2switch",
    "legal_neighbors": 40740,
    "strict_improvements": 0,
    "best_unchanged": true,
    "actual_D_reused": 5,
    "bad_unordered_reused": 8
  },
  {
    "id": "fixed-nine-vertex-degree-completion",
    "scope": "只释放12/13的八条incident边，九点准确残余degree",
    "completions": 230,
    "best_unchanged": true,
    "actual_D_reused": 5,
    "bad_unordered_reused": 8
  }
]
```

**原始证据：** [research/ddp/breadth_20261027_wave2/extension105_d4/REPORT.md](../../research/ddp/breadth_20261027_wave2/extension105_d4/REPORT.md)；[research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/REPORT.md](../../research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/REPORT.md)；[research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/REPORT.md](../../research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/REPORT.md)；[research/ddp/breadth_20261027_wave2/extension105_d4/best.edges](../../research/ddp/breadth_20261027_wave2/extension105_d4/best.edges)；[research/ddp/breadth_20261027_wave2/extension105_d4/best.independent_check.json](../../research/ddp/breadth_20261027_wave2/extension105_d4/best.independent_check.json)；[research/ddp/breadth_20261027_wave2/extension105_d4/best.json](../../research/ddp/breadth_20261027_wave2/extension105_d4/best.json)；[research/ddp/breadth_20261027_wave2/extension105_d4/first_calibration.json](../../research/ddp/breadth_20261027_wave2/extension105_d4/first_calibration.json)；[research/ddp/breadth_20261027_wave2/extension105_d4/first_expected.txt](../../research/ddp/breadth_20261027_wave2/extension105_d4/first_expected.txt)；[research/ddp/breadth_20261027_wave2/extension105_d4/inputs.json](../../research/ddp/breadth_20261027_wave2/extension105_d4/inputs.json)；[research/ddp/breadth_20261027_wave2/extension105_d4/production.json](../../research/ddp/breadth_20261027_wave2/extension105_d4/production.json)；[research/ddp/breadth_20261027_wave2/extension105_d4/run.json](../../research/ddp/breadth_20261027_wave2/extension105_d4/run.json)；[research/ddp/breadth_20261027_wave2/extension105_d4/source.edges](../../research/ddp/breadth_20261027_wave2/extension105_d4/source.edges)；[research/ddp/breadth_20261027_wave2/extension105_d4/terminal.json](../../research/ddp/breadth_20261027_wave2/extension105_d4/terminal.json)；[research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/best.edges](../../research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/best.edges)；[research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/best.json](../../research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/best.json)；[research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/best.verification_reuse.json](../../research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/best.verification_reuse.json)；[research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/candidates.jsonl](../../research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/candidates.jsonl)；[research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/completions.txt](../../research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/completions.txt)；[research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/first.expected.edges](../../research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/first.expected.edges)；[research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/first.independent_calibration.json](../../research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/first.independent_calibration.json)；[research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/fixed.edges](../../research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/fixed.edges)；[research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/inputs.json](../../research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/inputs.json)；[research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/run.json](../../research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/run.json)；[research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/source.edges](../../research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/source.edges)；[research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/terminal.json](../../research/ddp/breadth_20261027_wave2/extension105_d4/two_branch_completion/terminal.json)；[research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/best.edges](../../research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/best.edges)；[research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/best.json](../../research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/best.json)；[research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/best.verification_reuse.json](../../research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/best.verification_reuse.json)；[research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/first.cpp_calibration.json](../../research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/first.cpp_calibration.json)；[research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/first.expected.edges](../../research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/first.expected.edges)；[research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/first.independent_calibration.json](../../research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/first.independent_calibration.json)；[research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/inputs.json](../../research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/inputs.json)；[research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/run.json](../../research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/run.json)；[research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/source.edges](../../research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/source.edges)；[research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/terminal.json](../../research/ddp/breadth_20261027_wave2/extension105_d4/two_edge_switches/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定104c删两条不接边、加一点连其四端点；后续两个局部邻域属于本源跟进

**正向保证：** 所有候选simple4regular105/210；完整既定参数范围

**仍未完成：** 不排其他增阶操作或一般105图；不是整个source扩张族穷尽。

**启发与重启依据：** 此source已收束，不追加局部自由点或多边交换。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

