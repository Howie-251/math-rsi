---
type: experiment
node_id: exp:ddp-h9-qline-d12-family-42377
title: "完整新图族：(12,5)42343–42402，共60个阶数"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/h9_d12_global_extensions/REPORT.md; research/ddp/more_graphs_20261027/h9_d12_global_extensions/graphs/graph_d12_D5_n42377.edges; research/ddp/more_graphs_20261027/h9_d12_global_extensions/graphs/independent_all_source_BFS_42377.json; research/ddp/more_graphs_20261027/h9_d12_global_extensions/root_sequential_R4_checks.json; research/ddp/more_graphs_20261027/h9_d12_global_extensions/accepted_extensions.json; research/ddp/more_graphs_20261027/FINAL_RESULTS_PROOF.md; research/ddp/more_graphs_20261027/BASELINES_REFRESH.json; research/ddp/more_graphs_20261027/delivery/README.md; research/ddp/more_graphs_20261027/delivery/families.json; reviews/ddp/more_graphs_20261027.raw.json; research/ddp/more_graphs_20261027/h9_d12_global_remainder/REPORT.md; research/ddp/more_graphs_20261027/h9_d12_global_remainder/accepted_extensions.json; research/ddp/more_graphs_20261027/h9_d12_global_remainder/graphs/graph_d12_D5_n42391.edges; research/ddp/more_graphs_20261027/h9_d12_changed_base_round2/REPORT.md; research/ddp/more_graphs_20261027/h9_d12_changed_base_round2/RESULT.json; research/ddp/more_graphs_20261027/h9_d12_eightpin_constructive/REPORT.md; research/ddp/more_graphs_20261027/h9_d12_eightpin_constructive/RESULT.json; research/ddp/more_graphs_20261027/h9_d12_eightpin_constructive/graphs/graph_d12_D5_n42396.edges; research/ddp/more_graphs_20261027/h9_d12_native_changed_base/RESULT.json; research/ddp/more_graphs_20261027/h9_d12_native_changed_base/REPORT.md; research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/REPORT.md; research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/RESULT.json; research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/graphs/graph_d12_D5_n42397.edges; research/ddp/more_graphs_20261027/h9_d12_ninepin_coreguard/REPORT.md; research/ddp/more_graphs_20261027/h9_d12_ninepin_coreguard/RESULT.json; research/ddp/more_graphs_20261027/h9_baer_plane_extensions/graphs/graph_d12_D5_n42398.edges; research/ddp/more_graphs_20261027/h9_baer_plane_pool/THEOREM.md; research/ddp/more_graphs_20261027/h9_baer_plane_pool/REPORT.md; research/ddp/more_graphs_20261027/h9_baer_plane_extensions/REPORT.md; research/ddp/more_graphs_20261027/h9_baer_plane_extensions/RESULT.json; research/ddp/more_graphs_20261027/h9_baer_plane_extensions/independent_first_new_root.json; research/ddp/more_graphs_20261027/h9_redei15/production/accepted_sequence.json; research/ddp/more_graphs_20261027/h9_redei15/theory/PROOF.md; research/ddp/more_graphs_20261027/h9_redei15/production/independent_newroot42399.json; reviews/ddp/redei15_20261027.DISPOSITION.md"
added: 2026-10-27T17:10:44Z
tags: ["ddp", "method-ledger"]
---

# 完整新图族：(12,5)42343–42402，共60个阶数

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (12,5)；L=42342；candidate_graph_or_family n=42402

**距目标的证据：** 实际D=5，目标D=5；Every literal step has complete production degree/current-baseR4 coverage. Representative42377 has saved all-source BFS; later graphs accepted by induction without repeat BFS.；最强42402/m245937/max12/D5，共60阶数。新Rédei15机制产生最后4图；首步42399 fresh edge-file new-root检查通过，其余完整currentR4归纳，无重复old全BFS。

