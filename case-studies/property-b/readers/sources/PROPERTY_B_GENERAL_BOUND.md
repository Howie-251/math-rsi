# 单交结构带来的统一整数增益

本文证明：对每个整数 $k\ge12$，由指定 RS 重染判据得到的整数可染预算可以统一增加一个显式的正整数。所有染色结论均适用于任意有限简单 $k$ 元超图。

<p class="proof-status">定理、引理与完整证明 · 文献引用按所列版本标注</p>

## 三类结果：逐项下界、加强判据求值与统一公式

$m(k)$ 是不可二染的有限简单 $k$ 元超图所需的最少边数。从已知精确值 $m(4)=23$ 出发，本项目与合作者的工作在同一参考包络下展示三类结果：$k=5,\ldots,12$ 的逐项具体下界、本文结构加强判据C.2在 $k=12,13$ 的精确求值，以及对**每个整数 $k\ge12$**成立的统一增益定理。逐项结果利用各参数的结构与精确计算证书。**紫色与蓝色来自我们的同一个加强判据：紫色直接选取参数并严格求值，得到指定 $k$ 的更强数值；蓝色通过统一估计，导出适用于所有 $k\ge12$ 的简洁公式。** 该判据在正文编号为[推论C.2](#clique-corollary-c2)。

<div class="bound-summary"><div><span>逐项具体下界 · k = 5–12</span><strong>35 · 67 · 131 · 267 · 543 · 1112 · 2275 · 4664</strong><small>本项目与合作者的纸面证明／局部精确证书</small></div><div><span>我们的加强判据 · k = 12、13</span><strong>m(12) ≥ 4647 · m(13) ≥ 9564</strong><small>直接求值：增益14、25；严格数值证书</small></div><div><span>我们的统一公式 · 全部 k ≥ 12</span><strong>旧组合基线 ＋ 增长的整数增益</strong><small>同一统一定理已对全部 k≥12完成端到端Lean</small></div></div>

<p class="figure-mobile-hint">左右滑动图像，可查看完整坐标与图例。</p>

### 经典超图二染色问题 Property B $m(k)$｜小参数到一般定理，下界系统提升

<div class="bound-plot bound-delta" data-figure="delta"></div>

**差值主图。** 红色逐项结果、紫色加强判据点与蓝色统一公式使用同一定义的参考包络 $L_{\rm ref}(k)$：取正文已核五项明确参考式，并在 $k=5,\ldots,9$ 加入 GL Theorem 1 的具体下界后取最大值。这是指定参考集的共同包络，不称全部文献的世界最佳。全图共用同一条线性的 $k$ 横轴；红色读左侧线性轴，表示逐项结果的增益 $\Delta_{\rm ind}(k)=L_{\rm ind}(k)-L_{\rm ref}(k)$。$k=5,\ldots,12$ 依次增加3、3、3、4、5、27、30、31；$k=4$ 的零增量只标记既有精确值23。蓝色读右侧对数轴，表示统一定理相对同一包络保证增加的整数下限 $\Delta_{\rm cert}(k)=g_*(k)\le\Delta(k)$。对每个 $k\ge12$，共同包络恰为 $B_{\rm RS}(k)+1$。

**紫色图例“Our refined criterion: certified evaluation”表示我们的加强判据直接求值；蓝色“Our uniform formula (Lean)”表示由同一判据推导的统一公式。** 紫色菱形也读左侧线性轴，给出：$k=12$ 为 $4647-4633=14$，$k=13$ 为 $9564-9539=25$。这些是基于一般充分性证明、经独立数值复算的具体下界，不是新的文献基线，也不称这两项数值已经Lean核验。

在 $k=12$，红色锁点候选为 $4664-4633=31$，紫色直接求值为14，蓝色统一公式保证至少2；三者使用相同基线。$k=13$ 的C.2下界已经超过已核参考包络25；锁点探索尚未超过我们自己的C.2结果，且无成功完整新证书，图中不加入红点。两侧纵轴刻度独立，不能用曲线的视觉高低或交点判断数值反超。[共同基线的完整核验](context/propertyb-general/locks-vs-uniform-20261021/baselines/REPORT.md)

|$k$|共同参考包络|统一公式下界（增益）|我们的加强判据求值（增益）|锁点候选下界（增益）|
|---:|---:|---:|---:|---:|
|12|4633|4635（2）|4647（14）|4664（31）|
|13|9539|9542（3）|9564（25）|尚无超过C.2的完整新证书|

C.2接受预算分别为4646与9563，故相应 $m(k)$ 下界再加一。原始严格接受证书及下一预算的全参数排除均已独立复算；本次只将已有数值加入主图。[原始数值报告](context/propertyb-general/bridge-12-16-20261021/NUMERIC_REPORT.md) · [独立数值核验](context/propertyb-general/bridge-12-16-20261021/INDEPENDENT_NUMERIC_CHECK.md) · [本次绘图数据](context/propertyb-general/c2-figure-20261021/plot_c2_data.json)

一般段在 $k=12,13,14,15,16$ 保证至少增加2、3、4、6、9，并在 $k=17,32,64$ 分别保证至少增加13、2,346、152,837,269；这些是保守下限，非精确增量。对每个 $k\ge12$，$B_{\rm RS}(k)+1$ 正是正文所列五项明确参考界的最大值，因此蓝色曲线给出的也是新下界超过这一参考包络的保证增益。蓝线从12连续显示至64，同一解析定理覆盖全部 $k\ge12$；统一定理对全部 $k\ge12$ 已完成端到端Lean形式证明，蓝色实线覆盖相同范围。

### 小参数：逐项提高具体整数

<div class="bound-plot" data-figure="small"></div>

**小参数数值图。** 纵轴除以共同的指数因子 $2^k$，点旁数字仍为原始下界。灰点使用与差值主图相同的 $L_{\rm ref}$，$k=5,\ldots,13$ 依次为32、64、128、263、538、1085、2245、4633、9539。紫色菱形在12、13标出加强判据下界4647、9564；红色空心点保留12的锁点候选4664。前五项来自 [Grill–Linzmayer，Theorem 1，v3第7页](https://arxiv.org/pdf/2403.05674v3#page=7)，后四项为本文精确 RS 组合预算加一；其他参考式不超过这些值的证明与全参数核验证书见共同基线报告。$m(4)=23$ 来自 [Östergård（2014）](https://doi.org/10.1016/j.dam.2011.11.035)。

小参数的证明状态：$m(5)\ge35$ 有完整自然语言候选与局部证书，完整Lean尚未闭合；已完成Lean的五元下界为34。$k=10,11$ 采用合作者证明稿与既有局部证书。[原始材料与完整范围](research-wiki/PROPERTY_B_SMALL_K_TRANSFER.md)

六元当前为 $m(6)\ge67$：完整证明覆盖27–44点的全部实际分支，已完成完整参数域核对和独立概率复算，原超图染色接口已经闭合，尚无本参数Lean。[完整证明](context/propertyb-m6-67-progress-20261029/PROOF_M6_GE67.md) · [离线阅读页](M6_GE67.html) · [独立核验范围](context/propertyb-m6-67-progress-20261029/audit/INPUT_MAP.json) · [跨模型审阅范围](context/propertyb-m6-67-progress-20261029/reviews/DISPOSITION.md)

八元当前为 $m(8)\ge267$，九元当前为 $m(9)\ge543$。两项均有完整计算机辅助证明，分别覆盖47–120点、57–195点；全部2094型、3450型已由独立参数域重建和不同的下降阶乘注入概率实现复算通过，全部严格小于一。两项尚无本参数Lean，独立计算与跨模型审阅的范围分别记录。[八元证明](context/propertyb-m8-267-20261029/PROOF_M8_GE267.md) · [八元独立核验](context/propertyb-m8-267-20261029/independent/REVIEW.md) · [九元证明](context/propertyb-m9-543-20261029/PROOF_M9_GE543.md) · [九元独立核验](context/propertyb-m9-543-20261029/independent/REVIEW.md) · [八／九元完整离线阅读页](M8_M9_IMPROVEMENTS.html) · [联合审阅与验收](context/propertyb-small-updates-20261029/reviews-8-9/DISPOSITION.md)

七元当前为 $m(7)\ge131$：完整候选的424型及全部2,115,296个共同坏对整数向量已独立复算通过，尚未进行七元跨模型审阅或Lean核验。[七元证明及验证范围](context/propertyb-m7-131-20261029/PROOF_M7_GE131.md) · [七元独立复算](context/propertyb-m7-131-20261029/independent/RESULTS.json)

十二元当前展示更新为 $m(12)\ge4664$（相对4633增31）。新候选证明覆盖91–782点全部692个必要点数、664355个必要参数实例；独立程序重建完整参数域及全部迹重数／共度，并对20个边界实例用Fraction精确复算通过。独立检查没有第二次全量重算概率值。本次保持完整计算机辅助证明候选、无Lean；Grok已有效静态审阅新覆盖链，未发现实质问题；没有运行程序。[审阅范围与处置](context/propertyb-k12-4664-20261029/reviews/DISPOSITION.md)。[当前完整证明](context/propertyb-k12-4664-20261029/PROOF_M12_GE4664.md) · [完整计算汇总](context/propertyb-k12-4664-20261029/SUMMARY.json) · [独立核验范围](context/propertyb-k12-4664-20261029/independent/RESULTS.json)

此前 $m(12)\ge4661$（增28）的691429型证书、31型Fraction边界核验及3348个零／一锁型独立算术检查继续保留，属于旧实例证据，不作为新4664候选的全量第二算术复算。[旧实例阅读页](K12_LOCK_COMPARISON.html) · [旧证书报告](context/propertyb-general/k12-lock-pilot-20261021/pilot/REPORT.md) · [旧独立核验范围](context/propertyb-general/k12-lock-pilot-20261021/independent/REPORT.md)

小参数图的逐项结果使用空心点，加强判据求值使用紫色菱形；蓝色实线属于对全部 $k\ge12$ 已形式化的同一统一定理。

<details>
<summary>展开：每个小参数的数值与比较来源</summary>

|$k$|共同参考包络 $L_{\rm ref}$|本项目／合作者|共同基线增益|包络达到项|
|---:|---:|---:|---:|---|
|4|23（精确值）|—|0|Östergård 2014|
|5|32|35|3|GL 2024，Theorem 1|
|6|64|67|3|同上|
|7|128|131|3|同上|
|8|263|267|4|同上|
|9|538|543|5|同上|
|10|1085|1112|27|RS 精确组合预算加一|
|11|2245|2275|30|同上|
|12|4633|4664|31|同上；红点为锁点法新实例|

历史 GL 公式口径仍保留如下，仅用于对应此前展示。它们来自同文 [§2式(7)，v3第4页](https://arxiv.org/pdf/2403.05674v3#page=4) 的严格有理代入，是可行公式基线，不是原文报告纪录，也不是本次共同参考包络。

|$k$|历史 GL 式(7)基线|新展示值|相对历史口径增益|当前共同基线增益|
|---:|---:|---:|---:|---:|
|10|1070|1112|42|27|
|11|2213|2275|62|30|

原历史数据不覆盖，见[小参数历史来源](context/propertyb-general/bound-figure-20261021/SMALL_K_SOURCES.md)。本次绘图由[共同基线 JSON](context/propertyb-general/locks-vs-uniform-20261021/baselines/MATCHED_BASELINES.json)显式覆盖灰点与增益；[2026-10-29更新数据](context/propertyb-small-updates-20261029/plot_small_updates.json)更新六、七、八、九、十二元的新值与证明状态，不改参考包络；$k=12$ 的新值读取2026-10-29完整证书汇总，C.2的12、13点从原始数值证书派生并检查独立复算PASS，蓝线保留原统一公式数据。

</details>

<details>
<summary>展开：12–16与同一统一定理的连接</summary>

下表只使用统一增益公式的保守值，与蓝线完全一致；不混入红色锁点实例。旧基线为 $B_{\rm RS}+1$，新下界为 $B_{\rm RS}+1+g_*$。

|$k$|旧基线|统一定理的新下界|$\Delta_{\rm cert}=g_*$|
|---:|---:|---:|---:|
|12|4633|4635|2|
|13|9539|9542|3|
|14|19602|19606|4|
|15|40215|40221|6|
|16|82377|82386|9|

[五点绘图数据](context/propertyb-general/bridge-12-16-20261021/bridge_plot_data.json)由保存的精确证书派生，并经独立数值重算。[更强C.2数值表](context/propertyb-general/bridge-12-16-20261021/NUMERIC_REPORT.md)列出14、25、45、79、116的直接增益；其中12、13的14与25现以紫色菱形直接展示在主图，与红色逐项结果共读左轴，仍不混入同一统一公式的蓝线。

</details>

### 一般参数：统一增加可核验的整数

差值主图的蓝色曲线展示以下主定理所保证的增益：

$$m(k)\ge B_{\rm RS}(k)+1+\Delta(k),\qquad
\Delta(k)=\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)}\right\rfloor\ge2
\quad(k\ge12).$$

为绘图，对每个显示的整数 $k$ 保存一个严格通过旧判据的预算 $M_*(k)\le B_{\rm RS}(k)$，再取经定向舍入验证的整数 $g_*(k)\le\Delta(k)$。蓝色曲线画 $g_*$，因此它也是相对真正基线 $B_{\rm RS}(k)+1$ 的保证增益；没有把数值寻优冒充最大预算 $B_{\rm RS}$ 的求值。

主定理C与五项参考包络比较的同一解析证明现已延至全部 $k\ge12$：在这整个范围内，新下界超过所列五项明确参考界的最大值。12–16与17起使用同一个增益公式，增长主定理的端到端Lean范围已统一至 $k\ge12$；五项参考包络比较仍为纸面证明，图中具体数值由独立精确程序验证。一般定理的证明不依赖图中有限采样点；这些点只给出可复算的数值展示。[17起的数值见证与验证方法](context/propertyb-general/bound-figure-20261021/GENERAL_DATA.md) · [12起的统一解析证明](context/propertyb-general/bridge-12-16-20261021/ANALYTIC_EXTENSION.md) · [12起的Lean核验报告](context/propertyb-general/bridge-12-16-20261021/lean/REPORT.md)

<details>
<summary>展开：绝对下界总览（对数刻度）</summary>

<div class="bound-plot bound-overview" data-figure="overview"></div>

**绝对值参考图。** 纵轴为 $m(k)$ 的下界。一般段显示 $M_*+1$ 与 $M_*+1+g_*$，即旧判据和新定理的可验取值；新旧总量在此尺度上几乎重合。黑色菱形表示 $m(4)=23$；小参数灰点使用同一共同包络，空心点延至12并包含锁点候选4664；紫色菱形另展示12、13的C.2下界4647、9564，范围及证明状态见上文。一般段从12接起，实线属于同一已形式化的统一定理；箭头表示它继续适用于更大整数参数。

</details>

[下载整组矢量图 PDF](figures/propertyb_bounds/propertyb_bounds.pdf) · [差值主图 SVG](figures/propertyb_bounds/delta.svg) · [小参数 SVG](figures/propertyb_bounds/small.svg) · [绝对值参考 SVG](figures/propertyb_bounds/overview.svg)

## 基本定义与文献基线

**定义（超图与Property B）。** 有限简单 $k$ 元超图是 $H=(V,E)$，其中 $V$ 有限，$E\subseteq\binom Vk$。若存在 $c:V\to\{0,1\}$ 使每条边均含两色，则称 $H$ 具有 Property B。$m(k)$ 表示不具有 Property B 的此类超图的最少边数。全文 $\log$ 为自然对数。

**定义（RS组合判据的整数预算）。** 对整数 $k\ge12$，令

$$
d_k=2^{k-1},\qquad a_k(p)=1-(1-p)^k,\qquad
J_k(p)=\int_0^p(1-y^2)^{k-1}\,dy,
$$

并定义

$$
B_{\rm RS}(k)=\max\left\{M\in\mathbb Z_{\ge1}:\exists p\in[0,1],\quad
\frac{M(M-1)}{d_k^2}J_k(p)<a_k(p)^{M/d_k}\right\}.
$$

这个判据组合了 [Radhakrishnan–Srinivasan，Claim A.1，作者稿第26–27页](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=26)的正关联端项，以及 [Claim 2.4的证明，第7页的未编号积分](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=7)，再使用有向单交边对数至多 $M(M-1)$。**最大整数预算 $B_{\rm RS}$ 是本文据此定义的函数，原文没有直接定义这一记号或最大化量。** 两项估计在同一算法中的组合见[引理1](#core-lemma-1)；最大值非空、有限及 $2^k\le B_{\rm RS}(k)<k2^k$ 的证明见[引理B.4](#gain-lemma-b4)。

## 主定理：增长的整数增益

**定理C。** 设整数 $k\ge12$，并令

$$
\Delta(k)=\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)}\right\rfloor.
$$

