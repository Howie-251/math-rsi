# N7：共同中间匹配兼容与加权 through 上界

2026-11-03。本文新增工作证明均为 **unreviewed / unaccepted**。数学由主会话定稿，生成与交叉核对属于同会话核对。指定 native gpt-6.1-sol/high 文档执行者只负责忠实转写及文档一致性检查。未报告的 backend 与实际 effort 不作验证结论。

**加权工作定理。** 设 \(X\) 是完整的 767 母体，\(b\) 是 756 与换色 756 的共同有效容量。令 \(w\) 为实际 \(D\) 中同时有入、出红五的点数，则
\[
|X|+w\le3b+2 .
\tag{1}
\]
旧加权工作界为 \(3b+3\)。本定理降低加权容量一单位，无条件人口工作界见末节。

## 1. 模型、归一化与根工具

母体为有序 rank-3 signotope。对 \(a_1<a_2<a_3<a_4\)，按字典序排列的四个三元组颜色至多改变一次。\(R_k,B_k\) 表示红、蓝 \(k\) 点路径，由实际点上的连续三元组确定，路径对子序列遗传。weak7 指同一对实际首末点之间有一红一蓝两条路径且长度和至少为 \(9\)，内部可共享。767 禁 \(R_7,B_6,\mathrm{weak7}\)，766 禁 \(R_6,B_6,\mathrm{weak7}\)，756 禁 \(R_6,B_5,\mathrm{weak7}\)，换色 756 禁 \(R_5,B_6,\mathrm{weak7}\)。记 \(n=|X|\)。角色按标明的实际域计算，ambient 指 \(X\)。
\[
\begin{aligned}
S&=\operatorname{Src}_{R_6}(X),& T&=\operatorname{End}_{R_6}(X),& I&=S\cap T,\\
P&=S\setminus T,& Q&=T\setminus S,& D&=X\setminus(S\cup T),\\
U&=\operatorname{Src}_{R_5}(D),&V&=\operatorname{End}_{R_5}(D),&
C_0&=U\cap V,\qquad w=|C_0|.
\end{aligned}
\tag{2}
\]

既有工具沿用各自的保证层级。

- 旧加权式、实际 canonical 换核及头尾替换见 §3、§7–8。[加权稳定性稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7879_INTERFACE_AUDIT_AND_WEIGHTED_THROUGH_STABILITY_20261031.md>)
- 实际消 \(M\) 及完整 ambient 根工具见 §2–3，纤维容量与两侧锁端口见 §4–5。[锁纤维归一化稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCK_FIBER_NORMALIZATION_AND_DOUBLE_OMEGA_EXCLUSION_20261102.md>)
- 端点对 Hall、实际扩域及双 clean 修补核见 §2、§6。[实际端点对 Hall 稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_ENDPOINT_PAIR_HALL_MISALIGNMENT_EXCLUSION_20261102.md>)
- 实际根瓶颈与旧人口工作界见 §2、§8。[锁区间与临界闭合稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCK_INTERVAL_AND_CRITICAL_CLOSURE_20261102.md>)
- 跨角色根序、非交错根的旧人口参数式及 onefull 纯前供见 §2、§3、§5。[跨角色根序稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_CROSS_ROLE_ROOT_ORDER_AND_SEPARATED_CLASS_EXCLUSION_20261103.md>)

为证 (1)，由旧加权式只需排除 \(n+w=3b+3\)，允许任意 \(w\ge0\)。先在每一方向作旧 canonical 换核。由联合预算 \(n+w\le3b+5-\eta\)，归一化缺额 \(0\le\eta\le2\)。此处 \(\eta\) 的上界对任意 \(w\) 一样。以左侧为例，换核后实际 \(766\) 核 \(H\) 有 \(2b-\eta\) 点，含 \(D\)。从 \(H\) 启动的全部 ambient \(R_6\) 终点恰为域外锁集 \(\Omega\subseteq T\)，补集去掉 \(\Omega\) 后属于 \(S\)。核内 owner 集 \(A_H=H\cap S\subseteq P\)，每个 owner \(a_0\) 有 ambient 入 \(R_5\) 与出 \(B_5(a_0,\omega(a_0),\ldots)\)。其全部出 \(R_6\) 的终点及出 \(B_5\) 的第二点都是唯一锁 \(\omega(a_0)\)。余下的 mixed 集 \(M\subseteq P\setminus H\) 锁向 \(H\cap T\)，满足 \(|\Omega|+|M|\le\eta\)。

记 \(\Lambda=h(M)\subseteq Q\)，\(t_\Lambda=|\Lambda|\le |M|\)。作实际换核
\[
H_{\rm new}=(H\setminus\Lambda)\sqcup M,\quad
\Omega_{\rm new}=\Omega\sqcup\Lambda,\quad
\eta_{\rm new}=\eta-|M|+t_\Lambda .
\tag{3}
\]
旧 owner 保留且仍锁向旧 \(\Omega\)，新增 owner \(M\) 全锁向 \(\Lambda\)，故新核内部无 \(R_6\)，遗传 \(B_6\) 与 weak7 的禁形。每个新旧锁都有实际 owner 供应。补集中新增的 \(\Lambda\) 是 \(Q\) 点，剩余 mixed 集为空。\(D\) 和 \(C_0\) 仍在核内，且 \(W=(S\setminus\Omega)\cup C_0\) 保持，因为 \(\Lambda\cap S=\varnothing\)。新锁数至多新缺额，缺额不增。若换核后缺额为零，则新锁集为空，因而 \(M\) 已为空且此前已为缺额零的 fullstandard。两方向各自换核，ambient 角色保持。

以下用 \(H_L,H_R\) 表示这两个实际 766 核，大小分别为 \(2b-\alpha,2b-\beta\)。沿用左 owner \(A_H\) 与左锁 \(\Omega\)，记 \(a=|A_H|,o=|\Omega|\)。右侧有 \(B_H=H_R\cap T\subseteq Q\)，右锁 \(\Psi\subseteq S\setminus H_R\)，记 \(d=|B_H|,p=|\Psi|\)。每个右 owner 有 ambient 出 \(R_5\) 与入 \(B_5\)，其全部入 \(R_6\) 的首点及入 \(B_5\) 的倒数第二点同锁于 \(\Psi\) 中一点。两侧补集分别为 \((S\setminus A_H)\cup\Omega\) 与 \((T\setminus B_H)\cup\Psi\)，且 \(a\ge o,\ d\ge p\)。

