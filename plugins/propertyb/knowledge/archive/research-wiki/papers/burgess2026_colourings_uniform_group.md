---
type: paper
node_id: paper:burgess2026_colourings_uniform_group
title: "Colourings of Uniform Group Divisible Designs and Maximum Packings"
authors: ["Andrea C. Burgess", "Peter Danziger", "Diane Donovan", "Tara Kemp", "James G. Lefevre", "David A. Pike", "E. Şule Yazıcı"]
year: 2026
venue: "Journal of Combinatorial Designs"
external_ids:
  arxiv: null
  doi: "10.1002/jcd.70019"
  s2: null
tags: ["property-b", "group-divisible-design", "applicability-boundary"]
added: 2026-10-19T15:10:23Z
---

# Colourings of Uniform Group Divisible Designs and Maximum Packings

## One-line thesis
arXiv2510.05375v1的Thm4.4对TD(k+2,g)且k>ceil(g/2)给组均衡二染；当前a5非TD且TD(5,5)也缺严格阈值。点对唯一锚点机制为可迁移启发。

## Problem / Gap
研究uniform GDD与maximum packing的weak、block-equitable和group-equitable染色，这些条件有不同量词和对象域。

## Method
所读arXiv:2510.05375v1 §4.2通过锚点块标签正规化、标签二分和一群反色，利用TD跨组点对唯一性排除单色块。另有从已有小设计膨胀构造新设计的结果，不能据此重染任意给定设计。

## Key Results
v1 Theorem4.4：g≥4且k>ceil(g/2)时，每个TD(k+2,g)有指定的group-equitable二染结论。TD(5,5)对应k=3，严格条件3>3不成立；当前a5 H本身也不是TD。

## Assumptions
原始GDD同组点对不在块内；TD每块对每组恰取一点。当前H同组点对共度2，不能只因有五组就调用TD/GDD定理。

## Limitations / Failure Modes
Lemma2.3控制跨组单色点对数，不能自动保持weak合法性。Theorem4.6构造某个设计的存在性不等于任意已给H可染；v1与出版版本编号不混用。

## Reusable Ingredients
给锚点邻点按实际共边标号：非锚边内若两不同原组点同标签，会违反跨组点对唯一性。这项必要约束可迁移，原完整色族保证不能直接迁移。

## Open Questions
允许同组重复且锚组点不具唯一标签时，能否选择某个好锚点并修复其受限染色？固定锚0失败不否定存在好锚。

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
明确排除把更强block-equitable结论当作无损规范化；当前a5类其实不可能所有边均2/3。实际阅读范围为v1 §1、§2相关引理、§3.2及§4.2，详细回执context/propertyb35-paper/round01/literature/REPORT.md；[原始版本](https://arxiv.org/html/2510.05375v1)。

