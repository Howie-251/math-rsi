# Q8-orbit 跨域控制：源绑定、逆元与五根验收

本文只为同一个 producer 的两项固定控制提供纸面桥接，不增加独立方法或候选。实际原配方保留在 [AUTHOR_construction.json](../d3_D8_current360_Q8_source/AUTHOR_construction.json) 与 [AUTHOR_README.md](../d3_D8_current360_Q8_source/AUTHOR_README.md)。源是 Jianxiang Chen 的 (3,8)360 图的另一种 voltage 描述，非新纪录；本轮未重跑旧图 BFS。

## 真实源坐标与两个固定表示

源已使用列向量和标准矩阵

i=[[0,1],[-1,0]], j=[[1,1],[1,-1]], k=ij，

名字顺序为 1,i,j,k,-1,-i,-j,-k。因此无需另找 basis 或根据覆盖分数拟合 intertwiner，源到此标准坐标的变换就是恒等。

任意奇特征下，令

i_q=[[0,1],[-1,0]], j_q=[[u,v],[v,-u]], u²+v²=-1。

则 i_q²=j_q²=-I，i_q j_q=-j_q i_q，八个 ±I,±i_q,±j_q,±i_qj_q 构成真实 Q8 表示。仅冻结两项：

| q | (u,v) | 三条 semi-edge 的 normal translation part | hypothetical n | 目标 |
|---|---|---|---:|---|
| 5 | (0,2) | (1,0),(0,2),(0,4) | 1000 | (3,9)，L600 |
| 7 | (2,3) | (1,0),(2,3),(0,6) | 1960 | (3,10)，L1250 |

这两个 u/v 是事前固定的表示，不是看实际坏点后选择的 basis。小矩阵检查结果及完整矩阵/向量 lookup 见 [TARGET_CONTROLS.json](../d3_D8_current360_Q8_source/representation_analysis/TARGET_CONTROLS.json)。

q5 中 t²+1 分裂，故每个四阶矩阵有两条本域特征线；q7 中不分裂，故每个四阶矩阵没有本域特征线。但两个域上的**整个 Q8 都绝对不可约**：若 i,j 共同保持一条线，在该线上特征值 λ,μ 均非零，反交换关系将迫使 2λμ=0，矛盾。不能把 q5 误称成整个作用可约。

## 非零轨道 torsor 给出的明确 lift

对 Q8 的每个非单位元素 h，-I 或 h²=-I 都说明 h 没有特征值一。因此 Q8 在每个奇特征 V 的非零向量上自由。源 F3² 恰有八个非零向量，所以 e1=(1,0) 的轨道就是全部非零向量；每个源 v≠0 有唯一 h_v 满足 ρ3(h_v)e1=v。

定义 Lq(0)=0，Lq(v)=ρq(h_v)e1。于是 h_{hv}=h h_v，故

Lq(hv)=ρq(h)Lq(v)，Lq(-v)=-Lq(v)。

实际源用到的 nonzero normal vectors 的映射正好为

e1→e1，(1,1)→(u,v)，e2→e2，(0,2)=-e2→-e2。

它保留抽象 Q8 作用，不保留向量加法，也不是跨特征 field embedding。例如源 e1+e1=-e1，而目标 2e1≠-e1。因此旧 word endpoint 或旧覆盖结论不能直接搬过来。源非零 normal 只有一个 Q8 orbit，q5/q7 分别有三个/六个，这也是必须重新检查路线覆盖的原因。

## 逆元必须按新群形成

源与目标都用法

(v,h)(w,k)=(v+ρ(h)w,hk)。

新群的真逆为 (-ρq(h^-1)v,h^-1)。由上面的 equivariance 与负号性质，

Lq(-ρ3(h^-1)v)=-ρq(h^-1)Lq(v)。

所以这个规则和源单个 voltage 的真逆相容；实现仍应从每个新正 voltage 重算真逆，不把源数字标签直接当新坐标。这个相容性也不能推广成 Lq 保持多步加法。

semi-edge literal 是 (s,-I)，其平方恒为单位。它作为仿射反射的 fixed point 是 s/2；README 将 s 称 centre 的文字不应导致实现除二。控制严格使用 construction.json 的 translation part s，未改值。

## 每个目标模型连通、三正则

四条 identity link（0-2、0-3、0-4、1-4）组成 base 的 spanning tree。三条 semi-reflection 的 translation parts 是 s2=e1,s3=(u,v),s4=-e2。两两反射的乘积给 pure translation，且

det(s3-s2,s4-s2)=1-u+v，

q5 为3，q7 为2，均非零。因 q5、q7 都是素域，这些差生成整个 Fq² 加法群。其余两条 based loop 的 Q8 投影为 -i 与 -j，生成 Q8；有了全 normal translation 可以消去它们的 translation part。因此闭 walk voltages 生成整个 Fq²⋊Q8，完整 lift 连通。

每个小侧 base 点有三个不同 target base 邻居；每个大侧 base 点有两个不同 base 邻居与一个非平凡 involution semi-edge。因此模型 simple、三正则，n=5·8q²，m=3n/2。此处只是合法性与连通性，绝非目标直径保证。

## 为什么五个 deck 根足够且必要

实际边按 (base,g)→(other,g*a) 形成。群左乘 λ_h(base,g)=(base,hg) 保边，并在每个 base fibre 上传递，共五个 deck 轨道。因此若对五个 (base,e) 都完整 BFS，则全图直径恰为这五个 eccentricity 的最大值；不能因非 Cayley 的五底点图只查一个根就宣称 global D。

若所有根达到 q5 的 D≤9 或 q7 的 D≤10，就给出完整目标图。相应 Moore(3,8)=766<1000、Moore(3,9)=1534<1960，故成功时直径分别恰9、恰10。若首根超限即可反驳该固定控制，但首根 eccentricity 不能直接当全局直径。普通无序坏对需另有全量数据，本纸面分析不提供。

## 本分析的实际工作

仅运行一次小矩阵/向量算术：每个域72项 action equivariance 与72项单 voltage 真逆一致性，两个表示均 VALID，CPU0.002170067秒。没有枚举短词、生成图、运行 BFS 或 solver。40-controller 的 NB9/NB10 必要容量与两个实际目标图完全由唯一 producer 另行记录；本文件只合并进其同一研究 row。
