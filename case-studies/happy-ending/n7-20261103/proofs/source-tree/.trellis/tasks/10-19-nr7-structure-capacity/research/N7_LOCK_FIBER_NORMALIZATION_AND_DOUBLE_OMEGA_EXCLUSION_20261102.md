# N7：残余锁纤维换核与双 Ω 临界类排除

日期：2026-11-02。状态：**工作证明；全部新增 unreviewed/unaccepted，未独立审阅、未接受**。本文仅忠实整理主会话批准的数学内容。主会话及其数学协作者的推导与交叉核对属于同会话生成核对，不构成独立数学 review。指定 native gpt-6.1-sol/high 文档执行者仅转写和检查文档一致性，不自主数学研究、不补证；未报告的 backend 或实际 effort 不声称已核实。

本轮先通过真实换核消去残余 M*，再完整排除一侧 Ω、另一侧 clean 的全部正缺额机制。双侧 η 等于锁点数时，完整实际 middle 与 neutral 纤维预算排除 x≤y 的全部机制；双 η1 的三个根次序均排除。竞争路线给严格完整 F 下的同块换代表定理。旧 onefull、bothclean 沿用不重计，真正剩余双 Ω 机制仍明确保留。全局工作参数界保持，进一步下降一尚未证明。

唯一新增文件为本文及 `tmp/n7_lock_fiber_double_omega_20261102/DOCUMENT_CHECK.json`。旧稿、task.json、metadata、接受/assurance、绑定、runtime、运行及指针保持，不 commit、不 archive。未调用外部 Claude、未向外传材料，未执行科研代码、枚举、SAT、solver 或 proof 检查；仅用 PowerShell 作文档操作与一致性检查。

## 1. 模型、实际角色与依赖

沿最新 endpoint 稿的完整模型：有序 rank-3 signotope 的四点 packet 按 abc、abd、acd、bcd 至多换色一次。路径按实际顶点计长，并对子序列遗传。weak7 比较同一对实际首末点的反色路径，长度和至少 9，内部允许共享。767 禁 R7、B6、weak7；756 禁 R6、B5、weak7，其换色模型禁 R5、B6、weak7。b 是两种 756 模型共用的有效人口容量上界；N_sig 表示各模型的最大允许人口，不是强迫阈值。

本轮研究 n=3b+3、w=0 的临界层，全部角色在同一母体 X 中实际计算：

\[
S=\operatorname{Src}_{R6}(X),\quad T=\operatorname{End}_{R6}(X),\quad
I=S\cap T,\quad P=S\setminus T,\quad Q=T\setminus S,\quad
D=X\setminus(S\cup T),\quad
U=\operatorname{Src}_{R5}(D),\quad V=\operatorname{End}_{R5}(D).
\tag{1}
\]

ambient 指 X；注明域内的 Src、End 保留全部实际路径。以下匹配保留实际端点或相邻 pair，允许路径内部共享；不同角色层可在实际点上交叠，删 cover 时只按对应实际点计。

依赖均保持旧保证层级：

- [endpoint 两类统一排除稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_ENDPOINT_PAIR_HALL_MISALIGNMENT_EXCLUSION_20261102.md>) §1—6：模型、实际端点对 Hall、全部 onefull 与双侧 nonΩ/M0 排除；§7 为严格完整 F 的区间分划背景。
- [Hall 归一化与零 through 稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_HALL_DEFECT_ROOT_AUGMENTATION_AND_ZERO_THROUGH_CLOSURE_20261101.md>) §5：η≤2 的真实归一化、残余 mixed 与完整 port。
- [锁端口吸收稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCKED_PORT_ABSORPTION_AND_COMPLETE_REPARTITION_20261101.md>)：最早源、实际锁 pair、完整 Ω 供应与 F 旧位置引理。
- [weighted 稳定性稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7879_INTERFACE_AUDIT_AND_WEIGHTED_THROUGH_STABILITY_20261031.md>)：完整 port 与实际头尾替换；含 Ω 时本轮使用完整 port，不误用 clean 的更强蓝禁形。
- [参数工作界稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_DEFECT_ONE_PREDECESSOR_COMPRESSION_AND_GLOBAL_BOUND_20261031.md>)：全模型工作界及旧保证边界。
- [纯核与 private 重分划稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_PURE_CORE_ROOT_SEPARATION_AND_INTERLEAVED_REPARTITION_20261030.md>)：严格全部 F、全部 minimum bases 与旧位置引理。
- [R20 精确关系稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>)：合法 chart 删根与实际反向添点给精确 +1。

旧全部 onefull 及 bothclean 已完全排除，本轮沿用，不重新计数值 saving。

## 2. 消去残余 M* 的真实换核

一般左归一化中，H* 有 2b−η 点、η≤2。全部 H*-origin R6 终点的精确集合为 Ω⊂T∖H*。令 A_H=H*∩S⊂P、a=|A_H|；每个 owner 有 ambient 入 R5、出 B5，其全部出 R6 终点与 B5 第二点唯一锁在某 ω∈Ω。

残余 M*⊂P∖H* 是全部余下 mixed 源，每个 m0∈M* 锁 h(m0)∈H*∩T，且 o+|M*|≤η，其中 o=|Ω|。W=S∖(Ω∩S)=(R*∖Ω)⊔A_H 是旧实际有效 D7，|W|=b+h、h=3+η−o+a≤5。

