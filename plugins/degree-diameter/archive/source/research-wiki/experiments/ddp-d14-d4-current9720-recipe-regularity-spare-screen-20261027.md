---
type: experiment
node_id: exp:ddp-d14-d4-current9720-recipe-regularity-spare-screen-20261027
title: "(14,4)9720源：唯一7plain边共hub失败，全部相邻单点split排除"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d14_D4_current9720_source/REPORT.md; research/ddp/more_graphs_20261027/d14_D4_current9720_source/PREDICTION.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/SOURCE.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/RESULT.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/PLAIN_PAIR_STRUCTURE.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/AUTHOR_README.md; research/ddp/more_graphs_20261027/d14_D4_current9720_source/construction.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/AUTHOR_VERIFICATION.txt; research/ddp/more_graphs_20261027/d14_D4_current9720_source/SOURCE_RECEIPTS.json; research/ddp/more_graphs_20261027/d14_D4_current9720_source/LEDGER_CHECK.json; research/ddp/refresh_20261029/d14_D4_seven_plain_hub/GATE_RESULT.json; research/ddp/refresh_20261029/d14_D4_seven_plain_hub/INPUT.txt; research/ddp/refresh_20261029/d14_D4_seven_plain_hub/MISSING_TARGETS.json; research/ddp/refresh_20261029/d14_D4_seven_plain_hub/PARAMETERS.json; research/ddp/refresh_20261029/d14_D4_seven_plain_hub/PREDICTION.md; research/ddp/refresh_20261029/d14_D4_seven_plain_hub/REPORT.md; research/ddp/refresh_20261029/d14_D4_seven_plain_hub/RESULT.json; research/ddp/refresh_20261029/d14_D4_seven_plain_hub/TERMINAL.json; research/ddp/refresh_20261029/d14_D4_seven_plain_hub/check.cpp; research/ddp/refresh_20261029/d14_D4_seven_plain_hub/run_once.py; research/ddp/refresh_20261029/d14_D4_vertex_split_geodesic/INPUT.txt; research/ddp/refresh_20261029/d14_D4_vertex_split_geodesic/PREDICTION.md; research/ddp/refresh_20261029/d14_D4_vertex_split_geodesic/REPORT.md; research/ddp/refresh_20261029/d14_D4_vertex_split_geodesic/RESULT.json; research/ddp/refresh_20261029/d14_D4_vertex_split_geodesic/ROOT_RESULTS.jsonl; research/ddp/refresh_20261029/d14_D4_vertex_split_geodesic/TERMINAL.json; research/ddp/refresh_20261029/d14_D4_vertex_split_geodesic/check.cpp; research/ddp/refresh_20261029/d14_D4_vertex_split_geodesic/run_once.py; research/ddp/refresh_20261029/HUB_SPLIT_COMPLETED_WIKI_REPORT.md"
added: 2026-10-29T20:39:49Z
tags: ["ddp", "method-ledger"]
---

# (14,4)9720源：唯一7plain边共hub失败，全部相邻单点split排除

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (14,4)；L=9720；known_source_or_recovery n=9720；条件性n=9721（未据此计纪录）

**距目标的证据：** Primaryrecipe andsavedauthorverification bind9720/68040,all14regular. Therefore free0/slots0/minSatN14/zero-onefault0. Odd81fiber internallyunmatched hypothesisrefuted: p± aretwo distinctcross-cell perfectmatchings andcellsindependent. No localgraph/profile/BFS/candidate/newlowerbound.；7真实plain边/14互异端点通过，删边后T的R3仅9241/9720、漏479，首label1使拟hub距至少5，未生成9721图。随后81代表全部有distance4目标singleton首步支持，由left controllerAut排当前9720源全部相邻单点split；0划分枚举/候选图/oldold验收。

**其他指标（保持原计数类型）：**
```json
{
  "source_reported_D": 4,
  "source_m": 68040,
  "source_min_degree": 14,
  "source_max_degree": 14,
  "free_vertices": 0,
  "free_slots": 0,
  "minSatN": 14,
  "onefault": 0,
  "zeroSatN": 0,
  "degree_basis": "Authorrecipe andsavedverifier output, notlocalprofile",
  "controller_order": 120,
  "fiber": "GF3^4",
  "plain_pair_controller_order": 5,
  "cells_independent": true,
  "plain_pair_matches_between_cells": true,
  "plain_pair_factor_recipe_derived": {
    "C5": 24,
    "C10": 960
  },
  "raw_edge_header_read": false,
  "literal_downloaded": false,
  "compact_recipe_downloaded": true,
  "source_local_allroot_BFS": 0,
  "numerical_profile_runs": 0,
  "candidate_graphs": 0,
  "new_lower_bounds": 0,
  "prediction": "ODD_INTERNAL_MATCHING_SPARE_MODEL_REFUTED",
  "method_count_note": "Source/propertyrecord, notanexecutednewgraphconstruction.",
  "fixed7_hub_R3_missing": 479,
  "all_current_adjacent_vertex_splits_excluded": true,
  "adjacent_split_representatives_completed": 81,
  "new_graphs": 0,
  "old_old_candidate_BFS": 0
}
```