\(S\cup U\) 无 ambient \(B_5\) 终点，\(T\cup V\) 无 ambient \(B_5\) 源。\(W\) 中非 owner 且有 ambient 入 \(R_5\) 的点无 ambient \(B_5\) 源，owner 的 \(B_5\) 第二点锁在域外 \(\Omega\)，\(C_0\subseteq V\) 无 ambient \(B_5\) 源。于是 \(W\) 有完整端口，即 \(W\) 中有 ambient 入 \(R_5\) 的点，若启动 \(B_5\)，其第二点在 \(W\) 外。反序 \(W'=(T\setminus\Psi)\cup C_0\) 有完整反端口。末点在 \(S\cup U\) 的 \(B_4\) 可保首相邻对向右延长为 \(B_5\)，反序首点在 \(T\cup V\) 可保末相邻对向左延长。完整端口因而排除 \(W\) 内的红五末点与蓝四源的交会，反序亦然。两域是有效 \(D_7\) 基底，即无 \(B_5\)、无 weak7 且内部 \(\operatorname{End}_{R_5}\cap\operatorname{Src}_{B_4}=\varnothing\)。内部 \(R_6\) 横截至少为各域大小减 \(b\)，人口至多 \(b+5\)。一般记 \(t=n+w-3b\)，得到
\[
h_L=|W|-b=t+\alpha-o+a,\qquad
h_R=|W'|-b=t+\beta-p+d .
\tag{4}
\]
加权取等时 \(t=3\)。用 \(0\le o\le\alpha\le2\)、\(a\ge o\) 与 \(h_L\le5\)，左侧有锁时 \((\alpha,o,a)\) 只可能为 \((1,1,1),(1,1,2),(2,1,1),(2,2,2)\)，右侧反序同理。此分类用于整个加权取等层。

定义全部 ambient 相邻对根和核内端点如下。
\[
\begin{aligned}
\widehat E&=\{r\in W\cap T:\ \exists\text{实际 }R_6\text{ 末对 }(u,r),\ u\in W\},\\
\widehat F&=\{s\in W'\cap S:\ \exists\text{实际 }R_6\text{ 首对 }(s,v),\ v\in W'\},\\
e&=|\widehat E|,\quad f=|\widehat F|,\quad x=\min\widehat E,\quad y=\max\widehat F,\\
C&=\operatorname{End}_{R_5}(H_L),\quad C'=\operatorname{Src}_{R_5}(H_R),\\
Z_+&=C\cap D,\quad Z_-=C'\cap D,\quad c_+=|Z_+|,\quad c_-=|Z_-|.
\end{aligned}
\tag{5}
\]
两根族都在 \(I\)，且 \(h_L\le e\le6,\ h_R\le f\le6\)。下界来自横截容量，上界来自各根族是红 clique。具体而言，实际末对 \((u,r)\) 给所有 \(z>r\) 的末帽 \(\chi(u,r,z)=B\)，首对 \((s,v)\) 给所有 \(z<s\) 的首帽 \(\chi(z,s,v)=B\)，因为红桥分别可后接或前接成 \(R_7\)。对 \(r\in\widehat E\) 和 \(r<z<t_0\in S\cup U\)，若 \(\chi(r,z,t_0)=B\)，接 \(r\) 的实际末帽得到 \(B_4(u,r,z,t_0)\)。它可保首对延为 \(B_5\)，其首对两点均在 \(W\)，且 \(u\) 有 ambient 入 \(R_5\)，违完整端口。故 \(\chi(r,z,t_0)=R\)。对 \(s\in\widehat F\) 与 \(t_0<z<s,\ t_0\in T\cup V\)，反序得 \(\chi(t_0,z,s)=R\)。两扇允许中点 \(z\) 取 ambient 点。

## 2. 共同中间匹配与非交错根序

中间匹配只取一份。先从实际中间域删去 \(C_0\) 的 \(w\) 个实际点，再以剩域中全部实际 \(R_5\) 的首末点建二部图。若余域有 \(b+m\) 点且 \(m>0\)，最大匹配不足 \(m\) 时，König 定理给少于 \(m\) 个角色顶点的覆盖。删去相应实际点后余域仍超过 \(b\) 点且无 \(R_5\)，违反换色 756 容量。角色副本重合只会减少实际删点。两侧外匹配都沿这份中间匹配运输。任一交会给实际末对 \((u,r)\)、中间 \(R_5(u\to v)\) 及首对 \((s,v)\)，且 \(u<r<s<v\)。两帽给 \(B_4(u,r,s,v)\)，与中间红五同实际首末点，违反 weak7。

**非交错根序定理。** 若完整双向 M0 接口成立且 \(t=n+w-3b\ge2\)，则 \(x\ge y\) 不可能。

若 \(a_0\in A_H\cap\Psi\)，右锁的精确供应给实际 \(R_6(a_0\to b_0)\)，其中 \(b_0\in B_H\)。两侧唯一锁迫 \(b_0=\omega(a_0)\) 且 \(a_0=\psi(b_0)\)。沿共同实际相邻对 \((a_0,b_0)\) 接左出 \(B_5\) 与右入 \(B_5\)，得 \(B_8\)，从而得 \(B_6\)。反序排除 \(B_H\cap\Omega\)。因此
\[
H_L\cap H_R=D\sqcup A_H\sqcup B_H .
\tag{6}
\]
记 \(|D|=b+q\)，\(m=q+a+d-w\)，\(i=|I|\)，\(\delta=|\Omega\cap I|\)，\(\varepsilon=|\Psi\cap I|\)，\(\Gamma=(\Omega\cap I)\cup(\Psi\cap I)\)，\(\rho=|\Omega\cap\Psi|\)。补集计数给 \(|S|=b+t-w+\alpha-o+a+\delta\)，以及反序等式。代入 \(i=|S|+|T|+|D|-n\) 得
\[
i=m+t+\alpha+\beta-o-p+\delta+\varepsilon,\qquad
|I\setminus\Gamma|=m+t+\alpha+\beta-o-p+\rho .
\tag{7}
\]
若 \(x>y\)，则 \(e+f\le i\)。结合 (4) 得 \(m\ge t+(a-\delta)+(d-\varepsilon)\ge t\)。若 \(x=y\)，两根族至多共一点，由 \(e+f\le i+1\) 得 \(m\ge t-1+(a-\delta)+(d-\varepsilon)\ge1\)。

实际中间域 \((H_L\cap H_R)\setminus C_0\) 有 \(b+m\) 点。全部 \(R_5\) 首点在 \((Z_-\setminus C_0)\sqcup A_H\sqcup(C'\cap B_H)\)，末点在 \((Z_+\setminus C_0)\sqcup B_H\sqcup(C\cap A_H)\)。每个右纤维的最晚 owner \(b_0\) 不在 \(C'\)。否则将其核内出红五接入蓝五末对，蓝桥给 \(B_6\)，红桥给从同一右锁开始且终于更晚核内点的 \(R_6\)。该末点属于同一纤维，违最晚性。反序每个左纤维的最早 owner 不在 \(C\)。故 \(|C'\cap B_H|\le d-p,\ |C\cap A_H|\le a-o\)。固定上述容量论证给出的 \(m\) 条实际中间匹配，首末像为 \(J_U,J_V\)。用容器大小减去 \(m\) 得
\[
|(Z_-\setminus C_0)\setminus J_U|\le c_--q-p,\qquad
|(Z_+\setminus C_0)\setminus J_V|\le c_+-q-o .
\tag{8}
\]
容器和中间规模均已扣 \(w\)，两项在端口损失中抵消。

令 \(P_H=P\cap H_R,\ Q_H=Q\cap H_L\)。实际核 \(L_-=C'\cup P_H\cup B_H\)、\(L_+=C\cup Q_H\cup A_H\) 分别位于 \(H_R,H_L\)，无 \(R_6\)。若 \(C'\) 中一点终止 ambient \(B_5\)，接其核内出红五时蓝桥给 \(B_6\)，红桥给终于 \(H_R\) 的 \(R_6\)，所以蓝五倒数第二点是域外 \(\Psi\) 点。\(B_H\) 的入蓝五同样锁在 \(\Psi\)，\(P_H\subseteq S\) 无 ambient 蓝五末点身份。故 \(L_-\) 无 \(B_5\)，\(L_+\) 反序同理。两核为实际 756，缺额分别为
\[
\kappa_-=q+\beta-c_-\ge0,\qquad
\kappa_+=q+\alpha-c_+\ge0 .
\tag{9}
\]

取 \(B,A\subseteq I\setminus\Gamma\) 且 \(B<x,\ A>y\)，分别加到 \(L_-,L_+\)。新增 \(I\) 点无 ambient \(B_5\) 首末身份，且相应锁集仍缺席，两扩域无 \(B_5\)。左扩域的 \(R_6\) 只能终于 \(B\)，因若终于 \(B_H\)，首点必须在缺席的 \(\Psi\)。若末前驱在 \(P_H\cup B\cup C_0\subseteq W\)，末点会触发 \(\widehat E\)，与 \(B<x\) 矛盾。反序右扩域的 \(R_6\) 只能从 \(A\) 启动，若第二点在 \(Q_H\cup A\cup C_0\subseteq W'\)，会触发 \(\widehat F\)，与 \(A>y\) 矛盾。故两侧的全部实际相邻对图分别位于
\[
\bigl((Z_-\setminus C_0)\cup B_H\bigr)\times B,\qquad
A\times\bigl((Z_+\setminus C_0)\cup A_H\bigr).
\tag{10}
\]
实际删去二部顶点覆盖留下 756，故两侧最大匹配至少为 \(|B|-\kappa_-\)、\(|A|-\kappa_+\)。\(C_0\) 已在所有实际外路径的端口定位中排除，扣除 (8) 所列端口即足够。

对任意 ambient \(B_4\) 从 \(T\) 到 \(S\)，由其首点入 \(R_6\) 的末帽和末点出 \(R_6\) 的首帽可各补一点得到 \(B_6\)。故这种蓝四禁形。设 \((b_0,r)\) 为 \(b_0\in B_H\) 的实际末对，\((s,a_0)\) 为 \(a_0\in A_H\) 的实际首对。若 \(r<s\)，两帽给上述禁形 \(B_4(b_0,r,s,a_0)\)，所以 \(s\le r\)。此外根 \(x\) 的加强扇排除 \(x<s<a_0\)，根 \(y\) 的加强扇排除 \(b_0<r<y\)。因此全部 owner 首根至多为 \(x\)，末根至少为 \(y\)。

若 \(x>y\)，取 \(y<\tau<x\) 的同一 ambient 间隙，将 \(I\setminus\Gamma\) 分为 \(B<\tau\) 与 \(A>\tau\)。若全部实际 owner 首根中有一个 \(I\setminus\Gamma\) 根晚于 \(y\)，取其中最晚 \(z\le x\)，选其紧左间隙。所有 \(I\setminus\Gamma\) 的 owner 末根均不早于 \(z\)，故 \(B\) 无 owner 末根，\(A\) 至多有一个 owner 首根 \(z\)。否则选 \(y\) 紧右间隙，\(A\) 无 owner 首根，\(B\) 至多有一个 owner 末根 \(y\)。所以在两侧匹配中舍弃所有 owner 端口边，合计损失至多一条。若 \(x=y=z\)，则 \(z\notin\Gamma\)，取严格 \(z\) 切分，根总量少一个，而两边均无 owner 端口边。两种情形分别扣一次 owner 损失或共同根损失。舍去 (8) 的普通端口后，在同一中间匹配上的交会数 \(\ell\) 满足
\[
\begin{aligned}
\ell&\ge |I\setminus\Gamma|-1-\kappa_--\kappa_+
 -(c_--q-p)-(c_+-q-o)-m\\
 &=|I\setminus\Gamma|-m-\alpha-\beta+o+p-1
 =t+\rho-1\ge1.
\end{aligned}
\tag{11}
\]
任一交会由两帽得到同端 \(B_4/R_5\)，矛盾。

**Onefull 推论。** 若一侧为实际 fullstandard，跨角色根序稿 §5 的纯前供论证给 \(y\le x\)。它只用满侧的纯供给、两侧完整加强扇和真实相邻对，对另一侧缺额无数值限制。\(w=0\) 时严格，有 through 时允许等号。由非交错根序定理，\(t=3\) 的全部 onefull 排除。加权取等余下只需处理双正缺额且 \(x<y\) 的配置。

## 3. 加权取等层的双 clean 排除

设 \(t=3\)、\(x<y\) 且两锁集都为空。此时 \(H_L=X\setminus S,\ H_R=X\setminus T\)，\(\alpha,\beta\in\{1,2\}\)，\(i=q+3-w+\alpha+\beta\)。根数满足 \(3+\alpha\le e\le6,\ 3+\beta\le f\le6\)。

以下使用完整端口下的尾替换。若某实际 \(R_6\) 的第四、五、六点为 \(v_4,v_5,v_6\)，\(v_4\) 有 ambient 入 \(R_5\)，且 \(v_5<f_0\in\widehat F\)，取该红五末前驱 \(v_-\) 与 \(f_0\) 的实际首对 \((f_0,t_0)\)，其中 \(t_0\in W'\)。若 \(\chi(v_-,v_4,v_5)=R\)，则入红五追加 \(v_5,v_6\) 成 \(R_7\)，故该桥为蓝。若 \(\chi(v_4,v_5,f_0)=B\)，首帽给 \(B_5(v_-,v_4,v_5,f_0,t_0)\)，末对均在 \(W'\) 且 \(t_0\) 有 ambient 出 \(R_5\)，违完整反端口。故 \(\chi(v_4,v_5,f_0)=R\)，可将原末点替换成 \(f_0\)。头替换反序成立，要求第三点有 ambient 出 \(R_5\)，且用于替换的 \(\widehat E\) 根严格早于第二点。

收集全部 \(\widehat E<y\) 的实际末对中属于 \(W\) 的末前驱，记为 \(P_0\)，\(r=|P_0|\)。任何此种末前驱若在 \(T\cup C_0\subseteq T\cup V\)，则根 \(y\) 的加强左扇与末帽矛盾，故 \(P_0\subseteq P\)。反序收集全部 \(\widehat F>x\) 的实际首对中属于 \(W'\) 的第二点，得 \(Q_0\subseteq Q\)，记 \(s_0=|Q_0|\)。由 \(x<y\) 与根定义，两集均非空。

从 \(H_L\) 删除 \(C\) 后没有 \(R_5\)，换色容量给 \(|C|\ge b-\alpha\)。\(C\) 各点都有 ambient 入红五。若一点有 ambient 出蓝五，与核内入红五连接时蓝桥给 \(B_6\)，红桥给从 \(H_L\) 启动的 \(R_6\)，后者在 clean 侧也不可能。\(P_0\) 各点是实际末前驱，有 ambient 入 \(R_5\)，由 clean M0 端口无 ambient 出 \(B_5\)。若 \(r\ge\alpha+1\)，将 \(\alpha+1\) 个实际前驱加到 \(C\)，无 \(B_5\) 且超过 \(b\) 点，迫一条 \(R_6\)，其首点必为某个 \(p_0\in P_0\)。取该点对应的低末对 \((p_0,e_0)\)。若该红六末点晚于 \(e_0\)，原末帽给同端 \(B_3/R_6\) 矛盾，故末点不晚于 \(e_0<y\)。域内各点均有 ambient 入红五，故可尾替换到 \(y\)，与末帽给出的 \(B_3(p_0,e_0,y)\) 同端矛盾。因此 \(r\le\alpha\)，反序 \(s_0\le\beta\)。

令 \(k=|\widehat E\cap(-\infty,y)|\)。\(P_0\cup(\widehat E\cap[y,\infty))\) 横截 \(W\) 内全部 \(R_6\)，而 \(\widehat E\cap[y,\infty)\) 与 \(\widehat F\) 至多共有根 \(y\)。所以
\[
k\le e+r-3-\alpha,\qquad
(e-k)+f\le i+1,\qquad
q\ge2+w-r\ge w .
\tag{12}
\]
取实际 \(D\setminus C_0\) 内全部 \(R_5\) 的端点图。容量论证给一份 \(m=q-w\) 条中间匹配。\(m=0\) 时取空匹配。首、末像分别在 \(Z_-\setminus C_0,Z_+\setminus C_0\)，两侧未被匹配覆盖的普通端口数恰为 \(c_--q,c_+-q\)。

修补实际集合 \(L_-=Z_-\sqcup P\sqcup Q_0,\ L_+=Z_+\sqcup Q\sqcup P_0\)。\(L_+\) 的每一点均有 ambient 入红五且无 ambient 出蓝五，对 \(Z_+,P_0\) 已证，对 \(Q\subseteq T\) 则由入红六接出蓝五的两种桥色排除。若 \(L_+\) 有 \(R_6\)，它从 \(P_0\) 启动，原低末帽将末点限制在 \(y\) 之前，再尾替换 \(y\) 得同端矛盾。反序 \(L_-\) 无 \(B_5\)，且由头替换 \(x\) 排除终于 \(Q_0\) 的 \(R_6\)。因此两修补核为实际 756，缺额为
\[
\kappa_-=q+\beta-s_0-c_-\ge0,\qquad
\kappa_+=q+\alpha-r-c_+\ge0 .
\tag{13}
\]
严格在 \(y\) 切分，取 \(B=(I\cap(-\infty,y))\setminus\widehat E,\ A=I\cap(y,\infty)\)，故 \(|A|+|B|=i-1-k\)。两扩域仍无 \(B_5\)。

左域 \(L_-\cup B\) 的 \(R_6\) 若终于 \(t_0\in Q_0\)，取 \(Q_0\) 对应的高首对 \((f_0,t_0)\)，\(f_0>x\)。首帽与 weak7 迫该红六首点不早于 \(f_0\)。全域各点包括 \(B\subseteq I\) 都有 ambient 出红五，头替换 \(x\) 与 \(B_3(x,f_0,t_0)\) 同端矛盾。旧核其余点非 \(T\)，故红六终于 \(B\)。若末前驱在 \(P\cup B\cup C_0\subseteq W\)，末点会触发 \(\widehat E\)。若末前驱在 \(Q_0\subseteq T\)，因其根严格早于 \(y\)，根 \(y\) 的加强左扇与末帽矛盾。故全部左末对从 \(Z_-\setminus C_0\) 指向 \(B\)。

右域 \(L_+\cup A\) 的 \(R_6\) 若从 \(P_0\) 启动，原低末帽迫其末点不晚于对应的低根，新增 \(A>y\) 无点可参与，退回旧 \(L_+\) 矛盾。因此源在 \(A\)。第二点不能在 \(P_0<y\)，若在 \(Q\cup A\cup C_0\subseteq W'\) 则触发 \(\widehat F\)。故全部右首对从 \(A\) 指向 \(Z_+\setminus C_0\)。

由容量与 König 定理，两侧最大匹配至少为 \(|B|-\kappa_-\)、\(|A|-\kappa_+\)。舍弃中间匹配以外的端口，沿同一份中间匹配的交会数满足
\[
\begin{aligned}
\ell&\ge i-1-k-\kappa_--\kappa_+-(c_--q)-(c_+-q)-(q-w)\\
&=2+r+s_0-k\ge5+\alpha+s_0-e\ge1.
\end{aligned}
\tag{14}
\]
若 \(m=0\)，正交会数已与空匹配矛盾。其余情形任一交会的两外根分别严格在 \(y\) 左、右，实际 \(B_4\) 与中间 \(R_5\) 同端矛盾。四种缺额组合与任意 \(w\) 的双 clean 加权取等类均排除。

## 4. 加权取等层的含锁排除

设 \(t=3\)、\(x<y\)，两侧缺额均正，且至少一侧有锁。每个左锁纤维取最早 owner 组成 \(A_0\)，每个右锁纤维取最晚 owner 组成 \(B_0\)。则 \(|A_0|=o,\ |B_0|=p,\ A_0\cap C=B_0\cap C'=\varnothing\)，由 §2 的同纤维连接论证。clean 侧的代表集为空。

### 4.1 全部低前驱与中间规模

收集 \(\widehat E<y\) 的全部实际末对中属于 \(W\) 的末前驱。\(C_0\subseteq V\) 或 \(T\) 中的前驱由根 \(y\) 的加强左扇与末帽排除，故全部在 \(P\)。将其分成 ordinary 集 \(R\) 与 owner 集 \(R_A\)，大小为 \(r,r_A\)。\(R\) 在 \(H_L\) 外，实际末前驱有 ambient 入红五，由 M0 无 ambient 出蓝五。

\(K_0=C\sqcup A_0\subseteq H_L\) 是实际 756。若 \(C\) 中一点有 ambient 出蓝五，与入核内红五连接时蓝桥给 \(B_6\)，红桥使其蓝五第二点成为从 \(H_L\) 启动的红六末点，故第二点在域外 \(\Omega\)。\(A_0\) 的蓝五第二点亦锁在 \(\Omega\)。因此 \(K_0\) 无 \(B_5\)，并继承 \(H_L\) 的其他禁形。由 \(|C|\ge b-\alpha\) 得 \(|K_0|\ge b-\alpha+o\)。若 \(r>\alpha-o\)，加 \(\alpha-o+1\) 个 ordinary 前驱到 \(K_0\)，得到超过 \(b\) 点且无 \(B_5\) 的域，迫一条从新增前驱 \(u\) 启动的 \(R_6\)。原低末对 \((u,e_u)\) 的帽与 weak7 迫该红六末点不晚于 \(e_u<y\)。全域各点都有 ambient 入 \(R_5\)，尾替换 \(y\) 与 \(B_3(u,e_u,y)\) 同端矛盾。故 \(r\le\alpha-o\)。若 \(a_0\in R_A\) 有原末对 \((a_0,e_0)\)，其出 \(R_6\) 终于锁 \(\omega(a_0)\)，末帽与 weak7 迫 \(\omega(a_0)\le e_0\)。因 \(e_0\in W\) 避锁，实际有 \(\omega(a_0)<e_0<y\)。

用 \(k=|\widehat E\cap(-\infty,y)|\)。\(R\cup R_A\cup(\widehat E\cap[y,\infty))\) 横截 \(W\) 内全部 \(R_6\)，故
\[
k\le e+r+r_A-h_L,\qquad r+r_A\le\alpha-o+a\le2.
\tag{15}
\]
同 §2 的补集计数及根交集上界给
\[
\begin{aligned}
i&=q+3-w+\alpha+\beta-o-p+a+d+\delta+\varepsilon,\\
i&\ge e-k+f-1,\qquad
q\ge2+w-\delta-\varepsilon-r-r_A,\\
m&=q+o+p-w\ge2-r-r_A+(o-\delta)+(p-\varepsilon)\ge0.
\end{aligned}
\tag{16}
\]
这里使用 \(f\ge h_R\) 及 (15)，没有预设 \(q\ge0\)。

### 4.2 中间匹配及严格 \(y\) 切分

由交叉锁禁形 (6)，实际 \(D_0=(D\setminus C_0)\sqcup A_0\sqcup B_0\) 同时在两核内，有 \(b+m\) 点。全部 \(R_5\) 首点在 \(U_*=(Z_-\setminus C_0)\sqcup A_0\)，末点在 \(V_*=(Z_+\setminus C_0)\sqcup B_0\)，因为 \(B_0\cap C'=A_0\cap C=\varnothing\)。取该诱导域内全部 \(R_5\) 的实际端点图，由换色容量固定 \(m\) 条中间匹配，\(m=0\) 时取空匹配。两端像 \(J_U,J_V\) 满足
\[
|U_*\setminus J_U|=c_--q-p,\qquad
|V_*\setminus J_V|=c_+-q-o .
\tag{17}
\]
容器可以含无中间供给的点，(17) 同时计入未被匹配覆盖的 owner 代表。

右修补核 \(L_+^R=C\cup Q_H\cup A_H\cup R\) 为实际 756。\(C\) 与 \(A_H\) 的潜在蓝五第二点在缺席的 \(\Omega\)，\(Q_H\subseteq T\) 与 \(R\) 无 ambient 出蓝五。核内 owner 的红六末点锁在域外 \(\Omega\)，从 \(R\) 启动的红六则由原低末帽限制末点并尾替换 \(y\) 排除。左核 \(L_-=C'\cup P_H\cup B_H\) 沿用 §2。两缺额为
\[
\kappa_+=q+\alpha-r-c_+,\qquad \kappa_-=q+\beta-c_- .
\tag{18}
\]
令 \(B=(I\cap(-\infty,y))\setminus(\widehat E\cup\Gamma)\)，\(A=(I\cap(y,\infty))\setminus\Gamma\)。两侧扩域仍无蓝五。

左扩域的红六只能终于 \(B\)，因为终于 \(B_H\) 的红六需从域外 \(\Psi\) 启动，其余旧核点非 \(T\)。末前驱若在 \(P_H\cup B\cup C_0\subseteq W\)，会触发 \(\widehat E\)。若在 \(B_H\)，其末对根由 §2 的瓶颈至少为 \(y\)，与 \(B<y\) 矛盾。故全部末对只从 \(Z_-\setminus C_0\) 指向 \(B\)。

右扩域的红六从 \(A\) 启动。若从 owner 启动，末点锁在域外 \(\Omega\)。若从 \(R\) 启动，原低末帽迫末点早于 \(y\)，新增 \(A>y\) 无点可参与，退回旧核矛盾。第二点在 \(Q_H\cup A\cup C_0\subseteq W'\) 会触发 \(\widehat F\)，在 \(A_H\) 则首对根由瓶颈至多为 \(x<y\)，在 \(R<y\) 则不合实际顺序。故全部首对只从 \(A\) 指向 \(Z_+\setminus C_0\)。容量与 König 定理给左右外匹配至少为 \(|B|-\kappa_-\)、\(|A|-\kappa_+\)。

在左外匹配加入每个 \(\omega\in\Omega\) 且 \(\omega<y\) 的实际锁边 \((a_\omega,\omega)\)，其中 \(a_\omega\in A_0\) 为其代表。将 \(a_\omega\) 的 ambient 入 \(R_5\) 与出 \(B_5(a_\omega,\omega,\ldots)\) 连接，蓝桥给 \(B_6\)，故红桥产生实际 \(R_6\) 的末对 \((a_\omega,\omega)\)。反序在右外匹配加入每个 \(\psi\in\Psi\) 且 \(\psi>y\) 的实际首对 \((\psi,b_\psi)\)，\(b_\psi\in B_0\)。新边在端口层用 owner 代表，与普通 \(D\) 点不交。新边的根若在 \(I\) 则已由 \(\Gamma\) 从 \(A,B\) 排除，若在 \(P/Q\) 则也不在 \(A,B\)。所以可以真加，随后统一舍弃 (17) 中未被共同中间匹配覆盖的端口。

记 \(o_l=|\Omega\cap(-\infty,y)|,\ p_h=|\Psi\cap(y,\infty)|,\ \chi_0=\mathbf 1[y\notin\Gamma]\)，\(j_E=|\widehat E\cap\Psi\cap(-\infty,y)|\)。因 \(\widehat E\) 避开 \(\Omega\)，严格切分计数为
\[
|A|+|B|=i-\delta-\varepsilon+\rho-k-\chi_0+j_E .
\tag{19}
\]
在同一中间匹配上的交会数满足
\[
\begin{aligned}
\ell
&\ge |A|+|B|-\kappa_--\kappa_++o_l+p_h-(c_--q-p)-(c_+-q-o)-m\\
&=|A|+|B|-q-\alpha-\beta+r+w+o_l+p_h\\
&=3-o-p+a+d+\rho+r-k-\chi_0+j_E+o_l+p_h\\
&\ge \alpha-2o+2a+(d-p)-r_A-1+o_l+p_h .
\end{aligned}
\tag{20}
\]
最后用 (15)、\(e\le6\)、\(\chi_0\le1\)，并舍去非负的 \(\rho,j_E\)。任一交会的外根严格跨 \(y\)，两帽给同端 \(B_4/R_5\) 矛盾。若 \(m=0\)，正下界已与空匹配矛盾。

### 4.3 全部锁类型

若任一侧为非 \((1,1,1)\) 的有锁类型，反序使其位于左侧，\(x<y\) 在反序下保持。

- \((2,1,1)\) 时，(20) 给 \(\ell\ge1+(d-p)-r_A+o_l+p_h\)。\(r_A\le1\)，若 \(r_A=1\) 则 \(o_l=1\)，故 \(\ell\ge1\)。
- \((1,1,2)\) 时，\(\ell\ge2+(d-p)-r_A+o_l+p_h\)。若 \(r_A=0\) 下界至少为 \(2\)。若 \(r_A>0\)，唯一锁为低锁且 \(r_A\le2\)，故 \(\ell\ge1\)。
- \((2,2,2)\) 时，\(\ell\ge1+(d-p)-r_A+o_l+p_h\)。两锁与两 owner 一一对应，所以 \(o_l\ge r_A\)，故 \(\ell\ge1\)。

余下所有有锁侧均为 \((1,1,1)\)，令左侧有锁。由 \(r\le\alpha-o=0\)，严格低根 \(x<y\) 的实际末前驱只能为唯一 owner。于是 \(r_A=o_l=1\)。

若右侧也为 \((1,1,1)\)，右代表核 \(K_0^-=C'\sqcup B_0\) 由反序容量为实际 756 且至少有 \(b-1+1\) 点，故恰满 \(b\)。设有一条高首对 \((f_v,v)\)，\(f_v>x\)，其第二点 \(v\in W'\) 为 ordinary。根 \(x\) 的加强右扇与首帽排除 \(S\cup C_0\)，所以 \(v\in Q\) 且在 \(H_R\) 外。\(v\) 有 ambient 出红五，由 M0 无 ambient 入蓝五。\(K_0^-\cup\{v\}\) 无 \(B_5\)，因为旧核潜在蓝五的倒数第二点锁在域外 \(\Psi\)，而 \(v\in Q\) 也不在 \(\Psi\)。容量迫一条 \(R_6\) 终于 \(v\)，旧核终点若为 \(B_H\) 则需域外 \(\Psi\) 供给。首帽与 weak7 迫该红六首点不早于 \(f_v>x\)，全域点有 ambient 出红五，可头替换 \(x\)，与 \(B_3(x,f_v,v)\) 同端矛盾。故高首对没有 ordinary 第二点。根 \(y\) 的实际第二点必为唯一右 owner。其右锁 \(\psi>y\)，因为首帽与 weak7 排除 \(\psi<y\)，而 \(y\in W'\) 排除等号。因此 \(p_h=1\)，代入 (20) 得 \(\ell\ge1\)。

若右侧 clean，收集全部 \(\widehat F>x\) 的实际首对中属于 \(W'\) 的第二点 \(Q_0\)。根 \(x\) 的加强扇与首帽排除 \(S\cup C_0\)，故 \(Q_0\subseteq Q\)，其大小 \(s_0\ge1\)。将 \(\beta+1\) 个这种第二点加到 \(C'\)，由容量、首帽和头替换 \(x\) 得 \(s_0\le\beta\)，论证与 §3 的反序压缩相同。修补左核 \(\widetilde L_-=C'\cup P\cup Q_0\)，其每点无 ambient 入蓝五，且终于 \(Q_0\) 的 \(R_6\) 由头替换 \(x\) 排除，故为实际 756。缺额改为 \(\kappa_-=q+\beta-s_0-c_-\)。加入 \(B\) 后，新增 \(I\) 点均有 ambient 出红五，头替换仍排除终于 \(Q_0\) 的红六。若 \(Q_0\) 作末前驱，由 \(Q_0\subseteq T\) 及根早于 \(y\)，根 \(y\) 的加强左扇与末帽矛盾。故左外图仍由 \(Z_-\setminus C_0\) 指向 \(B\)，(20) 的下界净增 \(s_0\)。代入左 \((1,1,1)\) 及 \(r_A=o_l=1\)，得 \(\ell\ge s_0\ge1\)。反序含另一 clean 朝向。含锁类全部排除。

### 4.4 加权取等层的覆盖

从旧式 \(n+w\le3b+3\) 进入等号层后，双向实际归一化给 \(\alpha,\beta\le2\) 及 \(h_L,h_R\le5\)。缺额零由 §2 的 onefull 推论排除。两侧正缺额且 \(x\ge y\) 由 §2 排除。\(x<y\) 时，双 clean 由 §3 排除，至少一侧有锁由 §4.3 排除。所有加权取等配置均不可能。由整数性得到 (1)。其中 \(w\) 在母体的实际 \(D\) 中计算，归一化不改 \(D\)。上述证明直接排除旧上界的等号层。

## 5. 下一人口临界层的双 clean 重合端口排除

**重合端口定理。** 设 \(n=3b+2\)，\(w=0\)，双侧 clean，\(H_L=X\setminus S,\ H_R=X\setminus T\)，且 \(\alpha,\beta\in\{1,2\}\)。用 (5) 的核内角色定义
\[
G=Z_-\cap Z_+,\qquad g=|G| .
\tag{21}
\]
则 \(g=0\)。对 \(G\) 的定义只要求在 \(H_L\) 有入红五且在 \(H_R\) 有出红五，这两条路径可以用 \(D\) 外的点。

### 5.1 实际端口与增广根扇

反设 \(g\ge1\)。\(G\) 的点有 \(H_L\) 内入红五，且其首点在 \(X\setminus S\)。若 \(G\) 中该点有 ambient 出蓝五，接入红五时蓝桥给 \(B_6\)，红桥给从 \(H_L\) 启动的 \(R_6\)，两者皆不可能。故 \(G\) 点无 ambient 出蓝五。反序由 \(H_R\) 内出红五知其无 ambient 入蓝五。取
\[
W_g=S\cup G,\qquad W'_g=T\cup G .
\tag{22}
\]
\(W_g\) 无蓝五末点，\(W'_g\) 无蓝五源。\(W_g\) 中有 ambient 入红五的点均无 ambient 出蓝五，在 \(S\) 中由 clean M0，在 \(G\) 中由上述证明。反序 \(W'_g\) 中有 ambient 出红五的点均无 ambient 入蓝五。这兑现两侧完整端口。

末点 \(t_0\) 在 \(S\cup C'\) 的任何 \(B_4\) 可向右延长为 \(B_5\)，保其首相邻对。取 \(t_0\) 的出 \(R_6\)（\(t_0\in S\)），或 \(H_R\) 内出 \(R_5\)（\(t_0\in C'\)），用其第二点 \(t_+\) 作新点。设 \(z\) 为原蓝四倒数第二点。若 \(\chi(z,t_0,t_+)=R\)，分别给 \(R_7\) 或终于 \(H_R\) 的 \(R_6\)，均矛盾。故此桥为蓝。反序首点在 \(T\cup C\) 的蓝四可向左延长并保末相邻对。因 \(G\subseteq C'\cap C\)，上述延长与端口排除 \(W_g\) 内的红五末点与蓝四源交会，反序亦然。故两基底为实际 \(D_7\)。

令 \(\widehat E_g,\widehat F_g\) 依 (5) 的全部 ambient 相邻对定义，将其中基底分别替换为 \(W_g,W'_g\)。因 \(G\subseteq D\)，两根族仍在 \(I\)。此节用 \(e=|\widehat E_g|,\ f=|\widehat F_g|,\ x=\min\widehat E_g,\ y=\max\widehat F_g\)。容量横截给 \(e\ge2+\alpha+g,\ f\ge2+\beta+g\)。

取 \(e_0\in\widehat E_g\) 的实际末对 \((u,e_0)\)，\(u\in S\cup G\)。\(u\) 是实际末前驱，有 ambient 入红五，故由 clean 端口或 \(G\) 的核内入红五论证，无 ambient 出蓝五。设 \(e_0<z<t_0\) 且 \(t_0\in S\cup C'\)。若 \(\chi(e_0,z,t_0)=B\)，末帽给 \(B_4(u,e_0,z,t_0)\)。取上述出红六或核内出红五的第二点 \(t_+\)，蓝桥给 \(B_5(u,e_0,z,t_0,t_+)\)，与 \(u\) 无 ambient 出蓝五矛盾。因此 \(\chi(e_0,z,t_0)=R\)。反序 \(\widehat F_g\) 的加强左扇端域为 \(T\cup C\)，中点均可任取 ambient 点。特别地两根族各自为红 clique，所以 \(e,f\le6\)。

### 5.2 同一实际中间匹配排除非交错根序

置 \(m=\max(q-g,0),\ \mu=\min(q-g,0)\)，这里 \(q=|D|-b\)。在实际 \(D\setminus G\) 内取全部实际 \(R_5\) 的端点图，换色容量与 König 定理给一份 \(m\) 条匹配，\(m=0\) 时取空匹配。首末像分别包含于 \(Z_-\setminus G,\ Z_+\setminus G\)。

初始实际 756 核 \(C'\cup P,\ C\cup Q\) 及其缺额沿用双 clean 情形，缺额为 \(q+\beta-c_-,q+\alpha-c_+\)。任取 ambient 间隙 \(\tau\)，令
\[
B=(I\cap(-\infty,\tau))\setminus\widehat E_g,\qquad
A=(I\cap(\tau,\infty))\setminus\widehat F_g,\qquad
g_{\rm cut}(\tau)=|\widehat E_g\cap(-\infty,\tau)|+|\widehat F_g\cap(\tau,\infty)| .
\tag{23}
\]
两扩域无 \(B_5\)。左扩域的红六只能终于 \(B\)。若末前驱在 \(P\cup B\cup G\subseteq W_g\)，则末点触发 \(\widehat E_g\)，故外末对只从 \(Z_-\setminus G\) 指向 \(B\)。反序右外首对只从 \(A\) 指向 \(Z_+\setminus G\)。实际容量给左右匹配至少为根数减对应缺额。再舍去未被中间匹配覆盖的普通端口，分别至多 \(c_--g-m,c_+-g-m\)。由于 \(i=q+2+\alpha+\beta\)，在同一中间匹配上的交会数满足
\[
\begin{aligned}
\ell
&\ge i-g_{\rm cut}(\tau)-(q+\beta-c_-)-(q+\alpha-c_+)\\
&\qquad -(c_--g-m)-(c_+-g-m)-m
 =2+g-\mu-g_{\rm cut}(\tau).
\end{aligned}
\tag{24}
\]
正交会由两帽给同端 \(B_4/R_5\) 矛盾。若 \(x>y\)，取两根之间的间隙给 \(g_{\rm cut}=0\)，若 \(x=y\)，取紧邻该根一侧的间隙给 \(g_{\rm cut}=1\)。故只能 \(x<y\)。

### 5.3 全部实际前驱压缩及严格 \(y\) 切分

收集所有 \(\widehat E_g<y\) 的实际末对中属于 \(W_g\) 的前驱 \(P_0\)，以及所有 \(\widehat F_g>x\) 的实际首对中属于 \(W'_g\) 的第二点 \(Q_0\)，大小分别为 \(r,s_0\)。根 \(y\) 的加强左扇端域为 \(T\cup C\)，与末帽一起排除 \(T\cup G\) 的低前驱，故 \(P_0\subseteq P\)。反序根 \(x\) 的加强右扇排除 \(S\cup G\) 的高后继，故 \(Q_0\subseteq Q\)。两集均非空。§3 的压缩仍适用。加 \(P_0\) 到 \(C\) 或加 \(Q_0\) 到 \(C'\) 的论证只需要相应的 ambient 红五身份、干净的蓝五身份与完整尾或头替换。后两项已由 §5.1 的增强基底兑现。具体地，低前驱 \(p_0\) 启动的实际红六若终于对应根 \(e_0\) 之后，与低末帽同端矛盾，若末点不晚于 \(e_0<y\)，尾替换 \(y\) 后与同端 \(B_3(p_0,e_0,y)\) 矛盾。反序高后继 \(q_0\) 使用首帽及头替换 \(x\)。由容量得 \(1\le r\le\alpha,\ 1\le s_0\le\beta\)。

令 \(k=|\widehat E_g\cap(-\infty,y)|\)。\(P_0\cup(\widehat E_g\cap[y,\infty))\) 横截 \(W_g\) 内的全部红六，且 \(\widehat E_g\cap[y,\infty)\) 与 \(\widehat F_g\) 至多交于 \(y\)。于是
\[
k\le e+r-2-\alpha-g,\qquad (e-k)+f\le i+1,\qquad
q\ge1+2g-r\ge g .
\tag{25}
\]
最后用 \(g\ge1\) 且 \(r\le2\)。此时先前固定的同一中间匹配有 \(m=q-g\) 条，未被覆盖的普通端口恰为 \(c_\pm-q\)。

实际修补核 \(L_-=Z_-\sqcup P\sqcup Q_0\)、\(L_+=Z_+\sqcup Q\sqcup P_0\) 沿 §3 的头尾替换证明为 756，缺额仍为 (13)。严格在 \(y\) 切分，取 \(B=(I\cap(-\infty,y))\setminus\widehat E_g,\ A=I\cap(y,\infty)\)，有 \(|A|+|B|=i-1-k\)。

左扩域中，终于 \(Q_0\) 的红六由首帽、头替换 \(x\) 排除。其余红六只能终于 \(B\)。末前驱若在 \(Q_0\subseteq T\)，由根 \(y\) 的加强左扇与末帽矛盾，若在 \(P\cup B\cup G\) 则触发 \(\widehat E_g\)。右扩域中，从 \(P_0\) 启动的红六由末帽限制在 \(y\) 前，不能用新增 \(A\)，退回旧修补核矛盾。其余红六只能从 \(A\) 启动。第二点若在 \(P_0<y\) 则不合序，若在 \(Q\cup A\cup G\) 则触发 \(\widehat F_g\)。故左右两图只用 \(Z_-\setminus G\) 和 \(Z_+\setminus G\) 作普通端口。由容量取匹配后沿同一中间匹配，得到
\[
\begin{aligned}
\ell
&\ge i-1-k-\kappa_--\kappa_+-(c_--q)-(c_+-q)-(q-g)\\
&=1+g+r+s_0-k\ge3+2g+\alpha+s_0-e\ge1 .
\end{aligned}
\tag{26}
\]
最后用 \(g,\alpha,s_0\ge1,\ e\le6\)。空匹配时正交会下界已矛盾，非空时得到两外根严格跨 \(y\) 的实际链，其蓝四和红五同端，违反 weak7。故 \(G\ne\varnothing\) 的双 clean 类全排。

## 6. 参数结论、数值与剩余入口

由 (1)，下一人口临界 \(n=3b+2\) 强制 \(w=0\)。该层的全部 \(w=1\) 配置已由加权定理排除。完整双向 M0 中，全部 onefull 与 \(x\ge y\) 的配置由 §2 排除。双 clean 的极端缺额 \(0/3\) 由跨角色根序稿 §4 排除，§5 排除了双缺额 \(1/2\) 时 \(G\ne\varnothing\) 的全部配置。

该人口层仍有两类待覆盖。

- 双 clean、\(\alpha,\beta\in\{1,2\}\)、\(G=\varnothing\)、严格交错 \(x<y\)。剩余的低、高实际供应须在同一中间匹配上兼容，端口必须兑现相应实际核内红五身份。
- \(w=0\)、至少一侧有锁、两侧正缺额且严格交错 \(x<y\)。这里 canonical 缺额可达 \(3\)，§4 的四种有锁类型仅穷尽加权取等层。该层需要新的实际修补核与完整端点容器论证。

以 \(Q_{\rm cap}=N_{\rm sig}(7,6,7),\ F_{\rm cap}=N_{\rm sig}(7,7,7),\ C_{\rm cap}=N_{\rm sig}(7,6,6)\) 表示最大允许人口。旧精确归约给 \(F_{\rm cap}=Q_{\rm cap}+1\)，竞争容量桥 \(Q_{\rm cap}\le C_{\rm cap}+b+2\) 仍开放。[R20 精确归约](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>)

参数结论为
\[
Q_{\rm cap}\le3b+2,\qquad F_{\rm cap}\le3b+3,\qquad
w\ge1\ \Longrightarrow\ n\le3b+1\quad\text{对 767 配置}.
\tag{27}
\]
采用既有工作输入 \(b=25\)，全模型加权式给 \(n+w\le77\)，正 through 的 767 子类给 \(n\le76\)。无条件人口工作上界仍为 767 的 \(77\) 与 777 的 \(78\)，尚未推出全局 \(76/77\)。本轮加权容量下降 \(1\)，无条件人口上界下降 \(0\)。[既有研究综述与数值来源](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_SYNTHESIS_N7_20261103.md>)

## 7. 保证与文档回执

全部新增工作证明为 **unreviewed / unaccepted**。主会话的推导、交叉核对与本稿转写均属于同会话工作。文档回执的 `PASS_DOCUMENT_ONLY` 只表示转写与文件一致性检查通过。旧依赖沿用原保证层级。此次只作本地文档转写与核对，未调用外部 Claude 或外传研究材料，未运行科研代码、枚举、SAT、solver 或 proof 重放。
