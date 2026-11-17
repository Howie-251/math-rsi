# Hypercube Hamilton extension

入口 [mathrsi-hypercube-hamilton](skills/mathrsi-hypercube-hamilton/SKILL.md) 用于超立方体匹配的 Hamilton 路/圈延拓、保标记归约、受控辅助配对、全称森林秩证明、有限几何计划、难余域优先联合编码及局部极大域正证书。它提供可接入 MathRSI 五阶段的领域能力；不是只罗列历史 Q6 结果。

历史 Q6 包的 P6 是：每个 Q6 短边匹配、每个自由根 u、每个异奇偶目标 v（允许已覆盖），都有含原匹配的 Hamilton u–v 路。结合显式文献进口，推出 Q6 全匹配圈延拓和任意维至多六方向匹配圈延拓。最终 P6 审计为 `same-family / provisional`，无 Lean；`v3` 维护时的 A10 独立有限复算不提升整题保证等级。

- [数学与接口](skills/mathrsi-hypercube-hamilton/references/mathematics.md)：自由根、保根极大化、森林秩全称桥梁、补全与删除运输。
- [Q7 受控配对与 E16 联合闭包方法](skills/mathrsi-hypercube-hamilton/references/q7-methods.md)：实际原伙伴、辅助长边、供体配对因果选择、参数化 `Q₆` `Δ=2` 双桥、`Q₆` `A₈`、大面 `S₆` 基加小面符号孔联合证书及难余域优先停止纪律。
- [失败与修法](skills/mathrsi-hypercube-hamilton/references/failures.md)：源覆盖缺口、缺秩可复用对象、禁对及小切分。
- [A10 与 Q7 有界复现](skills/mathrsi-hypercube-hamilton/references/reproduction.md)：A10 独立 GF2 秩、`v5` S3/S2_STRONG 计划与 `v6` E16 完整随仓包及几何/计划独立核验。
- [Q6 原件归档](archive/README.md) 及 [库存](archive/INVENTORY.json)：正文/源码/报告/账本随仓，大证书流逐项登记省略。
- [Q6 实际使用](evidence/IMPLEMENTATION.md)、[v5 Q7 维护](../../development/evolution/v5-q7-20261114/plugin/IMPLEMENTATION.md) 与 `v6` E16 核验记录（`development/evolution/v6-c4free-rs7-20261117/checks/q7-e16.json`）。

Q7 研究基于 `MathRSI v3` 本地适配推进，前期成果在 `v5` 吸收，完整 **E16（`≥56` 边）** 闭包及难余域优先方法在 `v6` 吸收。当前已证范围为 **Q7 每个至少 56 边（至多 16 个原孔）短匹配的 Hamilton 圈延拓**（涵盖 E14、相邻原孔增广及独立孔 `μ ∈ {0,1,2,3,4}` 全部五族，独立 16 孔奇偶/重量界排除 `μ ≥ 5`；整证审计为 `PASS · same-family · provisional · sound-modulo-imports`）。偶数孔层 18–38（`≤55` 边）、完整 Q7（`R₇`）、自由根路径 `P₇` 和任意维七方向提升仍开放。`μ` 是原孔切面的最小绝对两色差，不是匹配方向数；Fink–Hotmar 的方向提升需要 `P_d`，不能仅凭 `R_d` 调用。

[Q7 E16 精选原件与基线合包](archive/q7-e16/README.md) 保留完整 E16 证明、全部 290 份已合入基线导入文件及独立几何/计划核验入口（统一省略 10 份大 `.cnf`/`.drup` 原轨迹与 Windows `.exe`，登记于 `archive/q7-e16/INVENTORY.json`；哈希清单不代替 DRUP 轨迹重放）；`v5` 快照 [archive/q7](archive/q7/README.md) 保持只读不动。新问题的 wiki、证书和日志写自身工作区；历史 Q7 对话或 Goal 状态不启动任何新研究。
