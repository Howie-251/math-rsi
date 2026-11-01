# Property B 的通用数学库存：33、34 与 35 候选之间真正可复用的部分

2026-10-14。本文按实际源码、既有构建记录和初等推导整理；本轮没有启动 Lean 构建、新分类或研究 Goal。所有路径均相对 `aris4math/`。T32、T33、T34 分别是“至多 32、33、34 边可染”，对应下界 `m(5)≥33、34、35`。前两者已有端到端验收；T34 的文字候选已写齐，Lean 尚未完整装配。下列已编译的通用引理不会因 T34 尚未完成而失效，但也不代替 T34。

**最值得固定的成果不是三个常数，而是：同一超图上的精确计数接口、可组合的坏对下界、以及证明局部分类覆盖真实输入的方法。** 有些已经是任意有限类型上的 Lean 定理；有些目前仍以 `Simple5Hypergraph` 为宿主，但数学证明不依赖 5；另有部分参数推广可用下文短证明固定为纸面引理。不能把这些层次混写。

## 推荐优先固定的五组定理

|优先组|为什么值钱|当前形式化范围|
|---|---|---|
|共享实际坏对向量的多布局弱对偶|不再给每个布局分配互相矛盾的最坏坏对；可跨局部形状复用|纯代数核心已任意有限索引与有理数；实际 Property B 接口任意点数、锁数、边数，宿主仍五元|
|避锁 link 坏对配额及重叠修复|把“有多少坏对”细化为“哪些槽必须有坏对”，并合法合并重叠配额|任意有限顶点、避锁集合和配额数，宿主五元；r≥3 版本有下文短证明|
|真实迹的恢复、投影、增锁与完整容量分类|每次增加锁点不重建表示；将数字表接回同一实际超图|锁数、点数均任意，宿主五元；抽象容量枚举本身与超图无关|
|整数度数及共度超额驱动的选点|先知道哪些锁点必然存在，再决定该算什么；减少伪输入|基本计数和超额为任意有限五元超图；一般 r 与一般图最大度的包装尚未作为统一 Lean 声明导出|
|共同环境的删点计数与结构相容性|用整除或总预算排除“每个局部都坏”的组合，避免逐个升级概率表|删点计数已任意有限块族；七点结论已 Lean；一般整除推论见下文|

此外，随机贪心失败覆盖与锁定联合排列计数是这五组依赖的成熟基础，应该保留稳定接口，毋须为下一常数重写。

## 1. 最小反例约化：通用机制与数值窗口必须分开

### 1.1 边上单射映射与染色拉回

**命题。** 设 H 是有限简单 r 元超图，f:V→W 在每条边上单射。以 f(e) 为边并去重得到 H′。则 H′ 仍 r 元，|E(H′)|≤|E(H)|，且 H′ 具有 Property B 蕴含 H 具有 Property B。

**证明。** 边上单射保留边大小；去重不增加边数；将 H′ 的染色沿 f 拉回，每条原边的两种颜色仍出现。

现有 Lean：`formal/Aris4Math/Reduction.lean` 中 `pushforward_edge_count_le`、`propertyB_pullback`、`propertyB_relabel_iff`。它们对顶点类型和映射通用，**宿主写死 Simple5Hypergraph**；r 元版本不是已经存在的导出声明。

### 1.2 任意边数预算下的点对覆盖约化

**纸面参数定理。** 对 r≥2、M≥0，若存在有限简单 r 元、≤M 边的不可染超图，则存在同样边数预算内、顶点数最少的不可染超图 K，且 K 每个不同点对均落在一条边中。

**证明。** 若 x,y 不共边，就合并它们。每条边上仍单射，边数不增，染色可拉回，而顶点数严格下降，矛盾。M 在论证中完全是参数。

现有 Lean 的合并核心 `smaller_counterexample_of_uncovered_pair` 不含 32/33/34 常数；选最小反例及最后 Target 包装分别在 `Reduction.lean`、`ThirtyThree/Reduction.lean`、`ThirtyFour/Reduction.lean` 实例化了边数。**建议以后抽出 M 参数包装，而非复制三份证明；本次没有改动源码。**

