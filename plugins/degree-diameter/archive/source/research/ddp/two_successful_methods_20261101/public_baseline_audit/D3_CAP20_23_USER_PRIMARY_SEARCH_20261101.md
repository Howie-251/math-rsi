# D3，20–23度：用户要求的公开primary定向搜索

**明确已有研究，不能由Comellas没有该行推成“无人做”。本次两批定向搜索及primary核读没有定位到达到3840／3984／4192／4336的公开构造；这四张本地图仍超过本次已核来源保证，全球最强与优先权未认证。**

| 最大度cap／D≤3 | 本地已接受点数（root给定） | 本次最大已核公开来源保证 | 证据类别 | 是否定位公开≥本地 |
|---|---:|---:|---|---|
| 20 | 3840 | 2791 | Rajiv实际19度2783图＋Delorme通用复制定理的推论 | 未定位 |
| 21 | 3984 | 2928 | PolarStar，q13／IQ degree7的合法公式实例 | 未定位 |
| 22 | 4192 | 3294 | PolarStar，q13／IQ degree8的合法公式实例 | 未定位 |
| 23 | 4336 | 3549 | PolarStar，q16／Paley13的合法公式实例 | 未定位 |

这些不是已取得的逐项全球纪录表，也没有定位四个数各自单独公布的边表。当前已读primary中单独明确报告的较大具体图是Rajiv的2783点／最大度19／D3，它也合法满足以上每个cap。用户的3250线索仍完整保留：URL、作者、日期及参数尚未绑定，未否认、未归为笔误或别的参数；一旦确认20／3，它会把20和21的比较基线至少提高到3250。当前2791不能拿来否定3250。[既存核查](USER3250_RECONCILIATION_20261101.json)

## 已有人实际做过哪些工作

[Loz、Pineda-Villavicencio，2010原论文](https://guillermo.com.au/pdfs/NewLargeGraphs(C).pdf)的Table2（PDF第19页）直接列D3：17度1610、18度1620、19度1638、20度1958；Table10还给20度1958的Cayley群与voltages。这是历史结果，不拿1958当今天纪录。

[Lakhotia等，SPAA2024 PolarStar作者论文](https://spcl.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf)§1.2明确讨论18–20及更高radix的D3比较；Theorems1–3与§7.1给可实例化构造。最新版Table1是网络性质比较，Table2是超节点参数，Figure1是拓扑族比较，不能误称它们是当前全球逐度纪录表。本文使用的是router图点数，未把attached endpoints当作图的阶数。

[Isham、Lakhotia、Monroe、Petrini的2026原论文v2](https://arxiv.org/html/2608.27253v2)（v1八月27日，v2十月22日）Table3明确有18／2340、19／2470、20／2600；该表题目限定为极性图设计空间，不能作为所有D3图的完整分类。[版本页](https://arxiv.org/abs/2608.27253v2)还说明19／20的完整文档在v1。既存[Rajiv九月30日原论文与数据](https://doi.org/10.5281/zenodo.23052995)的2783已经更强，故新旧材料按数值分开记。

## 四格保证的实际适用条件

20度的2791来自2783+ceil(2783/(19²+1))。2783源实际最大度≤19、D≤3，[Delorme1985 §7／p297](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf)的复制保证升度1可加至少8点。2791是公开来源的数学推论，不是Rajiv原Table1数值或已找到单独文件的图。

PolarStar使用ER_q的q²+q+1点、最大度≤q+1，加超节点degree d′后最大度≤q+1+d′、D≤3。IQ要求d′≡0或3 mod4，阶数2d′+2，所以q13、d′7／8分别给183×16=2928与183×18=3294。Paley要求2d′+1是≡1mod4的primepower；q16、Paley13（degree6）给273×13=3549，度≤23。q16作为Brown／ER底图合法，不把特殊GQ极性族的奇指数2幂限制误套到ER上。这些仅是所读族的下界。

## 本次检索范围与仍在的缺口

先读3250旧核查与23／24旧审计，未重复它们原来的整批数字搜索。本代理只新增两批、每批四query：

第1批：

- `"The Degree/Diameter Problem" "General Graphs"`
- `"diameter 3" "degree 20" largest graphs -site:researchgate.net`
- `"diameter 3" "degree 21" graphs -site:researchgate.net`
- `"diameter 3" "degree 22" "23" graphs`

第2批：

- `"diameter three" graph construction 2026 degree`
- `"PolarStar" "degree" "table" graphs`
- `"degree diameter" "20" "21" "22" "23" lower bounds`
- `"diameter three" "20" "Cayley" largest graphs`

作者包方面，继承同日已读的[Mizuno当前results.json](https://raw.githubusercontent.com/rmizuno42/ddp/main/results.json)（无20–23／D3项）；新读[V3R1T4S作者README](https://raw.githubusercontent.com/elder-plinius/V3R1T4S/main/known-knowns/biggest-graphs/README.md)列七个其它参数，不含本四格。没有据索引未列推成其它作者无人研究。一次候选PolarFly仓库入口404，没有把它当有效artifact或循环重试。

真实高degree专页是[http://www.combinatoricswiki.org/wiki/The_Degree_Diameter_Problem_for_General_Graphs](http://www.combinatoricswiki.org/wiki/The_Degree_Diameter_Problem_for_General_Graphs)，由PolarStar ref46及Isham ref34共同指明。此前3250审计开的是泛入口且超时，不能称已读该表。本轮root接管正确专页／Exoo／Loz档案入口，当前专页仍不可访问；正常CA的两个native尝试也未取得内容，未关闭TLS验证、未安装。详[root访问回执1](D3_CAP20_26_GLOBAL_TABLE_ACCESS_20261101.json)、[回执2](D3_CAP20_26_GLOBAL_TABLE_REQUESTS_ACCESS_20261101.json)。档案入口也未获得可用表；Wikipedia仅作找链接，不提供这里的数值依据。

因此结论是**本次检索best-located，不是无人做、全球不存在更大图、最优性或原创机制的证明**。实时高degree表、未索引作者资料、3250来源仍是具体缺口。0图下载、0BFS／Lean／solver／互审／真人消息；未改rootstate、目录HTML、Wiki或冻结包。完整机器记录见[D3_CAP20_23_USER_PRIMARY_SEARCH_20261101.json](D3_CAP20_23_USER_PRIMARY_SEARCH_20261101.json)。
