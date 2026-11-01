# 从 m(5) 积累到一般 k：数学工具与研究经验

## 当前：全部k≥12、同一增长公式且Δ≥2

2026-10-21，新解析证明与端到端Lean均已将原17起点延伸至全部k≥12。新[claim](claims/propertyb-general-growth-k12.md)保持同一RS全域最大预算与floor公式，证明Δ≥2及任意原始有限简单超图的两色结论；旧17起点claim及其审阅不改写。新证明见[ANALYTIC_EXTENSION](../context/propertyb-general/bridge-12-16-20261021/ANALYTIC_EXTENSION.md)，fresh[7单位／37义务审计](../context/propertyb-general/bridge-12-16-20261021/PROOF_AUDIT.md)为PASS_WITH_DECLARED_IMPORTS、same-family/provisional。实际Lean [Twelve](../formal/Aris4Math/General/Growth/Twelve.lean)指定构建及[独立原题导入](../formal/ReviewAuditGeneralGrowth12.lean)均exit0，传递公理仅标准三项；[证据](../context/propertyb-general/bridge-12-16-20261021/lean/VERIFICATION.json)来自主执行者本机记录。

本次可复用改进是重证真正需要的常数界：以k⁴≤9·2ᵏ和√M≥64替代旧17起点的更强估计，使相同真实结构调用闭合；有限12…16的精确有理种子仅用于参数不等式，未枚举超图。五项明确包络也在k≥12等于B_RS+1，但D仍纸面、E仍≥256纸面，均未Lean。新Grok最终审阅已有效end_turn（grok-4.7-build/xhigh），全文静态读取新源码／原题／日志，认可且无实质问题，未执行Lean、未重审旧核心全部证明体，见[本次处置](../context/propertyb-general/bridge-12-16-20261021/REVIEW_DISPOSITION.md)；本次不调用Gemini，旧17双模型仅作历史。旧35Lean／36研究继续暂停，无新Goal。以下17／32起点及旧展示数为历史。

## 当前：一般增长主定理C已完成端到端Lean

2026-10-21，全部整数k≥17的同一增长下界已完成形式化，不再只限RS核心或17元试点。最大预算对全部正整数的最大性、同一个严格参数见证、最小反例结构、统一整数增益和任意原始有限超图的Bool染色均在内部闭合。指定主构建与独立展开原题审计exit0，七项传递公理只有标准三项。证据：[完整报告](../context/propertyb-general-lean-growth/REPORT.md)、[实际核验记录](../context/propertyb-general-lean-growth/VERIFICATION.json)、[原题复述](../formal/ReviewAuditGeneralGrowth.lean)。最终跨家族审阅状态统一见报告；比较D/E仍为纸面证明。

本轮可复用的效率经验是先构建“任意原输入→结构判据→原结论”的真实调用，再消去数值前提。为最终结论寻找足够的中间界：公共点二分已经足够，无需为可省略的Gram加强增加形式化成本；只需自然数k时，用从16起的归纳证明k⁴≤2ᵏ，不强行翻译更强实变量导数论证。边界明确的模块交由Sol并行，root统一接口、正规构建和原题审计。每项简化保持最终命题不变，完整实际输入连接照常验收。

## 历史：一般RS核心Lean验证的启动准备

**2026-10-21：一般Lean阶段Goal准备就绪，尚未启动。** 旧一般纸面Goal已complete。本阶段拟验证一般RS真实概率核心，并完成任意有限简单17元超图、边数≤2^17的实际caller；完成后再决定完整一般定理形式化。由用户另行启动；本轮仅准备导航。旧35/36暂停，v2隔离。

入口：[阶段Goal](../GOAL_PROPERTYB_GENERAL_LEAN_PILOT.md) · [启动文本](../START_GOAL_PROPERTYB_GENERAL_LEAN_PILOT.txt) · [准备资料](../context/propertyb-general-lean-pilot/PREPARATION.md)。

## 2026-10-21 round02 当前：一般定理与指定终审已完成

对全部整数k≥17，已证明

$$
m(k)\ge B_{\rm RS}(k)+1+\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)}\right\rfloor.
$$

[主claim](claims/propertyb-general-growing-integer-gain.md)已按proof-checker登记verified（纸面证明，无新Lean）；[合并审计](../context/propertyb-general/round02/formal-audit/COMBINED_AUDIT.md)为PASS，核心与比较的Grok/Gemini指定终审均完成，见[CORE_DISPOSITION](../context/propertyb-general/round02/reviews/CORE_DISPOSITION.md)、[BASELINE_DISPOSITION](../context/propertyb-general/round02/reviews/BASELINE_DISPOSITION.md)。明确五项L_ref在k≥32等于B_RS+1；Goal完整比较尾K={k≥256}另包含指定零锁必要数据松弛对每个M>B_RS不通过，绝非全部潜在Grill方法或实际H witness。Grok比较按原生completed终稿记录，原MCP envelope缺失事实保留。

