# Degree82 / D3：balanced81源完整fullN复制的单参数公开门

2026-11-01 UTC。**在本次明确检查的公开范围内，最强保证为346450点；346515点候选多65点，没有定位到≥346515的公开构造。** 这是有界的best-located竞争门，不是全球纪录或原创优先权认证。只处理degree82，没有生成图或自动启动83及以上参数。

## 候选与公开保证分别来自哪里

候选使用本地已数学接受的balanced GQ(8,8) filled源，n342290、m13862745、全81度；不是Payne源。继承已完成几何及fullN接口，O65×spread65给4225个互不交的完整原N81，各复制一次，条件终图为

```text
Delta=82, D=3,
n=342290+4225=346515,
m=13862745+4225*81=14204970.
```

本门不重验这些本地数学前提，也不把本地源当公开来源。候选完整图尚未在本门生产或验收，计数不增加。

公开保证346450有独立的一手配方：[Isham–Lakhotia–Monroe–Petrini 2026 v2 §7.4、§7.7](https://arxiv.org/html/2608.27253v2#S7.SS7)给广义四边形极性乘积及绝对点复制。q=r=8时，两个585点极性商的乘积有585²=342225点、maxdegree81；绝对点有65²=4225个，满足复制的短距离条件。添一份得到degree82、order342225+4225=346450。它与公开unfilled opposite-GQ源加同fullO×spread复制给出的数值一致；不据数值一致宣称两图同构，也没有另定位到独立的346450数值边表。

## 只在cap82重新代入已核公式

PolarStar适用条件继承[作者原文Table2、Corollary1、§7.1](https://spcl.inf.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf)：host q为prime power；IQ的d′≡0或3(mod4)，Paley的d′为偶数且2d′+1为prime power。下表穷尽这些公式在q+1+d′≤82内的合法标量代入；其余已核族使用[Delorme原文](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf)及[既有GQ参数域](https://arxiv.org/html/2608.27253v2#S3.SS4.SSS2)。没有重跑旧80/81或q7公开门。

| 已核公开机制 | cap82最大值 | 最佳相关代入 |
|---|---:|---|
| PolarStar IQ |166054|q53，d′28，degree82|
| PolarStar Paley |155103|q61，d′20，degree82|
| opposite-GQ直接族 |342225|GQ(8,8)，degree81≤82|
| balanced公开O×spread一般复制 |346450|342225+4225，degree82|
| Payne q8复制宽松包络 |335872|327680+2×4096|
| Delorme folded＋复制 |84050|q32|
| standard12 duality＋复制 |84296|q16|
| 已核合法极性乘积＋复制 |346450|q=r=8|

逐族参数、合法代入数及精确整数算式在[JSON](DEGREE82_BALANCED_FULL_OVOID_COPY_TARGET_GATE_20261101.json)，独立可运行的[标量脚本](DEGREE82_BALANCED_FULL_OVOID_COPY_TARGET_GATE_20261101_scalar_check.py)只计算这一个cap，不调用任何旧gate。

## 唯一三条primary查询及当前公开入口

本次只执行一个batch、三条查询：`"degree diameter" "82" "diameter 3"`、`"346515" graph diameter`、`"degree-diameter-graphs" "diameter 3" "bounds"`，限定arXiv／GitHub／UPC／ETH相关primary域。结果没有定位到更强degree82构造；无关gists未用于任何数学判断。

另直接查看[Comellas原维护表](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/taula_delta_d.html)、其[当前D3描述页](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g3.html)，以及[f4t4nt作者公开仓库](https://github.com/f4t4nt/degree-diameter-graphs)。维护表/描述页呈现低degree条目，不能当作degree82全球表；作者README标注2026-10-27的59图清单，未见degree82条目。直接读2026 v2原文的产品与复制段也未给更强82数值。本次没有重新寻找JGT全文，没有以搜索未命中证明不存在其他公开构造。

## 选择结论与优先权边界

本候选没有被本次已定位公开保证阻断，root可据明确fullN规则决定是否生成并验收degree82完整图；本门本身没有启动生产。竞争优势只写 **346515−346450=65**。

[既有exact spread-fill优先权审查](SPREAD_FILL_SOURCE_PRIORITY_20261101.md)仍为UNKNOWN，关键JGT1985正文缺口照旧继承，不重查一圈。若同一filled342290源及相应复制接口已经公开，那么公开保证也可到346515，当前65点优势归0；不能把这个未解决缺口写成world SOTA。

实际标量CPU **0.021489324秒**，预算5CPU，全部本地进程终态。0完整图／BFS／Lean／solver／外审／Wikihelper；0旧q8field、spread、source或q7验证，0root计数／冻结包修改。未授权或派发83..98梯子。
