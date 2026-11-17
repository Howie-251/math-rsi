# N(7,r,s)截至2026-11-06的结构综合、路线审计与下一步主攻

现有全模型工作上界为 $757/766/767/777=40/49/75/76$。$b=25$ 已在限定 signotope 域人工接受，并有独立 25 点见证；后继结构链仍是未独立验收的工作证明。最新 23 点 full-Hall 反例和物理横截核验改变了选线：C49 已关闭全部 $I=\varnothing$ 的 75 点层，因此旧 $I=\varnothing,r=3$ 等细分不再是 $75\to74$ 的必要缺口。

下一步主攻选择“实际全路径横截／短帽分划的传播桥”；独立竞争路线是“同一 777 母体的全部合法根 chart 相容性”；766／757 第二单位交叠作为次级通用工具线。本轮未取得新的 39、48、74 或 75 终界。

本文截至 2026-11-06，是综合与路线选择，未重跑历史科学计算。历史详细账见[证据账](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-structural-roadmap-20261105/evidence-ledger.md>)；[上一版综合](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-structural-roadmap-20261105/synthesis.md>)的选线须按本轮新诊断更新。$b=25$ 的限定域接受和见证分别见[正式接受记录](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md>)与[独立见证核验](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n756-professor-review-20261027/evidence/E21/verification.json>)。

本轮检索覆盖根目录历次 RESEARCH_SYNTHESIS／RESEARCH_REVIEW 入口、既有 Trellis 研究目录、reports 中截至 11/06 的 N7／N766 报告，以及相关 tmp 原回执。历史早期细节部分沿用 11/05 evidence-ledger 的索引，未逐份重放旧的全部证明／证书；不声称全仓每个文件都已逐行审计，也不声称穷尽外部查新。

## 一、对象与数值账

$N_{\rm sig}(7,r,s)$ 是完整有序 rank-3 signotope 中，同时无蓝 $r$、红 $s$ 和 weak 7 的**最大避免人口**，不是 forcing 阈值。每个四点 packet 至多一次变色；路径长度按顶点数计。weak 7 要求同一对实际首末点的两色路径长度和至少为 9。不同路径的内部允许共享；换诱导集或合法 chart 后，所有这些对象必须重算。

记 $a$ 为 747 有效界，$b$ 为 756 及换色后的共同有效界；$A,C,Q,F$ 分别为 757、766、767、777 的实际容量。已写出工作证明的关系是

$$
A\le a+b-1,\qquad C\le2b-1,\qquad Q\le3b,\qquad F=Q+1.
$$

代入 $a=16,b=25$，得到

$$
(A,C,Q,F)\le(40,49,75,76).
$$

$Q\le C+b$ **仍未证明**。若该桥成立，应当得到 $49+25=74$、$F\le75$；不能把它与现有 75／76 混称为同一条已证链。

现有 $Q\le75$ 来自独立的 $3b$ 工作定理；若新桥成立，可进一步收紧至 74。这里的区别是证明依赖和可传播程度，不是把 $\le75$ 本身判为算术错误。旧可响应式为

$$
Q\le\min\{3b,\ C+b+5,\ A+C-1\},
$$

目前代入为 $\min\{75,79,88\}=75$。单独得到 $C\le48$，仍只有 $\min\{75,78,87\}=75$；单独得到 $A\le39$ 也不降低 $Q$。

参数收益应写成条件传播：

$$
C\le2b-\delta,\quad Q\le C+b-\gamma
\quad\Longrightarrow\quad
Q\le3b-\delta-\gamma,\qquad
F\le3b-\delta-\gamma+1.
$$

这不是已经证明了新桥。现有 $Q75$ 的承重连接见[替锁与 75／76 工作界](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCK_REPLACEMENT_COMMON_ROOT_EXCLUSION_AND_7576_BOUND_20261103.md>)和[依赖审计](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7576_DEPENDENCY_AUDIT_AND_SINGLE_THROUGH_EXCLUSION_20261103.md>)。

## 二、历史按真实结构贡献组织

下表保留各阶段的工作账；各行不是逐轮正式接受。$b:29\to28\to26\to25$ 的输入变化与结构收益必须分账，不能双计。