已复用的方法链是：保留同一实际超图与共同坏对对象，经最小顶点商约化接到真实单交图；以公共点／无公共点的经典线性交族团界削减γ，再把同一个严格RS参数见证转为统一增长的整数预算。这是覆盖全部原始对象域的解析证明，不是样例归纳。

研究的数学与规定审阅已闭合，最终展示／交付已完成，Goal工具已实际返回status=complete。恢复[PROGRESS](../context/propertyb-general/PROGRESS.md)，阅读[离线单卷](../PROPERTY_B_GENERAL_BOUND.html)，人工交接[HANDOFF](../HANDOFF_PROPERTYB_GENERAL.md)。旧36与35Lean继续暂停，不碰v2。

2026-10-21：数学、指定终审、离线HTML和人工交接均已完成交付；Goal工具已实际返回status=complete。最终验收入口为context/propertyb-general/round02/COMPLETION_AUDIT.md；最终HTML含532条内嵌公式，离线桌面／手机检查PASS，已用Microsoft Edge打开。旧36与35Lean暂停、v2隔离保持原状。

## 较早方向与推进快照（历史，以下候选／在途描述不覆盖当前状态）

## 2026-10-21 round02：已有完整统一候选，正在审计

新Goal已active。最小顶点反例约化、实际RS重染事件和有向单交计数已经接成完整纸面稿；单交团的公共点二分把统一团上界进一步压到约平方根边数。当前候选对全部整数 $k\ge17$ 给出

$$
m(k)\ge B_{\rm RS}(k)+1+\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)}\right\rfloor,
$$

其中 $B_{\rm RS}$ 是明确RS–FKG–精确积分判据的最大整数可染预算，已证明非空有限。完整规范在 [核心定理](../proofs/propertyb-general/CORE_THEOREM.md)、[整数预算](../proofs/propertyb-general/UNIFORM_INTEGER_GAIN.md)及[团界加强](../proofs/propertyb-general/CLIQUE_REFINEMENT.md)。该团界属于经典线性交族/Deza型事实，正文自含证明，不主张首创。

核心三源已过正式proof-checker全文审计与Grok/Gemini有效核心审阅，已登记[统一整数增益定理](claims/propertyb-general-growing-integer-gain.md)，无新Lean。新增完整比较源`BASELINE_COMPARISON.md`及正式合并审计证明：五项明确参考包络在 $k\ge32$ 等于 $B_{\rm RS}+1$；在 $k\ge256$，所列零锁必要数据松弛方案不能接受任何更大预算。比较跨家族终审与最终交付仍在途，必要数据松弛和真实超图分开，不预记整个Goal完成。当前状态和全部实际剩余在 [PROGRESS](../context/propertyb-general/PROGRESS.md)。下文保存方向形成时的库存综合。

2026-10-21。本文把现有成果按证明用途重新组织，供一般下界讨论复用。系统库存已覆盖 L1–L117，而不只是早期12组；逐组范围见[完整数学库存](../context/general-method-discussion-20261021/GENERAL_LEMMA_INVENTORY.md)，失败边界见[12项经验综合](../context/general-method-discussion-20261021/GENERAL_FAILURE_AND_EFFICIENCY.md)。

详细待启动文本：[GOAL_PROPERTYB_GENERAL_BOUND.md](../GOAL_PROPERTYB_GENERAL_BOUND.md)。已固定研究范围、分工和验收方法，尚未启动新Goal；旧36及35Lean继续暂停。

## 我们已有怎样的基础

已有一条可以参数化的证明主链：从任意超图约化到点对覆盖输入，用度数预算选择局部结构，再对同一实际超图进行条件排列计数或染色修复。后续研究积累的价值，主要是让不同位置、布局和修复操作共用原边信息，排除“各处同时最坏”的虚假情形。

当前成果的依据分开保存：

|材料|当前可用结论|
|---|---|
|m(5)≥33、≥34|完整自然语言证明与端到端Lean；可直接复用已验定理和接口|
|m(5)≥35|完整自然语言候选；完整Lean未完成，继续保持暂停|
|m(5)≥36研究|全题未证明；已保存完整分支、一般条件引理、反例与失败边界，研究Goal暂停|
|合作者 k=6,…,11 材料|给出65、130、266、542、1112、2275六个下界及局部证书；旧记录已重放103190型。本轮阅读不升级其证明验收状态|

