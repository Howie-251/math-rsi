# N7：六根骨架、外部 private 供应障碍与覆盖审计

日期：2026-10-30。状态：**工作稿；全部新增 unreviewed/unaccepted**。本文忠实转写主会话批准的数学；文档执行者不生成或补证数学。主会话与生成协作者互检不属于独立审阅，不改变旧稿的接受或 assurance 状态。

本轮主线是在双满、双五根、双 τ5 的临界接口中，将共同点集压到一个六根骨架与至多两个 gap 点，完整排除该接口的全部 q≥5 子类；竞争路线给出左侧蓝 product 对红 p 块的所有真实外供位置约束。二者均未关闭完整临界母体或完整路径角色族 F。本轮无新增无条件数值下降。

未调用外部 Claude 或其他外部服务；未运行科研代码、枚举、SAT、solver、证明器或证书重放。PowerShell 仅作文档写入、UTF-8、公式编号、链接及固定算术检查。唯一写入归属为本文和指定 DOCUMENT_CHECK.json；旧稿、任务元数据、接受/assurance、runtime、作业、CNF、proof 与配置均不改。

## 1. 依赖、模型与临界接口

主要依赖为 [任意次序 product 与全局根障碍稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_ARBITRARY_ORDER_PRODUCT_AND_GLOBAL_ROOT_BARRIERS_20261030.md>)、[共同根间隙与内部支持障碍稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMMON_ROOT_GAP_AND_INTERNAL_SUPPORT_OBSTRUCTIONS_20261030.md>)、[联合 through 与顺序紧割稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_JOINT_THROUGH_SATURATION_AND_ORDERED_CUTS_20261030.md>)。完整 F 及拟阵背景沿用上述依赖所引的 [重分块二分稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_TIGHT_CUT_JOINT_NEUTRAL_AND_REPARTITION_DICHOTOMY_20261029.md>) §6。依赖保留原保证边界，不在本文重审或升级接受。

完整有序 rank-3 signotope 对 a<b<c<d 的 packet 按 abc、abd、acd、bcd 排列，至多换色一次。单色路径长度按实际点计，且对子序列遗传；红路径也可由连续三元组全红判定。767 禁 R7、B6、weak7；weak7 比较同一对实际首末点的反色路径，长度和至少 9。换色 756 禁 R5、B6、weak7，b 为其有效容量上界。

先固定临界双满标准接口，而非任意两块满 766：

\[
n=|X|=3b+4,\quad S=\operatorname{Src}_{R6}(X),\quad
T=\operatorname{End}_{R6}(X),\quad |S|=|T|=b+4. \tag{1}
\]

两向真实 canonical/promotion 所提供的 unrestricted 蓝 fan、封闭与混合角色禁形均继承。定义

\[
I=S\cap T,\quad P=S\setminus T,\quad Q=T\setminus S,\quad
D=X\setminus(S\cup T),\quad U=\operatorname{Src}_{R5}(D),\quad
V=\operatorname{End}_{R5}(D). \tag{2}
\]

全局带 through 式在此给 w=|U∩V|=0，并有

\[
|D|=b+q,\quad |U|=|V|=q,\quad |P|=|Q|=b-q,\quad |I|=q+4. \tag{3}
\]

以下 §2—4 **仅**讨论

\[
E=\operatorname{End}_{R6}(S)=\{e_1<\cdots<e_5\},\quad
F=\operatorname{Src}_{R6}(T)=\{f_1<\cdots<f_5\},\quad
\tau_S=\tau_T=5. \tag{4}
\]

E、F 均在 I。E 是 W=S∪U 内全右红根，即 e<u<v 且三点在 W 时 χ(e,u,v)=R；F 是 W′=T∪V 内全左红根，即 u<v<f 且三点在 W′ 时 χ(u,v,f)=R。不得把根扇无条件延伸到全部 X 或全部 D。

依赖已给实际 private 根链及所有 cut 的条件：

\[
R6(a^*,e_1,e_2,e_3,e_4,e_5),\quad a^*<e_1,\qquad
R6(f_1,f_2,f_3,f_4,f_5,b^*),\quad b^*>f_5, \tag{5}
\]

