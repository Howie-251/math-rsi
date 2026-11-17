# N(7,r,s) 证据台账（截至 2026-11-05）

本表只忠实登记既有来源的结论、适用域和保证状态，不重新证明、审计数学有效性或升级接受。日期是原件记录日期；同日顺序按各更新的依赖关系排列。757/766/767/777 分别记 A/C/Q/F，均为完整有序 rank-3 signotope 的最大允许人口，不是几何强迫阈值。

## 1. 当前数值及证据层级

既有最新全模型工作链是

\[
A\le a+b-1,\qquad C\le2b,\qquad Q\le3b,\qquad F=Q+1\le3b+1.
\]

沿用有效输入 a=16、b=25，得到 **40/50/75/76**。这些上界不主张等号；后续结构工作证明仍为 unreviewed/unaccepted。普通态参考 26/30/31/32 不是一般完整模型容量界。几何强迫关系若运输适用，则为 ES(7)≤F+1，不能把避免人口76直接记成强迫76。[最新全局更新](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_SYNTHESIS_N7_20261103_7576_UPDATE.md>) · [11 月 4 日综合 §1](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-structural-roadmap-20261104/synthesis.md>)。

| 证据边 | 原件记录 | 保留限制 |
|---|---|---|
| b≤25 | [C8 接受记录](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md>)：C1–C10 human accepted、pending 为空 | 限 no B5/R6/weak7 完整有序 rank-3 域；原 same-family/provisional 保证不变，隐藏 backend/model/effort 不补认证 |
| 实际 b≥25 | [E21 verification.json](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n756-professor-review-20261027/evidence/E21/verification.json>)：pass=true；2300 三元组、12650 packet，零 packet/weak 违规，蓝/红高4/5 | 独立存在性证据；本轮未重跑；上界接受本身不产生见证 |
| 后续 A/C/Q/F 链 | 参数化手写工作证明及同会话依赖核查 | 不由 b25 接受连带升级为整链接受；文档 PASS 也不提供数学认证 |
| 11 月 4 日有限评审 | [原回应](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-structural-roadmap-20261104/reviewer-response.md>)、[路由回执](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-structural-roadmap-20261104/reviewer-receipt.json>)、[修正边界](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-structural-roadmap-20261104/review-resolution.md>) | 抽查未发现确认推导错误，不是整链逐行 PASS；backend、实际 effort 和跨模型独立性未核实，acceptance 为 provisional |

## 2. 历史综合与全局工作界演进

