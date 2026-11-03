---
type: experiment
node_id: exp:ddp-stale-d10d3-650-eight-fp-endpoint-transfer651-mip-unknown-20261101
title: "10D3 actual650 FP转移：8385容量全过，650变量精确投影18秒仍UNKNOWN，0候选"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: partial
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/SOURCE650_FP_TRANSFER_READ_GATE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/SOURCE650_FP_TRANSFER_READ_GATE.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_once.py; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_MODEL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_MODEL_MATRIX.npz; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_SOLVER_RETURN.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_HANDLE.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/ROOT_DISPOSITION.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/STRUCTURAL_AND_PROJECTED_ROOT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/STRUCTURAL_AND_PROJECTED_NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/NEXT_STRUCTURAL_READ_GATE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/NEXT_STRUCTURAL_READ_GATE.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/PROJECTED_F_COVER_EQUIVALENCE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/twin_class_packet_capacity_gate/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/twin_class_packet_capacity_gate/run_once.py; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/twin_class_packet_capacity_gate/run.cpp; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/twin_class_packet_capacity_gate/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/twin_class_packet_capacity_gate/TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/twin_class_packet_capacity_gate/FIRST_CAPACITY_PASS_WITNESS.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/twin_class_packet_capacity_gate/PAPER_SCOPE_REVIEW.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/projected_F_cover_once/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/projected_F_cover_once/run_once.py; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/projected_F_cover_once/MODEL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/projected_F_cover_once/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/projected_F_cover_once/TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/projected_F_cover_once/SOLVER_RETURN.json"
added: 2026-11-02T01:57:08Z
tags: ["ddp", "method-ledger"]
---

# 10D3 actual650 FP转移：8385容量全过，650变量精确投影18秒仍UNKNOWN，0候选

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** fixed_host_FP_twin_packet_capacity_and_exact_projected_cover_UNKNOWN

**目标与阶数：** (10,3)；L=650；条件性n=651（未据此计纪录）

