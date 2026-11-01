---
type: paper
node_id: paper:radhakrishnan2000_improved_bounds_algorithms
title: "Improved Bounds and Algorithms for Hypergraph Two-coloring"
authors: ["Jaikumar Radhakrishnan", "Aravind Srinivasan"]
year: 2000
venue: "Random Structures & Algorithms 16(1):4–32"
external_ids:
  arxiv: null
  doi: null
  s2: null
tags: ["property-b", "recoloring", "asymptotic-bounds"]
added: 2026-10-06T06:01:30Z
---

# Improved Bounds and Algorithms for Hypergraph Two-coloring

## One-line thesis
随机初始染色加慢速重染证明渐近下界；保留归责事件积分可得到适用于有限均匀度的概率条件。

## Problem / Gap

改进n-一致超图二染色的边数与局部相交阈值，并给出算法及去随机化分析。其随机初始染色后修复的路线，与后来从单色初态出发的随机贪心不同。

## Method

本地PDF p.4的slow recoloring：先独立公平二染色，再独立生成连续均匀延迟及Bernoulli-p开关；按延迟逐点扫描，只对属于初始单色且当前仍单色边、开关为1的顶点翻色。

pp.5–7将失败分成初始单色边仍未修复，以及重染后新生单色边。后者归责于触发翻色的另一条边；连续逐点版本只有单点交边对可能贡献，真实归责事件被可计算事件包含。

## Key Results

p.7给出充分大n下0.7√(n/ln n)2^n的全局阈值；p.13给出相应0.17常数的局部阈值。不能直接以这两个渐近常数认证n=5。

保留pp.6–7 Claims 2.1–2.4的积分，并按实际无序单交边对上界Γ求和，可得到Aglave Lemma 4.4使用的有限表达式：

B=2^(1−n)M(1−p)^n+4Γ·2^(1−2n)p∫₀¹(1−p²x²)^(n−1)dx。

B<1保证存在合法二染色。有理p时积分可按Σ_{j=0}^{n−1}(−1)^j binom(n−1,j)p^(2j)/(2j+1)精确计算。

## Assumptions

有限n-一致超图；初始颜色、延迟、开关独立。上述单交事件结论适用于连续逐点重染版本。Γ为无序边对数，系数4包含两个方向和两种颜色；若用有序γ=2Γ，相应系数为2γ。局部版pp.12–13中的D包含边自身，与Pluhár的“其他边数”约定不同。

## Limitations / Failure Modes

本地27页版本pp.1–27（含参考文献及附录）由文献分工完整阅读，pp.6、7、13视觉核对。正式期刊页为4–32，不能按本地PDF页号直接平移期刊引用。

pp.8–10离散延迟允许同批多个顶点翻色，此时大于1的边交也可能贡献归责事件，不能沿用连续版本的单交结论。去随机化、特殊相交族和大n结果各有条件；完整阅读没有升级为所有定理的独立审计。

## Reusable Ingredients

区分真实失败事件、归责见证与并集上界；保留积分得到有限参数条件；明确边对方向、颜色因子与算法版本。Aglave的28边证明提供了一次结构计数与该概率式结合的实例。

## Open Questions

本项目后续可比较不同算法的有限概率界，但不能将RS的重染事件直接代入锁点随机贪心公式。G1负责统一事件接口，G3负责扣除与min的合法组合。

## Claims

本页不创建claim节点。Aglave参数的精确复算记录在既有阅读笔记，其算术验证与结构适用性分别说明。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project

是Aglave有限m(5)下界的概率来源，也是区分算法模型的重要参照。[本地原文](../../ref/radhakrishnan_srinivasan_2000_two_coloring.pdf)，27页；[早期原文笔记](../../context/EARLY_HISTORY_AND_SOURCES.md)的RS部分给出页码、积分和精确代入；[Aglave论文页](aglave2020_improved_bounds_uniform.md)记录后续有限参数应用。

