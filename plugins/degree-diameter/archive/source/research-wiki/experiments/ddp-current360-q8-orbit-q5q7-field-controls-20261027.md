---
type: experiment
node_id: exp:ddp-current360-q8-orbit-q5q7-field-controls-20261027
title: "Current360 Q8torsor fieldcontrols:q5formal20<25;q7actualD13andallfaithfulrepresentationprojection<=37<49"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/REPORT.md; research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/PREDICTION.json; research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/PRE_GRAPH_GATE_UPDATE.json; research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/RECIPE.json; research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/INPUT.txt; research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/RESULT.json; research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/NATIVE_RESULT.json; research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/FIRST_BAD_ROOT_Q7.json; research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/CONTROL_CAPACITY_ROOT.json; research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/UNIVERSAL_ENDPOINT_PREDICTION_ROOT.json; research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/UNIVERSAL_ENDPOINT_RESULT_ROOT.json; research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/analyze_universal.py; research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/probe.cpp; research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/run.py; research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/native.log; research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/terminal.json; research/ddp/more_graphs_20261027/d3_D8_current360_Q8_source/AUTHOR_README.md; research/ddp/more_graphs_20261027/d3_D8_current360_Q8_source/AUTHOR_construction.json; research/ddp/more_graphs_20261027/d3_D8_current360_Q8_source/AUTHOR_verification.txt; research/ddp/more_graphs_20261027/d3_D8_current360_Q8_source/representation_analysis/TARGET_CONTROLS.json; research/ddp/more_graphs_20261027/d3_D8_current360_source/ANALYSIS_Q8_ORBIT_LIFT.md; research/ddp/more_graphs_20261027/d3_D8_current360_source/ANALYSIS_Q8_ORBIT_LIFT.json; research/ddp/more_graphs_20261027/d3_D8_current360_source/universal_module_analysis/RESULT.json; research/ddp/more_graphs_20261027/d3_D8_current360_source/ANALYSIS_UNIVERSAL_MODULE_SCOPE.md; research/ddp/more_graphs_20261027/d3_D8_current360_source/ANALYSIS_UNIVERSAL_MODULE_SCOPE.json; research/ddp/more_graphs_20261027/d3_D8_current360_source/universal_module_analysis/PREDICTION.json; research/ddp/more_graphs_20261027/d3_D8_current360_source/universal_module_analysis/check_q7_evaluations.py"
added: 2026-10-27T23:18:18Z
tags: ["ddp", "method-ledger"]
---

# Current360 Q8torsor fieldcontrols:q5formal20<25;q7actualD13andallfaithfulrepresentationprojection<=37<49

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** multi-target-finite-control-experiment-with-structural-exclusions

**目标与阶数：** (3,?)；L=不适用／见变体

