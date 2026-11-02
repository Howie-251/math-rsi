---
type: experiment
node_id: exp:ddp-stale-d11d3-715-cross-oldclass-helper-min3-tight-route-tradeoff-20261101
title: "11D3固定715全保边新增族严格NO：任意finite helpers及old-old/new-old/new-new边均排，须改旧边或换host"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/ROOT_DISPOSITION.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/HIGHER_DEGREE_CLOSURE_PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/HIGHER_DEGREE_CLOSURE_NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/HIGHER_DEGREE_CLOSURE_RESULT.json"
added: 2026-11-01T19:44:58Z
tags: ["ddp", "method-ledger"]
---

# 11D3固定715全保边新增族严格NO：任意finite helpers及old-old/new-old/new-new边均排，须改旧边或换host

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** paper_complete_fixed_host_augmentation_exclusion

**目标与阶数：** (11,3)；L=715

**距目标的证据：** Complete paper exclusion for the stated fixed-host preserved-oldedge family;no candidate graph/H enumeration/sourceBFS；原minHdegree3及8distinctleafpins/(b,c,s)20/8/0或21/7/1要求其3邻居H度数和13或12。新论证不要求helper是min点：任意d=4..7，ownclasses q≤11−d≤7，badowner≥65−q≥54+d；全H最低度3故neighbor spokes b≤8d，owncross c≤11−d。必要54+d≤b+c≤7d+11即43≤6d，逐排4..7（deficits19/13/7/1）。所有Hdegree只能3或≥8；min3点的3邻居度数和只能9或≥14，不能12/13，矛盾。一般mixedmin3在此固定保边scope也已关闭；原开放状态仅历史。累计小算式.022627260/5CPU，新增.000391260，0source/design/H枚举/BFS/solver/Lean重跑。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_parameter_pairs": 0,
  "new_Lean_instances": 0,
  "new_independent_method_claims": 0,
  "parent_fixed_induced_node": "ddp-stale-d11d3-715-fixed-induced-arbitrary-helpers-obstruction-20261101",
  "allows_cross_oldclass_edges": true,
  "all_oldedges_retained": true,
  "minimum_helper_degree_exact_necessary": 3,
  "own_leafpins_distinct_classes": 8,
  "necessary_b_c_s_cases": [
    [
      20,
      8,
      0
    ],
    [
      21,
      7,
      1
    ]
  ],
  "necessary_neighbor_helper_degree_sums": [
    13,
    12
  ],
  "minimum2_maximum_eligible_cover": 159,
  "required_eligible_vertices": 195,
  "centerpins_z": 0,
  "unused_leafslots_u": 0,
  "core_budget_excess_delta": 0,
  "pure_cubic_or_cycle_H_excluded": true,
  "general_mixed_min3_H_excluded": true,
  "H_graphs_generated": 0,
  "H_searches": 0,
  "source_core_design_BFS_rechecks": 0,
  "scalar_budget_check_CPU_seconds": 0.022236,
  "CPU_budget_seconds": 5,
  "source_facts_inherited_not_new_acceptance": true,
  "terminal": true,
  "historical_min3_checkpoint": {
    "status": "PARTIAL_CROSS_CLASS_SCOPE_MIN3_TWO_TIGHT_NECESSARY_CASES_STOP",
    "distance_text": "首次把h–ownpin–原P3邻居–crossedge路线、共享pin的helper reentry及center/leaf端口损耗一起计入。r=min degree_H，a=11−r：E≤3a+3b+a(10r−b)+3c+(a−1)s+a+3z。r2时≤159<195，排min2；继承moment加纸面partition边界排r0/1与r≥4。剩r=3恰8个不同class的leafpins，z=u=δ=0，只能(b,c,s)=(20,8,0)或(21,7,1)，邻helper度数和必须13或12；cycle和purecubicH不行。一般mixedH/min3仍UNKNOWN，0H枚举/0图，只有.022236/5CPU小整数预算核对，不是新source验收。",
    "metrics": {
      "new_graphs": 0,
      "new_parameter_pairs": 0,
      "new_Lean_instances": 0,
      "new_independent_method_claims": 0,
      "parent_fixed_induced_node": "ddp-stale-d11d3-715-fixed-induced-arbitrary-helpers-obstruction-20261101",
      "allows_cross_oldclass_edges": true,
      "all_oldedges_retained": true,
      "minimum_helper_degree_exact_necessary": 3,
      "own_leafpins_distinct_classes": 8,
      "necessary_b_c_s_cases": [
        [
          20,
          8,
          0
        ],
        [
          21,
          7,
          1
        ]
      ],
      "necessary_neighbor_helper_degree_sums": [
        13,
        12
      ],
      "minimum2_maximum_eligible_cover": 159,
      "required_eligible_vertices": 195,
      "centerpins_z": 0,
      "unused_leafslots_u": 0,
      "core_budget_excess_delta": 0,
      "pure_cubic_or_cycle_H_excluded": true,
      "general_mixed_min3_H_excluded": false,
      "H_graphs_generated": 0,
      "H_searches": 0,
      "source_core_design_BFS_rechecks": 0,
      "scalar_budget_check_CPU_seconds": 0.022236,
      "CPU_budget_seconds": 5,
      "source_facts_inherited_not_new_acceptance": true,
      "terminal": true
    }
  },
  "minimum3_open_checkpoint_is_historical": true,
  "complete_fixed715_all_oldedges_retained_nonempty_augmentation_family_excluded": true,
  "arbitrary_added_oldold_newold_newnew_edges_included": true,
  "intraP3_leafleaf_completions_included": true,
  "excluded_nonminimum_helper_degrees": [
    4,
    5,
    6,
    7
  ],
  "remaining_helper_degrees": [
    3,
    8,
    9,
    10,
    11
  ],
  "required_min3_neighbor_degree_sums": [
    12,
    13
  ],
  "actual_possible_min3_neighbor_degree_sums": "9 or>=14",
  "core_inequality": "54+d<=b+c<=8d+(11-d)=7d+11 implies43<=6d,impossible4..7",
  "full_scope_closed": true,
  "new_scalar_closure_CPU_seconds": 0.0003912600000000009,
  "cumulative_small_scalar_CPU_seconds": 0.02262726
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/ROOT_DISPOSITION.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/ROOT_DISPOSITION.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/HIGHER_DEGREE_CLOSURE_PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/HIGHER_DEGREE_CLOSURE_PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/HIGHER_DEGREE_CLOSURE_NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/HIGHER_DEGREE_CLOSURE_NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/HIGHER_DEGREE_CLOSURE_RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/HIGHER_DEGREE_CLOSURE_RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Actual fixed715 host,retain every oldedge,add a nonempty finite helper set H with arbitrary added simple old-old/new-old/new-new edges,maxdegree11,D<=3. All newold-old edges,including originalP3 leaf-leaf triangle completions,are included. The520 oldcore is saturated. Inherit source/core/design/moment inputs without revalidation. This is the complete edge-preserving augmentation family of this host,not generalN(11,3),oldedge deletions/replacements or anotherhost.

