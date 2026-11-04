# N7 双 clean 临界类的增广中间域排除

2026-11-03。本文新增工作证明为 **unreviewed / unaccepted**。数学由主会话定稿，推导和交叉核对属于同会话工作。指定 native gpt-6.1-sol/high 执行者负责转写与文档核对。

**工作定理。** 设 \(X\) 是有序 rank-3 signotope 的 767 母体，\(b\) 是 756 及换色 756 的共同有效容量。在 \(n=|X|=3b+2\) 层，设完整双向 M0 接口为双 clean，即 \(H_L=X\setminus S,\ H_R=X\setminus T\)。若 canonical 缺额 \(\alpha=2b-|H_L|\)、\(\beta=2b-|H_R|\) 均在 \(\{1,2\}\)，则严格交错 \(x<y\) 不可能。其中 \(S,T\) 是 ambient 红六的源、末点集，\(x,y\) 为下文定义的极端根。既有加权工作界给 \(w=0\)。本证明对 \(G=Z_-\cap Z_+\) 无附加要求。

## 1. 模型与既有接口

\(R_j,B_j\) 是红、蓝 \(j\) 点路径，路径由实际有序点上连续三元组的颜色确定，并对子序列遗传。\(\chi\) 为三元组颜色。四点 packet 按三元组字典序排列，颜色至多改变一次。weak7 禁止一红一蓝两条路径有相同的实际首末点且长度和至少为 \(9\)。767 禁 \(R_7,B_6,\mathrm{weak7}\)，756 禁 \(R_6,B_5,\mathrm{weak7}\)，换色 756 禁 \(R_5,B_6,\mathrm{weak7}\)。ambient 指 \(X\)，带域的端点角色只按该实际子域中的路径计算。

- 加权界 \(n+w\le3b+2\)、完整双向 M0、两帽与根扇、修补核及重合端口情形见 §1–3、§5–6。[共同中间匹配与加权界稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMMON_MIDDLE_COMPATIBILITY_AND_WEIGHTED_BOUND_20261103.md>)
- \(n=3b+2\) 下双 clean 的极端缺额排除、前驱压缩及严格切分见 §4，onefull 见 §5。[跨角色根序稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_CROSS_ROLE_ROOT_ORDER_AND_SEPARATED_CLASS_EXCLUSION_20261103.md>)
- 实际换核和完整 ambient 根接口见 §2–3。[锁纤维归一化稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCK_FIBER_NORMALIZATION_AND_DOUBLE_OMEGA_EXCLUSION_20261102.md>)
- 全量词的实际端点对图、顶点覆盖删点及同端 weak7 矛盾见 §2。[实际端点对 Hall 稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_ENDPOINT_PAIR_HALL_MISALIGNMENT_EXCLUSION_20261102.md>)

令

\[
\begin{aligned}
S&=\operatorname{Src}_{R_6}(X),& T&=\operatorname{End}_{R_6}(X),& I&=S\cap T,\\
P&=S\setminus T,& Q&=T\setminus S,& D&=X\setminus(S\cup T),\\
U&=\operatorname{Src}_{R_5}(D),& V&=\operatorname{End}_{R_5}(D),& w&=|U\cap V|,\\
C&=\operatorname{End}_{R_5}(H_L),& C'&=\operatorname{Src}_{R_5}(H_R),\\
Z_+&=C\cap D,& Z_-&=C'\cap D,& c_\pm&=|Z_\pm|.
\end{aligned}
\tag{1}
\]

