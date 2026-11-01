---
type: experiment
node_id: exp:propertyb36-critical-low-edge-minblue-three-centres-20261020
title: "24最小度七：同一极小蓝删边源至少三个三正集中心"
idea_id: "idea:propertyb36-common-marked-root-excess-20261020"
verdict: partial
confidence: medium
date: "2026-10-20"
hardware: "local exact integer arithmetic and original-H paper derivation"
duration: "paper derivation and bounded exact arithmetic"
provenance: "proofs/propertyb35/CRITICAL_LOW_EDGE_MINIMAL_BLUE_SOURCE.md; context/propertyb35-paper/round01/twentyfive/LOW_EDGE_REPAIR_INTERFACE.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/ROOT_ACCEPTANCE.md; context/propertyb35-paper/round01/root/whole_class_followup_20261020/GEMINI_TWENTYTHREE_ALL_FOUR_LOW_RESPONSE.json"
added: 2026-10-20T16:27:26Z
tags: ["property-b", "m5-ge36", "twentyfour", "min7", "critical-source", "minimal-blue", "conditional"]
---

# 24最小度七：同一极小蓝删边源至少三个三正集中心

**verdict:** `partial`  ·  **confidence:** `medium`  ·  tests `idea:propertyb36-common-marked-root-excess-20261020`

## Metrics
实际24/M34或35/paircover/min7，critical删低总度原边G且G含>=4七度。对所有proper H\G且G全红的染色取最小蓝类：10b+3P+2n2+n3+exB=4(M-1)，异色盈余X=4(M-1)+2(n2+n3)-b(24-b)。M34 b<=12；M35 b13时P0/X<=5，每个m_g4贡献5份互异cross盈余，故至多一m4，其余m<=3。因此同一源至少3名七度中心m<=3。

## Reasoning
root规范修正旧Gemini两处摘要：slack遍历全部非正g边；少量允许点的正出现数不自动排单向击中。Gemini1323有效SUCCESS，CLI gemini-4-argon-high/high，全文静态读新规范1..155行，明确纠正两处旧摘要并手核10b恒等式、异色盈余X、M34 b<=12及M35 b13时X<=5、至多一个m4，认可至少三个中心m<=3；未运行程序。root已全文读有效回应。这里只得到同一真实源态，后续联合修复尚未证明，24delta7仍开放；partial相对完整36。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

