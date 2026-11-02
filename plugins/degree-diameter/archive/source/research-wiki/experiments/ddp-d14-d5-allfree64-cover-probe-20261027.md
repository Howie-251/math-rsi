---
type: experiment
node_id: exp:ddp-d14-d5-allfree64-cover-probe-20261027
title: "(14,5)全部3685可接点：64个完整14pin构造无命中"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/allfree_cover_probe/REPORT.md; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/allfree_cover_probe/RESULT.json; research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/allfree_cover_probe/PREDICTION.json"
added: 2026-10-27T17:26:53Z
tags: ["ddp", "method-ledger"]
---

# (14,5)全部3685可接点：64个完整14pin构造无命中

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** (14,5)；L=94186；条件性n=94187（未据此计纪录）

**距目标的证据：** 复用rare15球、一次补3670球，allfree union覆盖全部94186；各target支持455..824。冻结64个不同首选，按最稀少未覆target约束及最大完整gain，每项选14pins，64/64完成，0命中，漏3705..4479；0图/0newroot及旧source全BFS。

**其他指标（保持原计数类型）：**
```json
{
  "free_candidates": 3685,
  "reused_R4_balls": 15,
  "new_R4_balls": 3670,
  "allfree_union_missing": 0,
  "target_support_min": 455,
  "target_support_max": 824,
  "frozen_constructs": 64,
  "constructs_completed": 64,
  "hits": 0,
  "newroot_missing_min": 3705,
  "newroot_missing_max": 4479,
  "CPU_including_compile": 4.412178511,
  "operation_prediction": "REFUTED",
  "global_atmost14_existence_prediction": "UNRESOLVED",
  "R4_cache_bytes": 43394560
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/allfree_cover_probe/REPORT.md](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/allfree_cover_probe/REPORT.md)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/allfree_cover_probe/RESULT.json](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/allfree_cover_probe/RESULT.json)；[research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/allfree_cover_probe/PREDICTION.json](../../research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/allfree_cover_probe/PREDICTION.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 复用rare15球、一次补3670球，allfree union覆盖全部94186；各target支持455..824。冻结64个不同首选，按最稀少未覆target约束及最大完整gain，每项选14pins，64/64完成，0命中，漏3705..4479；0图/0newroot及旧source全BFS。

**仍未完成：** General source extension feasibility remains open; no complete newgraph was generated.

**启发与重启依据：** 全候选点到达能力不缺，障碍转为14连接的共同覆盖，不能凭union满或总漏减少称解。操作预测64项命中被反驳，任意≤14freepin存在性仍UNRESOLVED。保存43MB完整R4与支持缓存，停止这个生成规则，不加starts或按3705续修；转其它参数。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

