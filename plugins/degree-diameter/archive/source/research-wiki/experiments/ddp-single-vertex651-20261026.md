---
type: experiment
node_id: exp:ddp-single-vertex651-20261026
title: "650源全部两边匹配的非正则651点扩张"
idea_id: "idea:ddp-matching-augmentation"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "one CPU per task"
duration: "0.361 enumeration CPU s"
provenance: "research/ddp/matching_single_vertex650/REPORT.md; research/ddp/matching_single_vertex650/DISTANCE_CHECK.md"
added: 2026-10-27T08:25:51Z
tags: ["ddp", "no-new-bound", "method-ledger"]
---

# 650源全部两边匹配的非正则651点扩张

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-matching-augmentation`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (5,5)；L=650；candidate_graph_or_family n=651

**距目标的证据：** 实际D=6，目标D=5；原报告bad（类型见详情）=59；Existing Wiki Metrics; no experiment rerun；1319500无序边对中6500共端点非法，1313000合法全部完成；没有新根五步全覆盖者，至少缺19，250匹配达到19。保存图全651根BFS为D6、59坏对，maxdegree5、唯一degree4。



**既有原文指标：** 1319500无序边对中6500共端点非法，1313000合法全部完成；没有新根五步全覆盖者，至少缺19，250匹配达到19。保存图全651根BFS为D6、59坏对，maxdegree5、唯一degree4。



**原始证据：** [research/ddp/matching_single_vertex650/REPORT.md](../../research/ddp/matching_single_vertex650/REPORT.md)；[research/ddp/matching_single_vertex650/DISTANCE_CHECK.md](../../research/ddp/matching_single_vertex650/DISTANCE_CHECK.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 该完整固定源构造族均失败；19是全族新根缺失最小值，59不是全族总坏对最小值。最大度目标允许非正则，新点度4合法。独立整数bitset整份覆盖直方图一致。

**启发与重启依据：** 该完整固定源构造族均失败；19是全族新根缺失最小值，59不是全族总坏对最小值。最大度目标允许非正则，新点度4合法。独立整数bitset整份覆盖直方图一致。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

