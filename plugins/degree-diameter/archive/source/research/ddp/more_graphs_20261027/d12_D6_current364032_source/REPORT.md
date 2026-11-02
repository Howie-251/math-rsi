# 当前 (12,6)=364032：原配方全 12 正则，保边 star/proxy 入口关闭

事前弱预测“至少有一个原型的满度邻点数不超过 1”被原配方推翻。该作者定义的 364032 点图全部 12 正则，故 free=0、minSatN=12、zero-fault/one-fault 原型均为 0；这是由原配方与小型实际 pattern 文件推出的结论，没有假装取得完整 literal。

## 当前来源与实际取到的文件

唯一相关台账未见此源已恢复。父代理已刷新主表，当前值为 364032；[官方 D6 说明](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g6.html) 对应 Dharunish Yugeswardeenoo 于 2026-10-07 提供的 H(11) 构造，不是猜测的 Bhakar metacyclic 图。

只下载官方 [recipe ZIP](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD6/deg12_diam6_n364032.zip)，共 231423 字节。包含 construction JSON、1332 条 spread-line 标签、9720 个细分记录和 9720 点 pattern 邻接；没有完整 364032 点边表，也没有 354312 点基图。

## 正则性的完整度数计算

基图是 H(11) 的点线 incidence 图，n0=354312、度 12。每条被细分的旧边删去后，两个旧端点各加回到同一新点的一条边，故每个旧点的度保持 12。

实际小包核对：9720 条 cut edge 互异，新点标签正好 354312..364031；840 条 spread line 各细分 7 条边，480 条各细分 8 条。完整 pattern 文件实际简单、无向，9720 个点全部恰有 10 个 pattern 邻点。其中：

- 5880 个 7 点组成员：同组 K7 给 6 邻点，外部恰 4 邻点。
- 3840 个 8 点组成员：同组 K8 给 7 邻点，外部恰 3 邻点。

每个新点再有两个旧端点，总度均为 12。因此整个原配方恰为 12 正则。边数也一致：

~~~text
old base edges             2125872
net subdivision increase      9720
same-line clique edges       31080
external pattern edges       17520
total                      2184192 = 12*364032/2.
~~~

小包结构检查 CPU 0.071927986 秒。以上是 recipe 支持的全图度数结论；未取得或重建完整 literal，未做旧源 BFS、R5 缓存、候选或 MIP。

## 关闭的范围与真实缺项

在保留所有旧边、上限度 12 的前提下，任一旧点都不能接新边。因此不仅原型完整邻集复制，依赖 free old pins 的 near-star/proxy 加点也没有合法连接；新点彼此连边不能使它们与旧图相连。这个入口已严格关闭，无需距离筛。

没有据此否定改变旧边的增广、其它构造或一般 (12,6) 更大图。若将来改变连接机制，首要资料缺项是作者编号的完整 H(11) 基图或整张源邻接。原 construction JSON 明说其 point/line 标签属于自己的 H(11) 编号，现有文件不能直接套到另一份任意编号的六边形。官方维护者同时注明尚未独立验证这个生成包；本轮也不声称新验了其 D6。源的公开阶数/直径与本轮已证明的度数后果分开记录。

证据：[冻结问题](PREDICTION.json)、[原配方](author_recipe/deg12_diam6_n364032_construction.json)、[pattern](author_recipe/deg12_diam6_n364032_pattern_graph.adj)、[源事实](SOURCE_FACTS.json)、[终态](RESULT.json)、[结构检查程序](profile_recipe.py)。本轮到此停止，只关闭这一个 current-source 的保边入口。
