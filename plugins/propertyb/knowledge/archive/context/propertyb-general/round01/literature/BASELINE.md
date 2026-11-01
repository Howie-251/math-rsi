# 一般 Property B 下界：原始来源与可用比较基线

核对日期：2026-10-21。执行范围：新一般 k 研究的文献基线；旧 36 与 35 Lean 保持暂停。本文件不宣称世界文献穷尽，不将已有本地小 k 候选升级为正式验收结果。

## 1. 直接结论

1. 不能只把 CK 的简化式当作比较界。RS2000 已经给出更强的一阶 FKG/Jensen 联合估计，以及尚未舍去的精确二阶积分；Grill–Linzmayer2024 已经保留实际有向单交边对数、M(M−1)、连续逐点 min、离散逐位置 min、实际度数/共度扣除和至多三锁。它们均属于既有来源链。
2. 已核的渐近常数不是只有 0.7：RS 原稿 p.7 与 CK2013/2015 均证明，任意固定 c<1/√2，充分大 k 时，至多 c·2^k√(k/ln k) 边均可染。等价地，liminf m(k)/(2^k√(k/ln k))≥1/√2。没有给出可直接用于任意具体 k 的统一 k₀。不能把 c=1/√2 的逐 k 非严格命题当成已有定理。
3. Grill2024 原始 Theorem 1 的无条件数值为 k=5,…,9 时 32,64,128,263,538；项目已验 m(5)≥34，高于其五元值。合作者 k=6,…,11 的 65,130,266,542,1112,2275 属于此前本地材料/重放层级，本次没有重新验算或升格。
4. 对 root 新提出的“最小顶点反例点对覆盖 + 单交图 clique 的 Gram 秩界 + Turán”统一 γ 上界：在本次实读的 RS2000 相关证明、Pluhár2009、Aglave2020 §4、Grill2024 §1–3、Ferber–Shapira2019 及 Blázsik–Lemons arXiv2406.12118 全文中，没有找到此应用或等价公式。这是有边界的未发现记录，不能据此宣称首创。Gram clique≤v 自身是标准等交集/Fisher 型线性代数事实。

## 2. 记号与整数约定

k≥2；H 为任意有限简单 k 元超图，M=|E(H)|；γ(H) 是**有向**、不同边的恰单点相交对数。无向对数为 γ/2。令

κ=M/2^(k−1),

J_k(p)=p∫₀¹(1−p²t²)^(k−1)dt
=Σ_{j=0}^{k−1}(−1)^j C(k−1,j)p^(2j+1)/(2j+1),  0≤p≤1.

凡证明“实际边数 M≤B 的 H 均可染”，所得整数结论是 m(k)≥B+1。凡仅得到 m(k)≥实数 R，整数化为 m(k)≥ceil(R)；不能自动加一。严格充分条件 P<1 在 P=1 时不提供结论。

## 3. RS2000：必须纳入的有限充分判据

来源：Jaikumar Radhakrishnan, Aravind Srinivasan, *Improved bounds and algorithms for hypergraph 2-coloring*, Random Structures & Algorithms 16(1) (2000), 4–32。原始作者稿本地 [PDF](../../../../ref/radhakrishnan_srinivasan_2000_two_coloring.pdf)，本次提取 [全文文本](RS2000_FULLTEXT.txt)；作者站同版 [PDF](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf)。本地为 27 页作者稿，不等同期刊排版页码。

### 3.1 正文线性判据

原稿 p.7 式(3)用 a=M/2^k，写作

Pr(fail)≤2a(1−p)^k+4a²p
=κ(1−p)^k+κ²p.

任意 p∈[0,1] 使右端<1 即可染。它适用于每个 k≥2，不是仅渐近式。

原稿 p.7 还明确给出：(i) 每个 k≥2，至多 (1/10)·2^k√(k/ln k) 边均可染；(ii) 每个固定 ε>0，充分大 k 时可将 1/10 换成 (1−ε)/√2。Theorem 2.1 为算法形式；0.7 只是一个便于陈述的常数。

