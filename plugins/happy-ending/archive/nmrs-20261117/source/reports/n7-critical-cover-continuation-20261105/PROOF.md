# 临界覆盖、hole预算与实际路径阻断

2026-11-05。本轮实质局部结果是二根全路径安全增广定理：在明确的canonical单free点、完整sink根与区间人口条件下，构造第二个真实free点，排除49点层中至少9个sink根的整个类。其后完整整理带hole覆盖、full-neutral及BRB推论，并分列真实反例；这些整理不声明原创首次或新证明机制。中性through加权重推则准确归回旧定理复核，不叫新排除或缺口修复。全部新编推导为 **same-session、unreviewed/unaccepted**，文档Sol只忠实转写，不进行独立数学评审。当前全模型工作链仍为 **40/49/75/76**，没有新的全局48或74。

## 1. 语义、状态与依赖范围

$N_{\rm sig}$表示完整有序rank-3 signotope的最大避免人口，不是forcing threshold。全部递增三元组完整染色，四点packet按$abc,abd,acd,bcd$至多变色一次；单色路径对子序列遗传，长度按实际顶点数计。$\mathrm{weak}(n)$禁止同一对实际首末点的异色路径长度和至少$n+2$，不要求内部不交。

各节明确注明自己的帽与容量假设；不将一个节的额外假设默认为全局已得。旧$C=N_{\rm sig}(7,6,6)\le49$为完整同会话工作证明，未独审；原$b=25$接受及same-family/provisional保证保持，不连带升级后续结构。[766严格容量正文](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n766-strict-capacity-20261105/PROOF.md>)。

## 2. 二根全路径安全增广的整类定理

固定$p\ge4$，设$X$禁$R_{p+1},B_{p+1},\mathrm{weak}(p+2)$，且$|X|\ge2$。令

$$
U=\operatorname{Src}_{R_p}(X),\qquad
V=\operatorname{End}_{B_p}(X),\qquad
X\setminus(U\cup V)=\{z\}.
\tag{T1}
$$

连接禁配给$U\cap V=\varnothing$；$U,V$分别命中全部实际红$p$、蓝$p$路径。这里的$z$是canonical唯一free点。定义$\Omega(X)$为全部合法短帽覆盖的最大交叠人口；等价地，是不交红/蓝物理hit集下的最大free人口。[既有覆盖/横截对应](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_OPTIMAL_OVERLAP_EXCHANGE_AND_CUT_INTERFACES_20261028.md>)。

若某个$a\in U$使$V\cup\{z,a\}$无$R_p$，则$U\setminus\{a\}$仍命中全部红$p$，保留$V$后已有两个free点$\{z,a\}$。若某个$b_0\in V$使$U\cup\{z,b_0\}$无$B_p$，换色侧同样直接得到$\Omega(X)\ge2$。以下仅处理这两方向**所有单加都不安全**的剩余接口。

建立完整ambient实际端点有向图：每条实际$R_p(a,b_0)$，$a\in U,b_0\in V\cup\{z\}$，给红边$a\to b_0$；每条实际$B_p(a,b_0)$，$a\in U\cup\{z\},b_0\in V$，反向给蓝边$b_0\to a$。必须收集全部实际边，不只private供应。

**定理。** 该图是DAG，唯一可能的sink为$z$，且$z$确有恰一种颜色的入边。若为红入，定义完整sink根集

$$
K=\{a\in U:N^+(a)=\{z\}\}.
$$

则$K$非空，并且

$$
\boxed{|V|<(p-2)|K|\quad\Longrightarrow\quad\Omega(X)\ge2.}
\tag{T2}
$$

蓝入情形通过换色并反序给出对偶整类结论。

**证明。** 每个$U/V$点由单加不安全的实际private路径至少产生一条出边：红路径只能从被加入的$U$点启动，蓝路径只能终于被加入的$V$点。$z$既不是ambient红$p$源，也不是蓝$p$末，故无出边。任何有向环都不经过$z$，因而是完整实际双色端点图的交替环，已由旧定理排除。[ambient交替环证明](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n766-strict-capacity-20261105/PROOF.md>)。

$|X|\ge2$保证$U\cup V$非空。每个非$z$点都有出边，DAG中的出边行走必须终于$z$，所以$z$确有入边。若红、蓝两色入边都有，则$z$同时为红$p$末与蓝$p$源，桥接迫$R_{p+1}$或$B_{p+1}$，矛盾。

