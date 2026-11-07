# 失败、证据与恢复入口

以下原件都在当前克隆，历史指令只说明当时发生的事。外层维护与解题分开，新研究不得改archive或直接改base。

| 触发/失败 | 实际改变的动作 | 不能推出什么 | 原件 |
|---|---|---|---|
| 固定异常→固定缺态charging被SAT反例击穿 | 复用模型止损，换e/m总基数命题，允许不同构型缺不同普通态 | 不表示一个共同模型同时占满全部普通态 | [50格审计](../../../archive/source/working/package/proofs/source-tree/reports/state_charging_transition_ordinary_matrix_20260901.md)、[精确分区](../../../archive/source/working/package/proofs/source-tree/reports/state_charging_qeq_exact_partition_20260902.md) |
| 逐锚点投影可含伪环 | 回同一母体实际支持，嵌入共同点对偏序排环 | 未给公共不变量不能宣称合法增广 | [R5](../../../archive/source/working/package/proofs/source-tree/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R5_COVER_AUGMENTATION_CAPACITY.md) |
| 首点移末翻符号保packet却BBBR→RRRR | 同时证明weak运输和合法chart；限原最左pivot实际操作 | packet合法不意味着保weak/短帽，内部pivot也未获许可 | [R20](../../../archive/source/working/package/proofs/source-tree/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md) |
| 残余R6两两相交命题失败 | 先证明两不交R6并集12点的完整有限入口，再核实际220色反例和canonical扩展 | 不反驳带近满H条件的新引理 | [D12](../../../archive/source/working/package/proofs/source-tree/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_ALL_CLASS_RESIDUAL_AUDIT_AND_DISJOINT_R6_COUNTEREXAMPLE_20261027.md) |
| 局部修补被核增大抵消 | 对原母体算净收益；保整族排除与条件工具，换共同饱和层级 | 不以细分数量宣称全局下降 | [R1–R27审计](../../../archive/source/working/package/proofs/source-tree/RESEARCH_REVIEW_R1_R27_20261026.md) |
| 旧W漏掉根落锁集的低前驱 | 收全ℛ，同批点剪枝损失换对侧合法扩核收益，固定一份M结算 | 左右各有匹配不表示击中同一条中间路径 | [完整低前驱](../../../archive/source/working/package/proofs/source-tree/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMPLETE_LOW_PREDECESSOR_COMPENSATION_AND_UPPER_BOUND_20261103.md) |
| 外部Closure只达固定schema/规则层 | 分列对象→赋值→实际CNF→证明→接受各箭头，缺哪条就补哪条 | Joint17固定RUP通过不证明全signotope C49迁移 | [Closure REPORT](../../../archive/source/working/package/proofs/source-tree/tmp/n7_global_proof_completion_20261027/closure/REPORT.md) |

## b25的历史接受怎样使用

[sat-756目录](../../../archive/source/working/package/proofs/sat-756/README.md)含55反例类注册表和95份小型文档/源码/收据原件。全部原CNF、DRAT/LRAT/GRAT证明主体及对应checker可执行不在包中；证明字节登记总和3,878,666,467,578。`checker_receipt_local_available`是原盘点字段，不能推本包有同样数量完整独立日志。A88完整GRAT/gratchk与后续C8人类接受有不同阶段语义，早中断checker不计。元数据中backend/effort不明继续不明，human acceptance保留same-family/provisional。

[原cardinality证明](../../../archive/source/working/package/proofs/sat-756/evidence/E01/cardinality-layer-theorem.md)描述反例lifting。E03/E04/E05/E06/E23给颜色、terminal、状态、基数与剪枝；不能按旧标签`no_red_5_path`猜极性，实际true红。compact外路径标记仅单向闭包，另需精确terminal计数。新引理/剪枝必须对实际原对象必要；schema正确与固定公式UNSAT各不能独自承担覆盖。

有真实重放请求时先列当前缺输入和资源，再在任务副本执行匹配的封存runtime。默认此插件只读历史接受与收据，不安装大求解环境、不外联取得TB数据、不重跑55单元。下界TSV小核验可立即执行，见certificate技能；它成功不能给上界任何新增credit。

## 来源状态与读者表述

可写：“历史受限容量25接受；本次独立检查一个25点抽象见证；新结构工作稿给40/50/75/76、继而几何≤77，独立复审尚缺；旧76/77/78链保留历史。” 不写“本插件已证明ES≤78”或“55SAT直接证明78”。新75/76原证明已完整随[新archive](../../../archive/n7-20261103/README.md)保存，仍是same-session/unreviewed/unaccepted。新方法与失败的实际输入见[取等执行说明](equality-exchange.md)，维护不提升验收。

[完整报告](../../../archive/source/source/report.md)是读者数学入口，[CURRENT](../../../archive/source/working/package/proofs/CURRENT.md)导航后续稿，E32两Lean摘录属于Schroeder比较，缺其导入模块，不能当本项目Lean。原figures有杯帽/weak示意、35状态/异常状态、共同匹配及结果关系，说明旁应保留各自数学指标与保证状态。

## 新原稿中的失败怎样直接改变任务

先用[equality-exchange §6](equality-exchange.md)的11点双红块反例，拒绝不带有效增强根/临界饱和的“私有供应必兼容”；保留这些额外假设的新问题。再用10点canonical例拒绝仅据两次单点成功提出的联合增广，转而核含两新点的全部混合路径。两个例由tools/check_strategy_examples.py直接重建，无需旧作者机器。

目标从n=3b+1换成n=3b时，重新算覆盖预算：regular共根可能多一单位，严格交错的核可保留owner，分离共根的同端B3+R5只有8。分别交还预算、核身份、实际延长义务，不把旧取等全文直接搬到新层。regular共同根加权式只覆盖明确根序子类，正through≤74也只是子类，不扩成无条件≤74。
