# 当前(12,4)6156源已恢复：81纤维命中，保边增点无余量

已取得当前6156点的实际边表与完整recipe。一次literal profile确认6156点、36936边，所有顶点degree12，空余点及空余槽均为0。因此固定cap12并保留这张图全部旧边的单点或连通新块扩张没有接口；本阶段没有运行R3覆盖搜索，也没有生成6157点图。

## 主表与描述页的实际差异

[当前Comellas主表](https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html)的(12,4)值为6156，未加表示最优的bold。其链接到的[D4描述页](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html)仍列旧5832，未包含6156；这与主表“数值先更新、详情按月更新”的说明一致。不能把旧5832或其它历史值作为当前纪录。

当前具体源在[Nishant Bhakar的作者仓库](https://github.com/f4t4nt/degree-diameter-graphs/tree/main/graphs/deg12/dia4)：实际边表、construction.json、README，以及对应search/route_chart_lifts中的build_6156.py、chart_6156.txt和badwords_6156.txt均已保存。没有请求Zenodo、访问无关仓库内容或重跑旧72controller/chart。

[SOURCE_FACTS.json](SOURCE_FACTS.json)保留主表精确cell和非bold状态，[official_main.html](official_main.html)与[official_desc_g4.html](official_desc_g4.html)保存两份原页面。下载来源和大小见[SOURCE_RECEIPTS.json](SOURCE_RECEIPTS.json)。当前实际源不存在数据缺口。

## 精确生成结构

顶点写作(c,g,x)，其中c∈{0,1,2,3}、g∈Z19、x∈F3^4。控制器有76点，两个正向标签为

    a(c,g) = ((c+1) mod4, g+va[c] mod19), va=(0,12,4,0);
    b(c,g) = (beta0[c], g+vb[c] mod19), beta0=(1,3,0,2), vb=(17,0,0,1).

另两个标签是a、b的逆映射。alpha、beta各有order76，并非四个controller involutions；标签之间的逆关系为a↔a^-1、b↔b^-1。

各标签t使用[construction.json](construction.json)给出的M_t与d_t，边为

    (v,x) ~ (t(v), M_t x + lambda*d_t), lambda∈F3.

每个标签给一条3点线，故度4×3=12。实际整数标号是

    81*(19*c+g) + x0 +3*x1 +9*x2 +27*x3.

这些M_t是模目标方向线的线性代表；相反标签表示同一无向关系的反向，不应直接把一个所存M矩阵当作另一个的GL4逆。源码[build_6156.py](build_6156.py)已完整保存，本阶段没有执行它去重新生成已知边表。

## 一次实际profile

|指标|实测|
|---|---:|
|实际n / m|6156 / 36936|
|degree12顶点|6156|
|free vertices / slots|0 / 0|
|每点满度邻居数|12，全部6156点|
|81点独立纤维|76|
|相邻纤维对|152|
|每个非空纤维对的边数|243|
|每点通往四个目标纤维的邻居数|3、3、3、3|
|literal quotient相对recipe缺边 / 多边|0 / 0|
|profile CPU秒|0.067733111|

因此76×81的结构预测得到支持；“存在空余点”的预测被反驳。这里的验证是实际度数、纤维邻接计数和76点quotient配方对照，没有BFS或直径重新验收。源D4继承作者公开完整图，图的实际距离未被再次测量。

假设增加任意非空新点集、旧图全部边保留且最大度≤12，则没有新旧边可加入，因为每个旧点已满度。新点无法与旧图连通，故不可能得到有限直径的扩张图。这关闭当前固定源的保边增点操作，不是任意6157点图的不存在性结果。稀有余量类、nearstar或R3 set cover均不应在这个空接口上继续跑。

## 有用的后续范围边界

作者README还报告：同一4点Schreier底图和固定charts上，对19至27阶群的voltage进行受限穷尽，Z19有72个controllability-word-filter通过者，20至27阶没有通过者。该范围是作者的具体source-family报告，本阶段未重跑或把它提升为所有controller/所有6157点图的排除。后续若继续路线覆盖机制，须有真实改变控制器或边结构的理由，不能把该已报告范围改名后再筛。

[RESULT.json](RESULT.json)、[terminal.json](terminal.json)均已终态，pending为空；[profile_source.py](profile_source.py)可复现一次profile。R3搜索、source BFS、新候选和新下界均为0，实际新候选n/D及普通无序坏对为null。未改全局Wiki、HTML或交付包。
