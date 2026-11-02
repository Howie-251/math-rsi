# 已验证120点源的C13覆盖：容量通过，两个固定电压profile失败

终态：全部14400个root/target槽的长度≤5形式容量通过，随后**原定两个起点各2000次单边电压提案均已实际完成**。最好1560点覆盖仍缺4870个代表root/target/sheet项，未达到D≤5。已生成完整1560点4680边六正则图；root唯一全1560源BFS已确认实际D6、31655个距离超过五的无序对，producer没有重复图BFS。没有新下界，不更换source、sheet数或电压域，不补满预算。

这与先前41点C9覆盖属于同一普通循环覆盖机制的底图参数比较，不算第二个独立方法。此120底图的局部短圈容量与41源有实际差别，故本次搜索由容量证据支持；容量通过本身不表示存在成功电压。

## 复用的真实源与完整电压范围

直接使用 [d6_D3_known.edges](../../../../context/DD_PORTFOLIO_START_20261026/baselines/d6_D3_known.edges)，120点360边、每点度六。其120根D3核验已在 [d6_D3_bfs.json](../../../../context/DD_PORTFOLIO_START_20261026/validation/d6_D3_bfs.json)，本次复用该结论，没有重跑同图BFS或重新下载来源。原图来源为 [Comellas / Michel de Messieres 的120点边表](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD3/graph_6_3_n120.txt)，项目保存来源信息为2026-10-26，条目日期2026-10-04。

对每条源边u<v赋z_e∈Z13，生成

    (u,i)—(v,i+z_e mod13)，i∈Z13。

反向减同一电压。覆盖有120·13=1560点、360·13=4680边、度六；目标D5的保存门槛为1518。没有额外同fiber边、边矩阵或affine自由度。

按源边顺序用确定性生成树规范119条边电压为零，其余241条边全自由。任意电压都能沿树通过各fiber的sheet平移变到此规范，故不把它当作额外构造限制。[tree_gauge.json](tree_gauge.json)保存原360边、树和自由边编号。

## 长度零至五的必要形式容量

沿walk累加正反向边电压并相消，得到自由边电压上的稀疏模13线性函数。固定端点的两个walk系数差是circulation；仅支撑在树上的circulation为零，所以删树坐标不损失不同函数。

先作便宜self槽筛：每根完整枚举1+6+36+216+1296+7776=9331条walk，含立即反走、重复顶点和长度零。全部120个self槽分别有19或23个不同形式，均不少于13。原始结果在 [self_capacity.json](self_capacity.json)。

随后扩展到所有目标槽的完整搜索输入：共120根、14400槽，每槽19–49个不同模13函数，共562440个稀疏形式。全部槽通过必要容量，原始walk共1119720条。[capacity.json](capacity.json)保存全部槽计数，[forms.txt](forms.txt)是按root/target排列的完整稀疏函数缓存；代码为 [capacity.py](capacity.py)、[full_capacity.py](full_capacity.py)。

先前 [41/C9试验](../cyclic_cover369/REPORT.md) 的self槽只有五个形式，少于九而立即排除；本源self和全槽均超过十三，不能沿用该障碍。不同函数在某次具体赋值仍可能相撞，这正是后续精确评分要处理的问题。

## 确实运行的两个固定profile

所有root/target/13个sheet状态都参与评分。程序为每条自由边预存受其影响的函数列表；一次电压改变只更新对应函数值和每槽13项实际命中计数，因此目标是精确的全120×120×13覆盖，不是抽样或局部代理目标，也没有每proposal做巨图BFS。

首个正式proposal另从全部562440函数重新计算，全部函数值、14400×13状态计数和总分与增量评分逐项一致。该评分直接用于正式批次，证据为 [first_incremental_calibration.json](first_incremental_calibration.json)。

两个fresh starts固定seed2026102761301、2026102761302，自由边初压独立取0–12；每次选一条自由边改为另外12个值之一。只执行各2000次提案，固定退火温度100→2，没有额外起点、续轮或提案。

| seed | 初始缺失代表状态项 | 本轮最少缺项 | 最终缺项 | 实际提案 | 接受 |
|---:|---:|---:|---:|---:|---:|
| 2026102761301 | 9432 | 5086 | 5086 | 2000 | 471 |
| 2026102761302 | 9560 | 4870 | 4870 | 2000 | 480 |

最好图的360项电压、120根各自缺项数、14400项缺失sheet masks在 [best_parameters.json](best_parameters.json)，完整图在 [best.edges](best.edges)。实际生成时检查无自环/重边、1560点4680边、每点度六；未在producer处做BFS或声称已知普通直径。

固定base root的sheet0足够代表其13个sheet roots：全体sheet同时加常数是覆盖图自同构。故4870个代表缺项对应全1560图63310个有序距离大于五的点对；这是完整符号walk计算的预测，现已由root从明确边表作唯一普通全源BFS确认，63310个有序对即31655个无序对。没有把代表缺项直接冒充无序点对数。

## 实际预算及范围

self筛CPU约0.332秒，完整容量和稀疏输入约2.360秒，编译1.541秒，native搜索约0.580秒；含driver的总CPU约4.826秒，低于20秒总预算。4000个提案全部完成后即停，没有填满剩余时间。运行源码为 [search.cpp](search.cpp)、[run_search.py](run_search.py)，日志为 [production.log](production.log)，准确终态在 [terminal.json](terminal.json)。

root已完成唯一最佳图全源BFS，见 [best.independent_check.json](best.independent_check.json)：简单、连通、六正则，实际D6，全部1560根，31655个>5无序对，CPU1.339501518秒。此入口没有待验项，也没有继续搜索。两个有限profile失败不排除该固定源的全部C13普通覆盖，更不排除其他1560点图；完整容量通过也不是存在性证书。本轮普通循环覆盖的底图比较到此收束，不追加底图、sheet或电压机制。
