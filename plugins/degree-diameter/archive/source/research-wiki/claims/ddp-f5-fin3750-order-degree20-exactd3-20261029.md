---
type: claim
node_id: claim:ddp-f5-fin3750-order-degree20-exactd3-20261029
name: "具体Fin3750公式图：阶数3750、最大度≤20、直径恰3"
description: "Kernel-verified fixed deterministic formula graph witnesses N(20,3)>=3750; latest-global novelty remains unconfirmed."
node_type: claim
status: verified
provenance: "research/ddp/refresh_20261029/f5_full_d20_D3/PROOF_AUDIT.json"
tags: ["degree-diameter", "Lean-kernel", "fixed-formula-graph", "diameter3"]
date: 2026-10-29
added: 2026-10-29T17:00:19Z
---

# 具体Fin3750公式图：阶数3750、最大度≤20、直径恰3

**status:** `verified`

## Statement
固定 `DegreeDiameter.Portfolio.F5Graph3750.graph : SimpleGraph (Fin 3750)` 满足：

- 顶点数为3750；
- 对每个顶点u，`graph.degree u ≤ 20`；
- 对每个u,v，存在真实图上Walk，长度≤3；并且存在一对顶点没有长度≤2的Walk，故直径恰3。

这是具体确定性参数图的存在见证，给出数学下界 `N(20,3) ≥ 3750`。
最终无参数、无额外前提的Lean定理为 `concrete_order_degree_and_D3` 与 `diameter_exact_three_in_project_definition`。

## Honest scope
只针对本节点所链接的固定30控制器、F5矩阵／方向／逆端口字面参数以及编码 `125*a+x0+5*x1+25*x2` 定义的公式图，不是一般F5族或任意输入图定理。真实直径使用项目定义 `DiameterAtMost G D := ∀u v, ∃p : G.Walk u v, p.length ≤ D`；未另称mathlib字面ediam定理。

Lean没有解析并证明磁盘ASCII边表等于公式图，也没有证明所有顶点度数恰20。二者均不影响本次阶数／最大度／真实直径构造见证；Goal允许确定性生成器与字面参数。边表本身已有独立全3750根验收，但不能把它写成Lean文本解析定理。

最新全球纪录、最优性与公开采用未确认。已核对published2783的比较与本数学下界分账；旧103个confirmed主表图并未因此获得Lean证明，整个Goal未据此完成。

## Evidence chain
证明出生依据：[proof-checker审计](../../research/ddp/refresh_20261029/f5_full_d20_D3/PROOF_AUDIT.json)，`proof_axis_status=verified`、`deterministic_kernel_verdict=PASS`、fatal/critical均0。

- [最终编译与公理回执](../../research/ddp/refresh_20261029/f5_full_d20_D3/FINAL_COMPILE_RESULT.json)：最终decoder与exact批均COMPLETE、相关模块exit0；900控制器单元、4500 NB decoder与500 adjacent decoder已在kernel核验。
- [输入绑定](../../research/ddp/refresh_20261029/f5_full_d20_D3/FORMAL_INPUT_BINDING_CHECK.json)：controller、matrix、direction、inversePort四组字面数据与PARAMETERS匹配；坐标／噪声公式与生成器匹配。
- [完整成功源快照](../../research/ddp/refresh_20261029/f5_full_d20_D3/FORMAL_FINAL_SOURCES)、[证明骨架](../../research/ddp/refresh_20261029/f5_full_d20_D3/PROOF_SKELETON.md)与[审计正文](../../research/ddp/refresh_20261029/f5_full_d20_D3/PROOF_AUDIT.md)。

两个最终定理仅依赖 `propext`、`Classical.choice`、`Quot.sound`；没有sorry、新增公理或native_decide。fresh只读语义审阅标same-family/provisional，确定性验收依据是实际Lean kernel，不以模型同意、论文或Python输出代替证明。本次Wiki写入没有重编译、BFS或求解。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

