---
type: experiment
node_id: exp:ddp-d15-source-and-20ball-prediction-20261027
title: "(15,5)100132源与覆盖预测：同单余量类20.11%对17.39%"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d15_D5_mizuno_extension/REPORT.md; research/ddp/more_graphs_20261027/d15_D5_mizuno_extension/RESULT.json; research/ddp/more_graphs_20261027/d15_D5_mizuno_extension/one_slot_comparison/PREDICTION.json; research/ddp/more_graphs_20261027/d15_D5_mizuno_extension/one_slot_comparison/RESULT.json; research/ddp/more_graphs_20261027/PUBLIC_BASELINES_1759.json"
added: 2026-10-27T18:01:05Z
tags: ["ddp", "method-ledger"]
---

# (15,5)100132源与覆盖预测：同单余量类20.11%对17.39%

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (15,5)；L=100132；known_source_or_recovery n=100132

**距目标的证据：** 实际100132/m749732/max15，degree13:18、14:2480、15:97634，free2498/slots2516。首20free点R4平均20042.3，占20.0159%；先前D14rare15为16.1100%。纠正余量类型后，完整单余量population的D15平均20.1129%、D14平均17.3888%，相同lex20规则也支持更高覆盖比例。

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 100132,
  "source_m": 749732,
  "free_vertices": 2498,
  "free_slots": 2516,
  "sampled_R4_balls": 20,
  "first20_mean_fraction": 0.200158790396676,
  "matched_one_slot_mean_D15": 0.20112948488640156,
  "matched_one_slot_mean_D14": 0.17388806171752097,
  "matched_one_slot_comparison_CPU": 0.158289577,
  "source_and20ball_CPU": 1.742385652,
  "oldsource_allBFS": 0,
  "sphere_prediction": "SUPPORTED",
  "global_atmost15_existence": "UNRESOLVED",
  "latest_public_15_D5": 102060,
  "latest_public_checked_UTC": "2026-10-27 17:59:33 UTC",
  "studied_D15_source_is_now_historical": true
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d15_D5_mizuno_extension/REPORT.md](../../research/ddp/more_graphs_20261027/d15_D5_mizuno_extension/REPORT.md)；[research/ddp/more_graphs_20261027/d15_D5_mizuno_extension/RESULT.json](../../research/ddp/more_graphs_20261027/d15_D5_mizuno_extension/RESULT.json)；[research/ddp/more_graphs_20261027/d15_D5_mizuno_extension/one_slot_comparison/PREDICTION.json](../../research/ddp/more_graphs_20261027/d15_D5_mizuno_extension/one_slot_comparison/PREDICTION.json)；[research/ddp/more_graphs_20261027/d15_D5_mizuno_extension/one_slot_comparison/RESULT.json](../../research/ddp/more_graphs_20261027/d15_D5_mizuno_extension/one_slot_comparison/RESULT.json)；[research/ddp/more_graphs_20261027/PUBLIC_BASELINES_1759.json](../../research/ddp/more_graphs_20261027/PUBLIC_BASELINES_1759.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 实际100132/m749732/max15，degree13:18、14:2480、15:97634，free2498/slots2516。首20free点R4平均20042.3，占20.0159%；先前D14rare15为16.1100%。纠正余量类型后，完整单余量population的D15平均20.1129%、D14平均17.3888%，相同lex20规则也支持更高覆盖比例。

**仍未完成：** No general source-family maximality is claimed; final concrete Lean remains incomplete.

**启发与重启依据：** 球密度预测获支持，只支持转实际构造，不证明15连接能共同覆盖，更不能把不同source/degree/field的比较当fieldsize单独因果效应。原fiber标签未绑定，不假定前100000就是旧core。 最新17:59主表15,5为102060；100132源仅为历史控制对象，100133已不是纪录目标。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

