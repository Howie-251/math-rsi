---
type: experiment
node_id: exp:ddp-wave11-gq-internal-capacity
title: "GQ内部图平均容量：全47参数、正则奇偶与max-degree边界"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave11/gq_internal_capacity/REPORT.md; research/ddp/breadth_20261027_wave11/gq_internal_capacity/RESULT.json; research/ddp/breadth_20261027_wave11/gq_internal_capacity/terminal.json; research/ddp/breadth_20261027_wave11/gq_internal_capacity/screen.py; reviews/ddp/wave11_scoped_review_20261027.json"
added: 2026-10-27T08:25:53Z
tags: ["ddp", "method-ledger"]
---

# GQ内部图平均容量：全47参数、正则奇偶与max-degree边界

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** necessary-capacity-screen

**目标与阶数：** 多目标：q2-r0→[3, 3]／L=None；q2-r1→[4, 3]／L=41；q2-r2→[5, 3]／L=72；q2-r3→[6, 3]／L=120；q2-r4→[7, 3]／L=170；q2-r5→[8, 3]／L=253；q2-r6→[9, 3]／L=585；q2-r7→[10, 3]／L=650；q2-r8→[11, 3]／L=715；q2-r9→[12, 3]／L=810；q3-r0→[4, 3]／L=41；q3-r1→[5, 3]／L=72；q3-r2→[6, 3]／L=120；q3-r3→[7, 3]／L=170；q3-r4→[8, 3]／L=253；q3-r5→[9, 3]／L=585；q3-r6→[10, 3]／L=650；q3-r7→[11, 3]／L=715；q3-r8→[12, 3]／L=810；q4-r0→[5, 3]／L=72；q4-r1→[6, 3]／L=120；q4-r2→[7, 3]／L=170；q4-r3→[8, 3]／L=253；q4-r4→[9, 3]／L=585；q4-r5→[10, 3]／L=650；q4-r6→[11, 3]／L=715；q4-r7→[12, 3]／L=810；q5-r0→[6, 3]／L=120；q5-r1→[7, 3]／L=170；q5-r2→[8, 3]／L=253；q5-r3→[9, 3]／L=585；q5-r4→[10, 3]／L=650；q5-r5→[11, 3]／L=715；q5-r6→[12, 3]／L=810；q7-r0→[8, 3]／L=253；q7-r1→[9, 3]／L=585；q7-r2→[10, 3]／L=650；q7-r3→[11, 3]／L=715；q7-r4→[12, 3]／L=810；q8-r0→[9, 3]／L=585；q8-r1→[10, 3]／L=650；q8-r2→[11, 3]／L=715；q8-r3→[12, 3]／L=810；q9-r0→[10, 3]／L=650；q9-r1→[11, 3]／L=715；q9-r2→[12, 3]／L=810；q11-r0→[12, 3]／L=810（逐变体，不合成一个距离）

**距目标的证据：** no_target_graph_generated；必要式q^3≤U=2rq²+rq(q+1)+r(r−1)+r(r−1)²。19项D3阶数越线，其中16项正则奇偶合法；13项被U排除，正则必要幸存为(q,r)=(3,1),(5,2),(7,3)。47项均无D4/5阶数改善；无新图或搜索。

**其他指标（保持原计数类型）：**
```json
{
  "object_level": "theoretical_parameter_table",
  "graph_generated": false,
  "parameter_pairs": 47,
  "summary": {
    "parameter_pairs": 47,
    "legal_by_regular_graph_parity": 36,
    "active_legal_pairs": 35,
    "strict_D3_order_improving_pairs": 19,
    "legal_strict_D3_order_improving_pairs": 16,
    "legal_strict_D3_necessary_passes": 3,
    "legal_strict_D3_capacity_excluded": 13,
    "D4_or_D5_strict_order_improvements": 0
  },
  "formula": {
    "far": "q^3",
    "upper": "2*r*q^2 + r*q*(q+1) + r*(r-1) + r*(r-1)^2",
    "simplified_upper": "3*r*q^2 + r*q + r^2*(r-1)",
    "type": "average over all roots in one bipartition side; necessary only"
  },
  "regular_necessary_passes": [
    {
      "q": 3,
      "r": 1,
      "n": 80,
      "degree": 5,
      "target_D": 3,
      "savedL": 72,
      "far_targets_per_root": 27,
      "average_capacity_upper_bound": 30,
      "status": "NECESSARY_PASS_NO_GRAPH_CONSTRUCTED"
    },
    {
      "q": 5,
      "r": 2,
      "n": 312,
      "degree": 8,
      "target_D": 3,
      "savedL": 253,
      "far_targets_per_root": 125,
      "average_capacity_upper_bound": 164,
      "status": "NECESSARY_PASS_ALREADY_TESTED_FINITE_PROFILE_FAILED"
    },
    {
      "q": 7,
      "r": 3,
      "n": 800,
      "degree": 11,
      "target_D": 3,
      "savedL": 715,
      "far_targets_per_root": 343,
      "average_capacity_upper_bound": 480,
      "status": "NECESSARY_PASS_NO_GRAPH_CONSTRUCTED"
    }
  ],
  "max_degree_relaxation": {
    "scope": "Allow arbitrary simple internal graphs of maximum degree at most r on each side. The same average U bound remains valid; parity is not an obstruction to this larger scope.",
    "proof": "The CA far route total is 2*m_P*q^2 <= N*r*q^2. All other upper bounds already use degree upper bounds only.",
    "strict_D3_order_improving_pairs": 19,
    "capacity_excluded_pairs": 15,
    "necessary_passes": [
      {
        "q": 3,
        "r": 1,
        "n": 80,
        "degree": 5,
        "savedL": 72,
        "far_targets_per_root": 27,
        "average_capacity_upper_bound": 30
      },
      {
        "q": 5,
        "r": 2,
        "n": 312,
        "degree": 8,
        "savedL": 253,
        "far_targets_per_root": 125,
        "average_capacity_upper_bound": 164
      },
      {
        "q": 7,
        "r": 3,
        "n": 800,
        "degree": 11,
        "savedL": 715,
        "far_targets_per_root": 343,
        "average_capacity_upper_bound": 480
      },
      {
        "q": 8,
        "r": 3,
        "n": 1170,
        "degree": 12,
        "savedL": 810,
        "far_targets_per_root": 512,
        "average_capacity_upper_bound": 618
      }
    ],
    "important_open_case": {
      "q": 8,
      "internal_max_degree": 3,
      "n": 1170,
      "graph_max_degree": 12,
      "savedL": 810,
      "status": "NECESSARY_PASS_NEAR_REGULAR_CHOICES_NOT_SEARCHED",
      "detail": "Each side has 585 vertices. An internal graph may have one degree-2 vertex and 584 degree-3 vertices. Exact 3-regular parity failure does not exclude this maximum-degree template."
    },
    "followup": "research/ddp/breadth_20261027_wave11/gq_commuting_obstruction/REPORT.md"
  },
  "regular_parity_does_not_exclude_maxdegree": true,
  "existing_q5_profile": {
    "path": "research/ddp/breadth_20261027_wave10/gq312_internal_cycles/best.independent_check.json",
    "q": 5,
    "r": 2,
    "n": 312,
    "degree": 8,
    "actual_D": 4,
    "bad_unordered_pairs_gt3": 4090,
    "verification": "root independent all-312-root BFS already completed; not rerun",
    "scope": "two finite internal-2-factor search starts only, not all 2-regular internal choices"
  },
  "existing_profile_not_rerun": true,
  "graph_generation_count": 0,
  "BFS_count": 0,
  "parameter_search_proposals": 0,
  "CPU_seconds": 0.0006663010000000011,
  "scoped_external_review": {
    "raw_path": "reviews/ddp/wave11_scoped_review_20261027.json",
    "scope": "GQ path-exhaustiveness/average-vs-pointwise/parity boundary only;not all code or all47 arithmetic independently rerun.",
    "model_reported": "gemini-3.8-flash-high"
  }
}
```