\[
|F_{\le c}|-|E_{\le c}|\le1\ \text{对所有 cut},\qquad
x=e_2=f_3<y=e_3=f_4. \tag{6}
\]

## 2. 六根骨架与 q≥5 子类的完整排除

### 2.1 工作定理与极值

**六根骨架工作定理（未正式接受）。** 在 §1 的全部限定条件下，

\[
E\cup F=\{f_1,f_2,x,y,e_4,e_5\},\qquad
f_1<f_2<x<y<e_4<e_5, \tag{7}
\]

\[
6\le|I|\le6+\mathbf1[e_1=f_2]+\mathbf1[f_5=e_4]\le8. \tag{8}
\]

先由根链和 R7 帽得

\[
e_5=\max(S\cup U),\qquad f_1=\min(T\cup V),\qquad
I\subseteq[f_1,e_5]. \tag{9}
\]

确实，若 z∈W 且 z>e5，根扇 χ(e4,e5,z)=R 把 (5) 左链追加成 R7。反向若 z∈W′ 且 z<f1，左根 f2 给 χ(z,f1,f2)=R，把 (5) 右链前接成 R7。

由 cut 在 f2 处得 e1≤f2，在 f5 处得 e4≤f5；(9) 又给 f1≤e1、f5≤e5。

### 2.2 最外两 gap 为空，故根并集恰是六点

若 i∈I∩(f1,f2)，实际有序七点 (f1,i,f2,x,y,f5,b*) 的连续三元组均红：

| 连续三元组 | 来源与实际适用域 |
| --- | --- |
| (f1,i,f2) | F 左根 f2；f1,i,f2∈T⊆W′ |
| (i,f2,x) | F 左根 x；i,f2,x∈T⊆W′ |
| (f2,x,y) | F 左根 y；三点在 T⊆W′ |
| (x,y,f5) | F 左根 f5；三点在 T⊆W′ |
| (y,f5,b*) | (5) 的原实际右链 |

故得 R7，矛盾。若 j∈I∩(e4,e5)，实际七点 (a*,e1,x,y,e4,j,e5) 同样给 R7：

| 连续三元组 | 来源与实际适用域 |
| --- | --- |
| (a*,e1,x) | (5) 的原实际左链 |
| (e1,x,y) | E 右根 e1；三点在 S⊆W |
| (x,y,e4) | E 右根 x；三点在 S⊆W |
| (y,e4,j) | E 右根 y；j∈I⊆S，三点在 W |
| (e4,j,e5) | E 右根 e4；j∈I⊆S，三点在 W |

因此 I 的这两处开 gap 为空。结合 f1≤e1≤f2 与 e4≤f5≤e5，且 e1、f5∈I，得到

\[
e_1\in\{f_1,f_2\},\qquad f_5\in\{e_4,e_5\}. \tag{10}
\]

E、F 的内部严格次序给 (7) 的六个严格有序实际点；它们全部在 I，故 |I|≥6。

### 2.3 中央 gap 为空，两侧内 gap 各至多一点

若 i∈I∩(x,y)，实际 R7(a*,e1,x,i,y,f5,b*) 的逐项依据为：

| 连续三元组 | 来源与实际适用域 |
| --- | --- |
| (a*,e1,x) | (5) 原实际左链 |
| (e1,x,i) | E 右根 e1；i∈I⊆S，三点在 W |
| (x,i,y) | E 右根 x；三点在 I⊆W |
| (i,y,f5) | F 左根 f5；i∈I⊆T，三点在 W′ |
| (y,f5,b*) | (5) 原实际右链 |

因此 I∩(x,y)=∅，重述依赖的共同根间隙结论。

若 i<j 均在 I∩(f2,x)，实际七点 (e1,i,j,x,y,f5,b*) 给 R7：

| 连续三元组 | 来源与实际适用域 |
| --- | --- |
| (e1,i,j) | E 右根 e1；i,j∈I⊆S，三点在 W |
| (i,j,x) | F 左根 x；i,j∈I⊆T，三点在 W′ |
| (j,x,y) | F 左根 y；三点在 T⊆W′ |
| (x,y,f5) | F 左根 f5；三点在 T⊆W′ |
| (y,f5,b*) | (5) 原实际右链 |

