---
type: experiment
node_id: exp:ddp-redei15-stable-triangle-twist-final-source-pools-20261028
title: "New disjoint stable triangle-twist702 orbit: D11 pool0, D12 all30 allowed-anchor completions fail"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/PREDICTION.json; research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/ERRATUM.json; research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/RESULT.json; research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/REPORT.md; research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/POOL_RESULT.json; research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/pool11.json; research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/pool12.json; research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/TERMINAL.json; research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/run.py; research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/prepare.py; research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/PREDICTION.json; research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/RESULT.json; research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/orbit.json; research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/run.py; research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/ANALYSIS_TWIST.md; research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/ANALYSIS_TWIST.json; research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/ANALYSIS_PLANE_CLOSURE.md; research/ddp/refresh_20261029/projected_guard_probe.py; research/ddp/refresh_20261029/H9_PROJECTED_GUARD_PREDICTION.md; research/ddp/refresh_20261029/H9_PROJECTED_GUARD_RESULT.json; research/ddp/refresh_20261029/H9_PROJECTED_GUARD_REPORT.md; research/ddp/refresh_20261029/ANALYSIS_PROJECTED_GUARD_REVIEW.md; research/ddp/refresh_20261029/ANALYSIS_PROJECTED_GUARD_REVIEW.json; research/ddp/refresh_20261029/RESOURCE_AND_EXISTING_DATA.md"
added: 2026-10-29T15:24:12Z
tags: ["ddp", "method-ledger"]
---

# New disjoint stable triangle-twist702 orbit: D11 pool0, D12 all30 allowed-anchor completions fail

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** new-stable-Galois-form-variant-of-successful-Redei15-mechanism

**目标与阶数：** 多目标：degree11_final37631→[11, 5]／L=37628；degree12_final42402→[12, 5]／L=42342；saved_original_exterior_vs_project_addition_guard_projection_20261029→[12, 5]／L=42342（逐变体，不合成一个距离）

**距目标的证据：** tiny确认新Galois形态真实、fixed5/pairs5、triangle1fixed、orbit702/stab8/旧orbit交0。D11完整786240原项degreepool0；D12 degreelegal167原项去重30（10pin5/11pin5/12pin20）。30均coremiss0，但current extras均不能在2/1/0预算补齐，unknown0/unvisited0/hit0/graph0。总1.793683217CPU含tiny.022166238，0sourceBFS/solver。 新投影检验30/30完成：原外围单独0可覆，新增单独10可覆（其余20预算0）；五个2guard项原外围仍0可覆，冻结存在预测REFUTED，CPU0.703871411，0新图/球/BFS/solver。1358/110是两类缺项跨case次数，distinct并集581/46，不能混为坏点对。

**其他指标（保持原计数类型）：**
```json
{
  "new_orbit_size": 702,
  "old_new_orbit_intersection": 0,
  "rational_stabilizer": 8,
  "fixed_points": 5,
  "conjugate_pairs": 5,
  "fixed_triangle_vertices": 1,
  "D11_legal_pinsets": 0,
  "D12_raw_degree_legal": 167,
  "D12_distinct_legal_pinsets": 30,
  "D12_pin_count_histogram": {
    "10": 5,
    "11": 5,
    "12": 20
  },
  "actual_current_R4_preparations": 30,
  "core_misses": 0,
  "allowed_anchor_complete_failures": 30,
  "unknown": 0,
  "unvisited": 0,
  "new_graphs": 0,
  "solver_calls": 0,
  "old_source_BFS": 0,
  "aggregate_CPU_seconds": 1.7936832169999999,
  "tiny_CPU_included_seconds": 0.022166238,
  "seed_metadata_erratum": "ERRATUM.json;actualorbitwascorrect;0rerun",
  "executed_cap0_extra_search_changed_outcomes": false,
  "new_lower_bound_mathematically_verified": false,
  "tiny_and_production_one_variant_record": true,
  "projected_guard_diagnostic": {
    "label": "saved_original_exterior_vs_project_addition_guard_projection_20261029",
    "source_n": 42402,
    "mandatory_pool_items": 30,
    "budgets_histogram": {
      "0": 20,
      "1": 5,
      "2": 5
    },
    "original_only_feasible": 0,
    "added_only_feasible": 10,
    "added_infeasible_zero_budget_cases": 20,
    "two_guard_cases": 5,
    "two_guard_original_feasible": 0,
    "completed": 30,
    "unattempted": 0,
    "prediction_verdict": "REFUTED",
    "CPU_seconds": 0.7038714110000001,
    "new_graphs": 0,
    "new_balls": 0,
    "BFS": 0,
    "solver_calls": 0,
    "scope": "Only saved current42402 eligible guard columns and original 0/1/2 budgets; newly freed guards after removal or joint rearrangement not covered."
  },
  "original_tiny_and_production_CPU_seconds": 1.7936832169999999,
  "aggregate_CPU_seconds_including_projected_guard_diagnostic": 2.497554628,
  "original_exterior_missing_occurrences_30_cases": 1358,
  "project_addition_missing_occurrences_30_cases": 110,
  "original_exterior_distinct_missing_union": 581,
  "project_addition_distinct_missing_union": 46,
  "missing_label_classification_was_posthoc_not_preregistered": true
}
```



