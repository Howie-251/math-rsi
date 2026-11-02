---
type: experiment
node_id: exp:ddp-current650-critical-middle-fivecut-hub-gate-10d3-20261027
title: "Source650 full endpoint-hub insertion with at most five cuts excluded by complete forced-pin search"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/REPORT.md; research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/PREDICTION.json; research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/RESULT.json; research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/STRUCTURE_ROOT.json; research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/EDGE_CRITICAL_MATCHINGS.jsonl; research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/WALK_COUNT_SCHEMA.json; research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/A2.u16le.bin; research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/A3.u16le.bin; research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/critical.cpp; research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/run.py; research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/RUN_RECEIPT.json; research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/terminal.json; research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/REPORT.md; research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/PREDICTION.json; research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/RESULT.json; research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/NATIVE_RESULT.json; research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/search.cpp; research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/run.py; research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/cached_edge_critical_input.txt; research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/ACTUAL_CASES.jsonl; research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/checkpoint.json; research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/RUN_HANDLE.json; research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/ANALYSIS_PROOF.md; research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/ANALYSIS_RESULT.json"
added: 2026-10-27T23:51:32Z
tags: ["ddp", "method-ledger"]
---

# Source650 full endpoint-hub insertion with at most five cuts excluded by complete forced-pin search

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-exact-constraint-exclusion

**目标与阶数：** (10,3)；L=650；条件性n=651（未据此计纪录）

