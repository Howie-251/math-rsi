---
type: experiment
node_id: exp:ddp-successful-d5-sources-ordinary-cover-route-capacity-20261029
title: "三张成功D5源的NB容量：普通cover越D6界及非平凡D5整域排除，单调扩至全部prefix"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/PREDICTION.md; research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/REPORT.md; research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/RESULT.json; research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/TERMINAL.json; research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/check.cpp; research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/run_once.py; research/ddp/refresh_20261029/SUCCESSFUL_D5_COVER_WIKI_REPORT.md; research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/independent_witnesses/CASES.txt; research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/independent_witnesses/PREDICTION.md; research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/independent_witnesses/RESULT.json; research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/independent_witnesses/WITNESSES.jsonl; research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/independent_witnesses/WITNESS_LIST.md; research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/independent_witnesses/check.cpp; research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/PREFIX_SCOPE_PROOF.md; research/ddp/refresh_20261029/COVER_MITM_D13_CALIBRATION_WIKI_REPORT.md"
added: 2026-10-29T21:49:56Z
tags: ["ddp", "method-ledger"]
---

# 三张成功D5源的NB容量：普通cover越D6界及非平凡D5整域排除，单调扩至全部prefix

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** 多目标：accepted_d5_source_11_n37631_ordinary_cover_capacity→[11, 6]／L=186033；accepted_d5_source_12_n42402_ordinary_cover_capacity→[12, 6]／L=364032；accepted_d5_source_13_n51457_ordinary_cover_capacity→[13, 6]／L=538740（逐变体，不合成一个距离）

**距目标的证据：** No cover graph generated or graph diameter measured; inherited literal sources retain their acceptedD5 status.；Actual NB<=6 witnesses0->13489:4<5,42324->796:8<9,49949->1574:2<11 (indeed excludesk>=3). Root0 NB<=5 witnesses102/53/191 eachhave count1. Three reads/five exactarc-DP roots, worker.123602CPU, compile+run.838358CPU. No sourceBFS, cover, solver, random choice or extra root. Logical106-graph scope is inherited, not recomputed.；独立MITM对6具体pair分别列尽17条NB短walk，全部匹配4/8/2和1/1/1，0.245694CPU，三source各独立读1次，无BFS或DP重跑；PREFIX_SCOPE_PROOF正式保存103prefix+3原base扩展。

**其他指标（保持原计数类型）：**
```json
{
  "computed_final_sources": 3,
  "source_literal_reads": 3,
  "actual_NB_DP_roots": 5,
  "graph_BFS_runs": 0,
  "cover_graphs_generated": 0,
  "solver_calls": 0,
  "worker_CPU_seconds": 0.123602,
  "aggregate_compile_run_CPU_seconds": 0.8383579999999998,
  "count_units": "Exact NB walks of lengths0..D from a fixed base root to a fixed target.",
  "logical_successful_prefixes": 103,
  "logical_original_public_bases": 3,
  "logical_applicable_base_graphs": 106,
  "prefix_extension_static_confirmed": true,
  "prefix_extension_new_computation": false,
  "independent_MITM_status": "PASS_ALL_SIX_WITNESSES_MATCH",
  "new_lower_bound_mathematically_verified": false,
  "complete_Lean_graph_instance": false,
  "new_graphs": 0,
  "independent_method_count_increment": 0,
  "independent_MITM_witness_pairs": 6,
  "independent_explicit_NB_walks": 17,
  "independent_MITM_source_reads": 3,
  "independent_MITM_CPU_seconds": 0.245694,
  "independent_MITM_BFS": 0,
  "independent_MITM_DP_repeats": 0
}
```



