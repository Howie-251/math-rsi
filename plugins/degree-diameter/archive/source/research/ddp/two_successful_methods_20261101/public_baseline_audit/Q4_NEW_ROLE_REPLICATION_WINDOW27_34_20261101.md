# Q4 new-role复制27..34：八个端点全部被公开保证阻断

核查日2026-11-01。只检验已接受7532/97750/max26源的290个new-role中心
复制，条件公式n=7532+290(Delta−26)=290Delta−8、m=97750+7225(Delta−26)。
本次新标量脚本（含当前作者API选读）实际0.103912025 CPU/5，未构图、解析或
重验旧图，未跑field、geometry、BFS、Lean或solver；未执行旧26/83公开门，未重查JGT。

|cap|条件n|条件m|本次已核公开配方保证|差值|结论|
|---:|---:|---:|---:|---:|---|
|27|7822|104975|8775|−953|阻断|
|28|8112|112200|9100|−988|阻断|
|29|8402|119425|9425|−1023|阻断|
|30|8692|126650|9750|−1058|阻断|
|31|8982|133875|10075|−1093|阻断|
|32|9272|141100|10400|−1128|阻断|
|33|9562|148325|33825|−24263|阻断|
|34|9852|155550|34850|−24998|阻断|

上表是已发表方法的合法标量推论，不是声称另找到了这些阶数的公开边表或完整
当前纪录表。即使将来发现更强公开图，也不会改变本次“全部阻断”的决定。

## 更早的27度阻断来自混合极性产品

[Isham–Lakhotia–Monroe–Petrini2026v2，§7.1、§7.4 Cor7.9/Lemma7.10](https://arxiv.org/html/2608.27253v2#S7.SS4)
允许q=2与r=8的广义四边形极性因子：两者均为奇指数2幂。产品阶数
[(2+1)(2²+1)]·[(8+1)(8²+1)]=15·585=8775，最大度3·9=27，直径3。
两个绝对点集合分别有5和65点。其Cartesian积有325点；任意不同两点至少在一个
因子里具有不同绝对坐标，该因子中距离至少3，因此产品内不相邻、也没有共同邻点。

故可套用[同文§7.7复述的Delorme复制定理](https://arxiv.org/html/2608.27253v2#S7.SS7)，
得到8775+325(Delta−27)=325Delta。每个旧点至多承接一个被复制中心的邻域，
所以不会把“复制k次”误当作只付一次degree。该配方本身已严格压过290Delta−8。
这是从公开产品及一般复制定理得出的推论，不把它冒称为原文逐项印出的27..32表。

作为不依赖这一步产品复制推论的交叉阻断：8775这个直接degree27产品已足以
压过27..30四个条件目标；degree31可用IQ(q19,d′11)的9144点，degree32可用
IQ(q23,d′8)的9954点；degree33/34可直接使用下述33825点degree33原图。

## PolarStar数值纠正

依[PolarStar原论文Table2、Proposition2/Corollary1及§7.1](https://spcl.inf.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf)
（继承已缓存完整primary文本），IQ纤维阶数为2d′+2，合法d′≡0或3(mod4)，
产品degree=q+1+d′、阶数(q²+q+1)(2d′+2)。所以q23,d′8给553·18=9954，
不是11060。11060=553·20对应d′9，而9不是合法IQ degree。q19,d′11合法，
给degree31、381·24=9144。脚本还只在27..34内枚举全部合法IQ/Paley代入。

## 35875/35的实际缓存来源与低degree适用性

已存一手[Delorme，EJC6(1985)291–302，§2、§7、§8(c)](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf)
给q=32=2⁵的合法极性商：base degree33、n=(33)(1025)=33825，绝对点1025个。
degree34复制一次给34850；旧缓存的35875/35正是再复制一次：33825+2·1025。
因此本门使用的是已经公开的33度base及其34度复制，绝没有将一个35度成图直接
当成cap≤34可用。此数值的可核配方归于Delorme；本次作者索引没有提供另一个
可作为出处的新Mizuno35 package。

## 当前作者索引、Comellas与检索边界

本次实际no-cache读取[rmizuno42/ddp当前README](https://github.com/rmizuno42/ddp/blob/main/README.md)、
[results.json](https://github.com/rmizuno42/ddp/blob/main/results.json)及
[results目录](https://github.com/rmizuno42/ddp/tree/main/results)，三个GitHub Contents API
入口均HTTP200，main引用，2026-11-01 13:02:28..31 UTC。该索引的D3条目是15度1458
和16度1920；未列27..34或35的D3 package，README未命中35875。此结论限于实际所读
三个入口，不等于证明作者在其他地方没有结果。机器摘要只保存所需字段，不保存哈希。

[Comellas当前维护表](https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html)
实际主表degree范围仍为3..16；[当前D3详情页](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g3.html)
亦未提供27..34完整比较。因此“表中没有”不作为不存在更强图的证据。
一批三条primary窄检索未带回额外相关构造；不相关数字、选举记录及图论仓库结果均弃置。
上述明确的正向公开构造已足以逐项阻断，结论不依赖无命中，也不依赖全球穷尽。

决定：不推荐任何新端点，0个图生成任务；不自动扫描35+或换源。旧7532合法实例和
当前三目标交付不变，root计数/报告/进度/恢复/Wiki/冻结包均未修改。全局纪录及
优先权不在本次有限公开门中认证。
