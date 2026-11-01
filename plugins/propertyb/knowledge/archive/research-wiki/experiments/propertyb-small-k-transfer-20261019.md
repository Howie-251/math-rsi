---
type: experiment
node_id: exp:propertyb-small-k-transfer-20261019
title: "合作者k6–11证书重放及向m5迁移的边界"
idea_id: "idea:propertyb36-40-structural-diagnosis"
verdict: partial
confidence: high
date: "2026-10-19"
hardware: "本机Mac，Python；k10/11 NumPy单线程"
duration: ""
provenance: "context/collaborator-small-k-20261019/；m6-m7/REPORT.md、m8-m9/REPORT.md、m10-m11/REPORT.md及原始日志"
added: 2026-10-19T08:36:46Z
tags: ["property-b", "m5-ge36", "collaborator", "exact-arithmetic", "unit-lock-selection"]
---

# 合作者k6–11证书重放及向m5迁移的边界

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:propertyb36-40-structural-diagnosis`

## Metrics
六组原证书共103190个局部参数配置全部严格界通过；k10/11各一条边界独立Fraction复算。k5/M35/v18–25/D≤15有限r加强未降低选锁阈值；25点中央三锁两型为29451/24871和4214/3553，均大于1。

## Reasoning
支持复用总度Caro–Wei选锁判据、真实迹压缩和整数向外舍入；有限迁移测试没有闭合m5新分支。partial指向36研究的贡献范围，非六组重放存在失败。数学阅读为same-family/provisional；未新增Lean或跨模型审阅。详细推导见research-wiki/PROPERTY_B_SMALL_K_TRANSFER.md。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

