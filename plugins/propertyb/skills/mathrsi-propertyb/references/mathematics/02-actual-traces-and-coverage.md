# 真实迹、共同投影与完整分类

## 实际caller的起点

固定同一H和单射锁标号f。先定义每条原边的精确锁迹，再定义μ为实际边数，包含数u为实际包含关联；不要先自由给一份整数μ再称其“真实”。L4的恢复公式证明总边数、度数与共度如何产生完整μ，特别包括空迹与单迹。

典型扩锁caller应先选真实外点z，再置 $p_T=\#\{e:e\cap S=f(T),z\in e\}$。证明 $p_T\le\mu_T$、总度和共度等式后，用L5容量枚举完整性得到实际p在目录里，再恢复新μ。若对新目录取代表，先有有标号完整域，再提供具体置换运输f、度数、迹、位置和证书；等度角色或标记中心须保持。仅检查代表不等价不是覆盖证明。

已有 `MultiLockRecovery.actual_recovered` 与部分末端写死33边的包装不是同一个范围；调用前打开声明。下方源码均来自保留的archive；本次只检索并阅读具体声明，没有重新执行Lean。

## 选点、恢复、投影和换标签的数学正文
## L4．真实迹的四个恒等式：恢复、投影、重标号、增锁

设 \(f:[s]\hookrightarrow V\) 是实际锁点，对 \(T\subseteq[s]\) 定义

\[
\mu_f(T)=\bigl|\{e\in E:e\cap f([s])=f(T)\}\bigr|.
\]

以下等式对一般有限边族成立，既不需要点对覆盖，也不需要特殊边数 \(M\)。

**恢复。** 令 \(u(T)=|\{e\in E:f(T)\subseteq e\}|\)，则

\[
u(T)=\sum_{U\supseteq T}\mu_f(U),\qquad
\mu_f(T)=u(T)-\sum_{U\supsetneq T}\mu_f(U).
\]

每条包含 \(f(T)\) 的边有唯一实际迹 \(U\supseteq T\)，故第一式由互斥分拆得到；把 \(U=T\) 一项移到左边，得到第二式。总边数、点度和共度分别给出 \(u(\varnothing)\)、\(u(\{i\})\)、\(u(\{i,j\})\)；给定所有大小至少3的迹的真实重数后，依大小递减就能恢复全部迹。自然数减法的无截断性来自该集合分拆等式，不能只依赖一个计算结果看似非负。

**投影。** 对单射 \(g:[t]\hookrightarrow[s]\)，

\[
\mu_{f\circ g}(T)=\sum_{U:\,g^{-1}(U)=T}\mu_f(U).
\]

旧迹为 \(U\) 的边在小锁集上的迹恰为 \(g^{-1}(U)\)，再按这些互斥旧迹求和，即得投影式。

**重标号。** 对置换 \(\pi:[s]\simeq[s]\)，\(\mu_{f\circ\pi}(T)=\mu_f(\pi(T))\)。这是投影式在双射时的单项情形。要固定置换方向；比较排序后的向量并不能替代此等式。

**增锁。** 取 \(z\notin f([s])\)，令 \(p_T\) 为旧迹等于 \(T\) 且含 \(z\) 的边数，则

\[
0\le p_T\le\mu_f(T),\quad
\sum_Tp_T=d(z),\quad
\sum_{T:\,i\in T}p_T=\lambda(f(i),z).
\]

旧迹为 \(T\) 的边按是否含 \(z\) 分成两族，故新迹重数分别为 \(\mu_f(T)-p_T\)（不含新锁点）和 \(p_T\)（含新锁点）。按所有旧迹求和，恰数全部含 \(z\) 的边；仅对含 \(i\) 的旧迹求和，恰数同时含 \(f(i),z\) 的边。这也证明了上面的度数与共度等式。特别地，

\[
p_{\varnothing}=d(z)-\sum_{\substack{T\subseteq[s]\\T\ne\varnothing}}p_T.
\]

在 \(r\) 元情形，\(|T|\ge r\) 时 \(p_T=0\)：否则该边包含 \(f(T)\) 和不同于这些锁点的 \(z\)，大小至少 \(r+1\)。

所有证明都由同一实际边族按互斥条件分拆得到；投影和增锁不能换成彼此无关的“可行向量”。这是跨多个局部视图使用共同约束的根基。

