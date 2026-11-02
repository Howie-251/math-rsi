---
id: ddp-open-parameter-construction-20261026
type: idea
status: proposed-research-goal
scope: "4<=Delta<=12; D in {3,4,5}; simple undirected graphs"
---
# 多参数度数—直径构造：让机制选择适合的参数

这是待执行研究策略，不是已证claim。用户决定不再将N(8,2)作为唯一固定目标。旧构造确实已做过，问题不是“未尝试正向”，而是固定参数下有效机制没有完成。

本轮选题池27格，首批12格见项目内`context/dd-portfolio-20261026/SCOPE_AND_CASES.md`，基线快照见`registry/cases.json`。真正主成果是完整图改善最新公开下界，或一个参数族的统一新下界；不强制证明最优。

建议机制：小商图/电压覆盖、非等长轨道/陪集、仿射纤维路由。每次先给完整生成定义和待解决覆盖义务，再选择能越过基线的参数。默认最多两条主要机制，不为每格建长期独立大SAT。

继承旧wiki中的失败范围与方法，不将D=2的具体定理搬成D>=3限制。n61端口/谱、n62–65和缺陷3总体推广本轮暂停。当前没有新图，不将准备包里的5张已知图算作成功。

关系建议：references→ddp-record-sources-20261026；uses→ddp-counterexample-gates-20261026；uses→ddp-known-baselines-20261026；context_from→现有dd82历史节点。按真实helper/schema入库，不凭这些名称新建重复节点。
