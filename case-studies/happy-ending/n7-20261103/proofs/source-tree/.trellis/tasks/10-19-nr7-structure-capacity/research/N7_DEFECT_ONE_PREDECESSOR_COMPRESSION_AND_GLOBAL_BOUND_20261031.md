# N7：亏一末前驱压缩、完整临界排除与全局工作上界

日期：2026-10-31。状态：**工作证明；全部新增 unreviewed/unaccepted，未独立审阅、未接受**。本文由既有指定原生 Sol/high 文档执行者忠实转写主会话与生成协作者已经生成、核对并批准的数学；执行者不自行研究、生成数学或补证。生成协作者的手工互检不是独立数学验证，`PASS_DOCUMENT_ONLY` 也不提升数学接受或 assurance 状态。

本轮完成参数层面的临界排除：以 756 及其换色模型的共同有效容量 b 为输入，排除全部 |X|=3b+4 的 767 配置，得到新的**参数工作界**

\[
N_{\rm sig}(7,6,7)\le3b+3,\qquad
N_{\rm sig}(7,7,7)\le3b+4. \tag{1}
\]

证明先把全部未提升方向统一成满 b+5 的有效 D7 基底，给出允许正、零、负中间人口缺额的完整匹配前缀式；再证明跨原 canonical H0 的新根扇扩张。双非 Ω 机制通过至多两个末前驱压缩低根路径族；含 Ω 机制通过修补满核及删除唯一 H0-origin 源，压缩到一个末前驱。最坏双 Ω 等号由共享同一实际 pair 的两条红五拼成红八排除。附录另给完整 F 的全源/全终划分，不重复计算数值收益。

本文仅新增本文及 `tmp/n7_defect_one_global_bound_20261031/DOCUMENT_CHECK.json`。旧 20261030 稿、其他旧稿、metadata、task.json、运行作业、CNF、proof、runtime、接受与 assurance 状态全部保持。未调用外部 Claude 或任何外部服务，未运行科研代码、枚举、SAT、solver、证明器或证书重放；PowerShell 仅用于文档操作与一致性检查。

## 1. 模型、旧工具与来源保证边界

### 1.1 完整模型及实际路径

X 是完整有序 rank-3 signotope。对 a<b<c<d，packet 按 abc、abd、acd、bcd 排列，至多换色一次。路径按实际顶点数计长，连续三元组同色决定实际单色路径，且单色路径对子序列遗传。weak7 指同一对**实际**首末点的反色路径长度和至少 9，内部允许相交。

767 禁 B6、R7、weak7；766 禁 B6、R6、weak7；756 禁 B5、R6、weak7，其换色模型禁 R5、B6、weak7。b 是 756 与换色模型的共同有效容量上界。所有 Src、End 均在注明的实际诱导点集内计算；ambient、global 或 X 表示母体身份。

记 S=Src_R6(X)、T=End_R6(X) 为**全部** ambient 红六源、终点。不能把它们换成某条路径或某个所选子族的端点。

### 1.2 继承的工作工具

本轮使用下列旧工作工具，保留其原有保证层级：

- 756 与换色模型的有效容量 b；766 容量至多 2b。
- D7 指无 B5、无 weak7 且内部 End_R5∩Src_B4=∅ 的实际配置；其容量至多 b+5，全部内部 R6 的横截数至多 5。
- 原 canonical 分解 X=H0⊔R0 中 H0 为 766，R0 为 D7；不存在两端均在 H0 的 ambient R6，内部点允许经过 R0。H0-origin R6 源的 canonical G 角色提供 ambient 入 R5、出 B5。
- 三链锁定：实际入 R5、出 R6、出 B5 共同存在时，该点的全部出红六终点与全部出蓝五第二点锁定到同一个实际点。
- 全模型旧工作界 N_sig(7,6,7)≤3b+4，以及临界中性区的零 through 结论。
- 上一稿已经排除“至少一个方向兑现满标准接口”的全部 |X|=3b+4 临界机制。

主要本地来源：

- [20261030 纯核根分离与交错重分划稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_PURE_CORE_ROOT_SEPARATION_AND_INTERLEAVED_REPARTITION_20261030.md>) §1—3、§7：全部双满与单侧满标准临界排除、未提升有效基底的来源。
- [联合 neutral 与重分划二分稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_TIGHT_CUT_JOINT_NEUTRAL_AND_REPARTITION_DICHOTOMY_20261029.md>) §1—2：原 canonical G、三链及统一联合预算。
- [联合 through 容量与顺序紧割稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_JOINT_THROUGH_SATURATION_AND_ORDERED_CUTS_20261030.md>) §1—3：全模型旧上界、临界零 through 与真实 promotion。
- [亏一联合稳定性与链接紧割稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_DEFECT_ONE_JOINT_STABILITY_AND_LINKAGE_CUTS_20261029.md>) §4：完整 good 第二点图及实际删点的 Hall 方法。
- [R20 精确归约原稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>) §0—4：合法删根、反向真实添点及 777/767 的精确数量关系。

