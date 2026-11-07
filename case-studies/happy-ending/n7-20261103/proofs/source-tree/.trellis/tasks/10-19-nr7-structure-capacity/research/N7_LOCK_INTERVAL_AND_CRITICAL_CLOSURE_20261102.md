# N7：锁区间禁形、完整尾部不相容与临界层全排

日期：2026-11-02。状态：**工作证明；全部新增 unreviewed/unaccepted，未独立审阅、未接受**。本文忠实整理主会话批准的数学内容。主会话及三名数学协作者的推导与交叉核对属于同会话生成核对，不构成独立数学 review。指定 native gpt-6.1-sol/high 文档执行者只转写及检查文档一致性，不自主研究、补证或认定接受；未报告的 backend、实际 effort 不声称已核实。

本轮给实际根瓶颈、锁区间角色排除与满核尾部不相容三个工具，完整排除非 tight Ω 类型及最后双饱和严格根分离类。全部临界入口逐项覆盖后，得到全模型参数工作上界下降一；具体数值只在参数定理证明之后代入。竞争路线仍明确分列，不作为本轮临界排空的附加前提。

唯一新增文件为本文及 `tmp/n7_lock_interval_critical_closure_20261102/DOCUMENT_CHECK.json`。所有旧稿、task.json、metadata、接受/assurance、绑定、runtime、运行及指针保持，不提交、不归档。未调用外部 Claude、未向外传材料，未运行项目脚本、科研代码、枚举、SAT、solver 或 proof 重放；PowerShell 仅用于文档操作与检查。

## 1. 模型、全部实际角色与旧依赖

完整有序 rank-3 signotope 的四点 packet 按 abc、abd、acd、bcd 至多换色一次。路径按实际顶点计长，连续三元组同色决定实际路径，并对子序列遗传。767 禁 R7、B6、weak7；756 禁 R6、B5、weak7，其换色模型禁 R5、B6、weak7。weak7 比较同一对实际首末点的反色路径，长度和至少 9，内部允许共享。b 是两种 756 模型共用的整数有效人口容量上界，不要求达到实例；N_sig 表示最大允许人口，不是 forcing 阈值。

研究 n=3b+3 临界层。旧全模型式 |X|+w≤3b+3 给 w=0；此旧依赖的保证层级不提升。全部 ambient 角色为

\[
S=\operatorname{Src}_{R6}(X),\quad T=\operatorname{End}_{R6}(X),\quad
I=S\cap T,\quad P=S\setminus T,\quad Q=T\setminus S,\quad
D=X\setminus(S\cup T),\quad
U=\operatorname{Src}_{R5}(D),\quad V=\operatorname{End}_{R5}(D),\quad w=|U\cap V|.
\tag{1}
\]

ambient 指母体 X。注明域中的 Src、End 均保留全部实际供应；端点图与相邻 pair 图也保留全部实际路径。匹配仅要求相应层端点不同，允许路径内部共享。角色层若在实际点上交叠，König cover 删除对应实际点至多为 cover 大小，仍击中全部路径。

主要依赖使用绝对本地链接，并保持旧保证边界：

