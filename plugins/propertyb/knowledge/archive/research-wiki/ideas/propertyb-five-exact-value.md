---
type: idea
node_id: idea:propertyb-five-exact-value
title: "长期拓展：确定m(5)的精确值"
stage: proposed
outcome: pending
added: 2026-10-13T08:25:22Z
based_on: ["paper:grill2024_improved_lower_bounds", "paper:aglave2020_improved_bounds_uniform", "paper:grill2024_some_upper_bounds"]
target_gaps: []
tags: ["property-b", "follow-up"]
---

# 长期拓展：确定m(5)的精确值

**stage:** `proposed`  ·  **outcome:** `pending`

分别推进严格普适下界和显式不可染构造，最终使两端相等。

## Thesis
目标是找到整数q并证明：所有边数<q的有限简单五元超图均可二染色，且存在恰q条边的不可染超图。2026-10-13项目已完成T32与T33，现有严格下界为34；下一普适阈值是34边可染，即m(5)≥35。已核查的Grill–Linzmayer 2024 Table 1记录上界51，这是已有文献快照，不宣称穷尽核实了最新上界。两侧严格改进都值得研究，精确值需上下界最终相等。复用[经验总览](../PROPERTY_B_RESEARCH_LESSONS.md)、[下一档指南](../PROPERTY_B_NEXT_BOUND_PLAYBOOK.md)及原有概率/结构引理、构造模型和文献；T33不再重启。原文：https://arxiv.org/html/2403.05674v3 。

## Key risks
没有证据可预先指定精确值。找到候选必须另证不可染，搜索未命中不能证明下界。本次只整理经验和下一档准备，不启动长期研究Goal。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

