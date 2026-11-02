# 单锚点equitable partition：一次全局cell-state试验

终态：**UNKNOWN，无incumbent**。在全33397个fold节点上，仅以节点类型和一个几何锚点进行1-WL稳定细化，得到650个generic cells与12个H(3) cells。随后一次全局cell-state MILP在30 CPU秒进程硬限内运行约28.19 CPU秒，未找到满足n≥42343的状态，也未证明不可行。没有生成新大图或新下界，没有扩时、重启solver handle、追加锚点。

这是同一H(9)几何框架中的全局分区参数化，与另一代理的全局随机三态方向不同；不把它算作新的构造大类。它没有固定区域外状态，也没有原作者7959个split的下界限制。

## 分区范围和实际结果

输入为 [Q_data.json](../../breadth_20261027_wave3/hexagon_partial_fold_scout/Q_data.json)。初始颜色只有generic、H(3)非绝对点、H(3)绝对点三类，再将最小编号的H(3)绝对点单独着色。锚点的H(3)索引、fold编号与原点代表均为2；未使用作者split/copy状态。

每轮签名为“旧颜色、各邻居颜色的计数”，按签名字典序编号；细化至稳定。总cell数依次为

    4 → 9 → 15 → 23 → 72 → 347 → 651 → 662 → 662。

| 类型 | 稳定cells | 大小及对应cell个数 |
|---|---:|---|
| generic | 650 | 3×1，9×2，18×1，27×70，54×576 |
| H(3) | 12 | 1×1，3×1，9×1，27×5，54×4 |
| 全部 | 662 | 共33397个原fold节点 |

逐个检查了全33397点的邻cell计数，同cell内均相同，因此实际得到equitable partition。没有据此宣称每个cell是某个已求得群作用的轨道。[partition.json](partition.json)保存全部节点到cell的映射、每个cell成员及邻cell重数；[partition_summary.json](partition_summary.json)保存轮次和大小统计。分区用CPU约1.19秒。generic cells低于3000的预设停止阈值，故执行以下一次IP。

## 全局MILP的变量与精确预算

每个generic cell i有两个二元变量x_i0、x_i1，和不超过1；三种状态分别为merged、split-0、split-1。每个H(3) cell h有整数z_h∈{0,1,2}，表示其每个点增加的copy数。全部cells均可自由选态、删改、着色；没有warmstart。

令m_ij为cell i中任意点到cell j的邻居数，s_i=x_i0+x_i1，d_i为其generic邻居数，i对应的H(3)邻居贡献记Z_i=Σ_h m_ih z_h。由于partition确实equitable，cell-constant状态下，下面的约束与逐点最大度12预算等价：

    Σ_j m_ij s_j + Z_i ≤ 2+d_i s_i；
    Σ_j m_ij x_jk + Z_i ≤ 2+d_i(1−x_ik)，k=0,1；
    Σ_j m_hj s_j + Σ_h′ m_hh′ z_h′ ≤ 5+[h为绝对点]。

前两行分别激活merged和对应颜色split的真实度约束；H(3)行来自基度7−[absolute]。每个cell的大小作为阶数权重，模型最大化

    gain=Σ_i |cell_i|s_i + Σ_h |cell_h|z_h，n=33397+gain，

并直接加入越过保存42342基线的门槛gain≥8946，即n≥42343。因目标是越线候选，没有用33397点平凡状态充当可行改善。普通padding twins不在本模型中。

模型共1312个整数/二元变量、2613行、30169个非零系数。代码在 [run_milp.py](run_milp.py)。若有incumbent，会展开成33033项三态和364项copy数，重新按真实Q/H(3)邻接逐点计度、核对阶数和变量界后才保存candidate；本轮没有incumbent，故没有candidate_state.json。

## 一次求解的终态和边界

只调用一次SciPy/HiGHS handle，threads=1；进程CPU硬限30秒，求解器内部时间约27.72秒。worker实际CPU28.190秒，含启动的child CPU28.286秒，墙钟约28.29秒。返回时间到、primal为空，终态为 `GLOBAL_CELL_TARGET_UNKNOWN_NO_VALID_INCUMBENT`。详见 [terminal.json](terminal.json)。未复用handle扩时，没有第二起点或第二锚点。

UNKNOWN既不说明此partition内没有越线状态，也不说明一般H(9)部分折叠无解。本次状态恒定约束作用于全部cells，属于全局生成，但仍是一般逐fiber自由模型的严格子类。几何定理保证合法状态的D≤5，不保证该cell-constant子类中存在足够大的状态。本轮没有全源BFS、没有安装依赖、没有新完整图。有限profile在此结束，保留partition及准确未决状态。
