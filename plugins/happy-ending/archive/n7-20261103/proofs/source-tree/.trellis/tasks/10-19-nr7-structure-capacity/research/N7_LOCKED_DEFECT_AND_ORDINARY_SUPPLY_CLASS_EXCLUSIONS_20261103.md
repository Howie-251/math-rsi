# N7 有锁临界层的缺额、普通供给与混合类排除

2026-11-03。本文新增工作证明均为 **unreviewed / unaccepted**。数学由主会话定稿，推导与交叉核对属于同会话工作。指定 native gpt-6.1-sol/high 执行者负责转写与文档核对。

## 1. 临界层与完整接口

设 \(X\) 为有序 rank-3 signotope 的 767 母体，\(b\) 是 756 和换色 756 的共同有效容量。\(R_j,B_j\) 表示实际红、蓝 \(j\) 点路径。四点 packet 的三元组按字典序排列，颜色至多改变一次。路径对子序列遗传。weak7 禁止同一对实际首末点之间有长度和至少为 \(9\) 的红、蓝路径。767 禁 \(R_7,B_6,\mathrm{weak7}\)，756 禁 \(R_6,B_5,\mathrm{weak7}\)，换色 756 禁 \(R_5,B_6,\mathrm{weak7}\)。ambient 指 \(X\)，核内角色按标明的实际域计算。

以下固定人口临界层 \(n=|X|=3b+2\)。记 \(S=\operatorname{Src}_{R_6}(X)\)、\(T=\operatorname{End}_{R_6}(X)\)，并令

\[
I=S\cap T,\qquad P=S\setminus T,\qquad Q=T\setminus S,\qquad
D=X\setminus(S\cup T),\qquad |D|=b+q.
\tag{1}
\]

记 \(w=|\operatorname{Src}_{R_5}(D)\cap\operatorname{End}_{R_5}(D)|\)。既有 \(n+w\le3b+2\) 给 \(w=0\)。完整双向 M0 归一化给实际 766 核 \(H_L,H_R\)，大小 \(2b-\alpha,2b-\beta\)。临界层缺额至多 \(3\)。既有 onefull 和非交错根序排除允许本文取 \(1\le\alpha,\beta\le3\) 及严格交错 \(x<y\)。

- 完整双向 M0、加权界、非交错根序及同一中间匹配见 §1–2，锁纤维修补核及切分见 §4，临界层见 §6。[共同中间匹配与加权界稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMMON_MIDDLE_COMPATIBILITY_AND_WEIGHTED_BOUND_20261103.md>)
- 完整实际换核、根工具、纤维端口见 §2–5。[锁纤维归一化稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCK_FIBER_NORMALIZATION_AND_DOUBLE_OMEGA_EXCLUSION_20261102.md>)
- 跨角色根序、实际核交集及 onefull 见 §2–3、§5。[跨角色根序稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_CROSS_ROLE_ROOT_ORDER_AND_SEPARATED_CLASS_EXCLUSION_20261103.md>)
- 从实际路径图到匹配及同端 weak7 矛盾见 §2。[实际端点对 Hall 稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_ENDPOINT_PAIR_HALL_MISALIGNMENT_EXCLUSION_20261102.md>)
- 双 clean 临界类的实际增广与 packet 论证见 §2–4。[双 clean 增广中间域稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_AUGMENTED_MIDDLE_CLEAN_CLASS_EXCLUSION_20261103.md>)

### 1.1 Owner、锁与普通供给

左 owner \(A_H=H_L\cap S\subseteq P\)，左锁 \(\Omega\subseteq T\setminus H_L\)，记 \(a=|A_H|,\ o=|\Omega|\)。每个左 owner 有 ambient 入 \(R_5\) 及出 \(B_5\)，其全部出 \(R_6\) 末点及出 \(B_5\) 第二点同为唯一锁 \(\omega\in\Omega\)。\(\Omega\) 恰为从 \(H_L\) 启动的 ambient \(R_6\) 的末点集，每个锁均有实际 owner。反序定义右 owner \(B_H=H_R\cap T\subseteq Q\)、右锁 \(\Psi\subseteq S\setminus H_R\) 及 \(d=|B_H|,\ p=|\Psi|\)。右 owner 有 ambient 出 \(R_5\) 及入 \(B_5\)，其全部入 \(R_6\) 首点及入 \(B_5\) 倒数第二点同为唯一右锁。设 \(u=a-o,\ v=d-p\)，均非负。clean 侧的锁集和 owner 集均为空。