若 i<j 均在 I∩(y,e4)，实际七点 (a*,e1,x,y,i,j,f5) 给 R7：

| 连续三元组 | 来源与实际适用域 |
| --- | --- |
| (a*,e1,x) | (5) 原实际左链 |
| (e1,x,y) | E 右根 e1；三点在 S⊆W |
| (x,y,i) | E 右根 x；i∈I⊆S，三点在 W |
| (y,i,j) | E 右根 y；i,j∈I⊆S，三点在 W |
| (i,j,f5) | F 左根 f5；i,j∈I⊆T，三点在 W′ |

因此仅有两处可能的额外实际点，且

\[
|I\cap(f_2,x)|\le1,\qquad |I\cap(y,e_4)|\le1. \tag{11}
\]

### 2.4 两个内 gap 的附加必要条件

若左 gap 有 l 且 e1=f1，实际七点 (f1,f2,l,x,y,e4,e5) 给 R7：

| 连续三元组 | 来源与实际适用域 |
| --- | --- |
| (f1,f2,l) | E 右根 f1=e1；l∈I⊆S，三点在 W |
| (f2,l,x) | F 左根 x；l∈I⊆T，三点在 W′ |
| (l,x,y) | F 左根 y；三点在 T⊆W′ |
| (x,y,e4) | E 右根 x；三点在 S⊆W |
| (y,e4,e5) | E 右根 y；三点在 S⊆W |

故左 gap 非空迫 e1=f2。若右 gap 有 r 且 f5=e5，实际七点 (f1,f2,x,y,r,e4,e5) 给 R7：

| 连续三元组 | 来源与实际适用域 |
| --- | --- |
| (f1,f2,x) | F 左根 x；三点在 T⊆W′ |
| (f2,x,y) | F 左根 y；三点在 T⊆W′ |
| (x,y,r) | E 右根 x；r∈I⊆S，三点在 W |
| (y,r,e4) | E 右根 y；r∈I⊆S，三点在 W |
| (r,e4,e5) | F 左根 e5=f5；r∈I⊆T，三点在 W′ |

故右 gap 非空迫 f5=e4。结合 (9)—(11)，所有 I 点均已计入六骨架和这两个受限 gap，得到 (8)。代回 |I|=q+4，得到

\[
q\in\{2,3,4\}. \tag{12}
\]

这确实排除该双满、双五根、双 τ5、w0 接口的全部 q≥5 子类；没有关闭整个五根分支。

## 3. 六点红链与三段红六的准确停止点

六骨架是实际红六。按实际次序 (f1,f2,x,y,e4,e5)，四个连续 triple 依次为 (f1,f2,x)、(f2,x,y)、(x,y,e4)、(y,e4,e5)。前两项来自 F 的左根 x、y，三点在 T⊆W′；后两项来自 E 的右根 x、y，三点在 S⊆W。因此

\[
R6(f_1,f_2,x,y,e_4,e_5). \tag{13}
\]

两端 f1、e5∈I，故存在 ambient 入 R6 终于 f1，以及 ambient 出 R6 始于 e5。与 (13) 组成三段依次共端点的红六。这种三段配置是否必为禁形仍未证明，不能据此关闭五根分支。

可记录下列附带必要接口，**不计为新的主收益**。设实际三段为

\[
\begin{aligned}
A&=(a_0,a_1,a_2,a_3,a_4,b),\\
B&=(b,b_1,b_2,b_3,b_4,c),\\
C&=(c,c_1,c_2,c_3,c_4,d),
\end{aligned}\qquad A,B,C\text{ 均为 }R6. \tag{14}
\]

则强迫

\[
B4(a_3,a_4,b_1,b_2),\qquad
B4(b_3,b_4,c_1,c_2),\qquad
B4(a_4,b,c,c_1). \tag{15}
\]

前两项短证使用同端 weak。无 R7 由 B 的前接及 A 的后接分别给 χ(a0,b,b1)=B、χ(a4,b,c)=B。若 χ(a3,a4,b1)=R，则 R6(a0,a1,a2,a3,a4,b1) 与 B3(a0,b,b1) 同端，矛盾。若 χ(a4,b1,b2)=R，则 R6(a4,b1,b2,b3,b4,c) 与 B3(a4,b,c) 同端，矛盾。因此四包 (a3,a4,b1,b2) 首末皆蓝，全部蓝，给第一项；第二项对偶。

