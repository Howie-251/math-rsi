---
type: experiment
node_id: exp:ddp-stale-d8d4-c30-gf4-binary-restriction-fivecover-input-20261101
title: "8D4五cover输入门：accepted F4/C30字面矩阵不保F2³，240与1200均未构造"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/c30_f2_fivecover_gate/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/c30_f2_fivecover_gate/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/c30_f2_fivecover_gate/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/c30_f2_fivecover_gate/TERMINAL.json"
added: 2026-11-01T17:57:59Z
tags: ["ddp", "method-ledger"]
---

# 8D4五cover输入门：accepted F4/C30字面矩阵不保F2³，240与1200均未构造

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** necessary_route_or_input_transfer_gate

**目标与阶数：** (8,4)；L=1100；条件性n=1200（未据此计纪录）

**距目标的证据：** No full target graph was generated; source legality inherited only；120个edge-local GF4矩阵的非binary系数共284项（α152、α+1共132）；controller0/port0在noise0将binary e2映到(α,0,α+1)。该字面rule未定义F2³闭源，故不存在可继承的240邻接，NB≤4五cover容量未运行；不是“某个已造240图的cover无解”。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_parameter_pairs": 0,
  "new_Lean_instances": 0,
  "new_independent_method_claims": 0,
  "conditional_base_order": 240,
  "conditional_cover_order": 1200,
  "accepted_source": {
    "n": 1920,
    "degree": 16,
    "q": 4,
    "reproduction_only": true
  },
  "binary_source_status": "not supplied/accepted; no claim of a degree8/order240 graph",
  "source_rule": {
    "path": "research/ddp/breadth_20261027_wave4/mizuno_d3_source/construction.json",
    "q": 4,
    "dimension": 3,
    "controller_order": 30,
    "edge_local_directed_matrices": 120,
    "GF4_encoding": {
      "0": "0",
      "1": "1",
      "2": "alpha",
      "3": "alpha+1"
    },
    "GF4_relation": "alpha^2+alpha+1=0",
    "coefficient_counts": {
      "0": 420,
      "1": 376,
      "2": 152,
      "3": 132
    }
  },
  "counterexample": {
    "controller": 0,
    "port": 0,
    "target_controller": 18,
    "matrix_GF4_codes": [
      [
        0,
        1,
        2
      ],
      [
        1,
        0,
        0
      ],
      [
        0,
        1,
        3
      ]
    ],
    "input": [
      0,
      0,
      1
    ],
    "noise": 0,
    "output_GF4_codes": [
      2,
      0,
      3
    ]
  },
  "minimum_NB_count": null,
  "actual_pair": null,
  "NB_capacity_gate_run": false,
  "source_BFS": 0,
  "CPU": {
    "this_saved_gate_process_seconds": 0.034669,
    "earlier_metadata_inspection_seconds": 0.001626606,
    "measured_process_total_seconds": 0.036295606,
    "limit_seconds": 10,
    "read_only_shell_and_manual_preparation": "brief local reads, file preparation and first path-resolution failure; not separately metered; this is a measured process subtotal rather than an exact cumulative CPU receipt"
  },
  "CPU_receipt_kind": "measured subtotal; brief preparation/path failure not individually metered",
  "previous_binary_global_matrix_exclusion_scope": {
    "report": "research/ddp/breadth_20261027_wave5/binary_route_chart3/REPORT.md",
    "terminal": "research/ddp/breadth_20261027_wave5/binary_route_chart3/terminal.json",
    "exact_scope": "four global inverse-label matrices over F2^3 with every one of 36 reduced three-letter words individually full rank",
    "does_not_exclude": [
      "edge-local binary matrices",
      "multiple-route union coverage",
      "a different binary C30 affine construction",
      "general degree8,D4 five-covers"
    ]
  },
  "terminal": true
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/c30_f2_fivecover_gate/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/c30_f2_fivecover_gate/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/c30_f2_fivecover_gate/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/c30_f2_fivecover_gate/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/c30_f2_fivecover_gate/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/c30_f2_fivecover_gate/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/c30_f2_fivecover_gate/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/c30_f2_fivecover_gate/TERMINAL.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Only the proposed standard F2^3 restriction of the accepted literal GF4/C30 edge-local rule, before any ordinary5cover. Not all binary edge-local maps, alternative embeddings or general8D4 covers.

**仍未完成：** No accepted target graph; broader rules beyond the exact recorded scope remain open.

**启发与重启依据：** Stop this literal-rule transfer. A new actual F2 edge-local chart plus its inverse/direction and source-legality evidence would be required before a five-cover route-count gate; this batch does not search for it.

**单独的重启条件：** Stop this literal-rule transfer. A new actual F2 edge-local chart plus its inverse/direction and source-legality evidence would be required before a five-cover route-count gate; this batch does not search for it.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

