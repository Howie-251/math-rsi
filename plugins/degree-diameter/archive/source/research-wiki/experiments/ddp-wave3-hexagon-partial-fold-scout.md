---
type: experiment
node_id: exp:ddp-wave3-hexagon-partial-fold-scout
title: "H9任意split/copy/twin定理与逐点witness恢复"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/THEOREM_SCOPE_REVIEW.md; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/REPORT.md; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/22907863_README.md; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/22907863_large-graphs-diameter-five-duality-order-four-split-cayley-hexagon-H9.txt; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/23056128_README.md; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/23056128_partial-folds-split-cayley-hexagon-H9-large-graphs-diameter-five.txt; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/Q_data.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/duality_source/graph_d10k5_n33397.edges.xz; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/duality_source/graph_d10k5_n33397_regular.edges.xz; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/duality_source/graph_d11k5_n35203.edges.xz; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/duality_source/graph_d12k5_n38167.edges.xz; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/duality_source/tau.txt.xz; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/graph_d11k5_n36563.edges.xz; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/graph_d12k5_n41699.edges.xz; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/graph_d13k5_n50750.edges.xz; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/tau.txt.xz; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/witnesses/pf_d11_k5_n36563.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/witnesses/pf_d12_k5_n41699.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/witnesses/pf_d13_k5_n50750.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/structure_check.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/witness12_state.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/zenodo_22907863.json; research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/zenodo_23056128.json"
added: 2026-10-27T08:25:51Z
tags: ["ddp", "method-ledger"]
---

# H9任意split/copy/twin定理与逐点witness恢复

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (12,5)；L=42342

**距目标的证据：** V/E与degree公式恢复；原witness S7959+copies280+twins63=41699，非新record。

**其他指标（保持原计数类型）：**
```json
{
  "known_author_n": 41699,
  "known_core_n": 41636,
  "Q_vertices": 33033,
  "H3_vertices": 364,
  "target_core_gain": 707,
  "source_known_D_upper_bound": 5
}
```





**原始证据：** [research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/THEOREM_SCOPE_REVIEW.md](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/THEOREM_SCOPE_REVIEW.md)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/REPORT.md](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/REPORT.md)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/22907863_README.md](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/22907863_README.md)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/22907863_large-graphs-diameter-five-duality-order-four-split-cayley-hexagon-H9.txt](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/22907863_large-graphs-diameter-five-duality-order-four-split-cayley-hexagon-H9.txt)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/23056128_README.md](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/23056128_README.md)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/23056128_partial-folds-split-cayley-hexagon-H9-large-graphs-diameter-five.txt](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/23056128_partial-folds-split-cayley-hexagon-H9-large-graphs-diameter-five.txt)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/Q_data.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/Q_data.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/duality_source/graph_d10k5_n33397.edges.xz](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/duality_source/graph_d10k5_n33397.edges.xz)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/duality_source/graph_d10k5_n33397_regular.edges.xz](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/duality_source/graph_d10k5_n33397_regular.edges.xz)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/duality_source/graph_d11k5_n35203.edges.xz](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/duality_source/graph_d11k5_n35203.edges.xz)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/duality_source/graph_d12k5_n38167.edges.xz](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/duality_source/graph_d12k5_n38167.edges.xz)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/duality_source/tau.txt.xz](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/duality_source/tau.txt.xz)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/graph_d11k5_n36563.edges.xz](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/graph_d11k5_n36563.edges.xz)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/graph_d12k5_n41699.edges.xz](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/graph_d12k5_n41699.edges.xz)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/graph_d13k5_n50750.edges.xz](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/graph_d13k5_n50750.edges.xz)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/tau.txt.xz](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/tau.txt.xz)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/witnesses/pf_d11_k5_n36563.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/witnesses/pf_d11_k5_n36563.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/witnesses/pf_d12_k5_n41699.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/witnesses/pf_d12_k5_n41699.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/witnesses/pf_d13_k5_n50750.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/witnesses/pf_d13_k5_n50750.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/structure_check.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/structure_check.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/witness12_state.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/witness12_state.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/zenodo_22907863.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/zenodo_22907863.json)；[research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/zenodo_23056128.json](../../research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/zenodo_23056128.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 原H9/duality与部分折叠作者资料；已有41699成品的局部结构恢复

**正向保证：** 点到线≤5奇路径投影给任意合法S/c的D≤5；H3完整blowup和旧邻居twins保留D≤5

**仍未完成：** 原PSL/PΓL轨道作用未恢复，后续pencil邻接/证明缺失；未做大BFS。

**启发与重启依据：** 已有逐点Q数据足够解除轨道常值约束，无需换群。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

