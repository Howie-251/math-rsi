---
type: experiment
node_id: exp:ddp-d13-singlefault-star-guard-mechanism-20261027
title: "成功机制实测：同10个core邻点的free代理补全3614私有目标"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/REPORT.md; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/RESULT.json; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/MECHANISM.md; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/MECHANISM.json; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/ORIGINALBASE_CONTROL.json; research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/CONTROL_PREDICTION.json"
added: 2026-10-27T17:50:48Z
tags: ["ddp", "method-ledger"]
---

# 成功机制实测：同10个core邻点的free代理补全3614私有目标

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (13,5)；L=51417；known_source_or_recovery n=51417

**距目标的证据：** prototype51013删满pin11352后缺3535core+79extras；guard50577完整补齐。D/G共享全部10core邻点，D-only=[50848,51013,51287]、G-only=[51275]均是extras，非fulltwins。3608洞有经共享分支的guard最短路，6core洞由G-only分支给更短路；每个原prototype≤5私有路线都须先经被删pin。

**其他指标（保持原计数类型）：**
```json
{
  "missing_core": 3535,
  "missing_extras": 79,
  "shared_core_neighbors": 10,
  "guard_shared_shortest_route_targets": 3608,
  "guard_only_shortest_branch_targets": 6,
  "guard_is_full_twin": false,
  "originalbase_control_prototype": 3962,
  "originalbase_control_missing": 0,
  "originalbase_control_retained_core_proxy": 50638,
  "originalbase_control_cases": 1,
  "total_analysis_CPU_seconds": 0.376492091,
  "other39_originalbase_checks": 0,
  "newgraphs": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/REPORT.md](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/REPORT.md)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/RESULT.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/RESULT.json)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/MECHANISM.md](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/MECHANISM.md)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/MECHANISM.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/MECHANISM.json)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/ORIGINALBASE_CONTROL.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/ORIGINALBASE_CONTROL.json)；[research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/CONTROL_PREDICTION.json](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/CONTROL_PREDICTION.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** prototype51013删满pin11352后缺3535core+79extras；guard50577完整补齐。D/G共享全部10core邻点，D-only=[50848,51013,51287]、G-only=[51275]均是extras，非fulltwins。3608洞有经共享分支的guard最短路，6core洞由G-only分支给更短路；每个原prototype≤5私有路线都须先经被删pin。

**仍未完成：** No general source-family maximality is claimed; final concrete Lean remains incomplete.

**启发与重启依据：** 优先找满pin的free核心邻域代理，先看代理是否已在保留集合，再完整currentR4；不是任意allanchor试配。最小对照3962删6216的10pins在ORIGINAL51417已全覆/degree合法，且保留50638已同core邻域；首seed对此例旧target覆盖非必要，其它39原base未复算，不能外推全部。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

