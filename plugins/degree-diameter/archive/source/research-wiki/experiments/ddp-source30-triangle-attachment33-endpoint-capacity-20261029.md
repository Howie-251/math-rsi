---
type: experiment
node_id: exp:ddp-source30-triangle-attachment33-endpoint-capacity-20261029
title: "Source30 triangle attachment to33: parallel80 and deranged160 both capacity-blocked"
idea_id: "idea:ddp-q3-three-step-plane-pencil31"
verdict: no
confidence: high
date: "2026-10-29"
hardware: ""
duration: ""
provenance: "research/ddp/refresh_20261029/controller33_parallel_triangle/PREDICTION.json; research/ddp/refresh_20261029/controller33_parallel_triangle/INPUT.json; research/ddp/refresh_20261029/controller33_parallel_triangle/CASES.json; research/ddp/refresh_20261029/controller33_parallel_triangle/PASSERS.json; research/ddp/refresh_20261029/controller33_parallel_triangle/RESULT.json; research/ddp/refresh_20261029/controller33_parallel_triangle/TERMINAL.json; research/ddp/refresh_20261029/controller33_parallel_triangle/run.py; research/ddp/refresh_20261029/controller33_parallel_triangle/REPORT.md; research/ddp/refresh_20261029/controller33_parallel_triangle/CUT_PAIR_PREDICTION.json; research/ddp/refresh_20261029/controller33_parallel_triangle/check_cut_pairs.py; research/ddp/refresh_20261029/controller33_parallel_triangle/CUT_PAIR_COUNTS.json; research/ddp/refresh_20261029/controller33_parallel_triangle/CUT_PAIR_RESULT.json; research/ddp/refresh_20261029/controller33_parallel_triangle/CUT_PAIR_OBSTRUCTION.md; research/ddp/refresh_20261029/controller33_deranged_attachment/PREDICTION.json; research/ddp/refresh_20261029/controller33_deranged_attachment/INPUT.json; research/ddp/refresh_20261029/controller33_deranged_attachment/run.py; research/ddp/refresh_20261029/controller33_deranged_attachment/CASES.json; research/ddp/refresh_20261029/controller33_deranged_attachment/PASSERS.json; research/ddp/refresh_20261029/controller33_deranged_attachment/RESULT.json; research/ddp/refresh_20261029/controller33_deranged_attachment/TERMINAL.json; research/ddp/refresh_20261029/controller33_deranged_attachment/FIRST_MISSING_TWO_STEP_COUNTS.json; research/ddp/refresh_20261029/controller33_deranged_attachment/FIRST_MISSING_CAPACITY_RESULT.json; research/ddp/refresh_20261029/controller33_deranged_attachment/REPORT.md; research/ddp/refresh_20261029/controller33_parallel_triangle/RAW_ANALYSIS_FIELDS.json; research/ddp/refresh_20261029/controller33_deranged_attachment/RAW_ANALYSIS_FIELDS.json; research/ddp/refresh_20261029/DERIVATION_PACKAGE.md"
added: 2026-10-29T15:42:10Z
tags: ["ddp", "method-ledger"]
---

