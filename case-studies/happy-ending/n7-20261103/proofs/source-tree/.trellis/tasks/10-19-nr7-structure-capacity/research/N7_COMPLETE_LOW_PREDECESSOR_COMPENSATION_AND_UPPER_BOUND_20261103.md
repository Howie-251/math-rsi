# N7 完整低前驱补偿与无条件人口工作上界

2026-11-03。本文新增工作证明均为 **unreviewed / unaccepted**。数学由主会话定稿，推导和交叉核对属于同会话工作。指定 native gpt-6.1-sol/high 执行者负责转写与文档核对。

**完整低前驱补偿定理。** 在 \(n=3b+2,\ w=0\) 层，完整双向 M0 接口下的严格交错 \(x<y\) 不可能。证明允许任意符合接口的锁纤维大小和核缺额，覆盖缺额 \(3\) 的情形。

**全局工作推论。** 设 \(b\) 是 756 与换色 756 的共同有效容量。最大允许人口满足 \(Q_{\rm cap}=N_{\rm sig}(7,6,7)\le3b+1\) 及 \(F_{\rm cap}=N_{\rm sig}(7,7,7)=Q_{\rm cap}+1\le3b+2\)。

## 1. 完整 M0 接口与基础修补核

设 \(X\) 为有序 rank-3 signotope 的 767 母体，\(\chi\) 是三元组颜色。四点 packet 中三元组按字典序排列，颜色至多改变一次。\(R_j,B_j\) 表示实际红、蓝 \(j\) 点路径，路径对子序列遗传。weak7 禁止同一对实际首末点之间存在长度和至少为 \(9\) 的红、蓝路径。767 禁 \(R_7,B_6,\mathrm{weak7}\)，766 禁 \(R_6,B_6,\mathrm{weak7}\)，756 禁 \(R_6,B_5,\mathrm{weak7}\)，换色 756 禁 \(R_5,B_6,\mathrm{weak7}\)。ambient 指 \(X\)，带域的路径角色只按该实际子域计算。

- 加权工作界、完整 M0、根工具、非交错根序与 onefull 排除见 §1–2。[共同中间匹配与加权界稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMMON_MIDDLE_COMPATIBILITY_AND_WEIGHTED_BOUND_20261103.md>)
- 实际 M0 换核与头尾替换见 §2–3，锁纤维代表见 §4–5。[锁纤维归一化稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCK_FIBER_NORMALIZATION_AND_DOUBLE_OMEGA_EXCLUSION_20261102.md>)
- 双 clean 有单独的增广中间域证明，保留为同会话交叉证据。[双 clean 排除稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_AUGMENTED_MIDDLE_CLEAN_CLASS_EXCLUSION_20261103.md>)
- 早期缺额、普通供给及混合类的分阶段排除见下稿。本文统一定理覆盖该稿所留的纯 owner 类。[有锁临界类排除稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCKED_DEFECT_AND_ORDINARY_SUPPLY_CLASS_EXCLUSIONS_20261103.md>)
- \(b=25\) 的工作输入及既有精确归约 \(F_{\rm cap}=Q_{\rm cap}+1\) 沿用研究综述中的来源和保证层级。[既有研究综述](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_SYNTHESIS_N7_20261103.md>)

### 1.1 人口、根与两侧端口

写 \(n=|X|\)，并定义

\[
\begin{aligned}
S&=\operatorname{Src}_{R_6}(X),& T&=\operatorname{End}_{R_6}(X),& I&=S\cap T,\\
P&=S\setminus T,& Q&=T\setminus S,& D&=X\setminus(S\cup T),\\
|D|&=b+q,&
w&=|\operatorname{Src}_{R_5}(D)\cap\operatorname{End}_{R_5}(D)|.
\end{aligned}
\tag{1}
\]

以下证明取 \(n=3b+2,\ w=0\) 且根严格交错。完整 M0 给实际 766 核 \(H_L,H_R\)，大小分别为 \(2b-\alpha,2b-\beta\)。临界层归一化后的正缺额在 \(1\) 至 \(3\) 之间，以下交会论证无需使用这个数值范围。

