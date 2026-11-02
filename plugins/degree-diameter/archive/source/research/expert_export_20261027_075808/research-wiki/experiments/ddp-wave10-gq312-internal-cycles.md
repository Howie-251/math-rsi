---
type: experiment
node_id: exp:ddp-wave10-gq312-internal-cycles
title: "W(3,5)关联图加两侧独立2factor：312点八度D3目标失败"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave10/gq312_internal_cycles/REPORT.md; research/ddp/breadth_20261027_wave10/gq312_internal_cycles/terminal.json; research/ddp/breadth_20261027_wave10/gq312_internal_cycles/search_result.json; research/ddp/breadth_20261027_wave10/gq312_internal_cycles/best.edges; research/ddp/breadth_20261027_wave10/gq312_internal_cycles/best_parameters.json; research/ddp/breadth_20261027_wave10/gq312_internal_cycles/best.factors.json; research/ddp/breadth_20261027_wave10/gq312_internal_cycles/best.independent_check.json; research/ddp/breadth_20261027_wave10/gq312_internal_cycles/geometry.json; research/ddp/breadth_20261027_wave10/gq312_internal_cycles/incidence.edges; research/ddp/breadth_20261027_wave10/gq312_internal_cycles/first_proposal_calibration.json; research/ddp/breadth_20261027_wave10/gq312_internal_cycles/generate.py; research/ddp/breadth_20261027_wave10/gq312_internal_cycles/search.cpp; research/ddp/breadth_20261027_wave10/gq312_internal_cycles/run.py"
added: 2026-10-27T07:58:08Z
tags: ["ddp", "method-ledger"]
---

# W(3,5)关联图加两侧独立2factor：312点八度D3目标失败

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (8,3)；L=253；candidate_graph_or_family n=312；条件性n=312（未据此计纪录）

**距目标的证据：** 实际D=4，目标D=3；普通无序坏对=4090；root_independent_all312_source_ordinary_BFS；完整312点1248边图simple、connected、8regular；root唯一全312源BFS确认D4，4090个>3无序坏对，与production精确R3评分一致。936旧incidence和两侧各156条factor边完全匹配，所有内部度2。

**其他指标（保持原计数类型）：**
```json
{
  "object_level": "finalgraph",
  "graph_generated": true,
  "graph_edges": 1248,
  "field": 5,
  "symplectic_dimension": 4,
  "points": 156,
  "lines": 156,
  "incidence_edges": 936,
  "incidence_degree": 6,
  "internal_factor_edges_each": 156,
  "internal_degree": 2,
  "starts": 2,
  "legal_proposals": 2000,
  "profiles": [
    {
      "start": 0,
      "seed": 20261027103121,
      "initial_bad": 4721,
      "final_bad": 4090,
      "raw": 1027,
      "legal": 1000,
      "illegal_rejects": 27,
      "accepted": 485,
      "strict_improvements": 268
    },
    {
      "start": 1,
      "seed": 20261027103122,
      "initial_bad": 4834,
      "final_bad": 4098,
      "raw": 1021,
      "legal": 1000,
      "illegal_rejects": 21,
      "accepted": 471,
      "strict_improvements": 252
    }
  ],
  "first_formal_proposal_calibrated": true,
  "all936_incidence_edges_retained": true,
  "exactly156_edges_in_each_factor": true,
  "whole_graph_all_pairs_BFS_performed": true,
  "roots_checked": 312,
  "unordered_distance_histogram": {
    "1": 1248,
    "2": 8438,
    "3": 34740,
    "4": 4090
  },
  "production_total_CPU_seconds": 1.8563930249999998,
  "root_check_CPU_seconds": 0.036682278000000006,
  "producer_BFS_performed": false,
  "pending_root_check": false
}
```





**原始证据：** [research/ddp/breadth_20261027_wave10/gq312_internal_cycles/REPORT.md](../../research/ddp/breadth_20261027_wave10/gq312_internal_cycles/REPORT.md)；[research/ddp/breadth_20261027_wave10/gq312_internal_cycles/terminal.json](../../research/ddp/breadth_20261027_wave10/gq312_internal_cycles/terminal.json)；[research/ddp/breadth_20261027_wave10/gq312_internal_cycles/search_result.json](../../research/ddp/breadth_20261027_wave10/gq312_internal_cycles/search_result.json)；[research/ddp/breadth_20261027_wave10/gq312_internal_cycles/best.edges](../../research/ddp/breadth_20261027_wave10/gq312_internal_cycles/best.edges)；[research/ddp/breadth_20261027_wave10/gq312_internal_cycles/best_parameters.json](../../research/ddp/breadth_20261027_wave10/gq312_internal_cycles/best_parameters.json)；[research/ddp/breadth_20261027_wave10/gq312_internal_cycles/best.factors.json](../../research/ddp/breadth_20261027_wave10/gq312_internal_cycles/best.factors.json)；[research/ddp/breadth_20261027_wave10/gq312_internal_cycles/best.independent_check.json](../../research/ddp/breadth_20261027_wave10/gq312_internal_cycles/best.independent_check.json)；[research/ddp/breadth_20261027_wave10/gq312_internal_cycles/geometry.json](../../research/ddp/breadth_20261027_wave10/gq312_internal_cycles/geometry.json)；[research/ddp/breadth_20261027_wave10/gq312_internal_cycles/incidence.edges](../../research/ddp/breadth_20261027_wave10/gq312_internal_cycles/incidence.edges)；[research/ddp/breadth_20261027_wave10/gq312_internal_cycles/first_proposal_calibration.json](../../research/ddp/breadth_20261027_wave10/gq312_internal_cycles/first_proposal_calibration.json)；[research/ddp/breadth_20261027_wave10/gq312_internal_cycles/generate.py](../../research/ddp/breadth_20261027_wave10/gq312_internal_cycles/generate.py)；[research/ddp/breadth_20261027_wave10/gq312_internal_cycles/search.cpp](../../research/ddp/breadth_20261027_wave10/gq312_internal_cycles/search.cpp)；[research/ddp/breadth_20261027_wave10/gq312_internal_cycles/run.py](../../research/ddp/breadth_20261027_wave10/gq312_internal_cycles/run.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** GF5四维symplectic W(3,5)的156点/156线，保留936关联边；两个156点侧各加入任意简单2factor。只两固定随机Hamilton初态，各1000合法two-edge switch，后续可分裂/合并cycle，不固定Hamilton。

**正向保证：** GF5 symplectic空间给156点/156条全等方线，每点/线关联度6；加每侧degree2因子后全度8。；全部原incidence边保留，原来≤3的cross-side路和同侧collinear两步路不失效；需修复非共线same-side远端。；几何metadata逐项确认非incident point-line的唯一collinear投影；必要几何关系不代替最终全对D检查。

**仍未完成：** 最好图仍有4090个距离4无序点对，目标D3未达；有限2000合法交换失败，不排除全部两侧2factor或一般312点图。

**启发与重启依据：** 关联几何严格保留大批近端/cross覆盖，独立2factor改变same-side远端路由，但该两起点未闭。停止固定批，不增q/field/source/degree/轮次；未来须明确新的same-side覆盖结构。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

