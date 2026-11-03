# (4,6)760源的flag/layer单点吸收：45568项完整结束，0新图

固定45568项全部结束，0命中、0未试、0UNKNOWN。45398项无法使新root在6步到达全部旧点；170项通过新root条件，但均有旧旧距离>6反例。因此“至少一项给出完整761/D6”的预测被反驳，本批按约停止。

## 实际源与固定生成

当前源为[760/1520图](../source760.header.edges)，全部degree4、公开diameter6。源和host结构由scout恢复，本生产程序没有重建H3几何或重复source全源验收。

源由728个原incidence点及32个flag-subdivision点构成。当前保留1424条core-core flag边，layer有32条边；实际layer是三个cycle，长度8、8、16，并非单个32cycle。每个layer点有一个原point邻点、一个原line邻点和两个layer邻点。具体绑定见[RECIPE_BINDING.json](../RECIPE_BINDING.json)。

候选F固定为一条现存core flag及一条现存layer边，两边的类型域分开，四端点不同。删F后新增x，与这四端点各连一次。全部旧degree恢复4，新x也是4，故每个展开候选为761/1522、4正则。它把一个新flag subdivision插入原layer中的一条边。

[frozen.json](../frozen.json)完整列出1424×32=45568项，顺序为flag lex外层、layer edge lex内层。没有增加其它删边、重新挑选layer队列或根据新反例修改候选。

## 完整D6证书，不能沿用D4的R1根集

设S为F四端点。所有被删边都位于G[S]内，任何旧点到S的最近路径在第一次进入S时就能停止，因此

    dist_(G−F)(v,S)=dist_G(v,S).

所以新root到全部旧点≤6，精确等价于sourceR5(S)覆盖全部760点。

旧旧点对采用A=closedR2_G(S)。若旧u,v均在A外，到删边端点距离均≥3；经过任意删边的路径长至少3+1+3=7。旧≤6路径因此不使用F，仍在新图中保留。完整验收只需检查A内每个旧root及新x到全图≤6。

源degree4给每端点R2最多1+4+12=17点，四端点总至多68个旧root，加新x至多69。这是完整覆盖论证，不是对称抽样；D6使用R2根集，不能用此前D4的R1代替。

## 实际检查范围和成本

一次计算760个需要的source端点R5球，同时在同一次BFS保存R2球。前100根只处理一次，随后完整完成所有根，没有重跑profile或source D6验收。缓存各72960字节，分别为[source_R5.u64le.bin](source_R5.u64le.bin)和[source_R2.u64le.bin](source_R2.u64le.bin)，元数据见[RADIUS_CACHE.json](RADIUS_CACHE.json)。

|指标|实测|
|---|---:|
|冻结候选 / 完整关闭|45568 / 45568|
|sourceR5新root筛失败|45398|
|新root通过后旧旧D6失败|170|
|modified-root BFS总次数|1015|
|单候选实际执行最多根数|12|
|一次sourceR5根 / 同次R2快照|760 / 760|
|native CPU秒|0.066705|
|含编译和输入预备总CPU秒|2.468014226|
|导出图 / 未试 / UNKNOWN|0 / 0 / 0|

对通过新root筛的候选，程序先完整检查新x，再按sourceR2闭球的标签顺序检查旧roots，遇首个确定反例即拒绝，所以不必为失败项继续执行理论上限69根。

例如ordinal2删去flag(0,364)与layer edge(729,730)，令新760邻接[0,364,729,730]。新root到所有旧点≤6，但旧0到733仍超过6步。该完整邻集与反例保存于[first_oldpair_witness.json](first_oldpair_witness.json)，没有把>6猜成确切全图直径7或全图坏对数。

[RESULT.json](RESULT.json)保存全部45568项的筛选/反例及根数；[probe.cpp](probe.cpp)、[run.py](run.py)、[candidates.txt](candidates.txt)可复现本批。170个新root成功不是170个完整图，也不是某一张图的170个普通无序坏对。

[terminal.json](terminal.json)已终态，pending为空。实际成功图n、D及普通无序坏对为null。结论仅关闭当前760图上“一条现存flag加一条现存layer边，新增同一个四端点root”的完整有限范围；不排除其它761点图或其它连接结构。未修改全局Wiki、HTML或既有交付包，不追加删边、layer边或badpair修补。