| 阶段 | 当时的 757／766／767／777 工作上界 | 真实结构贡献或输入变化 |
|---|---|---|
| 初期 | 45／58／103／206 | 初期工作账 |
| R5 | 44／58／101／201 | 实际覆盖的严格交叠 |
| R6，$b=28$ | 43／56／98／195 | 输入变化与当时结构链 |
| R7 | 43／56／89／177 | H／R 不交分解与五横截 |
| R8，$b=26$ | 41／52／83／165 | 输入变化与当时结构链 |
| R20 | 41／52／83／84 | 合法 chart 的精确关系 $F=Q+1$ |
| R23，$b=25$ | 40／50／80／81 | 新 $b$ 输入经旧链传播 |
| 2026-10-29 | 40／50／79／80 | 三匹配 |
| 2026-10-31 | 40／50／78／79 | 前驱压缩 |
| 2026-11-02 | 40／50／77／78 | 锁区间 |
| 2026-11-03 | 40／50／76／77，再到 40／50／75／76 | 共同中间、补偿、替锁依次推进 |
| 2026-11-05 | 40／49／75／76 | 实际替末 → 双色交替环无环 → 全路径安全增广，得到 C49 |
| 2026-11-06 | 40／49／75／76 | 最新诊断，没有数值下降 |

R20 是一般对象操作，C49 也是一般 $p\ge4$ 的定理；两者是真正符合“先结构、后数值”的范例。R1—R27 的历史范围见[阶段审阅记录](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_REVIEW_R1_R27_20261026.md>)；R20 原件见[全局证明架构与共同实现](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>)。完整数值来源仍以[历史证据账](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-structural-roadmap-20261105/evidence-ledger.md>)为入口。

## 三、可复用结构资产与旧路线处置

