# N_sig(7,r,s) 研究综合与策略审计

日期：2026-10-28。范围：本地连续 RESET R1–R27、10月26–28日相关后续原始研究稿，以及作为前提的 b25 接受记录。本报告由主会话负责分析与来源抽查，native Sol/high 文档执行代理忠实转写、检查文件与链接；不是逐条证明重新认证，也不是穷尽外部文献的独立审阅。全部结构草稿维持原有 unreviewed/unaccepted 状态，没有新全局界、接受升级或新运行。

**判断：目前有强烈的局部优化倾向，但没有证明整条结构路线已经耗尽。** 应保留真正改变全局组织的实际覆盖、边界增广和根归约，把研究单位改为近极值母体的共同实现，或实际完整路径的全局分块。给缺额命名、增加必要条件、把目标从50改成48，都不能自行成为突破。

## 1. 模型、数值与接受口径

\(N_{\rm sig}(n,r,s)\) 是完整有序 rank-3 signotope 中，同时避免蓝 \(r\) 链、红 \(s\) 链和 weak \(n\) 的**最大避免规模**。每个四点包按 abc/abd/acd/bcd 至多变色一次；链长计顶点；weak 使用同一对实际端点，两色路径长度和为 \(n+2\)。诱导子配置的路径、秩与状态必须重算，不能继承 ambient 最大值。几何强迫阈值只可沿对应关系写成

\[
\mathrm{ES}(7)\le N_{\rm sig}(7,7,7)+1.
\]

因此结构草稿的777上界81对应强迫82，不能写成 ES(7)≤81。下文757、756、766、767、777均指这套参数，不混用强迫阈值。

记 \(a=16\) 为有效747界，\(b=25\) 为有效756界，\(C\) 为实际766容量，\(c\ge C\) 为可用上界，\(D\) 为指定残余类容量，\(Q\) 为767容量。界不等于精确容量。b25 的 [C8正式人工接受](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md>)记载 C1–C10 全部人工接受，但保证仍是 same-family/provisional，隐藏 backend/effort 不可核实。接受只覆盖其既定模型的上界25，不单独证明存在25或等号；实际25构造另见R23及后续完整颜色证据。不能把10月26日接受倒填进R23当时的状态。

