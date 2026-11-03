---
type: experiment
node_id: exp:dd82-odd-primary-square-f3-small
title: "奇特征自伴平方判据的小有限域校验"
idea_id: "idea:dd82-n61-global-closure-spectral"
verdict: yes
confidence: high
date: "2026-10-19"
hardware: "local CPU"
duration: "wall 1.501969 s; CPU 1.501000 s"
provenance: "computations/dd82/spectral/odd_primary_square_check.py; computations/dd82/spectral/odd_primary_square_check.result.json"
added: 2026-10-19T13:02:36Z
tags: ["dd82", "finite-field", "algorithm-validation", "not-n61-exclusion"]
---

# 奇特征自伴平方判据的小有限域校验

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:dd82-n61-global-closure-spectral`

## Metrics
F3标准内积n1–4全部对称矩阵。n3:729扫描/33幂零/5可自伴开方；n4:59049扫描/1521幂零/129可自伴开方。零不一致；n4普通平方可行但自伴失败48个。

## Reasoning
原始型/维数平方类递推，与直接枚举全部对称幂零X并收集X²独立比对；保存普通根并直接乘法验证。仅验证有限域算法，没有B样本或61点图排除。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

