# 一般 Property B 正式正文的定点来源核查

核查日期：2026-10-21。范围为正文直接使用的 RS 延迟重染估计、本文最大整数预算的出处边界，以及既有比较函数的具体来源。只读规范证明与原始材料；未修改四份规范证明、renderer 或 Lean，未重跑文献作者的计算。

## 1. 引用版本与页码

**[RS2000]** Jaikumar Radhakrishnan and Aravind Srinivasan, *Improved bounds and algorithms for hypergraph 2-coloring*, Random Structures & Algorithms **16**(1) (2000), 4–32. DOI：[10.1002/(SICI)1098-2418(200001)16:1<4::AID-RSA2>3.0.CO;2-2](https://doi.org/10.1002/%28SICI%291098-2418%28200001%2916%3A1%3C4%3A%3AAID-RSA2%3E3.0.CO%3B2-2)。[Wiley 官方元数据](https://onlinelibrary.wiley.com/doi/10.1002/%28SICI%291098-2418%28200001%2916%3A1%3C4%3A%3AAID-RSA2%3E3.0.CO%3B2-2)核实作者、刊名、卷期、4–32页及2000-01-03首发日期。

实际数学核查依据为[作者站的27页作者稿](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf)，本地文件为 `ref/radhakrishnan_srinivasan_2000_two_coloring.pdf`。下面 RS 页码均指**作者稿自身印出的页码**，也是 PDF 页序，不能写成刊版页码。期刊正式排版为29页，本次未取得其逐页对应；不得将作者稿页数机械加3转换为刊页。

实际读取：作者稿 §2（pp.3–4）、§2.1（pp.5–7）、§2.2（p.8）及 Appendix A（pp.26–27）；核查相邻定义、Lemma/Claim/Equation 编号及其证明。其余章节未作为本次重新全文审计范围。`pdftotext -layout` 能完整显示编号，web PDF 抽取会把部分数字错误编码，因此以本地原PDF提取核编号。

## 2. RS 逐项定位

| 本文使用对象 | 原文准确位置 | 原文层级及使用边界 |
|---|---|---|
| 独立初色、独立均匀实数 delay、Bernoulli(p) 资格位；按 delay 一次处理各点 | §2 “Slow recoloring”，p.4，**The Algorithm**，Phase 1/2 和 Step i | 算法段无 Algorithm 编号。p.5 的 Boppana 简化是另一个表述；本文保留资格位版本。|
| 最终单色边分为初始同色未消除事件 A，以及最后翻转导致的 blame 事件 B | §2.1 “Analysis”，p.5，**Lemma 2.1** | 原文的失败事件覆盖；本文可完整重述。|
| 一条初始单色边保持原色的概率 | §2.1，p.6，**Claim 2.1** | 每一指定颜色为 `2^(−n)(1−p)^n`；并非边之间独立。|
| blame 只可能来自恰交一点的边对 | §2.1，p.6，**Claim 2.2**，并结合 p.5 事件定义 | Claim 2.2 明说交数大于1时概率0；交数0由触发翻转点必须共有而不可能。|
| 实际 blame 事件蕴含只涉及两条边的必要事件 | §2.1，p.6，**Claim 2.3** 及前面的 `E_Blue^1,E_Blue^2, Bhat_Blue` 定义 | 保持“蕴含/上界”的方向，不能把必要条件改说成充分条件。|
| 每个有向单交边对、每个颜色的精确积分上界 | §2.1，**Claim 2.4 的证明**，起于p.6、积分推导在p.7 | p.7 多行推导中保留 `2^(1−2n) p ∫_0^1 (1−p²x²)^(n−1) dx`，随后才用被积函数≤1放宽。该积分式**没有编号**，不能虚称“Eq.(4)”或“Claim 2.4 的原陈述”。Claim 2.4 陈述本身为较粗的 `≤2^(1−2n)p`。|
| 初始残留事件的线性并界 | §2.1，p.7，**Eq.(1)** | 原文设边数 `|E|=λ2^n`，右端为 `2λ(1−p)^n`。|
| 粗二阶总界及粗失败总界 | §2.1，p.7，**Eqs.(2),(3)** | 原文使用 `|E|²` 粗计数且积分≤p；这些编号不直接等同于本文含 J 和 M(M−1) 的组合式。|
| 初始残留事件的 FKG/Jensen 改进 | **Appendix A**, “Exploiting positive correlation”，**Claim A.1**, pp.26–27 | p.26 是 Claim 陈述、**Eq.(31)** 和 FKG 乘积下界；p.27 是 Jensen 及 `E|M(χ₀)|=2λ`。Eq.(31)只是条件平均等式，最终概率上界应引用 Claim A.1，而非单独把(31)当最终定理。|
| 原始渐近/算法定理 | §2.1，p.7，**Theorem 2.1** | 给0.1全n及充分大n的0.7倍 `2^n√(n/ln n)`，不是本文的最大整数预算定义。|

原文短佐证（总计不超过25个英文词）：p.26 为 “**Claim A.1**”；p.27 写 “**the last inequality follows from Jensen's inequality**”；p.7 的精确积分则位于 Claim 2.4 proof 的中间行。[RS 作者稿](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=26)

## 3. B_RS 的准确归属和本文必须证明的内容

在本文记号下，令 `d=2^(k−1)`、`a_k(p)=1−(1−p)^k`、`J_k(p)=∫_0^p(1−y²)^(k−1)dy`。作者稿使用 n 表示均匀度，而其 k 表示归一化边数；引用时必须换名，不能将两个 k 混用。

可直接归属 RS 的两项是：

1. Claim A.1 给初始单色且最终保持原色事件的总上界 `1−a_k(p)^(m/d)`。
2. Claim 2.4 proof 的未编号积分给每个有向单交对、每种颜色的上界 `2^(1−2k)J_k(p)`；两色相加为 `J_k(p)/d²`。[RS2000，§2.1 pp.6–7及Appendix A pp.26–27](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf)

本文将两项用于同一个算法和同一个实际 H，再经 Lemma 2.1 的覆盖及并界得到 `Pr(fail)≤1−a_k(p)^(m/d)+γ(H)J_k(p)/d²`。这是一条由 RS 已给估计直接推出、并在本文重证的组合结论。原文没有把它以本文完整记号编号为一条定理。其真实性来自共同算法和共同事件，不是把不相容算法的最好项拼接。

对简单 m 边超图取实际**有向**单交对数 `γ(H)≤m(m−1)`，继而定义

`B_RS(k)=max { M≥1 integer : ∃p∈[0,1], M(M−1)J_k(p)/d² < a_k(p)^(M/d) }`。

**原文没有名为 B_RS 的量，没有这个最大整数预算的定义，也没有证明这个定义的最大值存在。** 建议正文第一次定义后直接写：“这是本文由 RS2000 §2.1 Claim 2.4 的证明及 Appendix A Claim A.1 组合得到的整数预算，名称和最大化约定由本文定义。”随即给上述定位的直接链接。

必须在本文自证而不能只贴 RS citation 的内容包括：保持精确积分、把原文粗 `|E|²` 替为 `M(M−1)` 的计数；组合后充分判据的原始全超图接口；最大值非空和有限、实际 p 见证存在；`2^k≤B_RS(k)<k2^k`；所有新增 +1 或增长整数增益；新的最小顶点/单交团结构如何应用于同一实际反例。最大值存在性的证明不要求某个连续优化器达到最优值，正文现有整数有限集论证应保留。

## 4. 既有比较函数的定点来源

### Grill–Linzmayer

**[GL2024]** Karl Grill and Daniel Linzmayer, *Improved Lower Bounds for Property B*, [arXiv:2403.05674v3](https://arxiv.org/abs/2403.05674v3)，2024-06-20修订。[v3 PDF](https://arxiv.org/pdf/2403.05674v3)；[v3 HTML](https://arxiv.org/html/2403.05674v3)。本地 `ref/grill_linzmayer_2024_improved_lower_bounds_property_b.pdf`（12页）和 `ref/source_packages/grill_linzmayer_2403_05674/PropB.tex`。arXiv摘要页的“11 pages” comments 不应用来否认PDF实为12页。作者只有两位，TU Wien是机构。

本次实读 §1–2 pp.1–5、§3 结尾Theorem 1 p.7、§4 开头及Theorem 2 p.8；其余锁点证明和作者程序未重新审核。

| 本文比较项 | 原文准确位置 |
|---|---|
| 最小点数反例点对覆盖/Schönheim | §1，p.2，**Eq.(3)**；Goldberg–Russell 归属在式前一段 |
| 平衡染色比值 | §1，p.2，**Eq.(4)** |
| 对v取min、两必要下界取max | §1，p.2，**Eq.(5)** |
| 连续逐点三项min | §2，p.3，**Eq.(6)** |
| 单切点参数式 `2mx^n+γ∫_x^(1−x)u^(n−1)(1−u)^(n−1)du` | §2，p.4，**Eq.(7)** |
| 离散逐位置三项min | §2，p.4，**Eq.(8)** |
| `γ≤m(m−1)−r(r−1)`；`γ≤Σ_i[l_i(l_i−1)−r_i(r_i−1)]` | §2，p.5，在**Eq.(9)之后的两条未编号陈列式** |
| 小k已报告的普遍数值界32、64、128、263、538 | §3结尾，p.7，**Theorem 1**，对应k=5,…,9 |
| Catalan加强 | §4，p.8，**Theorem 2**；量词是固定v=2k+1，不能按原数值直接升级为全超图m(k)界 |

短原文佐证：Eq.(6)后解释γ为 “**ordered pairs of edges that have exactly one vertex in common**”（13词）。[GL2024，§2 p.3](https://arxiv.org/pdf/2403.05674v3#page=3)

正文所用 `L_GR` 可以直接称“GL2024 Eq.(5)所重述的 Goldberg–Russell 型界”，从而不冒称本次直接查阅 Goldberg–Russell 原论文。`C_k` 对应Eq.(6)，`D_k`对应Eq.(8)，但本文 `B_cont`、`B_pair`、`L_ref` 及其最大化/存在性、连续式换元为J的恒等式、所有k尾范围比较仍是本文定义或推导。指定零锁必要数据松弛还包含本文列出的额外标量测试；它不是GL原文的一条同名定理。

### Cherkashin–Kozik

**[CK2015]** Danila D. Cherkashin and Jakub Kozik, *A note on random greedy coloring of uniform hypergraphs*, Random Structures & Algorithms **47**(3) (2015), 407–413，DOI：[10.1002/rsa.20556](https://doi.org/10.1002/rsa.20556)。[Wiley官方元数据](https://onlinelibrary.wiley.com/doi/abs/10.1002/rsa.20556)核作者、卷期页、2014-05-30在线首发；2015是期刊年。[arXiv:1310.1368v1](https://arxiv.org/abs/1310.1368v1)为2013-10-04、6页作者稿；其编号与刊版不能混用。

本次按已存刊版 `ref/general-propertyb/cherkashin_kozik_2015_published.pdf` / `.txt` 读pp.407–410和p.412 Remarks，另比对arXiv开头。刊版公开副本来源：[Saint Petersburg Mathematical Society PDF](https://mathsoc.spb.ru/prize/2022/1.pdf)（本次直接web请求曾超时，但检索可定位，数学正文从既存刊版读取）。

准确刊版位置：Theorem 1及其后常数说明在p.408；Algorithm 1在p.409；§2 “PROPERTY B” proof，p.409 **Eq.(2.1)** 为两端并界，p.410 **Eq.(2.2)** 为中间危险对上界，p.410 **Eq.(2.3)** 为 `κ(1−p)^k+κ²p<1`。p.412 §5 **Remark (1)** 明说(2.3)是RS优化过的同一不等式；Remarks (3),(4)讨论排列与小顶点数的精细分析。

短原文佐证： “**Inequality (2.3) is exactly the inequality optimized in [7].**” [CK2015刊版，p.412](https://mathsoc.spb.ru/prize/2022/1.pdf#page=6)

CK在`2^(k−1)`归一化下允许每个固定常数c<√2、充分大k；改成`2^k`归一化是c/2<1/√2。不能把“充分大”写成某个未证有限起点，也不能把极限常数端点当直接可取。

### Pluhár

**[P2009]** András Pluhár, *Greedy colorings of uniform hypergraphs*, Random Structures & Algorithms **35**(2) (2009), 216–221，DOI：[10.1002/rsa.20267](https://doi.org/10.1002/rsa.20267)。[Wiley官方元数据](https://onlinelibrary.wiley.com/doi/abs/10.1002/rsa.20267)核卷期页及2009-02-10首发。本次定点读本地6页作者稿 `ref/pluhar_2009_greedy_colorings.pdf` §2.1 pp.2–3；未核作者稿与刊版逐页对应，因此不把作者稿p.2误报为刊p.217。

**Claim 1**（pp.2–3）证明中保留指定有向单交对的准确排列概率 `((k−1)!)²/(2k−1)!`，是未编号陈列式；随后作Stirling放宽。**Corollary 1**（p.3）给四次根型下界。本文纯pair预算可以直接引用该Claim的证明，并自行保留准确阶乘概率和整数严格阈值；`B_pair`名称和最大化约定是本文定义。

## 5. 自含结构证明与不额外冒填的来源

CORE中最小点数反例覆盖点对的旧事实已有GL2024 §1 Eq.(3)前的Goldberg–Russell归属；Gram秩界、补图独立集期望/Cauchy的Turán型界，以及CLIQUE中公共点/无公共点分流都在本文给完整短证。可将这些明确陈述为自含的引理，不必捏造历史原文定理编号。

若保留“Deza型”历史名称：M. Deza, *Solution d'un problème de Erdös–Lovász*, Journal of Combinatorial Theory, Series B **16**(2) (1974), 166–167，正确DOI为 [10.1016/0095-8956(74)90059-8](https://doi.org/10.1016/0095-8956%2874%2990059-8)，[Elsevier官方记录](https://www.sciencedirect.com/science/article/pii/0095895674900598)。本次只核官方元数据/摘要；直接正文访问403，未读这两页证明，故**不提供未经核实的定理编号**。正文自含的λ=1特殊情形不依赖这份未读证明。可以保留准确历史文献并说明此处直接证明所需特例，或删除模糊历史命名。

RS作者稿Appendix A引用的FKG原始文献是该稿参考文献[15]：C. M. Fortuin, J. Ginibre, P. N. Kasteleyn, *Correlational inequalities for partially ordered sets*, Communications in Mathematical Physics **22** (1971), 89–103。本次没有读取该原论文；本文只用独立Bernoulli坐标下递增事件正关联，并给归纳证明，因此可靠的直接数学定位是RS Appendix A Claim A.1，不能虚填FKG原论文某定理编号。

## 6. 交付正文的引用用法

正文首个 `B_RS` 定义处应同时有“本文定义”及[RS原稿§2.1 Claim 2.4 proof，p.7；Appendix A Claim A.1，pp.26–27]直接citation。CORE概率引理分别在算法段、blame/积分段、FKG/Jensen段就地引用；BASELINE在每个比较函数定义处引GL/CK/Pluhár准确位置。统一书目可用RS2000、CK2015、GL2024、P2009四个key，但key本身不能代替可点击的直接来源。

不使用“RS原定理B_RS”“RS某编号精确组合公式”“所有已知方法均被压过”等表述。本文最大预算及结构增益是明确组合与新推导，其文献依赖和自证部分如上分别固定。
