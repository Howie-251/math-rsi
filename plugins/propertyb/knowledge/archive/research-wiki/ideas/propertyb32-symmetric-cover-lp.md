---
type: idea
node_id: idea:propertyb32-symmetric-cover-lp
title: "已知不足：T32裸COVER LP与均匀分数解"
stage: archived
outcome: negative
added: 2026-10-13T08:29:00Z
based_on: []
target_gaps: []
tags: ["property-b", "failed-route", "scoped-failure"]
---

# 已知不足：T32裸COVER LP与均匀分数解

**stage:** `archived`  ·  **outcome:** `negative`

确定的对称松弛已有分数可行解，补非均衡染色约束也不能排除32边。

## Thesis
在19–25点，z_A=32/binom(v,5)满足全部染色、总边数、点对覆盖及最低度约束。裸COVER LP的对称平均解在均衡染色处最紧，因此增加全部非均衡染色约束不改变该LP最优值。只针对这个松弛，不否定条件化LP、整性或更高阶约束；不是最终T32证明的依赖。推导见[文献与LP诊断](../../context/LITERATURE_UPDATE_20261006.md)和[失败地图第11节](../PROPERTY_B_FAILURE_ATLAS.md)。

## Key risks
Lesson: 先将均匀分数解代入候选新约束；只有新结构、整性或高阶约束排除了该解时，才值得重启这个LP路线。
完整范围和原始证据见上方Thesis及对应失败地图条目。
新路线改变了这些条件时应重新判断，不能把本条当成通用禁令。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