令 m=|M*|、Λ=h(M*)、t=|Λ|≤m。由于 A_H∩T=∅，Λ⊂Q；删除它不删旧 H* 来源。定义

\[
H_{\rm new}=(H^*\setminus\Lambda)\sqcup M^*,\quad
\Omega_{\rm new}=\Omega\sqcup\Lambda,\quad
\eta_{\rm new}=\eta-m+t,\quad
R_{\rm new}=(R^*\setminus M^*)\sqcup\Lambda.
\tag{2}
\]

新核无 R6：任何新源只能在 A_H 或 M*；前者全部终点在域外 Ω，后者全部终点在域外 Λ。B6、weak7 遗传，因此 H_new 是真实 766。旧 A_H 全保留，各 Ω 的旧供应仍实际，Λ 各有 M* 供应，所以 Ω_new 恰为全部 H_new-origin 红六终点，新 A_H 为 A_H⊔M*。

R_new∖Ω_new⊂S。全部旧残余 mixed 源已吸收入核，新加到 R 的 Λ⊂Q 不是源，故 M_new=∅。同时

\[
o_{\rm new}=o+t\le\eta-m+t=\eta_{\rm new}\le\eta,\quad
\delta_{\rm new}=\delta=|\Omega\cap S|,\quad
W_{\rm new}=W,\quad
3+\eta_{\rm new}-o_{\rm new}+a_{\rm new}=h.
\tag{3}
\]

两方向可各自做该操作，不改变 X 或任何 ambient 角色。这是实际归约，不是单独数值 saving，不能把 M 仅在人口式中抹掉。

## 3. M0 后的完整实际根工具

之后均用 M0 归一化。Ω 非空的全部参数类型只有

\[
(\eta,o,a)\in\{(1,1,1),(1,1,2),(2,1,1),(2,2,2)\},
\tag{4}
\]

直接来自 1≤o≤η≤2、a≥o、h≤5。右对偶记 Ψ、B_H、β、p、d，p 为右锁数；竞争 F 节的 p 是另一个局部符号。M0 意味着 W 中除 A_H 外，全部 ambient End_R5 点均无 B5 源；双向完整 port 保持。

令 W'=T∖(Ψ∩T)，定义全部 ambient 相邻对根

\[
\begin{aligned}
\widehat E&=\{e\in W\cap T:\text{某 ambient R6 末 pair 为 }(s,e),\ s\in W\},\\
\widehat F&=\{f\in W'\cap S:\text{某 ambient R6 首 pair 为 }(f,t),\ t\in W'\}.
\end{aligned}
\tag{5}
\]

这些集合不是只取内部红六或选定见证。末帽及 weak7 给：若末 pair (p,e) 和 R6(p→z) 同存，则 z≤e；首 pair (f,t) 和 R6(z→t) 同存，则 z≥f。R7 帽同时给跨末/首相邻对的蓝三。

加强根扇为：若 e∈Ehat、e<z<t 且 t∈S∪U，则 χ(e,z,t)=R，middle z 可在 ambient 中；Fhat 完整对偶只要求首点在 T∪V，middle 也可 ambient。若相反为 B3，原末/首帽给 B4；从最后 S/U 点向右，或最前 T/V 点向左延长，保原相邻 pair 为 B5，违反 complete port。Ehat、Fhat 自身均为红 clique，大小至多 6；内部 R6 横截数至少 h，给 |Ehat|≥h，右侧同理。

完整 ambient 尾替换如下。取 R6(v1,v2,v3,z4,z5,z6)、z4∈End_R5(X)、z5<f∈Fhat；取入 z4 红五末前驱 d，及 f 原首 pair (f,t)，t∈W'。若 χ(d,z4,z5)=R，原入红五追加 z5、z6 成 R7，所以它为 B。若 χ(z4,z5,f) 也为 B，首帽 χ(z5,f,t)=B 给 B5(d,z4,z5,f,t)，其末 pair (f,t) 两点均在 W'，违完整反 port。因此该三元组为 R，可以替尾为 f。头替换完整反序，第三点须有 Src_R5(X) 身份。含 Ω 时这里使用完整 port，不能误用 M0 就声称所有相关点无 ambient B5 终点。

每个左 owner a 有 ambient 入 R5 和 B5(a,ω,…)；joining 的蓝桥给 B6，故红桥产生另一条末 pair 为 (a,ω) 的实际 R6。右 owner b 与锁 ψ 同理给实际 R6 首 pair (ψ,b)。后文加边依赖这些真实 pair，不能把 owner-origin R6 本身误称具有该相邻 pair。

**核内相邻对跨反根红扇。** 若 r∈End_R5(H_L)、t∈H_L，且 r<t<f∈Fhat，则 χ(r,t,f)=R。假设为 B，取 f 实际 R6 首 pair (f,v)、v∈W'，帽给 χ(t,f,v)=B。取 H_L 内入 r 红五的末前驱 d；若 χ(d,r,t)=R，直接得到完全位于 H_L 内部的 R6，因为 t∈H_L，矛盾。所以该桥为 B，形成 B5(d,r,t,f,v)，末 pair (f,v) 两点均在 W'，且 v 有 Src_R5(X) 身份，违完整反 port。完整反序同理。

