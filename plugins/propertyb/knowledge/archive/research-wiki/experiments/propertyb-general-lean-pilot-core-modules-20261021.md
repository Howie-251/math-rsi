---
type: experiment
node_id: exp:propertyb-general-lean-pilot-core-modules-20261021
title: "一般RS核心与17元Lean阶段：全链验证和交付完成"
idea_id: "idea:propertyb-restricted-k-general-bound"
verdict: yes
confidence: high
date: "2026-10-21"
hardware: "本机Lean4.24.0；固定Mathlib；正式指定入口构建与独立根审计"
duration: "正式构建18.58秒；独立根审计7.23秒；非整个阶段开发耗时"
provenance: "context/propertyb-general-lean-pilot/COMPLETION_AUDIT.md; context/propertyb-general-lean-pilot/final-build-result.json; context/propertyb-general-lean-pilot/final-audit-result.json; formal/ReviewAuditGeneralRSPilot.lean; context/propertyb-general-lean-pilot/reviews/C/DISPOSITION.md; PROPERTY_B_GENERAL_LEAN_PILOT.html.review.json; .aris/traces/render-html/2026-10-21_general-lean-pilot_final/"
added: 2026-10-21T05:36:03Z
tags: ["property-b", "general-rs", "lean-pilot", "formal-core-verified", "actual-caller", "stage-accepted"]
---

# 一般RS核心与17元Lean阶段：全链验证和交付完成

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:propertyb-restricted-k-general-bound`

## Metrics
一般 P、原染色充分判据 C 及任意裸 [Finite V] 上17元、≤2^17边的 Pilot 已全部装配并完成本阶段验收。正式 lake build Aris4Math.General.RS.PilotMain 成功；随后 formal/ReviewAuditGeneralRSPilot.lean 独立导入，以原始Finset边族和显式Bool两色见证复述Pilot与一般积分判据，exit0。七项最终导出／caller的传递公理均恰为propext、Classical.choice、Quot.sound。联合SampleLaw证明实际共同权重非负、总权1及sampleExpect有限和表示。一般P使用同一原始E的card和有向singlePairs gamma，无外供概率界、覆盖或证书前提。Grok-4.7-build/xhigh/end_turn与Gemini-4-argon-high/high/SUCCESS最终C均在P/C/Pilot明确范围有效接受，root已全文处置；两家静态读取源码和既有日志，未执行Lean。最终离线HTML包含两份规范正文、11个内嵌SVG公式及6张表，桌面／手机PASS；fresh保真PASS、零阻塞零警告（same-family/provisional，仅呈现审计）。正式构建18.58秒、post-build根审计7.23秒为既有缓存后的实测，不是整个阶段开发耗时。

## Reasoning
实际证明从RS初始单色触发和最后翻转点覆盖，经任意p Harris正关联／初始单色边均值／Jensen、真实单交对精确概率和共同样本并界，接到原V的Bool染色。数学形式链、指定跨家族终审、可复现报告和展示交付现均通过；本experiment verdict为yes，范围仅是一般RS核心与17元完整调用。既有一般纸面claim保持verified，本次不新建或修改claim。完整k≥17增长整数增益定理的Lean仍留待另行启动；旧35／36暂停、v2隔离。

可复用方法：（1）有限加权全排列＋真实活跃相对次序的a!b!/(a+b+1)!计数，再用Beta积分接精确J，避免连续随机过程的可测性和碰撞工程，同时保留准确积分。（2）末端实际caller尽早装配，核对原有限顶点、同一实际E和最终两色见证，使模块接口的额外前提在主链中及时消去。（3）singlePairs取同一E的有向对；指定颜色的2^(1−2k)J对两个颜色求和后给gamma/d²，明确区分有向／无向与双色因子。（4）Fintype或DecidableEq字典不同时，用Finset membership ext或显式card_congr桥接同一集合／交集；这修复表示对接，不改变数学定义或增加兼容性前提。来源为OrderCounting、PairProbability、Integral、Lift、ProbabilityBound的实际源码、构建／caller日志和最终C处置。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