**距目标的证据：** q5target3D9hyp1000:rawmin29passes,butstrict20formalendpointbound<25excludesallfaithfulactions/basepointsinfixedmodel,0graph/BFS. q7target3D10actual1960/2940simpleconnectedcubic:5orbitrootsecc13,13,12,13,13giveglobalD13;rootR10miss387,391,373,385,387. Subsequentall8faithfulF7normalizedactionsimages36,34,34,34,36,36,37,34max37<49closefixedmodel. 0newLB;ordinarybadpairsunmeasured.

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 360,
  "source_reported_D": 8,
  "source_group": "F3^2semidirectQ8",
  "source_BFS": 0,
  "mechanism_count": 1,
  "fixed_controls": 2,
  "q5": {
    "name": "q5",
    "target_Delta": 3,
    "target_D": 9,
    "savedL": 600,
    "n": {
      "actual": null,
      "hypothetical": 1000
    },
    "actual_D": null,
    "actual_graphs": 0,
    "BFS": 0,
    "result": "Strictformal20<25rejectionbeforegraph;allfaithfulF5actionsandnonzero torsorbasepoints inthisfixedrule."
  },
  "q7": {
    "name": "q7",
    "target_Delta": 3,
    "target_D": 10,
    "savedL": 1250,
    "n": {
      "actual": 1960,
      "hypothetical": null
    },
    "actual_D": 13,
    "actual_graphs": 1,
    "BFS": 5,
    "result": "Solefrozenq7graphactualD13;subsequentcachedalleight-actionmax37<49extendsfixedruleexclusion."
  },
  "raw_minima": {
    "D9": 29,
    "D10": 66
  },
  "producer_capacity_reenumerations": 0,
  "q5_critical_raw_formal_required": [
    29,
    20,
    25
  ],
  "q7_critical_raw_formal_required": [
    66,
    53,
    49
  ],
  "q7_individual_order4_split": false,
  "fullQ8_absolutely_irreducible_bothfields": true,
  "q7_firstbad_normal_orbit_counts": [
    0,
    15,
    97,
    130,
    18,
    62,
    65
  ],
  "q7_firstbad_controller_counts": [
    12,
    7,
    12,
    7,
    19,
    7,
    12,
    7,
    15,
    9,
    12,
    5,
    14,
    6,
    13,
    7,
    12,
    9,
    7,
    8,
    13,
    9,
    7,
    7,
    13,
    6,
    12,
    5,
    17,
    6,
    10,
    8,
    14,
    5,
    10,
    7,
    18,
    5,
    10,
    5
  ],
  "q7_nonzero_normal_orbits": 6,
  "q7_firstbad_missing": 387,
  "q7_firstbad_first_target": 9,
  "q7_root_eccentricities": [
    13,
    13,
    12,
    13,
    13
  ],
  "q7_root_R10_missing": [
    387,
    391,
    373,
    385,
    387
  ],
  "q7_allfaithful_representation_images": [
    36,
    34,
    34,
    34,
    36,
    36,
    37,
    34
  ],
  "q7_subsequent_maximage": 37,
  "q7_universal_analysis_additional_words": 0,
  "q7_universal_analysis_additional_graphs": 0,
  "q7_universal_analysis_additional_BFS": 0,
  "actual_graphs_total": 1,
  "actual_BFS_roots_total": 5,
  "native_CPU_seconds": 0.000736,
  "native_process_CPU_seconds": 0.002594999999999903,
  "compile_CPU_seconds": 0.970824,
  "producer_total_parent_children_CPU_seconds": 0.973612,
  "inherited_rawcapacity_CPU_seconds": 0.0023931709999999995,
  "inherited_formalcount_CPU_seconds": 0.005538226,
  "subsequent_representation_analysis_CPU_seconds": 0.0007156229999999986,
  "ordinary_bad_pair_count_scope": "Null;reportedcomplementsareindividualrootstates",
  "prediction": "REFUTED_FOR_BOTH_FIXED_TARGETS",
  "UNKNOWN": 0,
  "new_lower_bounds": 0,
  "whole_fixed_model_scope_proof": "ANALYSIS_UNIVERSAL_MODULE_SCOPE.md/json;allfaithfulQ8actions/nonzerobasepoints,notgeneralcubicgraphs"
}
```



**从属变体：**
```json
[
  {
    "name": "q5",
    "target_Delta": 3,
    "target_D": 9,
    "savedL": 600,
    "n": {
      "actual": null,
      "hypothetical": 1000
    },
    "actual_D": null,
    "actual_graphs": 0,
    "BFS": 0,
    "result": "Strictformal20<25rejectionbeforegraph;allfaithfulF5actionsandnonzero torsorbasepoints inthisfixedrule."
  },
  {
    "name": "q7",
    "target_Delta": 3,
    "target_D": 10,
    "savedL": 1250,
    "n": {
      "actual": 1960,
      "hypothetical": null
    },
    "actual_D": 13,
    "actual_graphs": 1,
    "BFS": 5,
    "result": "Solefrozenq7graphactualD13;subsequentcachedalleight-actionmax37<49extendsfixedruleexclusion."
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/REPORT.md](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/REPORT.md)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/PREDICTION.json](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/PREDICTION.json)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/PRE_GRAPH_GATE_UPDATE.json](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/PRE_GRAPH_GATE_UPDATE.json)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/RECIPE.json](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/RECIPE.json)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/INPUT.txt](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/INPUT.txt)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/RESULT.json](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/RESULT.json)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/NATIVE_RESULT.json](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/NATIVE_RESULT.json)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/FIRST_BAD_ROOT_Q7.json](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/FIRST_BAD_ROOT_Q7.json)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/CONTROL_CAPACITY_ROOT.json](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/CONTROL_CAPACITY_ROOT.json)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/UNIVERSAL_ENDPOINT_PREDICTION_ROOT.json](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/UNIVERSAL_ENDPOINT_PREDICTION_ROOT.json)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/UNIVERSAL_ENDPOINT_RESULT_ROOT.json](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/UNIVERSAL_ENDPOINT_RESULT_ROOT.json)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/analyze_universal.py](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/analyze_universal.py)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/probe.cpp](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/probe.cpp)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/run.py](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/run.py)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/native.log](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/native.log)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/terminal.json](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/quaternion_orbit_field_controls/terminal.json)；[research/ddp/more_graphs_20261027/d3_D8_current360_Q8_source/AUTHOR_README.md](../../research/ddp/more_graphs_20261027/d3_D8_current360_Q8_source/AUTHOR_README.md)；[research/ddp/more_graphs_20261027/d3_D8_current360_Q8_source/AUTHOR_construction.json](../../research/ddp/more_graphs_20261027/d3_D8_current360_Q8_source/AUTHOR_construction.json)；[research/ddp/more_graphs_20261027/d3_D8_current360_Q8_source/AUTHOR_verification.txt](../../research/ddp/more_graphs_20261027/d3_D8_current360_Q8_source/AUTHOR_verification.txt)；[research/ddp/more_graphs_20261027/d3_D8_current360_Q8_source/representation_analysis/TARGET_CONTROLS.json](../../research/ddp/more_graphs_20261027/d3_D8_current360_Q8_source/representation_analysis/TARGET_CONTROLS.json)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/ANALYSIS_Q8_ORBIT_LIFT.md](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/ANALYSIS_Q8_ORBIT_LIFT.md)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/ANALYSIS_Q8_ORBIT_LIFT.json](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/ANALYSIS_Q8_ORBIT_LIFT.json)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/universal_module_analysis/RESULT.json](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/universal_module_analysis/RESULT.json)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/ANALYSIS_UNIVERSAL_MODULE_SCOPE.md](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/ANALYSIS_UNIVERSAL_MODULE_SCOPE.md)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/ANALYSIS_UNIVERSAL_MODULE_SCOPE.json](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/ANALYSIS_UNIVERSAL_MODULE_SCOPE.json)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/universal_module_analysis/PREDICTION.json](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/universal_module_analysis/PREDICTION.json)；[research/ddp/more_graphs_20261027/d3_D8_current360_source/universal_module_analysis/check_q7_evaluations.py](../../research/ddp/more_graphs_20261027/d3_D8_current360_source/universal_module_analysis/check_q7_evaluations.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** OneQ8-orbit-moduletransfermechanismwithtwofrozencontrols. Actual360fivebaseK2,3sourceoverF3^2semidirectQ8;equivarianttorsormapsetsq5/q7translationsandfaithfulactions. Parent40-controllerrawcacheinherited,norepeat. q5formal20<25receivedbeforegraphs,rejectwithoutgraph. q7actualonlyone1960graphandall5deckorbitBFS. Subsequentexpert53formalcoefficientsevaluatedatall8canonicalF7actions,noextrawords/graphs/BFS.

**仍未完成：** Otherbasegraphs,voltagevectorsnotgivenbythissourceQ8orbitmap,othermodule/representationfamilies,andgeneralN(3,9)/N(3,10) arenotexcluded. q5actualDnullbecausegraphnotgenerated. AggregateactualDnullbecausevariantsdiffer;actualq7D13isinvariants,notamulti-targetsharedvalue.

**启发与重启依据：** Rawroutecapacityanduniversalformalcountsarenecessaryonly. Q8-equivariancepreservesaction/negationbutnotaddition;newnormalorbitscanremainuncoveredaftercorrectrepresentationtransfer. Split/nonsplitindividualeigenlinesalonearenotcoverageevidence. Fixedq5/q7orbit-voltagemodelclosed;nonewfields/matrices/vectors/bases/seedsfrommissingstatecounts.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

