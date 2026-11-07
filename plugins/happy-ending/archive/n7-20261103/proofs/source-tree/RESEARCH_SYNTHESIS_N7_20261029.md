# N_sig(7,r,s) 研究综合与策略审计：共同饱和与完整路径重分划

日期：2026-10-29。范围截至本地可得的 R1–R27、10月26–29日后续主稿、原始证据与 b25 接受记录。**当前实际可用的结构草稿链仍是40/50/80/81。研究呈现显著的局部优化倾向，但这不证明结构路线已经耗尽。** 最近两轮确实排除了共同等号中的完整子类；剩余问题仍是同一个近极值母体的完整供应能否共同实现，尚未得到新的全类容量下降。

本报告由主会话组织判断、核对来源并确定建议，native Sol/high 文档执行者负责忠实整理及机械检查。它审计研究策略和证据，不作逐条历史证明的重新认证。全部最新数学仍 **unreviewed/unaccepted**；旧结构稿没有因 b25 的接受而被连带接受。用户明确选择仅在当前会话完成综合，不向外部 Claude 发送材料。本轮没有独立审阅、科学运行、求解或证明重放。

建议将**同一 H–R 的共同饱和排除**作为主线，保留**实际完整路径的全局重分划**为真正竞争架构；平衡严格性承担支持和有限储备工作。要继续的是能进入完整近极值类的定理，不是不断增加剩余约束的名称。

## 1. 模型、有效输入与当前传播链

\(N_{\rm sig}(n,r,s)\) 是完整有序 rank-3 signotope 中同时避免蓝 \(r\) 链、红 \(s\) 链和 weak \(n\) 的最大规模。每个四点包按 abc/abd/acd/bcd 至多变色一次；路径长度按顶点计。weak 比较同一对**实际首末点**的两色路径，长度和达到 \(n+2\)，不要求内部不交。任何诱导配置的路径、最大秩和状态都须重新计算，不能直接继承 ambient 身份。

令 \(a=16\)、\(b=25\) 分别是有效747、756上界；\(C=N_{\rm sig}(7,6,6)\)、\(Q=N_{\rm sig}(7,6,7)\)、\(F=N_{\rm sig}(7,7,7)\)。\(D\) 专指残余类容量：无 B5、无 weak7，且内部 \(\operatorname{End}_{R5}\cap\operatorname{Src}_{B4}=\varnothing\)。后文中性实际集合统一记 \(D_0\)，避免把它与容量 \(D\) 混用。符号 b 是容量上界，不自动宣称精确等号。

b25 的 [C8人工接受记录](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md>)明确 C1–C10 全部 accepted、pending为空，限定完整有序rank-3、B5/R6/weak7避免域，保证仍为 same-family/provisional；实际 reviewer backend/model/effort 未核实。实际25点构造是另一条存在性证据，见下方R23及后续满核原件，不能由“上界已接受”替代，也不能把10月26日的接受倒写进更早轮次。

以下结构式按其原草稿层级使用。

| 结构接口 | 正确范围与意义 |
|---|---|
| 边界严格覆盖 | \(n\ge4,4\le r\le n\) 时，\(N(n,r,n)\le N(n,r-1,n)+N(n,r,n-1)-1\)。不能无条件套到766。 |
| 平衡拆分 | \(p\ge3\) 时，\(N(n,p+1,p+1)\le2N(n,p,p+1)\)，给 \(C\le2b\)。 |
| canonical H–R | \(n\ge6\) 时，实际不交分解给 \(Q_n\le C_n+D_n\)。七点残余以至多五点横截全部实际 R6，故 \(D\le b+5\)。 |
| 精确根归约 | \(n\ge4\) 时一般等帽关系 \(N(n,n,n)=N(n,n-1,n)+1\)，七点即 \(F=Q+1\)。 |

于是

\[
N_{757}\le a+b-1=40,\qquad C\le2b=50,
\qquad Q\le C+b+5\le80,\qquad F=Q+1\le81.
\]

几何强迫阈值沿对应关系是 \(\mathrm{ES}(7)\le F+1\)，所以本项目现链对应82。普通态参考

\[
O(n,r,s)=\sum_{j=n-s}^{r-2}\binom{n-2}{j}
\]

在757/766/767/777分别为26/30/31/32；它们不是已证明的一般完整模型上界。R12可分解类的精确普通容量也不自动控制任意prime叶。

## 2. 从历史台账看真正的架构变化

R5首次用实际覆盖、无环点对支持和合法增广兑现严格交叠一点；R7将766与残余真正分开，并用实际五横截改变相加架构；R20精确根归约消除了777独立双倍传播。它们改变的是全局组织。b29→28→26→25则是输入改进，应分别记功。

