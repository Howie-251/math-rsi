---
type: experiment
node_id: exp:ddp-wave10-binary1152-edge-local
title: "72控制点×F2⁴的逐边独立仿射线：1152点两起点失败"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave10/binary1152_edge_local/REPORT.md; research/ddp/breadth_20261027_wave10/binary1152_edge_local/terminal.json; research/ddp/breadth_20261027_wave10/binary1152_edge_local/search_result.json; research/ddp/breadth_20261027_wave10/binary1152_edge_local/best.edges; research/ddp/breadth_20261027_wave10/binary1152_edge_local/best_parameters.json; research/ddp/breadth_20261027_wave10/binary1152_edge_local/best.independent_check.json; research/ddp/breadth_20261027_wave10/binary1152_edge_local/capacity_screen.json; research/ddp/breadth_20261027_wave10/binary1152_edge_local/encoding_and_plan.json; research/ddp/breadth_20261027_wave10/binary1152_edge_local/search.cpp; research/ddp/breadth_20261027_wave10/binary1152_edge_local/run.py"
added: 2026-10-27T07:58:08Z
tags: ["ddp", "method-ledger"]
---

# 72控制点×F2⁴的逐边独立仿射线：1152点两起点失败

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (8,4)；L=1100；candidate_graph_or_family n=1152；条件性n=1152（未据此计纪录）

**距目标的证据：** 实际D=5，目标D=4；普通无序坏对=29152；root_independent_all1152_source_ordinary_BFS；完整1152点4608边图simple、connected、8regular；root唯一全1152源BFS确认D5、29152个距离>4无序点对。144条参数反关系逐项合法，参数重建全部4608边与保存best.edges完全匹配。

**其他指标（保持原计数类型）：**
```json
{
  "object_level": "finalgraph",
  "graph_generated": true,
  "graph_edges": 4608,
  "source_controller_vertices": 72,
  "source_controller_degree": 4,
  "fiber_size": 16,
  "field": 2,
  "fiber_dimension": 4,
  "independent_edge_parameters": 144,
  "starts": 2,
  "legal_proposals": 2000,
  "profiles": [
    {
      "seed": 20261027115201,
      "initial_bad": 30240,
      "best_bad": 29152,
      "final_bad": 29152,
      "legal_proposals": 1000,
      "accepted": 548,
      "move_counts_b_c_T": [
        329,
        305,
        366
      ]
    },
    {
      "seed": 20261027115202,
      "initial_bad": 68142,
      "best_bad": 31436,
      "final_bad": 31436,
      "legal_proposals": 1000,
      "accepted": 554,
      "move_counts_b_c_T": [
        345,
        336,
        319
      ]
    }
  ],
  "first_formal_proposal_calibrated": true,
  "all144_inverse_maps_verified": true,
  "parameters_reconstruct_edges": true,
  "whole_graph_all_pairs_BFS_performed": true,
  "roots_checked": 1152,
  "unordered_distance_histogram": {
    "1": 4608,
    "2": 29912,
    "3": 173952,
    "4": 425352,
    "5": 29152
  },
  "production_total_CPU_seconds": 2.106693456,
  "root_check_CPU_seconds": 0.38950397400000003,
  "producer_BFS_performed": false,
  "pending_root_check": false
}
```





**原始证据：** [research/ddp/breadth_20261027_wave10/binary1152_edge_local/REPORT.md](../../research/ddp/breadth_20261027_wave10/binary1152_edge_local/REPORT.md)；[research/ddp/breadth_20261027_wave10/binary1152_edge_local/terminal.json](../../research/ddp/breadth_20261027_wave10/binary1152_edge_local/terminal.json)；[research/ddp/breadth_20261027_wave10/binary1152_edge_local/search_result.json](../../research/ddp/breadth_20261027_wave10/binary1152_edge_local/search_result.json)；[research/ddp/breadth_20261027_wave10/binary1152_edge_local/best.edges](../../research/ddp/breadth_20261027_wave10/binary1152_edge_local/best.edges)；[research/ddp/breadth_20261027_wave10/binary1152_edge_local/best_parameters.json](../../research/ddp/breadth_20261027_wave10/binary1152_edge_local/best_parameters.json)；[research/ddp/breadth_20261027_wave10/binary1152_edge_local/best.independent_check.json](../../research/ddp/breadth_20261027_wave10/binary1152_edge_local/best.independent_check.json)；[research/ddp/breadth_20261027_wave10/binary1152_edge_local/capacity_screen.json](../../research/ddp/breadth_20261027_wave10/binary1152_edge_local/capacity_screen.json)；[research/ddp/breadth_20261027_wave10/binary1152_edge_local/encoding_and_plan.json](../../research/ddp/breadth_20261027_wave10/binary1152_edge_local/encoding_and_plan.json)；[research/ddp/breadth_20261027_wave10/binary1152_edge_local/search.cpp](../../research/ddp/breadth_20261027_wave10/binary1152_edge_local/search.cpp)；[research/ddp/breadth_20261027_wave10/binary1152_edge_local/run.py](../../research/ddp/breadth_20261027_wave10/binary1152_edge_local/run.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定72点简单4regular控制图；144条无向边各独立GL4(2)矩阵、非零b和任意affine offset c，GF2反边重新求逆；两预定初态各1000合法单边b/c/transvection proposals，无额外controller/field/move/seed。

**正向保证：** 控制点每个四邻cell，每方向binary line给两个不同邻点，因此任意合法边参数均给简单8regular1152图。；全部72×72端点的≤4walk加权容量均≥16（min16），只过必要筛，不保证存在可行参数。；首正式proposal以全部5392512条≤4walk逐位核对全部R4关系MATCH，正式提案复用；不充当最终独立BFS。

**仍未完成：** 最好图仍有29152个>4无序点对，实际直径比目标多1；只结束两段profile，不排全部逐边参数族或一般(8,4)图。

**启发与重启依据：** 独立GF2逐边逆矩阵/offset确实放松旧通用four-label chart限制，但容量和近端合法性不保证全对R4。此固定批已停，不追加move/seed/budget，重启须新的覆盖结构依据。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

