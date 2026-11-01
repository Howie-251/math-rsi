## 三类结果：逐项下界、加强判据求值与统一公式

$m(k)$ 是不可二染的有限简单 $k$ 元超图所需的最少边数。从已知精确值 $m(4)=23$ 出发，本项目与合作者的工作在同一参考包络下展示三类结果：$k=5,\ldots,12$ 的逐项具体下界、本文结构加强判据C.2在 $k=12,13$ 的精确求值，以及对**每个整数 $k\ge12$**成立的统一增益定理。逐项结果利用各参数的结构与精确计算证书。**紫色与蓝色来自我们的同一个加强判据：紫色直接选取参数并严格求值，得到指定 $k$ 的更强数值；蓝色通过统一估计，导出适用于所有 $k\ge12$ 的简洁公式。** 该判据在正文编号为[推论C.2](CLIQUE_REFINEMENT.md#clique-corollary-c2)。

<div class="bound-summary"><div><span>逐项具体下界 · k = 5–12</span><strong>35 · 67 · 131 · 267 · 543 · 1112 · 2275 · 4664</strong><small>本项目与合作者的纸面证明／局部精确证书</small></div><div><span>我们的加强判据 · k = 12、13</span><strong>m(12) ≥ 4647 · m(13) ≥ 9564</strong><small>直接求值：增益14、25；严格数值证书</small></div><div><span>我们的统一公式 · 全部 k ≥ 12</span><strong>旧组合基线 ＋ 增长的整数增益</strong><small>同一统一定理已对全部 k≥12完成端到端Lean</small></div></div>

<p class="figure-mobile-hint">左右滑动图像，可查看完整坐标与图例。</p>

### 经典超图二染色问题 Property B $m(k)$｜小参数到一般定理，下界系统提升

<div class="bound-plot bound-delta" data-figure="delta"></div>

**差值主图。** 红色逐项结果、紫色加强判据点与蓝色统一公式使用同一定义的参考包络 $L_{\rm ref}(k)$：取正文已核五项明确参考式，并在 $k=5,\ldots,9$ 加入 GL Theorem 1 的具体下界后取最大值。这是指定参考集的共同包络，不称全部文献的世界最佳。全图共用同一条线性的 $k$ 横轴；红色读左侧线性轴，表示逐项结果的增益 $\Delta_{\rm ind}(k)=L_{\rm ind}(k)-L_{\rm ref}(k)$。$k=5,\ldots,12$ 依次增加3、3、3、4、5、27、30、31；$k=4$ 的零增量只标记既有精确值23。蓝色读右侧对数轴，表示统一定理相对同一包络保证增加的整数下限 $\Delta_{\rm cert}(k)=g_*(k)\le\Delta(k)$。对每个 $k\ge12$，共同包络恰为 $B_{\rm RS}(k)+1$。

**紫色图例“Our refined criterion: certified evaluation”表示我们的加强判据直接求值；蓝色“Our uniform formula (Lean)”表示由同一判据推导的统一公式。** 紫色菱形也读左侧线性轴，给出：$k=12$ 为 $4647-4633=14$，$k=13$ 为 $9564-9539=25$。这些是基于一般充分性证明、经独立数值复算的具体下界，不是新的文献基线，也不称这两项数值已经Lean核验。

在 $k=12$，红色锁点候选为 $4664-4633=31$，紫色直接求值为14，蓝色统一公式保证至少2；三者使用相同基线。$k=13$ 的C.2下界已经超过已核参考包络25；锁点探索尚未超过我们自己的C.2结果，且无成功完整新证书，图中不加入红点。两侧纵轴刻度独立，不能用曲线的视觉高低或交点判断数值反超。[共同基线的完整核验](../../context/propertyb-general/locks-vs-uniform-20261021/baselines/REPORT.md)

|$k$|共同参考包络|统一公式下界（增益）|我们的加强判据求值（增益）|锁点候选下界（增益）|
|---:|---:|---:|---:|---:|
|12|4633|4635（2）|4647（14）|4664（31）|
|13|9539|9542（3）|9564（25）|尚无超过C.2的完整新证书|

C.2接受预算分别为4646与9563，故相应 $m(k)$ 下界再加一。原始严格接受证书及下一预算的全参数排除均已独立复算；本次只将已有数值加入主图。[原始数值报告](../../context/propertyb-general/bridge-12-16-20261021/NUMERIC_REPORT.md) · [独立数值核验](../../context/propertyb-general/bridge-12-16-20261021/INDEPENDENT_NUMERIC_CHECK.md) · [本次绘图数据](../../context/propertyb-general/c2-figure-20261021/plot_c2_data.json)

一般段在 $k=12,13,14,15,16$ 保证至少增加2、3、4、6、9，并在 $k=17,32,64$ 分别保证至少增加13、2,346、152,837,269；这些是保守下限，非精确增量。对每个 $k\ge12$，$B_{\rm RS}(k)+1$ 正是正文所列五项明确参考界的最大值，因此蓝色曲线给出的也是新下界超过这一参考包络的保证增益。蓝线从12连续显示至64，同一解析定理覆盖全部 $k\ge12$；统一定理对全部 $k\ge12$ 已完成端到端Lean形式证明，蓝色实线覆盖相同范围。

### 小参数：逐项提高具体整数

<div class="bound-plot" data-figure="small"></div>

**小参数数值图。** 纵轴除以共同的指数因子 $2^k$，点旁数字仍为原始下界。灰点使用与差值主图相同的 $L_{\rm ref}$，$k=5,\ldots,13$ 依次为32、64、128、263、538、1085、2245、4633、9539。紫色菱形在12、13标出加强判据下界4647、9564；红色空心点保留12的锁点候选4664。前五项来自 [Grill–Linzmayer，Theorem 1，v3第7页](https://arxiv.org/pdf/2403.05674v3#page=7)，后四项为本文精确 RS 组合预算加一；其他参考式不超过这些值的证明与全参数核验证书见共同基线报告。$m(4)=23$ 来自 [Östergård（2014）](https://doi.org/10.1016/j.dam.2011.11.035)。

小参数的证明状态：$m(5)\ge35$ 有完整自然语言候选与局部证书，完整Lean尚未闭合；已完成Lean的五元下界为34。$k=10,11$ 采用合作者证明稿与既有局部证书。[原始材料与完整范围](../../research-wiki/PROPERTY_B_SMALL_K_TRANSFER.md)

六元当前为 $m(6)\ge67$：完整证明覆盖27–44点的全部实际分支，已完成完整参数域核对和独立概率复算，原超图染色接口已经闭合，尚无本参数Lean。[完整证明](../../context/propertyb-m6-67-progress-20261029/PROOF_M6_GE67.md) · [离线阅读页](../../M6_GE67.html) · [独立核验范围](../../context/propertyb-m6-67-progress-20261029/audit/INPUT_MAP.json) · [跨模型审阅范围](../../context/propertyb-m6-67-progress-20261029/reviews/DISPOSITION.md)

八元当前为 $m(8)\ge267$，九元当前为 $m(9)\ge543$。两项均有完整计算机辅助证明，分别覆盖47–120点、57–195点；全部2094型、3450型已由独立参数域重建和不同的下降阶乘注入概率实现复算通过，全部严格小于一。两项尚无本参数Lean，独立计算与跨模型审阅的范围分别记录。[八元证明](../../context/propertyb-m8-267-20261029/PROOF_M8_GE267.md) · [八元独立核验](../../context/propertyb-m8-267-20261029/independent/REVIEW.md) · [九元证明](../../context/propertyb-m9-543-20261029/PROOF_M9_GE543.md) · [九元独立核验](../../context/propertyb-m9-543-20261029/independent/REVIEW.md) · [八／九元完整离线阅读页](../../M8_M9_IMPROVEMENTS.html) · [联合审阅与验收](../../context/propertyb-small-updates-20261029/reviews-8-9/DISPOSITION.md)

七元当前为 $m(7)\ge131$：完整候选的424型及全部2,115,296个共同坏对整数向量已独立复算通过，尚未进行七元跨模型审阅或Lean核验。[七元证明及验证范围](../../context/propertyb-m7-131-20261029/PROOF_M7_GE131.md) · [七元独立复算](../../context/propertyb-m7-131-20261029/independent/RESULTS.json)

十二元当前展示更新为 $m(12)\ge4664$（相对4633增31）。新候选证明覆盖91–782点全部692个必要点数、664355个必要参数实例；独立程序重建完整参数域及全部迹重数／共度，并对20个边界实例用Fraction精确复算通过。独立检查没有第二次全量重算概率值。本次保持完整计算机辅助证明候选、无Lean；Grok已有效静态审阅新覆盖链，未发现实质问题；没有运行程序。[审阅范围与处置](../../context/propertyb-k12-4664-20261029/reviews/DISPOSITION.md)。[当前完整证明](../../context/propertyb-k12-4664-20261029/PROOF_M12_GE4664.md) · [完整计算汇总](../../context/propertyb-k12-4664-20261029/SUMMARY.json) · [独立核验范围](../../context/propertyb-k12-4664-20261029/independent/RESULTS.json)

此前 $m(12)\ge4661$（增28）的691429型证书、31型Fraction边界核验及3348个零／一锁型独立算术检查继续保留，属于旧实例证据，不作为新4664候选的全量第二算术复算。[旧实例阅读页](../../K12_LOCK_COMPARISON.html) · [旧证书报告](../../context/propertyb-general/k12-lock-pilot-20261021/pilot/REPORT.md) · [旧独立核验范围](../../context/propertyb-general/k12-lock-pilot-20261021/independent/REPORT.md)

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

原历史数据不覆盖，见[小参数历史来源](../../context/propertyb-general/bound-figure-20261021/SMALL_K_SOURCES.md)。本次绘图由[共同基线 JSON](../../context/propertyb-general/locks-vs-uniform-20261021/baselines/MATCHED_BASELINES.json)显式覆盖灰点与增益；[2026-10-29更新数据](../../context/propertyb-small-updates-20261029/plot_small_updates.json)更新六、七、八、九、十二元的新值与证明状态，不改参考包络；$k=12$ 的新值读取2026-10-29完整证书汇总，C.2的12、13点从原始数值证书派生并检查独立复算PASS，蓝线保留原统一公式数据。

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

[五点绘图数据](../../context/propertyb-general/bridge-12-16-20261021/bridge_plot_data.json)由保存的精确证书派生，并经独立数值重算。[更强C.2数值表](../../context/propertyb-general/bridge-12-16-20261021/NUMERIC_REPORT.md)列出14、25、45、79、116的直接增益；其中12、13的14与25现以紫色菱形直接展示在主图，与红色逐项结果共读左轴，仍不混入同一统一公式的蓝线。

</details>

### 一般参数：统一增加可核验的整数

差值主图的蓝色曲线展示以下主定理所保证的增益：

$$m(k)\ge B_{\rm RS}(k)+1+\Delta(k),\qquad
\Delta(k)=\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)}\right\rfloor\ge2
\quad(k\ge12).$$