**从属变体：**
```json
[
  {
    "label": "accepted_d5_source_11_n37631_ordinary_cover_capacity",
    "target": [
      11,
      6
    ],
    "target_Delta": 11,
    "target_D": 6,
    "savedL": 186033,
    "baseline_scope": "Saved D6 comparison value frozen inPREDICTION, not a fresh global-record survey.",
    "source_n": 37631,
    "source_m": 205329,
    "source_degree_min": 6,
    "source_degree_max": 11,
    "source_literal": "research/ddp/more_graphs_20261027/h9_d11_followups/graph_d11_D5_n37631.edges",
    "required_sheets_to_exceed_saved_D6_bound": 5,
    "R6_witness": {
      "root": 0,
      "target": 13489,
      "NB_walks_through6": 4,
      "exact_length_counts": [
        0,
        0,
        0,
        0,
        1,
        1,
        2
      ]
    },
    "D6_excluded_sheets_from_witness_at_least": 5,
    "all_D6_improving_ordinary_covers_excluded": true,
    "R5_witness": {
      "root": 0,
      "target": 102,
      "NB_walks_through5": 1,
      "exact_length_counts_through5": [
        0,
        0,
        0,
        0,
        0,
        1
      ]
    },
    "D5_all_nontrivial_ordinary_covers_excluded": true,
    "actual_DP_roots": [
      0
    ],
    "source_literal_reads": 1,
    "source_D5_BFS_repeated": 0,
    "count_units": "Nonbacktracking base walks, not graph bad pairs or distinct lifted endpoints.",
    "logical_prefix_extension": {
      "successful_prefixes": 3,
      "public_base_order": 37628,
      "public_bases": 1,
      "all_witness_labels_present_in_public_base": true,
      "extension_basis": "Retained-edge prefix walk-set inclusion into final graph; no additional root or count.",
      "D6_improving_covers_excluded": true,
      "D5_nontrivial_covers_excluded": true
    },
    "cover_graphs_generated": 0,
    "solver_calls": 0,
    "independent_witness_status": "PASS_MITM_EXPLICIT_WALKS",
    "independent_witness_scope": "Only the statedR6 pair and statedroot0 R5 pair; no extra roots or full-source BFS."
  },
  {
    "label": "accepted_d5_source_12_n42402_ordinary_cover_capacity",
    "target": [
      12,
      6
    ],
    "target_Delta": 12,
    "target_D": 6,
    "savedL": 364032,
    "baseline_scope": "Saved D6 comparison value frozen inPREDICTION, not a fresh global-record survey.",
    "source_n": 42402,
    "source_m": 245937,
    "source_degree_min": 7,
    "source_degree_max": 12,
    "source_literal": "research/ddp/more_graphs_20261027/h9_redei15/production/continuation/graphs/graph_d12_D5_n42402.edges",
    "required_sheets_to_exceed_saved_D6_bound": 9,
    "R6_witness": {
      "root": 42324,
      "target": 796,
      "NB_walks_through6": 8,
      "exact_length_counts": [
        0,
        0,
        0,
        0,
        1,
        1,
        6
      ]
    },
    "D6_excluded_sheets_from_witness_at_least": 9,
    "all_D6_improving_ordinary_covers_excluded": true,
    "R5_witness": {
      "root": 0,
      "target": 53,
      "NB_walks_through5": 1,
      "exact_length_counts_through5": [
        0,
        0,
        0,
        0,
        0,
        1
      ]
    },
    "D5_all_nontrivial_ordinary_covers_excluded": true,
    "actual_DP_roots": [
      0,
      42324
    ],
    "source_literal_reads": 1,
    "source_D5_BFS_repeated": 0,
    "count_units": "Nonbacktracking base walks, not graph bad pairs or distinct lifted endpoints.",
    "logical_prefix_extension": {
      "successful_prefixes": 60,
      "public_base_order": 42342,
      "public_bases": 1,
      "all_witness_labels_present_in_public_base": true,
      "extension_basis": "Retained-edge prefix walk-set inclusion into final graph; no additional root or count.",
      "D6_improving_covers_excluded": true,
      "D5_nontrivial_covers_excluded": true
    },
    "cover_graphs_generated": 0,
    "solver_calls": 0,
    "independent_witness_status": "PASS_MITM_EXPLICIT_WALKS",
    "independent_witness_scope": "Only the statedR6 pair and statedroot0 R5 pair; no extra roots or full-source BFS."
  },
  {
    "label": "accepted_d5_source_13_n51457_ordinary_cover_capacity",
    "target": [
      13,
      6
    ],
    "target_Delta": 13,
    "target_D": 6,
    "savedL": 538740,
    "baseline_scope": "Saved D6 comparison value frozen inPREDICTION, not a fresh global-record survey.",
    "source_n": 51457,
    "source_m": 324863,
    "source_degree_min": 7,
    "source_degree_max": 13,
    "source_literal": "research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/continuation/graphs/graph_d13_D5_n51457.edges",
    "required_sheets_to_exceed_saved_D6_bound": 11,
    "R6_witness": {
      "root": 49949,
      "target": 1574,
      "NB_walks_through6": 2,
      "exact_length_counts": [
        0,
        0,
        0,
        0,
        1,
        1,
        0
      ]
    },
    "D6_excluded_sheets_from_witness_at_least": 3,
    "all_D6_improving_ordinary_covers_excluded": true,
    "R5_witness": {
      "root": 0,
      "target": 191,
      "NB_walks_through5": 1,
      "exact_length_counts_through5": [
        0,
        0,
        0,
        0,
        0,
        1
      ]
    },
    "D5_all_nontrivial_ordinary_covers_excluded": true,
    "actual_DP_roots": [
      0,
      49949
    ],
    "source_literal_reads": 1,
    "source_D5_BFS_repeated": 0,
    "count_units": "Nonbacktracking base walks, not graph bad pairs or distinct lifted endpoints.",
    "logical_prefix_extension": {
      "successful_prefixes": 40,
      "public_base_order": 51417,
      "public_bases": 1,
      "all_witness_labels_present_in_public_base": true,
      "extension_basis": "Retained-edge prefix walk-set inclusion into final graph; no additional root or count.",
      "D6_improving_covers_excluded": true,
      "D5_nontrivial_covers_excluded": true
    },
    "cover_graphs_generated": 0,
    "solver_calls": 0,
    "independent_witness_status": "PASS_MITM_EXPLICIT_WALKS",
    "independent_witness_scope": "Only the statedR6 pair and statedroot0 R5 pair; no extra roots or full-source BFS."
  }
]
```

