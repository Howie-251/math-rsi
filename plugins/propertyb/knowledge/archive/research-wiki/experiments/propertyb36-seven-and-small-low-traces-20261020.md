---
type: experiment
node_id: exp:propertyb36-seven-and-small-low-traces-20261020
title: "七六度点完整纸面分支与r3至7低迹统一约化"
idea_id: "idea:propertyb36-common-marked-root-excess-20261020"
verdict: partial
confidence: medium
date: "2026-10-20"
hardware: "local exact integer arithmetic and original-H paper derivation"
duration: "paper proof and bounded exact arithmetic"
provenance: "proofs/propertyb35/TWENTYFIVE_SEVEN_OR_MORE_SIX.md; proofs/propertyb35/TWENTYFIVE_SMALL_LOW_TRACES.md; proofs/propertyb35/TWENTYFIVE_EXACTLY_SIX_LOW.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/REVIEW_RECONCILIATION.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/GEMINI_TWENTYFIVE_R6_RESPONSE.json"
added: 2026-10-20T15:40:30Z
tags: ["property-b", "m5-ge36", "r7", "small-low-traces", "actual-caller", "provisional"]
---

# 七六度点完整纸面分支与r3至7低迹统一约化

**verdict:** `partial`  ·  **confidence:** `medium`  ·  tests `idea:propertyb36-common-marked-root-excess-20261020`

## Metrics
25点35条简单五边pair-cover，L为全部r名六度点。SEVEN_OR_MORE以EIGHT为r>=8进口，r7仅用M17：总高t7给星型A(0,6,0,0)、B(1,4,1,0)、C(2,3,0,1)，完整五库存由奇数低迹覆盖、16高的一低关联不足12、两F3共高后缺失唯一低点、quad后缺失三低奇数，以及quad+triple共同高点迫另一高度<=5逐一排除。小整数CHECK仅复算3型/5库存，CPU0.000266秒，无原H枚举。SMALL_LOW_TRACES对r3..7统一排四低与三低：quad的真实中心W<=26且m32<=3，细门<=9400；排quad后triple高pair共度1，中心W<=26、纯高避pairm32<=5，细门<=10016<10139。故非B只能低迹0/1/2，n1=r(7-r)、n2=C(r,2)、n0=35-r(13-r)/2。

## Reasoning
Root与独立Sol已核SEVEN_OR_MORE和SMALL_LOW_TRACES同一原H链；r7以三种星型及五库存真实补盖闭合，small统一迫r3..7非B仅低迹0/1/2。这是已成条件数学与局部完整receipt，partial相对完整m(5)>=36，未单独验收全25。
当前审阅以REVIEW_RECONCILIATION.md的14:37 UTC处置为准：Grok1285有效end_turn，实际grok-4.7-build/xhigh，静态读取SMALL/SEVEN及M17/宏星接口，认可声明进口下的r7及small-low-traces新caller；未执行程序或Lean。Gemini授权fresh retry1 cell1286有效SUCCESS，CLI选择gemini-4-argon-high/high，静态全文读取SMALL/SEVEN/EIGHT、宏星和M17六份文件，认可r8、r7及小r低迹门，手核六型概率与实际计数；未运行程序。Root已阅读全文并处置，两者新scope未发现实质问题。更早未完成的调用没有被当作认可，旧范围不自动覆盖后来的caller。实验继续partial，纸面结果保持drafted/provisional口径，不创建或升级verified claim。八个主要开放类仍八，25多六度在本节点形成时余r3..6且全部原边低迹<=2；新24四低caller的跨模型scope另记，不并入以上认可。
15:30后继：TWENTYFIVE_EXACTLY_SIX_LOW.md已给r6实际完整纸面证明，140标签独立普通ABC PASS，故当前25仅r3..5/低迹<=2。该新r6 scope现获Gemini1311有效静态SUCCESS、声明进口下成立、未执行程序，准确范围另记，不能借本节点旧r7/small认可外推。新24强门与r12另设partial节点。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