由既有加权界及 \(n=3b+2\) 得 \(w=0\)。记 \(|D|=b+q,\ i=|I|\)。完整双 clean 给 \(W=S,\ W'=T\)，并且

\[
|P|=b-q-\beta,\qquad |Q|=b-q-\alpha,\qquad i=q+2+\alpha+\beta.
\tag{2}
\]

\(\widehat E\) 收集全部实际 ambient \(R_6\) 末相邻对 \((u,h)\) 中的根 \(h\)，其中 \(u,h\in W\)。\(\widehat F\) 收集全部实际 ambient \(R_6\) 首相邻对 \((h,v)\) 中的根 \(h\)，其中 \(h,v\in W'\)。定义 \(e=|\widehat E|,\ f=|\widehat F|,\ x=\min\widehat E,\ y=\max\widehat F\)。两族均在 \(I\)，且 \(2+\alpha\le e\le6,\ 2+\beta\le f\le6\)。实际末对 \((u,h)\) 的末帽给 \(\chi(u,h,z)=B\) 对所有 \(z>h\)，实际首对 \((h,v)\) 的首帽给 \(\chi(z,h,v)=B\) 对所有 \(z<h\)。标准根扇的端域分别为 \(S\cup U\) 与 \(T\cup V\)，clean 加强扇可分别用 \(S\cup C'\) 与 \(T\cup C\)。下文用到的左扇实例仅要求左端 \(v\in T\) 且 \(v<z<y\)，这时 \(\chi(v,z,y)=R\)。

令 \(P_0\) 收集 \(\widehat E<y\) 的全部实际末对中在 \(W\) 的末前驱，\(Q_0\) 收集 \(\widehat F>x\) 的全部实际首对中在 \(W'\) 的第二点。记 \(r=|P_0|,\ s=|Q_0|,\ k=|\widehat E\cap(-\infty,y)|\)。低末帽与根 \(y\) 的左扇排除 \(T\) 内低前驱，反序排除 \(S\) 内高后继。两集由 \(x<y\) 非空。前驱与后继压缩及 \(S\) 中红六的实际横截给

\[
P_0\subseteq P,\qquad Q_0\subseteq Q,\qquad
1\le r\le\alpha,\qquad 1\le s\le\beta,\qquad
k\le e+r-2-\alpha.
\tag{3}
\]

末式使用横截 \(P_0\cup(\widehat E\cap[y,\infty))\)，其大小至少 \(|S|-b=2+\alpha\)。\(\widehat E\cap[y,\infty)\) 与 \(\widehat F\) 至多交于 \(y\)，所以 \((e-k)+f\le i+1\)。由 (2)、(3) 及 \(f\ge2+\beta\) 得 \(q\ge1-r\)。

既有实际修补核及缺额为

\[
\begin{aligned}
L_+&=Z_+\sqcup Q\sqcup P_0,& \kappa_+&=b-|L_+|=q+\alpha-r-c_+\ge0,\\
L_-&=Z_-\sqcup P\sqcup Q_0,& \kappa_-&=b-|L_-|=q+\beta-s-c_-\ge0.
\end{aligned}
\tag{4}
\]

两核均为 756。\(L_+\) 每点有 ambient 入 \(R_5\) 且无 ambient 出 \(B_5\)，\(L_-\) 每点有 ambient 出 \(R_5\) 且无 ambient 入 \(B_5\)。此外 \(q\ge0\)。若 \(r=1\)，这来自 \(q\ge1-r\)。若 \(r=2\)，则 \(\alpha=2\)，由 \(\kappa_+\ge0\) 得 \(q\ge c_+\ge0\)。

下文反复使用既有头尾替换。若一条实际 \(R_6\) 的第四点有 ambient 入 \(R_5\)，且第五点早于 \(\widehat F\) 中的根，则可用该根替换末点。反序头替换要求第三点有 ambient 出 \(R_5\)，且用于替换的 \(\widehat E\) 根早于第二点。对每个 \(p_i\in P_0\)，选一条实际低末对 \((p_i,e_i)\) 且 \(e_i<y\)。任何从 \(p_i\) 启动的 \(R_6\) 末点至多为 \(e_i\)，否则末帽给同端 \(B_3/R_6\)，违反 weak7。因此，若路径所在域的所有点都有 ambient 入 \(R_5\)，其第五点早于 \(y\)，可用 \(y\) 尾替换，再由同一低末帽得同端 \(B_3(p_i,e_i,y)/R_6\)。这排除了该域内从 \(p_i\) 启动的 \(R_6\)。

## 2. 实际中间增广与右核同时饱和

从根 \(x\) 选一条实际 \(R_6\) 末对 \((p,x)\)，其中 \(p\in W\)，故 \(p\in P_0\)。从根 \(y\) 选一条实际 \(R_6\) 首对 \((y,t)\)，其中 \(t\in W'\)，故 \(t\in Q_0\)。由 (4)，\(t\) 无 ambient 入 \(B_5\)。定义

\[
M=D\cup\{p\}\subseteq H_R,\qquad
J=\operatorname{End}_{R_5}(M)\setminus Z_+,\qquad j=|J|.
\tag{5}
\]

### 2.1 新红五末点的蓝五限制

首先 \(p\) 不能终止 \(M\) 中的 \(R_5\)。若有这样的路径，记其末前驱为 \(a_4\in D\)。如果 \(\chi(a_4,p,x)=R\)，在该红五末尾接 \(x\) 得从 \(D\) 启动的 \(R_6\)，违 \(D\cap S=\varnothing\)。所以该桥为蓝。再由两帽得 \(\chi(p,x,y)=B\) 与 \(\chi(x,y,t)=B\)，于是 \(B_5(a_4,p,x,y,t)\) 违反 \(t\) 无 ambient 入蓝五。因此 \(J\subseteq D\setminus Z_+\)。

任取 \(z\in J\)，固定 \(M\) 内一条终于 \(z\) 的实际红五。如果红五源在 \(D\)，设末前驱为 \(a\)。若有 ambient \(B_5\) 从 \(z\) 启动且第二点为 \(v\)，则 \(\chi(a,z,v)=B\) 给 \(B_6\)，而 \(\chi(a,z,v)=R\) 给从 \(D\) 启动的 \(R_6\)，均矛盾。

余下固定红五为 \(R_5(p,a_1,a_2,a_3,z)\)。若 \(z\) 无 ambient 出 \(B_5\)，蓝五限制已经成立。否则任取一条从 \(z\) 出发、第二点为 \(v\) 的 ambient \(B_5\)。桥 \(\chi(a_3,z,v)\) 若为蓝，得到 \(B_6\)。故桥为红，得到 \(R_6(p,a_1,a_2,a_3,z,v)\) 且 \(v\in T\)。末对 \((p,x)\) 的帽与 weak7 强迫 \(v\le x\)，因为 \(v>x\) 会给同端 \(B_3(p,x,v)\)。所以 \(p<z<v\le x\)。

令 \(d_0\) 为所选实际末对 \((p,x)\) 所在红六中紧邻 \(p\) 的前一点。若 \(\chi(d_0,p,z)=R\)，该红六的前五点接 \(z\) 得终于 \(D\) 的 \(R_6\)，违 \(D\cap T=\varnothing\)。故 \(\chi(d_0,p,z)=B\)，原红六给 \(\chi(d_0,p,x)=R\)。packet \((d_0,p,z,x)\) 首色蓝、第二色红，迫 \(\chi(p,z,x)=R\)。packet \((p,z,x,y)\) 首色红、第三色 \(\chi(p,x,y)=B\)，迫 \(\chi(z,x,y)=B\)。若 \(\chi(a_3,z,x)=B\)，再用 \(\chi(x,y,t)=B\) 得 \(B_5(a_3,z,x,y,t)\)，违反 \(t\) 无 ambient 入蓝五。故 \(\chi(a_3,z,x)=R\)，从而有

\[
R_6(p,a_1,a_2,a_3,z,x).
\tag{6}
\]

对任一从 \(z\) 启动的 ambient \(B_5\)，上面的桥与帽均给其第二点 \(v\in T\) 且 \(v\le x\)。若 \(v<x\)，根 \(y\) 的标准左扇给 \(\chi(v,x,y)=R\)。在 packet \((p,v,x,y)\) 中，第三色 \(\chi(p,x,y)=B\)，第四色 \(\chi(v,x,y)=R\)，因此首色 \(\chi(p,v,x)=B\)。于是 \(B_3(p,v,x)\) 与 (6) 同端，违反 weak7。结论是，\(J\) 中每一点有 ambient 入 \(R_5\)，且其从自身启动的任何 ambient \(B_5\) 的第二点都必须为 \(x\)。至此只用实际路径与颜色约束。

### 2.2 整体增广与同一份中间匹配

同时加入全部 \(J\)，令 \(L_+^*=L_+\sqcup J\)。因为 \(x\in I\) 而 \(L_+\cup J\subseteq D\cup Q\cup P_0\)，点 \(x\) 缺席。\(L_+\) 的点无 ambient 出 \(B_5\)，以 \(J\) 中的点为源的蓝五须有第二点 \(x\)，故 \(L_+^*\) 无 \(B_5\)。每点均有 ambient 入红五。若有 \(R_6\)，其源必在 \(P_0\)，因为其余点都不在 \(S\)。§1 的低帽与尾替换排除这样的红六。于是 \(L_+^*\) 为实际 756，故

\[
j\le \kappa_+=q+\alpha-r-c_+.
\tag{7}
\]

另一方面，\(M\) 有 \(b+q+1\) 个实际点。全部 \(R_5\) 源在 \(Z_-\cup\{p\}\)，因为 \(M\subseteq H_R\) 且 \(M\setminus\{p\}=D\)。全部末点在 \(Z_+\cup J\)。以 \(M\) 内全部实际 \(R_5\) 的首末点建二部图。若最大匹配不足 \(q+1\)，König 定理给至多 \(q\) 个角色顶点的覆盖。删去覆盖对应的实际点，仍余超过 \(b\) 点，且无 \(R_5\)，继承 \(B_6\) 与 weak7 禁形，违反换色 756 容量。源和末点的角色副本可以对应同一实际点，例如 \(J\) 与 \(Z_-\) 可重合。此时实际删点数只会减少。

匹配的末点数给 \(q+1\le c_++j\)，与 (7) 合并得到

\[
q+1\le c_++j\le q+\alpha-r .
\tag{8}
\]

由于 \(1\le r\le\alpha\le2\)，这已经排除 \(\alpha=1\) 或 \(r=2\)。余下必有

\[
\alpha=2,\qquad r=1,\qquad j=\kappa_+,\qquad
|L_+^*|=b,\qquad c_++j=q+1 .
\tag{9}
\]

固定 \(M\) 内恰 \(q+1\) 条实际 \(R_5\) 构成的一份端点匹配 \(\mathcal M\)。其末像是整个 \(Z_+\cup J\)，首像包含于 \(Z_-\cup\{p\}\)。令 \(\varepsilon\) 在 \(p\) 为已匹配首点时取 \(1\)，否则取 \(0\)。未被覆盖的旧左端口恰有

\[
c_--(q+1-\varepsilon)\ge0
\tag{10}
\]

个。

## 3. 两侧实际相邻对在增广中间匹配上的交会

严格在 \(y\) 切分。令

\[
B=(I\cap(-\infty,y))\setminus\widehat E,\qquad
A=I\cap(y,\infty),\qquad |A|+|B|=i-1-k .
\tag{11}
\]

此处 \(A,B\) 为实际根集合，式 \(\chi(\cdot)=B\) 或路径符号 \(B_j\) 中的 \(B\) 仍表示蓝色。

**左扩域 \(L_-\cup B\)。** 原核和新增 \(B\subseteq I\subseteq S\) 各点均无 ambient 入 \(B_5\)，且均有 ambient 出 \(R_5\)。若实际红六终于 \(t_0\in Q_0\)，取对应的高首对 \((f_0,t_0)\) 且 \(f_0>x\)。首帽与 weak7 迫红六首点不早于 \(f_0\)，故第二点晚于 \(x\)。用 \(x\) 头替换后，与首帽给的 \(B_3(x,f_0,t_0)\) 同端，矛盾。原核的其余点不在 \(T\)，因此域内红六只能终于 \(B\)。末前驱若在 \(P\cup B\subseteq W\)，末点会触发 \(\widehat E\)。若末前驱在 \(Q_0\subseteq T\)，则它和末点均早于 \(y\)，根 \(y\) 的标准左扇与该实际末对的末帽冲突。因此全部实际左末对属于 \(Z_-\times B\)。以这些相邻对建图，匹配至少为 \(|B|-\kappa_-\)，否则由 König 定理删除少于 \(|B|-\kappa_-\) 个实际点即可击中全部红六，并留下超过 \(b\) 点的 756。

**右扩域 \(L_+^*\cup A\)。** 点 \(x\) 仍缺席，因为 \(x<y\)。旧核点及新增 \(A\subseteq I\subseteq T\) 无 ambient 出 \(B_5\)，\(J\) 中的点若启动蓝五则第二点只能为 \(x\)，故右扩域无 \(B_5\)。全域有 ambient 入 \(R_5\) 身份。§1 的低帽与尾替换排除从 \(P_0\) 启动的红六，其余可能的源全在 \(A\)。源在 \(A\) 时，第二点不能在 \(P_0<y\)，也不能在 \(Q\cup A\subseteq W'\)，后者将触发 \(\widehat F\) 中晚于 \(y\) 的根。因此全部实际右首对属于 \(A\times(Z_+\cup J)\)。同一容量论证给匹配至少为 \(|A|\)，因为 \(L_+^*\) 已满 \(b\)。这里允许 \(J\) 中满足首对顺序的新高端口，且它们都在 \(\mathcal M\) 的末像内。

沿固定的 \(\mathcal M\) 运送两侧匹配。左侧至多舍弃 \(c_--(q+1-\varepsilon)\) 条使用未覆盖 \(Z_-\) 端口的边。若 \(\varepsilon=1\)，加入原先选定的实际左末对 \((p,x)\)。它与保留的左边无角色冲突，因为 \(p\notin Z_-\)、\(x\notin B\)，且根 \(x<y\)。右侧的端口全被 \(\mathcal M\) 覆盖。保留的全部左根严格早于 \(y\)，全部右根严格晚于 \(y\)。由于各侧匹配在相应端口角色上无重复，在同一 \(\mathcal M\) 上得到的交会条数 \(\ell\) 满足

\[
\begin{aligned}
\ell
&\ge (|B|-\kappa_-)-[c_--(q+1-\varepsilon)]
     +\varepsilon+|A|-(q+1)\\
&=|A|+|B|-\kappa_--c_-\\
&=1+\alpha+s-k .
\end{aligned}
\tag{12}
\]

最后一步代入 (2)、(4)、(11)。由 (3)、(9) 得 \(k\le e-3\le3\)，所以 (12) 至少为 \(s\ge1\)。

取一个交会。它提供 \(\mathcal M\) 内的实际 \(R_5(u\to v)\)、实际左末对 \((u,r_0)\) 和实际右首对 \((s_0,v)\)，其中 \(u<r_0<y<s_0<v\)。末帽给 \(\chi(u,r_0,s_0)=B\)，首帽给 \(\chi(r_0,s_0,v)=B\)，得到 \(B_4(u,r_0,s_0,v)\)。蓝四与中间红五同实际首末点 \(u,v\)，总长度为 \(9\)，违反 weak7。工作定理得证。

固定在 \(D\) 中的旧中间匹配可能遗漏右扩域可用的高端口。这里把实际中间域增为 \(D\cup\{p\}\)，再把其中新增的全部红五末点加入右修补核。容量使右核恰满，也使新增末端口全由同一份实际中间匹配覆盖。新增首端口 \(p\) 自带实际左末对 \((p,x)\)。因此在 (12) 中，左右供给都由同一份实际路径匹配兑现。整个交会论证只使用实际相邻对、König 覆盖和两帽，既未假设任意端点可交换或具有 Ferrers 性质，也未将抽象 Hall 错位当作实际反例。

## 4. 参数结论、数值与余下入口

结合既有双 clean 缺额 \(0/3\) 排除、非交错根序及 onefull 排除，本文关闭 \(n=3b+2\) 的全部双 clean 配置。既有重合端口结论已覆盖 \(G\ne\varnothing\) 的相应情形，本定理直接覆盖同一假设下的全部 \(G\)。结合既有加权工作界，双 clean 子类的参数上界为 \(n\le3b+1\)。

在全模型中，人口临界层 \(n=3b+2\) 仍有 \(w=0\)、至少一侧有锁、两侧正缺额且 \(x<y\) 的配置待排除。用 \(Q_{\rm cap}=N_{\rm sig}(7,6,7)\)、\(F_{\rm cap}=N_{\rm sig}(7,7,7)\) 表示最大允许人口，沿用既有精确归约及工作界，

\[
Q_{\rm cap}\le3b+2,\qquad F_{\rm cap}=Q_{\rm cap}+1\le3b+3 .
\tag{13}
\]

采用既有工作输入 \(b=25\)，双 clean 的 767 子类至多 \(76\) 点。全模型的 767、777 人口工作上界分别为 \(77\)、\(78\)。全局 \(76/77\) 尚待证明。

后续可考察锁纤维的结构边界，寻找既能增广实际中间域、又能保留锁端口限制的实际修补核。

本文所有新增结论均为 **unreviewed / unaccepted**。转写和交叉核对均属同会话工作，旧依赖沿用原保证层级。本轮只转写、核对本地文档，未调用外部 Claude 或外传材料，未执行科研代码、枚举、SAT、solver 或 proof 重放。
