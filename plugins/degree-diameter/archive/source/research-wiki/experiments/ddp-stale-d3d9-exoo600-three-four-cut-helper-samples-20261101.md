---
type: experiment
node_id: exp:ddp-stale-d3d9-exoo600-three-four-cut-helper-samples-20261101
title: "3D9 Exoo600→602改边：三cut与四cut各10000样本均漏helper覆盖，整规则保持UNKNOWN并停止"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: partial
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/PAPER_NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/run.cpp; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/run_once.py; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/ATTEMPTS.csv; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/PAPER_NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/run.cpp; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/run_once.py; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/ATTEMPTS.csv; research/ddp/more_graphs_20261027/d3_D9_current600_source/SOURCE_REPORT.md; research/ddp/more_graphs_20261027/d3_D9_current600_source/SOURCE_PROFILE.json; research/ddp/more_graphs_20261027/d3_D9_current600_source/CONDITIONAL_SUBDIVISION_LEMMA.md"
added: 2026-11-01T18:25:00Z
tags: ["ddp", "method-ledger"]
---

# 3D9 Exoo600→602改边：三cut与四cut各10000样本均漏helper覆盖，整规则保持UNKNOWN并停止

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** bounded_candidate_or_input_transfer_gate

**目标与阶数：** (3,9)；L=600；条件性n=602（未据此计纪录）

