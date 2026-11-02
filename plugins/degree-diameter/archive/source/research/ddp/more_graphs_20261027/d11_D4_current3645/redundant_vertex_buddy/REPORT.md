# 3645 删除旧点＋双新点：完整 twin-square 选点前提为空

固定结构选点实际没有实例；停止该类，不进入分配搜索。检查原 164 个 twin 的当前邻接，满足完整 untouched twin/line square 的有序 T0 为 0。没有新图、BFS、cutgraph 距离缓存或 A/B 分配实验。这不排除其它 v 或一般 3646 点协作构造。

## 结构直觉、预测与实际选择

来源沿用已验 [source3645.header.edges](../source3645.header.edges)、[原作者说明](../README.author.md) 及已恢复的 [twin→spread-linecopy 映射](../absorbed_pair_probe/HOST_BINDING.json)。当前源实际 3645/20044，七个 degree10 free 点为 3456,3489,3564,3571,3583,3603,3643；其余 degree11。旧 2673 两边吸收与 679 paired-switch 范围均不重跑。

本轮新机制是假设删除冗余旧点 v，新增相邻 a,b，n 净增 1。严格候选按 twin 标签递增选第一个满足下式的 T0，L0 为其原对应 spread-linecopy，T1=T0 xor1，L1=L0 xor1：

~~~text
N(T0)=P0∪{T1}, N(T1)=P1∪{T0},
N(L0)=P0∪{L1}, N(L1)=P1∪{L0},
|P0|=|P1|=10，P0/P1 全为当前 pointcopies。
~~~

这要求两侧等式和两个 switch 都真实保留。事前希望此结构能保护旧点对，并允许两个新根互助覆盖；当前全部 164 个 twin 均不满足，因此“有可选完整方块”的前提被推翻，不能把原 3444 点基图的关系直接继承给插入后的 3645 点源。只读结构检查 CPU 0.016929184 秒。

## 保留的有效条件定理

若今后某个实际图满足上述完整方块，则在 H=G−T0 中，两端都不是 T1 的所有旧 ≤4 路都能同长替换：经过 P0−T0−P0 的两步段改经 L0；经过 P0−T0−T1−P1 的三步段改为 P0−L0−L1−P1。因此只剩 T1 到其它旧点需要实际检查。这个定理是条件性的，本轮没有一个实际 v 满足其前提。

删除 v 后，pin 必须取 N_G(v) 与原 free 点（剔除 v）的并集，使用量不得超过 11−degree_H(pin)。新增 a,b 相邻，各最多接 10 个不同 old pins。精确新根条件为

~~~text
R3_H(A) ∪ R2_H(B) = V(H),
R3_H(B) ∪ R2_H(A) = V(H).
~~~

这些距离必须在删 v 后的 H 内计算。特别地，若 v degree11、N(v) 与七 free 不交，则恰 18 个 cap1 pins。可将它们完整分配为 A/B，要求 8≤|A|≤10，A/B 互换可固定首 pin 入 A。任何 target 若离某 pin 至多 2，则两个新根都自动在 4 步内到达；只对 R2_H(P) 之外的 targets，要求其 R3_H 支持 pin 集同时含两色。这是该 cap1 完整分配情形的精确 property-B＋平衡条件，不是用未删除源图缓存做充分条件。若有合格 v 并过分配，检查实际候选新 a、新 b、T1 三个根即可结合上面同长替路定理覆盖全部点对；本轮这些计算均未启动。

证据：[事前预测](PREDICTION.json)、[结构选择结果](STRUCTURAL_BINDING.json)、[终态](RESULT.json)。这里只关闭“当前 source 上完整 untouched-square 作为删除点保护”的具体入口，不扩更多 v、pin 微调或旧吸收类。
