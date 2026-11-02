# 2026-10-26 本轮来源更新

本页只记录已读资料、引用边界与当前公开门槛，不登记新的构造或本地证明。本次只写此文件，未运行图搜索/BFS，未修改 wiki、共享状态或 Goal。

## Comellas：低度 D3 的纯 Cayley 最优性报告

实际核读 Francesc Comellas，[*Non-Isomorphic Optimal Cayley Graphs*, arXiv:2606.10954v2](https://arxiv.org/html/2606.10954v2)：Introduction、§2.2、§3.2、§4.2、§5.2，以及参考文献 [5]、[6]。四节分别将度数 4、5、6、7、直径 3 的 Cayley 最优阶报告为 **30、60、108、168**。

这是**文献中的最优性报告**，不是本项目重新证明的 Cayley 上界。Introduction 将相关最优图归于 Conder；[6] 列为 *Largest Cayley graphs with prescribed degree and diameter*，当时标注仍在准备中；[5] 指向 Conder 的 Combinatorics Wiki 图目录。**本轮没有读取或复核 Conder 原始最优性证明**，也没有执行该文的 Sage 脚本或重新验证其附录图。论文关于不同构实例的搜索还明确不保证穷尽，不能把这种实例搜索当作最优性证明。[实际引用位置](https://arxiv.org/html/2606.10954v2#bib.bib6)

本轮决策只据此停止把 Δ=4..7、D=3 的**纯 Cayley 图**作为超过一般图公开纪录的入口。该报告不限制一般双轨道图、非 Cayley 电压提升或任意图；本地某个双轨道族的排除必须依据其自身数学证据。原稿 §5.2 对一般图纪录的时间性叙述也不能代替下面最新读取的 UPC 门槛。

## Isham 等：读取范围及 Goal 边界

实际来源为 Kelly Isham、Kartik Lakhotia、Laura Monroe、Fabrizio Petrini，[*Kronecker Products, Polarity Quotients and Large Graph Constructions*, arXiv:2608.27253v2](https://arxiv.org/html/2608.27253v2)，该 v2 标示日期为 2026-10-22。

本轮此前的读取范围已在 [585 点极点复制说明](polarity585_replication/DERIVATION_PACKAGE.md) 记录为 §7.1–§7.8。本次归档又直接核读摘要、§1.2.3、§7 的相关定义与构造陈述，重点核对 §7.2 的薄多边形、§7.4 的乘积参数、§7.6 的二边形例外、§7.7 的顶点复制及 §7.8.1 的实际参数；不声称通读全文或独立验证其 §5 结构证明及所引原始文献。

§7.8.1 用广义四边形参数 q1=1、q2=8，报告 **Δ=18、D=3、2340 点**的图。18 超出[当前 Goal](../../context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md) 的 4≤Δ≤12，因此不能计为本 Goal 成果或用作范围内突破。该文的极点乘积、绝对点复制信息可帮助理解已知构造，但没有自动给出本地新图或更强的复制上界。[参数原文](https://arxiv.org/html/2608.27253v2#S7.SS8.SSS1)

## UPC 当前 D3 门槛

2026-10-26 直接读取 [UPC 主表](https://web.mat.upc.edu/francesc.comellas/delta-d/taula_delta_d.html) 的 D=3 列，并对照 [Diameter 3 描述页](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g3.html)。主表当前为：

| 最大度 Δ | 一般图 D3 已知下界 | Comellas v2 报告的纯 Cayley 最优阶 |
|---:|---:|---:|
| 4 | 41 | 30 |
| 5 | 72 | 60 |
| 6 | 120 | 108 |
| 7 | 170 | 168 |
| 8 | 253 | 本次未据该文确定 |
| 9 | 585 | 本次未据该文确定 |
| 10 | 650 | 本次未据该文确定 |
| 11 | 715 | 本次未据该文确定 |
| 12 | 810 | 本次未据该文确定 |

一般图列是所读表中的已知构造下界，不是一般图最优性结论。要声称超过本轮门槛，必须给出阶严格更大的合法完整图；当前这些资料不使任何失败样本成为纪录，也不把纯 Cayley 限制转移给一般双轨道图。
