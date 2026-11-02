---
type: experiment
node_id: exp:ddp-d2-public106-internal-pin-old-edge-repair-scoped-gates-20261101
title: "新D2删补旧边主线：公开106源的4matching/指定oneRepair已闭；10..11pin内部重连唯一模型UNKNOWN"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: partial
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/SOURCE_PRED.md; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/SOURCE_RESULT.json; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/SOURCE_TERMINAL.json; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/CRITICAL_EDGE_PROFILES.json; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/MINIMAL4_PRED.md; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/MINIMAL4_PROOF.md; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/MINIMAL4_RESULT.json; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/MINIMAL4_FORCING_CERTIFICATE.json; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/MINIMAL4_TERMINAL.json; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/root_repair1_anchor_gate/PRED.md; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/root_repair1_anchor_gate/RESULT.json; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/root_repair1_anchor_gate/TERMINAL.json; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/internal_pin_rewiring/PRED.md; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/internal_pin_rewiring/run_once.py; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/internal_pin_rewiring/MODEL_SCOPE.json; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/internal_pin_rewiring/RESULT.json; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/internal_pin_rewiring/SOLVER_RETURN.json; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/internal_pin_rewiring/TERMINAL.json; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/INTERNAL_PIN_REWIRING_NOTE.md; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/structure_symmetry_sector/PRED.md; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/structure_symmetry_sector/NOTE.md; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/structure_symmetry_sector/RESULT.json; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/structure_symmetry_sector/TERMINAL.json; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/structure_symmetry_sector/BUDGET_LEDGER.json; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/sector_matching_extension/PRED.md; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/sector_matching_extension/NOTE.md; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/sector_matching_extension/RESULT.json; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/sector_matching_extension/TERMINAL.json; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/sector_matching_extension/ORDER7_GENERATOR_AND_ORBITS.json; research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/paper_S11_domination/NOTE.md"
added: 2026-11-01T17:25:38Z
tags: ["ddp", "method-ledger"]
---

# 新D2删补旧边主线：公开106源的4matching/指定oneRepair已闭；10..11pin内部重连唯一模型UNKNOWN

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (11,2)；L=106；条件性n=107（未据此计纪录）

**距目标的证据：** 用户明确希望现有D2图允许删补旧边；此前q4classic21→22适配与Brown57/91固定诱导障碍继承，旧N8/n61仍暂停。新实际11/106公开源582边，degree10点34/54、其余104点degree11；一次primary下载及5565共邻pairprofile已实际完成，不重复。MINIMAL4 forcing证书严格排4matching/noOldRepair模型，21必要候选边每条强迫未可用K={7,23,46,59}pin，0组合枚举不是抽样。指定K方向oneRepair的252anchors全有explicit oldpair反例，0pass，预测被反驳，不排一般oneRepair。随后改规则为joint选择10..11pins，只在其旧诱导图内部任意删补边，其余cross/outside旧邻接保持；6253vars/23161rows/193180nnz、唯一10秒HiGHS UNKNOWN无incumbent，case累计10.514675635/20CPU全terminal，0新图/参数/Lean。独立纸面支持闭Dom/真实degree/all mixed旧对分类必要充分，不把建模正确当可行；不一般排107，不续timer/seed。 最新sector单批0.014324454/4CPU终态、case累计10.544587884/20；7sector接口通过，但core8/10共享smallneighbors{0,31,42,55,71,82,96}，推翻signature唯一性。它们core四邻不同，不是完整twins/可自由互换；未开始5040 sector排列、未输出自同构/轨道，C7仍UNKNOWN，0solver/BFS续算/0图Lean。 后续matching传播已实际找到order7源自同构，8fixed+14个7cycles，582条源边逐一核过；case累计10.585169327/20CPU终态，首次order7即停，非完整自同构群。独立paper_S11_domination支持当前保持此C7、只改G[S]的S10/S11规则排除：S10新根至多104<107，S11源closed domination至多105<106；不把旧数值UNKNOWN改成solver已解、不一般排107。更强仅pinSET invariant而可打破内部C7的新预测未验，不能套此结论。D2新计算随用户专项检索先停，不续solver。

