---
type: experiment
node_id: exp:propertyb36-marked-partition-m17-20261020
title: "共同标记两划分：17304支持全核与三低M17门"
idea_id: "idea:propertyb36-common-marked-root-excess-20261020"
verdict: partial
confidence: medium
date: "2026-10-20"
hardware: "local exact finite arithmetic and original-H paper derivation"
duration: "bounded local replay; no new H search"
provenance: "proofs/propertyb35/THREE_LOW_EDGE_BALANCED_EXTENSION.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/marked_partition/PROOF.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/marked_partition/RESULT.json; context/propertyb35-paper/round01/root/whole_class_followup_20261020/marked_partition/independent/REPORT.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/marked_partition/independent/COMPARISON.json; context/propertyb35-paper/round01/root/whole_class_followup_20261020/GEMINI_R9_RETRY1_RESPONSE.json; context/propertyb35-paper/round01/root/whole_class_followup_20261020/GROK_R9_RESPONSE.json; context/propertyb35-paper/round01/root/whole_class_followup_20261020/REVIEW_RECONCILIATION.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/GROK_R8_RESPONSE.json; context/propertyb35-paper/round01/root/whole_class_followup_20261020/GEMINI_R8_RESPONSE.json; context/propertyb35-paper/round01/root/whole_class_followup_20261020/REVIEW_RECONCILIATION.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/GROK_R7_SMALL_RESPONSE.json; context/propertyb35-paper/round01/root/whole_class_followup_20261020/GEMINI_R8_R7_SMALL_RETRY1_RESPONSE.json"
added: 2026-10-20T14:44:09Z
tags: ["property-b", "m5-ge36", "marked-partitions", "common-budget", "r-ge9", "provisional"]
---

# 共同标记两划分：17304支持全核与三低M17门

**verdict:** `partial`  ·  **confidence:** `medium`  ·  tests `idea:propertyb36-common-marked-root-excess-20261020`

## Metrics
冻结完整264个5x5行列和4交矩阵。主实现全17304正格四匹配支持；独立列优先20点展开、另行匹配生成及2239230个字面六红子集，全部支持K、264个maxK和见证逐项一致。最小J-15maxK=324（source262，J624、K20）；17304支持代表112089个带点标签四横截集，不混用口径。独立full CPU0.017558秒，comparison0.041161秒。实际25/35/pair-cover三低共边G的q=D-5alpha<=17门已成稿；不要求三个中心为全部低点。

## Reasoning
M17/TEN/NINE已有Gemini1274有效SUCCESS（CLI gemini-4-argon-high/high）与Grok1275有效end_turn（grok-4.7-build/xhigh），均静态SOUND_WITH_DECLARED_IMPORTS，未执行程序；进口264交矩阵/J与17304标记/K、旧W门的范围保持。Grok旧r9 s=3摘要不当，正确是三重顶点t均3、其余t零，所有边只能在简单三点图内，不可能各度三；规范原论证正确，Grok1280后续明确确认更正。后续r8、r7及small各有新scope，不能由旧返回外推。
当前审阅以REVIEW_RECONCILIATION.md的14:37 UTC处置为准：Grok1285有效end_turn，实际grok-4.7-build/xhigh，静态读取SMALL/SEVEN及M17/宏星接口，认可声明进口下的r7及small-low-traces新caller；未执行程序或Lean。Gemini授权fresh retry1 cell1286有效SUCCESS，CLI选择gemini-4-argon-high/high，静态全文读取SMALL/SEVEN/EIGHT、宏星和M17六份文件，认可r8、r7及小r低迹门，手核六型概率与实际计数；未运行程序。Root已阅读全文并处置，两者新scope未发现实质问题。更早未完成的调用没有被当作认可，旧范围不自动覆盖后来的caller。实验继续partial，纸面结果保持drafted/provisional口径，不创建或升级verified claim。八个主要开放类仍八，25多六度余r3..6且全部原边低迹<=2；新24四低caller的跨模型scope另记，不并入以上认可。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

