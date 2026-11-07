# RESET R1–R27 研究综合与结构路线审计

日期：2026-10-26。范围：当前 `10-19-nr7-structure-capacity` 任务中，从 `RESTART_SETTING_ANALYSIS.md` 开始的 RESET R1 至 R27；不是更早归档的 RTQ R1。本报告由主会话依据原始数学稿和接受文件作研究判断，文档执行器负责整理。它不是 27 轮证明的逐行认证，不产生新定理接受状态。

**主要判断：研究已经出现较强的局部最优趋势，应把主投从继续细分局部供应模式，转为同一实际母体的联合取等与正缺额定理。** 最有价值的历史跃迁是 R5 的全局严格一单位、R7 的真实不交分解、R20 的对称模型精确归约；近十余轮大量工作改善了条件分支覆盖和反例校准，却没有再给全模型统一正缺额。这个判断不等于方法无用：当前材料已把“缺什么”压缩得相当明确，下一步应证明该缺口，或构造反例迫使路线转向。

当前能够组合出的研究草稿界为 **757/766/767/777：40/50/80/81**，普通目录参照为 **26/30/31/32**，相应上界差为 **14/20/49/49**。其中 $b=25$ 已在 10 月 26 日获得限定模型内的正式人工接受；整条结构组合链仍未独立审阅、未正式验收。开展更多理论轮次前，应先有限投入地审计外部49证明的模型假设；在迁移尚未建立时，优先目标是一般平衡类的同母体共饱和排除，争取 $N^{\mathrm{sig}}(7,6,6)\le49$；另一主线是允许独立50存在、直接证明 H–R 在同一母体里不能同时取满。两者都必须有全覆盖入口和实际操作，不能只给缺额重新命名。

本次独立 Claude 审查仅尝试一次，结果 **REVIEW_UNAVAILABLE**，没有审查报告、没有完成的 reviewer thread、没有替代审查或自动重试。因此，以下战略结论是主会话的文档与来源评估，不能称为“通过独立审计”。失败原始记录见[本次 trace](<D:/科研/math agent/erdos-szekeres-sat-main/.aris/traces/research-review/2026-10-26_r1-r27-structural-audit/run.meta.json>)。

## 1. 先固定模型、数量与证据状态

令 $N^{\mathrm{sig}}(n,r,s)$ 表示有限完整有序 rank-3 signotope 中，同时无蓝 $r$ 点路径、无红 $s$ 点路径、无 weak $n$-gon 的最大点数。每个递增三元组完整染红或蓝，每个四点包至多一次变色。路径长度按顶点数；weak 禁形要求两色路径共享**同一对实际左右外端点**，长度和为 $n+2$。R20 的论证由模型推出需要的内部不交性质，不应事先更换模型定义。

记 $P_B(x,y),P_R(x,y)$ 为固定实际端点的最长两色路径长度，则 weak-free 条件给出

\[
P_B(x,y)+P_R(x,y)\le n+1.
\]

两条来自不同端点、不同子配置或不同 chart 的路径，不能因为长度合适就合成禁形。诱导子配置必须重算所有路径、rank、state；ambient 路径能给子配置约束，却不自动成为子配置内部的路径见证。这是 R1 起始设置以及后续供应、删除和合法 chart 变换的共同底线。chart 指对同一抽象配置选择合法点序及对应符号的表示，不是绘图。参见 [R1 §1、§3–4](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESTART_SETTING_ANALYSIS.md>)、[R20 §2–4](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>)。

下文以757等三位数简写参数 $(n,r,s)=(7,5,7)$ 对应的容量，766、767、777同理；“实际核”只指母体的一个实际诱导子配置，不意味着唯一标准核。“共同实现”要求多组路径和状态来自同一完整染色母体，不能分别取各自最优的见证再拼起来。此处的普通目录是比较参照，差值为所给粗上界与参照之差，不是已知极值与参照之间的精确差。

这里的 $N$ 是“避免配置的最大规模”，不是强迫阈值。若几何点集向该模型的解释适用，则几何强迫阈值至多 $N^{\mathrm{sig}}(7,7,7)+1$。因此草稿的避免界 81 对应条件性强迫界 82。不能把避免 81 直接写为 $\mathrm{ES}(7)\le81$。

