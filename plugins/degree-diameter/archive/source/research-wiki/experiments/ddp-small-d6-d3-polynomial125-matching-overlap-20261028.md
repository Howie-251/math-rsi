---
type: experiment
node_id: exp:ddp-small-d6-d3-polynomial125-matching-overlap-20261028
title: "F5³多项式125源加任意matching：精确partner交叠给R3≤120"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/REPORT.md; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/PREDICTION.json; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/RESULT.json; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/terminal.json; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/check_overlap.py; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/PARTNER_BALL_MARGINALS.json; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/ANALYSIS_PROOF.md; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/ANALYSIS_PROOF.json; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/SCOUT_SCOPE_AND_OVERLAP_REVIEW.md; research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/SCOUT_SCOPE_AND_OVERLAP_REVIEW.json; research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/ANALYSIS_PROOF.md; research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/ANALYSIS_PROOF.json"
added: 2026-10-28T03:06:09Z
tags: ["ddp", "method-ledger"]
---

# F5³多项式125源加任意matching：精确partner交叠给R3≤120

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** (6,3)；L=120；条件性n=125（未据此计纪录）

**距目标的证据：** 首次q5显式端点评价全部125partner/其中120eligible，实际maxmarginal20、24witness，CPU0.001438583；原预测≤24被更强数据支持。任意matching至少5根缺项，未构建源/增强图且0BFS/Mtests/solver。

**其他指标（保持原计数类型）：**
```json
{
  "baseline_date": "2026-10-28",
  "same_family_parent_record": "ddp-wave11-polynomial343-matching-scout",
  "potential_partners": 125,
  "eligible_complement_partners": 120,
  "root_formal_triples": 125,
  "source_B3_exact": 55,
  "source_B2_exact": 21,
  "actual_max_partner_B2_marginal": 20,
  "maximizing_partners": 24,
  "predicted_max_marginal_threshold": 24,
  "prediction_status": "SUPPORTED_STRONGER_ACTUAL20",
  "matched_root_R3_upper": 120,
  "unmatched_root_R3_upper": 96,
  "uniform_missing_root_targets_lower_bound": 5,
  "first_exact_endpoint_body_CPU_seconds": 0.001438583,
  "complete_graphs_generated": 0,
  "source_BFS": 0,
  "target_BFS": 0,
  "matching_assignments_tested": 0,
  "solver_calls": 0,
  "UNKNOWN": 0,
  "independent_method_count_increment": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/REPORT.md](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/REPORT.md)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/PREDICTION.json](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/PREDICTION.json)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/RESULT.json](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/RESULT.json)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/terminal.json](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/terminal.json)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/check_overlap.py](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/check_overlap.py)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/PARTNER_BALL_MARGINALS.json](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/PARTNER_BALL_MARGINALS.json)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/ANALYSIS_PROOF.md](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/ANALYSIS_PROOF.md)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/ANALYSIS_PROOF.json](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/ANALYSIS_PROOF.json)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/SCOUT_SCOPE_AND_OVERLAP_REVIEW.md](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/SCOUT_SCOPE_AND_OVERLAP_REVIEW.md)；[research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/SCOUT_SCOPE_AND_OVERLAP_REVIEW.json](../../research/ddp/more_graphs_20261027/small_d6_D3_polynomial125_matching_overlap/SCOUT_SCOPE_AND_OVERLAP_REVIEW.json)；[research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/ANALYSIS_PROOF.md](../../research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/ANALYSIS_PROOF.md)；[research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/ANALYSIS_PROOF.json](../../research/ddp/more_graphs_20261027/small_d8_D3_polynomial343_arbitrary_matching_budget/ANALYSIS_PROOF.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定F5³ polynomial源保边加一个任意simple complement matching，含partial；原根B3=55、B2=21，全部120合法mate之B2新增marginal最大20，去重路类给matched≤120/unmatched≤96。

**正向保证：** The loop-deleted q5 polynomial source has maximum degree5 and origin degree4; one added matching gives maximum degree at most6.；The exact origin closed balls have sizes B3=55 and B2=21.；All120 eligible root mates were covered by exact two-step endpoint formulas; the actual maximum additional marginal is20.；The explicit endpoint deduplication remains valid for partial matchings and includes M-G-M paths.

**仍未完成：** 一般125/max6/D3图、absoluteC5+matching、多matching、任意加边或重连未排。

**启发与重启依据：** 与q7同polynomial/matching机制的小边界参数对照，不新增独立方法；singlematching整族停止。absoluteC5使用每absolute两个新槽，因此是明确改变规则，不被本闭范围误排。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

