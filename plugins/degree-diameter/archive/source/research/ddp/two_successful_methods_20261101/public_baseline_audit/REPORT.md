# (20,3)、(21,3)、(22,3)定向公开比较

检索日：2026-11-01 UTC。使用本机ARIS research-lit工作流，核读原作者论文、作者网页/仓库、已有本地primary及相关2026年一般族。没有运行图生成器、solver、Lean或BFS；没有联系作者或安装软件。

## 可接受的结论

| 参数 | 本次定位到的既有公开来源可保证下界 | 依据 | 本次请求给定的本地图 |
|---|---:|---|---:|
| (20,3) | 至少2791；其中明确列出的图为2783 | Rajiv September2026的19度2783点图＋Delorme1985 §7一般复制保证，2783+ceil(2783/362)=2791 | 3840 |
| (21,3) | 2928 | PolarStar的IQ规则：q=13，d'=7，(q²+q+1)(2d'+2)=183×16 | 3900 |
| (22,3) | 3294 | 同一IQ规则：q=13，d'=8，183×18 | 4125 |

这些数值只称 **best located prior public-source guarantees as of 2026-11-01**。2791是公开图和公开通用公式的直接存在性推论，没有找到该具体阶数单独发表的记录或边表；不能把它写成作者Table1原数值。未发现更强公开实例不证明截至今日全球最高；尤其21/22没有已取得的完整维护主表。PolarStar数值本身只证明特定已发表族的下界。请求时本地图参数由root给定、已独验，本任务未重新验图或计为确认全球纪录。若root另产更强本地图，应另用新验收结果更新最后一列。

主表3≤Δ≤16的范围不能提供20/21/22的全球最高值。原3750也是本地已有合法实例，不能把它当作已经公开并绑定的外部基线。

## 这次补查了哪些一般族

1. **Delorme极性商及复制。** 原1985论文§2(p292)、§8(c)(p299)给q为奇指数2幂时的D3图：degree=q+1，order=(q+1)(q²+1)。故q=16不能代入；q=8给585/degree9，下一q=32已需degree33。§7(p297)另给任意D≥2图升degree1至少增加ceil(n/(Δ²+1))个点；套19度2783图得到20度≥2791。此为源公式代入，不启动packing搜索。2026 Kronecker论文Table3给18/2340、19/2470、20/2600，同一130点复制到21/22只给2730/2860。一般opposite-GQ公式也核读，未把任意不满足几何存在条件的s,t当成图。
2. **2026极性乘积族。** 核读arXiv:2608.27253v2的§3.4及§7，区分需要极性的两因子产品与不要求单个因子有极性的opposite-GQ族；没有把Table3当成全图分类。
3. **2026渐近一般族。** arXiv:2608.03965v1 Proposition3.1提供H(k,q)的阶数和直径。仅作公开公式比较：k=3最小q=2时阶数为2893695，已超过Moore(22,3)=10187，因此该具体族没有degree≤22的D3实例。不能仅凭其给出的度数上界702作这种排除；这里用的是阶数和直径所迫的Moore界。这不是重新构造/计算图。
4. **2019 Suzuki-Cayley族。** Bachratý–Šiagiová–Širáň的Theorem5.1/预印本Theorem1要求q=2^(2n+1)、n≥1；q=8的阶数448，下一q≥32的度数已超过22。该渐近族未给出更强三格实例。
5. **2026具体报告与作者仓库。** 除本地Rajiv September论文外，实际取读了其July及August primary；后者明确20D3=2750，均未给21/22更强实例。Mizuno当前仓库索引没有20/21/22D3结果；读其论文和已列结果不能据此推断其他作者没有更强图。额外发现的13D5旁证单列，不扩数学支线。

## Primary入口

| 来源 | 本次相关位置/作用 |
|---|---|
| [Rajiv: New lower bounds from generalized quadrangles and hexagons](https://doi.org/10.5281/zenodo.23052995) | Table1：20D3=2783，前值2750；公开比较时间仅September2026。本地既有PDF已提取。 |
| [Rajiv: metacyclic groups, coset graphs and affine lifts](https://doi.org/10.5281/zenodo.22073603) | Theorem1/Table1及affine-line-lift段：20D3=2750，22控制点×125。 |
| [Rajiv: Four new largest known diameter-three graphs](https://doi.org/10.5281/zenodo.21180071) | July2026旧20D3=2202；不是当前更强数值。 |
| [Lakhotia et al.: PolarStar, SPAA2024](https://spcl.inf.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf) | IQ阶数/度数公式、Proposition2/Corollary1；21/22的两个可实例化下界。 |
| [Delorme, European J. Combin.6(1985),291–302](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf) | §2及§8(c)奇指数2幂及绝对点；§7一般升度保证，给2791这一公开来源推论。 |
| [Isham et al., arXiv:2608.27253v2](https://arxiv.org/html/2608.27253v2) | §3.3主表范围、§3.4一般族、§7产品/复制及Table3。v2为2026-10-22。 |
| [Cames van Batenburg–Korsky, arXiv:2608.03965v1](https://arxiv.org/html/2608.03965v1) | Proposition3.1有限公式；不能用渐近性替代小度实例。 |
| [Bachratý–Šiagiová–Širáň, JCTB134(2019),203–217](https://arxiv.org/html/1709.09760v1) | q受限的直径3 Cayley族。 |
| [Mizuno作者仓库](https://github.com/rmizuno42/ddp) | 当前索引/指定package/已存独立验证报告的只读检查。 |

## 覆盖范围与不确定性

本次不是所有论文、仓库和未入表结果的穷举。搜索涵盖degree-diameter/diameter-three一般构造与2026更新、已引经典几何族、两个相关作者仓库和三份Rajiv primary。维护主表止于16度，CombinatoricsWiki的完整当前内容未取到；定向arXiv元数据查询没有返回完整近期列表，已直接核读所引primary HTML并停止重复请求。作者未公开、未索引或未被这些引用链覆盖的更强构造仍可能存在。

因此global_record_confirmed继续false。35度20580仍低于已核Delorme公式35875；本次没有重开35度检索。所有比较仅为来源审阅和小整数公式代入，图正确性与公开新颖性分账。

旁证见[MIZUNO13_PRIMARY_READOUT.md](MIZUNO13_PRIMARY_READOUT.md)。机器可读摘要见RESULT.json。原始HTML、相关PDF的文字提取、API选读和检索入口均在此目录；无产物哈希。