补边到恰 M 边，需要 `binom(v,r)≥M`，不能无条件补。对于逐档推进还有另一条直接事实：已证明 ≤M−1 边均可染时，任何 ≤M 边反例自然恰有 M 边，不必额外补边。这是参数层事实，未声称已改写当前约化。

### 1.3 整数窗口

点对覆盖给出

\[
\delta(H)\ge \left\lceil\frac{v-1}{r-1}\right\rceil,\qquad
v\left\lceil\frac{v-1}{r-1}\right\rceil\le rM.
\]

一般式是下节计数的直接推论。对五元、M≤36，若 v≥26，则每点度至少 7，`5M≤180<26×7=182`，故 v≤25。**这是可证明的下一档纸面推论；现有 T34 导出 `ThirtyFour.card_le_twenty_five` 的显式前提仍是 M≤34。** 当 M=37，单凭这一论证已不能排除 v=26。

“19–25”中的下端 19 来自专门的小点数可染证明，不是合并定理。现有 T34 的 ≤18 点证明使用 17/18 点的严格重叠计数，不能未经重算就用于 35 边。通用约化可复用，固定窗口不可无限沿用。

## 2. 度数、共度超额与统一选点预算

设 H 有 v 点、M 边，d(x) 为点度，λ(x,y) 为不同点共度。

### 2.1 精确恒等式

对任意 r 元超图，双计数给出

\[
\sum_x d(x)=rM,\qquad \sum_{y\ne x}\lambda(x,y)=(r-1)d(x).
\]

若还点对覆盖，则定义

\[
\epsilon_x=(r-1)d(x)-(v-1)
 =\sum_{y\ne x}(\lambda(x,y)-1)\ge0.
\]

于是非单位共度伙伴数至多 εx。更一般，对 t≥1，满足 λ(x,y)≥t+1 的伙伴数至多 `floor(εx/t)`。

**证明。** 一条含 x 的边贡献 r−1 个其他点；点对覆盖使各项 λ−1 非负；每个 λ≥t+1 的伙伴至少消耗 t 单位超额。

现有 Lean `Structure.lean`：`sum_degrees`、`sum_codegrees_erase`、`pairCovering_degree_bound`、`sum_codegree_excess`、`badPartners_card_le_excess`。这些对 v、M 无固定范围，五元版本已验收。一般 t 的包装和一般 r 版本是上述短证明支持的纸面推论，未冒充已有 Lean 导出。

### 2.2 低度点数量

若所有点度至少 d，令 Sd={x:d(x)=d}，则

\[
|S_d|\ge \max(0,(d+1)v-rM).
\]

**证明。** `rM=Σd(x)≥d|Sd|+(d+1)(v−|Sd|)`。

对五元且最小度≥6：

|点数|M=32|M=33|M=34|一般式|
|---|---:|---:|---:|---|
|24|至少 8 个六度点|至少 3 个|可能没有|至少 max(0,168−5M)|
|25|至少 15 个六度点|至少 10 个|至少 5 个|至少 max(0,175−5M)|

这张表直接解释为何不能把旧概率表换一个边数就使用。M=35 时，25 点的六度点保证也消失。该事实不是下一下界不存在，只说明旧选锁入口可能完全失效。

### 2.3 从超额到可选锁点

在某个候选点集 S 上连边表示 λ≥2。若每点在 S 内的此类邻居数≤Δ，则贪心每次删去所选点及其至多 Δ 个邻居，可取得至少 `ceil(|S|/(Δ+1))` 个两两单位共度点。

Lean `Structure.exists_pairwise_avoiding_subset` 已对任意对称关系实现 **Δ=1** 版本，前提 `2k≤|S|`。另有 `ThirtyFour/TwentyFiveSelection.lean` 的 `unit_subset_of_bad_bound`：k、Δ 为参数，假设所选 S 中每点的全局非单位共度伙伴数≤Δ，且 `(k−1)(Δ+1)<|S|`；结论选出 k 个单位共度点。不过该声明的宿主仍固定 `Simple5Hypergraph (Fin 25)`。任意有限图上的一般 Δ 包装有上述初等证明，未声称项目已导出这一最一般版本。