| 资产 | 可复用内容、准确边界与处置 | 原始来源 |
|---|---|---|
| 1. R5／R6 | 全部实际短帽覆盖与严格一单位给出 A40。第二单位须控制同时出现多个新点的路径。 | [历史证据账](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-structural-roadmap-20261105/evidence-ledger.md>)、[R1—R27 记录](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_REVIEW_R1_R27_20261026.md>) |
| 2. R7／R20 | 实际 H／R、ambient 两端封闭、唯一锁／neutral，以及合法 chart 的 $F=Q+1$。不能运输任意不对称帽或任意内部 pivot。 | [R20 原件](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>) |
| 3. 10/28 最优覆盖／lex 交换 | 完整暴露路径族与共同成本已经是现有思想，不能重命名认领新机制。 | [最优交叠、交换与 cut 接口](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_OPTIMAL_OVERLAP_EXCHANGE_AND_CUT_INTERFACES_20261028.md>)、[历史证据账](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-structural-roadmap-20261105/evidence-ledger.md>) |
| 4. 10/29—11/03 | $M_0$、端口共同匹配、完整源末供给、替锁、精确实际点覆盖给出 Q75；正 $w$ 类至多 74。长依赖链未整链独立验收。 | [joint-through 与 cuts](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_JOINT_THROUGH_SATURATION_AND_ORDERED_CUTS_20261030.md>)、[替锁原件](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCK_REPLACEMENT_COMMON_ROOT_EXCLUSION_AND_7576_BOUND_20261103.md>)、[依赖审计](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7576_DEPENDENCY_AUDIT_AND_SINGLE_THROUGH_EXCLUSION_20261103.md>) |
| 5. 11/04 六份结构报告 | 低轮廓三满核、有序双极星全类、Hall 同步换核、短尾／纯 D 段、终端分离、单删障碍均有准确子类价值。其中 $I=\varnothing$ 的 75 点层现由 C49 统一关闭，不应继续以排全局 75 为由细化 $r=3$；对更低人口或其他命题的用途另计。 | [三满核](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-structural-theorems-20261104/research.md>)、[双极星](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-extremal-stars-and-run-exclusion-20261104/research.md>)、[Hall 换核](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-hall-stars-and-critical-exchange-20261104/research.md>)、[短尾与纯 D 段](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-shared-paths-and-safe-prefix-20261104/research.md>)、[终端分离](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-terminal-separation-20261104/research.md>)、[单删障碍](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-canonical-tail-and-deletion-barrier-20261104/research.md>) |
| 6. 11/05 net-augmentation | 直接 $M_0$、单侧／双侧全路径批量转移，以及 $m_L+m_R\le\delta_L+\delta_R+\varepsilon$；同一接收域的 $\varepsilon$ 只计一次。尚缺从任意临界母体提取全部输入的步骤。 | [PROOF](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-net-augmentation-20261105/PROOF.md>)、[NORMALIZATION](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-net-augmentation-20261105/NORMALIZATION.md>) |
| 7. global-path | 过大分离有序匹配排除在 $p=5$ 时上限 15；Hall 闭分量注入共同中性池在 $p=5$ 时至多 20；另有首对／末点矩形净收益条件。这些不是一般 $\tau$ 界。 | [RESEARCH](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-global-path-structure-20261105/RESEARCH.md>) |
| 8. 757／766-structure | 一般 fork，以及完整红 join 路径产品 $\tau=\min_i\tau_i,\ \nu=\min_i\nu_i$；实际 12 点 767 和 11 点 766 否定普适 $\tau\le2\nu$。旧 Ferrers／双色满匹配子类已被后来的一般 C49 证明覆盖。 | [PROOF](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-757-766-structure-20261105/PROOF.md>) |
| 9. n766-strict | 对 $p\ge4$，双短帽有效容量 $b$ 给出 $N_{\rm sig}(p+2,p+1,p+1)\le2b-1$。主证明不依赖 Through14／Joint17／Closure 或 UNSAT。24 点实际 balanced 双 through 反例否定普适“两色 through 不能同时含本色 $p$ 链”。30 点 neutral 解析等号例否定一般 strict-neutral 预算，不能借它收紧 $M_0$ owner 计费。 | [PROOF](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n766-strict-capacity-20261105/PROOF.md>)、[VERIFICATION](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n766-strict-capacity-20261105/VERIFICATION.md>) |
| 10. critical-cover 与 nested | 二根全路径释放；49 点层中，canonical free 域大小为 1 时至少 9 个 sink 根、free 域为空且两侧人口为 25／24 时至少 10 个 sink 的类已排；这里的 free 域与 767 的 ambient $I=S\cap T$ 不同。另有纯 packet 嵌套；outer-short 四环在一般 $p\ge6$ 有解析证明，$p=5$ 用 1…15 active-prefix checked UNSAT 加任意反例至多 15 点的覆盖归约；757 递增梯形整类。相应少根分支、multiple roots，以及 single-short-cycle 递增 $k\ge3$ 仍未闭，不能得到 C48。fusion 的 600 秒外部终止未决。 | [critical-cover](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-critical-cover-continuation-20261105/PROOF.md>)、[nested PROOF](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-nested-path-and-active-core-20261105/PROOF.md>)、[nested VERIFICATION](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-nested-path-and-active-core-20261105/VERIFICATION.md>)、[outer-short 证书](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_outer_short_upto15_certificate_20261105/VERIFICATION.md>) |
| 11. common-private | 完整 source／shared-H 贪心反例；须区分已 Linux 核验的旧 15 点与未执行的新解析族。source-only 横截、单色 position $\le2n$ 均失败。这不是实际内部点短帽横截失败。 | [PROOF](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-common-private-family-and-cover-obstructions-20261105/PROOF.md>)、[APPENDIX](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-common-private-family-and-cover-obstructions-20261105/APPENDIX.md>) |
| 12. clique-source，截至 11/06 | 23 点完整 757／766 模型：全部 R6 源为红六 $F$，端点图有饱和六匹配；全部 92 条 R6 独立重建，唯一最小物理横截为 $\{0,14,18\}$，$\tau=3$。它否定通用 full-Hall 排除，不否定 $\tau\le5$ 局部目标或 31 点 caller。fixed24 checked UNSAT 只排固定 23 点色表加指定插入／private 路径域。physical31 首片 600 秒外部 TERM、exit $-15$、无 solver 状态，没有 SAT／UNSAT 或成功 checker。31 点 caller 仅覆盖 757 临界 40 点中 $\lvert S\rvert=15$ 且 $S$ 含红六的分支；$\lvert S\rvert=16$ 时只留 30 点，六换五不足；其他分支仍开。$q=6$ 时，$q$ 条匹配路径的并至多 $q^2=36$ 点；这不能迁移成一般无短帽分划的有限核定理。 | [PROOF](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-clique-source-hall-20261105/PROOF.md>)、[VERIFICATION](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-clique-source-hall-20261105/VERIFICATION.md>)、[NEXT_SESSION](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-clique-source-hall-20261105/NEXT_SESSION.md>)、[transversal](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_hall_counterexample_transversal_20261106/transversal.json>)、[enumeration](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_hall_counterexample_transversal_20261106/enumeration.json>)、[replay receipt](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_hall_counterexample_transversal_20261106/replay_receipt.json>)、[physical31 RESULT](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_physical_cover31_20261106/solve_slice01_evidence/solve_slice01_cuts000/RESULT.json>) |

