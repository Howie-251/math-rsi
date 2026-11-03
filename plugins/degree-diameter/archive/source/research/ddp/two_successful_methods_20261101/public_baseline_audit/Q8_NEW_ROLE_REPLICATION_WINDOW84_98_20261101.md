# 同一G1角色复制规则：84–98度的有限竞争窗口

2026-11-01。**已核公开公式范围内，84–98度均未被更大保证阻断；最佳定位保证为4225Δ，条件候选为4226Δ−16，优势68–82点。** 86、90、94、98四个分散端点均值得在当前三图交付后作为同一规则的参数覆盖实例考虑；本门没有生成图、排队或授权生产。其余11个cap只是比较表，不派任务。全球最优与精确优先权仍UNKNOWN。

## 同一源、同一连接规则

唯一source是已数学接受的balanced k1图G1：346516点、14204970边、maxdegree82。J由其4225个first clones和first hub组成。每个J点的完整G1邻域分别是原N_U(c)或原65个fillers，彼此不交且全部落在旧H；复制这些first-role的冻结完整邻域。

在capΔ取r=Δ−82个额外role copies，等价于从H算k=Δ−81个总copy blocks：

```text
n = 346516 + r*4226 = 342290 + (Δ−81)*4226 = 4226Δ−16,
m = 14204970 + r*342225 = 13862745 + (Δ−81)*342225.
```

这延续已经验证的G1/new-role接口；本报告仅代入数量，未把条件公式记为实际图或kernel完成。

## 公开比较与GQ(4,16)边界