外部参数16来自 Baek 的 [On the Erdős–Tuza–Valtr Conjecture](https://arxiv.org/abs/2206.04260)，[Definition 2.1与Theorem 2.7](https://arxiv.org/html/2206.04260v2)的完全染色定义比本项目模型更一般。Baek–Balko 的 [SoCG 2025论文](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2025.13)区分 split/decomposable 与一般化失败，支持把分解作为独立研究对象，不能把递归类结论移植为全 signotope 界。Schroeder伴随页本轮返回503，不声称刚核实外部81或文献新颖性；本地源码只能按其原来源主张使用。

## 2. 已有结构定理与传播链：为什么当前是40/50/80/81

以下按原结构稿记录使用，不提升其接受状态。

**边界覆盖（R5/R6）。** 当 \(n\ge4,\ 4\le r\le n\) 时，

\[
N_{\rm sig}(n,r,n)\le N_{\rm sig}(n,r-1,n)+N_{\rm sig}(n,r,n-1)-1.
\]

严格一点来自全局点对序、无环支持下真实扩大覆盖、交叠至少一点。这不是任意参数递归，尤其不能无条件套到766／禁weak7。

**平衡拆分。** 设 \(p\ge3\)，容量参数在所述完整signotope模型中有效。在无蓝 \(p+1\)、红 \(p+1\)、weak \(n\) 的实际配置中，按实际红 \(p\) 链源分块，结合换色，得到
\(N_{\rm sig}(n,p+1,p+1)\le2N_{\rm sig}(n,p,p+1)\)，故 \(C\le2b\)。

**canonical H–R（R7）。** \(n\ge6\) 时实际不交分解 \(X=H\sqcup R\)，\(Q_n\le C_n+D_n\)。残余 \(D_n\) 除无蓝 \(n-2\)、weak \(n\) 外，还满足
\(\operatorname{End}_{R}(n-2)\cap\operatorname{Src}_{B}(n-3)=\varnothing\)；不是一般 \(N(n,n-2,n)\)。七点情形全部红六终点位于至多六点中，特殊删除以至多五点打中所有实际红六，故 \(D_7\le b+5\)。

**精确根归约（R20）。** 对 \(n\ge4\)，
\(N_{\rm sig}(n,n,n)=N_{\rm sig}(n,n-1,n)+1\)。这是指定 root/chart 关系，不是任意 pivot 变换都保持非对称短帽。

所以当前代数链为

\[
N_{757}\le a+b-1=40,\quad C\le2b=50,\quad Q\le C+b+5\le80,\quad N_{777}=Q+1\le81.
\]

R5、R7、R20改变全局组织；b29→28→26→25则是外部输入更新，两者必须分开计功。历史序列为：初始45/58/103/206；R5为44/58/101/201；R6在b28下43/56/98/195；R7同输入43/56/89/177；R8在b26下41/52/83/165；R20为41/52/83/84；R23采用b25为40/50/80/81。它们均是当时输入和草稿链下的历史数，不是精确容量或新文献纪录。

状态账本 \(M=O+e-m\)，其中
\[
O(n,r,s)=\sum_{j=n-s}^{r-2}\binom{n-2}{j},\qquad \max(r,s)\le n\le r+s-2.
\]
757/766/767/777的普通参考分别26/30/31/32；它不是已经证明的完整模型上界。756的已接受C1–C10支持 \(m\ge e\)，给25。R12的可分解类有精确 \(O\)，但一般 irreducible 叶可能就是整个对象，尚无全类有限核定理。

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

## 4. R27以后十四份原始记录及当前证据

前五份BALANCED49与五份D7构成10月26–27日连续工作，最后四份补充全缺额、残余、保端点扩张和空锁普适性。旧[10月27日综合](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_STRUCTURAL_SYNTHESIS_AND_ROADMAP_20261027.md>)只是次级背景，其Joint17待定和Closure规则FAIL已经被后续回执取代。

| 原始稿 | 本次综合中的位置与边界 |
|---|---|
| [balanced49迁移与联合缺额](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/BALANCED49_TRANSFER_AND_JOINT_DEFICIT_20261026.md>) | 区分几何定理与signotope语义迁移；尚不能使用C≤49。 |
| [共同尾与终点障碍](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/BALANCED49_CONTINUATION_SHARED_TAILS_AND_TERMINAL_BARRIERS_20261026.md>) | 实际前后供与端点身份；完整闭合义务另计。 |
| [全见证点对秩与分叉反例](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/BALANCED49_ALL_WITNESS_PAIR_RANKS_AND_FORK_COUNTEREXAMPLES_20261026.md>) | 全见证校准；有限反检、形式化切片不等于联合容量。 |
| [饱和Y交换与横截障碍](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/BALANCED49_SATURATED_Y_EXCHANGES_AND_TRANSVERSAL_OBSTRUCTIONS_20261026.md>) | 私人路径和实际替换；不可按路径数重复收费。 |
| [共同赋值与剩余H49支](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/BALANCED49_COMMON_ASSIGNMENT_AND_REMAINING_H49_BRANCH_20261027.md>) | Through14接通原始证据；满核删一加二的R6由b25直接强迫；C49一旦闭合，H49的B0自动空。 |
| [D7批量复制与临界横截](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/D7_BATCH_CLONING_OBSTRUCTIONS_AND_CRITICAL_TRANSVERSAL_TEST_20261027.md>) | 精确down-clone判据和整族冻结；全类目标仍开。 |
| [D7全局临界端点与完整决定](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/D7_GLOBAL_CRITICAL_ENDPOINTS_AND_COMPLETE_DECISION_20261027.md>) | 端点后缀与非末端替换；完整30点决定超时。 |
| [临界满核与端点校准](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/D7_CRITICAL_FULL_CORE_EQUALITY_AND_ENDPOINT_CALIBRATION_20261027.md>) | 完整25核允许两条分离R5加右根；内部条件不迫损失。 |
| [共同满核扩张与H49核心](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/D7_JOINT_EXTENSIONS_AND_H49_COMMON_CORE_20261027.md>) | 完整D26为Y25+a，a同时入出R6、τ1/α25、Y内e=m=2；单外根机制已被反例否定。另有H49同一S24供应。 |
| [D7扩张与共同语义桥](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/D7_GLOBAL_EXCHANGE_AND_BALANCED49_SEMANTIC_BRIDGE_20261027.md>) | E5/E6完整N30分支均超时未决；S24旧源不能再收费。 |
| [全缺额框架与Joint定理](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_GLOBAL_DEFICIT_FRAME_AND_JOINT_THEOREM_20261027.md>) | Joint17重放PASS、全类手写迁移及through缺额；Closure仍缺实际绑定。 |
| [全类残余与不交R6反例](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_ALL_CLASS_RESIDUAL_AUDIT_AND_DISJOINT_R6_COUNTEREXAMPLE_20261027.md>) | 完整D12有两条不交R6；否定两两相交路线。 |
| [保端点扩张与R26联合预算](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_ENDPOINT_PRESERVING_EXTENSION_AND_R26_JOINT_BUDGET_20261027.md>) | 实际端点扩张条件与同一H的共同预算；无严格全局下降。 |
| [空锁普适与操作边界](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_EMPTY_LOCK_UNIVERSALITY_AND_OPERATION_LIMITS_20261028.md>) | 任意D_n均可嵌入单点H的空锁canonical母体；实际分块判据。 |

**当前机器证据的三个层级。** [Joint17原始result](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_proof_completion_20261027/joint17/result.json>)为完整strict-RUP PASS，59479源子句、102563添加步骤，最终空子句为真。它关闭指定公式的重放缺口；全类语义运输仍是未独立审阅的手写推导。[Closure schema result](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_proof_completion_20261027/closure/result.json>)也为PASS，但明确 `UNSAT_checked=false`、`actual_cnf_equality_checked=false`。实际来源获取见[停止回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_proof_completion_20261027/closure_acquisition/abort_receipt.json>)：`ABORTED_BUDGET_FEASIBILITY`，完整Literal/CNF/RUP连接未取得。所以C49尚未闭合，C47/Q77/77778仍是目标。固定Closure规则没有internalBound时Terminal20不再自动是必要依赖，也不能据此声称完整原始Lean Model已经编译。

D7的R30 E5/E6超时仅表示未决定，见[完整执行报告](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_global_exchange_semantics_20261027/README.md>)。完整D12的[颜色](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/sat_colors.json>)、[直接语义回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/sat_semantics.json>)及[canonical扩张回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/extension_result.json>)支持其有限反例；10月28日[核查总回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_operation_20261028/result.json>)仍明确unreviewed/unaccepted。本报告只读这些来源，没有重跑。

D26单外根反例另有[完整颜色原件](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_joint_extensions_hr_20261027/single_root26/sat_colors.json>)、[直接语义核查](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_joint_extensions_hr_20261027/single_root26/sat_semantic_result.json>)及[满Y重算profile](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_joint_extensions_hr_20261027/single_root26/Y25_full_profile.json>)。这些原件的作用是让具体反例可以回查，不能反向证明完整D30存在，也不能由反例中的τ1推断一般最小横截至多一。反例只结束它实际否定的候选接口，不能扩大成对全部扩张路线的否定。

同样，公式重放、规则有效性、模型运输、人工接受需要四条不同的证据边。重放证明某份固定公式不可满足；规则有效性说明规定的构造子如何对应其语义；全类运输必须把每个目标母体送到同一公式赋值；人工接受再记录审查与决策。任何一条成功都不能代替其余三条。特别是源码层schema通过以后，仍须处理实际完整行集和变量编号是否正是被反驳的那份对象。今天的证据更新应清楚承认Joint17已经前进，同时保留Closure尚未接通的准确缺口，避免继续修理已经修好的边，或跳过尚未完成的边。

## 5. 目前最强的非数值工具：能推出什么

固定同一个实际766配置X，\(S_c,E_c\) 分别为X中颜色c的实际五链源集、末点集，\(t_c=|S_c\cap E_c|\)。全766类的Joint结论记为J：
\[
\min\{|X\setminus(E_R\cup E_B)|,|E_R\cap E_B|\}\le16,
\]
反序给源集合版本。令 \(M=2b-\delta\)，\(a_c=b-|S_c|\)、\(e_c=b-|E_c|\)，本段标量\(A=a_R+a_B\)、\(E=e_R+e_B\)。再定义实际集合\(Z_1=X\setminus(S_R\cup E_B)\)、\(Z_2=X\setminus(S_B\cup E_R)\)，\(q=|Z_1\cap Z_2|\)，以及
\[
z_1=a_R+e_B-\delta,\quad z_2=a_B+e_R-\delta,\quad0\le z_i\le\delta.
\]
原稿联合界为
\[
t_R+t_B\ge2b-32-\delta-(A-\delta)_+-(E-\delta)_++q
\ge2b-32-3\delta.
\]
这里16/32是固定七点模型输入，不是一般n常数。b25时δ=0/1/2只给18/15/12，而每色through≤13并不矛盾。以\(L=S_R\cap S_B\)、\(U=E_R\cap E_B\)记双源、双末集合，形式人口 \(|L|=|U|=16,t_R=t_B=6\)，加四个单角色点，总计48且满足这些标量条件；这不是实际signotope，而是证明标量系统不足的校准。必须加入完整颜色相关性。

共享前缀/尾工具 \(|P\setminus S_R|+|T\setminus E_B|\le z_1\) 使用同一次不交实际集合，另一neutral预算不能免费合并。

下面切换到R26的canonical配置\(X=H\sqcup R\)，所有集合均在同一X中定义。这里A改指\(F_+\cap R\)的可选实际子集，不是上段标量\(a_R+a_B\)；\(S=R\cap\operatorname{Src}_{R6}(X)\)，W是R中存在从H起点出发的ambient红六到达的点集，\(U=R\setminus(W\cup S)\)，\(E_A=o(A)\cap(S\setminus W)\)。其中\(F_+\)与出口映射o按下段实际锁定定义使用。R26最强的共同预算是
\[
|A|+|U|+|W|+|E_A|\le d_H=2b-|H|,
\qquad |U|+|W|\le d_H.
\]
旧“两份独立d预算”表述已被加强取代。实际K构造是价值所在，但没有证明正需求。

对R26锁定族F，红六全部终点与蓝五全部第二点同为出口 \(o(s)\)，出口集O。实际 \(K\in766,D'\in D_7\) 满足 \(K\cap D'=F\)、\(K\cup D'=X\setminus O\)、\(|K|+|O|\le2b\)。写 \(f=|F|,o=|O|,f\ge o\)，得到
\[
|X|\le\min\{3b+5-f,\ C+b+5-(f-o)\}.
\]
若已独立有 \(C\le2b-\Delta\)，正确合并是
\(|X|\le3b+5-\max\{f,\Delta+f-o\}\)，不是收取Δ+f，也不是把正反预算相加。

保端点扩张E对 \(n\ge5\)：混合源s的合格红 \(n-1\) 终点t，若存在蓝 \(n-2\) 的第二点不同于t，则所有x<s满足
\(P_R(x,t)\ge P_R(x,s)+2\)、\(P_R(x,s)+P_B(x,t)\le n-1\)。这是实际端点约束，尚未变成严格全局容量。

## 6. 局部最优诊断与应停止的机制

第一，10月28日普适嵌入把**任意** \(D_n\) 加一个蓝右根变为canonical H单点、R原样、正反锁族均空且全部蓝覆盖缺口出现的母体。因此这些标签本身挑中的还是全残余类。它否定“空锁自动缩小D”的逻辑，不否定近满大H与R之间可能存在联合定理。

第二，完整D12有18条红六，\(\nu_6=\tau_6=2,\alpha_6=10\)，且可保留为canonical残余，故两两相交为假。该例端点分离删除成本1，实际分块成本0；端点图或区间成本不能作为完整路径成本下界。全部路径区间跨越最早终点，不等于路径包含它，不能推Helly或matroid性质。

第三，满25核有e=m=0/7/8/10等类型；缺普通态可以由exceptional补偿。完整25还允许两条分离红五加右根。更强的完整D26反例Y25+a中，a同时结束和启动R6、τ=1、α=25，Y内e=m=2，全部颜色语义已核查。因此单外根的实际入出R6也不足。另对满Y及两个外点a,b，删任意y后Y−y+a+b已有R6，是b25直接强迫；“删一加二有路径”不是独立容易的新入口，真正交换须利用剩余其他外点。因而“饱和等于全ordinary”、把外点投影成核内两条链、重新攻单外根，均应停止。

第四，R27的完整修复回到旧核心，净收益为零；私人见证会共用支持，不能按尾或路径条数收费；最小横截基也不是matroid。第五，λ不是自由变量：每个顶点incident pair的顺序由三元色固定，所有兼容线性扩张的最小p(v)相同，优化λ不会改变canonical分块。第六，proper rootfan cut≤46与反向fan模块≤30是真实子类结论，但没有全类进入定理，继续微调旧模块不应作为主投。

这些失败共同定位到一个具体瓶颈：**近满的实际各部，怎样被迫共用同一个障碍；或者怎样构造成本更低、覆盖全部实际路径的分块。** 相对昨日综合，10月28日的全类空锁普适性使继续细化残余端点缺口的优先级下降。小H反例要求收窄量词，不能直接结束大H方向；有限模板关闭也不能结束一般母体。R5/R7/R20值得保留，因为它们已展示组织结构改变怎样兑现为全局收益。

## 7. 后续候选路线：量词、机制、里程碑与停止条件

本节全部是建议／待证目标，不启动任何执行。

**P0：有边界的旧证据闭合。** 对既有balanced49迁移，补齐实际Closure source、Literal/CNF字节与完整proof连接，而非再发明人口条件。里程碑是从每个目标signotope到同一实际公式赋值、再到已检查反驳的完整依赖链。仅全部义务闭合后，才可使用c49及Q79/77780。它是最具体的近期台阶，但不是新的主结构定理；本轮不下载、不重放，证据或预算仍不足就保持未闭合。

**P1（主线）：统一近极值平衡共同实现。** 对每个 \(X\in766,|X|=2b-\delta\)，同时使用四个大小在b−δ到b间的实际近满核、各自内部秩、全部共享源终及实际前缀/尾。要由完整入口迫使跨中点、跨颜色packet冲突或封闭供应的neutral成本，证明 \(\delta\ge\Delta\)，Δ必须由引理导出。首里程碑是一条覆盖整个小δ窗口的实际共用packet／闭供应障碍，并证明颜色禁形或严格净损失；不能只选有利见证。形式48人口可行迫使新引理使用全颜色相关性。一般p,n版本可以追求，但不悄悄泛化16。假设得到Δ=1/2/3，才分别有C49/48/47、Q79/78/77、77780/79/78。由遗传性，排除2b−k得到C≤2b−k−1；单把目标换48并未提供机制。若完整反例满足全入口，撤回候选；若仍只有固定模板，停止追加同类人口支。

这条线的第一份证明不必先许诺下降三个单位，但必须覆盖它自己声称的完整缺额窗口。每次选核都要说明：属于哪个同一母体、哪些路径在核内重算、哪些外供保留原端点、两种颜色为何能在同一次选择下使用。若分别为红色和蓝色选择了最有利的不同核心，就还没有得到共同实现矛盾。所有替代路径都可能规避一条选定连接，因此候选冲突须依赖全供应集合，或证明任意替代都付同一笔互斥成本。这是从既有人口条件走向新机制的实际门槛。

**P2（竞争架构）：真实全局路径分块。** 对每个767配置X，构造不交 \(X=K\sqcup Y\sqcup Z\)，其中K∈766、Y∈756、|Z|≤z。已有canonical加横截入口给z5。下一步应在所有实际合法分块上最小化|Z|，证明大于导出阈值的最小障碍允许有限批量重分配，且保留全部三元色、混合路径和多新点路径。首里程碑是完整可执行的重分配引理；10月28日§6的Src_R6充要判据可作接口，判据本身不提供构造。停止端点投影成本和固定一条尾的证明。收益为Q≤C+b+z、777≤C+b+z+1；C50时z4/3/2给Q79/78/77、77780/79/78。两块定理还能独立接入改进后的C。此目标比单纯数值界强，操作失败不否定容量目标。

具体交付应写出删除前后的实际点集，逐类解释一条可能新出现的红六为何必被另一块或删集打中，而不能只证明原来挑出的几条路径消失。批量操作尤其要处理使用两个或更多移入点的路径；它们不由逐点合法性自动覆盖。若证明只能维持“全部红六端点异块”，应返回完整路径判据，先用D12的零实际成本例检验是否施加了额外限制。真正值得计入进展的是一个适用于任意最小障碍的重分配步骤，或明确证明某种操作族必然不能降低成本。

**P3：同一H–R容量权衡。** 对每个canonical X=H⊔R，取红六最大无路径子集α和最小横截τ，则|R|=α+τ、α≤b、τ≤5。有效c≥C下的精确缺额为
\[
c+b+5-|X|=(c-|H|)+(b-\alpha)+(5-\tau).
\]
目标是从跨核全部供应证明此和统一至少η，而非假设每部单独变小。c50时η1排H50/R30；c49已获独立依据后再有η1，才给Q78/77779。若要在c49下得Q77，必须排整个78层：H48/R30以及H49/R29，后者含(α,τ)=(25,4)、(24,5)，不能只排一个饱和角。

在C49真正闭合的前提下，H49时 \(B_0=\{r\in R:H\cup\{r\}\text{无R6}\}\) 自动为空；不可继续把B0非空支当新主攻。可复用证书是实际 \(K=(H\setminus D_0)\cup A\in766\)，及其内部 \(N_K=K\setminus(\operatorname{Src}_{B5}(K)\cup\operatorname{End}_{R5}(K))\)，由 \(|K|+|N_K|\le2b\) 得
\(2b-|H|\ge|A|-|D_0|+|N_K|\)。里程碑是实际构造、不同neutral及正净值，不得跨不同K求和。R26已有实例，新增工作必须覆盖空锁且H近大的情形；可研究“所有扩张同时受阻”迫出的结构。公式只是组织目标，不是新定理；Δ与锁不可双收。

**P4：有边界的独立D7扩张稳定性备选。** 对每个R∈D7与最小横截T，t=|T|≤5、Y=R\T、d_Y=b−|Y|，求结构式d_Y≥f(t)，则 \(D\le b+\max_t(t-f(t))\)。第一目标仅t5⇒d_Y≥1，足以D≤b+4，不要求全类τ≤4。必须同时覆盖E5/E6、同一Y的全部五外点及多外点路径、所有e=m型；单外根实际入出R6已有完整D26反例，不能重列为里程碑。里程碑是保留全部外点共同实现的扩张稳定性引理，或核实完整D30反例；后者将停止D≤29并转向P3。强式 \(f(t)\ge(t-2)_+\) 会给D≤b+2，但目前没有证据支持，不能许诺，也不能因对象数字较小就排在P1/P2之前。

R12/SoCG2025分解作为储备：须证明近极值配置经有界删除进入proper cut，或直接约束prime容量。仅把未知母体改叫irreducible没有进入定理，优先级低于真实全路径操作。

## 8. 收益核算与下一交付

若**独立**证明C≤2b−Δ、D≤b+5−ε，则Q≤3b+5−Δ−ε、777≤3b+6−Δ−ε。H–R耦合η只有相对于已经降低的c,d另证，才能额外相加，不能把旧缺额重记。

| 条件性场景（b25） | C界 | Q界 | 777界 |
|---|---:|---:|---:|
| 当前草稿链 | 50 | 80 | 81 |
| 仅Δ1 | 49 | 79 | 80 |
| 仅ε1 | 50 | 79 | 80 |
| 独立Δ1与ε1 | 49 | 78 | 79 |
| Δ3 | 47 | 77 | 78 |
| P2实际z2，仍C50 | 50 | 77 | 78 |

757始终保持40；将757从40压39，没有新桥梁就不进入Q≤C+b+5链。777精确根等式也消除了独立求解777的必要。b已有单独25构造证据，除非先质疑并检验这些构造，继续压b低于25不是合理主投。

建议只选一条主线P1和一条竞争线P2；P3提供二者共用的全核证书，若P2找不到实际操作可由P3替换，P4仅有限投入备选，不同时铺开四条。先找到机制再决定Δ或z，Δ3、z2只是条件收益算例，绝非目前有证据的预测。下一份交付先固定一个全称陈述和3–5个现有对抗例，再依次证明全类进入、实际共享机制、严格净损失、最后传播。完成全类定理、给完整模型反例、或证明某个机制不能奏效，均算结构进展。增加标记、人口或无进入定理的条件模板不算里程碑。不提供任意成功概率、时间预言或开放式SAT计划；本次不启动作业。

建议固定的对抗资产可取五组：满25的多种ordinary/exceptional目录；D26单外根实际入出红六；D12不交红六及其零成本实际分块；任意残余加单蓝根所得空锁canonical母体；R27完整修复回旧核的零净收益。它们分别检验状态类型、外点相关性、全路径费用、全类进入和净预算，不能互相替代。候选陈述若刻意排除其中某例，应说明新的近满前提是否由目标母体自动满足；否则只是新命名的条件子类。

每个交付的验收顺序也应固定。先检查量词是否覆盖目标母体，再检查同一次实际集合操作，再检查禁形与内部秩，最后计算净损失和数值传播。若第一步没有进入定理，后面再精细的常数也不能成为全局结果；若第三步丢掉混合路径，最后的漂亮缺额仍无效。这样的停止条件允许保留有用局部引理，同时避免再次用完整表示或必要条件替代容量定理。

## 9. 本次审计边界与外部审阅回执

本次只完成当前会话综合、策略审计和主来源抽查；文档执行代理没有生成新数学，也没有作独立数学审查。未改任务metadata、状态、acceptance、旧稿、CNF、proof、封存运行或运行中作业。本次未启动新的科学代码、求解或证明重放；使用本地只读材料并核对公开文献。没有提交或归档。

外部Claude调用在创建job前被automatic approval review阻止，所述理由为“路由disabled，且没有新的对外分享授权”。用户随后明确选择“仅完成当前会话的综合与审计”，因此未重试、未改路由；没有jobId、完成的reviewer thread或外部独立结论。请求模型/effort也不能当成实际backend证据。四份原始trace依次为[request](<D:/科研/math agent/erdos-szekeres-sat-main/.aris/traces/research-review/2026-10-28_n7_synthesis/001-structural-audit.request.json>)、[单次meta](<D:/科研/math agent/erdos-szekeres-sat-main/.aris/traces/research-review/2026-10-28_n7_synthesis/001-structural-audit.meta.json>)、[原拒绝回执](<D:/科研/math agent/erdos-szekeres-sat-main/.aris/traces/research-review/2026-10-28_n7_synthesis/001-structural-audit.response.md>)、[run meta](<D:/科研/math agent/erdos-szekeres-sat-main/.aris/traces/research-review/2026-10-28_n7_synthesis/run.meta.json>)。主会话来源审计不能替代独立证明审阅，任何数学接受状态均未改变。
