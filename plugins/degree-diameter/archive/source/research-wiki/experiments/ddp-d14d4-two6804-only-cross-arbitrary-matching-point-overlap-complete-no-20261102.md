---
type: experiment
node_id: exp:ddp-d14d4-two6804-only-cross-arbitrary-matching-point-overlap-complete-no-20261102
title: "14D4两份6804只加跨副本matching：相位容量到实际点球，任意全/部分matching均NO"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-02"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/ROOT_DISPOSITION.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/NOTE.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/FINAL_MATCHING_DISPOSITION_NOTE.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/POINT_BALL_OVERLAP_PAPER.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/CONSTANT_PHASE_PRED.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/CONSTANT_PHASE_PAPER.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/CONSTANT_PHASE_RESULT.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/PHASE_PERMUTATION_PRED.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/PHASE_PERMUTATION_CAPACITY_PAPER.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/PHASE_PERMUTATION_SCOPE_ATTACK.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/run_phase_permutation_once.py; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/PHASE_CAPACITY_MODEL.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/PHASE_CAPACITY_RESULT.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/PHASE_CAPACITY_TERMINAL.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/ORDINARY_PI_NB_CHECK.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/NONBACKTRACKING_PRED.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/NONBACKTRACKING_CAPACITY_PAPER.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/run_phase_nb_once.py; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/NB_PHASE_CAPACITY_MODEL.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/NB_PHASE_CAPACITY_RESULT.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/NB_PHASE_CAPACITY_TERMINAL.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/NB_PHASE_SOLVER_STDOUT.log; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/OVERLAP_PRED.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/overlap_gate.cpp; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/OVERLAP_RESULT.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/OVERLAP_CHILD_RESULT.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/OVERLAP_SHELL_PROFILES.tsv; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/OVERLAP_ROOT_RESULTS.tsv; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/FIRST81_OVERLAP_RESULT.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/FIRST81_OVERLAP_SHELL_PROFILES.tsv; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/FIRST81_OVERLAP_ROOT_RESULTS.tsv; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/INITIAL_FORMAT_FAILURE_OVERLAP_RESULT.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/INITIAL_FORMAT_FAILURE_overlap_gate.cpp"
added: 2026-11-02T00:12:23Z
tags: ["ddp", "method-ledger"]
---

# 14D4两份6804只加跨副本matching：相位容量到实际点球，任意全/部分matching均NO

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** fixed_twocopy_crossmatching_route_capacity_and_point_overlap_experiment

**目标与阶数：** (14,4)；L=9720；条件性n=13608（未据此计纪录）