| 证据层级 | 截至本日能说什么 | 不能顺带推出什么 |
|---|---|---|
| C8 及 C1–C10 正式人工接受 | 在完整有序 rank-3、no B5、no R6、no weak7 域，所有有限阶满足 $m\ge e$、$N\le25$；review assurance 保留 same-family/provisional | C8 本身不构造 25 点，也不直接证明无限制几何 ES 界 |
| RESET R1–R27 数学稿 | 可以研究、比较其参数定理和条件分支；本文注明其依赖 | 主会话自检、文档检查、来源清单均不等于独立数学验收 |
| R23 的 25 点解析构造稿 | §9 分别提供 $e=m=0,7,8,10$ 的构造与目录校准 | 不是本次新运行、独立检查过的机器见证；不能回写为 C8 的存在性结论 |
| 本次独立审查请求 | 固定路由的一次调用失败，保存完整请求和失败证据 | 没有独立报告、通过结论、后端模型或实际 effort 的确认 |

正式输入以 [C8 接受记录](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md>) 和[基数层定理](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/cardinality-layer-theorem.md>) 为准。C8 的量词覆盖全部有限阶；它不是仅检查 26 个点后未经说明的外推。十行给出 $C_k:e\ge k\Rightarrow m\ge k$，结合异常数范围及 $N=25+e-m$ 得到 25。既有 proof/CNF/checker 绑定和历史接受范围均沿原记录，本报告没有重放证明。

## 2. 贯穿 27 轮的真正数学骨架

### 2.1 状态单射有用，但状态目录本身没有表达共同实现

令 $\sigma(u,v)$ 是以实际终端对 $(u,v)$ 结束的两色最长路径标签，$D(v)$ 是这些标签的下闭包。R1 的关键事实是

\[
\sigma(u,v)\in D(v)\setminus D(u),\qquad u<v.
\]

因此点到状态单射，全矩形目录有 $\binom{r+s-4}{r-2}$ 个下理想；普通状态数记为 $O$，实际异常占用数和普通缺失数分别记为 $e,m$，于是

\[
|X|=O+e-m.
\]

这个单射主要依靠完整染色和精确路径扩展；不能把 signotope 与 weak 约束“已用于单射”当作容量已被榨尽。相反，R2–R4 显示压缩起点、双向理想或端点目录后，可能失去单射或留下多重纤维。状态变少、投影更精细、必要不等式增多，都必须最终兑现为真实 $e-m$ 上界。

在常用三参数范围 $\max(r,s)\le n\le r+s-2$，普通参照为

\[
O(n,r,s)=\sum_{j=n-s}^{r-2}\binom{n-2}{j}.
\]

R12 在递归统一可分类中给出精确 $O$ 上界及几何递归构造；这不等于一般 signotope 类已被证明满足 $N=O$。为解释一般切分式，令 $a(Y),b(Y)$ 是 Y 内部实际蓝、红最长路径的顶点数，定义普通目录函数

\[
\Phi_n(a,b)=1+\sum_{\substack{1\le w\le a-1,\ 1\le h\le b-1\\w+h\le n-1}}\binom{w+h-2}{w-1}.
\]

空状态计1。置 $\phi_Y=\Phi_n(a(Y),b(Y))$，实际切分内节点的 slack 为 $d_Y=\phi_Y-\phi_{\mathrm{left}}-\phi_{\mathrm{right}}\ge0$。对一般实际切分树，R12 §6 的恒等式是

\[
|X|-O=\sum_{L\text{ leaf}}(e_L-m_L)-\sum_{Y\text{ internal}}d_Y-(O-\phi_X),\qquad d_Y\ge0.
\]

所以正超额最终落在不可统一切分的 prime 叶上。但根本身可能就是一个 prime 叶；R12 §9.2 给出真实五点校准。该恒等式指出了困难所在，没有自动把困难缩成小对象。参见 [R12 §4–6、§9](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R12_COMMON_REALIZABILITY_AND_UNIFORM_DEFICIT.md>)。

### 2.2 先写参数定理，再代入 7 和 25

目前支撑全局链的主要结构草稿只有少数几条：

\[
N^{\mathrm{sig}}(n,r,n)\le N^{\mathrm{sig}}(n,r-1,n)+N^{\mathrm{sig}}(n,r,n-1)-1,
\quad n\ge4,\ 4\le r\le n.
\tag{A}
\]