该加强不需要 Ω>f，也不要求 t 有额外角色。严格根分离中 forced 尾点若落在 (y,x)，所有 f≤y，便不满足 t<f，不能借该红扇宣称分离类闭合。

## 4. 一侧 Ω、另一侧 clean 的全部正缺额机制排除

### 4.1 人口、最早纤维与 ordinary 低前驱

左 α∈{1,2}、Ω 非空且 M0，使用 o、a、L=Ω∩S、δ、W 和 h=3+α−o+a。反向 clean：H'=X∖T、|H'|=2b−β、β∈{1,2}，Ψ=M'=∅。记 |D|=b+q，暂不预设 q 非负，则

\[
|T|=b+3+\beta,\quad i=|I|=q+3+\alpha+\beta-o+a+\delta,\quad
|P|=b-q-\beta,\quad H=D\sqcup Q_H\sqcup A_H,\quad
|Q_H|=b-q-\alpha-a.
\tag{6}
\]

令 C=End_R5(H)、C'=Src_R5(H')、c=|C∩D|、c'=|C'∩D|。C 点任何 ambient B5 第二点均在 Ω：核内入红五 joining 的蓝桥给 B6，红桥给 H-origin R6。C' 无 ambient B5 终点。

每条 Ω 纤维取最早 H-origin 源，组成 A0，|A0|=o、A0∩C=∅。后一个结论由核内入红五与 owner 出蓝五 joining：蓝桥给 B6，红桥给更早 H-origin 源到同一 Ω，矛盾。K0=C⊔A0 是实际 756。删全部 End_R5 后的换色容量给 |C|≥b−α，因此

\[
|K_0|=b-\kappa_0,\quad 0\le\kappa_0\le\alpha-o,\qquad
d_+=q+\alpha-c\ge0,\quad d_-=q+\beta-c'\ge0.
\tag{7}
\]

后两个缺额来自实际 756 集合 C∪Q_H∪A_H 与 C'∪P。

按 §3 定义 Ehat、Fhat，此处 W'=T。令 e、f 为其大小，x=min Ehat、y=max Fhat，有 h≤e≤6、3+β≤f≤6。

收集全部终于 Ehat<y、末前驱在 W 的 ambient pair：ordinary 前驱 R⊂W∖A_H，owner 前驱 R_A⊂A_H，大小分别 r、r_A。ordinary 点在 H 外且无 ambient B5 源。若 r>κ0，K0 加 κ0+1 个 ordinary 点超过 b 且无 B5（Ω 缺席），强迫 R6，其源只能是某个 ordinary p。原低末帽迫其终点≤e_p<y；全部点都有 End_R5(X) 身份，尾替换 y 后违反同端 weak7。因此 r≤κ0≤α−o，且 R_A<y。

令 k=|Ehat<y|。R∪R_A∪(Ehat≥y) 横截全部 W 内部 R6，另一边用 Fhat 与 Ehat≥y 至多交 y，得到

\[
k\le e+r+r_A-h,\qquad k\ge e+f-i-1,\qquad
q\ge2-\delta-r-r_A,\qquad m:=q+o\ge0.
\tag{8}
\]

最后一步用 r+r_A≤α−o+a=h−3≤2、δ≤o。先得到 m 非负后才调用 middle。

### 4.2 完整 middle、所有 cut 与 x=y 的直接排除

D_all=D⊔A0⊂H∩H'，人口 b+m。全部实际 R5 源包含于 (C'∩D)⊔A0，端点包含于 C∩D。若全端点二部图 matching 小于 m，König 删少于 m 个实际点，留下超过 b 点、无 R5/B6/weak7，违换色容量；角色层交叠时删点只更少。因此固定 m 条 matching，源像 J_U、末像 J_V 各 m 点，m=0 时为空 matching。只取这份 matching，不冒称全源族等于 (C'∩D)⊔A0。由实际端口大小有

\[
c'-q=(c'+o)-m\ge0,\qquad c-m\ge0.
\tag{9}
\]

任取 gap cut z，令 B=(I<z)∖(Ehat∪L)、A=(I>z)∖(Fhat∪L)。左域 C'∪P∪B 无 B5，R6 只能终于 B；末前驱若在 P∪B⊂W 就触发 Ehat，所以全部末 pair 由 C'∩D 指向 B。容量/König 给 matching≥|B|−d_-。加入全部 Ω<z 的实际锁边 a_ω→ω，包含 Ω∩Q；锁根与 B 不交，锁源 A0 与 D 不交。舍非 J_U 源至多 c'−q，故左至少 |B|+o_<z−β 条。

右域 C∪Q_H∪A_H∪A 无 B5，因为 Ω 全缺席。H-origin 源终点在缺席的 Ω，故源只能在 A；第二点若在 T 则触发 Fhat，余下只在 C∩D 或 A_H>z。容量 matching≥|A|−d_+；舍非 J_V 的 C∩D 端口 c−m 及 A_H>z，右至少 |A|−α+o−a_>z 条。

三图交会若为正，就有实际末 pair (u,r)、middle R5(u→v)、首 pair (s,v)，r<z<s，帽给 B4(u,r,s,v) 与 middle 红五同端 weak7。因此每个 gap 必须满足

