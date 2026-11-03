---
type: experiment
node_id: exp:ddp-wave11-polynomial343-matching-scout
title: "F7³多项式343源加任意matching：根半径三上界302严格排除"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/REPORT.md; research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/PREDICTION.json; research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/RESULT.json; research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/terminal.json; research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/check_endpoint_budget.py; research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/FORMAL_ENDPOINT_IMAGE.json; research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/ANALYSIS_PROOF.md; research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/ANALYSIS_PROOF.json; research/ddp/breadth_20261027_wave11/polynomial343_matching_scout/REPORT.md; research/ddp/breadth_20261027_wave11/polynomial343_matching_scout/RESULT.json; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/SCOUT_SCOPE_AND_OVERLAP_REVIEW.md; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/SCOUT_SCOPE_AND_OVERLAP_REVIEW.json"
added: 2026-10-28T03:06:09Z
tags: ["ddp", "method-ledger"]
---

# F7³多项式343源加任意matching：根半径三上界302严格排除

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** (8,3)；L=253；条件性n=343（未据此计纪录）

**距目标的证据：** 首次343形式端点三元组枚举image154/每d22，CPU0.000389805；纸面独立代数证明154并穷尽0M/首M/中M/末M/MGM五类，至少41个根缺项。无源或候选图、BFS、matching试验、solver。

**其他指标（保持原计数类型）：**
```json
{
  "baseline_date": "2026-10-28",
  "parent_source_record": "ddp-wave11-polynomial343-matching-scout",
  "formal_triples": 343,
  "formal_image": 154,
  "endpoints_per_first_coordinate": 22,
  "one_M_first_upper": 50,
  "one_M_middle_upper": 48,
  "one_M_last_upper": 43,
  "two_M_upper": 7,
  "uniform_R3_upper": 302,
  "uniform_missing_root_targets_lower_bound": 41,
  "count_type": "symbolic endpoint upper bound, not ordinary graph bad pairs",
  "first_exact_endpoint_body_CPU_seconds": 0.000389805,
  "matching_assignments_tested": 0,
  "complete_graphs_generated": 0,
  "source_BFS": 0,
  "target_BFS": 0,
  "solver_calls": 0,
  "UNKNOWN": 0,
  "same_family_general_odd_q_corollary": "q>=7",
  "independent_method_count_increment": 0
}
```



**从属变体：**
```json
[
  {
    "name": "arbitrary-single-matching-endpoint-budget",
    "status": "STRICT_EXCLUSION",
    "new_symbolic_triples": 343,
    "new_matching_tests": 0,
    "actual_n": null,
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "report_paths": [
      "research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/REPORT.md",
      "research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/PREDICTION.json",
      "research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/RESULT.json",
      "research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/terminal.json",
      "research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/check_endpoint_budget.py",
      "research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/FORMAL_ENDPOINT_IMAGE.json",
      "research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/ANALYSIS_PROOF.md",
      "research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/ANALYSIS_PROOF.json",
      "research/ddp/breadth_20261027_wave11/polynomial343_matching_scout/REPORT.md",
      "research/ddp/breadth_20261027_wave11/polynomial343_matching_scout/RESULT.json",
      "research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/SCOUT_SCOPE_AND_OVERLAP_REVIEW.md",
      "research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/SCOUT_SCOPE_AND_OVERLAP_REVIEW.json"
    ]
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/REPORT.md](../../research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/REPORT.md)；[research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/PREDICTION.json](../../research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/PREDICTION.json)；[research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/RESULT.json](../../research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/RESULT.json)；[research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/terminal.json](../../research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/terminal.json)；[research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/check_endpoint_budget.py](../../research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/check_endpoint_budget.py)；[research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/FORMAL_ENDPOINT_IMAGE.json](../../research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/FORMAL_ENDPOINT_IMAGE.json)；[research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/ANALYSIS_PROOF.md](../../research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/ANALYSIS_PROOF.md)；[research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/ANALYSIS_PROOF.json](../../research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/ANALYSIS_PROOF.json)；[research/ddp/breadth_20261027_wave11/polynomial343_matching_scout/REPORT.md](../../research/ddp/breadth_20261027_wave11/polynomial343_matching_scout/REPORT.md)；[research/ddp/breadth_20261027_wave11/polynomial343_matching_scout/RESULT.json](../../research/ddp/breadth_20261027_wave11/polynomial343_matching_scout/RESULT.json)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/SCOUT_SCOPE_AND_OVERLAP_REVIEW.md](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/SCOUT_SCOPE_AND_OVERLAP_REVIEW.md)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/SCOUT_SCOPE_AND_OVERLAP_REVIEW.json](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/SCOUT_SCOPE_AND_OVERLAP_REVIEW.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定F7³邻接(s,as-b,a²s+as²-c)，删loops，保全部旧边并添加任意一个complement内simple matching，允许partial。完整新根路径分类给B3≤302<343；不枚matching。

**正向保证：** The loop-deleted polynomial formula is simple undirected, maximum degree7, with the origin degree6.；The origin closed radius-three endpoint image is exactly154, proved algebraically and checked by343 formal triples.；The five reduced matching-path classes cover every possible augmented path of length at most3, including arbitrary partial matchings.

**仍未完成：** 一般343/max8/D3图、多个matching、任意加边、删边或重连未被排除。

**启发与重启依据：** 旧source节点同id更新；停止此任意singlematching族。奇prime-power q>=7同公式均失败只是同family代数推论，不多计实验或方法。改变连接规则或源才可另立具体问题，不按缺项优化matching。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