这是 R5 的严格增广思想在 R6 的一般化，载荷在于全局点对偏序、支持图无环和真实合法加点；不能把第二个严格单位凭对称性再收一次。参见 [R5](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R5_COVER_AUGMENTATION_CAPACITY.md>)、[R6 §6](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R6_OVERLAP_TWO_AND_766_TRANSFER.md>)。

对 $n\ge6$，设 $Q_n=N^{\mathrm{sig}}(n,n-1,n)$、$C_n=N^{\mathrm{sig}}(n,n-1,n-1)$，R7 给出同一母体的实际分解

\[
X=H\sqcup R,\qquad Q_n\le C_n+D_n.
\tag{B}
\]

$D_n$ 是无蓝 $(n-2)$ 路径、无 weak n，且内部没有“红 $(n-2)$ 路径末点同时为蓝 $(n-3)$ 路径起点”的残余类容量，**不是**普通 $N(n,n-2,n)$。在 $n=7$，五点横截机制给 $D_7\le b+5$，其中 $b$ 是有效的 756 上界。五点横截不能直接推广到所有 $n$。参见 [R7 §3、§8.4](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md>)。

R20 最关键的架构变化是

\[
N^{\mathrm{sig}}(n,n,n)=N^{\mathrm{sig}}(n,n-1,n)+1,\qquad n\ge4.
\tag{C}
\]

上界方向通过合法径向 chart 后删除一个实际根；下界方向对任意合法小模型真实添根。它给精确的一点差，而不是两份较大容量相加。根的这一单位已经付清，不能再以“根造成损失”为名加收。该操作不保所有不对称短色帽，也不授权任意内部 pivot。参见 [R20 §3–4、§7](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>)。

令 $a,b$ 分别为有效的 747、756 上界，旧工具组合为

\[
N^{\mathrm{sig}}(7,5,7)\le a+b-1,\qquad N^{\mathrm{sig}}(7,6,6)\le2b,
\]
\[
N^{\mathrm{sig}}(7,6,7)\le3b+5,\qquad N^{\mathrm{sig}}(7,7,7)\le3b+6.
\tag{D}
\]

代入旧外部输入 $a=16$、现已接受的 $b=25$，得到 40/50/80/81。这里 747 的输入地位、(A)–(C) 的草稿地位与 b25 的正式接受地位应分开。R8 当时采用 b26；R23 后来采用用户 b25 工作基线；**实际人工接受 b25 发生在 10 月 26 日**，不回写历史轮次。

## 3. R1–R27 全轮次台账：收益在哪里停止

下表“新增全局收益”指该轮新结构独立带来的全模型数值变化；局部分支排除和反例仍有研究价值。四项数字始终按 757/766/767/777 排列，属于当时草稿链。

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

因此，R9–R19 和 R21–R27 的新结构全局数值收益为零；R8、R23 的下降主要是输入 b 的更新。不能据此抹掉它们的条件覆盖进展，也不能把覆盖增加换算成尚不存在的全局下降。

## 4. 为什么判断为局部最优趋势

第一，条件收益的前提持续未被母体强迫。典型形式是“若某条共同尾、某个 fan、某种有限 owner 布局存在，则少一点”；之后不断放宽布局，但一般母体仍可能没有该入口。排除 q=11 与 m≥11 是实质覆盖，可是 q=1…10、m,m′=5…10 仍容纳共同饱和；没有新的全局覆盖定理时，多做相邻人口情形不会自动逼近闭合。

第二，修复或替换的净收益常恰好为零。R14 的完整优化回到原预算，R17 的便宜修复被核心扩张抵消，R27 §3 的 canonical 操作回到旧实际25核。操作本身完全合法不等于产生严格损失。新的证明应把保留人口、新增人口、删除人口和旧 slack 写在同一个等式里；只强调删得更少会重复计算收益。

第三，共享供应不能独立收费。同一实际路径、owner、neutral 点或出口能够服务多项要求。R16–R19 已用真实小模型说明“桥多”未必意味着删除贵，“双向需求多”未必意味着有两个独立池。R26 的全 X 预算需要保留以下实际身份。

