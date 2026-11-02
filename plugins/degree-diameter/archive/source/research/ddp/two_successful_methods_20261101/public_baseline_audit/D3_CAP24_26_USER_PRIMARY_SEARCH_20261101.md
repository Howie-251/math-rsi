# D3，最大度24／25／26：本次实际primary检索结论

检索日：2026-11-01 UTC。已完成授权的两批、共八条新检索，并打开相关作者论文、作者结果索引及维护者来源。**本轮没有定位并核实达到本地6160／7242／7532的外部公开构造。** 目前能支持的比较仍如下；这不是全球最优认证，也不认证这三张本地图的原创性。

| 最大度／直径 | 本地阶数 | best-located公开来源保证 | 来源性质与合法参数 | 本地差值 |
| --- | ---: | ---: | --- | ---: |
| 24／3 | 6160 | 6144 | Delorme opposite-GQ：GQ(3,5)，24×16² | +16 |
| 25／3 | 7242 | 7225 | Delorme opposite-GQ：GQ(4,4)，25×17² | +17 |
| 26／3 | 7532 | 7514 | 7225＋17²，一般诱导子图复制定理 | +18 |

前两项是已发表构造的参数代入；7514是本项目先前核定的已发表方法组合推论。它们都不等于本次找到了作者显式登记这些数值的纪录表格或对应边文件。未找到更大数值，只能保持best-located与GLOBAL／PRIORITY UNKNOWN。

## 本次实际读到的公开内容

[Isham、Lakhotia、Monroe、Petrini，2026-10-22的v2，§3.4.2](https://arxiv.org/html/2608.27253v2#S3.SS4.SSS2)明确重述Delorme的opposite-GQ公式

    degree=(s+1)(t+1), order=(s+1)(t+1)(st+1)^2, diameter3.

其存在参数包括(q−1,q+1)与(q,q)。取q=4分别得到6144与7225；这里原GQ无需自身有极性，不能误用只容许特定q的单GQ极性商。§7.8的Table3只列到度20，不能当24至26的完备表。

7514沿用[本地DEGREE26原推导](DEGREE26_EXTENSION_20261101.md)：GQ(4,4)有17点ovoid与17线spread；S=O×R的289个中心诱导136个K2与17个孤点。[Delorme《Grands graphes》，EJC6(1985)，§7 p297](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf)的一般诱导子图复制定理给7225＋289、升度至26、保D3。此处必须复制所需的诱导边；不能把S误称为距离至少3的中心集，再套独立中心特例。

本次打开[Mizuno作者仓库当前完整索引](https://github.com/rmizuno42/ddp)，其2026-10-23比较列出的八张图没有24／25／26度结果。这只是该作者索引的范围。两份Rajiv作者原文缓存也实读了摘要／Theorem1／Table1：2026-07的[四个D3结果](https://doi.org/10.5281/zenodo.21180071)为14、18、19、20度；2026-08的[十八项改进](https://doi.org/10.5281/zenodo.22073603)均度数≤20。这次Zenodo在线入口不可达，采用已有原文缓存，未把不可达当作无结果。

新读的[Cames van Batenburg–Korsky 2026，Proposition3.1](https://arxiv.org/html/2608.03965v1#S3)给渐近halved-flag族，但未给这三格的可用数值例子；其D3、q≥2实例的阶已经超过cap26的Moore上界，因而不能作为最大度≤26的反例。PolarStar在线PDF本次超时，继承已核的合法IQ／Paley数值：cap24/25/26分别至多4368/4914/5526与3991/4641/5219，均不改变上述比较；没有再跑参数扫或图程序。

## 高degree表格与原始增强式的真实缺口

[Comellas主表](https://web.mat.upc.edu/francesc.comellas/delta-d/taula_delta_d.html)仅含度3至16。24至26没有表格行，绝不能解释成没有人研究这些度数。沿2026作者论文的引文打开[CombinatoricsWiki原维护表](https://www.combinatoricswiki.org/wiki/The_Degree_Diameter_Problem_for_General_Graphs)，实际返回502；旧Rajiv原文也只将其描述为列到度20。没有据此获得覆盖24至26的当前完整表。

本次搜索返回了[Delorme，JGT9(3)(1985)，325–334的出版社原始元数据](https://doi.org/10.1002/jgt.3190090304)，但未获得正文；未盲重此前失败的官方PDF／ePDF入口。DBLP元数据跟随也不可达，没有发现可用的新全文副本。因此**原文是否有同度数spread-fill或更强增强式仍未解决**。已读EJC一般复制与spread存在性，尚不足以认定同一fill规则已发表；这项不足同样不能反向证明本地规则新颖。

## 精确检索范围

第一批：

1. `degree diameter graph records diameter 3 degree 24 25 26`
2. `"generalized quadrangles" "diameter three" Delorme graphs`
3. `"Large bipartite graphs with given degree and diameter" Delorme pdf`
4. `"degree 25" "diameter 3" graph`

第二批：

1. `"diameter" "7225" graph`
2. `site:github.com "degree24-diameter3" OR "degree25-diameter3" OR "degree26-diameter3"`
3. `"degree diameter" "24" "25" "26" records graphs`
4. `"generalized quadrangle" "augmentation" "diameter" graph`

检索并非只输入本地阶数哨兵。非primary摘要、无结果页面、character-degree graph、平面图、digraph等不相关命中未用作排除证据；没有从搜索摘要登记更强数值。八条检索已经用完，本报告到此停止，不自动扩大检索。

可用于对外表述的是：“三张本地合法图分别超过本次定位到的公开方法保证16、17、18点；是否超过所有公开结果、以及构造优先权，仍未知。”不能据此写全球SOTA或首次构造。机器记录与每项来源／日期／访问缺口见[同名JSON](D3_CAP24_26_USER_PRIMARY_SEARCH_20261101.json)。

0图下载／生成、0BFS／Lean／solver／field检查、0外审或真人联系；root文档、HTML、Wiki、冻结包和计数均未修改。
