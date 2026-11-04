# 原始来源定位

检索日期 2026-10-15。本轮为工程优化候选选择，非完整论文查新。papers/ 与 literature/ 目录不存在；读现有源码与 Trellis 原始记录后，进行了多组针对 Hall、LCG、support encoding、conditional cardinality、proof logging 的检索。文献说明通用技术，不证明本项目加速。

## 本地原始材料

- D:/科研/math agent/erdos-szekeres-sat-main/state_charging/cardinality_layers.py：state_path_bridge_clauses、materialize_cell 与默认编码。
- D:/科研/math agent/erdos-szekeres-sat-main/state_charging/f3_main_rank.py：当前单锚点 F3 的全部语义与计数定义。
- D:/科研/math agent/erdos-szekeres-sat-main/lib/downset_state_cnf.py：精确 terminal、cell witness、S 一热和 O 双向定义。
- D:/科研/math agent/erdos-szekeres-sat-main/lib/downset_state.py：独立路径重算、35 类型目录与分类。
- D:/科研/math agent/erdos-szekeres-sat-main/tmp/cr_pruning_ablation_20261012/methods.py：F1–F8 实际实现边界。
- D:/科研/math agent/erdos-szekeres-sat-main/tmp/cr_pruning_final_20261013/comparison_064.json：72 项完整初筛/确认原始比较。
- D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/cr-pruning-full-results-20261013.csv：逐项对照数据，计时有历史基线与并发差异。
- D:/科研/math agent/erdos-szekeres-sat-main/tmp/cr_pruning_c6e10_20261013/final_light/comparison_003.json：A[6,10] 三候选最终结果（若所在层级不同，Glob 精确定位同名文件）。
- D:/科研/math agent/erdos-szekeres-sat-main/tmp/f3_main_default_20261013/collected_final/deployment_receipt.json：生产部署证据。

## 权威服务器只读核对

按用户附件连接 /data/ktqiu_hdd/math_agent，未保存凭据进本报告。/opt/anaconda3/envs/forktqiu3/bin/python3.12 可调用。screen 列表有 m，未列出 n；未启动任务。

2026-10-15 读取的服务器源码 SHA256：

- state_charging/cardinality_layers.py = 013cc48189a470cbed9035f77366da7fbf943df53f8cf344bd46e78827a0554f
- state_charging/f3_main_rank.py = d5ea34863e4f7c00b20665c56bff06929e16a86721438434d48d429791287004

与 10 月 13 日生产部署记录一致。服务器 .trellis/scripts/get_context.py 不存在，所以 Trellis 进展从本地任务目录读取；没有把它表述为新服务器验收。旧 C7 的 sealed runtime 早于 F3 默认部署，本轮没有升级它。没有运行求解器、证明检查器或修改 server 文件。

## 原始论文 / 官方出版源

1. Bessiere et al., Decompositions of All Different, Global Cardinality and Related Constraints, IJCAI 2009. https://www.lirmm.fr/~bessiere/Site/stock/ijcai09-alldiff.pdf 。Hall 与有限分解思路，不能把小集合分解说成完整域一致性。
2. Ohrimenko, Stuckey, Codish, Propagation = Lazy Clause Generation, CP 2007. https://people.eng.unimelb.edu.au/pstuckey/papers/cp07a.pdf 。按需输出传播解释。
3. Ohrimenko, Stuckey, Codish, Lazy clause generation in retrospect, 2026. https://link.springer.com/article/10.1007/s10601-026-09390-9 。LCG 的解释子句与后续发展。
4. Boudane et al., Efficient Encodings of Conditional Cardinality Constraints. https://arxiv.org/abs/1804.00211 。不应给计数器全部内部子句随意加守卫；条件编码应验证传播。当前 F3 已把守卫放在输出界，不能据此声称发现 F3 bug。
5. Akgün et al., Exploiting short supports for improved encoding of arbitrary constraints into SAT, CP 2016. https://eprints.whiterose.ac.uk/id/eprint/141516/ 。支持编码可用 UP 实现目标约束的域过滤；具体收益依关系而定。
6. Demeulenaere et al., Compact-Table: Efficiently Filtering Table Constraints with Reversible Sparse Bit-Sets, 2016. https://arxiv.org/abs/1604.06641 。表约束传播、支持残余与位集合。
7. Dekker et al., Towards Modern and Modular SAT for LCG, CP 2025. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CP.2025.42 。IPASIR-UP 集成有工程边界，不能假设现用 AE 自带该接口。
8. Gocht, McCreesh, Nordström, An Auditable Constraint Programming Solver, CP 2022. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CP.2022.25 。较强传播需一并设计认证。
9. Wynn, A comparison of encodings for cardinality constraints in a SAT solver, 2018. https://arxiv.org/abs/1810.12975 。子句数/辅助变量数不充分预测性能。
10. Fleury and Kaufmann, Life span of SAT techniques, 2024. https://arxiv.org/abs/2402.01202 。vivification 等通用技术应考虑与现有 solver 重叠。
11. Kirchweger, Peitl, Szeider, Co-Certificate Learning with SAT Modulo Symmetries, 2023. https://arxiv.org/abs/2306.10427 。证书驱动学习的可借鉴架构，不支持随意重排本项目有序顶点。

检索命中的 frontiersinai.com/ecai/ecai2002/pdf/p0121.pdf 当前重定向到无关网站，已排除，不能引用其检索摘要为读过原文的证据。没有依据文献声称 N01–N10 已在本项目验证或具论文级新颖性。