**距目标的证据：** No13608graphwasgenerated/accepted. CompleteproofexcludesD<=4foronly-cross arbitraryperfectmatching(andpartialmatchingbycompletion)ontwoexact6804sourcecopies. Existing13regularsourceD4isnotneededforthisnegativeproof; sourceD4validityBFS0.；恒定phaseoffset族328<567先严格NO；改任意12phase排列，普通walk容量实际min573仅necessaryfeasible。其同π扣nonbacktracking折返后min547<567，被反驳；唯一新NB模型8秒4112nodes无incumbent，UNKNOWN而非INFEASIBLE。于是改查actualpoint球重复覆盖，旧uniform6860前提被literal反驳：全部6804新R2/R3 maxima B2=154/S2=140/B3=1588/S3=1434，安全未扣重U=6984。只取y0，对6803个z!=0交集13最小项各20/总260；任意M取u=M^-1(0)，跨copyR4覆盖<=6984-260=6724<6804，至少80漏点，整任意pointmatching族严格NO。无Aut/相位/源D4假设，partialmatching可补全亦NO。13.170781895/15CPU含格式失败和81→全6804扩域，0新图/参数/Lean。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_parameter_pairs": 0,
  "new_Lean_instances": 0,
  "new_independent_method_claims": 0,
  "single_record_for_four_adaptive_stages": true,
  "source_node": "ddp-d13-d4-current6804-source-20261027",
  "source_n": 6804,
  "source_m": 44226,
  "source_degree": 13,
  "target_hypothetical_n": 13608,
  "sourceD4_needed_for_negative_proof": false,
  "constantphase": {
    "verdict": "STRICT_NO_FIXED_PHASE_OFFSET_ALL_FIBRE_BIJECTIONS",
    "capacity_upper": 328,
    "phase_targets": 567,
    "deficit": 239
  },
  "ordinary_phase_pi": {
    "status": "FEASIBLE_NECESSARY_CAPACITY_ONLY",
    "permutation": [
      0,
      6,
      8,
      11,
      10,
      1,
      3,
      9,
      7,
      4,
      5,
      2
    ],
    "minimum": 573,
    "pointgraph_generated": false
  },
  "ordinary_pi_NB_check": {
    "status": "REFUTED_SAME_ORDINARY_PI",
    "minimum": 547,
    "needed": 567,
    "failedslots": 8
  },
  "NB_model": {
    "rawstatus": "UNKNOWN_TIME_LIMIT_NOT_INFEASIBLE",
    "configured_seconds": 8,
    "nodes": 4112,
    "incumbent": null,
    "model_feasibility_verdict_unchanged": true,
    "stopped_after_stronger_pointfamily_NO": true
  },
  "old_uniform_profile_claim": {
    "profile": [
      1,
      13,
      138,
      1400,
      5252
    ],
    "scope": "root0only_notuniform",
    "actual_literal_refuted": true,
    "old_raw_upper6860_not_used": true,
    "first81_then_all6804_corrective_extension_preserved": true
  },
  "actual_point_overlap": {
    "new_query_roots_R2_R3": 6804,
    "B2max": 154,
    "S2max": 140,
    "B3max": 1588,
    "S3max": 1434,
    "B1": 14,
    "raw_union_upper": 6984,
    "threshold_for_one_witness": 181,
    "y_witness": 0,
    "actual_z_checked": 6803,
    "thirteen_smallest_intersections": [
      20,
      20,
      20,
      20,
      20,
      20,
      20,
      20,
      20,
      20,
      20,
      20,
      20
    ],
    "thirteen_distinct_centres": [
      1142,
      1171,
      1708,
      1709,
      1710,
      1711,
      1722,
      1724,
      1731,
      1732,
      1743,
      1745,
      1747
    ],
    "mandatory_overlap": 260,
    "cross_R4_cover_upper": 6724,
    "target_count": 6804,
    "missing_targets_at_Minverse0_atleast": 80,
    "all_y_Lmin_claimed": false,
    "source_Aut_phase_affine_D4_assumptions_needed": false,
    "partial_crossmatching_corollary": true
  },
  "proof_query_vs_validation": {
    "new_coverage_R1_R2_R3_support": true,
    "sourceD4validationBFS": 0,
    "field_Lean_ARIS": 0,
    "final_literal_parse_count": 1,
    "format_failure_preserved": true,
    "first81_support_preserved": true
  },
  "cumulative_line_CPU": 13.170781895,
  "line_CPU_cap": 15,
  "all_processes_terminal": true,
  "no_timer_reset": true,
  "negative_Lean_required": false,
  "negative_Lean_run": false,
  "whole_only_cross_matching_line_stopped": true,
  "same_Goal": "ACTIVE",
  "old_N8_n61": "PAUSED"
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/ROOT_DISPOSITION.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/ROOT_DISPOSITION.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/NOTE.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/NOTE.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/FINAL_MATCHING_DISPOSITION_NOTE.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/FINAL_MATCHING_DISPOSITION_NOTE.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/POINT_BALL_OVERLAP_PAPER.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/POINT_BALL_OVERLAP_PAPER.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/CONSTANT_PHASE_PRED.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/CONSTANT_PHASE_PRED.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/CONSTANT_PHASE_PAPER.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/CONSTANT_PHASE_PAPER.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/CONSTANT_PHASE_RESULT.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/CONSTANT_PHASE_RESULT.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/PHASE_PERMUTATION_PRED.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/PHASE_PERMUTATION_PRED.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/PHASE_PERMUTATION_CAPACITY_PAPER.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/PHASE_PERMUTATION_CAPACITY_PAPER.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/PHASE_PERMUTATION_SCOPE_ATTACK.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/PHASE_PERMUTATION_SCOPE_ATTACK.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/run_phase_permutation_once.py](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/run_phase_permutation_once.py)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/PHASE_CAPACITY_MODEL.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/PHASE_CAPACITY_MODEL.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/PHASE_CAPACITY_RESULT.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/PHASE_CAPACITY_RESULT.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/PHASE_CAPACITY_TERMINAL.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/PHASE_CAPACITY_TERMINAL.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/ORDINARY_PI_NB_CHECK.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/ORDINARY_PI_NB_CHECK.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/NONBACKTRACKING_PRED.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/NONBACKTRACKING_PRED.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/NONBACKTRACKING_CAPACITY_PAPER.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/NONBACKTRACKING_CAPACITY_PAPER.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/run_phase_nb_once.py](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/run_phase_nb_once.py)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/NB_PHASE_CAPACITY_MODEL.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/NB_PHASE_CAPACITY_MODEL.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/NB_PHASE_CAPACITY_RESULT.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/NB_PHASE_CAPACITY_RESULT.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/NB_PHASE_CAPACITY_TERMINAL.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/NB_PHASE_CAPACITY_TERMINAL.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/NB_PHASE_SOLVER_STDOUT.log](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/NB_PHASE_SOLVER_STDOUT.log)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/OVERLAP_PRED.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/OVERLAP_PRED.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/overlap_gate.cpp](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/overlap_gate.cpp)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/OVERLAP_RESULT.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/OVERLAP_RESULT.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/OVERLAP_CHILD_RESULT.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/OVERLAP_CHILD_RESULT.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/OVERLAP_SHELL_PROFILES.tsv](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/OVERLAP_SHELL_PROFILES.tsv)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/OVERLAP_ROOT_RESULTS.tsv](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/OVERLAP_ROOT_RESULTS.tsv)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/FIRST81_OVERLAP_RESULT.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/FIRST81_OVERLAP_RESULT.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/FIRST81_OVERLAP_SHELL_PROFILES.tsv](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/FIRST81_OVERLAP_SHELL_PROFILES.tsv)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/FIRST81_OVERLAP_ROOT_RESULTS.tsv](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/FIRST81_OVERLAP_ROOT_RESULTS.tsv)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/INITIAL_FORMAT_FAILURE_OVERLAP_RESULT.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/INITIAL_FORMAT_FAILURE_OVERLAP_RESULT.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/INITIAL_FORMAT_FAILURE_overlap_gate.cpp](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/INITIAL_FORMAT_FAILURE_overlap_gate.cpp)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Two copies of actualsimple13regular6804/44226 literal; preservealloldedgesandaddonlycrossedgeswithcrossdegree<=1. Anyfullpoint-perfectmatchingM, no phase/fibre/affine/group/Aut restriction; partialcrossmatchingsalsoNObymonotonecompletiononequalcopies. Excludesonlythishost/rule,notgeneral14D4,otherhosts,oldoldcopy-internaladditions,oldedgerewiring,multi-crossdegreeorhelpervertices. Constantphase/ordinarypi/NB/pointoverlapareoneproblemrecord,notfourmethods.