\[
g(z):=|\widehat E<z|+|(\widehat F\setminus L)>z|
\ge3-o+a_{\le z}+o_{<z},\qquad |A|+|B|=i-\delta-g(z).
\tag{10}
\]

所有 Ω 低锁均计入，不仅是 δ 个 I 锁。

若 x>y，取两者中间 gap，g=0 而右侧至少 3−o≥1，矛盾。若 x=y，紧邻 y 左 gap 给 1[y∉L]≥3−o+a_<y+o_<y，唯一可能是 α=o=a=2、y∉L、A_H=A0>y、Ω>y。

此时 K0 满 b，|C|=b−α。若 Q_H 点不在 C，加到 K0 仍为 H 内无 R6、B5 且超过 b，故 Q_H⊂C。Z=C∩D 有 q+α=m 点。D_all 全部 End_R5 包含于 Z，删端点容量又迫至少 m 点，所以 End_R5(D_all)=Z。Z<y 的入红五不含 A_H>y，因此 Z<y⊂V、C<y⊂Q∪V。

取 Ehat 根 y 的实际末 pair (p,y)，p<y 不在 A_H，故 ordinary、无 B5 源，且在 K0 外。K0+p 超过 b 且无 B5，迫 R6 只能从 p 开始；帽迫终点≤y，而 y∈I 不在 K0+p，故终点<y。其五尾全在 C<y⊂T∪V。Fhat 根 y 的加强红扇对最后两点给红，直接 append y 成 R7。于是只剩 x<y。

### 4.3 修补高后继与紧邻 y 右 gap

Q0 收集全部 Fhat>x 的实际 ambient 首 pair (f,t) 中 t∈T 的点，大小 s≤β。若有 β+1 个，C' 加这些点超过 b 且无 B5（clean），迫 R6 终点为某 t；原首帽迫首点≥f_t>x，全部点有 Src_R5(X) 身份，头替换 x 违反同端 weak7。若 t∈S，Ehat 根 x 的加强扇给 χ(x,f_t,t)=R，原首帽给 B，故 Q0⊂Q。y 的第二点 t_y∈Q0 且 t_y>y，所以 s_≤y≤s−1。

修补 L_+=C∪Q_H∪A_H∪R、L_-=C'∪P∪Q0 均为 756。前者无 B5 因 Ω 缺席；H-origin R6 源终点在域外 Ω，其余 R 源的原帽迫终点<y，全部点有 End_R5(X)，尾换 y 矛盾。后者无 B5，终于 Q0 的 R6 由帽和头替换 x 排除。非负缺额为

\[
\kappa_+=q+\alpha-r-c\ge0,\qquad
\kappa_-=q+\beta-s-c'\ge0.
\tag{11}
\]

取紧邻 y 右 gap，令 B=(I≤y)∖(Ehat∪L)、A=(I>y)∖L，则

\[
|A|+|B|=i-\delta-k-\mathbf1[y\in\widehat E].
\tag{12}
\]

左域 L_-∪B 中，Q0 作为终点仍由头替换 x 排除；全部点有 Src_R5(X)，B⊂S。于是终点在 B，全部末前驱只在 C'∩D 或 Q0≤y。不能把“Q0 不能作终点”误写成“不能作末前驱”。容量 matching≥|B|−κ_-，舍 Q0≤y 至多 s−1，再加全部 Ω≤y 锁边，舍非 J_U 源，保留至少 |B|+o_≤y−β+s−s_≤y 条。

Ω 低锁即使属于 Q0 也不撞层：该 Q0 作源的普通边已全舍；锁根与 B 不交，锁源 A0 与 D 不交。

右域 L_+∪A 中，H-origin 源终点在缺席的 Ω；ordinary R 源的帽迫终点<y，新 A>y 不参与，故全在旧 L_+，矛盾。余下源在 A；第二点不在 R<y，也不在 Q_H∪A⊂T（否则触发 Fhat），只能在 C∩D 或 A_H>y。容量 matching 扣非 J_V 与 A_H>y 后保留至少 |A|−α+r+o−a_>y 条。

沿 m=q+o 条 middle，交会下界为

\[
\ell\ge |A|+|B|+o_{\le y}-q-\alpha-\beta+r-a_{>y}+s-s_{\le y}.
\tag{13}
\]

代人口、k≤e+r+r_A−h、e≤6 与 s−s_≤y≥1，得到

\[
\ell\ge(\alpha-o)+(a-o)+(a_{\le y}-r_A)+o_{\le y}
+\mathbf1[y\notin\widehat E].
\tag{14}
\]

全部项非负；α>o 或 a>o 立即为正。否则 α=o=a、r=0。x<y 有低 Ehat 根，全部实际前驱只能是 owner p。owner 出 R6 终于其锁 ω，原末 pair (p,e_p) 的帽和同端 weak7 迫 ω≤e_p；e_p∈W、Ω∩W=∅ 排等号，故 ω<e_p<y，o_≤y≥1。因此下界严格为正。

每链 r≤y<s，给实际蓝四与 middle 红五同端 weak7 矛盾。m=0 时正的交集下界已经与空 matching 矛盾，不从空图冒造链。整个 oneΩ+clean 分支关闭，含 q<0 边界、全部根数及 x=y。结合 §2，也覆盖消 M 后一侧 Ω-only、反向 clean 的机制；旧 onefull 与 bothclean 沿前稿，不重计。

