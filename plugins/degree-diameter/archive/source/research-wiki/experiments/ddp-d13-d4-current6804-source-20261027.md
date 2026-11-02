---
type: experiment
node_id: exp:ddp-d13-d4-current6804-source-20261027
title: "(13,4)6804源：完整<=6中央匹配hub模型UNKNOWN，split与固定小域已闭"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d13_D4_current6804/REPORT.md; research/ddp/more_graphs_20261027/d13_D4_current6804/RESULT.json; research/ddp/refresh_20261029/d13_D4_six_matching_hub/DISTANCES_TO_T.json; research/ddp/refresh_20261029/d13_D4_six_matching_hub/PARAMETERS.json; research/ddp/refresh_20261029/d13_D4_six_matching_hub/PREDICTION.md; research/ddp/refresh_20261029/d13_D4_six_matching_hub/REPORT.md; research/ddp/refresh_20261029/d13_D4_six_matching_hub/RESULT.json; research/ddp/refresh_20261029/d13_D4_six_matching_hub/TERMINAL.json; research/ddp/refresh_20261029/d13_D4_six_matching_hub/first_gate.py; research/ddp/refresh_20261029/d13_D4_six_matching_hub/one_line_edge_extension/CASES.jsonl; research/ddp/refresh_20261029/d13_D4_six_matching_hub/one_line_edge_extension/INPUT.json; research/ddp/refresh_20261029/d13_D4_six_matching_hub/one_line_edge_extension/PREDICTION.md; research/ddp/refresh_20261029/d13_D4_six_matching_hub/one_line_edge_extension/REPORT.md; research/ddp/refresh_20261029/d13_D4_six_matching_hub/one_line_edge_extension/RESULT.json; research/ddp/refresh_20261029/d13_D4_six_matching_hub/one_line_edge_extension/TERMINAL.json; research/ddp/refresh_20261029/d13_D4_six_matching_hub/one_line_edge_extension/gate.py; research/ddp/refresh_20261029/d13_D4_vertex_split_geodesic/PREDICTION.md; research/ddp/refresh_20261029/d13_D4_vertex_split_geodesic/REPORT.md; research/ddp/refresh_20261029/d13_D4_vertex_split_geodesic/RESULT.json; research/ddp/refresh_20261029/d13_D4_vertex_split_geodesic/ROOTS.jsonl; research/ddp/refresh_20261029/d13_D4_vertex_split_geodesic/TERMINAL.json; research/ddp/refresh_20261029/d13_D4_vertex_split_geodesic/check_supports.py; research/ddp/refresh_20261029/HUB_SPLIT_COMPLETED_WIKI_REPORT.md; research/ddp/refresh_20261029/d13_D4_joint_matching_hub/HANDLE.json; research/ddp/refresh_20261029/d13_D4_joint_matching_hub/MODEL.json; research/ddp/refresh_20261029/d13_D4_joint_matching_hub/PREDICTION.md; research/ddp/refresh_20261029/d13_D4_joint_matching_hub/REPORT.md; research/ddp/refresh_20261029/d13_D4_joint_matching_hub/RESULT.json; research/ddp/refresh_20261029/d13_D4_joint_matching_hub/SELECTORS.tsv; research/ddp/refresh_20261029/d13_D4_joint_matching_hub/TERMINAL.json; research/ddp/refresh_20261029/d13_D4_joint_matching_hub/check_candidate.cpp; research/ddp/refresh_20261029/d13_D4_joint_matching_hub/prepare.cpp; research/ddp/refresh_20261029/d13_D4_joint_matching_hub/run_once.py; research/ddp/refresh_20261029/JOINT_HUB_CONTROLLER33_WIKI_REPORT.md"
added: 2026-10-29T20:58:06Z
tags: ["ddp", "method-ledger"]
---

# (13,4)6804源：完整<=6中央匹配hub模型UNKNOWN，split与固定小域已闭

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (13,4)；L=6804；known_source_or_recovery n=6804