**从属变体：**
```json
[
  {
    "q": 2,
    "r": 0,
    "side_order": 15,
    "n": {
      "actual": null,
      "hypothetical": 30
    },
    "degree": 3,
    "target_D": 3,
    "savedL": null,
    "far_targets_per_root": 8,
    "average_capacity_upper_bound": 0,
    "capacity_terms": {
      "internal_then_incidence_average": 0,
      "incidence_then_internal_average": 0,
      "opposite_side_internal_relay": 0,
      "pure_internal_two_steps": 0,
      "pure_internal_three_steps": 0
    },
    "capacity_margin": -8,
    "capacity_pass": false,
    "regularity_parity_possible": true,
    "active_degree_range": false,
    "strict_D3_order_improvement": false,
    "status": "OUTSIDE_ACTIVE_DEGREE_RANGE",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": null,
        "strict_order_improvement": null,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": null,
        "strict_order_improvement": null,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": null,
        "strict_order_improvement": null,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q2-r0",
    "target": [
      3,
      3
    ],
    "target_Delta": 3,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 2,
    "r": 1,
    "side_order": 15,
    "n": {
      "actual": null,
      "hypothetical": 30
    },
    "degree": 4,
    "target_D": 3,
    "savedL": 41,
    "far_targets_per_root": 8,
    "average_capacity_upper_bound": 14,
    "capacity_terms": {
      "internal_then_incidence_average": 4,
      "incidence_then_internal_average": 4,
      "opposite_side_internal_relay": 6,
      "pure_internal_two_steps": 0,
      "pure_internal_three_steps": 0
    },
    "capacity_margin": 6,
    "capacity_pass": true,
    "regularity_parity_possible": false,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "REGULARITY_PARITY_IMPOSSIBLE",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 41,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 104,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 364,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q2-r1",
    "target": [
      4,
      3
    ],
    "target_Delta": 4,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 2,
    "r": 2,
    "side_order": 15,
    "n": {
      "actual": null,
      "hypothetical": 30
    },
    "degree": 5,
    "target_D": 3,
    "savedL": 72,
    "far_targets_per_root": 8,
    "average_capacity_upper_bound": 32,
    "capacity_terms": {
      "internal_then_incidence_average": 8,
      "incidence_then_internal_average": 8,
      "opposite_side_internal_relay": 12,
      "pure_internal_two_steps": 2,
      "pure_internal_three_steps": 2
    },
    "capacity_margin": 24,
    "capacity_pass": true,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "NO_STRICT_D3_ORDER_IMPROVEMENT",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 72,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 252,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 650,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q2-r2",
    "target": [
      5,
      3
    ],
    "target_Delta": 5,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 2,
    "r": 3,
    "side_order": 15,
    "n": {
      "actual": null,
      "hypothetical": 30
    },
    "degree": 6,
    "target_D": 3,
    "savedL": 120,
    "far_targets_per_root": 8,
    "average_capacity_upper_bound": 60,
    "capacity_terms": {
      "internal_then_incidence_average": 12,
      "incidence_then_internal_average": 12,
      "opposite_side_internal_relay": 18,
      "pure_internal_two_steps": 6,
      "pure_internal_three_steps": 12
    },
    "capacity_margin": 52,
    "capacity_pass": true,
    "regularity_parity_possible": false,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "REGULARITY_PARITY_IMPOSSIBLE",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 120,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 441,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 1518,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q2-r3",
    "target": [
      6,
      3
    ],
    "target_Delta": 6,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 2,
    "r": 4,
    "side_order": 15,
    "n": {
      "actual": null,
      "hypothetical": 30
    },
    "degree": 7,
    "target_D": 3,
    "savedL": 170,
    "far_targets_per_root": 8,
    "average_capacity_upper_bound": 104,
    "capacity_terms": {
      "internal_then_incidence_average": 16,
      "incidence_then_internal_average": 16,
      "opposite_side_internal_relay": 24,
      "pure_internal_two_steps": 12,
      "pure_internal_three_steps": 36
    },
    "capacity_margin": 96,
    "capacity_pass": true,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "NO_STRICT_D3_ORDER_IMPROVEMENT",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 170,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 684,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 2810,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q2-r4",
    "target": [
      7,
      3
    ],
    "target_Delta": 7,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 2,
    "r": 5,
    "side_order": 15,
    "n": {
      "actual": null,
      "hypothetical": 30
    },
    "degree": 8,
    "target_D": 3,
    "savedL": 253,
    "far_targets_per_root": 8,
    "average_capacity_upper_bound": 170,
    "capacity_terms": {
      "internal_then_incidence_average": 20,
      "incidence_then_internal_average": 20,
      "opposite_side_internal_relay": 30,
      "pure_internal_two_steps": 20,
      "pure_internal_three_steps": 80
    },
    "capacity_margin": 162,
    "capacity_pass": true,
    "regularity_parity_possible": false,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "REGULARITY_PARITY_IMPOSSIBLE",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 253,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 1100,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 5334,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q2-r5",
    "target": [
      8,
      3
    ],
    "target_Delta": 8,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 2,
    "r": 6,
    "side_order": 15,
    "n": {
      "actual": null,
      "hypothetical": 30
    },
    "degree": 9,
    "target_D": 3,
    "savedL": 585,
    "far_targets_per_root": 8,
    "average_capacity_upper_bound": 264,
    "capacity_terms": {
      "internal_then_incidence_average": 24,
      "incidence_then_internal_average": 24,
      "opposite_side_internal_relay": 36,
      "pure_internal_two_steps": 30,
      "pure_internal_three_steps": 150
    },
    "capacity_margin": 256,
    "capacity_pass": true,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "NO_STRICT_D3_ORDER_IMPROVEMENT",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 585,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 1768,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 9020,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q2-r6",
    "target": [
      9,
      3
    ],
    "target_Delta": 9,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 2,
    "r": 7,
    "side_order": 15,
    "n": {
      "actual": null,
      "hypothetical": 30
    },
    "degree": 10,
    "target_D": 3,
    "savedL": 650,
    "far_targets_per_root": 8,
    "average_capacity_upper_bound": 392,
    "capacity_terms": {
      "internal_then_incidence_average": 28,
      "incidence_then_internal_average": 28,
      "opposite_side_internal_relay": 42,
      "pure_internal_two_steps": 42,
      "pure_internal_three_steps": 252
    },
    "capacity_margin": 384,
    "capacity_pass": true,
    "regularity_parity_possible": false,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "REGULARITY_PARITY_IMPOSSIBLE",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 650,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 2485,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 33397,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q2-r7",
    "target": [
      10,
      3
    ],
    "target_Delta": 10,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 2,
    "r": 8,
    "side_order": 15,
    "n": {
      "actual": null,
      "hypothetical": 30
    },
    "degree": 11,
    "target_D": 3,
    "savedL": 715,
    "far_targets_per_root": 8,
    "average_capacity_upper_bound": 560,
    "capacity_terms": {
      "internal_then_incidence_average": 32,
      "incidence_then_internal_average": 32,
      "opposite_side_internal_relay": 48,
      "pure_internal_two_steps": 56,
      "pure_internal_three_steps": 392
    },
    "capacity_margin": 552,
    "capacity_pass": true,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "NO_STRICT_D3_ORDER_IMPROVEMENT",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 715,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 3444,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 37628,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q2-r8",
    "target": [
      11,
      3
    ],
    "target_Delta": 11,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 2,
    "r": 9,
    "side_order": 15,
    "n": {
      "actual": null,
      "hypothetical": 30
    },
    "degree": 12,
    "target_D": 3,
    "savedL": 810,
    "far_targets_per_root": 8,
    "average_capacity_upper_bound": 774,
    "capacity_terms": {
      "internal_then_incidence_average": 36,
      "incidence_then_internal_average": 36,
      "opposite_side_internal_relay": 54,
      "pure_internal_two_steps": 72,
      "pure_internal_three_steps": 576
    },
    "capacity_margin": 766,
    "capacity_pass": true,
    "regularity_parity_possible": false,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "REGULARITY_PARITY_IMPOSSIBLE",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 810,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 5832,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 42342,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q2-r9",
    "target": [
      12,
      3
    ],
    "target_Delta": 12,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 3,
    "r": 0,
    "side_order": 40,
    "n": {
      "actual": null,
      "hypothetical": 80
    },
    "degree": 4,
    "target_D": 3,
    "savedL": 41,
    "far_targets_per_root": 27,
    "average_capacity_upper_bound": 0,
    "capacity_terms": {
      "internal_then_incidence_average": 0,
      "incidence_then_internal_average": 0,
      "opposite_side_internal_relay": 0,
      "pure_internal_two_steps": 0,
      "pure_internal_three_steps": 0
    },
    "capacity_margin": -27,
    "capacity_pass": false,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": true,
    "status": "D3_AVERAGE_CAPACITY_IMPOSSIBLE",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 41,
        "strict_order_improvement": true,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 104,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 364,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q3-r0",
    "target": [
      4,
      3
    ],
    "target_Delta": 4,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 3,
    "r": 1,
    "side_order": 40,
    "n": {
      "actual": null,
      "hypothetical": 80
    },
    "degree": 5,
    "target_D": 3,
    "savedL": 72,
    "far_targets_per_root": 27,
    "average_capacity_upper_bound": 30,
    "capacity_terms": {
      "internal_then_incidence_average": 9,
      "incidence_then_internal_average": 9,
      "opposite_side_internal_relay": 12,
      "pure_internal_two_steps": 0,
      "pure_internal_three_steps": 0
    },
    "capacity_margin": 3,
    "capacity_pass": true,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": true,
    "status": "NECESSARY_PASS_NO_GRAPH_CONSTRUCTED",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 72,
        "strict_order_improvement": true,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 252,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 650,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q3-r1",
    "target": [
      5,
      3
    ],
    "target_Delta": 5,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 3,
    "r": 2,
    "side_order": 40,
    "n": {
      "actual": null,
      "hypothetical": 80
    },
    "degree": 6,
    "target_D": 3,
    "savedL": 120,
    "far_targets_per_root": 27,
    "average_capacity_upper_bound": 64,
    "capacity_terms": {
      "internal_then_incidence_average": 18,
      "incidence_then_internal_average": 18,
      "opposite_side_internal_relay": 24,
      "pure_internal_two_steps": 2,
      "pure_internal_three_steps": 2
    },
    "capacity_margin": 37,
    "capacity_pass": true,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "NO_STRICT_D3_ORDER_IMPROVEMENT",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 120,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 441,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 1518,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q3-r2",
    "target": [
      6,
      3
    ],
    "target_Delta": 6,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 3,
    "r": 3,
    "side_order": 40,
    "n": {
      "actual": null,
      "hypothetical": 80
    },
    "degree": 7,
    "target_D": 3,
    "savedL": 170,
    "far_targets_per_root": 27,
    "average_capacity_upper_bound": 108,
    "capacity_terms": {
      "internal_then_incidence_average": 27,
      "incidence_then_internal_average": 27,
      "opposite_side_internal_relay": 36,
      "pure_internal_two_steps": 6,
      "pure_internal_three_steps": 12
    },
    "capacity_margin": 81,
    "capacity_pass": true,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "NO_STRICT_D3_ORDER_IMPROVEMENT",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 170,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 684,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 2810,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q3-r3",
    "target": [
      7,
      3
    ],
    "target_Delta": 7,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 3,
    "r": 4,
    "side_order": 40,
    "n": {
      "actual": null,
      "hypothetical": 80
    },
    "degree": 8,
    "target_D": 3,
    "savedL": 253,
    "far_targets_per_root": 27,
    "average_capacity_upper_bound": 168,
    "capacity_terms": {
      "internal_then_incidence_average": 36,
      "incidence_then_internal_average": 36,
      "opposite_side_internal_relay": 48,
      "pure_internal_two_steps": 12,
      "pure_internal_three_steps": 36
    },
    "capacity_margin": 141,
    "capacity_pass": true,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "NO_STRICT_D3_ORDER_IMPROVEMENT",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 253,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 1100,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 5334,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q3-r4",
    "target": [
      8,
      3
    ],
    "target_Delta": 8,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 3,
    "r": 5,
    "side_order": 40,
    "n": {
      "actual": null,
      "hypothetical": 80
    },
    "degree": 9,
    "target_D": 3,
    "savedL": 585,
    "far_targets_per_root": 27,
    "average_capacity_upper_bound": 250,
    "capacity_terms": {
      "internal_then_incidence_average": 45,
      "incidence_then_internal_average": 45,
      "opposite_side_internal_relay": 60,
      "pure_internal_two_steps": 20,
      "pure_internal_three_steps": 80
    },
    "capacity_margin": 223,
    "capacity_pass": true,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "NO_STRICT_D3_ORDER_IMPROVEMENT",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 585,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 1768,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 9020,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q3-r5",
    "target": [
      9,
      3
    ],
    "target_Delta": 9,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 3,
    "r": 6,
    "side_order": 40,
    "n": {
      "actual": null,
      "hypothetical": 80
    },
    "degree": 10,
    "target_D": 3,
    "savedL": 650,
    "far_targets_per_root": 27,
    "average_capacity_upper_bound": 360,
    "capacity_terms": {
      "internal_then_incidence_average": 54,
      "incidence_then_internal_average": 54,
      "opposite_side_internal_relay": 72,
      "pure_internal_two_steps": 30,
      "pure_internal_three_steps": 150
    },
    "capacity_margin": 333,
    "capacity_pass": true,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "NO_STRICT_D3_ORDER_IMPROVEMENT",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 650,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 2485,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 33397,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q3-r6",
    "target": [
      10,
      3
    ],
    "target_Delta": 10,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 3,
    "r": 7,
    "side_order": 40,
    "n": {
      "actual": null,
      "hypothetical": 80
    },
    "degree": 11,
    "target_D": 3,
    "savedL": 715,
    "far_targets_per_root": 27,
    "average_capacity_upper_bound": 504,
    "capacity_terms": {
      "internal_then_incidence_average": 63,
      "incidence_then_internal_average": 63,
      "opposite_side_internal_relay": 84,
      "pure_internal_two_steps": 42,
      "pure_internal_three_steps": 252
    },
    "capacity_margin": 477,
    "capacity_pass": true,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "NO_STRICT_D3_ORDER_IMPROVEMENT",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 715,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 3444,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 37628,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q3-r7",
    "target": [
      11,
      3
    ],
    "target_Delta": 11,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 3,
    "r": 8,
    "side_order": 40,
    "n": {
      "actual": null,
      "hypothetical": 80
    },
    "degree": 12,
    "target_D": 3,
    "savedL": 810,
    "far_targets_per_root": 27,
    "average_capacity_upper_bound": 688,
    "capacity_terms": {
      "internal_then_incidence_average": 72,
      "incidence_then_internal_average": 72,
      "opposite_side_internal_relay": 96,
      "pure_internal_two_steps": 56,
      "pure_internal_three_steps": 392
    },
    "capacity_margin": 661,
    "capacity_pass": true,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "NO_STRICT_D3_ORDER_IMPROVEMENT",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 810,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 5832,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 42342,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q3-r8",
    "target": [
      12,
      3
    ],
    "target_Delta": 12,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 4,
    "r": 0,
    "side_order": 85,
    "n": {
      "actual": null,
      "hypothetical": 170
    },
    "degree": 5,
    "target_D": 3,
    "savedL": 72,
    "far_targets_per_root": 64,
    "average_capacity_upper_bound": 0,
    "capacity_terms": {
      "internal_then_incidence_average": 0,
      "incidence_then_internal_average": 0,
      "opposite_side_internal_relay": 0,
      "pure_internal_two_steps": 0,
      "pure_internal_three_steps": 0
    },
    "capacity_margin": -64,
    "capacity_pass": false,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": true,
    "status": "D3_AVERAGE_CAPACITY_IMPOSSIBLE",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 72,
        "strict_order_improvement": true,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 252,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 650,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q4-r0",
    "target": [
      5,
      3
    ],
    "target_Delta": 5,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 4,
    "r": 1,
    "side_order": 85,
    "n": {
      "actual": null,
      "hypothetical": 170
    },
    "degree": 6,
    "target_D": 3,
    "savedL": 120,
    "far_targets_per_root": 64,
    "average_capacity_upper_bound": 52,
    "capacity_terms": {
      "internal_then_incidence_average": 16,
      "incidence_then_internal_average": 16,
      "opposite_side_internal_relay": 20,
      "pure_internal_two_steps": 0,
      "pure_internal_three_steps": 0
    },
    "capacity_margin": -12,
    "capacity_pass": false,
    "regularity_parity_possible": false,
    "active_degree_range": true,
    "strict_D3_order_improvement": true,
    "status": "REGULARITY_PARITY_IMPOSSIBLE",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 120,
        "strict_order_improvement": true,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 441,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 1518,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q4-r1",
    "target": [
      6,
      3
    ],
    "target_Delta": 6,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 4,
    "r": 2,
    "side_order": 85,
    "n": {
      "actual": null,
      "hypothetical": 170
    },
    "degree": 7,
    "target_D": 3,
    "savedL": 170,
    "far_targets_per_root": 64,
    "average_capacity_upper_bound": 108,
    "capacity_terms": {
      "internal_then_incidence_average": 32,
      "incidence_then_internal_average": 32,
      "opposite_side_internal_relay": 40,
      "pure_internal_two_steps": 2,
      "pure_internal_three_steps": 2
    },
    "capacity_margin": 44,
    "capacity_pass": true,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "NO_STRICT_D3_ORDER_IMPROVEMENT",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 170,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 684,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 2810,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q4-r2",
    "target": [
      7,
      3
    ],
    "target_Delta": 7,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 4,
    "r": 3,
    "side_order": 85,
    "n": {
      "actual": null,
      "hypothetical": 170
    },
    "degree": 8,
    "target_D": 3,
    "savedL": 253,
    "far_targets_per_root": 64,
    "average_capacity_upper_bound": 174,
    "capacity_terms": {
      "internal_then_incidence_average": 48,
      "incidence_then_internal_average": 48,
      "opposite_side_internal_relay": 60,
      "pure_internal_two_steps": 6,
      "pure_internal_three_steps": 12
    },
    "capacity_margin": 110,
    "capacity_pass": true,
    "regularity_parity_possible": false,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "REGULARITY_PARITY_IMPOSSIBLE",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 253,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 1100,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 5334,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q4-r3",
    "target": [
      8,
      3
    ],
    "target_Delta": 8,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 4,
    "r": 4,
    "side_order": 85,
    "n": {
      "actual": null,
      "hypothetical": 170
    },
    "degree": 9,
    "target_D": 3,
    "savedL": 585,
    "far_targets_per_root": 64,
    "average_capacity_upper_bound": 256,
    "capacity_terms": {
      "internal_then_incidence_average": 64,
      "incidence_then_internal_average": 64,
      "opposite_side_internal_relay": 80,
      "pure_internal_two_steps": 12,
      "pure_internal_three_steps": 36
    },
    "capacity_margin": 192,
    "capacity_pass": true,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "NO_STRICT_D3_ORDER_IMPROVEMENT",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 585,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 1768,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 9020,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q4-r4",
    "target": [
      9,
      3
    ],
    "target_Delta": 9,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 4,
    "r": 5,
    "side_order": 85,
    "n": {
      "actual": null,
      "hypothetical": 170
    },
    "degree": 10,
    "target_D": 3,
    "savedL": 650,
    "far_targets_per_root": 64,
    "average_capacity_upper_bound": 360,
    "capacity_terms": {
      "internal_then_incidence_average": 80,
      "incidence_then_internal_average": 80,
      "opposite_side_internal_relay": 100,
      "pure_internal_two_steps": 20,
      "pure_internal_three_steps": 80
    },
    "capacity_margin": 296,
    "capacity_pass": true,
    "regularity_parity_possible": false,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "REGULARITY_PARITY_IMPOSSIBLE",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 650,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 2485,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 33397,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q4-r5",
    "target": [
      10,
      3
    ],
    "target_Delta": 10,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 4,
    "r": 6,
    "side_order": 85,
    "n": {
      "actual": null,
      "hypothetical": 170
    },
    "degree": 11,
    "target_D": 3,
    "savedL": 715,
    "far_targets_per_root": 64,
    "average_capacity_upper_bound": 492,
    "capacity_terms": {
      "internal_then_incidence_average": 96,
      "incidence_then_internal_average": 96,
      "opposite_side_internal_relay": 120,
      "pure_internal_two_steps": 30,
      "pure_internal_three_steps": 150
    },
    "capacity_margin": 428,
    "capacity_pass": true,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "NO_STRICT_D3_ORDER_IMPROVEMENT",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 715,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 3444,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 37628,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q4-r6",
    "target": [
      11,
      3
    ],
    "target_Delta": 11,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 4,
    "r": 7,
    "side_order": 85,
    "n": {
      "actual": null,
      "hypothetical": 170
    },
    "degree": 12,
    "target_D": 3,
    "savedL": 810,
    "far_targets_per_root": 64,
    "average_capacity_upper_bound": 658,
    "capacity_terms": {
      "internal_then_incidence_average": 112,
      "incidence_then_internal_average": 112,
      "opposite_side_internal_relay": 140,
      "pure_internal_two_steps": 42,
      "pure_internal_three_steps": 252
    },
    "capacity_margin": 594,
    "capacity_pass": true,
    "regularity_parity_possible": false,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "REGULARITY_PARITY_IMPOSSIBLE",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 810,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 5832,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 42342,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q4-r7",
    "target": [
      12,
      3
    ],
    "target_Delta": 12,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 5,
    "r": 0,
    "side_order": 156,
    "n": {
      "actual": null,
      "hypothetical": 312
    },
    "degree": 6,
    "target_D": 3,
    "savedL": 120,
    "far_targets_per_root": 125,
    "average_capacity_upper_bound": 0,
    "capacity_terms": {
      "internal_then_incidence_average": 0,
      "incidence_then_internal_average": 0,
      "opposite_side_internal_relay": 0,
      "pure_internal_two_steps": 0,
      "pure_internal_three_steps": 0
    },
    "capacity_margin": -125,
    "capacity_pass": false,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": true,
    "status": "D3_AVERAGE_CAPACITY_IMPOSSIBLE",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 120,
        "strict_order_improvement": true,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 441,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 1518,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q5-r0",
    "target": [
      6,
      3
    ],
    "target_Delta": 6,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 5,
    "r": 1,
    "side_order": 156,
    "n": {
      "actual": null,
      "hypothetical": 312
    },
    "degree": 7,
    "target_D": 3,
    "savedL": 170,
    "far_targets_per_root": 125,
    "average_capacity_upper_bound": 80,
    "capacity_terms": {
      "internal_then_incidence_average": 25,
      "incidence_then_internal_average": 25,
      "opposite_side_internal_relay": 30,
      "pure_internal_two_steps": 0,
      "pure_internal_three_steps": 0
    },
    "capacity_margin": -45,
    "capacity_pass": false,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": true,
    "status": "D3_AVERAGE_CAPACITY_IMPOSSIBLE",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 170,
        "strict_order_improvement": true,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 684,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 2810,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q5-r1",
    "target": [
      7,
      3
    ],
    "target_Delta": 7,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 5,
    "r": 2,
    "side_order": 156,
    "n": {
      "actual": null,
      "hypothetical": 312
    },
    "degree": 8,
    "target_D": 3,
    "savedL": 253,
    "far_targets_per_root": 125,
    "average_capacity_upper_bound": 164,
    "capacity_terms": {
      "internal_then_incidence_average": 50,
      "incidence_then_internal_average": 50,
      "opposite_side_internal_relay": 60,
      "pure_internal_two_steps": 2,
      "pure_internal_three_steps": 2
    },
    "capacity_margin": 39,
    "capacity_pass": true,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": true,
    "status": "NECESSARY_PASS_ALREADY_TESTED_FINITE_PROFILE_FAILED",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 253,
        "strict_order_improvement": true,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 1100,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 5334,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q5-r2",
    "target": [
      8,
      3
    ],
    "target_Delta": 8,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 5,
    "r": 3,
    "side_order": 156,
    "n": {
      "actual": null,
      "hypothetical": 312
    },
    "degree": 9,
    "target_D": 3,
    "savedL": 585,
    "far_targets_per_root": 125,
    "average_capacity_upper_bound": 258,
    "capacity_terms": {
      "internal_then_incidence_average": 75,
      "incidence_then_internal_average": 75,
      "opposite_side_internal_relay": 90,
      "pure_internal_two_steps": 6,
      "pure_internal_three_steps": 12
    },
    "capacity_margin": 133,
    "capacity_pass": true,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "NO_STRICT_D3_ORDER_IMPROVEMENT",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 585,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 1768,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 9020,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q5-r3",
    "target": [
      9,
      3
    ],
    "target_Delta": 9,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 5,
    "r": 4,
    "side_order": 156,
    "n": {
      "actual": null,
      "hypothetical": 312
    },
    "degree": 10,
    "target_D": 3,
    "savedL": 650,
    "far_targets_per_root": 125,
    "average_capacity_upper_bound": 368,
    "capacity_terms": {
      "internal_then_incidence_average": 100,
      "incidence_then_internal_average": 100,
      "opposite_side_internal_relay": 120,
      "pure_internal_two_steps": 12,
      "pure_internal_three_steps": 36
    },
    "capacity_margin": 243,
    "capacity_pass": true,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "NO_STRICT_D3_ORDER_IMPROVEMENT",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 650,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 2485,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 33397,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q5-r4",
    "target": [
      10,
      3
    ],
    "target_Delta": 10,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 5,
    "r": 5,
    "side_order": 156,
    "n": {
      "actual": null,
      "hypothetical": 312
    },
    "degree": 11,
    "target_D": 3,
    "savedL": 715,
    "far_targets_per_root": 125,
    "average_capacity_upper_bound": 500,
    "capacity_terms": {
      "internal_then_incidence_average": 125,
      "incidence_then_internal_average": 125,
      "opposite_side_internal_relay": 150,
      "pure_internal_two_steps": 20,
      "pure_internal_three_steps": 80
    },
    "capacity_margin": 375,
    "capacity_pass": true,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "NO_STRICT_D3_ORDER_IMPROVEMENT",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 715,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 3444,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 37628,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q5-r5",
    "target": [
      11,
      3
    ],
    "target_Delta": 11,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 5,
    "r": 6,
    "side_order": 156,
    "n": {
      "actual": null,
      "hypothetical": 312
    },
    "degree": 12,
    "target_D": 3,
    "savedL": 810,
    "far_targets_per_root": 125,
    "average_capacity_upper_bound": 660,
    "capacity_terms": {
      "internal_then_incidence_average": 150,
      "incidence_then_internal_average": 150,
      "opposite_side_internal_relay": 180,
      "pure_internal_two_steps": 30,
      "pure_internal_three_steps": 150
    },
    "capacity_margin": 535,
    "capacity_pass": true,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "NO_STRICT_D3_ORDER_IMPROVEMENT",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 810,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 5832,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 42342,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q5-r6",
    "target": [
      12,
      3
    ],
    "target_Delta": 12,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 7,
    "r": 0,
    "side_order": 400,
    "n": {
      "actual": null,
      "hypothetical": 800
    },
    "degree": 8,
    "target_D": 3,
    "savedL": 253,
    "far_targets_per_root": 343,
    "average_capacity_upper_bound": 0,
    "capacity_terms": {
      "internal_then_incidence_average": 0,
      "incidence_then_internal_average": 0,
      "opposite_side_internal_relay": 0,
      "pure_internal_two_steps": 0,
      "pure_internal_three_steps": 0
    },
    "capacity_margin": -343,
    "capacity_pass": false,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": true,
    "status": "D3_AVERAGE_CAPACITY_IMPOSSIBLE",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 253,
        "strict_order_improvement": true,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 1100,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 5334,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q7-r0",
    "target": [
      8,
      3
    ],
    "target_Delta": 8,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 7,
    "r": 1,
    "side_order": 400,
    "n": {
      "actual": null,
      "hypothetical": 800
    },
    "degree": 9,
    "target_D": 3,
    "savedL": 585,
    "far_targets_per_root": 343,
    "average_capacity_upper_bound": 154,
    "capacity_terms": {
      "internal_then_incidence_average": 49,
      "incidence_then_internal_average": 49,
      "opposite_side_internal_relay": 56,
      "pure_internal_two_steps": 0,
      "pure_internal_three_steps": 0
    },
    "capacity_margin": -189,
    "capacity_pass": false,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": true,
    "status": "D3_AVERAGE_CAPACITY_IMPOSSIBLE",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 585,
        "strict_order_improvement": true,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 1768,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 9020,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q7-r1",
    "target": [
      9,
      3
    ],
    "target_Delta": 9,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 7,
    "r": 2,
    "side_order": 400,
    "n": {
      "actual": null,
      "hypothetical": 800
    },
    "degree": 10,
    "target_D": 3,
    "savedL": 650,
    "far_targets_per_root": 343,
    "average_capacity_upper_bound": 312,
    "capacity_terms": {
      "internal_then_incidence_average": 98,
      "incidence_then_internal_average": 98,
      "opposite_side_internal_relay": 112,
      "pure_internal_two_steps": 2,
      "pure_internal_three_steps": 2
    },
    "capacity_margin": -31,
    "capacity_pass": false,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": true,
    "status": "D3_AVERAGE_CAPACITY_IMPOSSIBLE",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 650,
        "strict_order_improvement": true,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 2485,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 33397,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q7-r2",
    "target": [
      10,
      3
    ],
    "target_Delta": 10,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 7,
    "r": 3,
    "side_order": 400,
    "n": {
      "actual": null,
      "hypothetical": 800
    },
    "degree": 11,
    "target_D": 3,
    "savedL": 715,
    "far_targets_per_root": 343,
    "average_capacity_upper_bound": 480,
    "capacity_terms": {
      "internal_then_incidence_average": 147,
      "incidence_then_internal_average": 147,
      "opposite_side_internal_relay": 168,
      "pure_internal_two_steps": 6,
      "pure_internal_three_steps": 12
    },
    "capacity_margin": 137,
    "capacity_pass": true,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": true,
    "status": "NECESSARY_PASS_NO_GRAPH_CONSTRUCTED",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 715,
        "strict_order_improvement": true,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 3444,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 37628,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q7-r3",
    "target": [
      11,
      3
    ],
    "target_Delta": 11,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 7,
    "r": 4,
    "side_order": 400,
    "n": {
      "actual": null,
      "hypothetical": 800
    },
    "degree": 12,
    "target_D": 3,
    "savedL": 810,
    "far_targets_per_root": 343,
    "average_capacity_upper_bound": 664,
    "capacity_terms": {
      "internal_then_incidence_average": 196,
      "incidence_then_internal_average": 196,
      "opposite_side_internal_relay": 224,
      "pure_internal_two_steps": 12,
      "pure_internal_three_steps": 36
    },
    "capacity_margin": 321,
    "capacity_pass": true,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": false,
    "status": "NO_STRICT_D3_ORDER_IMPROVEMENT",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 810,
        "strict_order_improvement": false,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 5832,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 42342,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q7-r4",
    "target": [
      12,
      3
    ],
    "target_Delta": 12,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 8,
    "r": 0,
    "side_order": 585,
    "n": {
      "actual": null,
      "hypothetical": 1170
    },
    "degree": 9,
    "target_D": 3,
    "savedL": 585,
    "far_targets_per_root": 512,
    "average_capacity_upper_bound": 0,
    "capacity_terms": {
      "internal_then_incidence_average": 0,
      "incidence_then_internal_average": 0,
      "opposite_side_internal_relay": 0,
      "pure_internal_two_steps": 0,
      "pure_internal_three_steps": 0
    },
    "capacity_margin": -512,
    "capacity_pass": false,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": true,
    "status": "D3_AVERAGE_CAPACITY_IMPOSSIBLE",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 585,
        "strict_order_improvement": true,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 1768,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 9020,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q8-r0",
    "target": [
      9,
      3
    ],
    "target_Delta": 9,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 8,
    "r": 1,
    "side_order": 585,
    "n": {
      "actual": null,
      "hypothetical": 1170
    },
    "degree": 10,
    "target_D": 3,
    "savedL": 650,
    "far_targets_per_root": 512,
    "average_capacity_upper_bound": 200,
    "capacity_terms": {
      "internal_then_incidence_average": 64,
      "incidence_then_internal_average": 64,
      "opposite_side_internal_relay": 72,
      "pure_internal_two_steps": 0,
      "pure_internal_three_steps": 0
    },
    "capacity_margin": -312,
    "capacity_pass": false,
    "regularity_parity_possible": false,
    "active_degree_range": true,
    "strict_D3_order_improvement": true,
    "status": "REGULARITY_PARITY_IMPOSSIBLE",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 650,
        "strict_order_improvement": true,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 2485,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 33397,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q8-r1",
    "target": [
      10,
      3
    ],
    "target_Delta": 10,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 8,
    "r": 2,
    "side_order": 585,
    "n": {
      "actual": null,
      "hypothetical": 1170
    },
    "degree": 11,
    "target_D": 3,
    "savedL": 715,
    "far_targets_per_root": 512,
    "average_capacity_upper_bound": 404,
    "capacity_terms": {
      "internal_then_incidence_average": 128,
      "incidence_then_internal_average": 128,
      "opposite_side_internal_relay": 144,
      "pure_internal_two_steps": 2,
      "pure_internal_three_steps": 2
    },
    "capacity_margin": -108,
    "capacity_pass": false,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": true,
    "status": "D3_AVERAGE_CAPACITY_IMPOSSIBLE",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 715,
        "strict_order_improvement": true,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 3444,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 37628,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q8-r2",
    "target": [
      11,
      3
    ],
    "target_Delta": 11,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 8,
    "r": 3,
    "side_order": 585,
    "n": {
      "actual": null,
      "hypothetical": 1170
    },
    "degree": 12,
    "target_D": 3,
    "savedL": 810,
    "far_targets_per_root": 512,
    "average_capacity_upper_bound": 618,
    "capacity_terms": {
      "internal_then_incidence_average": 192,
      "incidence_then_internal_average": 192,
      "opposite_side_internal_relay": 216,
      "pure_internal_two_steps": 6,
      "pure_internal_three_steps": 12
    },
    "capacity_margin": 106,
    "capacity_pass": true,
    "regularity_parity_possible": false,
    "active_degree_range": true,
    "strict_D3_order_improvement": true,
    "status": "REGULARITY_PARITY_IMPOSSIBLE",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 810,
        "strict_order_improvement": true,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 5832,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 42342,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q8-r3",
    "target": [
      12,
      3
    ],
    "target_Delta": 12,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 9,
    "r": 0,
    "side_order": 820,
    "n": {
      "actual": null,
      "hypothetical": 1640
    },
    "degree": 10,
    "target_D": 3,
    "savedL": 650,
    "far_targets_per_root": 729,
    "average_capacity_upper_bound": 0,
    "capacity_terms": {
      "internal_then_incidence_average": 0,
      "incidence_then_internal_average": 0,
      "opposite_side_internal_relay": 0,
      "pure_internal_two_steps": 0,
      "pure_internal_three_steps": 0
    },
    "capacity_margin": -729,
    "capacity_pass": false,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": true,
    "status": "D3_AVERAGE_CAPACITY_IMPOSSIBLE",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 650,
        "strict_order_improvement": true,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 2485,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 33397,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q9-r0",
    "target": [
      10,
      3
    ],
    "target_Delta": 10,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 9,
    "r": 1,
    "side_order": 820,
    "n": {
      "actual": null,
      "hypothetical": 1640
    },
    "degree": 11,
    "target_D": 3,
    "savedL": 715,
    "far_targets_per_root": 729,
    "average_capacity_upper_bound": 252,
    "capacity_terms": {
      "internal_then_incidence_average": 81,
      "incidence_then_internal_average": 81,
      "opposite_side_internal_relay": 90,
      "pure_internal_two_steps": 0,
      "pure_internal_three_steps": 0
    },
    "capacity_margin": -477,
    "capacity_pass": false,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": true,
    "status": "D3_AVERAGE_CAPACITY_IMPOSSIBLE",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 715,
        "strict_order_improvement": true,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 3444,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 37628,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q9-r1",
    "target": [
      11,
      3
    ],
    "target_Delta": 11,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 9,
    "r": 2,
    "side_order": 820,
    "n": {
      "actual": null,
      "hypothetical": 1640
    },
    "degree": 12,
    "target_D": 3,
    "savedL": 810,
    "far_targets_per_root": 729,
    "average_capacity_upper_bound": 508,
    "capacity_terms": {
      "internal_then_incidence_average": 162,
      "incidence_then_internal_average": 162,
      "opposite_side_internal_relay": 180,
      "pure_internal_two_steps": 2,
      "pure_internal_three_steps": 2
    },
    "capacity_margin": -221,
    "capacity_pass": false,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": true,
    "status": "D3_AVERAGE_CAPACITY_IMPOSSIBLE",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 810,
        "strict_order_improvement": true,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 5832,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 42342,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q9-r2",
    "target": [
      12,
      3
    ],
    "target_Delta": 12,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  },
  {
    "q": 11,
    "r": 0,
    "side_order": 1464,
    "n": {
      "actual": null,
      "hypothetical": 2928
    },
    "degree": 12,
    "target_D": 3,
    "savedL": 810,
    "far_targets_per_root": 1331,
    "average_capacity_upper_bound": 0,
    "capacity_terms": {
      "internal_then_incidence_average": 0,
      "incidence_then_internal_average": 0,
      "opposite_side_internal_relay": 0,
      "pure_internal_two_steps": 0,
      "pure_internal_three_steps": 0
    },
    "capacity_margin": -1331,
    "capacity_pass": false,
    "regularity_parity_possible": true,
    "active_degree_range": true,
    "strict_D3_order_improvement": true,
    "status": "D3_AVERAGE_CAPACITY_IMPOSSIBLE",
    "all_target_comparisons": [
      {
        "target_D": 3,
        "savedL": 810,
        "strict_order_improvement": true,
        "routing_guarantee": "D3 requires additional coverage"
      },
      {
        "target_D": 4,
        "savedL": 5832,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      },
      {
        "target_D": 5,
        "savedL": 42342,
        "strict_order_improvement": false,
        "routing_guarantee": "D<=4 from retained incidence graph"
      }
    ],
    "id": "q11-r0",
    "target": [
      12,
      3
    ],
    "target_Delta": 12,
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "graph_generated": false,
    "scope": "Exact regular parity status applies only to r-regular internal graphs;capacity inequality also bounds maxdegree<=r."
  }
]
```