合作者材料的准确范围、通用定理及归属见[小 k 提取报告](../context/general-method-discussion-20261021/SMALL_K_EXTRACTION.md)。有限多个新值提供方法检验，不自动推出一条一般 k 的新下界。

用户选择的目标是：寻找明确的整数范围 \(K\subseteq\{2,3,\ldots\}\) 和阈值 \(B(k)\)，使

\[
\forall k\in K,\ \forall H\text{ 有限简单 }k\text{ 元超图},\quad
|E(H)|\le B(k)\Longrightarrow H\text{ 可二染色}.
\]

这样得到 \(m(k)\ge B(k)+1\)。可以限制 \(k\)，顶点数、度数或交叠条件则必须在证明内部全部处理。具体 \(K,B(k)\) 尚未确定；本次整理没有启动新Goal。

## 一、已经接近可直接使用的一般骨架

**商约化、度数预算和贪心失败覆盖。** 对 \(k\ge2\)，L1–L3的一般数学内容无需五元假设。最小顶点反例覆盖每个点对，因而

\[
\sum_x d(x)=kM,\qquad
\sum_{y\ne x}(\lambda_{xy}-1)=(k-1)d(x)-(v-1),
\qquad
v\left\lceil\frac{v-1}{k-1}\right\rceil\le kM.
\]

随机贪心失败必有两条实际边只交于一点，并在排列中首尾相接。L3的失败覆盖及无放回联合计数已有一般Lean；完整超图调用和其余结构模块仍有五元接口。

合作者的通用选锁判据也已经写成证明。对整数 \(D\ge\lceil(v-1)/(k-1)\rceil\)，置

\[
Z=(D+1)v-kM,\qquad T=(k-1)(D+1)-v+2.
\]

给定整数 \(s\ge2\)，当 \(Z>0\) 且 \(4(k-1)Z>(s-1)T^2\)，可保证 \(s\) 个度数至多 \(D\)、两两共度恰一的点。它把总度预算、冲突图独立集和Cauchy不等式合在一起，能替代一部分逐度谱选点。来源为[小 k 迁移页](PROPERTY_B_SMALL_K_TRANSFER.md)与合作者定理B。

这一骨架的接口问题已经明确：必须同时检查**能保证选出的结构**是否足以让后续概率界严格。单独增大锁数菜单或精化算术，都不能弥补选点存在性。

## 二、最值得保留的统一加强：共享同一批实际数据

### 共同坏对与多布局

L7的有限弱对偶对一般有限指标成立。真实坏对数量向量 \(z\) 满足 \(0\le z\le c\)、\(Az\ge q\)，则对非负乘子 \(\delta\)，

\[
w\cdot z\ge \delta\cdot q
-\sum_s c_s\max\{0,(\delta A)_s-w_s\}.
\]

这条代数引理已在有理数上Lean验证。L8允许不同布局共用同一个 \(z\)；若若干合法布局的上界经凸组合小于一，至少一个布局成功。各布局可有不同概率空间，无需假设独立。

它的作用很具体：同一批坏对不能在每个布局中都自由换到最便宜的槽里。L4的迹恢复、投影和重标号负责保持共同对象，L10的删点守恒进一步排除所有视图同时取坏值。L16、L36及后续多视图连接扩充了同一机制。

一般弱对偶已经可用；返回Property B的现有Lean调用仍是五元。推广时要补真实 \(H\) 到 \(z,c,A,q,w\) 的语义，而不必重证整套代数。源码入口见[库存L4、L7–L10](../context/general-method-discussion-20261021/GENERAL_LEMMA_INVENTORY.md)。

### 真实关联矩阵，而非任意抽象交叠图

L83、L88、L95及后续加强保留了局部参数表容易丢掉的可实现性。

例如，取任意一批实际原边，其关联矩阵为 \(A\)，底集大小为 \(v\ge2\)，每行恰有 \(k\) 个一。则

\[
C=A\left(I_v-\frac1vJ_v\right)A^\mathsf T
=AA^\mathsf T-\frac{k^2}{v}J
\]

半正定且秩至多 \(v-1\)，从而
\[
(\operatorname{tr}C)^2\le(v-1)\operatorname{tr}(C^2).
\]

证明只用常量方向的正交投影及特征值Cauchy不等式。关键是它对**每一个实际原边子族**都成立；可以约束交叠总量、最高度前缀和共同邻居容量。现有五元研究已用真实主矩阵排除保存的抽象图松弛。

L95还有一般 \(k\ge4\) 的双计数：令 \(Q\) 连接交恰有 \(k-1\) 点的原边，\(\lambda_P\) 为点对共度，则

\[
\binom{k-2}{2}\sum_F\binom{d_Q(F)}2
\le3\sum_P\binom{\lambda_P}3.
\]

