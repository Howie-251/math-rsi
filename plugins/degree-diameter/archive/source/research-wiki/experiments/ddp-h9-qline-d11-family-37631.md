---
type: experiment
node_id: exp:ddp-h9-qline-d11-family-37631
title: "完整新图族：(11,5)各阶37629–37631，最强37631全源验收"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/h9_other_degrees/REPORT.md; research/ddp/more_graphs_20261027/h9_d11_followups/REPORT.md; research/ddp/more_graphs_20261027/h9_d11_followups/graph_d11_D5_n37631.edges; research/ddp/more_graphs_20261027/h9_d11_followups/independent_all_source_BFS_37631.json; research/ddp/more_graphs_20261027/h9_d11_followups/root_sequential_R4_checks.json; research/ddp/more_graphs_20261027/h9_other_degrees/mapping11_result.json; research/ddp/more_graphs_20261027/h9_core_quotient_capacity/REPORT.md; research/ddp/more_graphs_20261027/FINAL_RESULTS_PROOF.md; research/ddp/more_graphs_20261027/BASELINES_REFRESH.json; research/ddp/more_graphs_20261027/delivery/README.md; research/ddp/more_graphs_20261027/delivery/families.json; reviews/ddp/more_graphs_20261027.raw.json; research/ddp/more_graphs_20261027/h9_d11_changed_base_retries/REPORT.md; research/ddp/more_graphs_20261027/h9_d11_two_qline_block/REPORT.md; research/ddp/more_graphs_20261027/h9_d11_shared_anchor_block/REPORT.md"
added: 2026-10-27T12:06:15Z
tags: ["ddp", "method-ledger"]
---

# 完整新图族：(11,5)各阶37629–37631，最强37631全源验收

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (11,5)；L=37628；candidate_graph_or_family n=37631

**距目标的证据：** 实际D=5，目标D=5；普通无序坏对=0；Strongest37631: root all37631-source ordinary BFS. Every prefix separately has root earlier-graph R4 induction certificate; not inferred by deleting vertices.；最强n37631/m205329/max11/D5/全37631根bad0。各整数阶前缀有独立完整earlier-R4证据；共3例，公开基线37628，最强提升3。Lean完整实例未完成。

**其他指标（保持原计数类型）：**
```json
{
  "new_lower_bound_mathematically_verified": true,
  "improved_parameter_pair": [
    11,
    5
  ],
  "example_orders": [
    37629,
    37630,
    37631
  ],
  "example_count": 3,
  "strongest_n": 37631,
  "strongest_m": 205329,
  "public_baseline": 37628,
  "improvement": 3,
  "roots_checked": 37631,
  "all_source_check_CPU_seconds": 41.0824,
  "all_source_check_wall_seconds": 10.2909,
  "Lean_complete": false,
  "complete_Lean_instances": 0,
  "Goal_complete": false,
  "public_submission": false,
  "source_author": "Dharunish Yugeswardeenoo; underlying partial-fold/duality Rishabh Rajiv",
  "prefix_validation": "Independent complete new-old R4 plus retained old-old routes; strongest has all-source BFS",
  "family_generator": "research/ddp/more_graphs_20261027/delivery/family_generator.py",
  "global_original_lines": 5380830,
  "global_degree_feasible_10pin_sets": 24,
  "first_hit_pool_index": 3,
  "subsequent_scope_items": 20,
  "subsequent_hits": 2,
  "old_first3_failed_not_retried": true,
  "current_split_fibers": 4074,
  "old_witness_split_fibers": 3075,
  "old_current_split_intersection": 305,
  "core_WL_classes": 33397,
  "core_WL_pairs": 4074,
  "core_WL_singletons": 29323,
  "fixed_d12_core_only_quotient_degree_invariant_extras": 672,
  "final_batch_review_status": "SUCCESS",
  "actual_reviewer_model": "gemini-3.8-flash-high",
  "actual_reviewer_effort": "high",
  "current_base_37631_all_remaining_single_Qline_oneanchor_closed": true,
  "pure_adjacent_2Qline_pairs_tested": 210,
  "pure_adjacent_2Qline_hits": 0,
  "shared_old_anchor_pairs_tested": 210,
  "shared_anchor_hits": 0
}
```



