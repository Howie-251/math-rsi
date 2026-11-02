---
type: experiment
node_id: exp:ddp-f4-3840-all-edge-essential-degree19-thinning-gate-20261101
title: "固定F4/3840图全部38400边有唯一三步见证：保全部顶点纯删边降19严格排除"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/f4_degree19_retained_vertices_gate/PRED.json; research/ddp/two_successful_methods_20261101/f4_degree19_retained_vertices_gate/RESULT.json; research/ddp/two_successful_methods_20261101/f4_degree19_retained_vertices_gate/PROOF.md; research/ddp/two_successful_methods_20261101/f4_degree19_retained_vertices_gate/REPORT.md; research/ddp/two_successful_methods_20261101/f4_degree19_retained_vertices_gate/CONTROLLER_CERTIFICATE.json; research/ddp/two_successful_methods_20261101/f4_degree19_retained_vertices_gate/LITERAL_SINGLE_PAIR_CHECK.json; research/ddp/two_successful_methods_20261101/f4_degree19_retained_vertices_gate/TERMINAL.json; research/ddp/two_successful_methods_20261101/f4_degree19_retained_vertices_gate/check_controller.py; research/ddp/refresh_20261029/f5_d20_edge_criticality_20261029/EDGE_CRITICALITY.md"
added: 2026-11-01T05:59:59Z
tags: ["ddp", "method-ledger"]
---

# 固定F4/3840图全部38400边有唯一三步见证：保全部顶点纯删边降19严格排除

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** controller

**目标与阶数：** (19,3)；L=不适用／见变体

**距目标的证据：** No new candidate graph or diameter measurement. Existing3840/20 source is inherited; only controller routes/ranks and one literal endpoint pair checked.；全部7500控制器三步walk中1260个distance3唯一端点对均actual F4 noise-rank3，覆盖300/300 first-darts；故38400条原无向边每条都被某原顶点对唯一长度≤3路线强制。任意非空纯删边均破坏D3，不能在保3840顶点下删匹配或削到max19。单一字面端点对比对唯一路线PASS，0旧根BFS/solver/新图/Lean，CPU0.063980878。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_Lean_instances": 0,
  "new_general_lemmas": 0,
  "new_lower_bound_mathematically_verified": false,
  "source_n": 3840,
  "source_degree": 20,
  "source_D": 3,
  "controller_vertices": 60,
  "controller_darts": 300,
  "controller_length3_walks": 7500,
  "unique_distance3_pairs": 1260,
  "rank3_unique_pairs": 1260,
  "covered_first_darts": 300,
  "essential_original_undirected_edges": 38400,
  "determinant_histogram": {
    "1": 434,
    "2": 410,
    "3": 416
  },
  "literal_endpoint_pair_checks": 1,
  "source_BFS_roots": 0,
  "solver_calls": 0,
  "Lean_rebuilds": 0,
  "CPU_seconds": 0.063980878,
  "independent_construction_framework_claimed": false,
  "generic_unique_route_lemma_inherited_from_F5": true
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/f4_degree19_retained_vertices_gate/PRED.json](../../research/ddp/two_successful_methods_20261101/f4_degree19_retained_vertices_gate/PRED.json)；[research/ddp/two_successful_methods_20261101/f4_degree19_retained_vertices_gate/RESULT.json](../../research/ddp/two_successful_methods_20261101/f4_degree19_retained_vertices_gate/RESULT.json)；[research/ddp/two_successful_methods_20261101/f4_degree19_retained_vertices_gate/PROOF.md](../../research/ddp/two_successful_methods_20261101/f4_degree19_retained_vertices_gate/PROOF.md)；[research/ddp/two_successful_methods_20261101/f4_degree19_retained_vertices_gate/REPORT.md](../../research/ddp/two_successful_methods_20261101/f4_degree19_retained_vertices_gate/REPORT.md)；[research/ddp/two_successful_methods_20261101/f4_degree19_retained_vertices_gate/CONTROLLER_CERTIFICATE.json](../../research/ddp/two_successful_methods_20261101/f4_degree19_retained_vertices_gate/CONTROLLER_CERTIFICATE.json)；[research/ddp/two_successful_methods_20261101/f4_degree19_retained_vertices_gate/LITERAL_SINGLE_PAIR_CHECK.json](../../research/ddp/two_successful_methods_20261101/f4_degree19_retained_vertices_gate/LITERAL_SINGLE_PAIR_CHECK.json)；[research/ddp/two_successful_methods_20261101/f4_degree19_retained_vertices_gate/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/f4_degree19_retained_vertices_gate/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/f4_degree19_retained_vertices_gate/check_controller.py](../../research/ddp/two_successful_methods_20261101/f4_degree19_retained_vertices_gate/check_controller.py)；[research/ddp/refresh_20261029/f5_d20_edge_criticality_20261029/EDGE_CRITICALITY.md](../../research/ddp/refresh_20261029/f5_d20_edge_criticality_20261029/EDGE_CRITICALITY.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixed accepted3840/20regular original graph, keep every3840 vertex and delete any nonempty subset of original edges only. Excludes pure thinning/perfect-matching deletion. Does not exclude rewiring, deleting vertices, changing charts or general19D3 graphs.

**正向保证：** 1260条唯一distance3 controller路均用实际逐边矩阵计算满rank，不是假设同一chart。；每个300dart都有first-position witness；取任意源坐标与原边noise λ、后两步noise0后，rank3唯一性强制该lifted原边。；进一步删边不会创造新的短路线，因此覆盖任意非空删边集合，而非仅单边测试。

**仍未完成：** 未找到新19D3图，不证明一般19D3无解，不新增Lean。继承不同F5/3750源已知unique-route判据，只检验在实际F4/C60逐边chart源的迁移。

**启发与重启依据：** 预测每个dart都能作唯一远端route首步被1260rank3/300覆盖支持。相邻层pencil冗余不能抵消远端唯一路线义务，停止固定3840顶点纯删边/删matching搜索。真正下一规则须改边重建路线、删点改变义务或换源；这些域未搜索或排除。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

