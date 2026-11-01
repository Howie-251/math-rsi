---
type: experiment
node_id: exp:propertyb36-twentyfive-tight-b13-exclusion-20261020
title: "二十五点多六度源的共同紧边界与蓝13排除"
idea_id: ""
verdict: partial
confidence: high
date: "2026-10-20"
hardware: ""
duration: ""
provenance: "proofs/propertyb35/TWENTYFIVE_TIGHT_B13_EXCLUSION.md；context/propertyb35-paper/round01/twentyfive/whole_class_attack_20261020/TIGHT_B13_REPAIR.md；TIGHT_B13_RESULT.json"
added: 2026-10-20T10:49:59Z
tags: ["property-b", "m5-ge36", "shared-original-edge-counting"]
---

# 二十五点多六度源的共同紧边界与蓝13排除

**verdict:** `partial`  ·  **confidence:** `high`

## Metrics
25点共同紧边界b=13,u=0,N2=2完整排除。先得c0、两个六度红汇点、坏边唯一六度点z；最大汇点owner流迫z不在汇点三蓝边且全部四个匹配端点命中z的N4，最终点对(z,h)无原边覆盖。独立小核26256个角色投影、72可行投影、53130个五集必要角色迁移PASS，CPU0.046471秒。

## Reasoning
仅排除全局最小蓝源的一条紧边界，不关闭25点r≥3整支或全局m5≥36。没有枚举原超图、铺新布局或重跑旧大表。root/Sol独立数学核为same-family/provisional；Grok/Gemini针对本新scope的审阅在途，不能记PASS，无正式proof-checker claim。b12共同紧面的新规约保留准确进口，其他非紧源仍开。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

