# 固定650点增加perfect matching降直径：两个结构起点的有限终态

结论：两个指定起点各5000次合法全局matching switch均完成。**最佳仍D5，有31918个距离大于四的无序对**；root唯一全650源BFS与producer精确评分完全一致，并确认1625条原边全部保留、新增325边确为perfect matching。没有degree6/D4新下界，不追加起点、交换、source或强制head–head修补。

这次保留650顶点与所有旧边，提高度到六、目标D4；旧650→651增点并保持degree5/D5的试验不覆盖本任务。只结束这一个2×5000短profile，一般固定源补图perfect matching是否能做到D4仍开放。

## 源、正向保证与精确目标

源为 [rithwik650_source.edges](../../m1_degree5_transfer/rithwik650_source.edges)。复用已有 [source_graph_validation.json](../../m1_degree5_transfer/source_graph_validation.json)：650点1625边、simple connected五正则、D5。采用scout已保存的 [source650_distances.u8](../shortcut_matching_scout/source650_distances.u8) 和87800项旧D5无序对，未重跑source全根BFS或重新下载。其旧D5层分布为LL52250、LB25000、LH5500、BB3750、BH1000、HH300。

F是650点上的325边perfect matching，且F与源边集合不交。G′=G∪F恰650点1950边六正则，阶数超过保存(6,4)=441；旧图仍为连通生成子图，故D(G′)≤5。所有旧距离≤4点对自动保持合格，唯一评分目标是旧距离五的87800对；本轮没有把旧距离四或单条F的覆盖当作代理目标。

## 两个实际结构起点

第一个seed2026102776501只用C25平移，沿原source编码设26行：

    20个leaf行：v=x+25i，i=0..19；
    5个block行：v=500+5x+b，b=0..4；
    1个head行：v=625+x；x∈Z25。

固定shuffle leaf行后，head行先配一个leaf行，五个block行各配一个不同leaf行，剩14个leaf行成七对，共13个row pairs。每对用x↦x+δ逐点匹配，优先选全25条边旧距离均为五的δ；实际13对都找到，全部325条F边确为旧D5。记录在 [initial0_row_pairs.json](initial0_row_pairs.json)、[initial0.F.edges](initial0.F.edges)。这只约束初态，不要求整个500阶群不变，正式swap可破坏全部行结构。

第二个seed2026102776502直接在旧D5图上作一次随机greedy，得到323边并剩四点；随后用两次长度三augmenting repair，把旧matched边ab替为ua、vb，配完四点。实际检查105633个greedy候选、四次greedy skip、12次repair边扫描；最终325边全部旧D5。构造成功，无fallback、无Blossom、无重试seed。准确日志为 [initial1_construction.json](initial1_construction.json)，初态为 [initial1.F.edges](initial1.F.edges)。

后续两起点都允许任意非source边，未把“初态旧D5偏好”或层分布强加为必要条件。

## 正式move、完整评分和一次校准

每次选择F两条不同边ab、cd，端点自动互异；尝试换为ac/bd或ad/bc，若新边属于原source则拒绝。F始终perfect matching，旧1625边从未删除。

记完整新图邻接矩阵为M，计算布尔R₂=I∨M∨M²，再取R₂²，恰为全部650点对的距离≤4关系。与旧D5 masks相交后计缺失无序对，就是新图真实全部距离>4无序对。此评分包含使用两条F边的路线。事实上四步最短path最多用两条matching边；只计单F路线不完整，本轮没有作这种删减。

首个正式合法proposal另逐根直接枚举长度0–4的全部walk：每根1555条、合计1010750条，全部650×650可达bit与布尔平方逐项一致。该proposal直接复用于批次，没有重新开始。证据为 [first_proposal_calibration.json](first_proposal_calibration.json)。

温度固定150→2，每起点只运行5000合法提案。非法draw另计，不因末段改善续跑。

| seed | 初态旧D5 F边 | 初态坏对 | 本轮最佳/最终坏对 | 合法提案 | 非法draw | 接受 |
|---:|---:|---:|---:|---:|---:|---:|
| 2026102776501 | 325 | 37925 | 31918 | 5000 | 121 | 2104 |
| 2026102776502 | 325 | 36516 | 32254 | 5000 | 80 | 2101 |

“最佳”仅指本批实际评分状态，不是完整交换邻域或全部perfect matchings的最优性结论。

## root唯一最终BFS和剩余点对

root从 [best.edges](best.edges) 与原source边表独立重建，确认simple、connected、全六度；650根普通BFS得到D5、31918个距离>4无序对。独立核对原1625边完整包含、新增325边每点恰度一，故确实是本机制。全部结果在 [best.independent_check.json](best.independent_check.json)，CPU约0.256秒，没有第二次最终检查。

| 剩余D5点对层 | 无序对数 |
|---|---:|
| leaf–leaf | 18816 |
| leaf–block | 9198 |
| leaf–head | 2084 |
| block–block | 1344 |
| block–head | 364 |
| head–head | 112 |
| 合计 | 31918 |

旧300个head–head远端仍余112个，没有自动闭合。当前分层数据仅描述保存的最好图，不据此追加HH定向修补或提出全族不存在性。

完整matching在 [best.F.edges](best.F.edges)，原source标签0–649保持；行坐标和δ用于重建初态，最终F允许完全破坏该对称性。所有坏对及分层计数在 [best_score.json](best_score.json)。代码为 [search.cpp](search.cpp)、[run.py](run.py)，实际游标/计时在 [production.log](production.log)、[terminal.json](terminal.json)。

native准备与搜索CPU约1.472秒，含编译总CPU约3.406秒，单worker、20秒预算未触及；10000个合法提案全部完成后即停。producer没有source BFS或最终图BFS；root只完成上述新图的唯一最终全源检查。新下界仍为零，任务在此收束，一般matching存在性保留开放。