## 四、主会话结构审核

当前存在显著的局部优化趋势，但不能说整个方法已走死：$Q:80\to75$、$C:50\to49$ 是真实的工作证明进步。需要停止的是没有接回原临界域与活跃传播式的细化。

具体问题有七类。第一，端点投影丢失实际内部共享，full-Hall 反例已经直接证实。第二，单条 private 族无法控制同时释放多个点后的完整暴露族。第三，把“极大／贪心不可再加”误当成最大容量。第四，反复细化已被 $I=\varnothing$ 定理覆盖的域。第五，不查看活跃传播式，导致 C／A 的下降无法影响 Q。第六，改名复推旧加权 through 与相同的净收益恒等式。第七，固定小 CNF 排除没有接入全类。

这里有直接的局部贪心／不完整 oracle 反例，而非仅是类比。[10/28 原件 §5–6、§9](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_OPTIMAL_OVERLAP_EXCHANGE_AND_CUT_INTERFACES_20261028.md>)给出已在 Linux 固定验证的 12 点实际例：原四点横截 $T$ 不能通过释放至多两点取得严格收益，但整体四换二可从 used 4 降至 2；两换二可以走平台，所以不能称所有有界交换均失败。另一个 6 点实际例中，命中全部单点 private 族仍漏掉同时被两个释放点命中的第三条红五。它们不是接近 49／75 的极值实例，也不反驳全局最优覆盖命题。

不能仅按标签、日志、文档数量或 UNSAT 次数评估进展。必须保留 packet 与同端 weak；抽象任意超图的弱多边形已有公开反例，不能用更宽对象的结论代换本项目。

## 五、主攻 P1：混合短帽分划／物理横截传播桥

### 一般命题与完整标签目标

对一般 $p\ge4$，定义

$$
b_p=N_{\rm sig}(p+2,p,p+1),\qquad
c_p=N_{\rm sig}(p+2,p+1,p+1),\qquad
q_p=N_{\rm sig}(p+2,p+1,p+2).
$$

目标是

$$
q_p\le c_p+b_p.
$$

现有 $Q\le3b$ 只在七边形工作链中使用，不擅自推广到所有 $p$。

对任意目标 $X$，显式要求 $X$ 禁蓝 $(p+1)$、红 $(p+2)$ 和 weak $(p+2)$。寻找实际集合 $K$，满足：

1. $K$ 命中全部实际红 $(p+1)$ 路径；
2. $X[K]$ 无红 $(p+1)$、无蓝 $p$。

于是 $X\setminus K$ 是 balanced，$K$ 是短帽，立即得到

$$
|X|\le c_p+b_p.
$$

这是一个明确的充分结构命题，强于单纯数值不等式，目前未证。允许 $K$ 包含路径内部点；不把 $K$ 限在源集，也不要求端点图无匹配。

已知 23 点例的 $K=\{0,14,18\}$ 本身不足 5／6 点，确实满足短帽条件，所以该例反驳 Hall 快捷路，却不反驳 P1。若未来找到真实母体不存在上述顶点标签，它只否定这个充分分划命题，不自动否定数值 $Q\le C+b$；届时应转向临界层 $\tau\le25$ 或另一条净计数定理。一般分划存在性不能默认缩到 $q^2$ 核，该量词问题的有限覆盖尚无定理。

