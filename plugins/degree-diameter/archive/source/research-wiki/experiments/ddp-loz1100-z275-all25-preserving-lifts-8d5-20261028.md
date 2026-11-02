---
type: experiment
node_id: exp:ddp-loz1100-z275-all25-preserving-lifts-8d5-20261028
title: "Loz1100旧125个固定5cover严格闭域保留；新phase-only F5的60联立tuple唯一试验UNKNOWN"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/REPORT.md; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/PREDICTION.json; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/ROOT_PREDICTION.md; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/RESULT.json; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/CASES.jsonl; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/ANALYSIS_NORMALIZATION.md; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/ANALYSIS_NORMALIZATION.json; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/ANALYSIS_CYCLE_COMPLEMENTARITY.md; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/ANALYSIS_CYCLE_COMPLEMENTARITY.json; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/run.py; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/RUN_HANDLE.json; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/terminal.json; research/ddp/more_graphs_20261027/d4_source_transfer/REPORT.md; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/all_action_lifts/REPORT.md; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/all_action_lifts/PREDICTION.json; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/all_action_lifts/RESULT.json; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/all_action_lifts/CASES.jsonl; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/all_action_lifts/INHERITED_R2_WIKI_ROW.json; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/all_action_lifts/run.py; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/all_action_lifts/RUN_HANDLE.json; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/all_action_lifts/terminal.json; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/ANALYSIS_ALL_ACTION_LIFTS.md; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/ANALYSIS_ALL_ACTION_LIFTS.json; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/base_route_multiplicity_gate/PREDICTION.json; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/base_route_multiplicity_gate/RESULT.json; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/base_route_multiplicity_gate/check.py; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/base_route_multiplicity_gate/FIVE_ROUTE_PREDICTION.json; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/base_route_multiplicity_gate/FIVE_ROUTE_RESULT.json; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/base_route_multiplicity_gate/five_routes.py; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/base_route_multiplicity_gate/COMPARISON.json; research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/base_route_multiplicity_gate/REPORT.md; research/ddp/two_successful_methods_20261101/d8_D5_phase_voltage_gate/PRED.md; research/ddp/two_successful_methods_20261101/d8_D5_phase_voltage_gate/NOTE.md; research/ddp/two_successful_methods_20261101/d8_D5_phase_voltage_gate/SIGNED_PHASE_ROUTE_FORMS.json; research/ddp/two_successful_methods_20261101/d8_D5_phase_voltage_gate/RESULT.json; research/ddp/two_successful_methods_20261101/d8_D5_phase_voltage_gate/SOLVER_RETURN.json; research/ddp/two_successful_methods_20261101/d8_D5_phase_voltage_gate/TERMINAL.json; research/ddp/two_successful_methods_20261101/d8_D5_phase_voltage_gate/BUDGET_LEDGER.json"
added: 2026-11-01T16:45:35Z
tags: ["ddp", "method-ledger"]
---

# Loz1100旧125个固定5cover严格闭域保留；新phase-only F5的60联立tuple唯一试验UNKNOWN

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (8,5)；L=5334；candidate_graph_or_family n=5500