**从属变体：**
```json
[
  {
    "label": "fixed_seven_plain_matching_edges_common_hub_20261029",
    "status": "FIXED_MATCHING_HUB_REJECTED_ENDPOINT_R3_GATE",
    "source_n": 9720,
    "source_m": 68040,
    "source_degree": 14,
    "proposed_n": 9721,
    "proposed_m": 68047,
    "removed_edges": 7,
    "distinct_endpoints": 14,
    "B_order": 6,
    "A_outside_B_subgroup": true,
    "fixed_fiber": [
      1,
      0,
      1,
      1
    ],
    "endpoint_R3_covered": 9241,
    "endpoint_R3_missing": 479,
    "witness": 1,
    "witness_coordinates": "(I,0,(1,0,0,0))",
    "prospective_hub_distance_lower_bound": 5,
    "modified_old_multisource_R3_BFS": 1,
    "source_D4_revalidation": 0,
    "candidate_graphs_generated": 0,
    "candidate_BFS": 0,
    "native_CPU_seconds": 0.005219,
    "aggregate_prepare_compile_native_CPU_seconds": 1.288826814,
    "exact_scope": "Only frozen B^k phase0-to1 sixplain edges plus A phase2-to3 oneplain edge, all atfixed xstar.",
    "other_matching_hubs_excluded": false,
    "hub_distance_lemma": "If all removed edges have both endpoints in T, d_(G-M)(x,T)=d_G(x,T): a shortest path to T cannot use a removed edge before reaching T. A new hub joined only to T has distance1+d_G(x,T). This says nothing by itself about old-old candidate distances."
  },
  {
    "label": "all_current9720_adjacent_single_vertex_splits_geodesic_singletons_20261029",
    "status": "COMPLETE_ALL_CURRENT9720_ADJACENT_VERTEX_SPLITS_EXCLUDED",
    "source_n": 9720,
    "source_degree": 14,
    "representative_roots": 81,
    "completed": 81,
    "singleton_rejections": 81,
    "literal_roots_covered_by_left_controller_action": 9720,
    "example": {
      "root": 0,
      "target": 83,
      "sole_first_neighbor": 398
    },
    "partition_assignment_domain_if_needed": 8192,
    "actual_partition_assignments_tested": 0,
    "geodesic_support_BFS": 81,
    "source_D4_revalidation": false,
    "candidate_graphs_generated": 0,
    "candidate_BFS": 0,
    "native_CPU_seconds": 0.036461,
    "aggregate_prepare_compile_native_CPU_seconds": 1.069389204,
    "split_lemma": "For old distance4 target t, every <=4 path from either split side must avoid the new internal split edge; otherwise contraction gives an old path<=3. Thus all old geodesic first-neighbor supports must meet both color classes; a singleton rejects every partition.",
    "exact_scope": "Retain allG-v edges; partition all14 oldneighbors between two adjacent split vertices. Currentliteral source only.",
    "other_sources_or_multi_vertex_edits_excluded": false
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/d14_D4_current9720_source/REPORT.md](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/REPORT.md)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/PREDICTION.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/PREDICTION.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/SOURCE.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/SOURCE.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/RESULT.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/RESULT.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/PLAIN_PAIR_STRUCTURE.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/PLAIN_PAIR_STRUCTURE.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/AUTHOR_README.md](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/AUTHOR_README.md)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/construction.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/construction.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/AUTHOR_VERIFICATION.txt](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/AUTHOR_VERIFICATION.txt)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/SOURCE_RECEIPTS.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/SOURCE_RECEIPTS.json)；[research/ddp/more_graphs_20261027/d14_D4_current9720_source/LEDGER_CHECK.json](../../research/ddp/more_graphs_20261027/d14_D4_current9720_source/LEDGER_CHECK.json)；[research/ddp/refresh_20261029/d14_D4_seven_plain_hub/GATE_RESULT.json](../../research/ddp/refresh_20261029/d14_D4_seven_plain_hub/GATE_RESULT.json)；[research/ddp/refresh_20261029/d14_D4_seven_plain_hub/INPUT.txt](../../research/ddp/refresh_20261029/d14_D4_seven_plain_hub/INPUT.txt)；[research/ddp/refresh_20261029/d14_D4_seven_plain_hub/MISSING_TARGETS.json](../../research/ddp/refresh_20261029/d14_D4_seven_plain_hub/MISSING_TARGETS.json)；[research/ddp/refresh_20261029/d14_D4_seven_plain_hub/PARAMETERS.json](../../research/ddp/refresh_20261029/d14_D4_seven_plain_hub/PARAMETERS.json)；[research/ddp/refresh_20261029/d14_D4_seven_plain_hub/PREDICTION.md](../../research/ddp/refresh_20261029/d14_D4_seven_plain_hub/PREDICTION.md)；[research/ddp/refresh_20261029/d14_D4_seven_plain_hub/REPORT.md](../../research/ddp/refresh_20261029/d14_D4_seven_plain_hub/REPORT.md)；[research/ddp/refresh_20261029/d14_D4_seven_plain_hub/RESULT.json](../../research/ddp/refresh_20261029/d14_D4_seven_plain_hub/RESULT.json)；[research/ddp/refresh_20261029/d14_D4_seven_plain_hub/TERMINAL.json](../../research/ddp/refresh_20261029/d14_D4_seven_plain_hub/TERMINAL.json)；[research/ddp/refresh_20261029/d14_D4_seven_plain_hub/check.cpp](../../research/ddp/refresh_20261029/d14_D4_seven_plain_hub/check.cpp)；[research/ddp/refresh_20261029/d14_D4_seven_plain_hub/run_once.py](../../research/ddp/refresh_20261029/d14_D4_seven_plain_hub/run_once.py)；[research/ddp/refresh_20261029/d14_D4_vertex_split_geodesic/INPUT.txt](../../research/ddp/refresh_20261029/d14_D4_vertex_split_geodesic/INPUT.txt)；[research/ddp/refresh_20261029/d14_D4_vertex_split_geodesic/PREDICTION.md](../../research/ddp/refresh_20261029/d14_D4_vertex_split_geodesic/PREDICTION.md)；[research/ddp/refresh_20261029/d14_D4_vertex_split_geodesic/REPORT.md](../../research/ddp/refresh_20261029/d14_D4_vertex_split_geodesic/REPORT.md)；[research/ddp/refresh_20261029/d14_D4_vertex_split_geodesic/RESULT.json](../../research/ddp/refresh_20261029/d14_D4_vertex_split_geodesic/RESULT.json)；[research/ddp/refresh_20261029/d14_D4_vertex_split_geodesic/ROOT_RESULTS.jsonl](../../research/ddp/refresh_20261029/d14_D4_vertex_split_geodesic/ROOT_RESULTS.jsonl)；[research/ddp/refresh_20261029/d14_D4_vertex_split_geodesic/TERMINAL.json](../../research/ddp/refresh_20261029/d14_D4_vertex_split_geodesic/TERMINAL.json)；[research/ddp/refresh_20261029/d14_D4_vertex_split_geodesic/check.cpp](../../research/ddp/refresh_20261029/d14_D4_vertex_split_geodesic/check.cpp)；[research/ddp/refresh_20261029/d14_D4_vertex_split_geodesic/run_once.py](../../research/ddp/refresh_20261029/d14_D4_vertex_split_geodesic/run_once.py)；[research/ddp/refresh_20261029/HUB_SPLIT_COMPLETED_WIKI_REPORT.md](../../research/ddp/refresh_20261029/HUB_SPLIT_COMPLETED_WIKI_REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Exactcurrent9720 authorrecipe, sourcekeep-all-oldedges augmentation only. Anypositive addedorder isblocked atmax14 because alloldvertices saturated. No old8303/8332/8019, no group/field/controller transfer.；后续唯一7plain匹配边共hub及81fiber代表的全部相邻singlevertexsplit geodesic gate按明确范围执行；不同于旧保边append或controller迁移。

**仍未完成：** 此全正则源保边append、固定7plain-edge hub和全部相邻singlevertexsplit各已关闭。其它matching hub、额外改边、多点改造及一般(14,4)仍开放。

**启发与重启依据：** Oddfiber cardinality onlyforces matching defects for internalone-factors. Cross-cell matchings alongcontrollerp oforder5 avoid thatparity obstruction and give2neighbors everywhere, includingfixedfibercoords. Useactualrecipe before degreespaceinference; reopenonlyfor a separatelyjustified edge-changing ornewsource rule.；固定7边共hub规则已停，不换coset/xstar。当前源相邻单点split已被全81代表singleton门排除，不能再试另一根或邻居划分。其它matching hub、其它源或多点改造未排。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