- [锁纤维归一化与双 Ω 稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCK_FIBER_NORMALIZATION_AND_DOUBLE_OMEGA_EXCLUSION_20261102.md>) §1—3 给模型、无损消 M 换核、四种 Ω 类型、完整 port、全部 ambient 相邻根、actual 锁 pair 与头尾替换；§4 为 oneΩ+clean 全排，§5 给真实交集和全部 middle 供应，§6 给双饱和 x≤y 全排及双 η1 全排。
- [endpoint 统一排除稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_ENDPOINT_PAIR_HALL_MISALIGNMENT_EXCLUSION_20261102.md>) §5 全部 onefull，§6 全部 bothclean；一般实际端点对 Hall 与严格完整 F 背景亦沿用。
- [Hall 归一化稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_HALL_DEFECT_ROOT_AUGMENTATION_AND_ZERO_THROUGH_CLOSURE_20261101.md>) §5 提供 η≤2 canonical 入口与完整接口。
- [锁端口吸收稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCKED_PORT_ABSORPTION_AND_COMPLETE_REPARTITION_20261101.md>)：最早/最晚 owner、实际锁供应与完整端口。
- [weighted 稳定性稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7879_INTERFACE_AUDIT_AND_WEIGHTED_THROUGH_STABILITY_20261031.md>)：完整 port、实际头尾替换及原全模型加权工作式。
- [原参数工作界稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_DEFECT_ONE_PREDECESSOR_COMPRESSION_AND_GLOBAL_BOUND_20261031.md>)：旧临界入口与保证边界。
- [R20 精确关系稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>)：合法 chart 删根及实际反向添点给精确 +1。
- [纯核与完整 private 稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_PURE_CORE_ROOT_SEPARATION_AND_INTERLEAVED_REPARTITION_20261030.md>)：严格完整 F 与全部 minimum bases 的竞争背景。

上一稿真实消 M 换核可分别施于两方向，保持 X、ambient 角色及 W，η 不增，归约到 M0。Ω-only 的核记 H_L、H_R，左 owner 为 A_H⊂P、锁集 Ω⊂T，右 owner 为 B_H⊂Q、锁集 Ψ⊂S。Ω 非空时只有

\[
(\eta,o,a)\in\{(1,1,1),(1,1,2),(2,1,1),(2,2,2)\}.
\tag{2}
\]

W=S∖(Ω∩S)、W'=T∖(Ψ∩T) 保持完整 port。Ehat 收集 e∈W∩T，使某 ambient R6 末 pair 为 (s,e)、s∈W；Fhat 收集 f∈W'∩S，使某 ambient R6 首 pair 为 (f,t)、t∈W'。它们保留全部实际相邻对，不只内部或选定见证。ordinary 身份、完整头尾替换与加入 actual 锁 pair 均沿上一稿 §3—5。

## 2. 实际根瓶颈

令 x=min Ehat、y=max Fhat。若某实际 R6 首 pair 为 (s,a)、a∈A_H⊂S，且 s>x，Ehat 根 x 的加强右红扇给 χ(x,s,a)=R，而该实际首 pair 的 R7 左帽给 B，矛盾。因此全部此类 pair 只能 s≤x。

完整对偶，实际 R6 末 pair (b,r)、b∈B_H⊂T 若 r<y，则 Fhat 根 y 的加强左红扇给 χ(b,r,y)=R，原末帽给 B，矛盾。因此

\[
\text{actual 首 pair }(s,a),\ a\in A_H\Longrightarrow s\le x;\qquad
\text{actual 末 pair }(b,r),\ b\in B_H\Longrightarrow r\ge y.
\tag{3}
\]

紧邻 x 左侧 cut 中，owner 首 pair 逃逸最多占根 x 的一条 matching 边；紧邻 y 右侧 cut 中，owner 末 pair 逃逸最多占根 y 的一条边。若该根因 Γ、Ehat 或 Fhat 被删，损失为 0。若右根全部 >y≥x，右 A_H escape 全为 0。

这是全部实际 pair 的定位，不是挑一个有利 matching。每个正交会链保留实际末 pair (u,r)、middle R5(u→v)、实际首 pair (s,v)，次序 u<r<cut<s<v。两条 R6 的帽给 B4(u,r,s,v)，与同一实际端点 u、v 的 middle 红五违反 weak7。

## 3. 锁区间角色排除定理

一般左 owner a 有实际 R6(a→ω) 和 B5(a,ω,z1,z2,z3)。任 a<t<ω，若 χ(a,t,ω)=B，就与该红六同端 weak7，故为 R。packet(a,t,ω,z1) 的第一项 R、第三项 χ(a,ω,z1)=B，至多一次换色迫第四项 χ(t,ω,z1)=B。因此有实际 B5(t,ω,z1,z2,z3)。

全局 T∩Src_B5(X)=∅：入 R6 与出 B5 joining，红桥给 R7，蓝桥给 B6。所以