置 \(W=S\setminus\Omega,\ W'=T\setminus\Psi\)。以这两个完整基底定义全部实际根 \(\widehat E,\widehat F\)。\(\widehat E\) 收集所有两点均在 \(W\) 的 ambient \(R_6\) 末对中的末点，\(\widehat F\) 收集所有两点均在 \(W'\) 的 ambient \(R_6\) 首对中的首点。两根族均在 \(I\)。写 \(e=|\widehat E|,\ f=|\widehat F|,\ x=\min\widehat E,\ y=\max\widehat F\)。其容量界为

\[
h_L=|W|-b=2+\alpha+u\le e\le6,\qquad
h_R=|W'|-b=2+\beta+v\le f\le6,\qquad h_L,h_R\le5.
\tag{2}
\]

实际末对 \((u_0,r_0)\) 对 \(z>r_0\) 给末帽 \(\chi(u_0,r_0,z)=B\)，实际首对 \((s_0,v_0)\) 对 \(z<s_0\) 给首帽 \(\chi(z,s_0,v_0)=B\)。下文用到根 \(y\) 的左红扇，即 \(z_0\in T,\ z_0<z_1<y\) 时 \(\chi(z_0,z_1,y)=R\)，以及反序的右红扇。完整反端口禁止一个 ambient \(B_5\) 的末对两点均在 \(W'\) 且末点有 ambient 出 \(R_5\)。正向完整端口反序成立。

既有跨角色禁形排除首点在 \(T\)、末点在 \(S\) 的 \(B_4\)，因为两端分别用入、出红六的帽扩成 \(B_6\)。任意以 \(A_H\) 点为第二点的实际 \(R_6\) 首对，其首根至多 \(x\)。任意以 \(B_H\) 点为末前驱的实际 \(R_6\) 末对，其末根至少 \(y\)。这些瓶颈也可由根 \(x,y\) 的加强扇与实际帽直接读出。

收集 \(\widehat E<y\) 的全部实际末对中位于 \(W\) 的末前驱。根 \(y\) 的左扇与末帽排除前驱在 \(T\)，故这些点在 \(P\)。将它们分成核外 ordinary 集 \(R\subseteq P\setminus H_L\) 和 owner 集 \(R_A\subseteq A_H\)，记 \(r=|R|,\ r_A=|R_A|\)。反序，收集 \(\widehat F>x\) 的全部实际首对中在 \(W'\) 的普通第二点，得 \(Q_0\subseteq Q\setminus H_R\)，记 \(s=|Q_0|\)。\(R\) 中各点有 ambient 入 \(R_5\) 且无 ambient 出 \(B_5\)，\(Q_0\) 中各点有 ambient 出 \(R_5\) 且无 ambient 入 \(B_5\)。既有普通供给压缩给

\[
r\le\alpha-o,\qquad s\le\beta-p.
\tag{3}
\]

定义 \(o_l=|\Omega\cap(-\infty,y)|,\ p_h=|\Psi\cap(y,\infty)|\)。一个低末对若由 owner 供应，末帽与 weak7 迫其唯一锁不晚于对应末根。该末根在 \(W\) 中且早于 \(y\)，故锁严格更早。由每个纤维的一位代表以及总共 \(u\) 个额外 owner，得 \(r_A\le o_l+u\)。根 \(y\) 的实际第二点是普通高后继或右 owner。若为右 owner，首帽与 weak7 迫其锁不早于 \(y\)，而 \(y\in W'\) 避开 \(\Psi\)，故该锁严格晚于 \(y\)。所以

\[
r_A\le o_l+u,\qquad s+p_h\ge1 .
\tag{4}
\]

### 1.2 代表中间域和两侧修补核

从每个左纤维取最早 owner 得 \(A_0\)，从每个右纤维取最晚 owner 得 \(B_0\)，故 \(|A_0|=o,\ |B_0|=p\)。交叉锁禁形给 \(A_H\cap\Psi=B_H\cap\Omega=\varnothing\)。例如，若左 owner 也是右锁，实际右锁供给迫对应右 owner 与该左 owner 互锁，两条沿同一相邻对的蓝五接成 \(B_8\)，继承 \(B_6\)。反序亦然。因此

\[
H_L\cap H_R=D\sqcup A_H\sqcup B_H,\qquad
D_0=D\sqcup A_0\sqcup B_0\subseteq H_L\cap H_R.
\tag{5}
\]

定义 \(C=\operatorname{End}_{R_5}(H_L),\ C'=\operatorname{Src}_{R_5}(H_R)\)，\(Z_+=C\cap D,\ Z_-=C'\cap D,\ c_\pm=|Z_\pm|\)。左纤维最早代表不能在 \(C\) 中。若有核内红五终于该代表，将其接该代表的出蓝五。蓝桥给 \(B_6\)，红桥给终于同一锁的红六，且首点是核内更早的 owner，违反代表的最早性。反序 \(B_0\cap C'=\varnothing\)。因此 \(D_0\) 中全部 \(R_5\) 首点在 \(Z_-\sqcup A_0\)，末点在 \(Z_+\sqcup B_0\)。

设 \(P_H=P\cap H_R,\ Q_H=Q\cap H_L\)。修补核取

\[
\begin{aligned}
L_+&=C\cup Q_H\cup A_H\cup R=Z_+\sqcup Q_H\sqcup A_H\sqcup R,\\
L_-&=C'\cup P_H\cup B_H\cup Q_0=Z_-\sqcup P_H\sqcup B_H\sqcup Q_0 .
\end{aligned}
\tag{6}
\]

每个 \(C\) 点若有 ambient 出蓝五，将其与 \(H_L\) 内入红五连接。蓝桥给 \(B_6\)，红桥给从 \(H_L\) 启动的红六，其末点即蓝五第二点，故第二点在 \(\Omega\)。\(A_H\) 点也有相同的锁限制。\(Q_H\subseteq T\) 无 ambient 出蓝五，\(R\) 亦然。\(L_+\) 中 \(C,Q_H,A_H\) 均在 \(H_L\)，新增 \(R\subseteq P\) 与 \(\Omega\subseteq T\) 不交，故 \(\Omega\) 缺席，\(L_+\) 无 \(B_5\)。

\(L_+\) 的每点有 ambient 入 \(R_5\)。其中红六若从 \(A_H\) 启动，末点必须在缺席的 \(\Omega\)。其余可能的源只在 \(R\)。对 \(p_0\in R\) 取对应低末对 \((p_0,e_0)\) 且 \(e_0<y\)。末帽与 weak7 迫任何从 \(p_0\) 启动的红六终于不晚于 \(e_0\) 的点。若全域各点都有 ambient 入红五，既有尾替换以 \(y\) 替末点，与末帽给出的 \(B_3(p_0,e_0,y)\) 同端矛盾。故 \(L_+\) 无 \(R_6\)。反序，\(L_-\) 各点有 ambient 出红五，其潜在蓝五倒数第二点只在缺席的 \(\Psi\)。红六终于 \(B_H\) 需从 \(\Psi\) 启动，终于 \(Q_0\) 则由对应高首帽及头替换 \(x\) 排除。两核均为实际 756。

由 (5)，\(H_L=D\sqcup Q_H\sqcup A_H\)，\(H_R=D\sqcup P_H\sqcup B_H\)。交叉锁禁形及 \(P_H,Q_H\) 的核内身份保证 \(P_H\) 避开 \(\Psi\)、\(Q_H\) 避开 \(\Omega\)。\(Q_0\subseteq Q\) 避开 \(\Psi\)。于是两核缺额为

\[
\kappa_+=b-|L_+|=q+\alpha-r-c_+\ge0,\qquad
\kappa_-=b-|L_-|=q+\beta-s-c_-\ge0 .
\tag{7}
\]

## 2. 定理 A：大缺额与额外纤维 owner 的统一排除

**工作定理 A。** 在 §1 的完整接口下，\(\max(\alpha,\beta)+u+v\ge3\) 的整个临界类不可能。

记 \(i=|I|,\ \delta=|\Omega\cap I|,\ \varepsilon=|\Psi\cap I|,\ \rho=|\Omega\cap\Psi|\)，令 \(\Gamma=(\Omega\cap I)\cup(\Psi\cap I)\)。两侧补集计数给

\[
i=q+2+\alpha+\beta-o-p+a+d+\delta+\varepsilon .
\tag{8}
\]

严格在 \(y\) 切分，取

\[
B=(I\cap(-\infty,y))\setminus(\widehat E\cup\Gamma),\qquad
A=(I\cap(y,\infty))\setminus\Gamma .
\tag{9}
\]

\(A,B\) 表示实际点集，路径记号和颜色等式中的 \(B\) 表示蓝色。两侧新增的 \(I\) 点保持所需 ambient 红五身份与蓝五限制，并且对应锁集仍缺席。

**左扩域。** \(L_-\cup B\) 的全部 \(R_6\) 终于 \(B\)。终于 \(B_H\) 需缺席的 \(\Psi\) 作首点，终于 \(Q_0\) 由高首帽及头替换 \(x\) 排除，其余旧核点非 \(T\)。末前驱若在 \(P_H\cup B\subseteq W\)，会触发 \(\widehat E\)。若在 \(B_H\)，末根至少 \(y\)。若在 \(Q_0\subseteq T\)，根 \(y\) 的左扇与实际末帽矛盾。故全部实际左末对只从 \(Z_-\) 指向 \(B\)。

**右扩域。** \(L_+\cup A\) 的全部 \(R_6\) 从 \(A\) 启动。owner 的末点锁在缺席的 \(\Omega\)，从 \(R\) 启动则由低帽与尾替换 \(y\) 排除。第二点若在 \(Q_H\cup A\subseteq W'\)，会触发 \(\widehat F\) 中晚于 \(y\) 的根。若在 \(A_H\)，首根至多 \(x<y\)。若在 \(R<y\)，顺序不允许。故全部实际右首对只从 \(A\) 指向 \(Z_+\)。

用各扩域内全部实际相邻对建二部图。König 顶点覆盖对应实际删点，击中全部红六而保留其他禁形。两个扩域的人口分别为 \(b+|B|-\kappa_-\)、\(b+|A|-\kappa_+\)，因此相应外匹配至少为 \(|B|-\kappa_-\)、\(|A|-\kappa_+\)。

代表域 \(D_0\) 有 \(b+q+o+p\) 个实际点。取

\[
m=\max(q+o+p,0),\qquad \mu=\min(q+o+p,0).
\tag{10}
\]

以 \(D_0\) 内全部实际 \(R_5\) 的首末点建图。若 \(m>0\)，换色 756 容量和 König 定理给一份 \(m\) 条实际中间匹配。否则取空匹配。覆盖删点只按实际点计数，角色副本重合只会减少删点。中间首末容器分别为 \(Z_-\sqcup A_0,\ Z_+\sqcup B_0\)，未覆盖数恰为 \(c_-+o-m,\ c_++p-m\)。

对每个 \(\omega\in\Omega\) 且 \(\omega<y\)，把实际锁末对 \((a_\omega,\omega)\) 加入左匹配，\(a_\omega\in A_0\) 是该纤维代表。将 \(a_\omega\) 的入红五与出蓝五连接，蓝桥给 \(B_6\)，红桥给所需实际红六末对。反序，将每个 \(\psi\in\Psi\) 且 \(\psi>y\) 的实际锁首对 \((\psi,b_\psi)\) 加入右匹配，\(b_\psi\in B_0\)。代表端口不在 \(D\)，锁根若在 \(I\) 则已由 \(\Gamma\) 排除，否则不在 \(A,B\)，故两边新增的实际锁边都无角色冲突。

令 \(k=|\widehat E\cap(-\infty,y)|,\ \chi_0=\mathbf 1[y\notin\Gamma],\ j_E=|\widehat E\cap\Psi\cap(-\infty,y)|\)。由于 \(\widehat E\) 避开 \(\Omega\)，有

\[
N:=|A|+|B|=i-\delta-\varepsilon+\rho-k-\chi_0+j_E .
\tag{11}
\]

两侧沿同一份中间匹配运输，舍去未覆盖的容器端口。交会条数满足

\[
\begin{aligned}
\ell
&\ge N-\kappa_--\kappa_++o_l+p_h
 -(c_-+o-m)-(c_++p-m)-m\\
&=2-o-p+a+d+\rho+r+s-k-\chi_0+j_E+o_l+p_h-\mu .
\end{aligned}
\tag{12}
\]

横截 \(R\cup R_A\cup(\widehat E\cap[y,\infty))\) 击中 \(W\) 内全部实际红六，故 \(k\le e+r+r_A-h_L\)。将其代入 (12)，用 \(e\le6,\ \chi_0\le1\)，舍去非负的 \(\rho,j_E\)，再由 (4) 得

\[
\begin{aligned}
\ell&\ge \alpha+2u+v-3+s+o_l-r_A+p_h-\mu\\
&\ge \alpha+u+v-3+s+p_h-\mu
\ge \alpha+u+v-2-\mu .
\end{aligned}
\tag{13}
\]

若 \(\alpha+u+v\ge3\)，则 \(\ell\ge1\)。若 \(m=0\)，这与空匹配矛盾。否则交会提供实际中间 \(R_5(z_-\to z_+)\)、左末对 \((z_-,r_0)\)、右首对 \((s_0,z_+)\)，且 \(z_-<r_0<y<s_0<z_+\)。两帽给同端 \(B_4(z_-,r_0,s_0,z_+)\)，违反 weak7。反序给 \(\beta+u+v\ge3\) 的排除，定理 A 得证。

因此缺额 \(3\) 及任一 \(h_L,h_R=5\) 的整类均排除。剩余 \(\max(\alpha,\beta)=2\) 时必有 \(u=v=0\)，\(\alpha=\beta=1\) 时必有 \(u+v\le1\)。

## 3. 定理 B：普通供给触发实际中间域增广

**工作定理 B。** 若 \(r>0\)，则 \(r\le\alpha-o-1\)。反序，若 \(s>0\)，则 \(s\le\beta-p-1\)。因此在定理 A 余下的临界层，有锁侧具有对应普通供给的整类均排除，缺额为 \(1\) 的 clean 侧具有对应普通供给的整类也排除。

### 3.1 新普通首点与代表点的末点限制

取 \(p_0\in R\) 和其实际低末对 \((p_0,e_0)\)，\(e_0<y\)。从根 \(y\) 固定一条实际首对 \((y,t_y)\) 且 \(t_y\in W'\)。因为 \(t_y\) 是实际首对第二点，具有 ambient 出红五。定义

\[
M=D_0\sqcup\{p_0\}.
\tag{14}
\]

若 \(M\) 内有 \(R_5\) 终于 \(p_0\)，记其末前驱为 \(d_1\)。接 \(e_0\) 的桥若为红，得到 \(R_6\)。红五原首点若在 \(D\cup B_0\)，违反这些点非 \(S\)。原首点若在 \(A_0\)，红六必须终于 \(\Omega\)，但 \(e_0\in W\) 避开 \(\Omega\)。所以桥必为蓝。由两帽得到 \(B_5(d_1,p_0,e_0,y,t_y)\)。它的末对两点均在 \(W'\)，违反完整反端口。因此 \(p_0\) 不能是 \(M\) 中的红五末点。

以下 packet 推导用于从 \(p_0\) 启动的实际 \(R_5(p_0,a_1,a_2,a_3,z)\)，其中 \(z\notin T\)。若 \(z\) 启动 ambient \(B_5\) 且第二点为 \(v_0\)，连接两路径的桥若为蓝，得到 \(B_6\)。红桥则给 \(R_6(p_0,a_1,a_2,a_3,z,v_0)\)，故 \(v_0\in T\)，且由 \((p_0,e_0)\) 的末帽和 weak7 得 \(v_0\le e_0\)。于是 \(p_0<z<v_0\le e_0<y\)。

取原实际末对 \((p_0,e_0)\) 所在红六中 \(p_0\) 的前一点 \(h\)。若 \(\chi(h,p_0,z)=R\)，原红六前五点接 \(z\) 得终于非 \(T\) 点的红六，矛盾。故 \(\chi(h,p_0,z)=B\)，而 \(\chi(h,p_0,e_0)=R\)。packet \((h,p_0,z,e_0)\) 迫 \(\chi(p_0,z,e_0)=R\)。packet \((p_0,z,e_0,y)\) 首色红，第三色 \(\chi(p_0,e_0,y)=B\)，迫 \(\chi(z,e_0,y)=B\)。若 \(\chi(a_3,z,e_0)=B\)，则由 \(\chi(e_0,y,t_y)=B\) 得 \(B_5(a_3,z,e_0,y,t_y)\)，违反完整反端口。故该桥为红，得到

\[
R_6(p_0,a_1,a_2,a_3,z,e_0).
\tag{15}
\]

任一从 \(z\) 启动的蓝五的第二点 \(v_0\) 若严格早于 \(e_0\)，由 \(v_0\in T\) 及根 \(y\) 左扇得 \(\chi(v_0,e_0,y)=R\)。packet \((p_0,v_0,e_0,y)\) 第三色蓝、第四色红，迫 \(\chi(p_0,v_0,e_0)=B\)，与 (15) 同端违反 weak7。因此此类 \(z\) 的任何 ambient 出蓝五的第二点必为 \(e_0\)。

现在若 \(M\) 内有红五终于 \(a_0\in A_0\)，把它与 \(a_0\) 的出蓝五连接，蓝桥给 \(B_6\)，红桥给终于 \(\omega(a_0)\) 的红六。若红五首点在 \(D\cup B_0\)，红桥违反非 \(S\) 身份。若首点在 \(A_0\)，它与 \(a_0\) 必须属同一锁纤维，每个纤维仅一位代表，违反红五首点严格早于末点。剩余首点只能是 \(p_0\)。因为 \(a_0\in P\) 非 \(T\)，上述 packet 推导适用，迫其出蓝五第二点 \(\omega(a_0)=e_0\)。然而 \(\omega(a_0)\in\Omega\) 而 \(e_0\in W\)。等价地，帽先迫 \(\omega(a_0)<e_0\)，再由左扇与 packet 给同端 \(B_3(p_0,\omega(a_0),e_0)\) 的矛盾。故 \(A_0\) 也不能承载 \(M\) 内红五末点。

### 3.2 新末点整体加入右核

定义

\[
J=(\operatorname{End}_{R_5}(M)\cap D)\setminus Z_+,\qquad j=|J|.
\tag{16}
\]

由 §3.1，\(M\) 的全部实际红五末点在 \(Z_+\sqcup B_0\sqcup J\)。任取 \(z\in J\) 并固定一条 \(M\) 中终于 \(z\) 的红五。若从 \(z\) 有 ambient 出蓝五，两路径的连接桥必须为红，否则给 \(B_6\)。若红五首点在 \(D\cup B_0\)，红桥给从非 \(S\) 点启动的红六，故这种情形无出蓝五。若首点在 \(A_0\)，红桥给由该 owner 启动、终于蓝五第二点的红六，故该第二点在 \(\Omega\)。若首点为 \(p_0\)，§3.1 的 packet 推导迫该第二点为 \(e_0\)。于是 \(J\) 各点有 ambient 入红五，其蓝五第二点只能在 \(\Omega\cup\{e_0\}\)。

整体加入 \(J\) 得 \(L_+\sqcup J\)。点 \(e_0\in I\) 缺席，锁集 \(\Omega\) 也仍缺席，因为 \(J\subseteq D\)。故增广核无 \(B_5\)。全域每点有 ambient 入红五。owner 启动的红六需终于缺席的 \(\Omega\)，\(R\) 启动的红六由低帽和尾替换排除，其他点非 \(S\)。因此增广核为实际 756，\(j\le\kappa_+\)。

从 \(M\) 删除全部实际 \(R_5\) 末点，余域无红五并继承其他禁形，故为换色 756，人口至多 \(b\)。不论 \(q\) 的符号，由端点容器和 (7) 得

\[
q+o+p+1
\le|\operatorname{End}_{R_5}(M)|
\le c_++p+j
\le q+\alpha-r+p .
\tag{17}
\]

故 \(r\le\alpha-o-1\)。反序得 \(s\) 的结论。证明对每个纤维只选一位代表，允许任意符合接口的额外 owner 数。

定理 A 之后，左有锁且 \(r>0\) 时，由 (3) 仅可能 \((\alpha,o,r)=(2,1,1)\)，与 (17) 矛盾。反序排除右有锁且 \(s>0\)。左 clean 且 \(\alpha=1\) 时，(17) 排除 \(r>0\)，右侧反序亦然。这些带对应普通供给的临界配置均被排除。

## 4. 定理 C：一侧 clean、另一侧有锁的整类排除

**工作定理 C。** 在 §1 的临界层，一侧 clean 且另一侧有锁的全部配置不可能。

反序后令左侧 clean，即 \(A_H=\Omega=\varnothing\)。根 \(x<y\) 必有普通低前驱，所以 \(r>0\)。由 A、B 得 \(\alpha=2,\ r=1,\ \beta\in\{1,2\},\ u=v=0,\ s=0\)。右侧有锁，故 \(p\ge1\)，且 \(B_H=B_0\) 在每个右纤维中恰有一位 owner。用 §3 的实际低末对 \((p_0,e_0)\) 和实际中间域

\[
M=D\sqcup B_0\sqcup\{p_0\}.
\tag{18}
\]

由 §3，\(M\) 无红五终于 \(p_0\)。新红五末点集 \(J\) 可整体加入右修补核 \(L_+\)，得到实际 756。

### 4.1 同时增广左核与右核

\(M\) 中无 \(R_5\) 从 \(B_0\) 启动。否则取 \(b_0\in B_0\) 的入蓝五，其末对为 \((\psi(b_0),b_0)\)，与从 \(b_0\) 启动的红五相接。蓝桥给 \(B_6\)，红桥给从 \(\psi(b_0)\) 启动的红六。其末点不能在非 \(T\) 的 \(D\cup\{p_0\}\)，只能在 \(B_0\)。该末点的唯一右锁须为 \(\psi(b_0)\)，而该纤维只有一个 owner，故末点必为 \(b_0\)，违反实际顺序。

令 \(Y=(\operatorname{Src}_{R_5}(M)\cap D)\setminus Z_-\)。对任意 \(z\in Y\)，选一条从 \(z\) 启动的 \(M\) 内红五，其末点在 \(D\cup B_0\)。若有 ambient 蓝五终于 \(z\)，与该红五连接。蓝桥给 \(B_6\)，红桥给一条以蓝五倒数第二点为首点、以红五末点为末点的红六。红六末点在 \(D\) 不可能，若在 \(B_0\) 则其首点必在 \(\Psi\)。故 \(Y\) 每点有 ambient 出红五，任何终于其中一点的蓝五倒数第二点只在 \(\Psi\)。

\(L_-\sqcup Y\) 无蓝五，因为 \(\Psi\) 缺席。红六若终于旧核 \(B_H\)，需从缺席的 \(\Psi\) 启动。\(s=0\) 给 \(Q_0=\varnothing\)，其余旧核点及 \(Y\) 均非 \(T\)，所以无红六。故左增广核为实际 756。此处允许 \(p_0\in\Psi\)，因为只把 \(p_0\) 加到 \(M\)，实际左增广核只加入 \(Y\subseteq D\)。

左右增广缺额为

\[
\kappa_-^*=q+\beta-c_--|Y|,\qquad
\kappa_+^*=q+1-c_+-|J| .
\tag{19}
\]

\(M\) 的实际红五首点在 \(Z_-\sqcup Y\sqcup\{p_0\}\)，末点在 \(Z_+\sqcup J\sqcup B_0\)。取

\[
m'=\max(q+p+1,0),\qquad \mu'=\min(q+p+1,0).
\tag{20}
\]

由换色容量和 König 定理，在 \(M\) 内固定一份恰 \(m'\) 条的实际红五端点匹配。若 \(m'=0\)，取空匹配。

### 4.2 同一份增广匹配上的正交会

沿用严格 \(y\) 切分 (9)。左侧扩域 \((L_-\sqcup Y)\cup B\)，右侧扩域 \((L_+\sqcup J)\cup A\)，其全部实际红六的相邻对仍按 §2 定位。左域新增 \(Y\subseteq D\) 有出红五且潜在蓝五倒数第二点在缺席的 \(\Psi\)，故左末对只从 \(Z_-\cup Y\) 指向 \(B\)。右域中 \(e_0\) 仍缺席，因为 \(e_0<y\)，\(J\) 中各点有入红五而其潜在蓝五第二点需 \(e_0\)。低帽与尾替换仍排除 \(R\) 启动的红六，\(J\) 非 \(S\)，故右首对只从 \(A\) 指向 \(Z_+\cup J\)。容量给两份外匹配，分别至少为 \(|B|-\kappa_-^*,\ |A|-\kappa_+^*\)。

在左外匹配加入实际末对 \((p_0,e_0)\)。\(p_0\notin D,\ e_0\in\widehat E\) 保证端口、根都无冲突。右外匹配加入全部 \(\Psi>y\) 的实际锁首对，右端口为其 \(B_0\) 代表。这里只有右锁，\(\Gamma=\Psi\cap I,\ \rho=0\)。根 \(y\in W'\) 避锁，故 \(\chi_0=1\)。由 (8) 得 \(i-|\Gamma|=q+4+\beta\)，于是 (11) 给

\[
N=q+3+\beta-k+j_E .
\tag{21}
\]

沿同一份 \(M\) 内红五匹配运输。未覆盖的完整首末容器分别有 \(c_-+|Y|+1-m'\)、\(c_++|J|+p-m'\) 个点。扣除相应外边后，交会条数满足

\[
\begin{aligned}
\ell
&\ge N-\kappa_-^*-\kappa_+^*+1+p_h
 -(c_-+|Y|+1-m')-(c_++|J|+p-m')-m'\\
&=3-k+j_E+p_h-\mu' .
\end{aligned}
\tag{22}
\]

由于左侧 clean 且 \(r=1,\ h_L=4\)，横截界给 \(k\le e+r-h_L=e-3\le3\)。又 \(s=0\)，由 (4) 得 \(p_h\ge1\)。因此 \(\ell\ge1\)。空中间匹配时已矛盾。其余情形一个交会给实际中间红五和两外相邻对，外根严格跨 \(y\)，两帽生成同端蓝四，违反 weak7。定理 C 得证，包括 \(p_0\in\Psi\) 的情形。

## 5. 临界覆盖、参数结论与数值

定理 A 排除了含缺额 \(3\) 或额外 owner 超出纤维预算的整个临界类。定理 B 排除了余下有锁侧带普通供给的整个临界类。定理 C 与既有双 clean 增广中间域结果合并，排除了所有至少一侧 clean 的 \(n=3b+2\) 配置。混合类的证明同时增广实际中间域及两侧修补核，新增首末点均进入同一份实际匹配的容器，外匹配的端口损失由该份匹配统一计数。

因此若仍有 \(n=3b+2\) 配置，它必须满足 \(w=0,\ x<y\)，且

\[
\Omega\ne\varnothing,\quad \Psi\ne\varnothing,\quad
\alpha,\beta\in\{1,2\},\quad
u+v\le2-\max(\alpha,\beta),\quad r=s=0 .
\tag{23}
\]

若最大缺额为 \(2\)，两侧每纤维均只有一位 owner。若两侧缺额均为 \(1\)，额外 owner 总数至多一。此处纯 owner 临界类仍待排除。

以 \(Q_{\rm cap}=N_{\rm sig}(7,6,7),\ F_{\rm cap}=N_{\rm sig}(7,7,7)\) 记全模型最大允许人口，沿用既有工作界和精确归约

\[
Q_{\rm cap}\le3b+2,\qquad F_{\rm cap}=Q_{\rm cap}+1\le3b+3 .
\tag{24}
\]

采用既有工作输入 \(b=25\)，767、777 的全模型工作上界仍分别为 \(77\)、\(78\)。全局 \(76/77\) 尚待证明。

本文新增结论均为 **unreviewed / unaccepted**。转写与交叉核对属于同会话工作，旧依赖沿用各自保证层级。本轮只转写、核对本地文档，未调用外部 Claude 或外传材料，未执行科研代码、枚举、SAT、solver 或 proof 重放。
