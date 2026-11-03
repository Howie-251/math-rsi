# 固定31点 quartic 控制器的 F3³ edge-pattern 求解器

工具已完成校准。本轮上游 `global31_two_bowties` 的有限生成没有 raw passer，因此收到输入0、MILP调用0、产生新图0。未自行构造31点输入，也未扩大上游搜索。

从项目根目录，对 root 明确给定的候选运行：

```
python research/ddp/breadth_20261027_wave5/controller31_pattern_solver/run_one.py PATH_TO_INPUT
```

输入可以是含 `edges`（及可选 `n`）的JSON，或零起始编号的无向边表，支持首行 `31 62`。要求简单四正则31点图。结果保存在 `item_00/` 等子目录，`batch.json` 持久计数；本批最多八个输入，总CPU上限60秒，任何成功立即终止批次。UNKNOWN不重试。不会自动扫描目录或生成候选。

## 确定性端口和 reverse 配对

`core.label_graph` 对每个连通分量从最小编号点作确定性Euler回路（邻居按编号选择），沿偶长回路交替两色，得到两个2factor。每个2factor从圈最小点开始、先走较小邻居并定向，给出 a±、b± 四个出端口和逆映射 `[1,0,3,2]`。逐点检查两色度二、四邻点唯一及端口逆相容。

每条中心无向边 u<v 产生九个三步NB路径对：起点取u除v外的三个邻点，终点取v除u外的三个邻点。非闭路径把较小端点置于起点；闭路径和其逆取字典序较小者。因此每个反向对恰保留一次，31点时共有62·9=558对，每对有唯一中心无向边。

端点行是所有无序点对（含对角），共496行。原始路径对数为k；目标good数为相邻0、其余（包括对角）1。对角的一对反向路径在有向计数中对应两个good闭walk，恰与31点饱和条件 `G=J−A+I` 一致。

## 十八选一的稀疏 bad-path 模型

局部选项取自已核验的 `wave4/mizuno_d3_source/q3_local_patterns.json`，按实际中央边的出发port选择18种pattern及实现矩阵。每个pattern在该边的3×3九条路径对中恰坏掉两条；反边采用逆矩阵，bad turn转置。

先检查 `k<target`，出现即拒绝。再作直接局部消元：相邻端点行的每条路径必须bad；raw k=1的非邻/对角路径必须good。不满足这些必要条件的edge选项删除，任何edge无选项即拒绝，不调用solver。

剩余每个edge/option使用一个二元变量。每条edge的18选项one-hot；每个端点行要求 `选中bad数=k−target`。每列仅有一个one-hot系数，以及至多两个端点行系数（两个bad路径可落同一端点行，此时系数二），最多1116变量、558行。模型是固定31点饱和证书的精确模型，不把相同等式硬套为30点一般可行性条件。

`worker.py` 使用现有 SciPy milp/HiGHS，单线程、每项solver time_limit五秒、独立进程CPU硬限七秒；八项最坏子进程CPU不超过56秒，driver和一次成功production留在总60秒范围。整数incumbent须直接满足全部等式；超时无incumbent记UNKNOWN，不回退重试。

## 若成功

选择结果以实际F3矩阵重算：每条边的逆及方向相容、全部124个有向边的四平面pencil并为27点、全部1116条有向NB3的秩、完整good计数矩阵 `J−A+I`，并输出961个有序控制器对的路由证书。

随后生成837点、5022边的显式图（编码 `27u+x0+3x1+9x2`），直接检查简单边集和所有度数十二，保存 `graph837.edges`、`construction.json`、`production_check.json`。不做全图BFS；由root执行唯一最终普通BFS。没有成功时不生成候选大图。

## 已完成的有限校准

`calibrate.py` 的明确输入是原Mizuno30点图及旧31点缺口图：

- 原30图仅用于编码试验，确定性Euler/2factor及ports通过；540个reverse路径对的端点计数与独立无标签NB3枚举一致。
- 给各边任取其第一个局部pattern，实际矩阵路由逐一检查全部540个路径对及其逆，rank2/3与紧凑bad-path判定完全一致。该局部测试不是30点q3全局证书，也未生成810点baseline。
- `wave4/controller31_triangle_extension/best_raw_coverage.json` 被立即检出17个无序、34个有序所需路径缺口，未调用solver。

校准CPU0.033秒，详细结果在 `calibration.json`。上游本轮raw passers为零，所以全局MILP与成功production尚无实际通过样例；已校准的代码范围和未运行范围明确保留，没有用工具就绪冒充新构造。