\[
(a,\omega(a))\cap T=\varnothing,\qquad
(\psi(b),b)\cap S=\varnothing\quad\text{（完整对偶）}.
\tag{4}
\]

这排除全部锁区间穿过反向角色的配置，不要求中间点额外角色。特别地，若 Ω>x、x∈T，且 A_H⊂P 不含 x，则全部 A_H>x；对偶 Ψ<y、y∈S 迫 B_H<y。本轮最后证明只需前向结论，不用对偶位置必要条件。

## 4. 满核尾部与实际首对不相容定理

母体为 767。设 K=C⊔A0 是满 b 的 756，A0>x、x∉K；p<x、p∉K，有实际 R6 末 pair (p,x)。K+p 无 B5，且其中每条 R6 都只能从 p 开始。另有实际 R6 首 pair (x,a*)，a*∈S；这里不把 x 称为 Fhat。

再假定每个 r∈C<x，或者 r∈T，或者有一条首点不在 S 的实际入 R5。则整个配置不可能。

证明：容量在 K+p 的 b+1 点迫 R6，源为 p。原末帽及 weak7 迫其终点 t≤x；x 在域外，所以 t<x，五尾都在 C<x。记末两点 r<t。

若 r∈T，入 R6 与任意从 r 开始的 B4 joining，红桥给 R7，故蓝桥能向左延为 B5。若有非 S-source 的入 R5，红桥会产生从非 S 首点启动的 R6，同样不可能，所以任意这样的 B4 也能向左延。

实际首 pair (x,a*) 的帽给 χ(t,x,a*)=B。若 χ(r,t,x)=B，就有 B4(r,t,x,a*)，左延为终于 a*∈S 的 B5。全局 End_B5(X)∩S=∅：入 B5 与出 R6 joining 的两色分别给 B6、R7。因此矛盾。故 χ(r,t,x)=R，可以 append x 到原 R6，产生 R7。

该参数定理的全部假设在 §7 实际兑现，不能只作为额外条件留下。

## 5. 至少一侧 (η,o,a)=(2,1,1) 的全部机制排除

### 5.1 全部角色、低前驱预算与非负 middle 规模

左 α=2、o=a=1，Ω={ω}、A_H={a}=A0。右 (β,p,d) 可为任一允许 Ω 类型：p 为 Ψ 锁数，d 为 B_H owner 数，B0 为每条纤维的 latest 点，|B0|=p。令 L=Ω∩I、J=Ψ∩I、Γ=L∪J、δ=|L|、ε=|J|、ρ=|L∩J|，|D|=b+q，则

\[
i=|I|=q+5+\beta-p+d+\delta+\varepsilon,\qquad
|Q_H|=b-q-3,\quad |P_H|=b-q-\beta-d,\qquad
h_L=5,\quad h_R=3+\beta-p+d.
\tag{5}
\]

令 C=End_R5(H_L)、C'=Src_R5(H_R)、Z_+=C∩D、Z_-=C'∩D，大小 c、c'。最早/最晚 owner 引理给 a∉C、B0∩C'=∅。K0=C⊔{a} 为实际 756，|C|≥b−2，因此

\[
|K_0|=b-\kappa_0,\quad \kappa_0\in\{0,1\},\qquad
5\le e=|\widehat E|\le6,\quad h_R\le f=|\widehat F|\le6.
\tag{6}
\]

收集全部 Ehat<y 的实际末 pair 在 W 内的前驱，ordinary R、owner R_A，大小 r、r_A。若前驱在 T，Fhat 根 y 的加强扇与末帽冲突，所以均在 P。ordinary R 在 H_L 外，实际末前驱身份给 End_R5(X)，再由 M0 给无 ambient B5 源。

若 r>κ0，K0 加 κ0+1 个这样的点超过 b 且无 B5：C、a 全部 B5 第二点锁在域外 Ω，新 ordinary 点无 B5 源。迫 R6 源为某 p0∈R；帽迫终点≤e_p0<y，全点有 End_R5(X)，尾换 y 后同端 weak7，矛盾。所以 r≤κ0≤1、r_A≤1。