**距目标的证据：** 实际simple6804/44226，全13regular、free0、minSatN13；84个81fiber均independent。额外3402反射matching边连接controller g与g+42（非平凡中心y^6），坐标x→−x+(0,0,1,0)，均跨42对不同fiber，非fiber内部匹配。；固定M6端点R3漏312/tmax4，首22距拟hub5；其单额外线边完整144全失败、单q至多补81/312；81fiber代表全部有singleton geodesic支持，故当前6804源全部相邻单点split失败，无需枚4096划分。0新图。；完整3402选择器/<=6中央边模型30618变量/2119435子句唯一60秒调用UNKNOWN，solver60.029439CPU/总62.967105CPU，round1，无SAT选择/候选/旧pair反例cut；已停止，不继续写prep或running。

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 6804,
  "source_m": 44226,
  "degree13": 6804,
  "free_vertices": 0,
  "matching_edges": 3402,
  "paired_fibers": 42,
  "intrafiber_edges": 0,
  "profile_CPU": 0.132924,
  "odd_internalmatching_prediction": "REFUTED",
  "BFS": 0,
  "fixed6_hub_new_root_gate": "FAILED_312_GAPS",
  "fixed6_one_line144_pass": 0,
  "all_current_adjacent_vertex_splits_excluded": true,
  "adjacent_split_representatives_completed": 81,
  "new_graphs": 0,
  "arbitrary_joint_matching_question_status": "UNKNOWN_TERMINAL",
  "arbitrary_joint_matching_solver_calls_recorded": 1,
  "arbitrary_joint_matching_solver_CPU_seconds": 60.029439,
  "arbitrary_joint_matching_total_CPU_seconds": 62.967105000000004,
  "arbitrary_joint_matching_actual_candidate_checks": 0,
  "arbitrary_joint_matching_CEG_cuts": 0
}
```



**从属变体：**
```json
[
  {
    "label": "fixed_six_central_matching_edges_common_hub_20261029",
    "status": "REJECTED_NEW_ROOT_DISTANCE_GATE",
    "source_n": 6804,
    "source_m": 44226,
    "source_degree": 13,
    "proposed_n": 6805,
    "removed_matching_edges": 6,
    "endpoints": 12,
    "fixed_fiber": [
      0,
      0,
      2,
      0
    ],
    "fixed_fiber_code": 18,
    "t_max": 4,
    "distance_histogram": {
      "0": 12,
      "1": 144,
      "2": 1404,
      "3": 4932,
      "4": 312
    },
    "missing_R3": 312,
    "witness": 22,
    "witness_distance_to_T": 4,
    "prospective_hub_distance": 5,
    "shortest_path_to_T": [
      22,
      6525,
      67,
      723,
      18
    ],
    "exact_scope": "Only the frozen a^k orbit, xstar and six central matching edges.",
    "source_multisource_BFS": 1,
    "source_allroot_revalidation": 0,
    "candidate_graphs_generated": 0,
    "candidate_BFS": 0,
    "old_old_candidate_distances_checked": false,
    "CPU_seconds": 0.056620988,
    "hub_distance_lemma": "If all removed edges have both endpoints in T, d_(G-M)(x,T)=d_G(x,T): a shortest path to T cannot use a removed edge before reaching T. A new hub joined only to T has distance1+d_G(x,T). This says nothing by itself about old-old candidate distances."
  },
  {
    "label": "fixed_six_matching_hub_one_additional_line_edge_all144_20261029",
    "status": "COMPLETE_NO_NEW_ROOT_PASS",
    "fixed_matching_unchanged": true,
    "raw_T_to_external_line_edges": 144,
    "distinct_external_q": 144,
    "completed": 144,
    "passing": 0,
    "existing_R3_gaps": 312,
    "maximum_gaps_covered_by_one_q": 81,
    "minimum_gaps_remaining": 231,
    "source_radius3_checks": 144,
    "original_multisource_BFS_repeated": 0,
    "candidate_graphs_generated": 0,
    "candidate_BFS": 0,
    "CPU_seconds": 0.116250719,
    "exact_scope": "Keep frozen M6; delete one additional original line edge v-q withv inT,q outsideT, and joinq to same hub. No otherM or second line edge.",
    "other_matching_hubs_excluded": false
  },
  {
    "label": "all_current6804_adjacent_single_vertex_splits_geodesic_singletons_20261029",
    "status": "COMPLETE_NO_ADJACENT_SPLIT",
    "source_n": 6804,
    "source_degree": 13,
    "representative_roots": 81,
    "completed": 81,
    "singleton_rejections": 81,
    "literal_roots_covered_by_left_controller_action": 6804,
    "singleton_targets_per_root_min": 1080,
    "singleton_targets_per_root_max": 1121,
    "example": {
      "root": 0,
      "target": 19,
      "sole_first_neighbor": 3411,
      "path": [
        0,
        3411,
        1164,
        4605,
        19
      ]
    },
    "partition_assignment_domain_if_needed": 4096,
    "actual_partition_assignments_tested": 0,
    "geodesic_support_BFS": 81,
    "candidate_graphs_generated": 0,
    "candidate_BFS": 0,
    "CPU_seconds": 0.5895588940000001,
    "split_lemma": "For old distance4 target t, every <=4 path from either split side must avoid the new internal split edge; otherwise contraction gives an old path<=3. Thus all old geodesic first-neighbor supports must meet both color classes; a singleton rejects every partition.",
    "exact_scope": "Retain allG-v edges; partition all13 oldneighbors between two adjacent split vertices. Currentliteral source only.",
    "other_sources_or_multi_vertex_edits_excluded": false
  },
  {
    "label": "arbitrary_at_most6_central_matching_hub_joint_selection_question_20261029",
    "status": "UNKNOWN",
    "record_type": "completed_bounded_full_selector_necessary_model",
    "source_n": 6804,
    "maximum_selected_matching_edges": 6,
    "matching_selectors": 3402,
    "complete_selector_scope": true,
    "full_D4_conditions_encoded": false,
    "target_R3_cover_clauses": 6804,
    "cover_literals": 9221688,
    "C2_variables": 6804,
    "C2_equivalence_selector_incidence": 950292,
    "representative_support_roots": 81,
    "representative_critical_pairs": 13230,
    "expanded_critical_implication_cuts": 1111320,
    "variables": 30618,
    "clauses": 2119435,
    "literals": 14407522,
    "solver_rounds": 1,
    "solver_exit_code": 0,
    "solver_aggregate_CPU_seconds": 60.029439,
    "aggregate_CPU_seconds": 62.967105000000004,
    "actual_candidate_checks": 0,
    "generated_candidate_graphs": 0,
    "exact_old_pair_CEG_cuts": 0,
    "selected_matching_solution_returned": false,
    "running": false,
    "solver_handle_recorded": true,
    "mathematical_exclusion_recorded": false,
    "scope_note": "All3402 central matching selectors and<=6 budget, with complete endpointR3 and proved necessary C2 implications; not a complete old-old distance model.",
    "stopped_no_automatic_timer_continuation": true
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/d13_D4_current6804/REPORT.md](../../research/ddp/more_graphs_20261027/d13_D4_current6804/REPORT.md)；[research/ddp/more_graphs_20261027/d13_D4_current6804/RESULT.json](../../research/ddp/more_graphs_20261027/d13_D4_current6804/RESULT.json)；[research/ddp/refresh_20261029/d13_D4_six_matching_hub/DISTANCES_TO_T.json](../../research/ddp/refresh_20261029/d13_D4_six_matching_hub/DISTANCES_TO_T.json)；[research/ddp/refresh_20261029/d13_D4_six_matching_hub/PARAMETERS.json](../../research/ddp/refresh_20261029/d13_D4_six_matching_hub/PARAMETERS.json)；[research/ddp/refresh_20261029/d13_D4_six_matching_hub/PREDICTION.md](../../research/ddp/refresh_20261029/d13_D4_six_matching_hub/PREDICTION.md)；[research/ddp/refresh_20261029/d13_D4_six_matching_hub/REPORT.md](../../research/ddp/refresh_20261029/d13_D4_six_matching_hub/REPORT.md)；[research/ddp/refresh_20261029/d13_D4_six_matching_hub/RESULT.json](../../research/ddp/refresh_20261029/d13_D4_six_matching_hub/RESULT.json)；[research/ddp/refresh_20261029/d13_D4_six_matching_hub/TERMINAL.json](../../research/ddp/refresh_20261029/d13_D4_six_matching_hub/TERMINAL.json)；[research/ddp/refresh_20261029/d13_D4_six_matching_hub/first_gate.py](../../research/ddp/refresh_20261029/d13_D4_six_matching_hub/first_gate.py)；[research/ddp/refresh_20261029/d13_D4_six_matching_hub/one_line_edge_extension/CASES.jsonl](../../research/ddp/refresh_20261029/d13_D4_six_matching_hub/one_line_edge_extension/CASES.jsonl)；[research/ddp/refresh_20261029/d13_D4_six_matching_hub/one_line_edge_extension/INPUT.json](../../research/ddp/refresh_20261029/d13_D4_six_matching_hub/one_line_edge_extension/INPUT.json)；[research/ddp/refresh_20261029/d13_D4_six_matching_hub/one_line_edge_extension/PREDICTION.md](../../research/ddp/refresh_20261029/d13_D4_six_matching_hub/one_line_edge_extension/PREDICTION.md)；[research/ddp/refresh_20261029/d13_D4_six_matching_hub/one_line_edge_extension/REPORT.md](../../research/ddp/refresh_20261029/d13_D4_six_matching_hub/one_line_edge_extension/REPORT.md)；[research/ddp/refresh_20261029/d13_D4_six_matching_hub/one_line_edge_extension/RESULT.json](../../research/ddp/refresh_20261029/d13_D4_six_matching_hub/one_line_edge_extension/RESULT.json)；[research/ddp/refresh_20261029/d13_D4_six_matching_hub/one_line_edge_extension/TERMINAL.json](../../research/ddp/refresh_20261029/d13_D4_six_matching_hub/one_line_edge_extension/TERMINAL.json)；[research/ddp/refresh_20261029/d13_D4_six_matching_hub/one_line_edge_extension/gate.py](../../research/ddp/refresh_20261029/d13_D4_six_matching_hub/one_line_edge_extension/gate.py)；[research/ddp/refresh_20261029/d13_D4_vertex_split_geodesic/PREDICTION.md](../../research/ddp/refresh_20261029/d13_D4_vertex_split_geodesic/PREDICTION.md)；[research/ddp/refresh_20261029/d13_D4_vertex_split_geodesic/REPORT.md](../../research/ddp/refresh_20261029/d13_D4_vertex_split_geodesic/REPORT.md)；[research/ddp/refresh_20261029/d13_D4_vertex_split_geodesic/RESULT.json](../../research/ddp/refresh_20261029/d13_D4_vertex_split_geodesic/RESULT.json)；[research/ddp/refresh_20261029/d13_D4_vertex_split_geodesic/ROOTS.jsonl](../../research/ddp/refresh_20261029/d13_D4_vertex_split_geodesic/ROOTS.jsonl)；[research/ddp/refresh_20261029/d13_D4_vertex_split_geodesic/TERMINAL.json](../../research/ddp/refresh_20261029/d13_D4_vertex_split_geodesic/TERMINAL.json)；[research/ddp/refresh_20261029/d13_D4_vertex_split_geodesic/check_supports.py](../../research/ddp/refresh_20261029/d13_D4_vertex_split_geodesic/check_supports.py)；[research/ddp/refresh_20261029/HUB_SPLIT_COMPLETED_WIKI_REPORT.md](../../research/ddp/refresh_20261029/HUB_SPLIT_COMPLETED_WIKI_REPORT.md)；[research/ddp/refresh_20261029/d13_D4_joint_matching_hub/HANDLE.json](../../research/ddp/refresh_20261029/d13_D4_joint_matching_hub/HANDLE.json)；[research/ddp/refresh_20261029/d13_D4_joint_matching_hub/MODEL.json](../../research/ddp/refresh_20261029/d13_D4_joint_matching_hub/MODEL.json)；[research/ddp/refresh_20261029/d13_D4_joint_matching_hub/PREDICTION.md](../../research/ddp/refresh_20261029/d13_D4_joint_matching_hub/PREDICTION.md)；[research/ddp/refresh_20261029/d13_D4_joint_matching_hub/REPORT.md](../../research/ddp/refresh_20261029/d13_D4_joint_matching_hub/REPORT.md)；[research/ddp/refresh_20261029/d13_D4_joint_matching_hub/RESULT.json](../../research/ddp/refresh_20261029/d13_D4_joint_matching_hub/RESULT.json)；[research/ddp/refresh_20261029/d13_D4_joint_matching_hub/SELECTORS.tsv](../../research/ddp/refresh_20261029/d13_D4_joint_matching_hub/SELECTORS.tsv)；[research/ddp/refresh_20261029/d13_D4_joint_matching_hub/TERMINAL.json](../../research/ddp/refresh_20261029/d13_D4_joint_matching_hub/TERMINAL.json)；[research/ddp/refresh_20261029/d13_D4_joint_matching_hub/check_candidate.cpp](../../research/ddp/refresh_20261029/d13_D4_joint_matching_hub/check_candidate.cpp)；[research/ddp/refresh_20261029/d13_D4_joint_matching_hub/prepare.cpp](../../research/ddp/refresh_20261029/d13_D4_joint_matching_hub/prepare.cpp)；[research/ddp/refresh_20261029/d13_D4_joint_matching_hub/run_once.py](../../research/ddp/refresh_20261029/d13_D4_joint_matching_hub/run_once.py)；[research/ddp/refresh_20261029/JOINT_HUB_CONTROLLER33_WIKI_REPORT.md](../../research/ddp/refresh_20261029/JOINT_HUB_CONTROLLER33_WIKI_REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 实际simple6804/44226，全13regular、free0、minSatN13；84个81fiber均independent。额外3402反射matching边连接controller g与g+42（非平凡中心y^6），坐标x→−x+(0,0,1,0)，均跨42对不同fiber，非fiber内部匹配。；追加固定六中央匹配边共hub、固定M6加一条T到外部线边全144项，以及81代表覆盖全源的相邻单点split首步门。任意<=6中央匹配完整选择器必要模型已实际唯一调用UNKNOWN，不是整族排除。

**仍未完成：** 保边append已因全正则阻断；本固定hub/单线域与全部当前source相邻单点split已按精确范围关闭。其它matching选择、其它改边、多点改造和一般(13,4)仍开放。

**启发与重启依据：** 不能只因81奇数就假定84个未匹配spares：controller中心平移消除了fixedfiber。当前cap13保全部旧边增点/多helper没有接口，未跑R3/BFS或SAT。固定真实source与旧84-controllerquarticNB模型分层，不泛排修改controller/删边。；固定M和单线补端点域停止，不据局部少缺项换seed。相邻split的singleton是整root全部划分障碍，由left controllerAut覆盖所有6804顶点。其它matching hub与多点改造仍开放；任意<=6中央M共同覆盖模型已有一次真实UNKNOWN，无候选；停止该批，不自动续timer或下一CEG轮，不将必要条件建模完整误当真正D4整族排除。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._



<!-- TWO6804_POINT_OVERLAP_FOLLOWUP_20261102 -->
## 2026-11-02 两副本only-crossmatching后续与profile更正

[实际point-overlap终态](ddp-d14d4-two6804-only-cross-arbitrary-matching-point-overlap-complete-no-20261102.md)：固定source两copy保全部旧边，只加任意全/部分crossmatching均不能D4。全6804新R2/R3给B2max154/S2max140/B3max1588/S3max1434；旧root0的(1,13,138,1400,5252)不能当uniform，6860旧预测不用于证明。正确6984−260=6724<6804。此后续不依赖sourceAut/源D4假设，不覆盖本节点旧hub/split/允许oldold操作的全部范围；旧UNKNOWN原样保留。无新source验收/图/Lean。
