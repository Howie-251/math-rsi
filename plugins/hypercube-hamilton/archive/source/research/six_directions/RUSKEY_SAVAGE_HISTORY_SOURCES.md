# Ruskey–Savage 猜想：历史、结果边界与来源核查

核查日期：2026-11-02。本文是文献说明，不替代本项目的证明审计，也不主张结果首次出现于本项目。正文以原论文、作者存档与出版商记录为依据；无法读取原文的新线索单列。

## 1. 猜想说什么、何时提出、为什么值得研究

令超立方体图 $Q_n$ 的顶点为所有 $n$ 位二进制串，两点恰在一位不同才相邻。匹配 $M$ 是两两不共端点的边集。Ruskey–Savage 猜想断言：对每个 $n\ge2$，每个 $M\subseteq E(Q_n)$ 都包含在某个 Hamilton 圈中。这里“扩张”要求保留全部指定边，并由一个圈恰好遍历全部 $2^n$ 个顶点。

问题通常追溯到 Frank Ruskey、Carla Savage 于 **1993 年**发表的 *Hamilton Cycles that Extend Transposition Matchings in Cayley Graphs of $S_n$*，*SIAM Journal on Discrete Mathematics* **6(1):152–166**，DOI **10.1137/0406012**。出版商标示卷期为 February 1993；页面另列的 2012 年上线时间不是猜想提出年份。[出版商原始书目](https://epubs.siam.org/doi/10.1137/0406012)；[后续论文中明确的猜想表述，Conjecture 1](https://arxiv.org/pdf/2501.19029v1)。

其意义在于研究“局部预先指定的边”能否组织成“全局的一次遍历”。超立方体上的 Hamilton 圈对应循环二进制 Gray 码，因此问题也可以看作带指定相邻关系的 Gray 码构造。普通 Hamilton 性不能自动保证保留任意匹配；完美匹配的结论也不能直接覆盖全部匹配，因为一般匹配未必可补成超立方体内的完美匹配。[Fink–Hotmar 引言](https://arxiv.org/pdf/2501.19029v1)；[Fink–Mütze 原文](https://arxiv.org/html/2401.01769v2)。

## 2. 主要已核实进展

| 年份与原始文献 | 已证明范围 | 不应扩大成什么 |
|---|---|---|
| **2007**，Jiří Fink，*Perfect matchings extend to Hamilton cycles in hypercubes*，JCTB **97(6):1074–1076** | 每个完美匹配可扩张为 Hamilton 圈，解决 Kreweras 猜想 | 不等于任意匹配情形 |
| **2013 预印本／2014 期刊**，Fan Wang、Heping Zhang，*Prescribed matchings extend to Hamiltonian cycles in hypercubes with faulty edges*，Discrete Mathematics **321:35–44** | 对 $n\ge2$，$|M|\le2n-1$ 足够 | 该线性大小界不是目前全部进展的最终上界 |
| **2019 卷期**，Jiří Fink，*Matchings Extend into 2-Factors in Hypercubes*，Combinatorica **39:77–84** | 任意匹配可扩张为 2-factor，即若干互不相交的圈覆盖全部顶点 | 不保证这些圈能合成一个圈 |
| **2024 预印本／2025 期刊**，Jiří Fink、Torsten Mütze，*Matchings in Hypercubes Extend to Long Cycles*，SIAM JDM **39(3):1826–1854** | 任意匹配可扩张为一个至少覆盖 $(2/3)2^n$ 个顶点的圈 | 不保证覆盖全部顶点 |
| **2025 预印本／2026 正式会议章**，Jiří Fink、Vojtěch Hotmar，五方向论文 | 任意维数中，使用至多五个坐标方向的匹配可扩张为 Hamilton 圈；另给出指定端点路径分类 | 圈扩张和完整端点分类的提升前提不同 |

对应一手来源：[Fink 2007 作者 PDF](https://kam.mff.cuni.cz/~fink/publications/kreweras1.pdf)；[Wang–Zhang PDF，摘要及第 5 节](https://arxiv.org/pdf/1301.2931)，[2014 出版记录](https://www.sciencedirect.com/science/article/pii/S0012365X13005153)；[Fink 2-factor 作者 PDF](https://ktiml.mff.cuni.cz/~fink/publication/west.pdf)，[DOI](https://doi.org/10.1007/s00493-017-3731-8)；[长环首次提交和修订记录](https://arxiv.org/abs/2401.01769)，[期刊出版记录：2025-09-12 上线](https://epubs.siam.org/doi/abs/10.1137/24M1670093)。

五方向论文必须区分版本。2025-01-31 的 PDF 标题为 *Matchings of five directions in hypercube extends to Hamilton cycles and paths with prescribed ends*，作者是 **Fink–Hotmar**。正式章节标题改为 *Matchings with Five Directions in Hypercubes Extend to Hamilton Cycles and Paths with Prescribed Ends*，收入 **WG 2025** 论文集，LNCS **16124:258–269**，但出版商明确标注 **2026-01-02** 首次上线，DOI **10.1007/978-3-032-11835-6_19**。当前部分摘要索引把 arXiv:2501.19029 的标题错列为长环论文，引用时应以 PDF 和正式出版页为准。本目录 `paper.txt` 对应 Fink–Hotmar，不能写作 Fink–Mütze。[预印本 PDF](https://arxiv.org/pdf/2501.19029v1)；[正式章节](https://link.springer.com/chapter/10.1007/978-3-032-11835-6_19)。

## 3. 六方向旧结果与本项目 P6 的正确位置

Abid Ali、Weihua Yang、Gohar Ali、Ioan-Lucian Popa、Dilara Akter Mitu 的 *Kinds of Matchings Extending to Hamiltonian Cycles in Hypercube Networks*，**Symmetry 17(7),995**，于 **2025-06-24** 发表，DOI **10.3390/sym17070995**。其 Theorem 12 是附带限制的 $Q_6$ 圈扩张；Theorem 13 是附带限制的至多六方向推广。原文明确写有 “does not cover every two vertices at a distance of 3”。因此它不是无条件的六方向定理。该英文条件在摘要、正文间表述不够一致；介绍时保留其存在即可，未经独立审计不要自行改写成“只要不是完美匹配”。本次核查了目录中的 `symmetry_995.txt` 第 9、16 页对应文本。[原文链接](https://www.mdpi.com/2073-8994/17/7/995)；[出版版本记录](https://www.mdpi.com/2073-8994/17/7/995/notes)。

Fink–Hotmar v1 的 **Conjecture 2** 要求：给定匹配和两个异奇偶端点 $u,v$，且 $u$ 未被匹配覆盖，存在包含匹配的 Hamilton $u$–$v$ 路径。这正是本项目 $P_6$ 对应的六维命题。其 **Theorem 5** 明确说明：若该命题在维数 $d$ 成立，则对所有 $n\ge d$，至多使用 $d$ 个方向的匹配都可扩张为 Hamilton 圈。因此，若项目的 $P_6$ 证明与证书全部成立，结合该已发表的提升框架，得到无额外覆盖限制的六方向圈结论。[原文第 2 页，Conjecture 2、Theorem 5](https://arxiv.org/pdf/2501.19029v1)。

这条推论既不能称为解决所有维数的完整 Ruskey–Savage 猜想，也不能称为解决六方向任意指定端点的完整分类。后者在原文 **Theorem 7** 使用更强的 **Conjecture 5**：排除 C1–C3 障碍后要有两条不同的指定端点 Hamilton 路径。仅有一个端点未覆盖的 $P_6$ 不提供这一前提。

## 4. 截至核查日的新文献线索与核查限制

已核实 **2026-05-11** 出版的 Ali–Ba–Yang，*Hamiltonian paths extending a set of matchings in hypercubes*，J. Combinatorial Optimization **51,43**，DOI **10.1007/s10878-026-01418-3**。其 2025 预印本 Theorem 1.3 为 $n\ge5$、$|M|\le3n-13$、异奇偶端点及 **$xy\notin M$** 的路径结论。出版商摘要省略了最后这一必要限制，故不能直接照抄摘要为无条件端点结论。[期刊页](https://link.springer.com/article/10.1007/s10878-026-01418-3)；[原始预印本 Theorem 1.3](https://arxiv.org/pdf/2506.21432)。

另有 **Abid Ali、Gohar Ali、Weihua Yang** 的 *On Extension of Matchings to Hamiltonian Cycles in 6-Cubes*，Journal of Interconnection Networks **26(04),2550022**，DOI **10.1142/S0219265925500227**。SIAM 引用列表与论文作者关联的 ResearchGate 页面显示其 **2025 年 10 月已在线发表**；SIAM 列出日期为 **2025-10-04**。公开论文摘要明确报告：**$Q_6$ 中每个至多 20 条边的匹配均可扩张为 Hamilton 圈**。这是大小受限的圈结论，不是全部 $Q_6$ 匹配的圈结论，也不是带一个未覆盖指定端点的 $P_6$。出版商正文/PDF 返回 403、ResearchGate 显示全文未公开，故本次没有审计其证明方法。部分索引编排为 2026 年 12 月印刷卷期；核查日早于该时间，宜以“2025 年在线发表”叙述，不能说 2026 年 12 月已经出版。[公开论文摘要](https://www.researchgate.net/publication/396201366_On_Extension_of_Matchings_to_Hamiltonian_Cycles_in_6-Cubes)；[出版商入口](https://www.worldscientific.com/doi/10.1142/S0219265925500227)；[SIAM 引用列表](https://epubs.siam.org/doi/10.1137/0406012)。
本次没有取得完整猜想已被解决的一手证明，也不能以有限检索证明本项目具有首创性。适合主稿的定位是：详细陈述并核验本项目的六维强端点命题与其六方向推论，同时明确与上述已发表结果的前提差异。

