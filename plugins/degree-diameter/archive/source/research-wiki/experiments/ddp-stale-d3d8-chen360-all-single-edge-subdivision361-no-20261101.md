---
type: experiment
node_id: exp:ddp-stale-d3d8-chen360-all-single-edge-subdivision361-no-20261101
title: "3D8 Chen360→361：逐540旧边新rootR8均失败，严格排固定源全部单细分，非一般3D8"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/ROOT_DISPOSITION.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/FIRST_NEWROOT_FAILURE.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/ATTEMPTS.csv; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/OUTPUT_ACCOUNTING.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/run.cpp; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/run_once.py; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/format_guard_failure/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/format_guard_failure/TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/format_guard_failure/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/PAPER_SCOPE_REVIEW.md"
added: 2026-11-01T19:17:55Z
tags: ["ddp", "method-ledger"]
---

# 3D8 Chen360→361：逐540旧边新rootR8均失败，严格排固定源全部单细分，非一般3D8

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** bounded_or_exact_modified_graph_gate

**目标与阶数：** (3,8)；L=360；条件性n=361（未据此计纪录）

**距目标的证据：** No accepted final target graph; actual candidate root checks and exact scope below；sourceChen2018 360/540 cubic,input binding1次成功；initial数值upper-neighbor错误guard先失败，修正只要求每无向边出现一次，HTTP仍1/rawparse累计2，0candidate/0BFS失败成本保留。随后540/540oldedge都生成对应361/541单细分邻接并检查actualnewrootR8，全部FAIL，firstfailedtargetdist9共540次；oldoldBFS0。newroot条件R7_(G-e)({u,v})=all，且endpoint-min等于原G。degree2rootB8≤511大于361，只说明可试，不保证覆盖。首rawedge[1,141]对应normalized[0,140]，new360到old22的shortest9路保存。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_parameter_pairs": 0,
  "new_Lean_instances": 0,
  "new_independent_method_claims": 0,
  "Moore_bound": 766,
  "located_baseline": 360,
  "Moore_space": 406,
  "Moore_gap_is_not_constructibility": true,
  "source_identity": "JianxiangChen360,primary2018-10-16",
  "source_order": 360,
  "source_edges": 540,
  "source_cubic_binding": true,
  "source_D8": "PRIMARY_INHERITED_NOT_NUMERICALLY_VALIDATED",
  "target_edges": 541,
  "target_degree_histogram_by_construction": {
    "2": 1,
    "3": 360
  },
  "degree2_root_B8_upper": 511,
  "root_capacity_does_not_exclude_target": true,
  "all_oldedges_tested": 540,
  "all_distinct_edges_explicit": true,
  "newroot_R8_failures": 540,
  "newroot_R8_passes": 0,
  "recorded_first_failure_distance_histogram": {
    "9": 540
  },
  "actual_final_newroot_BFS": 540,
  "old_label_BFS": 0,
  "source_D8_validation_BFS": 0,
  "original_pair_diagnostic_BFS": 0,
  "first_newroot_failure": {
    "stage": "FAIL_NEWROOT_R8",
    "removed_edge_normalized": [
      0,
      140
    ],
    "removed_edge_raw": [
      1,
      141
    ],
    "inserted_normalized_newlabel": 360,
    "added_edges": [
      [
        0,
        360
      ],
      [
        140,
        360
      ]
    ],
    "failed_source": 360,
    "failed_target": 22,
    "distance": 9,
    "actual_final_shortest_path_normalized": [
      360,
      0,
      141,
      2,
      145,
      6,
      153,
      13,
      169,
      22
    ],
    "actual_final_shortest_path_raw_old1to360_new361": [
      361,
      1,
      142,
      3,
      146,
      7,
      154,
      14,
      170,
      23
    ]
  },
  "complete_fixed_single_subdivision_scope_excluded": true,
  "general_parameter_excluded": false,
  "newroot_distance_formula": "1+min(d_(G-e)(u,t),d_(G-e)(v,t))",
  "endpoint_min_preserved": "d_(G-e)({u,v},t)=d_G({u,v},t)",
  "paper_global_upper9": true,
  "newrootpass_not_oldoldcertificate": true,
  "failed_format_attempt_preserved": true,
  "format_failure_was_not_mathematicalNO": true,
  "HTTP_downloads": 1,
  "raw_parse_attempts": 2,
  "successful_input_bindings": 1,
  "cumulative_CPU": 3.760862073,
  "CPU_budget": 20,
  "no_timer_reset": true,
  "terminal": true,
  "root_acceptance": "ROOT_ACCEPTED_COMPLETE_FIXED_CHEN360_SINGLE_EDGE_SUBDIVISION_NO"
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/ROOT_DISPOSITION.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/ROOT_DISPOSITION.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/FIRST_NEWROOT_FAILURE.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/FIRST_NEWROOT_FAILURE.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/ATTEMPTS.csv](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/ATTEMPTS.csv)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/OUTPUT_ACCOUNTING.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/OUTPUT_ACCOUNTING.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/run.cpp](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/run.cpp)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/run_once.py](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/run_once.py)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/format_guard_failure/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/format_guard_failure/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/format_guard_failure/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/format_guard_failure/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/format_guard_failure/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/format_guard_failure/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/PAPER_SCOPE_REVIEW.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/PAPER_SCOPE_REVIEW.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Only this fixed primary Chen360 graph,one deleted oldedge replaced by a length2 path through one newvertex;not other edits/sources or general3D8 All540literal oldedges explicitly tested;noautomorphism representative assumption. Sourcegate/formatcorrection/peredgechecks are one mechanismnode,not540methods.

**仍未完成：** Only this bounded sample or exact fixedsource edit scope stops; generaltarget remainsopen. Same Goal ACTIVE,oldN8/n61 PAUSED.

**启发与重启依据：** STOP every single-edge subdivision of this fixedChen360 source;do not rerun anotherlabel of the sameedge orall540. A subsequent attempt must change the actualgenerationrule beyondonesubdivision,not infer general3D8nonexistence. Multipleedits/othersources remainoutside and are not automatically scheduled.

**单独的重启条件：** STOP every single-edge subdivision of this fixedChen360 source;do not rerun anotherlabel of the sameedge orall540. A subsequent attempt must change the actualgenerationrule beyondonesubdivision,not infer general3D8nonexistence. Multipleedits/othersources remainoutside and are not automatically scheduled.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