左 owner 集 \(A_H=H_L\cap S\subseteq P\)，左锁集 \(\Omega\subseteq T\setminus H_L\)，记 \(a=|A_H|,\ o=|\Omega|\)。每个左 owner \(a_0\) 有 ambient 入红五及出蓝五。其全部 ambient 出 \(R_6\) 末点与出 \(B_5\) 的第二点同为唯一锁 \(\omega(a_0)\in\Omega\)。\(\Omega\) 恰为所有从 \(H_L\) 启动的 ambient \(R_6\) 的末点集，各锁都有实际 owner。反序，右 owner 集 \(B_H=H_R\cap T\subseteq Q\)，右锁集 \(\Psi\subseteq S\setminus H_R\)，记 \(d=|B_H|,\ p=|\Psi|\)。每个右 owner 有 ambient 出红五及入蓝五，全部入 \(R_6\) 的首点及入 \(B_5\) 的倒数第二点同为唯一右锁。置 \(u=a-o\ge0,\ v=d-p\ge0\)。

交叉锁交集 \(A_H\cap\Psi\) 为空。若 \(a_0\) 属于此交集，右锁的实际供给给 \(R_6(a_0\to b_0)\) 且 \(b_0\in B_H\)。两侧唯一锁迫 \(b_0=\omega(a_0)\)、\(a_0=\psi(b_0)\)。于是以 \((a_0,b_0)\) 开头的出蓝五与以同一对结束的入蓝五可沿该对接成 \(B_8\)，继承 \(B_6\)，矛盾。反序得 \(B_H\cap\Omega=\varnothing\)。结合两核补集分别为 \((S\setminus A_H)\cup\Omega\)、\((T\setminus B_H)\cup\Psi\)，有

\[
D_{\rm all}:=H_L\cap H_R=D\sqcup A_H\sqcup B_H .
\tag{2}
\]

令 \(\delta=|\Omega\cap I|,\ \varepsilon=|\Psi\cap I|\)。按上述补集计数，

\[
\begin{aligned}
|S|&=b+2+\alpha-o+a+\delta,\qquad
|T|=b+2+\beta-p+d+\varepsilon,\\
i:=|I|&=|S|+|T|+|D|-n
       =q+2+\alpha+\beta+u+v+\delta+\varepsilon .
\end{aligned}
\tag{3}
\]

原完整根基底为 \(W=S\setminus\Omega,\ W'=T\setminus\Psi\)。\(\widehat E\) 收集全部实际 ambient \(R_6\) 末对中两点均在 \(W\) 的末根，\(\widehat F\) 收集全部实际 ambient \(R_6\) 首对中两点均在 \(W'\) 的首根。两族均在 \(I\)。写 \(x=\min\widehat E,\ y=\max\widehat F\)，当前 \(x<y\) 且 \(y\notin\Psi\)。实际末对 \((z,r)\) 给末帽 \(\chi(z,r,s)=B\) 对所有 \(s>r\)，实际首对 \((s,t)\) 给首帽 \(\chi(r,s,t)=B\) 对所有 \(r<s\)。下文使用的标准根扇为

\[
\begin{array}{ll}
\chi(x,z,t)=R & \text{若 }x<z<t,\ t\in S,\\
\chi(t,z,y)=R & \text{若 }t<z<y,\ t\in T .
\end{array}
\tag{4}
\]

