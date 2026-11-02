---
type: experiment
node_id: exp:ddp-wave11-gq-commuting-obstruction
title: "GQ内部邻接commuting阻断：三个regular幸存及q8 max3子类"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave11/gq_commuting_obstruction/REPORT.md; research/ddp/breadth_20261027_wave11/gq_commuting_obstruction/RESULT.json; research/ddp/breadth_20261027_wave11/gq_commuting_obstruction/terminal.json; research/ddp/breadth_20261027_wave11/gq_commuting_obstruction/check.py"
added: 2026-10-27T08:25:53Z
tags: ["ddp", "method-ledger"]
---

# GQ内部邻接commuting阻断：三个regular幸存及q8 max3子类

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** paper-commutation-obstruction

**目标与阶数：** 多目标：q3-commuting-side→[5, 3]／L=72；q5-commuting-side→[8, 3]／L=253；q7-commuting-side→[11, 3]／L=715；q8-commuting-side→[12, 3]／L=810（逐变体，不合成一个距离）

**距目标的证据：** no_target_graph_generated；C²=q²I+(q+1)J使PC=CP强迫P正则，且support(PC)=support(CP)合并两个端点内部路由项。三个regular幸存Ucomm依次21<27、114<125、333<343；q8 odd585侧max3若commute则degree≤2，混合界348<512。任一侧commute均不能D3。

**其他指标（保持原计数类型）：**
```json
{
  "object_level": "paper_conditional_subclass_obstruction",
  "graph_generated": false,
  "equal_degree_formula": "r*q^2 + r*q*(q+1) + r*(r-1) + r*(r-1)^2",
  "mixed_degree_formula": "p*q^2 + s*q*(q+1) + p*(p-1) + p*(p-1)^2",
  "commuting_forces_regular": true,
  "opposite_side_commutation_required": false,
  "automorphism_scope": "P=sum of collinearity-automorphism permutation matrices only when the sum is symmetric, has zero diagonal, and already has entries in {0,1}; this sum commutes with C",
  "removing_loops_or_thresholding_preserves_commutation_claimed": false,
  "q8_noncommuting_max3_near_regular_open": true,
  "graph_generation_count": 0,
  "BFS_count": 0,
  "solver_calls": 0,
  "residual_status": {
    "q3r1": "one separate complete finite MILP was UNKNOWN with no incumbent; not rerun",
    "q5r2": "existing two-start finite profile D4/4090 bad; not rerun or generalized to all choices",
    "q7r3": "no graph construction or search",
    "q8max3": "no graph construction or search; open noncommuting near-regular case"
  },
  "proof_status": "Self-contained same-model paper derivation;no external-review or Lean proof claim.",
  "CPU_seconds": 2.0349000000002837e-05
}
```