ε=0、1 的极端情况也值得单列：五元 25 点的六度中心与所有其他点共度 1；五元 24 点的六度中心恰有一个共度 2 的伙伴，其他伙伴共度 1，因而恰有一对入射边在中心外相交。**“唯一坏对”只来自超额恰 1，不能转用于 23 点六度中心，其超额为 2。**

## 3. 通用的随机贪心失败与锁定排列计数

### 3.1 失败必有临界单交边对

对任何有限 r 元超图，r≥2，给定顶点顺序，按现有红→蓝贪心扫描。若输出失败，则存在不同边 A,B 及 x，使

\[
A\cap B=\{x\},\quad x=\max A=\min B.
\]

**证明。** 算法最终没有全红边；取一条全蓝边 B 的最早点 x。x 被翻蓝的见证边 A 在 x 时仍全红，x 是 A 最后点，因此 A 的其余点在 x 前，B 的其余点在 x 后。

Lean `Greedy.uniform_failure_covered`、`failureAt_covered`、`failure_event_cover` **已经以一般 uniformity 参数 n≥2 表述**，不是只有五元。最后返回项目 `PropertyB` 的包装仍是 Simple5。

反向不成立：存在临界对不意味着贪心一定失败。不能把上界工具改称等价判据。

### 3.2 无放回联合计数

锁定 s 个不同顶点到 s 个不同位置；余下 N=v−s 个点均匀双射到自由位置。对不同的自由点集 A,B，要求其像分别落入不相交自由位置集 L,R。设 |A|=a、|B|=b、|L|=ℓ、|R|=h，则

\[
\Pr(\sigma(A)\subseteq L,\sigma(B)\subseteq R)
=\frac{\binom{\ell}{a}\binom h b}{\binom N a\binom{N-a}b}.
\]

A、B 不交保证 a+b≤N。公式来自先选 A 的位置，再在余位放 B；不是将两个边事件当成独立事件。

Lean `JointCounting.locked_joint_subset_ratio`、`card_locked_joint_subset` 对 **任意有限类型 α 和任意有限锁点索引 ι** 成立，根本不要求超图。`Counting.card_prescribed_images` 给锁定样本大小 N!。这些是真正可直接跨领域复用的定理。

`ConditionalUnion.propertyB_of_position_bounds` 将真实临界事件概率上界接回原染色。具体 `Numeric.edgeWeight`、`pairWeight` 中仍出现 `5−|T|`，所以不能因计数底层通用就宣称整个数值概率引擎已支持任意 r。

## 4. 真实迹重数：精确恢复与投影

取不同锁点 f:[s]↪V。对 T⊆[s] 记

\[
\mu_f(T)=|\{e\in E:e\cap f([s])=f(T)\}|.
\]

### 4.1 上包含计数与精确重数恢复

记 `u(T)=|{e:f(T)⊆e}|`。则

\[
u(T)=\sum_{U\supseteq T}\mu_f(U),\qquad
\mu_f(T)=u(T)-\sum_{U\supsetneq T}\mu_f(U).
\]

在 |T|≤2 时，u 分别就是 M、点度、共度。因此给出所有 |T|≥3 的精确重数，再给出总边数/点度/共度，即可唯一恢复全部重数，包括空迹。

Lean `ThirtyThree/MultiLockRecovery.lean` 的 `count_add_larger`、`actual_recovered`；任意 s,v，仍 Simple5。恒等式本身不依赖 uniformity；`count_eq_zero_of_large` 的阈值 5 依赖五元。自然数减法之所以合法，是从真实分拆等式得到，不是任意整数表都自动有非负恢复。

### 4.2 投影与换标号

若 g:[t]↪[s] 选出部分锁点，则

\[
\mu_{f\circ g}(T)=\sum_{U:g^{-1}(U)=T}\mu_f(U).
\]

对置换 π:[s]≃[s]，