**距目标的证据：** No F-cover object,651candidate,donorassignment,PPpairing,newrootoroldrootBFS. Old1170window and new650integerprojectionboth timed outwithoutincumbent; complete8385capacityuppergate excludednone.；旧1170/1302/90480唯一20秒UNKNOWN及22.084731374CPU完整保历史。新包容量门8385/8385全upper-pass、0fail、minsurplus46；Cf均72/Dp均86，65对twin的D全不同。首P0/73的U366、T449、实际八包并337，漏29，只展示该argmax重复，不能排其它cover。按K8,2消去donor得到650binary/652rows/50440nnz的整数精确F-cover投影，sole18秒HiGHS实际18.007674689CPU、status1/TimeLimit/primalNone，仍UNKNOWN。无F-cover、donor/PP/651graph/BFS。最终42.416193092/45含root整理，禁止第三solve/seed。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_parameter_pairs": 0,
  "new_Lean_instances": 0,
  "new_independent_method_claims": 0,
  "source_n": 650,
  "source_m": 3250,
  "source_regular_degree": 10,
  "source_P": 130,
  "source_F": 520,
  "source_F_neighborhood_twin_pairs": 65,
  "inherited_P_cycle_lengths": [
    79,
    21,
    30
  ],
  "hypothetical_order": 651,
  "hypothetical_m_when3new_PP": 3255,
  "target_maxdegree": 10,
  "already_old_PP_allowed_underdegree9": true,
  "eight_distinct_F_P_cuts": true,
  "source_B2_F_coverage_exact_by_twin_paper": true,
  "PPrepairs_cannot_aid_newroot_F_le3": true,
  "model_binary_variables": 650,
  "model_FP_variables": 1040,
  "model_starP_variables": 130,
  "model_rows": 652,
  "model_nonzeros": 50440,
  "objective": "zero_feasibility",
  "solver": "SciPy milp/HiGHS",
  "solver_threads": 1,
  "solver_time_limit_seconds": 18,
  "solver_calls": 2,
  "solver_actual_status": 1,
  "solver_message": "Time limit reached. (HiGHS Status 13: model_status is Time limit reached; primal_status is None)",
  "solver_incumbent": null,
  "solver_returned_infeasible": false,
  "certified_infeasibility": false,
  "mip_node_count": null,
  "mip_dual_bound": null,
  "mip_gap": null,
  "solver_CPU_seconds": 18.007674688999998,
  "prediction_status": "CAPACITY_UPPER_PASS_SUPPORTED; ACTUAL_F_COVER_EXISTENCE_UNRESOLVED",
  "frozen_prototypes": 0,
  "planned_pairing_domain": 15,
  "actual_pairings": 0,
  "newroot_BFS": 0,
  "oldroot_BFS": 0,
  "source_validity_BFS": 0,
  "candidate_graphs": 0,
  "literal_input_parses": 1,
  "existing_A2_reused": true,
  "new_walkmatrix_field_Lean_review_runs": 0,
  "prior_read_CPU_seconds": 1.50087698,
  "new_preparation_CPU_seconds": 0.25,
  "actual_parent_allthreads_CPU_seconds": 20.333854394,
  "actual_children_CPU_seconds": 0,
  "wholecase_CPU_seconds": 42.416193092,
  "wholecase_CPU_cap_seconds": 45,
  "all_processes_terminal": true,
  "old_purehub_scope": "delete1to5oldedges/newhubadjacentALLdistinctendpoints/nootheradditionsCOMPLETE_NO_inherited",
  "shortlist_cells_newly_tested": 14,
  "shortlist_new_legal_graphs": 0,
  "same_Goal": "ACTIVE",
  "old_N8_n61": "PAUSED",
  "historical_original_1170_record_before_structural_projection_20261102": {
    "id": "ddp-stale-d10d3-650-eight-fp-endpoint-transfer651-mip-unknown-20261101",
    "title": "10D3 actual650八FP端点转移：1170变量单窗口20秒无incumbent，UNKNOWN而非不可行",
    "family": "F-neighborhood-twin coverage with FP endpoint transfer and PP repairs",
    "idea_family": "idea:ddp-open-parameter-construction-20261026",
    "date": "2026-11-01",
    "wiki_verdict": "partial",
    "record_type": "fixed_host_FP_surgery_core_coverage_feasibility_UNKNOWN_no_candidate",
    "target_Delta": 10,
    "target_D": 3,
    "savedL": 650,
    "baseline_date": "Inherited actual650/3250 Delorme polarity-replication source and current saved-main650; no new public-source search or sourceD3 validation",
    "n": {
      "actual": null,
      "hypothetical": 651
    },
    "actual_graph_Delta": null,
    "actual_D": null,
    "actual_D_scope": "No651graph,prototypeorordinarydistanceBFSwasgenerated. OneexactF-onlycoverageMIPwindowreturnedUNKNOWNwithoutincumbent;15PPpairingsandnewroot/oldrootstageswereNOT_ENTERED.",
    "ordinary_bad_unordered_pairs": null,
    "ordinary_bad_target_D": 3,
    "new_lower_bound": false,
    "scope": "Fixedactual650/3250all10sourcewithP130,F520,65F-neighborhoodtwinsandPPcycles79/21/30. Select8oldFPcutswithdistinctFandPends;addonezadjacentall8Fand2selecteddonorP;pairremaining6Pby3PPrepairs,allowingalready-oldPPedgeswithunderdegree9becausecap<=10. OneHiGHSfeasibilitywindowonlyselectsthe8cuts/2PstarbyexactsourceB2Fcoverage. Noincumbent,soNOprototypefreeze,pairing,candidateorD3test. Notthesameasold<=5cut/allendpoints/purehubNO;notageneralFP-familyexclusion.",
    "outcome_class": "ROOT_ACCEPTED_ACTUAL_TIMEOUT_UNKNOWN_NO_FAMILY_EXCLUSION",
    "distance_text": "正预测是存在8FP/2Pstar使新根三步覆盖520F。继承twin替路将删边后F-only门精确写成sourceB2(S)，PP修补不能补z→F。一次1170binary(1040FP+130Pstar)/1302rows/90480nnz、c=0、threads1/time_limit20，HiGHS实际status1 Time limit reached/primalNone，x为空；不是rawINFEASIBLE。solver20.013963667CPU，进程20.333854394，累计22.084731374/45含read1.50087698+prep.25。无incumbent，预测UNRESOLVED，未冻结原型、0/15pairings、0新旧根BFS、0候选图，不能归因旧P损伤或把未进入stage记失败。",
    "lesson_and_restart_condition": "STOPthissinglefeasibilitywindowwithoutsecondsolver,seed,prototypeorbudgetextension. KeepUNKNOWNdistinctfromcertifiedNO;thereisnocandidatefromwhichtoinferoldPdamage. Themodelisreviewable,butnoincumbentdoesnotproveF-routecoverageimpossible. ExistingPPedgesremainlegalunderdegree9inthepreparedpairinginterface;itwasnotexecuted. Anyfutureworkrequiresanexplicitnewboundedstructuralquestion;donotautomaticallyrepeatthesametimewindow.",
    "restart_condition": "Anewexplicitboundedquestionorchangedconnection/encodingauthorizedbyroot;notmerelymoretime,anotherseedorthesameF-coverfeasibilitywindow.",
    "unclosed_gap": "WholeFP-transferfamilyremainsUNKNOWN;nocertifiedinfeasibility,integerportselection,15pairingresult,newrootcoverageoroldoldD3evidence. No651graph/newparameter/Lean/methodorpriorityclaim. SameGoalACTIVE,oldN8/n61PAUSED.",
    "positive_guarantees": [
      "ActualsourceandP/F/twins/A2A3comefromthe650degree10D3cache,notother650degree5D5or6D4objects.",
      "SourceR2usescachedordinaryA2positivityplusidentityandadjacency;noBFS,newmatrixmultiplication,fieldorsourceD3validation.",
      "F/Pcutend<=1,starPrequiresdonorP,sumcuts8,sumstarP2andall520Fcoverageconstraintsareinthepersisted1170binarymodel.",
      "TheF-neighborhoodtwinbridgehandlescutendpointsthatarenotallstarspokes;genericall-endpointdistanceinvarianceisnotmisapplied.",
      "Actualsolverstatus1/noincumbentisnotINFEASIBLEorstrictfamilyNO;alllaterstagesareexplicitlyunexecuted."
    ],
    "other_metrics": {
      "new_graphs": 0,
      "new_parameter_pairs": 0,
      "new_Lean_instances": 0,
      "new_independent_method_claims": 0,
      "source_n": 650,
      "source_m": 3250,
      "source_regular_degree": 10,
      "source_P": 130,
      "source_F": 520,
      "source_F_neighborhood_twin_pairs": 65,
      "inherited_P_cycle_lengths": [
        79,
        21,
        30
      ],
      "hypothetical_order": 651,
      "hypothetical_m_when3new_PP": 3255,
      "target_maxdegree": 10,
      "already_old_PP_allowed_underdegree9": true,
      "eight_distinct_F_P_cuts": true,
      "source_B2_F_coverage_exact_by_twin_paper": true,
      "PPrepairs_cannot_aid_newroot_F_le3": true,
      "model_binary_variables": 1170,
      "model_FP_variables": 1040,
      "model_starP_variables": 130,
      "model_rows": 1302,
      "model_nonzeros": 90480,
      "objective": "zero_feasibility",
      "solver": "SciPy milp/HiGHS",
      "solver_threads": 1,
      "solver_time_limit_seconds": 20,
      "solver_calls": 1,
      "solver_actual_status": 1,
      "solver_message": "Time limit reached. (HiGHS Status 13: model_status is Time limit reached; primal_status is None)",
      "solver_incumbent": null,
      "solver_returned_infeasible": false,
      "certified_infeasibility": false,
      "mip_node_count": null,
      "mip_dual_bound": null,
      "mip_gap": null,
      "solver_CPU_seconds": 20.013963667,
      "prediction_status": "UNRESOLVED_NO_INCUMBENT_NOT_REFUTED",
      "frozen_prototypes": 0,
      "planned_pairing_domain": 15,
      "actual_pairings": 0,
      "newroot_BFS": 0,
      "oldroot_BFS": 0,
      "source_validity_BFS": 0,
      "candidate_graphs": 0,
      "literal_input_parses": 1,
      "existing_A2_reused": true,
      "new_walkmatrix_field_Lean_review_runs": 0,
      "prior_read_CPU_seconds": 1.50087698,
      "new_preparation_CPU_seconds": 0.25,
      "actual_parent_allthreads_CPU_seconds": 20.333854394,
      "actual_children_CPU_seconds": 0,
      "wholecase_CPU_seconds": 22.084731374,
      "wholecase_CPU_cap_seconds": 45,
      "all_processes_terminal": true,
      "old_purehub_scope": "delete1to5oldedges/newhubadjacentALLdistinctendpoints/nootheradditionsCOMPLETE_NO_inherited",
      "shortlist_cells_newly_tested": 14,
      "shortlist_new_legal_graphs": 0,
      "same_Goal": "ACTIVE",
      "old_N8_n61": "PAUSED"
    },
    "evidence_paths": [
      "research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/SOURCE650_FP_TRANSFER_READ_GATE.md",
      "research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/SOURCE650_FP_TRANSFER_READ_GATE.json",
      "research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_PRED.md",
      "research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_once.py",
      "research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_MODEL.json",
      "research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_MODEL_MATRIX.npz",
      "research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_SOLVER_RETURN.json",
      "research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_RESULT.json",
      "research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_TERMINAL.json",
      "research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_HANDLE.json",
      "research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_NOTE.md",
      "research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/ROOT_DISPOSITION.json"
    ]
  },
  "current_model_F_variables": 520,
  "current_model_starP_variables": 130,
  "current_projection_solver_calls": 1,
  "old_solver_resumed": false,
  "capacity_pairs_checked": 8385,
  "capacity_upper_pass": 8385,
  "capacity_upper_fail": 0,
  "capacity_minimum_surplus": 46,
  "C_f_uniform_packet_size": 72,
  "D_p_uniform_packet_size": 86,
  "twin_D_equal_pairs": 0,
  "first_capacity_witness": {
    "starP": [
      0,
      73
    ],
    "U": 366,
    "upper": 449,
    "actual_residual_union": 337,
    "missing": 29,
    "not_a_candidate": true
  },
  "current_integer_projection_equivalent_to_old_F_cover_only": true,
  "maximum_safe_donor_assignment_bound_per_yz": 256,
  "single_canonical_donor_failure_not_full_yz_exclusion": true,
  "structural_and_projected_terminal_20261102": {
    "status": "ROOT_ACCEPTED_CAPACITY_GATE_LOOSE_AND_PROJECTED_TIMEOUT_STILL_UNKNOWN_STOP",
    "source": "actual650/3250,d10,D3inherited,F520/P130/65twinclasses",
    "target": [
      10,
      3,
      651
    ],
    "actual_capacity_pairs": 8385,
    "capacity_upper_pass": 8385,
    "capacity_upper_fail": 0,
    "minimum_upper_surplus": 46,
    "C_f_size": 72,
    "D_p_size": 86,
    "twin_D_equal_count": 0,
    "first_capacity_witness": {
      "starP": [
        0,
        73
      ],
      "residual": 366,
      "upper449_vs_actual337": true,
      "actual_missing_F": 29,
      "not_candidate": true
    },
    "exact_projection_model": {
      "variables": 650,
      "rows": 652,
      "nnz": 50440,
      "equivalent_to_old_F_cover_only": true,
      "new_solver_calls": 1,
      "solver_time_window": 18,
      "actual_solver_CPU": 18.007674688999998,
      "status": 1,
      "primal": null
    },
    "previous_original_window": "1170/1302/90480,once20secondsUNKNOWN; not resumed",
    "whole_rule_status": "UNKNOWN",
    "numeric_infeasibility_or_No_claim": false,
    "Fcover_object_donor_PP_pairings_newroot_oldroot_BFS_graph_Lean_ARIS": 0,
    "old_case_CPU_before_root": 42.316193092,
    "root_disposition_charge_CPU": 0.1,
    "wholecase_CPU": 42.416193092,
    "case_cap": 45,
    "root_read": [
      "twin_class_packet_capacity_gate/PRED.md",
      "twin_class_packet_capacity_gate/run_once.py",
      "twin_class_packet_capacity_gate/run.cpp",
      "twin_class_packet_capacity_gate/RESULT.json",
      "twin_class_packet_capacity_gate/FIRST_CAPACITY_PASS_WITNESS.json",
      "twin_class_packet_capacity_gate/PAPER_SCOPE_REVIEW.md",
      "PROJECTED_F_COVER_EQUIVALENCE.md",
      "projected_F_cover_once/PRED.md",
      "projected_F_cover_once/run_once.py",
      "projected_F_cover_once/RESULT.json",
      "projected_F_cover_once/SOLVER_RETURN.json"
    ],
    "new_graph_parameter_Lean": [
      0,
      0,
      0
    ],
    "stop": "no thirdMIP/seed/extraFPcuts. Switch parameter; preserve projected exactness/cache for future new insight.",
    "Goal_complete": false
  },
  "new_source_A2_A3_BFS_graph_Lean_ARIS": 0,
  "no_third_solve_or_seed": true
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/SOURCE650_FP_TRANSFER_READ_GATE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/SOURCE650_FP_TRANSFER_READ_GATE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/SOURCE650_FP_TRANSFER_READ_GATE.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/SOURCE650_FP_TRANSFER_READ_GATE.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_once.py](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_once.py)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_MODEL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_MODEL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_MODEL_MATRIX.npz](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_MODEL_MATRIX.npz)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_SOLVER_RETURN.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_SOLVER_RETURN.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_HANDLE.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_HANDLE.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/ROOT_DISPOSITION.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/ROOT_DISPOSITION.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/STRUCTURAL_AND_PROJECTED_ROOT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/STRUCTURAL_AND_PROJECTED_ROOT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/STRUCTURAL_AND_PROJECTED_NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/STRUCTURAL_AND_PROJECTED_NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/NEXT_STRUCTURAL_READ_GATE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/NEXT_STRUCTURAL_READ_GATE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/NEXT_STRUCTURAL_READ_GATE.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/NEXT_STRUCTURAL_READ_GATE.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/PROJECTED_F_COVER_EQUIVALENCE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/PROJECTED_F_COVER_EQUIVALENCE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/twin_class_packet_capacity_gate/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/twin_class_packet_capacity_gate/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/twin_class_packet_capacity_gate/run_once.py](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/twin_class_packet_capacity_gate/run_once.py)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/twin_class_packet_capacity_gate/run.cpp](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/twin_class_packet_capacity_gate/run.cpp)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/twin_class_packet_capacity_gate/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/twin_class_packet_capacity_gate/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/twin_class_packet_capacity_gate/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/twin_class_packet_capacity_gate/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/twin_class_packet_capacity_gate/FIRST_CAPACITY_PASS_WITNESS.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/twin_class_packet_capacity_gate/FIRST_CAPACITY_PASS_WITNESS.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/twin_class_packet_capacity_gate/PAPER_SCOPE_REVIEW.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/twin_class_packet_capacity_gate/PAPER_SCOPE_REVIEW.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/projected_F_cover_once/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/projected_F_cover_once/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/projected_F_cover_once/run_once.py](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/projected_F_cover_once/run_once.py)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/projected_F_cover_once/MODEL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/projected_F_cover_once/MODEL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/projected_F_cover_once/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/projected_F_cover_once/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/projected_F_cover_once/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/projected_F_cover_once/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/projected_F_cover_once/SOLVER_RETURN.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/projected_F_cover_once/SOLVER_RETURN.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixed actual650/3250 all10 source,F520/P130/65K8,2twinclasses and PP cycles79/21/30. EightFPcuts have distinctF/Pends; newz joins8F+2selecteddonorP; remaining6P may be repaired by15pairings, retaining already-oldPPedges as legaldegree9 branches. The650binary projection is integer-equivalent only to the oldF-cover selection,notfull651/D3. All8385actualstarPpairs pass the capacityupperbound; no actualFcover found. Two distinct explicitlyauthorized solverencodings each had onewindow,notanoldtimercontinuation.