它可以精确改写成顶点标签 $x_v\in\{0,1\}$：每条实际红 $(p+1)$ 路径 $P$ 满足

$$
1\le\sum_{v\in P}x_v\le p,
$$

每条实际蓝 $p$ 路径 $Q$ 满足

$$
\sum_{v\in Q}x_v\le p-1.
$$

取 $K=\{v:x_v=1\}$。前一个约束保证两侧均无长红，后一个约束保证 $K$ 无短蓝；反向也成立。这个等价式只是把完整结构目标说明白，不宣称已解决标签存在性，也不把旧横截目标认领为新定理。它展示必须保留真实路径超图，而非仅保留端点边。量词是 $\forall X\,\exists$ 标签；检查一个标签或若干路径不能构成证明。

### 从最大 balanced 域到两级交换目标

主实施数学对象应先选**最大人口**的 balanced 诱导域 $H$。其补集 $K=X\setminus H$ 是最小红 $(p+1)$ 物理横截；每个 $k\in K$ 必有 private 长红路径 $P_k$，满足 $P_k\cap K=\{k\}$。

不能止于单条 private 路径。对任意 $I\subseteq K,\ J\subseteq H$，须检查完整的新路径：若

$$
(H\setminus J)\cup I
$$

仍 balanced 且 $|I|>|J|$，便反驳 $H$ 的最大性。贪心只给 inclusion-maximal 的 $H$，不能替代 maximum。最小横截中出现坏红 $(p+1)$／蓝 $p$ 时，应研究全部暴露族并保持共用 $H$；本文未证明坏型一定可增广。

从每个坏 minimum transversal 强行取得严格人口增广，是比“存在某个混合分划”更强的充分命题，不能预设。更合适的可选路线是两级优化：先最大化 $|H|$，再在这些 $H$ 中最小化

$$
\Phi(K)=K\text{ 中实际红 }(p+1)\text{ 路径与蓝 }p\text{ 路径的总数}.
$$

若 $\Phi(K)>0$，待证存在保持 $H'$ balanced 的交换，使 $|H'|>|H|$，或使 $|H'|=|H|$ 且 $\Phi(K')<\Phi(K)$。这是具体但尚未证明的交换目标；其存在性才是创新义务，最优性和势函数本身不给新界。允许平台等成本操作，避免再次要求每步严格人口收益。

“有最大 $H$ 的短帽补集”仍强于任意混合分划存在；若这一加强被反例击穿，不能否定较弱目标。这里没有声称每个 minimum transversal 都必定是短帽。

### 可以先完成的临界里程碑

第一里程碑可以更弱：只对 75 点临界 $X$ 证明

$$
\tau_{R6}(X)\le25.
$$

结合 C49，删去至多 25 点后仍有至少 50 点 balanced，产生矛盾，从而得到 $Q\le74,\ F\le75$。全参数响应桥另证，不能把临界排除冒称为普适分划。

已有安全补入接口为

$$
|X|\le C+b-m+h,
$$

其中 $h$ 是全剩余路径的物理 hit 成本。现在 $C=49,b=25$，所以 $m-h\ge0$ 已足以给出 74，$m-h\ge1$ 给出 73；旧 C50 时要求正一单位的调度应更新。这并不意味着无需证明 $m-h$。相关全路径转移与同一接收域的计费见[net-augmentation](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-net-augmentation-20261105/PROOF.md>)和[规范化接口](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-net-augmentation-20261105/NORMALIZATION.md>)。

### 本轮直接核对的临界必要条件

令 $S,T$ 分别为 ambient 全部 R6 的源、末点，令

$$
D=X\setminus(S\cup T),\qquad I=S\cap T,\qquad
w=|\operatorname{Src}_{R5}(D)\cap\operatorname{End}_{R5}(D)|.
$$

在 $|X|=75$ 时，任何红六横截 $K$ 都满足

$$
|K|\ge75-C\ge26,
$$

因为补集 balanced。特别地，$|S|,|T|\ge26$。