**其他指标（保持原计数类型）：**
```json
{
  "new_named_complete_graphs": 0,
  "new_Lean_instances": 0,
  "new_frameworks": 0,
  "independent_method_count_added": 0,
  "source_public_reproduction_not_new_graph": true,
  "source_n": 106,
  "source_m": 582,
  "source_degree_histogram": {
    "10": 2,
    "11": 104
  },
  "spare_vertices": [
    34,
    54
  ],
  "primary_URL": "https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD2/deg11_diam2_n106_adjlist.txt",
  "source_downloads": 1,
  "source_pair_profile_checks": 5565,
  "source_BFS": 0,
  "user_D2_old_edge_modification_authorized": true,
  "oldN8_n61_still_paused": true,
  "previous_q4classic21to22_and_Brown57_91_induced_scope_inherited": true,
  "minimal4": {
    "status": "EXACT_NO_MINIMAL4_MATCHING_BY_UNAVAILABLE_CRITICAL_PIN_CERTIFICATE",
    "scope": "Onlydelete4matchingoldedges awayfromT,addonevertex adjacentexactlyT+8endpoints,nootherold-oldrepair",
    "candidate_edges": 21,
    "potential_combinations": 5985,
    "combinations_enumerated": 0,
    "strict_forcing_proof": true,
    "no_general107_exclusion": true,
    "result": "research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/MINIMAL4_RESULT.json",
    "proof": "research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/MINIMAL4_PROOF.md"
  },
  "specified_K_oneRepair": {
    "status": "ALL_SPECIFIED_ONE_REPAIR_ANCHORS_REJECTED_BY_EXPLICIT_OLD_PAIR",
    "specified_first_edges": 21,
    "anchors": 252,
    "passes": 0,
    "prediction_refuted": true,
    "scope": "K={7,23,46,59}directionalanchors_5deletedmatching_plusoneoldrepair_nopin_a_k",
    "general_oneRepair_or107_excluded": false,
    "result": "research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/root_repair1_anchor_gate/RESULT.json"
  },
  "internal_pin_rewiring": {
    "status": "UNKNOWN_NO_INTEGER_CANDIDATE",
    "pin_count": [
      10,
      11
    ],
    "all_changes_only_inside_selected_pins": true,
    "cross_and_outside_edges_unchanged": true,
    "variables": 6253,
    "constraints": 23161,
    "nonzeros": 193180,
    "objective": "minactualoldedgeeditcount",
    "solver_calls": 1,
    "solver_wall_limit": 10,
    "integer_incumbent": false,
    "case_CPU": 10.514675635000001,
    "case_budget": 20,
    "terminal": true,
    "exact_interface_independent_paper_SUPPORTED": true,
    "independent_note": "research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/INTERNAL_PIN_REWIRING_NOTE.md",
    "infeasibility_or_whole_family_exclusion_claimed": false,
    "no_timer_restart": true,
    "new_graph": 0
  },
  "parent_ideas": [
    "ddp-d2-brown91-cap11-fixed-induced-arbitrary-helper-order106-bound-20261101"
  ],
  "portfolio_parameter_Lean_method_increment": [
    0,
    0,
    0,
    0
  ],
  "structure_symmetry_sector_once": {
    "status": "SECTOR_SIGNATURE_INTERFACE_REFUTED",
    "passed_interface": "seven disjoint sectors each one vertex per smallcolor",
    "refuted_prediction": "core_small_signature_uniquely_determines_image",
    "core_counterexample": [
      8,
      10
    ],
    "common_small_neighbors": [
      0,
      31,
      42,
      55,
      71,
      82,
      96
    ],
    "fixed_order_sector_signature": [
      0,
      6,
      2,
      5,
      4,
      3,
      1
    ],
    "not_complete_open_twins": true,
    "other_core_neighbors_differ": true,
    "batch_CPU": 0.014324454,
    "batch_budget": 4,
    "case_cumulative_CPU": 10.544587884000002,
    "case_budget": 20,
    "terminal": true,
    "sector_permutations5040_enumerated": 0,
    "no_generator_returned": true,
    "C7": "UNKNOWN",
    "no_general_isomorphism_or_orbit_claim": true,
    "solver_BFS_source_retests": 0,
    "new_graph_Lean": 0,
    "no_automatic_continuation": true,
    "note": "research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/structure_symmetry_sector/NOTE.md",
    "later_status": "SUPERSEDED_ONLY_C7_UNKNOWN_BY_ACTUAL_ORDER7_WITNESS_PRIOR_SIGNATURE_COUNTEREXAMPLE_PRESERVED"
  },
  "sector_matching_extension_actual": {
    "status": "ORDER7_AUTOMORPHISM_FOUND",
    "generator_order": 7,
    "fixed_vertices": [
      7,
      17,
      23,
      34,
      46,
      54,
      59,
      105
    ],
    "orbit_histogram": {
      "1": 8,
      "7": 14
    },
    "full_source_edges_per_permutation_checked": 582,
    "accepted_permutations": 3,
    "tested_sector_prefix": 1026,
    "full_sector_enumeration": false,
    "first_order7_stop": true,
    "no_full_automorphism_group_claim": true,
    "batch_CPU": 0.021510295999999998,
    "case_cumulative_CPU": 10.585169327000003,
    "case_budget": 20,
    "all_processes_terminal": true,
    "no_BFS_or_solver": true,
    "note": "research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/sector_matching_extension/NOTE.md"
  },
  "C7_preserving_internal_S10_S11_paper_exclusion": {
    "status": "INDEPENDENT_PAPER_SUPPORTED_SCOPED_EXCLUSION",
    "source": [
      11,
      2,
      106
    ],
    "target_order": 107,
    "pin_sizes": [
      10,
      11
    ],
    "fixed_scope": "preserve_this_actual_C7_fix_new_z_change_only_old_edges_inside_invariant_S",
    "S10_newroot_upper": 104,
    "S11_closed_domination_upper": 105,
    "required_source_order": 106,
    "earlier_numerical_MILP_UNKNOWN_not_rewritten": true,
    "general107_excluded": false,
    "noninvariant_pins_or_symmetry_breaking_or_cross_S_edits_not_excluded": true,
    "stronger_pinset_only_prediction": "UNTESTED_AT_THIS_SYNC_NOT_A_CONCLUSION",
    "note": "research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/paper_S11_domination/NOTE.md"
  },
  "current_research_execution": {
    "status": "D2_NEW_COMPUTATION_PAUSED_FOR_USER_PUBLIC_SEARCH_NO_SOLVER_CONTINUATION",
    "oldN8_n61_still_paused": true,
    "no_timer_seed_or_model_continuation": true,
    "new_graph_parameter_Lean_method_increments": [
      0,
      0,
      0,
      0
    ]
  }
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/SOURCE_PRED.md](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/SOURCE_PRED.md)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/SOURCE_RESULT.json](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/SOURCE_RESULT.json)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/SOURCE_TERMINAL.json](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/SOURCE_TERMINAL.json)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/CRITICAL_EDGE_PROFILES.json](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/CRITICAL_EDGE_PROFILES.json)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/MINIMAL4_PRED.md](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/MINIMAL4_PRED.md)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/MINIMAL4_PROOF.md](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/MINIMAL4_PROOF.md)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/MINIMAL4_RESULT.json](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/MINIMAL4_RESULT.json)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/MINIMAL4_FORCING_CERTIFICATE.json](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/MINIMAL4_FORCING_CERTIFICATE.json)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/MINIMAL4_TERMINAL.json](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/MINIMAL4_TERMINAL.json)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/root_repair1_anchor_gate/PRED.md](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/root_repair1_anchor_gate/PRED.md)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/root_repair1_anchor_gate/RESULT.json](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/root_repair1_anchor_gate/RESULT.json)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/root_repair1_anchor_gate/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/root_repair1_anchor_gate/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/internal_pin_rewiring/PRED.md](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/internal_pin_rewiring/PRED.md)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/internal_pin_rewiring/run_once.py](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/internal_pin_rewiring/run_once.py)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/internal_pin_rewiring/MODEL_SCOPE.json](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/internal_pin_rewiring/MODEL_SCOPE.json)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/internal_pin_rewiring/RESULT.json](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/internal_pin_rewiring/RESULT.json)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/internal_pin_rewiring/SOLVER_RETURN.json](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/internal_pin_rewiring/SOLVER_RETURN.json)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/internal_pin_rewiring/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/internal_pin_rewiring/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/INTERNAL_PIN_REWIRING_NOTE.md](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/INTERNAL_PIN_REWIRING_NOTE.md)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/structure_symmetry_sector/PRED.md](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/structure_symmetry_sector/PRED.md)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/structure_symmetry_sector/NOTE.md](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/structure_symmetry_sector/NOTE.md)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/structure_symmetry_sector/RESULT.json](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/structure_symmetry_sector/RESULT.json)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/structure_symmetry_sector/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/structure_symmetry_sector/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/structure_symmetry_sector/BUDGET_LEDGER.json](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/structure_symmetry_sector/BUDGET_LEDGER.json)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/sector_matching_extension/PRED.md](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/sector_matching_extension/PRED.md)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/sector_matching_extension/NOTE.md](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/sector_matching_extension/NOTE.md)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/sector_matching_extension/RESULT.json](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/sector_matching_extension/RESULT.json)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/sector_matching_extension/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/sector_matching_extension/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/sector_matching_extension/ORDER7_GENERATOR_AND_ORBITS.json](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/sector_matching_extension/ORDER7_GENERATOR_AND_ORBITS.json)；[research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/paper_S11_domination/NOTE.md](../../research/ddp/two_successful_methods_20261101/d2_record106_edge_repair/paper_S11_domination/NOTE.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 仅实际public106/582 max11D2源的已授权删补旧边改造；minimal4matching/noOldRepair、限定K方向oneRepair anchors、联合选10..11pins并仅重连S内部三个精确子域分账；非Brown91固定诱导图，不是一般107无解。

**仍未完成：** Actual107graphnotfound;internalpinrewiringUNKNOWN;otheroldedgechangesandgeneral107remainopen.

**启发与重启依据：** 已授权D2新主线允许改旧边，不能再套旧固定诱导Brown障碍。minimal4 forcing揭示oldpairs与新pin的竞争义务，oneRepair指定anchor仍不能兼顾旧端点路线，故改成pin集内部联合重连；一次数值UNKNOWN保留，后续需root依据新结构决定，不自动穷举新pins/seed或续timer。此源106公开复现0成果、三个试验同一机制0newmethod，不重启旧N8/n61或旧D2适配。 新sector反例只关闭“small-signature唯一强迫”接口，不能从restrictedsignature相同推出全图twins或合法symmetry。C7未排但不自动做5040枚举/同构/solver，case原20CPU不重置；下一结构区分需root另作有依据决定。 实际order7替代此前C7UNKNOWN，但旧small-signature唯一性反例保留。纸面界改变下一步：停止此C7-preserving内部S10/S11规则；非对称pin/跨S改边/其它模型未被关闭，不能自动扩大排除或启动solver。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