**正向保证：** For<=4crosscopywalks,3crossesforceamatchingbacktrack,soone-cross exactunion is union_a0..3 union_xinSa(u) B_(3-a)(M(x)); shortest-prefixshellsensureallallowedroutesincluded.；All6804actualclosedR2/R3shellprofiles provide globalmaxima154/140/1588/1434; formeruniformroot0profile and6860 predictionarefalseassumptionsnotusedinthefinalproof.；Forfixedy0,13imagesofN(M^-1(0))are13distinctactualcentresdifferentfrom0. TheirB3(0)/B2(z)intersectionssumatleastthe13smallest260, safelydeductedwithoutovercountingA0.；SurjectivitysuppliesrootM^-1(0)forallM; one y0witness suffices, notall-yLmin. No sourceAut/phase/affine matchingor inheritedsourceD4assumption.；Partialonly-crossmatchingcanbecompletedtoperfectmatchingbetweenunusedvertices; additioncannotincreasedistances,soD4partialwouldcontradictfullNO. Doesnotallowadditionalcopy-internaloldoldedges.

**仍未完成：** General14D4andother13608constructionsremainunexcluded. NBphasecapacitymodelitselfremainsUNKNOWNnotINFEASIBLE; strongerpointgraphNOdoesnotchangethatsolverreturn. One y suffices; all-yLminnotmeasured. No13608graphacceptance,formalgraphwitnessornewglobalrecord. New3645readinheritsoldNOand8D4K19readpreparationarenotnewexperimentnodeshere.

**启发与重启依据：** STOPthis two6804 retained-oldedges only-crossmatching mechanism. Ordinarywalkcapacitysuccessdidnotbecomepointcoverage; exactNBrefutedtheordinarywitness, thenfiniteactualballoverlapclosedallpointmatchingsbeyondphaseconstraints. Uniformroot0profilewasrefutedratherthanforcedontoallroots; actualmaximaandonepreimagewitnessremovedAut/uniform assumptions. Noadditionalphase/fibre/permutation/NBsolver/copy/degreewindow. KeepNBnecessary-modelUNKNOWNdistinctfromstrongeractualgraph-familyNO.

**单独的重启条件：** Onlyanewboundedstructuralquestionthatchangeshost,allowableoldoldedges/rewiring,crossdegreeorhelperrules; do not resume theclosedonly-crosspointmatching line or oldNBtimer.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

