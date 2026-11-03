---
type: experiment
node_id: exp:ddp-h9-global-coverage-20261027
title: "H9整体覆盖对照：675条Q-line恢复、统一旧覆盖及343完整星上限"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/global_coverage_20261027/REPORT.md; research/ddp/global_coverage_20261027/h9_relation/REPORT.md; research/ddp/global_coverage_20261027/h9_relation/star_containment.json; research/ddp/global_coverage_20261027/h9_bare_core_clones/REPORT.md; research/ddp/global_coverage_20261027/h9_bare_core_clones/integer_upper_bound.json; research/ddp/global_coverage_20261027/h9_bare_core_clones/STAR_CONTAINMENT_EXTENSION.json; research/ddp/global_coverage_20261027/h9_clone_capacity/REPORT.md; research/ddp/global_coverage_20261027/h9_global_rule/REPORT.md; research/ddp/global_coverage_20261027/tail165_mechanism/PREDICTIONS.md; research/ddp/global_coverage_20261027/tail165_mechanism/RESULT.json; research/ddp/global_coverage_20261027/tail165_mechanism/P4_COUNTERFACTUAL.md; research/ddp/global_coverage_20261027/tail165_mechanism/P4_RESULT.json; research/ddp/global_coverage_20261027/tail165_mechanism/P5_PAIR_PREDICTION.md; research/ddp/global_coverage_20261027/tail165_mechanism/P5_RESULT.json; research/ddp/global_coverage_20261027/h9_global_rule/P6_PREDICTION.md; research/ddp/global_coverage_20261027/tail165_mechanism/P6_RESULT.json; research/ddp/global_coverage_20261027/h9_line_signature/REPORT.md; research/ddp/global_coverage_20261027/h9_line_pair_rule/REPORT.md; research/ddp/global_coverage_20261027/h9_quadric_line_signature/REPORT.md; research/ddp/global_coverage_20261027/h9_quadric_line_rule/REPORT.md; research/ddp/global_coverage_20261027/h9_quadric_center/REPORT.md; research/ddp/global_coverage_20261027/quadric_batch/RESULT.json; research/ddp/global_coverage_20261027/h9_quadric_line_extension_pool/REPORT.md; research/ddp/global_coverage_20261027/quadric_extension/RESULT.json; research/ddp/global_coverage_20261027/quadric_anchor_completion/REPORT.md"
added: 2026-10-27T10:43:01Z
tags: ["ddp", "method-ledger"]
---

# H9整体覆盖对照：675条Q-line恢复、统一旧覆盖及343完整星上限

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (12,5)；L=42342；known_source_or_recovery n=42342

**距目标的证据：** 实际D=5，目标D=5；Existing public42342 source: inherited geometric core plus all986 sequential earlier-R4 induction checks; not a new graph or repeated full-source BFS.；已有42342图986步有序保径通过。675个分散附件全部识别为Q(6,9)奇异线像+anchors，坐标API可生成；统一旧核心→新点≤5证明完成。静态独立批充分证书及中心anchor预测失败。此结构研究另导出42343完整新图，独立新纪录节点分账。

