---
type: experiment
node_id: exp:ddp-redei15-nonstable-longside-current42402-placement-20261028
title: "Rédei15 nonstable-plane longside family:64line gate passes but complete5971968-parameter degree pool empty"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_production/PREDICTION.json; research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_production/POOL_RESULT.json; research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_production/POOL12.json; research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_production/RESULT.json; research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_production/TERMINAL.json; research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_production/run.py; research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_production/prepare.py; research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/PREDICTION.json; research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/RESULT.json; research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/TERMINAL.json; research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/eligible_lines_d12.json; research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/eligible_lines_d13.json; research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/LONGSIDE_PROOF.md; research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/LONGSIDE_PROOF.json; research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/ANALYSIS_PLANE_CLOSURE.md; research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/ANALYSIS_PLANE_CLOSURE.json; research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/NONSTABLE_PLANES64.json; research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/PLANES64_RESULT.json; research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/AFFINE_PATTERNS.json; research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/affine_patterns.txt; research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/prepare_planes64.py; research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_production/REPORT.md; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/bind_source.py; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/RESULT.json; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/fold13_classes.json; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/CORE_COVER_TRANSFER.md"
added: 2026-10-28T04:49:53Z
tags: ["ddp", "method-ledger"]
---

# Rédei15 nonstable-plane longside family:64line gate passes but complete5971968-parameter degree pool empty

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** new-placement-variant-of-existing-successful-Redei15-mechanism

**目标与阶数：** 多目标：degree12_first_longside_gate→[12, 5]／L=42342；degree12_nonstable_full_projectivity_pool→[12, 5]／L=42342；degree13_complete_longside_gate_and_uniform_plane15_corollary→[13, 5]／L=51417（逐变体，不合成一个距离）

**距目标的证据：** D12首门64线非空但完整384plane pool degreelegal0，0C12/0R4/0graph/0solver。D13 cap4首门0：1764条三pair全merge且3pin全满，1876条三pair全split，无mixed；引用全局D13 fiber绑定推出更强15点plane-set界。0新sourceBFS。

**其他指标（保持原计数类型）：**
```json
{
  "actual_planes": 384,
  "projectivity_parameters_per_plane": 15552,
  "affine_masks_per_plane": 486,
  "parameter_multiplicity_per_mask": 32,
  "actual_mask_tests": 186624,
  "raw_projectivity_parameters_covered": 5971968,
  "degree_legal_neighborhoods": 0,
  "R4_calls": 0,
  "source_BFS": 0,
  "solver_calls": 0,
  "candidate_graphs": 0,
  "D13_gate_eligible": 0,
  "D13_stronger_plane15_theorem": true,
  "D12_all_nonstable_plane_Redei15_scope_closed": true,
  "sourcebound_D13_fibers_required": true,
  "oriented_D13_raw_graph_map_assumed": false,
  "checkpoint_CPU_subtotal_seconds": 0.5556526509999999,
  "CPU_accounting_note": "aggregate_CPU_seconds is the sum of recorded preparation checkpoints and the completed production process; initial gate optional-diagnostic serialization overhead after its checkpoint was not separately timed. It is not asserted as exact entire-pipeline process usage. Gate had10CPU hardlimit; all other recorded work was subsecond, far below60CPU budget.",
  "initial_gate_exit_code": 1,
  "initial_gate_failure_phase": "optional per-line numeric diagnostic serialization after RESULT and both eligible pools were already complete",
  "gate_numerical_repeat": false,
  "new_lower_bound_mathematically_verified": false,
  "record_not_independent_method_count": true
}
```



