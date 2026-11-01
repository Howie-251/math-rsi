# 合作者小 k 材料：向 m(5) 迁移的机制与边界

2026-10-19。本页整理合作者提供的 k=6,…,11 证明材料；原作者的数学归约、证书和归档保持原归属，本页不主张这些机制为本项目新发明。
本次工作是完整读纸面与源码、重放原算术证书，以及限定参数的小型迁移核对；没有启动新研究 Goal。
旧 m(5)≥35 的 Lean Goal 仍 paused，新 m(5)≥36 自然语言 Goal 尚未启动；本页不改变已验收下界或创建 verified claim。
数学阅读标记为 `review_independence: same-family`、`acceptance_status: provisional`。
没有新增 Grok/Gemini 审阅、Lean 验证或公开纪录查新；本机算术通过与这些验收层次分别报告。

## 材料、准确宣称与实际重放

所有宣称均针对任意有限简单 k 元超图，不以点对覆盖、正则性或固定点数为原始假设。
点对覆盖来自最小顶点反例的商约化；补边到恰 M 还须验证候选点数域有 `C(v,k)≥M`。

| k | 合作者宣称下界 | 所证边数预算 M | 本机重放局部型数 | 原材料 |
|---:|---:|---:|---:|---|
|6|m(6)≥65|64|200|[证明](../propertyB_small_k/propertyB_m6_proof.md)／[程序](../propertyB_small_k/propertyB_m6_certificate.py)|
|7|m(7)≥130|129|115|[证明](../propertyB_small_k/propertyB_m7_proof.md)／[程序](../propertyB_small_k/propertyB_m7_certificate.py)|
|8|m(8)≥266|265|1,290|[共同证明](../propertyB_small_k/propertyB_k8_k9_proof.md)／[程序](../propertyB_small_k/propertyB_m8_certificate_v2.py)|
|9|m(9)≥542|541|2,568|[共同证明](../propertyB_small_k/propertyB_k8_k9_proof.md)／[程序](../propertyB_small_k/propertyB_m9_certificate_v2.py)|
|10|m(10)≥1112|1111|28,545|[共同证明](../propertyB_small_k/propertyB_k10_k11_research.md)／[验证器](../propertyB_small_k/propertyB_k10_k11_verified.py)|
|11|m(11)≥2275|2274|70,472|[共同证明](../propertyB_small_k/propertyB_k10_k11_research.md)／[完整归档](../propertyB_small_k/propertyB_k10_k11_bundle.zip)|

合计 **103,190** 个局部参数型，六组原证书均本机退出0、严格界通过；它们不枚举整图。
k6–9使用 Fraction 精确比较；k10–11使用经安全界检查的整数向外舍入。
k10、k11各一条最紧双锁边界另由独立编写的 Fraction 实现复算，共两条；未另做六组全量独立实现。
静态阅读未发现改变这些具体候选结论的实质错误；算术通过仍依赖纸面约化、真实输入与有限分类覆盖。
详细实际范围、命令、时长与日志见 [k6–7](../context/collaborator-small-k-20261019/m6-m7/REPORT.md)、[k8–9](../context/collaborator-small-k-20261019/m8-m9/REPORT.md)、[k10–11](../context/collaborator-small-k-20261019/m10-m11/REPORT.md)。

k10/11 的单独 `verified.py` 依赖同目录 `propertyB_k10_k11_certified.py`，后者只在zip中；不能仅复制前者运行。
复现时把归档完整解压到独立目录，安装 Python≥3.10 与 NumPy，再在解压目录依次执行：

```sh
python3 -B propertyB_k10_k11_verified.py 10
python3 -B propertyB_k10_k11_verified.py 11
```

不使用 `-O`，否则会跳过断言。本机运行限制BLAS/OMP为单线程；实际解包副本与日志保存在上述k10–11报告目录。

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
来源为合作者 [k10/11稿的定理B](../propertyB_small_k/propertyB_k10_k11_research.md)；k8/9稿用其三锁版本。
它是已有 [L2度数／共度预算](PROPERTY_B_REUSABLE_LEMMAS.md) 的有效组合，不重命名为全新基础机制。

可再保留整数r而不对全部实数最优化。由最低度及外部度数，

`r≥max(0,ceil(Z/(D+1−d0)))`，`r≤v`。

对每个r取

`2e_upper=2 floor(min(((k−1)D−v+1)r,(T−1)r−(k−1)Z,r(r−1))/2)`。

这分别使用逐点excess、总度预算及简单图界；负上界的r不可能，其余r保证 `ceil(r²/(r+2e_upper))`。
对留下的r取最小即得普适保证；Z≤0时保留r=0且保证0。留下的r仅满足必要条件，不宣称都有真实超图。
本轮固定 `k=5,M=35,v=18..25,D=d0..15,s=2..10` 的整数扫描，**没有降低连续判据所得的任何最小D**。
完整表及全部r分数见 [pilot说明](../context/collaborator-small-k-20261019/m6-m7/K5_SELECTION_PILOT.md)／[JSON](../context/collaborator-small-k-20261019/m6-m7/K5_SELECTION_PILOT.json)。