R∪R_A∪(Ehat≥y) 横截 W 内全部 R6，配合并集下界得到

\[
k:=|\widehat E<y|\le e+r+r_A-5,\qquad
k\ge e+f-i-1,\qquad
q\ge2-\delta-\varepsilon-r-r_A,\quad m:=q+1+p\ge0.
\tag{7}
\]

最后一步用 r+r_A≤2、δ+ε≤1+p。x=y 时 Ehat、Fhat 至多共一点另给 m≥2，x>y 时两族不交另给 m≥3。这里不预设 q≥0。

### 5.2 真实 middle、全部扩域 pair 与 root escape

上一稿交叉锁禁形给真实 D0=D⊔{a}⊔B0⊂H_L∩H_R，人口 b+m。全部 R5 源包含于 Z_-⊔{a}，全部末点包含于 Z_+⊔B0。König 删实际点及换色 756 容量迫至少 m 条 matching；固定 m 条 actual middle，源/末像 J_U、J_V。角色层交叠时删除只更少。

完整容器大小 c'+1、c+p，所以 middle 外端口数为

\[
c'-q-p\ge0,\qquad c-q-1\ge0.
\tag{8}
\]

不能把所选供应预设为 middle，也不假定 c、c' 取等。原小核 L_-=C'∪P_H∪B_H、L_+=C∪Q_H∪{a} 都是实际 756，缺额

\[
\kappa_-=q+\beta-c'\ge0,\qquad \kappa_+=q+2-c\ge0.
\tag{9}
\]

无 B5 来自全部核端点/owner 的锁目标在域外，以及 P_H、Q_H 的全局蓝禁形；无 R6 因为各在原 H_R、H_L 内。

取紧邻 y 右 gap，B=(I≤y)∖(Ehat∪Γ)、A=(I>y)∖Γ，Fhat 无 >y 根。左扩域 R6 全部末 pair 只能 Z_-→B 或 B_H→B：终于 B_H 的 R6 必须从 Ψ 启动，但 Ψ 全缺席，其他旧点非 T；P_H、B 若为末前驱均在 W，会触发 Ehat。右扩域全部首 pair 只能 A→Z_+ 或 A→a：原 owner 起点只能终于缺席的 Ω，其他旧点非 S；Q_H、A 为第二点均在 W'，会触发 Fhat。两域无 B5，根集避 Γ，全部锁仍在域外。

§2 的实际 root 瓶颈给左 B_H pair 逃逸只能占 root y，损失 ε_L≤1[y∈B]；若 y∈Ehat 或 Γ 就是 0。x≤y 时，右 pair(s,a) 必有 x<s<a，Ehat 根 x 的扇与首帽冲突，所以 ε_R=0；x>y 时 ε_R≤1，因为只有一个 owner。

先舍普通 B_H、a 逃逸，再加入全部 Ω≤y actual 锁边 a→ω（含 ω∈Q）、全部 Ψ>y actual 锁边 ψ→b_ψ（含 ψ∈P）。普通 Z_-、Z_+ 与 A0、B0 锁端口不交，锁根与 B、A 不交。再舍 (8) 的真实 middle 外端口，左右分别保留至少

\[
|B|-\beta+p-\varepsilon_L+o_{\le y},\qquad
|A|-2+1-\varepsilon_R+p_{>y}
\tag{10}
\]

条。沿 m 条 middle 交会下界为

\[
\ell\ge |A|+|B|-q-2-\beta-\varepsilon_L-\varepsilon_R+o_{\le y}+p_{>y}.
\tag{11}
\]

全部数量来自全 pair graph 的容量，不是仅存在某条好路径。

### 5.3 x>y 与 x=y

x>y 时，Ehat≤y 为空，|A|+|B|=q+5+β−p+d+ρ，且 ε_L、ε_R≤1，故

\[
\ell\ge1+(d-p)+\rho+o_{\le y}+p_{>y}\ge1.
\tag{12}
\]