**距目标的证据：** Originalr2 predictionREFUTED by25R5failures;newfouraction predictionREFUTED by100R5failures. Combinedall125actual5500/22000/simple8regularconnected graphs failidentityR5,withkernel5pointcoverage/R4projection1100 allsupported.0hit/unknown/untested;exactnegativeDnull andordinarybadpairsnull. 最新不同生成规则的phase-dependent additiveF5门：300signed phase-edge forms在60tight tuples内0恒等alias，不能推整tuple/60共同可实现。19tree gauge保留phase19 holonomy，1261整数vars/600rows/4880nnz；唯一11.007321186CPU solver返回UNKNOWN无incumbent，whole11.296287249/20终态，0新图/参数/Lean。旧125不重跑也不扩排到phase-only；不续timer/phase/seed，完整D5仍未知。

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 1100,
  "source_D_inherited": 4,
  "source_model": "RIGHT C20 semidirect2 Z55",
  "target_m": 22000,
  "raw_lifts_covered_by_normalization": 3125,
  "normalized_objects": 125,
  "objects_processed": 125,
  "actual_implicit_graphs": 125,
  "identity_R5_checks": 125,
  "kernel_R5_guarantee_checked_all25": true,
  "R4_projection_count_each": 1100,
  "all_first_missing_projections_nonidentity": true,
  "source_BFS_count": 0,
  "solver_calls": 0,
  "compile_CPU_seconds": 0,
  "worker_CPU_seconds": 1.116319,
  "hard_worker_CPU_seconds": 20,
  "prediction": "REFUTED",
  "cycle_complementarity_prediction": "SUPPORTED_ALL125",
  "new_lower_bounds": 0,
  "unknown": 0,
  "untested": 0,
  "root_R5_missing_per_case": [
    109,
    66,
    148,
    106,
    111,
    76,
    62,
    155,
    75,
    98,
    167,
    128,
    99,
    47,
    91,
    113,
    86,
    127,
    87,
    79,
    79,
    66,
    133,
    85,
    57,
    106,
    172,
    248,
    102,
    100,
    148,
    91,
    158,
    193,
    96,
    170,
    145,
    96,
    116,
    216,
    100,
    72,
    223,
    50,
    96,
    68,
    97,
    303,
    81,
    76,
    88,
    85,
    171,
    75,
    110,
    87,
    108,
    111,
    51,
    98,
    67,
    73,
    109,
    117,
    82,
    82,
    58,
    96,
    81,
    108,
    76,
    68,
    64,
    111,
    134,
    66,
    54,
    133,
    110,
    50,
    109,
    94,
    142,
    80,
    102,
    124,
    67,
    145,
    53,
    63,
    118,
    127,
    69,
    58,
    95,
    43,
    63,
    146,
    77,
    80,
    115,
    81,
    108,
    58,
    89,
    80,
    111,
    192,
    135,
    98,
    82,
    46,
    122,
    121,
    88,
    91,
    86,
    152,
    57,
    50,
    128,
    106,
    135,
    49,
    83
  ],
  "first_missing_projections_per_case": [
    [
      0,
      21
    ],
    [
      0,
      6
    ],
    [
      0,
      18
    ],
    [
      0,
      18
    ],
    [
      0,
      6
    ],
    [
      0,
      8
    ],
    [
      0,
      6
    ],
    [
      0,
      23
    ],
    [
      0,
      39
    ],
    [
      0,
      16
    ],
    [
      0,
      23
    ],
    [
      0,
      29
    ],
    [
      0,
      16
    ],
    [
      0,
      23
    ],
    [
      0,
      24
    ],
    [
      0,
      8
    ],
    [
      0,
      39
    ],
    [
      0,
      10
    ],
    [
      0,
      26
    ],
    [
      0,
      32
    ],
    [
      0,
      47
    ],
    [
      0,
      32
    ],
    [
      0,
      12
    ],
    [
      0,
      23
    ],
    [
      0,
      29
    ],
    [
      0,
      37
    ],
    [
      0,
      6
    ],
    [
      0,
      4
    ],
    [
      0,
      6
    ],
    [
      0,
      39
    ],
    [
      0,
      1
    ],
    [
      0,
      11
    ],
    [
      0,
      11
    ],
    [
      0,
      28
    ],
    [
      0,
      52
    ],
    [
      0,
      22
    ],
    [
      0,
      22
    ],
    [
      0,
      11
    ],
    [
      0,
      11
    ],
    [
      0,
      16
    ],
    [
      0,
      39
    ],
    [
      0,
      32
    ],
    [
      0,
      2
    ],
    [
      0,
      13
    ],
    [
      0,
      22
    ],
    [
      0,
      22
    ],
    [
      0,
      51
    ],
    [
      0,
      6
    ],
    [
      0,
      11
    ],
    [
      0,
      22
    ],
    [
      0,
      31
    ],
    [
      0,
      8
    ],
    [
      0,
      23
    ],
    [
      1,
      49
    ],
    [
      0,
      32
    ],
    [
      1,
      43
    ],
    [
      0,
      15
    ],
    [
      0,
      39
    ],
    [
      0,
      52
    ],
    [
      0,
      34
    ],
    [
      0,
      37
    ],
    [
      0,
      1
    ],
    [
      0,
      16
    ],
    [
      0,
      6
    ],
    [
      0,
      39
    ],
    [
      0,
      16
    ],
    [
      0,
      16
    ],
    [
      0,
      27
    ],
    [
      0,
      24
    ],
    [
      0,
      12
    ],
    [
      0,
      39
    ],
    [
      0,
      48
    ],
    [
      1,
      29
    ],
    [
      0,
      16
    ],
    [
      0,
      16
    ],
    [
      0,
      1
    ],
    [
      0,
      8
    ],
    [
      0,
      12
    ],
    [
      0,
      7
    ],
    [
      0,
      39
    ],
    [
      1,
      1
    ],
    [
      0,
      39
    ],
    [
      0,
      37
    ],
    [
      0,
      24
    ],
    [
      0,
      23
    ],
    [
      0,
      18
    ],
    [
      1,
      33
    ],
    [
      0,
      39
    ],
    [
      0,
      39
    ],
    [
      0,
      32
    ],
    [
      0,
      29
    ],
    [
      0,
      23
    ],
    [
      1,
      0
    ],
    [
      0,
      8
    ],
    [
      0,
      26
    ],
    [
      0,
      12
    ],
    [
      0,
      43
    ],
    [
      0,
      10
    ],
    [
      0,
      16
    ],
    [
      0,
      43
    ],
    [
      0,
      23
    ],
    [
      1,
      33
    ],
    [
      0,
      23
    ],
    [
      0,
      23
    ],
    [
      0,
      24
    ],
    [
      0,
      32
    ],
    [
      0,
      23
    ],
    [
      0,
      1
    ],
    [
      0,
      3
    ],
    [
      0,
      32
    ],
    [
      0,
      34
    ],
    [
      0,
      23
    ],
    [
      0,
      15
    ],
    [
      0,
      23
    ],
    [
      0,
      8
    ],
    [
      0,
      31
    ],
    [
      0,
      52
    ],
    [
      0,
      12
    ],
    [
      0,
      2
    ],
    [
      0,
      38
    ],
    [
      0,
      2
    ],
    [
      0,
      29
    ],
    [
      0,
      8
    ],
    [
      0,
      23
    ],
    [
      0,
      1
    ]
  ],
  "ordinary_bad_count_units": "null;single-rootR5missing targets,quotientprojectioncounts andfibercoveragehistograms are separate units",
  "original_r2_metrics_preserved": {
    "source_n": 1100,
    "source_D_inherited": 4,
    "source_model": "RIGHT C20 semidirect2 Z55",
    "target_m": 22000,
    "raw_lifts_covered_by_normalization": 625,
    "normalized_objects": 25,
    "objects_processed": 25,
    "actual_implicit_graphs": 25,
    "identity_R5_checks": 25,
    "kernel_R5_guarantee_checked_all25": true,
    "R4_projection_count_each": 1100,
    "all_first_missing_projections_nonidentity": true,
    "source_BFS_count": 0,
    "solver_calls": 0,
    "compile_CPU_seconds": 0,
    "worker_CPU_seconds": 0.24695499999999998,
    "hard_worker_CPU_seconds": 20,
    "prediction": "REFUTED",
    "cycle_complementarity_prediction": "SUPPORTED",
    "new_lower_bounds": 0,
    "unknown": 0,
    "untested": 0,
    "root_R5_missing_per_case": [
      109,
      66,
      148,
      106,
      111,
      76,
      62,
      155,
      75,
      98,
      167,
      128,
      99,
      47,
      91,
      113,
      86,
      127,
      87,
      79,
      79,
      66,
      133,
      85,
      57
    ],
    "first_missing_projections_per_case": [
      [
        0,
        21
      ],
      [
        0,
        6
      ],
      [
        0,
        18
      ],
      [
        0,
        18
      ],
      [
        0,
        6
      ],
      [
        0,
        8
      ],
      [
        0,
        6
      ],
      [
        0,
        23
      ],
      [
        0,
        39
      ],
      [
        0,
        16
      ],
      [
        0,
        23
      ],
      [
        0,
        29
      ],
      [
        0,
        16
      ],
      [
        0,
        23
      ],
      [
        0,
        24
      ],
      [
        0,
        8
      ],
      [
        0,
        39
      ],
      [
        0,
        10
      ],
      [
        0,
        26
      ],
      [
        0,
        32
      ],
      [
        0,
        47
      ],
      [
        0,
        32
      ],
      [
        0,
        12
      ],
      [
        0,
        23
      ],
      [
        0,
        29
      ]
    ],
    "ordinary_bad_count_units": "null;single-rootR5missing targets,quotientprojectioncounts andfibercoveragehistograms are separate units"
  },
  "legal_action_lifts": [
    2,
    57,
    112,
    167,
    222
  ],
  "kernel_R5_guarantee_checked_all125": true,
  "original_r2_prediction": "REFUTED",
  "new_four_action_prediction": "REFUTED",
  "new_action_worker_CPU_seconds": 0.869364,
  "combined_separate_workers_CPU_seconds": 1.116319,
  "original_r2_not_rerun": true,
  "new_objects": 100,
  "budget_scope": "Two distinct finiteworkers:originalr2 20CPUlimit;newremaining100 20CPUlimit;originalnotrerun.",
  "source_NB_le5_minimum_routes": 5,
  "source_tight_fibres": 3,
  "tight_g3_fibre_fullcover_settings": 10,
  "targeted_five_route_image_histogram": {
    "2": 10,
    "3": 45,
    "4": 60,
    "5": 10
  },
  "diagnostic_raw_shortage_prediction": "REFUTED",
  "diagnostic_uniform_alias_prediction": "REFUTED",
  "diagnostic_new_graphs": 0,
  "diagnostic_old_BFS_reruns": 0,
  "diagnostic_CPU_seconds": 0.014279437999999998,
  "new_phase_only_additive_F5_gate": {
    "status": "UNKNOWN_SINGLE_BOUNDED_SOLVER",
    "source": "fixedLoz1100RIGHTlaw",
    "deck": "additiveF5_phase-dependenttheta_sourcephasepositiveandreversesignsameedge",
    "old125_metacyclic_domain_rerun": false,
    "old125_strict_scope_preserved": true,
    "route_forms": 300,
    "tight_five_tuples": 60,
    "identical_coefficient_pairs_within_tuples": 0,
    "no_alias_is_not_joint_realizability": true,
    "gauge": "19type0spanningtreeequations;phase19holonomyfree",
    "theta_variables": 61,
    "total_integer_variables": 1261,
    "equality_rows": 600,
    "nonzeros": 4880,
    "solver_calls": 1,
    "solver_CPU": 11.007321186,
    "whole_CPU": 11.296287248999999,
    "whole_budget": 20,
    "solver_budget": 12,
    "integer_incumbent": false,
    "independent_UNSAT_proof": false,
    "terminal": true,
    "no_automatic_continuation": true,
    "no_5500_graph_generated": true,
    "new_graph_parameter_Lean_method_increment": [
      0,
      0,
      0,
      0
    ],
    "scope": "onlynewphase-dependentadditiveF5rule;notnormal-coordinate-dependentvoltages_arbitrarydeckpermutations_generalN8D5",
    "prediction": "UNKNOWN_joint60tuplesnotresolved",
    "note": "research/ddp/two_successful_methods_20261101/d8_D5_phase_voltage_gate/NOTE.md"
  }
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/REPORT.md](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/REPORT.md)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/PREDICTION.json](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/PREDICTION.json)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/ROOT_PREDICTION.md](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/ROOT_PREDICTION.md)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/RESULT.json](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/RESULT.json)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/CASES.jsonl](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/CASES.jsonl)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/ANALYSIS_NORMALIZATION.md](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/ANALYSIS_NORMALIZATION.md)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/ANALYSIS_NORMALIZATION.json](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/ANALYSIS_NORMALIZATION.json)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/ANALYSIS_CYCLE_COMPLEMENTARITY.md](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/ANALYSIS_CYCLE_COMPLEMENTARITY.md)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/ANALYSIS_CYCLE_COMPLEMENTARITY.json](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/ANALYSIS_CYCLE_COMPLEMENTARITY.json)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/run.py](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/run.py)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/RUN_HANDLE.json](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/RUN_HANDLE.json)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/terminal.json](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/terminal.json)；[research/ddp/more_graphs_20261027/d4_source_transfer/REPORT.md](../../research/ddp/more_graphs_20261027/d4_source_transfer/REPORT.md)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/all_action_lifts/REPORT.md](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/all_action_lifts/REPORT.md)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/all_action_lifts/PREDICTION.json](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/all_action_lifts/PREDICTION.json)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/all_action_lifts/RESULT.json](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/all_action_lifts/RESULT.json)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/all_action_lifts/CASES.jsonl](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/all_action_lifts/CASES.jsonl)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/all_action_lifts/INHERITED_R2_WIKI_ROW.json](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/all_action_lifts/INHERITED_R2_WIKI_ROW.json)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/all_action_lifts/run.py](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/all_action_lifts/run.py)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/all_action_lifts/RUN_HANDLE.json](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/all_action_lifts/RUN_HANDLE.json)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/all_action_lifts/terminal.json](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/all_action_lifts/terminal.json)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/ANALYSIS_ALL_ACTION_LIFTS.md](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/ANALYSIS_ALL_ACTION_LIFTS.md)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/ANALYSIS_ALL_ACTION_LIFTS.json](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/ANALYSIS_ALL_ACTION_LIFTS.json)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/base_route_multiplicity_gate/PREDICTION.json](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/base_route_multiplicity_gate/PREDICTION.json)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/base_route_multiplicity_gate/RESULT.json](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/base_route_multiplicity_gate/RESULT.json)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/base_route_multiplicity_gate/check.py](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/base_route_multiplicity_gate/check.py)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/base_route_multiplicity_gate/FIVE_ROUTE_PREDICTION.json](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/base_route_multiplicity_gate/FIVE_ROUTE_PREDICTION.json)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/base_route_multiplicity_gate/FIVE_ROUTE_RESULT.json](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/base_route_multiplicity_gate/FIVE_ROUTE_RESULT.json)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/base_route_multiplicity_gate/five_routes.py](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/base_route_multiplicity_gate/five_routes.py)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/base_route_multiplicity_gate/COMPARISON.json](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/base_route_multiplicity_gate/COMPARISON.json)；[research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/base_route_multiplicity_gate/REPORT.md](../../research/ddp/more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/base_route_multiplicity_gate/REPORT.md)；[research/ddp/two_successful_methods_20261101/d8_D5_phase_voltage_gate/PRED.md](../../research/ddp/two_successful_methods_20261101/d8_D5_phase_voltage_gate/PRED.md)；[research/ddp/two_successful_methods_20261101/d8_D5_phase_voltage_gate/NOTE.md](../../research/ddp/two_successful_methods_20261101/d8_D5_phase_voltage_gate/NOTE.md)；[research/ddp/two_successful_methods_20261101/d8_D5_phase_voltage_gate/SIGNED_PHASE_ROUTE_FORMS.json](../../research/ddp/two_successful_methods_20261101/d8_D5_phase_voltage_gate/SIGNED_PHASE_ROUTE_FORMS.json)；[research/ddp/two_successful_methods_20261101/d8_D5_phase_voltage_gate/RESULT.json](../../research/ddp/two_successful_methods_20261101/d8_D5_phase_voltage_gate/RESULT.json)；[research/ddp/two_successful_methods_20261101/d8_D5_phase_voltage_gate/SOLVER_RETURN.json](../../research/ddp/two_successful_methods_20261101/d8_D5_phase_voltage_gate/SOLVER_RETURN.json)；[research/ddp/two_successful_methods_20261101/d8_D5_phase_voltage_gate/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/d8_D5_phase_voltage_gate/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/d8_D5_phase_voltage_gate/BUDGET_LEDGER.json](../../research/ddp/two_successful_methods_20261101/d8_D5_phase_voltage_gate/BUDGET_LEDGER.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** FixedLoz1100 π55 source recipe RIGHT C20/action2onZ55. TargetZ275 withall5 legalactionlifts r2/57/112/167/222;for eachr allsource-label-preserving voltage lifts normalize625to25 positives(1,0),(12,33+55s),(11,1),(16,19+55t),s,t0..4. Combined125normalizedobjects covering3125rawchoices. Originalr2batch inherited,notrerun;100newcasebatch completesclass. Notother275basegenerators.

**仍未完成：** OtherZ275basegenerators/phase/sourceprojections,othercoverrules or general5500graphs/N(8,5) remainunexcluded. Noexactnegativeglobaldiameter orordinaryallpairbadcount was measured.

**启发与重启依据：** Completekernelcyclecomplementarity survives everylegalactionlift butcross-fiberD5coverage fails for allnormalizedsource-preserving action/voltage choices. The originalr2 failure was not extrapolated:fournewactions were explicitly tested. This fullfiniteclass nowcloses; no extraactions/s/t/primes/phases orbadpairtuning. Other275basegenerators require a substantively differentrule. Targeteddiagnostics refutedraw-shortage anduniversalalias guesses:minimum5routes,10settings filltightg3fibre; r2s1t1 stillmissesdifferentfibre(0,6). Stopthejointlyfailedclass; nogeneralordinary-coverexclusion follows. 新phase-only只说明universalalias障碍未发生，变量耦合仍未解，UNKNOWN不升级无望。该门已终态，不自动继续F5phase/换field/seed；旧125范围保持原严格边界，新工作由D2旧边改造与现D4证明两问题占用，不开第3数学线。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

