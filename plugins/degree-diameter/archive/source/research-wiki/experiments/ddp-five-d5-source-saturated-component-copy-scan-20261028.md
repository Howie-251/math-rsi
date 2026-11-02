---
type: experiment
node_id: exp:ddp-five-d5-source-saturated-component-copy-scan-20261028
title: "Five D5 sources: all complete saturated components fail copy-capacity and size/exit gates"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/PREDICTION.json; research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/RESULT.json; research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/REPORT.md; research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/SOURCE_PROFILES.jsonl; research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/COMPONENTS_D11.jsonl; research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/COMPONENTS_D12.jsonl; research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/COMPONENTS_D13.jsonl; research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/COMPONENTS_D14.jsonl; research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/COMPONENTS_D15.jsonl; research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/TERMINAL.json; research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/scan.cpp; research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/run.py; research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/inputs.txt; research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/ANALYSIS_PROOF.md; research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/ANALYSIS_PROOF.json; research/ddp/more_graphs_20261027/h9_paired_full_neighborhood_clone_rule/BINDING_RESULT.json"
added: 2026-10-28T04:49:54Z
tags: ["ddp", "method-ledger"]
---

# Five D5 sources: all complete saturated components fail copy-capacity and size/exit gates

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** complete-saturated-component-copy-rule-eligibility-test

**目标与阶数：** 多目标：变体→[11, 5]／L=37628；变体→[12, 5]／L=42342；变体→[13, 5]／L=51417；变体→[14, 5]／L=94186；变体→[15, 5]／L=102060（逐变体，不合成一个距离）

**距目标的证据：** 五源各仅1个giant饱和component，size依次35160/28545/38333/90501/101250；五者均同时失败boundary容量、每点外邻和diam3 Moore-size必要门。eligible0，internalR3根0、R4/BFS/solver/graph均0。worker0.274693CPU，含compile总1.557719699CPU。

**其他指标（保持原计数类型）：**
```json
{
  "sources_complete": 5,
  "saturated_components_complete": 5,
  "component_sizes": [
    35160,
    28545,
    38333,
    90501,
    101250
  ],
  "capacity_fail_components": 5,
  "exit_fail_components": 5,
  "Moore_size_fail_components": 5,
  "eligible_components": 0,
  "internal_R3_roots": 0,
  "R4_calls": 0,
  "source_D5_BFS": 0,
  "solver_calls": 0,
  "new_graphs": 0,
  "worker_CPU_seconds": 0.274693,
  "aggregate_CPU_seconds": 1.5577196990000002,
  "new_lower_bound_mathematically_verified": false,
  "same_neighborhood_mechanism_variant": true
}
```



