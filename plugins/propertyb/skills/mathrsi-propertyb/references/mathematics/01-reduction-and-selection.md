# 最小反例、完整域与实际选锁

## 先把域证明完整

欲证“任意有限简单k元超图、至多M边皆可染”，可以反设存在原反例，再取顶点数最少者。点对覆盖是内部归约产物，不能写进顶层题目。由下方L1拉回、L2双计数取得必要上端；小点数用平衡染色或专门修复排除。两色类大小a、b的均匀固定大小染色，指定边单色概率为

$$p_v=\frac{\binom ak+\binom bk}{\binom vk},\qquad a=\lfloor v/2\rfloor,\ b=\lceil v/2\rceil.$$

$Mp_v<1$ 给严格可染。等号需真实扣交或另一论证。删孤立点与添孤立点的方向分别核清。若要把“≤M”统一补到恰M，须证明该点数上 $\binom vk\ge M$；补边保留不可染和点对覆盖，但实际度数/迹必须从补后的同一H重算。逐档已有≤M−1结果时，反例恰M可直接来自旧结果，不必补边。

新M的程序先生成全部满足整数覆盖必要式的v，再排小点数；不要拷贝旧窗口。六元M66必须含44点，九元M542必须含195点，十二元M4663的下端91亦不同于旧M4660的93。它们见[07实例](07-small-k-working-examples.md)。

## 从全域预算到可保证的局部结构

若只需少量锁点，先用最低度、真实单位伙伴池或低度冲突图，不立即自由枚举所有锁间共度。L2提供每个中心的坏伙伴数；后面的Caro–Wei把低度人数和总度耦合，实际弱楔/共同中心等则用于该充分保证不够的分支。

每个存在性结论都要匹配概率引擎的输入：取得s个≤D单位锁后，所有允许度数组和真实迹都须严格。不能先选一个方便的低度元组求值，再默认H里有它。

下方L19/L26取得的是**实际原边**，经常比任意选k低点再枚举共度便宜；其中结论只提供低边入口，修复仍另证。

## 基础定理与原证明
## L1．边上单射商保留不可染性，最小反例必点对覆盖

**命题。** 设 H 是有限简单 r 元超图，f:V→W 在每条边上单射。以所有 f(e) 为边、合并重复像边得到 H′。则 H′ 仍 r 元，边数不增加；H′ 的任一 Property B 染色沿 f 拉回后，是 H 的 Property B 染色。

证明只用边上单射保留边大小、去重不增加边数、每条像边的两种颜色都可拉回。因而若 H 不可染，H′ 也不可染。

**最小反例推论。** 对 r≥2、任意边数预算 M，若存在不可染对象，选择其中顶点数最小的一个。若不同点 x,y 不共边，合并它们在每条边上仍单射，产生更小不可染对象，矛盾。因此它点对覆盖。

来源：[Reduction.lean](../../../../knowledge/archive/formal/Aris4Math/Reduction.lean) 的 `pushforward_edge_count_le`、`propertyB_pullback`、`propertyB_relabel_iff`、`smaller_counterexample_of_uncovered_pair`。这些是五元接口；32/33/34的顶层归约另有各自参数包装。

可复用的是这个商与拉回机制。固定“19–25点”的窗口还依赖 L2 的上端及专门的小点数染色定理，不能随 M 自动沿用。补边到恰 M 还需要可用边数至少 M；逐档研究若已证明 ≤M−1 均可染，则任何 ≤M 的反例本来就恰有 M 条边。



## L2．整数度数与共度超额是选锁点的统一预算

设 H 有 v 点、M 条 r 元边，r≥2；d(x) 是度数，λ(x,y) 是不同点的共度。双计数给出

\[
\sum_x d(x)=rM,\qquad
\sum_{y\ne x}\lambda(x,y)=(r-1)d(x).
\]

若 H 点对覆盖，则

\[
\epsilon_x=(r-1)d(x)-(v-1)
=\sum_{y\ne x}(\lambda(x,y)-1)\ge0.
\]

因此 \(\lambda(x,y)\ge t+1\) 的伙伴至多有 \(\lfloor\epsilon_x/t\rfloor\) 个（整数 \(t\ge1\)）；尤其非单位共度伙伴数至多 \(\epsilon_x\)。每个这样的伙伴至少消耗 \(t\) 单位超额，这就是证明。

另有两个直接推论：

\[
v\left\lceil\frac{v-1}{r-1}\right\rceil\le rM,
\qquad
|\{x:d(x)=a\}|\ge\max\{0,(a+1)v-rM\}
\quad\text{若所有 }d(x)\ge a.
\]

第二式中令 \(S_a=\{x:d(x)=a\}\)，由 \(rM\ge a|S_a|+(a+1)(v-|S_a|)\) 移项即得。保留整数取整很重要。

|五元、最小度≥6|M=32|M=33|M=34|M=35|
|---|---:|---:|---:|---:|
|24点六度点数量保证|8|3|0|0|
|25点六度点数量保证|15|10|5|0|

这里0表示这一预算没有给出正下界，不表示实际数量必为0。它解释了下一档困难常先发生在“锁点还能不能选到”，而非最后一个分数。

