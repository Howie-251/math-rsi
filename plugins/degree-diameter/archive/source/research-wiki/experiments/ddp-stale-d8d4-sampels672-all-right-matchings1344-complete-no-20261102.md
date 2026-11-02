---
type: experiment
node_id: exp:ddp-stale-d8d4-sampels672-all-right-matchings1344-complete-no-20261102
title: "8D4两份published Sampels672全672右平移匹配NO：六phase各最多106/112，单层已不足"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-02"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/ROOT_DISPOSITION.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/READ_GATE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/READ_GATE.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/PAPER_INTERFACE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/run_once.py; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/SOURCE_BINDING.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/SOURCE_GRAPH_CANONICAL.edges; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/ALL_T_RESULTS.tsv; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/ATTEMPT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/PHASE_COMPATIBILITY_DIAGNOSTIC_PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/diagnose_saved_phase_compatibility.py; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/PHASE_COMPATIBILITY_DIAGNOSTIC.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/PHASE_COMPATIBILITY_DIAGNOSTIC_NOTE.md"
added: 2026-11-02T00:46:43Z
tags: ["ddp", "method-ledger"]
---

# 8D4两份published Sampels672全672右平移匹配NO：六phase各最多106/112，单层已不足

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (8,4)；L=1100；条件性n=1344（未据此计纪录）

**距目标的证据：** Published672/2352simple7regularsourceidentityclosedR4=672isoneknownsourcereproduction,notnewgraphresult. All672actualrightmatchingU_tcrosssetsfailD4;no1344candidateorordinarycandidateBFS/fresh/Lean/ARIS.；新published RIGHT源canonical672/2352/degree7，identity闭R4=672仅复现。精确跨层endpoint集合U_t=union_(a+b<=3)S^a*t*S^b；≤4的三cross可消matching回退，源同步leftH作用使identity根完整。全部672t完整，0个U_t=H、0个1344候选。保存行诊断事前预测“六phase分别可满112但共享t有pair冲突”，实测六phase各最大106/112、各0局部满，预测被反驳；障碍已经是单层实际端点覆盖不足，不只是相容性冲突。原batch/保存行诊断/root处置累计1.645124787/10CPU，0新图/参数/Lean/candidateBFS/ARIS。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_parameter_pairs": 0,
  "new_Lean_instances": 0,
  "new_independent_method_claims": 0,
  "source_reproductions": 1,
  "source_reproduction_not_new_result": true,
  "source": {
    "group": "C6_RIGHT_semidirect39_Z112",
    "law": "(a,b)(c,d)=(a+c mod6,b*39^c+d mod112)",
    "canonical_labels": "112*a+b; not claimed to be author raw labels",
    "S7": [
      [
        2,
        73
      ],
      [
        4,
        23
      ],
      [
        5,
        54
      ],
      [
        1,
        22
      ],
      [
        5,
        71
      ],
      [
        1,
        31
      ],
      [
        3,
        42
      ]
    ],
    "n": 672,
    "m": 2352,
    "degree": 7,
    "identity_closed_ball_counts": [
      1,
      8,
      50,
      283,
      672
    ],
    "exact_word_endpoint_counts": [
      1,
      7,
      43,
      240,
      649
    ],
    "identity_R4": 672
  },
  "rightmatching_domain": {
    "full_domain": 672,
    "checked": 672,
    "exact_crossfull_hits": 0,
    "mapping": "M_t(h)=h*t",
    "all_leftH_equivariant_matchings": true,
    "t_involution_or_source_Aut_required": false,
    "actual_new1344_candidates": 0
  },
  "saved_phase_diagnostic": {
    "savedrows": 672,
    "phase_size": 112,
    "maxima": [
      106,
      106,
      106,
      106,
      106,
      106
    ],
    "full112_t_counts": [
      0,
      0,
      0,
      0,
      0,
      0
    ],
    "argmax_t": [
      137,
      475,
      161,
      145,
      609,
      261
    ],
    "phase_normalization": "relativephase=(targetabsolutephase-t.phase)mod6; relative[j]=savedcounts[(t.phase+j)mod6]",
    "preregistered_prediction": "all6phasescanindividuallyfill112butaminimallyincompatiblepair exists",
    "prediction_supported": false,
    "minimum_incompatible_cardinality": 1,
    "single_layer_failure_not_just_shared_parameter_conflict": true,
    "no_new_Ut_source_or_BFS_queries": true
  },
  "original_native_CPU": 0.278501838,
  "original_stage_CPU": 1.478501838,
  "saved_diagnostic_CPU": 0.016622949,
  "diagnostic_stage_CPU": 1.545124787,
  "root_disposition_charge": 0.1,
  "final_case_CPU": 1.645124787,
  "case_CPU_cap": 10,
  "all_processes_terminal": true,
  "candidate_BFS_fresh_Lean_ARIS": 0,
  "old684_K19_source_DP_reruns": 0,
  "no_automatic_otherS_t_action_window": true,
  "same_Goal": "ACTIVE",
  "old_N8_n61": "PAUSED",
  "negative_Lean_required": false
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/ROOT_DISPOSITION.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/ROOT_DISPOSITION.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/READ_GATE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/READ_GATE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/READ_GATE.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/READ_GATE.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/PAPER_INTERFACE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/PAPER_INTERFACE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/run_once.py](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/run_once.py)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/SOURCE_BINDING.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/SOURCE_BINDING.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/SOURCE_GRAPH_CANONICAL.edges](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/SOURCE_GRAPH_CANONICAL.edges)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/ALL_T_RESULTS.tsv](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/ALL_T_RESULTS.tsv)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/ATTEMPT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/ATTEMPT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/PHASE_COMPATIBILITY_DIAGNOSTIC_PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/PHASE_COMPATIBILITY_DIAGNOSTIC_PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/diagnose_saved_phase_compatibility.py](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/diagnose_saved_phase_compatibility.py)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/PHASE_COMPATIBILITY_DIAGNOSTIC.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/PHASE_COMPATIBILITY_DIAGNOSTIC.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/PHASE_COMPATIBILITY_DIAGNOSTIC_NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/PHASE_COMPATIBILITY_DIAGNOSTIC_NOTE.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** FixedpublishedSampels672CayleysourcewithactualRIGHTlaw(a,b)(c,d)=(a+c mod6,b*39^c+d mod112),canonical112a+b(notauthorrawlabels),thefixedinverse-closedS7. Preservealloldedgesoftwocopies;matchingM_t(h)=h*t,allt∈H672. Theseareexactlyallleft-H-equivariantbijectionsforone-regular-orbitCayleysource;donotrequiretselfinverseorsourceR_tAut. All672completedNO. Savedphaseanalysisusesonlysame672storedrows,notnewparameters. Notarbitrarypointmatching,oldedgeedits/otherS/host/general8D4;notold684H342orK19domain.

