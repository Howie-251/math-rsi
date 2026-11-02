---
type: experiment
node_id: exp:ddp-stale-d10d4-signed-f2-15552-transfer3072-inverse-failure-20261101
title: "10D4目标3072的signed-F2迁移：0→183无反向，指定整数lift仅char3可能互反，未构造图"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/PRED.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/NOTE.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/PAPER_INTERFACE.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/RESULT.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/TERMINAL.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/COUNTEREXAMPLE.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/NEW_BINARY_GLOBAL_TYPES.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/run_once.py"
added: 2026-11-01T18:25:00Z
tags: ["ddp", "method-ledger"]
---

# 10D4目标3072的signed-F2迁移：0→183无反向，指定整数lift仅char3可能互反，未构造图

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** bounded_candidate_or_input_transfer_gate

**目标与阶数：** (10,4)；L=2556；条件性n=3072（未据此计纪录）

**距目标的证据：** No accepted final target graph or complete global target diameter; source facts and scoped checks only；F2不是旧F3证明自动特化：26个新关系逆检查后实际0→183(globaltype1,noise1)仅有type3可回controller0，binary reverse噪声候选标签2/13都非0；真互反关系失败，8个真实global stays跳过。singularB本非GL，检查的是存在reverse noise。signed整数B3v1=−3e1，旧mod3为0而F2残留e1；指定同一整数lift在任意char≠3亦无法由v3=(1,1,1,1)抵消。0图/0BFS，未尝试ORsymm修度数或第二lift。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_parameter_pairs": 0,
  "new_Lean_instances": 0,
  "new_independent_method_claims": 0,
  "Moore_bound": 8201,
  "located_baseline": 2556,
  "Moore_space": 5645,
  "hypothetical_target": 3072,
  "target_margin_if_legal": 516,
  "Moore_gap_is_not_constructibility": true,
  "inherited_source": {
    "n": 15552,
    "controller_count": 192,
    "fiber": "F3^4",
    "published_reproduction": true,
    "controller_only_inherited": true
  },
  "coefficient_rule": "0→0,1→1,2→integer−1 then mod2; no field homomorphism claimed",
  "counterexample": {
    "kind": "ACTUAL_DIRECTED_RELATION_NOT_RECIPROCAL",
    "global_type": 1,
    "source_label": 0,
    "target_label": 183,
    "input_controller": 0,
    "output_controller": 11,
    "input_coordinates": [
      0,
      0,
      0,
      0
    ],
    "noise": 1,
    "output_coordinates": [
      1,
      1,
      1,
      0
    ],
    "original_arc": {
      "from": 0,
      "to": 11,
      "pivot": 0,
      "v": [
        1,
        2,
        2,
        0
      ],
      "c": [
        0,
        0,
        0,
        0
      ],
      "B": [
        [
          0,
          0,
          0,
          0
        ],
        [
          0,
          2,
          0,
          1
        ],
        [
          2,
          1,
          2,
          1
        ],
        [
          0,
          2,
          2,
          2
        ]
      ],
      "v_offset": 25,
      "c_offset": 0,
      "column_offsets": [
        18,
        69,
        72,
        66
      ]
    },
    "signed_integer_B": [
      [
        0,
        0,
        0,
        0
      ],
      [
        0,
        -1,
        0,
        1
      ],
      [
        -1,
        1,
        -1,
        1
      ],
      [
        0,
        -1,
        -1,
        -1
      ]
    ],
    "signed_integer_v": [
      1,
      -1,
      -1,
      0
    ],
    "binary_arc": {
      "from": 0,
      "to": 11,
      "B": [
        [
          0,
          0,
          0,
          0
        ],
        [
          0,
          1,
          0,
          1
        ],
        [
          1,
          1,
          1,
          1
        ],
        [
          0,
          1,
          1,
          1
        ]
      ],
      "v": [
        1,
        1,
        1,
        0
      ],
      "c": [
        0,
        0,
        0,
        0
      ]
    },
    "reverse_original_arcs": [
      {
        "from": 11,
        "to": 0,
        "pivot": 0,
        "v": [
          1,
          1,
          1,
          1
        ],
        "c": [
          0,
          0,
          0,
          0
        ],
        "B": [
          [
            0,
            0,
            0,
            0
          ],
          [
            2,
            1,
            1,
            2
          ],
          [
            1,
            0,
            1,
            1
          ],
          [
            0,
            2,
            1,
            2
          ]
        ],
        "v_offset": 40,
        "c_offset": 0,
        "column_offsets": [
          15,
          57,
          39,
          69
        ]
      }
    ],
    "reverse_binary_arcs": [
      {
        "from": 11,
        "to": 0,
        "B": [
          [
            0,
            0,
            0,
            0
          ],
          [
            1,
            1,
            1,
            1
          ],
          [
            1,
            0,
            1,
            1
          ],
          [
            0,
            1,
            1,
            1
          ]
        ],
        "v": [
          1,
          1,
          1,
          1
        ],
        "c": [
          0,
          0,
          0,
          0
        ]
      }
    ],
    "all_actual_reverse_noise_candidates": [
      {
        "reverse_controller": 0,
        "noise": 0,
        "coordinates": [
          0,
          1,
          0,
          0
        ],
        "label": 2
      },
      {
        "reverse_controller": 0,
        "noise": 1,
        "coordinates": [
          1,
          0,
          1,
          1
        ],
        "label": 13
      }
    ],
    "reverse_target_arc_count": 1,
    "entire_global_labels_are_distinct": true
  },
  "new_true_arc_reverse_tests": 26,
  "actual_global_stays_skipped": 8,
  "paper_char3_necessary_corollary": {
    "status": "PAPER_ONLY_SAME_SIGNED_INTEGER_FAMILY",
    "unique_return_controller11_to0": true,
    "obstruction": "0=−3e1+s(1,1,1,1) forces s0 then3=0",
    "scope": "all fields of char!=3 for these fixed signed coefficients; not different integer lifts or redesigned relations",
    "new_field_runs": 0
  },
  "integral_type0_contrast": "B0v0=0 and B0^2=I−v0e0^T hold as signed integer identities; one successfultype does not transfer alltypes",
  "actual_process_CPU": 0.04016489,
  "charged_CPU": 0.24016489000000002,
  "preparation_charge": 0.2,
  "CPU_budget": 20,
  "new_target_graph_generated": false,
  "target_BFS": 0,
  "old_F3_field_rank_graph_BFS_Lean_checks": 0,
  "solver_remote_runs": 0,
  "terminal": true
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/PRED.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/PRED.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/NOTE.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/NOTE.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/PAPER_INTERFACE.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/PAPER_INTERFACE.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/RESULT.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/RESULT.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/COUNTEREXAMPLE.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/COUNTEREXAMPLE.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/NEW_BINARY_GLOBAL_TYPES.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/NEW_BINARY_GLOBAL_TYPES.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/run_once.py](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/run_once.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Only the literal signed integer lift0→0,1→1,2→−1 of the five actual F3 affine templates, then reduction toF2; original192 controller unchanged. No field-homomorphism claim, symmetrization, alternate integer representatives or other fields/templates tested. Paper corollary uses the same signed integers and unique11→0 return arc to require characteristic3.

**仍未完成：** The general degree/diameter target remains open; stop only the explicitly sampled or failed input rule.

**启发与重启依据：** STOP this one signed-F2 recipe and do not scan positive2/fields or silently symmetrize. The characteristic condition is only for these exact signed integer representatives; redesigned matrices or different representatives and general10D4 remain open. OldF3 source/kernel remains accepted but is not a certificate for the failed transfer.

**单独的重启条件：** STOP this one signed-F2 recipe and do not scan positive2/fields or silently symmetrize. The characteristic condition is only for these exact signed integer representatives; redesigned matrices or different representatives and general10D4 remain open. OldF3 source/kernel remains accepted but is not a certificate for the failed transfer.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

