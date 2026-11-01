---
type: experiment
node_id: exp:propertyb-matched-baselines-k13-prefix-20261021
title: "共同参考包络与k13混合锁证书停止点"
idea_id: ""
verdict: partial
confidence: high
date: "2026-10-21"
hardware: "本机"
duration: "k5…11基线重放约0.224秒；k13总计算约99秒"
provenance: "context/propertyb-general/locks-vs-uniform-20261021/"
added: 2026-10-21T09:38:22Z
tags: ["property-b", "matched-baselines", "k13", "lock-certificate", "bounded-prefix"]
---

# 共同参考包络与k13混合锁证书停止点

**verdict:** `partial`  ·  **confidence:** `high`

## Metrics
k5…12共同L_ref为32,64,128,263,538,1085,2245,4633；新展示值35,65,130,266,542,1112,2275,4661；共同增益3,1,2,3,4,27,30,28。k13 M9544完整前缀v105…971、214248型通过，v972/d=e81未过；余972…1217未覆盖。

## Reasoning
参考包络只取六项已核明确参考，不声称全部文献最强。k10/11历史GL式(7)口径+42/+62保留，共同基线增益改+27/+30。k13逐d拼接修复旧v857缺口，但v972的零/一/二锁上界不严格，完整三锁D域无可用D；没有新完整下界，也不是不存在性或路线极限。一般k≥12统一增长已有Lean，claim:propertyb-general-growth-k12保持verified；固定实例和展示值沿用各自原验收状态。详见context/propertyb-general/locks-vs-uniform-20261021/STATUS.md。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