第三项有独立的直接短证：A 的无 R7 后接帽迫 χ(a4,b,z)=B 对所有 z>b；C 的无 R7 前接帽迫 χ(z,c,c1)=B 对所有 z<c。分别取 z=c、z=b，得到两个连续蓝 triple (a4,b,c)、(b,c,c1)，所以实际 (a4,b,c,c1) 为 B4；也可由对应四包首末皆蓝得全蓝。

这些局部蓝四尚不能自动传到末 pair (b3,b4) 所需的其他位置；本文没有把 (15) 提升成三段红六不可能。

## 4. 八点局部校准与其缺少的完整接口

取实际八点次序

\[
A=f_1<B=e_1=f_2<C<D=x<E=y<F<G=e_4=f_5<H=e_5. \tag{16}
\]

所有三元组均红，唯 ABC、FGH 蓝。任意四点包若包含蓝 triple，它只能在首位或末位：ABC、FGH 分别是连续三点，包中第四点只能落于它们外侧；四点包也不可能同时包含这两个不交蓝 triple。因此所有包至多换色一次，完整 signotope 合法。

任何七点由八点删除一点得到，不可能同时击中两个不交蓝 triple，故不可能为 R7。全部蓝路径长至多 3；蓝三只发生在 ABC、FGH 这两个连续三点区间，其同实际端点区间内红路径长至多 2。其余同端蓝路径长至多 2，而红路径长至多 6，所以无 weak7，也无 B6。

在这个局部八点集 I 上，指定

\[
E=\{B,D,E,G,H\},\qquad F=\{A,B,D,E,G\}. \tag{17}
\]

具有所需右/左红 fan：两个蓝例外的最小点 A、F 均不在 E；其最大点 C、H 均不在 F。可取 a*=A、b*=H，两条根链都沿同一实际红六 (A,B,D,E,G,H)，它也是六根骨架。

该例只满足列出的左右根扇及两条提炼根链；没有实现原双满母体的 E=End_R6(S)、F=Src_R6(T) 全部端点身份、全部 τ5-private 条件及 P/Q 外供。尤其指定根集中的早位 D、E 在八点 I 内不一定是 R6 终点。因此不能称其满足完整五根接口，也不能当作临界双满反例。它只说明六根扇、局部链与 |I|=8 的上端局部模式本身仍不足以关闭全接口。

## 5. 竞争主结果：蓝 product 对红 p 块的完整外供位置障碍

### 5.1 先给参数定理

设 p≥3，完整有序 signotope 禁 B_(p+1)、R_(p+2) 及同实际端点的 R_(p+1)+B3。设 A={a1<⋯<ap} 是实际红 p，D 是与其不交的蓝 (p−1) 点集，满足

\[
D<A,\qquad D\cup\{a\}\text{ 为 }B_p\ \text{对每个 }a\in A,\qquad d^*=\max D. \tag{18}
\]

**外供位置工作定理。** 有

\[
A\cup\{d^*\}\text{ 为 }R_{p+1};\qquad
v\notin A,\ A\cup\{v\}\text{ 为 }R_{p+1}\ \Longrightarrow\ v\le d^*. \tag{19}
\]

v=d* 是允许的，不能把第二项写成普遍严格不等式。反序得到对偶定理。

### 5.2 d* 对 A 的每个 pair 全红

任取 x<y∈A。如果每个 d∈D 都使 χ(d,x,y)=B，则 D+x+y 的全部三元组蓝：D 内部蓝；两 D 点加 x 或 y 由 (18) 蓝；一 D 点加 x、y 由该假设蓝。于是得到 B_(p+1)，矛盾。

故存在 d∈D 使 χ(d,x,y)=R。若 d=d*，已经成立。若 d<d*，四包 (d,d*,x,y) 是 (B,B,R,?)，前两项来自 D+x、D+y 蓝，迫末项 χ(d*,x,y)=R。因此 d* 对 A 每个 pair 全红，结合 A 内部红即得 (19) 第一项。

### 5.3 排除 v>d* 的三种实际位置

反设 v>d*、v∉A 且 A+v 为 R_(p+1)。

