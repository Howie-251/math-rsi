# N7：纯核根严格分离与交错重分划

日期：2026-10-30。状态：**工作稿；全部新增 unreviewed/unaccepted**。本文由指定文档执行者忠实转写主会话已经生成、批准的数学；执行者不自行研究、补证或选择新数学路线。生成协作者之间的互检不是独立审阅，`PASS_DOCUMENT_ONLY` 也不提升数学接受或 assurance 状态。

本稿首要工作定理排除**全部双满标准临界接口**：包含双四根、混合四/五根、双五根，以及各横截数为 4 或 5 的所有组合。证明先把一侧容量迫出的红六纯尾限制在完整红五终点核内，得到全部左根严格早于全部右根，再用统一外侧 Hall 缺额与中间 perfect 匹配导出的前缀不等式矛盾。不再要求某侧横截数为 5，不作根人口或固定 q 分类。

进一步，§7 以对侧满核的纯前供绕过本侧缺失的满核纯尾，排除全部“至少一侧已兑现满标准接口”的临界机制，并排除双方 Ω0/M 近满机制的端点盈一分支。仍有两侧均未提升的精确残余，故没有无条件数值新降。竞争路线 §6 给完整 F 的交错外供右继红源闭合。旧工作链及 40/50/79/80 的当前数值分账保留。

本稿仅新增本文及指定 `DOCUMENT_CHECK.json`。旧稿、任务 metadata、task.json、接受/assurance 状态、CNF、proof、runtime、运行作业与配置均保留。未调用外部 Claude 或其他外部服务；未执行科研代码、枚举、SAT、solver、证明器或证书重放。PowerShell 仅作必要的文档操作与一致性检查。

## 1. 模型、主要依赖与标准接口

### 1.1 模型及来源边界

模型是完整有序 rank-3 signotope。对任意 a<b<c<d，packet 按 abc、abd、acd、bcd 排列，至多换色一次。路径按实际顶点数计长；连续三元组同色决定实际单色路径，且单色路径对子序列遗传。weak7 比较同一对**实际**首末点的反色路径，长度和至少 9，内部允许共享。

767 禁 R7、B6、weak7；766 禁 R6、B6、weak7；756 禁 B5、R6、weak7，其换色模型禁 R5、B6、weak7。b 是 756 及换色模型的共同有效容量上界。本文先保持 b 为参数，不先代入 b=25。

主要本地依赖为：

- [完整核 profile 与 private 重分划稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMPLETE_CORE_PROFILES_AND_PRIVATE_REPARTITION_20261030.md>) §1—2：完整模型、旧纯尾屏障与双满接口。
- [亏一联合稳定性与链接紧割稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_DEFECT_ONE_JOINT_STABILITY_AND_LINKAGE_CUTS_20261029.md>) §4：不要求横截数为 5 的根提升、全部 good 第二点外图及一单位 Hall 缺额。
- [联合 through 容量与顺序紧割稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_JOINT_THROUGH_SATURATION_AND_ORDERED_CUTS_20261030.md>) §1—3：满核角色分划、临界零 through、完整中间匹配与真实 promotion 的适用边界。
- [联合 neutral 与重分划二分稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_TIGHT_CUT_JOINT_NEUTRAL_AND_REPARTITION_DICHOTOMY_20261029.md>) §1—2：§7 使用的 canonical G 角色、三链锁定与联合预算。

这些来源保持各自保证层级，引用不构成重审或接受升级。Src、End 均在注明的实际诱导点集内部计算；ambient 或 X 表示在母体 X 内计算。

### 1.2 双满标准临界接口的全部假设

设 X 为 767 配置，且已经兑现以下双满**标准**临界接口：

\[
|X|=3b+4,\qquad
S=\operatorname{Src}_{R6}(X),\quad T=\operatorname{End}_{R6}(X),
\quad H=X\setminus S,\quad H'=X\setminus T,
\quad |H|=|H'|=2b. \tag{1}
\]

S、T 是全部 ambient 红六的源、终点，不能替换成选定路径端点。canonical 接口或已经严格证明的真实 promotion 还给出：末点在 S 的任意 ambient B4 均能保留首 pair 延为 ambient B5，早期点不必属于 S；T 有反向首点延长。并且

\[
S\cap\operatorname{End}_{R5}(X)\cap\operatorname{Src}_{B5}(X)=\varnothing,
\qquad
T\cap\operatorname{Src}_{R5}(X)\cap\operatorname{End}_{B5}(X)=\varnothing.
\tag{2}
\]

这些延长与 mixed 禁形是明确接口，不可仅从“有两块满 766”推出。

定义实际区域与内部红五端点族

\[
I=S\cap T,\quad P=S\setminus T,\quad Q=T\setminus S,
\quad D=X\setminus(S\cup T),
\quad U=\operatorname{Src}_{R5}(D),\quad V=\operatorname{End}_{R5}(D),
\quad q=|I|-4. \tag{3}
\]

继承满核角色分划、容量及临界 through 结论：

\[
|D|=b+q,\quad |P|=|Q|=b-q,\quad |U|=|V|=q,
\quad U\cap V=\varnothing,\quad |I|=q+4, \tag{4}
\]

\[
Z:=\operatorname{End}_{R5}(H)=Q\sqcup V,\quad |Z|=b,
\qquad
Z':=\operatorname{Src}_{R5}(H')=P\sqcup U,\quad |Z'|=b. \tag{5}
\]

置

\[
E=\operatorname{End}_{R6}(S),\quad F=\operatorname{Src}_{R6}(T),
\quad e=|E|,\quad f=|F|,\qquad E,F\subseteq I,\quad 4\le e,f\le5.
\tag{6}
\]

