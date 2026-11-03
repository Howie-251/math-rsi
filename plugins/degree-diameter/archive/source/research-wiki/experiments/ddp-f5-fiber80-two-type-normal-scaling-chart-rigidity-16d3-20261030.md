---
type: experiment
node_id: exp:ddp-f5-fiber80-two-type-normal-scaling-chart-rigidity-16d3-20261030
title: "S80 two-type normal-scaling affine fibers: local76 gate and tightN25 rigidity imply order<=1920"
idea_id: "idea:ddp-q3-three-step-plane-pencil31"
verdict: no
confidence: high
date: "2026-10-30"
hardware: "singleCPU,125pointlocalcalibrationandCNFpreparationonly"
duration: "Local0.025032128CPU;fixedC25CNFprepare2.399239534CPU;rigiditypaper0newsolver"
provenance: "research/ddp/refresh_20261029/f5_fiber80_structure_gate/PREDICTION.json; research/ddp/refresh_20261029/f5_fiber80_structure_gate/PROOF.md; research/ddp/refresh_20261029/f5_fiber80_structure_gate/REPORT.md; research/ddp/refresh_20261029/f5_fiber80_structure_gate/RESULT.json; research/ddp/refresh_20261029/f5_fiber80_structure_gate/TERMINAL.json; research/ddp/refresh_20261029/f5_fiber80_structure_gate/check_once.py; research/ddp/refresh_20261029/f5_fiber80_controller25/EDGE_VARIABLES.json; research/ddp/refresh_20261029/f5_fiber80_controller25/INPUT_SCOPE.json; research/ddp/refresh_20261029/f5_fiber80_controller25/MODEL.json; research/ddp/refresh_20261029/f5_fiber80_controller25/MODEL_CODE.md; research/ddp/refresh_20261029/f5_fiber80_controller25/PAIR_ROUTE_GATES.json; research/ddp/refresh_20261029/f5_fiber80_controller25/PREDICTION_AND_SCOPE.md; research/ddp/refresh_20261029/f5_fiber80_controller25/PREPARE_HANDLE.json; research/ddp/refresh_20261029/f5_fiber80_controller25/PREPARE_TERMINAL.json; research/ddp/refresh_20261029/f5_fiber80_controller25/STOP_BY_CHART_RIGIDITY.md; research/ddp/refresh_20261029/f5_fiber80_controller25/prepare.py; research/ddp/refresh_20261029/FULLK2_C21_S80_WIKI_REPORT.md; reviews/ddp/new_fiber_route_obstructions_20261030.prompt.md; reviews/ddp/new_fiber_route_obstructions_20261030.response.json; reviews/ddp/new_fiber_route_obstructions_20261030.DISPOSITION.md; research/ddp/refresh_20261029/NEWFIBER_REVIEW_D15_K2_WIKI_REPORT.md"
added: 2026-10-30T01:51:56Z
tags: ["ddp", "method-ledger"]
---

