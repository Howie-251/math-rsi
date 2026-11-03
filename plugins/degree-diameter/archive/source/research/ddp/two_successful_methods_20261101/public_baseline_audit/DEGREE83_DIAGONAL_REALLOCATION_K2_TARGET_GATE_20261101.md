# degree83／D3：diagonal reallocation k2唯一目标公开门

2026-11-01 UTC。**本次已核公开范围内，最强保证350675；条件候选350742多67点，未被本次定位到的其他构造阻断。** 这是单参数best-located门，不是degree83全球纪录认证。只作标量计算及一个三查询batch，没有生成k2图、重验旧图或启动84+。

## 条件候选与真正的新参数

已读root [general note](../retained_edge_transfer/DIAGONAL_FILL_REALLOCATION_GENERAL_NOTE.md)。采用已接受private balanced81源H，n342290／m13862745，p=R=65、4225中心。k=2时，每center加入两个只连原N_U的clones，另加两个只连全部65源fillers的hubs；H全部边保留。因此

```text
degree cap = 81+2 = 83,
n = 342290 + 2*(4225+1) = 350742,
m = 13862745 + 2*(81*4225+65-65) = 14547195.
```

重复同center的clones通过共同原U邻点相距2，hubs通过源filler相距2；其余路线继承general note的U-only端点与filler/flag接口。这是k>1及degree83的条件实例，不能拿已有k1两个实图当作本候选已生成或已验收。

## 实际最佳公开保证来自公开方法的标量后果

[Isham–Lakhotia–Monroe–Petrini 2026 v2 §7.4、§7.7](https://arxiv.org/html/2608.27253v2#S7.SS7)及[Delorme1985 §7](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf)给独立公开配方：q=r=8的GQ polarity product有585²=342225点、maxdegree81；两个factor各有65个absolute vertices，乘积给4225个可复制点。

这些乘积点两两无1／2路：任意不同两点至少在一个factor的absolute coordinate不同，而该factor的不同absolute vertices无edge或common neighbor。因此删除selfloops后的乘积也满足Delorme复制所需距离条件。公开复制允许k份，不是只能一份，取k2得到

```text
342225 + 2*4225 = 350675，maxdegree83，D3。
```

数值也等于公开unfilled opposite-GQ源的fullO×spread一般复制保证；不据相同order声称两图同构。这是**已发表方法可保证的数值**，没有另定位到印出的degree83数值条目或350675完整边表；不把本次算出的应用包装成论文原文明确列出的新纪录。

## 只在cap83代入已核公式

PolarStar条件继承[作者Table2／Corollary1／§7.1](https://spcl.inf.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf)：q为prime power，IQ的d′≡0或3(mod4)，Paley的d′偶且2d′+1为prime power，degree=q+1+d′≤83。GQ参数域、Delorme folded及standard12 duality、已核polarity product沿用此前读取的一手公式；本次只新算cap83，没有执行旧82脚本。

|公开公式范围|cap83最大值|最佳有关代入|
|---|---:|---|
|PolarStar IQ|169968|q59、d′23、degree83|
|PolarStar Paley|155103|q61、d′20、degree82≤83|
|opposite-GQ直接族|342225|GQ(8,8)，degree81|
|balanced公开O×spread一般复制|350675|342225+2×4225|
|q8 Payne复制宽松包络|339968|327680+3×4096|
|Delorme folded＋复制|85075|q32|
|standard12 duality＋复制|85324|q16|
|已核合法GQ polarity组合＋复制|350675|q=r8，degree81源加2份|

Payne行沿用既有conservative envelope，不冒称本次新定位了其数值边表。其值仍低于350675，不改变选择。已核其他不平衡GQ直接族也均低于表中balanced最大值。所有合法标量代入数、category maxima及候选绑定见[JSON](DEGREE83_DIAGONAL_REALLOCATION_K2_TARGET_GATE_20261101.json)；[脚本](DEGREE83_DIAGONAL_REALLOCATION_K2_TARGET_GATE_20261101.py)只计算此cap，无图生成或旧gate调用。

## 本次唯一三查询batch的范围

只查询 `"degree diameter" "83" "diameter 3"`、`"350742" graph diameter`、`"350675" graph diameter replication`，限定arXiv／GitHub／UPC／ETH primary域。没有定位到相关更强83构造或新规则的匹配实例；返回的SVG尺寸、软件ticket ID及UPC数值handle等同号结果全部丢弃，不用于数学比较。

这是有限negative query，不能证明350742未发表或是全球最佳。没有第二批查询，没有重新寻找JGT1985全文，也未把低degree公开表误读成degree83的完整表。

## 优先权未知怎样影响67点优势

[精确sourcefill审查](SPREAD_FILL_SOURCE_PRIORITY_20261101.md)及[改规则的有限归属查询](DIAGONAL_FILL_REALLOCATION_TARGETED_QUERY_20261101.md)仍为UNKNOWN，原JGT1985正文缺口原样继承。本门将比较拆清楚：

- 当前已核unfilled公开保证350675：条件候选多67。
- 若filled H342290及标准fullN复制已公开：它们可给350740，候选只剩2点优势；不能把67仍全归新规则。
- 若相同diagonal reallocation＋hub规则也已公开：公开可达350742，优势归0。

因此本门只允许root据实际best-located保证选择是否生产**这一张**degree83候选，不能认证世界纪录、精确原创性或其他degree的可行性。发现更强公开源时应停止该target；本次已核范围未发现这种阻断。

实际标量CPU0.034119546秒，预算5；本地进程全终态。0新图/验证实例、0旧field/geometry/BFS/Lean/solver/付费外审、0Wikihelper/root计数/旧冻结包修改；未自动授权生产或84+。