**从属变体：**
```json
[
  {
    "label": "degree12_first_longside_gate",
    "source_n": 42402,
    "source_m": 245937,
    "rational_lines": 3640,
    "closure_cap": 3,
    "eligible_lines": 64,
    "candidate_graphs": 0,
    "target_Delta": 12,
    "target_D": 5,
    "savedL": 42342,
    "target": [
      12,
      5
    ]
  },
  {
    "label": "degree12_nonstable_full_projectivity_pool",
    "source_n": 42402,
    "source_m": 245937,
    "planes": 384,
    "raw_parameters": 5971968,
    "affine_pattern_masks": 486,
    "subset_tests": 186624,
    "degree_legal_patterns": 0,
    "distinct_C12": 0,
    "R4_calls": 0,
    "candidate_graphs": 0,
    "target_Delta": 12,
    "target_D": 5,
    "savedL": 42342,
    "target": [
      12,
      5
    ]
  },
  {
    "label": "degree13_complete_longside_gate_and_uniform_plane15_corollary",
    "source_n": 51457,
    "source_m": 324863,
    "rational_lines": 3640,
    "closure_cap": 4,
    "eligible_lines": 0,
    "one_split_line_pair_was_allowed": true,
    "all3merged_lines_with_all3pins_full": 1764,
    "all3split_lines": 1876,
    "oriented_rawmap_assumed": false,
    "candidate_graphs": 0,
    "stronger_corollary_reference": "research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/ANALYSIS_PLANE_CLOSURE.md",
    "target_Delta": 13,
    "target_D": 5,
    "savedL": 51417,
    "target": [
      13,
      5
    ]
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_production/PREDICTION.json](../../research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_production/PREDICTION.json)；[research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_production/POOL_RESULT.json](../../research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_production/POOL_RESULT.json)；[research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_production/POOL12.json](../../research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_production/POOL12.json)；[research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_production/RESULT.json](../../research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_production/RESULT.json)；[research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_production/TERMINAL.json](../../research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_production/TERMINAL.json)；[research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_production/run.py](../../research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_production/run.py)；[research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_production/prepare.py](../../research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_production/prepare.py)；[research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/PREDICTION.json](../../research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/PREDICTION.json)；[research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/RESULT.json](../../research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/RESULT.json)；[research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/TERMINAL.json](../../research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/TERMINAL.json)；[research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/eligible_lines_d12.json](../../research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/eligible_lines_d12.json)；[research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/eligible_lines_d13.json](../../research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/eligible_lines_d13.json)；[research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/LONGSIDE_PROOF.md](../../research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/LONGSIDE_PROOF.md)；[research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/LONGSIDE_PROOF.json](../../research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/LONGSIDE_PROOF.json)；[research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/ANALYSIS_PLANE_CLOSURE.md](../../research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/ANALYSIS_PLANE_CLOSURE.md)；[research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/ANALYSIS_PLANE_CLOSURE.json](../../research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/ANALYSIS_PLANE_CLOSURE.json)；[research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/NONSTABLE_PLANES64.json](../../research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/NONSTABLE_PLANES64.json)；[research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/PLANES64_RESULT.json](../../research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/PLANES64_RESULT.json)；[research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/AFFINE_PATTERNS.json](../../research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/AFFINE_PATTERNS.json)；[research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/affine_patterns.txt](../../research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/affine_patterns.txt)；[research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/prepare_planes64.py](../../research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_gate/prepare_planes64.py)；[research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_production/REPORT.md](../../research/ddp/more_graphs_20261027/h9_redei15/nonstable_longside_production/REPORT.md)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/bind_source.py](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/bind_source.py)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/RESULT.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/RESULT.json)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/fold13_classes.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/fold13_classes.json)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/CORE_COVER_TRANSFER.md](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/CORE_COVER_TRANSFER.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 当前42402/cap12上所有非Frobenius稳定奇异平面中的projective Rédei15 whole-class邻域、总pins<=12：cardinality强制3内部phi pairs及完整6点longside；64合法交线×6planes×15552项目参数经486/mask精确去重，共186624实际mask tests覆盖5971968原参数。D13先全3640line cap4门，并用当前全局singleton/phi-pair绑定加强为任意单奇异平面15点whole-class总pins<=13不可合法。

**正向保证：** Standard six-point longside complement is a Baer subline, so an explicit projectivity maps it to all six nonfixed points on a rational line.；Whole-class closure gives orientation-free inheritedcoreR4 for any legal complete blocking set.；The normalized24×8×81 projectivities exhaust the fixed longside footprint in each selected plane.；The firstline gate was implemented withcap4 for degree13, not the incomplete all-three-merge-only subgate.；Cardinality forces every legal D12 nonstable-plane Rédei15 wholeclosure into the completed six-point-longside family; this is not only an arbitrary selected footprint.

**仍未完成：** 稳定plane的任意PGL3(F9) placements、其它blockers、少于15raw点、multi-plane或实质不同协作规则未被该结论排除；不自动执行。

**启发与重启依据：** 非稳定几何和完整projectivity域确实存在，首门非空不保证off-line9类能同时unsplit/free。D12本非稳定plane Rédei15 wholeclosure族已完整关闭；不续anchors/planes。D13强结论依赖实际全局fiber绑定与全3640line统计，不借旧12map或未恢复orientation。

**单独的重启条件：** This finite placement scope is complete; no automatic extra affine maps, planes, anchors or changedsource retry from the empty pool.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