取红入情形。按DAG拓扑序取最后一个非$z$顶点，它必须只指向$z$；因$z$没有蓝入边，该顶点在$U$，所以$K$非空。所有$K$点均早于$z$，依序写成$k_1<\cdots<k_m<z$。

每个$k_i$的单加不安全见证位于$V\cup\{z,k_i\}$，只能始于$k_i$；由于其完整出邻只有$z$，必终于$z$。因此$(k_m,z)$内至少有$p-2$个$V$点。若每个相邻开区间$(k_i,k_{i+1})$也至少有$p-2$个$V$点，则$m$个不交开区间共同给

$$
|V|\ge m(p-2),
$$

与式(T2)前件矛盾。故存在相邻根$u<v$，其间$V$点少于$p-2$；$m=1$时末段本身已否定该前件，不产生被遗漏的边界例。

构造新的不交hit集

$$
U'=(U\setminus\{u,v\})\cup\{z\},\qquad V'=V.
\tag{T3}
$$

全部蓝路径仍由$V$命中。若有红$p$漏过$U'$，它必须完整位于$V\cup\{u,v\}$，源只能为$u$或$v$。若末点在$V$，该根具有指向$V$的ambient红出邻，与完整根定义矛盾；若末点为另一个根，只可能从$u$到$v$，其$p-2$个内部点必须都在$V\cap(u,v)$，人口不足。其余末点不可能。故全部实际红$p$也被$U'$命中，包括同时用到两个被释放根的路径，不以private族代替完整暴露族。

新hit集恰留下$\{u,v\}$两个free点，等价短帽覆盖交叠为二，所以$\Omega(X)\ge2$。证毕。

### 2.1 49点层的准确数值caller

取$p=5,b=25,n=49$。canonical$U\cup\{z\}$无蓝五、$V\cup\{z\}$无红五，两侧均至多25点，人口和为50，迫$|U|=|V|=24$。若完整红sink根数至少9，则$24<3|K|$，定理给$\Omega\ge2$，进而$n\le25+25-2=48$，矛盾；蓝sink对偶相同。

因此这个**至少9个完整sink根的49点接口整类**已排除。canonical free域为空，以及canonical free域为一点但对应根数至多8的分支仍开；没有普适$\Omega\ge2$，也没有全局C48。对singleton不能使用“图必有入边、$K$非空”，本定理已以$|X|\ge2$显式排除该空真边界。

## 3. 带hole的严格覆盖定理

固定$p\ge4$，设$X$为无$\mathrm{weak}(p+2)$的完整有序signotope。设正整数$a,b$是有效容量：对本节调用的任意实际子域，无$B_p$者人口至多$a$，无$R_p$者人口至多$b$。令

$$
H=\operatorname{End}_{B_p}(X)\cap\operatorname{Src}_{R_p}(X),
\qquad h=|H|.
$$

**定理。** 有

$$
\boxed{|X|\le a+b+h-1.}
\tag{H1}
$$

**证明。** 定义实际覆盖域

$$
A=X\setminus\operatorname{End}_{B_p}(X),\qquad
B=X\setminus\operatorname{Src}_{R_p}(X).
$$

$A$无$B_p$，$B$无$R_p$，故$|A|\le a,|B|\le b$，且$A\cup B=X\setminus H$。若$A\cap B$非空，直接计数即得式(H1)。若$A\cup B$为空，$|X|=h$，由$a,b\ge1$同样得到结论。

只剩非空不交覆盖$A\sqcup B=X\setminus H$。假设每个$a_0\in A$都不能安全加入$B$、每个$b_0\in B$都不能安全加入$A$。前者给$B\cup\{a_0\}$内实际$R_p$，其源只能是$a_0$，因为$B$没有ambient $R_p$源；末点在$B$。后者给$A\cup\{b_0\}$内实际$B_p$，其末只能是$b_0$，因为$A$没有ambient $B_p$末；源在$A$。

在$A\sqcup B$上取**完整ambient实际路径端点图**：红$p$路径从$A$到$B$记正向边，蓝$p$路径反向记从$B$到$A$的辅助边。全部失败保证每顶点有出边，非空有限图必有交替环。旧替末/最短交替环定理仅用$\mathrm{weak}(p+2)$便排除这种完整ambient环，不需要额外的$R_{p+1}/B_{p+1}$帽，矛盾。[完整替末与交替环证明 §§2–3](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n766-strict-capacity-20261105/PROOF.md>)。

故有一点可全路径安全加入另一侧。保留原侧，新增侧仍为对应无色$p$路径容量域，因此原$|A|+|B|$至少节省一，再加未覆盖的$h$个hole，得到式(H1)。一侧为空时，向空侧加入实际单点自然安全。

