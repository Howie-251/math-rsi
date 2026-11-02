# 72控制点上的逐边二进制仿射线提升

## Target
目标(Δ,D)=(8,4)，保存2026-10-26门槛1100。固定已有72点四正则controller，每fiber取F2^4，实际阶数公式72·16=1152。推导每条边独立仿射线关系的完整生成规则及核验标准，不声称已证明D4。

## Status
COHERENT AS STATED（构造规则及待判覆盖问题；D4尚未成立）。

## Invariant Object
不变量是展开图的全部1152×1152距离≤4关系，不以单字满秩率或控制图距离代替。

## Assumptions and Notation
沿用wave5/mizuno_d4_source/controller72.labels.json的已保存controller C，逆标签[3,2,1,0]。每条无向边e选一个方向u→v，独立选T_e∈GL4(2)、b_e≠0、c_e∈F2^4。V={(u,x):u∈C,x∈F2^4}。

## Derivation Strategy and Map
完整边关系→逆一致性→固定degree/order→原图真正R4→一次有限profile。与旧F2四标签通用chart不同：144条controller边的映射独立，且允许仿射offset；不要求全部108个约化四字对任意controller通用。

## Main Derivation Steps
1. [identity/definition] 对每x和λ∈F2，加入(u,x)—(v,T_ex+c_e+λb_e)。反向矩阵T_e^-1、反向b=T_e^-1b_e、反向c=T_e^-1c_e；在特征二减号等于加号。
2. [proposition] T_e可逆、b_e非零，故正反向每点各恰有两个邻点。controller简单且每点四个不同邻cell，故展开图简单、八正则，边数1152·8/2=4608。无需假设连通；连通/直径由真正展开关系检查。
3. [identity] 给定base walk e1…ek，fiber终点为一个仿射子空间；k≤4时秩≤k。即使单个四路满秩也只覆盖该base终点，不保证所有controller端点。多条短路的子空间并才是真正的覆盖对象。
4. [proposition/filter] 若controller一对点距3，且只有一条长度≤4的walk，则其fiber端点至多2^3=8<16，整个逐边模型都不可能D4。直接在controller上枚举≤4walk作此必要筛，不重跑任何旧全源BFS。
5. [identity/evaluation] R2=I∨A∨A²，R4=R2·R2（布尔矩阵积）。缺项对称，除二为普通无序距离>4点对。首个正式proposal另按全部长度0…4原始walk逐bit校准。仅最佳保存图作root唯一全源BFS。

## Remarks and Interpretation
第一个候选把原F3正向矩阵的2解释为−1后降为F2（0→0，1/2→1），重新求F2逆，不能假定原F3反向矩阵在F2仍互逆。两个正向矩阵均满秩；生成的候选不等于原q3构造定理在q2自动成立。

## Boundaries and Non-Claims
旧2419200通用四标签chart无解保持有效，未重跑或撤回。这里只有该72控制图的逐边规则；若profile失败，既不排除所有逐边规则，也不排除其他八度图。不更换controller、fiber或域，也不因坏对下降续预算。

## Open Risks
控制器可能有独立于矩阵的短路容量障碍；即使必要筛通过，大量四路秩约束与短路子空间并也可能无法同时满足。没有成功概率或D4存在性保证。

## Finite Experiment
先做controller唯一短路必要筛；若通过，两个预定起点（signed原矩阵、固定seed逐边随机），每个最多1000提案，native CPU软限18秒/硬限20秒，一worker。动作改一条边的非零b、offset或可逆线性变换；不改变旧source、控制器或度数。保存完整规则、best.edges及真实终态；无自动加种子/邻域/时间。此文件是本有限实验计划。