\[
\mu_{f\circ\pi}(T)=\mu_f(\pi(T)).
\]

**证明。** 每条边在新标签下的迹是旧迹的逆像；按旧纤维不交求和。删除锁点并没有删除边，空迹尤其必须保留。

现有 Lean：`ThirtyFour.LockProjection.count_comp`、`count_le_projected`、`LockRelabel.count_comp_perm`。s、t、v 均任意，Simple5 宿主；数学内容适用于任意有限集合族。编译依据见 `middle-lean/PERFORMANCE_NOTES.md` r18，以及 r39 构建重放。

## 5. 增锁定理与容量剪枝完整性

已有锁集合 S，再添加真实新点 x∉S。令

\[
p_T=|\{e:e\cap S=T,\ x\in e\}|.
\]

则新迹重数完整地由

\[
\mu'(T)=\mu(T)-p_T,\qquad
\mu'(T\cup\{x\})=p_T
\]

决定，并且

\[
0\le p_T\le\mu(T),\qquad
\sum_Tp_T=d(x),\qquad
\sum_{T\ni i}p_T=\lambda(i,x).
\]

r 元时 |T|≥r 蕴含 pT=0。若表只保存非空 T，则

\[
p_\varnothing=d(x)-\sum_{T\ne\varnothing}p_T.
\]

**证明。** 同一旧迹纤维按是否含 x 分成两个不交子族；其余等式都是这组纤维对 x 入射边及 (i,x) 共边的分拆。

Lean：`LockExtension.count_split`、`promotion_le_old`、`sum_promotion_degree`、`count_new_singleton`；`PromotionCatalog.sum_promotion_codegree`、`actual_mem_of_old`；`PromotionReconstruction.extend_actual`。全部支持任意 n,v，宿主 Simple5，r19/r22 及实际 caller 构建已通过。

### 5.1 抽象容量枚举定理

有有限条目 (ai,bi)，非负整数成本 `c(ai,j)`，容量 Cj。逐项选择 `0≤xi≤bi`，仅在当前成本≤剩余容量时递归。任何满足

\[
0\le x_i\le b_i,\qquad\forall j,\ \sum_i c(a_i,j)x_i\le C_j
\]

的真实分配必在输出列表中。

**证明。** 对条目列表归纳：真实首项符合当前容量，扣除它后的真实尾部仍符合剩余容量，所以未被剪去。

`BoundedAllocations.mem_enumerate` 已对任意条目类型 α、任意有限容量索引 β 形式化，与超图无关。`decode_actual` 给读回正确性；实际提升使用 `PromotionCatalog.actual_mem` 接入该定理。

这套东西证明“所有实际输入都留下”，不是“列表中每个整数表都可实现为超图”。后者不需要强行证明：在覆盖真实输入的松弛域上逐项证明可染足够；松弛域中失败的一项却不能当成实际反例。

真实连接还要满足：列出所有可能非零迹；具体 `PromotionCatalog.listed_budget` 要求列出的旧类型无重复，才能把列表预算改写为类型 Finset 求和并以列出量≤实际容量；空提升真实恢复；新旧锁确实不同。这个无重复条件属于实际计数/预算连接，**不是** `BoundedAllocations.decode_actual` 的前提：读回允许重复条目，它们存储同一个 actual value。仅验证保存的若干代表不具有这种完备性。

## 6. 避锁坏对配额：可推广到 r≥3

设 H 简单 r 元，r≥3；固定中心 x 和 R⊆V\{x}。令 F_R 是包含 x 且避开 R 的边族，f=|F_R|，u=v−1−|R|。令 bR 为 F_R 中不同无序边对 {e,e′}、满足 `(e\{x})∩(e′\{x})≠∅` 的数量。则

\[
(r-1)f\le u+(r-2)b_R,
\]

因此

\[
b_R\ge\max\left(0,\left\lceil\frac{(r-1)f-u}{r-2}\right\rceil\right).
\]