为绘图，对每个显示的整数 $k$ 保存一个严格通过旧判据的预算 $M_*(k)\le B_{\rm RS}(k)$，再取经定向舍入验证的整数 $g_*(k)\le\Delta(k)$。蓝色曲线画 $g_*$，因此它也是相对真正基线 $B_{\rm RS}(k)+1$ 的保证增益；没有把数值寻优冒充最大预算 $B_{\rm RS}$ 的求值。

主定理C与五项参考包络比较的同一解析证明现已延至全部 $k\ge12$：在这整个范围内，新下界超过所列五项明确参考界的最大值。12–16与17起使用同一个增益公式，增长主定理的端到端Lean范围已统一至 $k\ge12$；五项参考包络比较仍为纸面证明，图中具体数值由独立精确程序验证。一般定理的证明不依赖图中有限采样点；这些点只给出可复算的数值展示。[17起的数值见证与验证方法](../../context/propertyb-general/bound-figure-20261021/GENERAL_DATA.md) · [12起的统一解析证明](../../context/propertyb-general/bridge-12-16-20261021/ANALYTIC_EXTENSION.md) · [12起的Lean核验报告](../../context/propertyb-general/bridge-12-16-20261021/lean/REPORT.md)

<details>
<summary>展开：绝对下界总览（对数刻度）</summary>

<div class="bound-plot bound-overview" data-figure="overview"></div>

**绝对值参考图。** 纵轴为 $m(k)$ 的下界。一般段显示 $M_*+1$ 与 $M_*+1+g_*$，即旧判据和新定理的可验取值；新旧总量在此尺度上几乎重合。黑色菱形表示 $m(4)=23$；小参数灰点使用同一共同包络，空心点延至12并包含锁点候选4664；紫色菱形另展示12、13的C.2下界4647、9564，范围及证明状态见上文。一般段从12接起，实线属于同一已形式化的统一定理；箭头表示它继续适用于更大整数参数。

</details>

[下载整组矢量图 PDF](../../figures/propertyb_bounds/propertyb_bounds.pdf) · [差值主图 SVG](../../figures/propertyb_bounds/delta.svg) · [小参数 SVG](../../figures/propertyb_bounds/small.svg) · [绝对值参考 SVG](../../figures/propertyb_bounds/overview.svg)