引用不构成对来源的重审或接受升级。本轮新增的跨 H0 根扇在 §5 完整证明，不能把它当作旧 W'∪V 根域直接使用。

## 2. 反设临界与 canonical 联合预算的穷尽分类

反设存在 767 配置 X，|X|=3b+4。对任一方向的原 canonical 分解 X=H0⊔R0，置

\[
d=2b-|H_0|\in\{0,1\},\qquad
\Omega=\{e\in R_0:\text{有 }H_0\text{-origin ambient R6 终于 }e\},
\quad S_0=R_0\cap S,\quad J=R_0\setminus(\Omega\cup S_0).
\tag{2}
\]

d∈{0,1} 来自 |H0|≤2b、|R0|≤b+5 及临界总点数。定义全部 canonical 残余 mixed 点

\[
M=R_0\cap S\cap\operatorname{End}_{R5}(X)
\cap\operatorname{Src}_{B5}(X). \tag{3}
\]

三链把每个 m∈M 的全部出 R6 终点与全部出 B5 第二点锁到 h(m)。继承的联合预算是

\[
|J|+|M|+
\left|\Omega\cup\bigl(h(M)\setminus(H_0\cup J)\bigr)\right|
\le d. \tag{4}
\]

d=0 整侧为满标准接口；d=1、|J|=1 通过真实 promotion 也兑现满标准接口。任何方向出现这两类，已由上一稿的单侧满标准接口定理排除。

所以剩余每一方向都必须是 d=1 的未提升类型，恰分为：

| 类型 | 完整 canonical 条件 |
|---|---|
| 非 Ω、M0 | Ω=J=M=∅ |
| 非 Ω、M1 | Ω=J=∅，M={m}，h(m)∈H0 |
| 单 Ω | Ω={ω}，J=M=∅ |

这张表由同一个联合预算穷尽，不是额外假定某侧已 promotion。后文先统一所有未提升方向，再分别排除双非 Ω 与至少一侧单 Ω。

## 3. 有效满 D7 基底、完整禁配与根域

### 3.1 全局源的基础延长性质

任一 ambient R6 源不能同时是 ambient B5 终点：入蓝五与出红六在 joining 三元组处，桥蓝给 B6，桥红给 R7。

任何末点在 S 的 ambient B4 都能保留首 pair 延为 ambient B5。具体地，取该末点出 R6 的第二点；若与原 B4 末前驱的桥红，该末前驱前接出红六就成 R7，所以桥蓝。反序给 T 的对应首点延长性质。

### 3.2 非 Ω 方向的有效基底

Ω=J=∅ 时，原 canonical H0 没有 ambient R6 源：H0-origin 的终点不可能在 H0，落 R0 的全部终点又由 Ω为空排除。因此全部全局源 S=R0，大小 b+5，取 W=S。

W 是原 D7。若 r∈W∩End_R5(X) 启动 ambient B5，它必须是唯一可能的 M点 m，第二点锁定为 h(m)∈H0⊂X∖W；M为空时根本不存在这种蓝五源。

### 3.3 单 Ω 方向的唯一 H0-origin 源

现设 Ω={ω}、J=M=∅。置 A_H=H0∩S，因 Ω非空而 A_H非空。原 canonical H0—H0 的 ambient 红六封闭与 G 角色给每个 a0∈A_H ambient 入 R5、出 B5，全部出 R6 终点都是 ω。三链于是将全部出 B5 第二点也锁为 ω。

R0∖{ω} 全部属于 S。无论 ω本身是否属于 S，都有

\[
W=S\setminus\{\omega\}
=(R_0\setminus\{\omega\})\sqcup A_H. \tag{5}
\]

W 中每点都是全局红六源，因此无 ambient B5 终点，且 §3.1 的 B4 延长成立。W 内 junction 若在 R0∖{ω}，其内部 B4 延成 B5 就使该点落入原 M=∅；若在 A_H，延长后保留的第二点必须为 ω，然而 ω不在 W。两者均不可能，W 为实际 D7。

