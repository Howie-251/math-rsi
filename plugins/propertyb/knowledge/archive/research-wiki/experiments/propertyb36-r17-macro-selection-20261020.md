---
type: experiment
node_id: exp:propertyb36-r17-macro-selection-20261020
title: "十七六度点：整除选型与真实低W中心"
idea_id: ""
verdict: yes
confidence: high
date: "2026-10-20"
hardware: "analytic original-H proof; existing exact macro gate"
duration: "paper derivation only; no new enumeration"
provenance: "proofs/propertyb35/TWENTYFIVE_MANY_SIX.md §§1–6; proofs/propertyb35/TWENTYFIVE_MACRO_STAR_COLORING.md; proofs/propertyb35/TWENTYFIVE_FIVE_LOW_EDGE.md; context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/R17_MACRO_GATE.md; context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/GEMINI_RECONCILIATION.md; context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/GEMINI_R17_RESPONSE.json; context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/GROK_R17_PLUS_RESPONSE.json"
added: 2026-10-20T14:04:22Z
tags: ["property-b", "m5-ge36", "r17", "macro-star", "incidence-divisibility", "actual-caller"]
---

# 十七六度点：整除选型与真实低W中心

**verdict:** `yes`  ·  **confidence:** `high`

## Metrics
Scope: exactly r=17 degree-six points in an actual 25-vertex, 35-distinct-5-edge pair-cover H. If a five-low original edge exists, use the earlier five-low theorem; otherwise the analytic macro selection below completes this exact r17 subclass.
Without a five-low edge, every low point is pair-type (one l2 plus five l4 incident edges) or triple-type (two l3 plus four l4). Integrality forces p=8 pair-type vertices, nine triple-type vertices, and original-edge inventory (n2,n3,n4)=(4,6,19): 29 low-containing edges and six high-only edges.
For each high pair, common low traces are disjoint; at most four have size two, so at most seven low-containing common edges and total pair codegree lambda<=13. Any actual triple-type low center has high-block sizes (2,2,1,1,1,1), hence Wz<=2(13-1)=24<=25. The imported W<=25 macro gate returns an actual Bool coloring. No new enumeration or numerical experiment was needed.

## Reasoning
verdict=yes applies only to the exact r17 subclass, not to all 25-point inputs or the full m(5)>=36 goal. Root and Sol checked the complete original-H derivation and the actual macro-gate hypotheses. Combining this new r17 result with the earlier r>=18 theorem closes r>=17, without asserting that r17 must contain a five-low edge.
The reusable mechanism is per-low-point defect classification, common incidence divisibility, and disjoint low traces on one actual high pair; it selects a real low-W center rather than separately optimizing incompatible local views. It avoids continuing the earlier nine r21 design cases.
Review update: GEMINI_R17_RESPONSE.json is a valid SUCCESS. Root read its full response: Gemini independently confirmed p=8, the low-trace inventory (4,6,19), high-pair codegree<=13, and a real triple-type low center with W<=24. The response explicitly imports the existing W<=25 macro gate and five-low theorem; it performed static mathematical review and did not execute programs. This is completed cross-family static review of the new r17 derivation, with the declared earlier gates retained as imports. Together with the two earlier valid Gemini responses for the three-low/five-low/r>=18 chain, the three responses cover r>=17; they are not three independent reviewers. Grok cell1261 has now returned a valid end_turn: actual grok-4.7-build/xhigh, statically accepting the declared-import r>=17 chain; see GROK_R17_PLUS_RESPONSE.json. It did not execute the 264-orbit/literal/macro programs. This old scope does not cover M17, r>=9, or r8. No Lean theorem or claim node is created.
Eight major classes remain open. The general 25-point many-low branch now has r=3..16 and no five-low original edge; the other conditional W gates do not provide unconditional coverage of that range. Full m(5)>=36 remains unproved.

Later-scope navigation only: the separately recorded shared-budget r>=9 and new r8 analytic extension reduce the current 25-point residual to r3..7; this original r17 experiment and its mathematical evidence remain unchanged.

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