# S80 two-type normal-scaling affine fibers: local76 gate and tightN25 rigidity imply order<=1920

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-q3-three-step-plane-pencil31`

## Metrics
**对象层级：** controller

**目标与阶数：** (16,3)；L=1920；条件性n=2000（未据此计纪录）

**距目标的证据：** 76boundforcesnontriangleedgeinC4;wordbudgetN<=29-2t-c4forcesN<=27,thenN26triangledivisibilityandN27C4obstructionleave25. N25hasat2/c40rootwithtight8dist2+12dist3supply;allnonneighborNB2mustmixed,forcingpureA/pureBtriangles. Choosebothendpointnormalsoutsidethreepossiblelevels:all5hiddenfiberpointsaremissed. ThusN<=24,order<=1920. Localcalibration0.025032128CPU;C25necessaryCNF333343/1129292prepared2.399239534CPUbutstoppedbeforeanysolver.

**其他指标（保持原计数类型）：**
```json
{
  "fiber_size": 80,
  "neighbors_per_port": 4,
  "conditional_lift_degree": 16,
  "controller_degree": 4,
  "hypothetical_controller_N25_order": 2000,
  "universal_backtrack_union_upper": 76,
  "control_budget": "N<=29-2t-c4",
  "framework_controller_upper_bound": 24,
  "framework_order_upper_bound": 1920,
  "upper_bound_attained_claimed": false,
  "local_chart_calibration_CPU_seconds": 0.025032127999999994,
  "reverse_pairs_checked": 1280,
  "backtrack_images_checked": 1920,
  "sampled_chart_six_union_histogram": {
    "55": 160,
    "43": 160
  },
  "all_accepted_charts_preserve_S80_as_a_set_required": false,
  "root_degree5_affine_local_static_support": true,
  "external_review_status": "SUCCESS_SOUND_AS_STATED",
  "Lean_formalized": false,
  "controller_lifts_generated": 0,
  "SAT_calls": 0,
  "large_graph_BFS": 0,
  "general_N16D3_upper_bound_claimed": false,
  "nonnormal_preserving_charts_or_other_fibers_excluded": false,
  "new_record": false,
  "actual_external_review": {
    "status": "SUCCESS_SOUND_AS_STATED",
    "actual_model": "gemini-3.8-flash-high",
    "effort": "high",
    "thread_id": "12c1d715-0369-4a25-9755-3fb41033c3bd",
    "C21_scope": "FixedFanoflagC21,uniform100singleaffineplanedeletion,everystepnoisetransversetotargetnormal;edge-specificchartsandfiber-specificplanesallowed.",
    "S80_scope": "F5*_a×F5*_b×F5_h,twoinversepairedtypesApassiveb/Bpassiveaonlynonzeroscale;thewholeframehascontrollerN<=24.",
    "generalN16D3_upper_bound_claimed": false,
    "old3750_LRAT_used_as_basis_for_these_newrules": false,
    "reviewer_executed_C25_or_largegraph_or_LRAT_or_Lean": false,
    "response": "reviews/ddp/new_fiber_route_obstructions_20261030.response.json",
    "disposition": "reviews/ddp/new_fiber_route_obstructions_20261030.DISPOSITION.md"
  }
}
```



**从属变体：**
```json
[
  {
    "label": "S80_line_and_one_admissible_chart_quadruple_local_calibration_20261030",
    "status": "S80_LOCAL_STRUCTURE_AND76_BASELINE_SUPPORTED",
    "fiber_size": 80,
    "per_port_degree": 4,
    "local_CPU_seconds": 0.025032127999999994,
    "universal_six_image_upper": 76,
    "sample_43_or55_union_not_a_universal_obstruction": true,
    "solver_calls": 0,
    "large_graphs": 0
  },
  {
    "label": "N25_t2_tight_route_inventory_pure_triangles_hidden5_obstruction_20261030",
    "status": "LOCAL_PAPER_FRAMEWORK_EXCLUDED_ABOVE1920_EXTERNAL_PENDING",
    "mixed_three_word_hidden_values_per_fixed_normals_at_most": 4,
    "t2root_dist2_targets": 8,
    "t2root_dist3_targets": 12,
    "t2root_NB3_nonneighbor_supply": 32,
    "same_type_NB2_forbidden_at_nonadjacent_targets": true,
    "two_triangles_forced_pure_A_and_pure_B": true,
    "excluded_normal_levels_per_coordinate_at_most": 3,
    "nonzero_normal_choices": 4,
    "hidden_targets_entirely_missed": 5,
    "controller_N25_excluded": true,
    "framework_N_at_most24": true,
    "additional_computation_or_solver": 0,
    "external_review_status": "SUCCESS_SOUND_AS_STATED",
    "actual_external_review": {
      "status": "SUCCESS_SOUND_AS_STATED",
      "actual_model": "gemini-3.8-flash-high",
      "effort": "high",
      "thread_id": "12c1d715-0369-4a25-9755-3fb41033c3bd",
      "C21_scope": "FixedFanoflagC21,uniform100singleaffineplanedeletion,everystepnoisetransversetotargetnormal;edge-specificchartsandfiber-specificplanesallowed.",
      "S80_scope": "F5*_a×F5*_b×F5_h,twoinversepairedtypesApassiveb/Bpassiveaonlynonzeroscale;thewholeframehascontrollerN<=24.",
      "generalN16D3_upper_bound_claimed": false,
      "old3750_LRAT_used_as_basis_for_these_newrules": false,
      "reviewer_executed_C25_or_largegraph_or_LRAT_or_Lean": false,
      "response": "reviews/ddp/new_fiber_route_obstructions_20261030.response.json",
      "disposition": "reviews/ddp/new_fiber_route_obstructions_20261030.DISPOSITION.md"
    }
  },
  {
    "label": "C25_fixed_three_triangle_chain_plus6K3_necessary_capacity_model_prepared_then_stopped_20261030",
    "status": "C25_FIXED_MOTIF_NB2_NB3_CAPACITY_CNF_PREPARED_NOT_SOLVED",
    "controller_order": 25,
    "fixed_edges": 27,
    "extra_edge_variables": 233,
    "variables": 333343,
    "clauses": 1129292,
    "complete_only_within_fixed_motif": true,
    "controls_necessary_not_sufficient_for_S80": true,
    "prepare_CPU_seconds": 2.399239534,
    "actual_solver_calls": 0,
    "charts_constructed": false,
    "large_graphs": 0,
    "planned_solver_not_launched_due_to_new_rigidity": true
  }
]
```

**原始证据：** [research/ddp/refresh_20261029/f5_fiber80_structure_gate/PREDICTION.json](../../research/ddp/refresh_20261029/f5_fiber80_structure_gate/PREDICTION.json)；[research/ddp/refresh_20261029/f5_fiber80_structure_gate/PROOF.md](../../research/ddp/refresh_20261029/f5_fiber80_structure_gate/PROOF.md)；[research/ddp/refresh_20261029/f5_fiber80_structure_gate/REPORT.md](../../research/ddp/refresh_20261029/f5_fiber80_structure_gate/REPORT.md)；[research/ddp/refresh_20261029/f5_fiber80_structure_gate/RESULT.json](../../research/ddp/refresh_20261029/f5_fiber80_structure_gate/RESULT.json)；[research/ddp/refresh_20261029/f5_fiber80_structure_gate/TERMINAL.json](../../research/ddp/refresh_20261029/f5_fiber80_structure_gate/TERMINAL.json)；[research/ddp/refresh_20261029/f5_fiber80_structure_gate/check_once.py](../../research/ddp/refresh_20261029/f5_fiber80_structure_gate/check_once.py)；[research/ddp/refresh_20261029/f5_fiber80_controller25/EDGE_VARIABLES.json](../../research/ddp/refresh_20261029/f5_fiber80_controller25/EDGE_VARIABLES.json)；[research/ddp/refresh_20261029/f5_fiber80_controller25/INPUT_SCOPE.json](../../research/ddp/refresh_20261029/f5_fiber80_controller25/INPUT_SCOPE.json)；[research/ddp/refresh_20261029/f5_fiber80_controller25/MODEL.json](../../research/ddp/refresh_20261029/f5_fiber80_controller25/MODEL.json)；[research/ddp/refresh_20261029/f5_fiber80_controller25/MODEL_CODE.md](../../research/ddp/refresh_20261029/f5_fiber80_controller25/MODEL_CODE.md)；[research/ddp/refresh_20261029/f5_fiber80_controller25/PAIR_ROUTE_GATES.json](../../research/ddp/refresh_20261029/f5_fiber80_controller25/PAIR_ROUTE_GATES.json)；[research/ddp/refresh_20261029/f5_fiber80_controller25/PREDICTION_AND_SCOPE.md](../../research/ddp/refresh_20261029/f5_fiber80_controller25/PREDICTION_AND_SCOPE.md)；[research/ddp/refresh_20261029/f5_fiber80_controller25/PREPARE_HANDLE.json](../../research/ddp/refresh_20261029/f5_fiber80_controller25/PREPARE_HANDLE.json)；[research/ddp/refresh_20261029/f5_fiber80_controller25/PREPARE_TERMINAL.json](../../research/ddp/refresh_20261029/f5_fiber80_controller25/PREPARE_TERMINAL.json)；[research/ddp/refresh_20261029/f5_fiber80_controller25/STOP_BY_CHART_RIGIDITY.md](../../research/ddp/refresh_20261029/f5_fiber80_controller25/STOP_BY_CHART_RIGIDITY.md)；[research/ddp/refresh_20261029/f5_fiber80_controller25/prepare.py](../../research/ddp/refresh_20261029/f5_fiber80_controller25/prepare.py)；[research/ddp/refresh_20261029/FULLK2_C21_S80_WIKI_REPORT.md](../../research/ddp/refresh_20261029/FULLK2_C21_S80_WIKI_REPORT.md)；[reviews/ddp/new_fiber_route_obstructions_20261030.prompt.md](../../reviews/ddp/new_fiber_route_obstructions_20261030.prompt.md)；[reviews/ddp/new_fiber_route_obstructions_20261030.response.json](../../reviews/ddp/new_fiber_route_obstructions_20261030.response.json)；[reviews/ddp/new_fiber_route_obstructions_20261030.DISPOSITION.md](../../reviews/ddp/new_fiber_route_obstructions_20261030.DISPOSITION.md)；[research/ddp/refresh_20261029/NEWFIBER_REVIEW_D15_K2_WIKI_REPORT.md](../../research/ddp/refresh_20261029/NEWFIBER_REVIEW_D15_K2_WIKI_REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** NewS80={a=x-y!=0,b=z!=0}inF5^3,80points,fourfixeddirectionsandinversepairedAports0/1andBports2/3. Astepsscaleonlypassivenormalb,Bstepsscaleonlypassivenormala;activeF5*normalhasfourchoices. Reverse-compatiblechartsneednotpreserveS80asset. Onanysimplequarticcontroller,the16regularliftcannotD3withN>=25undertheseexacttwo-typeconditions.

**正向保证：** Thischangesfiber/charts/controllerandisnotarelabelingoftheclosed3750inducedproblem.；TheglobalframeworkboundcomesfromPROOFsection9,notfromthesinglechart43/55imageunions.；TheunrunfixedC25motifmodelisnecessaryonly;itwasnotreportedUNSAT.

**仍未完成：** 精确定义S80两type normal-scaling框架N≤24、阶数≤1920，实际外审SUCCESS/SOUND AS STATED。其它S/被动normal混合/非uniform/其它关系与一般N(16,3)未排。C25必要模型仅prepare，因定理停止启动，不能写solverUNSAT；未Lean、未生成2000图。

**启发与重启依据：** Theinitial76andN25necessaryinventorydidnotconstructalift. Tightwordaccountingatamandatoryt2rootforcesport-typepurity,thenownfiberhiddenvaluesgivetheactualobstruction. StopthisexactS80normal-scalingframeworkandunrunC25solver;changingonlycontrollercyclesortimerscannotfixit. OtherS/normalmixing/noiserelationsremainoutside.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