由于 |R0|=b+5，|W|=b+4+|A_H|≤b+5，且 A_H非空，迫 A_H={a}。因此唯一性不是预设，而是实际 D7 容量的结论。并且 a启动 ambient B5，故不能是 ambient R6 终点：否则入红六与出蓝五 joining 给 R7/B6。

取 δ=1[ω∈S]≤1。对 r∈W∩End_R5(X) 的 ambient B5，R0∖{ω} 内普通点由 M为空排除；a的全部蓝五第二点锁定为 ω∈T、ω不在 W。

### 3.4 两向统一有效接口

两种方向统一为 W⊂S，|W|=b+5，W为 D7；正向剩余点至多为单 Ω端口 ω，反向对应 ν：

\[
S=W\sqcup\delta\{\omega\},\qquad
T=W'\sqcup\varepsilon\{\nu\},\qquad
|W|=|W'|=b+5,\qquad \delta,\varepsilon\in\{0,1\}.
\tag{6}
\]

若 δ=1，则 ω∈T；若 ε=1，则 ν∈S。δ=0 或 ε=0 时，相应端口项按 0 理解，不引入不存在的实际点。

每个有效基底还具有以下**完整内侧 mixed 禁配**：若 r∈W∩End_R5(X)，任何从 r启动的 ambient B5，其第二点必在 W外；若 t∈W'∩Src_R5(X)，任何终于 t的 ambient B5，其倒数第二点必在 W'外。普通点根本不能有该蓝五；可能的异常点分别锁到实际外部终点或源点。这不是只对内部 B5 的限制。

### 3.5 中性区、全部 good 与完整根域

定义

\[
I=S\cap T,\quad D=X\setminus(S\cup T),\quad
U=\operatorname{Src}_{R5}(D),\quad V=\operatorname{End}_{R5}(D),
\qquad U\cap V=\varnothing. \tag{7}
\]

最后一式是临界全模型旧 through 结论。置

