---
type: idea
node_id: idea:propertyb-six-64-edge-threshold
title: "跨均匀度推广：研究64条六元边的可二染性"
stage: proposed
outcome: pending
added: 2026-10-07T14:48:28Z
based_on: ["paper:grill2024_improved_lower_bounds", "paper:cherkashin2015_note_random_greedy"]
target_gaps: []
tags: ["property-b", "follow-up"]
---

# 跨均匀度推广：研究64条六元边的可二染性

**stage:** `proposed`  ·  **outcome:** `pending`

候选目标 m(6)≥65，复用Property B文献与概率方法，将五元专用Lean接口推广。

## Thesis
候选命题：对任意有限 V 和 E⊆binom(V,6)，|E|≤64 蕴含 Property B，即 m(6)≥65。已核对文献 Grill–Linzmayer arXiv:2403.05674v3 Theorem 1 给 m(6)≥64，仅排除≤63边。可复用wiki中的随机贪心、临界有序单交边对、低度锁点与精确条件计数思路；Lean中部分算法引理不要求五元，但Simple5Hypergraph、结构分类和数值证书含五元专用假设，须明确泛化接口。下一步先对n=6,m=64推导自己的顶点范围、度数和局部类型，不能沿用五元19–25点。原文：https://arxiv.org/html/2403.05674v3 。

## Key risks
基线为直接核对的2024原文，不宣称已经穷尽后续文献。m(6)≥65尚未由本项目证明；问题与m(5)≥34没有此处已证的难度排序或蕴含关系。六元结构与形式实现均有新增工作。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