**其他指标（保持原计数类型）：**
```json
{
  "new_lower_bound_mathematically_verified": true,
  "improved_parameter_pair": [
    12,
    5
  ],
  "example_orders": [
    42343,
    42344,
    42345,
    42346,
    42347,
    42348,
    42349,
    42350,
    42351,
    42352,
    42353,
    42354,
    42355,
    42356,
    42357,
    42358,
    42359,
    42360,
    42361,
    42362,
    42363,
    42364,
    42365,
    42366,
    42367,
    42368,
    42369,
    42370,
    42371,
    42372,
    42373,
    42374,
    42375,
    42376,
    42377,
    42378,
    42379,
    42380,
    42381,
    42382,
    42383,
    42384,
    42385,
    42386,
    42387,
    42388,
    42389,
    42390,
    42391,
    42392,
    42393,
    42394,
    42395,
    42396,
    42397,
    42398,
    42399,
    42400,
    42401,
    42402
  ],
  "example_count": 60,
  "strongest_n": 42402,
  "strongest_m": 245937,
  "public_baseline": 42342,
  "improvement": 60,
  "roots_checked": 0,
  "all_source_check_CPU_seconds": 60.4583,
  "all_source_check_wall_seconds": 15.1431,
  "Lean_complete": false,
  "complete_Lean_instances": 0,
  "Goal_complete": false,
  "public_submission": false,
  "source_author": "Dharunish Yugeswardeenoo; underlying partial-fold/duality Rishabh Rajiv",
  "prefix_validation": "Complete current-base degree/R4 production induction; strongest does not have a new all-source scan.",
  "family_generator": "research/ddp/more_graphs_20261027/delivery/family_generator.py",
  "global_degree_pool": 609,
  "global_10pin_new_scope": 592,
  "global_10pin_processed": 592,
  "accepted_in_last_batch": 0,
  "unattempted_10pin": 0,
  "unattempted_8pin": 0,
  "failed_earlier_items_retried": true,
  "original_7_retested": true,
  "final_batch_review_status": "SUCCESS",
  "actual_reviewer_model": "gemini-3.8-flash-high",
  "actual_reviewer_effort": "high",
  "latest_wholegraph_BFS_executed": false,
  "last_allsource_order": 42377,
  "guaranteed_bad_pairs_by_complete_induction": 0,
  "latest14_review_executed": false,
  "prior_review_scope_examples": 38,
  "global_10pin_unattempted": 0,
  "production_remainder_scope": 225,
  "production_remainder_hits": 14,
  "source_graph_reverified": false,
  "latest_examples_review_executed": true,
  "round2_frozen_scope": 371,
  "round2_hits": 1,
  "round2_exact_failures_at_recorded_base": 311,
  "round2_current_item_UNKNOWN": 1,
  "round2_unattempted": 58,
  "eightpin_constructive_scope": 13,
  "eightpin_constructive_hits": 4,
  "eightpin_constructive_degree_blocked": 7,
  "eightpin_constructive_no_hit": 2,
  "eightpin_constructive_CPU_seconds": 10.39475236,
  "original_7_retested_indices": [
    2,
    3
  ],
  "initial_global_batch_exact_failures": 280,
  "initial_global_batch_degree_rejected": 55,
  "native_changed_base_batch": {
    "status": "ALL_FROZEN_ITEMS_TERMINAL",
    "initial_n": 42396,
    "initial_m": 245865,
    "final_n": 42396,
    "final_m": 245865,
    "frozen_candidates": 350,
    "rows_attempted": 350,
    "items_unattempted": 0,
    "complete_items": 350,
    "unknown_items": 0,
    "accepted_extensions": 0,
    "final_graph": "research/ddp/more_graphs_20261027/h9_d12_eightpin_constructive/graphs/graph_d12_D5_n42396.edges",
    "native_prepare_calls": 350,
    "native_selected_R4_calls": 0,
    "CPU_parent_and_all_children_seconds": 23.578617641000005,
    "CPU_accounting": "Freeze parent plus runningparent and every native child; delivery child added below",
    "Python_reverse_target_BFS": 0,
    "MIP_calls": 0,
    "allsource_BFS": 0,
    "externalreview": 0,
    "pending": [],
    "row_status_counts": {
      "EXACT_NO_AT_MOST_TWO_ANCHORS": 350
    },
    "samebase_prior_failures_repeated": false,
    "failed_current_batch_items_retried": false,
    "general_family_excluded": false,
    "freeze_summary": {
      "source_n": 42396,
      "source_m": 245865,
      "universe596": 596,
      "samebase_skipped": 0,
      "currentdegree_skipped_after_samebase": 246,
      "frozen_candidates": 350,
      "prior_accepted_line_copy_candidates": 0,
      "prepare_CPU_seconds": 0.13720159,
      "coverage_checks": 0
    },
    "new_graphs_generated": 0,
    "new_lower_bounds": 0,
    "delivery_modified": false,
    "fixed42396_full_tenpin_Qline_atmost2_scope_closed": true,
    "closure_reason": "Samebase remained42396;246currentdegreeinfeasible plus350completeexact<=2failures cover all596originaltenpin classes. Degreeonlyincreases, so originallyinfeasiblelines cannot enter the pool.",
    "eightpin_family_excluded": false,
    "report": "REPORT.md"
  },
  "current42396_10pin_pool_closed": true,
  "current42396_exact_two_failures": 350,
  "current42396_degree_blocked_10pin_sets": 246,
  "latest_review_scope": "New Redei15 theorem and four extensions; accepted with85-count arithmetic correction"
}
```



