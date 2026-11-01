# 非单位边交图：有界原始文献核查

日期：2026-10-20；检索开始约05:29 UTC，成稿约05:32 UTC。执行 `research-lit` 的定向原文核查；6个检索式，未开泛综述或模型评阅。研究判断为 same-family / provisional。本报告不改变项目已验收下界或任何分支状态。

**结论：** 本次找到一篇本地19篇索引未列的直接相关原论文：Blázsik–Lemons 的单交图二分充分条件。它不覆盖“存在一条原边的非单位交度≤2”的新条件。本次核到的原始来源没有可直接排除全部21–25点35边原输入的新定理、勘误或反例；有限检索没有证明这类结果不存在，也不足以判定新引理的文献优先权。Grill–Linzmayer 当前 arXiv 版本记录仍止于v3，其实际 Theorem 1 仍为 m(5)≥32。

## 1. 先核的本地对象

已读 `research-wiki/query_pack.md`、相关 paper 节点（尤其 Ferber–Shapira、Grill–Linzmayer）、`proofs/propertyb35/TWENTYONE_TWENTYTWO_MINIMUM_NONUNIT_DEGREE_THREE.md` 及 `middle/eight_red_foursets_seventeen_20261020/PROOF.md`。

这里 Γ 的顶点是35条实际原边，不同边相邻 iff 交数≠1。令 G₁=H^[1] 为交数恰1的图，则两者是同一35点集上的简单补图。切勿与“普通非空交图”、原顶点度或共度混同。

## 2. 已定位的原始结果与准确适用差异

| 原论文、实际读取范围 | 核到的结果 | 对本项目的适用差异 |
|---|---|---|
| Zoltán L. Blázsik, Nathan W. Lemons, *The connection between the chromatic numbers of a hypergraph and its 1-intersection graph*, arXiv:2406.12118v1 (2024)。PDF pp.1–6与对应HTML，重点pp.2–4。 | Theorem 1.4（p.2）：对边大小至少2的任意超图，χ(G₁)=2 ⇒ χ(H)=2。无均匀度、点数、paircover、原点度前提。Theorem 1.5仅给χ(G₁)=4 ⇒ χ(H)≤4。 | 二分条件必须对**整个G₁**成立；Γ中某个点度≤2只使该点在G₁度≥32，并不推出G₁二分。后一个四染结果不保证Property B。没有核到本任务同款的非单位交图最小度必要条件。 |
| Asaf Ferber, Asaf Shapira, *A quantitative Lovász criterion for Property B*, arXiv:1903.04968v1 (2019)。本轮重读PDF pp.1–2定理与算法，既有wiki已记全文阅读。 | Proposition 1.1（p.1）：不可二染的k一致超图，其**有序**单交边对数m₂≥k C(2k−1,k)。Theorem 1（p.2）：等号迫含K^(k)_(2k−1)。 | k=5、35边时无126边的K⁵₉，故m₂>630，偶数性给m₂≥632。约束单交对**总数**，不控制每条原边的Γ度；不含21–25点的小点数修复。 |
| András Gyárfás, Alexander W. N. Riasanovsky, Melissa U. Sherman-Bennett, *Chromatic Ramsey number of acyclic hypergraphs*, arXiv:1509.00551（2015预印本；论文列2017年期刊）。本轮读PDF p.6定义/Thm13、pp.7–9相关证明段。 | Theorem 13（印刷p.6）：若H是**3一致**且χ(G₁)≥2，则χ(H)≤χ(G₁)。后续证明利用无单交三元分量的特殊分类和图骨架。 | 不能把3一致删掉后套五元H，也不能任意每条五边取一个三子集后认为G₁结构保持。Blázsik–Lemons才给一般边长的二分特例。 |
| Karl Grill, Daniel Linzmayer, *Improved Lower Bounds for Property B*, arXiv:2403.05674v3 (2024)。本轮核官方版本页、PDF p.7 Theorem 1及pp.4–6方法段；本地旧全文笔记未重做。 | Theorem 1（p.7）：m(5)≥32，另给m(6)≥64、m(7)≥128、m(8)≥263、m(9)≥538。官方版本历史仅v1 (3月8日)、v2 (3月20日)、v3 (6月20日)。 | m(5)≥32只排除≤31边；不是≤35边定理。本次未核到此文2024后新版或已发表更强五元界。 |

