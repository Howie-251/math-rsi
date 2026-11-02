# VT60：原始目录范围与本原作用的实际核验

2026-10-12。本次只读既有 Cayley 排除、query pack、本机工具与官方原始来源，没有重新搜索 S5、A5×C2、A6 或正在由另一代理处理的 S6 作用。

**已严格完成：官方 PrimGrp 60 次目录中的九个实际作用均不能产生最大度至多 8 的非空简单图。** 九条记录已提取，具体生成元的全部无序点对轨道已完整核算。推广成“任意 60 点本原作用不可能”还明确依赖该目录/其分类来源的完整性；本次小计算不证明不存在第十条本原群。

没有找到可以直接声称“全部 60 点度 8 顶点传递图已经分类/排除”的主来源。这是此次有界检索结果，不是不存在该文献的定理。

## 主要原始来源的真实范围

| 来源 | 实际覆盖 |
| --- | --- |
| Holt–Royle，A Census of Small Transitive Groups and Vertex-Transitive Graphs，J. Symbolic Computation 101 (2020), 51–60，[作者原稿](https://arxiv.org/abs/1811.09015)，[作者机构存档](https://wrap.warwick.ac.uk/id/eprint/119335/) | 全部次数小于 48 的传递群及全部阶数小于 48 的顶点传递图；不是 60 点完整排除。 |
| Royle–Holt，[官方 Zenodo 数据 4010122](https://zenodo.org/records/4010122) | 全部 10–47 点顶点传递图，每阶 tar 按度数分成 gzip，每行 graph6；无 60 点文件。 |
| Hulpke，[TransGrp 作者仓库](https://github.com/hulpke/transgrp)，[实际手册源码](https://raw.githubusercontent.com/hulpke/transgrp/master/doc/transgrp.tex) | 普通目录到 47 次，另有 48 次补充数据。48 次共 195826352 群、压缩超过 30 GB，本次未下载。不能假设存在完整的 60 次传递群库。 |
| [GAP PrimGrp 官方手册 §1.1](https://gap-packages.github.io/primgrp/doc/chap1.html)，[官方仓库](https://github.com/gap-packages/primgrp) | 本原群目录，而非全部传递群。手册写涵盖次数小于 4096 的全部本原群，同时保留 “believed to be complete” 的限定；当前 README 的范围扩至小于 8192。两者都涵盖 60，但本稿不把库自述当作此次独立证明。 |

PrimGrp 的[官方文献表](https://gap-packages.github.io/primgrp/doc/chapBib.html)列出 Dixon–Mortimer，The primitive permutation groups of degree less than 1000，Math. Proc. Cambridge Philos. Soc. 103 (1988), 213–238；Roney-Dougal，The primitive permutation groups of degree less than 2500，J. Algebra 292 (2005), 154–183；Quick (2011) 的后续扩展。此前读取到的是官方文献表和手册，分类原论文本身的具体完整性陈述另作下文限定。

### 限定追加核查：已发表分类与本次未取得的部分

已读 [Cambridge 出版社的 Dixon–Mortimer 原论文页面](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/abs/primitive-permutation-groups-of-degree-less-than-1000/FBD0495CD1164FE2423829E8BAF82895)，其原文开头明确以列出所有小于 1000 次的本原群为目标，并说明使用有限单群分类；准确 DOI 是 10.1017/S0305004100064793，正式发表时间为 1988 年，网页上线时间 2008 年不是论文年份。

已读 [Roney-Dougal 2005 的出版社摘要](https://www.sciencedirect.com/science/article/pii/S0021869305002541)及[作者所属 St Andrews 的正式发表记录](https://research-portal.st-andrews.ac.uk/en/publications/the-primitive-permutation-groups-of-degree-less-than-2500/)。这不是仅有库的“相信完整”说法：已发表论文明确声称完成小于 2500 次本原群分类，使用 O'Nan–Scott 和 Aschbacher 定理；DOI 为 10.1016/j.jalgebra.2005.04.017。60 确实在其范围内。

但本次无法取得上述两篇完整原文的具体表格/定理页面：出版社全文入口受限。没有亲自将原论文的 60 次分类行与当前九条电子记录逐条接上，因此不提供未经读取的定理编号，也不把原论文摘要加电子库代码说成已独立核尽的分类链。机构目录中检索到的 handle 10023/2045 实际指向后续 4096 次论文，不能误标为 2005 年原文。

据此采用保守但准确的最终范围：**库内九个本原作用的排除已由实际生成元完全核实；所有 60 次本原作用的排除，是援引已发表低次数分类及官方目录正确对应关系的结论，仍明确列作外部分类依赖。** 不宣称本次重证分类完整性；若后续要求去除电子目录对应关系这一依赖，需要取得原分类的相应表格，而不是重复九作用 BFS。

## 九条原始记录和实际数据

原始文件：[官方 data/gps1.g](https://raw.githubusercontent.com/gap-packages/primgrp/master/data/gps1.g)。其中 PRIMGRP[60] 恰含九条记录，已原样提取到 [PRIMGRP_60.records.g](../../computations/dd82/construction/primitive60_catalog_run/PRIMGRP_60.records.g)。

[官方 lib/primitiv.gi](https://raw.githubusercontent.com/gap-packages/primgrp/master/lib/primitiv.gi)文件头将第五字段定义为 Collected suborbits；识别函数也计算点稳定子在其余点上的轨道长度与之比较。因此 [[12,2],[15,1],[20,1]] 是子度 12、12、15、20。

| 序号 | 名称/描述符 | 官方非平凡子度 | 本次无向边轨道度 |
| --- | --- | --- | --- |
| 1 | Alt(5)^2，阶 3600 | 12,12,15,20 | 12,12,15,20 |
| 2 | Alt(5)^2.2，阶 7200 | 24,15,20 | 15,20,24 |
| 3 | Alt(5) wreath Sym(2)，阶 7200 | 24,15,20 | 15,20,24 |
| 4 | Alt(5) wreath Sym(2)，阶 7200 | 12,12,15,20 | 12,12,15,20 |
| 5 | Alt(5)^2.2^2，阶 14400 | 24,15,20 | 15,20,24 |
| 6 | PSL(2,59) | 59 | 59 |
| 7 | PGL(2,59) | 59 | 59 |
| 8 | A60 | 59 | 59 |
| 9 | S60 | 59 | 59 |

第 3、4 条虽有相同抽象群名称，仍保留为不同置换作用。前五条给出完整 60 点置换生成元，本次逐字解析其循环。后四条是紧凑描述符，使用标准作用展开：

- PSL(2,59) 在 $\mathbf F_{59}\cup\{\infty\}$ 上由 $x\mapsto x+1$ 和 $x\mapsto-1/x$ 生成。
- PGL(2,59) 再加 $x\mapsto ax$，其中 $a$ 为最小二次非剩余。
- A60 使用 $(1\,2\,\dots\,59)$ 与 $(58\,59\,60)$；S60 使用 $(1\,2\,\dots\,60)$ 与 $(1\,2)$。

PSL 的平移固定 $\infty$ 且在其余点传递，反演把 $\infty$ 送到 0，故此作用二传递。PGL、A60、S60 同样二传递，后四条理论上也直接只有一个非对角无向轨道。

## 唯一实际运行与推论

源码：[primitive60_catalog_orbits.py](../../computations/dd82/construction/primitive60_catalog_orbits.py)。

实际输出：[primitive60_catalog_run/result.json](../../computations/dd82/construction/primitive60_catalog_run/result.json)。

每个作用先用具体生成元核查 60 点传递性，再对全部 $\binom{60}{2}=1770$ 个无序点对作轨道 BFS。全部生成元像、轨道代表及轨道边表均保留。每个轨道逐点核查同度，轨道不交且合计恰有 1770 对。没有枚举图。

唯一运行 complete=true，全部九条完成；CPU **0.035305184 秒**，wall **5.592895482 秒**（包含读取原始网页的网络等待），单核、CPU 限制 5 秒。没有安装软件、下载整库或生成哈希。

任意群不变简单图的边集必为无向点对轨道之并，不交轨道的度可加。九个作用每个非空轨道的度至少 12，因此不存在非空最大度至多 8 的不变图，当然不存在直径 2 目标。

若采用官方 60 次本原目录的完整性，任意本原自同构作用可重标号为九者之一，便可推出任意本原 60 点目标排除。**这一步是外部分类依赖，不能由本次点对 BFS 本身推出。** 本次没有覆盖任意非本原传递群，也没有声称出现新的可行构造实例。

## 工具与尚未满足的下一域

本机 command -v gap、sage、magma 均无结果；Python 中 libgap、sage、pynauty 不可导入。已有 SymPy 和 NetworkX，分别位于 /opt/conda/lib/python3.11/site-packages/sympy/ 和 /opt/conda/lib/python3.11/site-packages/networkx/。未安装新工具。

另一个真实但本次未筛选的原始数据入口是 Conder–Potočnik 的 [rotary-map census](https://rotarymaps.graphsym.net/)，其中有至多 3000 边 rotary maps 的骨架，另扩展可定向情形至 6000 边。[接口说明](https://rotarymaps.graphsym.net/files/byEdges/MagmaPackageDescription.html)给出 ImportSkeletons.mgm、Skeletons-3000.txt 和 Sk[n,k]；[列说明](https://rotarymaps.graphsym.net/files/skeletons/ColumnDescription.html)含点数、边数、度、重边数和直径。

可定义其有限子域为：简单骨架、60 点、240 边、度 8。须先提取相应元数据，再取得少量完整图或生成元，并排掉已有 Cayley/已闭作用的副本。本次未下载 141 MB 骨架包，未取得此子域数量，也未证明其中存在脱离旧族的实例，所以**不能将其称为已经可执行的新构造候选**。其完整性只覆盖承认 rotary-map 嵌入的图，不覆盖全部顶点传递图。

目前仍缺任意 60 点非本原传递作用的可遍历完整域，或已明确脱离旧作用的具体实例；上述官方完整传递目录和本机工具不能直接填补此缺口。本次不启动非本原图搜索。
