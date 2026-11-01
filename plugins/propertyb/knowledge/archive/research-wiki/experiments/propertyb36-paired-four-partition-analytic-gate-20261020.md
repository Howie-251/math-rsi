---
type: experiment
node_id: exp:propertyb36-paired-four-partition-analytic-gate-20261020
title: "19点配对补色工具：解析15228与完整锐门12324"
idea_id: "idea:propertyb36-common-marked-root-excess-20261020"
verdict: partial
confidence: medium
date: "2026-10-20"
hardware: "local exact integer arithmetic and original-H paper derivation"
duration: "independent full labeled domain and IE CPU0.246136 seconds"
provenance: "context/propertyb35-paper/round01/root/whole_class_followup_20261020/paired_four_partition/REPORT.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/paired_four_partition/sharp_gate/REPORT.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/paired_four_partition/independent_sharp/REPORT.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/paired_four_partition/independent_sharp/RESULT.json; proofs/propertyb35/TWENTYFOUR_FOUR_LOW_EDGE.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/REVIEW_RECONCILIATION.md"
added: 2026-10-20T15:38:08Z
tags: ["property-b", "m5-ge36", "paired-partitions", "exact-IE", "actual-caller", "provisional"]
---

# 19点配对补色工具：解析15228与完整锐门12324

**verdict:** `partial`  ·  **confidence:** `medium`  ·  tests `idea:propertyb36-common-marked-root-excess-20261020`

## Metrics
S=X disjoint-union T，|X|16、|T|3，在S19均匀9蓝10红，N92378。P/Q为同一X上的任意两份4x4划分；两个待补中心分别有其四块星，并共同连接T。准确联合补色失败<=15228（通用上界，不声称锐界）。单划分冲突5226，T红/蓝强迫计数3120/3528，交624/264；粗根界10986+5226=16212亦成立。共同块数c=0/1/2/4分别给14388/15228/15144/11874；c2只在根并上扣一次924交，不重扣其余事件。完整覆盖是行整数分拆3+1/2+2/2+1+1/1+1+1+1及c四分，无新矩阵域。
实际caller若已核固定费用68068、v补色7722，则16212已给92002<92378，余376；用15228得91018，余1360。旧v费用8346配15228也严格91642，余736。这些数值门不代替实际原边分类。
新24点实际规范TWENTYFOUR_FOUR_LOW_EDGE.md现已存在：24点至多35简单五边pair-cover，任意原边至少含四名六度点即可染；因此非B全部低迹<=3，且六度点数<=12，即r>=13子类可染。实际内部重复图按辐条及低低匹配穷尽；有辐条两类界87532/89767，无辐条c0/c1/c2界89693/87871/92002，全部小于92378。该规范实际使用16212已足够，15228为通用加强而非其必要依赖。r13末端准确三低边26条、非低关联52，而11名非低点各需至少五条三低边，要求55矛盾。
后继锐门另完整生成465行排序类/43轨，主字面计数与独立逐格10147全标号矩阵+完整行列群+块事件容斥全项一致。43根并/蓝core/红core/总数、43轨大小及465运输逐项一致，最大12324仅全1矩阵取等，分解10452+1296+576；独立CPU0.246136。该独立证据是新锐门全域核，不与较早解析15228四分混淆。

## Reasoning
partial同时记录通用两划分联合补色工具及其新24点四低原边实际caller，仍相对完整m(5)>=36而非整24点验收。通用15228只靠共同块数的解析四分与一次合法根交；新24规范额外保留六度点唯一重复邻点、低低匹配/辐条、每组真实原边分类及最后Bool补色。第五点可以也是六度点，未预设其degree或先选无重复三中心。
新24四低原边及r≥13范围已获Grok1301有效end_turn（grok-4.7-build/xhigh）与Gemini1302有效SUCCESS（CLI gemini-4-argon-high/high）的本scope静态数学审阅；root全文核两回应，未发现实质错误。两者没有执行程序、没有重跑92378样本；原始响应为whole_class_followup_20261020/{GROK,GEMINI}_TWENTYFOUR_FOUR_LOW_RESPONSE.json，元数据位于response.structuredContent。审阅不覆盖通用15228加强、当时尚未送审的12324锐门或23外重复门，也不覆盖新24三低结论、全24或36；没有创建或升级claim。后继强三低与r12共同预算规范已使原24最小度六的其余输入压至一至十一个低点且全部低迹<=3，八主要类仍开，完整m(5)>=36未证。本文不声称重跑新24小核；数值证据以规范引用的FOUR_LOW_EDGE_CHECK.json及旧92378字面核为准。无新H枚举、矩阵域或Lean；本节点仍以相对完整36的partial结论保存，不替代正式proof-checker验收。
15:30收口：12324已有独立全43容斥与10147标号域PASS；Grok新基础三低回应有效静态认可基础criterion及7/7、7/8，未执行程序。新红组+三低强门+r12整链Grok1312仍在途，不把基础意见外推。完整36未证，节点继续partial，不创建verified claim。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