# Source30 triangle attachment to33: parallel80 and deranged160 both capacity-blocked

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-q3-three-step-plane-pencil31`

## Metrics
**对象层级：** controller

**目标与阶数：** (16,3)；L=1920；controller n=33；条件性n=2112（未据此计纪录）；从属目标：[[16, 3]]

**距目标的证据：** controller-only stored edge lists and exact short-route counts; no exact global controller D or field graph；平行80项全raw门失败，240cutpairs全唯一2walk／0个3walk，因此任q>1、q^3纤维／每arc最多q分支／无内部纤维边的提升均D3失败，允许offset与任意关系。错位160项修480cutpairs且每对NB3=2，局部预测SUPPORTED；其余firstmissing均非邻且无3walk，134项无2walk、26项仅1个，在64纤维／每arc最多4分支下最多0/16<64，联合存在预测REFUTED。0未试、0targetgraph／BFS／solver；普通坏对与目标实际D均null。

**其他指标（保持原计数类型）：**
```json
{
  "controller_candidates_generated": 240,
  "actual_controller_counts_by_variant": {
    "parallel": 80,
    "deranged": 160
  },
  "actual_controller_n": 33,
  "actual_controller_m": 66,
  "actual_controller_degree": 4,
  "target_field_graphs": 0,
  "actual_target_n": null,
  "actual_target_D": null,
  "hypothetical_field_order": 2112,
  "hypothetical_field_degree": 16,
  "source_or_controller_BFS": 0,
  "new_field_matrix_search": 0,
  "solver_calls": 0,
  "passers": 0,
  "untested": 0,
  "aggregate_CPU_seconds": 0.186564984,
  "no_nonisomorphism_claim": true,
  "new_lower_bound_mathematically_verified": false,
  "same_mechanism_two_variants_not_two_independent_methods": true
}
```



**从属变体：**
```json
[
  {
    "label": "parallel_subdivision_same_new_vertex_80",
    "target_Delta": 16,
    "target_D": 3,
    "target": [
      16,
      3
    ],
    "savedL": 1920,
    "n": {
      "actual": 33,
      "hypothetical": 2112
    },
    "object_level": "controller",
    "actual_controller_degree": 4,
    "actual_controller_m": 66,
    "controller_cases": 80,
    "raw_NB3_pass": 0,
    "failed": 80,
    "untested": 0,
    "structural_prediction": "SUPPORTED",
    "joint_prediction": "REFUTED",
    "first_missing_class_histogram": {
      "old-old": 66,
      "new-old": 14
    },
    "all_missing_class_occurrences": {
      "old-old": 5460,
      "new-old": 3612
    },
    "cutpairs_checked": 240,
    "cutpair_length2_length3_histogram": {
      "1,0": 240
    },
    "raw_controller_CPU_seconds": 0.056890039999999996,
    "cutpair_diagnostic_CPU_seconds": 0.0018728059999999977,
    "total_CPU_seconds": 0.058762845999999994,
    "strong_closed_scope": "All q^3-fiber lifts q>1 of these80 controllers, with atmostq neighbors across each controllerarc and nointernalfiberedges, failD3; arbitrary maps and offsets included. Eachsubdividedcutpair hasonlyone2walk andno3walk, so atmostq^2 endpoints.",
    "target_field_graphs": 0,
    "actual_target_n": null,
    "actual_target_D": null,
    "ordinary_bad_unordered_pairs": null,
    "source_or_controller_BFS": 0,
    "solver_calls": 0
  },
  {
    "label": "two_deranged_threecycle_attachments_160",
    "target_Delta": 16,
    "target_D": 3,
    "target": [
      16,
      3
    ],
    "savedL": 1920,
    "n": {
      "actual": 33,
      "hypothetical": 2112
    },
    "object_level": "controller",
    "actual_controller_degree": 4,
    "actual_controller_m": 66,
    "controller_cases": 160,
    "raw_NB3_pass": 0,
    "failed": 160,
    "untested": 0,
    "local_cut_pair_repair_prediction": "SUPPORTED480/480",
    "joint_prediction": "REFUTED",
    "cutpair_actual_NB3_histogram": {
      "2": 480
    },
    "first_missing_class_histogram": {
      "old-old": 132,
      "new-old": 28
    },
    "all_missing_class_occurrences": {
      "old-old": 10272,
      "new-old": 6792
    },
    "first_missing_no_three_walk": true,
    "first_missing_two_walk_histogram": {
      "0": 134,
      "1": 26
    },
    "q4_endpoint_capacity_bounds": [
      0,
      16
    ],
    "target_fiber_size": 64,
    "raw_controller_CPU_seconds": 0.11984576899999999,
    "saved_firstmissing_diagnostic_CPU_seconds": 0.007956368999999998,
    "total_CPU_seconds": 0.12780213799999998,
    "strong_closed_scope": "All160 controllers have a savednonadjacent pair withno3walk andk≤1 twowalk; arbitrary4branch-per-arc/64fiber relations cannotcover64 endpoints within3, evenwithoffsets.",
    "unexecuted_other_transposition_settings": 240,
    "transposition_status": "Paper fixed-point obstruction only; not generated or counted in the executed160.",
    "target_field_graphs": 0,
    "actual_target_n": null,
    "actual_target_D": null,
    "ordinary_bad_unordered_pairs": null,
    "source_or_controller_BFS": 0,
    "solver_calls": 0
  }
]
```

**原始证据：** [research/ddp/refresh_20261029/controller33_parallel_triangle/PREDICTION.json](../../research/ddp/refresh_20261029/controller33_parallel_triangle/PREDICTION.json)；[research/ddp/refresh_20261029/controller33_parallel_triangle/INPUT.json](../../research/ddp/refresh_20261029/controller33_parallel_triangle/INPUT.json)；[research/ddp/refresh_20261029/controller33_parallel_triangle/CASES.json](../../research/ddp/refresh_20261029/controller33_parallel_triangle/CASES.json)；[research/ddp/refresh_20261029/controller33_parallel_triangle/PASSERS.json](../../research/ddp/refresh_20261029/controller33_parallel_triangle/PASSERS.json)；[research/ddp/refresh_20261029/controller33_parallel_triangle/RESULT.json](../../research/ddp/refresh_20261029/controller33_parallel_triangle/RESULT.json)；[research/ddp/refresh_20261029/controller33_parallel_triangle/TERMINAL.json](../../research/ddp/refresh_20261029/controller33_parallel_triangle/TERMINAL.json)；[research/ddp/refresh_20261029/controller33_parallel_triangle/run.py](../../research/ddp/refresh_20261029/controller33_parallel_triangle/run.py)；[research/ddp/refresh_20261029/controller33_parallel_triangle/REPORT.md](../../research/ddp/refresh_20261029/controller33_parallel_triangle/REPORT.md)；[research/ddp/refresh_20261029/controller33_parallel_triangle/CUT_PAIR_PREDICTION.json](../../research/ddp/refresh_20261029/controller33_parallel_triangle/CUT_PAIR_PREDICTION.json)；[research/ddp/refresh_20261029/controller33_parallel_triangle/check_cut_pairs.py](../../research/ddp/refresh_20261029/controller33_parallel_triangle/check_cut_pairs.py)；[research/ddp/refresh_20261029/controller33_parallel_triangle/CUT_PAIR_COUNTS.json](../../research/ddp/refresh_20261029/controller33_parallel_triangle/CUT_PAIR_COUNTS.json)；[research/ddp/refresh_20261029/controller33_parallel_triangle/CUT_PAIR_RESULT.json](../../research/ddp/refresh_20261029/controller33_parallel_triangle/CUT_PAIR_RESULT.json)；[research/ddp/refresh_20261029/controller33_parallel_triangle/CUT_PAIR_OBSTRUCTION.md](../../research/ddp/refresh_20261029/controller33_parallel_triangle/CUT_PAIR_OBSTRUCTION.md)；[research/ddp/refresh_20261029/controller33_deranged_attachment/PREDICTION.json](../../research/ddp/refresh_20261029/controller33_deranged_attachment/PREDICTION.json)；[research/ddp/refresh_20261029/controller33_deranged_attachment/INPUT.json](../../research/ddp/refresh_20261029/controller33_deranged_attachment/INPUT.json)；[research/ddp/refresh_20261029/controller33_deranged_attachment/run.py](../../research/ddp/refresh_20261029/controller33_deranged_attachment/run.py)；[research/ddp/refresh_20261029/controller33_deranged_attachment/CASES.json](../../research/ddp/refresh_20261029/controller33_deranged_attachment/CASES.json)；[research/ddp/refresh_20261029/controller33_deranged_attachment/PASSERS.json](../../research/ddp/refresh_20261029/controller33_deranged_attachment/PASSERS.json)；[research/ddp/refresh_20261029/controller33_deranged_attachment/RESULT.json](../../research/ddp/refresh_20261029/controller33_deranged_attachment/RESULT.json)；[research/ddp/refresh_20261029/controller33_deranged_attachment/TERMINAL.json](../../research/ddp/refresh_20261029/controller33_deranged_attachment/TERMINAL.json)；[research/ddp/refresh_20261029/controller33_deranged_attachment/FIRST_MISSING_TWO_STEP_COUNTS.json](../../research/ddp/refresh_20261029/controller33_deranged_attachment/FIRST_MISSING_TWO_STEP_COUNTS.json)；[research/ddp/refresh_20261029/controller33_deranged_attachment/FIRST_MISSING_CAPACITY_RESULT.json](../../research/ddp/refresh_20261029/controller33_deranged_attachment/FIRST_MISSING_CAPACITY_RESULT.json)；[research/ddp/refresh_20261029/controller33_deranged_attachment/REPORT.md](../../research/ddp/refresh_20261029/controller33_deranged_attachment/REPORT.md)；[research/ddp/refresh_20261029/controller33_parallel_triangle/RAW_ANALYSIS_FIELDS.json](../../research/ddp/refresh_20261029/controller33_parallel_triangle/RAW_ANALYSIS_FIELDS.json)；[research/ddp/refresh_20261029/controller33_deranged_attachment/RAW_ANALYSIS_FIELDS.json](../../research/ddp/refresh_20261029/controller33_deranged_attachment/RAW_ANALYSIS_FIELDS.json)；[research/ddp/refresh_20261029/DERIVATION_PACKAGE.md](../../research/ddp/refresh_20261029/DERIVATION_PACKAGE.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 同一实际30点/4度controller的十个triangle×各三external-cut选择8=80，identity附着与两个固定点自由3-cycle附着160。实际只生成80+160个33/66/4regular labelled controllers，不是240张2112图或240非同构图；F5正对照另沿旧source节点，不与这里混算。

**正向保证：** 两种attachment均保所有避开三cut的旧controller路线，所有实际controller简单4regular、十一指定三角。；错位附着确实为全部480个cutpair补回三步路；此局部修复不冒完整共同覆盖。；最终拒绝由无三步且两步容量不足给出，不再只依赖单路线满秩充分证书。

**仍未完成：** 一般controller生成、其它六端点配对、内部纤维边或不同宽度关系，以及一般(16,3)仍开放；本轮没有下一自动模板队列。

**启发与重启依据：** 停止这两套固定attachment，不给已被controller容量阻断的设置续矩阵／offset／预算。下一规则须同时保被切边短路线和其它旧旧／新旧点对。原31/2760是另一已保存有限族，不改其统计；此处不排一般33controller、一般2112图或(16,3)。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