x=y 时，y∈Ehat∩Fhat，故 y∉Γ；|A|+|B|=q+4+β−p+d+ρ，ε_L=ε_R=0，所以

\[
\ell\ge2+(d-p)+\rho+o_{\le y}+p_{>y}\ge2.
\tag{13}
\]

两者均得正交会矛盾。

### 5.4 x<y：只修补 ordinary R

只把 ordinary 低前驱 R 加到右核，L_+^R=L_+∪R，不引入 Q0。C、a 的 B5 第二点在缺席的 Ω，Q_H⊂T 无 B5 源，新 R 无 B5 源，所以无 B5。若有 R6，H_L-origin 源 a 只能终于缺席的 Ω；源 p0∈R 时，原末帽迫终点≤e_p0<y，全点 End_R5(X) 尾换 y 给 weak7。所以 L_+^R 是实际 756，缺额 κ_+^R=q+2−r−c≥0。

扩域 L_+^R∪A 中，R-origin 源的帽迫终点<y，新 A>y 不参与，故全在旧核，矛盾；R<y 也不能作 A 的第二点。右 A_H escape 仍为 0，左 ε_L≤1[y∈B]，故 (11) 多出 +r。

设 r_y=1[y∈Ehat]、j_E=|Ehat∩Ψ∩(−∞,y]|，则

\[
|A|+|B|=q+5+\beta-p+d+\rho-k-r_y+j_E,\qquad
r_y+\varepsilon_L\le1.
\tag{14}
\]

代 k≤e+r+r_A−5、e≤6，得到

\[
\ell\ge1+(d-p)-r_A+\rho+j_E+o_{\le y}+p_{>y}.
\tag{15}
\]

若 r_A=1，唯一 owner a 有实际末 pair(a,e_a)、e_a<y，又有 R6(a→ω)。末帽和同端 weak7 迫 ω≤e_a，而 e_a∈W、Ω∩W=∅ 排等号，故 ω<e_a<y，o_≤y=1≥r_A；r_A=0 时直接。因此 ℓ≥1。

每个正交会保留 actual 末 pair(u,r0)、middle R5(u→v)、首 pair(s0,v)，r0≤y<s0；两条 R6 的帽给 B4(u,r0,s0,v)，与 middle 同端 weak7。m=0 时正交集下界已经与空 matching 冲突，不冒造路径。

至少一侧 (2,1,1) 的全部机制至此排除，包含任一另一 Ω 类型、extra owners、q 负、四/五/六根、Ω 的 I 交重叠或为空。没有用“小核 756 可加点所以大核 766 可加点”，也没有把 Q0 不能作终点当作不能作末前驱。

## 6. 双侧饱和 strict x>y：含 η1 的全部机制排除

入口为 η=o=α、β=p 均在 {1,2}。上一稿 §5 已完整给 owner A_H、B_H，大小 a、d；每纤维 earliest A0、|A0|=α，latest B0、|B0|=β，以及

\[
\begin{aligned}
C&=Z_+\sqcup Q_H\sqcup(A_H\setminus A_0),\quad
C'=Z_-\sqcup P_H\sqcup(B_H\setminus B_0),\\
K_+&=C\sqcup A_0,\quad K_-=C'\sqcup B_0,\qquad |K_+|=|K_-|=b.
\end{aligned}
\tag{16}
\]

D_all=D⊔A_H⊔B_H 有完整 actual R5 源族、末族

\[
U^\dagger=Z_-\sqcup A_H\sqcup(B_H\setminus B_0),\quad
V^\dagger=Z_+\sqcup B_H\sqcup(A_H\setminus A_0),\quad
|U^\dagger|=|V^\dagger|=m=q+a+d,
\tag{17}
\]

及 full m-perfect；|Z_+|=q+α、|Z_-|=q+β。I 去 Γ 人口为 m+3+ρ，ρ=|Ω∩Ψ|。