这里不声称替末后的新路径保留最初跨侧失败见证的纯内部支持；新边只须属于完整ambient端点图，允许经过hole或其他实际点。证毕。

### 3.1 767中的准确后果与hole身份

取$p=5$，另假定$X$禁$B_6,R_7,\mathrm{weak7}$。无$B_5$子域受既有757容量$a=40$控制，无$R_5$子域受换色756容量$b=25$控制，所以

$$
|X|\le64+h.
\tag{H2}
$$

因此整个$h\le10$类至多74点；尚未证明任意母体都满足$h\le10$。

本节$H$是入蓝五与出红五交集。每个$h_0\in H$都不是ambient红六源：若其入蓝五接出红六，桥蓝得蓝六、桥红得红七。因此$H$内部不可能有红六。

若$H$内部有蓝五，设末点为$h_0$、末前驱为$v\in H$，取$h_0$的实际出红五。连接桥若蓝就延长原蓝五为蓝六，故必须红；于是前接$v$产生从$v$启动的红六，与$v\in H$的上一禁配矛盾。所以$H$也无蓝五。这些身份尚未兑现一般$h\le10$，不能据其直接声称全局74。

## 4. full-neutral经典满容量排除

固定$p\ge4$。设$Y$无$R_{p+1},B_{p+1}$，定义全部ambient角色

$$
E=\operatorname{End}_{R_p}(Y),\qquad
S=\operatorname{Src}_{B_p}(Y),\qquad
Z=Y\setminus(E\cup S).
$$

再显式假定

$$
Z\cap\operatorname{End}_{B_p}(Y)=\varnothing,
\qquad |Z|=c_p=\binom{2p-4}{p-2}.
\tag{N1}
$$

该额外假设禁止的是**ambient**蓝$p$末点，不只是$Z$内部无蓝$p$路径。

**定理。** 此时$S$为空，整个$Y$无$B_p$。若另有$\mathrm{weak}(p+2)$禁止及相应短帽容量$b$，则$|Y|\le b$。

**证明。** $E\cap S$为空：入红$p$与出蓝$p$在同点连接，桥红给$R_{p+1}$，桥蓝给$B_{p+1}$，均不允许。按定义$Z$既无$R_p$也无$B_p$。

反设$s\in S$。$Z\cup\{s\}$有$c_p+1$点，经典杯帽容量迫出$R_p$或$B_p$。红$p$路径没有可能末点：$Z$避开$E$，而$s\in S$也不在$E$。蓝$p$路径的源只能是$s$，因为$Z$避开$S$；由式(N1)，其末点也只能是$s$，与实际$p$路径首末互异矛盾。因此$S$为空，$Y$没有蓝$p$路径。

若还具有weak禁止，$Y$属于无$B_p,R_{p+1},\mathrm{weak}(p+2)$的短帽域，人口至多$b$。证毕。

$p=5$时$c_5=20$，可用$b=25$。本定理不命中真正M0 tight-owner接口的$|Z|\le10$区域，不能改写为未证的$o\le\alpha-1$。经典容量只在式(N1)的满20入口使用。[经典容量原接口](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-extremal-stars-and-run-exclusion-20261104/research.md>)。

## 5. BRB矩形不共存

固定$p,q\ge3$，设$X$禁$B_{p+1},R_{q+1},\mathrm{weak}(q+1)$，后者的同端阈值为$q+3$。实际端点满足$a<c<b_0<d$。

**定理。** 实际路径$R_q(a,b_0)$、$B_p(a,d)$、$B_p(c,b_0)$不能同时存在。

**证明：先处理共同源接口。** 先只取$R_q(a,b_0)$与$B_p(a,d)$，证明$\chi(a,b_0,d)=B$。反设该三元组红，记蓝链为

$$
a,u_1,\ldots,u_{p-2},d.
$$

没有$u_i=b_0$，否则蓝路径遗传会给$\chi(a,b_0,d)=B$。若$u_i<b_0$，红$q$同端禁止蓝三，迫$\chi(a,u_i,b_0)=R$；但packet$(a,u_i,b_0,d)$前三项为$R,B,R$，非法。故全部$u_i>b_0$。

对packet$(a,b_0,u_i,d)$，第二项$\chi(a,b_0,d)=R$、第三项$\chi(a,u_i,d)=B$，迫整包为$R,R,B,B$。所以$\chi(a,b_0,u_i)=R$、$\chi(b_0,u_i,d)=B$。