这里 X 属于实际767类，$\delta=3b+5-|X|$。$F_+$ 是全部同时启动 R6/B5 的实际源中，**所有**红6终点与**所有**蓝5第二点均锁定为同一个实际出口的源；$F_-$ 为反序对偶族。$\varepsilon_K,\varepsilon_D\ge0$ 是同一次批量操作所得实际 K、D 的剩余容量，不能从不同操作分别选最优值。

\[
|X|+|F_\pm|\le3b+5,
\qquad\delta=|F_+|+\varepsilon_K+\varepsilon_D,
\]

但只能推出 $\max(|F_+|,|F_-|)\le\delta$，没有证明两者之和也小于 δ，更没有迫使任一锁定族非空。这个接口已经相当强；当 δ=0 而两族均空时继续改名记账，不能产生新的一点。参见 [R26 §2.4、§4.3](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R26_GLOBAL_BREAKTHROUGHS_AND_EXTREMAL_COUNTERTESTS.md>)。

第四，必要充分表示正在替代容量不等式。R27 的 π/record/e 标准形比固定模板更完整，但依然要证明不存在满足全部端点预算的16点赋值。把未知转换成表示是合理压缩；若没有闭合更新规则和新容量定理，它还不是上界。R12 的 prime 叶同理：定位困难不能当作解决困难。

从研究管理角度，这些迹象指向“同一抽象层的边际回报下降”，不是数学上的不可行性定理。完整覆盖一个先前遗漏的无限族仍然值得记录；但若剩余母体没有变小、净预算没有改变，就应把精细局部工具存为引理库，停止以该工具继续加轮次。反例校准的价值也在这里：它能告诉我们哪一类结构信息必须保留，而非只告诉我们某个漂亮猜想失败。

历史上真正改变全局界的 R5/R7/R20，恰好都改变了**全局组织方式**：严格增广、实际不交分解、精确降一阶归约。这支持下一轮优先换定理层级，而非继续给已有账本增加标签。也必须保留反例的准确范围：R17 的参数族不能否定766专属结论，R27 十点反例不能否定所有高容量接口，critical16 子类不能代表一般766。

还有两项应及时止损。其一，b25 已改变取等类，历史“假如26则 e8/m7”的规范化不能移植为“一切满25都是 e8”。R23 §9 的 e0/e7/e8/e10 正是强制校准；b 本身已有25点解析构造草稿支持其尖锐性，继续压 b 不是合理默认主投。其二，R18 §0.1 已指出，incident pairs 的顺序由三元颜色确定，改变全局线性扩张 λ 不会改变各顶点的最小 incident pair。不能把“优化 λ”当作免费极值操作；真正换 chart 又必须证明 weak 与短色帽如何运输。

## 5. 外部位置：内部突破和文献贡献分开

