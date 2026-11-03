---
type: experiment
node_id: exp:ddp-michel72-split-edge73-endpoint-gate-20261028
title: "Michel geometric72 split-edge73: all720 partitions have no eligible endpoint on either side"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/REPORT.md; research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/SOURCE_ELIGIBILITY_PRED.json; research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/SOURCE_ELIGIBILITY_REPORT.md; research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/SOURCE_ELIGIBILITY_RESULT.json; research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/SOURCE_CLOSED_R2.json; research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/SOURCE_ELIGIBILITY_TERMINAL.json; research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/source/PROVENANCE.json; research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/source/SOURCE_NOTES.md; research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/source/OFFICIAL_72_deg5D3_SageMath.txt; research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/source/michel72.s6; research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/source/source72.edges; research/ddp/more_graphs_20261027/small_d5_D3_exoo72_split_edge73/ANALYSIS_COVERAGE.md; research/ddp/more_graphs_20261027/small_d5_D3_exoo72_split_edge73/ANALYSIS_COVERAGE.json"
added: 2026-10-28T04:21:02Z
tags: ["ddp", "method-ledger"]
---

# Michel geometric72 split-edge73: all720 partitions have no eligible endpoint on either side

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (5,3)；L=72；条件性n=73（未据此计纪录）

**距目标的证据：** 全部720分割均X_A=X_B=空；95040次端点R2位集包含测试，无一个端点能修任一child所缺整类旧距离3目标。因此0合法联合端点边，固定clean split+absorbed-edge规则严格失败。CPU0.027586116；0候选图、候选边参数枚举、source/candidate BFS或solver。

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 72,
  "source_m": 180,
  "source_degree": 5,
  "source_reported_D": 3,
  "source_author": "Michel de Messieres",
  "source_author_date": "2026-10-13",
  "source_record": "https://doi.org/10.5281/zenodo.23510655",
  "source_literal_bytes_downloaded": 6354,
  "source_literal_decoding_only": true,
  "canonical_partitions": 720,
  "eligible_endpoints_per_side_per_partition": 66,
  "endpoint_mask_subset_tests": 95040,
  "both_sides_empty_partitions": 720,
  "partitions_with_joint_eligible_edge": 0,
  "candidate_edge_parameters_enumerated": 0,
  "closed_R2_ball_size_histogram": {
    "24": 36,
    "25": 36
  },
  "CPU_seconds": 0.027586115999999994,
  "candidate_graphs": 0,
  "source_D3_BFS": 0,
  "candidate_BFS": 0,
  "solver_calls": 0,
  "new_lower_bound_mathematically_verified": false,
  "new_independent_method_count": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/REPORT.md](../../research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/REPORT.md)；[research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/SOURCE_ELIGIBILITY_PRED.json](../../research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/SOURCE_ELIGIBILITY_PRED.json)；[research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/SOURCE_ELIGIBILITY_REPORT.md](../../research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/SOURCE_ELIGIBILITY_REPORT.md)；[research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/SOURCE_ELIGIBILITY_RESULT.json](../../research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/SOURCE_ELIGIBILITY_RESULT.json)；[research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/SOURCE_CLOSED_R2.json](../../research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/SOURCE_CLOSED_R2.json)；[research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/SOURCE_ELIGIBILITY_TERMINAL.json](../../research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/SOURCE_ELIGIBILITY_TERMINAL.json)；[research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/source/PROVENANCE.json](../../research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/source/PROVENANCE.json)；[research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/source/SOURCE_NOTES.md](../../research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/source/SOURCE_NOTES.md)；[research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/source/OFFICIAL_72_deg5D3_SageMath.txt](../../research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/source/OFFICIAL_72_deg5D3_SageMath.txt)；[research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/source/michel72.s6](../../research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/source/michel72.s6)；[research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/source/source72.edges](../../research/ddp/more_graphs_20261027/small_d5_D3_michel72_split_edge73/source/source72.edges)；[research/ddp/more_graphs_20261027/small_d5_D3_exoo72_split_edge73/ANALYSIS_COVERAGE.md](../../research/ddp/more_graphs_20261027/small_d5_D3_exoo72_split_edge73/ANALYSIS_COVERAGE.md)；[research/ddp/more_graphs_20261027/small_d5_D3_exoo72_split_edge73/ANALYSIS_COVERAGE.json](../../research/ddp/more_graphs_20261027/small_d5_D3_exoo72_split_edge73/ANALYSIS_COVERAGE.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定官方Michel de Messieres几何72点/180边/全5正则D3源，区别于旧Exoo72。每个v将完整N(v)分A2/B3并连相邻children；仅考虑删一条两端outside closedN[v]的旧边xy，再各加u-x,w-y。全部72*C(5,2)=720分割做原源端点覆盖必要门，不生成73图。

**正向保证：** 官方primary脚本给出完整michel72 sparse6，直接解码确认为72点、180边、简单5正则；D3及与Exoo非同构继承官方说明。；精确child门E_A subset closedR2_G(x)、E_B subset closedR2_G(y)继承已审数学证明；它是本源上的必要条件，未把旧Exoo数值迁移。；全部72个closedR2由邻接两层并集一次取得，球大小24或25各36个；720分割和66个候选端点每侧均完整检查。

**仍未完成：** 仅排该Michel72源上endpoint outside closedN[v]的2+3 split加一条吸收边；其它端点域、更多cut/helper、其它源和一般73点max5/D3图未排。

**启发与重启依据：** 整类缺路必须先有可覆盖端点，再考虑释放旧边；同scope两侧均无端点时不应展开73图或solver。此为既有插点家族的新actual-source变式，独立方法增量0；不续本源预算、换seed或追坏对。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

