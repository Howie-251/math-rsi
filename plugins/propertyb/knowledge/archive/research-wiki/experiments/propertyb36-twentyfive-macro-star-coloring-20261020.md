---
type: experiment
node_id: exp:propertyb36-twentyfive-macro-star-coloring-20261020
title: "二十五点六星宏观随机染色与共度二多低点推论"
idea_id: ""
verdict: partial
confidence: high
date: "2026-10-20"
hardware: ""
duration: ""
provenance: "proofs/propertyb35/TWENTYFIVE_MACRO_STAR_COLORING.md；context/propertyb35-paper/round01/twentyfive/macro_star_coloring_20261020/REPORT.md；RESULT.json；MILP_RESULT.json；VERIFY_MILP_RESULT.json；COMMON_W_EXCESS.md"
added: 2026-10-20T11:10:28Z
tags: ["property-b", "m5-ge36", "macro-star-coloring"]
---

# 二十五点六星宏观随机染色与共度二多低点推论

**verdict:** `partial`  ·  **confidence:** `high`

## Metrics
25点35简单五边/paircover的六星宏观门：任一六度z满足Wz<=25即Property B，3840样本至少17成功。实际共同低点计数进一步给全λ<=2且r>=8可染。A/B/C六型概率共339840边样本独立核PASS；单次246型/39约束MILP取得13非零型精确松弛，全部15固定A最小65/64、B151/144、C1487/768，独立49920边样本复核PASS，solver CPU4.42931秒。

## Reasoning
局部宏星门和有共度条件的整r区间已证明；不能写整个25/r>=3或m5>=36。MILP松弛不是实际H或非B反例，仅说明这组矩约束与union bounds不足。未扩大域。无cap2的解析分解保留净量E-Z-D，尚不能控制，未新增无条件整r范围。same-family/provisional，未新增跨家族本scope审阅或正式proof-checker claim。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