本节重新定义 root 域，不沿用 §5 紧邻 y 右 gap 的 A、B。令 Γ=(Ω∩I)∪(Ψ∩I)、ρ=|Ω∩Ψ|；对 y<c<x 的 ambient gap，取 B=(I<c)∖(Ehat∪Γ)、A=(I>c)∖(Fhat∪Γ)，实际扩域为 K_-∪B、K_+∪A。

两扩域各无 B5，因为 Ψ、Ω 锁点分别全部缺席；全部 R6 分别具有末 pair Z_-/B_H→B、首 pair A→Z_+/A_H。由满核的实际容量/König 论证，两图各有饱和全部 roots 的 matching。x>y 使 Ehat 不在 cut 左、Fhat 不在 cut 右，所以 A⊔B=I∖Γ，且 |A|+|B|−m=3+ρ。middle 外只剩 neutral B0、A0；extra owners 已在 middle，不能重复扣。

取全 ambient 点序中紧邻 x 左 gap c，右根 A≥x。§2 实际 root 瓶颈使右 A_H escape 仅能占 root x，舍 neutral target 的损失 ε_R≤1[x∈A]；左 neutral 损失 ε_L≤β。加全部低 Ω、高 Ψ 实际锁 pair 后

\[
\ell\ge3+\rho-\varepsilon_L-\varepsilon_R+|\Omega<c|+|\Psi>c|.
\tag{18}
\]

若至少一向 η1，反序定向使 β=1，x>y 在反序仍保持，故 ℓ≥3−1−1=1，整类关闭，含单锁侧 extra owners。不依赖上一稿的极端位置必要式作新假设，也不要求某供应端点先落在一条预选红五上。只余 α=β=2，即双侧 (2,2,2)。

## 7. 最后双 (2,2,2) 严格根分离的单端闭合

本节 α=β=o=p=a=d=2，A0=A_H、B0=B_H；C=Z_+⊔Q_H、C'=Z_-⊔P_H，K_+=C⊔A_H、K_-=C'⊔B_H 满 b。完整 D_all 红五源族 U†=Z_-⊔A_H、末族 V†=Z_+⊔B_H，各 m=q+4，full perfect。A、B、Γ 及两个实际扩域继承 §6 的重新定义。证明只用近 x 左一个 cut，不先推 Ψ<y、B_H<y，也不依赖两个紧割不相容。

### 7.1 单 cut 的零预算迫真实首 pair 与 Ω>x

取紧邻 x 左 ambient gap c。x>y 给无 Ehat/Fhat 根损失，|A|+|B|−m=3+ρ。左 owner 逃逸 ε_L≤2，右 ε_R≤1 且只能为 actual 首 pair(x,a*)。加入全部低 Ω、高 Ψ 锁边后仍是 (18)。若没有正交会矛盾，必须

\[
\varepsilon_L=2,\quad\varepsilon_R=1,\quad\rho=0,\quad
|\Omega<c|=0,\quad|\Psi>c|=0.
\tag{19}
\]

只取所需结论：右 escape 为 1 迫存在真实 R6 首 pair(x,a*)，a*∈A_H。c 是全 X 中 x 紧左 gap，所以 Ω<x 为空；x∈Ehat⊂W 排 Ω=x，故 Ω>x。这里不把 x 称为 Fhat；a*∈P，不是 T。

### 7.2 从锁区间推出全部 A_H>x

每个 a∈A_H 锁 ω(a)>x，而 x∈I⊂T。若 a<x，x 落入被 §3 排除的 (a,ω(a))∩T；a=x 又由 A_H⊂P 排除。因此

\[
A_H>x.
\tag{20}
\]

owner 次序由完整路径性质实际证明，没有预设。后续不需要 B_H 的位置。

### 7.3 每个低 C 点的全部 B4 均实际可左延

任 r∈C<x，分为 Q_H 与 Z_+。若 r∈Q_H⊂T，ambient 入 R6 与任意从 r 开始的 B4 joining，红桥给 R7，所以蓝桥可左延为 B5。

