# C7：一次强制退出原 HS 核心及受限严格下降

2026-10-12。本次从已有 63 坏对图出发，完整检查指定邻域中所有真实退出原 HS 核心的
候选，最少坏对数为 77。选择该图后，在至少一个原 HS 七边轨道仍缺失的域内检查完整
邻域，无严格改善。最终独立 BFS 确认为 58 点、232 边、八正则、直径三、77 个坏对。
已删除七条原 HS 边并新增七条旧旧边，确实离开原 HS 保留分支。

首步是允许分数变差的强制退出，不是将 63→77 称为改善；之后才使用严格下降。
没有中性扩展、随机重启或追加预算。这个局部结果不排除整个 C7 目标域。

## 输入、退出判据与完整邻域

输入为 [上一轮完整输出](CYCLIC7_EIGHT_ORBITS58_SWITCH_RESULT.md) 的
cyclic7_eight_orbits58_switch_run/candidate.best.json。
保留固定点 0,1 间的边，以及 0 到七轨道 S=0、1 到七轨道 T=7 的完整接口，共十五条边。
其余三十一个边轨道仍从全部二百二十个非固定 C7 边轨道中选择。

程序从原始 hs50.edges 读取实际 175 条 HS 边，按已验证的 C7 坐标重标。
其中七条为固定保留的 c—S 边，另外 168 条恰组成二十四个完整七边轨道。
退出判据是这二十四个轨道中至少一个不再被选择，等价于实际删除至少七条原 HS 边。
它不把恢复全部原 HS 边的结果当作退出；没有另加商矩阵、S/T 独立性等必要条件筛选。

邻域与上一轮完全相同：单个轨道的全部合法位移，或两个轨道的四端点全部三种配对，
再遍历两条新轨道的全部合法位移。内部位移为 1,2,3，跨轨道位移为 0,…,6。
新轨道互异且不得与未删除轨道重合。环端点计两次，因此所有候选保持简单性和完整八正则度数。

第一层把最佳合格值初始化为无穷大，从所有退出邻居选择分数最小者，即使它超过 63。
后续每层只接受坏对数严格减少的合格邻居。代码增量更新原 HS 缺失轨道数，
保存时又从实际展开边集读取原标号，核对该数量乘七恰等于实际原 HS 删边数。
评分仍是两固定代表权重一、八个七轨道代表各权重七的完整二步覆盖计数。

## 实际首次退出图

令 (a,b;d) 表示从七轨道 a 的 t 连接到轨道 b 的 t+d，位移模七。
完整邻域选出的首个最优退出 move 为

\[
\text{删除 }(0,7;0),(2,3;1),\qquad
\text{加入 }(0,3;0),(2,7;4).
\]

其中原 HS 轨道为 (2,3;1)，在本地二百二十轨道编号中为 101。
它删除的原 HS 标号边为

\[
\{3,41\},\{6,8\},\{9,40\},\{20,42\},
\{27,47\},\{30,35\},\{44,49\}.
\]

新增七条旧旧边为

\[
\{1,8\},\{4,41\},\{5,20\},\{9,45\},
\{12,35\},\{25,47\},\{37,44\}.
\]

另一个被移除和加入的轨道均是到新增七轨道 T 的附件。
核心内部度数保持 (0,2,0,0,0,2,2,0)，故 S,T 仍独立；这只是实际结果，
没有用作中间候选的硬筛。首次退出图就是最终图，后续没有接受严格改善。

## 完整次数与失败分类

| 阶段 | 起始坏对 | 所选／最佳坏对 | 合法非恒等参数 | 保留完整原核而拒绝 | 实际评分 | 完整 |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| 强制退出 | 63 | 77 | 49,221 | 3,732 | 45,489 | 是 |
| 严格下降 | 77 | 77 | 49,222 | 20 | 49,202 | 是 |

每层均遍历 205 个单轨道参数、60,183 个双轨道参数。
总计 94,691 次合格候选评分，参数表示可能重复同一结果，不能称为互异图数。

最终所有固定点对均在距离二以内。其余坏对由独立 BFS 分类如下：

| 七轨道对 | 缺失位移 | 坏对数 |
| --- | --- | ---: |
| 1,7 | 0 | 7 |
| 2,2 | ±2 | 7 |
| 2,6 | 5 | 7 |
| 2,7 | 2,6 | 14 |
| 3,3 | ±1 | 7 |
| 4,7 | 1 | 7 |
| 5,7 | 2,5 | 14 |
| 6,7 | 1,4 | 14 |

同一轨道内的正负位移描述同一个无向坏对轨道，所以每行 ±d 对应七个坏对。
共有 21 个旧—旧坏对、56 个旧—新增轨道坏对。完整证据保留每个坏对及其共同邻点。
本次成功避开了返回原 HS 核心的退路，但没有同时修复这些新旧缺口；这就是当前具体未完成义务。

## 资源和产物

一次运行总 CPU 为 1.621758441 秒，wall 为 16.236207619 秒，低于三十 CPU 秒总限并提前停止。
编译 CPU 为 1.547218 秒，搜索进程为 0.028762 秒，独立 BFS 为 0.031392 秒；
搜索内部 CPU 为 0.027386 秒。没有追加运行。

- [C++ 源码](../../../computations/dd82/construction/cyclic7_eight_orbits58_core_exit_search.cpp)；
  [一次运行脚本](../../../computations/dd82/construction/cyclic7_eight_orbits58_core_exit_run.py)。
- [实际完整域及原 HS 轨道标记](../../../computations/dd82/construction/cyclic7_eight_orbits58_core_exit_run/domain.json)；
  [搜索分阶段统计](../../../computations/dd82/construction/cyclic7_eight_orbits58_core_exit_run/search.json)；
  [资源](../../../computations/dd82/construction/cyclic7_eight_orbits58_core_exit_run/resources.json)。
- [首次退出图完整边表](../../../computations/dd82/construction/cyclic7_eight_orbits58_core_exit_run/first_exit.edges)；
  [首次退出的完整参数](../../../computations/dd82/construction/cyclic7_eight_orbits58_core_exit_run/first_exit.json)；
  [精确原核变化](../../../computations/dd82/construction/cyclic7_eight_orbits58_core_exit_run/first_exit.structure.json)。
- [最终图](../../../computations/dd82/construction/cyclic7_eight_orbits58_core_exit_run/candidate.best.json)；
  [独立 BFS 全部坏对](../../../computations/dd82/construction/cyclic7_eight_orbits58_core_exit_run/candidate.best.verification.json)；
  [轨迹与坏对分类](../../../computations/dd82/construction/cyclic7_eight_orbits58_core_exit_run/failure_structure.json)。

搜索结果中的 best_bad_pairs=77 指退出后域内的最终最好值，不否认输入图原先只有 63 个坏对。
原输入和首次退出分别保存在 state000、state001；本轮没有重写上一轮源码或结果。
