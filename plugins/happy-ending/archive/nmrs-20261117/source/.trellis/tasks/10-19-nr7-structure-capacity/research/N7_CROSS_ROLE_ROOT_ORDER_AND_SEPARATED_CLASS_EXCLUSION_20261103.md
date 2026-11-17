# N7 跨角色根序与非交错临界类全排

2026-11-03。本文新增工作定理均为 **unreviewed / unaccepted**。数学由主会话定稿，同会话转写与检查只核对文件一致性。本文沿用既有工作界与容量输入，新增全局数值下降为零。

## 1. 模型与完整双向 M0 接口

母体 \(X\) 是有序 rank-3 signotope。对 \(a<b<c<d\)，四点 packet \(abc,abd,acd,bcd\) 至多换色一次。单色路径按实际点计长，要求所有连续三元组同色，且对子序列遗传。\(R_k,B_k\) 分别表示红、蓝 \(k\) 点路径。weak7 指同一对实际首末点上有一红一蓝两条路径，长度和至少为 \(9\)，内部可以共享。767 禁 \(R_7,B_6,\mathrm{weak7}\)，756 禁 \(R_6,B_5,\mathrm{weak7}\)，换色后的 756 禁 \(R_5,B_6,\mathrm{weak7}\)。\(b\) 是两种 756 共用的有效人口上界，\(N_{\rm sig}\) 记相应模型的最大允许人口。

在同一 \(X\) 中计算全部 ambient 角色，带域的 \(\operatorname{Src}\) 和 \(\operatorname{End}\) 在所标域中计算。

\[
\begin{aligned}
S&=\operatorname{Src}_{R_6}(X),&T&=\operatorname{End}_{R_6}(X),& I&=S\cap T,\\
P&=S\setminus T,& Q&=T\setminus S,& D&=X\setminus(S\cup T),\\
U&=\operatorname{Src}_{R_5}(D),& V&=\operatorname{End}_{R_5}(D),&
C_0&=U\cap V,\quad w=|C_0|.
\end{aligned}
\tag{1}
\]

设 \(n=|X|=3b+\sigma,\ \sigma\ge2\)。完整双向 M0 沿用 canonical 换核与实际消 \(M\) 的接口。两实际 766 核 \(H_L,H_R\) 分别有 \(2b-\alpha,2b-\beta\) 点，均含 \(D\)。左 owner 集 \(A_H=H_L\cap S\subseteq P\)，左锁集 \(\Omega\subseteq T\setminus H_L\) 恰为所有从 \(H_L\) 启动的 ambient \(R_6\) 终点。每个左 owner \(a_0\) 有 ambient 入 \(R_5\) 及出 \(B_5(a_0,\omega(a_0),\ldots)\)，其全部出 \(R_6\) 终点和全部出 \(B_5\) 第二点都等于唯一锁 \(\omega(a_0)\)。记 \(a=|A_H|,o=|\Omega|\)，有 \(a\ge o\)。反序接口给 \(B_H=H_R\cap T\subseteq Q\)、\(\Psi\subseteq S\setminus H_R\)，记 \(d=|B_H|,p=|\Psi|\)，有 \(d\ge p\)。右 owner \(b_0\) 有 ambient 出 \(R_5\) 和入 \(B_5(\ldots,\psi(b_0),b_0)\)，其全部入 \(R_6\) 首点及入 \(B_5\) 倒数第二点都是 \(\psi(b_0)\)。补集为 \(X\setminus H_L=(S\setminus A_H)\cup\Omega\)、\(X\setminus H_R=(T\setminus B_H)\cup\Psi\)。