**更远的一个确定推论。** 五元、点对覆盖且 M≤36 时仍有 v≤25：若 v≥26，则每点至少7度，总度≥182>180≥5M。但 M=37 时这一预算不再排除26点；同时，小点数端也须重新研究。这不是 m(5) 的新下界。

**选点推论。** 在候选点集 \(S\) 内，连边表示非单位共度。若该简单冲突图最大度至多 \(\Delta\)，则每次选一点并删除它和邻居，可取得至少 \(\lceil|S|/(\Delta+1)\rceil\) 个两两单位共度点。对所需 \(k\ge1\)，只需 \(|S|>(k-1)(\Delta+1)\)。

源码：[Structure.lean](../../../../knowledge/archive/formal/Aris4Math/Structure.lean) 的 `sum_degrees`、`sum_codegrees_erase`、`pairCovering_degree_bound`、`sum_codegree_excess`、`badPartners_card_le_excess` 是五元一般点数接口；`exists_pairwise_avoiding_subset` 是一般对称关系的 Δ=1 选择。另有 [TwentyFiveSelection.lean](../../../../knowledge/archive/formal/Aris4Math/ThirtyFour/TwentyFiveSelection.lean) 的 `unit_subset_of_bad_bound`，k、Δ可变，但宿主固定五元25点。一般 r、一般阈值 t 的统一包装是上述纸面推广。

特别地，25点六度中心的 ε=0；24点六度中心的 ε=1，恰有一个共度2伙伴，故恰有一对入射边在中心外相交。23点六度中心 ε=2，不能沿用“唯一坏对”。

**2026-10-19通用选锁补充。** 合作者把总度预算与Caro–Wei组合为一般k的低度单位锁判据；完整证明、有限r加强及k5实际边界见[小k迁移笔记](../../../../knowledge/archive/research-wiki/PROPERTY_B_SMALL_K_TRANSFER.md)。这是本组预算的进一步组合，尚未新增Lean接口。

## 一、总度预算下的低度单位锁判据

设点对覆盖的简单 k 元超图恰有 M 边，`d0=ceil((v−1)/(k−1))`，取整数 `D≥d0`。
令 `L={x:d(x)≤D}`、`r=|L|`，在L上以 `λxy≥2` 连冲突图G的边；独立点集即两两共度恰1的锁集。
记

`Z=(D+1)v−kM`，`T=(k−1)(D+1)−v+2`。

L外顶点度至少D+1，故 `Σ_{x∈L}d(x)≤(D+1)r−Z`。
点对覆盖又给出 `deg_G(x)≤Σ_{y≠x}(λxy−1)=(k−1)d(x)−(v−1)`。
相加得到 `2e(G)≤(T−1)r−(k−1)Z`，保留了低度点个数与总度之间的关联。
Caro–Wei及Cauchy给出 `α(G)≥r²/(r+2e(G))≥r²/(Tr−(k−1)Z)`。
当Z>0，真实r非零且末分母为正；完成平方得到

`r²/(Tr−(k−1)Z)≥4(k−1)Z/T²`。

例如相减通分后的分子为 `(Tr−2(k−1)Z)²`；真实可行时T>0。
所以 **`Z>0` 且 `4(k−1)Z>(s−1)T²` 保证至少s个度≤D的单位共度锁点**。
这里严格大于s−1再用独立数为整数，不能把边界等号视为成功。
来源为合作者 [k10/11稿的定理B](../../../../knowledge/archive/propertyB_small_k/propertyB_k10_k11_research.md)；k8/9稿用其三锁版本。
它是已有 [L2度数／共度预算](../../../../knowledge/archive/research-wiki/PROPERTY_B_REUSABLE_LEMMAS.md) 的有效组合，不重命名为全新基础机制。

可再保留整数r而不对全部实数最优化。由最低度及外部度数，

`r≥max(0,ceil(Z/(D+1−d0)))`，`r≤v`。

对每个r取

`2e_upper=2 floor(min(((k−1)D−v+1)r,(T−1)r−(k−1)Z,r(r−1))/2)`。

这分别使用逐点excess、总度预算及简单图界；负上界的r不可能，其余r保证 `ceil(r²/(r+2e_upper))`。
对留下的r取最小即得普适保证；Z≤0时保留r=0且保证0。留下的r仅满足必要条件，不宣称都有真实超图。
本轮固定 `k=5,M=35,v=18..25,D=d0..15,s=2..10` 的整数扫描，**没有降低连续判据所得的任何最小D**。
完整表及全部r分数见 [pilot说明](../../../../knowledge/archive/context/collaborator-small-k-20261019/m6-m7/K5_SELECTION_PILOT.md)／[JSON](../../../../knowledge/archive/context/collaborator-small-k-20261019/m6-m7/K5_SELECTION_PILOT.json)。

## L17. Brooks迫出的单位权完整分量

设非负整数加权冲突图每点加权度为$D\ge3$，普通支撑图有$n$点，独立数为$a$，并有$s$个$K_{D+1}$连通分量。删去这些分量后用Brooks定理作$D$染色，再取最大色类及每个删去分量的一点，得