五元 Lean 接口：[MultiLockRecovery.lean](../../../../knowledge/archive/formal/Aris4Math/ThirtyThree/MultiLockRecovery.lean) 的 `count_add_larger`、`actual_recovered`；[LockProjection.lean](../../../../knowledge/archive/formal/Aris4Math/ThirtyFour/LockProjection.lean) 的 `count_comp`；[LockRelabel.lean](../../../../knowledge/archive/formal/Aris4Math/ThirtyFour/LockRelabel.lean) 的 `count_comp_perm`；[LockExtension.lean](../../../../knowledge/archive/formal/Aris4Math/ThirtyFour/LockExtension.lean) 的 `count_split`、`promotion_le_old`、`sum_promotion_degree`、`count_new_singleton`；[PromotionCatalog.lean](../../../../knowledge/archive/formal/Aris4Math/ThirtyFour/PromotionCatalog.lean) 的 `sum_promotion_codegree`、`actual_mem_of_old`；[PromotionReconstruction.lean](../../../../knowledge/archive/formal/Aris4Math/ThirtyFour/PromotionReconstruction.lean) 的 `extend_actual`。锁数和点数是参数，一般 r 还不是这些实际接口的导出范围。另须区分同文件的末端包装 `realizes_recovered`：它仍固定33边；不能因基础恢复通用，就用该包装直接处理34边。

**2026-10-19单位星实例。** 若多个选点各与同一中心共度1，则过中心边在邻点上的非空迹构成同一集合划分；非中心库存由包含数扣去这一划分后作莫比乌斯反演恢复。完整一般k/d证明见[UNIT_STAR_RECOVERY](../../../../knowledge/archive/proofs/propertyb35/UNIT_STAR_RECOVERY.md)。多个投影必须共享同一个划分与包含数，19点δ8已通过这一条件将残域压到33型。选至少5邻点时仍须块大小≤k−1，不能遗漏边大小约束。



## L5．带容量递归生成可以成为完整分类的证明

给定有限条目列表 \(((a_i,b_i))_{i=1}^n\)、有限容量索引 \(J\)、非负整数成本 \(c_{ij}\) 和容量 \(C_j\)。递归在每个条目选择 \(0\le x_i\le b_i\)，若任何 \(j\) 的本步消耗超过剩余容量就剪去，否则扣去消耗继续。

**完整性命题。** 任何同时满足逐项上界和 \(\sum_{i=1}^n c_{ij}x_i\le C_j\)（每个 \(j\in J\)）的实际分配，都出现在该递归输出中。

证明对列表归纳。空列表的唯一分配被保留。非空列表的实际头项满足 \(0\le x_1\le b_1\)，且由非负性及总预算，\(c_{1j}x_1\le C_j\)。因此该头项不被剪去；尾项满足 \(\sum_{i=2}^n c_{ij}x_i\le C_j-c_{1j}x_1\)，由归纳假设被保留。这个证明利用非负整数成本，不能将同一剪枝无证明地移植到负成本。

[BoundedAllocations.lean](../../../../knowledge/archive/formal/Aris4Math/ThirtyFour/BoundedAllocations.lean) 的 `mem_enumerate` 已对任意条目类型、有限容量类型证明这一方向。其输入为 `value : α → ℕ`，重复标签取同一 value；描述任意逐项分配时可改用唯一条目索引实例化。`decode_map`、`decode_actual` 证明函数读回。读回本身允许重复条目，因为它们取同一实际 value；若 caller 把列表求和改写成类型 Finset 求和，则仍须核对重数或去重条件。

这个定理只证明**合法实际分配没有漏掉**，不宣称所有生成行都对应真实超图，也不宣称输出无重复。松弛域全部通过足以应用；其中有未过行时，要判断它可否由真实对象实现。将本引理与 L4 组合，才能从“表已生成”走到“任意实际 H 已被覆盖”。



## L9．单位共度把大迹压成线性块族

若 s 个锁点两两共度恰为1，则每个大小≥2的迹重数至多1，两个不同非零此类迹的交至多一点。否则同一锁点对会同时落入两条不同实际边，与共度1矛盾。特别地，大小≥3的迹族满足

\[
\sum_{T:\,|T|\ge3,\ \mu(T)>0}\binom{|T|}{2}\le\binom s2.
\]

证明是每个锁点对最多被一个大迹使用。

**五锁推论。** s=5 时，大迹族至多两个成员。若存在两个，它们必须是交一点的三元集，并集为全部五点；第三个若与它们分别交至多一点，总大小≤2，矛盾。因此完整带标签域为：空族1种、单大迹16种、两兼容三元迹15种，共32种。

[FiveLockClassification.lean](../../../../knowledge/archive/formal/Aris4Math/ThirtyThree/FiveLockClassification.lean) 的 `actual_count_le_one`、`actual_intersection_le_one`、`admissible_card_le_two`、`admissible_in_table`、`actual_recovered_in_table` 已实现五锁分类及实际调用。32型是大迹族的分类，不是完整超图的分类；次数、空迹和单迹还要由 L4 恢复。换成六锁、非单位共度或允许重复大迹，不能沿用“至多两个”或布尔表。