同一历史口径下，初始45/58/103/206，经R5变44/58/101/201，R6在b28下43/56/98/195，R7同输入43/56/89/177，R8采用b26为41/52/83/165，R20为41/52/83/84，R23采用b25为40/50/80/81。数字记录当时输入与草稿链，不是精确容量或外部新纪录。下面逐字保留昨日台账，原始入口也完整保留；其中“新增0”仅指当轮没有新增全局数值下降。
更早的后继参数研究也应计入，而不能把R1当全部起点。[10月16日状态可达性稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/757-766-mathematical-structure-20261016.md>)证明757的56个、766的70个形式downset各自可在小合法配置实现，非空构造至多8点；不同状态用不同母体，不是近满共同实现，也未宣称几何可实现。[同日红六端点稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/757-red-six-fan-gap-20261016.md>)以实际端点T属747、补集S属756给16+历史29=45，共同起点加强仍有条件。10月19日原四轮见[完整归档](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/README.md>)及[第四轮总结](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/snapshot/STAGE_SUMMARY.md>)：均未独立接受、全局收益0，留下源终条件缺额、交叠／hole运输和双向状态式；曾纠正异常面积Φ≥19与Φ≤14冲突，状态增长可复用同一hole、所选尾并集也不能直接按25收费。旧45点c10..13、58点c14/15是已被新输入取代的目标尺度，不是b25下现存极值。INITIAL_BASELINE按b29重建45/58/103/206；更早八九月756工作是上游输入，不另算后继架构突破。

## 3. R1–R27完整台账

以下逐行提取自[10月26日综合的原表](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_REVIEW_R1_R27_20261026.md>)，保留每轮primary入口；所有数字按历史口径阅读。“新增0”只指该轮结构没有新增全局数值下降，不抹掉条件类覆盖价值。

| 轮次与原始稿 | 主要工作与留下的东西 | 全局数值或准确边界 |
|---|---|---|
| [R1](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESTART_SETTING_ANALYSIS.md>) | 状态单射、径向切口、共同外端目录；指出压缩后纤维容量未知 | 45/58/103/206；新增 0 |
| [R2](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R2_COMMON_START_CAPACITY.md>) | 共同起点纤维非 Markov；777 中 $K=N-1$ 仍未给容量下降 | 新增 0 |
| [R3](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R3_BIDIRECTIONAL_IDEAL_INTERVALS.md>) | 双向理想区间精化，投影容量未降 | 新增 0 |
| [R4](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R4_BIDIRECTIONAL_COVER_DEFICIT.md>) | 实际覆盖与缺额取等；缺严格正值 | 新增 0 |
| [R5](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R5_COVER_AUGMENTATION_CAPACITY.md>) | 全局点对序、无环支持、合法增广，首次严格 −1 | 44/58/101/201，结构收益真实进入全局草稿 |
| [R6](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R6_OVERLAP_TWO_AND_766_TRANSFER.md>) | 一般 n 推广；第二单位仍不普适 | b28 输入传播为 43/56/98/195；固定旧输入的新数值收益 0 |
| [R7](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md>) | 真实不交 H–R 残余和五点横截，改变相加架构 | b28 下 43/56/89/177 |
| [R8](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R8_UNIFORM_DEFICIT_AND_JOINT_CAPACITY.md>) | 联合资源预算，未强迫新缺额 | b26 外部输入传播为 41/52/83/165 |
| [R9](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R9_RESOURCE_STABILITY_AND_TRANSVERSAL_COST.md>) | 可达簇与资源稳定性；粗容量 300 不能兑现 | 新增 0 |
| [R10](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R10_EXIT_WITNESSES_AND_CORE_TRANSVERSALS.md>) | 共同尾窗、出口替换；有条件改善，无一般入口 | 新增 0 |
| [R11](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R11_OWNER_CERTIFICATES_AND_JOINT_DEFICIT.md>) | owner 证书、全源至多 15 等限制；未迫正需求 | 新增 0 |
| [R12](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R12_COMMON_REALIZABILITY_AND_UNIFORM_DEFICIT.md>) | 可分类精确 O；一般正超额定位到 prime 叶 | 新增 0；全类 prime 容量仍未知 |
| [R13](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R13_GLOBAL_STRUCTURE_AND_JOINT_CAPACITY.md>) | 边界超图与 mixed triples 强制必要修复需求 | 缺修复成本上界；新增 0 |
| [R14](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R14_JOINT_REALIZABILITY_AND_GLOBAL_DEFICIT.md>) | 双锚点、完整空侧修复优化恰回 $M-J$ | 该预算路线无净收益；新增 0 |
| [R15](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R15_GLOBAL_COMPATIBILITY_AND_UNIFORM_DEFICIT.md>) | 全端点 frontier 与 Σ 上界；没有正需求下界 | 新增 0 |
| [R16](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R16_TERMINAL_FRONTIERS_AND_JOINT_STATE_REALIZABILITY.md>) | 桥匹配条件、真实十点 Σ=0 校准 | 条件性收益无普适前提；新增 0 |
| [R17](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R17_GLOBAL_CO_SATURATION_AND_CAPACITY_TRADEOFFS.md>) | 匹配数与真实删除成本可相差大；节省抵消旧 slack | 反例族 $p\ge4,n\ge2p-1$，不是766反例；新增 0 |
| [R18](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R18_GLOBAL_SATURATION_AND_IRREDUCIBLE_CAPACITY.md>) | 真实22点需两次修复；特定 fan 强迫三个缺态 | fan 前提未覆盖全类；新增 0 |
| [R19](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R19_GLOBAL_REALIZABILITY_AND_CAPACITY_ARCHITECTURE.md>) | 共同26核与全部最小横截，暴露重用及多供应 | 新增 0 |
| [R20](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>) | 全 chart 精确一点归约；H–R 全路径接口 | b26 下 41/52/83/84，777 从165降84；不等于文献新纪录 |
| [R21](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R21_GLOBAL_CAPACITY_AND_SUPPLY_REALIZABILITY.md>) | D 双核与 sweep；自由规范化、短帽保持均不成立 | 新增 0 |
| [R22](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R22_GLOBAL_ARCHITECTURE_AND_CAPACITY_REALIZABILITY.md>) | 可逆 root chart 与 record 表示 | 表示完整不等于新增排除；新增 0 |
| [R23](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md>) | 非平凡中点类精确30、经典满容量 pair 供应、25点多目录 | b25 工作输入传播 40/50/80/81；本轮结构新增 0 |
| [R24](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R24_GLOBAL_COMPATIBILITY_AND_EXTREMAL_REALIZATION.md>) | 排除整个 X80 的 q=11 人口支；非中点30族全插入临界 | q=1…10 保留；新增 0 |
| [R25](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R25_GLOBAL_EXTREMAL_STRUCTURE_AND_JOINT_REALIZABILITY.md>) | 排除 X80 嵌入 m 或 m′=11…15；旧 fan 模块整类仍30 | m,m′=5…10 与 $m+m'+q-w\ge15$ 无矛盾；新增 0 |
| [R26](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R26_GLOBAL_BREAKTHROUGHS_AND_EXTREMAL_COUNTERTESTS.md>) | 全 X 内禀锁定预算、proper cut 类46、critical16 等价 | 正反预算不能相加；临界16开放；新增 0 |
| [R27](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R27_GLOBAL_REALIZABILITY_AND_SATURATED_CORE_COUNTERTESTS.md>) | 任意经典满核两整族的全合法 chart 排除；十点 lacing 反例；完整 π/e 表示 | canonical 删除零净收益；一般 critical16 未闭；新增 0 |