\[
E=\operatorname{End}_{R6}(W),\quad F=\operatorname{Src}_{R6}(W'),
\quad e=|E|,\quad f=|F|,\qquad
\tau_{R6}(W)=\tau_{R6}(W')=5,\quad 5\le e,f\le6.
\tag{8}
\]

横截下界 5 来自：任一红六横截删除后为 756，故从 b+5 点中至少删 5 点；上界由 D7 工具给出。E本身是红六横截，删 E容量也给 e≥5；反向给 f≥5。

E 是 W∪U 的完整右红根。若其中有 B3(e0,x,y)，取 W内终于 e0的 R6，末前驱 r。禁 R7 迫 χ(r,e0,x)=B，得到 B4(r,e0,x,y)。末点在 W时使用 §3.1；末点在 U时接其 D内出 R5 的下一点，红桥会产生终于 D的 R6，故桥蓝。于是这条 B4 可保首 pair 延成 ambient B5，其第二点 e0∈W，违反 r的完整 mixed 禁配。反序给 F在 W'∪V 的完整左红根。因此

\[
\begin{aligned}
&\chi(e_0,x,y)=R &&(e_0\in E,\ e_0<x<y,\ x,y\in W\cup U),\\
&\chi(x,y,f_0)=R &&(f_0\in F,\ x<y<f_0,\ x,y\in W'\cup V).
\end{aligned} \tag{9}
\]

E、F自身各为全红点集，禁 R7给 e,f≤6，完成 (8)；不能把六根误作大小五的 minimum 横截。端点身份还给 E⊂I∖δ{ω}、F⊂I∖ε{ν}。

U中每点也不能是 ambient B5终点：入蓝五与该点在 D内的出红五 joining，桥蓝给 B6，桥红给终于 D的 R6。因此 W∪U无 B5。W∪U 的内部 junction 不能在 W：内部 B4延成 B5 后保留的第二点在 W∪U，而 W点的潜在锁点属于 T且在 W外，所以也不可能落入 U⊂D。令 good 为 W∪U 的全部 junction，故 good⊂U。删全部 good 后是 D7，容量给 b+5+|U|−|good|≤b+5，迫 good=U。反向同理全部 V都是 good。

## 4. 完整外 Hall、中间匹配与任意缺额前缀公式

### 4.1 外图保留全部实际第二点

任一 good u∈U 有 W∪U 内入 R5及内部 B4(u,i0,x,y)。把 B4保首 pair 延为 ambient B5，再接入 R5末前驱：桥蓝给 B6，所以桥红，得到末 pair 为 (u,i0) 的实际 R6。故 i0∈W∩T，且 i0∉E，因为 B3(i0,x,y) 与 E的右根性质冲突。该红六的末 pair还给全部 ambient 蓝 fan：

\[
u<i_0,\qquad \chi(u,i_0,z)=B\quad\text{对全部 ambient }z>i_0.
\tag{10}
\]

以全部这些实际第二点为邻边，不删替代路径。对 C0⊂U，实际集 (W∖N(C0))∪C0 为 D7：W的 junction 由完整禁配排除，C0上所有 B4第二点均已删除。容量给 |N(C0)|≥|C0|，所以普通 Hall覆盖全部 U。反向全部 V也有普通 Hall，外边附带全 ambient 左蓝 fan。

外图的实际目标层为

\[
A=(I\setminus\delta\{\omega\})\setminus E,\qquad
B=(I\setminus\varepsilon\{\nu\})\setminus F.
\tag{11}
\]

这里字母 B是反向外图的副本层，只在本节作集合记号，不是颜色或后文 H0内角色族。

### 4.2 中间人口允许负缺额

置 i=|I|，由 |S|=b+5+δ、|T|=b+5+ε 得

\[
d_D=|D|-b=i-6-\delta-\varepsilon,\qquad
\ell=\max\{0,d_D\},\qquad \mu=\min\{0,d_D\}.
\tag{12}
\]

中间图保留 D内全部实际 R5 的 U→V端点边。若 d_D≤0，取空匹配；若 d_D>0 而最大匹配≤d_D−1，König cover 至多 d_D−1 个端点副本。删除对应实际点命中全部 D内 R5，实际删除数不超过副本数，余集至少 b+1点且无 R5、B6、weak7，违反换色 756容量。因此中间图有至少 ℓ条匹配边。

两侧外匹配覆盖全部 U、V，所以所选 ℓ条中间边都能复合成 ℓ条分层副本点不交的实际完整链 A→U→V→B。路径内部可以相交，不需要给中间红五分配独占实际点。

### 4.3 实际完整链的顺序比较

任链记为 a0→u→v→b0。若 a0<b0，则外图顺序给 u<a0<b0<v。两侧全 ambient 蓝 fan给 B4(u,a0,b0,v)，中间边给实际 D内 R5(u→v)；两者同实际首末点，4+5=9，违 weak7。所以每条完整链都满足 b0≤a0。

对任意 cut c，链中 A≤c 的点均映入 B≤c，故 A前缀−B前缀≤|A|−ℓ。利用 E、F与端口的实际集合身份，得到本轮核心公式

\[
\boxed{
|F_{\le c}|-|E_{\le c}|-
\delta\,\mathbf1[\omega\le c]+\varepsilon\,\mathbf1[\nu\le c]
\le |A|-\ell=6+\varepsilon-e+\mu.}
\tag{13}
\]

该式适用于 d_D正、零、负及实际端口重合情形，没有固定 q或根人口分类。ℓ是实际完整链数；局部边、外支持人口不能替代它。d_D≤0使用空匹配，不出现负匹配规模。

## 5. 新引理：跨原 canonical H0 的根扇扩张

**跨 H0 根扇工作引理。** 设 H0为原 canonical 766，C=End_R5(H0)，对侧有效 W'具有 §3.4 的完整禁配。对任意 f0∈F=Src_R6(W')、x∈C、y∈H0，若 x<y<f0，则

\[
\chi(x,y,f_0)=R. \tag{14}
\]

证明反设 χ(x,y,f0)=B。取 W'内始于 f0的实际 R6，第二点为 t。若 χ(y,f0,t)=R，可把 y前接这条红六成 R7，故该桥蓝，得到 B4(x,y,f0,t)。

取 H0内终于 x的实际 R5，末前驱 d0。若 χ(d0,x,y)=R，可将 y接到该红五，得到 H0内部 R6，违 H0为 766。因此该桥也蓝，得到

\[
B5(d_0,x,y,f_0,t). \tag{15}
\]

t∈W'，且出 f0红六去首后给 t ambient R5源身份；而 (15) 的倒数第二点 f0也在 W'，违反对侧完整禁配。因此 (14) 成立。

这是本轮新增扩张，不把 C当作 T∪V 的子集，也不把原 H0假作全局 source-free。这里仅用 H0**内部**无 R6，以及对侧有效基底的完整禁配。

## 6. 双非 Ω：完整低根路径族的两末前驱压缩

### 6.1 缺一角色核与全局无源

双方均非 Ω 时，W=S=R0、W'=T=R0'，各有 b+5点，δ=ε=0。H=X∖S、H'=X∖T各有 2b−1点。全局 S、T定义保证 H完全没有 ambient R6源，H'完全没有 ambient R6终点。

取 C=End_R5(H)。删除 C后 H无 R5，换色容量给 |C|≥b−1。每个 c∈C不能启动 ambient B5：用 H内入 c红五末前驱 joining，桥蓝给 B6，桥红给从 H内点启动的 ambient R6，违 H全局无源。因此

\[
|C|\ge b-1,\qquad C\cap\operatorname{Src}_{B5}(X)=\varnothing.
\tag{16}
\]

§5 的扩张根扇适用于 H、C与对侧 T、F。正向 M为空或单点 m；所有非 M的 S∩End_R5(X) 点都没有 ambient B5源。

### 6.2 两个不同普通末前驱会产生同端禁形

令 f*=max F，L=E∩(−∞,f*)，k=|L|。考虑**所有**终于 L的 S内部 R6及各自实际末前驱。

假设其中有两个不同的非 M末前驱 p1、p2，分别选择其原终点 e1'<f*、e2'<f*；这里 e1'、e2'仅表示各自所选终点，不是根序列索引。p_i∈S∩End_R5(X)且不属 M，所以都无 ambient B5源。

C⊔{p1,p2} 至少 b+1点，无 B5且继承无 weak7，756容量迫 R6。C⊂H没有 ambient R6源，故强制红六的首点只能是某个 p∈{p1,p2}。记其终点为 z，p所对应的原终点为 e_p。

原入 e_p红六的末 pair (p,e_p) 对所有晚于 e_p的实际点给蓝帽。若 z>e_p，则 B3(p,e_p,z)与强制 R6同实际端点，违 weak7。所以

\[
z\le e_p<f^*. \tag{17}
\]

此处允许 z=e_p，允许 z是另一个 p，不能擅自排除这些位置。

强制红六除首 p外最多只有一个非 C点。因此保留 p和四个 C点，可取实际子序列 R5(p,c1,c2,c3,c4)，其中 c4≤z≤e_p<f*。跨 H根扇给 χ(c3,c4,f*)=R，追加 f*得到实际 R6(p,c1,c2,c3,c4,f*)。

原入 e_p红六的末 pair又给 B3(p,e_p,f*)，两条路径同实际首末点 p、f*，6+3=9，违 weak7。故假设不成立。

### 6.3 全部低根路径的横截压缩与前缀冲突

由上节，全部终于 L的 S内部 R6，其非 M末前驱最多一个；加上可能的 M点 m，至多两个实际点命中全部这些路径。用这至多两点替换 E中的 k个低根，高根对应路径仍由其终点命中，得到全部 S内部 R6的横截。由 τ_R6(S)=5，

\[
e-k+2\ge5,\qquad k\le e-3. \tag{18}
\]

这里压缩对象是全部低根路径族，不是选出一条方便见证后声称全族被命中。

另一方面，(13) 在 δ=ε=0时给 F前缀−E前缀≤6−e+μ，d_D=i−6。取 c=f*，由 ≤f*改为严格 <f*至多少一个 E点，得到

\[
k\ge e+f-7-\mu\ge e-2, \tag{19}
\]

其中 f≥5、μ≤0。与 (18) 矛盾。

**双非 Ω 整类排除工作定理。** 双方非 Ω的全部未提升临界机制不可实现，包括两侧各自 M0/M1、全部五/六根及所有合法人口；不要求 C满 b，也不要求旧 u=v=q的剩余身份。d_D≤0时空匹配仍给有效前缀式，因此没有负匹配边界漏洞。

## 7. 含 Ω：修补满核与删除唯一内点后的单末前驱压缩

不妨正向是 Ω={ω}、J=M=∅。另一方向可以是非 Ω或单 Ω。沿 §3.3，H0∩S={a}，W=(R0∖{ω})⊔{a}，a不是 ambient R6终点，δ=1[ω∈S]。

### 7.1 H0 的两个角色与修补满核

在原 H0内置 C=End_R5(H0)、B_H=Src_B5(H0)。两族不交：若同一点在 H0内有入 R5、出 B5，joining桥红给 H0内部 R6，桥蓝给 B6。删除各角色后的补集分别受换色 756或 756容量约束，故 |C|、|B_H|均至少 b−1。

a不属于 B_H，因为其全部 ambient B5第二点为 ω∉H0。a也不属于 C：若有 H0内 R5终于 a，末前驱为 d0，取 ambient B5(a,ω,…)；桥 χ(d0,a,ω)蓝给 B6，红则将 ω接到该 H0红五，产生首点严格早于 a的 H0-origin R6，违 H0-origin源唯一为 a。

由 |H0|=2b−1，得到完整角色身份与修补满核

\[
H_0=C\sqcup B_H\sqcup\{a\},\qquad
|C|=|B_H|=b-1,\qquad K=C\sqcup\{a\},\quad |K|=b.
\tag{20}
\]

对每个 c∈C，若有 ambient B5始于 (c,h)，取 H0内部入 c红五的末前驱 joining。桥蓝给 B6，桥红给 H0-origin R6终于 h，所以 h=ω。连同 a，得到

\[
\text{从 }K\text{ 中任何点启动的全部 ambient B5，第二点均为 }\omega.
\tag{21}
\]

C没有任何 ambient R6源，因为 H0的唯一全局红六源是 a且 a∉C。这里没有把整个 H0误作全局无源。

### 7.2 低根路径若末前驱不是 a 就矛盾

仍令 f*=max F。任取 e0∈E、e0<f*，再取**任意** W内部终于 e0的实际 R6，末前驱 p。假设 p≠a，则 p∈R0∖{ω}，且 p∈S∩End_R5(X)。原 M为空迫 p无 ambient B5源。

K+p恰有 b+1点，且不含 ω。由 (21)，K上的所有潜在蓝五源都需要第二点 ω；p又不能启动蓝五，因此 K+p无 B5。它继承无 weak7，756容量迫实际 R6。

这条红六的首点不可能属于 H0：任何 H0-origin R6都终于 ω，而 ω不在该集合中。首点只能是 p，写为

\[
R6(p,z_1,z_2,z_3,z_4,q),\qquad
z_1,z_2,z_3,z_4,q\in K\subseteq H_0. \tag{22}
\]

由于 a不是 ambient R6终点，q∈C。原入 e0红六的末 pair蓝帽和同端 weak迫 q≤e0；q=e0又不可能，因为 q∈H0，而 e0∈W∩T且不能为 a，故 e0∈R0。因此

\[
q<e_0<f^*. \tag{23}
\]

四个内部点 z_i至多一个是 a。删除 a后，仍能保留三个 C点 c1<c2<c3，加上 q，得到实际子序列 R5(p,c1,c2,c3,q)。§5 的跨 H0根扩张适用于任意对侧有效 W'，故 χ(c3,q,f*)=R，追加 f*得实际 R6(p,c1,c2,c3,q,f*)。

原入 e0红六末 pair又给 B3(p,e0,f*)，两者同实际端点 p、f*，违 weak7。因此 p≠a不可能。

这一删除唯一内点的步骤处理了新尾末前驱 z4=a的逃逸：并不要求原强制红六的最后两点都在 C，而是删 a后仍保留首 p加四个 C点再用新根扇。

### 7.3 全部低根路径压缩到一个实际点

令 k=|E∩(−∞,f*)|。由 §7.2，所有严格低根对应的全部 W内部 R6都只能以 a为末前驱。用 {a}替换这 k个根，其余路径仍由高根终点命中，得到全部 W内部 R6横截。τ_R6(W)=5 因而给

\[
e-k+1\ge5,\qquad k\le e-4. \tag{24}
\]

这里对每条低根入路径都证明末前驱等于同一个 a，而非只选定一条路径。

### 7.4 通用 cut 只剩双 Ω 的唯一等号

取实际指标

\[
r=\mathbf1[f^*\in E],\qquad
w=\mathbf1[\omega\le f^*],\qquad
n=\mathbf1[\nu\le f^*]. \tag{25}
\]

缺失端口时对应 δw或 εn按 0理解。将 c=f*代入 (13)，并用 |E≤f*|=k+r，得到

\[
k\ge e+f-6-\varepsilon-\delta w+\varepsilon n-r-\mu.
\tag{26}
\]

结合 (24)、r,w≤1、n≥0，推得

\[
f\le3+\delta+\varepsilon+\mu\le5. \tag{27}
\]

而 f≥5。故唯一可能边界是 δ=ε=1、μ=0、f=5。Ω×非 Ω、任一删端口不兼源终、全部 d_D<0的机制已经矛盾。

在余下边界中，(24)、(26) 的精确式强迫 w=r=1、n=0、k=e−4。由于 δ=1使 ω不在 W及 E，而 f*∈E，得到准确位置

\[
\omega<f^*<\nu,\qquad f^*\in E,\qquad k=e-4.
\tag{28}
\]

这里只推出 f*位于两端口之间，**没有推出全部 E<ν**。若 ω=ν，w=1、n=0已经矛盾。

### 7.5 最坏双 Ω：共享实际 pair 的两红五拼成红八

δ=ε=1时反侧也必为单 Ω。对反侧完整反序应用 §7.1—7.4，得 e=5，并且恰有一个 F根严格在 min E右侧、min E∈F。

正向 k=e−4=1且 f*=max F∈E，写 E={e1<⋯<e5}、F={f1<⋯<f5}，得到 f5=e2；反向恰有一个 F根严格在 e1右且 e1∈F，得到 e1=f4。令

\[
x=e_1=f_4<y=e_2=f_5. \tag{29}
\]

E自身红五来自完整右根域，F自身红五来自完整左根域。因此有两条实际红五

\[
R5(f_1,f_2,f_3,x,y),\qquad R5(x,y,e_3,e_4,e_5).
\tag{30}
\]

它们共享的是同一个实际有序 pair (x,y)，可直接拼为

\[
R8(f_1,f_2,f_3,x,y,e_3,e_4,e_5). \tag{31}
\]

八点严格有序且无重复，全部连续三元组均继承两条红五。由子序列遗传得到禁用 R7，矛盾。这里没有使用仅一个共享点就自动拼链的错误规则。

**含 Ω 双未提升整类排除工作定理。** 至少一侧单 Ω的全部双未提升临界机制均不可实现，覆盖双 Ω及 Ω×非 Ω、全部 δ/ε与 d_D边界；不存在仍需列开的旧“双 Ω逃逸”或“尾末前驱为 a”分支。

### 7.6 统一结算：完整路径击中数对完整匹配前缀

两类证明可用同一公式表达。若所有严格低根 E_<f*对应的**全部** W内部 R6可由至多 ρ个实际点击中，τ_R6(W)=5 给

\[
k\le e+\rho-5. \tag{32}
\]

与通用 cut (13) 结合，并保留 (25) 的 r、w、n，得到

\[
f\le\rho+1+\varepsilon+\delta w-\varepsilon n+r+\mu
\le\rho+2+\delta+\varepsilon+\mu,\qquad \mu\le0.
\tag{33}
\]

双非 Ω证明兑现 ρ=2、δ=ε=0，所以 f≤4，与 f≥5矛盾。Ω证明兑现 ρ=1，所以 f≤3+δ+ε+μ≤5，只剩 §7.5已经由共享实际 pair拼 R8排除的等号。

ρ仅表示对全部低根路径的实际击中集合大小上界，不是锁映射 h(m)，也不是中间匹配数 ℓ。这里统一解释已经证明的两个机制，不添加假设，不另计独立 saving。

## 8. 全部临界机制覆盖与参数工作上界

### 8.1 穷尽覆盖

canonical d∈{0,1}及联合预算 (4) 给全部方向机制的穷尽分类。任何 |X|=3b+4 的临界候选落在下列三行之一：

| 全部临界机制 | 排除依据 | 覆盖结果 |
|---|---|---|
| 至少一侧满标准，包括 d0或 J1真实 promotion | 20261030 上一稿单侧满标准接口主定理 | 旧工作定理整类排除 |
| 两侧均未提升且双非 Ω，各允许 M0/M1 | 本稿 §6的全部低根路径族两末前驱压缩 | 本轮整类排除，含旧双 b−1纯角色核残余 |
| 两侧均未提升且至少一侧单 Ω | 本稿 §7的一末前驱压缩及双 Ω等号共享 pair拼 R8 | 本轮整类排除，含 Ω×非 Ω与双 Ω所有端口边界 |

所以全部 |X|=3b+4 的 767 配置均不存在。结合旧 |X|≤3b+4，得到本轮参数层面的工作定理

\[
\boxed{N_{\rm sig}(7,6,7)\le3b+3.} \tag{34}
\]

这不是仅给新的必要条件或只关闭某个固定人口子类；它已经在完整 canonical 分类内覆盖全部临界机制。但其数学保证状态仍是本轮未独审、未接受的工作证明。

### 8.2 精确删根传播与单次收益

R20已给合法删根与反向真实添点的精确关系

\[
N_{\rm sig}(7,7,7)=N_{\rm sig}(7,6,7)+1. \tag{35}
\]

因此

\[
\boxed{N_{\rm sig}(7,7,7)\le3b+4.} \tag{36}
\]

本轮相较旧参数工作界 3b+4、3b+5，各下降一个单位。双非 Ω与含 Ω证明是对同一临界层的互补覆盖，不是两个可叠加 saving；也不重复计算旧 through所得的下降或同一个主引理。

### 8.3 最后代入既有授权工作输入

先有参数结论 (34)、(36)，再代入既有用户授权的 b=25工作输入，得到

\[
N_{\rm sig}(7,6,7)\le78,\qquad
N_{\rm sig}(7,7,7)\le79. \tag{37}
\]

其余既有参数工作链不变：

\[
N757\le a+b-1,\qquad C766\le2b;
\qquad a=16,\ b=25\ \Longrightarrow\ 40,\ 50. \tag{38}
\]

| 项目 | 旧工作界 | 本轮工作界 | 本轮单次变化 |
|---|---:|---:|---:|
| N757，a=16、b=25 | 40 | 40 | 0 |
| C766，b=25 | 50 | 50 | 0 |
| N_sig(7,6,7)，b=25 | 79 | 78 | −1 |
| N_sig(7,7,7)，b=25 | 80 | 79 | −1 |

b=25是既有用户授权工作输入；用户报告的 UNSAT、证书验证中与旧正式 accepted状态分层保持。本轮没有读取新证书、执行证书验证或将用户报告提升为 accepted。本轮新的 78/79是参数手证的**工作结论**，不是已经独立验证或接受的结果。

一般完整 F的全部机制仍未解决，附录只给明确条件下的完整划分。是否还能进一步得到 77/78未证明。本轮临界排除不能外推为任意更小 F都可满足，也不能继续把已经关闭的双 b−1核或双 Ω列为本轮开放。

## 9. 竞争路线附录：完整 F 的全源/全终划分

本附录独立于主线，不使用 rank-1 product、选定大小 p的块、private 外供位置或右继红源。它保留完整 F，且不另计数值 saving。

### 9.1 全源划分工作定理

设 p≥3，完整有序 signotope X禁 B_(p+1)、R_(p+2)。完整约束族 F的红成员是实际 R_(p+1)，蓝成员是实际 Bp；每个原红成员的 G-trace包含某个完整块 G_i。若每个 G_i至少含一个**非 ambient R_(p+1)源**，则

\[
Y=\operatorname{Src}_{R_{p+1}}(X),\qquad K=X\setminus Y
\tag{39}
\]

满足完整 F：每个原红成员同时遇 Y、K，每个原蓝成员遇 K。

证明：每个原红成员的实际首点属于 Y，故遇 Y；其包含的整块 G_i有非源，故该成员也遇 K。若某个原蓝 Bp全落 Y，其末点 t启动实际 R_(p+1)。取入蓝路径末前驱 u、出红路径第二点 w，在 χ(u,t,w)处 joining；桥蓝给 B_(p+1)，桥红给 R_(p+2)，都矛盾。因此每个原蓝成员都遇 K，完整分划得证。

### 9.2 全终划分及精确边界

反序完全同理：若每个 G_i至少含一个非 ambient R_(p+1)终点，则

\[
Y=\operatorname{End}_{R_{p+1}}(X),\qquad K=X\setminus Y
\tag{40}
\]

也满足完整 F。

这两个条件覆盖一整类此前右继非源的机制，而非只固定某条 private供应。一般完整 F仍可能同时含全源块与全终块，尚未普遍证明它都可满足。代 p=5仅得到 B6/R7背景下的附加结构定理；不把主线全部临界排除外推到任意较小的完整 F。

## 10. 文档回执与科研保证边界

本稿全部新增 **unreviewed/unaccepted**。本轮参数手证及生成协作者互检不构成独立数学验证，文档执行者也未承担独立数学研究或审阅角色。指定原生 Sol/high仅作为执行角色记录；未报告的 backend或实际 effort不作可验证结论。

文档回执为 `tmp/n7_defect_one_global_bound_20261031/DOCUMENT_CHECK.json`，只检查严格 UTF-8、公式号连续唯一、全部本地依赖链接存在、参数与数值代入及新旧界的单次 saving措辞、指定两新路径的写入范围。`PASS_DOCUMENT_ONLY`不表示数学 accepted、已独审或 assurance升级。

本轮文档完成不代表长期任务完成。旧稿与所有运行、CNF、proof、runtime、metadata、task.json、接受状态保持；没有外部审阅、科研代码、枚举、SAT/solver或新证书执行。尚未证明的进一步 77/78与一般完整 F边界按 §8—9保留。