$S$ 无 B5：若 $S$ 内有 B5，取其末点的 ambient 出 R6；桥为红便给出 R7，桥为蓝便给出 B6。$T$ 由反序同理。于是 $b=25$ 迫使 $S$ 和 $T$ 内部各有 R6；它们分别的末点、首点落在 $I$ 中，所以 $I\ne\varnothing$。旧正 $w$ 排除再给出 $w=0$。

因此任何主攻反例都必须面对

$$
|X|=75,\qquad I\ne\varnothing,\qquad w=0,\qquad
\tau_{R6}(X)\ge26,
$$

以及 $S,T$ 内部同时强迫长红。这个必要条件包是已有容量的直接后果，不是新上界；不能用小稀疏反例充当临界反例。

## 六、独立竞争 P2：同一 777 母体的合法根 chart 共同结构

设 $Y$ 是 76 点 777 候选，遍历全部合法蓝根 $r$，每次删根并重新计算

$$
X_r,\ S_r,\ T_r,\ D_r,\ I_r,\ w_r.
$$

只需证明至少一个合法根满足

$$
I_r=\varnothing\quad\text{或}\quad w_r>0,
$$

就与现有两类至多 74 的结论矛盾，因为每个 $X_r$ 应有 75 点。这样得到 $F\le75$，再配合 $F=Q+1$ 得 $Q\le74$。更强的混合证书也可代替这两个判据。新充分目标比只找 $w_r>0$ 更宽，因为已经纳入 C49 给出的 $I_r=\varnothing$ 类。

关键是证明所有合法 charts 不可能同时具有 $I_r\ne\varnothing,w_r=0$。不能把多个 chart 的人口预算相加，不能任取非法 pivot，也不能保留旧 chart 的角色。第一动作应写清相邻合法 chart 上实际路径、源末与缺额如何运输，寻找可证明的循环总量或势函数。

[根循环原件 §3.6、式 (22)–(24)](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_JOINT_THROUGH_SATURATION_AND_ORDERED_CUTS_20261030.md>)的工作定理给出 $3\le$ 合法蓝根数 $\le6$，且全部合法根构成单一合法循环。因此 P2 只需分析 3–6 个彼此相容的合法 charts，而非所有任意 pivot。

该相容性目前未证。小例全 $w=0$ 只反驳没有近饱和前提的版本。此线有独立表示价值，但预计比 P1 更不确定，不给虚构成功概率。合法运输的现有范围以[R20 原件](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>)为准。

## 七、次级 P3：统一第二交叠，优先形成一般交换定理

对 balanced 的实际覆盖 $U\cup V=X$，要求 $U$ 无蓝 $p$、$V$ 无红 $p$，定义 $\Omega$ 为最大交叠。恒有

$$
|X|+\Omega\le2b.
$$

已有 $\Omega\ge1$ 是 C49 的来源。目标是在 $|X|=2b-1$ 层证明 $\Omega\ge2$，得到

$$
C\le2b-2;
$$

$p=5$ 时即 48。757 对应 747／756 覆盖的第二交叠则给出

$$
A\le a+b-2=39.
$$

已经闭合的多 sink、四环、递增梯形是工具；下一有效定理必须同时处理完整多点暴露、multiple roots 与 zero-free／one-free，不能把 single-root 的一个局部闭合当成全局 48。第一动作是检查现有 short-cycle 归约是否确实覆盖上述全部残域；只有全域归约成立，才值得主攻 fusion。已有工具与残差见[critical-cover](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-critical-cover-continuation-20261105/PROOF.md>)和[nested-path](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-nested-path-and-active-core-20261105/PROOF.md>)。

独立的 C48／A39 不降低 Q75。桥成立后，C48 可传为 Q73／F74；所以本线是桥的配套，或独立的 A／C 成果，不抢占终界主线。

## 八、执行顺序与止损

先压缩并核清 C49、Q75 和 $F=Q+1$ 的承重接口，不重跑已 accepted 的 $b=25$。主数学以 P1 为首，P2 保持不同机制的竞争，P3 限于能产出一般交换定理的工作。31 点 private／full-Hall 只作为 757 一个明确分支的局部探针，不能当作整题主线。

在原限定模型范围内，$b=N_{\rm sig}(7,5,6)=25$ 已由上界接受和实际 25 点见证双向支持。因此继续尝试普适 $b\le24$ 不是可行的后继突破方向。如果利用某个 25 点核在共同母体中的额外条件，必须写成条件缺额或共同相容性结论，不能否定独立的 25 点构造。