## 5. 双侧饱和 Ω：交叉锁、真实 middle 与 cut 预算

### 5.1 交叉锁禁形与两个核的真实交集

两边 Ω-only，A_H⊂P、Ω⊂T，B_H⊂Q、Ψ⊂S。证明 A_H∩Ψ=B_H∩Ω=∅。若 a∈A_H∩Ψ，精确 Ψ 供应有 R6(a→b)、b∈B_H。左唯一锁迫 b=ω(a)，右唯一锁迫 a=ψ(b)。于是有实际 B5 从 pair (a,b) 开始，另一个 B5 以同一实际 pair (a,b) 结束；沿该 pair 接成 B8，从而有 B6，矛盾。另一个交集同理。

因此两个核的实际交集为

\[
A_H\cap\Psi=B_H\cap\Omega=\varnothing,\qquad
H_L\cap H_R=D\sqcup A_H\sqcup B_H.
\tag{15}
\]

这是源/终实际供应的结论，不能用形式角色替代。

### 5.2 饱和纤维、全部 extra owners 与完整 middle

现设左右 η=o=α∈{1,2}、β=p∈{1,2}。owner 数 a≥α、d≥β；α=2 时 a=2，α=1 时 a∈{1,2}，右侧同理。左每纤维取最早源 A0、|A0|=α，右每纤维取最晚终点 B0、|B0|=β。令 C=End_R5(H_L)、C'=Src_R5(H_R)。

|C|≥b−α，A0∩C=∅，而 C⊔A0 为 756，故 K_+=C⊔A0 恰满 b、|C|=b−α。加 Q_H 或 A_H 任一点仍为 H_L 内无 R6、B5，所以 Q_H⊂C、A_H∖A0⊂C。完整反序 K_-=C'⊔B0 满 b，P_H=P∩H_R⊂C'、B_H∖B0⊂C'。于是实点不交分解为

\[
C=Z_+\sqcup Q_H\sqcup(A_H\setminus A_0),\qquad
C'=Z_-\sqcup P_H\sqcup(B_H\setminus B_0),
\tag{16}
\]

其中 Z_+=C∩D、Z_-=C'∩D；|Q_H|=b−q−α−a、|P_H|=b−q−β−d，给

\[
|Z_+|=q+\alpha,\qquad |Z_-|=q+\beta.
\tag{17}
\]

D_all=D⊔A_H⊔B_H 是 (15) 的真实交集，人口 b+m，m=q+a+d。其全部红五源包含于 U†，全部端点包含于 V†，其中

\[
\begin{aligned}
U^\dagger&=Z_-\sqcup A_H\sqcup(B_H\setminus B_0),\\
V^\dagger&=Z_+\sqcup B_H\sqcup(A_H\setminus A_0),\qquad
|U^\dagger|=|V^\dagger|=m.
\end{aligned}
\tag{18}
\]

由删除全部源/端点后的换色容量与 König cover，取等为 Src_R5(D_all)=U†、End_R5(D_all)=V†，完整 actual R5 图有 m-perfect matching。m≥0 先由两族的实际大小得到，甚至 q≥−min(α,β)、m≥1。源末层交叠不影响实际删点论证。

不能忽略 extra owners：A_H∖A0、B_H∖B0 已是 middle 合法端口，只有 neutral A0、B0 尚需支付逃逸损失。

### 5.3 所有实际相邻 pair 的严格 cut 预算

记 L=Ω∩I、L'=Ψ∩I、δ=|L|、ε=|L'|、Γ=L∪L'、j=|L∩L'|=|Ω∩Ψ|，有

\[
|I|=q+3+a+d+\delta+\varepsilon,\qquad
|W|=b+3+a,\quad |W'|=b+3+d,\qquad
3+a\le e\le6,\quad3+d\le f\le6.
\tag{19}
\]

Ehat、Fhat 如 §3，x=min Ehat、y=max Fhat。

任取 gap c，B=(I<c)∖(Ehat∪Γ)、A=(I>c)∖(Fhat∪Γ)。K_-∪B 无 B5：Ψ 全缺席，新 I 根无 B5 终点。任何 R6 若终于 B_H，其全部源在缺席的 Ψ，故排除；其他旧 K_- 点不是 T，所以终点在 B。末前驱若在 P_H∪B⊂W 则触发 Ehat，余下只在 Z_- 或 B_H<c。容量给至少 |B| 条 matching；舍 neutral B0<c 至多 |B0<c| 条，B_H∖B0 全已在 U†，不能再扣。再加全部 Ω<c 锁边 A0→Ω，含 Q 锁；A0 与保留普通源不交、锁根与 B 不交。左至少 |B|−|B0<c|+|Ω<c| 条。

右侧完整反序，K_+∪A 全部 R6 源在 A，第二点只在 Z_+ 或 A_H>c。舍 neutral A0>c，extra A_H∖A0 已在 V†，再加全部 Ψ>c 锁边 Ψ→B0，含 P 锁。右至少 |A|−|A0>c|+|Ψ>c| 条。全部中间端口被 perfect 覆盖。

令 g(c)=|(Ehat∖Ψ)<c|+|(Fhat∖Ω)>c|，则 |A|+|B|=|I|−|Γ|−g(c)。三图 actual 交会下界为

