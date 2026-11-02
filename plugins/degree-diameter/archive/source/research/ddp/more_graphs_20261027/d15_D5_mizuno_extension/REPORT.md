# (15,5)100132点源：实际球比例支持后续有限构造

最新后续：授权后的[全2498空余点固定64次构造](allfree_cover_probe/REPORT.md)已完成，0命中，按范围停止。下文保留首20球截点；完整R4缓存与当前接口已在后续目录保存。

已绑定当前100132点基图。首20个空余点的R4球平均覆盖20.015879%的旧图，高于事前比较的14度稀有类别16.109967%；球比例预测得到支持。是否能选择≤15个空余点覆盖整个旧图仍未决，本轮没有启动全候选构造或生成100133点图。

## 来源与真实余量

[公开条目](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g5.html#155)将100132点图归于 Sami Hani Badaoui 与 Sarah Ellen Mary Vaughan，公布日期为2026年10月22日，说明它修改、增广和扩展了 Ryosuke Mizuno 的图。原Mizuno机制是32点三正则控制器×F5^5，使用自逆标签和仿射路线的满秩、超平面束覆盖。这与此前364控制器×F3^5的14度源不同；没有把旧100000点图的纤维标签直接移植到当前source。

[当前实际边表](source100132.edges)单次流式下载于2026-10-27 17:34:47 UTC完成，8,832,393字节，453.2墙秒。全过程保留[下载进度](DOWNLOAD_PROGRESS.json)与[handle记录](DOWNLOAD_HANDLE.json)，未并发重复请求；进程已结束，没有遗留在途下载。[SOURCE.json](SOURCE.json)保存精确官方URL和完成时间。

实际边数749732、最大度15，与外部comparison期待值一致，但本结论来自完整literal读取。

|度|实际顶点数|空余槽|
|---|---:|---:|
|13|18|36|
|14|2480|2480|
|15|97634|0|
|合计可接点|2498|2516|

完整点号及余量见[free_ports.json](free_ports.json)，实际度缓存为[degree15.u8.bin](degree15.u8.bin)。源直径5继承公开基图，不重复source全源BFS。

## 事前预测与20球实测

[PREDICTION.json](PREDICTION.json)在下载和球计算前冻结：当前source按标签升序的前20个空余点，其平均R4比例高于14度稀有15点的实测平均；另独立预测全部空余点中存在≤15的完整cover。理论根R4容量44326/100132高于33321/94186，是开展测量的理由，不是完整覆盖证明。

实际20个sample均为degree14：

    31, 34, 95, 145, 152, 169, 325, 463, 492, 508,
    509, 528, 569, 584, 647, 777, 790, 822, 830, 851.

|量|实测|
|---|---:|
|单球覆盖数范围|18485–20990|
|平均单球覆盖数|20042.3|
|当前sample平均覆盖比例|20.015879%|
|D14 rare15比较比例|16.109967%|
|source全源BFS / 新图|0 / 0|
|native CPU秒，含附带star筛|0.23053|
|含编译总CPU秒|1.742385652|

每个球的0–4层计数保存在[PROFILE.json](PROFILE.json)。20个完整球保存为[first20_R4.u64le.bin](first20_R4.u64le.bin)，按sample顺序每行1565个little-endian uint64；[INTERFACE.json](INTERFACE.json)提供可直接交给producer的源、度数和缓存绑定。后续不应重复计算这20个球。

这只是预定20点样本，不是全部2498空余点的均值。新sample根度14，旧rare15根度12，不能把差异全部归因于控制器或域。球比例的正向反馈支持root考虑下一项有限全free构造，但不证明球间互补，也没有自动启动64起点或其它搜索。

## 附带完整spare-star筛

依root的互补授权，复用同一native邻接内存检查全部100132个prototype：令satN(v)为v的满度15邻点数；非孤立且satN(v)=0者，可新增一个邻集恰为N(v)的false twin。旧D5保证该新点到所有旧点≤5，且每个邻点都有合法度余量。此规则的[事前预测](SPARE_STAR_PREDICTION.json)是没有这样的prototype。

[SPARE_STAR_RESULT.json](SPARE_STAR_RESULT.json)得到0个通过者，完整关闭此source上的精确full-neighborhood twin操作，额外CPU仅0.002705秒；没有重复读取源、计算R4或运行额外BFS。它不排除其它≤15pin邻集。

[RESULT.json](RESULT.json)和[terminal.json](terminal.json)均已终态，pending为空。球比例预测SUPPORTED，≤15pin存在性UNRESOLVED；实际目标图n、D及普通无序坏对均为null。当前正向依据是实际球覆盖比例，而非图已构成；下一构造范围交由root安排。