**证明。** 删去 x 后得到不同的 (r−1) 元集合。若其余点的入射数为 az，则 `Σaz=(r−1)f`，而 `az≤1+binom(az,2)`。双计数得 `Σbinom(az,2)=Σ{e,e′}|(e∩e′)\{x}|`；不同 link 边交大小≤r−2，每个相交对至多贡献 r−2。

**不要求点对覆盖，也不要求 R 由锁点构成。** 这比某一具体 24 点或 23 点引理更通用。

当前 Lean `ThirtyThree.AvoidedLink.avoided_bad_pair_budget/lower` 已实现 r=5，任意 V,x,R；`RefinedDeletion.avoided_dual_lower` 把它接到真实有向坏对权重。一般 r 是上述已给出证明的纸面推广，未有通用 uniformity 的 Lean 声明。r=2 时分母为零，不适用此分式；简单图的中心 link 是互异单点，此时 f≤u。

简单性不可省：如果允许重复相同边，不同副本的 link 交大小可以为 r−1，r−2 的上界失效。

## 7. 重叠配额的容量修复弱对偶

**纯代数定理。** 取有限槽集 S、配额集 Q。真实坏对数或其松弛向量 z 满足 `0≤zs≤cs`，以及 `Σs aqs zs≥qq`。对任意非负乘子 δq，有

\[
\sum_s w_s z_s\ge
\sum_q\delta_q q_q-
\sum_s c_s\max\left(0,\sum_q\delta_q a_{qs}-w_s\right).
\]

**证明。** 先将每个配额乘 δ 再求和。逐槽有 `(Σδa−w)z≤max(0,Σδa−w)c`，相加即可。

Lean `ThirtyFour.MixedLayoutDual.quota_repair` 已对任意有限 S,Q、**有理数数组**成立；a 和 w 本身无非负前提，z 的非负、容量以及 δ 非负才是精确条件。它是有限弱对偶，不要求 LP 最优解、强对偶或求解器正确。

用于超图时，槽必须来自同一实际坏对集合，容量必须是真实上界。无序槽 T≠U 的容量是 μTμU，同槽是 binom(μT,2)；若用有序槽则同槽是 μT(μT−1)，双向权重须按相同约定配套。`RefinedDeletion.dual_bad_weight_lower` 用每方向半罚项避免重扣。

r-uniform 推广不改变纯代数定理；只须重证该问题中的真实配额和计数连接。换成实数的数学证明也相同，但当前 Lean 声明是 ℚ，不能称已对任意有序域形式化。

## 8. 共享真实坏对的多布局定理

对同一 H 固定一组锁点和真实坏对数据 z。每个布局 l 的已证明失败上界设为

\[
U_l(z)=F_l+\sum_j\min\{a_{lj},c_{lj}-D_{lj}(z)\},
\qquad D_{lj}(z)=\sum_s w_{ljs}z_{js}.
\]

这里 a 可以已经是 A、B 两个端点界的最小值。取 γl≥0、Σγ=1，以及 `0≤βlj≤γl`。逐位置有

\[
\gamma_l\min(a,c-D)\le(\gamma_l-\beta_{lj})a+\beta_{lj}c-\beta_{lj}D.
\]

把同一 z 的合并权重 `Σl βlj wljs` 送入第 7 节配额修复，得到每个中心的下界 Lj。若

\[
\sum_l\gamma_lF_l+
\sum_{l,j}((\gamma_l-\beta_{lj})a_{lj}+\beta_{lj}c_{lj})-
\sum_jL_j<1,
\]

则 `ΣγlUl(z)<1`，所以至少有一个布局 U<1，从而 H 可染。

Lean：`MixedLayoutDual.min_split/average_le/exists_strict_of_average` 是抽象有限有理数定理；`MixedLayoutCounts.mixed_deduction` 绑定实际坏对；`MixedLayoutApplication.propertyB_of_mixed_layouts` 最终返回原 `PropertyB H`。实际应用对 n,v,edgeCount 参数化，仍为 Simple5，且当前具体接口要求 `emptyPairCap=none`；不能无改动与额外空迹 pair cap 叠加。

