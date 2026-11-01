---
type: idea
node_id: idea:propertyb-five-33-edge-threshold
title: "已证明：33条五元边必然可二染色"
stage: archived
outcome: positive
added: 2026-10-13T07:48:37Z
based_on: ["paper:grill2024_improved_lower_bounds", "paper:ferber2019_quantitative_lovász_criterion"]
target_gaps: ["gap:G5"]
tags: ["property-b", "follow-up", "lean"]
---

# 已证明：33条五元边必然可二染色

**stage:** `archived`  ·  **outcome:** `positive`

T33端到端形式证明完成，得到m(5)≥34；原Goal交付文件同步收齐。

## Thesis
原目标任意有限简单五元超图≤33边可二染色，现已由Aris4Math.propertyB_of_at_most_thirty_three证明。原题量词、最小反例归约、19–25点全部分支、真实数据与染色见证全部闭合；显式1138-job Main构建及ReviewAudit33独立原题审计均通过。正式claim:propertyb-m5-ge34；阅读PROOF_PACKAGE_33.html，交接HANDOFF_FOR_REVIEW_33.md。阶段探索原记录保留于context/propertyb33/、experiments及final-audit/WIKI_IDEA_HISTORY.md。

## Key risks
精确m(5)尚未确定；下界34不等于34边反例。Grok与Gemini最终审阅只是查错证据；标准Lean内核证明、命题对齐和外部复现分别报告。不重开已完成T33，不自动研究T34。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