$p=3$时已得$B_p(b_0,u_1,d)$。$p\ge4$时，packet$(a,b_0,u_1,u_2)$的前两项红、第三项蓝，迫$\chi(b_0,u_1,u_2)=B$，其余蓝链保留，同样得到$B_p(b_0,u_1,\ldots,d)$。

取原红$q$路径的末前驱$t$。若$\chi(t,b_0,u_1)=R$，原红链后接$u_1$得到$R_{q+1}$；所以该三元组蓝。前接$t$又把蓝$p$延长为$B_{p+1}$，矛盾。因此共同源接口必有$\chi(a,b_0,d)=B$。

**加入内蓝链。** 记$B_p(c,b_0)$的末前驱为$t$，则$a<t<b_0$。$R_q(a,b_0)$的同端weak禁止迫$\chi(a,t,b_0)=R$。packet$(a,t,b_0,d)$第一项红、第三项蓝，迫末项$\chi(t,b_0,d)=B$。内蓝$p$后接$d$成为$B_{p+1}$，矛盾，定理证毕。

反序版本保持相应首末身份；证明不要求$p\le q$、路径内部不交、几何实现或挑选特定支持。BRB及完整交替环不能再记作757新数值收益；下文HKH实际反例说明其他开放链不自动服从同一排除。

**历史定位。** 共同源证明在$q=6,3\le p\le6$时已完整见于 [RESET-R5 §6](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R5_COVER_AUGMENTATION_CAPACITY.md:115>)：内部点全部移到$b_0$之后、RRBB、改蓝首、红末前驱延蓝均已给出。本文按一般$p,q$整理，并把内蓝末对后一packet的直接后果显式列出，不重认领当前757参数的新机制。

## 6. 实际反检：覆盖谓词和路径形状必须分开

### 6.1 十一点实际几何与两种完整覆盖

固定几何点按零基编号$0,\ldots,10$，坐标为

$$
\begin{aligned}
&(0,0),(10,-1),(20,-10),(30,-30),(40,-89),(50,-100),\\
&(60,-89),(70,-30),(80,-10),(90,-1),(100,0).
\end{aligned}
$$

正整数方向为红。既有精确验证给全部蓝五恰为

$$
\begin{gathered}
(0,1,2,3,4),\ (0,1,2,3,5),\\
(5,7,8,9,10),\ (6,7,8,9,10).
\end{gathered}
$$

全部红五恰为16条$(l,4,5,6,r)$，其中$l\in\{0,1,2,3\}$、$r\in\{7,8,9,10\}$。两条蓝五$0\to5$、$5\to10$存在，却不能通用压缩成蓝五$0\to10$；反色红五同外端$0\to10$确实存在。实际红through为空、蓝through为$\{5\}$。这是有限实际几何反检，不是一般free人口界。[完整witness](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_endpoint_triangle_20261105/witness.json>)。

对同一完整红/蓝路径族，要求物理红hit集$U$、蓝hit集$V$不交：若每条路径须有端点被相应hit集命中，精确最大free数为4；若允许在整条实际路径内部任意位置命中，精确最大free数为8。两者分别完整搜索$3^{11}=177147$个单标签赋值，不能混用谓词。

一个endpoint最优赋值是$U=\{0,1,2,3\},V=\{4,5,6\}$；一个whole-path最优赋值是$U=\{4\},V=\{0,7\}$。后者free为$\{1,2,3,5,6,8,9,10\}$。完整最优计数及每条实际路径命中证书见 [cover_optima.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_endpoint_triangle_20261105/cover_optima.json>)。

### 6.2 十四点757的实际HKH反例

既有完整signotope见证满足无$B_5,R_7,\mathrm{weak7}$，零基支持$a=0,c=1,b_0=12,d=13$，同时有

$$
\begin{aligned}
R_6(0,12)&=(0,2,6,8,10,12),\\
R_6(1,13)&=(1,4,6,7,9,13),\\
B_4(1,12)&=(1,2,9,12).
\end{aligned}
$$

这是实际HKH排除的反例，允许真实内部点共享；没有附加诱导纯内部或private供应条件，也不宣称几何可实现。最大红/蓝长为6/4，同端和至多8。[semantic.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_hkh_crossing_probe_20261105/semantic.json>)。

上述两个实际反检与本稿解析定理分别承担各自范围，不能将有限运行升格为全局定理。科学原始证据与状态见 [VERIFICATION.md](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-critical-cover-continuation-20261105/VERIFICATION.md>)；未闭义务见 [NEXT_SESSION.md](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-critical-cover-continuation-20261105/NEXT_SESSION.md>)。