### 3.2 附录的更强第一项

原稿 p.7 Remark 及 pp.26–27 Appendix Claim A.1 给出

Pr(存在初始单色且一直未修复的边)
≤1−[1−(1−p)^k]^κ.

完整论证：条件于初始染色，针对所有初始单色边，事件“该边至少有一个可重染点”在独立 Bernoulli 变量中正相关（FKG）；然后对初始单色边数使用 Jensen，其期望为 κ。指数 κ 不要求整数。

因此一个已有充分判据为

**RS-FKG:** 1−[1−(1−p)^k]^κ+κ²p<1.

当 κ≥1 时，第一项≤κ(1−p)^k，且通常严格小；κ<1 时不要声称它强于线性项，可取两界的最小值。

### 3.3 正文没有立即舍去的精确积分

原稿 p.6 Claim 2.4 的计算先得到：每个实际有向单交对、指定新单色方向，blame 事件概率

≤2^(1−2k)·J_k(p),

随后才用 J_k(p)≤p 得到简化。对两种颜色、γ 个实际有向单交对求和得

Pr(产生新单色边)≤γ·4^(1−k)J_k(p).

于是以下是**本次把原文已证不等式合在一起写出的直接推论**，不是新方法：

**RS-FKG-exact:**

1−[1−(1−p)^k]^κ+γ·4^(1−k)J_k(p)<1.

无条件可代 γ≤M(M−1)。为避免丢掉既有能力，比较新的普遍 γ 上界时至少应对比这个版本；也可对第一项同时保留线性界取 min。

精确判定提示：若 p 为有理数，J_k(p) 为有理数。写 κ=M/d，d=2^(k−1)，以及 Q=γ·4^(1−k)J_k(p)。对 0<Q<1，条件等价于 Q^d<[1−(1−p)^k]^M，可化为整数比较；大 k 时更适合严格区间对数，不要求构造巨大整数。这只是复现建议，本次未执行数值扫描。

## 4. Cherkashin–Kozik2013/2015：版本和渐近常数