| 来源与定位 | 当时记录及变动归属 | 尚未兑现或保证状态 |
|---|---|---|
| [R1–R27 复盘，2026-10-26，§§1–3](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_REVIEW_R1_R27_20261026.md>) | 当时40/50/80/81。历史顺序：45/58/103/206 → R5 44/58/101/201 → R6 b28 下43/56/98/195 → R7 43/56/89/177 → R8 b26 下41/52/83/165 → R20 41/52/83/84 → R23 b25 下40/50/80/81 | R5 实际严格覆盖、R7 不交分解/五点横截、R20 精确根归约是结构收益；b29→28→26→25 是输入收益。R1–R27 并未逐行重新认证；该次 Claude 请求 REVIEW_UNAVAILABLE |
| [综合，2026-10-28，§§2–4](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_SYNTHESIS_N7_20261028.md>) | 保持40/50/80/81；边界覆盖仅 n≥4、4≤r≤n；平衡拆分 C≤2b；canonical Q≤C+D、D≤b+5；F=Q+1 | 一般 C49 仍不可用；完整共同实现和全路径重分划未闭合 |
| [10/28 最优交叠/交换接口](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_OPTIMAL_OVERLAP_EXCHANGE_AND_CUT_INTERFACES_20261028.md>)、[lex 覆盖与耦合成本](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LEX_OPTIMAL_COVERS_AND_COUPLED_PARTITION_COST_20261028.md>) | ρ、完整暴露路径族的批量交换及耦合分划成本接口已有原稿 | 本次综合不把这些接口或重排序认领为新数学；其普适正净收益仍须另证 |
| [综合，2026-10-29，§§3–5](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_SYNTHESIS_N7_20261029.md>) | 保持40/50/80/81；完整保留 R1–R27 台账与后续十份主稿的条件类覆盖 | 共同饱和必要式不等于正净损失；单核反例不等于双满近界母体 |
| [综合，2026-11-03，§2 表](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_SYNTHESIS_N7_20261103.md>) | 汇总10/29三匹配 Q≤3b+4（79/80），10/31前驱压缩 Q≤3b+3（78/79），11/02锁区间 Q≤3b+2（77/78）。10/30加权 n+w≤3b+4、10/31加权 n+w≤3b+3 分别登记 | 同日后续更新已超越开篇77/78；按时间阅读，不覆盖新稿。Q≤C+b+2 未由 Q≤3b+2 推出 |
| [人口更新，11/03](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_SYNTHESIS_N7_20261103_UPPER_BOUND_UPDATE.md>) | 共同中间匹配 n+w≤3b+2；完整低前驱补偿排临界层，Q≤3b+1、F≤3b+2，40/50/76/77 | 阶段排除与统一闭合不重复计下降；同会话 unreviewed/unaccepted |
| [审计与加权更新，11/03](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_SYNTHESIS_N7_20261103_AUDIT_AND_WEIGHTED_UPDATE.md>) | 同会话15项义务核查；参数无关 M0 补写；增强根双向补偿给 n+w≤3b+1；全局仍40/50/76/77 | 下一人口层仅余增强根共同根接口；这时75/76尚未取得 |
| [共同根更新，11/03](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_SYNTHESIS_N7_20261103_COMMON_ROOT_UPDATE.md>) | 排多 owner 纤维与错误锁序，得到实际 b 点中性核对全部外点逐点 R5，及满侧根数预算 | 逐点供给不保证跨侧连接；全局仍40/50/76/77 |
| [clean 闭合更新，11/03](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_SYNTHESIS_N7_20261103_CLEAN_CLOSURE_UPDATE.md>) | 旧根排除、q≥2；关闭人口临界层至少一侧 clean 整类 | 双有锁仍余；全局仍40/50/76/77 |
| [75/76 更新，11/03](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_SYNTHESIS_N7_20261103_7576_UPDATE.md>) | 实际 b+1 替锁域与私有 R5 矛盾关闭整个 n=3b+1 层；Q≤3b、F≤3b+1，全局40/50/75/76 | 新工作证明仍 unreviewed/unaccepted；原加权界 n+w≤3b+1 保持 |
| [75/76 审计与正 through，11/03](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_SYNTHESIS_N7_20261103_7576_AUDIT_WEIGHTED_UPDATE.md>) | 同会话16项依赖核查；排 t=1,w=1，故 n+1[w>0]≤3b，正 through 子类≤74 | 一般 n+w≤3b 尚未证明；t=1,w≥2 加权层与 t=0,w0 人口层保留 |
| [t0 更新，11/03](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_SYNTHESIS_N7_20261103_T0_CRITICAL_UPDATE.md>) | I=∅ 时 n+max(∣U∣,∣V∣)≤3b；D 有 R5 整类≤74。临界 I 空时 S/D/T 各b点、四实际供应 | 严格交错、严格分离、共同根/锁根、空根族但 I 非空仍开；复制族只到2b+20=70，不能排满50 |
| [regular 共同根更新，11/04](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_SYNTHESIS_N7_20261104_COMMON_ROOT_UPDATE.md>) | 限 w0、有效共同根 z∈I\Γ、I 内左锁晚于z且右锁早于z：n+Λ≤3b，Λ=h0+max(u+hU,v+hV)。n=3b 迫这些权重零，只余 eL/eR/dD 之一为1 | 只覆盖指定 regular 接口；三支不等于全局穷尽目录，指定覆盖亏一不排其他更好覆盖。全局40/50/75/76未变 |

## 3. 11 月 4 日结构报告（按来源依赖顺序）

以下均为 same-session、unreviewed/unaccepted，均未新增全局工作数值界。令 f_p(r)=binom(p+r−3,p−2)、c_p=binom(2p−4,p−2)。