旧根提升与完整外 Hall 给 (6)，不要求横截数为 5。具体地，W=S⊔U 内 E 的每个点是右红根，W'=T⊔V 内 F 的每个点是左红根：

\[
\chi(e_0,x,y)=R\quad(e_0\in E,\ e_0<x<y,\ x,y\in W),
\qquad
\chi(x,y,f_0)=R\quad(f_0\in F,\ x<y<f_0,\ x,y\in W').
\tag{7}
\]

这里左根的完整适用域包括 V；仅知道 T 内左根不够支持后文的纯核末端桥。

为说明 (7) 的来源，取 S 内终于 e0 的实际 R6，末前驱为 r。若 W 中有 B3(e0,x,y)，χ(r,e0,x) 红则原红六追加 x 成 R7；蓝则 B4(r,e0,x,y) 可保首 pair 延为 ambient B5，违反 r∈S∩End_R5(X) 与 (2)。W 中末点在 U 的 B4 延长，使用该 U 点在 D 内出 R5 的下一点：红桥会产生终于 D 的 R6，故桥蓝。反序给 F 的完整左根域。以上不调用 private 根链或横截数为 5 的假设。

## 2. 单侧纯核根分离定理

**工作定理（纯核根严格分离）。** 在 §1 的双满标准临界接口内，全部 F 根严格早于全部 E 根：

\[
F<E,\qquad\text{即}\quad \max F<\min E. \tag{8}
\]

本定理不先代入 b 的数值，不使用横截数为 5、private 根链或五根人口分类。只有一侧容量迫出的完整纯核供应即足够。

### 2.1 完整核 Z 没有 ambient B5 源

Q 中每点是 ambient R6 终点，不能同时成为 ambient B5 源：入 R6 与出 B5 的 joining，桥红给 R7，桥蓝给 B6。

V 中每点在 D 内结束实际 R5，也不能启动 ambient B5：用该入红五的末前驱 joining，桥蓝给 B6；桥红给以 D 内点为首的 ambient R6，违反 D 不含任何 ambient R6 源。因此

\[
Z\cap\operatorname{Src}_{B5}(X)=\varnothing. \tag{9}
\]

这里保留全部 ambient B5 的否定，不能仅用 Z 内没有 B5 代替下节对外部点 p 的检查。

### 2.2 为每个右根构造尾部全部落在 Z 的实际红六

任取 e0∈E。按 E 的定义，取 S 内部终于 e0 的一条实际 R6，记其末前驱为 p。于是 p∈S∩End_R5(X)。mixed 禁形 (2) 迫 p 没有 ambient B5 源。

p∉Z，因为 p∈S 而 Z⊂H=X∖S。结合 (9)，Z+p 有 b+1 个点且无 B5，继承无 weak7；若也无 R6 就是超过 b 容量的实际 756。因此容量迫出实际 R6。

Z⊂H 不含任何 ambient R6 源，所以这条红六的首点只能是 p，其后五点**全部**在 Z。写为

\[
R6(p,z_1,z_2,z_3,z_4,q_0),\qquad
z_1,z_2,z_3,z_4,q_0\in Z,\qquad q_0\in Z\cap T=Q.
\tag{10}
\]

最后等式来自 Z=Q⊔V、V⊂D，与 D∩T=∅。这是比任意纯 H 尾更强的纯核供应；后面必须使用 z4、q0 都在 Z。

### 2.3 同端禁形先迫 q0<e0

q0=e0 不可能，因为 q0∈Q 而 e0∈S。若 q0>e0，原 S 内红六的末 pair (p,e0) 与 q0 作红三元组就会追加成 R7。因此

\[
\chi(p,e_0,q_0)=B. \tag{11}
\]

B3(p,e0,q0) 与 (10) 的 R6 有同一对实际首末点 p、q0，长度和 3+6=9，违反 weak7。故 q0<e0。

### 2.4 完整左根域再迫 max F<q0

令 f*=max F。q0=f* 不可能，因为 Q∩I=∅ 而 F⊂I。若 q0<f*，则 z4<q0<f* 且 z4、q0 都属于 Z=Q⊔V⊂T⊔V。由 (7) 的完整左根域得

\[
\chi(z_4,q_0,f^*)=R. \tag{12}
\]

去掉 (10) 的首点 p，余下实际 R5(z1,z2,z3,z4,q0) 可追加 f* 成 R6。其首点 z1∈Z⊂X∖S，却成为 ambient R6 源，矛盾。因此

\[
f^*<q_0<e_0\qquad\text{对每个 }e_0\in E. \tag{13}
\]

这证明 (8)。纯尾全部落在 Z 同时保证了末桥可用以及新红六的首点不在 S；任意 H 尾无法直接替代这个步骤。整个证明未用 τ、private 链或固定 q。

## 3. 统一四/五根前缀缺额与整支排除

### 3.1 完整外图各只损失一个单位

置 A=I∖E、B=I∖F，故

\[
|A|=q+4-e,\qquad |B|=q+4-f. \tag{14}
\]

以下使用全部 good 蓝 fan 外边，而非挑选少量支持。先在 W=S⊔U 定义全部 junction

\[
G_W=\operatorname{End}_{R5}(W)\cap\operatorname{Src}_{B4}(W)\subseteq U,
\quad B_{\mathrm{bad}}=U\setminus G_W,\quad k=|B_{\mathrm{bad}}|\le1.
\tag{15}
\]

旧 §4 的实际 D7 删除证明给 k≤1。每个 good u 的所有 W 内 B4(u,a,x,y) 第二点 a 都保留为边。先把 B4 保首 pair 延成 ambient B5，再接 u 的入 R5 末前驱：蓝桥会给 B6，所以桥红，产生末 pair 为 (u,a) 的实际 R6。于是 a∈I∖E=A，且这条实际红六给全 ambient fan

\[
u<a,\qquad \chi(u,a,z)=B\quad\text{对全部 ambient }z>a. \tag{16}
\]

对任意 C⊆G_W，在实际诱导集 (S∖N(C))⊔C⊔B_bad 内，S 上的 junction 被 mixed 禁形排除，C 上所有 B4 第二点被删除，bad 点本来就不是 W 的 junction。因此它是 D7；旧容量给完整 Hall 式

\[
|N(C)|\ge |C|+k-1. \tag{17}
\]

若 k=1，good 图有普通 Hall，可匹配全部 q−1 个 good 点；若 k=0，Hall 缺额至多一，仍有 q−1 条匹配边。bad 与 Hall 只损失一次，不独立再减一个单位。反向完整外图同样给 q−1 条 B—V 匹配边，并附带

\[
b_0<v,\qquad\chi(z,b_0,v)=B\quad\text{对全部 ambient }z<b_0.
\tag{18}
\]

在使用这些匹配数之前，(8) 与 e,f≥4 已给 E∩F=∅ 以及

\[
q+4=|I|\ge e+f\ge8,\qquad q\ge4. \tag{19}
\]

所以本证明不会把 q−1 或 q−2 当成负的匹配、链接规模，也无需小 q 分类。

### 3.2 中间完整实际端点图的 perfect

中间图保留 D 内**全部实际 R5** 的 U→V 端点边。若其最大匹配小于 q，König 定理给至多 q−1 个端点副本的 cover。删除其对应的实际顶点，删除数不超过副本数，命中全部 D 内 R5；余集至少 b+1 点，继承无 B6、weak7 且无 R5，违反换色 756 容量。故中间图有 q-perfect。

这里是端点副本匹配，其边各有实际 D 内 R5 见证；没有要求不同红路径的内部点互不相交。

### 3.3 至少 q−2 条实际完整链

固定左右各 q−1 条外侧匹配及中间 q-perfect。左侧 q−1 个不同 U 副本经中间 perfect 到达 q−1 个不同 V 副本；右侧外匹配也使用 q−1 个 V 副本。V 总共 q 点，所以两组 V 像交集至少 q−2。

由此得到至少 q−2 条分层副本点不交的实际完整链

\[
a\longrightarrow u\longrightarrow v\longrightarrow b_0,
\qquad a\in A,\ u\in U,\ v\in V,\ b_0\in B. \tag{20}
\]

每条中间边由实际 D 内 R5(u→v) 见证，两条外边各自带有 (16)、(18) 的全部 ambient fan。若 a<b0，则 u<a<b0<v；两个 fan 给 χ(u,a,b0)=χ(a,b0,v)=B，构成实际 B4(u,a,b0,v)。它与中间实际 R5 有同一对实际端点 u、v，4+5=9，违反 weak7。因此

\[
b_0\le a\qquad\text{对每条完整链}. \tag{21}
\]

这是完整链的比较结论，不把某条孤立外边或局部红边当作已经兑现的 A→B 链。

### 3.4 前缀不等式与全部双满标准临界接口的矛盾

选其中 q−2 条完整链。对任意 cut c，已匹配的 A 点若≤c，其 B 像由 (21) 也≤c。因此

\[
|A_{\le c}|-|B_{\le c}|
\le |A|-(q-2)=6-e,
\qquad
|F_{\le c}|-|E_{\le c}|\le6-e.
\tag{22}
\]

第二式与第一式等价，因为 A=I∖E、B=I∖F。取 c=f*=max F。根严格分离 (8) 给 |F≤c|=f、|E≤c|=0，故

\[
f\le6-e,\qquad e+f\le6, \tag{23}
\]

与 e+f≥8 矛盾。

**工作定理（全部双满标准临界接口不可实现）。** §1 的双满标准临界接口不存在。它统一覆盖双四根、混合四/五根、双五根及所有 τ4/5 组合；不是仅增加一个必要条件，也不是只排除 τ5 子类。本轮排除仍以已经兑现的完整标准接口为范围，不能把尚未兑现双满的临界机制自动带入。

## 4. 可迁移的完整链匹配缺额公式

以下单列 §3.4 使用的抽象计数，便于在其他实际接口中复用。设 |I|=m，E,F⊆I，|E|=e，|F|=f，A=I∖E，B=I∖F。假设已经兑现 ℓ 条 A→B 完整链，链在各层副本上点不交，且每条链的实际端点满足 b≤a。

对任意 cut c，链中 A≤c 的点均映入 B≤c，所以

\[
|F_{\le c}|-|E_{\le c}|
=|A_{\le c}|-|B_{\le c}|
\le m-e-\ell. \tag{24}
\]

若另有 F<E，取 c=max F 得

\[
e+f+\ell\le m. \tag{25}
\]

双满情形 m=q+4、ℓ≥q−2，故 e+f≤6，与 e,f≥4 冲突。ℓ 必须数**实际完整链**；局部边数、外侧支持人口或未兑现的可组合端点不能替代 ℓ。这个公式与主定理的匹配结算是同一收益，不另计第二次下降。

## 5. 独立辅助：零 through 的逆序红四禁形

**辅助工作引理。** 设 D 无 R6、B6，U=Src_R5(D)、V=End_R5(D)，且 U∩V=∅。不可能同时存在两条实际红四

\[
R4(v_1,v_2,v_3,v_4)<R4(u_1,u_2,u_3,u_4),
\qquad v_i\in V,\quad u_i\in U, \tag{26}
\]

其中“<”表示前一条的全部实际点均早于后一条的全部实际点。

若 χ(v3,v4,u1)=R，则红四 (v1,v2,v3,v4) 追加 u1 成 R5，迫 v1∈U，与 v1∈V、U∩V=∅ 矛盾。因此 χ(v3,v4,u1)=B。

若 χ(v4,u1,u2)=R，则 v4 前接红四 (u1,u2,u3,u4) 成 R5，迫 u4∈V，与 u4∈U 矛盾。因此 χ(v4,u1,u2)=B。两者给实际 B4(v3,v4,u1,u2)。

取 D 内终于 v3 的一条实际 R5，末前驱为 d；取 D 内始于 u2 的一条实际 R5，其第二点为 t。实际顺序为

\[
d<v_3<v_4<u_1<u_2<t. \tag{27}
\]

若 χ(d,v3,v4)=R，入 v3 的红五追加 v4 成 R6；若 χ(u1,u2,t)=R，出 u2 的红五前接 u1 成 R6。两者均被假设禁止，故这两个桥也都蓝。于是四个连续蓝三元组给

\[
B6(d,v_3,v_4,u_1,u_2,t), \tag{28}
\]

违反 D 无 B6。引理得证。

主定理的证明更短，**不依赖此辅助引理**；它保留为独立可用禁形，不与根分离、匹配矛盾重复计收益。

## 6. 竞争路线：交错外供的右继红源闭合

本节的 D_p、V_p 是独立竞争路线中的记号，分别表示 basis 的 p−1 点部分与完整 private 外供族；它们不等于前文中性区 D 或其红五终点族 V。

### 6.1 参数、完整成员与额外右继条件

设 p≥3，X 是完整有序 signotope，禁 B_(p+1)、R_(p+2)，以及同实际端点的 R_(p+1)+B3。给定完整约束族 F，其红成员全为实际 R_(p+1)，蓝成员全为实际 Bp。目标是实际分划 K⊔Y=X，使每个原红成员同时遇 K、Y，每个原蓝成员遇 K。全过程保留完整 F，不删成员或选择有利子族。

假设红成员族的横截数为 p，且全部 minimum 红横截恰为 p 个两两不交块 G_i 的 rank-1 product bases。每个 G_i 是实际红块，大小至少 2，每个 product basis 都是实际 Bp。写 G=∪G_i；每个原红成员 H 的 trace H∩G 都包含某个完整块 G_i。

其中一个块恰有 p 点，记 A={a1<⋯<ap}。选择一个 basis S=D_p⊔{s}，其中 s∈A、|D_p|=p−1、D_p<A。在这个固定 basis 位置，假设全部 s-private 原红成员（即 H∩S={s}）都遇 G 外。

由 trace 条件、private 性和点数，这些全部 private 成员恰为 A⊔{v}，v∉G。以 V_p 收集**全部**这样的外点；S 的 minimality 保证 V_p 非空。记 d*=max D_p，并为每个 v∈V_p 定义

\[
\sigma(v)=\min\{d\in D_p:d>v\}. \tag{29}
\]

下面的位置引理将保证 σ 总存在。本工作定理额外要求：每个 σ(v) 都是 ambient R_(p+1) 源。

**工作定理（交错外供右继红源闭合）。** 在上述完整假设下，

\[
Y=D_p\cup V_p,\qquad K=X\setminus Y \tag{30}
\]

满足完整 F。因而在完整 F 的 UNSAT 背景下，此类机制整体被排除，不是仅新增一个必要条件。右继红源是明确额外条件，不能从任意 product 或任意外供自动推断。

### 6.2 自足的位置引理

先证明 d*⊔A 是实际 R_(p+1)。任取 x<y∈A。若对所有 d∈D_p 都有 χ(d,x,y)=B，由每个 D_p⊔{a} 都是 Bp，D_p⊔{x,y} 的全部三元组便都蓝，给 B_(p+1)，矛盾。因此某个 d∈D_p 使 χ(d,x,y)=R。若 d<d*，packet(d,d*,x,y) 前三项为 (B,B,R)，至多换色一次迫末项 χ(d*,x,y)=R；若 d=d* 则已得所需颜色。A 内部红，因此

\[
R_{p+1}(d^*,a_1,\ldots,a_p). \tag{31}
\]

再取任意实际红 A⊔{v}，v∉A。若 v>d*，分三种位置。

第一，v>a2。红 A⊔{v} 的最前两点是 a1、a2，χ(d*,a1,a2)=R，所以可前接 d* 成 R_(p+2)，矛盾。

第二，a1<v<a2。禁 R_(p+2) 迫 χ(d*,a1,v)=B，否则 d* 可前接红 A⊔{v}。对每个 d<d*、d∈D_p，packet(d,d*,a1,v) 的首末项都蓝，故全蓝，特别 χ(d,d*,v)=χ(d,a1,v)=B。

第三，d*<v<a1。禁 R_(p+2) 迫 χ(d*,v,a1)=B。另一方面，(31) 的红(p+1)与蓝三 (d*,v,ap) 若同端就成禁形，故 χ(d*,v,ap)=R。对每个 d<d*、d∈D_p，packet(d,d*,v,ap) 形为 (?,B,?,R)，迫 χ(d,d*,v)=B；再看 packet(d,d*,v,a1)=(B,B,?,B)，迫 χ(d,v,a1)=B。

后两种情形中，对任意 d<e<d*、d,e∈D_p，packet(d,e,d*,v) 的首末项都蓝，迫 χ(d,e,v)=B。加上 D_p⊔{a1} 是蓝 basis，得到 D_p⊔{v,a1} 的所有三元组均蓝，即 B_(p+1)，仍矛盾。

所以任何这样的 v 都有 v≤d*。实际 V_p⊂X∖G，故 v不能等于 d*∈G，最终得到

\[
v<d^*<a_1\quad(v\in V_p),\qquad
v\in\operatorname{Src}_{R_{p+1}}(X). \tag{32}
\]

源身份由实际红 v⊔A 兑现。特别，(29) 的 σ(v) 总存在。

### 6.3 完整红成员同时遇两侧

对任何原红成员 H，若 H遇 D_p 就遇 Y。否则 H∩D_p=∅，又 S 是红横截，故 H∩S={s}；它是前述完整 s-private 族的成员。因此 H=A⊔{v}，v∈V_p⊂Y，仍遇 Y。

另一方面，Y∩G=D_p。D_p 在每个块中至多一个点，而每块至少两个点，所以 Y不能包含任何完整块 G_i。每个原红成员的 trace 都包含某个完整块，故没有原红成员全落 Y。于是每个原红成员也遇 K。这一验证针对完整 F 的全部红成员。

### 6.4 交错位置下已经强制的全部所需颜色

记 a=ap。对 v∈V_p、d∈D_p，若 v<d，实际红 v⊔A 与同端蓝三 (v,d,a) 不能共存，所以 χ(v,d,a)=R。对 v<w∈V_p，同理有 χ(v,w,a)=R。

若 d<v，则 d<v<d*<a。packet(d,v,d*,a) 的末两项 χ(d,d*,a)=B、χ(v,d*,a)=R，迫前两项均蓝，特别 χ(d,v,a)=B。于是

\[
\begin{aligned}
&\chi(v,d,a)=R &&(v<d,\ v\in V_p,\ d\in D_p),\\
&\chi(v,w,a)=R &&(v<w,\ v,w\in V_p),\\
&\chi(d,v,a)=B &&(d<v,\ d\in D_p,\ v\in V_p).
\end{aligned} \tag{33}
\]

以下三类 packet 分别强制所需交错颜色：

- v<d<e，v∈V_p、d,e∈D_p：packet(v,d,e,a)=(?,R,R,B)，迫 χ(v,d,e)=R，即 VDD 红。
- v<d<w，v,w∈V_p、d∈D_p：packet(v,d,w,a)=(?,R,R,B)，迫 χ(v,d,w)=R，即 VDV 红。
- d<v<e，d,e∈D_p、v∈V_p：packet(d,v,e,a)=(?,B,B,R)，迫 χ(d,v,e)=B，即 DVD 蓝。

这里只固定这三类所需颜色，不声称其他交错类型也固定。

### 6.5 一般 joining 与蓝成员的完整排除

先记一般 joining 事实：ambient R_(p+1) 源 t 不能是 Bp 终点。否则取入 Bp 的末前驱 u，与出红(p+1)的第二点 w；χ(u,t,w) 蓝给 B_(p+1)，红给 R_(p+2)，两色都矛盾。因此 (32) 保证 V_p 中每点不能作为 Bp 终点。

若 Y 内有实际 Bp，因为 |D_p|=p−1，它至少含一个 V_p 点；其末点不能在 V_p，故末点 d∈D_p。VDD、VDV 红排除两类连续交错，使这条蓝路径的顺序形状只能是

\[
D_L<V_C<d,\qquad
D_L\subseteq D_p,\quad \varnothing\ne V_C\subseteq V_p. \tag{34}
\]

取 v*=max V_C，d0=σ(v*)≤d。按额外右继条件，d0 是 ambient R_(p+1) 源。若 d0=d，原 Bp 终于红源，已经违反 joining。

若 d0<d，把原蓝路径末点 d 换成 d0。对任意 v<w∈V_C，packet(v,w,d0,d)=(?,B,R,R)，迫 χ(v,w,d0)=B；对任意 d_L∈D_L、v∈V_C，χ(d_L,v,d0)=B 由 DVD 蓝给出；任意两个 D_L 点与 d0 都在蓝 D_p 内，三元组也蓝；其他三元组继承原蓝路径。因此替换后仍是实际 Bp，终点为红源 d0，再违 joining。

所以 Y 内无 Bp。原完整 F 的每个蓝成员都是 Bp，不可能全在 Y，故全部遇 K。结合 §6.3，分划 (30) 满足完整 F，定理得证。

### 6.6 右继条件的自然兑现与剩余范围

若每个被 V_p 占据的间隙，其右继 σ(v) 都是某个大小 p+1 的实际红块的最小点，该整块直接兑现 σ(v) 的 ambient R_(p+1) 源身份，故可调用定理。允许其他短块以及 D_p 中的非源点；只须这些非源点紧前的间隙没有 provider。

原先 V_p<min D_p 且 min D_p 为红源的机制是本定理的特例；上一稿最左分离红块大小至少 p 给 min D_p 红源的自然兑现推论也继承。仍开的情形是：某个有实际外供的间隙，其右继不是 ambient 红(p+1)源。不能据本定理宣称一般完整 F 机制已经关闭。

代 p=5，背景禁形为 B6、R7、同实际端点 R6+B3。本定理没有产生无条件数值下降，且全部新增继续为 unreviewed/unaccepted。

## 7. 亏一主线：单侧满标准接口整类排除与双近满残余

### 7.1 临界 canonical 的完整分类

仍设 |X|=3b+4。任一方向的原 canonical 分解为 X=H0⊔R0，其中 H0 为 766，R0 为容量至多 b+5 的 D7。置

\[
d=2b-|H_0|\in\{0,1\},\quad
\Omega=\{e\in R_0:\text{有 }H_0\text{-origin ambient R6 终于 }e\},
\quad S_0=R_0\cap S,\quad J=R_0\setminus(\Omega\cup S_0).
\tag{35}
\]

这里 S 仍是全部全局 R6 源。定义 M=R0∩S∩End_R5(X)∩Src_B5(X)。旧三链工具将每个 m∈M 的全部出 R6 终点与全部出 B5 第二点锁定为同一个 h(m)。联合预算为

\[
|J|+|M|+
\bigl|\Omega\cup\bigl(h(M)\setminus(H_0\cup J)\bigr)\bigr|
\le d. \tag{36}
\]

d=0 时整侧为满标准接口。d=1 且 |J|=1 时，真实 promotion 也兑现满标准接口。其余未提升情形恰有三种：Ω=J=M=∅；仅 M={m} 非空且 h(m)∈H0；仅 Ω={ω} 非空且 J=M=∅。后文不把这些未提升方向虚构为满核。

### 7.2 每个未提升方向都产生统一的满 D7 基底 W

先考虑 Ω=J=∅，包括 M为空或 M={m} 的两种情形。此时全部全局源 S=R0，大小 b+5。取 W=S、δ=0，W为 D7。若 M={m}，锁点 h(m)∈H0 且是全局 R6 终点，故不在 W∪U。

W∪U 的内部 junction 不在 W：W 内点启动的内部 B4 可延为 ambient B5，若同时结束 R5 就必须属于 M；若该点为 m，延长保留的第二点又被锁定为 h(m)，但 h(m)不在 W∪U，仍矛盾。

令 E_W=End_R6(W)。取 W 内终于 e 的红六，末前驱为 r。若 W∪U 中有 B3(e,x,y)，禁 R7 迫 χ(r,e,x)=B，得到 B4(r,e,x,y)，再延为 ambient B5。若 r∉M，违反 mixed 角色条件；若 r=m，第二点 e必须等于 h(m)，但 e∈W 而 h(m)在 W外，矛盾。因此 E_W 为 W∪U 的完整右红根。

再考虑 Ω={ω}、J=M=∅。先证明全部 H0-origin 源只有一个。置 A_H=H0∩S，它非空；canonical 的 G 角色给每个 a∈A_H ambient 入 R5 与出 B5，其全部出 R6 终点均为 ω，三链因而将所有出 B5 第二点也锁为 ω。R0∖{ω} 全属 S。无论 ω是否也属于 S，都有

W=S∖{ω}=(R0∖{ω})⊔A_H。

每个全局 R6 源都无 ambient B5 终点。任何终于 S 的 B4 都能接该源的一条出 R6 第二点，保首 pair 延成 B5：若桥红，原 B4 的末前驱前接该出红六便成 R7，所以桥蓝。

W 内的 junction 若在 R0∖{ω}，其 B4 延成 B5 就令该点属于原 M=∅；若在 A_H，延成 B5 的第二点必须为 ω，然而 ω不在 W。两者均不可能，故 W 是 D7。由 |W|=b+4+|A_H|≤b+5 及 A_H非空，迫 A_H={a}。这是实际推导出的唯一性，不是预设。

因此该情形 W也有 b+5 点。令 δ=1[ω∈S]≤1；ω∈T，所以 W∪U 上位于 a的潜在 junction 仍因其锁点 ω在外而被排除，E_W 的右根提升也由同样的锁第二点论证成立。

三个未提升情形统一给出

\[
W\subseteq S,\quad |W|=b+5,\quad
S\setminus W=\delta\{\omega\}\subseteq T,\quad \delta\in\{0,1\},
\quad W\text{ 为 D7},
\tag{37}
\]

且 W∪U 的全部内部 junction 只能落在 U，E_W 是 W∪U 的完整右红根。δ=0 时不需要实际引入 ω，后文所有含 δ 的 ω项按 0 理解。

### 7.3 对侧满核兑现纯前供及精确人口

现在假设反向已经兑现满标准接口：T 为全部全局 R6 终点，|T|=b+4，H'=X∖T 有 2b 点，并具有 T 的 mixed 禁形和首点延长。记

\[
I_W=W\cap T,\quad I_{\rm full}=S\cap T=I_W\sqcup\delta\{\omega\},
\quad P_{\rm full}=S\setminus T=W\setminus T,
\quad u=|U|,\quad v=|V|. \tag{38}
\]

只使用 H' 的单满角色分划，即可得 Z'=P_full⊔U=Src_R5(H')，大小恰为 b。确实，P_full 中点有 R6 后供，不能是 B5 终点，故由满 H' 角色落入 Src_R5；U也属于该角色族。又 D=H'∖P_full，删除 U 后 D 无 R5，换色 756 容量给 u≥|D|−b=b−|P_full|，角色族大小给相反不等式，所以全部取等。于是

\[
|Z'|=b,\quad |I_W|=u+5,\quad |I_{\rm full}|=u+5+\delta,
\quad |D|=b+u,\quad v\ge u. \tag{39}
\]

最后 v≥u 由删除 D 内全部 R5 终点 V 的换色容量给出。此处不需要 H0满，也不需要本侧已经 promotion。

### 7.4 普通左 Hall、亏一右 Hall 与完整链

W∪U 的 junction 只能在 U。删除全部 good 后为 D7，故 b+5+u−|good|≤b+5，迫全部 U都是 good。每个 good u0的入 R5 与内部 B4(u0,i,x,y) 延成的 B5 joining，得到末 pair 为 (u0,i) 的实际 R6，因此 i∈I_W∖E_W，并带全部 ambient 蓝 fan χ(u0,i,z)=B（z>i）。

对任意 C⊆U，实际集 (W∖N(C))∪C 为 D7，容量给普通 Hall。删除 E_W 后为 756，故 |E_W|≥5；Hall 的目标 I_W∖E_W 必须容纳 u 个点，又迫 |E_W|≤5。因此

\[
|E_W|=5,\qquad A_0=I_W\setminus E_W,\quad |A_0|=u,
\qquad U\longleftrightarrow A_0\text{ 有 perfect 外匹配}.
\tag{40}
\]

反向 T∪V 使用标准 mixed 接口与 |T|=b+4，给 bad≤1、完整外 Hall 匹配至少 v−1 条，目标为 B0=I_full∖F，其中 F=Src_R6(T)⊂I_full。删除 F 后为 756 给 |F|≥4；这里不预先声称 F只有 4/5 根。

D 内全部 R5 的 U→V 端点图有覆盖全部 U 的匹配：否则 König cover 至多 u−1 个端点副本，删除对应实际点后至少剩 b+1 点且无 R5，违换色 756 容量。左外 perfect 经中间匹配使用 u 个 V 副本，右外匹配至多漏一个 V，因此得到至少 u−1 条实际完整链

\[
A_0\longrightarrow U\longrightarrow V\longrightarrow B_0,
\qquad b_0\le a_0\text{ 对每条完整链成立}. \tag{41}
\]

最后的顺序比较仍由两侧全 ambient 蓝 fan 与中间实际 R5 的同端 weak7 矛盾给出，不能由孤立局部边代替。

### 7.5 对侧纯前供强迫 F<E_W

任取 f0∈F，取 T 内始于 f0 的实际 R6，记第二点为 t。则 t∈T∩Src_R5(X)，T 的 mixed 禁形迫 t无 ambient B5 终点。Z' 中点也都无 ambient B5 终点：P_full 用其 R6 后供，U用其 D 内 R5 后供 joining。

因此 Z'+t有 b+1 点、无 B5、继承无 weak7，756 容量迫实际 R6。Z'⊂X∖T，故这条红六的末点只能为 t，首点属于 Z'∩S=P_full。写为

\[
R6(p_0,z_1,z_2,z_3,z_4,t),\qquad
p_0,z_1,z_2,z_3,z_4\in Z',\quad p_0\in P_{\rm full}.
\tag{42}
\]

原出 f0红六的首 pair (f0,t) 具有全左蓝帽：更早点若作红桥就可前接成 R7。若 p0<f0，该帽给 B3(p0,f0,t)，与 (42) 同实际端点，违反 weak7。p0=f0 又因 P_full∩T=∅ 不可能，故 p0>f0。

令 e*=min E_W。若 p0>e*，则 p0,z1∈Z'⊂W∪U，右根性质给 χ(e*,p0,z1)=R。把 e* 前接到 (42) 前五点构成的 R5，得到终于 z4∈Z'⊂X∖T 的 R6，矛盾。p0=e* 因 P_full∩I_W=∅ 排除。所以

\[
f_0<p_0<e^*\quad\text{对每个 }f_0\in F,
\qquad F<E_W. \tag{43}
\]

分离先迫 E_W 的五点与至少四点 F 不交，均在大小 u+5+δ 的 I_full 内，故 u≥4−δ≥3，(41) 的 u−1 链数合法。对任意 cut c，完整链给 A0前缀−B0前缀≤1；代入两层实际定义得到

\[
|F_{\le c}|-|(E_W)_{\le c}|-
\delta\,\mathbf1[\omega\le c]\le1. \tag{44}
\]

取 c=max F，(43) 给 |F|−δ·1[ω≤c]≤1，即 |F|≤2，与 |F|≥4 矛盾。这样对侧满核的 b 点纯前供绕过了本侧 H0缺失的纯尾；没有声称本侧发生了虚构 promotion。

### 7.6 至少一侧满标准接口的整类排除

**工作定理（单侧满标准接口整类排除）。** 在 |X|=3b+4 时，只要任一方向已经兑现满标准接口，整个临界候选就不可实现。

证明：另一方向按 §7.1 分类。d=0 或 d=1、|J|=1 时真实兑现双满，调用 §3 的统一四/五根排除；其余 Ω0/M0、Ω0/M1、单 Ω三种情形均由 §7.2—7.5 的 W 论证排除。反序适用。

因此“未提升亏一”不再笼统全部开放，剩余仅能在**两侧都未提升**的机制中寻找。尚未证明全部临界配置至少有一侧满标准接口，不能把这个进入条件擅自加入一般配置。

### 7.7 双 Ω0/M 近满：端点盈一分支排除

现在双方均 Ω=J=∅，每侧允许 M为空或单点，锁点各自在本方向 H0内。此时全局 S、T各有 b+5 点，H=X∖S、H'=X∖T各为 2b−1。参数身份为

\[
|I|=q+6,\quad |P|=|Q|=b-q-1,\quad |D|=b+q,
\quad q\ge-1. \tag{45}
\]

这里不能预先假定 q≥0。近满 H 中 B5 源至少有 b−1 个，Q⊔V与其不交，故 v≤q+1；删除 V 的 D 容量给 v≥q。反序同理，得到

\[
u,v\in\{q,q+1\},\qquad u,v\ge0. \tag{46}
\]

W=S∪U、W'=T∪V 的基底 mixed 异常都锁到外部，所以全部 U、V 都 good，普通 Hall 分别覆盖全部 U、V，且 E、F 的完整右/左根提升成立。S、T本身为满 b+5 的 D7，横截删除容量及旧 D7 横截界给

\[
\tau_{R6}(S)=\tau_{R6}(T)=5,
\qquad e=|E|,\ f=|F|\in\{5,6\}. \tag{47}
\]

横截数为 5 不表示六个根都是 minimum 横截，后文不作这种替换。

先设 v=q+1，则 Z=Q⊔V 恰有 b 点。右侧普通 Hall 的目标大小 q+6−f≥v，迫 f≤5，故

\[
|Z|=b,\quad f=5\qquad(v=q+1). \tag{48}
\]

当 q≥0，D 内中间 R5 端点匹配至少有 q 条。q=0 时取空匹配；只有 q≥1 时才使用 König 反证：若最大匹配≤q−1，删至多 q−1 个端点对应实际点，剩至少 b+1 点且无 R5，违换色 756 容量。两侧外匹配覆盖全部 U、V，故可复合得到 q 条实际完整链。逐链顺序比较给

\[
|F_{\le c}|-|E_{\le c}|\le(q+6-e)-q=6-e.
\tag{49}
\]

取 c=max F，记 E_low={e0∈E:e0≤max F}、k=|E_low|。由 f=5 得

\[
k\ge e-1. \tag{50}
\]

对任意低根 e0∈E_low 的每一条 S 内 R6，取其末前驱 p。若 p不是唯一 M点 m，则 p无 ambient B5 源。满核 Z+p的纯尾与 F 的完整左根屏障可按 §2 逐步应用，直接迫 e0>max F，矛盾。因此全部这些低根对应的所有 S 内红六都以同一个 m为末前驱；若 M为空，则低根根本不存在。

M={m} 时，实际集合 (E∖E_low)∪{m} 命中 S 的全部 R6：高根对应路径由终点命中，低根对应路径由同一末前驱 m命中。τ=5 因而迫

\[
e-k+1\ge5,\qquad k\le e-4, \tag{51}
\]

与 (50) 矛盾。M为空时 k=0，也直接与 (50)、e≥5 矛盾。反序同理排除 u=q+1。

边界 q=−1 时由 (46) 有 u=v=0，I有五点；E、F各至少五点，故 E=F=I。此时 Q满 b点，全部 E根都属于低根。同一纯核屏障迫全部 S 内 R6经过唯一 m，违反 τ=5；M为空则直接矛盾。因此该边界也被排除。

### 7.8 双未提升的精确剩余

双 Ω0/M 近满机制只剩

\[
u=v=q\ge0,\qquad
|Q\sqcup V|=|P\sqcup U|=b-1. \tag{52}
\]

这是仍开的近满分支，不能称为双满。除此之外，双未提升中的单 Ω×单 Ω、单 Ω×非 Ω机制仍开。本节没有排除这些残余，也没有证明一般临界候选一定进入已排除的单侧满标准类。

## 8. 当前全局覆盖与数值分账

本轮排除全部双满标准临界接口，并进一步排除全部至少一侧已兑现满标准接口的临界机制。不能继续把双满四根/混合根或单侧满、另一侧未提升列为开放。当前覆盖与剩余为：

| 临界机制或竞争接口 | 本稿结论与范围 |
|---|---|
| 双满标准，双四根/混合四五根/双五根，任意 τ4/5 | §2—3 整支排除 |
| 至少一侧满标准，另一侧任一 canonical d0/1 机制 | §7.1—7.6 整支排除 |
| 双 Ω0/M 近满，u或v=q+1，含 q=−1 边界 | §7.7 排除 |
| 双 Ω0/M 近满，u=v=q≥0，两纯角色核均 b−1 | §7.8 仍开；不是双满 |
| 双未提升中的单 Ω×单 Ω、单 Ω×非 Ω | 仍开 |
| 完整 F 的交错外供，每个有供间隙右继均为红源 | §6 完整 SAT 分划，UNSAT 背景下整类排除 |
| 完整 F 的有供间隙右继非源 | 仍开 |

一般 |X|=3b+4 的临界 767 尚未全部进入已关闭机制，故不能宣称无条件 N767≤3b+3，亦不能宣称无条件 N777≤3b+4。

保留当前工作链

\[
N757\le a+b-1,\qquad C766\le2b,
\qquad N767\le3b+4,\qquad N777\le3b+5. \tag{53}
\]

代入 a=16、b=25，分别为 40、50、79、80。这里继续保持原始结果、证书状态与接受状态的既有分层，本文没有读取新证书或升级证明状态。

只有最终排除**所有**临界机制，才可能兑现条件目标 N767≤78、N777≤79；本稿尚未实现该无条件新降。主定理、抽象缺额公式与辅助引理均不按多个独立全局 saving 累加。

## 9. 文档回执与保证边界

本文全部新增 **unreviewed/unaccepted**。文档执行者角色为项目指定原生 Sol/high 的转写与文档操作角色；这不是独立数学审阅，未报告的 backend 或实际 effort 不作验证结论。

文档检查仅涵盖指定写入范围、UTF-8、公式号、本地链接、状态措辞及固定算术；记录于指定 `tmp/n7_pure_core_root_separation_20261030/DOCUMENT_CHECK.json`。该回执的 `PASS_DOCUMENT_ONLY` 仅表示这些文档项目通过，不表示证明已经独立验证、accepted 或 assurance 升级。本文已转写主会话当前批准的全部段落，未留下“亏一待补”的占位，开放分支按 §8 精确保留。