\[
\ell\ge3+j-g(c)-|B_0<c|-|A_0>c|+|\Omega<c|+|\Psi>c|.
\tag{20}
\]

任何严格正下界立即给 u<r<c<s<v 的实际蓝四与 middle 红五同端 weak7 矛盾。此式是后续整类定理的中间步骤，不单独冒称新排除。

### 5.4 低根/高根的全部前驱压缩

低根 ordinary 前驱为空。若 ordinary p 是 Ehat<y 的某实际 W 前驱，满 K_+ 加 p 超过 b 且无 B5，迫从 p 开始的 R6。原末帽迫终点≤e_p<y；全部点有 End_R5(X)，尾换 y 违同端 weak7。

故 Ehat<y 的全部 W 前驱均在 A_H。令 r 为这些实际低 owner 前驱数，k=|Ehat<y|，横截给

\[
k\le e+r-3-a.
\tag{21}
\]

若 x<y，则 r≥1，每低 owner 的锁 ω<e_p<y，由末帽、weak7 及 e_p∉Ω 得到。完整反序，高 Fhat>x 的全部 W' 第二点都在 B_H，锁 ψ>f_t；特别 y 的 owner 第二点 b>ψ>y。这里均使用全部 ambient pair 集合。

## 6. 双侧 η=锁点数的 x≤y 全排与双 η1 全排

### 6.1 严格 x<y：含 η1 与 2×2 等号的完整关闭

用 strict cut y，B=(I<y)∖(Ehat∪Γ)、A=(I>y)∖Γ。令 χ=1[y∉Γ]、ρ=|Ehat∩Ψ∩(−∞,y)|、k=|Ehat<y|，根损失为 k+χ−ρ，因为 Fhat 没有 >y 的根。(20) 变为

\[
\ell\ge3+j-\chi-k+\rho-|B_0<y|-|A_0>y|+|\Omega<y|+|\Psi>y|.
\tag{22}
\]

若至少一侧 η1，反向选择使 β=1，此时 d 可为 1 或 2。y 的高 owner 第二点迫唯一 Ψ>y、latest B0>y，所以 |B0<y|=0、|Ψ>y|=1。

若 α=1，a 可为 1 或 2。低 owner 存在迫唯一 Ω<y，且 earliest A0<y，故左 neutral 逃逸为 0、Ωlow=1，得到

\[
\ell\ge5+j-\chi-k+\rho\ge4-k\ge1,
\tag{23}
\]

因为 k≤e+r−3−a≤3。若 α=2，则 a=2、A0=A_H，锁一一对应。令 a_l=|A_H<y|≥r≥1、o_l=|Ω<y|≥r，且 |A0>y|=2−a_l。代 k≤e+r−5 得

\[
\ell\ge6-e-r+a_l+o_l\ge r\ge1.
\tag{24}
\]

因此含 η1 的全部 x<y 关闭，extra owner 无遗漏。

余 α=β=2、a=d=2。高 owner 给 |B0<y|≤1、|Ψ>y|≥1；低 r≥1，A_Hlow≥r、Ωlow≥r。前式给

\[
\ell\ge5-e-r+|A_H<y|+|\Omega<y|+j+\rho\ge r-1\ge0.
\tag{25}
\]

若没有正下界矛盾，必须 e=6、r=1、k=2、χ=1、j=ρ=0，且 A_Hlow=Ωlow=B_Hlow=Ψhigh=1。若 y∉Ehat，因为 χ=1 给 y∉Γ，可以把 y 加入 B；右根仍 >y，全部实际定位保持，neutral 与锁计数不变，左 matching 增 1，矛盾。因此 y∈Ehat，且 y=e3。

完整反序应用同一论证，若尚未矛盾则 f=6、x∈Fhat，且 x=f4，原 Fhat 恰有两点 >x。于是

\[
\widehat E=\{x,e_2,y,e_4,e_5,e_6\},\qquad
\widehat F=\{f_1,f_2,f_3,x,f_5,y\}.
\tag{26}
\]

两个实际红 clique 共享 pair (x,y)，所以 R8(f1,f2,f3,x,y,e4,e5,e6) 的每个连续三元组属于其中之一，产生 R7，矛盾。这关闭 2×2 的整个等号类，不是只列必要条件。

### 6.2 共同根 x=y=z 的全部机制排除

z∈Ehat∩Fhat，故 z∉Γ。紧邻 z 任一侧 gap 的根损失为 1。令 u0=|A0<z|、v0=|B0>z|、o_l=|Ω<z|、p_r=|Ψ>z|。若没有正匹配，(20) 给

\[
u_0+v_0+o_l+p_r+j\le\alpha+\beta-2\le2.
\tag{27}
\]

若 u0=0，由各纤维 earliest 知全部 A_H>z。取 Ehat 根 z 的末 pair (p,z)，p<z 不在 A_H，所以 ordinary 且在 K_+ 外。K_++p 为满 b 加 1、无 B5，迫 R6 源为 p；原帽迫终点≤z，z∈I 不在 core 也不等于 p，故终点<z。五尾全在 C<z，因为 A_H 全 >z。