r39 日志重放记录上述声明及标准三公理。该通用实际接口在 T34 的已完成分支中已经使用，**并非只剩一个未被调用的数值 lemma**。

量词顺序为 `∀H，固定真实数据，选择布局，再随机排列余下顶点`。不能抽样后选择锁点来沿用条件概率。更不能为每个布局引入彼此独立的 z_l 却声称利用了同一 H 的约束。

这一组是最值得保留的改进：成功条件来自多个旧界不能同时最坏，而不一定来自再增加一两个锁点。它仍只给充分条件；未找到 γ、β、δ 不代表没有好布局。

## 9. 单位共度使大迹成为线性块族

若所选 s 个锁点两两共度恰为 1，则每个大小≥2 的迹重数至多 1；两个不同的非零大迹交至多一个点。否则有两个不同实际边都包含同一锁点对，与共度 1 矛盾。

一般 s 时，大迹还满足简单的 pair-packing 预算

\[
\sum_{T:\,|T|\ge3}\binom{|T|}{2}\le\binom s2.
\]

每个锁点对最多被一个大迹使用。这是纸面普适推论；不是“五锁最多两个”的任意 s 推广。

s=5 时大小≥3 的线性块族最多两个成员：两个不同大迹的并已是全部五点；第三个若分别只交前两者至多一点，总大小≤2，矛盾。于是完整带标签域为 1 个空族、16 个单大迹族、15 个兼容双三元族，总计 32。

Lean `ThirtyThree/FiveLockClassification.lean`：`actual_count_le_one`、`actual_intersection_le_one`、`admissible_card_le_two`、`admissible_in_table`、`actual_recovered_in_table`。32 型结论固定 **五个锁点且 pair codegree=1**，不固定 v 或 M。换成六锁、非单位共度、或允许重复大迹，必须更换分类域；不可沿用布尔大迹表。

## 10. 删点计数与“局部坏型无法同时成立”

对任意有限点集 W、任意有限块族 B，有

\[
\sum_{x\in W}|\{B\in\mathcal B:x\notin B\}|
=\sum_{B\in\mathcal B}|W\setminus B|.
\]

Lean `SevenPoint.absent_incidence_count` 已完全一般；不要求线性、uniformity 或超图。

**通用整除推论。** 若 |W|=N，每个块均包含于 W 且大小 q<N，并假设每次删除一点后仍完整保留的块数均等于 t，则

\[
(N-q)|\mathcal B|=Nt.
\]

因此若 `(N−q) ∤ Nt`，必有一个删点结果的完整块数不等于 t。证明只要代入上述恒等式。现有 Lean `exists_deletion_not_two` 是 N=7、q=3、t=2 的实例：4 不整除 14。一般整除推论本次给出完整纸面证明，未新建 Lean 声明。

这提供可重复使用的研究模式：所有局部迹必须来自同一共同块族；先写共同的总和/守恒式，再检查所有局部坏残型能否同时满足。**不能直接宣称任意残型集合都被这个一阶恒等式排除。** 若残型统计包含新产生的迹、被删除的点对或重数合并，必须先证明其与该共同块族统计的对应；“完整保留的块”不是任意一种“删点后的迹”。

## 最后需要保留的边界

1. 稳定通用层：真实有限集合计数、贪心临界事件、容量完整性、坏对弱对偶；这些不依赖下界常数 33/34/35。
2. 参数实例层：度数分支、选锁保证、重复共度图和具体残型；每次边数变化都要重证适用范围。
3. 数值证书层：布局、非负乘子、有限分类表与严格差额；可由程序寻找，但必须连到第 2 层的真实输入，并由第 1 层给出染色。
4. 不能从三个成功实例推断“以后都能靠相同锁点数解决”。更不能从 T34 文字稿完整推断 T34 端到端形式证明已完成。

建议先把以上已有声明做成索引和少量明确命题包装，让下一分支直接调用。通用 r 元版本应由真实新用途驱动，避免为了抽象而重构已经冻结的 T32/T33 工程。数学内容足以整理成一章工具引理；是否属于新的文献贡献须另做出处判断，本清单不宣称原创性。
