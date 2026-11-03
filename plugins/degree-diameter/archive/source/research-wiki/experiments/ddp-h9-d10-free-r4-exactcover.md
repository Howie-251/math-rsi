---
type: experiment
node_id: exp:ddp-h9-d10-free-r4-exactcover
title: "(10,5)364余量点覆盖：四支严格界、余一支RAW不可行，未出新图"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/h9_other_degrees/degree10_exact_cover/REPORT.md; research/ddp/more_graphs_20261027/h9_other_degrees/degree10_exact_cover/RESULT.json; research/ddp/more_graphs_20261027/h9_other_degrees/degree10_exact_cover/symmetry/REPORT.md; research/ddp/more_graphs_20261027/h9_other_degrees/degree10_exact_cover/symmetry_g2_root/REPORT.md; research/ddp/more_graphs_20261027/h9_other_degrees/degree10_exact_cover/symmetry_cases/REPORT.md; research/ddp/more_graphs_20261027/h9_degree10_two_vertex_block/REPORT.md"
added: 2026-10-27T12:06:15Z
tags: ["ddp", "method-ledger"]
---

# (10,5)364余量点覆盖：四支严格界、余一支RAW不可行，未出新图

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-coverage-model-no-final-graph

**目标与阶数：** (10,5)；L=33397；条件性n=33398（未据此计纪录）

**距目标的证据：** 原LP9.036789；已验证5轨道无损分支，四支整数dual严格排除；case0 LP9.985499、唯一MIP报告Infeasible但无可信proof，整个单点族不作严格排除。无新图。另行转两相邻新点互助块，未得完整候选前不算新纪录。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs_generated": 0,
  "original_spare_vertices": 364,
  "original_target_rows": 33397,
  "deduplicated_cover_rows": 26117,
  "LP_objective": 9.036789297658839,
  "original_model_MIP_result": "UNKNOWN_NO_INCUMBENT",
  "original_LP_MIP_CPU_seconds": 116.546768,
  "integer_dual_numerator": 9036606,
  "integer_dual_denominator": 1000000,
  "integer_pins_lower_bound": 10,
  "SL3_plus_J_candidates": 5617,
  "old_symmetry_pin_orbits": 192,
  "verified_new_pin_orbit_sizes": [
    84,
    84,
    28,
    84,
    84
  ],
  "new_case_count": 5,
  "family_excluded": false,
  "five_cases_processed": true,
  "strict_integer_dual_cases": 4,
  "uncertified_MIP_infeasible_cases": 1,
  "whole_family_excluded": false,
  "two_vertex_block_status": "UNKNOWN_HARD_CPU_LIMIT_NO_RETURNED_INCUMBENT",
  "two_vertex_block_LP": 16.147239263803808,
  "two_vertex_block_new_graphs": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/h9_other_degrees/degree10_exact_cover/REPORT.md](../../research/ddp/more_graphs_20261027/h9_other_degrees/degree10_exact_cover/REPORT.md)；[research/ddp/more_graphs_20261027/h9_other_degrees/degree10_exact_cover/RESULT.json](../../research/ddp/more_graphs_20261027/h9_other_degrees/degree10_exact_cover/RESULT.json)；[research/ddp/more_graphs_20261027/h9_other_degrees/degree10_exact_cover/symmetry/REPORT.md](../../research/ddp/more_graphs_20261027/h9_other_degrees/degree10_exact_cover/symmetry/REPORT.md)；[research/ddp/more_graphs_20261027/h9_other_degrees/degree10_exact_cover/symmetry_g2_root/REPORT.md](../../research/ddp/more_graphs_20261027/h9_other_degrees/degree10_exact_cover/symmetry_g2_root/REPORT.md)；[research/ddp/more_graphs_20261027/h9_other_degrees/degree10_exact_cover/symmetry_cases/REPORT.md](../../research/ddp/more_graphs_20261027/h9_other_degrees/degree10_exact_cover/symmetry_cases/REPORT.md)；[research/ddp/more_graphs_20261027/h9_degree10_two_vertex_block/REPORT.md](../../research/ddp/more_graphs_20261027/h9_degree10_two_vertex_block/REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixed unregularF33397: every one-vertex monotone augmentation has pins among the364 H3 sparevertices. Full R4-covering Booleanmodel with cardinality<=10; 26117 deduplicated targetrows.

**正向保证：** 364个sparepoints的R4并集确实覆盖全部33397，≤10是否足够仍开放。；五轨道[84,84,28,84,84]来自全26117行保持的实际列置换；固定首个被选轨道代表、前面轨道置零的五分支无损。

**仍未完成：** N10仍无新下界；单点case0未可信认证，两点互助块LP允许但唯一MIP窗口无返回候选，UNKNOWN不排除该族。

**启发与重启依据：** 不原样延长旧MIP；只因已验证新的对称性约束才开展一次有限分支检验。分支未解决继续保留原可行性，不以小坏对下降续算。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