**六锁的具体边界例。** 在1…6上，123、145、246、356四个三元集两两交一点。各用互不相同的新点补成五元边，再把尚未覆盖的点对16、25、34分别用三个独有新点补成五元边。得到七条简单五元边，六个锁点之间每个点对共度恰为1，却有四个大迹。因此“至多两个”在六锁上确实为假；该例反驳的是错误推广，不是 Property B 主命题。



## L16．由真实迹选择外点，比要求全部外点布局严格更强

设有限简单k元超图H及锁集G，且每个跨对x∉G、g∈G都满足λ(x,g)=1。记μ(T)为原边的精确G迹重数。对每个真实外点x，含x边的非空G迹两两不交且覆盖G，因此组成集合划分Π_x；每块大小至多k−1。同一个块T在Π_x恰出现一次，不能把不同边副本当成重复块。

若已知所有可行局部(μ,Π)输入，并有某个非空T满足μ(T)>0、|T|<k，且所有含T的可行Π均给严格染色证书，则H可染。证明：取一条真实G迹为T的边e，再取x∈e\G，其实际Π_x必含T；套用严格证书即可。不要求所有可行Π都严格，也不用先给全部外点指定划分。

更强的共同边际恒等式是

\[
\sum_{x\notin G}\mathbf 1\{T\in\Pi_x\}=(k-|T|)\mu(T).
\]

两边都数“原边e的G迹恰为T、x∈e\G”的关联。若所有非严格Π满足某个线性不等式，按真实外点求和并代入上述精确边际可直接排除μ。有限求解器可以寻找该不等式，但证明由逐Π不等式及边际恒等式承担。

本轮25点a5实例：[GROUP5_EXTERNAL_STAR.md](../../../../knowledge/archive/context/propertyb35-paper/round01/twentyfive/GROUP5_EXTERNAL_STAR.md)完整245输入仅65严格，选T调用仍排10组类；第12号残类每份Π的非单块数≤1+1_{6∈Π}，实际求和给25≤20+3=23矛盾，另排一类。独立域/逐行有理重放通过。此引理是一般纸面计数与调用原则，未新增Lean；剩余七无组边类的20分拆正见证不构造完整H。



## L18. 最小空迹的真实换点势能

对任意超图、同样大小的点集$I$与$I'=(I\setminus\{i\})\cup\{x\}$，记$\mu_0(I)$为避开$I$的边数，$\mu_i(I)$为$I$迹恰为$\{i\}$的边数；令$r_x$计旧空迹中含$x$的边，$s_{xi}$计旧单迹$\{i\}$中含$x$的边。按原边分类直接得

