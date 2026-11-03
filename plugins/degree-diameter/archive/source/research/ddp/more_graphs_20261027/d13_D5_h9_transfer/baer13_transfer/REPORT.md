# Baer13 向当前(13,5)基图的整类闭包迁移

合法池为空，事前“至少一个整类闭包可在度13内实现”的预测被反驳。完整复用7560个Baer13形状与1120个F3定义奇异平面，检查8467200次放置。1740次放置的全部必选邻点都具有当前度余量，但邻点数全部超过13，因此没有可交给producer的候选，也没有生成新图。

|量|实测|
|---|---:|
|flat / nonflat平面|364 / 756|
|全部Baer–平面放置|8467200|
|闭包邻点全部degree<13的放置|1740|
|其中需要21 / 22 / 26邻点|814 / 158 / 768|
|闭包邻点数≤13且度数合法|0|
|进程CPU秒|0.98348703|

固定基图为[当前51417点邻接表](../source51417.adjlist.txt)，324451边、最大度13。基线与作者来源继承[来源事实](../SOURCE_FACTS.json)，保存时间为2026-10-27 16:58 UTC。邻接表署名 Dharunish Yugeswardeenoo，并注明 Rishabh Rajiv 的基础构造和对偶数据。真实度数直接复用上一个当前source绑定所生成的degree13缓存，本次没有重读图或计算source距离。

这里的点对合记为φ：它是GF9坐标Frobenius，在作者文件notation中为tau²；作者的tau本身不能与φ混同。对每个13点Baer集合B，使用

    C = pi13(B ∪ φ(B)).

C包含每个被B触及的当前fold类的全部顶点，因此不需要类内方向映射。若j是B内完整非fixed φ点对数，t是所触及类中当前被split的点对数，则

    |C| = 13 − j + t.

所以度预算条件为t≤j，另须逐个检查C中所有顶点的当前degree<13。整类闭包保留上游已经证明的Baer极性覆盖与局部满射quotient路径提升，因此提供核心R4保证；它不自动覆盖当前附加863点。即便存在合法池，完整旧图覆盖仍须producer另验。

原计划还允许在方向恢复成功后另作直接13raw点筛。该条件未达成：[GAUGE_RESULT.json](../raw_map_recovery/GAUGE_RESULT.json)给出旧核心K2,2 block变为当前matching block的精确见证，类内pair翻转不能消除边数变化。因此本轮只执行上述orientation-free闭包模式；没有运行直接13raw点模式，也不把闭包负结果外推给缺少有效映射的其它规则。

复用的完整形状为[7560-mask缓存](../../h9_baer_plane_pool/baer_masks.u64.bin)，平面和坐标均使用已存缓存，没有重新生成轨道、平面或旧degree12候选池。前10平面只处理一次，[profile10planes.json](profile10planes.json)投影CPU约0.674秒后完成全部范围。[closure_shape_summary.json](closure_shape_summary.json)记录系数Frobenius置换及闭包大小分布；[build_pool.py](build_pool.py)可复现此次筛选。

[pool13.json](pool13.json)保持producer使用的records格式，此次records为空。[RESULT.json](RESULT.json)、[terminal.json](terminal.json)均为终态，pending为空。BFS、R4计算、锚点搜索、新图数全部为0；实际目标图的n、D和普通无序坏对为null。已通知root与producer停止此固定池。

结论仅关闭当前51417基图、1120个保存平面内的7560个Baer形状所对应的整类闭包迁移。其它形状、其它平面、基图或有效连接规则不在本次范围；不因空池扩大同一筛选或声称(13,5)无更大图。