若 r∈Z_+<x，完整 middle 末点覆盖给一条实际入 r 红五，源只能 Z_-⊂D 或 A_H；A_H>x>r 不可能作源，故源在 Z_-，不在 ambient S。它与任意从 r 开始的 B4 joining，红桥会造从非 S 点启动的 R6，矛盾，因此同样可左延为 B5。

路径内部可以含 B_H，无须全在 D；只用实际 source 身份。该论证作用于每个 r 及其全部 B4，不是只选有利供应。

### 7.4 满核加真实末前驱，强迫完整低尾

取 Ehat 根 x 的一条 ambient R6 末 pair(p0,x)，p0∈W、p0<x。A_H>x 使 p0 非 owner；H_L∩S=A_H、W⊂S 给 p0∉H_L，真是 K_+ 外一点。末前驱有 ambient End_R5 身份，M0 给它无 ambient B5 源。

K_++p0 无 B5 必须同时检查三项：C 的任何 ambient B5 第二点均在 Ω，A_H 的任何 B5 第二点也在 Ω（完整锁）；Ω 不在 K_+、也不含 p0（p0∈W）；p0 自身无 B5 源。不能仅引用最后一项。

K_++p0 有 b+1 点，weak7 遗传，756 容量迫 R6。若源在 H_L，只能为 A_H，但全部 A_H-origin R6 终点在域外 Ω，所以实际 source 只能 p0。原末 pair(p0,x) 帽及同端 weak7 迫新终点 t≤x。x∈I，而 H_L∩S=A_H⊂P，所以 x∉K_++p0，故

\[
t<x,\qquad\text{该 R6 的全部五尾都在 }C<x,
\tag{21}
\]

因为全部 A_H>x。

### 7.5 兑现一般尾部定理，append x 成 R7

记末两点 r<t<x。7.1 的 actual 首 pair(x,a*) 给 χ(t,x,a*)=B，否则 prepend t 到对应 R6 得 R7。若 χ(r,t,x)=B，就有 actual B4(r,t,x,a*)，7.3 将其左延为终于 a*∈S 的 B5，与全局 End_B5∩S=∅ 矛盾。因此该三元组为 R，append x 到 7.4 的强制红六，产生实际 R7。

这是 §4 一般满核尾部不相容定理全部假设的实际兑现。最后整类关闭。不使用 owner-private 端点假设，不要求任一 middle 边可扩 perfect，不拼复制链，不假称 x∈Fhat；甚至只需中间完整端点覆盖，不需指定一条预选 u→v 红五。

## 8. 全部临界入口覆盖审计与参数上界

取任 767 母体 X，在 n=3b+3 层由旧全模型式得 w=0。旧 canonical 归一化给 η_L、η_R≤2；上一稿 §2 的实际消 M 分别作用两侧，保持 X、ambient 角色及 W，η 不增，得到 M0。

消 M 后若 η_new=0，则原 M 必空：M 非空时 t=|h(M)|≥1，且 η_new≥o+t≥1。因此 η_new=0 只来自原 η=0 的 fullstandard，没有把任意新满 766 冒作 fullstandard。Ω_new=Ω⊔h(M) 为空也迫原 Ω、M 均空，换核未改变原 clean 入口。

全部入口与封闭证据如下，没有遗漏分支：

| 临界入口 | 完整封闭证据 |
|---|---|
| 任一 η=0 | endpoint 稿 §5 全部 onefull |
| 两 η 正、双 Ω 空 | endpoint 稿 §6 全部 bothclean |
| 恰一方向 Ω 非空 | 上一稿 §4 oneΩ+clean 全排 |
| 两 Ω 非空，至少一侧 (2,1,1) | 本稿 §5 三个根次序全排，另一侧四类型、q 负与新增根等号均覆盖 |
| 否则两侧 η=锁数，x≤y | 上一稿 §6 完整排除，共同根和 2×2 等号均含在内 |
| 两侧饱和 x>y，任一 η1 | 本稿 §6 实际 root 瓶颈 |
| 两侧饱和 x>y，双 η2 | 本稿 §7 单端锁区间及满核低尾不相容 |

