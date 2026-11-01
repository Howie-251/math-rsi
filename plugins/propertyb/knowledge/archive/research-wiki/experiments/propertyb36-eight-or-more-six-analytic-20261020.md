---
type: experiment
node_id: exp:propertyb36-eight-or-more-six-analytic-20261020
title: "八六度点：四低共同高点与无quad缺失二低修复"
idea_id: "idea:propertyb36-common-marked-root-excess-20261020"
verdict: partial
confidence: medium
date: "2026-10-20"
hardware: "analytic same-H proof only"
duration: "no new computation"
provenance: "proofs/propertyb35/TWENTYFIVE_EIGHT_OR_MORE_SIX.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/r8_quad/REPORT.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/r8_no_quad/REPORT.md; proofs/propertyb35/THREE_LOW_EDGE_BALANCED_EXTENSION.md; proofs/propertyb35/TWENTYFIVE_MACRO_STAR_COLORING.md; proofs/propertyb35/TWENTYFIVE_NINE_OR_MORE_SIX.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/GROK_R9_RESPONSE.json; context/propertyb35-paper/round01/root/whole_class_followup_20261020/REVIEW_RECONCILIATION.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/GROK_R8_RESPONSE.json; context/propertyb35-paper/round01/root/whole_class_followup_20261020/GEMINI_R8_RESPONSE.json; context/propertyb35-paper/round01/root/whole_class_followup_20261020/REVIEW_RECONCILIATION.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/GROK_R7_SMALL_RESPONSE.json; context/propertyb35-paper/round01/root/whole_class_followup_20261020/GEMINI_R8_R7_SMALL_RETRY1_RESPONSE.json"
added: 2026-10-20T14:44:09Z
tags: ["property-b", "m5-ge36", "r8", "common-budget", "low-trace-defect", "provisional"]
---

# 八六度点：四低共同高点与无quad缺失二低修复

**verdict:** `partial`  ·  **confidence:** `medium`  ·  tests `idea:propertyb36-common-marked-root-excess-20261020`

## Metrics
实际25/35/simple5/pair-cover、恰r8。M17非B共用总高超额t=8，低六星仅A(0,5,1,0)、B(1,3,2,0)、C(1,4,0,1)。C点数0/4/8。C8唯一四低高点Q度>=12而原边总度至多2+9=11；C4共同Q使全高避Q边<=3，真实C中心W<=26及(3,2)型数m<=3，细宏星326W+308m<=9400<10139染色。C0时B数b=1/4/7；b7正t高点通过F3最多盖6低，矛盾。b4四F3单位高pair图仅2P3，两中心t4，删两中心后超额<=17，某B低W<=17。b1唯一B的两F3耗尽t8，第三F3必须共享positive高x；x已覆盖6低，唯一ell1含原B不可用，补缺二低必须用ell2而重复另一F3低pair，矛盾。无新计算、MILP、H搜索或r7拓展。结合已证r>=9，r>=8有完整纸面候选。

## Reasoning
r8的C8/C4/C0实际链已由root与独立Sol核读。Grok1280有效静态SOUND_WITH_DECLARED_IMPORTS于r8，未执行程序或重证M17/宏星进口；它也确认旧r9 s=3摘要应为简单三点图不能各度三，原规范不变。Gemini对M17/TEN/NINE的旧意见本身不覆盖r8，后续1286的准确新增范围如下。
当前审阅以REVIEW_RECONCILIATION.md的14:37 UTC处置为准：Grok1285有效end_turn，实际grok-4.7-build/xhigh，静态读取SMALL/SEVEN及M17/宏星接口，认可声明进口下的r7及small-low-traces新caller；未执行程序或Lean。Gemini授权fresh retry1 cell1286有效SUCCESS，CLI选择gemini-4-argon-high/high，静态全文读取SMALL/SEVEN/EIGHT、宏星和M17六份文件，认可r8、r7及小r低迹门，手核六型概率与实际计数；未运行程序。Root已阅读全文并处置，两者新scope未发现实质问题。更早未完成的调用没有被当作认可，旧范围不自动覆盖后来的caller。实验继续partial，纸面结果保持drafted/provisional口径，不创建或升级verified claim。八个主要开放类仍八，25多六度余r3..6且全部原边低迹<=2；新24四低caller的跨模型scope另记，不并入以上认可。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

