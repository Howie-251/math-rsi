---
type: experiment
node_id: exp:propertyb-k12-lock-certificate-20261021
title: "k12 M4660完整锁点证书及独立复核范围"
idea_id: ""
verdict: partial
confidence: high
date: "2026-10-21"
hardware: "本机单BLAS/OMP线程"
duration: "原M4660完整遍历86.712秒；独立零/一锁重算1.690秒"
provenance: "context/propertyb-general/k12-lock-pilot-20261021/"
added: 2026-10-21T09:38:22Z
tags: ["property-b", "k12", "lock-certificate", "computer-assisted", "partial-independent-replay"]
---

# k12 M4660完整锁点证书及独立复核范围

**verdict:** `partial`  ·  **confidence:** `high`

## Metrics
M4660；v93…782；691429型全部严格通过（0/1/2/3锁：419/2929/87807/600274）。独立完整重建参数域691429型，31型Fraction边界重算及全部3348个零/一锁型不同分母整数重算通过。共同基线4633，新候选4661，增益28。

## Reasoning
在合作者一般锁点准则及最小反例归约下，得到m(12)≥4661的计算机辅助证明候选。两/三锁未进行第二次完整概率算术重放，尚未Lean，不创建或提升verified claim。新Grok真实grok-4.7-build/xhigh/end_turn确认一般准则可迁移；请求时M4647尚未全跑，不是最终M4660整表审阅。完整来源及状态见context/propertyb-general/locks-vs-uniform-20261021/STATUS.md。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