## 4. 10月26–27日：证据前进与容量未闭合须同时记账

昨日[综合报告](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_SYNTHESIS_N7_20261028.md>)整理了balanced49、Through14、Joint17、Closure与D7连续工作。其历史条目无需重新命名为新突破；本次着重保留决定现状的证据边界。

[balanced49迁移稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/BALANCED49_TRANSFER_AND_JOINT_DEFICIT_20261026.md>)区分几何结论与signotope语义。后续[共同赋值稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/BALANCED49_COMMON_ASSIGNMENT_AND_REMAINING_H49_BRANCH_20261027.md>)接通Through14指定原始证据，并指出满Y删一加二存在R6本就是b25所迫，不能再当独立入口。Through14的[固定字节回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/balanced49_abstract_port_20261026/through14_replay_result.json>)与Joint17的[公式绑定](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/balanced49_remaining_hr_20261027/joint17_binding/result.json>)各保其原范围；全类语义仍是未独审、未接受的手写迁移。

[Joint17完整result](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_proof_completion_20261027/joint17/result.json>)是固定公式strict-RUP PASS，59479源子句、102563添加步骤并推出空子句；这是已完成的证据，不能继续说它仍待重放。但从任意目标母体到同一公式赋值的全类运输，仍须按[全缺额联合稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_GLOBAL_DEFICIT_FRAME_AND_JOINT_THEOREM_20261027.md>)的原层级阅读。

[Closure result](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_proof_completion_20261027/closure/result.json>)的PASS只核schema，明确 `UNSAT_checked=false`、`actual_cnf_equality_checked=false`。[获取停止回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_proof_completion_20261027/closure_acquisition/abort_receipt.json>)是 `ABORTED_BUDGET_FEASIBILITY`，`CNF_binding=false`。实际完整Literal/CNF/proof绑定没有闭合，故C49不可用。固定公式反驳、规则有效性、全类语义运输和人工接受是四条不同证据边，不能互相替代。文档检查和有限fixture也不属于接受。

