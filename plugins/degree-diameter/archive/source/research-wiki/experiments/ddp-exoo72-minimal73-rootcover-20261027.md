---
type: experiment
node_id: exp:ddp-exoo72-minimal73-rootcover-20261027
title: "Exoo72最小73点插入：4992120项均无root三步覆盖"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d5_exoo72_extension/REPORT.md; research/ddp/more_graphs_20261027/d5_exoo72_extension/root_cover_preflight/PREDICTION.json; research/ddp/more_graphs_20261027/d5_exoo72_extension/root_cover_preflight/REPORT.md; research/ddp/more_graphs_20261027/d5_exoo72_extension/root_cover_preflight/RESULT.json; research/ddp/more_graphs_20261027/d5_exoo72_extension/root_cover_preflight/enumerate.cpp"
added: 2026-10-27T15:27:58Z
tags: ["ddp", "method-ledger"]
---

# Exoo72最小73点插入：4992120项均无root三步覆盖

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** necessary-root-coverage-model-no-final-graph

**目标与阶数：** (5,3)；L=72；条件性n=73（未据此计纪录）

**距目标的证据：** 4992120项全查：连原图R2并覆盖72旧点的必要条件也0通过；故删除后新root条件0。0图、0候选BFS、0旧旧后筛；总编译/计算1.557CPU秒。

**其他指标（保持原计数类型）：**
```json
{
  "root_operations": 4992120,
  "matching_triples": 832020,
  "necessary_original_R2_cover": 0,
  "newgraphs_generated": 0,
  "oldold_checked": false,
  "candidate_BFS": 0,
  "native_CPU_seconds": 0.014127,
  "total_children_CPU_seconds": 1.5569399999999998
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d5_exoo72_extension/REPORT.md](../../research/ddp/more_graphs_20261027/d5_exoo72_extension/REPORT.md)；[research/ddp/more_graphs_20261027/d5_exoo72_extension/root_cover_preflight/PREDICTION.json](../../research/ddp/more_graphs_20261027/d5_exoo72_extension/root_cover_preflight/PREDICTION.json)；[research/ddp/more_graphs_20261027/d5_exoo72_extension/root_cover_preflight/REPORT.md](../../research/ddp/more_graphs_20261027/d5_exoo72_extension/root_cover_preflight/REPORT.md)；[research/ddp/more_graphs_20261027/d5_exoo72_extension/root_cover_preflight/RESULT.json](../../research/ddp/more_graphs_20261027/d5_exoo72_extension/root_cover_preflight/RESULT.json)；[research/ddp/more_graphs_20261027/d5_exoo72_extension/root_cover_preflight/enumerate.cpp](../../research/ddp/more_graphs_20261027/d5_exoo72_extension/root_cover_preflight/enumerate.cpp)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Fixedactual72source;delete3pairwisedisjointedges;joinnewrootto5of6endpoints.832020matchingtriples×6omittedends,complete.

**仍未完成：** 一般(5,3)超过72仍未解；此受限范围不是全题，完整Lean实例0。

**启发与重启依据：** 停止这一操作，不盲加删边数/seed；旧源是否所有增点都无望未由此证明。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