**情形一：v>a2。** 将 d* 前接到实际 A+v 红链，首连续 triple 为 (d*,a1,a2)，由 §5.2 红；其余连续 triple 由 A+v 红。得到 R_(p+2)，矛盾。

**情形二：a1<v<a2。** 若 χ(d*,a1,v)=R，前接 d* 到 A+v 就得 R_(p+2)，所以

\[
\chi(d^*,a_1,v)=B. \tag{20}
\]

对任意 d<d*、d∈D，四包 (d,d*,a1,v) 首项由 D+a1 蓝、末项由 (20) 蓝，故全蓝，尤其 χ(d,d*,v)=B、χ(d,a1,v)=B。

**情形三：d*<v<a1。** 无 R_(p+2) 迫 χ(d*,v,a1)=B。§5.2 的 R_(p+1)(d*,A) 与同端 weak 禁形又迫 χ(d*,v,ap)=R。对 d<d*、d∈D，四包 (d,d*,v,ap) 为 (?,B,?,R)，故 χ(d,d*,v)=B；再看 (d,d*,v,a1)=(B,B,?,B)，得 χ(d,v,a1)=B。

后两种情形都已得 D 中含 d* 的 pair 与 v 组成蓝 triple，且每个 d∈D 与 v、a1 组成蓝 triple。若 d<e<d* 均在 D，四包 (d,e,d*,v) 首项 D 内部蓝、末项 (e,d*,v) 蓝，故全蓝，特别 χ(d,e,v)=B。当 |D|=2 时不需这一步。

于是 D+v+a1 的全部三元组蓝：D 内部蓝；D pair+a1 由 (18) 蓝；D pair+v 由刚才推导蓝；D point+v+a1 在两情形均已证蓝。这是 p+1 个实际点，形成 B_(p+1)，矛盾。三类穷尽 v>d*、v∉A，(19) 完成。

### 5.4 再代 p=5

取 p=5，假设正是禁 B6、R7 及同端 R6+B3。一个红五点块 A 左侧若有满足完整蓝 product 的蓝四点集 D，则 d*+A 是红六，任何 A+v 红六的外点都必须 v≤max D。该结论没有预先要求拟阵、private 性或删去任何额外路径。

## 6. 在完整 F 中保留所有成员的准确解释

沿旧完整路径拟阵背景，F 是所研究完整路径角色约束族，G 是全部 minimum 红横截的并。保留 F 的全部红、蓝成员及全部 G 外点，不把 G 当成 UNSAT 核。

在纯 rank1 背景下，取一个大小 p 的红块 A，以及 minimum basis

\[
S=D\cup\{s\},\qquad s\in A,\quad |D|=p-1,\quad D<A. \tag{21}
\]

假设这个位置的每一条 s-private 红成员 H 都触及 G 外。private 意味 H∩S={s}；完整 trace 结构迫 H 含整块 A。每个 H 有 p+1 个点，而 |A|=p，故只能是

\[
H=A\cup\{v\},\qquad v\notin G. \tag{22}
\]

全部 bases 为蓝 p product，所以 (18) 对 D 与 A 的每一点成立。§5 给 v≤max D；又 max D∈G 而 v∉G，实际点不相等，因此每个真实 private 外点都严格满足

\[
v<\max D. \tag{23}
\]

这约束该位置的**每一条**真实 private 外供，排除 D 与 A 之间、A 内部靠右位置及 A 右方的外供；全部 F、其他 private 和非private 成员均被保留。它没有关闭全部外供，因为更左外点仍可能，不能宣传完整 F 已 SAT。

这里 H=A+v 的点数论证明确使用 |A|=p。一般的交集或一次单点换点不足以排除全部 F；先 cover-private 再修蓝仍会重复旧 C1/C2 障碍。完整 G 外 private 供应与完整 F 的一般分支仍待解，不能只额外加局部条件便当作完成。

## 7. 四根分支的真实极值结论及 Hall 缺额

回到双满标准接口，但本节不要求五根。若 |E|=τS=4，写 E={e1<e2<e3<e4}。由 minimum 横截取 e2-private 实际 R6，首点记 a*。private 性保证 a*≠e1；若 a*>e1，右根 e1 可前接该实际 R6 得 R7，所以 a*<e1。同端 weak7 迫 χ(a*,e1,e2)=R；其余连续 triple 来自 E 右根扇，因此得实际 R5(a*,e1,e2,e3,e4)。

