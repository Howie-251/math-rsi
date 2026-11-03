---
type: experiment
node_id: exp:ddp-gq8-canonical-circlepole-c3-3705-20261027
title: "GQ8 canonicalcircle-pole C3 graph3705:oppositelinephases2/3/4 but actualD5"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/REPORT.md; research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/PREDICTION.json; research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/PRE_RUN_DERIVATION.json; research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/PAPER_PRECHECK_ROOT.md; research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/FIELD_PREFLIGHT.json; research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/RECIPE.json; research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/GEOMETRY.json; research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/PHASE_PREFLIGHT.json; research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/FIRST_FAILURE.json; research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/RESULT.json; research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/NATIVE_RESULT.json; research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/probe.cpp; research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/run.py; research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/native.log; research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/terminal.json; research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/CIRCLE_POLE_THEORY_REPORT.md; research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/CIRCLE_POLE_THEORY_FIELDS.json; research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/ANALYSIS_PROOF.md"
added: 2026-10-27T23:07:09Z
tags: ["ddp", "method-ledger"]
---

# GQ8 canonicalcircle-pole C3 graph3705:oppositelinephases2/3/4 but actualD5

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (11,4)；L=3645；candidate_graph_or_family n=3705

**距目标的证据：** 实际D=5，目标D=4；Specifiedfieldvalid. OppositeS0/Sinfinity pure4phasehist2/3/4,sooriginal3/3/3predictionrefuted andparentpaperrefinementreceivedbeforeanyphase numeric supported. Actual3705/19500/simple/undirected,max11,1755degree10/1950degree11. Root0R4missing19allpointvertices,first220=(point73,sheet1). Universalupper5 pluscounterexamplegivesexactD5;noordinaryglobalbadpairs/newLB.