**从属变体：**
```json
[
  {
    "q": 3,
    "side_order": 40,
    "n": {
      "actual": null,
      "hypothetical": 80
    },
    "target_D": 3,
    "target_Delta": 5,
    "savedL": 72,
    "commuting_side_degree": 1,
    "other_side_max_degree": 1,
    "far_targets_per_root": 27,
    "pointwise_capacity_upper_bound": 21,
    "terms": {
      "merged_endpoint_internal_routes": 9,
      "opposite_side_internal_relay": 12,
      "internal_two_steps": 0,
      "internal_three_steps": 0
    },
    "uncovered_far_targets_per_commuting_side_root_at_least": 6,
    "unordered_bad_pairs_on_commuting_side_at_least": 120,
    "obstruction": "D3 impossible if either side commutes with its closed collinearity matrix",
    "scope": "original equal-r-regular scope, also valid if other side has maximum degree<=r",
    "id": "q3-commuting-side",
    "target": [
      5,
      3
    ],
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "bad_pair_lower_bound_type": "proven conditional distance4 unordered pairs within commuting side;not measured graph badcount",
    "graph_generated": false
  },
  {
    "q": 5,
    "side_order": 156,
    "n": {
      "actual": null,
      "hypothetical": 312
    },
    "target_D": 3,
    "target_Delta": 8,
    "savedL": 253,
    "commuting_side_degree": 2,
    "other_side_max_degree": 2,
    "far_targets_per_root": 125,
    "pointwise_capacity_upper_bound": 114,
    "terms": {
      "merged_endpoint_internal_routes": 50,
      "opposite_side_internal_relay": 60,
      "internal_two_steps": 2,
      "internal_three_steps": 2
    },
    "uncovered_far_targets_per_commuting_side_root_at_least": 11,
    "unordered_bad_pairs_on_commuting_side_at_least": 858,
    "obstruction": "D3 impossible if either side commutes with its closed collinearity matrix",
    "scope": "original equal-r-regular scope, also valid if other side has maximum degree<=r",
    "id": "q5-commuting-side",
    "target": [
      8,
      3
    ],
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "bad_pair_lower_bound_type": "proven conditional distance4 unordered pairs within commuting side;not measured graph badcount",
    "graph_generated": false
  },
  {
    "q": 7,
    "side_order": 400,
    "n": {
      "actual": null,
      "hypothetical": 800
    },
    "target_D": 3,
    "target_Delta": 11,
    "savedL": 715,
    "commuting_side_degree": 3,
    "other_side_max_degree": 3,
    "far_targets_per_root": 343,
    "pointwise_capacity_upper_bound": 333,
    "terms": {
      "merged_endpoint_internal_routes": 147,
      "opposite_side_internal_relay": 168,
      "internal_two_steps": 6,
      "internal_three_steps": 12
    },
    "uncovered_far_targets_per_commuting_side_root_at_least": 10,
    "unordered_bad_pairs_on_commuting_side_at_least": 2000,
    "obstruction": "D3 impossible if either side commutes with its closed collinearity matrix",
    "scope": "original equal-r-regular scope, also valid if other side has maximum degree<=r",
    "id": "q7-commuting-side",
    "target": [
      11,
      3
    ],
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "bad_pair_lower_bound_type": "proven conditional distance4 unordered pairs within commuting side;not measured graph badcount",
    "graph_generated": false
  },
  {
    "q": 8,
    "side_order": 585,
    "n": {
      "actual": null,
      "hypothetical": 1170
    },
    "target_D": 3,
    "target_Delta": 12,
    "savedL": 810,
    "commuting_side_degree": 2,
    "other_side_max_degree": 3,
    "far_targets_per_root": 512,
    "pointwise_capacity_upper_bound": 348,
    "terms": {
      "merged_endpoint_internal_routes": 128,
      "opposite_side_internal_relay": 216,
      "internal_two_steps": 2,
      "internal_three_steps": 2
    },
    "uncovered_far_targets_per_commuting_side_root_at_least": 164,
    "unordered_bad_pairs_on_commuting_side_at_least": 47970,
    "obstruction": "D3 impossible if either side commutes with its closed collinearity matrix",
    "scope": "max-degree-3 near-regular allowed; commutation forces regular degree<=2 on an odd side",
    "id": "q8-commuting-side",
    "target": [
      12,
      3
    ],
    "actual_D": null,
    "actual_graph_Delta": null,
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": null,
    "bad_pair_lower_bound_type": "proven conditional distance4 unordered pairs within commuting side;not measured graph badcount",
    "graph_generated": false
  }
]
```

**原始证据：** [research/ddp/breadth_20261027_wave11/gq_commuting_obstruction/REPORT.md](../../research/ddp/breadth_20261027_wave11/gq_commuting_obstruction/REPORT.md)；[research/ddp/breadth_20261027_wave11/gq_commuting_obstruction/RESULT.json](../../research/ddp/breadth_20261027_wave11/gq_commuting_obstruction/RESULT.json)；[research/ddp/breadth_20261027_wave11/gq_commuting_obstruction/terminal.json](../../research/ddp/breadth_20261027_wave11/gq_commuting_obstruction/terminal.json)；[research/ddp/breadth_20261027_wave11/gq_commuting_obstruction/check.py](../../research/ddp/breadth_20261027_wave11/gq_commuting_obstruction/check.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 保留GQ全部incidence；任意一侧实际simple undirected内部邻接P满足PC=CP时，对侧只需maxdegree上限且无需commute。q3/r1、q5/r2、q7/r3及q8/max3四项；不排双侧均noncommuting内部图。

**正向保证：** Ucomm(q;p,s)=p*q²+s*q(q+1)+p(p−1)+p(p−1)²为commuting侧逐点上界；对侧不要求正则、commute或共同群作用。；正规奇偶只在已由commutation推出正则后使用，q8非commuting近3正则选择没有被奇偶排除。；简单无loop、无重数且对称的collinearity-automorphism permutation矩阵和属于commuting子类；删loops或去重复后必须另查真实PC=CP，不自动外推。

**仍未完成：** 四项一般maxdegree幸存都要求两侧真实内部邻接noncommuting才可能成功。q3一般双matching一次MILP仍UNKNOWN；q5原两startD4/4090仅有限失败；q7/r3、q8/max3双侧noncommuting没有构图或搜索。

**启发与重启依据：** 自动同几何矩阵commute的简单automorphism factor不能修复far覆盖；后续须在两侧均打破commuting结构并给覆盖互补依据。仅派生纸面障碍，不恢复任何profile、solver窗口或参数队列。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

