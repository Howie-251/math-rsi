---
type: experiment
node_id: exp:ddp-d15-d4-literal15552-all648-k2-cooperative-cover-20261030
title: "Literal15552(15,4) all648-port K2 cooperation: exact route gate, direct fractional witness and complete integer UNKNOWN"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-30"
hardware: "singleworker;oneboundedintegercall"
duration: "Route1.111414086CPU+prepare0.809767605CPU;terminalsolver120.009668/whole121.957097678CPU"
provenance: "research/ddp/refresh_20261029/d15_D4_K2_route_gate/COMPILE_HANDLE.json; research/ddp/refresh_20261029/d15_D4_K2_route_gate/COMPILE_PROCESS_RESULT.json; research/ddp/refresh_20261029/d15_D4_K2_route_gate/HANDLE.json; research/ddp/refresh_20261029/d15_D4_K2_route_gate/NATIVE_HANDLE.json; research/ddp/refresh_20261029/d15_D4_K2_route_gate/NATIVE_PROCESS_RESULT.json; research/ddp/refresh_20261029/d15_D4_K2_route_gate/NATIVE_RESULT.json; research/ddp/refresh_20261029/d15_D4_K2_route_gate/PREDICTION_AND_SCOPE.md; research/ddp/refresh_20261029/d15_D4_K2_route_gate/REPORT.md; research/ddp/refresh_20261029/d15_D4_K2_route_gate/RESULT.json; research/ddp/refresh_20261029/d15_D4_K2_route_gate/T0_SUPPORTS.json; research/ddp/refresh_20261029/d15_D4_K2_route_gate/TERMINAL.json; research/ddp/refresh_20261029/d15_D4_K2_route_gate/gate.cpp; research/ddp/refresh_20261029/d15_D4_K2_route_gate/run_once.py; research/ddp/refresh_20261029/d15_D4_K2_fulltarget/COVERAGE_ROWS.json; research/ddp/refresh_20261029/d15_D4_K2_fulltarget/INPUT_SCOPE.json; research/ddp/refresh_20261029/d15_D4_K2_fulltarget/MODEL.json; research/ddp/refresh_20261029/d15_D4_K2_fulltarget/MODEL_CODE.md; research/ddp/refresh_20261029/d15_D4_K2_fulltarget/PREDICTION_AND_SCOPE.md; research/ddp/refresh_20261029/d15_D4_K2_fulltarget/PREPARE_HANDLE.json; research/ddp/refresh_20261029/d15_D4_K2_fulltarget/PREPARE_TERMINAL.json; research/ddp/refresh_20261029/d15_D4_K2_fulltarget/ROOT_CODE_REVIEW.md; research/ddp/refresh_20261029/d15_D4_K2_fulltarget/SELECTOR_MAP.json; research/ddp/refresh_20261029/d15_D4_K2_fulltarget/SOLVER_HANDLE.json; research/ddp/refresh_20261029/d15_D4_K2_fulltarget/SOLVER_TERMINAL.json; research/ddp/refresh_20261029/d15_D4_K2_fulltarget/prepare.py; research/ddp/refresh_20261029/d15_D4_K2_fulltarget/run_once.py; research/ddp/refresh_20261029/NEWFIBER_REVIEW_D15_K2_WIKI_REPORT.md; research/ddp/refresh_20261029/d15_translation_symmetry_gate/FIBER_PROJECTIONS.json; research/ddp/refresh_20261029/d15_translation_symmetry_gate/FREE_PORT_ORBITS.json; research/ddp/refresh_20261029/d15_translation_symmetry_gate/HANDLE.json; research/ddp/refresh_20261029/d15_translation_symmetry_gate/INPUT_AND_EQUATIONS.json; research/ddp/refresh_20261029/d15_translation_symmetry_gate/KERNEL_BASIS.json; research/ddp/refresh_20261029/d15_translation_symmetry_gate/PREDICTION_AND_SCOPE.md; research/ddp/refresh_20261029/d15_translation_symmetry_gate/REPORT.md; research/ddp/refresh_20261029/d15_translation_symmetry_gate/RESULT.json; research/ddp/refresh_20261029/d15_translation_symmetry_gate/TERMINAL.json; research/ddp/refresh_20261029/d15_translation_symmetry_gate/run_once.py"
added: 2026-10-30T02:56:25Z
tags: ["ddp", "method-ledger"]
---