**其他指标（保持原计数类型）：**
```json
{
  "actual_n": 3705,
  "actual_m": 19500,
  "degree_histogram": {
    "10": 1755,
    "11": 1950
  },
  "geometry_points": 585,
  "geometry_lines": 585,
  "spread_lines": 65,
  "field_polynomial_binary": 67,
  "field_j": 2,
  "F8": [
    0,
    1,
    14,
    15,
    22,
    23,
    24,
    25
  ],
  "phase_pure_geodesics": 9,
  "phase_histogram": [
    2,
    3,
    4
  ],
  "original_balanced_prediction": "REFUTED",
  "pre_numeric_refined_prediction": "SUPPORTED",
  "wholegraph_D4_prediction": "REFUTED",
  "actual_graphs": 1,
  "actual_root_R4_BFS": 1,
  "first_failed_root": 0,
  "first_missing_target": 220,
  "first_root_R4_missing_states": 19,
  "first_root_missing_types": {
    "point": 19
  },
  "failed_root_layers": [
    1,
    10,
    92,
    786,
    2797
  ],
  "global_D5_evidence": "Firstactualrootcounterexampleplusuniversalupper5,nofullallpairssurvey",
  "ordinary_bad_pair_count_scope": "Notmeasured;19isone-rootR4statecomplement",
  "native_CPU_seconds": 0.007247,
  "compile_CPU_seconds": 1.3844690000000002,
  "total_parent_children_CPU_seconds": 1.394181,
  "phase_checkpoint_CPU_seconds": 0.006031,
  "source_all_roots_BFS_repeated": 0,
  "other_rules_tested": 0,
  "cached_pencil_repair_diagnostic": "Points73=(1,0),137=(3,0),3notinF8;nosingleqonSinfinitycollinearwithboth",
  "cached_diagnostic_newgraphs": 0,
  "cached_diagnostic_newBFS": 0,
  "UNKNOWN": 0,
  "new_lower_bounds": 0,
  "expert_paper_and_cached_analysis": {
    "analysis_kind": "paper-check-and-cached-coordinate-obstruction",
    "same_candidate_row_only": true,
    "pole_rule_valid": true,
    "determinants_nonzero": true,
    "chi_K_projective_well_defined": true,
    "per_nonspread_line_flag_histogram": [
      3,
      3,
      3
    ],
    "per_line_flag_balance_scope": "not a four-step route coverage certificate",
    "standard_spread_pair_paper_histogram": [
      2,
      3,
      4
    ],
    "reverse_orientation_histogram": [
      2,
      4,
      3
    ],
    "original_333_prediction": "REFUTED; root revision frozen before receiving phase numeric results; candidate unchanged",
    "global_coboundary_collapse": "excluded by the three distinct phases for S0 to Sinfinity; does not prove D4",
    "cached_same_pencil_single_partner_obstruction": {
      "source_point_id": 0,
      "source_coordinates": [
        0,
        2
      ],
      "target_points": [
        {
          "point_id": 73,
          "coordinates": [
            1,
            0
          ],
          "actual_missing_vertex": 220,
          "sheet": 1
        },
        {
          "point_id": 137,
          "coordinates": [
            3,
            0
          ],
          "actual_missing_vertex": 413,
          "sheet": 2
        }
      ],
      "F8": [
        0,
        1,
        14,
        15,
        22,
        23,
        24,
        25
      ],
      "conditions": [
        "y in F8*",
        "3*y in F8*"
      ],
      "contradiction": "3=(3*y)/y would belong to F8, but cached encoding has 3 outside F8",
      "status": "REFUTED_FOR_THIS_SAME_PENCIL_SINGLE_PARTNER_ROUTE_RULE",
      "scope": "One source point, one same-spread-line partner, routes using one new point-matching edge, two incidence edges and one line-K3 edge. General joint matchings are not excluded."
    },
    "new_graphs": 0,
    "new_BFS": 0,
    "new_solver_runs": 0,
    "evidence_paths": [
      "PREDICTION.json",
      "PAPER_PRECHECK_ROOT.md",
      "GEOMETRY.json",
      "FIRST_FAILURE.json",
      "CIRCLE_POLE_THEORY_REPORT.md"
    ]
  }
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/REPORT.md](../../research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/REPORT.md)；[research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/PREDICTION.json](../../research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/PREDICTION.json)；[research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/PRE_RUN_DERIVATION.json](../../research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/PRE_RUN_DERIVATION.json)；[research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/PAPER_PRECHECK_ROOT.md](../../research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/PAPER_PRECHECK_ROOT.md)；[research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/FIELD_PREFLIGHT.json](../../research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/FIELD_PREFLIGHT.json)；[research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/RECIPE.json](../../research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/RECIPE.json)；[research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/GEOMETRY.json](../../research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/GEOMETRY.json)；[research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/PHASE_PREFLIGHT.json](../../research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/PHASE_PREFLIGHT.json)；[research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/FIRST_FAILURE.json](../../research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/FIRST_FAILURE.json)；[research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/RESULT.json](../../research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/RESULT.json)；[research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/NATIVE_RESULT.json](../../research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/NATIVE_RESULT.json)；[research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/probe.cpp](../../research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/probe.cpp)；[research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/run.py](../../research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/run.py)；[research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/native.log](../../research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/native.log)；[research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/terminal.json](../../research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/terminal.json)；[research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/CIRCLE_POLE_THEORY_REPORT.md](../../research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/CIRCLE_POLE_THEORY_REPORT.md)；[research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/CIRCLE_POLE_THEORY_FIELDS.json](../../research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/CIRCLE_POLE_THEORY_FIELDS.json)；[research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/ANALYSIS_PROOF.md](../../research/ddp/more_graphs_20261027/d11_D4_gq8_circle_pole_C3_3705/ANALYSIS_PROOF.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Exactlyonecanonicalq8geometry rule:fixedGF64 t6+t+1/j2,585points/585isotropiclines/65spreadlines,det-character C3voltagesfromline-dependent normcirclepoles,alllinefibresK3,spreadlinepointneighbor-twinswithK3;no pointmatching. Phasegatefirst,oneactualgraphafterall3colours,firstR4failure stops. Noadditionalpole/field/basis/phase/seed/graph.

**仍未完成：** Othercirclepolevoltagechoices,otherfields/bases,moregeneraljointmatchingmechanisms,andgeneralN(11,4) arenotexcluded. Noadditional graph generatedforcachedpencildiagnostic. All-root3705BFS notperformed afterfirstfailure.

**启发与重启依据：** Aline-pairthree-colourpencil necessarygate canpasswhileotherpointpairphasesfail. Theline-dependentcirclepoleisamateriallydifferentroute rulefromoldq7same-f/RREF+J, butthissolecanonicalruleisnotD4. Stop withoutchoosingnewpolebythe19misses. Cachedpoint73/137alsoexcludesthesinglecommon-collinear-intermediate pencilrepair;otherjointmatchingsremainopen.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