有限计算之前，先冻结一般命题、实际输入覆盖，以及正反输出分别起什么作用。如需 SAT，只在 Linux 按新输入绑定受控运行；本轮不启动。每轮合格产出应为下列之一：

- 普适递推；
- 包含原临界域的严格整类排除；
- 完整合法增广；
- 迫使改变路线的真实反例。

连续两轮只添加必要标签，或扩大相同失败模型却没有改变 caller，就停止该细化。不能以扩大算力代替尚未建立的核覆盖。成果按“覆盖哪个原输入类、证明多少净收益、传给哪条活跃上界”验收。

## 九、外部来源与保证

本轮作的是定向文献核查，不称穷尽查新。

| 来源 | 本轮核对与可调用范围 |
|---|---|
| [Baek，arXiv:2206.04260v2，Theorem 2.7](https://arxiv.org/html/2206.04260v2) | 17 点 forcing 对应 747 人口至多 16。原文的一般有序三元染色也覆盖本项目子类。 |
| [Baek–Balko，SoCG 2025，Theorem 7 与 §3](https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/html/LIPIcs.SoCG.2025.13/LIPIcs.SoCG.2025.13.html) | weak 7 反例在任意有序三元染色域；§3 仍将 signotope 列作可能成立的更强假设，不能搬来反驳本项目。split 只共享一端，不能替代 weak 的双端要求。 |
| [Bergold–Felsner–Scheucher，SoCG 2023](https://drops.dagstuhl.de/storage/00lipics/lipics-vol258-socg2023/LIPIcs.SoCG.2023.17/LIPIcs.SoCG.2023.17.pdf) | 点对偏序是已有 $M_0$ 进口；扩张定理本身不保证保留本题全部帽与 weak。 |
| [Schroeder companion](https://michaelschroeder.ai/research/ErdosSzekeres/companion) | 仍是 2026-09-19 v1 作者报告的 ES7 至多 81、几何 756 等于 25；无 external peer review，并自述 native-evaluation 信任边界。本轮没有重建，不能替本项目 signotope 49 验收。 |
| [Damásdi–Dong–Scheucher–Zeng，saturation，arXiv:2312.01223](https://arxiv.org/abs/2312.01223) | 原文 v3 说明几何饱和与极值不同：$n=7$ 有 28 点不可几何单加的饱和构造，因此“不能再添点”一般不等于最大人口。本例只是方法学提醒，不作为本题混合分划的反例或进口。 |

### 独立审阅的实际状态

本次新任务为 n7-structure-synthesis-20261106，请求 deep／max，job 为 f6b45648250b4f178e589709ec4782ca。2026-11-06 新加坡时间 10:26:02 启动、10:26:09 以失败终止，真实状态为 **failed／incomplete／unaccepted**，没有数学意见。原始溯源见[trace README](<D:/科研/math agent/erdos-szekeres-sat-main/.aris/traces/research-review/2026-11-06_n7-structure-synthesis/README.md>)与[分层状态记录](<D:/科研/math agent/erdos-szekeres-sat-main/.aris/traces/research-review/2026-11-06_n7-structure-synthesis/status.json>)。

请求的 semantic 模型为 claude-fable-5-1、wire 模型为 claude-fable-5-1-reversed、工具为 Read,Grep,Glob。CLI 初始化报告模型字面 claude-fable-5-1-reversed[1m]；assistant 模型为 unrecognized，内容为空；工具调用为 0。CLI 以 exit code 1 结束，分类 cli_nonzero_exit。后端模型与 effort 不可验证；没有 verdict，accepted=false。请求配置不能替代已报告的后端证据。本轮未重试或 fallback。

主会话核读与新的直接推导不冒充独立审核。报告没有改变旧接受、jobs、CNFs／proofs、task 状态、wiki 或 Goal。工作流问题只记录为：审核通道再次不可用，影响独立验收；维护需要单独授权，本轮不修改核心或验收规则。

本轮交付是综合、准确残差、结构命题和排序；原上界突破尚未完成。