**距目标的证据：** Earlier critical matching prediction allFF9 was refuted (1952 forbidden /128 unexcluded). Follow-up exhaustively enumerated128 anchors,4 size7 covers+274 size8,2820 per-anchor deduplicated endpoint sets.260 sets pass full oldR2 coverage;0 five-edge realizations contain the anchor and satisfy every cut critical constraint. Therefore the exact <=5-cut/all-endpoints singlehub family has no valid651/D3 graph.0 modified graphs/BFS or solver.

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 650,
  "source_m": 3250,
  "source_D_inherited": 3,
  "P_vertices": 130,
  "F_vertices": 520,
  "port_twin_pairs_sharing_eight_F_neighbors": 65,
  "source_edge_types": {
    "FF": 2080,
    "FP": 1040,
    "PP": 130
  },
  "matching_histograms": {
    "FF": {
      "0": 0,
      "1": 0,
      "2": 0,
      "3": 0,
      "4": 0,
      "5": 0,
      "6": 0,
      "7": 2,
      "8": 126,
      "9": 1952
    },
    "FP": {
      "0": 1040,
      "1": 0,
      "2": 0,
      "3": 0,
      "4": 0,
      "5": 0,
      "6": 0,
      "7": 0,
      "8": 0,
      "9": 0
    },
    "PP": {
      "0": 130,
      "1": 0,
      "2": 0,
      "3": 0,
      "4": 0,
      "5": 0,
      "6": 0,
      "7": 0,
      "8": 0,
      "9": 0
    }
  },
  "first_unexcluded_FF": [
    1,
    9,
    8
  ],
  "first_matching7_FF": [
    16,
    132,
    7
  ],
  "inherited_endpoint_R2_P_union_max": {
    "FF": 40,
    "FP": 24,
    "PP": 8
  },
  "prediction": "REFUTED",
  "complete_walk_counts": {
    "length2_row_sum": 100,
    "length3_row_sum": 1000,
    "walk_type": "ordinary walks; not distances or NB routes"
  },
  "source_distance_BFS_count": 0,
  "modified_graphs": 0,
  "modified_BFS_count": 0,
  "solver_calls": 0,
  "native_CPU_seconds": 0.02883,
  "total_parent_children_CPU_seconds_excluding_inherited_root_structure": 0.8167302740000001,
  "inherited_root_structure_CPU_seconds": 0.026184923,
  "new_lower_bounds": 0,
  "untested_source_edges": 0,
  "UNKNOWN_source_edges": 0,
  "critical_stage_prediction": "REFUTED",
  "forced_cover_stage_prediction": "REFUTED",
  "forced_cover_stage": {
    "status": "COMPLETE_FIXED_FAMILY_NO_HIT",
    "hit": false,
    "complete": true,
    "anchors_total": 128,
    "size7_base_covers": 4,
    "size8_base_covers": 274,
    "anchor_endpoint_sets_after_per_anchor_dedup": 2820,
    "endpoint_sets_passing_full_R2": 260,
    "actual_distinct_cutsets": 0,
    "duplicate_cutsets_skipped": 0,
    "modified_hub_R3_passes": 0,
    "modified_R3_root_checks": 0,
    "CPU_seconds": 0.035215,
    "source_BFS": 0,
    "A2_or_A3_recomputation": 0,
    "ordinary_unordered_bad_pairs": null,
    "receipt": {
      "exit_code": 0,
      "compile_CPU_seconds": 1.214182,
      "native_process_CPU_seconds": 0.03683699999999979,
      "driver_CPU_seconds": 0.035775769
    }
  },
  "complete_fixed_family": true,
  "followup_native_CPU_seconds": 0.035215,
  "followup_total_parent_children_CPU_seconds": 1.286794769
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/REPORT.md](../../research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/REPORT.md)；[research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/PREDICTION.json](../../research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/PREDICTION.json)；[research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/RESULT.json](../../research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/RESULT.json)；[research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/STRUCTURE_ROOT.json](../../research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/STRUCTURE_ROOT.json)；[research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/EDGE_CRITICAL_MATCHINGS.jsonl](../../research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/EDGE_CRITICAL_MATCHINGS.jsonl)；[research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/WALK_COUNT_SCHEMA.json](../../research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/WALK_COUNT_SCHEMA.json)；[research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/A2.u16le.bin](../../research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/A2.u16le.bin)；[research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/A3.u16le.bin](../../research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/A3.u16le.bin)；[research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/critical.cpp](../../research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/critical.cpp)；[research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/run.py](../../research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/run.py)；[research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/RUN_RECEIPT.json](../../research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/RUN_RECEIPT.json)；[research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/terminal.json](../../research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/terminal.json)；[research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/REPORT.md](../../research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/REPORT.md)；[research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/PREDICTION.json](../../research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/PREDICTION.json)；[research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/RESULT.json](../../research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/RESULT.json)；[research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/NATIVE_RESULT.json](../../research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/NATIVE_RESULT.json)；[research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/search.cpp](../../research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/search.cpp)；[research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/run.py](../../research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/run.py)；[research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/cached_edge_critical_input.txt](../../research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/cached_edge_critical_input.txt)；[research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/ACTUAL_CASES.jsonl](../../research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/ACTUAL_CASES.jsonl)；[research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/checkpoint.json](../../research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/checkpoint.json)；[research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/RUN_HANDLE.json](../../research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/RUN_HANDLE.json)；[research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/ANALYSIS_PROOF.md](../../research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/ANALYSIS_PROOF.md)；[research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/ANALYSIS_RESULT.json](../../research/ddp/more_graphs_20261027/d10_D3_current650_critical_middle_gate/forced_pin_cover_search/ANALYSIS_RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** One hub adjacent to ALL distinct endpoints of 1..5 deleted old edges; all other old edges retained; no other added edges. No exclusion of arbitrary 651-vertex graphs.

**仍未完成：** Other651 graphs, more than five cut edges, additional helpers, omitted endpoint spokes, and different rewiring rules are not excluded. This is not a general upper bound on N(10,3).

**启发与重启依据：** The first critical test did not close the family; its128 real exceptions gave a complete forced-cover enumeration rather than a blind hub search. OldR2 coverage alone has260 passers but none is realizable by the required five critical-compatible cuts. This exact family is closed; a restart requires a materially different insertion rule, not another seed or more time.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