$$a\ge s+\left\lceil\frac{n-s(D+1)}D\right\rceil=\left\lceil\frac{n-s}D\right\rceil,\qquad s\ge n-Da.$$

完整分量的每个内部权重都至少一，每点已有$D$条邻边且总权$D$，故全部权恰一。对25点全七度，$D=4$；最大单位集$a=6$强制至少一个真实五点组，$a=5$强制全部五组。一般证明、Brooks原文实际阅读页及迁移边界见[规范引理](../../../../knowledge/archive/proofs/propertyb35/BROOKS_CLIQUE_COMPONENTS.md)。这是依赖已发表Brooks定理的纸面引理，未新增Lean；单个五组分量不提供其余20点的分组，不能直接搬用a5双外点异组caller。



## L19. 总度盈余给真实低度边及小击中集

设$k$元超图有$M$边、$n$点且最低度$d$。写$d(v)=d+t_v$、$E=\sum_vt_v=kM-dn$，令$P=\{v:t_v>0\}$、$p=|P|$。有$\sum_{v\in P}d(v)=dp+E$；若此数小于$M$，必有边避开$P$。点对覆盖且$p\ge2$时，等号情形也有一条边避开$P$，因为至少一次边关联重复。

对$p$个正整数盈余，$\sum t_v^2\le(E-p+1)^2+p-1$；结合

$$\sum_{e}\sum_{v\in e}d(v)=nd^2+2dE+\sum_vt_v^2$$

得到实际低总度边。对24点35边最低度七，这把低边模式压为77777或77778。若无全七度边，$P$是5至7点的真实击中集，仅四个盈余谱；不可染时还必须含一条内部五边。五高点的剩余多迹超额只有三，三种整数分拆即覆盖全部输入，[650标签/81轨道原始界全严格](../../../../knowledge/archive/context/propertyb35-paper/round01/twentyfour/high_cover_five/PROOF.md)。这是先压实际全域再做小算术，不需要自由五锁库存。



## L26. 非B横截数与共同二阶矩给真实低度边

任意非B的k元超图都有 $\tau(H)\ge k$。写 $t_v=d_H(v)-d$、$E=kM-dn$、$Q=\sum t_v^2$，直接双计数 $\sum_e\sum_{v\in e}t_v=dE+Q$。若最大盈余点为v、a=t_v，点对覆盖进一步给

$$\sum_{e\not\ni v}\sum_{u\in e}t_u\le(d-1)(E-a)+Q-a^2\le(a+d)(E-a)-a(p-1),$$

其中p是正盈余点数。p<k时，非B又迫有全最小度边。另一方面，若每条边盈余至少s，避开最高k−1点的真实边保证这些最高盈余之和至多E−s。两种同一H上的约束联合，得到[完整低边归约](../../../../knowledge/archive/context/propertyb35-paper/round01/literature-degree/GLOBAL_LOW_EDGE_REDUCTION.md)：24δ7与21δ8都有实际边总盈余≤1（各两种度模式），23δ7≤3（七模式），22δ7≤6。22通过最高第四盈余仅1/2/3的三个解析支闭合，不需表。

这是选择真实五边的共同入口，省掉先选任意五低点再自由扩共度的外层；不是后续修复已经完成。23阈值降到2的单纯聚合尝试，有明确有理分数松弛障碍；不把分数模型当整数超图或目标反例。


## 保留整数度数的Q门：完整短证明

设点对覆盖的简单k元H有v点、M边，k≥2。令a=k−1、b=v−2、δ=ceil((v−1)/(k−1))，取整数D≥δ。置

\[
Z=(D+1)v-kM>0,\qquad
Q=\max_{d\in\{\delta,\ldots,D\}}(ad-b)(D+1-d).
\]

则存在至少Z/Q个度≤D且两两共度1的点，因而Z>(s−1)Q保证s个。所有分母为正：ad−b≥1且D+1−d≥1。

证明：L={x:d(x)≤D}满足Σ_L(D+1−d(x))≥Z。L上的非单位冲突图G有1+deg_G(x)≤ad(x)−b。随机顺序中早于全部邻居的点组成独立集，所以

\[
\alpha(G)\ge\sum_{x\in L}\frac1{1+\deg_G(x)}
\ge\sum_{x\in L}\frac1{ad(x)-b}
\ge\sum_{x\in L}\frac{D+1-d(x)}Q\ge Z/Q.
\]

最后用独立数为整数。∎

六元37点/M66/D13给Z122、Q60；连续二次函数最大值61.25过松，整数最大值60足够保证三锁。这个例子只验选点门，完整染色须随后所有实际迹严格。原完整证明和尾部实际换点另见[诊断包](../../../../knowledge/archive/context/propertyb-m6-67-diagnosis-20261029/DERIVATION_PACKAGE.md)与[整数门独立范围](../../../../knowledge/archive/context/propertyb-m6-67-diagnosis-20261029/integer-lock/REVIEW.md)；诊断包的旧“完整目标未闭”不是最终六元67状态，后继见07。
