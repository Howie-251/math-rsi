# Hypercube Hamilton extension

入口 [mathrsi-hypercube-hamilton](skills/mathrsi-hypercube-hamilton/SKILL.md) 用于超立方体匹配的 Hamilton 路/圈延拓、保标记归约、受控辅助配对、全称森林秩证明、有限几何计划、难余域优先联合编码、同格保守覆盖及极大结构闭合。它提供可接入 MathRSI 五阶段的领域能力；不是只罗列历史 Q6 结果。

历史 Q6 包的 P6 是：每个 Q6 短边匹配、每个自由根 u、每个异奇偶目标 v（允许已覆盖），都有含原匹配的 Hamilton u–v 路。结合显式文献进口，推出 Q6 全匹配圈延拓和任意维至多六方向匹配圈延拓。最终 P6 审计为 `same-family / provisional`，无 Lean；`v3` 维护时的 A10 独立有限复算不提升整题保证等级。

- [数学与接口](skills/mathrsi-hypercube-hamilton/references/mathematics.md)：自由根、保根极大化、森林秩全称桥梁、补全与删除运输。
- [Q7 完整闭合方法](skills/mathrsi-hypercube-hamilton/references/q7-closure-methods.md)：同一配对顺序拼接、ordinary/full/unknown 保守代价、增广结构与保边回代、方向饱和和共同群双面穷尽。
- [Q7 完整证明阅读](knowledge/q7-closure-proof.md)、[准确来源地图](SOURCE_MAP.md)与[完整闭合归档/重放](archive/q7-closure/README.md)。
- [Q7 早期受控配对与 E16 联合闭包方法](skills/mathrsi-hypercube-hamilton/references/q7-methods.md)：实际原伙伴、辅助长边、供体配对因果选择、参数化 `Q₆` `Δ=2` 双桥、`Q₆` `A₈`、大面 `S₆` 基加小面符号孔联合证书及难余域优先停止纪律。
- [失败与修法](skills/mathrsi-hypercube-hamilton/references/failures.md)：源覆盖缺口、缺秩可复用对象、禁对及小切分。
- [A10 与 Q7 有界复现](skills/mathrsi-hypercube-hamilton/references/reproduction.md)：A10 独立 GF2 秩、`v5` S3/S2_STRONG 计划与 `v6` E16 完整随仓包及几何/计划独立核验。
- [Q6 原件归档](archive/README.md) 及 [库存](archive/INVENTORY.json)：正文/源码/报告/账本随仓，大证书流逐项登记省略。
- [Q6 实际使用](evidence/IMPLEMENTATION.md)、[v5 Q7 维护](../../development/evolution/v5-q7-20261114/plugin/IMPLEMENTATION.md) 与 `v6` E16 核验记录（`development/evolution/v6-c4free-rs7-20261117/checks/q7-e16.json`）。

Q7 研究基于 **MathRSI v3 本地适配**推进，前期方法在 v5、完整 E16（≥56 边）在 v6 吸收；2026-11-19 原项目已接受**完整 R7：Q7 任意大小的实际短匹配均可保全部原边延拓为 128 点简单全短 Hamilton 单圈**。新闭合先以 E36 及密层给全部 ≥46 边阈值，再用原图双计数与方向饱和排空极大45边，任意输入只添自由短边成极大超匹配，遂接回同一原 M。E16 的 56 边结果保留为历史里程碑；当前完整结论不再受该阈值限制。原项目等级保持 **sound-modulo-imports / same-family / provisional**，无 Lean 或外部同行认证。

**P7 指定端点路径、任意维七方向提升、任意长边匹配和一般维猜想仍在范围外。** Fink–Hotmar Theorem5 要求 P_d，不能仅凭 R7 调用。μ 是原孔切面的最小绝对物理两色差，不是匹配方向数。

新 [Q7 完整闭合包](archive/q7-closure/README.md) 接入全部匹配大小的原题回代；它来自 lite 档案，E38 核心保留而旧层部分大证书省略。E38 新结构重放与完整传递证书重放分别报告，不能用核心复验或文件一致性冒称全部旧层从零重算。本次纳入是主线维护和经验吸收，不追认历史运行版本。

[Q7 E16 精选原件与基线合包](archive/q7-e16/README.md) 保留完整 E16 证明、全部 290 份已合入基线导入文件及独立几何/计划核验入口（统一省略 10 份大 `.cnf`/`.drup` 原轨迹与 Windows `.exe`，登记于 `archive/q7-e16/INVENTORY.json`；哈希清单不代替 DRUP 轨迹重放）；`v5` 快照 [archive/q7](archive/q7/README.md) 保持只读不动。旧 E16/q7 归档中的开放叙述按日期阅读，不覆盖当前完整 R7。新问题的 wiki、证书和日志写自身工作区；历史 Q7 对话或 Goal 状态不启动任何新研究。
