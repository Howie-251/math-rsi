---
type: experiment
node_id: exp:ddp-published-quartic-cayley-census69orders-4d3-d4-20261028
title: "Published complete quartic Cayley census:23619 graphs give no improvement of41/104"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/REPORT.md; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/MODEL_SCOPE.md; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/PREDICTION.json; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/RESULT.json; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/CASES.jsonl; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/MEMBER_RECEIPTS.json; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/INPUT_RECEIPT.json; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/PARSER_CALIBRATION.json; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/filter.py; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/run.py; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/checkpoint.json; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/terminal.json; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/DOWNLOAD_RECEIPT.json; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/INITIAL_BATCH_RECEIPT.json; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/RETRY_110_RECEIPT.json; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/ANALYSIS_SCOPE.md; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/ANALYSIS_SCOPE.json; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/LITERATURE_SCOPE.md; research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/LITERATURE_SCOPE.json"
added: 2026-10-28T01:54:26Z
tags: ["ddp", "method-ledger"]
---

# Published complete quartic Cayley census:23619 graphs give no improvement of41/104

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** published-complete-census-literal-filter

**目标与阶数：** (4,?)；L=不适用／见变体

**距目标的证据：** 23619 source catalogue graphs decoded, all simple4regular and filename-order matched;23619 root0 target-radius failures;0 rootpasses/positive graphs/untested graph records. No negative exact global diameters or ordinary pair counts were computed.

**其他指标（保持原计数类型）：**
```json
{
  "selected_members": 69,
  "complete_members": 69,
  "uncompressed_input_bytes": 9318753,
  "decoded_literal_graphs": 23619,
  "actual_root_radius_traversals": 23619,
  "rootpasses": 0,
  "candidate_graphs": 0,
  "untested_graph_records": 0,
  "negative_globalD": null,
  "ordinary_bad_unordered_pairs": null,
  "old_baseline_allsource_BFS": 0,
  "decoder_adjacency_comparisons": 3,
  "extra_decoder_BFS": 0,
  "network_requests_by_filter": 0,
  "solver_calls": 0,
  "new_lower_bounds": 0,
  "worker_CPU_seconds": 4.182995,
  "driver_CPU_seconds": 0.0016920749999999943,
  "workers": 1
}
```



**从属变体：**
```json
[
  {
    "target_Delta": 4,
    "target_D": 3,
    "savedL": 41,
    "orders": [
      42,
      43,
      44,
      45,
      46,
      47,
      48,
      49,
      50,
      51,
      52,
      53
    ],
    "source_graphs": 671,
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "outcome": "all literal root-target-radius checks fail;0untested"
  },
  {
    "target_Delta": 4,
    "target_D": 4,
    "savedL": 104,
    "orders": [
      105,
      106,
      107,
      108,
      109,
      110,
      111,
      112,
      113,
      114,
      115,
      116,
      117,
      118,
      119,
      120,
      121,
      122,
      123,
      124,
      125,
      126,
      127,
      128,
      129,
      130,
      131,
      132,
      133,
      134,
      135,
      136,
      137,
      138,
      139,
      140,
      141,
      142,
      143,
      144,
      145,
      146,
      147,
      148,
      149,
      150,
      151,
      152,
      153,
      154,
      155,
      156,
      157,
      158,
      159,
      160,
      161
    ],
    "source_graphs": 22948,
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "outcome": "all literal root-target-radius checks fail;0untested"
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/REPORT.md](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/REPORT.md)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/MODEL_SCOPE.md](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/MODEL_SCOPE.md)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/PREDICTION.json](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/PREDICTION.json)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/RESULT.json](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/RESULT.json)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/CASES.jsonl](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/CASES.jsonl)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/MEMBER_RECEIPTS.json](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/MEMBER_RECEIPTS.json)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/INPUT_RECEIPT.json](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/INPUT_RECEIPT.json)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/PARSER_CALIBRATION.json](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/PARSER_CALIBRATION.json)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/filter.py](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/filter.py)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/run.py](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/run.py)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/checkpoint.json](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/checkpoint.json)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/terminal.json](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/radius_filter/terminal.json)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/DOWNLOAD_RECEIPT.json](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/DOWNLOAD_RECEIPT.json)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/INITIAL_BATCH_RECEIPT.json](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/INITIAL_BATCH_RECEIPT.json)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/RETRY_110_RECEIPT.json](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/RETRY_110_RECEIPT.json)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/ANALYSIS_SCOPE.md](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/ANALYSIS_SCOPE.md)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/ANALYSIS_SCOPE.json](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/census_index_access/selected_orders_20261028/ANALYSIS_SCOPE.json)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/LITERATURE_SCOPE.md](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/LITERATURE_SCOPE.md)；[research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/LITERATURE_SCOPE.json](../../research/ddp/more_graphs_20261027/small_d4_D4_C3_times_quarterturn108_20261028/LITERATURE_SCOPE.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Conditional on the published complete connected simple quartic Cayley census through1025: exactly69 complete order members42..53 and105..161, every graph line decoded and filtered. This covers all improved maximum-degree4 Cayley graphs in the(4,3)/(4,4) cells by Moore bounds. Not a new census or a general-graph exclusion.

**仍未完成：** General non-Cayley graphs, other degrees/diameters, and the exact Cayley extrema below41/104 are not decided.

**启发与重启依据：** No further quartic Cayley-group searches can improve the two current bounds if this published complete census is trusted. A future attempt in these cells needs a non-Cayley mechanism, or a concrete error in this inherited census/literal binding. This is not an automatic new-template queue.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