**从属变体：**
```json
[
  {
    "order": 37629,
    "degree": 11,
    "D5_by_complete_induction": true,
    "allsource_BFS_here": false,
    "not_independent_method": true
  },
  {
    "order": 37630,
    "degree": 11,
    "D5_by_complete_induction": true,
    "allsource_BFS_here": false,
    "not_independent_method": true
  },
  {
    "order": 37631,
    "degree": 11,
    "D5_by_complete_induction": true,
    "allsource_BFS_here": true,
    "not_independent_method": true
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/h9_other_degrees/REPORT.md](../../research/ddp/more_graphs_20261027/h9_other_degrees/REPORT.md)；[research/ddp/more_graphs_20261027/h9_d11_followups/REPORT.md](../../research/ddp/more_graphs_20261027/h9_d11_followups/REPORT.md)；[research/ddp/more_graphs_20261027/h9_d11_followups/graph_d11_D5_n37631.edges](../../research/ddp/more_graphs_20261027/h9_d11_followups/graph_d11_D5_n37631.edges)；[research/ddp/more_graphs_20261027/h9_d11_followups/independent_all_source_BFS_37631.json](../../research/ddp/more_graphs_20261027/h9_d11_followups/independent_all_source_BFS_37631.json)；[research/ddp/more_graphs_20261027/h9_d11_followups/root_sequential_R4_checks.json](../../research/ddp/more_graphs_20261027/h9_d11_followups/root_sequential_R4_checks.json)；[research/ddp/more_graphs_20261027/h9_other_degrees/mapping11_result.json](../../research/ddp/more_graphs_20261027/h9_other_degrees/mapping11_result.json)；[research/ddp/more_graphs_20261027/h9_core_quotient_capacity/REPORT.md](../../research/ddp/more_graphs_20261027/h9_core_quotient_capacity/REPORT.md)；[research/ddp/more_graphs_20261027/FINAL_RESULTS_PROOF.md](../../research/ddp/more_graphs_20261027/FINAL_RESULTS_PROOF.md)；[research/ddp/more_graphs_20261027/BASELINES_REFRESH.json](../../research/ddp/more_graphs_20261027/BASELINES_REFRESH.json)；[research/ddp/more_graphs_20261027/delivery/README.md](../../research/ddp/more_graphs_20261027/delivery/README.md)；[research/ddp/more_graphs_20261027/delivery/families.json](../../research/ddp/more_graphs_20261027/delivery/families.json)；[reviews/ddp/more_graphs_20261027.raw.json](../../reviews/ddp/more_graphs_20261027.raw.json)；[research/ddp/more_graphs_20261027/h9_d11_changed_base_retries/REPORT.md](../../research/ddp/more_graphs_20261027/h9_d11_changed_base_retries/REPORT.md)；[research/ddp/more_graphs_20261027/h9_d11_two_qline_block/REPORT.md](../../research/ddp/more_graphs_20261027/h9_d11_two_qline_block/REPORT.md)；[research/ddp/more_graphs_20261027/h9_d11_shared_anchor_block/REPORT.md](../../research/ddp/more_graphs_20261027/h9_d11_shared_anchor_block/REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixed literal Q-line/anchor extension sequence from the public37628 graph; alloldedges retained; complete examples at every order37629..37631. Strongest expanded edge list independently all-source checked.

**正向保证：** Every new point has a distinct complete neighbor set; every affected olddegree had a free slot.；Root independently checked each complete current-base radius4 cover before adding future vertices.；Strongest graph rebuilt from edge list: simple,connected,max11,exactD5,all37631roots,0badpairs.；Literal family generator dry-run exactly matches the strongest verified edge set; no search is needed to reproduce a prefix.

**仍未完成：** 数学构造、完整覆盖与最强图独立全源验收已完成，Gemini同线程批次审阅SUCCESS；完整Lean仍0，未宣称最优或公开接收。

**启发与重启依据：** 几何规则自动处理全部旧核心，剩余degree与extras覆盖作有界精确完成。只接受完整新图，不按坏对下降续轮；未试候选和当时base拒绝范围分开保留。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

