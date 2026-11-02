---
type: experiment
node_id: exp:ddp-polarity13-c3-freeports-threehelpers42-4d3-20261028
title: "Polarity13 cyclic3 lift plus threehelpers: external-target obstruction excludes42 template beforeSAT"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/REPORT.md; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/MODEL_SCOPE.md; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/PREDICTION.json; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ORIGINAL_PREPARATION_PREDICTION.json; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/RESULT.json; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ROUTE_CLASS_CERTIFICATE.json; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/INPUT.json; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/MODEL_STATS.json; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/PREPARATION_RECEIPT.json; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/PREPARATION_NOTE.md; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/VARIABLE_MAP.json; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/REACH2_MAP.json; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/model.cnf; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/compile.py; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/decode.py; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/bind_obstruction.py; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/terminal.json; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ANALYSIS_CONSTRUCTION.md; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ANALYSIS_CONSTRUCTION.json; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ANALYSIS_EXTERNAL_OBSTRUCTION.md; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ANALYSIS_EXTERNAL_OBSTRUCTION.json; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/SOURCE_SCOPE.md; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/SOURCE_SCOPE.json; research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/BASELINE_PRIMARY_RECEIPT.json"
added: 2026-10-28T02:49:06Z
tags: ["ddp", "method-ledger"]
---

# Polarity13 cyclic3 lift plus threehelpers: external-target obstruction excludes42 template beforeSAT

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** prepared-exact-CNF-and-uniform-route-exclusion

**目标与阶数：** (4,3)；L=41；条件性n=42（未据此计纪录）

**距目标的证据：** ExactCNF prepared8436vars/19048clauses but0SAT. Actualbase classesA4/S6/E3 and eachA-to-E one2path. Eachhelper needs>=3directspokes tocover9external targets; P3middle2spokes hascoverage<=6/misses>=3. Any3helpergraph mustmaxdegree1 yetconnectedforD3, contradiction. Uniformlowerbound, not measuredordinarybadpairs.

**其他指标（保持原计数类型）：**
```json
{
  "base_n": 13,
  "base_m": 24,
  "old_lift_n": 39,
  "absolute_ports": 12,
  "helper_count": 3,
  "structural_variables": 138,
  "ternary_shift_assignments": 531441,
  "labeled_port_completions": 831600,
  "structural_assignments": 441946335600,
  "potential_edges": 248,
  "fixed_true_edges": 38,
  "CNF_variables": 8436,
  "CNF_clauses": 19048,
  "CNF_bytes": 272551,
  "successful_compiler_body_CPU_seconds": 0.14176162,
  "route_binding_CPU_seconds": 0.000600980000000001,
  "historical_total_CPU": null,
  "solver_calls": 0,
  "chosen_graphs": 0,
  "graph_BFS": 0,
  "voltage_assignments_enumerated": 0,
  "new_lower_bounds": 0,
  "fixedP3_uniform_external_missing_lowerbound": 3,
  "count_type": "uniform newhelper-to-external target bound; no expandedgraphbadpairs"
}
```





**原始证据：** [research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/REPORT.md](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/REPORT.md)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/MODEL_SCOPE.md](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/MODEL_SCOPE.md)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/PREDICTION.json](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/PREDICTION.json)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ORIGINAL_PREPARATION_PREDICTION.json](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ORIGINAL_PREPARATION_PREDICTION.json)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/RESULT.json](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/RESULT.json)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ROUTE_CLASS_CERTIFICATE.json](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ROUTE_CLASS_CERTIFICATE.json)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/INPUT.json](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/INPUT.json)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/MODEL_STATS.json](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/MODEL_STATS.json)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/PREPARATION_RECEIPT.json](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/PREPARATION_RECEIPT.json)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/PREPARATION_NOTE.md](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/PREPARATION_NOTE.md)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/VARIABLE_MAP.json](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/VARIABLE_MAP.json)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/REACH2_MAP.json](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/REACH2_MAP.json)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/model.cnf](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/model.cnf)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/compile.py](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/compile.py)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/decode.py](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/decode.py)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/bind_obstruction.py](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/bind_obstruction.py)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/terminal.json](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/terminal.json)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ANALYSIS_CONSTRUCTION.md](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ANALYSIS_CONSTRUCTION.md)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ANALYSIS_CONSTRUCTION.json](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ANALYSIS_CONSTRUCTION.json)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ANALYSIS_EXTERNAL_OBSTRUCTION.md](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ANALYSIS_EXTERNAL_OBSTRUCTION.md)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ANALYSIS_EXTERNAL_OBSTRUCTION.json](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/ANALYSIS_EXTERNAL_OBSTRUCTION.json)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/SOURCE_SCOPE.md](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/SOURCE_SCOPE.md)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/SOURCE_SCOPE.json](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/SOURCE_SCOPE.json)；[research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/BASELINE_PRIMARY_RECEIPT.json](../../research/ddp/more_graphs_20261027/small_d4_D3_polarity13_C3_ports42/BASELINE_PRIMARY_RECEIPT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 13-point F3 orthogonal-polarity base, unchanged39-vertex cyclic3 lift, exactly3helpers and any maxdegree4 free-absolute-port completion. The original prepared CNF has fixedhelperP3; a uniform proof excludes even arbitrary3helper internalgraph in this unchangedlift/freeport class. Not all42graphs, otherhelpercounts or changedoldedges.

**仍未完成：** General42-point maxdegree4/D3 graphs and materiallydifferentsource/oldedge/helperrules remain unexcluded.

**启发与重启依据：** Free-port count is insufficient: local geometric target types can require more spokes perhelper than internalconnectivity permits. This fullthreehelper completion class stops before SAT; a future task must actually change the old route structure/helpercount/base, not rerun this CNF or retunevoltages.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