已查到的 Schroeder 预印本伴随页报告 2026-09-19 v1 的 $\mathrm{ES}(7)\le81$、$\mathrm{ES}(8)\le319$ 和平面非对称25界；该页明确不是外部同行评审结论。本次只核对来源和局部源码，不重新验证其 Lean、CNF 或 refutation。因此它是**已查到的预印本报告值**，不是本报告独立确认的最新纪录。[伴随页](https://michaelschroeder.ai/research/ErdosSzekeres/companion)

本地 `heptagons.tex` 的 Equality partition、Population certificates 和 Balanced heptagon bound，给出了值得直接研究的全局模板：同一50点母体的四个实际 starter/end 集共同取25；through 人口至多13、特定带外供内部类至多19、双极端人口至少一类至多16，再合到一个共同赋值。下一步应抽取这些断言的精确假设，判断哪些只用 packet 与同端点条件，哪些依赖几何解释及证书接口。直接继承几何49或重跑已经结束的 C_r 都不能替代这个迁移证明。[本地源码，约129–214行及216行后](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/paper/heptagons.tex>)

Baek–Balko 的 SoCG 2025 文献在 decomposable 类中讨论 Erdős–Tuza–Valtr 型结论，并将一般 signotope 版本保留为开放问题；因此“递归类精确 O”和“全 signotope 精确 O”不是同一难度。[论文 §2 Theorem 8、§3](https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/html/LIPIcs.SoCG.2025.13/LIPIcs.SoCG.2025.13.html)

Rote 的预印本 Appendix B 已讨论 marked-pivot 的抽象 order-type 视角；R20 内部从165到84的改进应作为本项目架构修复评价，不能仅凭内部数字差宣称文献新颖性。[Rote Appendix B](https://arxiv.org/html/2503.02336v1) Baek 的 ETV 参数公式及平面等价叙述也须保持原模型，不能免费提升为任意 signotope 迁移定理。[Baek，摘要与 Theorem 1.5](https://arxiv.org/html/2206.04260v2)

## 6. 下一步路线：先给定理目标和第一条缺失引理

### 前置：有限投入的外部基线与假设审计

在继续攻50之前，应先回答一个可能改变主投的问题：外部 balanced49 证明是否只用了本项目已有的 rank-3 四点包、实际路径及同端点 weak 语义？如果是，50瓶颈可能已被外部结果在同一域中解决，后续应从49出发；如果不是，应指出精确的几何专属前提，而不是笼统写“模型不同”。当前只读过相关源码，没有建立全部有限语义覆盖，故这里保留条件判断。

这项工作应交付一个小而完整的假设映射表：每个外部结构引理需要什么，当前 signotope 模型提供什么，选点后哪些 rank 重算、哪些仍是 ambient，compact CNF 每条约束如何由实际母体满足。重点是“每个目标配置都给出一个被否定公式的赋值”，而非观察公式中出现 packet 字样就宣称可以迁移。即使公式只表达必要条件，仍须证明选点、owner 标记和所有取等人口的有限覆盖。几何对偶、反射和 projective/root 操作也分别核对。

这属于来源与语义核查，不自动构成人工接受的导入，更不意味着现在启动证书检查。若迁移成功，49+30 给出避免79、对称避免80和强迫81；要得到新的强迫80仍需**额外一单位**。若迁移失败，留下具体缺失前提，路线 A 的第一条引理就有明确对象。此步骤能够避免在已经外部解决的子问题上继续积累内部局部情形。

### A. 近期最高优先：一般平衡类的联合取等排除

**目标。** 对同一个实际平衡配置 X 和有效非对称容量 b，证明

\[
2b-|X|\ge1.
\tag{E}
\]

入口应使用该 X 的全部实际两色 starter/end 集。第一条缺失引理不是“某一类25核不可扩”，而是：**四个实际满25核的共享供应，不能在同一 X 同时实现全部取等条件。** 要给真实增广、交换或修复；或者直接强迫一对同实际端点的禁配路径。局部人口表可以参与证明，但必须说明每个 X 都进入哪一分支，且所有替代供应已覆盖。

必备校准是 R23 的 e0/e7/e8/e10 四种25目录；若拟议引理只看 e8 固定家族，必须立即修改假设或退回条件命题。外部13/19/16人口结构可提供候选桥梁，但每条必须重建参数级证明，或精确证明模型到现有证书的赋值映射。仅仅获得另一份取等分划没有解决共同实现。

**可执行的中间定理：带实际外供的边界延伸容量。** 设 ambient X 无 $B_{p+1}$、$R_{p+1}$ 和 weak n，实际 $Y\subseteq X$ 内部无 $B_p,R_p$，且 $\max Y$ 是 ambient 一条红 p 路径的实际起点。研究是否能在一个明确证明有效的参数域内得到

\[
|Y|\le\binom{2p-4}{p-2}-d(n,p).
\tag{E1}
\]

这里不能先定义 d，再把它当作正缺额。当前真正的候选是 $d(7,5)\ge1$：经典内部容量20在实际末点外供条件下下降至19，正对应外部 population(ii) 的20→19。这比直接复述“所有50不存在”更像一条可以抽取、证伪或迁移的结构定理。其他参数上 d 是否为正必须单独证明，不宣称普适。

R23 的经典满容量实际末 pair 供应可作为输入，但外部红路径必须保持实际身份；内部供应与 ambient 供应相接时，要核对同一端点和连接三元颜色。不能把不同诱导集合中分别存在的链混接。即便(E1)的当前目标成立，它本身也**不证明49**：仍须把 through 源终限制和四集合取等条件放进同一个赋值，排掉剩余共同实现。这给出了该中间定理的用途，也防止又把一个必要人口限制误当作最终闭合。

**收益。** 若(E)成立，b25 给 766≤49；由旧残余30和 R20 得 767≤79、777≤80，几何强迫≤81。这匹配上文预印本报告值，不超越81。最小有效反检是构造实际50，或给所提关键引理一个符合全部路径条件的反例；发现真实50就应停止一般49目标，转向 B。没有全覆盖入口时，停止继续追加单个 q/m 人口情形。

### B. 同一母体 H–R 的联合极值相容性

**目标。** 在 R7 的实际 $X=H\sqcup R$ 中，若 u,d 分别是两类单独有效的界，证明对同一 X 有

\[
(u-|H|)+(d-|R|)\ge k.
\tag{F}
\]

于是 $Q_7\le u+d-k$，$N^{\mathrm{sig}}(7,7,7)\le u+d-k+1$，强迫阈值≤$u+d-k+2$。取 u=50、d=30，k=1 给强迫81，k=2 才给强迫80。这是待证目标；给出 δ 的定义或等式不构成(F)的证明。

第一条缺失引理应覆盖 R26 中 $F_+=F_-=\varnothing$ 的零缺额分支，以及共享出口和实际 residual 预算，不能把正反两个 max 不等式相加。可单独检验的残余子目标是：对每个大小5的最小横截 T，都有 $|R\setminus T|\le b-1$，从而 $D_7\le b+4$。它目前未证；应先面对完整残余类。若独立30确实存在，仍可研究它与 H50 是否相容，无需否定30本身。

操作上，较小删除集可能使保留核心变大，必须计算净收益。要形成新的几何强迫80界，总共需要两个未重复的一单位，不能把已有根一点或同一 saving 重新收费。

这条线的意义在于独立极值相容性与单独极值存在性不同。即使 A 被实际50反例推翻，也不能推出 H50 能和残余30共存。反过来，即使找到独立残余30，也不能推出80母体存在。研究对象应是实际嵌入后的两侧路径如何共用首末点、neutral 和所有替代尾，而非两张孤立配置的整数规模之和。新引理若只控制一条选定最优路径，应先检查换另一条合法见证后是否仍然成立。

### C. 中长期：prime 组件的结构定理

R12 已把超额集中到 prime 叶。可追求：每个近极值 prime，要么允许具有量化净收益的合法增广，要么强迫一个有限的同端点障碍和正缺额。定理必须同时提供进入条件、实际操作和可加成本；共享见证不能分别收费。

适合起步的对象是目标平衡类、H–R 联合类的 deficit1/2，或带根 profile 的精确接口，而非宣称“所有 prime 都≤O”。后一命题几乎直接触及一般 ETV 目标，不能包装为廉价下一引理。若采用有限状态转移，须证明对实际扩展封闭，并有容量不等式；纯标准形和未受控的状态数不能算闭合。出现根叶规模仍无界、接口信息无法传递时，应收缩定理范围。

### D. 有限投入的竞争方向：critical16 构造反检

这条线用来检验“766 的30天花板是否可信”，不预设上界正确。R26 §8 定义带极端根的17点模型：内部16点是766，根峰≤(3,2)或换色，逐点根 profile 和≤4。在 **g4/g4 子类内**，critical16 存在等价于31存在，也等价于32存在。正见证会给实际32，推翻该 signotope 子类的30天花板，但不自动成为几何 ES 反例；完整否定也只关闭 g4/g4，g3/g5 及一般 prime 仍开放。

R27 §5 的完整 π/e 表示和全部端点预算可作为准确接口。自然16模板、旧固定 T44 六尾和任意饱和经典核的若干整类已经被排，继续小改旧30块的回报低。应先在符号层找新结构或排除引理，必要时才把**完整17点680个三元颜色**作为有限反检；本报告不授权启动求解。R27 的十点 laced→inverse 反例要求任何接口先检查全部两色帽和同端点预算，不能凭“交织很密”推断变换后出现障碍。

### E. 支持方法：把计算结果提炼成可迁移的结构句子

已接受的 $m\ge e$ 以及已知紧等式可以启发统一 shared-witness 子句、人口限制和交换引理。计算的合理角色是反驳一条精确候选定理，或在完整缩减定理后认证有限剩余核心。F3 等编码工程改善求解能力，本身不等于新的数学进展。已结束的756参数扫描无需重开；若移植外部已认证49，应列为模型迁移及基线建立，不冒称新的研究界。

## 7. 下一轮应交付什么，什么情况下停止

建议保留一条主线 A/B 的共同实现证明，加一条有投入上限的 D 构造反检。下一次工作先压缩证明依赖 DAG，列清 R5/R7/R20 与正式756输入的接口，再写**一条**针对所有 X 的候选平衡或联合缺额定理，包含四件事：假设、实际操作、统一数量式、能够推翻它的反例条件。研究方向排序是判断，不给没有依据的成功概率。

每轮结束只计三类可复核进展：全局界是否改变；是否新增一个覆盖全类的结构引理；尚未覆盖的家族是否被严格、可量化地缩小。只有标签增多、标准形变长、未知量换名或净预算为零，就停止该粗化。条件覆盖可以记录，但不能被写成未发生的全局改善。独立审查恢复后，应优先审真正承重的依赖链和新候选定理，而不是要求审阅者在27轮长稿中替研究者选择目标。

为了让“进入全类”可检查，下一份候选定理应明确回答以下五项。第一，输入是任意 X，还是已经假设满50/满80；近满非零缺额是否需要另证。第二，所选源终、横截、chart 是否在同一个母体中同时定义，是否允许为不同子结论另选更有利对象。第三，删除或增广后完整四点包、两色短帽和所有同端点 weak 是否保留。第四，正缺额来自哪个互斥事件，已收过的根、重叠或 neutral 为什么不会再收一次。第五，现有真实小模型和25点多目录是否满足该引理的假设，若满足又为何不成为反例。

停止标准也应对应上述量词。一个特定 fan 被全位置排除，可以结束该 fan 架构；它不能结束一般母体。某个充分条件被反例推翻，应撤回该接口或收窄其域，不能仅增加例外名称而继续把它列为全局主线。反之，一项排除虽不降全局界，若确实关闭一个此前未覆盖的无限族，应保留其定理价值并注明剩余族。这样的台账同时保护已有成果和研究预算。

最后，文献基线核查、结构定理、构造反检、证明接受是四种不同交付。来源核对只能决定优先级；提出目标只能决定下一问题；新解析构造仍需独立核验；完整数学推导也仍需沿项目接受流程处理。把这四步分清，会比继续增加轮次更快地判断此路线是否值得持续投入。

本文已完成的是用户所需的源文件综合与路线判断；没有进行 SAT、枚举、实验、证明重放、运行中任务调整或新的数学验收。所有代码和 solver 工作仍以 Linux 服务器为执行目标；本次没有启动任何作业。上面的路线是后续交付建议，不是额外自动执行授权。

## 8. 独立审查失败的完整出处

| 项目 | 原始观察 |
|---|---|
| 请求 | semantic `claude-fable-5-1`；wire `claude-fable-5-1-reversed`；deep/max；tools `Read,Grep,Glob` |
| 请求任务 | `reset-r1-r27-structural-audit-20261026`；只给中性任务、验收问题和绝对 primary artifact 路径 |
| job | `a7ecfa3facaf464bb362afd6e9273931`；2026-10-26 04:06:16Z 创建，04:06:20Z failed |
| 完成状态 | `REVIEW_UNAVAILABLE`；`threadId=null`、`response=null`；没有 reviewer report |
| receipt | exit code 1；CLI init 报 `claude-fable-5-1-reversed[1m]`；工具 Glob/Grep/Read |
| 最终 CLI event | subtype `success`，但 `is_error=true`；1188ms；`modelUsage={}`；synthetic assistant 内容为空 |
| 可核实边界 | init 的模型字符串只是 CLI 报告；后端模型、实际 effort 未核实；不能因 subtype 字面为 success 宣称审查成功 |
| 后续动作 | orchestrator 自动重试0；fallback false；没有改路由、替代 reviewer 或数学接受状态 |

原输入见[完整 trace payload](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/r1_r27_review_trace_payload_20261026.json>)，sanitized receipt 见[失败证据](<D:/科研/math agent/erdos-szekeres-sat-main/.aris/review-state/claude-review-deep/evidence/7a63bb611cfc468ab6baaeb58c293db9.json>)。trace 目录保留原始 request、start response、final status 和 receipt 全文；response Markdown 明确说明没有审查正文，不以本报告填充 reviewer 回复。
