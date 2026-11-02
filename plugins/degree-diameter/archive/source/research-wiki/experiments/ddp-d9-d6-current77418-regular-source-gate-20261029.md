---
type: experiment
node_id: exp:ddp-d9-d6-current77418-regular-source-gate-20261029
title: "Current77418 source is9regular: no retained-edge expansion slots"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: partial
confidence: high
date: "2026-10-29"
hardware: ""
duration: ""
provenance: "research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/PREDICTION.json; research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/RESULT.json; research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/REPORT.md; research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/SOURCE_NOTES.json; research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/LOCAL_SCOPE_CHECK.json; research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/PRIMARY_1_RECEIPT.json; research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/PRIMARY_2_RECEIPT.json; research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/profile_literal.py; research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/HANDLE.json; research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/TERMINAL.json; research/ddp/refresh_20261029/SOURCE_GUARD_Q8_FINAL_WIKI_REPORT.md"
added: 2026-10-29T18:52:16Z
tags: ["ddp", "method-ledger"]
---

# Current77418 source is9regular: no retained-edge expansion slots

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (9,6)；L=77418；known_source_or_recovery n=77418

**距目标的证据：** 实际D=6，目标D=6；Official current-sourceD6 assertion inherited; no source distance BFS.；实际77418/348381/simple/symmetric/all9regular，free0/slots0。固定保全部旧顶点与旧边的任何非空connected增广在max9下不可能；普通degree不足证明无需距离球。sourceD6继承官方，CPU.641021884、2primary、0距离BFS/球/solver/候选。

**其他指标（保持原计数类型）：**
```json
{
  "actual_source_n": 77418,
  "actual_source_m": 348381,
  "actual_source_degree_histogram": {
    "9": 77418
  },
  "free_vertices": 0,
  "free_slots": 0,
  "CPU_seconds": 0.6410218839999999,
  "primary_pages_or_files": 2,
  "original_H8_n": 74898,
  "modified_spread_lines": 504,
  "new_vertices": 2520,
  "current_modified_source_bipartite": false,
  "source_D6_inherited": true,
  "source_distance_BFS": 0,
  "new_balls": 0,
  "candidate_graphs": 0,
  "solver_calls": 0,
  "new_lower_bound_mathematically_verified": false,
  "independent_new_method": false,
  "source_credit": "Official Comellas current77418 H8 flag-subdivision construction"
}
```





**原始证据：** [research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/PREDICTION.json](../../research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/PREDICTION.json)；[research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/RESULT.json](../../research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/RESULT.json)；[research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/REPORT.md](../../research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/REPORT.md)；[research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/SOURCE_NOTES.json](../../research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/SOURCE_NOTES.json)；[research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/LOCAL_SCOPE_CHECK.json](../../research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/LOCAL_SCOPE_CHECK.json)；[research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/PRIMARY_1_RECEIPT.json](../../research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/PRIMARY_1_RECEIPT.json)；[research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/PRIMARY_2_RECEIPT.json](../../research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/PRIMARY_2_RECEIPT.json)；[research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/profile_literal.py](../../research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/profile_literal.py)；[research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/HANDLE.json](../../research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/HANDLE.json)；[research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/TERMINAL.json](../../research/ddp/refresh_20261029/d9_D6_source_mechanism_gate/TERMINAL.json)；[research/ddp/refresh_20261029/SOURCE_GUARD_Q8_FINAL_WIKI_REPORT.md](../../research/ddp/refresh_20261029/SOURCE_GUARD_Q8_FINAL_WIKI_REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Current official77418 literal only: one full degree/edge parse, two primary pages/files. Source H8 plus flag-subdivision/K5/external3 recipe, not the182618/186033 tower.

**正向保证：** 直接literal确认每个旧点已经满9度；oldedges全保则无法给任一旧点添加连接到新点的边。；Recipe中每新点2old+4clique+3external=9；actual triangle表明整个modified source非二分，不能直接称全源异色锚层。

**仍未完成：** 一般(9,6)、删旧边手术、不同source未排；10D6=137180 literal未下载或profile，不混为本次已测。

**启发与重启依据：** 此源不支持保边append，停止该入口；只有实质删边／重接规则或不同source才是新问题，不借free0开启proxy/guard梯子。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

