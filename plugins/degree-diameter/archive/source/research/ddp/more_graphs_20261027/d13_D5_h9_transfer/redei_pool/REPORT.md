# 当前(13,5)基图上的 Rédei15 有限度数池

固定池为空，事前“至少有一个度数合法放置”的预测被反驳。已完整检查保存的702个 PGL3(F3) 形状在1120个 F3 定义的奇异平面中的全部786240次放置；没有一次的全部 mandatory pins 都有空余度。因此本池不能交出可供锚点完成的候选，也没有生成51418点图。

基图为公开的51417点、324451边、最大度13图，公开基线取自2026-10-27 16:58 UTC保存的[来源事实](../SOURCE_FACTS.json)。原始[邻接表](../source51417.adjlist.txt)署名 Dharunish Yugeswardeenoo，并注明 Rishabh Rajiv 的基础构造和对偶数据。此任务仅单次读取当前邻接表生成真实度数，不重复检验其直径。共同50554点核心及当前类映射由上游[绑定结果](../RESULT.json)继承；本任务不使用旧degree12点映射或旧度数。

复用[orbit.json](../../h9_redei15/pool/orbit.json)的702个形状、已保存的364个flat与756个nonflat平面和原始坐标。每个15点形状含5个Frobenius不动点及5对共轭点，完整包含其所触及的split类，所以映射后的pin集合不依赖类内未定向的标号。mandatory pin数为10+s；度13允许s≤3，余下锚点预算为3−s。所有mandatory pins都必须满足当前degree<13，增加锚点不能修复一个已满度的mandatory pin。

|量|实测|
|---|---:|
|复用形状、平面|702、1120|
|完整放置范围|786240|
|全部mandatory pins有空余度的放置|0|
|去重后10–13pin集合|0|
|flat / nonflat已处理平面|364 / 756|
|当前有空余度顶点 / 总空余槽|13248 / 19519|
|进程CPU秒|0.210511479|

前10平面只处理一次，随后完成全部范围；其记录见[profile10planes.json](profile10planes.json)。当前364个F3定义原始点中仍有108个对应顶点未满度，见[F3固定点度分布](F3_fixed_point_degree_profile.json)；所以这里不是“所有F3点都满度”的简单障碍，而是固定702个形状和当前余量配置不能同时兼容。

[pool13.json](pool13.json)保持旧producer可读的records格式，此次records为空。[sources.json](sources.json)绑定实际source与degree13缓存；[build_pool.py](build_pool.py)可复现有限池生成。[RESULT.json](RESULT.json)和[terminal.json](terminal.json)均为终态，pending为空。覆盖、锚点测试、source BFS、新图数均为0，实际目标图的n、D及普通无序坏对保持null。

已通知独立producer空池终态，停止本次覆盖完成。结论只关闭当前51417基图上、保存的1120个平面内、固定PGL3(F3)轨道这项度数池；不排除其它Galois形态、其它平面或基图，也不排除(13,5)更大图。需要真实改变形状、可用度配置或基图才有重开依据。