**从属变体：**
```json
[
  {
    "order": 42343,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": true
  },
  {
    "order": 42344,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42345,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": true
  },
  {
    "order": 42346,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42347,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42348,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42349,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42350,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42351,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42352,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42353,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42354,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42355,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42356,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42357,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42358,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42359,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42360,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42361,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42362,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42363,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42364,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42365,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42366,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42367,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42368,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42369,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42370,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42371,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42372,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42373,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42374,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42375,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42376,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42377,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": true
  },
  {
    "order": 42378,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42379,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42380,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42381,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42382,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42383,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42384,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42385,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42386,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42387,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42388,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42389,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42390,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42391,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42392,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42393,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42394,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42395,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42396,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42397,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42398,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42399,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42400,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42401,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  },
  {
    "order": 42402,
    "D5_by_complete_induction": true,
    "not_independent_method": true,
    "allsource_BFS_here": false
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/h9_d12_global_extensions/REPORT.md](../../research/ddp/more_graphs_20261027/h9_d12_global_extensions/REPORT.md)；[research/ddp/more_graphs_20261027/h9_d12_global_extensions/graphs/graph_d12_D5_n42377.edges](../../research/ddp/more_graphs_20261027/h9_d12_global_extensions/graphs/graph_d12_D5_n42377.edges)；[research/ddp/more_graphs_20261027/h9_d12_global_extensions/graphs/independent_all_source_BFS_42377.json](../../research/ddp/more_graphs_20261027/h9_d12_global_extensions/graphs/independent_all_source_BFS_42377.json)；[research/ddp/more_graphs_20261027/h9_d12_global_extensions/root_sequential_R4_checks.json](../../research/ddp/more_graphs_20261027/h9_d12_global_extensions/root_sequential_R4_checks.json)；[research/ddp/more_graphs_20261027/h9_d12_global_extensions/accepted_extensions.json](../../research/ddp/more_graphs_20261027/h9_d12_global_extensions/accepted_extensions.json)；[research/ddp/more_graphs_20261027/FINAL_RESULTS_PROOF.md](../../research/ddp/more_graphs_20261027/FINAL_RESULTS_PROOF.md)；[research/ddp/more_graphs_20261027/BASELINES_REFRESH.json](../../research/ddp/more_graphs_20261027/BASELINES_REFRESH.json)；[research/ddp/more_graphs_20261027/delivery/README.md](../../research/ddp/more_graphs_20261027/delivery/README.md)；[research/ddp/more_graphs_20261027/delivery/families.json](../../research/ddp/more_graphs_20261027/delivery/families.json)；[reviews/ddp/more_graphs_20261027.raw.json](../../reviews/ddp/more_graphs_20261027.raw.json)；[research/ddp/more_graphs_20261027/h9_d12_global_remainder/REPORT.md](../../research/ddp/more_graphs_20261027/h9_d12_global_remainder/REPORT.md)；[research/ddp/more_graphs_20261027/h9_d12_global_remainder/accepted_extensions.json](../../research/ddp/more_graphs_20261027/h9_d12_global_remainder/accepted_extensions.json)；[research/ddp/more_graphs_20261027/h9_d12_global_remainder/graphs/graph_d12_D5_n42391.edges](../../research/ddp/more_graphs_20261027/h9_d12_global_remainder/graphs/graph_d12_D5_n42391.edges)；[research/ddp/more_graphs_20261027/h9_d12_changed_base_round2/REPORT.md](../../research/ddp/more_graphs_20261027/h9_d12_changed_base_round2/REPORT.md)；[research/ddp/more_graphs_20261027/h9_d12_changed_base_round2/RESULT.json](../../research/ddp/more_graphs_20261027/h9_d12_changed_base_round2/RESULT.json)；[research/ddp/more_graphs_20261027/h9_d12_eightpin_constructive/REPORT.md](../../research/ddp/more_graphs_20261027/h9_d12_eightpin_constructive/REPORT.md)；[research/ddp/more_graphs_20261027/h9_d12_eightpin_constructive/RESULT.json](../../research/ddp/more_graphs_20261027/h9_d12_eightpin_constructive/RESULT.json)；[research/ddp/more_graphs_20261027/h9_d12_eightpin_constructive/graphs/graph_d12_D5_n42396.edges](../../research/ddp/more_graphs_20261027/h9_d12_eightpin_constructive/graphs/graph_d12_D5_n42396.edges)；[research/ddp/more_graphs_20261027/h9_d12_native_changed_base/RESULT.json](../../research/ddp/more_graphs_20261027/h9_d12_native_changed_base/RESULT.json)；[research/ddp/more_graphs_20261027/h9_d12_native_changed_base/REPORT.md](../../research/ddp/more_graphs_20261027/h9_d12_native_changed_base/REPORT.md)；[research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/REPORT.md](../../research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/REPORT.md)；[research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/RESULT.json](../../research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/RESULT.json)；[research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/graphs/graph_d12_D5_n42397.edges](../../research/ddp/more_graphs_20261027/h9_d12_ninepin_saturated_deletion/graphs/graph_d12_D5_n42397.edges)；[research/ddp/more_graphs_20261027/h9_d12_ninepin_coreguard/REPORT.md](../../research/ddp/more_graphs_20261027/h9_d12_ninepin_coreguard/REPORT.md)；[research/ddp/more_graphs_20261027/h9_d12_ninepin_coreguard/RESULT.json](../../research/ddp/more_graphs_20261027/h9_d12_ninepin_coreguard/RESULT.json)；[research/ddp/more_graphs_20261027/h9_baer_plane_extensions/graphs/graph_d12_D5_n42398.edges](../../research/ddp/more_graphs_20261027/h9_baer_plane_extensions/graphs/graph_d12_D5_n42398.edges)；[research/ddp/more_graphs_20261027/h9_baer_plane_pool/THEOREM.md](../../research/ddp/more_graphs_20261027/h9_baer_plane_pool/THEOREM.md)；[research/ddp/more_graphs_20261027/h9_baer_plane_pool/REPORT.md](../../research/ddp/more_graphs_20261027/h9_baer_plane_pool/REPORT.md)；[research/ddp/more_graphs_20261027/h9_baer_plane_extensions/REPORT.md](../../research/ddp/more_graphs_20261027/h9_baer_plane_extensions/REPORT.md)；[research/ddp/more_graphs_20261027/h9_baer_plane_extensions/RESULT.json](../../research/ddp/more_graphs_20261027/h9_baer_plane_extensions/RESULT.json)；[research/ddp/more_graphs_20261027/h9_baer_plane_extensions/independent_first_new_root.json](../../research/ddp/more_graphs_20261027/h9_baer_plane_extensions/independent_first_new_root.json)；[research/ddp/more_graphs_20261027/h9_redei15/production/accepted_sequence.json](../../research/ddp/more_graphs_20261027/h9_redei15/production/accepted_sequence.json)；[research/ddp/more_graphs_20261027/h9_redei15/theory/PROOF.md](../../research/ddp/more_graphs_20261027/h9_redei15/theory/PROOF.md)；[research/ddp/more_graphs_20261027/h9_redei15/production/independent_newroot42399.json](../../research/ddp/more_graphs_20261027/h9_redei15/production/independent_newroot42399.json)；[reviews/ddp/redei15_20261027.DISPOSITION.md](../../reviews/ddp/redei15_20261027.DISPOSITION.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Literal extension sequence from public42342; every integer42343..42402 is a fullD5 graph. Includes Q-line, Baer13 and Rédei15 neighborhoods.

**正向保证：** Each accepted full neighbor set has distinct vertices and free current degree slots.；Complete R4 is checked in the actual immediately preceding graph, including all earlier additions.；Retaining all old edges and adding this full neighbor set proves D<=5 inductively; the Moore D4 bound gives exactD5.；Literal generator reproduces the current strongest edge set; representative42377 has the saved independent all-source check.

**仍未完成：** Complete concrete Lean instances remain unfinished. Earlier failures are scoped to their actual bases; no family maximality claim.

**启发与重启依据：** UNKNOWN is not infeasible. Eight-pin sets plus four anchors produced complete graphs using greedy two-prefix/exact-two-tail search on the changed base. Changed base and changed algorithm effects are not separated; no old-base feasibility claim. Current42396 full596 ten-pin pool:246 degree-blocked and350 exact<=two-anchor failures. Do not repeat this same-base pool. Two remaining eight-pin cases are not excluded.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