反例应只结束它实际否定的机制。完整[D12主稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_ALL_CLASS_RESIDUAL_AUDIT_AND_DISJOINT_R6_COUNTEREXAMPLE_20261027.md>)及[直接语义回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/sat_semantics.json>)给出不交R6，否定残余红六两两相交；其零成本实际分块也说明端点区间成本并非全路径成本下界。[D26共同扩张稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/D7_JOINT_EXTENSIONS_AND_H49_COMMON_CORE_20261027.md>)和[完整核查](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_joint_extensions_hr_20261027/single_root26/sat_semantic_result.json>)给出Y25+a，a同时入出R6、τ=1、α=25、Y内e=m=2，结束单外根刚性。

[空锁普适稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_EMPTY_LOCK_UNIVERSALITY_AND_OPERATION_LIMITS_20261028.md>)把任意D残余嵌入H单点的canonical母体，说明空锁标签本身没有缩小残余类。D7完整30点的E5/E6分支在[执行报告](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_global_exchange_semantics_20261027/README.md>)中仍超时未决。这些都不是H50或X80反例，不能从小H普适嵌入外推大H共同饱和必可实现。

读这些来源还要区分“完整实际实例”和“全类定理”。例如满25内部private见证反例确实保留完整颜色、packet和所有路径，足以推翻无双满前提的普遍端点化；它并未给同一766的50点母体。lex稿的纸面反例有完整定义，但当轮机器执行不可用，不能援引邻稿机器通过来填补其执行记录。全尾六点枚举中某些关键前提没有触发，应照原稿保留真空边界；不能用大量枚举数量掩盖它没有检验近满共同兼容这一事实。固定fixture与一般参数证明各自承担不同作用。

同样，Through14与Joint17的固定公式结果是有效资产，不应因为全类运输未审而抹掉；但反向也不能因为公式PASS而把所有后续范围当成已认证。最新端点刚性的参数化证明与条件数字窗口分开：前者在共同等号和既有结构接口下给双预算等号、五端点；m9/10等数值还依赖旧语义运输。研究时可条件使用该窗口，报告时必须保留依赖，不能声称已无条件穷尽所有m分支。

## 5. 10月28–29日十份主稿：逐项结算而不重复分支

下表按主稿组织；各A/B/C分支是同一次生成的来源，不当成相互独立的突破或审阅。

| 主稿 | 新的实质或准确停止处 |
|---|---|
| [统一全尾区间稳定性，10月28日](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_UNIFORM_TAIL_INTERVAL_STABILITY_20261028.md>) | 全尾结构、区间条件与完整路径障碍对偶被明确化；小规模有限一致性通过。没有四近满核共同不相容、严格缺额或z4。 |
| [最优交叠交换与切口接口，10月28日](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_OPTIMAL_OVERLAP_EXCHANGE_AND_CUT_INTERFACES_20261028.md>) | 完整实际暴露族与切口判据；小例否定局部贪心完备、private-only认证和最近点对压缩。需要批量交换，未迫全类正收益。 |
| [lex最优覆盖与耦合成本，10月28日](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LEX_OPTIMAL_COVERS_AND_COUPLED_PARTITION_COST_20261028.md>) | 等成本交换和净收益公式成立于明确前提；全类正规化、安全回填单调性被纸面完整反例否定。本稿有限机器执行未完成，不填作通过。 |
| [近容量兼容与双向重分配，10月28日](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_NEAR_CAPACITY_COMPATIBILITY_AND_BIDIRECTIONAL_REPARTITION_20261028.md>) | 逐位置插入与双向搬移保留完整路径；小规模母体可核查。人口headroom不自动保证接收核安全，全类存在性仍缺。 |
| [满容量内部插入与路径交换屏障，10月28日](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_FULL_CAPACITY_INTERNAL_INSERTIONS_AND_PATH_EXCHANGE_BARRIER_20261028.md>) | 满25也有仅内部private见证；同端路径可能须同时替换p−1个内部点。否定单满核自动端点化与普遍小步交换，未排双满临界类。 |
| [饱和接口匹配与临界支持，10月28日](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_SATURATED_INTERFACE_MATCHINGS_AND_CRITICAL_OBSTRUCTION_SUPPORTS_20261028.md>) | 实际端点图与完整MUS内部某些区间共享签名被约束。Hall不等于独占支持；未证明一般MUS进入这些签名，纯红分支仍开。 |
| [完整pair扇与紧核二分，10月29日](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_FULL_PAIR_FAN_BOUNDARY_AND_TIGHT_CORE_DICHOTOMY_20261029.md>) | 完整支持上的紧／严格Hall二分及缺角接口具体化；没有证明临界母体必有低边界载体，也未迫所有实际边进入某完美匹配。 |
| [H50–R30共同饱和与全支持，10月29日](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_H50_R30_COMMON_SATURATION_AND_FULL_SUPPORT_BARRIERS_20261029.md>) | 同母体共享P的两个满25核及mixed路径定位，三有序R5支持由旧工具组合。缺同一实际pair；内部插入曾漏新三元组，已修正。 |
| [neutral-through残余增广与MUS，10月29日](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_NEUTRAL_THROUGH_RESIDUAL_AUGMENTATION_AND_MUS_SUPPORT_20261029.md>) | canonical满H下实际增广给条件loss=w，排共同等号全部w≥1支；完整MUS unique-private支持也有真排除。仍无一般z4或X80排除。 |
| [残余端点刚性与强制等号，10月29日](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_RESIDUAL_ENDPOINT_RIGIDITY_AND_FORCED_ROLE_EQUALITIES_20261029.md>) | 强制双角色预算取等；正反残余均恰五端点；全B4第二点图Hall与另一合法残余得到认证。五端点双等号仍开，补集未证766。 |

