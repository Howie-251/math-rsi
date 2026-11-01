---
type: experiment
node_id: exp:propertyb36-twentyfive-tight-b12-exclusion-20261020
title: "二十五点最小蓝十二紧面的共同匹配排除"
idea_id: ""
verdict: partial
confidence: high
date: "2026-10-20"
hardware: ""
duration: ""
provenance: "proofs/propertyb35/TWENTYFIVE_TIGHT_B12_EXCLUSION.md；context/propertyb35-paper/round01/twentyfive/whole_class_attack_20261020/B12_TRANSFER.md；B12_CHECK.py；B12_RESULT.json；B12_REVIEW.md"
added: 2026-10-20T10:59:15Z
tags: ["property-b", "m5-ge36", "shared-original-edge-counting"]
---

# 二十五点最小蓝十二紧面的共同匹配排除

**verdict:** `partial` · **confidence:** `high`

## Metrics

在25点、35简单五边、paircover、非B且有六度点的同一原H上，以唯一坏边含低点的源域依次min(b,u,δ)、max|S|，完整排除b12/u0/N2=3。不是整个25点多六度分支。

三条二蓝原边形成同一匹配；低红汇点ℓ2/3。任红汇点的私有交换只用二级u最优，匹配使n1≤2；ℓ3时高汇点n2≤1且n2=1迫n1≤1，统一跨色行费κ≥5。E0全部由共同owner流与共享割预算排除，E1只余ℓ3/c1/无高汇点的唯一双owner。匹配六低端点均命中双owner z的两N4，owner流又迫z不在低汇点的N3；逐G/N1/N2/N3/N4检查，无原边覆盖(z,h)，矛盾。

## Reasoning

原H、低点单位共度、共同三匹配、同一批私有边与中性交换在整条链中保持。高汇点的u比较不被冒充三级中性；maxS流仅用于已经证明中性的低点交换。ℓ2时只称已标记匹配端点低，不把第三个未标记对偷加低度前提。

[规范全文](../../proofs/propertyb35/TWENTYFIVE_TIGHT_B12_EXCLUSION.md)、[原始实际源稿](../../context/propertyb35-paper/round01/twentyfive/whole_class_attack_20261020/B12_TRANSFER.md)及同目录B12_CHECK.py/B12_RESULT.json/B12_REVIEW.md绑定本范围。纸面独立核为same-family/provisional；指定跨家族审阅由主代理按本完整scope归档，不提前记作通过。小核只核角色数、owner投影和精确整数，不枚举原超图或未知染色，不以有限必要谱代替实际输入覆盖。

## Remaining scope

u>0、N2≥4的蓝十二源，以及其他非紧蓝数仍开；没有新完整r≥3可染分支或新全局下界。本结果可复用的是三匹配对高汇点的共同价格，以及保留旧汇点流失项后收束到同一双owner的证明机制。
