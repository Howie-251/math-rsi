---
type: experiment
node_id: exp:ddp-f4-nucleus-c4-conic-routes-general-quotient-hall-c72-20261101
title: "F4 nucleus-C4新路线接口与72控制器Hall障碍：conic/general quotient及70点手术同节点记账"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/PRED.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/RESULT.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/REPORT.md; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/MECHANISM_PROOF.md; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/MECHANISM_CHECK_RESULT.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/GENERAL_QUOTIENT_INTERFACE.md; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/DOMAIN_CHECK.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/PREPROCESS_RESULT.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/GATE_PROOF.md; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/SEMILINEAR_MAPS.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/TERMINAL.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/Exoo72/HALL_OBSTRUCTION.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/Exoo72/UNIQUE_ROUTE_GATE.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/Michel72/HALL_OBSTRUCTION.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/Michel72/UNIQUE_ROUTE_GATE.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/general_quotient_relaxation/PRED.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/general_quotient_relaxation/RESULT.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/general_quotient_relaxation/PROOF.md; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/general_quotient_relaxation/QUOTIENT_BINDING.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/general_quotient_relaxation/Exoo72/MINIMAL_HALL_CERTIFICATE.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/general_quotient_relaxation/Michel72/MINIMAL_HALL_CERTIFICATE.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/PRED.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/PREFLIGHT_RESULT.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/BOUNDARY_CERTIFICATE.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/RESULT.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/TERMINAL.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/SURVIVOR_OUTCOMES.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/ONE_TARGETED_FAILURE_CHECK.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/PROOF.md; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/REPORT.md; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/STRUCTURAL_CROSS_OBSTRUCTION.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/PRED.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/RESULT.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/PROOF.md; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/REPORT.md; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/TERMINAL.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/BOUNDARY_ATTEMPTS.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/H_BOUNDARY_CACHE.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/OLD_CROSS_ARGUMENT_ESCAPE_EXAMPLE.json; research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/check_once.py"
added: 2026-11-01T06:31:21Z
tags: ["ddp", "method-ledger"]
---

# F4 nucleus-C4新路线接口与72控制器Hall障碍：conic/general quotient及70点手术同节点记账

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** controller

**目标与阶数：** (22,3)；L=不适用／见变体；条件性n=4608（未据此计纪录）；从属目标：[[22, 3]]