这条序列包含真实进展，也显示机制反复回到同一边界：必要供应、端点图和形式人口，最终还需在同一个完整母体中兑现同端禁形或合法净增益操作。最后两稿比“又加一个必要条件”更强，因为它们以更大实际诱导集调用旧容量，排除了完整子类；但没有闭合的最后一步不能略去。

## 6. 最新进展的准确量词与剩余等号窗口

先取任意canonical767分解 \(X=H\sqcup R\)，**只在 \(|H|=2b\)** 下定义

\[
D_0=X\setminus\bigl(\operatorname{Src}_{R6}(X)\cup
\operatorname{End}_{R6}(X)\bigr),\qquad
w=|\operatorname{Src}_{R5}(D_0)\cap\operatorname{End}_{R5}(D_0)|.
\]

neutral-through主稿以完整残余增广得到

\[
|R|+w\le b+5,\qquad |X|\le3b+5-w.
\]

证明保留全部R点、全部五点横截及多点混合供应；不是逐owner收费。它没有覆盖未满H的一般近满情形。共同等号 \(|X|=3b+5\) 因而必有w=0；b25时排除的是X80中全部w≥1子类，不是证明每个候选必有w≥1。

共同等号下，令 \(S=\operatorname{Src}_{R6}(X)=R\)、\(T=\operatorname{End}_{R6}(X)\)，各b+5；\(I=S\cap T\)，\(|I|=5+q\)。\(U=\operatorname{Src}_{R5}(D_0)\)、\(V=\operatorname{End}_{R5}(D_0)\)各q，现有 \(U\cap V=\varnothing\)。H与其反向核H′内部重算的红through数为m、m′，正反蓝角色需求为j、t。最新版不是强迫期望的严格预算，而是证明

\[
j+m'=b,\qquad t+m=b.
\]