中点 \(z\) 可取任意满足顺序的 ambient 点。正向 M0 已消去全部 mixed 点，故 \(W\) 中非 owner 若有 ambient 入 \(R_5\)，就无 ambient 出 \(B_5\)。下文使用这项 M0 普通点性质，它给出对整个 \(X\) 的蓝五限制。反向完整端口则禁止一条 ambient \(B_5\) 的末点有 ambient 出 \(R_5\) 且末对两点同在 \(W'\)。

**尾替换。** 给定实际 \(R_6(v_1,v_2,v_3,v_4,v_5,v_6)\)，若 \(v_4\) 有 ambient 入 \(R_5\) 且 \(v_5<y\)，取入红五末前驱 \(d_0\) 和原根 \(y\) 的实际首对 \((y,t_y)\subseteq W'\)。若 \(\chi(d_0,v_4,v_5)=R\)，入红五可接 \(v_5,v_6\) 成 \(R_7\)，故该桥为蓝。若 \(\chi(v_4,v_5,y)=B\)，首帽 \(\chi(v_5,y,t_y)=B\) 给 \(B_5(d_0,v_4,v_5,y,t_y)\)。末对 \((y,t_y)\) 在 \(W'\)，且 \(t_y\) 有 ambient 出红五，违反完整反端口。故 \(\chi(v_4,v_5,y)=R\)，可将原红六末点替为 \(y\)。此处 \(t_y\) 可以是右 owner。

### 1.2 基础实际 756 核

令 \(C=\operatorname{End}_{R_5}(H_L),\ C'=\operatorname{Src}_{R_5}(H_R)\)，\(Z_+=C\cap D,\ Z_-=C'\cap D,\ c_\pm=|Z_\pm|\)，\(Q_H=Q\cap H_L,\ P_H=P\cap H_R\)。取

\[
\begin{aligned}
K_+&=C\cup Q_H\cup A_H=Z_+\sqcup Q_H\sqcup A_H\subseteq H_L,\\
K_-&=C'\cup P_H\cup B_H=Z_-\sqcup P_H\sqcup B_H\subseteq H_R .
\end{aligned}
\tag{5}
\]

\(K_+\) 内无 \(R_6\)。若 \(C\) 中一点启动 ambient \(B_5\)，将其与 \(H_L\) 内入红五连接，蓝桥给 \(B_6\)，红桥给从 \(H_L\) 启动的红六，故蓝五第二点属于 \(\Omega\)。左 owner 的出蓝五同样锁在 \(\Omega\)，而 \(Q_H\subseteq T\) 无 ambient 出蓝五。于是 \(\Omega\) 缺席保证 \(K_+\) 无 \(B_5\)。且 \(K_+\) 各点均有 ambient 入红五，对 \(C,A_H\) 由定义，对 \(Q_H\) 由入红六。反序 \(K_-\) 无 \(R_6,B_5\)，其点均有 ambient 出红五，潜在蓝五的倒数第二点只在缺席的 \(\Psi\)。两核均为实际 756。由 \(H_L=D\sqcup Q_H\sqcup A_H,\ H_R=D\sqcup P_H\sqcup B_H\) 得

\[
\kappa_+=b-|K_+|=q+\alpha-c_+\ge0,\qquad
\kappa_-=b-|K_-|=q+\beta-c_-\ge0 .
\tag{6}
\]

## 2. 收集全部低前驱并增广右核

用 \(W_{\rm alt}=S\setminus A_H\)。令 \(\mathcal R\) 收集所有实际 ambient \(R_6\) 末对 \((z,r)\) 中的末前驱 \(z\)，要求 \(z,r\in W_{\rm alt}\) 且 \(r<y\)。因为实际末根同时在 \(T\)，且 \(I\subseteq W_{\rm alt}\)，条件等价于 \(z\in S\setminus A_H,\ r\in I,\ r<y\)。特别地，允许低末根 \(r\in\Omega\)。

若 \(z\in T\)，根 \(y\) 的左扇给 \(\chi(z,r,y)=R\)，与实际末帽矛盾。故 \(\mathcal R\subseteq P\setminus A_H\)，且所有前驱早于 \(y\)。它们在原基底 \(W\)，因为 \(\Omega\subseteq T\)。每个实际末前驱都有 ambient 入红五，故由 M0 的普通点性质，无 ambient 出蓝五。它们在 \(H_L\) 外，因而与 \(K_+\) 不交。记 \(\tau=|\mathcal R|\)，对每个 \(z\in\mathcal R\) 固定一条对应的实际低末对 \((z,r_z)\)，其中 \(r_z<y\)。

令 \(K_+^*=K_+\sqcup\mathcal R\)。旧核的潜在出蓝五需要第二点在 \(\Omega\)，而新增 \(\mathcal R\subseteq P\) 既避开 \(\Omega\)，又无 ambient 出蓝五，故增广核无 \(B_5\)。若有 \(R_6\)，源必在 \(A_H\cup\mathcal R\)。\(A_H\) 的红六需要终于缺席的 \(\Omega\)。若从 \(z\in\mathcal R\) 启动，末帽与 weak7 迫红六末点不晚于 \(r_z\)。全域各点有 ambient 入红五，第五点早于 \(y\)，故可尾替换到 \(y\)，与 \(B_3(z,r_z,y)\) 同端违反 weak7。此论证允许 \(r_z\in\Omega\)，所选低末根只用于末帽。于是 \(K_+^*\) 为实际 756 且

\[
\kappa_+^*:=b-|K_+^*|=\kappa_+-\tau\ge0 .
\tag{7}
\]

令 \(\widetilde W=S\setminus(A_H\cup\mathcal R)\)，\(\widetilde E\) 收集两点均在 \(\widetilde W\) 的全部实际 ambient \(R_6\) 末对的末根。若 \(\widetilde E\) 有低于 \(y\) 的根，相应末前驱本应属于 \(\mathcal R\)，矛盾。因此 \(\widetilde E\cap(-\infty,y)=\varnothing\)。只需再记 \(e_y=\mathbf1[y\in\widetilde E]\)。

## 3. 不对称切分与两侧实际相邻对

取

\[
\begin{aligned}
B&=\bigl((I\cap(-\infty,y])\setminus\Psi\bigr)
       \setminus\bigl(\{y\}\cap\widetilde E\bigr),\\
A&=(I\cap(y,\infty))\setminus(\Omega\cup\Psi).
\end{aligned}
\tag{8}
\]

集合 \(B\) 与颜色及路径记号中的 \(B\) 由上下文区分。左域允许不晚于 \(y\) 的左锁点，只需避开 \(\Psi\)。右域同时避开两侧锁。定义

\[
\delta_l=|\Omega\cap I\cap(-\infty,y]|,\quad
\delta_h=|\Omega\cap I\cap(y,\infty)|,\quad
\rho_h=|\Omega\cap\Psi\cap(y,\infty)|.
\tag{9}
\]

交叉锁交集在 \(I\) 内。计数先删 \(\Psi\cap I\)，再删尚未扣除的晚于 \(y\) 的左锁，最后按 \(e_y\) 删 \(y\)。因为 \(y\notin\Psi\)，而 \(y\) 可在 \(\Omega\)，有

\[
N:=|A|+|B|
=i-\varepsilon-\delta_h+\rho_h-e_y
=q+2+\alpha+\beta+u+v+\delta_l+\rho_h-e_y .
\tag{10}
\]

### 3.1 左扩域允许 owner 端口

\(K_-\cup B\) 无 \(B_5\)，因为 \(\Psi\) 缺席，且新增 \(B\subseteq S\) 无 ambient 入 \(B_5\)。若域内 \(R_6\) 终于 \(B_H\)，其首点必须是缺席的 \(\Psi\) 点。旧核其余点非 \(T\)。故所有实际红六终于 \(B\)，末前驱位于 \(Z_-,P_H,B_H\) 或 \(B\)。若前驱在 \(P_H\setminus(A_H\cup\mathcal R)\) 或 \(B\)，则末前驱、末根都在 \(\widetilde W\)。这会触发 \(\widetilde E\)，但低于 \(y\) 的根不存在，而 \(y\) 若属于 \(\widetilde E\) 已从 \(B\) 删去。余下实际左端口只在 \(Z_-\cup A_H\cup\mathcal R\cup B_H\)。

用该扩域内全部实际红六末对建图。若匹配不足 \(|B|-\kappa_-\)，König 定理给更小的顶点覆盖。删相应实际点后余域仍大于 \(b\)，且所有红六均被击中，余域为 756，矛盾。因此取一份至少 \(|B|-\kappa_-\) 条的左匹配。

舍去 \(\mathcal R\) 前驱边至多 \(\tau\) 条。实际域若缺少其中某些前驱，只会减少舍弃数。再舍去 \(B_H\) 前驱边，设舍弃数为 \(\epsilon_L\)。若实际末对的前驱在 \(B_H\subseteq T\) 且末根严格早于 \(y\)，根 \(y\) 的左扇与末帽矛盾。故这些边只能终于 \(y\)，匹配的根无重复，所以

\[
\epsilon_L\le\mathbf1[y\in B],\qquad
e_y+\epsilon_L\le1 .
\tag{11}
\]

余下实际左匹配至少有 \(|B|-\kappa_--\tau-\epsilon_L\) 条，端口在 \(Z_-\cup A_H\)，末根均不晚于 \(y\)。这些 owner 左端口由扩域中的实际末对兑现。

### 3.2 右扩域获得同量的增广容量

\(K_+^*\cup A\) 无 \(B_5\)，因为 \(\Omega\) 缺席，\(A\subseteq T\) 无 ambient 出蓝五。红六若从 \(A_H\) 启动，需要末点在缺席的 \(\Omega\)。若从 \(\mathcal R\) 启动，低帽仍迫末点早于 \(y\)。新增 \(A\) 的点也有 ambient 入红五，故尾替换仍给矛盾。因而全部实际红六从 \(A\) 启动。

设实际首对为 \((s,t)\)，\(s\in A\)。若 \(t\in Q_H\cup A\)，则 \(s,t\in W'\)，会触发 \(\widehat F\) 中晚于 \(y\) 的根。若 \(t\in A_H\subseteq S\)，因 \(x<s<t\)，根 \(x\) 的标准右扇给 \(\chi(x,s,t)=R\)，而实际首帽给蓝，矛盾。若 \(t\in\mathcal R\)，则 \(t<y<s\)，不合顺序。因此全部实际右首对为 \(A\to Z_+\)。用全部首对及容量覆盖论证，得到至少 \(|A|-\kappa_+^*=|A|-\kappa_++\tau\) 条的右匹配。

记 \(p_h=|\Psi\cap(y,\infty)|\)。对每个 \(\psi\in\Psi\) 且 \(\psi>y\)，选该右纤维的一位代表 \(b_\psi\in B_H\)。将末对为 \((\psi,b_\psi)\) 的入蓝五与从 \(b_\psi\) 启动的出红五连接。蓝桥会给 \(B_6\)，故红桥给实际红六首对 \((\psi,b_\psi)\)。将这些 \(p_h\) 条实际首对加到右匹配，锁根在 \(A\) 外，代表点与 \(Z_+\) 不交，且不同纤维的代表不同，故无角色冲突。右侧所有首根严格晚于 \(y\)。左侧直接使用 §3.1 的实际匹配。

## 4. 全 owner 中间域与补偿恒等式

在实际 \(D_{\rm all}\) 内取全部红五的首末端点图。由 \(D_{\rm all}\subseteq H_L\cap H_R\)，源容器和末点容器分别为

\[
Z_-\sqcup A_H\sqcup(C'\cap B_H),\qquad
Z_+\sqcup B_H\sqcup(C\cap A_H).
\tag{12}
\]

每个左纤维的最早 owner 不在 \(C\)。若它有 \(H_L\) 内的入红五，接其出蓝五时蓝桥给 \(B_6\)，红桥给从更早的 \(H_L\) 点启动并终于同一左锁的红六。该首点属于 \(A_H\) 且在同一纤维，违反最早性。反序，每个右纤维的最晚 owner 不在 \(C'\)。因此

\[
|C\cap A_H|\le a-o=u,\qquad |C'\cap B_H|\le d-p=v .
\tag{13}
\]

两容器大小分别至多 \(c_-+a+v,\ c_++d+u\)。

\(D_{\rm all}\) 有 \(b+q+a+d\) 个实际点。置

\[
m=\max(q+a+d,0),\qquad \mu=\min(q+a+d,0).
\tag{14}
\]

若 \(m>0\) 且最大端点匹配不足 \(m\)，König 定理给少于 \(m\) 个角色顶点的覆盖。删去对应实际点后，余域仍超过 \(b\)，且无 \(R_5\)，继承其他禁形，违反换色 756 容量。角色副本对应同一实际点时，实际删点只会更少。固定一份恰 \(m\) 条的实际红五匹配，\(m=0\) 时取空匹配。首容器中未覆盖数至多 \(c_-+a+v-m\)，末容器中未覆盖数至多 \(c_++d+u-m\)。这些上界包含全部未覆盖的实际外端口。容器中的额外角色无需各自兑现外供给。

沿这同一份中间匹配运输 §3 的两侧外匹配。先舍弃各侧未被中间匹配覆盖的端口，再用两侧所覆盖的中间边数之和减去 \(m\)，得到交会条数

\[
\begin{aligned}
\ell
&\ge N-\kappa_- -\tau-\epsilon_L-\kappa_++\tau+p_h\\
&\qquad -(c_-+a+v-m)-(c_++d+u-m)-m\\
&=2+\delta_l+\rho_h+p_h-e_y-\epsilon_L-\mu\\
&\ge1 .
\end{aligned}
\tag{15}
\]

等式代入 (6)、(10)、(14)，使用 \(m=q+a+d-\mu\)。左侧至多损失 \(\tau\) 条低前驱边，右核增广使右侧容量下界增加 \(\tau\)，两项精确抵消。末式由 (11)、\(\delta_l,\rho_h,p_h\ge0\) 及 \(\mu\le0\)。

若 \(m=0\)，正交会下界已与空匹配矛盾。否则一个交会提供实际中间 \(R_5(z\to t)\)、实际左末对 \((z,r)\) 和实际右首对 \((s,t)\)，且 \(z<r\le y<s<t\)。由末帽 \(\chi(z,r,s)=B\) 与首帽 \(\chi(r,s,t)=B\) 得 \(B_4(z,r,s,t)\)。蓝四与中间红五同实际首末点，总长度 \(4+5=9\)，违反 weak7。完整严格交错类排除。

## 5. 临界层全覆盖与参数界

由既有加权工作界 \(n+w\le3b+2\)，若 \(n=3b+2\) 则 \(w=0\)。既有双向 canonical 核的联合预算 \(n+w\le3b+5-\eta\) 在该层给每侧缺额至多 \(3\)。实际 M0 换核消去 mixed 点，保持 \(D\)，且缺额不增。对归一化后的完整接口，任一缺额为零时是 fullstandard，已由既有 onefull 排除。两侧正缺额时，\(x\ge y\) 由既有非交错根序排除，\(x<y\) 由本文排除。人口 \(3b+2\) 的全部情况均已覆盖，故由整数性得到

\[
Q_{\rm cap}=N_{\rm sig}(7,6,7)\le3b+1,\qquad
F_{\rm cap}=N_{\rm sig}(7,7,7)=Q_{\rm cap}+1\le3b+2 .
\tag{16}
\]

采用既有工作输入 \(b=25\)，全模型的 767、777 人口工作上界分别为 \(76\)、\(77\)，各比此前 \(77\)、\(78\) 下降一。既有加权工作界仍为 \(n+w\le3b+2\)。双 clean 的单独排除以及有锁临界层的分阶段排除都纳入这一次人口下降，早期文稿的残余目录及数值保留为各阶段的历史记录。

## 6. 证明策略与保证状态

原基底 \(W=S\setminus\Omega\) 的低根集合看不到落在 \(\Omega\) 的低末根。仅用普通左端口，还会舍去实际中间域已包含的 owner。本文恢复全部普通低末对，允许实际左末对使用 \(A_H\)，并在包含全部 owner 的实际中间域中统一计数。右修补核增加的容量恰抵左侧低前驱损失，最终无需分别穷尽锁纤维类型。owner 与锁直接换位可能产生 mixed 点，后续 M0 归一化可能把它换回。本文的交会来自实际路径和实际容量。

后续的核查重点是本稿及承重依赖的独立审查，随后可检验界的锐性与进一步下降到 \(3b\) 所需的结构。

全部新增工作结论为 **unreviewed / unaccepted**。数学推导、交叉核对及文档转写均属同会话工作，旧依赖沿用各自保证层级。文档检查仅覆盖文件一致性。本轮未调用外部 Claude 或外传材料，未执行科研代码、枚举、SAT、solver 或 proof 重放。