| 原件定位 | 确切记录的整类结果或操作 | 未闭合接口 |
|---|---|---|
| [structural-theorems，§§1–5](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-structural-theorems-20261104/research.md>) | S<D<T 四供应下，全部 D 内 R_(p−1) 首 pair 扇轮廓给完整端点矩形；三满核至多两类时 b≤max{c_p+p−1,d_p+2(p−1)}，d_p=binom(2p−4,p−3)。p5 为 b≤24，含 singleton 整支 | 轮廓≥3、非分离三块、I 非空等未覆盖；后续 ordered 全轮廓结果见下 |
| [同稿，§7–8](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-structural-theorems-20261104/research.md>) | regular 旧并核候选会恢复全部被删 R6 的机制障碍；13点三合法根解析例，各删根 chart 有 R6 且 w0 | 否定具体候选与无临界前提快捷式；未否定一般 P1b 或临界根循环目标；13点例未机械运行 |
| [extremal-stars-and-run-exclusion，§§1–3、7](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-extremal-stars-and-run-exclusion-20261104/research.md>) | 全部有序四供应类 min(∣S∣,∣T∣)≤m_p=f_p(floor((p+1)/2))，p5≤10，轮廓数不限；临界 I 空连续纯D段≥19整类排除，Γ5(κ5(6))=Γ5(10)=24 | I 非空、I 空全部纯D段≤18仍开；一般 H≤9与从任意母体提取实际11/5双星未证明 |
| [hall-stars-and-critical-exchange，§§1–5](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-hall-stars-and-critical-exchange-20261104/research.md>) | I 空实际全部 R_(p+1) 端点图 Hall；最早末点入度≤λ_p=f_p(floor(p/2))+f_p(ceil(p/2))+1。p5：r=0/1/2分别 b≤15/22/24，故全部排除。度一末点可全子集同步交换，总量≤c_p | Hall 不传给仅纯D路径的子图；紧 Hall 非平凡分量换入域可能产生新源，不能都归D |
| [同稿，§§6–10](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-hall-stars-and-critical-exchange-20261104/research.md>) | 角色饱和限定接口下长纯K段整类排除；任意767终点段屏障；极端源后至少两个D，反序亦同 | 不是一般 I 非空 r≤2 排除；I 空 r3 共同结构继续开放 |
| [shared-paths-and-safe-prefix，§§1–4](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-shared-paths-and-safe-prefix-20261104/research.md>) | 安全补入实际 m 点与末域 Q 给 ∣Q∣≤b−m；若 H 命中其余全部长路径，h=∣H\Q∣，则 n≤M+b−m+h≤3b−m+h。共同前缀、最大末点经过末D、统一红尾扇分别关闭明确接口类 | 任意临界母体提取 m=2、h≤1 未证明；需覆盖全部路径，不能只看供应或private族 |
| [同稿，§5](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-shared-paths-and-safe-prefix-20261104/research.md>) | I 空r3中 J=F∪D+、Z=D∪F 实际 R5 端点图满足 ∣J∣=f+3≥13、α(J)≤3 | 从同一染色推出四点独立集或可至多四色仍未证明；不得预设perfect/interval |
| [single-through-terminal-separation，§§1、7.1–7.2](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-terminal-separation-20261104/research.md>) | 临界单交叠 I={σ}、(P∪D)<Q 给 b≤c_p+4，p5排75，该类≤74；扩展特定唯一中性R_p源末的交错类。缺额统一 δ+i=1、P<Q且D<Q亦 b≤c_p+4；I空终端分离74与旧75均排，该类≤73 | 完整I空r3、一般I非空r2、共同支撑的2换1仍开；不能外推全局73/74 |
| [canonical-tail-and-deletion-barrier，§§1–5](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-canonical-tail-and-deletion-barrier-20261104/research.md>) | I空临界且S<T，r_j≤p−2、ℓ−r_j>f_p(a−1)、b−j>f_p(p+1−a)时整类不存在。p5 r3余支被迫ℓ=4、r0=…=r4=3，三个晚D全在第五T之后 | 只是残支共同必要结构，未排母体；完整2换1横截仍未下降 |
| [同稿，§§6–9](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-canonical-tail-and-deletion-barrier-20261104/research.md>) | I空临界r≥2时，单删后可达右终端分离 iff maxD<t1（t1是第二T）；成功删点恰为全部入t0长路径的物理点交集。反序同理。最新r3余支两向均不可达 | 结束该单删运输路线，不表示r3不存在；安全补入全局m2/h1、四点独立集、全局74仍未证 |

## 4. 具体反例与固定公式证据（与全类结论分列）

