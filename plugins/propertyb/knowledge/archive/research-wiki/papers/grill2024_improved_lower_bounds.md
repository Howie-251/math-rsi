---
type: paper
node_id: paper:grill2024_improved_lower_bounds
title: "Improved Lower Bounds for Property B"
authors: ["Karl Grill", "Daniel Linzmayer"]
year: 2024
venue: "arXiv:2403.05674; local version v3"
external_ids:
  arxiv: "2403.05674"
  doi: null
  s2: null
tags: ["property-b", "random-greedy", "finite-vertices", "locked-vertices"]
added: 2026-10-06T06:01:30Z
---

# Improved Lower Bounds for Property B

## One-line thesis
通过有限顶点数的离散随机贪心与锁定低度顶点，证明 m(5)≥32 等小均匀度下界；未排除本项目的32边情形。

## Problem / Gap

研究非二染色 n-一致超图的最少边数 m(n)，并引入固定顶点数 m(n,v)。对小 n，保留有限顶点数与边的共同出现信息，可以改进不依赖 v 的渐近分析。引言 pp.1–2 说明此问题与已有上下界。

## Method

pp.3–4 分析随机贪心失败所必需的临界顶点：同一点是某边末点、另一边首点。式(6)为连续权重上界，式(8)为均匀随机排列的离散上界；γ计数有序单点交边对。p.6 将低度顶点固定在中心位置，p.7 进一步控制两个、三个标记顶点的精确边型 l_A 与包含计数 L_A。p.5 说明计算使用C和GNU libgmp，以共同分母转成精确整数运算。

## Key Results

p.7 Theorem 1 给出 m(5)≥32、m(6)≥64、m(7)≥128、m(8)≥263、m(9)≥538。m(5)≥32排除的是至多31边；没有排除本项目的32边。

p.6 Table 1 的未锁定离散方法对n=5得到30，单锁定得到31，三锁定再到32。pp.8–10 Theorem 2研究v=2n+1下的Catalan阈值和两个特殊偶数n族；不适用于本项目n=5、v=22或23的直接排除。

## Assumptions

有限简单n-一致超图；随机性来自顶点排列。p.2 的pair-covering是固定边数上限后再取顶点数最小的反例所满足的条件，不是任意固定v超图的性质。L_A表示含A的边数，l_A表示与标记集合交恰为A的边数，不能互换。

## Limitations / Failure Modes

本地v3共12页，已由文献阅读分工完整阅读pp.1–12，并视觉核对pp.6–8；这不是对全部有限计算的独立证明审计。本地PDF没有代码清单、仓库链接或嵌入附件。2026-10-06补查[arXiv v3源包](https://arxiv.org/src/2403.05674v3)：实际只有gzip压缩的单个[PropB.tex](../../ref/source_packages/grill_linzmayer_2403_05674/PropB.tex)，未附C/GMP程序；不据此判断作者从未在其他位置公开代码。

p.6锁点公式、p.7的n=6计数和p.8的L_0分母文字存在需要谨慎转写的位置，具体观察及相称修正见[后期笔记](../../context/LATE_HISTORY_AND_BASELINE.md)。不能据局部笔误否定整个定理，也不能把本项目统一多锁定公式和link扣除归为原文现成结论。

## Reusable Ingredients

可复用：p.2最小反例顶点合并、Schönheim双层取整界和平衡染色界；pp.3–4的临界事件与逐位置min；pp.6–7的低度锁点和精确边型组织。新的条件分布仍须重新推导，各位置必须重新比较A_k、B_k、C_k，而非把C_k的变化量直接从总和扣除。

## Open Questions

项目待办G1–G4见[gap map](../gap_map.md)：独立重建统一概率式、保证结构选点与枚举覆盖、审计link扣除及活跃最小项、闭合全部v情形。原文结尾还讨论增加锁点数量与渐近改进的可能性；该建议不等于已证明新渐近界。

## Claims

本页只记录文献定理及本项目依赖范围，不创建claim节点。m(5)≥32的文献来源与m(5)≥33的项目目标分开存放。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

核心基准文献。[本地原文](../../ref/grill_linzmayer_2024_improved_lower_bounds_property_b.pdf)，12页，arXiv:2403.05674v3；作者仅Karl Grill和Daniel Linzmayer，TU Wien是机构。

阅读与页码证据：[后期记录及原文基线](../../context/LATE_HISTORY_AND_BASELINE.md)；32边候选的独立归属：[主任务书阅读笔记](../../context/MAIN_TASK_READING.md)。正式目标以项目单独维护的规格为准。
