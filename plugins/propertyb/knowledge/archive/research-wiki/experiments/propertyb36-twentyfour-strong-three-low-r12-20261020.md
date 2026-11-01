---
type: experiment
node_id: exp:propertyb36-twentyfour-strong-three-low-r12-20261020
title: "24点强三低补色与至少十二六度点的共同预算闭合"
idea_id: "idea:propertyb36-common-marked-root-excess-20261020"
verdict: partial
confidence: medium
date: "2026-10-20"
hardware: "local exact integer arithmetic and original-H paper derivation"
duration: "paper proof and bounded exact arithmetic"
provenance: "proofs/propertyb35/TWENTYFOUR_THREE_LOW_SEVEN.md; proofs/propertyb35/TWENTYFOUR_TWELVE_OR_MORE_SIX.md; proofs/propertyb35/MONOCHROMATIC_FOUR_SET_OVERLAP.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/twentyfour_three_low/UNION_REFINEMENT.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/twentyfour_three_low/UNION_RESULT.json; context/propertyb35-paper/round01/root/whole_class_followup_20261020/paired_four_partition/independent_sharp/RESULT.json; context/propertyb35-paper/round01/root/whole_class_followup_20261020/GROK_TWENTYFOUR_THREE_LOW_RESPONSE.json; context/propertyb35-paper/round01/root/whole_class_followup_20261020/REVIEW_RECONCILIATION.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/GROK_TWENTYFOUR_R12_RESPONSE.json; context/propertyb35-paper/round01/root/whole_class_followup_20261020/GEMINI_TWENTYFOUR_R12_RESPONSE.json"
added: 2026-10-20T16:15:16Z
tags: ["property-b", "m5-ge36", "twentyfour", "shared-budget", "r12", "strong-three-low", "provisional"]
---

# 24点强三低补色与至少十二六度点的共同预算闭合

**verdict:** `partial`  ·  **confidence:** `medium`  ·  tests `idea:propertyb36-common-marked-root-excess-20261020`

## Metrics
24点至多35简单五边pair-cover。固定颜色组内部union解析扣红六1595、红七2035、蓝七及以上616，原边索引分组互不重复。任三six+7+d原边可染，最坏92328/92378余50；三six+8+8/9/10全strict。非B含8的F3须alpha0,p0,s8=0,sbig2/3,d_big>=9+s。r12逐低行迫qLL0/3/6、n1=0；共同高点行3a+2b=12+K，N8<=K>=11<=12-2q。q3/q6度预算矛盾；q0 A/B/C与inactive共同row预算迫唯一big，末端big11/a3=8/K12使F3的3low全重复big，强门迫big>=12，矛盾。结合四低>=13门，实际>=12six可染，非B仅r1..11/低迹<=3。

## Reasoning
root已全文核新actual H链、固定组扣交、q0/3/6穷尽和末端重复预算。Grok1312有效end_turn（root实测grok-4.7-build/xhigh），完整静态读红组/强三低/r12三规范，手核覆盖与共同收费，SOUND_WITH_DECLARED_IMPORTS；Gemini1313有效SUCCESS，CLI gemini-4-argon-high/high，静态全文读红组/基础三低/强三低/r12四规范，声明进口下认可。两者均未执行程序，进口基础三低/旧四低及配对12324；root已读两完整回应。旧摘要S外笔误正确S内，规范原本正确。后继r11已root全文核另设节点，新scope跨审待；不能借本r12意见覆盖r11。partial相对完整36，不创建verified claim。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