**从属变体：**
```json
[
  {
    "label": "degree11_final37631",
    "source_m": 205329,
    "raw_occurrences": 786240,
    "legal_pinsets": 0,
    "R4_checks": 0,
    "target_Delta": 11,
    "target_D": 5,
    "target": [
      11,
      5
    ],
    "savedL": 37628,
    "source_n": 37631,
    "n": {
      "actual": null,
      "hypothetical": 37632
    }
  },
  {
    "label": "degree12_final42402",
    "source_m": 245937,
    "raw_degree_legal": 167,
    "legal_distinct_pinsets": 30,
    "pin_count_histogram": {
      "10": 5,
      "11": 5,
      "12": 20
    },
    "allowed_guard_tests": {
      "2": {
        "pool_items": 5,
        "mandatory_pin_count": 10,
        "allowed_guards": 2,
        "mandatory_missing_counts": [
          40,
          42,
          40,
          47,
          46
        ],
        "native_found_guard_sets": 0,
        "complete_allowed_guard_failure": true,
        "native_two_complete_flags": [
          true,
          true,
          true,
          true,
          true
        ]
      },
      "1": {
        "pool_items": 5,
        "mandatory_pin_count": 11,
        "allowed_guards": 1,
        "mandatory_missing_counts": [
          56,
          47,
          44,
          42,
          35
        ],
        "native_found_guard_sets": 0,
        "complete_allowed_guard_failure": true,
        "native_two_complete_flags": [
          false,
          false,
          false,
          false,
          false
        ]
      },
      "0": {
        "pool_items": 20,
        "mandatory_pin_count": 12,
        "allowed_guards": 0,
        "mandatory_missing_counts": [
          54,
          70,
          44,
          38,
          52,
          50,
          53,
          35,
          45,
          48,
          53,
          63,
          60,
          46,
          35,
          81,
          46,
          61,
          54,
          41
        ],
        "native_found_guard_sets": 0,
        "complete_allowed_guard_failure": true,
        "native_two_complete_flags": [
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false,
          false
        ]
      }
    },
    "R4_prepare_calls": 30,
    "core_misses": 0,
    "hit": 0,
    "unknown": 0,
    "unvisited": 0,
    "target_Delta": 12,
    "target_D": 5,
    "target": [
      12,
      5
    ],
    "savedL": 42342,
    "source_n": 42402,
    "n": {
      "actual": null,
      "hypothetical": 42403
    }
  },
  {
    "label": "saved_original_exterior_vs_project_addition_guard_projection_20261029",
    "target_Delta": 12,
    "target_D": 5,
    "target": [
      12,
      5
    ],
    "savedL": 42342,
    "source_n": 42402,
    "n": {
      "actual": null,
      "hypothetical": 42403
    },
    "record_type": "exact_saved_column_diagnostic_not_new_graph",
    "mandatory_pool_items": 30,
    "budgets_histogram": {
      "0": 20,
      "1": 5,
      "2": 5
    },
    "original_only_feasible": 0,
    "added_only_feasible": 10,
    "added_infeasible_zero_budget_cases": 20,
    "two_guard_cases": 5,
    "two_guard_original_feasible": 0,
    "completed": 30,
    "unattempted": 0,
    "prediction_verdict": "REFUTED",
    "CPU_seconds": 0.7038714110000001,
    "new_graphs": 0,
    "new_balls": 0,
    "BFS": 0,
    "solver_calls": 0,
    "scope": "Only saved current42402 eligible guard columns and original 0/1/2 budgets; newly freed guards after removal or joint rearrangement not covered.",
    "static_review": "research/ddp/refresh_20261029/ANALYSIS_PROJECTED_GUARD_REVIEW.md"
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/PREDICTION.json](../../research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/PREDICTION.json)；[research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/ERRATUM.json](../../research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/ERRATUM.json)；[research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/RESULT.json](../../research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/RESULT.json)；[research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/REPORT.md](../../research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/REPORT.md)；[research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/POOL_RESULT.json](../../research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/POOL_RESULT.json)；[research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/pool11.json](../../research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/pool11.json)；[research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/pool12.json](../../research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/pool12.json)；[research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/TERMINAL.json](../../research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/TERMINAL.json)；[research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/run.py](../../research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/run.py)；[research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/prepare.py](../../research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/prepare.py)；[research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/PREDICTION.json](../../research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/PREDICTION.json)；[research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/RESULT.json](../../research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/RESULT.json)；[research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/orbit.json](../../research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/orbit.json)；[research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/run.py](../../research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/run.py)；[research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/ANALYSIS_TWIST.md](../../research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/ANALYSIS_TWIST.md)；[research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/ANALYSIS_TWIST.json](../../research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/ANALYSIS_TWIST.json)；[research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/ANALYSIS_PLANE_CLOSURE.md](../../research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/ANALYSIS_PLANE_CLOSURE.md)；[research/ddp/refresh_20261029/projected_guard_probe.py](../../research/ddp/refresh_20261029/projected_guard_probe.py)；[research/ddp/refresh_20261029/H9_PROJECTED_GUARD_PREDICTION.md](../../research/ddp/refresh_20261029/H9_PROJECTED_GUARD_PREDICTION.md)；[research/ddp/refresh_20261029/H9_PROJECTED_GUARD_RESULT.json](../../research/ddp/refresh_20261029/H9_PROJECTED_GUARD_RESULT.json)；[research/ddp/refresh_20261029/H9_PROJECTED_GUARD_REPORT.md](../../research/ddp/refresh_20261029/H9_PROJECTED_GUARD_REPORT.md)；[research/ddp/refresh_20261029/ANALYSIS_PROJECTED_GUARD_REVIEW.md](../../research/ddp/refresh_20261029/ANALYSIS_PROJECTED_GUARD_REVIEW.md)；[research/ddp/refresh_20261029/ANALYSIS_PROJECTED_GUARD_REVIEW.json](../../research/ddp/refresh_20261029/ANALYSIS_PROJECTED_GUARD_REVIEW.json)；[research/ddp/refresh_20261029/RESOURCE_AND_EXISTING_DATA.md](../../research/ddp/refresh_20261029/RESOURCE_AND_EXISTING_DATA.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 新stable triangle-twist702 F3orbit（与旧702 exact不交）×既有1120stableplanes，实际accepted37631/cap11及42402/cap12；完整degree过滤后D12所有30 distinct mandatory whole-class邻域逐一full currentR4及其全部可用2/1/0 anchors精确检查。不含all-square control pool、更多F9 placements或D13。 2026-10-29追加同30组已保存完整guard列的目标投影诊断：分别只要求原外围/项目新增，保最终42402的guard域及原0/1/2预算；没有新球或旧整组覆盖复跑。

**正向保证：** New702 orbit exact disjointness from old702 is bound by the scout record.；All15point neighborhoods remain full Frobeniusclasses and have inheritedcoreR4 coverage.；Actual full-current R4 confirms every candidate covers the whole core; failure is in current extras.；All actual0/1/2anchor budgets were decided completely without a solver.；原保存guard列投影后二cover由target支持索引求交精确决定，新增单独10项各有字面guard见证；不声称联合扩张成功。

**仍未完成：** OtherGaloisforms/stableplaneF9projectivities,otherblockers or genuinely different cooperative rules. No automatic continuation.

**启发与重启依据：** 新形态保留10+s mandatorypin预算和已证明coreR4，实际extras仍是joint成败条件。局部几何与core覆盖SUPPORTED，完整extension预测REFUTED；不按漏点继续guard或其它realform。实际执行orbit与误写matrix metadata分账保ERRATUM，cap0多查无guard不影响本批结论，future-only修复不当已执行。 已保存缺项分类不是新预测；随后投影预测在计算前冻结。当前原外围已独立超出guard预算，不能再将失败只归新增60点，停止同池重排长搜。移除新增点可能释放新的端口/guards，不在该最终图缓存域内，不能因此排所有联合重排。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