则 $\Delta(k)\ge2$。对任意有限集合 $V$ 和任意 $E\subseteq\binom Vk$，若

$$|E|\le B_{\rm RS}(k)+\Delta(k),$$

则存在 $c:V\to\{0,1\}$，使每条 $e\in E$ 满足 $\{c(x):x\in e\}=\{0,1\}$。因此

$$\boxed{m(k)\ge B_{\rm RS}(k)+1+\Delta(k).}$$

**证明。** [引理B.4](#gain-lemma-b4)给出最大预算及其严格参数见证。[引理C.1](#clique-lemma-c1)与[推论C.2](#clique-corollary-c2)在同一最小顶点反例上削减有向单交对数；[引理B.1](#gain-lemma-b1)的参数控制保证该削减吸收新增的 $\Delta(k)$ 条边。全部不等式及原超图染色结论的推导见下文[定理C的完整证明](#clique-theorem-c)。∎

旧组合判据本身给出 $m(k)\ge B_{\rm RS}(k)+1$。定理C在整个 $k\ge12$ 范围将该下界增加 $\Delta(k)$；它不改变领先的渐近阶。对全部 $k\ge12$ 的五项明确参考包络比较见[定理D](#comparison-theorem-d)，对 $k\ge256$ 的指定零锁必要数据测试方案的比较见[定理E](#comparison-theorem-e)。

## 文献下界与本文结果对照

以下统一使用 $m(k)$ 表示不可二染的有限简单 $k$ 元超图的最少边数。为便于比较，记

$$F(k)=2^k\sqrt{\frac{k}{\log k}},\qquad c_P(k)=\frac{e^{-1/(12k)}}{\sqrt2\,\pi^{1/4}}.$$

### 论文原文给出的下界

|论文／结果|下界|适用范围|与本文的关系|
|---|---|---|---|
|Radhakrishnan–Srinivasan（2000）|$m(k)>0.1F(k)$；对每个固定 $0<c<1/\sqrt2$，有 $m(k)>cF(k)$|第一式对所有 $k\ge2$；第二式对充分大 $k\ge k_0(c)$|建立 $2^k\sqrt{k/\log k}$ 量级。原文 Theorem 2.1 用常数0.7表述充分大范围，其前段给出任意 $c<1/\sqrt2$。[作者稿p.7，Theorem 2.1及其前段](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=7)|
|Cherkashin–Kozik（2015）|对每个固定 $0<c<1/\sqrt2$，有 $m(k)>cF(k)$|充分大 $k\ge k_0(c)$|用随机贪心染色简化同一渐近下界的证明。原文使用 $2^{k-1}$ 归一化，常数写为 $c'<\sqrt2$；此处 $c=c'/2$。[刊版p.408，Theorem 1及其后段](ref/general-propertyb/cherkashin_kozik_2015_published.pdf#page=2)，[DOI](https://doi.org/10.1002/rsa.20556)|
|Pluhár（2009）|$m(k)>c_P(k)\,k^{1/4}2^k$|所有 $k\ge2$|随机贪心法的四次根下界；准确单交对概率还给出下表的阶乘判据。[作者稿p.3，Corollary 1](ref/pluhar_2009_greedy_colorings.pdf#page=3)，[DOI](https://doi.org/10.1002/rsa.20267)|
|Grill–Linzmayer（2024）|$(m(5),m(6),m(7),m(8),m(9))\ge(32,64,128,263,538)$，逐分量比较|$k=5,6,7,8,9$|这是该文锁点分析给出的具体小参数结果；一般 $k$ 的连续式和覆盖式另外列于下表。[v3 p.7，Theorem 1](https://arxiv.org/pdf/2403.05674v3#page=7)|
|本文：增长主定理C|$m(k)\ge B_{\rm RS}(k)+1+\Delta(k)$|所有 $k\ge12$|在明确的RS组合整数基线上统一增加 $\Delta(k)\ge2$；主定理的端到端Lean已覆盖全部 $k\ge12$。[定理C](#clique-theorem-c) · [完整形式证明](PROPERTY_B_GENERAL_LEAN.html)|

表中严格实数界 $m(k)>X$ 对应整数界 $m(k)\ge\lfloor X\rfloor+1$。RS与CK的渐近结论没有在这里指定统一的有限起点；本文的改进是精确有限预算之上的加性整数增益；该加性项不改变 $B_{\rm RS}$ 基线的领先渐近项。

### 同一有限参数下的精确比较

下面各 $B$ 都是**本文从所引分析定义的最大整数可染预算**，对应 $m(k)$ 的下界为 $B+1$；这些记号及最大化约定不冒充原论文的定义。令 $d=2^{k-1}$、$\kappa=M/d$，$a=a_k(p)$、$J=J_k(p)$，并令

$$\beta_k=\frac{((k-1)!)^2}{(2k-1)!}.$$

|文献来源|本文比较的有限判据／下界|已证明的关系|
|---|---|---|
|RS的正关联端项＋精确积分|$B_{\rm RS}$：存在 $p\in[0,1]$ 使 $M(M-1)J/d^2<a^\kappa$|作为统一比较基线；组合的原始来源为 [Claim A.1](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=26) 与 [Claim 2.4证明中的积分](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=7)|
|CK刊版式(2.3)，亦为RS优化的线性式|$B_{\rm lin}$：存在 $p\in[0,1]$ 使 $\kappa(1-p)^k+\kappa^2p<1$|$B_{\rm lin}\le B_{\rm RS}$，$k\ge12$。[CK刊页410](ref/general-propertyb/cherkashin_kozik_2015_published.pdf#page=4)|
|Pluhár Claim 1证明的准确排列概率|$B_{\rm pair}$：$M(M-1)\beta_k<1$|$B_{\rm pair}\le B_{\rm cont}\le B_{\rm RS}$，$k\ge12$。[作者稿pp.2–3](ref/pluhar_2009_greedy_colorings.pdf#page=2)|
|GL式(6)–(7)，取平凡有向边对上界|$B_{\rm cont}$：存在 $p\in[0,1]$ 使 $\kappa(1-p)^k+M(M-1)J/d^2<1$|$B_{\rm cont}\le B_{\rm RS}$，$k\ge12$。[GL §2](https://arxiv.org/html/2403.05674v3#S2)|
|GL式(3)–(5)重述的Goldberg–Russell型界|$L_{\rm GR}=\min_{v\ge2k-1}\max\{S_k(v),\lceil R_k(v)\rceil\}$；$S_k,R_k$定义见[引理D.1](#comparison-lemma-d1)|$L_{\rm GR}\le2^k<B_{\rm RS}+1$，$k\ge12$。[GL §1](https://arxiv.org/html/2403.05674v3#S1)|

这些支配关系的证明见[引理D.2](#comparison-lemma-d2)、[引理D.3](#comparison-lemma-d3)。因此对所有 $k\ge12$，上述五项明确下界的最大值恰为

$$L_{\rm ref}(k)=B_{\rm RS}(k)+1,$$

而本文得到

$$\boxed{m(k)\ge L_{\rm ref}(k)+\Delta(k),\qquad \Delta(k)=\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)}\right\rfloor\ge2.}$$

这是[定理D](#comparison-theorem-d)中已证明的逐参数比较。GL的小参数多锁定理保留其原范围；对 $k\ge256$ 的指定零锁必要数据方案，另有[定理E](#comparison-theorem-e)的比较。主定理C已完成全部 $k\ge12$ 的端到端Lean形式证明。比较D、E仍由正文的完整纸面证明支撑。

### 三个保守的增益例子

只用后文证明的 $B_{\rm RS}(k)\ge2^k$，便得到以下增益下限；这里没有计算 $B_{\rm RS}(k)$ 本身。

|$k$|比较基线|至少增加|
|---:|---|---:|
|17|$B_{\rm RS}(k)+1$|11|
|32|$L_{\rm ref}(k)=B_{\rm RS}(k)+1$|1,638|
|64|$L_{\rm ref}(k)=B_{\rm RS}(k)+1$|89,478,485|

这些数字采用整数与有理数保守估计，帮助理解增益规模；整个参数范围的证明在下文，不由这些例子外推。


## 证明依赖

以下依次证明概率引理、最小反例结构、最大预算的良定性和整数增益。图中每个结点均对应正文中的已编号结果；点对覆盖和团界是证明内部推出的结论，不是主定理对原超图的附加假设。

<div class="proof-route"><div><b>引理1</b><span>实际重染失败上界</span></div><i>＋</i><div><b>引理2、3、C.1</b><span>最小反例与单交团</span></div><i>→</i><div><b>推论C.2</b><span>结构加强的可染判据</span></div><i>＋</i><div><b>引理B.1、B.4</b><span>参数控制与最大预算</span></div><i>→</i><div><b>定理C</b><span>统一的正整数增益</span></div></div>


## 一、一般二染色判据与完整原图连接

<a id="core-definition-1"></a>
### 定义1：超图、二染色与单交边对

设 $k\ge2$ 为整数。有限简单 $k$ 元超图是二元组 $H=(V,E)$，其中 $V$ 为有限集合，$E\subseteq\binom Vk$ 为集合；因而每条边有恰好 $k$ 个顶点，且没有重复边。记 $v=|V|$、$m=|E|$。

若存在染色 $c:V\to\{0,1\}$，使每条边 $f\in E$ 都满足

$$
\exists x,y\in f,\qquad c(x)=0,\quad c(y)=1,
$$

则称 $H$ 具有 **Property B**。记 $m(k)$ 为不具有 Property B 的有限简单 $k$ 元超图的最小边数。此最小值存在：顶点数为 $2k-1$ 的完全 $k$ 元超图在任意二染色中都有至少 $k$ 个同色顶点，故不具有 Property B。

定义实际有向单交边对集合及其大小为

$$
\mathcal P(H)=\{(f,g)\in E\times E:f\ne g,\ |f\cap g|=1\},
\qquad \gamma(H)=|\mathcal P(H)|.
$$

其中 $(f,g)$ 与 $(g,f)$ 分别计数。定义单交图 $S(H)$ 为以 $E$ 为顶点集的简单图，两条不同原边在 $S(H)$ 中相邻，当且仅当它们恰交一点。

<a id="core-definition-2"></a>

### 定义2：解析量与结构上界

对整数 $k\ge2$、实数 $0<p\le1$ 及整数 $M\ge1$，定义

$$
d_k=2^{k-1},\qquad
 a_k(p)=1-(1-p)^k,\qquad
 J_k(p)=\int_0^p(1-y^2)^{k-1}\,dy,
$$

以及

$$
v_k(M)=\left\lfloor\frac{1+\sqrt{1+4k(k-1)M}}2\right\rfloor,
\qquad
g_k(M)=\min\left\{M(M-1),\left(1-\frac1{v_k(M)}\right)M^2\right\}.
$$

这里 $0<a_k(p)\le1$、$J_k(p)\ge0$，且 $v_k(M)\ge k$。

<a id="core-definition-3"></a>

### 定义3：随机重染过程及必要事件

给定有限简单 $k$ 元超图 $H=(V,E)$ 和 $0<p\le1$。各顶点 $x\in V$ 独立选初始颜色 $c_x\in\{0,1\}$，两色各以概率 $1/2$ 出现；独立选资格位 $b_x\sim\operatorname{Bernoulli}(p)$ 及时刻 $t_x\sim\operatorname{Unif}[0,1]$。以上全部随机量相互独立。

按时刻递增处理每个顶点一次。处理 $x$ 时，若 $b_x=1$，且存在含 $x$ 的边 $g$ 在初态为单色、截至处理 $x$ 前仍全部保持该初始颜色，则翻转 $x$；否则保持颜色。记最终染色为 $c^{\mathrm{fin}}$，失败事件为

$$
\mathcal F=\{\exists f\in E,\ \exists q\in\{0,1\},\ \forall z\in f,\ c_z^{\mathrm{fin}}=q\}.
$$

时刻互异以概率 $1$ 成立；碰撞时按预先固定的顶点次序处理，不影响下列概率。该过程为 Radhakrishnan–Srinivasan 的延迟重染算法，见 [RS2000, §2 “Slow recoloring”, 作者稿第4页 “The Algorithm”](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=4)。

定义初态残留事件

$$
\mathcal R=\{\exists f\in E:\ f\text{ 初始单色，且 }b_z=0\text{ 对所有 }z\in f\text{ 成立}\}.
$$

对 $(f,g)\in\mathcal P(H)$、$f\cap g=\{x\}$ 和目标颜色 $q\in\{0,1\}$，定义必要事件 $\mathcal N_{f,g}^{q}$ 为以下条件同时成立：

- $g$ 初始全为颜色 $1-q$，且 $b_x=1$；
- 对所有 $z\in f\setminus\{x\}$，若 $c_z=1-q$，则 $b_z=1$ 且 $t_z<t_x$；
- 对所有 $z\in g\setminus\{x\}$，若 $b_z=1$，则 $t_z>t_x$。

此事件仅规定初态、资格位和次序条件；其定义不要求 $f$ 最终单色，也不要求算法实际以 $g$ 触发 $x$ 的翻转。

<a id="core-lemma-1-1"></a>
### 引理1.1：独立 Bernoulli 变量的正关联

设 $b_1,\ldots,b_n$ 为相互独立的 Bernoulli 变量，其参数可分别取 $[0,1]$ 中的任意值。若实函数 $u,w:\{0,1\}^n\to\mathbb R$ 均关于各坐标单调不减，则

$$
\mathbb E[uw]\ge\mathbb E[u]\mathbb E[w].
$$

因此，对任意有限个关于这些坐标递增的事件 $A_1,\ldots,A_r$，有

$$
\Pr\left(\bigcap_{i=1}^r A_i\right)\ge\prod_{i=1}^r\Pr(A_i).
$$

**证明。** 对坐标数 $n$ 归纳。$n=0$ 时两函数均为常数，结论为等式。设结论对 $n-1$ 个坐标成立，并以 $\theta$ 表示最后一位取 $1$ 的概率。全协方差公式给出

$$
\operatorname{Cov}(u,w)
=\mathbb E[\operatorname{Cov}(u,w\mid b_n)]
 +\operatorname{Cov}(\mathbb E[u\mid b_n],\mathbb E[w\mid b_n]).
$$

第一项由归纳假设非负。令 $u_i$、$w_i$ 分别为将最后一位固定为 $i$ 后对其余坐标取期望的值；单调性给出 $u_1\ge u_0$、$w_1\ge w_0$，故第二项等于

$$
\theta(1-\theta)(u_1-u_0)(w_1-w_0)\ge0.
$$

这证明两函数的结论。取事件指示函数即得两个递增事件的正关联；由于递增事件的交仍递增，再对事件个数归纳得到有限交结论。∎

这是独立乘积测度下正关联的自含证明；[RS2000, Appendix A, Claim A.1 的证明，作者稿第26页](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=26)以 FKG 不等式调用这一事实。

<a id="core-lemma-1-2"></a>
### 引理1.2：初态残留概率

设 $k\ge2$、$0<p\le1$，且 $H$ 为实际边数 $m\ge1$ 的有限简单 $k$ 元超图。对定义3的随机过程，至少一条边初始单色且最终保持其初始单色颜色，当且仅当 $\mathcal R$ 发生。并且

$$
\Pr(\mathcal R)\le1-a_k(p)^{m/d_k}.
$$

**证明。** 每个顶点至多翻转一次。因此，初始为颜色 $q$ 的边最终仍全为 $q$，当且仅当它没有顶点翻转。若它的全部资格位为零，便没有顶点翻转。反之，若它存在有资格顶点而最终没有顶点翻转，则其中最早的有资格顶点被处理时，这条边仍全为原色，因而触发翻转，矛盾。这证明所述事件等价。

条件于初始染色，记初始单色边数为 $X$。对每条初始单色边 $f$，事件 $A_f=\{\exists z\in f:b_z=1\}$ 是资格位的递增事件，且其条件概率为 $a_k(p)$。由引理1.1，

$$
\Pr(\mathcal R^{\mathrm c}\mid c)\ge a_k(p)^X.
$$

每条 $k$ 元边初始单色的概率为 $2^{1-k}=1/d_k$，故 $\mathbb E X=m/d_k$。因 $a=a_k(p)>0$，函数 $x\mapsto a^x$ 为凸函数；$a=1$ 时它为常函数。Jensen 不等式于是给出

$$
\Pr(\mathcal R^{\mathrm c})\ge\mathbb E[a_k(p)^X]
\ge a_k(p)^{\mathbb E X}=a_k(p)^{m/d_k}.
$$

取补事件即得结论。∎

此估计及其正关联、Jensen 证明见 [RS2000, Appendix A, Claim A.1，作者稿第26–27页](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=26)。其中原文式(31)是条件平均等式，Claim A.1 的最终概率上界使用正关联与 Jensen；这里保留该上界未作线性放宽的形式。

<a id="core-lemma-1-3"></a>
### 引理1.3：新单色边的必要单交事件

设 $k\ge2$、$0<p\le1$，且 $H$ 为有限简单 $k$ 元超图。对定义3的过程，以概率 $1$ 有

$$
\mathcal F\subseteq\mathcal R\ \cup\!
 \bigcup_{(f,g)\in\mathcal P(H)}\ \bigcup_{q\in\{0,1\}}\mathcal N_{f,g}^{q}.
$$

此外，每个 $(f,g)\in\mathcal P(H)$ 和 $q\in\{0,1\}$ 均满足

$$
\Pr(\mathcal N_{f,g}^{q})=2^{1-2k}J_k(p).
$$

**证明。** 先限制到所有时刻互异的概率 $1$ 事件。若 $f$ 最终全为 $q$，且初态也全为 $q$，则由引理1.2得到 $\mathcal R$。否则，在 $f$ 中初始为 $1-q$ 的非空顶点集中，选取处理最晚者 $x$。这些顶点最终均为 $q$，故均已翻转。$x$ 翻转时，有一条含 $x$ 的触发边 $g$，它初始全为 $1-q$，且直到当时仍全为 $1-q$。

若还存在 $z\in(f\cap g)\setminus\{x\}$，则 $z$ 初始为 $1-q$、最终为 $q$，所以必须在 $x$ 之前翻转；这与 $g$ 在处理 $x$ 时仍保持初始单色矛盾。因此 $f\cap g=\{x\}$。因为 $|f|=k\ge2$，这又蕴含 $f\ne g$。

$x$ 翻转需要 $b_x=1$。$f\setminus\{x\}$ 中所有初始为 $1-q$ 的顶点都在 $x$ 之前翻转，故均有资格且时刻小于 $t_x$。对 $g\setminus\{x\}$ 中任一有资格顶点 $z$，若 $t_z<t_x$，则由于 $g$ 在处理 $x$ 前未有顶点翻转，$z$ 被处理时便会由 $g$ 触发翻转，矛盾。因此 $t_z>t_x$。这些正是 $\mathcal N_{f,g}^{q}$ 的全部条件，覆盖关系得证。这一论证也覆盖 $f$ 初态全为 $1-q$、最终全为 $q$ 的情形。

再固定单交对 $(f,g)$ 及交点 $x$，条件于 $t_x=t$。对每个 $S\subseteq f\setminus\{x\}$，规定 $S$ 恰为该集合中初始颜色为 $1-q$ 的顶点集，同时规定 $g$ 初始全为 $1-q$。因 $|f\cup g|=2k-1$，此初态配置的概率为 $2^{-(2k-1)}$。其余资格及次序条件分别发生于互不相交的顶点集：$x$ 有资格的概率为 $p$；每个 $z\in S$ 有资格且早于 $x$ 的概率为 $pt$；每个 $z\in g\setminus\{x\}$ 不同时满足有资格和早于 $x$ 的概率为 $1-pt$。故相应联合概率为

$$
2^{1-2k}p(pt)^{|S|}(1-pt)^{k-1}.
$$

不同 $S$ 的初始配置互斥。对 $S$ 求和、再对 $t$ 积分，得到

$$
\begin{aligned}
\Pr(\mathcal N_{f,g}^{q})
&=2^{1-2k}p\int_0^1(1-pt)^{k-1}(1+pt)^{k-1}\,dt\\
&=2^{1-2k}\int_0^p(1-y^2)^{k-1}\,dy
=2^{1-2k}J_k(p).
\end{aligned}
$$

最后一步使用换元 $y=pt$。∎

必要事件的单交归约见 [RS2000, §2.1, Lemma 2.1 与 Claims 2.1–2.3，作者稿第5–6页](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=5)；精确积分见 [RS2000, Claim 2.4 的证明，作者稿第7页未编号积分式](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=7)。原文在该积分之后才进一步放宽概率；这里直接保留积分。

<a id="core-lemma-1"></a>
### 引理1：完整RS上界

设 $k\ge2$ 为整数、$0<p\le1$，$H$ 为实际边数 $m\ge1$ 的有限简单 $k$ 元超图。则定义3的实际重染失败概率满足

$$
\Pr(\mathcal F)\le
1-a_k(p)^{m/2^{k-1}}+
\frac{\gamma(H)}{4^{k-1}}J_k(p).\tag{1}
$$

**证明。** 对引理1.3的覆盖关系使用并界，再代入引理1.2及引理1.3的概率式，得

$$
\begin{aligned}
\Pr(\mathcal F)
&\le\Pr(\mathcal R)+\sum_{(f,g)\in\mathcal P(H)}\sum_{q\in\{0,1\}}
\Pr(\mathcal N_{f,g}^{q})\\
&\le1-a_k(p)^{m/2^{k-1}}+2\gamma(H)2^{1-2k}J_k(p),
\end{aligned}
$$

而 $2\cdot2^{1-2k}=4^{1-k}$，故得式(1)。∎

引理1将 [RS2000, Appendix A, Claim A.1](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=26) 的残留估计与 [RS2000, Claim 2.4 的证明](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=7)中的精确积分作用于同一实际算法，并保留实际有向单交对数。式(1)是这些估计的组合，不是对原文某一条定理的逐字转述。

<a id="core-lemma-2"></a>
### 引理2：最小顶点反例覆盖

设整数 $k\ge2$、$M\ge1$。若存在边数至多 $M$ 的非 Property B 有限简单 $k$ 元超图，则其中存在顶点数最少的反例 $H=(V,E)$。对任一这样的 $H$，记 $v=|V|$、$m=|E|$，则 $m\ge1$、$v\ge k$，任意两个不同顶点都同处于至少一条边，且

$$
\binom v2\le m\binom k2\le M\binom k2,
\qquad v\le v_k(M).\tag{2}
$$

此约化见 [Grill–Linzmayer，§1，式(3)前的Goldberg–Russell论证](https://arxiv.org/html/2403.05674v3#S1)。

**证明。** 有限顶点数的非空集合有最小值，故可选取所述 $H$。没有边的超图具有 Property B，因此 $m\ge1$，继而 $v\ge k$。

若两个不同顶点 $x,y$ 从未同处一条边，将它们合并，其他顶点不变。每条原边的像仍有恰好 $k$ 个顶点；以这些像边组成集合得到简单 $k$ 元超图，其边数不超过 $m$。若像超图具有 Property B，将其染色沿合并映射拉回，便使每条原边同时含两色，违背 $H$ 为反例。因此像超图仍为边数至多 $M$ 的反例，却比 $H$ 少一个顶点，矛盾。

于是每对不同顶点至少同处一条边。计数所有“顶点对包含于边”的关联，得 $\binom v2\le m\binom k2\le M\binom k2$。解关于 $v$ 的二次不等式并利用 $v$ 为整数，即得 $v\le v_k(M)$。∎

<a id="core-lemma-3-1"></a>
### 引理3.1：由团数控制图的边数

设 $G$ 为有 $m\ge1$ 个顶点的有限简单图。若其每个团的大小都不超过实数 $r\ge1$，则

$$
2|E(G)|\le\left(1-\frac1r\right)m^2.
$$

**证明。** 令 $T$ 为 $G$ 的补图，记 $T$ 的顶点度数为 $\delta_1,\ldots,\delta_m$。均匀随机排列全部顶点，并选取早于自身全部 $T$ 邻居的顶点。若两个所选顶点在 $T$ 中相邻，则它们各自都须早于对方，矛盾；故所选集合在 $T$ 中独立，在 $G$ 中为团，其大小至多 $r$。

顶点 $i$ 被选中的概率为 $1/(\delta_i+1)$。取期望，再用 Cauchy–Schwarz 不等式，得到

$$
r\ge\sum_{i=1}^m\frac1{\delta_i+1}
\ge\frac{m^2}{\sum_{i=1}^m(\delta_i+1)}
=\frac{m^2}{m+2|E(T)|}.
$$

因为 $m+2|E(T)|=m^2-2|E(G)|>0$，整理即得结论。∎

此为 Turán 团数上界所对应的边数不等式；上面的随机排列证明不需要精确 Turán 数或等号情形的分类。

<a id="core-lemma-3"></a>
### 引理3：Gram矩阵与单交图界

设 $k\ge2$，且 $H=(V,E)$ 为实际边数 $m\ge1$、顶点数 $v$ 的有限简单 $k$ 元超图。则 $S(H)$ 的每个团大小至多 $v$，且

$$
\gamma(H)\le\left(1-\frac1v\right)m^2.\tag{3}
$$

若此外 $m\le M$ 且 $H$ 是引理2中的最小顶点反例，则

$$
\gamma(H)\le g_k(M).\tag{4}
$$

**证明。** 取 $S(H)$ 中任一 $q$ 点团，即取 $q$ 条两两恰交一点的不同原边。令 $A$ 为这些边的 $0/1$ 关联矩阵，行对应所选边，列对应 $V$。每行恰有 $k$ 个 $1$，不同两行的内积为 $1$，故

$$
AA^{\mathsf T}=(k-1)I_q+J_q,
$$

其中 $I_q$ 为单位矩阵，$J_q$ 为全一矩阵。对非零实向量 $z\in\mathbb R^q$，由于 $k\ge2$，有

$$
z^{\mathsf T}AA^{\mathsf T}z
=(k-1)\sum_{i=1}^qz_i^2+\left(\sum_{i=1}^qz_i\right)^2>0.
$$

因此 $AA^{\mathsf T}$ 为正定矩阵，$q=\operatorname{rank}(AA^{\mathsf T})\le\operatorname{rank}(A)\le v$。将引理3.1用于 $G=S(H)$、$r=v$，并注意 $2|E(S(H))|=\gamma(H)$，便得式(3)。

若 $H$ 是引理2的反例，则 $v\le v_k(M)$。因 $m\le M$，式(3)给出

$$
\gamma(H)\le\left(1-\frac1{v_k(M)}\right)M^2.
$$

另一方面，按有向不同边对计数，总有 $\gamma(H)\le m(m-1)\le M(M-1)$。对这两个上界取最小值即为式(4)。∎

<a id="core-theorem-a"></a>
### 定理A：无附加结构假设的充分判据

设整数 $k\ge2$、$M\ge1$。若存在实数 $p\in(0,1]$ 满足

$$
1-a_k(p)^{M/2^{k-1}}+
\frac{g_k(M)}{4^{k-1}}J_k(p)<1,\tag{A}
$$

则任意边数至多 $M$ 的有限简单 $k$ 元超图均具有 Property B。因此 $m(k)\ge M+1$。

**证明。** 没有边的超图具有 Property B。若结论不成立，由引理2可取顶点数最少的反例 $H$，其实际边数满足 $1\le m\le M$。将引理1用于这个 $H$。因为 $0<a_k(p)\le1$ 且 $m\le M$，有

$$
1-a_k(p)^{m/2^{k-1}}\le1-a_k(p)^{M/2^{k-1}}.
$$

再由引理3的式(4)、$J_k(p)\ge0$ 以及假设(A)，实际失败概率满足

$$
\Pr(\mathcal F)
\le1-a_k(p)^{M/2^{k-1}}+
\frac{g_k(M)}{4^{k-1}}J_k(p)<1.
$$

所以补事件 $\mathcal F^{\mathrm c}$ 有正概率，存在一个随机结果使最终染色中没有单色边。其最终染色为 $H$ 的合法二染色，与 $H$ 为反例矛盾。因此所有边数至多 $M$ 的原始超图均具有 Property B。根据 $m(k)$ 的定义，$m(k)\ge M+1$。∎

### 参考文献

[RS2000] Jaikumar Radhakrishnan and Aravind Srinivasan. *Improved bounds and algorithms for hypergraph 2-coloring*. Random Structures & Algorithms **16**(1) (2000), 4–32. [DOI](https://doi.org/10.1002/%28SICI%291098-2418%28200001%2916%3A1%3C4%3A%3AAID-RSA2%3E3.0.CO%3B2-2)；[作者稿](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf)；本地副本：`ref/radhakrishnan_srinivasan_2000_two_coloring.pdf`。本文的章节、命题编号及具体页码均按该作者稿标注。

## 二、旧预算的有限性与统一加一余量

### 定义B.1：精确接受集合与预算

给定整数 $k\ge12$，令 $d=2^{k-1}$，并对 $p\in[0,1]$ 定义

$$
a_k(p)=1-(1-p)^k,\qquad
J_k(p)=\int_0^p(1-y^2)^{k-1}\,dy.
$$

定义整数接受集合

$$
\mathcal A_k=\left\{M\in\mathbb Z_{\ge1}:\exists p\in[0,1],\quad
\frac{M(M-1)}{d^2}J_k(p)<a_k(p)^{M/d}\right\}.
$$

<a id="gain-definition-brs"></a>
此判据由 [引理1](#core-lemma-1) 的实际重染失败上界和有向单交对数 $\gamma(H)\le M(M-1)$ 得到。其概率分析来自 [Radhakrishnan–Srinivasan 作者稿](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf)：第4页第2节给出延迟重染算法，第6页给出 Claim 2.4，第7页其证明中的未编号式给出所用精确积分，第26–27页附录A的 Claim A.1 给出正关联与 Jensen 估计。本文组合这些估计、保留精确积分并采用 $M(M-1)$ 的有向对计数，定义 $\mathcal A_k$ 及下述预算；原文不逐字包含这一预算量。

引理B.4将证明 $\mathcal A_k$ 非空且有限，因此下式良定：

$$
B_{\rm RS}(k)=\max\mathcal A_k
=\max\left\{M\in\mathbb Z_{\ge1}:\exists p\in[0,1],\quad
\frac{M(M-1)}{d^2}J_k(p)<a_k(p)^{M/d}\right\}.\tag{1}
$$

### 引理B.1：接受参数的控制

<a id="gain-lemma-b1"></a>
设 $k\ge12$ 为整数，$M\in\mathcal A_k$ 且 $M\ge2^k$。设 $p\in[0,1]$ 是接受不等式的见证，记 $a=a_k(p)$、$J=J_k(p)$、$\kappa=M/d$。则

$$
p>\frac1{k^2},\qquad J\ge\frac1{2k^2},\qquad
\kappa<2k,\qquad \kappa\log a>-2\log k.
$$

**证明。** 因为 $M\ge2^k$，所以 $\kappa\ge2$、$M\ge2$。接受不等式给出

$$
\frac{\kappa^2}2J\le\frac{M(M-1)}{d^2}J<a^\kappa.\tag{3}
$$

当 $p=0$ 时，接受不等式两边同为零，因此 $p>0$，从而 $a>0$。若 $p\le1/k^2$，则对 $0\le y\le p$，Bernoulli 不等式给出

$$
(1-y^2)^{k-1}\ge1-(k-1)y^2\ge1-\frac{k-1}{k^4}\ge\frac12.
$$

因此 $J\ge p/2$。又由 Bernoulli 不等式有 $a\le kp$，故 (3) 蕴含

$$
\frac{\kappa^2}{4k}<(kp)^{\kappa-1}\le kp\le\frac1k\le\frac{\kappa^2}{4k},
$$

矛盾。这里使用了 $0<kp\le1/k\le1$ 及 $\kappa\ge2$。所以 $p>1/k^2$。在区间 $[0,1/k^2]$ 上使用同一被积函数下界，得到

$$
J\ge\frac1{2k^2},\qquad
a^\kappa>\frac{\kappa^2}{4k^2}\ge\frac1{k^2}.
$$

由于 $a\le1$，后一严格不等式一方面给出 $\kappa^2/(4k^2)<1$，另一方面可以取对数。因此

$$
\kappa<2k,\qquad \kappa\log a>-2\log k.\tag{4}
$$

∎

### 引理B.2：统一增长比较

<a id="gain-lemma-b2"></a>
对所有实数 $x\ge17$，有

$$
2^{x/2}>8x+4x\log x.\tag{5}
$$

此外，若 $k\ge17$、$M\ge2^k$ 均为整数，$N=M+1$，$v=v_k(N)$，则 $v\ge k$，并且

$$
\frac1v\ge\frac1{2k\sqrt M}>\frac{4+2\log k}{M}.\tag{6}
$$

**证明。** 先验证 (5) 的起点。由

$$
e^3>\sum_{j=0}^5\frac{3^j}{j!}=\frac{92}5>17
$$

得到 $\log17<3$。又 $\sqrt2>7/5$，故在 $x=17$ 时，(5) 左边大于 $256\cdot7/5>340$，右边小于 $340$。由

$$
\log2=\int_1^2\frac{dt}{t}>\frac12
$$

可得比值 $2^{x/2}/[x(2+\log x)]$ 的对数导数满足

$$
\frac{\log2}2-\frac1x-\frac1{x(2+\log x)}
>\frac14-\frac2x\ge\frac14-\frac2{17}>0.
$$

所以 (5) 对全部 $x\ge17$ 成立。

根据 $v_k(N)$ 的定义，$N\ge1$ 蕴含 $v\ge k$，且

$$
v\le1+k\sqrt N\le2k\sqrt M.
$$

最后一个不等式使用 $N\le2M$、$\sqrt2<3/2$ 以及 $1\le(k/2)\sqrt M$。又由 $\sqrt M\ge2^{k/2}$ 和 (5) 得到 $\sqrt M>8k+4k\log k$；将其除以 $2kM$，即得 (6)。∎

### 引理B.3：接受预算的加一转换

<a id="gain-lemma-b3"></a>
设 $k\ge17$ 为整数，$M\in\mathcal A_k$ 且 $M\ge2^k$。则任意边数至多 $M+1$ 的有限简单 $k$ 元超图均具有 Property B。

**证明。** 取 $M$ 的一个接受见证 $p$，沿用引理B.1中的 $a,J,d,\kappa$。令 $N=M+1$、$v=v_k(N)$，并置

$$
R=\frac{N^2(1-1/v)}{M(M-1)}>0.
$$

由 $\log(1+t)\le t$、$\log(1-t)\le-t$ 的适用情形，结合引理B.2的 (6) 及引理B.1的 (4)，得到

$$
\begin{aligned}
\log R
&\le\frac2M-\frac1v+\frac1{M-1}\\
&\le\frac4M-\frac1v\\
&<-\frac{2\log k}{M}\\
&<\frac{\kappa\log a}{M}=\frac{\log a}{d}.
\end{aligned}
$$

第二步使用 $1/(M-1)\le2/M$。所有对数均有定义，因为 $M\ge2$、$v\ge k\ge17$、$a>0$。于是

$$
\frac{g_k(N)}{M(M-1)}\le R<a^{1/d}.
$$

将此式与 $M$ 的接受不等式相乘，得到

$$
\frac{g_k(N)}{d^2}J<a^{(M+1)/d}.
$$

引理B.1给出 $p>0$，所以该不等式满足定理A对参数的要求，并且正是定理A在预算 $N$ 的充分条件。因此任意至多 $M+1$ 边的原始超图均可二染。∎

### 引理B.4：接受集合的有限最大值

<a id="gain-lemma-b4"></a>
对每个整数 $k\ge12$，集合 $\mathcal A_k$ 非空且有限，含有 $2^k$，且其每个元素均小于 $k2^k$。因此 $B_{\rm RS}(k)$ 存在，满足 $2^k\le B_{\rm RS}(k)<k2^k$，并且该最大整数本身有一个接受见证 $p\in(0,1]$。

**证明。** 取 $M_0=2^k$、$p=1/k$。由二项式展开的前三项，

$$
(1-1/k)^{-k}=\left(1+\frac1{k-1}\right)^k
\ge1+\frac{k}{k-1}+\frac{k}{2(k-1)}>\frac52,
$$

故 $(1-1/k)^k<2/5$，即 $a_k(1/k)>3/5$。又 $J_k(1/k)\le1/k$，因此

$$
\frac{M_0(M_0-1)}{d^2}J_k(1/k)
<\frac4k\le\frac13<\frac9{25}<a_k(1/k)^2.
$$

这证明 $M_0\in\mathcal A_k$。若 $M\in\mathcal A_k$ 且 $M\ge2^k$，引理B.1给出 $M/d<2k$，即 $M<k2^k$；若 $M<2^k$，同一上界也成立。因此 $\mathcal A_k$ 是非空有限整数集合，必有最大元。最大元属于 $\mathcal A_k$，故有实际见证；由引理B.1，该见证满足 $p>0$。这里无需假定任何连续参数优化问题的最优值可达。∎

### 定理B：统一加一增益

<a id="gain-theorem-b"></a>
对每个整数 $k\ge17$，式 (1) 定义的预算满足

$$
2^k\le B_{\rm RS}(k)<k2^k,\qquad
\boxed{m(k)\ge B_{\rm RS}(k)+2.}\tag{2}
$$

等价地，任意有限简单 $k$ 元超图，只要边数至多 $B_{\rm RS}(k)+1$，就具有 Property B；此结论不附加顶点数、点对覆盖、度数、共度或线性条件。

**证明。** 引理B.4保证 $B_{\rm RS}(k)\in\mathcal A_k$、$B_{\rm RS}(k)\ge2^k$，并给出 (2) 中预算的上下界。将引理B.3用于 $M=B_{\rm RS}(k)$，即得所有至多 $B_{\rm RS}(k)+1$ 边的原始超图均可二染。因此不可二染超图至少有 $B_{\rm RS}(k)+2$ 条边。∎

### 精确性与比较范围

积分是显式有理系数多项式：

$$
J_k(p)=\sum_{j=0}^{k-1}(-1)^j\binom{k-1}j\frac{p^{2j+1}}{2j+1}.
$$

令 $Q=M(M-1)J_k(p)/d^2\ge0$。接受判据等价于 $Q^d<a_k(p)^M$，因而是 $p\in[0,1]$ 上有理多项式的严格正性问题。引理B.4将候选整数 $M$ 限制在有限区间内；定义及统一证明均不依赖浮点搜索。

对任何 $M\in\mathcal A_k$，CORE引理1配合 $\gamma(H)\le M(M-1)$，直接给出任意至多 $M$ 边的原始超图均可二染。因此式 (1) 的判据给出的整数下界为 $m(k)\ge B_{\rm RS}(k)+1$，定理B将它在整个 $k\ge17$ 范围至少提高一。其他参考函数及指定离散位置／度共度测试方案的比较见 [BASELINE_COMPARISON.md](#comparison-theorem-d)，其范围由各自定理陈述。

## 三、公共点二分与增长的整数增益

### 引理C.1：单交团的公共点二分

<a id="clique-lemma-c1"></a>
设整数 $k\ge2$、$q\ge1$、$v\ge k$，$V$ 为大小 $v$ 的有限集合，$e_1,\ldots,e_q\subseteq V$ 为互异的 $k$ 元集合，且对所有 $i\ne j$ 有 $|e_i\cap e_j|=1$。则：

- 若 $\bigcap_{i=1}^q e_i\ne\varnothing$，则 $q(k-1)+1\le v$；
- 若 $\bigcap_{i=1}^q e_i=\varnothing$，则 $q\le k^2-k+1$。

因此，对任意 $v$ 点简单 $k$ 元超图 $H$，有

$$
\omega(S(H))\le\max\left\{k^2-k+1,\left\lfloor\frac{v-1}{k-1}\right\rfloor\right\}.
$$

**证明。** 若存在公共点 $x$，两两单交保证 $e_i\setminus\{x\}$ 互不相交。因此所有边的并集恰有 $q(k-1)+1$ 个顶点，得到第一个结论；这也包括 $q=1$ 的情形。

若没有公共点，固定一条边 $e$。对每个 $x\in e$，存在族中一条不含 $x$ 的边 $f_x$。设 $d_x$ 是族中含 $x$ 的边数。这些边与 $f_x$ 的交点两两不同：若两条含 $x$ 的边在 $f_x$ 上有同一交点 $y$，则因 $x\notin f_x$ 而 $y\ne x$，这两条边便至少交于 $x,y$ 两点，违背假设。故 $d_x\le|f_x|=k$。每条不同于 $e$ 的边恰交 $e$ 一点，因而

$$
q-1=\sum_{x\in e}(d_x-1)\le k(k-1).
$$

这给出第二个结论。最后，将二分应用于 $S(H)$ 的任意非空团，即得所述团数上界；若 $H$ 无边，其单交图的团数为零，上界仍成立。∎

### 推论C.2：加强的无结构二染色判据

<a id="clique-corollary-c2"></a>
设整数 $k\ge2$、$N\ge1$。定义

$$
r_k(N)=\min\left\{v_k(N),\max\left\{k^2-k+1,\left\lfloor\frac{v_k(N)-1}{k-1}\right\rfloor\right\}\right\},
$$

以及

$$
g_k^*(N)=\min\left\{N(N-1),N^2\left(1-\frac1{r_k(N)}\right)\right\}.
$$

若存在 $p\in(0,1]$ 满足

$$
\frac{g_k^*(N)}{4^{k-1}}J_k(p)<a_k(p)^{N/2^{k-1}},
$$

则任意边数至多 $N$ 的有限简单 $k$ 元超图均具有 Property B。因此 $m(k)\ge N+1$。结论不附加顶点数、点对覆盖、度数、共度或线性假设。

**证明。** 因 $N\ge1$，有 $v_k(N)\ge k$；又 $k^2-k+1\ge k$，故 $r_k(N)\ge k\ge2$，定义中的分母均非零。

若结论不成立，按CORE引理2选取边数至多 $N$ 的最小顶点反例 $H$，记实际顶点数为 $v$、边数为 $m$。该引理给出 $v\le v_k(N)$。CORE引理3的关联矩阵论证给出 $\omega(S(H))\le v$，引理C.1则给出另一团数上界。结合这两个界及右端对 $v$ 的单调性，得到

$$
\omega(S(H))\le r_k(N).
$$

为将此界转为有向单交对数的上界，令 $T$ 为 $S(H)$ 的补图，顶点度数记为 $d_1,\ldots,d_m$。引理3.1中随机排列选独立集的论证及 Cauchy–Schwarz 不等式给出

$$
r_k(N)\ge\alpha(T)\ge\sum_{i=1}^m\frac1{d_i+1}
\ge\frac{m^2}{m+2|E(T)|}.
$$

由 $\gamma(H)=m(m-1)-2|E(T)|$，可得

$$
\gamma(H)\le\left(1-\frac1{r_k(N)}\right)m^2.
$$

再结合 $\gamma(H)\le m(m-1)$ 及 $m\le N$，得到 $\gamma(H)\le g_k^*(N)$。将这一上界代入CORE引理1，并使用 $0<a_k(p)\le1$、$m\le N$，实际失败概率至多为

$$
1-a_k(p)^{N/2^{k-1}}+\frac{g_k^*(N)}{4^{k-1}}J_k(p)<1.
$$

于是存在合法二染色，与 $H$ 是反例矛盾。∎

### 定理C：增长的整数增益

<a id="clique-theorem-c"></a>
设整数 $k\ge12$，并以定义B.1定义 $B_{\rm RS}(k)$。置

$$
\Delta(k)=\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)}\right\rfloor.
$$

则 $\Delta(k)\ge2$，且任意边数至多 $B_{\rm RS}(k)+\Delta(k)$ 的有限简单 $k$ 元超图均具有 Property B。因此

$$
\boxed{m(k)\ge B_{\rm RS}(k)+1+
\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)}\right\rfloor}
\qquad(k\ge12).
$$

**证明。** 先证明对任意整数 $M\in\mathcal A_k$、$M\ge2^k$，都可在同一个接受参数下增加

$$
s=\left\lfloor\frac{\sqrt M}{8(1+\log k)}\right\rfloor
$$

条边。取接受见证 $p$，记 $a=a_k(p)$、$J=J_k(p)$、$d=2^{k-1}$、$\kappa=M/d$，并令 $t=\sqrt M$、$N=M+s$。引理B.1保证 $p>0$、$a>0$，且

$$
\kappa\log a>-2\log k.
$$

先控制 $s$ 的范围。由

$$
\log2=\int_1^2\frac{du}{u}>\frac12,
\qquad e^3>1+3+\frac92+\frac{27}6=13>12,
$$

可得 $\log12<3$；对于实数 $x\ge12$，比值 $2^{x/2}/[8(1+\log x)]$ 的对数导数满足

$$
\frac{\log2}2-\frac1{x(1+\log x)}
>\frac14-\frac1{12}>0.
$$

在起点12，该比值大于 $64/32=2$。结合 $t\ge2^{k/2}$，得到 $s\ge2$。又因 $8(1+\log k)>1$ 且 $M\ge1$，有 $s\le t\le M$，从而 $N\le2M$。

接着控制 $r=r_k(N)$。对实数 $x\ge12$，

$$
\frac{d}{dx}\log\frac{2^{x/2}}{x^2}
=\frac{\log2}2-\frac2x
>\frac14-\frac2{12}>0.
$$

由起点 $12^2=144<3\cdot2^6=192$，得到

$$
k^2-k+1\le k^2<3\cdot2^{k/2}\le3t.
$$

根据 $v=v_k(N)$ 的定义，有 $v\ge k$、$v(v-1)\le k(k-1)N$，故

$$
\frac{v-1}{k-1}\le\sqrt{\frac{kN}{k-1}}\le2t.
$$

最后一步使用 $N\le2M$ 及 $k/(k-1)\le2$。因此，推论C.2中定义的 $r$ 满足

$$
k\le r\le3t.
$$

由 $t\ge2^{k/2}\ge64>24$ 及 $s$ 的定义，有统一严格余量

$$
(2+2\log k)s+2\le\frac t4+2
<\frac t3\le\frac M r.
$$

再由初等对数不等式 $\log(1+u)\le u$、$\log(1-u)\le-u$ 的适用情形，

$$
\begin{aligned}
\log\frac{N^2(1-1/r)}{M(M-1)}
&=2\log\left(1+\frac sM\right)+\log\left(1-\frac1r\right)
+\log\left(1+\frac1{M-1}\right)\\
&\le\frac{2s+2}{M}-\frac1r\\
&<-\frac{2s\log k}{M}\\
&<\frac{s\kappa\log a}{M}=\frac{s\log a}{d}.
\end{aligned}
$$

第二行使用 $1/(M-1)\le2/M$；第三行使用上述严格余量；第四行使用引理B.1及 $s>0$。所有对数均有定义，因为 $M\ge2$、$r\ge k\ge12$、$a>0$。因此

$$
\frac{g_k^*(N)}{M(M-1)}<a^{s/d}.
$$

与 $M$ 的同一个接受见证的不等式相乘，得到

$$
\frac{g_k^*(N)J}{d^2}<a^{N/d}.
$$

推论C.2的参数条件 $k\ge2$、$N\ge1$、$p\in(0,1]$ 均已满足，故任意至多 $N=M+s$ 边的原始有限简单 $k$ 元超图均可二染。该推论在内部选取最小顶点反例，证明其点对覆盖，并将同一实际单交图的团数界转为实际重染失败概率小于1；这些结构均不是原始超图的附加假设。

最后，引理B.4给出 $B_{\rm RS}(k)\in\mathcal A_k$ 及 $B_{\rm RS}(k)\ge2^k$；取 $M=B_{\rm RS}(k)$，便得到 $s=\Delta(k)\ge2$ 以及所述染色结论和整数下界。∎

引理C.1是线性交族的自含团界。其公共点二分只用于约束同一实际超图的单交团，不要求将全部团划为两种全局结构。定理C始终保留同一个接受见证 $p$，用有向单交对数的削减吸收新增的 $\Delta(k)$ 条边。与其他明确参考界的比较见 [BASELINE_COMPARISON.md](#comparison-theorem-d)。

## 四、参考界与有限测试方案的完整比较

### 定义D.1：参考预算与参考包络

本节固定整数 $k\ge12$。超图、Property B及 $m(k)$ 沿用定义1；本节的所有全域染色结论均量化任意有限简单 $k$ 元超图。

令 $d=2^{k-1}$、$r=k-1$，并记

$$
\kappa=\frac Md,\qquad
a_k(p)=1-(1-p)^k,\qquad
J_k(p)=\int_0^p(1-y^2)^r\,dy,\qquad
\gamma_0(M)=M(M-1).
$$

沿用前文的整数预算

$$
B_{\rm RS}(k)=\max\left\{M\in\mathbb Z_{\ge1}:\exists p\in[0,1],\quad
1-a_k(p)^{M/d}+\frac{\gamma_0(M)}{d^2}J_k(p)<1\right\}.
\tag{B1}
$$

式(B1)是本文定义的预算函数：将 [RS2000，Claim A.1、式(31)，作者稿第26–27页](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=26)的正关联端项，与 [RS2000，Claim 2.4的证明，第7页未编号积分](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=7)组合，并对有向单交边对使用 $\gamma(H)\le M(M-1)$。完整组合由本文引理1证明；原文没有定义同名的 $B_{\rm RS}$。定义B.1及引理B.4已证明其良定性，并给出

$$2^k\le B_{\rm RS}(k)<k2^k.$$

为固定比较对象，再定义：

* $B_{\rm lin}(k)$：存在 $p\in[0,1]$ 使 $\kappa(1-p)^k+\kappa^2p<1$ 的最大整数预算。所用线性充分判据见 [CK2015，§2，式(2.1)–(2.3)，刊页409–410](https://doi.org/10.1002/rsa.20556)；其最大整数预算记号由本文定义。
* $B_{\rm cont}(k)$：以 $\gamma=\gamma_0(M)$ 代入 [GL2024，§2，式(6)–(7)](https://arxiv.org/html/2403.05674v3#S2)所给连续式（本文式(B7)）后，使其严格小于1的最大整数预算。
* $B_{\rm pair}(k)$：满足 $\gamma_0(M)\beta_k<1$ 的最大整数预算，其中
  $$\beta_k=\int_0^1[x(1-x)]^{k-1}dx=\frac{((k-1)!)^2}{(2k-1)!}.$$
  准确排列概率见 [P2009，§2.1，Claim 1及其证明，作者稿第2–3页](https://doi.org/10.1002/rsa.20267)；本文将其写成Beta积分并定义此最大整数预算。
* $L_{\rm GR}(k)$：Goldberg–Russell型的Schönheim覆盖与平衡染色min–max下界，准确公式为引理D.1的式(B5)，出处见 [GL2024，§1，式(3)–(5)](https://arxiv.org/html/2403.05674v3#S1)。

本节的**参考包络**明确取为

$$
\boxed{L_{\rm ref}(k)=\max\bigl\{
B_{\rm RS}(k)+1,\ B_{\rm lin}(k)+1,\ B_{\rm cont}(k)+1,
B_{\rm pair}(k)+1,\ L_{\rm GR}(k)\bigr\}.}
\tag{B2}
$$

这里每个 $B$ 是可染边数预算，下界要再加一；$L_{\rm GR}$ 本身已经是 $m(k)$ 的下界。所有最大值的存在性将在比较中一并得到。

<a id="comparison-theorem-d"></a>

### 定理D：参考包络比较

对每个整数 $k\ge12$，定义D.1的参考包络满足

$$L_{\rm GR}(k)\le2^k,
\qquad L_{\rm ref}(k)=B_{\rm RS}(k)+1.\tag{B3}$$

因此，前文增长增益定理在此范围给出

$$
m(k)\ge L_{\rm ref}(k)+
\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)}\right\rfloor.
\tag{B4}
$$

其中式(B4)的整数增益 $\Delta(k)$ 满足 $\Delta(k)\ge2$。

**证明。** 由引理D.2，$L_{\rm GR}(k)\le2^k$；由引理B.4，$2^k\le B_{\rm RS}(k)$。引理D.3证明其余三个预算均不超过 $B_{\rm RS}(k)$。代入定义D.1的式(B2)，即得(B3)。再由定理C的增长整数增益结论，得到(B4)。∎

**比较范围。** Grill已发表的锁点数值定理适用于 $k=5,\ldots,9$，不提供本节 $k\ge12$ 的另一条完整数值函数。其固定 $v=2k+1$ 的Catalan结论也不能单独加入全超图包络作为同值下界。RS/CK的渐近常数结论，对每个固定 $c<1/\sqrt2$ 在充分大 $k$ 成立；本节用准确有限判据比较，不把未知起点或端点常数冒用为逐 $k$ 数值。

定理E另证明：对 $k\ge256$，一个明确列出测试项目的Grill零锁必要数据松弛方案，不能接受任何 $M>B_{\rm RS}(k)$。这是对该有限测试方案的补充比较，不将全部可能的真实结构推理或多锁扩展混入(B2)。

<a id="comparison-lemma-d1"></a>

### 引理D.1：覆盖与平衡染色下界

设整数 $k\ge2$。对整数 $v\ge2k-1$，置

$$
S_k(v)=\left\lceil\frac vk\left\lceil\frac{v-1}{k-1}\right\rceil\right\rceil,
\qquad
R_k(v)=\frac{\binom vk}
{\binom{\lfloor v/2\rfloor}k+\binom{\lceil v/2\rceil}k}.
$$

则

$$
L_{\rm GR}(k)=\min_{v\in\mathbb Z,\ v\ge2k-1}
\max\{S_k(v),\lceil R_k(v)\rceil\},
\qquad m(k)\ge L_{\rm GR}(k).\tag{B5}
$$

该公式见 [GL2024，式(3)–(5)](https://arxiv.org/html/2403.05674v3#S1)；以下给出其全域形式的证明。

**证明。** 若存在非B超图，在边数不增加的反例中取顶点数最少者。前文的合并点归约保证它覆盖每个点对。因此每点度至少 $\lceil(v-1)/(k-1)\rceil$；按关联总数计数，边数 $m$ 至少为 $S_k(v)$。

在同一 $v$ 点超图上，均匀抽取大小为 $\lfloor v/2\rfloor$ 的红色类。每条指定边单色的概率是 $1/R_k(v)$。非B意味着每份这样的染色都有单色边，所以期望单色边数 $m/R_k(v)\ge1$，即 $m\ge\lceil R_k(v)\rceil$。此处不能在 $R_k(v)$ 为整数时多加一。两种必要条件作用于同一个实际反例，随后取 $v$ 的最小值即得(B5)。$v\le2k-2$ 时可将两色类均取少于 $k$ 点，直接可染，故无遗漏。∎

<a id="comparison-lemma-d2"></a>

### 引理D.2：覆盖与平衡包络的统一上界

若整数 $k\ge12$，则 $L_{\rm GR}(k)\le2^k$。

**证明。** 取

$$q=2^{\lfloor k/2\rfloor},\qquad v=(k-1)q.$$

先证明 $v>4k^2$。两个奇偶起点分别是

$$
(12-1)2^6=704>576=4\cdot12^2,
\qquad
(13-1)2^6=768>676=4\cdot13^2.
$$

令 $F(k)=(k-1)2^{\lfloor k/2\rfloor}/k^2$。对整数 $k\ge12$，

$$
\frac{F(k+2)}{F(k)}
=\frac{2(k+1)k^2}{(k-1)(k+2)^2}>1,
$$

因为分子减分母等于 $k^3-k^2+4>0$。分别从12和13以步长2归纳，便得到全部整数 $k\ge12$ 的 $v>4k^2$；特别地，$v\ge2k-1$ 是式(B5)的合法输入。这一归纳不需要逐个参数枚举。

又有 $\lceil(v-1)/(k-1)\rceil=q$，从而

$$S_k(v)=\left\lceil\frac{(k-1)q^2}k\right\rceil\le q^2\le2^k.\tag{B6}$$

还要上界同一个 $v$ 的 $R_k(v)$。令 $a=\lfloor v/2\rfloor$、$b=\lceil v/2\rceil$。对 $t\in\{a,b\}$ 和 $j=0,\ldots,k-1$，

$$\frac{t-j}{v-j}\ge\frac12\left(1-\frac{2k}v\right).$$

因此单色概率 $P=1/R_k(v)$ 满足

$$
P=\frac{\binom ak+\binom bk}{\binom vk}
\ge2^{1-k}\left(1-\frac{2k}v\right)^k
\ge2^{1-k}\left(1-\frac{2k^2}v\right)>2^{-k}.
$$

这里 Bernoulli 不等式适用，因为 $0<2k/v<1$；最后的严格不等式使用 $v>4k^2$。所以 $R_k(v)<2^k$，且 $\lceil R_k(v)\rceil\le2^k$。与(B6)合用得到(B3)的第一式。这是选择一个 $v$ 上界外层最小值，不是断言所有 $v$ 的max项都不超过 $2^k$。∎

<a id="comparison-lemma-d3"></a>

### 引理D.3：其余参考预算的支配关系

若整数 $k\ge12$，则定义D.1中的三个最大整数预算均存在，并满足

$$B_{\rm pair}(k)\le B_{\rm cont}(k)\le B_{\rm RS}(k),\qquad B_{\rm lin}(k)\le B_{\rm RS}(k).$$

**证明。** [GL2024，§2，式(6)](https://arxiv.org/html/2403.05674v3#S2)的连续上界在本文记作

$$
C_k(M,\gamma)=\int_0^1\min\{Mkx^r,Mk(1-x)^r,\gamma[x(1-x)]^r\}\,dx.
\tag{B7}
$$

对 $x\in[0,1/2]$，第二端点项不小于第一项；坏对项与第一项的比值 $\gamma(1-x)^r/(Mk)$ 随 $x$ 非增。因此两项至多交换一次，允许交换点在端点。令交换位置为 $x=(1-p)/2$ 并积分，得到准确恒等式

$$
C_k(M,\gamma)=\min_{0\le p\le1}
\left\{\kappa(1-p)^k+\frac\gamma{d^2}J_k(p)\right\}.\tag{B8}
$$

对 $\kappa\ge1$、$0\le z\le1$，Bernoulli凸性不等式给

$$1-(1-z)^\kappa\le\kappa z.$$

代入 $z=(1-p)^k$，可见(B1)的失败上界不大于同一 $p$ 的(B8)表达式（取 $\gamma=\gamma_0$）；又 $J_k(p)\le p$ 且 $\gamma_0/d^2\le\kappa^2$，故(B1)也不大于线性判据。于是任何 $M\ge d$ 被连续或线性判据接受，都会被(B1)接受。较小的 $M<d$ 已低于 $B_{\rm RS}\ge2^k$。这证明

$$B_{\rm cont}(k),\ B_{\rm lin}(k)\le B_{\rm RS}(k)\qquad(k\ge12).$$

连续min逐点不大于坏对项，故 $C_k(M,\gamma_0)\le\gamma_0\beta_k$，进而 $B_{\rm pair}\le B_{\rm cont}$。这些集合非空：当 $M=1$ 时，坏对项及连续min均为零；线性判据取 $p=1$ 时等于 $1/d^2<1$。又因每个被接受的整数均不超过有限的 $B_{\rm RS}$，三个集合的最大值均存在。故上述三个预算均有定义，且满足本引理的支配关系。∎

<a id="comparison-definition-d2"></a>

### 定义D.2：零锁必要数据测试方案

固定整数 $k\ge2$、$M\ge1$。定义如下必要数据松弛方案：它遍历整数 $v\ge2k-1$ 及下列有限数据；$S_k(v)\le M$ 已使 $v$ 的范围有限。

选一个标号中心0，给出整数度 $d_0,\ldots,d_{v-1}$、中心共度 $c_i$（$i>0$）和最大共度参数 $r_i$。只保留下述测试均通过的数据：

1. $1\le d_i\le M-1$，$\sum_i d_i=kM$；所有度至少为 $\ell=\lceil(v-1)/(k-1)\rceil$，并有 $S_k(v)\le M$。
2. $1\le c_i\le\min(d_0,d_i)$，$\sum_{i>0}c_i=(k-1)d_0$；$r_0=\max_{i>0}c_i\le d_0$，对 $i>0$ 有 $c_i\le r_i\le d_i$，并有 $r_i\le\max_{j\ne i}d_j$。
3. 对每个 $i>0$，令 $\theta_i=(k-1)d_i-c_i$，要求
   $$v-2\le\theta_i\le\sum_{j>0,\,j\ne i}\min(r_i,r_j),\qquad \sum_{i>0}\theta_i\text{为偶数}.$$
4. 覆盖点对的标量条件 $v(v-1)\le k(k-1)M$。

这些是标量与逐行容量测试，**没有**要求存在一张同时满足全部行和的对称共度矩阵，也没有要求存在实际边族。实际非B输入不能有度为 $M$ 的点，否则将该点染红、其余点染蓝即proper；所以第1项未丢掉非B对象。下文仅在 $r_i=c_i$（$i>0$）的子域构造不通过数据，不把这项等式作为一般原H的必要条件。

对这样的数据，记 $R=\max_i r_i$，使用 [GL2024，§2，第5页式(9)之后的两条未编号不等式](https://arxiv.org/pdf/2403.05674v3#page=5)给出的两条上界

$$
\Gamma_1=M(M-1)-R(R-1),\qquad
\Gamma_2=\sum_i\bigl[d_i(d_i-1)-r_i(r_i-1)\bigr],\qquad
\Gamma=\min(\Gamma_1,\Gamma_2).
$$

测试方案仅在每份保留数据均满足至少一个充分条件时接受 $M$：平衡染色联合上界 $M/R_k(v)$ 严格小于1，或下列离散式严格小于1。后者是 [GL2024，§2，式(8)](https://arxiv.org/html/2403.05674v3#S2)的零锁形式：

$$
\begin{aligned}
D_k(v,M,\gamma)=\frac1v\sum_{h=1}^v\min\biggl\{
&Mk\frac{\binom{h-1}r}{\binom{v-1}r},\quad
Mk\frac{\binom{v-h}r}{\binom{v-1}r},\\
&\gamma\frac{\binom{h-1}r\binom{v-h}r}
{\binom{v-1}r\binom{v-k}r}\biggr\}.
\end{aligned}\tag{B9}
$$

不可能的二项式取零。该方案只比较(B9)、两条指定 $\gamma$ 公式及上述数据测试；不包含实际边族可实现性、edge-critical结构、完整真实共度或任意多锁推理。

<a id="comparison-theorem-e"></a>

### 定理E：指定零锁测试方案的预算限制

对每个整数 $k\ge256$、每个整数 $M>B_{\rm RS}(k)$，存在通过全部上述测试的数据，其平衡联合上界大于1，且 $D_k(v,M,\Gamma)>1$。因此该明确的“全部松弛数据均须通过”方案不能接受任何这样的固定 $M$。

**证明。** 引理E.1构造通过定义D.2全部数据测试的输入，并证明其平衡联合上界大于1以及 $\Gamma\ge\Lambda$。因 $M>B_{\rm RS}(k)\ge2^k$，有 $\kappa=M/2^{k-1}>2$。若 $\kappa\le3k$，引理E.3给出 $D_k(v,M,\Lambda)>1$；若 $\kappa\ge3k$，引理E.4给出相同结论。式(B9)关于第三个参数非减，故 $D_k(v,M,\Gamma)>1$。这份保留输入使两项充分条件均不通过，定义D.2的方案因而不接受 $M$。∎

<a id="comparison-lemma-e1"></a>

### 引理E.1：满足全部数据测试的输入

设整数 $k\ge256$、$M>B_{\rm RS}(k)$。令 $t=\sqrt M$、$T=\lfloor M/k^{16}\rfloor$、$D=M-T$、$v=\lfloor(k-2)t\rfloor$。则存在定义D.2保留的一份数据，其平衡染色联合上界大于1，且存在实数 $\Lambda$ 满足

$$\Gamma\ge\Lambda\ge M^2/2,\qquad \gamma_0(M)-\Lambda\le2MT+4M.$$

**证明。** 按上述记号取

$$
v=\lfloor(k-2)t\rfloor,\qquad n=v-1,\qquad
T=\left\lfloor\frac M{k^{16}}\right\rfloor,\qquad D=M-T.
$$

先记一个全范围余量：对所有实数 $x\ge256$，

$$2^{x/2}>300x^{10}.\tag{B10}$$

因为 $\log(2^{x/2}/x^{10})$ 的导数大于 $1/4-10/256>0$，而在256有 $2^{128}>300\cdot2^{80}$。由 $M>B_{\rm RS}\ge2^k$ 得 $t>300k^{10}$；特别 $T\ge1$ 且 $D<M$。

将 $(k-1)D$ 均分为 $n$ 个尽量相等的整数 $c_i$，将 $kT$ 独立均分为 $n$ 个尽量相等的整数 $b_i$。取

$$d_0=D,\qquad d_i=c_i+b_i\ (i>0),\qquad r_i=c_i\ (i>0),\qquad r_0=R=\max_i c_i.$$

两个均分的向上取整重数分别选择以保持各自精确总和，不要求二者的余数位置相同。总度为

$$D+\sum_{i>0}(c_i+b_i)=D+(k-1)D+kT=kM.$$

以下取整范围用于核全部测试：

$$v\ge\frac k2t,\qquad t\le c_i\le2t,\qquad 0\le b_i\le t/2.\tag{B11}$$

第一式由 $v\ge(k-2)t-1$ 得到。令 $\varepsilon=k^{-16}$。$c_i$的均值大于 $[(k-1)/(k-2)](1-\varepsilon)t$，至少超过 $t$ 达 $t/[2(k-2)]>1$，所以向下取整仍不小于 $t$。另一方面 $n\ge(k-3)t$，故 $c_i\le[(k-1)/(k-3)]t+1\le2t$；同理

$$b_i\le\frac{k}{k-3}\varepsilon t+1\le t/2.$$

这些不等式在 $k\ge256$、$t>300k^{10}$ 下均有严格余量。于是所有非中心度不超过 $5t/2<M$；中心度 $D\ge M/2\ge t$，且 $D<M$。又 $c_i\le2t\le D$，所以中心共度的范围测试通过。

由于 $(v-1)/(k-1)<t-t/(k-1)<t-1$，所有度均不小于 $\ell$；总度等式给 $v\ell\le kM$，故 $S_k(v)\le M$。粗点对覆盖式也由 $v\le(k-2)t$ 直接得到。

普通点的目标共度行和为

$$\theta_i=(k-2)c_i+(k-1)b_i.$$

其下界 $\theta_i\ge(k-2)t\ge v>v-2$。其上界 $\theta_i<3kt$，而

$$\sum_{j>0,\,j\ne i}\min(c_i,c_j)\ge(v-2)t\ge3kt.$$

所以逐行上限也通过。总行和

$$\sum_i\theta_i=(k-1)(k-2)D+k(k-1)T$$

为偶数，因两个系数都是相邻整数之积。普通点的 $r_i$ 在已指定的中心共度 $c_i$ 中达到；中心参数为 $r_0=\max_i c_i$。

令 $P$ 是一条指定边在均匀平衡染色下单色的概率。引理D.2证明中的平衡单色概率乘积估计给

$$MP\ge\kappa\left(1-\frac{2k}v\right)^k
\ge\kappa\left(1-\frac{2k^2}v\right)>1,\tag{B12}$$

因为 $\kappa=M/d\ge2$、$v>4k^2$。因此平衡染色联合界不排除这份数据。这是充分判据的数值不通过，不是实际染色失败概率的下界。

记

$$\Lambda=D(D-1)-R(R-1).$$

两条旧公式满足 $\Gamma_1\ge\Lambda$，而

$$\Gamma_2=\Lambda+\sum_{i>0}\bigl[d_i(d_i-1)-c_i(c_i-1)\bigr]\ge\Lambda.$$

因此 $\Gamma\ge\Lambda$。还由 $R\le2t$ 得

$$
\gamma_0-\Lambda\le2MT+4M,\qquad
\Lambda\ge M^2(1-2k^{-16})-5M\ge M^2/2.
\tag{B13}
$$

以上证明了所构造数据的全部测试条件及断言的两个数值界。∎

<a id="comparison-lemma-e2"></a>

### 引理E.2：离散位置式与连续积分的比较

设整数 $k\ge2$、$v\ge2k-1$、$M\ge1$，实数 $\gamma\ge0$，并令 $r=k-1$、$N=v-2k+3$、$s=N/v$。定义

$$
f(x)=\min\{Mkx^r,Mk(1-x)^r,\gamma[x(1-x)]^r\},\qquad
C=\int_0^1f(x)dx,\qquad L=f(1/2).
$$

则式(B9)所定义的 $D_k$ 满足

$$D_k(v,M,\gamma)\ge s^{2k-1}C-\frac{2s^{2k-2}}vL.$$

**证明。** $f$关于 $1/2$ 对称，在 $[0,1/2]$ 非减，所以总变差至多 $2L$。沿用

$$N=v-2k+3,\qquad s=N/v.$$

在(B9)中只保留 $h=k-1,\ldots,v-k+2$，令 $j=h-k+1$，便有 $j=0,\ldots,N$。两个分子降阶乘的最小因子分别为 $j$、$N-j$；分母降阶乘均至多 $v^r$。端项因此有 $s^r$ 因子、坏对项有 $s^{2r}$ 因子；再用 $s^r\ge s^{2r}$，每个保留位置的最小项至少为 $s^{2r}f(j/N)/v$。

总变差的黎曼和估计给

$$\sum_{j=0}^N f(j/N)\ge NC-2L.$$

于是得到关于实际离散式的代数下界

$$\boxed{D_k(v,M,\gamma)\ge s^{2k-1}C-\frac{2s^{2k-2}}vL.}\tag{B14}$$

这证明了断言，且保留了式(B9)的 $1/v$ 因子及离散位置偏移。∎

<a id="comparison-lemma-e3"></a>

### 引理E.3：中间预算区间的严格下界

在引理E.1的假设和构造下，若 $2\le\kappa=M/2^{k-1}\le3k$，则 $D_k(v,M,\Lambda)>1$。

**证明。** 取 $\gamma=\Lambda$、$q=\Lambda/d^2$，并按引理E.2定义相应的 $f,C,L,s$，即 $C=C_k(M,\Lambda)$、$L=f(1/2)$、$s=(v-2k+3)/v$。由(B8)，

$$C=\min_{0\le p\le1}\{\kappa(1-p)^k+qJ_k(p)\}.$$

括号内的导数为 $(1-p)^r[q(1+p)^r-\kappa k]$。若 $q\ge\kappa k$，最小点是 $p_*=0$，$C=\kappa$。否则，由 $q\ge\kappa^2/2$ 得 $\kappa k/q\le k<2^r$，所以唯一最小点在内部且

$$p_*=(\kappa k/q)^{1/r}-1\le k^{1/(k-1)}-1\le\frac{2\log k}k<\frac12.$$

最后一个非严格比较可由 $e^u-1\le u/(1-u)$ 及 $k/2\ge1+\log k$ 得到。令 $z=(1-p_*)^k$；由 $\log(1-p)\ge-2p$，

$$z\ge k^{-4}.$$

对 $\kappa\ge2$、$0\le z\le1$，

$$h_\kappa(z)=\kappa z-1+(1-z)^\kappa\ge z^2.\tag{B15}$$

$\kappa=2$时等号成立；固定 $z$，令 $u=1-z$，则关于 $\kappa$ 的导数 $z+u^\kappa\log u\ge z+u\log u\ge0$。端点由连续性处理。

记

$$F_0(M,p)=1-a_k(p)^{M/d}+\frac{M(M-1)}{d^2}J_k(p).$$

由 $M>B_{\rm RS}$ 的定义，对同一个 $p_*$ 有 $F_0(M,p_*)\ge1$。因此

$$
\begin{aligned}
C&=F_0(M,p_*)+h_\kappa(z)
-\frac{\gamma_0-\Lambda}{d^2}J_k(p_*)\\
&\ge1+k^{-8}-18k^{-14}-\frac{36k^2}M.
\end{aligned}\tag{B16}
$$

这里用(B13)、$T/M\le k^{-16}$、$J_k\le1$和 $\kappa\le3k$。若 $p_*=0$，$F_0(M,0)=1$、$h_\kappa(1)=\kappa-1\ge1$，故同一较弱估计仍成立。

又 $C\le\kappa\le3k$、$L\le q\le\kappa^2\le9k^2$。由 $1-s^{2k-1}\le(2k-1)(2k-3)/v$，(B14)给

$$D_k(v,M,\Lambda)\ge C-\frac{30k^3}v\ge C-\frac{60k^2}t.$$

结合(B16)及 $M>t$，

$$
D_k(v,M,\Lambda)>1+k^{-8}-18k^{-14}-\frac{96k^2}t>1.
\tag{B17}
$$

最后由(B10)，$96k^2/t<(96/300)k^{-8}$；而 $18k^{-14}=(18/k^6)k^{-8}<(1/3)k^{-8}$，两个损失的和严格小于 $k^{-8}$，故断言成立。∎

<a id="comparison-lemma-e4"></a>

### 引理E.4：大预算区间的严格下界

在引理E.1的假设和构造下，若 $\kappa=M/2^{k-1}\ge3k$，则 $D_k(v,M,\Lambda)>1$。

**证明。** 令 $q=\Lambda/d^2$，并按引理E.2取 $\gamma=\Lambda$，记相应积分与中点值为 $C=C_k(M,\Lambda)$、$L=f(1/2)$。由(B13)，$q\ge\kappa^2/2\ge\kappa k$，由(B8)，函数 $p\mapsto\kappa(1-p)^k+qJ_k(p)$ 的导数为 $(1-p)^r[q(1+p)^r-\kappa k]\ge0$，故其最小值在 $p=0$ 取得，得到 $C=\kappa$。又 $L=\min\{\kappa k,q\}=\kappa k$。直接由(B14)，

$$
\begin{aligned}
D_k(v,M,\Lambda)
&\ge\kappa\left[1-\frac{(2k-1)(2k-3)+2k}v\right]\\
&\ge\kappa\left[1-\frac{4k^2+2k}v\right]
\ge\kappa/2>1.
\end{aligned}
$$

倒数第二步使用 $v\ge(k/2)t$ 与 $t>300k^{10}$。故本区间的严格下界成立。∎

**说明。** 引理E.3所用 $F_0(M,p)\ge1$ 直接来自(B1)的最大值定义，对每个 $M>B_{\rm RS}$ 均成立；不需要另行假设可接受预算集合下闭。

### 本节文献与引用位置

RS–FKG及有向坏对积分来自 [Radhakrishnan–Srinivasan作者稿](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf)§2及Claim 2.4的证明（作者稿第4–7页）、附录A的Claim A.1与式(31)（作者稿第26–27页）。线性判据见 [CK2015，§2，式(2.1)–(2.3)，刊页409–410](https://doi.org/10.1002/rsa.20556)；其渐近结论为Theorem 1。准确排列概率见 [P2009，§2.1，Claim 1及Corollary 1，作者稿第2–3页](https://doi.org/10.1002/rsa.20267)。

(B5)的可读原始陈述见 [Grill–Linzmayer2024式(3)–(5)](https://arxiv.org/html/2403.05674v3)，以及[Aglave等2020](https://arxiv.org/abs/1602.00218)刊页83的Lemma4.3；两者将该方法归于Goldberg–Russell。(B7)、(B9)及两条度/最大共度公式使用同一Grill原文。Goldberg–Russell作者稿的实际正文以四元情形为主，并附局部错误警示，故本节一般公式不以其未核的局部分类为进口；所需全域归约与计算已在正文自含证明。

公共点二分的恰单点交特例已由引理C.1完整证明，本节引用该引理。

原始资料的实际核对及本轮有界检索范围见[最终文献核对记录](context/propertyb-general/round02/final-literature/REPORT.md)。参考包络采用(B2)的明确组成；固定小 $k$ 数表与固定 $v$ 特例仍按其原量词使用。

## 参考文献与核验资料

[RS2000] J. Radhakrishnan and A. Srinivasan. *Improved bounds and algorithms for hypergraph 2-coloring*. Random Structures & Algorithms **16**(1), 4–32, 2000. [作者稿](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf)；[本地PDF](ref/radhakrishnan_srinivasan_2000_two_coloring.pdf)。所引算法、Lemma 2.1、Claims 2.1–2.4、Claim A.1及页码均依27页作者稿，页码不冒作期刊排版页码。

[CK2015] D. D. Cherkashin and J. Kozik. *A note on random greedy coloring of uniform hypergraphs*. Random Structures & Algorithms **47**(3), 407–413, 2015. [DOI](https://doi.org/10.1002/rsa.20556)。本文引用刊版§2式(2.1)–(2.3)，第409–410页。

[P2009] A. Pluhár. *Greedy colorings of uniform hypergraphs*. Random Structures & Algorithms **35**(2), 216–221, 2009. [DOI](https://doi.org/10.1002/rsa.20267)。准确排列概率见§2.1的Claim 1证明，作者稿第2–3页。

[GL2024] K. Grill and D. Linzmayer. *Improved Lower Bounds for Property B*. [arXiv:2403.05674v3](https://arxiv.org/abs/2403.05674v3), 20 June 2024. 本文使用§1式(3)–(5)、§2式(6)–(8)以及式(9)之后两条未编号的单交对上界。

本卷组合的四个规范来源是[一般充分判据](proofs/propertyb-general/CORE_THEOREM.md)、[统一整数加一](proofs/propertyb-general/UNIFORM_INTEGER_GAIN.md)、[团界加强与增长增益](proofs/propertyb-general/CLIQUE_REFINEMENT.md)、[参考界完整比较](proofs/propertyb-general/BASELINE_COMPARISON.md)。它们保持规范地位；本页与[Markdown阅读稿](PROPERTY_B_GENERAL_BOUND.md)提供完整合并阅读。各具体引用、版本和页码的核对记录见[文献定位](context/propertyb-general/formal-exposition-20261021/SOURCE_MAP.md)。

本文全部整数k≥12的增长主定理C已完成[端到端Lean形式证明](PROPERTY_B_GENERAL_LEAN.html)：最大预算、至少二的统一增益、实际反例结构、概率判据和原Bool染色均已连接；[独立原命题及公理审计](context/propertyb-general/bridge-12-16-20261021/lean/VERIFICATION.json)已通过。比较定理D、E仍为本文所给的纸面证明。原[RS核心与17元试点](PROPERTY_B_GENERAL_LEAN_PILOT.html)保留为前一阶段记录。

交接与验证补充：[人工交接](HANDOFF_PROPERTYB_GENERAL.md)、[合并数学审计](context/propertyb-general/round02/formal-audit/COMBINED_AUDIT.md)、[核心审阅处置](context/propertyb-general/round02/reviews/CORE_DISPOSITION.md)、[比较审阅处置](context/propertyb-general/round02/reviews/BASELINE_DISPOSITION.md)。
