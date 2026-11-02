---
type: experiment
node_id: exp:ddp-d13-d4-c9-action4-transfer-20261027
title: "连通C9作用4单候选8748：首根ecc5、918个四步缺项"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d13_D4_current6804/c9_action4_transfer/REPORT.md; research/ddp/more_graphs_20261027/d13_D4_current6804/c9_action4_transfer/RESULT.json; research/ddp/more_graphs_20261027/d13_D4_current6804/c9_action4_transfer/counterexample.json"
added: 2026-10-27T18:48:42Z
tags: ["ddp", "method-ledger"]
---

# 连通C9作用4单候选8748：首根ecc5、918个四步缺项

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (13,4)；L=6804；candidate_graph_or_family n=8748

**距目标的证据：** 预测D4被首根反例推翻。全局D未知且至少5；全图边未导出，run.py可重建唯一字面。已有I/R2/G4/中心包充分证书只覆盖85/108controller点。

**其他指标（保持原计数类型）：**
```json
{
  "n": 8748,
  "m": 56862,
  "degree13": 8748,
  "first_root": 0,
  "first_root_eccentricity": 5,
  "single_root_R4_missing_targets": 918,
  "global_D_lower_bound": 5,
  "roots_checked": 1,
  "ordinary_unordered_badpairs": null,
  "good4_words": 88,
  "full_R2_packets": 10,
  "full_central_packets": 32,
  "certified_controller_vertices": 85,
  "controller_n": 108,
  "CPU": 0.104727329,
  "oldsource_BFS": 0,
  "parameter_candidates": 1
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d13_D4_current6804/c9_action4_transfer/REPORT.md](../../research/ddp/more_graphs_20261027/d13_D4_current6804/c9_action4_transfer/REPORT.md)；[research/ddp/more_graphs_20261027/d13_D4_current6804/c9_action4_transfer/RESULT.json](../../research/ddp/more_graphs_20261027/d13_D4_current6804/c9_action4_transfer/RESULT.json)；[research/ddp/more_graphs_20261027/d13_D4_current6804/c9_action4_transfer/counterexample.json](../../research/ddp/more_graphs_20261027/d13_D4_current6804/c9_action4_transfer/counterexample.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 仅C9 semidirect_4 C12，原a/b/z及全部fiber chart/c不变。实际生成simple connected13regular8748/56862，首根0 BFS即ecc5，停止。0→730距离5；全局直径未测，918仅此根R4未覆盖targets，不是无序坏对。

**仍未完成：** No general parameter-family exclusion; complete Lean remains unproved.

**启发与重启依据：** C9改为奇模数确修C8不连通，但连通与三coset包不能保证所有控制终点共同覆盖。此单一移模候选收束，不调整r、生成元或chart续分数。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