**正向保证：** Historical original1170binary/1302rows/90480nnz sole20secondUNKNOWN is preserved verbatim in historical_original_1170_record_before_structural_projection_20261102.；All8385unorderedactualstarPpairs were visited;65sametwinpairs retained. C/Dpackets were extracted fromcachedoldcovercoefficients without source/A2/A3 ornewBFS.；Class0/1/2capacity is a valid upperbound; its decreasingmarginal top6 optimization is exact for that bound,notactualglobalcover. Allpairs pass and the firstactualunion337<U366.；Everyclass isK8,2: sumy<=2 and sumz<=sumy permit exactinteger donor reconstruction. Actual130starPcolumns remain separate; twinDcolumns differ.；The new650variablemodel got its own single18secondwindow and noincumbent; compression neither proves speedup norinfeasibility. It doesnotresume theoldsolver.；ExistingPPedges may remain withdegree9. Downstreamdonor/pairing/newroot/oldold stages were neverentered. Singlecanonicaldonorfailure wouldnotcloseotherassignments.

**仍未完成：** The fixedFP-transferF-cover and general651/D3 questions remainUNKNOWN. No integer Fcover,donor assignment,PPrepair or fullD3candidate exists. A futurefeasible y/z can have atmost256 localdonor assignments; onecanonicalfailure cannot rejecttheothers. No globalrecord,newgraph,parameter,Lean ormethodclaim.

**启发与重启依据：** Capacity was not scarce: ignoring cross-class overlap leaves every starpair unexcluded, while the first argmax stillmisses29. Exact integer projection removes locally reconstructible donor assignments without merging actualstarP Dcolumns or promising speedup. The new18secondwindow yielded noincumbent,notinfeasibility. Stop this source/FP-cover line; no thirdsolve,seed,morecuts,canonical-donor extrapolation or unexecutedrepairstage failure claims.

**单独的重启条件：** STOP current650FP-cover chain. No thirdsolve/seed or automaticdonor/15pairing/BFS. A future separatelyauthorized genuinelynewstructuralquestion must retain both UNKNOWN solver histories and exactscope.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