**距目标的证据：** No accepted final target graph or complete global target diameter; source facts and scoped checks only；旧source非二分，不能使用odd-bipartite自动细分覆盖。三cut样本9999先漏helper600、1案600通过却601到old2距10；四cut真实消除“同cut两端必同为pins”的强制关联，但10000案全部漏helper600R9。两轮双方helper都通过为0，modified old-labelled BFS均0，不能说本轮发现old-old损伤。两次“出现双方helper覆盖”预测均被样本推翻；不是整个3cut/4cut族NO。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_parameter_pairs": 0,
  "new_Lean_instances": 0,
  "new_independent_method_claims": 0,
  "Moore_bound": 1534,
  "located_baseline": 600,
  "Moore_space": 934,
  "Moore_gap_is_not_constructibility": true,
  "source_order": 600,
  "source_edges": 900,
  "source_degree": 3,
  "source_D9": "primary inherited; no sourceD9BFS",
  "source_bipartite": false,
  "symmetry_unbound": true,
  "target_cubic_edges": 903,
  "three_cut": {
    "seed": 202611010309,
    "distinct_configurations_finished": 10000,
    "rejected_helper600": 9999,
    "rejected_helper601": 1,
    "both_helpers_passed": 0,
    "rejected_old_old": 0,
    "helper_root_BFS_count": 10001,
    "modified_graph_old_label_BFS_count": 0,
    "first_helper600_failure": {
      "configuration": {
        "cut_edge_indices": [
          255,
          455,
          637
        ],
        "cut_edges": [
          [
            85,
            122
          ],
          [
            167,
            551
          ],
          [
            232,
            400
          ]
        ],
        "repair": [
          122,
          400
        ],
        "pins600": [
          85,
          551
        ],
        "pins601": [
          167,
          232
        ]
      },
      "BFS": {
        "root": 600,
        "target": 49,
        "distance": 10,
        "reached": 602,
        "eccentricity": 10,
        "actual_path": [
          600,
          85,
          282,
          376,
          210,
          431,
          58,
          334,
          206,
          456,
          49
        ]
      }
    },
    "first_helper601_failure": {
      "configuration": {
        "cut_edge_indices": [
          15,
          238,
          578
        ],
        "cut_edges": [
          [
            5,
            325
          ],
          [
            79,
            253
          ],
          [
            212,
            462
          ]
        ],
        "repair": [
          5,
          79
        ],
        "pins600": [
          212,
          462
        ],
        "pins601": [
          253,
          325
        ]
      },
      "BFS": {
        "root": 601,
        "target": 2,
        "distance": 10,
        "reached": 602,
        "eccentricity": 10,
        "actual_path": [
          601,
          253,
          371,
          569,
          512,
          36,
          328,
          142,
          109,
          531,
          2
        ]
      }
    },
    "prediction_both_helpers_supported": false,
    "complete_configuration_family_exclusion": false
  },
  "four_cut": {
    "seed": 202611010309,
    "distinct_configurations_finished": 10000,
    "rejected_helper600": 10000,
    "rejected_helper601": 0,
    "both_helpers_passed": 0,
    "rejected_old_old": 0,
    "helper_root_BFS_count": 10000,
    "modified_graph_old_label_BFS_count": 0,
    "first_helper600_failure": {
      "configuration": {
        "cut_edge_indices": [
          255,
          455,
          637,
          715
        ],
        "cut_edges": [
          [
            85,
            122
          ],
          [
            167,
            551
          ],
          [
            232,
            400
          ],
          [
            267,
            428
          ]
        ],
        "repairs": [
          [
            122,
            267
          ],
          [
            167,
            232
          ]
        ],
        "pins600": [
          85,
          400
        ],
        "pins601": [
          428,
          551
        ]
      },
      "BFS": {
        "root": 600,
        "target": 2,
        "distance": 10,
        "reached": 602,
        "eccentricity": 10,
        "actual_path": [
          600,
          85,
          282,
          461,
          25,
          501,
          103,
          177,
          592,
          531,
          2
        ]
      }
    },
    "prediction_both_helpers_supported": false,
    "complete_configuration_family_exclusion": false
  },
  "first_rule_charged_CPU": 1.4148908329999998,
  "cumulative_charged_CPU": 2.860445652,
  "CPU_budget": 20,
  "no_timer_reset": true,
  "actual_modified_helper_root_BFS_total": 20001,
  "modified_old_label_root_BFS": 0,
  "source_validity_D9_BFS": 0,
  "helper_cooperation_formula": "R7_K(A) union R7_K(B) union [R8_K(A) intersect R8_K(B)] covers all old vertices",
  "complete_family_exclusion": false,
  "ordinary_fulltarget_badpairs": null,
  "global_target_D": null,
  "terminal": true
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/PAPER_NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/PAPER_NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/run.cpp](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/run.cpp)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/run_once.py](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/run_once.py)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/ATTEMPTS.csv](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/ATTEMPTS.csv)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/PAPER_NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/PAPER_NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/run.cpp](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/run.cpp)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/run_once.py](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/run_once.py)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/ATTEMPTS.csv](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/ATTEMPTS.csv)；[research/ddp/more_graphs_20261027/d3_D9_current600_source/SOURCE_REPORT.md](../../research/ddp/more_graphs_20261027/d3_D9_current600_source/SOURCE_REPORT.md)；[research/ddp/more_graphs_20261027/d3_D9_current600_source/SOURCE_PROFILE.json](../../research/ddp/more_graphs_20261027/d3_D9_current600_source/SOURCE_PROFILE.json)；[research/ddp/more_graphs_20261027/d3_D9_current600_source/CONDITIONAL_SUBDIVISION_LEMMA.md](../../research/ddp/more_graphs_20261027/d3_D9_current600_source/CONDITIONAL_SUBDIVISION_LEMMA.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** One fixed inherited Exoo600 cubic/D9 source. First fixed-seed10000 distinct configurations:3matching cuts,1original-nonedge endpoint repair,remaining4pins2+2 at adjacent helpers. Second10000:4matching cuts,onepin percut,remaining4endpoints2old repairs,adjacent helpers2+2. Bounded samples only, not complete domains; no other seed/source/cut pattern.

**仍未完成：** The general degree/diameter target remains open; stop only the explicitly sampled or failed input rule.

**启发与重启依据：** STOP both bounded samples under the same20CPU ledger. No fifth cut, secondseed or source-D9/BFS rerun. A future experiment needs a genuinely changed premise; AFY70/D5 completeNO must not be imported as Exoo600/D9 exclusion.

**单独的重启条件：** STOP both bounded samples under the same20CPU ledger. No fifth cut, secondseed or source-D9/BFS rerun. A future experiment needs a genuinely changed premise; AFY70/D5 completeNO must not be imported as Exoo600/D9 exclusion.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

