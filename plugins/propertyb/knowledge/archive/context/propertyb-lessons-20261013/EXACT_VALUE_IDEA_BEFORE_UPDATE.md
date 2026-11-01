---
type: idea
node_id: idea:propertyb-five-exact-value
title: "长期拓展：确定m(5)的精确值"
stage: proposed
outcome: pending
added: 2026-10-07T14:48:28Z
based_on: ["paper:grill2024_improved_lower_bounds", "paper:aglave2020_improved_bounds_uniform", "paper:grill2024_some_upper_bounds"]
target_gaps: []
tags: ["property-b", "follow-up"]
---

# 长期拓展：确定m(5)的精确值

**stage:** `proposed`  ·  **outcome:** `pending`

同时推进普适下界和显式不可染构造，最终让两端达到同一个整数。

## Thesis
目标是找到整数q并证明：所有边数<q的有限简单五元超图均可二染色，且存在恰q条边的不可二染色五元超图。项目已交付下界33；已核对Grill–Linzmayer 2024 Table 1记录有效上界51，故当前可用区间为33≤m(5)≤51，不把该表宣称为已穷尽核实的最新上界。可复用现有全部wiki、最小反例约化、概率/结构引理、固定超图NAE模型与文献构造。可以先研究33边阈值，也可寻找少于51边且有可核查不可染证明的构造；每一侧的严格改进均有意义，精确值要求上下界最终相等。文献：https://arxiv.org/html/2403.05674v3 。

## Key risks
跨度显著大于把现下界提高1，没有证据可预先指定精确值。启发式搜索用于发现候选；找不到构造不能证明下界，找到构造必须另行验证其全部染色均失败。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