# Literal15552(15,4) all648-port K2 cooperation: exact route gate, direct fractional witness and complete integer UNKNOWN

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (15,4)；L=15552；条件性n=15554（未据此计纪录）

**距目标的证据：** T0empty;alltargetR2providers3..18(5184targetshave3),R3providers67..185. OneR2cachegeneration648balls/oneoldsource_read,oldR3reused,1.111414086CPU. Complete1296selectors/19440vars/69306clausescontainsall31104two-sidecoverage rows. Actualone-t120UNKNOWN/code0,120.009668solver/121.957097678wholeCPU,24samePIDobservationtimeouts,0candidate/source-read/BFS/newgraphduringintegercall;stopped,notK2infeasibility.；完整同步fiber平移方程2880×768满秩768，核0、群仅identity，648个freeport各自成轨道，0.671092911CPU。该候选自同构不能提供固定单anchor的无损K2归约；未检验/排除全部Aut，原完整K2仍UNKNOWN。

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 15552,
  "source_m": 116316,
  "source_D4_inherited": true,
  "literal_ports": 648,
  "all_port_spares": 1,
  "side_pin_limit": 14,
  "source_file": "/inspire/hdd/global_user/mahaitong-240108120090/ar4math/research/ddp/more_graphs_20261027/d15_D4_current15552/source15552.header.edges",
  "old_R3_cache": "/inspire/hdd/global_user/mahaitong-240108120090/ar4math/research/ddp/more_graphs_20261027/d15_D4_current15552/single_vertex_R3_cover/R3_MASKS.bin",
  "route_source_reads": 1,
  "new_R2_balls": 648,
  "old_R3_recomputed": 0,
  "old_source_D4_BFS": 0,
  "R2_provider_min": 3,
  "R2_provider_max": 18,
  "R2_min_count_targets": 5184,
  "R3_provider_min": 67,
  "R3_provider_max": 185,
  "T0_size": 0,
  "route_gate_CPU_seconds": 1.111414086,
  "prepare_CPU_seconds": 0.809767605,
  "selectors": 1296,
  "variables": 19440,
  "clauses": 69306,
  "coverage_rows_all": 31104,
  "coverage_rows_unique": 31104,
  "all_ports_and_targets_encoded": true,
  "solver_status": "UNKNOWN",
  "actual_solver_calls": 1,
  "solver_CPU_seconds": 120.009668,
  "whole_CPU_seconds": 121.95709767800001,
  "observation_timeouts": 24,
  "same_PID_waited_to_exit": true,
  "current_running": false,
  "graphs_generated": 0,
  "integer_K2_family_excluded": false,
  "direct_fractional_each_side_port_weight": "1/70",
  "direct_fractional_each_side_sum": "324/35",
  "side_limit": 14,
  "direct_fractional_minimum_coverage": "(67+3)/70>=1",
  "direct_fractional_joint_usage_per_port": "1/35<=1",
  "direct_fractional_new_LP_calls": 0,
  "direct_fractional_optimality_claimed": false,
  "integer_existence_inferred_from_fractional": false,
  "new_record": false,
  "synchronous_fiber_translation_kernel_dimension": 0,
  "translation_based_K2_anchor_reduction_supported": false,
  "all_source_automorphisms_excluded": false
}
```



**从属变体：**
```json
[
  {
    "label": "all648_literal_R2_provider_gate_reuse_R3_20261030",
    "status": "T0_NECESSARY_GATE_PASSES_NO_INTEGER_EXISTENCE_CONCLUSION",
    "T0_size": 0,
    "computed_R2_balls": 648,
    "R2_min": 3,
    "R2_max": 18,
    "R2_min_count_targets": 5184,
    "R3_min": 67,
    "R3_max": 185,
    "source_reads": 1,
    "R3_recomputed": 0,
    "old_source_D4_BFS": 0,
    "aggregate_CPU_seconds": 1.111414086,
    "solver_calls": 0,
    "new_graphs": 0
  },
  {
    "label": "uniform_one_over70_per_side_exact_fractional_witness_from_provider_bounds_20261030",
    "status": "DIRECT_RATIONAL_RELAXATION_FEASIBLE_NO_LP",
    "ports_per_side": 648,
    "each_variable": "1/70",
    "each_side_total": "324/35<14",
    "coverage_at_least": "(67+3)/70=1",
    "joint_per_port": "1/35<=1",
    "LP_calls": 0,
    "integer_pins_or_graph_claimed": false
  },
  {
    "label": "all648_literalports_full15552_two_side_integer_single120s_call_20261030",
    "status": "UNKNOWN_TERMINAL",
    "selectors": 1296,
    "variables": 19440,
    "clauses": 69306,
    "all_target_rows": 31104,
    "all_ports_included": true,
    "side_pin_limit": 14,
    "capacity1_mutexes": 648,
    "grouping": false,
    "symmetry": false,
    "line_constraint": false,
    "LP_support_filter": false,
    "driver_pid": 3068247,
    "solver_pid": 3068250,
    "actual_solver_calls": 1,
    "returncode": 0,
    "solver_CPU_seconds": 120.009668,
    "whole_CPU_seconds": 121.95709767800001,
    "observation_timeouts": 24,
    "same_PID_waited_to_exit": true,
    "whole_CPU_budget": 150,
    "solver_window": 120,
    "SAT_candidates": 0,
    "source_reads": 0,
    "BFS_runs": 0,
    "graphs_generated": 0,
    "running": false,
    "automatic_continuation": false,
    "pending": [],
    "current_result": "research/ddp/refresh_20261029/d15_D4_K2_fulltarget/SOLVER_TERMINAL.json"
  },
  {
    "label": "full_synchronous_fiber_translation_kernel_gate_20261030",
    "status": "NO_NONTRIVIAL_FREEPORT_TRANSLATION_ACTION",
    "scope": "Only source-preserving simultaneous fiber translations x_c -> x_c+t_c for the literal 192-controller linear recipe; not all automorphisms.",
    "equations": 2880,
    "unknowns": 768,
    "rank": 768,
    "kernel_dimension": 0,
    "translation_group_order": 1,
    "all_960_arcs_checked": true,
    "deleted_virtual_loops_preserved": true,
    "literal_free_ports": 648,
    "free_port_orbits": 648,
    "freeport_transitive": false,
    "K2_single_anchor_reduction_justified": false,
    "CPU_seconds": 0.671092911,
    "source_graph_reads": 0,
    "BFS_runs": 0,
    "solver_calls": 0,
    "graph_exports": 0,
    "running": false,
    "all_Aut_excluded": false,
    "K2_family_excluded": false,
    "result": "research/ddp/refresh_20261029/d15_translation_symmetry_gate/RESULT.json"
  }
]
```

**原始证据：** [research/ddp/refresh_20261029/d15_D4_K2_route_gate/COMPILE_HANDLE.json](../../research/ddp/refresh_20261029/d15_D4_K2_route_gate/COMPILE_HANDLE.json)；[research/ddp/refresh_20261029/d15_D4_K2_route_gate/COMPILE_PROCESS_RESULT.json](../../research/ddp/refresh_20261029/d15_D4_K2_route_gate/COMPILE_PROCESS_RESULT.json)；[research/ddp/refresh_20261029/d15_D4_K2_route_gate/HANDLE.json](../../research/ddp/refresh_20261029/d15_D4_K2_route_gate/HANDLE.json)；[research/ddp/refresh_20261029/d15_D4_K2_route_gate/NATIVE_HANDLE.json](../../research/ddp/refresh_20261029/d15_D4_K2_route_gate/NATIVE_HANDLE.json)；[research/ddp/refresh_20261029/d15_D4_K2_route_gate/NATIVE_PROCESS_RESULT.json](../../research/ddp/refresh_20261029/d15_D4_K2_route_gate/NATIVE_PROCESS_RESULT.json)；[research/ddp/refresh_20261029/d15_D4_K2_route_gate/NATIVE_RESULT.json](../../research/ddp/refresh_20261029/d15_D4_K2_route_gate/NATIVE_RESULT.json)；[research/ddp/refresh_20261029/d15_D4_K2_route_gate/PREDICTION_AND_SCOPE.md](../../research/ddp/refresh_20261029/d15_D4_K2_route_gate/PREDICTION_AND_SCOPE.md)；[research/ddp/refresh_20261029/d15_D4_K2_route_gate/REPORT.md](../../research/ddp/refresh_20261029/d15_D4_K2_route_gate/REPORT.md)；[research/ddp/refresh_20261029/d15_D4_K2_route_gate/RESULT.json](../../research/ddp/refresh_20261029/d15_D4_K2_route_gate/RESULT.json)；[research/ddp/refresh_20261029/d15_D4_K2_route_gate/T0_SUPPORTS.json](../../research/ddp/refresh_20261029/d15_D4_K2_route_gate/T0_SUPPORTS.json)；[research/ddp/refresh_20261029/d15_D4_K2_route_gate/TERMINAL.json](../../research/ddp/refresh_20261029/d15_D4_K2_route_gate/TERMINAL.json)；[research/ddp/refresh_20261029/d15_D4_K2_route_gate/gate.cpp](../../research/ddp/refresh_20261029/d15_D4_K2_route_gate/gate.cpp)；[research/ddp/refresh_20261029/d15_D4_K2_route_gate/run_once.py](../../research/ddp/refresh_20261029/d15_D4_K2_route_gate/run_once.py)；[research/ddp/refresh_20261029/d15_D4_K2_fulltarget/COVERAGE_ROWS.json](../../research/ddp/refresh_20261029/d15_D4_K2_fulltarget/COVERAGE_ROWS.json)；[research/ddp/refresh_20261029/d15_D4_K2_fulltarget/INPUT_SCOPE.json](../../research/ddp/refresh_20261029/d15_D4_K2_fulltarget/INPUT_SCOPE.json)；[research/ddp/refresh_20261029/d15_D4_K2_fulltarget/MODEL.json](../../research/ddp/refresh_20261029/d15_D4_K2_fulltarget/MODEL.json)；[research/ddp/refresh_20261029/d15_D4_K2_fulltarget/MODEL_CODE.md](../../research/ddp/refresh_20261029/d15_D4_K2_fulltarget/MODEL_CODE.md)；[research/ddp/refresh_20261029/d15_D4_K2_fulltarget/PREDICTION_AND_SCOPE.md](../../research/ddp/refresh_20261029/d15_D4_K2_fulltarget/PREDICTION_AND_SCOPE.md)；[research/ddp/refresh_20261029/d15_D4_K2_fulltarget/PREPARE_HANDLE.json](../../research/ddp/refresh_20261029/d15_D4_K2_fulltarget/PREPARE_HANDLE.json)；[research/ddp/refresh_20261029/d15_D4_K2_fulltarget/PREPARE_TERMINAL.json](../../research/ddp/refresh_20261029/d15_D4_K2_fulltarget/PREPARE_TERMINAL.json)；[research/ddp/refresh_20261029/d15_D4_K2_fulltarget/ROOT_CODE_REVIEW.md](../../research/ddp/refresh_20261029/d15_D4_K2_fulltarget/ROOT_CODE_REVIEW.md)；[research/ddp/refresh_20261029/d15_D4_K2_fulltarget/SELECTOR_MAP.json](../../research/ddp/refresh_20261029/d15_D4_K2_fulltarget/SELECTOR_MAP.json)；[research/ddp/refresh_20261029/d15_D4_K2_fulltarget/SOLVER_HANDLE.json](../../research/ddp/refresh_20261029/d15_D4_K2_fulltarget/SOLVER_HANDLE.json)；[research/ddp/refresh_20261029/d15_D4_K2_fulltarget/SOLVER_TERMINAL.json](../../research/ddp/refresh_20261029/d15_D4_K2_fulltarget/SOLVER_TERMINAL.json)；[research/ddp/refresh_20261029/d15_D4_K2_fulltarget/prepare.py](../../research/ddp/refresh_20261029/d15_D4_K2_fulltarget/prepare.py)；[research/ddp/refresh_20261029/d15_D4_K2_fulltarget/run_once.py](../../research/ddp/refresh_20261029/d15_D4_K2_fulltarget/run_once.py)；[research/ddp/refresh_20261029/NEWFIBER_REVIEW_D15_K2_WIKI_REPORT.md](../../research/ddp/refresh_20261029/NEWFIBER_REVIEW_D15_K2_WIKI_REPORT.md)；[research/ddp/refresh_20261029/d15_translation_symmetry_gate/FIBER_PROJECTIONS.json](../../research/ddp/refresh_20261029/d15_translation_symmetry_gate/FIBER_PROJECTIONS.json)；[research/ddp/refresh_20261029/d15_translation_symmetry_gate/FREE_PORT_ORBITS.json](../../research/ddp/refresh_20261029/d15_translation_symmetry_gate/FREE_PORT_ORBITS.json)；[research/ddp/refresh_20261029/d15_translation_symmetry_gate/HANDLE.json](../../research/ddp/refresh_20261029/d15_translation_symmetry_gate/HANDLE.json)；[research/ddp/refresh_20261029/d15_translation_symmetry_gate/INPUT_AND_EQUATIONS.json](../../research/ddp/refresh_20261029/d15_translation_symmetry_gate/INPUT_AND_EQUATIONS.json)；[research/ddp/refresh_20261029/d15_translation_symmetry_gate/KERNEL_BASIS.json](../../research/ddp/refresh_20261029/d15_translation_symmetry_gate/KERNEL_BASIS.json)；[research/ddp/refresh_20261029/d15_translation_symmetry_gate/PREDICTION_AND_SCOPE.md](../../research/ddp/refresh_20261029/d15_translation_symmetry_gate/PREDICTION_AND_SCOPE.md)；[research/ddp/refresh_20261029/d15_translation_symmetry_gate/REPORT.md](../../research/ddp/refresh_20261029/d15_translation_symmetry_gate/REPORT.md)；[research/ddp/refresh_20261029/d15_translation_symmetry_gate/RESULT.json](../../research/ddp/refresh_20261029/d15_translation_symmetry_gate/RESULT.json)；[research/ddp/refresh_20261029/d15_translation_symmetry_gate/TERMINAL.json](../../research/ddp/refresh_20261029/d15_translation_symmetry_gate/TERMINAL.json)；[research/ddp/refresh_20261029/d15_translation_symmetry_gate/run_once.py](../../research/ddp/refresh_20261029/d15_translation_symmetry_gate/run_once.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixedliteral15552/116316source,oldD4inheritedandalloldedgesretained. Addadjacenthelpersy,zandchooseA,Bfromall648degree14/spare1oldvertices,|A|,|B|<=14,AintersectionBempty. ExactcoverageR3(A)unionR2(B)=VandR3(B)unionR2(A)=V. NoLPpoolfilter,grouping,symmetryorline restriction.

**正向保证：** Newsourceanddiameterradiiwereselectedexplicitly;thisisnottheoldsinglehelpertaskor14degreetimerresume.；Everyoldtargetisencodedonbothsidesfromliteralcacheorder,withoutdiscardingdistinctports.；ThefractionalrelaxationhasanexplicituniformrationalwitnesswithoutanLPcall;thisdoesnotgiveintegerpins.

**仍未完成：** Thespecificall648-portK2extensionof15552sourceisUNKNOWN,nocandidate15554graph. DirectfractionalfeasibilitydoesnotresolveintegerA/B. Originalsinglehelperandother15degreesourcesarenotrerunorexcluded.

**启发与重启依据：** Thetwo-helpermechanismtransferswithradii3/2andspare1disjointports,notbyassuming14degreefacts. T0gatehasnoobstructionandproviderboundsalreadygivefullfractionalfeasibility,sointegercompatibilityistheunresolvedquestion. ThefullunrestrictedliteralportselectorbatchactuallyendedUNKNOWN;stopwithoutinfeasibilityclaimorautomatictimer/seed/source-laddercontinuation.；同步平移入口经完整线性方程门已停止，不据此假设独立fiber平移或强加A0；其它实际自同构若要归约仍须给出作用和保全依据。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

