# 固定 Q8-torsor 电压族的 universal module 上界

这是同一 producer 记录的补充证明，不重枚短词，不构图，不 BFS，不改变固定控制的参数。Root 的现成数据和脚本为 [UNIVERSAL_ENDPOINT_RESULT_ROOT.json](quaternion_orbit_field_controls/UNIVERSAL_ENDPOINT_RESULT_ROOT.json)、[analyze_universal.py](quaternion_orbit_field_controls/analyze_universal.py)、[独立 controller 容量缓存](quaternion_orbit_field_controls/CONTROL_CAPACITY_ROOT.json)。以下继承其端点计数，检查其数学适用范围。

## 1. 四元数整数系数为何给所有目标表示的上界

令 R 为整数 Hamilton quaternion 环，Z-基为 1,i,j,k，其中 i²=j²=-1，ij=k=-ji。固定电压模型中，非零 normal voltage 正好是：

- cross 1→3：-i；
- semi-edge 2、3、4：1、j、i。

它们都作用在同一基向量 z 上。其余四条 identity link 与 cross 1→2 的 normal 为零；Q8 部分按真实源名字固定。对任意目标 Q8 表示 ρ 与任意 z，定义

Eρ,z(c0+c1i+c2j+c3k)=c0 z+c1ρ(i)z+c2ρ(j)z+c3ρ(k)z。

它是 Z-线性 evaluation，并满足 E(h a)=ρ(h)E(a)。因此 universal normal 的递推 n→n+h a 在评价后，正好是新仿射群右乘的 normal 递推。每个短路的真实端点是其整数系数端点的 evaluation，真实不同端点数最多为不同整数系数个数。

逆边也正确：对 voltage (a,h)，真逆 normal 是 -h^-1 a；Root 脚本按此式生成反向，而非独立搬移旧负向量。semi-edge 的 h=-1，所以其真逆仍为自身。这些都是 R 中的恒等式，对目标矩阵的选法、基向量及有限域取模均有效。

这里不声称不同整数系数一定评价为不同端点；有限域可能产生更多碰撞，所以它只能是上界。也不声称 source F3 向量加法可跨域保持。

## 2. 为什么 NB 枚举足以作完整必要条件

给定 base 每个顶点的三条 dart 都到不同 base 类型，唯一同-base 的 semi-edge 也具有确定的逆。因此 40-controller 的每条相邻状态边具有唯一反向 dart。脚本用 previous controller vertex 删除的正是相邻逆边。

任意长度≤D的实际 walk 若含一对相邻逆 dart，删去它们保留相同完整 affine endpoint，并减少两步。重复消去得到长度≤D的 NB walk。所以保留全部 NB 前缀不会漏掉任何可在 D 步到达的端点。Root 脚本的 D10 全前缀数3070，与1+3(2^10−1)相同；关键槽 raw29/raw66 又与独立 controller DP 缓存一致。本分析只读这些既存数据，未重新枚词。

## 3. q5：整个指定 torsor-lift 族被上界排除

D9 的关键槽是 source (base2,Q8=1) 到 target (base2,Q8=-1)，controller id20。Root 得到29条 NB≤9 路线，但在 R 中只有20个不同 normal 系数。

任何 F5² 目标 module 有25个 normal 状态，而 evaluation 的像至多20。因此不论如何选择忠实 Q8/F5² 表示、非零 torsor 基向量或等价坐标，这个关键槽都不能覆盖全部25状态。它关闭的是这一组固定 abstract Q8 voltages 与共同 torsor 向量模型，不只冻结的(u,v)=(0,2)。

这没有排除独立更换 normal voltages、不同 base/作用模型或一般1000点 cubic 图。这里没有生成或导出1000点图，也没有实际图直径、普通坏对数。

## 4. q7：八种表示／基向量的完整规范化

D10 的关键槽是 source (base2,1) 到 target (base3,1)，controller id24。66条路线给53个不同整数端点。53≥49，故“单靠形式数不足”的原预测被反驳，不能由此直接判覆盖失败。

但 q7 还允许一个很小的完整理论评价。令 z≠0。由于 -1 在 F7 不是平方，i没有F7特征线，因此 (z,-iz) 总是一组基。在此基下 i=[[0,1],[-1,0]]。反交换关系强迫 j=[[u,v],[v,-u]]，再由 j²=-I 得 u²+v²=6。这一方程恰有八解：

(2,3),(2,4),(3,2),(3,5),(4,2),(4,5),(5,3),(5,4)。

它们穷尽所有忠实二维 F7 表示配非零基向量的该规范形式；不是事后挑八个候选。evaluation 在此基下就是

(c0,c1,c2,c3)→(c0+u c2+v c3, -c1+v c2-u c3) mod7。

本分析先冻结“八解的最大 image<49”预测，然后仅评价 Root 已存的53个整数系数，共424次小整数映射；没有重枚路线。结果按上述顺序为：

| (u,v) | critical image |
|---|---:|
| (2,3) | 36 |
| (2,4) | 34 |
| (3,2) | 34 |
| (3,5) | 34 |
| (4,2) | 36 |
| (4,5) | 36 |
| (5,3) | 37 |
| (5,4) | 34 |

最大37<49，预测得到支持。因此该固定 torsor-voltage 模型下，所有忠实 Q8/F7² 表示及非零 torsor 基向量都不可能 D≤10。零基向量只给零 normal 电压，也不能覆盖49状态。没有选择 image37 的参数另造图，原 producer 的唯一冻结控制仍为(u,v)=(2,3)。

精确八行 image/missing 集见 [本分析 RESULT](universal_module_analysis/RESULT.json)，[事前预测](universal_module_analysis/PREDICTION.json) 与 [评价脚本](universal_module_analysis/check_q7_evaluations.py)。CPU0.000715623秒；新增短词枚举、图、BFS、solver 均为零。

## 5. 结论口径

q5 由20<25的 universal 上界关闭；q7 先得到53≥49、再由全部八种表示的 image≤37关闭。两者都只涉及固定五底点／Q8分量／共同 torsor normal 电压关系。它们不排一般 cubic 新纪录，也不把代表槽缺项写成全图普通无序坏对。任何实际控制图及其 BFS 范围仍由唯一 producer 记录。