**原始证据：** [research/ddp/breadth_20261027_wave11/gq_internal_capacity/REPORT.md](../../research/ddp/breadth_20261027_wave11/gq_internal_capacity/REPORT.md)；[research/ddp/breadth_20261027_wave11/gq_internal_capacity/RESULT.json](../../research/ddp/breadth_20261027_wave11/gq_internal_capacity/RESULT.json)；[research/ddp/breadth_20261027_wave11/gq_internal_capacity/terminal.json](../../research/ddp/breadth_20261027_wave11/gq_internal_capacity/terminal.json)；[research/ddp/breadth_20261027_wave11/gq_internal_capacity/screen.py](../../research/ddp/breadth_20261027_wave11/gq_internal_capacity/screen.py)；[reviews/ddp/wave11_scoped_review_20261027.json](../../reviews/ddp/wave11_scoped_review_20261027.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** q∈{2,3,4,5,7,8,9,11}，0≤r≤11−q，共47项；保留GQ(q,q)全部incidence，加两侧任意简单r-regular内部图。U容量也适用于内部maxdegree≤r；正则奇偶排除只针对exact regular。每参数保留D3/4/5门槛比较。

**正向保证：** 保留incidence使全部跨侧对≤3、同侧共线对≤2、全图D≤4，只需补q³个同侧远点/根。；AC逐点≤rq²；CA只作全侧平均≤rq²，不把平均错作逐点界。；相同U对内部maxdegree≤r仍有效，但Nr偶数只约束exact r-regular。

**仍未完成：** q8每侧585奇数只排exact3regular，不排一度2加584度3的max3内部图；该1170点degreecap12模型通过U必要筛，双侧非commuting选择仍开放。三个regular幸存也未由U构成图；其commuting子类的后续阻断另行记录。

**启发与重启依据：** 按完整路径类别先计平均容量，再比较保存门槛。奇偶不得扩张成max-degree排除；必要通过不是存在。未授权参数搜索，重开需覆盖远端的实质结构，而非仅列参数。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