**原始证据：** [research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/PREDICTION.md](../../research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/PREDICTION.md)；[research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/REPORT.md](../../research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/REPORT.md)；[research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/RESULT.json](../../research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/RESULT.json)；[research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/TERMINAL.json](../../research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/TERMINAL.json)；[research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/check.cpp](../../research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/check.cpp)；[research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/run_once.py](../../research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/run_once.py)；[research/ddp/refresh_20261029/SUCCESSFUL_D5_COVER_WIKI_REPORT.md](../../research/ddp/refresh_20261029/SUCCESSFUL_D5_COVER_WIKI_REPORT.md)；[research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/independent_witnesses/CASES.txt](../../research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/independent_witnesses/CASES.txt)；[research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/independent_witnesses/PREDICTION.md](../../research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/independent_witnesses/PREDICTION.md)；[research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/independent_witnesses/RESULT.json](../../research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/independent_witnesses/RESULT.json)；[research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/independent_witnesses/WITNESSES.jsonl](../../research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/independent_witnesses/WITNESSES.jsonl)；[research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/independent_witnesses/WITNESS_LIST.md](../../research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/independent_witnesses/WITNESS_LIST.md)；[research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/independent_witnesses/check.cpp](../../research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/independent_witnesses/check.cpp)；[research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/PREFIX_SCOPE_PROOF.md](../../research/ddp/refresh_20261029/successful_d5_cover_d6_capacity/PREFIX_SCOPE_PROOF.md)；[research/ddp/refresh_20261029/COVER_MITM_D13_CALIBRATION_WIKI_REPORT.md](../../research/ddp/refresh_20261029/COVER_MITM_D13_CALIBRATION_WIKI_REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Computed only three finalaccepted literals37631/42402/51457 at the five prescribed DP roots. Unique-lifting NB bounds close ordinary covers atD6 sheet thresholds5/9/3 respectively and all nontrivial k>=2 covers atD5. Static retained-edge monotonicity extends this to103 successful prefixes plus3public bases without new counting.

**正向保证：** For an ordinary k-sheet graph cover, shortest lifted paths project to NB base walks, and each base walk has a unique lift from a fixed lifted root. Thus a target with c NB walks throughD admits at mostc reachable points in its k-pointfiber, so c<k excludes diameter<=D. No regular/deck-Galois cover or regular source assumption is used.；All six witness pairs are already labeled inside their respective originalpublic bases. For every retained-edge successful prefixGi, every NB walk between those fixed labels inGi remains the same NB walk inGfinal; hence the earlier count is atmost the saved final count. Nprefix<=Nfinal means floor(L6/Nprefix)+1>=floor(L6/Nfinal)+1=5,9,11. Therefore the final-source witnesses exclude every ordinary cover of all103 accepted prefixes and3 public bases that exceeds the respective savedD6bound. The R5 counts atmost1 likewise exclude k>=2 throughout these106 logical base graphs. No106-source computation is claimed.

**仍未完成：** 数量已获独立六pair显式MITM核对。只关闭这些base/prefix的指定ordinary-cover域；改边、branched/non-cover映射、其它基图和一般D6格仍开放，无新图或Lean定理。

**启发与重启依据：** Stop ordinary covers of these sources/prefixes at the statedD5/D6 thresholds; changing sheet count, voltage group or regularity cannot evade unique path lifting. Reopening requires changing base adjacency or projection rule, e.g. a genuine non-cover construction, with its own concrete coverage question. Do not mistake these NB-walk counts for ordinary bad pairs, sampled voltage failures or all-source BFS.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