**从属变体：**
```json
[
  {
    "Delta": 11,
    "source_n": 37631,
    "source_m": 205329,
    "saturated_vertices": 35160,
    "total_components": 1,
    "components_examined": 1,
    "capacity_fail_components": 1,
    "exit_fail_components": 1,
    "Moore_size_fail_components": 1,
    "necessary_gate_pass_components": 0,
    "internal_R3_fail_components": 0,
    "internal_R3_roots": 0,
    "eligible_components": 0,
    "component_size_histogram": {
      "35160": 1
    },
    "target_Delta": 11,
    "target_D": 5,
    "target": [
      11,
      5
    ],
    "savedL": 37628,
    "n": {
      "actual": null,
      "hypothetical": 72791
    }
  },
  {
    "Delta": 12,
    "source_n": 42402,
    "source_m": 245937,
    "saturated_vertices": 28545,
    "total_components": 1,
    "components_examined": 1,
    "capacity_fail_components": 1,
    "exit_fail_components": 1,
    "Moore_size_fail_components": 1,
    "necessary_gate_pass_components": 0,
    "internal_R3_fail_components": 0,
    "internal_R3_roots": 0,
    "eligible_components": 0,
    "component_size_histogram": {
      "28545": 1
    },
    "target_Delta": 12,
    "target_D": 5,
    "target": [
      12,
      5
    ],
    "savedL": 42342,
    "n": {
      "actual": null,
      "hypothetical": 70947
    }
  },
  {
    "Delta": 13,
    "source_n": 51457,
    "source_m": 324863,
    "saturated_vertices": 38333,
    "total_components": 1,
    "components_examined": 1,
    "capacity_fail_components": 1,
    "exit_fail_components": 1,
    "Moore_size_fail_components": 1,
    "necessary_gate_pass_components": 0,
    "internal_R3_fail_components": 0,
    "internal_R3_roots": 0,
    "eligible_components": 0,
    "component_size_histogram": {
      "38333": 1
    },
    "target_Delta": 13,
    "target_D": 5,
    "target": [
      13,
      5
    ],
    "savedL": 51417,
    "n": {
      "actual": null,
      "hypothetical": 89790
    }
  },
  {
    "Delta": 14,
    "source_n": 94186,
    "source_m": 657452,
    "saturated_vertices": 90501,
    "total_components": 1,
    "components_examined": 1,
    "capacity_fail_components": 1,
    "exit_fail_components": 1,
    "Moore_size_fail_components": 1,
    "necessary_gate_pass_components": 0,
    "internal_R3_fail_components": 0,
    "internal_R3_roots": 0,
    "eligible_components": 0,
    "component_size_histogram": {
      "90501": 1
    },
    "target_Delta": 14,
    "target_D": 5,
    "target": [
      14,
      5
    ],
    "savedL": 94186,
    "n": {
      "actual": null,
      "hypothetical": 184687
    }
  },
  {
    "Delta": 15,
    "source_n": 102060,
    "source_m": 765045,
    "saturated_vertices": 101250,
    "total_components": 1,
    "components_examined": 1,
    "capacity_fail_components": 1,
    "exit_fail_components": 1,
    "Moore_size_fail_components": 1,
    "necessary_gate_pass_components": 0,
    "internal_R3_fail_components": 0,
    "internal_R3_roots": 0,
    "eligible_components": 0,
    "component_size_histogram": {
      "101250": 1
    },
    "target_Delta": 15,
    "target_D": 5,
    "target": [
      15,
      5
    ],
    "savedL": 102060,
    "n": {
      "actual": null,
      "hypothetical": 203310
    }
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/PREDICTION.json](../../research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/PREDICTION.json)；[research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/RESULT.json](../../research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/RESULT.json)；[research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/REPORT.md](../../research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/REPORT.md)；[research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/SOURCE_PROFILES.jsonl](../../research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/SOURCE_PROFILES.jsonl)；[research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/COMPONENTS_D11.jsonl](../../research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/COMPONENTS_D11.jsonl)；[research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/COMPONENTS_D12.jsonl](../../research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/COMPONENTS_D12.jsonl)；[research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/COMPONENTS_D13.jsonl](../../research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/COMPONENTS_D13.jsonl)；[research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/COMPONENTS_D14.jsonl](../../research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/COMPONENTS_D14.jsonl)；[research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/COMPONENTS_D15.jsonl](../../research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/COMPONENTS_D15.jsonl)；[research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/TERMINAL.json](../../research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/TERMINAL.json)；[research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/scan.cpp](../../research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/scan.cpp)；[research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/run.py](../../research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/run.py)；[research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/inputs.txt](../../research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/inputs.txt)；[research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/ANALYSIS_PROOF.md](../../research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/ANALYSIS_PROOF.md)；[research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/ANALYSIS_PROOF.json](../../research/ddp/more_graphs_20261027/h9_saturated_component_copy_scan/ANALYSIS_PROOF.json)；[research/ddp/more_graphs_20261027/h9_paired_full_neighborhood_clone_rule/BINDING_RESULT.json](../../research/ddp/more_graphs_20261027/h9_paired_full_neighborhood_clone_rule/BINDING_RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 五个固定D5现图37631/cap11、42402/cap12、51457/cap13、94186/cap14、102060/cap15；一次完整扫描每个饱和诱导图连通component C，只允许完整复制C及其全部旧外边界、旧边全保留。充分证书要求induced internaldiam<=3、每c有外邻及所有外vertex的新增负载<=实际余量。

**正向保证：** The component-copy lemma gives fullD5 without graph-distance search when its load/exit/internal-diameter hypotheses hold.；All actual saturated vertices are covered by the complete component enumeration; this is not a k-by-k subset search.

**仍未完成：** Other adjacency rules,unsaturated subsets,changedsource or other multi-helper mechanisms.

**启发与重启依据：** 组件复制充分规则有效，容量必须按整个component的多重边界负载核；稀少satN1叶不意味着孤立P3。完整component首门已全拒，本批不续unsaturated C或size阶梯。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