所以**严格分支才被排除**。将旧Joint17语义迁移与R25共同嵌入范围作为条件输入，m、m′为9/10，j、t为15/16；每方向仅剩 \((m',j)=(9,16)\) 或 \((10,15)\)，及其对偶。这不是四个已实际实现的配置。paired75740只覆盖j=t15、因此m=m′10的子支，不能代表全部剩余候选。

最新主稿进一步给

\[
E=\operatorname{End}_{R6}(S),\quad |E|=5,
\qquad |\operatorname{Src}_{R6}(T)|=5.
\]

它排除的是共同X80中两方向的六端点支，不是所有独立D7的六端点配置。令 \(W=S\sqcup U\)。W内全部从U启动的实际B4，其第二点都在 \(I\setminus E\)；对每个 \(A\subseteq U\) 删除完整第二点邻域后，实际配置仍属D7，故 \(|N(A)|\ge|A|\)。Hall来自逐子集的实际诱导删除，不是“每点有供应”直接推出；匹配保留多U路径，却仍不等于内部不交或共同外端点。

取 \(P=S\setminus T\)、\(K'=P\sqcup U\)，认证的另一残余 \(K'\sqcup E\) 规模b+5、\(\tau_{R6}=5\)。这是合法整块残余，不能降格为仅条件交换；但它不是canonical S，且**补集未证766**，因此不能把它当成新H–R分解继续套满核封闭。E按序为e1至e5时，e4、e5是W最后两个点；不意味着所有非E点在e2前。

在paired40子支，每个合法747增广点f满足f<e4，反向有对应限制。更强f<e2已经撤回：插到e2与e3之间须检查三个新连续三元组，第三个 \((f,e3,e4)\) 不由右根性质控制。局部允许RRRB只暴露证明缺口，不是完整X80反例。同理，之前紧核插入少验第二个新三元组，不能保留原cap6结论。

MUS线也有真实但有限的支持排除：完整不可满足族的五点红横截必须本身为蓝B5；若某横截点只有唯一private红六，则其五个替换横截同时迫六条实际蓝路径。packet与同端weak于是排若干区间共享位置。它未证明每个MUS都有五横截或唯一private；纯红MUS红横截数至少6的分支仍开，也没有自动临界态下降。

两种Hall也须分开。common-P并集的全R6 incidence匹配，把内部B0点匹配到最终A0端点，来自整个并集的最小横截数q；最新B4第二点匹配，则来自W的全部junction及对每个子集的实际删邻域。这两者都给次序支配，但边代表不同路径位置，不能拼成一条实际红路径或当作相反有向边。需要共同首末点的旧点对势函数，也不能仅凭两个匹配套用。

另一残余K′∪E的合法性有助于把“操作失败”定位得更准：不是所有替换都未认证，而是这次认证只覆盖残余侧，尚未证明另一侧避R6。把任意新的合法残余重新叫作canonical源集会错误增加ambient身份；其中U点并不启动ambient R6。其他最小五横截也未证明全部是端点集、唯一或满足matroid交换。完整供应图有匹配与可自由交换整个分块是两种不同的结论。

## 7. 为何反复停在局部优化，又为何还不能宣告耗尽

常见循环是：把完整颜色投影为人口或图，推出必要供应，挑选有利见证，再试图独立收费。投影丢掉的是同一母体内供应的共存、共享支持和实际首末点。Hall只匹配incidence；紧集只是结构信息，并不等于矛盾。两条红五加不同中间pair产生的两个蓝四，也不能自动拼出蓝六。

满25等号 \(m_{\rm miss}=e\) 是两个计数相等。原charging证明没有给逐owner非负slack，也没有给两个不同诱导核间的单调双射。共同P的状态各自增长，不能因共同点相同便认为states相同；更不能把ambient标签当另一诱导核内部状态。旧普通／exceptional数量再细，也补不出这种运输。

合法插入必须逐个检查**全部新连续三元组**；多点搬移还要检查经过多个新点的路径。只修private阻挡可能留下全新mixed违例。删一约束后另有满足赋值，也不表示它保留本轮σ、支持和横截，无法自动成为单违例下一状态。若没有严格下降的整数势，反复换临界赋值不能当成终止证明。

小完整反例有效地否定普遍局部机制，却没有触及实际近极值的全部联合前提；应在失败接口停下，而不是由此否定所有结构。反过来，把未控全X改名为prime、把q/w/j再细分、列出更多有条件供应，也没有给全类入口。近期w≥1、严格预算及六端点分支的排除是真进展；若后续只是再命名五端点等号剩余约束，仍会回到局部优化。

b已有实际25构造，继续单攻b<25不是合理主投。精确根等式也降低独立777路线价值。757若只降到39，当前尚无一般新桥进入Q链；只有paired-cover共同子类可能利用它，不能先记成全局一点收益。

## 8. 后续方案：先固定定理，再讨论数字

以下全部是建议与待证目标，没有新结论或新作业授权。本节的先后顺序是资源优先级，不是四条同时展开的流水线。

### P1 主线：同一H–R共同饱和的稳定性

对每个canonical767母体，令α为R中最大R6-free子集规模、τ为最小R6横截。于是 \(|R|=\alpha+\tau\)、\(\alpha\le b\)、\(\tau\le5\)，有精确恒等式

\[
3b+5-|X|=(2b-|H|)+(b-\alpha)+(5-\tau).
\]

**首个全类目标是证明右侧至少1**，等价于排三份同时饱和 \((2b,b,5)\)。恒等式仅组织目标，不是新定理。最有希望的首引理应同时使用最新正反各五实际端点、全支持及两个共享P满核，迫同一对实际外端点的weak7，或给完全合法且净收益为正的重分划。必须保留全部残余点、所有替代供应及多点路径，不能退回严格Hall或三块R5人口。

若目标成立，则 \(Q\le3b+4,F\le3b+5\)，b25给79/80，不需要先有C49。要再进到总缺额至少2，须覆盖总缺额≤1的整个窗口：满角以外，还包括

\[
(|H|,\alpha,\tau)=(2b-1,b,5),\ (2b,b-1,5),\ (2b,b,4).
\]

仅再次排X80不能得到第二单位。全窗口成功才有Q78、F79、几何80。b是固定七点模型有效上界，常数5不泛化为所有n。

首里程碑应是完整残余端点同步，或处理全部mixed路径的实际交换，并有从每个目标母体进入该引理的证明。如果只得到图上不等式、选定supplier或一组形式人口，不能继续许诺缺额；应记录首个断点并停止同类细化。

相对昨日建议，优先级发生实质调整：从先在独立平衡容量上广泛寻找C49，转向直接排共同角(H2b、αb、τ5)。原因是今天的端点刚性已经给每个共同等号候选统一入口：w0、双预算等号、正反各五端点，而独立H50并不带这些额外跨残余条件。这个入口不是矛盾，却使主问题比“任意饱和H50是否存在”更集中。P3仍保留，但不再要求所有路线先等C49。

第一步可把满角的实际集合、禁形、全部供应、已证明的双向端点身份写在同一页；第二步只选择一个足以产生正净值的操作或同端点同步引理；第三步检查它是否覆盖等号窗口的每个尚存分支。若碰到反例，回到该引理的量词修正，而不是同时更换母体、状态标签和目标数字。这样保留真正完成的子类排除，也让下一轮的首断点可以精确比较。只有满角闭合后，才把同样检验扩到一缺额三种分配。
### P2 竞争架构：完整路径最小删除与实际重分划

对每个767母体X，定义

\[
z(X)=\min\{|Z|:X=K\sqcup Y\sqcup Z,
\ K\in766,\ Y\in756\}.
\]

对**存活顶点** \(X\setminus Z\)，完整充要约束是：每条实际R6同时遇K、Y，每条实际B5遇K。B6与weak由母体遗传；不能把已遇Z的原路径继续要求两块都命中。现有canonical加五横截给z≤5。

**首目标是 \(\sup_X z(X)\le4\)**，而非先挑一个容易修的private族。成功给 \(Q\le C+b+4,F\le C+b+5\)，C50/b25时79/80；z≤3再给78/79。所需定理是所有实际最小障碍的完整路径修复：纯红MUS且τ≥6、mixed MUS、多private支持、移点后多重违例均须覆盖。

第一份有价值交付是严格下降整数势的普遍修复，或每个最小障碍必进入一组已分类支持形的入口。unique-private引理目前只处理子类，不可换名当一般交换。若有实际反例否定z4，应停止这个更强的结构定理；它不证明数值Q79为假，也不自动结束P1。

### P3 支持与储备：平衡容量的严格性

目标为 \(C\le2b-\Delta\)。应同时使用同一H的四个实际满核及两色完整端点图，证明紧／严格二分的**两种情况**都兑现实际颜色缺陷。严格Hall仍缺支持密度入口；紧集只有在packet-compatible cut/interface被证明后才有用，不能假设它天然是区间或laminar模块。先证明共同核的状态运输或内部attainment，再使用25点满容量的等号条件。

首个Δ1给C49、Q79、F80；Δ2给48/78/79。它可与P2独立组合，前提是两项分别成立、适用范围兼容且不重复计算同一损失；不要求证明来源或工具彼此分离。旧C49 Closure是一项有边界的证明缺口闭合机会，须补实际来源及CNF绑定；它不是新数学，更不支持无限重试。建议只作一次明确边界的结构／证据缺口调查，本轮不发新任务或作业。

### P4 低优先储备：独立D扩张稳定性

对任意R∈D7，取最小横截T、\(t=|T|\le5\)、\(Y=R\setminus T\)、\(d=b-|Y|\)。寻找真正结构下界 \(d\ge f(t)\)，则

\[
D\le b+\max_{0\le t\le5}\{t-f(t)\}.
\]

若其余f≥0、f(5)≥1，就足以D≤b+4。这里要保留全部五外点的共同作用，覆盖独立残余的E5/E6及全部e=m类型；X80的五端点定理没有排除独立E6。D26已否定更简单的单外根机制。完整D30反例会否定D29，但不否定大H–R不能共同饱和的P1。

长期split/prime方向仅在有界删除进入定理或有界prime容量入口时再投入。把整X称为prime不构成降维。当前不宜用四条储备路线分散两条承重主线。

完整染色极值构造仍是有用的反检。若核实一个实际H50，它将结束普遍C49，却不反驳联合Q79；实际D30将结束独立D29，却不反驳联合Q79。若核实实际767中的X80，结合旧上界80与根等式，则在旧结构成立的条件下，这个抽象模型将有Q80/F81锋利；继续改善几何界就须明确转向更窄模型或额外几何性质。目前检索材料没有这三类构造。形式人口可行、小D12/D26和局部合法packet都不是这些反模型。只有固定具体引理后才建议有边界反检，本轮没有启动作业。

## 9. 收益、几何比较与下一份可验收交付

以b25、基线C50、z5为统一记账起点。耦合η指直接相对该基线的联合缺额，不能再与同一次损失的Δ或z节省相加；同源改进只能取更强者，分别证明、适用范围兼容且不重复计同一损失的全类改进才可相加；证明共享工具本身不妨碍组合。

| 条件场景，均为待证时的传播 | C界 | z的可用界 | Q界 | F界 | 几何ES(7)界 |
|---|---:|---:|---:|---:|---:|
| 当前草稿链 | 50 | 5 | 80 | 81 | 82 |
| 仅独立C49 | 49 | 5 | 79 | 80 | 81 |
| 仅普遍z4 | 50 | 4 | 79 | 80 | 81 |
| 独立C49与普遍z4 | 49 | 4 | 78 | 79 | 80 |
| P1直接联合η2，无C改进 | 50 | 5 | 78 | 79 | 80 |

单个单位仍有项目价值；若要在几何比较上超过下述特定81主张，需要总计两个单位。主会话本轮核实[Schroeder作者伴随页](https://michaelschroeder.ai/research/ErdosSzekeres/companion)，其Version 1、2026年9月19日列ES7≤81、ES8≤319及几何756=25，未宣称外部同行评审。本报告仅把它记为作者预印本主张，没有独立重建其全部证明，不称其为signotope全类定理，也不声称它是全球最新最佳。项目几何80若最终成立，将在数值上超过**该特定81主张**。

[Baek论文v2](https://arxiv.org/html/2206.04260v2)提供基础完全染色界的来源；[Baek–Balko，SoCG 2025](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2025.13)关于split/decomposition的区分支持独立研究分解类，不能运输成任意signotope的容量定理。文献比较与本地接受状态分别记账。

下一份交付应固定一个全称定理、完整等号窗口、首个断裂步骤及相应反例，而非继续非正式轮次。P1优先，P2保持真正替代；P3只有一次有边界调查，P4储备。验收顺序是全类入口、同一次实际操作、全部禁形与内部秩、严格净损失，最后才传播数字。

对抗资产至少覆盖满25多状态类型、D26入出R6、D12不交路径与零实际成本、任意D的小H空锁嵌入，以及同端路径可能须同时替换p−1内部点。候选若排除某资产，应证明新的近满前提由目标母体自动满足；否则仍是人为收窄子类。完成全类定理、给出完整实际反例，或严格结束一个无效机制，都可验收。不预测成功概率或时间。

具体记录可用一个紧凑表格：第一列写母体及全部量词，第二列列真正保留的实际点集和路径位置，第三列写所需共同端点或新三元组，第四列记首次不能推出的结论，第五列注明它是完整反例、局部合法逃逸还是未决定。这个表不以“候选剩余很多”作结，而要求明确指出哪条性质尚未由目标母体强迫。任何省略某种多点路径的修复都应先在此处暴露，避免直到容量传播时才发现缺口。

若交付的是下降操作，整数势须在同一次合法分划上定义，并逐条说明所有新违例被何处吸收；等成本平台移动可以作为中间步，但必须有严格降低的副势和有限性。若交付的是同端weak，须显示同一首点、同一末点、两色实际顶点序列及长度和9，分别存在的入供和出供不能替代。若交付的是子类排除，应列出完整进入条件及仍开放的互补类，并说明是否真正删除先前存活的临界分支。上述都是已有问题的验收要求，不是本轮已经完成的引理。

## 10. 本次审计、文件与外部审阅边界

综合截止可得2026-10-29文件，依靠原始材料抽取与主会话判断，没有重新证明全部历史。历史记忆CLI遇EPERM时，以直接项目材料和会话检索回退；这种来源访问不构成独审。本报告只新增本文件及[文档检查回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_synthesis_20261029/DOCUMENT_CHECK.json>)，不改变任务in_progress、metadata、接受/assurance、历史报告、封存CNF/proof或运行作业；不提交、不归档。

当前[review-runtime.json](<D:/科研/math agent/erdos-szekeres-sat-main/.aris/review-runtime.json>)为 `activated=true`；[README](<D:/科研/math agent/erdos-szekeres-sat-main/.aris/README.md>)仍写disabled/false，属于旧证据，不能据此说当前路线被禁用。[10月29日既有阻止回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_pair_fan_20261029/REVIEW_BLOCKED.json>)记录的是一次具体未发表材料导出的自动审批拒绝：未明确授权把那些内部研究原件送往外部Claude。它没有jobId、没有确认服务执行、没有Claude数学答复。本轮用户明确选择不外传，因此没有新review调用、重试或配置调整。

请求模型和effort、CLI报告值、backend证据仍分别处理；隐藏backend/actual effort不可验证。本轮没有独立PASS、接受升级、实验、solver、checker或证明重放；机械文档检查仅核链接、台账、公式分隔及传播算术，不属于数学认证。**当前40/50/80/81保持；实际开放的是五端点、双预算等号、w0及全部mixed供应在同一近极值母体中的共同实现。**