[Isham等2026v2 §3.4.2](https://arxiv.org/html/2608.27253v2#S3.SS4.SSS2)重述opposite-GQ构造：GQ(s,t)产生degree `(s+1)(t+1)`、order `(s+1)(t+1)(st+1)^2`。所以GQ(4,16)的真实公开source为degree85、359125点，已在本窗口纳入，不能漏掉。

不过，它的R仍是65。针对已核**partial/fullO×spread矩形复制配方**，p≤R，所以每次最多pR≤4225个中心；即使赋予其最有利full65×spread65条件，复制包络也只是

```text
359125 + (Δ−85)*4225 = 4225Δ  （Δ≥85）.
```

这是该矩形配方的包络，**不是任意中心code或Delorme一般诱导复制的全局容量上界**。没有由degreecount声称unfilled的84度flags也强制4225；没有新断言Q⁻(5,4)上存在所需full ovoid/spread。

实际使用的公开下界不依赖这些未知存在性：[2026v2 §7.4、§7.7](https://arxiv.org/html/2608.27253v2#S7.SS7)与[Delorme1985 §7](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf)已有q8×q8 polarity-product source：585²=342225点、degree81；两个65点absolute集合的乘积给4225个可复制点。任意不同两点至少在一个GQ因子中具有不同absolute coordinate，该因子排除edge/common-neighbor，所以满足复制接口。由此公开方法直接保证

```text
342225 + (Δ−81)*4225 = 4225Δ.
```

这些数字是已发表方法的标量后果，没有新定位到逐cap印出数值或独立公开完整边表。

## 有限窗口实际结果

| Δ | 条件候选n | 已核best-located公开保证 | 差额 |
|---:|---:|---:|---:|
|84|354968|354900|68|
|85|359194|359125|69|
|86|363420|363350|70|
|87|367646|367575|71|
|88|371872|371800|72|
|89|376098|376025|73|
|90|380324|380250|74|
|91|384550|384475|75|
|92|388776|388700|76|
|93|393002|392925|77|
|94|397228|397150|78|
|95|401454|401375|79|
|96|405680|405600|80|
|97|409906|409825|81|
|98|414132|414050|82|

全部15cap均逐一代入此前已读的合法prime-power参数：[PolarStar Table2/Corollary1](https://spcl.inf.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf)的IQ和Paley族、四种已读opposite-GQ直接族、balanced公开partial/fullO×spread复制、Delorme folded及standard12-duality复制、合法GQ-polarity×GQ-polarity及GQ-polarity×triangle/digon组合。没有在q4、q16等不许可参数上擅自假设GQ polarity。

| cap | PolarStar IQ最大 | Paley最大 | 直接GQ最大 | 合法polarity组合及复制最大 |
|---:|---:|---:|---:|---:|
|86|189150|187673|359125|363350|
|90|219414|216001|359125|380250|
|94|249678|241521|359125|397150|
|98|279942|277977|359125|414050|

每个cap的代入参数、case数量及其余category maxima完整保存在JSON。Payne q8矩形最有利包络也低于4225Δ。triangle因子的所有absolute点不自动有互不交邻域，因此脚本把“所有absolute乘积”的乐观值单列为**comparison envelope**；实际保证只使用有效单coordinate复制code。乐观包络仍不能超过winning q8×q8保证，故不影响本门结论，也不把未经证明的load1当公开下界。

## 四个分散端点的取舍

|候选|条件n／m|决定|理由|
|---|---|---|---|
|86|363420／15573870|值得考虑生产|第一个选定的新参数；总k5，沿已验G1 first-role复制，+70公开差额。|
|90|380324／16942770|值得考虑生产|窗口中段新参数；总k9，公开族没有新阻断，可与同一规则共用证明接口。|
|94|397228／18311670|值得考虑生产|上半窗口的分散参数；总k13，+78，价值在参数覆盖而非新机制。|
|98|414132／19680570|值得考虑生产|有限窗口端点，总k17，选定四例中最大差额82，检验更大重复数的同一接口。|

四者的科学内容是一条规则的四个端点。若只选一个用于跨multiplicity检验，98信息量较大；若先求较小实际产物，86规模最小。90/94可作为需要更多参数覆盖时的中间实例。这些取舍不触发任何生产或后台队列；先完成当前三图kernel与终审，再由root作一次明确派发。未选的cap即使有正margin，也没有生产建议或自动任务。

## 一个能改变source选择的代数直觉

仅当真实GQ有实际full ovoid和spread时，p=R的一般reallocation式在固定final capΔ可化为

```text
n = Δ(R²+1)−(s+t).
```

因此在同R65、确有这些接口的source之间，balanced(8,8)常数为−16，而条件GQ(4,16)常数为−20；后者source degree还高4，不能仅凭其未扩张order较大就判断它更有利。balanced在这个fullO/spread同R模型中有4点优势。这是既有公式的source选择解释，不是新的存在性定理、额外图或一般复制最优性结论。

## 公开归属、查询与实际终态

本次只执行一批3条primary定向查询，覆盖degree98/D3、359125及GQ(4,16) spread/ovoid。没有定位到更强的窗口构造；数字相同的软件ticket、CSV和代码测试数据丢弃。查询返回的GQ(4,16)唯一性论文不是新的degree-diameter结果。未重查JGT正文，未增加第二批查询。有限未命中不证明全球穷尽。

归属沿用[exact source-fill UNKNOWN](SPREAD_FILL_SOURCE_PRIORITY_20261101.md)和[改规则有限归属查询](DIAGONAL_FILL_REALLOCATION_TARGETED_QUERY_20261101.md)：若filled H342290加标准fullN复制已公开，候选相对该更强公开保证只剩k=Δ−81点优势，即本窗口3–17点；若相同reallocation+hub规则已公开，优势归0。当前68–82只针对本门实际可核的4225Δ保证，不称world SOTA。

[新脚本](Q8_NEW_ROLE_REPLICATION_WINDOW84_98_20261101.py)实际只运行一次，标量0.370097835CPU／5；[JSON](Q8_NEW_ROLE_REPLICATION_WINDOW84_98_20261101.json)保存完整结果。0图/验证实例/field/spread/BFS/Lean/solver/付费外审/Wikihelper，未执行旧83脚本，未修改root文件或冻结包，没有排队。数学图计数146／37不变。交付期间root另报告q4具体Lean完成、总Lean38，这不改变本窗口标量比较；本门自身不增加Lean计数。
