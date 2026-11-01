---
type: experiment
node_id: exp:propertyb36-twentythree-r13-restricted-three-low-20261020
title: "23点r13：实际三低选边与完整76401键闭合"
idea_id: "idea:propertyb36-common-marked-root-excess-20261020"
verdict: partial
confidence: medium
date: "2026-10-20"
hardware: "local deterministic exact arithmetic and original-H proof"
duration: "independent 76401 keys CPU2.814529 seconds"
provenance: "context/propertyb35-paper/round01/root/whole_class_followup_20261020/twentythree_three_low/REPORT.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/twentythree_three_low/independent/AUDIT.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/twentythree_three_low/independent/RESULT.json; context/propertyb35-paper/round01/root/whole_class_followup_20261020/ROOT_ACCEPTANCE.md"
added: 2026-10-20T16:27:26Z
tags: ["property-b", "m5-ge36", "twentythree", "r13", "three-low", "independent-replay", "provisional"]
---

# 23点r13：实际三低选边与完整76401键闭合

**verdict:** `partial`  ·  **confidence:** `medium`  ·  tests `idea:propertyb36-common-marked-root-excess-20261020`

## Metrics
四低门先给非B低迹<=3和r<=13；r13迫26条三低、9纯高、全部低对共度1。十高总度97，选实际度7/8/9高点与任意low同边，另一high任意d>=7。低行excess2的完整三低零低重复域，U7/8/9分别20798/26419/29184键，全76401strict；U8/U9的d<U键亦全含。独立另七模式笛卡尔积重建完整域，逐34实际原边索引重算所选证书、自由组/固定组/组内扣交，逐键费用全同；最大23173/24310与21005/21879。

## Reasoning
root已全文读REPORT和independent/AUDIT，核实际H到r13低迹及高点选择、全部未知d与原补色接口，认可完整纸面候选。独立仅进口已验四低门、14单星计数与同色四集扣表，不调用生产生成/费用函数，不枚举H。新scope跨家族审阅待；准确23delta6仅余r<=12，r12九个必要残键未排，不能把四低旧双静态意见外推r13。partial相对全36，不创建verified claim。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