来源：Danila D. Cherkashin, Jakub Kozik, *A note on random greedy coloring of uniform hypergraphs*, Random Structures & Algorithms 47(3) (2015), 407–413，DOI [10.1002/rsa.20556](https://doi.org/10.1002/rsa.20556)。期刊在线首发为 2014-05-30；arXiv v1 日期 2013-10-04。

- 旧本地六页 [arXiv PDF](../../../../ref/cherkashin_kozik_2015_random_greedy.pdf) 对应 [1310.1368v1](https://arxiv.org/abs/1310.1368v1)，已有 [全文提取](../../../general-method-discussion-20261021/CK2013_FULLTEXT.txt)。
- 本次新增七页期刊排版 [PDF](../../../../ref/general-propertyb/cherkashin_kozik_2015_published.pdf)，来源 [数学学会公开原文](https://www.mathsoc.spb.ru/prize/2022/1.pdf)，[提取文本](../../../../ref/general-propertyb/cherkashin_kozik_2015_published.txt)。本次重点核期刊 pp.407、409–410、412；其余内容没有作为全篇重新审计。

期刊 p.410 式(2.3)为 κ(1−p)^k+κ²p<1。令 κ_k=c√(k/ln k)、p_k=ln(k/κ_k)/k，左端极限为 c²/2，故每个 c<√2、充分大 k，至多 c·2^(k−1)√(k/ln k) 边均可染。归一化到 2^k 的常数为 c/2<1/√2。

期刊 p.412 Remark(1)明确说这个有限不等式正是 RS 优化的式子；Remark(3)说明只依赖均匀排列；Remark(4)指出小顶点数精细排列分析可以更好。不能把连续时间改写为随机排列本身当作新贡献。

## 5. Grill–Linzmayer2024：明确强于简化 CK 的比较项

来源：Karl Grill, Daniel Linzmayer, *Improved Lower Bounds for Property B*, [arXiv:2403.05674v3](https://arxiv.org/html/2403.05674v3)，修订 2024-06-20。作者只有这两位，TU Wien 是机构，不是第三作者。本地 [PDF](../../../../ref/grill_linzmayer_2024_improved_lower_bounds_property_b.pdf) 与 [原始 TeX](../../../../ref/source_packages/grill_linzmayer_2403_05674/PropB.tex)。本次直接读 TeX §1–3、§4 定理及结论；没有重跑作者计算。

### 5.1 旧连续精确界

式(6)为

C_k(M,γ)=∫₀¹min{Mkx^(k−1),Mk(1−x)^(k−1),γx^(k−1)(1−x)^(k−1)}dx.

C_k(M,γ)<1 ⇒ 可染。式(7)等价地对 x∈[0,1/2] 优化

2Mx^k+γ∫_x^(1−x)u^(k−1)(1−u)^(k−1)du.

原文明确 γ≤M(M−1)。中央积分及 M(M−1) 修正已经在这篇原文中直接出现。

### 5.2 旧离散精确界

对 v≥2k−1，式(8)可按位置 h=1,…,v 写成

D_k(v,M,γ)=Σ_h (1/v) min{
Mk C(h−1,k−1)/C(v−1,k−1),
Mk C(v−h,k−1)/C(v−1,k−1),
γ C(h−1,k−1)C(v−h,k−1)/[C(v−1,k−1)C(v−k,k−1)]}.

不可能的二项式按0；原文位置从0写起，在 h=0 为0，使用1…v可避免负上标。D<1⇒该 v 的超图可染。

式(3)–(5)给已有全域覆盖：最小顶点反例点对覆盖，故

S_k(v)=ceil((v/k)·ceil((v−1)/(k−1)))≤M；

以及平衡染色排除条件

M·[C(floor(v/2),k)+C(ceil(v/2),k)]/C(v,k)<1.

因此使用离散界时，不可挑一个 v 证明后宣称全超图下界；须对所有未被 S_k(v)>M 或平衡界排除的 v 覆盖。简单覆盖已给有限上限 v(v−1)≤k(k−1)M。v≤2k−2 可直接平衡染色。

### 5.3 已有共度扣除

§2明确列出：若一对点共同出现于 r 条边，则 γ≤M(M−1)−r(r−1)；若 d_i 是点度，r_i=max_{j≠i}λ_ij，则

γ≤Σ_i[d_i(d_i−1)−r_i(r_i−1)].

此外 §3引入一、二、三锁和真实出现型。未找到其使用单交图 clique≤v 或 Turán 的公式。

### 5.4 已发表数值和固定顶点特例

| k | Goldberg–Russell（其Table1） | 连续 CK 类（Table1） | 零锁离散（Table1） | Theorem1 |
|---:|---:|---:|---:|---:|
|5|28|27（Aglave加强29）|30|32|
|6|51|57|62|64|
|7|94|119|126|128|
|8|174|248|259|263|
|9|328|516|533|538|

这些是 m(k) 下界，色边预算比表中数字少1。Table1的“连续CK类”使用作者所描述的精确连续程序，不应标成只优化 κ(1−p)^k+κ²p 的数值。

Theorem2仅为 v=2k+1：k=2^a−2,a≥3 时 m(k,2k+1)≥(C_{k+1}+3)/2；k=2^r(2^(2a)+1)−2,r,a≥1 时 m(k,2k+1)≥C_{k+1}/2+3。这里 C_j 为 Catalan数。不能直接当作 m(k) 的全域同值下界。

## 6. 其他已核原始材料和后续范围

| 来源 | 本次实际阅读范围 | 对本轮比较的含义 |
|---|---|---|
|Pluhár2009，*Greedy colorings of uniform hypergraphs*，RSA35,216–221，DOI10.1002/rsa.20267；[本地PDF](../../../../ref/pluhar_2009_greedy_colorings.pdf)，[提取](PLUHAR2009_FULLTEXT.txt)|§1–2与相关结论，非重新审计全部局部引理|实际有向单交对发生率 ((k−1)!)²/(2k−1)!，以及 M(M−1) 计数早已出现。Corollary1给 m(k)>2^(−1/2)π^(−1/4)e^(−1/(12k))k^(1/4)2^k；本基线直接保留准确阶乘概率，不依赖其十进制简化。连续min保留纯二阶项已涵盖此能力。|
|Aglave–Amarnath–Shannigrahi–Singh2020，*Improved bounds for uniform hypergraphs without Property B*，Australas. J. Comb.76(1),73–86，[arXiv1602.00218](https://arxiv.org/abs/1602.00218)，[本地PDF](../../../../ref/aglave_et_al_2020_improved_bounds.pdf)，[提取](AGLAVE2020_FULLTEXT.txt)|§4全文（刊页83–84），引言背景；构造章节仅检索|Lemma4.4已显式保留 J_k(p) 和无向单交对数γ_u（系数4γ_u·2^(1−2k)）。其 m(5)≥29 用v=23真实度谱扣除，无向对≤335/334；无Turán/Gram。|
|Ferber–Shapira2019/2020，*A quantitative Lovász criterion for Property B*，CPC29,956–960，[arXiv1903.04968](https://arxiv.org/html/1903.04968v1)，[本地PDF](../../../../ref/ferber_shapira_2019_quantitative_lovasz.pdf)|原文§1与Proposition1.1证明，全文针对关键词检索|非B必有 γ≥k C(2k−1,k)；等号强迫含完整 K_{2k−1}^{(k)}。这是下界/等号结构，不是root候选的全域γ上界。|
|Cherkashin2023，*On small non-uniform hypergraphs without property B*，[arXiv2303.03803](https://arxiv.org/abs/2303.03803)，[本地PDF](../../../../ref/cherkashin_2023_small_nonuniform.pdf)|全文5页|主要新贡献为非均匀总权重q(k)的上界改进；不能转写成一般均匀 m(k) 下界改进。原文引言仍列RS/CK量级。|
|Blázsik–Lemons，*The connection between the chromatic numbers of a hypergraph and its 1-intersection graph*，[arXiv2406.12118v1全文](https://arxiv.org/html/2406.12118v1)，期刊Discrete Mathematics349(2)(2026),114810，DOI10.1016/j.disc.2025.114810|arXiv HTML全文（含§2、§3）；期刊PDF下载TLS失败，未读期刊排版|证明1-intersection graph为二分图时H可二染，及四染推广；全文未见Gram/Turán计数上界。不是给出新的普遍m(k)数值函数。|
|Grill–Linzmayer2026，*An Overview of Property B*，Sum(m)it280,BSMS32,173–181，DOI[10.1007/978-3-032-18810-6_9](https://link.springer.com/chapter/10.1007/978-3-032-18810-6_9)|只读公开元数据、摘要、参考文献；全文付费，未读数表|引用链包含Grill2024、RS、CK等；不能将摘要当作新的数值基线或证明其没有新内容。|
|Ryn–Kozik2026，*Property B for random non-uniform hypergraphs*，[arXiv2610.07379v1](https://arxiv.org/html/2610.07379v1)|§1–§3定理陈述；后续算法证明未读|固定有限edge-size profile后，顶点数→∞的随机模型a.a.s.结论；不覆盖任意H，不替代本Goal的m(k)下界。|

Schmidt1964的历史有限界在不同二级来源出现 n/(n+4)·2^n 与 (1−2/n)·2^n 两种写法。本次未读Schmidt两页原文，因此不将某个写法纳入正式已核基线。Pluhár上述显式界/连续min在本研究相关k范围已提供可直接读取的更强比较工具；若最终新定理选择其可能活跃的小k范围，仍应核原文，不能凭二级转述加一。

## 7. 建议采用的比较包络

对候选整数范围 K，至少同时维护两条数值包络：

**公开原始已核包络** L_pub(k)：取已知精确小k值（m(2)=3,m(3)=7,m(4)=23）、Grill Theorem1在5…9的数值、Goldberg–Russell式(5)、Grill连续/离散及适用锁点结论、RS-FKG-exact所推出的最大整数结论之最大值。对于较大k，渐近常数只用于渐近比较；未核k₀时不得将其硬当某个有限值。

**本地材料包络** L_local(k)：额外记录已验m(5)≥34，以及合作者k6…11的65,130,266,542,1112,2275；后六者保留原证据层级。新工作若只超越公开包络但未超本地候选，应如实说明。旧m(5)≥35纸面候选及未完成36不混入已验基线。

“取全部现有公式的最大值”目前是**定义与复现要求**，不是本次已经算出所有k的函数表。特别是Grill锁点部分只报告5…9，不存在本次已核的任意k锁点数表。root选定K后，应在该范围实际比较活跃项，才可宣称新整数下界。

## 8. root新候选的定点检索结果

候选：最小顶点非B输入给v(v−1)≤k(k−1)M；单交图任意clique的关联Gram=(k−1)I+J，从而clique≤v；Turán给γ≤(1−1/v)M²，进一步代v≤V(k,M)，也可保留精确平衡Turán数。

本次在上述实读原文中逐项检索并核查相邻证明，未见此串联。Aglave与Grill的已列γ加强是**局部度/共度**型，可能在某些小k更强，所以新定理应允许与它们取min，不能宣称新γ界逐输入都优于旧局部门。RS §2.2还研究“很少单交对”的算法改进，但没有本候选的普遍γ上界。

全域新γ上界如果成立，对“RS-FKG-exact + M(M−1)”的实数阈值能严格改善，不等于已经超越更强的离散/锁点整数包络；需要root当前正在做的统一范围/取整比较。候选不改渐近领先常数本身不影响其作为新有限统一改进的价值。

## 9. 检索覆盖收据

已固定、已处理主ID：RS2000作者原稿/DOI；1310.1368v1与期刊10.1002/rsa.20556；2403.05674v3；1602.00218/2020期刊§4；1903.04968v1；Pluhár2009；2303.03803；2406.12118v1。有限范围处理：2610.07379v1只读引言与定理；2026综述只读公开元数据/摘要/参考。

外部检索：2026-10-21以Property B/m(k)/lower bounds/RS常数/单交图/Turán/Fisher/Gram关键词检索；ARIS arxiv_fetch.py执行search '"property B"' --max15成功，结果包括2403.05674、1903.04968、2610.07379、2303.03803等。未使用Zotero/Obsidian（当前无可调用工具）；直接复用项目ref原文，不重复下载现有材料。

未完成/仍需核：2026综述全文；Schmidt1964原文及其严格号归属；候选K中的最强整数包络实际计算；更广泛的等交图极值文献中是否早有root串联公式。本次没有新超图枚举、小k 103190型重放、Lean或MCP reviewer。

### round02补充的有限网页查询

2026-10-21，root另以Turán、Gram、Property B 2026相关题词作补充网页查询，未发现直接给出当前串联方法的新来源；结果主要不相关，或属于已经识别的随机非均匀Property B研究。此项为root本轮有限查询的记录，不是本文整理者新执行的检索。精确query/URL清单与新增全文阅读收据未交本整理子任务，故不补造，也不据此宣称文献穷尽或候选首创。范围说明见[补充查询记录](../../round02/recovery/FRESH_SEARCH_NOTE.md)。原有未核全文与强基线比较义务保留。
