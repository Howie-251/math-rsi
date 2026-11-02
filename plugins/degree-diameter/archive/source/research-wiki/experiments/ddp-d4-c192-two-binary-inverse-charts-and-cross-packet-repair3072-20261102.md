---
type: experiment
node_id: exp:ddp-d4-c192-two-binary-inverse-charts-and-cross-packet-repair3072-20261102
title: "D4 C192二元受控chart：同层全16，局部跨组8→16但其它pair仍漏，两个固定chart NO"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: partial
confidence: high
date: "2026-11-02"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_cross_coupled3072/ROOT_DISPOSITION.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_cross_coupled3072/NOTE.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_identity_chart3072/READ_GATE.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_identity_chart3072/READ_GATE.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_pair_swaps3072/PRED.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_pair_swaps3072/run_once.py; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_pair_swaps3072/RESULT.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_pair_swaps3072/TERMINAL.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_pair_swaps3072/FIRST_BAD_PACKET.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_cross_coupled3072/PRED.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_cross_coupled3072/run_once.py; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_cross_coupled3072/RESULT.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_cross_coupled3072/TERMINAL.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_cross_coupled3072/FIRST_BAD_PACKET.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_cross_coupled3072/PAPER_INTERFACE.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/cap15_arbitrary_pin_extension15553/READ_GATE.md"
added: 2026-11-02T01:57:08Z
tags: ["ddp", "method-ledger"]
---

# D4 C192二元受控chart：同层全16，局部跨组8→16但其它pair仍漏，两个固定chart NO

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** controller

**目标与阶数：** (10,4)；L=2556；条件性n=3072（未据此计纪录）

**距目标的证据：** No complete3072literalgraphorgraphBFS. Two fixed inverse-compatibleF2^4charts were checked by actualordinarytypedwordimageunions0..4,all192controllers/all16sourcefibrecoordinates for self-fibres,and at leastonecrossfailurepercontrollerroot. Samefibrecoverpositive; crossD4failsbothfixedcharts.；真实bar[0,3,4,1,2]阻止五distinctnoise/allI的误设；合法pairedidentity零offset只span<=3，不连通。第一chart M0=I，M1/3交换e1/e2、M2/4交换e3/e4，v=[15,1,4,2,8]。两return的五circuit支持samefibre<=4，实际全部192×16self均16；但每controllerroot有cross失败。首0→1仅2022/4020，两image嵌套8。依据此缺口改唯一M0 columns[4,7,1,13]，原packet8→16支持且self全16保留，却另0→3的234/0234/4323只并12或14；x0首漏y9。两个各781ordinarywords含backtracks，逐全部16sourcecoords，0完整图/BFS/solver/Lean/ARIS。最终1.233294418/10，停止第三matrix/field。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_parameter_pairs": 0,
  "new_Lean_instances": 0,
  "new_independent_method_claims": 0,
  "single_aggregate_research_record": true,
  "hypothetical_target": [
    10,
    4,
    3072
  ],
  "base_controller_order": 192,
  "fibre_size": 16,
  "actual_bar": [
    0,
    3,
    4,
    1,
    2
  ],
  "old_cap15_unrestricted_extension_status": "MILP_AND_SAT_UNKNOWN_INHERITED_ONLY",
  "old_cap15_not_rerun_or_new_record": true,
  "identity_baseline_five_distinct_noises_illegal": true,
  "legal_paired_identity_zerooffset_span_atmost": 3,
  "legal_paired_identity_zerooffset_disconnected": true,
  "baseline_chart": {
    "M0": [
      1,
      2,
      4,
      8
    ],
    "M1_M3": [
      2,
      1,
      4,
      8
    ],
    "M2_M4": [
      1,
      2,
      8,
      4
    ],
    "v": [
      15,
      1,
      4,
      2,
      8
    ],
    "same_fibre_roots_complete": 192,
    "firstbad": [
      0,
      1
    ],
    "source_fibre_all16_counts": [
      8,
      8,
      8,
      8,
      8,
      8,
      8,
      8,
      8,
      8,
      8,
      8,
      8,
      8,
      8,
      8
    ],
    "wordpacket": [
      "2022",
      "4020"
    ],
    "cross_controller_root_failures": 192
  },
  "cross_chart": {
    "M0": [
      4,
      7,
      1,
      13
    ],
    "M1_M3": [
      2,
      1,
      4,
      8
    ],
    "M2_M4": [
      1,
      2,
      8,
      4
    ],
    "v": [
      15,
      1,
      4,
      2,
      8
    ],
    "same_fibre_roots_complete": 192,
    "previous_bad0to1_repaired_all16": true,
    "evidence": "firstbadcontroller now3, code scansascendingandword2022noisebasis proof",
    "new_first_bad": {
      "controllerroot": 0,
      "controllertarget": 3,
      "source_x": 0,
      "first_missing_y": 9,
      "actual_fibre_covered_for_x": 12,
      "whole_fibre_source_counts": [
        12,
        14,
        14,
        12,
        14,
        12,
        12,
        14,
        14,
        12,
        12,
        14,
        12,
        14,
        14,
        12
      ],
      "actual_controller_word_packet": [
        {
          "word": [
            2,
            3,
            4
          ],
          "noise_rank": 2,
          "zero_source_image_mask": 1285
        },
        {
          "word": [
            0,
            2,
            3,
            4
          ],
          "noise_rank": 3,
          "zero_source_image_mask": 42405
        },
        {
          "word": [
            4,
            3,
            2,
            3
          ],
          "noise_rank": 3,
          "zero_source_image_mask": 255
        }
      ]
    },
    "cross_controller_root_failures": 192
  },
  "same_fibre_roots_eachchart": 192,
  "source_fibre_coordinates_eachroot": 16,
  "all_same_fibre_counts": 16,
  "cross_root_failures_eachchart": 192,
  "ordinary_words_length0to4_eachchart": 781,
  "samefibre_prediction_supported": true,
  "targeted_crosspacket_8to16_supported": true,
  "wholeD4_prediction_refuted_for_two_fixedcharts": true,
  "general_binary_chart_family_NO": false,
  "actual_native_CPU": 0.333294418,
  "wholecase_CPU": 1.233294418,
  "case_cap": 10,
  "full_target_graph_generated": false,
  "source_F3_oldR3_fullgraphBFS_Lean_ARIS_solver": 0,
  "new_small_source_readgates_included": false,
  "all_stages_terminal": true,
  "same_Goal": "ACTIVE",
  "old_N8_n61": "PAUSED"
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_cross_coupled3072/ROOT_DISPOSITION.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_cross_coupled3072/ROOT_DISPOSITION.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_cross_coupled3072/NOTE.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_cross_coupled3072/NOTE.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_identity_chart3072/READ_GATE.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_identity_chart3072/READ_GATE.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_identity_chart3072/READ_GATE.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_identity_chart3072/READ_GATE.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_pair_swaps3072/PRED.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_pair_swaps3072/PRED.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_pair_swaps3072/run_once.py](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_pair_swaps3072/run_once.py)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_pair_swaps3072/RESULT.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_pair_swaps3072/RESULT.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_pair_swaps3072/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_pair_swaps3072/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_pair_swaps3072/FIRST_BAD_PACKET.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_pair_swaps3072/FIRST_BAD_PACKET.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_cross_coupled3072/PRED.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_cross_coupled3072/PRED.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_cross_coupled3072/run_once.py](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_cross_coupled3072/run_once.py)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_cross_coupled3072/RESULT.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_cross_coupled3072/RESULT.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_cross_coupled3072/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_cross_coupled3072/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_cross_coupled3072/FIRST_BAD_PACKET.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_cross_coupled3072/FIRST_BAD_PACKET.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_cross_coupled3072/PAPER_INTERFACE.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/binary_cross_coupled3072/PAPER_INTERFACE.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/cap15_arbitrary_pin_extension15553/READ_GATE.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/cap15_arbitrary_pin_extension15553/READ_GATE.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** ActualC192 typed5porttransitionJSON with bar[0,3,4,1,2],zeroaffineconstants,192xF2^4. Identitybaselinepaperonly: five distinctcircuits withallI violate realreversecontract; pairingidentitynoises leaves span<=3/disconnected. Thetwoexplicitnonidentitycolumnmatrixcharts inroot each have completeordinary<=4route checks asstated. Onlythesefixedcharts areNO,notallbinarymaps/general3072/(10,4). Oldcap15 arbitraryfreepin MILP/SATUNKNOWN inherited without rerun,newentry or changedverdict. No completegraph produced.

