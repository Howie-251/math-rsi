---
type: experiment
node_id: exp:ddp-stale-d4d3-messieres-n2n3-two-cut4star-source-comparison-20261101
title: "4D3 N2/N3两cut对照＋N2定向三cut修补全终态：6150旧规则NO，3048修补参数无联合覆盖"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/ROOT_DISPOSITION.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/run_once.py; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/N2_RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/N3_RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/N2_ALL_PAIR_PARAMETERS.tsv; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/N3_ALL_PAIR_PARAMETERS.tsv; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/N2_ALL_PAIR_STAGES.tsv; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/N3_ALL_PAIR_STAGES.tsv; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/ONE_OLDPAIR_ROUTE_DIAGNOSTIC.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/source_N2.NORMALIZED_ADJ.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/source_N3.NORMALIZED_ADJ.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/run_once.py; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/ROOT_DISPOSITION.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/SIX_SAVED_BASES.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/ALL_ACTUAL_VARIANTS.tsv"
added: 2026-11-01T20:27:43Z
tags: ["ddp", "method-ledger"]
---

# 4D3 N2/N3两cut对照＋N2定向三cut修补全终态：6150旧规则NO，3048修补参数无联合覆盖

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (4,3)；L=41；条件性n=42（未据此计纪录）

**距目标的证据：** All6150actual42/84edited candidates rejected;newrootfirst thenoldlabelsuntilfirstfailure,noaccepted42/globalDclaim；旧A域N2/N3各3075全访：N2六次newrootR3pass全部oldoldfail、14candidate旧根，N3无pass；旧pair0→1 ONE_PIN由3变4，1.503331119/5CPU。新B域基于六个真实pass基例逐做一port交换/第三cut+oldoldrepair：3048参数（跨基例未去重），2622未修savedpair；426确实修好pair，却426全部newrootR3失败，joint0/finaloldrootstage0。联合预测被完整有限域反驳，不是旧pair毫无改善。首基例303第三cut0–18、删star–1、加1–0与star–18：旧0→1从4变1，但41→1新最短41–2–15–34–1长4。新case.249139578/5CPU、sourceJSONparse1/sourceD3BFS0/旧A域不重跑。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_parameter_pairs": 0,
  "new_Lean_instances": 0,
  "new_independent_method_claims": 0,
  "related_N1_experiment": "ddp-stale-d4d3-messieres-n1-all3075-two-cut-fourstar42-no-20261101",
  "related_cached_source_node": "ddp-stale-d4d5-messieres-three41-any-ninecover-capacity-20261101",
  "ordinaryninecover_same_scope": false,
  "actual_source_domains": [
    3075,
    3075
  ],
  "all_configurations_finished": 6150,
  "newroot_passes": [
    6,
    0
  ],
  "newroot_fails": [
    3069,
    3075
  ],
  "oldold_fails_after_newrootpass": [
    6,
    0
  ],
  "candidate_oldroot_BFS": [
    14,
    0
  ],
  "prediction_newroot_supported": true,
  "complete42hits": 0,
  "source_cached_JSON_parses": [
    1,
    1
  ],
  "source_single_pair_diagnostic": 1,
  "source_D3_allroot_nonisomorphism_rechecks": 0,
  "diagnostic": {
    "source": "N2",
    "pair": [
      0,
      1
    ],
    "pins": [
      1,
      2,
      4,
      35
    ],
    "cuts": [
      [
        1,
        4
      ],
      [
        2,
        35
      ]
    ],
    "pin_relation": "ONE_PIN",
    "old_path": [
      0,
      37,
      4,
      1
    ],
    "old_distance": 3,
    "new_shortest_path": [
      0,
      18,
      8,
      13,
      1
    ],
    "new_distance": 4,
    "old_route_unique_claimed": false
  },
  "old_route_unique_claimed": false,
  "contrast_to_N1": "N1had3newrootpassbutoldoldfailwithfirstBOTH_NONPIN;N2has6butfirstONE_PINfails;N3hasnone. Changedsourcealonedidnotmakebothtypesofroutework.",
  "complete_NO_scope": "OnlycachedN2/N3 fixed41sources,two disjointoldedgedeletions,newpointjoinedtoallfourendpoints",
  "cumulative_charged_CPU_seconds": 1.503331119,
  "CPU_budget_seconds": 5,
  "prior_readgate_CPU_seconds": 1.125664745,
  "no_timer_reset": true,
  "original_two_cut_batch_all_processes_terminal": true,
  "separate_changed_generation_scope": {
    "status": "ROOT_ACCEPTED_COMPLETE_NO_SIX_N2_BASES_TARGETED_THREECUT_REPAIR42",
    "terminal_result_received": true,
    "root_reported_in_progress": false,
    "source": "N2only,sixsavednewrootPASS_oldoldFAILbasecases",
    "base_configurations": [
      303,
      1286,
      1446,
      2076,
      2248,
      2844
    ],
    "rule": "p in originalfourpins,thirdorientedsourceedge(a,b)outsidepins,p-aoriginalnonedge;deletea-b andstar-p,addp-a andstar-b",
    "meaning": "threeoriginalcutsplusoldoldrepair,maintains4regularity;differentfromoldtwo-cut4starfamily",
    "parameter_configurations": 3048,
    "parameters_per_base": [
      508,
      508,
      508,
      508,
      508,
      508
    ],
    "cross_base_literal_deduplication": false,
    "independent_or_nonisomorphic_graph_count_claimed": false,
    "saved_pair_failed": 2622,
    "saved_pair_repaired": 426,
    "newroot_R3_fail_after_pair_repaired": 426,
    "joint_pair_repair_newroot_pass": 0,
    "final_oldlabel_BFS_roots": 0,
    "targeted_pair_BFS": 3048,
    "newroot_BFS": 426,
    "prediction": "AtleastonevariantrepairssavedpairandpreservesnewrootR3",
    "prediction_supported": false,
    "first_concrete_tradeoff": {
      "base": 303,
      "original_cuts": [
        [
          1,
          4
        ],
        [
          2,
          35
        ]
      ],
      "third_cut": [
        0,
        18
      ],
      "removed_star_pin": 1,
      "added_oldold_edge": [
        1,
        0
      ],
      "new_star_pin": 18,
      "saved_oldpair": [
        0,
        1
      ],
      "oldpair_distance_before": 4,
      "oldpair_distance_after": 1,
      "newroot_failed_pair": [
        41,
        1
      ],
      "newroot_distance_after": 4,
      "newroot_shortest_path": [
        41,
        2,
        15,
        34,
        1
      ]
    },
    "wholecase_CPU_seconds": 0.249139578,
    "CPU_budget_seconds": 5,
    "source_JSON_parses": 1,
    "source_D3_BFS_roots": 0,
    "old_two_cut_batch_repeated": false,
    "scope": "OnlysixsavedN2two-cutnewrootPASS/oldoldFAILbases,thethirdcutoutsideoriginalfourpins,p-aoriginalnonedge,specifiedonepinreplacementandoneoldoldrepair",
    "not_excluded": "general3-cutrepairrule,otherbases,sources,repairpatterns,generalN4D3",
    "all_processes_terminal": true,
    "next": "PAUSE_THIS_MINIMAL_STAR_AND_ONE_PORT_EXCHANGE_LINE_NO_N4_SECOND_REPAIR_OR_SEED"
  },
  "historical_changed_rule_pending_checkpoint": {
    "status": "ROOT_AUTHORIZED_SEPARATE_BOUNDED_CHANGED_RULE_BATCH",
    "terminal_result_received": false,
    "source": "N2only,sixactualnewrootPASSbasecases",
    "rule": "choosep in4pins andthirdoriginaledge(a,b)outsidepins withp-aoldnonedge;deletea-b andstar-p,addp-a andstar-b",
    "meaning": "threeoriginalcutsplusoldoldrepair,maintains4regularity;nottheruled-outtwocut4starfamily",
    "prediction": "AtleastonevariantrepairsitsfirstoldpairandkeepsnewrootR3;complete42unknown",
    "maximum_variants": 3936,
    "CPU_budget_seconds": 5,
    "owner": "/root/f9_56862_independent",
    "root_reported_in_progress": true,
    "no_result_claimed": true,
    "no_N4_or_blindcut_ladder": true
  },
  "targeted_repair_terminal": true,
  "targeted_repair_joint_prediction_supported": false,
  "targeted_repair_old_two_cut_batch_repeated": false,
  "mechanism_line_paused": true,
  "targeted_repair_parameter_configurations_not_independent_graphs": 3048
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/ROOT_DISPOSITION.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/ROOT_DISPOSITION.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/run_once.py](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/run_once.py)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/N2_RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/N2_RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/N3_RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/N3_RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/N2_ALL_PAIR_PARAMETERS.tsv](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/N2_ALL_PAIR_PARAMETERS.tsv)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/N3_ALL_PAIR_PARAMETERS.tsv](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/N3_ALL_PAIR_PARAMETERS.tsv)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/N2_ALL_PAIR_STAGES.tsv](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/N2_ALL_PAIR_STAGES.tsv)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/N3_ALL_PAIR_STAGES.tsv](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/N3_ALL_PAIR_STAGES.tsv)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/ONE_OLDPAIR_ROUTE_DIAGNOSTIC.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/ONE_OLDPAIR_ROUTE_DIAGNOSTIC.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/source_N2.NORMALIZED_ADJ.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/source_N2.NORMALIZED_ADJ.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/source_N3.NORMALIZED_ADJ.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/source_N3.NORMALIZED_ADJ.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/run_once.py](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/run_once.py)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/ROOT_DISPOSITION.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/ROOT_DISPOSITION.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/SIX_SAVED_BASES.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/SIX_SAVED_BASES.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/ALL_ACTUAL_VARIANTS.tsv](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/ALL_ACTUAL_VARIANTS.tsv)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** ScopeA:cachedliteralN2/N3,eachall3075unorderedpairsofdisjointoldedges,delete2edges/addone4star,completeNO. ScopeB:onlysixsavedN2newrootPASS_oldoldFAILbases;choosep in original4pins andorientedthirdoriginaledge(a,b)outsidepins withp-aoldnonedge,deletea-b andstar-p,addp-a andstar-b. All3048parameterconfigurations completed,withoutcross-base literaldeduplication;not3048independentgraphs. ScopeBcompleteNOonlyforthisboundedrule,notall3cutrepairs,otherbases/sources/repairpatterns/general4D3.

**仍未完成：** General3cutrepairrules,otherbases/sources/repairpatterns and generalN(4,3) remain open. Both recorded finitebatches are terminal and paused;no accepted42graph or further experiment authorized.

**启发与重启依据：** Pause the N1/N2/N3 minimalstar and one-local-port-exchange line. The targetedrepair really fixes426savedpairs but always losesnewrootcoverage in this exact domain,so preserve/repair routes must be designed jointly. No N4,secondrepair,seed or source/cut ladder. Next choose anotherparameter fromthe15oldcells or propose explicit simultaneousmulti-routecompensation before a new bounded experiment. General3cut/otherrepairs remain unexcluded,not automatically authorized.

**单独的重启条件：** Anotherparameter or a genuinely new interface with explicit simultaneous oldpair and newroot route compensation;no continuation of the closed two-cut or specified six-base repair domains.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