四种 Ω 类型由 (2) 穷尽，所以全部 n=3b+3 的临界配置排空。得到工作定理：在既有完整模型、b 共用 756 有效容量与已列依赖下，

\[
N_{\rm sig}(7,6,7)\le3b+2.
\tag{22}
\]

更大人口可取 3b+3 点诱导子配置，767 禁形遗传；在该子配置中重新计算 ambient S、T、D、w，再用旧加权式取得其 w=0，不假设原 w 遗传。因此这是全模型上界，不是子类条件界。沿 R20 合法 chart 已证精确 +1，

\[
N_{\rm sig}(7,7,7)=N_{\rm sig}(7,6,7)+1\le3b+3.
\tag{23}
\]

§4 的额外假设已在 §7 全部兑现，没有把未闭竞争入口当作主证明前提。所有新工作仍 unreviewed/unaccepted，旧依赖保证不升级。

本轮仅加强无条件人口上界；旧加权式 |X|+w≤3b+3 保持原值，只作为临界层 w=0 的入口。本轮未证明新的 |X|+w≤3b+2。

最后、仅最后代入既有用户授权工作输入 b=25：

\[
N_{\rm sig}(7,6,7)\le77,\qquad N_{\rm sig}(7,7,7)\le78,
\qquad 3\cdot25+2=77,\quad3\cdot25+3=78.
\tag{24}
\]

原工作 78/79 在新的工作证明层各降 1。本轮下降来自新结构，不是新求解输入，不重计旧 b=25 收益；未读取或重验证 b=25 证书，不改旧 accepted 层级。

## 9. 竞争路线与本轮方法审计

严格完整 F 的同块换代表旧定理保留，本轮联合换块没有新整类排除。改变 Y∩A 需要漏另一块，否则 Y 含全蓝 product basis；若漏含 d* 的 B*，E+{d,a1,v}、E+{d,a1,w} 等含 G 外点的 p-set 不是 minimum 横截，完整 F 中存在真实 B* private blocker，不能省略整族。

这里 B* private blocker 是相对于 product basis S0=E∪{d,d*,a1}，即 A 的代表改为 a1：其余 represented blocks 被所测试的 p-set 击中，只剩 B*，故该 blocker 与 S0 只交 d*。不声称它相对旧 A 代表 s 也必是 private。

该开放构造不再是本轮参数上界前提。rootcycle 全局 positive-through 仍未证明，但不需要它完成本轮临界排空。

本轮方法的实质是把按 owner 人数扣 loss 升级为按实际 root 占用上限；把预选某条 middle R5 的拼接问题换成已兑现的全端点覆盖，再由单个核低尾追加 R7。只用一个端 cut，不依赖两个 Hall 紧割的未证交换闭包。

证明没有使用任意 middle 边可扩 perfect、一般 owner-private 必是端点、同根 blue3 误当 weak7、小核可加点推出大核可加点等不合法接口。这里完成的是整类排除，不是必要条件累积。

## 10. 保证、文档回执与不变状态

全部新增 unreviewed/unaccepted。主会话与三名数学协作者的交叉核对属于同会话生成检查，不构成独立数学 review。指定 native Sol/high 仅忠实转写及文档检查，未知 backend、actual effort 不声称已验证。PASS_DOCUMENT_ONLY 只代表文档一致性，不认证数学、不升级接受或 assurance。

回执为 `tmp/n7_lock_interval_critical_closure_20261102/DOCUMENT_CHECK.json`，检查限严格 UTF-8、公式连续唯一、本地链接可读、参数代入字符串及手工算术、七保护文件当前 SHA256 和 task status/completedAt，以及指定两新路径。

未调用外部 Claude、未传研究材料，未执行科研代码、枚举、SAT、solver 或 proof 重放。所有旧稿、task.json、metadata、接受/assurance、绑定、runtime、运行及指针保持；task 仍 in_progress、completedAt=null。不提交、不归档，仅新增本文和回执。主会话已全文通读并完成指定精度修正；同会话核查不构成独立数学审阅，长期任务仍未完成。