| 来源/实际数据 | 已记录的否定或验证范围 | 不能外推 |
|---|---|---|
| [D12 语义回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_disjoint_path_mechanism_20261027/sat_semantics.json>)；[原稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_ALL_CLASS_RESIDUAL_AUDIT_AND_DISJOINT_R6_COUNTEREXAMPLE_20261027.md>) | 实际不交R6，否定残余R6必两两相交 | 非近满共同饱和反例 |
| [D26 语义回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_joint_extensions_hr_20261027/single_root26/sat_semantic_result.json>)；[原稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/D7_JOINT_EXTENSIONS_AND_H49_COMMON_CORE_20261027.md>) | Y25+a、a同时入出R6、τ1/α25；否定单外根加满25自动刚性/正缺额 | 非H50或X80实例 |
| [满25内部插入原稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_FULL_CAPACITY_INTERNAL_INSERTIONS_AND_PATH_EXCHANGE_BARRIER_20261028.md>) | 完整实际单核见证阻断自动把内部路径搬到指定端点 | 不否定带双满共同条件的端点运输 |
| [12点rootcycle/uncrossing原稿 §7](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_ARBITRARY_ORDER_PRODUCT_AND_GLOBAL_ROOT_BARRIERS_20261030.md>) | 全合法删根chart均w0；另有交错R6反例 | 只否定无近满前提版本，非临界777反例 |
| [13点through-clique族原稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_THROUGH_CLIQUE_COUNTERFAMILY_AND_LOWER_PARAMETER_FRONTIER_20261103.md>) | 3p−2点实际族，单色through clique与双向供给可共存 | 不排两色四满核目标 |
| [canonical十点联合插入，附录](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_T0_COMMON_ROOT_EXCESS_EXCLUSION_20261104.md>) | 两次单独插入合法但联合违法；实际757三相交B4块 | 非40点近界反例，不否定带共同条件的联合交换 |
| [17点完整颜色](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_four_r5_chain_20261104/coloring.tsv>)、[validation.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_four_r5_chain_20261104/validation.json>)；[解释 §§6.1–6.4](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-shared-paths-and-safe-prefix-20261104/research.md>) | Linux既有验证：680三元组、2380packet、131054递增子集、136端点对；违规0、红蓝高5/5、同端和≤8。四顺次R5存在，且端点图Hall失败 | 否定链数或无incoming B5本身即矛盾；非满25双极饱和反例 |
| [12点r2完整颜色](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_four_r5_chain_20261104/coloring-r2.tsv>)、[r2-validation.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_four_r5_chain_20261104/r2-validation.json>)；[解释 §7](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-shared-paths-and-safe-prefix-20261104/research.md>) | Linux既有验证：220三元组、495packet、4083子集、66端点对；违规0、红蓝高6/4、同端和≤8。I={σ}且极端源后两个D，实际R6跳过末D | 非75点临界反例；保有共同前缀/统一红扇的放大类已受该报告容量界约束 |
| [Through14 固定字节回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/balanced49_abstract_port_20261026/through14_replay_result.json>)、[Joint17 result](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_proof_completion_20261027/joint17/result.json>) | 既有固定公式结果：Joint17 strict-RUP PASS，59479源子句、102563添加并导空 | 固定公式反驳不替代任意母体的完整共同赋值运输或人工接受 |
| [Closure result](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_proof_completion_20261027/closure/result.json>)、[停止回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_proof_completion_20261027/closure_acquisition/abort_receipt.json>) | schema PASS；UNSAT_checked=false、actual_cnf_equality_checked=false；ABORTED_BUDGET_FEASIBILITY、CNF_binding=false | C49未闭合，不能用该PASS认领49 |

## 5. 搜索覆盖与文档检查

本次以 PowerShell/rg 检索根目录 `RESEARCH_REVIEW_R1_R27_20261026.md`、`RESEARCH_SYNTHESIS_N7_20261028.md`、`...20261029.md`、全部 `...20261103*.md`、`...20261104*.md`，以及 reports 的 N7 20261104/20261105 文件名。除首批四份结构报告外，又定位上述 **single-through-terminal-separation** 与 **canonical-tail-and-deletion-barrier** 两份11月4日后续原件；截至本次检索，未定位11月5日新增数学研究原件。此结论限这些实际检索范围，不是全仓穷尽或外部文献查新。

本台账执行者仅做文档写入与一致性检查，未运行科研代码、Python、枚举、solver、证书重放或review。既有机器回执均按原件登记，未重新执行。来源本身的文档 PASS 不作数学保证。主会话唯一新鲜评审任务已于2026-11-05 03:17:17 UTC以failed结束，result=null、REVIEW_UNAVAILABLE，没有返回评审意见或reviewer memory，未重试。终止状态不等于成功完成评审或接受；本轮综合与路线判断仍未独审。见 [review-state.json](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-structural-roadmap-20261105/review-state.json>) 与 [review-outcome.md](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-structural-roadmap-20261105/review-outcome.md>)。