一组三条原边的三种中心共用同一份点对计数，因此系数三不能随意删去。这些是可直接引用的必要结构约束；仍须与失败概率或修复结论接合。来源：[主矩阵推导](../context/propertyb35-paper/round01/middle/a1_incidence_rank_subset_20261020/DERIVATION.md)、[一般wedge证明](../context/propertyb35-paper/round01/middle/high_intersection_wedges_codegree_excess_20261020/LEMMA.md)。

## 三、从“选一个好初态”到“完成修复”

**一般源态选择已经有实质内容。** L68、L74把低度点族的边迹矩与唯一单色边事件相连。设反例 \(H\) 有 \(M\) 条边，随机染色中各边单色概率相同，均为 \(p\)。对指定的 \(L\) 条原边，

\[
\Pr(\text{恰一条单色边，且属于指定族})
\ge 2-(2M-L)p.
\]

这是对每份染色的单色边数逐态计数所得，不要求坏事件独立。加权版本能让**同一份初态**的坏边同时包含若干指定点，避免把分别取得的好性质拼成并不存在的初态。完整一般证明在[边迹矩与唯一坏边选择](../proofs/propertyb35/UNIQUE_BAD_EDGE_FAMILY_MOMENTS.md)。

**随机横截集给出一般修复语言。** L23从每个正约束集独立抽一点，取所抽点的并；若点 \(x\) 的命中概率为 \(q_x\)，则负约束集 \(F\) 被全部命中的概率至多 \(\prod_{x\in F}q_x\)。因此

\[
\sum_{F\in\mathcal N}\prod_{x\in F}q_x<1
\]

便保证存在满足全部正负约束的修复。它允许非均匀抽样，完整纸面证明见[随机横截修复](../proofs/propertyb35/RANDOM_TRANSVERSAL_REPAIR.md)。

L37再把多个负事件共用的点容量换算成正关联费用；L63、L75及owner计数追踪换色时同一原边的角色变化。这些比固定的“几个四集、度数七”数值门更适合提炼参数化结论。但当前L37的负集大小仍固定为三、四，owner紧面常数也有五元专用部分。

这里最应保留的失败经验是：好初态不等于可修复；一次换色可能生成新的私有边，必须计入。原边同时承担正负约束时，约束出现次数可能超过原度数，不能省掉重复角色。这是一般化需要补的实际连接。

## 四、怎样利用这些积累，而不再次陷入局部扩表

1. **先找完整区间的共同不等式。** 对候选 \(B(k)\)，由约化给出全部可能的 \(v\)，再用能覆盖整段 \(v\) 的选点与概率／修复估计。已有小 k 结果用于检查紧端点、符号和量级。
2. **保留实际耦合，优先加强正在决定上界的项。** 若总界是 \(\sum_h\min(A_h,B_h,C_h-D_h)\)，只提高非活跃项的扣除可能没有任何收益。共同矩、共享坏对或真实容量，必须在活跃项上产生可证明的下降。
3. **用失败见证确定该改哪一层。** 抽象signed系统的反例、抽象图松弛和一张证书不严格各自有不同含义；先判断是选点不足、真实约束被丢失，还是估计过松，再决定是否重算。
4. **以统一覆盖的变化衡量进展。** 成功处理更多局部行，不一定减少全题剩余义务。批量算术交给Sol和确定性程序；主代理负责参数范围、实际对象连接和跨家族意见的核算。

解析证明可以保留明确的有限求和、组合系数及少量端点核验。关键是它们由一个统一论证控制，而不是把逐参数未证明的程序结果直接列为定理假设；不额外要求最终式必须是初等闭式。

## 与 Cherkashin–Kozik 的关系和当前结论

[Cherkashin–Kozik原文](https://arxiv.org/abs/1310.1368)提供简洁的一般贪心分析；[Grill–Linzmayer](https://arxiv.org/html/2403.05674v3)已经使用离散排列与逐位置取最小值改进有限参数。我们应从这些已知机制及自己的共同数据工具继续推进，不能把离散化本身当作新贡献。

本次梳理的判断是：**已有积累足以支撑一次有明确数学接口的一般 k 研究，而且潜力不限于旧三锁模板。** 目前还没有给出一个新的 \(K,B(k)\)，也没有证明这些加强在全部必要输入上留下严格增益。缺的是这一层统一比较与覆盖，而不是重新从零建立每个基础引理。

Grok与Gemini讨论了目标、旧证书边界及部分共同数据工具；117组全库存的整理由Sol分工、主代理抽核关键来源完成，不能称两位外部模型逐条审阅了117组。实际范围、纠正及原回应见[讨论记录](../context/general-method-discussion-20261021/DISCUSSION_REPORT.md)。旧36研究与35 Lean均保持暂停。
