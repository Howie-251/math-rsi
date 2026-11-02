# 170→171三条matching边插入：完整family的new-root容量失败

结论：**整个指定三条旧边matching插入family都无法让新点三步覆盖全部旧点；最好仍遗漏11点。** 因此不进入unique-path或完整旧对筛，本固定family没有D3图。保存一个按最少new-root遗漏选出的fallback，路径条件预测共79坏对；该选法没有优化全图坏对。root已完成唯一最终全171源BFS，D4且79个坏对逐项匹配；producer没有BFS。无新下界，不追加seed、可删边数或其他171点结构。

限定历史检索未发现完全相同的171点family。源来自 [signed_double340/source.edges](../../breadth_20261027_wave7/signed_double340/source.edges)，但本操作是删三边并加一个六度点，区别于该目录原来的340点signed double。

## 复用的170源和三个完整判定

已有 [source_check.json](../../breadth_20261027_wave7/signed_double340/source_check.json) 确认170点595边、simple connected七正则、D3。直接复用其 [source_distances.json](../../breadth_20261027_wave7/signed_double340/source_distances.json) 和 [distance3_paths.json](../../breadth_20261027_wave7/signed_double340/distance3_paths.json)：10350个旧D3无序对及每对全部1–6条三步路径。没有重跑源BFS。

取三条两两不接旧边D，端点集S有六点；删D，新点w=170连接全部S。旧点都仍七度，新点度六，故n=171、m=595−3+6=598、最大度七。目标D3若成立才会超过保存170。

1. **旧距离≤2的点对永远仍≤3。** 两步旧路径至多含一条被删matching边，用经w的两步替代该旧边，只增加一步；被删的一步旧边本身也被两步替代。
2. **w半径三覆盖全部旧点，当且仅当S在旧G中二步支配。** 删除边都在S内部。到S的最短路可从其最后一个S点开始，因而不用任何S内部删边；dist_(G−D)(S,x)=dist_G(S,x)。于是新点距离就是1+dist_G(S,x)。
3. **旧D3对的判定完整。** 若有某条缓存旧三步路径避开D，它仍在。否则≤3的新路径必须经w；恰在 `u∈S且v∈N_G[S]` 或反向时可修复。N_G[S]可用旧闭邻域，因为被删除边仅在S内部；两端都在S时直接由w两步连接。

因此new-root二步支配、unique-path必要筛和全部旧三步路径supports能给出完整D3判定，不需要逐candidate BFS。所有候选其实D≤4：旧三步路径若只删一边，替代后至多四；若删两边，只可能是首尾两边，两个端点均在S而由w两步连接；新点到任意旧点也至多四。结合本轮new-root失败，整个本family的候选均为D4，而非一般171点图的上界。

## 完整参数范围与实际过滤数

每条源边先存其两端闭半径二球的并，以三个64-bit word表示170旧点。三条edge的这些mask再取并，直接得到S的二步覆盖；matching筛保证六端点互异。程序按源edge ID字典序走完全部无序三元组；共享前两边端点的后续整段可直接计数跳过，不产生遗漏。

| 层次 | 实际计数 |
|---|---:|
| 全部raw三元组C(595,3) | 34930665 / 34930665 |
| 三条边两两不接的合法matching | 32846935 |
| 其中S二步支配全部170点 | 0 |
| capacity拒绝的合法matching | 32846935 |
| unique-path筛实际进入/测试 | 0 / 0 |
| 完整旧D3候选筛实际进入 | 0 |
| hit | 0 |
| 最小new-root遗漏 | 11 |

最后游标为edge IDs[592,593,594]，complete=true。完整原族没有任何候选过new-root容量，因此没有为了跑旧路径筛继续加计算。unique缓存和按首条路径定位受影响pair的代码已准备，但本次实际调用数确为零。统计见 [terminal.json](terminal.json)。

## 保存的fallback及其一次完整路径预测

fallback采用全族最小new-root遗漏、同分取首个字典序matching；它不是全图坏对最少图。删除edge IDs[100,288,373]，即

    (20,47)，(58,154)，(73,76)，

新点邻居为S={20,47,58,73,76,154}。新点三步到不了的11个旧点为

    {22,31,36,41,46,48,67,101,122,130,137}。

选定后仅对这一图，将全部10350个旧D3对按上述完整路径条件计算：old–old坏对68个，new–old坏对11个，总79。这个最终所选图预测与枚举中未进入的formal full filter是两件事，计数已在terminal区分。

完整图在 [fallback.edges](fallback.edges)，参数、全部79坏对和选法在 [fallback_predictions.json](fallback_predictions.json)。已检查171点598边、旧170点度七、新点度六；producer没有普通BFS。root从明确边表和源边表独立重建，唯一全171根BFS确认简单、连通、171点598边，旧170点各七度、新点六度；恰删三条不接边并加六条新点边的规则完全吻合。实际D4、79个距离大于三的无序对，其中new–old11、old–old68，全部79项预测逐对MATCH。见 [fallback.independent_check.json](fallback.independent_check.json)，CPU约0.02104秒。该次检查只针对fallback，没有把其79当作全族最优或重复枚举。

## 成本和scope

输入准备CPU约0.051秒，编译1.717秒，native枚举与所选图预测约0.436秒；总CPU约2.207秒，低于15秒预算。实际代码为 [run.py](run.py)、[search.cpp](search.cpp)，压缩输入为 [source_b2.txt](source_b2.txt)、[paths.txt](paths.txt)，准确原始终态为 [search_result.json](search_result.json)。无重启、无第二family或更一般图搜索。

结论仅排除该固定170源“删三条不接边、加一点连其六端点”的完整family。没有排除任意171点、最大度七、D3图，也没有证明fallback的79是全图坏对全局最小值。无hit后按规定在此停止。