**其他指标（保持原计数类型）：**
```json
{
  "snapshot_UTC": "2026-10-27 10:43:01 UTC",
  "known_source_order": 42342,
  "known_source_max_degree": 12,
  "new_graphs_generated": 0,
  "new_lower_bounds": 0,
  "old_full_all_source_BFS_repeated": false,
  "common_core_order": 41356,
  "common_core_edges": 234318,
  "current_extras": 986,
  "star_containing_actual": 176,
  "strict_superset_actual": 0,
  "non_star_actual": 810,
  "fixed41636_ordinary_clone_optimum": 63,
  "fixed41356_ordinary_clone_optimum": 343,
  "fixed41356_full_star_containing_count_upper_bound": 343,
  "fixed41356_all_star_total_order_upper_bound": 41699,
  "star_upper_bound_cover_rows": 287,
  "minimum_nonstar_for_current986": 643,
  "minimum_nonstar_for_target987": 644,
  "static_R4_condition_failed_vertices": 7,
  "static_pinset_pair_condition_failures": 1,
  "static_conditions_are_not_finalgraph_badpair_counts": true,
  "ordered986_failed_steps": 0,
  "ordered_tail165_failed_steps": 0,
  "P1": "REFUTED",
  "P2": "SUPPORTED_165_STEPS",
  "P3": "SUPPORTED_986_STEPS",
  "P4": "SUPPORTED_FIXED_HELPER_COUNTERFACTUAL",
  "P5": "PARTIALLY_REFUTED_one_of_two_not_independently_safe",
  "P6": "REFUTED_FIXED_TWO_HELPER_UNIVERSAL_LAYER",
  "P6_remaining_vertices": 163,
  "P6_failed_R4_vertices": 6,
  "P6_all_pinset_pair_conditions_pass": true,
  "P6_new_multisource_tests": 7,
  "P6_reused_static_R4_rows": 156,
  "LP_calls": 0,
  "MIP_calls": 0,
  "pin_optimization": false,
  "active_question": "Mathematical hit obtained; preserve mechanism evidence and complete new graph delivery/formalization in its own node.",
  "Q_line_matched_source_objects": 675,
  "Q_line_image10": 657,
  "Q_line_image7": 18,
  "Q_line_witness_uniqueness_checked": false,
  "line_api_independent_of_source_adjacency": true,
  "uniform_oldcore_to_new_bound": 5,
  "arbitrary_new_new_bound_only": 6,
  "selected_centers": 675,
  "distinct_centers": 649,
  "P8_core_set_pairs_per_condition": 227475,
  "P8_mandatory_failed_sufficient_conditions": 15639,
  "P8_full_core_attachment_failed_sufficient_conditions": 1752,
  "P8_failure_not_necessity_and_not_finalgraph_badpairs": true,
  "finite_geometric_lines_generated": 52569,
  "degree_feasible_mandatory_sets": 7,
  "P9_all_seven_mandatory_only_full_extensions_failed": true,
  "P10": "FIRST_COMPLETE_INSTANCE_FOUND_SEPARATE_RECORD",
  "resulting_new_graph_node": "exp:ddp-h9-qline-42343"
}
```



**从属变体：**
```json
[
  {
    "label": "Fixed41636 ordinary twins",
    "optimum": 63,
    "order_ceiling": 41699,
    "new_graph": false
  },
  {
    "label": "BareK full-star-containing family",
    "optimum_ordinary_clones": 343,
    "all_star_count_ceiling": 343,
    "order_ceiling": 41699,
    "new_graph": false
  },
  {
    "label": "Existing42342 ordered certificate",
    "earlier_R4_checks": 986,
    "failed_steps": 0,
    "known_source": true,
    "new_graph": false
  },
  {
    "label": "Fixedtwohelpers P6",
    "status": "REFUTED",
    "optimization": false,
    "new_multisource_tests": 7,
    "new_graph": false
  }
]
```

