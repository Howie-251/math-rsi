---
type: idea
node_id: idea:propertyb-five-33-edge-threshold
title: "研究中：判定33条五元边是否必然可二染色"
stage: active
outcome: pending
added: 2026-10-07T15:46:07Z
based_on: ["paper:grill2024_improved_lower_bounds", "paper:ferber2019_quantitative_lovász_criterion"]
target_gaps: ["gap:G5"]
tags: ["property-b", "follow-up", "lean"]
---

# 研究中：判定33条五元边是否必然可二染色

**stage:** `active`  ·  **outcome:** `pending`

T33 Goal已启动，复用原wiki和Lean；新主定理尚未解决。

## Thesis
研究T33：任意有限简单五元超图至多33边是否必有Property B。优先证明m(5)≥34；若有严格33边反例则结合旧claim propertyb-m5-ge33确定m(5)=33。详细启动文本：../../GOAL_PROPERTYB_33.md；规格与恢复地图：../../context/propertyb33-preparation/CONTEXT_HANDOFF.md。用户已启动新Goal，原32边完成状态保留；当前进度见../../context/propertyb33/PROGRESS.md。

准备阶段已得到：用整数度下界26×7>165及均衡染色33/34<1严格约化到19–25点；19点全局有序单交边对数≤1002，精确界228291/230945<1（纸面论证与算术交叉核对，尚未新Lean装配）。20点相同全局法4599/4420>1仍不足。22点三种共度1锁对仍可保证；23点有六度点时完整66/677选点仍成立，无六度分支满足Σ(d−7)=4；24点六度点r≥7即可选四锁，r=3..6需新结构，原Lean独立集阈值要加强。依据和复用边界见DIAGNOSTIC.md、SUPPLEMENT_GLOBAL_PAIRS.md、ROUTE_CHECK.md及REVIEW_RECONCILIATION.md。

原wiki中的文献、失败经验、精确算术和Lean基础继续复用，不复制独立知识库。先实现Target33与新约化/19点分支，同时定位20–25点具体义务。Numeric.validProfile、RealizesProfile包含32/992等间接旧参数，需要新接口，而非机械替换输入。

## Key risks
新主命题仍未解决。具体旧上界>1不是反例，也不证明整个概率框架不可能；未重算的分支不能记为失败。结构纸面推导与新Lean已构建必须分开。Grok/Gemini讨论提供具体修订，不提供数学真值保证；开放性和最新纪录另据原始文献核对。全部新研究保留在aris4math。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

