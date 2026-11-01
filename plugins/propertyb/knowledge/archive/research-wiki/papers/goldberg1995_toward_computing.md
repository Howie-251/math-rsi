---
type: paper
node_id: paper:goldberg1995_toward_computing
title: "Toward Computing m(4)"
authors: ["Mark K. Goldberg", "Hilton C. Russell"]
year: 1995
venue: "Ars Combinatoria 39:139–148"
external_ids:
  arxiv: null
  doi: null
  s2: null
tags: ["property-b", "historical-source", "author-correction"]
added: 2026-10-06T06:01:30Z
---

# Toward Computing m(4)

## One-line thesis

作者警告若干旧证明有误；本次全页审读还给出了印刷 Lemma 5 的明确反例。

## Problem / Gap

论文研究四元非 Property B 超图的最少边数及固定顶点数下界，以限制不可二染超图的结构。首页后来附加的作者警告要求逐项区分可靠结果与有误的论证。

## Method

正文考察均衡二染划分被哪些超边阻止，并以两条四元边交集为0或3定义辅助图的相邻关系。另使用合并不共边顶点的约化；对于简单超图，合并后去重只保证边数不增加。

## Key Results

作者首页警告明确保留 m_9(4)≥19 的证明，并未声称所有原结论都可靠。本次独立审计以11点、267条四元边的超图反驳p.6印刷 Lemma 5：两条辅助图同分支且非 special pair 的边，共同阻止的均衡染色数仍可为0。该反例已由两套独立有限枚举核验。

## Assumptions

Lemma 5反例满足上下文中的全图不可二染、11点和唯一孤立超边等条件。其构造为Q₀={1,2,3,4}，E={Q₀}∪{Q∈C([11],4):|Q∩Q₀|∈{1,2}}；它是四元历史引理的反例，不是本项目五元目标的反例。

## Limitations / Failure Modes

本次全部10个物理页均已逐页视觉阅读，正文抽取乱码仍不作可读文本。已定位的错误是把辅助图连通性当成任意端点的染色交叠保证；p.4 Lemma 2还漏写影响计数的非单色条件。作者警告没有指认这些具体机制，本次诊断不能冒充作者勘误，也不能扩大为旧论文所有定理皆假。

## Reusable Ingredients

以明确样本空间核对条件计数、逐对确认事件交叠，以及在顶点合并后允许重复边去重，是可用于检查当前证明的具体经验。作者明确保留的 m_9(4)≥19 与本次反驳的 Lemma 5应分别引用。

## Open Questions

当前证明的加权扣除是否逐一来自实际边对，而非仅来自某种连通关系？本次定点核查未发现这一历史错误机制在当前候选中重现，但不以此单项审计宣告主定理完成。

## Claims

_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

[作者原文](https://www.cs.rpi.edu/~goldberg/publications/m-of-4.pdf)、[本地PDF](../../ref/goldberg_russell_1995_toward_m4.pdf)与[全页阅读及反例审计](../../context/HISTORICAL_PITFALL_AUDIT.md)记录当前证据；[较早的首页检查记录](../../context/LATE_HISTORY_AND_BASELINE.md)保留为历史记录。审计为 same-family/provisional；它回答具体错误机制是否重现，不改变本项目T的验收状态。

