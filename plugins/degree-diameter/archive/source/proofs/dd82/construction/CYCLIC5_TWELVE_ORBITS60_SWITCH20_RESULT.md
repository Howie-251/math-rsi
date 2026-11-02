# 实际 20 坏对种子的完整轨道切换邻域

2026-10-12 的唯一实验完整检查了实际 20 坏对种子的下述邻域，没有严格改善。
最终仍为 60 点、240 边的八正则图，独立全源 BFS 得到直径 3 和恰好 20 个坏对。
这是该实际种子的局部结果，不是全部十二个 C5 轨道图的排除。

## 输入与商结构

输入为 [真实自同构提升](CYCLIC5_TWELVE_ORBITS60_SIGNATURE_LIFT.md) 得到的
seed20：它是原 petersen_all_matchings_run/candidate.best.edges 的准确重标号，
具有经全部 240 边核验的自由 C5 作用。完整的 354 个五边轨道中选取 48 个，
顶点编号为 5a+t。

从这 48 个轨道直接求得商矩阵 M=2I+A(K6,6)，两侧为

- {0,2,5,7,9,10}；
- {1,3,4,6,8,11}。

全部十二个内部度数均为 2，准确矩阵保存在
[seed.quotient.json](../../../computations/dd82/construction/cyclic5_twelve_orbits60_switch20_run/seed.quotient.json)。
[纯数学障碍](CYCLIC5_K66_QUOTIENT_EXCLUSION.md) 已排除保持该商的全部电压赋值，
并证明任何目标图在这十二个轨道中必须至少有两个独立轨道。
本次切换允许移除内部轨道、改变商矩阵，没有将必要商条件作为中间态硬筛。

## 准确邻域及停止条件

直接复制已核对的原 switch 源码，保留 move 域和坏对评分：

1. 对每个选中轨道，尝试相同商端点的全部合法位移。
2. 对每对选中轨道，将四个商端点按全部三种配对重接；每条新轨道尝试全部合法位移。
   跨轨道位移为 0,…,4，内部轨道位移为 1,2。
3. 两条新轨道必须互异，且不能与未删除轨道重合；跳过恒等替换。

商环的两个端点计两次，因此操作严格保持各顶点度数和简单性。
新轨道允许重用被删除轨道，故没有遗漏只改变其中一个轨道的合法情形。
同一结果可能由多个参数表示，下面的次数不是互异图数。

仅接受严格减少坏对的 move；完整邻域没有改善立即停止。
不接受中性 move，无随机重启，也不改变评分。
原先硬编码的初始 50 已替换为读取输入实际分数，并与 20 核对。
保存图的字段改为 selected_from_complete_neighborhood，避免把“来自完整旧邻域的
改善图”误称为自身已检查的局部极小。最终局部停止结论记录在 search.json。

## 实际结果与资源

| 项目 | 实际值 |
| --- | ---: |
| 单轨道参数 | 204 |
| 双轨道及三配对参数 | 71,874 |
| 合法非恒等 move 评分次数 | 60,792 |
| 完整邻域 | 是 |
| 接受 move | 0 |
| 初始／最终坏对 | 20／20 |
| 编译 CPU | 1.298022 秒 |
| 搜索进程 CPU | 0.017969 秒 |
| 独立 BFS CPU | 0.029646 秒 |
| 整批 CPU（含 Python） | 1.353140378 秒 |
| 整批 wall | 1.364646479 秒 |

搜索内部计时为 0.016021 CPU 秒。总授权上限为 30 CPU 秒，实验因完整邻域无严格改善提前结束。
独立检查器读取展开边表，不使用搜索器覆盖缓存；保存了全部 20 个坏对及共同邻居信息。
这些坏对仍全部位于原六纤维坐标的第 4、5 纤维之间；在新 C5 坐标中，
(8,11) 和 (9,10) 各缺位移 2、4，每个缺位移给出五个坏对。

## 文件

- [C++ 搜索源码](../../../computations/dd82/construction/cyclic5_twelve_orbits60_switch20.cpp)；
  [单次运行脚本](../../../computations/dd82/construction/cyclic5_twelve_orbits60_switch20_run.py)。
- [搜索统计](../../../computations/dd82/construction/cyclic5_twelve_orbits60_switch20_run/search.json)；
  [实际资源](../../../computations/dd82/construction/cyclic5_twelve_orbits60_switch20_run/resources.json)。
- [最终完整边表](../../../computations/dd82/construction/cyclic5_twelve_orbits60_switch20_run/candidate.best.edges)；
  [全部轨道参数及图](../../../computations/dd82/construction/cyclic5_twelve_orbits60_switch20_run/candidate.best.json)；
  [独立全图 BFS](../../../computations/dd82/construction/cyclic5_twelve_orbits60_switch20_run/candidate.best.verification.json)。

原 50 坏对种子的 switch 源码和结果均未修改。本次没有继续扩大 move、预算或实验队列。