## 二、整数向外舍入：把有理算术放在正确方向

固定每个位置h，令A_h、B_h为边终止／起始概率和，C_h为全部互异有向类型对的记账上界。
单交临界对覆盖失败；已知实际坏对不能临界，对其最少可扣权D_h有

`P(Fail)≤Σ_h min(A_h,B_h,C_h−D_h)`。

取统一尺度S（作者实现为`2^52`）。对非负概率p，整数 `ceil(Sp)` 给上界，`floor(Sp)` 给下界。
用上取整系数形成 `Â_h,B̂_h,Ĉ_h`；其乘数必须是非负整数重数，特别同型有向对数为 `ℓ_T(ℓ_T−1)`。
对k≥3，真实link给坏对下界 `q=ceil(((k−1)d−(v−1))/(k−2))`；每无序类型格容量为 `C(ℓ_T,2)` 或 `ℓ_Tℓ_U`。
每格扣除权取两个方向的下取整之和，按容量从最轻格装满q，得整数 `D̂_h`。
任一真实q坏对集合可放入这些容量格；对其逐项下取整，再对所有合法装填取min，所以 `D̂_h≤S D_h`。
故 `Ĉ_h−D̂_h≥S(C_h−D_h)`；A、B同向上界，min的单调性保证

`Ucert=Σ_h min(Â_h,B̂_h,Ĉ_h−D̂_h)≥S Σ_h min(A_h,B_h,C_h−D_h)`。

因此纯整数比较 **`Ucert<S`** 即足够；没有把浮点近似当证明。
必须保留零权格及其容量：q>0未必有正扣除，扣了C也未必改变该位置活跃的min项。
作者缓存每(v,锁数)权表并向量化类型重数；NumPy int64仅在实际中间积和界小于`2^63−1`后使用，最终和用Python整数。
安全界应覆盖减对角前的`M²`正项和；不只检查最终`M(M−1)`，更不能只看最终结果未溢出。
这项实现策略可先迁移到已有k5算术，不解决锁点存在或分类覆盖。
带负系数的多布局dual不能直接套“所有系数上取整”：须按符号定方向并保留同一实际坏对与配额，另证整体支配。
上述数学机制分别已有 [L3失败计数、L6 link坏对、L7容量弱对偶](PROPERTY_B_REUSABLE_LEMMAS.md)；新增价值主要在算术实现组织。

## 三、结构压缩优先，以及 k=5 的具体瓶颈

两两单位共度的锁集，其大小≥2的真实迹各出现一次，并把锁点完全图的边分解成若干完全子图。
给定这些块与各锁点度数，单锁重数和空迹重数自动恢复；三锁恰为一条三元块或三条二元块两型。
这是 [L4实际迹、L9单位共度packing](PROPERTY_B_REUSABLE_LEMMAS.md) 的紧凑输入方式；锁数增加后仍须证明分类完备。
合作者按点数段只用0／1／2／3锁，先证明选点再验全部度数组；成功的主要压缩发生在算术之前。
不能因k10/11三锁够用，便推断k5的实际困难也是加速相同三锁表。

对 `k=5,M=35,v=25,D=7`，`Z=25,T=9`，连续界`400/81>4`保证5个单位锁，有限r加强仍只保证5。
更一般地，此v的s=6判据差值恒为

`16Z−5T²=−5(4(D+1)−33)²≤0`。

故对任意D，这一严格充分判据均不给6个锁；这不是实际不存在六单位点的结论。
对v=18，三锁判据差值恒为

`8Z−T²=−16(D+1−17/2)²−500<0`。

本轮D≤15的有限r版也不能保证两个单位锁；不能据此否定18点其他染色方法。
此外，25点三名七度锁固定在中央位置11、12、13，两种迹型按同一证书精确复算，分别为

`U_separate=29451/24871>1`，`U_triple=4214/3553>1`。

这些分数由k10/11阅读任务的独立Fraction实现得到，见 [实际复算](../context/collaborator-small-k-20261019/m10-m11/INDEPENDENT_CHECKS.json)。
它们定位了这一固定布局三锁证书的失败边界，不排除其他布局或加强的三锁估计；既不是不可染反例，也不说明m(5)≥36为假。
因此保留现有九／十锁结构、最大单位集分流和共享真实坏对的多布局方法；先把向外舍入与缓存迁到实际活跃算术，再衡量收益。
已有 [L1–L4、L6–L8](PROPERTY_B_REUSABLE_LEMMAS.md)、[研究经验](PROPERTY_B_RESEARCH_LESSONS.md) 与 [失败地图](PROPERTY_B_FAILURE_ATLAS.md) 继续作为主线，不因材料整理重启或替换。
本页交付的是可复用推导、实现方向及明确失败边界，尚无新的完整36下界证明。
