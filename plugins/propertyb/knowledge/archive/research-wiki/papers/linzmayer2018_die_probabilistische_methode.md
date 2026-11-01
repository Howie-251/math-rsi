---
type: paper
node_id: paper:linzmayer2018_die_probabilistische_methode
title: "Die probabilistische Methode in der Kombinatorik"
authors: ["Daniel Linzmayer"]
year: 2018
venue: "TU Wien diploma thesis"
external_ids:
  arxiv: null
  doi: "10.34726/hss.2018.54401"
  s2: null
tags: ["property-b", "heuristic-search", "thesis"]
added: 2026-10-06T08:09:30Z
---

# Die probabilistische Methode in der Kombinatorik

## One-line thesis

学位论文以概率方法和模拟退火研究 Property B，并给出11、12点五元超图的66边构造。

## Problem / Gap

论文综述组合学中的概率方法，并在第10章研究小参数非 Property B 超图的构造搜索。其2018年背景界为29≤m(5)≤51，不能将这个历史数值当成当前最优下界。

## Method

第10章固定边数，以未被单色边覆盖的二分划分数作为目标函数，通过替换边进行 simulated annealing。实现用位集表示边并维护划分计数；目标值为零时得到一份候选不可二染边集，搜索未命中不证明不存在。

## Key Results

§10.2.1（pp.74–77）报告 m(5,11)=m(5,12)=66；Appendix A（p.80）列出两份66边构造。本轮阅读来源中的论证与边表，但没有独立重跑这两份构造的染色穷举。

## Assumptions

这里 m(5,v) 固定顶点数v，不能与不限制顶点数的 m(5) 混用。构造的成功检查需要覆盖全部二染划分，而不是只覆盖一个抽样子集。

## Limitations / Failure Modes

本地PDF共93页；已读题名、摘要、目录，§8 pp.57–59、第10章 pp.71–78、结论p.79及Appendix A p.80。其他章节及附录代码未全文阅读；没有取得32边反例或≥33证明。

## Reusable Ingredients

固定边数的划分覆盖模型、模拟退火目标函数及可单独核验的显式边表，可用于理解既有反例搜索；任何新的候选边集仍应独立检查 Property B。

## Open Questions

独立枚举能否复核 Appendix A 的两份66边边表及其顶点标签？本轮没有将该复算作为当前主证明的依赖。

## Claims

_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

[TU Wien机构库](https://repositum.tuwien.at/handle/20.500.12708/3487)、[本地PDF](../../ref/linzmayer_2018_probabilistische_methode.pdf)及[阅读记录](../../context/search_latest_bounds_20261006.md)提供既有启发式搜索的原始证据；这是2018年 diploma thesis，并非博士论文。其固定11、12点结果不反驳本项目在所有顶点数上的目标。

