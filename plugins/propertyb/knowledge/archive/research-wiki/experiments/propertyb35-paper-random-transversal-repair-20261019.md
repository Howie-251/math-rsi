---
type: experiment
node_id: exp:propertyb35-paper-random-transversal-repair-20261019
title: "随机横截集通用引理绕过低重合PM分类"
idea_id: ""
verdict: yes
confidence: high
date: "2026-10-19"
hardware: ""
duration: ""
provenance: "proofs/propertyb35/RANDOM_TRANSVERSAL_REPAIR.md; context/propertyb35-paper/round01/twentyfour/low_edge/k7_no_four_trace/GLOBAL_REPAIR_CRITERION.md"
added: 2026-10-19T18:25:37Z
tags: ["propertyb35-paper", "general-lemma", "random-transversal"]
---

# 随机横截集通用引理绕过低重合PM分类

**verdict:** `yes`  ·  **confidence:** `high`

## Metrics
非均匀占用乘积界自含耦合；s4/t2、三负三集十八负四集界29841/32768。

## Reasoning
从每个正集独立选一点；条件于不选x的单调重抽耦合给任意其他占用事件负相关，按点数归纳得乘积上界。root与独立Sol分别推导，不需Tutte/交图目录。原边零固定迹需正负双计，原度数预算随之修正。实际24点固定集击中所有边，低重合支合法进入；三重点仍需加强，统一乘积充分条件的失败不反驳修复。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