若 z>e4 且 z∈S∪U，右根 e3 给 χ(e3,e4,z)=R，追加成 R6。若 z∈S，则这是 S 内部 R6，z 必在 E=End_R6(S)，与 z>e4 矛盾。若 z∈U⊆D，则 z 成为 ambient R6 终点，与 D 的定义矛盾。因此

\[
|E|=\tau_S=4\ \Longrightarrow\ e_4=\max(S\cup U),\qquad
|F|=\tau_T=4\ \Longrightarrow\ f_1=\min(T\cup V). \tag{24}
\]

第二项由反序获得。该四根结论不依赖五根私有链。

但外侧 Hall 一般只保证 q−1；不能因两端目标 A=I∖E、B=I∖F 都大小 q，便声称存在全 q 链接或 E=F。五根且 τ4 更不能自动获得 §1 的 private 根链。四根极值、Hall 缺额、五根 τ4 是不同的未闭合接口。

## 8. 覆盖审计与下一优先

| 结论 | 实际覆盖 | 仍然开放 |
| --- | --- | --- |
| 全局 n+w≤3b+4 | 全部 767；包括四根、τ4、亏一的 positive-through 子类 | 各机制的 w0 共同实现 |
| 双满完整 S→T 及 Y 内 P→Q perfect；共同点严格跨越 | 全部双满 q、根数、τ；以及已双向真实 promotion 的接口 | 未提升 canonical d1 的 Ω 单点、M 单点、全空 w0 |
| 六根骨架与 |I|≤8 | 仅双满、双五根、双 τ5；全部 q≥5 子类排除 | q=2、3、4 的完整 K 外供与禁配实际交会 |
| 三段依次共端点 R6 及局部 B4 | 必要接口 | 三段是否必禁，末 pair 传蓝 |
| 外供位置定理及 (23) | 完整蓝 product 与选定大小 p 的纯 rank1 块 A；该位置全部外部 private | 更左 G 外供应；完整 F 的一般可满足性 |
| 四根 extremum (24) | |E|=τS=4 及反向 | 外 Hall 缺额、全 q 链接、五根 τ4 的 private 链 |

不能把单向 promotion 当成已兑现双满。五个合法根所给中央区与两侧 756 区联合饱和仍开放；耳区计数会重复实际点，不能把独立预算相加。pair 换根的方向约束也不推出路径颜色平均。本文不收录长八点全局 root 校准，避免引入没有在本轮给出完整证明的额外材料。

下一优先保留四项：q=2/3/4 的完整 K 外供与禁配实际交会；中央区和两侧的联合饱和；竞争路线中 G 外 private 的完整 F，不能只增加局部条件；四根、Hall 缺额与未提升亏一分别处理。

## 9. 参数界先行与数值分账

当前工作证明链仍为

\[
N757\le a+b-1,\qquad C766\le2b,\qquad
N767\le3b+4,\qquad N777\le3b+5. \tag{25}
\]

再代 a=16、b=25，固定算术为

\[
a+b-1=40,\qquad2b=50,\qquad3b+4=79,\qquad3b+5=80. \tag{26}
\]

本轮无新增无条件数值下降，收益为 0。q≥5 子类的排除、外供位置与四根极值均不改写成全局 78/79，也没有宣布完整临界分支关闭。

## 10. 文档回执与保证边界

本文及 [文档检查回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_six_root_skeleton_20261030/DOCUMENT_CHECK.json>) 是本轮唯一写入归属。回执按最终保存内容记录 SHA256、UTF-8 字节/行数、公式界定符、编号唯一连续、本地链接存在性及固定算术 40/50/79/80；结果 PASS_DOCUMENT_ONLY 仅表示文档检查通过。

数学保持 **unreviewed/unaccepted**；生成协作者互检不算独审。外部审阅、外部服务、科研代码、枚举、SAT、solver、证明器及证书重放均为 0。未改旧稿、任务元数据、接受/assurance、runtime、作业、CNF、proof 或配置；未打开页面，未宣布长期研究完成。