**原始证据：** [research/ddp/global_coverage_20261027/REPORT.md](../../research/ddp/global_coverage_20261027/REPORT.md)；[research/ddp/global_coverage_20261027/h9_relation/REPORT.md](../../research/ddp/global_coverage_20261027/h9_relation/REPORT.md)；[research/ddp/global_coverage_20261027/h9_relation/star_containment.json](../../research/ddp/global_coverage_20261027/h9_relation/star_containment.json)；[research/ddp/global_coverage_20261027/h9_bare_core_clones/REPORT.md](../../research/ddp/global_coverage_20261027/h9_bare_core_clones/REPORT.md)；[research/ddp/global_coverage_20261027/h9_bare_core_clones/integer_upper_bound.json](../../research/ddp/global_coverage_20261027/h9_bare_core_clones/integer_upper_bound.json)；[research/ddp/global_coverage_20261027/h9_bare_core_clones/STAR_CONTAINMENT_EXTENSION.json](../../research/ddp/global_coverage_20261027/h9_bare_core_clones/STAR_CONTAINMENT_EXTENSION.json)；[research/ddp/global_coverage_20261027/h9_clone_capacity/REPORT.md](../../research/ddp/global_coverage_20261027/h9_clone_capacity/REPORT.md)；[research/ddp/global_coverage_20261027/h9_global_rule/REPORT.md](../../research/ddp/global_coverage_20261027/h9_global_rule/REPORT.md)；[research/ddp/global_coverage_20261027/tail165_mechanism/PREDICTIONS.md](../../research/ddp/global_coverage_20261027/tail165_mechanism/PREDICTIONS.md)；[research/ddp/global_coverage_20261027/tail165_mechanism/RESULT.json](../../research/ddp/global_coverage_20261027/tail165_mechanism/RESULT.json)；[research/ddp/global_coverage_20261027/tail165_mechanism/P4_COUNTERFACTUAL.md](../../research/ddp/global_coverage_20261027/tail165_mechanism/P4_COUNTERFACTUAL.md)；[research/ddp/global_coverage_20261027/tail165_mechanism/P4_RESULT.json](../../research/ddp/global_coverage_20261027/tail165_mechanism/P4_RESULT.json)；[research/ddp/global_coverage_20261027/tail165_mechanism/P5_PAIR_PREDICTION.md](../../research/ddp/global_coverage_20261027/tail165_mechanism/P5_PAIR_PREDICTION.md)；[research/ddp/global_coverage_20261027/tail165_mechanism/P5_RESULT.json](../../research/ddp/global_coverage_20261027/tail165_mechanism/P5_RESULT.json)；[research/ddp/global_coverage_20261027/h9_global_rule/P6_PREDICTION.md](../../research/ddp/global_coverage_20261027/h9_global_rule/P6_PREDICTION.md)；[research/ddp/global_coverage_20261027/tail165_mechanism/P6_RESULT.json](../../research/ddp/global_coverage_20261027/tail165_mechanism/P6_RESULT.json)；[research/ddp/global_coverage_20261027/h9_line_signature/REPORT.md](../../research/ddp/global_coverage_20261027/h9_line_signature/REPORT.md)；[research/ddp/global_coverage_20261027/h9_line_pair_rule/REPORT.md](../../research/ddp/global_coverage_20261027/h9_line_pair_rule/REPORT.md)；[research/ddp/global_coverage_20261027/h9_quadric_line_signature/REPORT.md](../../research/ddp/global_coverage_20261027/h9_quadric_line_signature/REPORT.md)；[research/ddp/global_coverage_20261027/h9_quadric_line_rule/REPORT.md](../../research/ddp/global_coverage_20261027/h9_quadric_line_rule/REPORT.md)；[research/ddp/global_coverage_20261027/h9_quadric_center/REPORT.md](../../research/ddp/global_coverage_20261027/h9_quadric_center/REPORT.md)；[research/ddp/global_coverage_20261027/quadric_batch/RESULT.json](../../research/ddp/global_coverage_20261027/quadric_batch/RESULT.json)；[research/ddp/global_coverage_20261027/h9_quadric_line_extension_pool/REPORT.md](../../research/ddp/global_coverage_20261027/h9_quadric_line_extension_pool/REPORT.md)；[research/ddp/global_coverage_20261027/quadric_extension/RESULT.json](../../research/ddp/global_coverage_20261027/quadric_extension/RESULT.json)；[research/ddp/global_coverage_20261027/quadric_anchor_completion/REPORT.md](../../research/ddp/global_coverage_20261027/quadric_anchor_completion/REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Same explicit source pair41699/42342 and common K41356. Exact fixedK ordinary/full-star-containing augmentation ceiling; source-only static/ordered R4 comparisons and two frozen shortcut counterfactuals. No new optimizer, graph, old S/c rerun or local pin repair.

**正向保证：** 共同K的全部234318边精确相同，其D≤5由旧partial-fold定理继承。；287个分割预算行给出343整类上界且旧343独立克隆可行；extra anchors/new-new edges不会绕过核心完整星负载约束。；实测宽包含分类为176完整星且均exact、810 non-star；不将它们直接命名为pencils。；已有986步更早邻集R4覆盖完整更早诱导图，完整证明已有source D≤5，涵盖所有点对类型。；P4/P5保存的helper路线确实提供旧核心shortcut，区别于普通独立克隆。；675/675匹配非H9的ambientQ singularlines，657像10、18像7；完整两点坐标→line→fold-pins API可重现。；flatness与7381点壳/切超平面计数证明B(p,x)=0 iff H点距≤4；每Q-line遇p-perp，故mandatorypins保证全部旧核心五步覆盖。；675条selectedline均有唯一平面中心；632个非空image10 anchor集反驳直接中心phi-fiber规则，不换witness拟合。

**仍未完成：** 675的mandatory几何规则已恢复；源anchors仍无统一几何公式，剩余135 non-star未识别。P8只反驳静态核心充分证书，不否定新增独立点之间的互助。新42343图的全图验收与Lean在独立节点记录。

**启发与重启依据：** 实际改用Q-line全旧核心覆盖规则，649已识别中心的81线有限degree筛得到7项；固定至多2anchors精确完整覆盖得到首次新图。不再按坏对下降调参，不扩中心或加第三anchor；已转该数学成果的交付与形式化。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

