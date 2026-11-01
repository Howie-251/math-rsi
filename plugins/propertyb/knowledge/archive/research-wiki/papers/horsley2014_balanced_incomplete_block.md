---
type: paper
node_id: paper:horsley2014_balanced_incomplete_block
title: "On balanced incomplete block designs with specified weak chromatic number"
authors: ["Daniel Horsley", "David A. Pike"]
year: 2014
venue: "Journal of Combinatorial Theory Series A 123, 123–153"
external_ids:
  arxiv: null
  doi: "10.1016/j.jcta.2013.12.004"
  s2: null
tags: ["property-b", "designs", "quantifier-boundary"]
added: 2026-10-19T15:10:23Z
---

# On balanced incomplete block designs with specified weak chromatic number

## One-line thesis
渐近构造具有指定弱染色数/均衡blocking集的设计；存在某设计不等于给定H可染，k5的群大小条件也不含g5。

## Problem / Gap
构造具有指定weak chromatic number或均衡blocking集的设计，研究渐近存在性及整除条件。

## Method
预先限制块的颜色组成，再通过有向边着色图的渐近分解、GDD和Wilson基本构造制造设计。所读Lemma2.3、2.4、5.1不是给定设计的通用重染算法。

## Key Results
Lemma2.3在k≥5时允许g=k−1或g≥2k−2，并要求充分大的群数及相应整除条件。k5时g4或g≥8，均不覆盖g5；Lemma5.1还要求群大小为充分大的20倍数。

## Assumptions
结论的量词是存在满足条件的设计，且带渐近大小及整除假设；GDD的同组点对规则仍必须满足。

## Limitations / Failure Modes
即使参数条件放宽，存在某个可染设计也不能证明当前所有H可染。当前25点五组输入同时不满足相关小参数和对象前提。

## Reusable Ingredients
区分weak与equitable，并用允许块的颜色组成和点对预算检查目标是否相容；不能把目标构造限定当作给定H无损化简。

## Open Questions
是否存在适用于当前五组各5点、内共度2外共度1的有限重染定理？本次定向文献阅读未找到。

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
用于核查量词、参数与前人染色机制，不作为m(5)≥36的直接证明依赖。本次读arXiv:1209.6111v2 §1–2及Lemma5.1相关证明，未逐项重算全部同余代数；回执context/propertyb35-paper/round01/literature/REPORT.md；[原始版本](https://arxiv.org/html/1209.6111v2)。