**正向保证：** ActualsourceusespublishedRIGHTlawandfixedS7,notold684laworleftmultiplicationconvention. SourceidentityclosedR4=672isrecordedseparatelyasreproduction,withnonewgraphcount.；U_t=union S^a*t*S^bfor a+b<=3recordsactualendpointsandall≤4crossroutes,notwalkcapacityorjustrightshiftprism. SynchronousleftHactsonthejoinedgraph,soidentitycrossrootcoversallrootswithinthisequivariantfamily.；Full672rightt-domainwascompletedoncewithallper-tcrosscoverage/firstmissingdataretained. tneednotbeaninvolutionorgraphautomorphism;reverseusesrightt^-1.；Phasepostprocessonlynormalizesstoredabsolutephasetorelative(targetphase-t.phase)mod6. Allsixmaxima106andzero112witnessesrefutethepreviousindividually-full/pair-incompatibleprediction.；OriginalRESULT/TERMINALphaseCPUvaluesremainhistorical;ROOTdisposition1.645124787includesdiagnosticandrootreadchargewithoutreset.

**仍未完成：** Arbitrarynon-equivariantmatching,oldedgechanges,otherS/host/helperrulesandgeneral8D4remainunexcluded. No1344graphwasgenerated/accepted/formalized. Relativephaseargmaxonlywitnesses106not112;nofullphasewitnessexistsinthisfinitefamily. Sourcecanonicallabelsareexplicitlynewrecipecoordinates,notauthorrawbinding. GoalACTIVE/oldN8n61PAUSED;9D4readonlygateisnotthisnode.

**启发与重启依据：** STOPthisSampels672fixedS/allrighttranslationmatchingrule. Thephasepredictionwasrefutedratherthanrelabelledaspartialsuccess:eachindividualrelativephasealreadyfailsforall672t. No justificationforanotherparameterwindoworshared-tpaircompatibilitysearchwithsameS. SourceidentityR4reproductionandlocalphaseargmaxwitnessesarenotnewconstructionresults.

**单独的重启条件：** Onlya newlyauthorizedboundedquestionwithmeaningfullychangedsource/generator/edge/matchingrule;noautomaticothert/solver/window/S/action/source. Noold684K19timerresumed.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

