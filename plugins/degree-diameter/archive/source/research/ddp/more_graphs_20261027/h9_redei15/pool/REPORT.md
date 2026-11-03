# Rédei15：固定PGL3(F3)轨道与1120平面的完整degree候选池

候选池已完成并交付producer。固定N12基图42398得到85组不同实际邻集；N11基图37631没有合法项。事前“至少一组N12合法邻集”预测获支持。本任务没有R4、anchor补全、源BFS或图生成，不把候选数算作新图。

形状直接继承 [SHAPE.json](../SHAPE.json)：F9=a+3bu、u²=−1上的x⁵ graph九点加六个方向无穷远点，共15点，极小blocking、Frobenius稳定、五个fixed points，既无完整F9线，也不含Baer13。没有重复它的91线检验；一次字段绑定确认全部81个加/乘项与既有H9 geometry.py一致。

三条F3 projective生成元为坐标循环、x0+=x1、diag(2,1,1)，产生PGL3(F3)，阶5616。该15点mask轨道实际为702，stabilizer8，全部项仍15点、五fixed；若五对非fixed点都合并，fold后为10pins。完整91点索引、702个mask、local15 IDs、parent/generator及矩阵保存在 [orbit.json](orbit.json)。这里只穷尽固定F3群轨道，不宣称覆盖全部Rédei形状、全PGL3(F9)或其它Galois forms。

平面直接复用旧缓存的364个flat与756个nonflat F3-defined totally singular planes，共1120个，未重建平面、H9 incidence、旧Baer masks或旧pool。每个平面使用缓存basis及91个raw point IDs，再用两份已有point→actualcore映射、绑定相应基图的degree缓存筛选。raw总occurrences为702×1120=786240。

| 固定基图 | raw degree合法 | pin数也合法 | distinct实际pinsets |
|---|---:|---:|---:|
| N11：37631点/205329边 | 0 | 0 | 0 |
| N12：42398点/245889边 | 699 | 85 | 85 |

N12的699项中，614项fold后仍有13至15pins，超过degree12预算；合法85项没有实际pinset重复。flat提供50项、nonflat35项。合法邻集的预算为：

| mandatory pins | 项数 | 可用anchors上限 |
|---:|---:|---:|
| 10 | 15 | 2 |
| 11 | 23 | 1 |
| 12 | 47 | 0 |

N11的零项发生在实际degree筛，不是R4失败，也不是全部N11构造不可能；只关闭此固定702×1120degree池。其它Galois forms未测。

交付文件为 [pool12.json](pool12.json)（约345KB）与 [pool11.json](pool11.json)。每项保存pins、anchor_cap、当前degree/free slots、完整raw15、plane kind/global/local index、basis、orbit index/local15 IDs、raw坐标及所有plane/orbit引用。source绑定及缓存路径在 [sources.json](sources.json)。它们固定在42398/37631；producer若改了基图，须使用当时实际degree与完整R4，不能把池筛选当覆盖证明。

先10个planes仅执行一次，预估全程约0.174CPU秒后完成其余1110。orbit实际CPU0.011225918秒，pool进程CPU0.198393225秒，总约0.209619143秒；单核、预算90CPU秒。没有因预算剩余追加形状、平面或群。程序为 [prepare_orbit.py](prepare_orbit.py)、[build_pool.py](build_pool.py)，预测与profile见 [PREDICTION.json](PREDICTION.json)、[profile10planes.json](profile10planes.json)，终态见 [RESULT.json](RESULT.json)、[terminal.json](terminal.json)，pending=[]。

交付后producer在canonical第二项pool_index8生成42399点候选，mandatory10pins加anchors2258、7506，完成当时全42398旧点的覆盖检查后停止；这是 [production/first_hit.json](../production/first_hit.json) 的独立生产结果，root验收另记。本池完整85项，producer只试了2项，余83项未试；不能把它们登记为失败，也不把生产代理的工作重复计入pool成本或验证。