### 6.3 固定n15的outer-short原始否定不是第三个反例

最后一份定点公式在15点balanced766上，固定$a=0,d=14$，测试某个$1\le c<b_0\le13$同时具有

$$
R_4(a,d),\qquad R_5(c,b_0),\qquad
B_5(a,b_0),\qquad B_5(c,d).
$$

外红四只要求存在，没有额外禁止外红五。唯一AE调用返回 `RAW_UNSAT_FIXED_N15_FORMULA_UNCHECKED`，solver exit20、7.837402286008秒，180秒预算未超时；没有proof或checker，也没有实际反例染色。它只保留该固定公式的未检查原始否定，**不能证明普适single-defect-cycle排除，也不覆盖更小n或允许padding外推**。outer-short四路径接口仍未解析闭合。[真实README](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_outer_short_cycle_probe_20261105/README.md>) · [result.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_outer_short_cycle_probe_20261105/result.json>)。

## 7. 旧定理复核与重复路线识别

本轮重推了中性域红五through的加权排除，但Root全文比对后确认：不仅结论，连同$C_0$供给、物理覆盖及左右替锁方法，都已存在于 [N7_7576_DEPENDENCY_AUDIT_AND_SINGLE_THROUGH_EXCLUSION_20261103.md §§2–5](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7576_DEPENDENCY_AUDIT_AND_SINGLE_THROUGH_EXCLUSION_20261103.md>)。本轮未发现旧稿缺口，故这是旧定理正确重推/复核，不是新结构排除、承重修复或数值突破，不重复转写成长篇新成果。

准确旧式为：$X$禁$R_7,B_6,\mathrm{weak7}$，$D=X\setminus(\operatorname{Src}_{R_6}(X)\cup\operatorname{End}_{R_6}(X))$，$w=|\operatorname{Src}_{R_5}(D)\cap\operatorname{End}_{R_5}(D)|$，则

$$
n+\min(w,1)\le3b,\qquad n+w\le3b+1.
\tag{W1}
$$

旧证明对$t=n+w-3b=1$重做去掉$C_0$后的供给等号，再恢复整个$D$的端点覆盖；内部经过$C_0$的路径仍由完整ambient左到右红五禁形控制，不是漏去该族。S/T邻点根排除及两侧替锁迫$C_0$在共同根两边各有一点，故$t=1$迫$w\ge2$。这正是旧稿的完整方法，不是本轮新技术。

在$b=25$时，旧式已给正$w$类人口至多74。结合上一轮 [完整ambient红六无through类≤74](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n766-strict-capacity-20261105/PROOF.md>)，75点剩余入口是$I\ne\varnothing,w=0$；这里$I$是ambient红六源末交集，$w$是$D$内红五through，两者不可混淆。尚未证明一般$n+w\le3b$，也没有用本轮复算排除$t=1,w\ge2$。重复发现旧结果，是需要在下一路线选择前检查原证据的具体例子。

另一个止损来自回读 [旧$t=0$原稿 §§2–4](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_T0_CRITICAL_LAYER_AND_SATURATION_BARRIERS_20261103.md>)：严格交错分支原已排除$\alpha=0$或$\beta=0$，因此新C49带来的$\alpha,\beta\ge1$没有进一步缩小这一剩余分支。clean供给取等即使能整理为三个实际满$b$短帽核$X=K\sqcup J_-\sqcup J_+$，也不能据此断言任意两核并集balanced。跨核红六仍可能出现；仅删除某个角色集的端点匹配边，也不保证其余实际见证内部避开该集，不能直接把路径搬到新并域。本轮没有关闭clean严格交错整类，缺的是完整实际路径的并域桥，不是更多端点标签。

## 8. 防止局部最优：仍需实际全局入口

暂停端点小模板增补、同色两run压缩、HKH整类禁形和重复$t=1$推导。现有实际反例与历史正文已分别约束这些接口；只改标签、挑单一路径或重复旧等号，不计新排除。766主攻二根定理后49点剩余类的完整批量交换，outer-short只是其中未闭子接口；757须使用同一实际满16/满25域的共同结构。767尚缺$I\ne\varnothing,w=0$临界母体的真实全路径净收益、可普适提取的安全矩形/覆盖，或直接排除75点的全类桥；普适$Q\le C+b$仍未证明。不把整理推论数量、固定n15原始否定或重复旧证明视作全局推进。
