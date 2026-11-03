---
type: experiment
node_id: exp:ddp-source972-affineblocks-freepaths-buddy-routing-20261027
title: "(13,3)972实际块结构：仿射fix-lines与18P2+6P3+9P4+3P6 free路径"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d13_D3_current972_source/block_geometry_analysis/REPORT.md; research/ddp/more_graphs_20261027/d13_D3_current972_source/block_geometry_analysis/PREDICTION.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/block_geometry_analysis/RESULT.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/block_geometry_analysis/F_COMPONENT_PREDICTION.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/block_geometry_analysis/F_COMPONENT_RESULT.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/block_geometry_analysis/terminal.json; research/ddp/more_graphs_20261027/d13_D3_current972_source/block_geometry_analysis/analyze.py; research/ddp/more_graphs_20261027/d13_D3_current972_source/SOURCE_PROFILE.json"
added: 2026-10-27T21:21:43Z
tags: ["ddp", "method-ledger"]
---

# (13,3)972实际块结构：仿射fix-lines与18P2+6P3+9P4+3P6 free路径

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (13,3)；L=972；known_source_or_recovery n=972

**距目标的证据：** This worker inspected only existing source adjacency; sourceD3 inherited, no distance BFS performed. No new graph was generated.；36/36内部affine、72/72外K3,3平行线均吻合；fixedline横截四kernel。30blocks三free的own-blockR2分割27，6blocks仅21。36P3预测被推翻，实际18P2+6P3+9P4+3P6，未假称新图成功。

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 972,
  "source_m": 6264,
  "blocks": 36,
  "block_size": 27,
  "quotient_degree": 4,
  "quotient_edges": 72,
  "affine_internal_involutions": 36,
  "fixed_line_free_vertices": 108,
  "external_K3_3_relations": 72,
  "free_line_parallel_kernel_orientations": 0,
  "single_free_ownblock_R2": 9,
  "three_free_ownblock_R2_histogram": {
    "27": 30,
    "21": 6
  },
  "ownblock21_ids": [
    1,
    3,
    5,
    7,
    9,
    11
  ],
  "free_graph_edges": 72,
  "free_graph_components": 36,
  "free_component_types": {
    "P2": 18,
    "P3": 6,
    "P4": 9,
    "P6": 3
  },
  "all_P3_prediction": "REFUTED",
  "affine_prediction": "SUPPORTED",
  "ordinary_BFS": 0,
  "R2_balls_or_matrix_recomputed": 0,
  "solver_runs": 0,
  "candidate_graphs": 0,
  "block_CPU_seconds": 0.021839626,
  "free_component_CPU_seconds": 0.004904312000000001,
  "baseline_date": "2026-10-27",
  "source_credit": "Actual current972 author literal already bound by source_scout; this analysis reuses that literal and profile."
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d13_D3_current972_source/block_geometry_analysis/REPORT.md](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/block_geometry_analysis/REPORT.md)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/block_geometry_analysis/PREDICTION.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/block_geometry_analysis/PREDICTION.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/block_geometry_analysis/RESULT.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/block_geometry_analysis/RESULT.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/block_geometry_analysis/F_COMPONENT_PREDICTION.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/block_geometry_analysis/F_COMPONENT_PREDICTION.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/block_geometry_analysis/F_COMPONENT_RESULT.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/block_geometry_analysis/F_COMPONENT_RESULT.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/block_geometry_analysis/terminal.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/block_geometry_analysis/terminal.json)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/block_geometry_analysis/analyze.py](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/block_geometry_analysis/analyze.py)；[research/ddp/more_graphs_20261027/d13_D3_current972_source/SOURCE_PROFILE.json](../../research/ddp/more_graphs_20261027/d13_D3_current972_source/SOURCE_PROFILE.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定actual972的36×27标签和local三进制F3³。只拟合36内部affineinvolution、72个K3,3仿射line关系、free诱导components；无坐标搜索、R2球/全矩阵/LP/MIP/候选。

**仍未完成：** Structural analysis alone neither proves nor excludes a974-vertex cooperative extension. Producer outcomes are in a separate record.

**启发与重启依据：** buddyR1给同一free-path内直接补路，而mainR2可经非free跨组件；两helper≤24pins至少留12组件无pin，其targets仍须两色R2共同覆盖。此结构只解释正在独立求解的联合覆盖，不另开参数/solver。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