原始链接：

- [Blázsik–Lemons PDF v1](https://arxiv.org/pdf/2406.12118v1)，[官方版本页](https://arxiv.org/abs/2406.12118)。PDF第一页日期June 19, 2024；HTML当前生成页的2026日期不作为论文新版证据。
- [Ferber–Shapira PDF](https://arxiv.org/pdf/1903.04968)。
- [Gyárfás–Riasanovsky–Sherman-Bennett PDF](https://arxiv.org/pdf/1509.00551)。
- [Grill–Linzmayer PDF v3](https://arxiv.org/pdf/2403.05674v3)，[官方版本历史](https://arxiv.org/abs/2403.05674)。

## 3. 能立即复用的精确判断

以下是本报告的直接推论，不冒充原论文原句。

对于35边不可染五元H，由Ferber–Shapira有 |E(G₁)|≥316。因此单交图二分判据单独不会给当前假设反例再添约束：35点二分图至多⌊35²/4⌋=306边，而非二分性已被这个总数下界蕴含。更强地，由Mantel的基本计数判据，G₁必有三角形。

补图恒等式为

    m₂(H)=35·34−2|E(Γ)|=1190−2|E(Γ)|。

因此Ferber–Shapira给 |E(Γ)|≤279。若root的新21/22点定理最终验收，则δ(Γ)≥3又给 |E(Γ)|≥ceil(35·3/2)=53。两者合并只是

    53≤|E(Γ)|≤279，

没有数值矛盾，不能据此闭合全21/22分支。

Blázsik–Lemons pp.3–4的有限重染过程有一个可借鉴接口：从H删一条边的合法染色出发，每次只翻转一次尚未翻转的顶点；新产生的反色单色边与正在修的单色边恰交一点。全局二分性使两种单色风险固定落在G₁的两侧，阻止队列重复和耗尽。若希望转为本项目的**局部**修复，仍必须重新证明对应不变量和终止，不能把“新坏边沿单交传播”本身当作终止证明。其Lemma 2.1是这一两侧不变量，并非额外的无条件删边延伸定理。

八红17点引理是带方向、带精确颜色配额的双族约束：A族只禁全红，B族只禁全蓝，且要求10红7蓝。上述原文的普通Property B结论既无该配额也无这种正负分工，不能直接替代它。已读来源中没有找到与这份有限引理完全相同的陈述；此项不构成查新认证。

## 4. 查询、覆盖与未验证项

共6个网页检索式（其后只打开结果和原文，无额外搜索）：

1. `hypergraph property B "intersection graph" "one" Lovasz`
2. `"Property B" "non-singleton" intersection`
3. `"m(5)" "Property B" 2025 2026`
4. `"2403.05674"`
5. `"property B" "intersection" "minimum degree" hypergraph`
6. `"m(5)" "Grill" lower bound property B`

本轮正文使用的4篇原论文均已取得可读原文；读取深度如表。未独立审计它们全部证明或全部有限计算，未读取Lovász书的原始Exercise 13.33，也未核期刊最终版与预印本的逐字差异。新发现论文的刊物数据库条目只作定位，没有据它扩张定理范围。

检索出现的AI working report、GitHub问题、二手综述/镜像及LLM式摘要均未作为定理或当前最优界来源。一个二手结果把arXiv:2610.11642描述为随机超图Property B；实际打开官方arXiv题名却是 *A counterexample to the Erdős--Sós bipartite-link conjecture*，故排除该不匹配条目。

六次有界检索没有定位2024后的、可由本轮原文验证的m(5)数值下界更新；这里只能报告“未定位”，不能宣称公开下界已被完整查尽、没有勘误，或没人证明过类似Γ最小度命题。没有运行Lean，没有枚举原H，没有访问编码理论项目，没有修改wiki/nav/主稿。
