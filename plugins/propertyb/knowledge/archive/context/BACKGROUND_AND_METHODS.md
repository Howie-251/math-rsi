# 背景材料与随机贪心方法

本文整理已阅读的背景讲稿、旁支问题综述，以及随机贪心和 Catalan 算术的原始文献。当前研究目标是排除 32 条边的非二染色 5-一致超图，尝试证明 \(m(5)\ge33\)。这里记录的方法、来源和阅读结论为这一目标提供上下文；不构成该目标已经完成的声明。

页码均为对应本地 PDF 的物理页码。背景材料的页数取自 [PDF 清单](pdf_inventory.json)。阅读覆盖、出处核对、精确算术和完整证明审计是不同状态，以下分别说明。

## 1. 背景与综述阅读覆盖

12 份背景材料合计 **85 页**，全部对应文本已读。视觉补读用于核对提取损坏的公式及图片页；没有把全文文本阅读标成逐页视觉审查。

| 本地 PDF | 页数 | 已读范围与视觉补读 | 内容与当前任务的关系 |
|---|---:|---|---|
| [background/0317.pdf](../background/0317.pdf) | 14 | pp.1–14；全文文本 | Property B、\(m(n)\) 和构造型上界的基础介绍。 |
| [background/0520.pdf](../background/0520.pdf) | 15 | pp.1–15；另视觉核对 p.9 | 随机染色、随机贪心、临界顶点及锁定低度顶点；直接相关。 |
| [background/0612.pdf](../background/0612.pdf) | 8 | pp.1–8；另视觉核对 p.5 | 固定顶点数、顶点对覆盖和平衡染色；直接相关。 |
| [background/0722.pdf](../background/0722.pdf) | 10 | pp.1–10；另视觉核对 p.9 | \(v=2n+1\) 的 Steiner/Catalan 阻碍；提供方法背景。 |
| [bg.pdf](../bg.pdf) | 7 | pp.1–7；全文文本 | 0317 背景幻灯片的中文讲稿，内容重复。 |
| [Untitled.pdf](../Untitled.pdf) | 1 | p.1；全文文本 | 以递归构造为主的介绍性摘要，没有证明或计算证书。 |
| [Erdos #36.pdf](<../Erdos %2336.pdf>) | 5 | pp.1–5；全文文本 | 最小重叠问题中文讲稿；旁支背景。 |
| [Unit Distances in Convex Polygons.pdf](<../Unit Distances in Convex Polygons.pdf>) | 7 | pp.1–4 文本；pp.5–7 图片页逐页视觉补读 | 凸多边形单位距离问题；图片页重复前面的讲稿内容，非空白。 |
| [Survey Problem/Erdős_problem_96.pdf](<../Survey Problem/Erdős_problem_96.pdf>) | 3 | pp.1–3；全文文本 | 单位距离问题的英文幻灯片；旁支背景。 |
| [Survey Problem/Erdos_problem_7.pdf](<../Survey Problem/Erdos_problem_7.pdf>) | 4 | pp.1–4；全文文本 | 奇数互异模数覆盖系统；旁支背景。 |
| [Survey Problem/Erdos_problem_36.pdf](<../Survey Problem/Erdos_problem_36.pdf>) | 5 | pp.1–5；全文文本 | 最小重叠问题英文幻灯片；与中文讲稿同主题。 |
| [Survey Problem/Erdos_problem_835.pdf](<../Survey Problem/Erdos_problem_835.pdf>) | 6 | pp.1–6；全文文本 | Johnson 图染色；旁支背景。 |

这些文件主要是介绍性材料。相同结论在中英文讲稿中重复出现，不增加其独立证据数量。

## 2. 统一符号与基本定义

设 \(H=(V,E)\) 为有限简单 \(n\)-一致超图，\(v=|V|\)，\(m=|E|\)。Property B 指存在映射 \(c:V\to\{0,1\}\)，使每条边均含两种颜色。定义

\[
m(n)=\min\{|E|:H\text{ 为非二染色的 }n\text{-一致超图}\}.
\]

\(m(n,v)\) 是限定恰有 \(v\) 个顶点的相应极值。\(m(n)\) 是“存在一个非二染色例子”的最小边数阈值，不表示所有边数达到该值的超图都非二染色。

| 符号 | 本文含义 |
|---|---|
| \(k\) | 随机排列中的位置；涉及多色定理时改用 \(r\) 表示色数。 |
| \(A_k,B_k,C_k\) | 对应末点、首点、同时首末事件的有效概率上界。 |
| \(\gamma\) | 交集恰为一个顶点的**有序**不同边对数。 |
| \(L_A\) | 包含全部标记顶点集合 \(A\) 的边数。 |
| \(l_A\) | 与标记顶点全集的交恰为 \(A\) 的边数。 |
| \(C_t\) | Catalan 数 \(\binom{2t}{t}/(t+1)\)。 |
| \(\nu_2(a)\) | 因子 2 在正整数 \(a\) 中的指数；有理数时按分子赋值减分母赋值延拓。 |
| \(s_2(a)\) | 非负整数 \(a\) 的二进制数位和。 |

0317 pp.3–9、0520 p.2 与 bg pp.2–5 给出基础定义及 \(m(1)=1,m(2)=3,m(3)=7,m(4)=23\) 的文献背景。讲稿中的 Fano 平面是 \(m(3)\le7\) 的见证；仅展示它不等于证明下界 \(m(3)\ge7\)。

0317 pp.10–12、bg p.6 主要介绍构造型上界。所指 Aglave 等人的论文始于 2016 年预印本，正式发表于 2020 年；bg 的“最新进展”用语应按历史介绍理解。Untitled.pdf 的递归构造设想同样不改变当前的下界任务。

## 3. 固定顶点数与两种不同的计数界

### 3.1 顶点对覆盖需要最小反例条件

0612 p.4 的“最小相关反例”应明确为：在边数不超过指定上限的非二染色超图中，进一步选取顶点数最小者。这样的超图覆盖每个顶点对。

理由是，若 \(x,y\) 不共处任何边，将二者识别不会改变边的大小；删除可能重复的边也不会增加边数。商超图的合法染色可以拉回原超图，因此商超图仍非二染色，与顶点数最小矛盾。这一约化不能直接套给任意固定 \(v\) 的实例，尤其不能套给补了孤立点的实例。

若每个顶点对都被覆盖，则每个顶点的度数至少为 \(\lceil(v-1)/(n-1)\rceil\)，从而

\[
m\ge \left\lceil\frac vn\left\lceil\frac{v-1}{n-1}\right\rceil\right\rceil.
\]

这正是 0612 p.5 的双层向上取整公式，已视觉核对。直接对全部顶点对作一次计数，只得到较弱的 \(\lceil\binom v2/\binom n2\rceil\)；内层取整来自逐顶点度数约束。

### 3.2 平衡染色界

0612 p.6 另给出

\[
m(n,v)\ge
\frac{\binom vn}
{\binom{\lfloor v/2\rfloor}{n}+\binom{\lceil v/2\rceil}{n}}.
\]

在均匀选择两侧大小分别为 \(\lfloor v/2\rfloor,\lceil v/2\rceil\) 的染色时，分母与分子的比值是一条指定边单色的概率；用并集界即可得到上式。用于整数边数时还需整体向上取整。若 \(v<2n-1\)，可以把两侧都取成小于 \(n\)，直接得到合法染色，无须计算零分母。

0612 p.7 的

\[
m(n,2n+1)\ge\frac{\binom{2n+1}{n}}{n+2}=\frac{C_{n+1}}2
\]

来自**平衡染色界**，不是 p.5 的顶点对覆盖界。例如 \(n=5,v=11\) 时，两者分别给出 66 和 7。讲稿把它们都称为 covering bound 容易混淆。

Goldberg–Russell 的顶点对约化及上述界可在 Grill–Linzmayer 的引言中追踪；背景阅读阶段确认了该出处，但没有以此声称已审计所有 \(v\) 情形。

## 4. 随机贪心：可复用的事件与精确概率

### 4.1 Cherkashin–Kozik 的随机模型

本地 [Cherkashin–Kozik PDF](../ref/cherkashin_kozik_2015_random_greedy.pdf) pp.2–3：给每个顶点独立赋予 \(U[0,1]\) 出生时间，按升序扫描，优先染蓝，仅在将形成全蓝边时改红。出生时间几乎必然互异，其诱导排列均匀；p.5 Remark 3 明确指出算法只使用排列。

该算法不会留下全蓝边。若最终出现全红边 \(f\)，取其排列首点 \(x\)。\(x\) 被改红时必是另一条边 \(e\) 的排列末点。因此

\[
\{\text{算法失败}\}\subseteq
\bigcup_{(e,f)}\{\max_\sigma e=\min_\sigma f\}.
\]

把右侧的有向事件称为冲突。若发生冲突，\(e\cap f=\{x\}\)：另一个共同顶点将同时被要求排在 \(x\) 之前和之后。反过来，存在冲突边对并不保证算法失败。因此“无临界点/冲突边对”是成功的充分条件。

对一个指定方向、交集为单点的边对，精确概率为

\[
q_n=\int_0^1x^{n-1}(1-x)^{n-1}\,dx
=\frac{((n-1)!)^2}{(2n-1)!}.
\]

该积分形式见 CK p.3，阶乘形式见 [Pluhár PDF](../ref/pluhar_2009_greedy_colorings.pdf) pp.2–3。故 \(P(\text{失败})\le\gamma q_n\)。若改为按无序边对求和，每对的两个方向必须明确处理，不能再无说明地使用同一 \(\gamma\)。

CK p.3 进一步分割出生时间区间。令 \(m=\kappa2^{n-1}\)，中央区间长度为 \(p\in[0,1]\)，有

\[
P(\text{失败})\le\kappa(1-p)^n+\kappa^2p.
\]

式 (1.3) 严格小于 1 是有限参数的充分条件。随后选择随 \(n\) 变化的参数，才得到 \(\Omega(2^n\sqrt{n/\log n})\) 的渐近定理。渐近结论和“充分大的 \(n\)”常数不能直接当作 \(n=5\) 的数值证据。

### 4.2 Pluhár 原文的算法与计数表述

Pluhár p.2 的二色算法按文字表述为：初始全蓝，将每条边的排列首点改红。这与 CK 的末点贪心规则不同；可共用的充分条件是不存在上述冲突边对，不应逐字混用两个实现。

Pluhár Claim 1 将红边数 \(X\) 等同于全部 precedes 指示变量之和。用于本项目时，采用成立且足够的关系

\[
X\le Z,\qquad Z=\#\{\text{冲突有序边对}\}.
\]

一条红边可以有多个见证，而冲突边对也未必对应一条红边；因此一般不能写成等号。\(\mathbb E[X]\le\mathbb E[Z]\) 仍足以支持其期望上界。原文 p.2 的算法文字和该等号均已视觉核对。这是对可复用计数关系的限定，不是整篇定理被否定的结论。

Pluhár p.3 Lemma 2 给出多色的有序链刻画；pp.4–5 Theorem 4 给出局部引理条件。这里已全文阅读，但没有重建全部多色常数及依赖图计数。

### 4.3 有限位置求和与锁点的边界

0520 pp.9–10 意图表达的形式是

\[
P(\text{失败})\le\sum_kP(\text{位置 }k\text{ 临界})
\le\sum_k\min\{A_k,B_k,C_k\}.
\]

\(A_k,B_k,C_k\) 必须分别**不小于**相应事件概率。p.9 却将三项写成小于等于事件概率，和“上界”及后续推理方向不一致；已视觉确认，知识库采用上面的正确方向。

锁定顶点后，排列分布是相应的条件分布，需要重新计算边型与事件概率。即使有效降低了 \(C_k\)，只有当它改变该位置的最小项时才改变总和，不能把全部 \(C_k\) 扣除量直接从总界减掉。低度顶点及共度数轮廓的存在性也须由结构论证保证。

0520 p.13 报告的 \(m(5)\ge32,m(6)\ge64,m(7)\ge128,m(8)\ge263,m(9)\ge538\) 已对应到 Grill–Linzmayer Theorem 1；这里确认的是来源，不是对其全部计算程序的独立复现。

### 4.4 多色局部版本的事件限定

CK pp.3–4 用有序 \(r\)-链作为多色失败见证，并分开处理短边与不含短边的冲突链。p.4 局部版本把 \(C_s\) 简写为“链冲突”，但引用的概率估计来自“链冲突且链中没有短边”。复用该证明时，应明确用

\[
C'_s=\{s\text{ 冲突且其每条边均非短边}\}
\]

与短边事件 \(S_f\) 一起覆盖失败事件。不能把不含短边条件下所得的联合事件上界，直接套给未限定的冲突链。这个区别已核对 p.4 原始页面。

## 5. Catalan 算术与设计结构

### 5.1 精确的二进赋值定理

本地 [Deutsch–Sagan PDF](../ref/deutsch_sagan_2006_catalan_motzkin.pdf) p.3 Theorem 2.1 给出

\[
\nu_2(C_t)=s_2(t+1)-1,\qquad t\ge0.
\]

所以 \(C_t\) 为奇数当且仅当 \(t=2^a-1\)。采用 \(\nu_2\) 可避免把原文的 order/“largest power”误读成 \(2^{\nu_2}\) 本身。

pp.3–6 的组合证明对 Catalan 二叉树施加二群作用。设 \(d=s_2(t+1)-1\)，所有轨道大小都被 \(2^d\) 整除；大小恰为 \(2^d\) 的轨道数是奇数，其余轨道大小被 \(2^{d+1}\) 整除。将轨道大小相加便得精确赋值。Lemma 2.3 的轨道计数递推在 p.6 通过二叉全分割得到组合解释。本节及相关证明已精读，pp.3–5 还作了视觉核对。

对项目中的有理数理想共度数，二进赋值只能直接控制因子 2。若要断言 \(4L_{12}^0\in\mathbb Z\)，还须说明分母没有未被约去的奇素因子。即使已知 \(L_{12}^0\notin\mathbb Z\)，仍需量化它到整数的距离，才能决定概率界是否严格小于 1。

### 5.2 \(v=2n+1\) 的结构背景

0722 pp.2–4 引述 de Vries 的结论：达到 \(C_{n+1}/2\) 的阈值需要 Steiner 结构 \(S(n-1,n,2n+1)\)，即每个 \((n-1)\)-子集恰处于一条边中。这是文献定理的二手介绍；本背景分工未完整阅读 de Vries 原证明。

0722 p.6 与 p.9 的两族改进对应 Grill–Linzmayer Theorem 2：

\[
n=2^a-2,\ a\ge3
\quad\Longrightarrow\quad
m(n,2n+1)\ge\frac{C_{n+1}+3}{2},
\]

\[
n=2^r(2^{2a}+1)-2,\ r,a\ge1
\quad\Longrightarrow\quad
m(n,2n+1)\ge\frac{C_{n+1}}2+3.
\]

第二族指数已视觉核对。两族均为偶数 \(n\)，且都限定 \(v=2n+1\)，不能直接作为 \(n=5,v=22,23\) 的排除证据。

0722 p.8 的近阈值公式还隐含 \(m=m_0+x\)、\(m_0=C_{n+1}/2\) 和特定极端度数情形。其形如

\[
1+\frac{n!(n-1)!}{(2n-1)!}
\bigl(x-n|L_{12}-L_{12}^0|\bigr)
\]

的表达式，只有在相关前提成立且 \(n|L_{12}-L_{12}^0|>x\) 时才严格小于 1。讲稿的“非整数导致下降”应按这一量化条件理解。

## 6. 旁支问题：保留上下文，不改变研究目标

| 主题与材料 | 核心内容 | 可保留的边界 |
|---|---|---|
| 最小重叠：Erdos #36.pdf pp.1–5；Survey #36 pp.1–5 | 平分 \([2N]=A\sqcup B\)，研究 \(r_{A,B}(x)=|A\cap(B+x)|\)；有 \(\sum_xr_{A,B}(x)=N^2\)。 | 有限 \(N\) 的候选核验不能单独给出渐近常数改进；需有构造族或连续/离散转移。讲稿中的 \(0.379005<c<0.380876\) 只记录为其所述历史界。 |
| 凸单位距离：Unit Distances… pp.1–7；Survey #96 pp.1–3 | \(U_{\rm conv}(N)=O(N)\) 猜想，讲稿列出 \(2N-7\le U_{\rm conv}(N)\le N\log_2N+4N\)。 | “每尺度 \(O(N)\)”是讲稿直观解释；局部禁形或 charging 方案须有全局组合证明。凸位置指实际凸多边形顶点，应区别弱凸位置。 |
| 奇数覆盖系统：Survey #7 pp.1–4 | 剩余类覆盖 \(\mathbb Z\)，可等价检查模数最小公倍数 \(M\) 的完整周期。 | 模数必须大于 1；讲稿遗漏此项。普通覆盖允许重复覆盖，不能误设为恰覆盖一次。有限搜索失败不证明不存在。 |
| Johnson 图：Survey #835 pp.1–6 | 要求等价于某个 \(k>2\) 满足 \(\chi(J(2k,k))=k+1\)。相邻顶点并成 \((k+1)\)-集，给出等价及团下界。 | \(k=10\) 只是讲稿建议的候选。小规模排除与 Ma–Tang 必要条件在本分工中仍是二手记录，未读原证明。 |

最小重叠幻灯片 p.2 使用 \(c=\liminf M_N/N\)。该定义直接保证的是对每个 \(\varepsilon>0\) 最终有 \(M_N\ge(c-\varepsilon)N\)，不能无条件把边界常数 \(c\) 本身写成最终逐点下界。

奇数覆盖幻灯片 p.4 把“\(9\mid M\) 或 \(15\mid M\)”写为 likely。已找到 Balister 等合作者的原作者讲义，将其明确陈述为定理；这里已核对讲义陈述，未重建证明。

这些材料共同强调候选生成与确定性验证的分离，但没有提供本项目 \(m(5)\ge33\) 的结构引理或计算证书。

## 7. 原始文献阅读深度与版本

| 本地来源 | 页数与覆盖 | 阅读深度 | 版本及范围 |
|---|---|---|---|
| [Cherkashin–Kozik](../ref/cherkashin_kozik_2015_random_greedy.pdf) | 6 页，pp.1–6 全部 | 全文阅读；随机模型、二色事件与式 (1.1)–(1.3)重点阅读；p.4视觉核对 | PDF 显示 arXiv:1310.1368v1，2013-10-04。文件名用2015期刊年份，但未逐项比对期刊最终版。没有重建全部局部引理渐近计算。 |
| [Pluhár](../ref/pluhar_2009_greedy_colorings.pdf) | 6 页，pp.1–6 全部 | 全文阅读；二色算法、边对概率重点阅读；p.2视觉核对 | 以本地论文版本为准；没有进行全部多色常数、局部依赖计数的独立审计。 |
| [Deutsch–Sagan](../ref/deutsch_sagan_2006_catalan_motzkin.pdf) | 22 页，pp.1–22 均接触 | pp.2–6 精读定理2.1及证明；其余浏览；pp.3–5视觉核对 | PDF 显示 arXiv:math/0407326v1；未与2006期刊最终版逐项比对。其他章节不标作证明审计。 |

Deutsch–Sagan 的浏览范围：pp.6–10 为 Motzkin、Riordan、hex tree 等序列的奇偶性；pp.10–14 为 Lucas 同余及模 3 结果；pp.14–20 为其他模数、Gould、Apéry/Delannoy、Eulerian、非交叉图等结果与猜想；pp.20–22 为参考文献。这些部分未纳入当前证明依赖链。

## 8. 已定位的来源入口

以下区分“已读原文”与“仅定位来源”；不将检索到题名或摘要登记为全文阅读。

| 来源 | 链接或文献标识 | 本文采用状态 |
|---|---|---|
| Cherkashin–Kozik, *A note on random greedy coloring of uniform hypergraphs* | [arXiv:1310.1368](https://arxiv.org/abs/1310.1368)；Random Structures & Algorithms 47(3), 2015, 407–413 | 本地6页版本全文已读。 |
| Pluhár, *Greedy colorings of uniform hypergraphs* | [DOI:10.1002/rsa.20267](https://doi.org/10.1002/rsa.20267) | 本地6页版本全文已读。 |
| Deutsch–Sagan, *Congruences for Catalan and Motzkin numbers and related sequences* | [DOI:10.1016/j.jnt.2005.06.005](https://doi.org/10.1016/j.jnt.2005.06.005) | 本地版本按第7节分层阅读。 |
| Grill–Linzmayer, *Improved Lower Bounds for Property B* | [arXiv:2403.05674](https://arxiv.org/abs/2403.05674) | 本分工曾核对v3相关公式与定理出处；核心全文阅读记录由主线文献整理另行维护。 |
| Aglave–Amarnath–Shannigrahi–Singh, *Improved Bounds for Uniform Hypergraphs without Property B* | [正式期刊PDF](https://ajc.maths.uq.edu.au/pdf/76/ajc_v76_p073.pdf)；[arXiv:1602.00218](https://arxiv.org/abs/1602.00218) | 本分工核对题名、作者、摘要和2016预印本/2020期刊年份。 |
| Goldberg–Russell, *Toward computing m(4)* | Ars Combinatoria 39 (1995), 139–148 | 从核心论文参考文献追踪；本分工未读原文。 |
| de Vries, *On property B and on Steiner systems* | [DOI:10.1007/BF01179788](https://doi.org/10.1007/BF01179788) | 已定位；本分工未读完整原证明。 |
| Grill–Linzmayer, *An Overview of Property B* | [DOI:10.1007/978-3-032-18810-6_9](https://doi.org/10.1007/978-3-032-18810-6_9) | 已定位2026年章节；未取得并阅读全文。 |
| White, *Erdős’ minimum overlap problem* | [arXiv:2201.05704](https://arxiv.org/abs/2201.05704) | 旁支原始来源已定位，未全文阅读。 |
| Aggarwal, *On Unit Distances in a Convex Polygon* | [arXiv:1009.2216](https://arxiv.org/abs/1009.2216) | 旁支上界来源已定位，未全文阅读。 |
| Edelsbrunner–Hajnal, *A lower bound on the number of unit distances between the vertices of a convex polygon* | [原作者PDF](https://pub.ista.ac.at/~edels/Papers/1991-03-UnitDistancesConvexPolygon.pdf)；JCTA 56 (1991), 312–316 | 旁支下界来源已定位，未全文阅读。 |
| Balister–Bollobás–Morris–Sahasrabudhe–Tiba, *Erdős covering systems* | [arXiv:2211.01417](https://arxiv.org/abs/2211.01417)；[Morris报告讲义](https://people.maths.ox.ac.uk/scott/dmpfiles/robmorris.pdf) | 论文已定位；讲义中的9或15整除定理陈述已核对，未重建证明。 |