**距目标的证据：** Conditional72×F4^3 order4608/degree22 route theorem, no4608 fiber graph. FixedExoo72/Michel72 map gates strictly fail.70point surgery returned zeroD3controller and zero4480fiber graph.；新增fiber内部N,wN的C4使conic-symmetry真逆规则在controllerdistance0/1/2自动覆全64；D3 iff controllerD3且每distance3pair有goodrank word。任意数量bad conicsecants都漏非零N(全部10面的union61)，不再依赖≤4word门。proof-only CPU0.032770784不读controller。实际120conic semilinear maps/每portpair24，Exoo72/Michel72各72/108middleedges空。释放到全部120个五点quotient bijections后旧Exoo0→51修成12，但另外24edges空；Michel36空，CPU0.098530715。无SAT/360map生成/D0D2求解/fiber图。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_Lean_instances": 0,
  "new_independent_frameworks": 0,
  "new_lower_bound_mathematically_verified": false,
  "conditional_route_characterization_paper": true,
  "conditional_route_theorem_Lean": false,
  "hypothetical_controller_order": 72,
  "hypothetical_fiber_order": 64,
  "hypothetical_graph_order": 4608,
  "hypothetical_graph_degree": 22,
  "internal_fiber_generators": [
    "N",
    "wN"
  ],
  "cross_degree": 20,
  "proof_only_CPU_seconds": 0.032770784,
  "proof_only_controller_inputs_read": false,
  "conic_semilinear_maps": 120,
  "conic_maps_per_portpair": 24,
  "conic_empty_edges": {
    "Exoo72": 72,
    "Michel72": 108
  },
  "general_quotient_permutations_per_edge": 120,
  "general_quotient_empty_edges": {
    "Exoo72": 24,
    "Michel72": 36
  },
  "old_Exoo0to51_repaired_domain": 12,
  "general_quotient_CPU_seconds": 0.098530715,
  "general_quotient_gate_only_unique_distance3_rank_necessity": true,
  "general_allbadN_argument_used": false,
  "general_quotient_includes_shears_scales_and_offsets_necessary_scope": true,
  "split360_map_generation": 0,
  "D0_D2_numeric_search": 0,
  "solver_calls": 0,
  "fiber_graphs": 0,
  "Lean_calls": 0,
  "general70_oldold_edge_repair_scope_closed": true
}
```



**从属变体：**
```json
[
  {
    "label": "Exoo72_adjacent_pair_delete_plus_four_crossmatching_controller70",
    "target": [
      22,
      3
    ],
    "hypothetical_n": 4480,
    "status": "COMPLETE_SURGERY_NO_CONTROLLER_D3",
    "source_edges": 180,
    "matchings_per_edge": 24,
    "parameter_assignments": 4320,
    "assignments_are_not_distinct_graph_count": true,
    "boundary_failures": 4008,
    "boundary_survivors": 312,
    "existing_H_le3_terms_retained": true,
    "all_survivors_processed": true,
    "literal_simple5regular_checked": 312,
    "new_D3_controllers": 0,
    "new_fiber_graphs": 0,
    "SAT_calls": 0,
    "old_source_BFS": 0,
    "preflight_CPU_seconds": 0.112039755,
    "survivor_stage_CPU_seconds": 0.053327988,
    "total_measured_CPU_seconds": 0.165369792,
    "CPU_budget": 20,
    "scope": "Only literalExoo72 delete an adjacentpair then add one crossperfectmatching between the remaining4+4neighbors. Other70controllers/surgeries open; Hall stages receive noD3survivor.",
    "structural_status": "ALL180_DELETED_EDGES_HAVE_INCOMPATIBLE_UNIQUE_CROSS_PAIRS",
    "all4320_matchings_structurally_excluded": true,
    "unique_cross_pair_count_histogram": {
      "3": 24,
      "6": 132,
      "9": 24
    },
    "each_deleted_edge_has_two_unique_cross_pairs_sharing_boundary_vertex": true,
    "required_matching_degree_at_one_vertex": 2,
    "available_matching_degree": 1,
    "structural_CPU_seconds": 0.028433571,
    "structural_controller_BFS_or_shortword_recomputation": 0
  },
  {
    "label": "Exoo72_adjacent_pair_delete_all_oldold_edge_repairs_under_max5",
    "target": [
      22,
      3
    ],
    "hypothetical_n": 4480,
    "status": "COMPLETE_ALL105_MATCHINGS_NO_D3_CONTROLLER",
    "inherited_purecross_assignments_not_rerun": 4320,
    "new_assignments_evaluated": 14580,
    "combined_assignments": 18900,
    "source_edges": 180,
    "total_perfect_matchings_per_edge": 105,
    "new_matching_types_per_edge": 81,
    "partial_matching_WLOG_complete": true,
    "all28_boundarypair_gate_fail": true,
    "boundary_survivors": 0,
    "new_controller_full_R3_checks": 0,
    "new_D3_controllers": 0,
    "new_fiber_graphs": 0,
    "solver_calls": 0,
    "new_Lean": 0,
    "total_CPU_seconds": 0.25110093,
    "CPU_budget_seconds": 15,
    "old_source_BFS": 0,
    "scope": "FixedExoo72 deleteadjacenttwo, retainallH, add arbitrary oldoldedges undercap5; all partialmatchings onindependent8boundary extend toperfectmatching. Not nonadjacentdeletion,delete4,othercontrollers,rewiringretainedH or general70controllers.",
    "old_cross_proof_not_extended": true,
    "old_cross_proof_escape_example": {
      "deleted": [
        0,
        45
      ],
      "old_unique_pair": [
        51,
        18
      ],
      "new_matching": [
        [
          51,
          59
        ],
        [
          62,
          71
        ],
        [
          15,
          18
        ],
        [
          56,
          58
        ]
      ],
      "new_path": [
        51,
        59,
        36,
        18
      ],
      "not_directly_matched": true,
      "another_boundary_pair_fails": [
        51,
        62
      ]
    }
  }
]
```

**原始证据：** [research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/PRED.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/PRED.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/RESULT.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/RESULT.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/REPORT.md](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/REPORT.md)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/MECHANISM_PROOF.md](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/MECHANISM_PROOF.md)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/MECHANISM_CHECK_RESULT.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/MECHANISM_CHECK_RESULT.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/GENERAL_QUOTIENT_INTERFACE.md](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/GENERAL_QUOTIENT_INTERFACE.md)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/DOMAIN_CHECK.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/DOMAIN_CHECK.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/PREPROCESS_RESULT.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/PREPROCESS_RESULT.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/GATE_PROOF.md](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/GATE_PROOF.md)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/SEMILINEAR_MAPS.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/SEMILINEAR_MAPS.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/Exoo72/HALL_OBSTRUCTION.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/Exoo72/HALL_OBSTRUCTION.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/Exoo72/UNIQUE_ROUTE_GATE.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/Exoo72/UNIQUE_ROUTE_GATE.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/Michel72/HALL_OBSTRUCTION.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/Michel72/HALL_OBSTRUCTION.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/Michel72/UNIQUE_ROUTE_GATE.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/Michel72/UNIQUE_ROUTE_GATE.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/general_quotient_relaxation/PRED.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/general_quotient_relaxation/PRED.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/general_quotient_relaxation/RESULT.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/general_quotient_relaxation/RESULT.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/general_quotient_relaxation/PROOF.md](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/general_quotient_relaxation/PROOF.md)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/general_quotient_relaxation/QUOTIENT_BINDING.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/general_quotient_relaxation/QUOTIENT_BINDING.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/general_quotient_relaxation/Exoo72/MINIMAL_HALL_CERTIFICATE.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/general_quotient_relaxation/Exoo72/MINIMAL_HALL_CERTIFICATE.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/general_quotient_relaxation/Michel72/MINIMAL_HALL_CERTIFICATE.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/general_quotient_relaxation/Michel72/MINIMAL_HALL_CERTIFICATE.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/PRED.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/PRED.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/PREFLIGHT_RESULT.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/PREFLIGHT_RESULT.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/BOUNDARY_CERTIFICATE.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/BOUNDARY_CERTIFICATE.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/RESULT.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/RESULT.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/SURVIVOR_OUTCOMES.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/SURVIVOR_OUTCOMES.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/ONE_TARGETED_FAILURE_CHECK.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/ONE_TARGETED_FAILURE_CHECK.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/PROOF.md](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/PROOF.md)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/REPORT.md](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/REPORT.md)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/STRUCTURAL_CROSS_OBSTRUCTION.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_pair_surgery/STRUCTURAL_CROSS_OBSTRUCTION.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/PRED.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/PRED.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/RESULT.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/RESULT.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/PROOF.md](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/PROOF.md)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/REPORT.md](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/REPORT.md)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/BOUNDARY_ATTEMPTS.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/BOUNDARY_ATTEMPTS.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/H_BOUNDARY_CACHE.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/H_BOUNDARY_CACHE.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/OLD_CROSS_ARGUMENT_ESCAPE_EXAMPLE.json](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/OLD_CROSS_ARGUMENT_ESCAPE_EXAMPLE.json)；[research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/check_once.py](../../research/ddp/two_successful_methods_20261101/f4_c72_nucleus_C4/controller70_general_matching/check_once.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** HomogeneousF4^3 full-line five-conic cross mechanism, true inverse semilinear darts, compatible local port lines, internalN,wN C4 and directed nucleus coefficient condition(E) for automatic conic-domain D0/D1/D2 and D3 goodword iff. Separate unique-distance3 necessary Hall condition applies to arbitrary invertible affine-semilinear port-line maps including shears/scales/offsets and arbitrary within-fiber edges, only on the fixedExoo72/Michel72 controllers with actual unique-route witnesses. Does not transfer common-zero/allbadN necessity outside conic homogeneous maps or exclude othercontrollers/general22D3.

**正向保证：** internalC4用额外2度修复旧selflayer覆盖障碍；旧cross-only controller≤68界不能套到新22度机制。；conic域D0 tangent完整pencil、D1四secant加tangent、D2共base四actualcosets给自动覆盖；goodword rank3充分，allbadsecants漏N给同域必要性。；general quotient释放增加target nucleus joker列，确实把旧Exoo局部Hall空域修为12，支持局部修复预测；重查全部180edge却另有24/36空域。；Exoo24→61的rows1,2,4只能映到cols3(joker),4，三入二；Michel对应三入二也仍阻断。该必要性来自唯一controller三步路的rank，非旧conic allbadN论证。；GENERAL_QUOTIENT_INTERFACE区分360split lifts与5760exact-normalized shear lifts；全120S5 quotient门涵盖其全部必要projective行为，但没有实际生成360/5760matrices。；后续结构解释覆盖全部180被删边/4320matching：每条原uv都有至少两项共享同一边界端点的unique旧A_i-u-v-B_j义务；girth5使未直接matching的对应A-B对无法用其他matching在三步内修复。同端点因此需2条直接matching边却只准1，形成同时实现矛盾。沿用既存unique-route账本，结构CPU0.028433571，0BFS/shortword重算；实际312controller检查历史仍保留，不冒称被跳过。；后续更宽oldold修复门实际新增14580非purecross perfectmatchings全28boundary必要门失败(CPU0.25110093)，继承4320旧cross不重跑，合18900=180×105；partialmatchings可补perfectmatching，故闭固定相邻2点删除+保H/max5的全部增边修复。旧cross必须directmatch论证不能照搬：删0,45的same-sideedge51-59确用51-59-36-18修旧51,18而不directmatch，但另一51,62边界义务失败。新门据exact boundary路径式及cachedH证书，0新controllerR3/solver/fiber；不接非邻pair/删4/portseed。

**仍未完成：** 这是条件机制/有限源障碍，没有4608或4480合法新图/纪录/Lean。general maps只保证D1自动；D0需覆盖M15缺集，D2须实际四cosets齐全，不能把span/rank或不同word不同base的mask当覆盖。那些sufficient interfaces未数值验收，360splitmaps/D0D2/SAT均未派。其他控制器、跨噪声关系、非线性映射或一般22D3仍开放。

**启发与重启依据：** 先用内部C4和nucleus共缺向量把旧selflayer/坏word问题变成可检验结构条件，再把conic symmetry放开到全部quotient；一次旧Hall修好不等于全edge可实现，新的3→2 Hall在更宽域仍严格。停止这两个72controller的map/SAT梯子，保留conditional接口用于另一个有依据controller。受控70点手术的cheap边界门必须保existingH≤3路线；全部4320赋值中4008边界fail/312survive，后者实际全非D3，所以停止该精确手术族，不把preflight幸存当controller成果。 后续结构解释覆盖全部180被删边/4320matching：每条原uv都有至少两项共享同一边界端点的unique旧A_i-u-v-B_j义务；girth5使未直接matching的对应A-B对无法用其他matching在三步内修复。同端点因此需2条直接matching边却只准1，形成同时实现矛盾。沿用既存unique-route账本，结构CPU0.028433571，0BFS/shortword重算；实际312controller检查历史仍保留，不冒称被跳过。 后续更宽oldold修复门实际新增14580非purecross perfectmatchings全28boundary必要门失败(CPU0.25110093)，继承4320旧cross不重跑，合18900=180×105；partialmatchings可补perfectmatching，故闭固定相邻2点删除+保H/max5的全部增边修复。旧cross必须directmatch论证不能照搬：删0,45的same-sideedge51-59确用51-59-36-18修旧51,18而不directmatch，但另一51,62边界义务失败。新门据exact boundary路径式及cachedH证书，0新controllerR3/solver/fiber；不接非邻pair/删4/portseed。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