**正向保证：** Use actualtypedtransitionorder,not sortedACTUAL_CONTROLLER_TARGETSneighborlists; actualreverseportbar is[0,3,4,1,2].；Both explicitcharts satisfy therealreversecontract. All192x16self-fibreimageunions cover16,not merelysourcex0.；All781ordinarywords0..4 include shortwords andcontrollerbacktracks; full-labelholdingsteps maycontract,not samecontroller/differentfibresteps.；Thefirstchartbadpacket2022/4020 is nested8 for all16sourcecoordinates; thecrosscoupledM0fixesit to16 but the new0to3packet stillgives12/14.；Oldcap15arbitraryfreepinMILP/SATUNKNOWN is inheritedonly. No oldF3field,sourceD4validation,oldR3,BFS,solver,Lean orARIS rerun.；ThetwofixedchartNO is completeatitsactualroutegate level; itdoesnotexcludeallF2^4charts or createa graph/methodcount.

**仍未完成：** Other inverse-compatiblebinary maps,offsetrules,controllers and general(10,4)/3072 remainunexcluded. Oldcap15sourceextension remainsUNKNOWN. No fulltargetgraph,actualgraphD4,newlowerbound,parameter,Lean,methodorpriorityclaim. NewsmallD4sourcereadgates are notpartofthisnode.

**启发与重启依据：** Completed true reverse and fivecircuit returns can cover the self-fibre while cross-controllertransport stillhasinvariantspaces/cosetgaps. A concreteM0 repair fixes the targeted8-to16packet without making a globalD4construction: anotherpairmisses12/14. Keepthislocalpositive distinctfromglobalgraphsuccess and stopthisfixedchartchain without thirdmatrix/field. Theoldcap15UNKNOWN isnotnewnumerics or a familyNO.

**单独的重启条件：** STOP twoexplicitbinarycharts and identitybaseline. No thirdmatrix/field or automaticF2/Fq/controllerladder. Only a separatelyauthorized materiallydifferentquestion outsidefixedchartscope canrestart.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

