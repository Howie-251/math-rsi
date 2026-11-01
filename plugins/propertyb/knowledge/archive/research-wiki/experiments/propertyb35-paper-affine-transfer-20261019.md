---
type: experiment
node_id: exp:propertyb35-paper-affine-transfer-20261019
title: "仿射色族任意23边增广与五组全为边的a5分支"
idea_id: "idea:propertyb36-40-structural-diagnosis"
verdict: yes
confidence: high
date: "2026-10-19"
hardware: ""
duration: ""
provenance: "proofs/propertyb35/SYMMETRY_COLOR_TRANSFER.md；context/propertyb35-paper/round01/twentyfive/FULL_GROUP_EDGE_CASE.md、AFFINE_AUGMENTATION_REPLAY.json、GEMINI_ANCHOR_COUNTEREXAMPLE_CHECK.json；round01/reviews/GEMINI_AFFINE_RESULT.json"
added: 2026-10-19T15:07:52Z
tags: ["property-b", "m5-ge36", "actual-input", "exact-proof"]
---

# 仿射色族任意23边增广与五组全为边的a5分支

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:propertyb36-40-structural-diagnosis`

## Metrics
标准AG(2,5)的12000自同构/3000色集；全部53130五集分11真轨道，单色概率至多21/500，23边并合界483/500。完整成员和生成元/BFS另一算法一致。

## Reasoning
一般有限群传送定理已写规范源，主代理核读；a5五组均为边时删去得2-(25,5,1)，直接证明仿射公理，明确导入Mac Innes1907五阶唯一性再拉回色族。Gemini4有效静态审阅未发现问题，未自行运行程序。至少一组非边仍开放；固定锚点反例只否定任意指定锚的方案，全25锚实际核查其余24有解。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

