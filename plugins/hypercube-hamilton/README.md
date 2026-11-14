# Hypercube Hamilton extension

入口 [mathrsi-hypercube-hamilton](skills/mathrsi-hypercube-hamilton/SKILL.md)用于超立方体匹配的Hamilton路/圈延拓、保标记归约、受控辅助配对、全称森林秩证明、有限几何计划及局部极大域正证书。它提供可接入MathRSI五阶段的领域能力；不是只罗列历史Q6结果。

历史Q6包的P6是：每个Q6短边匹配、每个自由根u、每个异奇偶目标v（允许已覆盖），都有含原匹配的Hamilton u–v路。结合显式文献进口，推出Q6全匹配圈延拓和任意维至多六方向匹配圈延拓。最终P6审计为same-family/provisional，无Lean；v3维护时的A10独立有限复算不提升整题保证等级。

- [数学与接口](skills/mathrsi-hypercube-hamilton/references/mathematics.md)：自由根、保根极大化、森林秩全称桥梁、补全与删除运输。
- [Q7受控配对与几何计划](skills/mathrsi-hypercube-hamilton/references/q7-methods.md)：实际原伙伴、辅助长边、供体配对因果选择、两返回、固定/条件计划和真实池系数。
- [失败与修法](skills/mathrsi-hypercube-hamilton/references/failures.md)：源覆盖缺口、缺秩可复用对象、禁对及小切分。
- [A10完整有界复现](skills/mathrsi-hypercube-hamilton/references/reproduction.md)：1024森林、1048576连通位和独立GF2秩；不只读metadata。
- [原件归档](archive/README.md)及[库存](archive/INVENTORY.json)：正文/源码/报告/账本随仓，大证书流逐项登记省略。现仓库不能重算全部P6大流，不宣称全题replay-ready。
- [Q6实际使用](evidence/IMPLEMENTATION.md)：原维护命令、退出码与准确范围。v5的Q7插件使用和工具运行见[本轮维护](../../development/evolution/v5-q7-20261114/plugin/IMPLEMENTATION.md)。

Q7研究基于MathRSI v3本地适配推进，方法在v5吸收。已证范围是Q7每个至少57边匹配的圈延拓；56边层完整μ2、μ4及若干μ3整族。完整Q7、P7和七方向仍开放。μ是原孔切面的最小绝对两色差，不是匹配方向数。Fink–Hotmar的方向提升需要P_d，不能仅凭R_d调用。

新的[Q7精选原件与可移植复验](archive/q7/README.md)保留真实证明、消费者与输入；[Q7有界复现](skills/mathrsi-hypercube-hamilton/references/reproduction.md#q7固定计划与多省略核)说明具体命令和范围。该精选不冒称完整原研究24k条目都随仓，也不升级原same-family/provisional审计。旧Q6入口、A10与局部极大正证书能力保留。

archive原件只读。新问题的wiki、证书和日志写自身工作区；历史Q7对话或Goal状态不启动任何新研究。
