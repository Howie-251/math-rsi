---
type: experiment
node_id: exp:ddp-stale-d3d6-exoo132-adjacent-helpers-repair134-sample-20261101
title: "3D6 Exoo132→134：10000三cut相邻helpers样本全漏联合覆盖，原规则UNKNOWN并停止"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: partial
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/ROOT_DISPOSITION.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/SOURCE_INPUT_BINDING.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/ATTEMPTS.csv; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/run.cpp; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/run_once.py; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/ROOT_DISPOSITION.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/PAPER_SCOPE_REVIEW.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/SOURCE_LITERAL_RETRIEVAL.json"
added: 2026-11-01T19:17:55Z
tags: ["ddp", "method-ledger"]
---

# 3D6 Exoo132→134：10000三cut相邻helpers样本全漏联合覆盖，原规则UNKNOWN并停止

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** bounded_or_exact_modified_graph_gate

**目标与阶数：** (3,6)；L=132；条件性n=134（未据此计纪录）

**距目标的证据：** No accepted final target graph; actual candidate root checks and exact scope below；source132/198上界input一次绑定132labels/198simpleedges/全3degree；D6由primary继承。133由degree≤2根B6≤127迫全cubic再奇偶排，因此试134/201。新相邻helper条件R4_H(A)∪R4_H(B)∪[R5_H(A)∩R5_H(B)]=all，比D5多一层提供试验依据。实际10000distinct：9997先helper132R6失败，余3 helper133R6失败，both0/old-labelled BFS0。联合cover预测未获本样本支持，不能写成old-old损伤或整个familyNO。首helper132到old3、helper133到old11各距7，完整路线保存。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_parameter_pairs": 0,
  "new_Lean_instances": 0,
  "new_independent_method_claims": 0,
  "Moore_bound": 190,
  "located_baseline": 132,
  "Moore_space": 58,
  "Moore_gap_is_not_constructibility": true,
  "source_order": 132,
  "source_edges": 198,
  "source_D6": "PRIMARY_INHERITED_NOT_NUMERICALLY_VALIDATED",
  "source_identity": "Exoo1998 cubicD6,notPSL132",
  "source_input_binding": {
    "status": "PASS_LITERAL_SIMPLE_CUBIC_INPUT",
    "n": 132,
    "m": 198,
    "raw_edge_occurrences": 198,
    "row_count": 132,
    "duplicate_row_labels": 0,
    "selfloops": 0,
    "all132_labels_present_and_degree3": true,
    "source_D6_BFS": 0,
    "raw_parse_count": 1
  },
  "target_cubic_edges": 201,
  "degree2_root_B6_upper": 127,
  "n133_impossible_by_local_degree_and_parity": true,
  "seed": 202611010306,
  "distinct_configurations": 10000,
  "first_helper_failures": 9997,
  "second_helper_failures_after_firstpass": 3,
  "both_helpers_passed": 0,
  "actual_modified_helper_BFS_roots": 10003,
  "modified_old_label_BFS": 0,
  "source_D6_BFS": 0,
  "optional_original_pair_diagnostic_BFS": 0,
  "first_helper132_failure": {
    "configuration": {
      "cut_edge_indices": [
        39,
        161,
        186
      ],
      "cut_edges": [
        [
          18,
          44
        ],
        [
          88,
          89
        ],
        [
          111,
          112
        ]
      ],
      "repair": [
        88,
        111
      ],
      "pins132": [
        18,
        112
      ],
      "pins133": [
        44,
        89
      ]
    },
    "BFS": {
      "root": 132,
      "target": 3,
      "distance": 7,
      "reached": 134,
      "eccentricity": 7,
      "actual_path": [
        132,
        18,
        16,
        17,
        5,
        4,
        7,
        3
      ]
    }
  },
  "first_helper133_failure": {
    "configuration": {
      "cut_edge_indices": [
        39,
        93,
        136
      ],
      "cut_edges": [
        [
          18,
          44
        ],
        [
          46,
          84
        ],
        [
          72,
          73
        ]
      ],
      "repair": [
        46,
        72
      ],
      "pins132": [
        18,
        44
      ],
      "pins133": [
        73,
        84
      ]
    },
    "BFS": {
      "root": 133,
      "target": 11,
      "distance": 7,
      "reached": 134,
      "eccentricity": 7,
      "actual_path": [
        133,
        73,
        77,
        76,
        69,
        68,
        70,
        11
      ]
    }
  },
  "whole_configuration_family_excluded": false,
  "prediction_joint_coverage_supported": false,
  "root_acceptance": "ROOT_ACCEPTED_SAMPLE_UNKNOWN_NOT_FAMILY_NO",
  "cumulative_CPU": 1.872316415,
  "CPU_budget": 20,
  "no_timer_reset": true,
  "terminal": true,
  "reporting_template_correction": {
    "status": "ROOT_CORRECTED_WITHOUT_NUMERIC_RERUN",
    "current_radius": 6,
    "current_target": [
      134,
      201
    ],
    "paper": "../PAPER_SCOPE_REVIEW.md",
    "old600template_not_current_scope": true
  }
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/ROOT_DISPOSITION.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/ROOT_DISPOSITION.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/SOURCE_INPUT_BINDING.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/SOURCE_INPUT_BINDING.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/ATTEMPTS.csv](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/ATTEMPTS.csv)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/run.cpp](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/run.cpp)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/run_once.py](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/run_once.py)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/ROOT_DISPOSITION.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/ROOT_DISPOSITION.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/PAPER_SCOPE_REVIEW.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/PAPER_SCOPE_REVIEW.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/SOURCE_LITERAL_RETRIEVAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/SOURCE_LITERAL_RETRIEVAL.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Three disjoint old edge cuts; one original-nonedge repair on two cut endpoints; other four pins split2+2; helpers adjacent. One fixedseed10000-distinct sample only;not allmatching/repair choices. Source is actualExoo1998 cubicD6,not degree6/D3 PSL132. Sourcegate andsample are one mechanismnode.

**仍未完成：** Only this bounded sample or exact fixedsource edit scope stops; generaltarget remainsopen. Same Goal ACTIVE,oldN8/n61 PAUSED.

**启发与重启依据：** STOP this completed sample: no automaticseed/cutpattern/sample extension. A future experiment requires genuinely changed helpercoverage generation,not merely re-running the samepattern. Broader134graphs andotheroldedge edits remainopen;no numericalplan is started here.

**单独的重启条件：** STOP this completed sample: no automaticseed/cutpattern/sample extension. A future experiment requires genuinely changed helpercoverage generation,not merely re-running the samepattern. Broader134graphs andotheroldedge edits remainopen;no numericalplan is started here.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