$$\mu_0(I')=\mu_0(I)-r_x+\mu_i(I)-s_{xi}.$$

若$I$在一类可容许点集中最小化空迹，且该真实换点保持可容许性，就有$r_x+s_{xi}\le\mu_i(I)$。无需额外概率表，也不要求换点后类型不变。本轮[七单位集的应用](../../../../knowledge/archive/context/propertyb35-paper/round01/twentyfive/A7_MINIMUM_EMPTY_CORE.md)用私邻居换点保持unit性质，先由全池度数推出core0必有下降，然后只需选择core19；内／外伙伴私星由227／231压到95／21。这个结论是存在可选core19，不是H内完全没有core0。先最小化空迹、再最大化其他势能时，后者只能对保持第一势能的交换使用。

25点全七度a7已实际用此势能闭合：在所有七单位集上最小化空迹，core0的总空迹度矛盾为35≤28，core19外／内私星分别压成21／95。其完整101／815双星及固定原始界接回原H，见[完整a7正文](../../../../knowledge/archive/context/propertyb35-paper/round01/twentyfive/A7_MINIMUM_EMPTY_CLOSURE.md)。这条结论不声称H中不存在其他core0集合；只需选到一个最优core19。



## L36. 同一真实全池的有限视图自然连接

若原H的每个选点视图都必须落在有限残域，且视图共享原H的同一包含数I_A，则原H产生全部视图关系的自然连接中的一个元素。完整连接为空便排除‘所有局部视图都不严格’，而不需要枚举原H。完备性必须分别证明残域覆盖与每份共有变量的真实绑定，不能只检查已存代表的拼接。

[21点六度中心+六unit8](../../../../knowledge/archive/context/propertyb35-paper/round01/twentyone-high/unique6_with7/new_structure_20261020/SIX_UNIT8_POOL_PROOF.md)是实际应用：3+3中心块用八份点对关联对七次非中心度排除；共度一完整星的六个五视图共有连接依次153/999/898/207/15/0，两种独立标准库实现一致。旧三份六锁严格证书为明确依赖；已核代码没有唯一六度/无七度或自由点度≥8的隐藏过滤。它把21唯一六/a1压到五unit8/十unit9/一unit7角色，不是完整21结论。


## 单位星的完整参数化证明

下文给的是一般k/d星恢复，当前并无新增Lean包装。它解释为什么若干小视图可以做共同自然连接：它们必须是同一个划分和包含数的限制，而非各视图各选一个最坏库存。

# 单位邻点星：共同划分与全部真实迹的恢复

## 命题

设 $H=(V,E)$ 为有限简单 $k$ 元超图，$k\ge2$，$M=|E|$。选不同顶点 $x,y_1,\ldots,y_s$，满足每个 $y_i$ 与 $x$ 的共度恰为1。记 $d=d(x)$，以 $Y=\{1,\ldots,s\}$ 为邻点标签。

则存在 $Y$ 的唯一集合划分 $\Pi$，每块大小至多 $k-1$、块数至多 $d$，使过 $x$ 的边在所选锁点上的全部精确迹为

$$
\mu(\{x\}\cup B)=1\quad(B\in\Pi),\qquad
\mu(\{x\})=d-|\Pi|,
$$

其他含 $x$ 的精确迹重数为0。

对非空 $A\subseteq Y$，记

$$
I_A=\#\{e\in E:\{y_i:i\in A\}\subseteq e\},\qquad
p_A=\mathbf1\{A\subseteq B\text{ 对某 }B\in\Pi\}.
$$

定义 $J_\varnothing=M-d$，$J_A=I_A-p_A$ 对 $A\ne\varnothing$。则不含 $x$ 的边在邻点上的精确迹重数由下式唯一恢复：

$$
\mu_0(T)=\sum_{A\supseteq T}(-1)^{|A|-|T|}J_A
\qquad(T\subseteq Y).
$$

全部实际重数均非负。若 $|A|>k$ 则 $I_A=0$，若 $|T|>k$ 则 $\mu_0(T)=0$。若 $|T|=k$，精确迹已经包含整条边，简单性进一步给出 $\mu_0(T)\le1$。

## 证明

每个 $y_i$ 恰在一条过 $x$ 的边中。将具有同一条这样的边的邻点标签归为一块，得到覆盖 $Y$ 的互不相交非空块族 $\Pi$。一条过 $x$ 的 $k$ 元边至多包含 $k-1$ 个邻点，所以块大小受限；块对应不同的过 $x$ 边，故块数至多 $d$。非空块精确迹只出现一次，否则其中任意邻点会与 $x$ 共边至少两次。剩余 $d-|\Pi|$ 条过 $x$ 边没有所选邻点。这证明含中心部分，且由实际中心边唯一确定 $\Pi$。

固定非空 $A$。包含其全部邻点的过中心边存在当且仅当 $A$ 落在一个划分块中，存在时恰有一条。因此 $J_A$ 正是不含中心、包含 $A$ 全部邻点的边数。按照不含中心的边的精确迹分组，

$$
J_A=\sum_{U\supseteq A}\mu_0(U)
$$

对空 $A$ 也成立，因为不含中心边共 $M-d$ 条。

将该式代入恢复公式并交换有限和，$\mu_0(U)$ 的系数为

$$
\sum_{T\subseteq A\subseteq U}(-1)^{|A|-|T|}
=(1-1)^{|U\setminus T|}.
$$

该系数在 $U=T$ 时为1，在其他 $U\supsetneq T$ 时为0，故得到原本的精确重数。这同时证明公式和唯一性；非负性与边大小约束由其实际计数含义得到。证毕。

## 完整局部分类怎样调用

若度数、两两共度及更高阶包含数尚未完全固定，可枚举所有允许的 $\Pi$ 与 $I_A$，按恢复公式计算重数，并剔除负数项或超过边大小的项。只要允许域包含每个实际 $\Pi,I_A$，该分类就不会漏掉真实超图。保留的抽象库存不必全部能延拓成完整超图；只需对所有保留项证明结论。

若先处理若干较小邻点集，它们的划分都必须是同一个 $\Pi$ 的限制，包含数也必须是同一组 $I_A$ 的投影。因此可要求每个投影落在已证明的残域中，再枚举共同恢复；不能将不同投影的局部最坏数据独立拼接。

在五元应用中，选至少5个邻点时必须显式排除大小5的划分块：那会产生含中心的6元边。若恰选5个邻点，则最高阶包含数 $I_Y=\mu_0(Y)\in\{0,1\}$，因为过中心的边不可能包含全部五个邻点，且简单超图只有一条可能的边 $\{y_1,\ldots,y_5\}$。19点的四邻点应用没有前一项额外筛选，因为其块天然至多4。

本引理适用于任意边大小与中心度数；没有新增Lean实现。已完成的实例是[19点最小度8](../../../../knowledge/archive/context/propertyb35-paper/round01/nineteen/DELTA8_PROOF.md)，其中三个／四个邻点的共同库存分别为66型与33个残型。