**仍未完成：** GeneralN(11,3),oldedge deletion/replacement and otherhosts remain open;no new graph/parameter/Lean or method count.

**启发与重启依据：** STOP every nonempty finite edge-preserving augmentation of this exact715host,including mixedmin3H and internalP3 triangle completion. A next construction must delete/replace oldedges or changehost;neither alternative is excluded or automatically authorized by this proof. Do not restart a preserved-edge Hsearch or label generalN11D3 impossible.

**单独的重启条件：** A genuinely changed oldedge-deletion/replacement rule or differenthost under a bounded research decision.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._



<!-- 715_COMPLETE_CLOSURE_16416_A_ACTUAL_20261101 -->
<details>
<summary>历史中间检查点：mixedmin3当时仍开放，已被上面的完整闭合覆盖</summary>


# 11D3旧715允许跨旧class边：排helper最低度2，剩minimum3的两种极紧路线预算；未排一般mixedH

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** paper_necessary_route_capacity_boundary

**目标与阶数：** (11,3)；L=715

**距目标的证据：** Paper route accounting and one small scalar integer-budget check;no H graph or candidate/BFS；首次把h–ownpin–原P3邻居–crossedge路线、共享pin的helper reentry及center/leaf端口损耗一起计入。r=min degree_H，a=11−r：E≤3a+3b+a(10r−b)+3c+(a−1)s+a+3z。r2时≤159<195，排min2；继承moment加纸面partition边界排r0/1与r≥4。剩r=3恰8个不同class的leafpins，z=u=δ=0，只能(b,c,s)=(20,8,0)或(21,7,1)，邻helper度数和必须13或12；cycle和purecubicH不行。一般mixedH/min3仍UNKNOWN，0H枚举/0图，只有.022236/5CPU小整数预算核对，不是新source验收。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_parameter_pairs": 0,
  "new_Lean_instances": 0,
  "new_independent_method_claims": 0,
  "parent_fixed_induced_node": "ddp-stale-d11d3-715-fixed-induced-arbitrary-helpers-obstruction-20261101",
  "allows_cross_oldclass_edges": true,
  "all_oldedges_retained": true,
  "minimum_helper_degree_exact_necessary": 3,
  "own_leafpins_distinct_classes": 8,
  "necessary_b_c_s_cases": [
    [
      20,
      8,
      0
    ],
    [
      21,
      7,
      1
    ]
  ],
  "necessary_neighbor_helper_degree_sums": [
    13,
    12
  ],
  "minimum2_maximum_eligible_cover": 159,
  "required_eligible_vertices": 195,
  "centerpins_z": 0,
  "unused_leafslots_u": 0,
  "core_budget_excess_delta": 0,
  "pure_cubic_or_cycle_H_excluded": true,
  "general_mixed_min3_H_excluded": false,
  "H_graphs_generated": 0,
  "H_searches": 0,
  "source_core_design_BFS_rechecks": 0,
  "scalar_budget_check_CPU_seconds": 0.022236,
  "CPU_budget_seconds": 5,
  "source_facts_inherited_not_new_acceptance": true,
  "terminal": true
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/ROOT_DISPOSITION.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/ROOT_DISPOSITION.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Retain all oldedges of actual715 P3/core source,but allow newold-old edges across eligible oldclasses,arbitrary finite helperH and helper-old spokes,max11/D3. Core520 stays saturated. Inherit accepted actualclass/core and Steiner moment inputs;no source/design revalidation. This enlarges the old fixed-induced strictNO scope and is not covered by that oldNO. No deletion/replacement or changedsource.

**仍未完成：** Existence or impossibility for general mixedH with minimumdegree3 remains open;no completegraph candidate.

**启发与重启依据：** Stop this paper boundary,not generalmin3nonexistence. A future mixedH proposal must realize eight distinct leafpins and one of the two exact route/neighbor-degree cases while controlling overlap. Do not rerun oldfixed-inducedNO,cycle orpurecubicH;do not infer an arbitrary-helper-familyNO after crossclass edges are allowed. No Hsearch or newnumerical batch is authorized here.

**单独的重启条件：** A concrete mixedmin3H rule consistent with both core coverage and eligible endpoint route budgets,under a separate bounded computation decision.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._


</details>