对任 t∈Z_+<z，完整 middle 中入 t 红五的首点只能在 Z_-⊂D 或 B_H∖B0⊂Q，因为 A_H>z 不能出现；这些首点均不在 S。因此从 t 开始的任意 B4 都能向左延长：joining 红桥会产生从非 S 首点启动的红六。Q_H⊂T 原本可左延。所以对全部 C<z 的首点、middle ambient，Fhat 根 z 的完整 port 帽给入红扇，可以在上述 R6 后直接 append z 成 R7。这里不能统称 D-origin，必须允许 B_H extra∈Q。v0=0 的情况完整反序，用 prepend 排除。

剩下 u0,v0≥1。(27) 只允许 α=β=2、u0=v0=1、o_l=p_r=j=0，所以全部 Ω>z、Ψ<z，且 z∉Γ。

取 Ehat 根 z 的末 pair (p,z)。若 p∈A_H，它的锁 ω>z，末帽 B3(p,z,ω) 与 R6(p→ω) 同端 weak7，矛盾；故 p ordinary。K_++p 迫 R6 源为 p，终点 t<z。同一红六的最后前驱若为 owner a，其锁 ω>z>t，实际末 pair (a,t) 的帽给 B3(a,t,ω)，与 owner R6(a→ω) 同端 weak7，矛盾。所以最后两点 r、t 都在 C<z。

此时 r∈End_R5(H_L)、t∈H_L 且 r<t<z∈Fhat，直接用 §3 的核内相邻对跨反根红扇得 χ(r,t,z)=R，上述实际 R6 append z 成 R7。Ω>z 用于排除上述两处实际末前驱的 owner 身份；红扇本身不需要 Ω>z。共同根的全部机制关闭。

### 6.3 严格根分离 x>y：双 η1 排除与准确剩余

若 α=β=1，在 (y,x) 中任取 gap，没有根损失，(20) 给

\[
\ell\ge3+j-\alpha-\beta=1+j>0.
\tag{28}
\]

所以双 η1 的三个次序全关闭，包含 extra owners 与消 M 后进入的机制。

双侧 η=锁数剩余只可能 x>y 且至少一侧 η2。α+β=3 时，零预算要求 A0 全在 x 右、B0 全在 y 左、Ω>x、Ψ<y、j=0；因为整个 (y,x) 的每个 gap 都适用该预算，earliest/latest 进而给

\[
A_H>x,\qquad B_H<y,\qquad \Omega>x,\qquad\Psi<y,\qquad j=0
\quad(\alpha+\beta=3\text{ 的未排零预算类}).
\tag{29}
\]

这些是实际必要条件，不算排除。α=β=2 不冒称同样强式；严格 x>y 尚未统一关闭。

## 7. 严格完整 F 的同块换代表排除定理

### 7.1 全部 F 背景与唯一两 provider 残余

本节 p 为独立局部路径参数，p≥3。严格继承 endpoint 稿 §7：禁 B_(p+1)、R_(p+2) 与同实际端点 R_(p+1)+B3；F 保留全部红 R_(p+1) 和蓝 Bp。红横截数 p，全部 minimum bases 恰为 p 个各至少 2 点红块 G_i 的 rank1 product，每个 basis 是实际 Bp；G 是全部 bases 的并，每个红 (p+1) 的 trace 含某整块。

A 为 p 点块，S=D⊔{s}、D<A。该 s 位置全部 private 红恰为 A+v，V 恰为全部 G 外 provider。旧位置引理给 V<d*=max D，V∪{d*} 全部为 ambient R_(p+1) 源；旧交错 DVD 蓝、VDD/VDV 红。旧区间占用完整分划定理沿 endpoint §7，不冒称重证。

专取 V={v,w}、v<w。旧定理只剩

\[
D=E\sqcup\{d,d^*\},\quad |E|=p-3,\quad
E<v<w<d<d^*<A,\qquad B_p(E\cup\{v,w,d\}).
\tag{30}
\]

令 B_d 为含 d 的整个 rank1 block，保留全部实际点。**同块换代表定理：**若 B_d 不包含于 (w,d*)，则要么已直接违反禁 B_(p+1)，要么可合法换同块代表后构造满足全部 F 的 K⊔Y。

### 7.2 换代表后完整 private 族保持的证明

坏蓝 p 终于 d，joining 迫 d 不能是 ambient R_(p+1) 源，否则桥两色分别给 B_(p+1)、R_(p+2)。因此 A+d 非红。

对任 z∈B_d∖{d}，

\[
S_{\rm new}=(D\setminus\{d\})\cup\{z,s\}
\tag{31}
\]

仍为 minimum product basis。A 位置的 private 族仍恰为 A+v、A+w：新 private 的 trace 必含整块，避开其他代表迫完整块只能是 A，所以红成员为 A+t。若 t∈G，新出现的唯一可能是被移走的 d，但 A+d 非红；旧两个 G 外 provider 继续 private，其他 G 外点不新增。不能只凭换 basis 就声称 private 保持。

### 7.3 排除越过 A 的同块点与构造完整分划

若任 z∈B_d 有 z>a1=min A，E+d*+a1+z 是实际全蓝 product basis。R_(p+1)(d*,A) 不能前接 w，所以 χ(w,d*,a1)=B。packet(w,d*,a1,z) 首末 B 迫全 B。

对每 e∈E，旧 DVD 给 χ(e,w,d*)=B；packet(e,w,d*,a1)、packet(e,w,a1,z) 依次补出全部涉及 e,w,a1,z 的蓝色。两个 E 点加 w 的三元组继承原坏 Bp，其他三元组位于 product basis。于是 E+w+d*+a1+z 是实际 B_(p+1)，矛盾。因此整个 B_d<A。