令 \(W=(S\setminus\Omega)\cup C_0,\ W'=(T\setminus\Psi)\cup C_0\)。消 \(M\) 只交换 \(P/Q\) 角色点，故 \(C_0\subseteq D\) 保留在两核。\(C_0\subseteq U\) 的点无 ambient \(B_5\) 终点身份，\(C_0\subseteq V\) 的点无 ambient \(B_5\) 源身份，加回 \(C_0\) 保持完整端口。即 \(W\) 中属于 ambient \(\operatorname{End}_{R_5}\) 的点若启动 \(B_5\)，其第二点在 \(W\) 外。反向 \(W'\) 中属于 ambient \(\operatorname{Src}_{R_5}\) 的点若终止 \(B_5\)，其倒数第二点在 \(W'\) 外。有效 \(D_7\) 基底 \(W,W'\) 无 \(B_5\)，内部 \(R_6\) 横截分别至少 \(|W|-b,|W'|-b\)。定理 B 采用旧 weighted 接口与消 \(M\) 后的完整端口，覆盖实际兑现该接口的 \(w=1\) 配置。一般 \(w\) 的全类归一化沿用各自入口条件。

根族取全部 ambient 相邻对。

\[
\begin{aligned}
\widehat E&=\{e_0\in W\cap T:\ \exists\text{ ambient }R_6\text{ 的末对 }(u,e_0),\ u\in W\},\\
\widehat F&=\{f_0\in W'\cap S:\ \exists\text{ ambient }R_6\text{ 的首对 }(f_0,v),\ v\in W'\},\\
e&=|\widehat E|,\quad f=|\widehat F|,\quad x=\min\widehat E,\quad y=\max\widehat F .
\end{aligned}
\tag{2}
\]

由于 \(C_0\) 与 \(S,T\) 不交，根都在 \(I\)，前驱或后继可以在 \(C_0\)。加强根扇给 \(\chi(e_0,z,t)=R\) 当 \(e_0<z<t\) 且 \(t\in S\cup U\)，及 \(\chi(t,z,f_0)=R\) 当 \(t<z<f_0\) 且 \(t\in T\cup V\)。中点 \(z\) 可取 ambient 点。实际 \(R_6\) 末对 \((u,r)\) 对任意 \(s>r\) 给 \(\chi(u,r,s)=B\)，否则追加 \(s\) 得 \(R_7\)。首对 \((s,v)\) 对任意 \(r<s\) 反序给 \(\chi(r,s,v)=B\)。下文称其为末帽、首帽。

\[
\begin{aligned}
C&=\operatorname{End}_{R_5}(H_L),\qquad C'=\operatorname{Src}_{R_5}(H_R),\\
Z_+&=C\cap D,\quad Z_-=C'\cap D,\quad c_+=|Z_+|,\quad c_-=|Z_-|.
\end{aligned}
\tag{3}
\]

端点图和相邻对图均由相应域内的全部实际路径生成。用 König 定理删一个二部图顶点覆盖时，删去对应的实际点至多与覆盖等大，即使角色层有共同实际点。匹配只要求同一角色层中的端点互异，实际路径内部可共享。

- §3–4 给实际换核、加回 \(C_0\) 与加强根扇接口，§7 给旧加权式。[Weighted through 稳定性稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7879_INTERFACE_AUDIT_AND_WEIGHTED_THROUGH_STABILITY_20261031.md>)
- §2 给实际消 \(M\)，§3 给 ambient 根与头尾替换，§4–5 给实际锁与核交集接口。[锁纤维归一化稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCK_FIBER_NORMALIZATION_AND_DOUBLE_OMEGA_EXCLUSION_20261102.md>)
- §2 给由全路径定位到匹配的容量证明，§5 给 onefull 纯前供与匹配接口，§6 给 clean 压缩与修补核。[实际端点对 Hall 稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_ENDPOINT_PAIR_HALL_MISALIGNMENT_EXCLUSION_20261102.md>)
- §2 给实际 owner 根瓶颈，§8 给现行 767、777 参数工作界。[锁区间与临界闭合稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCK_INTERVAL_AND_CRITICAL_CLOSURE_20261102.md>)

## 2. 定理 A：跨角色蓝四禁形

**定理 A。** 767 母体中不存在 \(B_4(b_0,r,s,a_0)\) 且 \(b_0\in T,\ a_0\in S\)。

取一条入 \(b_0\) 的实际 \(R_6\)，末前驱记为 \(b_-\)。若 \(\chi(b_-,b_0,r)=R\)，追加 \(r\) 即得 \(R_7\)，故桥为蓝。取一条从 \(a_0\) 出发的实际 \(R_6\)，第二点记为 \(a_+\)。若 \(\chi(s,a_0,a_+)=R\)，在该 \(R_6\) 前接 \(s\) 即得 \(R_7\)，故桥亦为蓝。于是 \(b_-,b_0,r,s,a_0,a_+\) 构成 \(B_6\)。新点严格在原路径两端之外，六点互异。矛盾。

**跨角色根序。** 对任意实际末对 \((b_0,r)\)、\(b_0\in B_H\) 和任意实际首对 \((s,a_0)\)、\(a_0\in A_H\)，有 \(s\le r\)。若 \(r<s\)，两帽给 \(B_4(b_0,r,s,a_0)\)，违反定理 A。此序关系在选匹配前对全部 ambient owner 相邻对联合成立。


## 3. 定理 B：完整双向 M0 的非交错根序全排

**定理 B。** 若 \(\sigma\ge2\) 且 §1 的完整加权双向 M0 接口成立，则 \(x\ge y\) 不可能。结论允许任意满足接口的缺额、owner 数与锁点数，覆盖 \(\alpha>o\) 或 \(\beta>p\) 的非饱和情形和 \(w=1\)。

### 3.1 实际交集、人口与中间规模

若 \(a_0\in A_H\cap\Psi\)，\(\Psi\) 的精确供应给实际 \(R_6(a_0\to b_0)\)，其中 \(b_0\in B_H\)。左唯一锁迫 \(b_0=\omega(a_0)\)，右唯一锁迫 \(a_0=\psi(b_0)\)。于是有实际 \(B_5\) 以 \((a_0,b_0)\) 开头，另一个 \(B_5\) 以同一对结束，沿该对接成 \(B_8\) 并继承 \(B_6\)。反序排除 \(B_H\cap\Omega\)。结合两核的补集描述，

\[
A_H\cap\Psi=B_H\cap\Omega=\varnothing,\qquad
D_{\rm all}:=H_L\cap H_R=D\sqcup A_H\sqcup B_H .
\tag{4}
\]

记 \(|D|=b+q,\ m=q+a+d,\ i=|I|,\ \delta=|\Omega\cap I|,\ \varepsilon=|\Psi\cap I|\)，及 \(\Gamma=(\Omega\cap I)\cup(\Psi\cap I),\ \rho=|\Omega\cap\Psi|\)。锁集的交集在 \(I\) 中。左补集计数给 \(|S|=b+\sigma+\alpha-o+a+\delta\)，反序有 \(|T|=b+\sigma+\beta-p+d+\varepsilon\)。用 \(i=|S|+|T|+|D|-n\) 得

\[
\begin{aligned}
i&=q+\sigma+\alpha+\beta-o-p+a+d+\delta+\varepsilon,\\
|I\setminus\Gamma|&=m+\sigma+\alpha+\beta-o-p+\rho .
\end{aligned}
\tag{5}
\]

\(\widehat E\) 击中 \(W\) 的全部内部 \(R_6\)，故删去它后余域为 756。反向同理。完整 \(D_7\) 基底给

\[
e\ge |W|-b=\sigma+\alpha-o+a+w,\qquad
f\ge |W'|-b=\sigma+\beta-p+d+w .
\tag{6}
\]

两根族均在 \(I\) 中，且 \(x>y\) 使之不交，故 \(e+f\le i\)。由 \(\delta\le o,\varepsilon\le p\) 得

\[
q\ge \sigma+2w-\delta-\varepsilon,\qquad
m\ge\sigma+2w+(a-o)+(d-p)\ge\sigma>0 .
\tag{7}
\]

若 \(x=y=z\)，两根族至多共一点，\(e+f\le i+1\)，由同样的加权估计得 \(q\ge\sigma+2w-\delta-\varepsilon-1\)，因而 \(m\ge\sigma+2w-1+(a-o)+(d-p)\ge1\)。两种非交错根序均有实际正中间规模 \(m\)，且允许 \(q<0\)。

### 3.2 全部中间路径及匹配

\(D_{\rm all}\) 中全部 \(R_5\) 源点在 \(Z_-\sqcup A_H\sqcup(C'\cap B_H)\)，全部终点在 \(Z_+\sqcup B_H\sqcup(C\cap A_H)\)。路径同时位于 \(H_L,H_R\)，实际点按 (4) 分解。

每个右锁纤维取最晚 owner \(b_0\)。若 \(b_0\in C'\)，用其核内出 \(R_5\) 与入 \(B_5(\ldots,\psi(b_0),b_0)\) 连接。蓝桥给 \(B_6\)，红桥给从 \(\psi(b_0)\) 开始、终于更晚核内点的 \(R_6\)。该更晚点必是同一右锁纤维的 owner，违反最晚性。反序，左锁纤维的最早 owner 不在 \(C\)，所以

\[
|C'\cap B_H|\le d-p,\qquad |C\cap A_H|\le a-o .
\tag{8}
\]

\(D_{\rm all}\) 有 \(b+m\) 点，无 \(B_6\) 及 weak7。若完整 \(R_5\) 端点图的最大匹配小于 \(m\)，König 定理给少于 \(m\) 个角色顶点覆盖。删相应实际点，余域超过 \(b\) 点且无 \(R_5\)，违反换色 756 容量。固定任意 \(m\) 条中间匹配，源像记 \(J_U\)、终像记 \(J_V\)。源终容器分别最多有 \(c_-+a+d-p\)、\(c_++a+d-o\) 点，且分别含 \(J_U,J_V\)，故

\[
|Z_-\setminus J_U|\le c_--q-p,\qquad
|Z_+\setminus J_V|\le c_+-q-o .
\tag{9}
\]

两右端由实际匹配存在保证非负，匹配可以只覆盖容器的一部分。

### 3.3 实际 756 核与两侧全相邻对定位

令 \(P_H=P\cap H_R,\ Q_H=Q\cap H_L\)，取

\[
L_-:=C'\cup P_H\cup B_H=Z_-\sqcup P_H\sqcup B_H,\qquad
L_+:=C\cup Q_H\cup A_H=Z_+\sqcup Q_H\sqcup A_H .
\tag{10}
\]

二者分别在 \(H_R,H_L\)，故无 \(R_6\)。若 \(C'\) 中一点是 ambient \(B_5\) 终点，取该点核内出 \(R_5\) 与 \(B_5\) 连接。蓝桥给 \(B_6\)，红桥给终于 \(H_R\) 的 \(R_6\)，其首点即 \(B_5\) 的倒数第二点，故该点在 \(\Psi\) 中。\(B_H\) 的 \(B_5\) 倒数第二点也由唯一锁在 \(\Psi\)。\(P_H\subseteq S\) 的点无 ambient \(B_5\) 终点身份，因接上其出 \(R_6\) 的两种桥色分别给 \(B_6\) 或 \(R_7\)。\(\Psi\) 在域外，故 \(L_-\) 无 \(B_5\)，反序给 \(L_+\) 无 \(B_5\)。两者是实际 756。由两核分解，\(|P_H|=b-q-\beta-d,\ |Q_H|=b-q-\alpha-a\)，所以

\[
\kappa_-=b-|L_-|=q+\beta-c_-\ge0,\qquad
\kappa_+=b-|L_+|=q+\alpha-c_+\ge0 .
\tag{11}
\]

以下定位只要求 \(B,A\subseteq I\setminus\Gamma\) 且 \(B<x,\ A>y\)。严格分离时可取 \(y<\tau<x\) 的 ambient 间隙，并令 \(B=(I\cap(-\infty,\tau))\setminus\Gamma,\ A=(I\cap(\tau,\infty))\setminus\Gamma\)。两扩域 \(L_-\cup B,\ L_+\cup A\) 仍无 \(B_5\)，因相应锁集全缺席，而新增 \(I\) 点既无 ambient \(B_5\) 终点身份也无其源身份。左域 \(R_6\) 若终于 \(B_H\)，其源必须在缺席的 \(\Psi\) 中，故终点只能在 \(B\)。若末前驱在 \(P_H\cup B\subseteq W\)，终点会属于 \(\widehat E\)，但 \(B<x\)。反序，右域 \(R_6\) 只能从 \(A\) 启动，若第二点在 \(Q_H\cup A\subseteq W'\) 则触发 \(\widehat F\)，但 \(A>y\)。两侧全部相邻对分别位于

\[
(Z_-\cup B_H)\times B,\qquad A\times(Z_+\cup A_H).
\tag{12}
\]

删各自图的顶点覆盖对应实际点后，余域无 \(R_6,B_5,\mathrm{weak7}\)，人口至多 \(b\)。König 定理给两最大匹配分别至少 \(|B|-\kappa_-\)、\(|A|-\kappa_+\)。


### 3.4 严格分离时全 owner 根序将两侧损失合计压到一

取全 ambient owner 根族

\[
\begin{aligned}
\mathcal R&=\{s\in I\setminus\Gamma:\ \exists\text{实际 }R_6\text{ 首对 }(s,a_0),\ a_0\in A_H\},\\
\mathcal L&=\{r\in I\setminus\Gamma:\ \exists\text{实际 }R_6\text{ 末对 }(b_0,r),\ b_0\in B_H\}.
\end{aligned}
\tag{13}
\]

定理 A 给每个 \(s\in\mathcal R\) 都不晚于每个 \(r\in\mathcal L\)。若 \(s>x\)，根 \(x\) 的加强右红扇给 \(\chi(x,s,a_0)=R\)，与首帽矛盾。若 \(r<y\)，根 \(y\) 的加强左红扇给 \(\chi(b_0,r,y)=R\)，与末帽矛盾。因此 \(\mathcal R\) 的点均不晚于 \(x\)，\(\mathcal L\) 的点均不早于 \(y\)。

若 \(\mathcal R\) 有点晚于 \(y\)，取 \(z=\max\mathcal R\le x\)，选 \(z\) 紧左 ambient 间隙内的 \(\tau\in(y,x)\)。所有 \(\mathcal L\) 的点均不早于 \(z\)，所以 \(B\) 内没有 \(\mathcal L\) 根，\(A\) 内至多有一个 \(\mathcal R\) 根 \(z\)。否则选 \(y\) 紧右间隙内的 \(\tau\in(y,x)\)，此时 \(A\) 内无 \(\mathcal R\) 根，\(B\) 内至多有一个 \(\mathcal L\) 根 \(y\)。两种选法涵盖空根族、两族共有一根及 \(z=x\)。从任意两侧匹配中删全部涉及 \(A_H,B_H\) 的边，合计至多损失一条，因为匹配中每个实际根至多占一条边。

### 3.5 严格分离时同一中间匹配上的正交会

再舍弃普通 \(Z_-\) 端口不在 \(J_U\) 的边与 \(Z_+\) 端口不在 \(J_V\) 的边。由 (9)，总损失至多 \((c_--q-p)+(c_+-q-o)\)。将保留左匹配的 \(J_U\) 端像沿固定中间匹配运输到 \(J_V\)，与保留右匹配的 \(J_V\) 端像取交。由 \(|J_V|=m\)，交会数满足

\[
\begin{aligned}
\ell
&\ge |A|+|B|-\kappa_--\kappa_+-1-(c_--q-p)-(c_+-q-o)-m\\
&=|I\setminus\Gamma|-m-\alpha-\beta+o+p-1\\
&=\sigma+\rho-1\ge1 .
\end{aligned}
\tag{14}
\]

任一交会给实际末对 \((u,r)\)、实际中间 \(R_5(u\to v)\) 与实际首对 \((s,v)\)，满足 \(u<r<\tau<s<v\)。两帽给 \(B_4(u,r,s,v)\)，与中间红五同实际首末点，违反 weak7。这关闭严格分离类，包括双饱和单锁的严格分离。

### 3.6 共同根时两侧 owner 损失为零

令 \(x=y=z\)。由于 \(z\in\widehat E\cap\widehat F\)，它分别避开 \(\Omega,\Psi\)，故 \(z\notin\Gamma\)。用 \(z\) 作严格切分，取 \(B=(I\cap(-\infty,z))\setminus\Gamma,\ A=(I\cap(z,\infty))\setminus\Gamma\)。两根族分别满足 \(\widehat E\ge z\)、\(\widehat F\le z\)，所以 §3.3 的全相邻对定位和匹配下界仍成立。§3.4 的根瓶颈使所有 \(B_H\) 的末对根不早于 \(z\)，所有 \(A_H\) 的首对根不晚于 \(z\)。因此 \(B\) 上没有 \(B_H\) 端口边，\(A\) 上没有 \(A_H\) 端口边。共同根 \(z\) 只从根总数中扣一次。它在 \(I\)，不在 \(D\) 或 \(P/Q\) 的端口层。

由 §3.1 的 \(m\ge1\) 以及 §3.2 的容器与中间匹配下界，可以沿同一中间匹配交会。扣掉非 \(J_U,J_V\) 的普通端口后，由 (9)、(11) 得

\[
\begin{aligned}
\ell
&\ge |I\setminus\Gamma|-1-\kappa_--\kappa_+-(c_--q-p)-(c_+-q-o)-m\\
&=|I\setminus\Gamma|-1-m-\alpha-\beta+o+p\\
&=\sigma+\rho-1\ge1 .
\end{aligned}
\tag{15}
\]

相应链满足 \(u<r<z<s<v\)，两帽给 \(B_4(u,r,s,v)\)，与中间 \(R_5(u\to v)\) 同端违反 weak7。故共同根类也排除，定理 B 得证。

## 4. 定理 C：双 clean 的极端缺额全排

**定理 C。** 在 \(n=3b+2,w=0\) 层，设完整双向 M0 且双锁集皆空，\(H_L=X\setminus S,\ H_R=X\setminus T\)，两侧缺额 \(0\le\alpha,\beta\le3\)。则任一缺额为 \(0\) 或 \(3\) 的配置均不可能。该接口下仅余 \(\alpha,\beta\in\{1,2\}\) 且 \(x<y\)。

### 4.1 低前驱压缩与高后继压缩

此处 \(W=S,\ W'=T,\ i=q+2+\alpha+\beta,\ |D|=b+q,\ |P|=b-q-\beta,\ |Q|=b-q-\alpha\)。仍用 (3) 的 \(C,C',Z_\pm,c_\pm\)。横截容量及根扇给 \(2+\alpha\le e\le6,\ 2+\beta\le f\le6\)，因为各根族是红 clique。令 \(P_0\) 为全部低根 \(e_0\in\widehat E,\ e_0<y\) 的 ambient 末对中落在 \(S\) 的前驱，\(r=|P_0|\)。反序，令 \(Q_0\) 为全部高根 \(f_0\in\widehat F,\ f_0>x\) 的 ambient 首对中落在 \(T\) 的后继，\(s_0=|Q_0|\)。

完整尾替换适用如下。设一条实际 \(R_6\) 的第四、五点为 \(v_4,v_5\)，\(v_4\) 有 ambient 入 \(R_5\) 且 \(v_5<f_0\in\widehat F\)。取该入 \(R_5\) 的末前驱 \(v_-\) 及 \(f_0\) 的首对 \((f_0,t)\)，\(t\in T\)。若 \(\chi(v_-,v_4,v_5)=R\)，入 \(R_5\) 追加原红六的末二点给 \(R_7\)。故此桥为蓝。若 \(\chi(v_4,v_5,f_0)=B\)，首帽给 \(\chi(v_5,f_0,t)=B\)，进而 \(B_5(v_-,v_4,v_5,f_0,t)\) 违反完整反向端口，因为 \(t\) 有出 \(R_5\) 且 \(f_0,t\) 均在 \(T\)。所以 \(\chi(v_4,v_5,f_0)=R\)，可将原末点替为 \(f_0\)。反序头替换使用第三点的 ambient 出 \(R_5\) 身份与严格早于第二点的 \(\widehat E\) 根。

取 \(p_0\in P_0\) 所供低末对 \((p_0,e_0)\)。若 \(p_0\in T\)，根 \(y\) 的加强左红扇给 \(\chi(p_0,e_0,y)=R\)，与末帽冲突，故 \(P_0\subseteq P\)。\(C\) 各点有核内入 \(R_5\)，所以无 ambient \(B_5\) 源身份。否则连接两路径，蓝桥给 \(B_6\)，红桥给 \(H_L\)-origin \(R_6\)。\(P_0\) 各点是实际末前驱，有 ambient 入 \(R_5\)，由 M0 与双 clean 接口也无 \(B_5\) 源。\(H_L\) 删掉 \(C\) 后无 \(R_5\)，由换色容量得 \(|C|\ge b-\alpha\)。若 \(r\ge\alpha+1\)，将 \(\alpha+1\) 个前驱加入 \(C\) 得超过 \(b\) 点的无 \(B_5\) 集，容量迫一条 \(R_6\)，源为其中某个 \(p_0\)。末帽和 weak7 迫其末点不晚于对应 \(e_0\)，否则该末点与 \(p_0\) 间有同端 \(B_3\)。因此该路径第五点早于 \(y\)。域内所有点都有 ambient 入 \(R_5\)，故可尾替换到 \(y\)，与 \(B_3(p_0,e_0,y)\) 同端违反 weak7。完整反序压缩 \(Q_0\)。

令 \(k=|\widehat E\cap(-\infty,y)|\)。\(P_0\cup(\widehat E\cap[y,\infty))\) 横截 \(S\) 的全部内部 \(R_6\)，因为低末根的前驱落在 \(P_0\)，其余路径的末根保留。因此

\[
P_0\subseteq P,\quad r\le\alpha,\qquad Q_0\subseteq Q,\quad s_0\le\beta,\qquad
k\le e+r-2-\alpha .
\tag{16}
\]


### 4.2 任意间隙的根损失下界

置 \(m_0=\max(q,0),\ \mu=\min(q,0)\)。固定 \(D\) 中 \(m_0\) 条实际 \(R_5\) 端点匹配，源像 \(J_U\subseteq Z_-\)，终像 \(J_V\subseteq Z_+\)。若 \(q>0\)，由 \(|D|=b+q\) 与换色容量作 §3.2 的 König 删除论证，若 \(q\le0\) 则取空匹配。

初始两核 \(C'\cup P=Z_-\sqcup P\)、\(C\cup Q=Z_+\sqcup Q\) 是 (10) 的双 clean 特例，故为实际 756，缺额分别为 \(q+\beta-c_-\)、\(q+\alpha-c_+\)。任取 ambient 间隙 \(\tau\)，置 \(B=(I\cap(-\infty,\tau))\setminus\widehat E,\ A=(I\cap(\tau,\infty))\setminus\widehat F\)。扩域无 \(B_5\)。左域全部 \(R_6\) 终于 \(B\)，若末前驱在 \(P\cup B\subseteq S\) 则触发 \(\widehat E\)，故末对仅在 \(Z_-\times B\)。右域反序仅有 \(A\times Z_+\) 中的首对。容量给两匹配大小至少为根数减对应缺额。扣掉中间匹配外端口，损失再分别至多 \(c_--m_0,c_+-m_0\)。记

\[
g(\tau)=|\widehat E\cap(-\infty,\tau)|+|\widehat F\cap(\tau,\infty)|.
\tag{17}
\]

在固定中间匹配上的交会数下界为

\[
\begin{aligned}
\ell&\ge |A|+|B|-(q+\beta-c_-)-(q+\alpha-c_+)\\
&\qquad -(c_--m_0)-(c_+-m_0)-m_0\\
&=2-\mu-g(\tau).
\end{aligned}
\tag{18}
\]

任何交会由两帽产生同端 \(B_4/R_5\) 矛盾。因此每个间隙 \(g(\tau)\ge2-\mu\)。若 \(x>y\)，中间间隙给 \(g=0\)。若 \(x=y\)，紧邻任一侧的间隙给 \(g=1\)。两者均不可能。于是 \(x<y\)，\(x\) 有 \(P_0\) 前驱，\(y\) 有 \(Q_0\) 后继，故 \(r,s_0\ge1\)。结合 (16) 排除 \(\alpha=0\) 或 \(\beta=0\)。

### 4.3 实际修补核与严格 \(y\) 切分

修补实际集合

\[
L_+=C\cup Q\cup P_0=Z_+\sqcup Q\sqcup P_0,\qquad
L_-=C'\cup P\cup Q_0=Z_-\sqcup P\sqcup Q_0 .
\tag{19}
\]

\(L_+\) 的每一点都有 ambient 入 \(R_5\)，且无 ambient \(B_5\) 源。对 \(C,P_0\) 已在 §4.1 说明，对 \(Q\subseteq T\) 由入 \(R_6\) 接出 \(B_5\) 的两种桥色排除。若 \(L_+\) 有 \(R_6\)，其源在 \(P_0\)，原低末对的帽与 weak7 迫其末点不晚于对应 \(e_0<y\)，尾替换 \(y\) 给同端 \(B_3/R_6\) 矛盾。\(L_-\) 反序用 \(Q_0\) 的高首对及头替换 \(x\)。两修补核均为实际 756，其缺额为

\[
\kappa_+=q+\alpha-r-c_+\ge0,\qquad
\kappa_-=q+\beta-s_0-c_-\ge0.
\tag{20}
\]

取严格 \(y\) 切分，令 \(B=(I\cap(-\infty,y))\setminus\widehat E,\ A=I\cap(y,\infty)\)，所以 \(|A|+|B|=i-1-k\)。两扩域仍无 \(B_5\)。若左扩域中的 \(R_6\) 终于 \(t\in Q_0\)，取其对应高首对 \((f_0,t)\) 且 \(f_0>x\)。首帽及 weak7 迫这条红六的首点不早于 \(f_0\)，否则有同端 \(B_3\)。全域点都有 ambient 出 \(R_5\)，包括 \(B\subseteq I\)，故可头替换为 \(x\)，与 \(B_3(x,f_0,t)\) 同端矛盾。其他旧核点都非 \(T\)，所以 \(R_6\) 终于 \(B\)。若末前驱在 \(P\cup B\)，触发 \(\widehat E\)。若末前驱在 \(Q_0\subseteq T\)，实际末对 \((t,r_{\rm left})\) 满足 \(t<r_{\rm left}<y\)，根 \(y\) 的加强左扇给 \(\chi(t,r_{\rm left},y)=R\)，与末帽冲突。因此 \(Q_0\) 作为末前驱的损失为零，左域只剩 \(Z_-\to B\)。

右扩域中，若 \(R_6\) 从 \(p_0\in P_0\) 启动，原低末对的帽与 weak7 迫其末点不晚于对应 \(e_0<y\)，新增 \(A>y\) 无点能参与，遂与 \(L_+\) 无 \(R_6\) 冲突。因此右域 \(R_6\) 从 \(A\) 启动。\(P_0<y\) 不能作第二点，第二点在 \(Q\cup A\subseteq T\) 会触发 \(\widehat F\) 且 \(A>y=\max\widehat F\)。故仅有 \(A\to Z_+\)。

由容量取两侧匹配，扣缺额 (20) 及中间外端口后，在 \(m_0\) 条中间匹配上的交会数满足

\[
\begin{aligned}
\ell
&\ge |A|+|B|-\kappa_--\kappa_+-(c_--m_0)-(c_+-m_0)-m_0\\
&=1+r+s_0-k-\mu\\
&\ge3+\alpha+s_0-e-\mu .
\end{aligned}
\tag{21}
\]

若 \(\alpha=3\)，用 \(e\le6\) 得 \(\ell\ge s_0-\mu\ge1\)，与两帽给出的同端 \(B_4/R_5\) 矛盾。若 \(m_0=0\)，正交会下界已与中间匹配为空矛盾。反序排除 \(\beta=3\)，定理 C 得证。


## 5. 推论：完整接口的全部 onefull 排除

设 \(n=3b+\sigma,\ \sigma\ge2\)，且完整加权双向 M0 中至少一侧是缺额零的实际 fullstandard。不妨该侧为右侧，\(H_R=X\setminus T\) 有 \(2b\) 点且全局无 \(R_6\) 终点。记满反向前供 \(Z'=\operatorname{Src}_{R_5}(H_R)=P\sqcup U\)，\(|Z'|=b\)，其点无 ambient \(B_5\) 终点。这个身份可由容量直接看出。删去 \(Z'\) 后的换色容量给 \(|Z'|\ge b\)；任何终于 \(Z'\) 中一点的 ambient \(B_5\) 可在末点连接核内出 \(R_5\)，蓝桥给 \(B_6\)，红桥给终于 \(H_R\) 的 \(R_6\)，故 \(Z'\) 自身为 756 且至多 \(b\) 点。另一方面，\(H_R\) 内的 \(B_5\) 终点集也至少有 \(b\) 点，因为删去它得到实际 756。此终点集与 \(Z'\) 不交，所以二者分划 \(H_R\)。\(P\) 的点有 ambient 出 \(R_6\)，无 ambient \(B_5\) 终点，故 \(P\subseteq Z'\)。\(U\subseteq Z'\) 来自 \(D\subseteq H_R\)。删去 \(U\) 后 \(D\) 至多 \(b\) 点，故 \(|P|+|U|\ge |P|+|D|-b=b\)，取等给完整身份。此满侧有 \(W'=T\cup C_0\)。

取任意 \(f_0\in\widehat F\) 和一条实际首对 \((f_0,t)\)，其中 \(t\in W'\)。若 \(t\in T\)，则 \(t\) 是实际第二点，有 ambient 出 \(R_5\)，由满侧 clean 端口知其无 ambient \(B_5\) 终点。\(Z'\cup\{t\}\) 有 \(b+1\) 点且无 \(B_5\)，容量给 \(R_6(p_0,z_1,z_2,z_3,z_4,t)\)，终点只能是 \(t\)，前五点在 \(Z'\)，首点 \(p_0\in P\)。若 \(p_0<f_0\)，原首帽给 \(B_3(p_0,f_0,t)\)，与纯前供红六同端违反 weak7。\(p_0=f_0\) 由 \(P\cap I=\varnothing\) 排除，故 \(f_0<p_0\)。若某 \(e_0\in\widehat E\) 满足 \(e_0<p_0\)，因 \(z_1\in Z'\subseteq S\cup U\)，其加强右扇给 \(\chi(e_0,p_0,z_1)=R\)。将 \(e_0\) 前接到五点前缀，得到终于 \(z_4\in H_R\) 的 \(R_6\)，矛盾。\(e_0=p_0\) 也由角色不交排除，故对任一 \(e_0\) 有 \(f_0<p_0<e_0\)。整个纯前供论证与另一侧缺额无关。

若 \(t\in C_0\)，则 \(t\in U\)。假如某 \(e_0\in\widehat E\) 满足 \(e_0<f_0\)，加强右扇给 \(\chi(e_0,f_0,t)=R\)，可前接到原实际红六成 \(R_7\)。故 \(f_0\le e_0\)。综上，\(w=0\) 时 \(y<x\)，有 through 时 \(y\le x\)。定理 B 排除这两种根序。反序得到另一侧 fullstandard 的同一结论。

## 6. 临界覆盖与尚余问题

旧加权工作式 \(n+w\le3b+3\) 使新临界 \(n=3b+2\) 仅有 \(w\in\{0,1\}\)。沿 canonical 缺额预算 \(\eta\le3-w\) 及实际消 \(M\) 入口讨论。消 \(M\) 时非空 \(M\) 至少产生一个新锁，且换核后缺额至少为新锁总数，所以缺额零仍来自原实际 fullstandard。两侧缺额都为正的配置才需要继续覆盖。

| 新临界入口 | 本稿覆盖及剩余 |
|---|---|
| 完整双向 M0，根序 \(x\ge y\) | 定理 B 全排，涵盖两种 through 数与非饱和锁 |
| 至少一侧实际 fullstandard | §5 的纯前供或 through 弱根序均落入定理 B |
| \(w=0\)，双 clean 且任一缺额极端 | 定理 C 排除缺额 \(0\) 或 \(3\)，余双缺额 \(1/2\) 且 \(x<y\) |
| \(w=0\)，至少一侧有锁 | 两侧正缺额、严格交错 \(x<y\) 仍需覆盖 |
| \(w=1\)，两侧正缺额 | 严格交错 \(x<y\) 仍需覆盖 |

此表按已证结论划出仍需覆盖的入口。旧 \(n=3b+3\) 层的四种 \(\Omega\) 参数类型只在其旧预算下穷尽，不能拿来穷尽 \(\eta=3\) 的入口。下一步优先处理严格交错两侧在同一实际中间匹配上的兼容，尤其 \(w=1\) 与双 clean 的双缺额 \(1/2\) 情形。双 clean 可检验真实满核与中间扩域的全部端口，含非饱和锁时可联合跨角色根序与实际修补核。克隆 through 虽能保持 packet、\(R_7\) 与 \(B_6\) 禁形，却可能将同端总长 \(8\) 的 \(R_5+B_3\) 或 \(R_4+B_4\) 升为 weak7，合法性尚缺。

此处用全局容量简记 \(Q_{\rm cap}=N_{\rm sig}(7,6,7)\)、\(F_{\rm cap}=N_{\rm sig}(7,7,7)\)、\(C_{\rm cap}=N_{\rm sig}(7,6,6)\)，以区别集合角色。现有工作界和后续目标分别为

\[
Q_{\rm cap}\le3b+2,\qquad F_{\rm cap}=Q_{\rm cap}+1\le3b+3,\qquad
\text{目标为 }Q_{\rm cap}\le3b+1,\ F_{\rm cap}\le3b+2 .
\tag{22}
\]

容量桥 \(Q_{\rm cap}\le C_{\rm cap}+b+2\) 仍开放。现有实际 \(25\) 点构型给容量输入的下限，排除 \(b=24\) 作为有效容量上界。采用既有工作输入 \(b=25\)，保留 \(3\cdot25+2=77,\ 3\cdot25+3=78\)，即 767、777 的工作人口上界仍为 \(77/78\)。本稿的条件整类排除尚未推出 \(76/77\) 或更强的无条件加权界。[原有研究综述](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_SYNTHESIS_N7_20261103.md>)

## 附录 A：最少非普通端口数的精确公式

设有限二部图 \(G=(L_{\rm reg}\sqcup L_{\rm neutral},B)\) 存在饱和 \(B\) 的匹配。令 \(\epsilon\) 为所有这种匹配中所用 neutral 点数的最小值，\(N_{\rm reg}(J)\) 为 \(J\subseteq B\) 的普通邻居。则

\[
\epsilon
=|B|-\nu\bigl(G[L_{\rm reg},B]\bigr)
=\max_{J\subseteq B}\bigl(|J|-|N_{\rm reg}(J)|\bigr).
\tag{23}
\]

任何饱和匹配所用普通点数至多为普通子图的匹配数，给出第一等式的下界。反过来，从普通子图的最大匹配出发，在全图中依增广路增广，直至 \(B\) 饱和。每次增广保持先前已匹配的普通左点仍匹配，而任何匹配使用的普通点数又至多是普通子图的最大匹配数，故终态恰使用这么多普通点。最后一等式是普通子图的 Hall 缺额式。此式计算的是完成全根匹配所需的最少额外端口数，owner 子图的最大匹配数一般是另一数量。定理 B 直接以全实际 owner 根序控制损失，无需先计算此式。

