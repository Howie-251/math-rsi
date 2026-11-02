---
type: experiment
node_id: exp:ddp-20400-six-wl-aut-regular-action-20261027
title: "20400源六个实际Aut恢复：阶16/12/16三逆对，fullAut regular/order20400有证"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/six_generators/REPORT.md; research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/six_generators/PREDICTION.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/six_generators/GENERATORS.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/six_generators/RESULT.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/six_generators/run.py; research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/root0.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/AUTOMORPHISM_CHECK.json"
added: 2026-10-27T19:58:37Z
tags: ["ddp", "method-ledger"]
---

# 20400源六个实际Aut恢复：阶16/12/16三逆对，fullAut regular/order20400有证

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (6,7)；L=20400；known_source_or_recovery n=20400

**距目标的证据：** N0=[850,4183,13044,16575,17412,18426]；逆对850↔16575阶16，4183↔17412阶12，13044↔18426阶16。Γ轨道邻闭＋继承sourceconnected得transitive；root0 rootedWL单点给fullAut stabilizer1，故Γ=fullAut、regular/order20400。由此六incidentedge代表覆盖全source任意edge subdivision，candidate结果由独立expert row承载。

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 20400,
  "source_m": 61200,
  "actual_automorphisms": 6,
  "new_WL_runs": 5,
  "reused_first_map": true,
  "first_map_edgecheck_repeated": false,
  "new_WL_rounds_per_root": 8,
  "generator_neighbor_ids": [
    850,
    4183,
    13044,
    16575,
    17412,
    18426
  ],
  "generator_orders": [
    16,
    12,
    16,
    16,
    12,
    16
  ],
  "inverse_index": [
    3,
    4,
    5,
    0,
    1,
    2
  ],
  "new_edgechecks": 306000,
  "edge_failures": 0,
  "full_inverse_permutations_checked": true,
  "root0_stabilizer_trivial": true,
  "group_transitive_proved": true,
  "regular_group_order": 20400,
  "fullAut_order": 20400,
  "group_orbit_enumerated": false,
  "multiplicationtable": false,
  "CPU_seconds": 0.994189695,
  "graph_BFS": 0,
  "candidate_graphs": 0,
  "new_lower_bounds": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/six_generators/REPORT.md](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/six_generators/REPORT.md)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/six_generators/PREDICTION.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/six_generators/PREDICTION.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/six_generators/GENERATORS.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/six_generators/GENERATORS.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/six_generators/RESULT.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/six_generators/RESULT.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/six_generators/run.py](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/six_generators/run.py)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/root0.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/root0.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/AUTOMORPHISM_CHECK.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/rooted_wl_recovery/AUTOMORPHISM_CHECK.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 只复用actualCSR/root0colors/首0→850map，补其它5N0根1WL各8轮离散，完整验证5新pi双射/rootimage/61200edges。6全permutation阶及逆配对全部核对；不枚举group/orbit/table、不BFS/候选/原source重parse。

**仍未完成：** Normalgroupcoordinates/matrixpresentation and parameter-transferred largergraphs remain unperformed; sourceD7 inherited rather than newBFS.

**启发与重启依据：** 唯一root WL离散可把actualAut恢复变为固定邻根canonicalcolor匹配，从缺gens转为完整permutation Cayley接口。真实oldadj采用g∘pi_i的rightstep，不能把pi_i(v)直接当原标签rightstep。小矩阵normalform仍需另给明确normal25/quotient坐标任务，不自动展开群搜索。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