若有 z∈B_d 不在 (w,d*)，现在只可能 z<w 或 d*<z<a1，不能等于 G 外 provider 或 d*。z<v 时，两个 provider 同处新 D 的最后 gap；v<z<w 时，分处两个 gap，旧完整 F 区间定理均适用。若 d*<z<a1，两个 provider 的右继为保留的旧 d*，而 d* 是实际红 (p+1) 源，旧右继源定理适用。因此

\[
Y=(D\setminus\{d\})\cup\{z,v,w\},\qquad K=X\setminus Y
\tag{32}
\]

满足全部红、蓝 F，没有删除非 private 成员。

### 7.4 精确残余与不能采用的换基

尚未关闭的精确残余必须满足

\[
B_d\subseteq(w,d^*),\qquad
B_p(E\cup\{v,w,z\})\text{ 对每个 }z\in B_d\text{ 都实际成立}.
\tag{33}
\]

任一个失败，同块换代表即可完成分划。不能声称全部双 provider 已闭。

移走 d* 的另一块换基会漏掉已实际为红的成员 A+d*；坏蓝 T 含 G 外 provider，也不意味 T 是 minimum transversal。下一竞争突破须改变 Y∩A，同时控制全部被移走代表对应的红成员，不能只删减 private 约束。

## 8. 覆盖、策略边界与参数后数字

本轮新增工作结论为：消 M 的真实归约（不单独认领数值 saving）；oneΩ+clean 全排；双 η=锁数且 x≤y 全排；双 η1 三个根次序全排；严格完整 F 的上述同块换代表新类分划。旧 onefull、bothclean 沿用，不重复计覆盖或 saving。

若 n=3b+3 仍有反例，换核后两方向 Ω 都非空，至少一向 η2，并满足下述穷尽分类。

这是穷尽分类推论：消 M 后 Ω 非空只允许 (4) 的四种三元组；旧 onefull/bothclean 与新 oneΩ+clean 排除迫两向 Ω 非空；双 η1 全排迫至少一向 η2。若没有 (2,1,1)，两向必有 η=o，再由 x≤y 全排，只能严格 x>y。因此下列两种结构剩余是穷尽目录，不是仅列研究例子。

| 机制 | 尚未关闭的范围 |
|---|---|
| 至少一向 (η,o,a)=(2,1,1) | 可与任意另一 Ω 类型组合，尚未整类关闭 |
| 两向 η=o，至少一向 η2 | 只剩严格 x>y；α+β=3 的极端真实必要条件见 (29)，不算排除；2×2 不套该强式 |

另外两条全局竞争入口——合法 rootcycle 的 positive-through、任意 critical 进入完整 F——仍未证明；它们不是上述两类之外的新参数分支。

不声称这些剩余子类已有真实实例。

局部最优审计要求停止把逐个必要条件、仅选有利供应、修补小核 756 当大核可加点 766、排 Q0 终点当排末前驱，以及移走 d* 却忽略完整红成员当作推进。新推进价值来自完整实际 pair/König、neutral 纤维与补回全部锁，而不是有限 q 分类。

下一优先级是严格根分离中同一实际 middle 端点的兼容定理，先保留全源/全末供应，不能把普通 P/Q 见证直接称为新根；以及非 tight η2/o1 的整条核外 R6 尾与完整 port 的共同约束，不能从局部核直接推出降低 η。完整 F 改变与 A 的交集继续作为竞争路线。尚未兑现的条件不给数值 saving。

参数工作式仍为

\[
|X|+w\le3b+3,\qquad N_{\rm sig}(7,6,7)\le3b+3,\qquad
N_{\rm sig}(7,7,7)=N_{\rm sig}(7,6,7)+1\le3b+4.
\tag{34}
\]

只在最后代入既有用户授权工作输入 b=25：

\[
N_{\rm sig}(7,6,7)\le78,\qquad N_{\rm sig}(7,7,7)\le79.
\tag{35}
\]

全局 77/78 未证明。本轮额外无条件数值 saving 为 0，b=25 证书未重验证，未读取新证书，旧 accepted 层级不改。上述结构类排除不重复加到全局数值。

## 9. 保证、回执与不变状态

全部新增 unreviewed/unaccepted。同会话生成与交叉核查不构成独立数学 review。指定 native Sol/high 只负责忠实文档执行，不核实未报告的 backend 或实际 effort。PASS_DOCUMENT_ONLY 只说明文档一致性，不认证数学、不升级接受或 assurance。

回执为 `tmp/n7_lock_fiber_double_omega_20261102/DOCUMENT_CHECK.json`，检查限严格 UTF-8、公式 tag 连续唯一、本地链接可读、参数代入字符串与手工算术一致、六个保护文件当前 SHA256、task status/completedAt 及指定两新路径。

未调用外部 Claude、未向外传材料，未执行科研代码、枚举、SAT、solver 或 proof 检查。所有旧稿、task.json、metadata、接受/assurance、绑定、runtime、运行及指针保持；task 仍 in_progress、completedAt=null，不 commit、不 archive。主会话已全文通读并落实指定精度修正；这不构成独立数学审阅，长期任务未完成。
