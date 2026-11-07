# N7 加权补偿、双向间隙与增强根序

2026-11-03 · **同会话工作证明，unreviewed / unaccepted**。数学由主会话定稿，指定文档执行者负责转写与核验。

**全局加权定理。** 对任意完整 767 母体 \(X\)，设 \(b\) 是 756 与换色 756 的共同有效整数容量，\(w\) 是下文定义的实际中性域 through 数。则
\[
n+w\le 3b+1.
\tag{1}
\]

**增强根排除定理。** 对参数无关的完整双向 M0 接口，若 \(t=n+w-3b\ge1\)，严格交错、严格分离、落在锁集中的共根全部排除。其余共根情形只有在 \(t=1\)、共根不在两锁集、中间人口相对 \(b\) 的缺额截断为零，且 \(I\) 内的左锁都在共根右侧、右锁都在共根左侧时，才未被下文排除。特别在 \(n=3b+1\) 的人口临界层，\(w=0\)，只余这类共根。“共根不在两锁集”容许配置在别处有锁。

## 1. 实际域、参数和同一份中间匹配

模型沿用完整有序 rank-3 signotope。四点 packet 按字典序至多换色一次，实际单色路径对子序列遗传。767 禁 \(R_7,B_6,\mathrm{weak7}\)，766 禁 \(R_6,B_6,\mathrm{weak7}\)，756 禁 \(R_6,B_5,\mathrm{weak7}\)，换色 756 禁 \(R_5,B_6,\mathrm{weak7}\)。weak7 比较同一对实际首末点的两条异色路径，长度和至少 \(9\)。[证明义务审计 §1–2](N7_7677_PROOF_OBLIGATION_AUDIT_20261103.md)

令 \(n=|X|\)。除指定诱导域的路径外，首末身份均在母体 \(X\) 中计算。记
\[
\begin{aligned}
S&=\operatorname{Src}_{R_6}(X),\quad T=\operatorname{End}_{R_6}(X),\quad I=S\cap T,\\
P&=S\setminus T,\quad Q=T\setminus S,\quad D=X\setminus(S\cup T),\quad |D|=b+q,\\
U&=\operatorname{Src}_{R_5}(D),\quad V=\operatorname{End}_{R_5}(D),\quad C_0=U\cap V,\quad w=|C_0|,\\
\sigma&=n-3b,\qquad t=\sigma+w .
\end{aligned}
\tag{2}
\]

使用审计稿 §2 的参数无关 M0 换核。左、右核 \(H_L,H_R\) 是包含 \(D\) 的实际 766，人口分别为 \(2b-\alpha,2b-\beta\)。左 owner 集 \(A_H=H_L\cap S\subseteq P\)，右 owner 集 \(B_H=H_R\cap T\subseteq Q\)，大小分别为 \(a,d\)。每位左 owner 有 ambient 入红五与出蓝五，其全部出红六末点及出蓝五第二点唯一锁向 \(\Omega\subseteq T\setminus H_L\) 中一点。反序得到右锁集 \(\Psi\subseteq S\setminus H_R\)，及每位右 owner 的实际出红五、入蓝五和唯一锁。每锁都有实际供给。置 \(o=|\Omega|,\ p=|\Psi|,\ u=a-o,\ v=d-p\)，后两数非负。M0 的强普通点性质是，非 owner 的 \(S\) 点若有 ambient 入红五，就无 ambient 出蓝五。右侧反序。

交叉锁交集 \(A_H\cap\Psi\) 与 \(B_H\cap\Omega\) 为空。交叉重合将令两侧锁同一实际红六的首末点，出蓝五与入蓝五可沿这一对接成 \(B_8\)，违反 \(B_6\) 禁形。由两核补集 \((S\setminus A_H)\cup\Omega\)、\((T\setminus B_H)\cup\Psi\)，得
\[
\begin{aligned}
D_{\rm all}&=H_L\cap H_R=D\sqcup A_H\sqcup B_H,\\
i=|I|&=q+\sigma+\alpha+\beta+u+v+\delta+\varepsilon,\\
\delta&=|\Omega\cap I|,\qquad \varepsilon=|\Psi\cap I|,\qquad
\Gamma=(\Omega\cup\Psi)\cap I,\qquad \rho=|\Omega\cap\Psi|.
\end{aligned}
\tag{3}
\]
式 (3) 使用 \(|I|=|S|+|T|+|D|-n\)。两锁交集都在 \(I\)。[原统一补偿 §1.1](N7_COMPLETE_LOW_PREDECESSOR_COMPENSATION_AND_UPPER_BOUND_20261103.md)

记 \(C=\operatorname{End}_{R_5}(H_L)\)、\(C'=\operatorname{Src}_{R_5}(H_R)\)、\(Z_+=C\cap D,\ Z_-=C'\cap D,\ c_\pm=|Z_\pm|\)，并记 \(Q_H=Q\cap H_L,\ P_H=P\cap H_R\)。基础核为
\[
\begin{aligned}
K_+&=Z_+\sqcup Q_H\sqcup A_H,\qquad
K_-=Z_-\sqcup P_H\sqcup B_H,\\
\kappa_+&=b-|K_+|=q+\alpha-c_+\ge0,\qquad
\kappa_-=b-|K_-|=q+\beta-c_-\ge0 .
\end{aligned}
\tag{4}
\]
它们在各自 766 核内。\(K_+\) 各点有 ambient 入红五。若 \(C\) 中一点有出蓝五，与核内入红五接桥，蓝桥给 \(B_6\)，红桥迫蓝五第二点在 \(\Omega\)。\(A_H\) 的出蓝五也锁在 \(\Omega\)，\(Q_H\subseteq T\) 无 ambient 出蓝五。故 \(K_+\) 为实际 756；\(K_-\) 反序同理，其点均有 ambient 出红五，潜在蓝五的倒数第二点必须在 \(\Psi\)。两式由实际人口计数。[原统一补偿 §1.2](N7_COMPLETE_LOW_PREDECESSOR_COMPENSATION_AND_UPPER_BOUND_20261103.md)

**公共中间域。** \(M=D_{\rm all}\setminus C_0\) 是人口为 \(b+q+a+d-w\) 的实际 766。令
\[
m=\max(q+a+d-w,0),\qquad \mu=\min(q+a+d-w,0).
\tag{5}
\]
取 \(M\) 中全部实际红五的首末点二部图。若匹配不足 \(m>0\)，König 定理给少于 \(m\) 个角色的顶点覆盖。删除相应实际点后，余域仍超过 \(b\) 且无红五，违反换色 756 容量。角色副本若对应同一实际点，只会减少实际删点。固定恰 \(m\) 条实际边的匹配，\(m=0\) 时取空匹配，其源、末像 \(J_U,J_V\) 各有 \(m\) 点，分别落在
\[
\mathcal U=(Z_-\setminus C_0)\sqcup A_H\sqcup(C'\cap B_H),
\qquad
\mathcal V=(Z_+\setminus C_0)\sqcup B_H\sqcup(C\cap A_H).
\tag{6}
\]
因为每个左纤维最早 owner 不在 \(C\)，每个右纤维最晚 owner 不在 \(C'\)，有 \(|C\cap A_H|\le u,\ |C'\cap B_H|\le v\)。例如，若最早左 owner 有核内入红五，接出蓝五时蓝桥给 \(B_6\)，红桥则从更早的同纤维 owner 启动红六，违反最早性。又 \(C_0\subseteq Z_+\cap Z_-\)，所以对容器内的任何实际供应端口，两侧未覆盖数至多
\[
c_--w+a+v-m,\qquad c_+-w+d+u-m.
\tag{7}
\]
外部两份匹配沿这一份中间匹配运输。各侧已覆盖的端口分别一一对应中间边。两侧已覆盖边数之和减 \(m\) 下界控制共用中间边数。容器包含固定中间匹配的像及所需外端口。容器中额外的点可以没有实际中间红五首末角色。[审计稿 §3–4](N7_7677_PROOF_OBLIGATION_AUDIT_20261103.md)

**实际端口与根。** 旧完整基底为 \(W=(S\setminus\Omega)\cup C_0,\ W'=(T\setminus\Psi)\cup C_0\)。\(\widehat E\) 收集全部实际红六末对两点同在 \(W\) 的末根，\(\widehat F\) 收集全部实际红六首对两点同在 \(W'\) 的首根。根都在 \(I\)。\(|W|-b=t+\alpha+u,\ |W'|-b=t+\beta+v\)，而基底无 \(B_5\)，所以 \(t\ge1\) 时容量迫实际红六，两根族均非空。令 \(x=\min\widehat E,\ y=\max\widehat F\)。

任一实际末对 \((j,r)\) 有末帽 \(\chi(j,r,z)=B\) 对所有 \(z>r\)，任一实际首对 \((s,k)\) 有首帽 \(\chi(z,s,k)=B\) 对所有 \(z<s\)。根扇分别给 \(\chi(r,z,v_0)=R\) 对 \(r<z<v_0\in S\cup U\)，以及 \(\chi(u_0,z,s)=R\) 对 \(u_0<z<s,\ u_0\in T\cup V\)。中点可取任意合序 ambient 点。反色桥由帽形成蓝四，再保原相邻对延蓝五，与完整端口冲突。若实际红六的第四点有 ambient 入红五、第五点早于有效首根，则可将其末点替换为该首根。反序，当第三点有 ambient 出红五、第二点晚于有效末根时，可替换首点。两种替换都使用完整端口，允许实际帽的相邻点是 owner。[原统一补偿 §1.1](N7_COMPLETE_LOW_PREDECESSOR_COMPENSATION_AND_UPPER_BOUND_20261103.md) · [共同中间稿 §1、§3](N7_COMMON_MIDDLE_COMPATIBILITY_AND_WEIGHTED_BOUND_20261103.md)

## 2. 双向间隙补偿

**引理。** 若 \(t\ge1\)，在同一母体上，只要一个有效末根 \(x\) 严格早于一个有效首根 \(y\)，就得到矛盾。此处有效指分别有实际末帽、首帽，且相应完整扇、头替换、尾替换均适用。

选严格间隙 \(x<c<y\)，\(c\) 不在点集内。定义 \(\mathcal R\) 为全部实际红六末对 \((j,r)\) 的前驱，要求 \(r\in I,\ r<c,\ j\in(S\setminus A_H)\cup C_0\)。反向定义 \(\mathcal Q\) 为全部实际红六首对 \((s,k)\) 的后继，要求 \(s\in I,\ s>c,\ k\in(T\setminus B_H)\cup C_0\)。由 \(y\) 左扇，\(\mathcal R\) 避开 \(T\cup C_0\)，故 \(\mathcal R\subseteq P\setminus A_H\) 且 \(\mathcal R<c\)。由 \(x\) 右扇，\(\mathcal Q\subseteq Q\setminus B_H\) 且 \(\mathcal Q>c\)。各 \(\mathcal R\) 点有 ambient 入红五，M0 给无 ambient 出蓝五；各 \(\mathcal Q\) 点有 ambient 出红五，M0 给无 ambient 入蓝五。

令 \(\tau_R=|\mathcal R|,\ \tau_Q=|\mathcal Q|\)。\(\mathcal R\) 与 \(H_L\) 不交，\(\mathcal Q\) 与 \(H_R\) 不交。若红六从 \(\mathcal R\) 的点启动，对应低末帽与 weak7 迫其末点不晚于该低根。全域点均有 ambient 入红五，故尾替换到 \(y\) 后与原帽给出的同端蓝三冲突。\(A_H\) 源的红六需要缺席的 \(\Omega\)，其余点无源身份。旧点的蓝五须用 \(\Omega\)，新增点无 ambient 出蓝五，故 \(K_+\sqcup\mathcal R\) 为实际 756。反向高帽、头替换证明 \(K_-\sqcup\mathcal Q\) 为实际 756：若一条红六终于 \(k\in\mathcal Q\)，取其相应高首对 \((s_k,k)\)，帽与 weak7 迫其首点不早于 \(s_k>c>x\)，并可将首点换为 \(x\)，与同端蓝三冲突。故 \(\tau_R\le\kappa_+,\ \tau_Q\le\kappa_-\)。

切分仅避开本侧的蓝五锁，取
\[
B=(I\cap(-\infty,c))\setminus\Psi,\qquad
A=(I\cap(c,\infty))\setminus\Omega .
\tag{8}
\]
两扩域分别为 \(K_-\sqcup\mathcal Q\sqcup B,\ K_+\sqcup\mathcal R\sqcup A\)。实际人口不重叠，因为原核和增广点在 \(D\sqcup P\sqcup Q\)，切分点域在 \(I\)。左域无蓝五，\(\Psi\) 缺席，\(\mathcal Q\) 与 \(B\) 的点无 ambient 入蓝五。右域反序无蓝五。两侧容许对侧锁点。

左域实际红六若终于 \(B_H\) 则需要 \(\Psi\) 源；若终于 \(\mathcal Q\)，所有点均有 ambient 出红五。高帽迫该红六的源不早于对应的 \(s_k>c>x\)，足以施行头替换 \(x\)。这一步对 \(B\) 中其他点与 \(x\) 的相对位置无要求。故末点只能在 \(B\)。末前驱在 \(B_H\) 或 \(B\) 属于 \(T\)，在 \(C_0\) 属于 \(V\)，均由 \(y\) 左扇排除。前驱在 \(\mathcal Q>c\) 则违顺序。\(P_H\setminus A_H\) 的前驱都属于 \(\mathcal R\)，其余实际端口在 \((Z_-\setminus C_0)\cup A_H\)。左扩域人口为 \(b-\kappa_-+\tau_Q+|B|\)。以全部末对建图，容量给至少 \(|B|-\kappa_-+\tau_Q\) 条实际匹配，删去 \(\mathcal R\) 端口边至多 \(\tau_R\)，所以左供给至少
\[
|B|-\kappa_-+\tau_Q-\tau_R .
\tag{9}
\]

右域若从 \(A_H\) 启动需要缺席锁，从 \(\mathcal R\) 启动则由低帽、尾替换 \(y\) 排除。全部实际红六从 \(A\) 启动。第二点若在 \(A_H\)、\(A\) 或 \(C_0\)，由 \(x\) 右扇排除，在 \(\mathcal R<c\) 则违顺序。\(Q_H\setminus B_H\) 的后继都属于 \(\mathcal Q\)，其余端口在 \((Z_+\setminus C_0)\cup B_H\)。容量给至少 \(|A|-\kappa_++\tau_R\) 条实际首对匹配，删去 \(\mathcal Q\) 端口边至多 \(\tau_Q\)，所以右供给至少
\[
|A|-\kappa_++\tau_R-\tau_Q .
\tag{10}
\]
这次切分不需要添锁边，也无切分点的根损失。负的匹配下界仍可使用，实际匹配数至少为零。

令 \(\delta_l=|\Omega\cap I\cap(-\infty,c)|\)、\(\varepsilon_h=|\Psi\cap I\cap(c,\infty)|\)。由 (3)、(8) 得 \(N=|A|+|B|=q+\sigma+\alpha+\beta+u+v+\delta_l+\varepsilon_h\)。两侧增广与删边精确相消。扣 (7) 并在同一份中间匹配上交会，
\[
\begin{aligned}
\ell
&\ge N-\kappa_--\kappa_+
 -(c_--w+a+v-m)-(c_+-w+d+u-m)-m\\
&=t+\delta_l+\varepsilon_h-\mu\ge t\ge1 .
\end{aligned}
\tag{11}
\]
\(m=0\) 时已矛盾。其余情况，一个交会给实际链 \(j<r<c<s<k\) 的两端帽，构成 \(B_4(j,r,s,k)\)，与中间同端 \(R_5(j\to k)\) 违反 weak7。

## 3. 增强根序与共根接口

用含 \(C_0\) 的加权基底 \(W,W'\) 定义 \(\widehat E,\widehat F\)，再取
\[
\begin{aligned}
E^+&=\widehat E\cup
 \{r\in I:\text{某实际红六末对为 }(j,r),\ j\in T\},\\
F^+&=\widehat F\cup
 \{s\in I:\text{某实际红六首对为 }(s,k),\ k\in S\},\\
x_e&=\min E^+,\qquad y_f=\max F^+.
\end{aligned}
\tag{12}
\]
新增末对的前驱 \(j\in T\) 无 ambient 出蓝五，新增首对的后继 \(k\in S\) 无 ambient 入蓝五。对新增末根，原右扇的反设仍由末帽成蓝四，再保首对延为从 \(j\) 启动的蓝五，矛盾。对新增首根，左扇反序。尾替换的蓝桥分支会产生终于 \(k\) 的蓝五，新增首对用 \(k\in S\) 直接排除。新增末对的头替换反序。因而这些根都是 §2 的有效根，无需它们避开 \(\Omega\) 或 \(\Psi\)。

若 \(x_e<y_f\)，§2 直接给矛盾。若 \(x_e>y_f\)，取间隙 \(y_f<c<x_e\)，令 \(B=(I\cap(-\infty,c))\setminus\Gamma,\ A=(I\cap(c,\infty))\setminus\Gamma\)。使用未增广的实际扩域 \(K_-\sqcup B,\ K_+\sqcup A\)，它们无蓝五。左域所有红六终于 \(B\)。若末前驱在 \(P_H\cup B\cup C_0\)，末对两点在 \(W\)，触发 \(\widehat E\) 的根早于 \(x_e\)。若前驱在 \(B_H\subseteq T\)，则触发 \(E^+\) 的根早于 \(x_e\)。故左端口只在 \(Z_-\setminus C_0\)。右域所有红六从 \(A\) 启动；若第二点在 \(Q_H\cup A\cup C_0\)，触发 \(\widehat F\)，若在 \(A_H\subseteq S\)，触发 \(F^+\)，均与 \(y_f\) 矛盾。故右端口只在 \(Z_+\setminus C_0\)。

两扩域用全部实际相邻对图给至少 \(|B|-\kappa_-\)、\(|A|-\kappa_+\) 条匹配。保守地沿用 (7) 的全容器扣除数。严格间隙时 \(N=|A|+|B|=|I\setminus\Gamma|=q+\sigma+\alpha+\beta+u+v+\rho\)，故
\[
\ell\ge N-\kappa_--\kappa_+
 -(c_--w+a+v-m)-(c_+-w+d+u-m)-m
 =t+\rho-\mu\ge1 .
\tag{13}
\]
交会产生的矛盾同 §2。若 \(x_e=y_f=z\)，在 \(z\) 作严格切分，同样定位纯普通端口。若 \(z\in\Gamma\)，原计数已删 \(z\)，所以 (13) 仍成立。两外根严格位于 \(z\) 两侧，\(z\) 本身无需同时属于 \(W,W'\)。若 \(z\notin\Gamma\)，严格切分额外删一个根，得到
\[
\ell\ge t+\rho-1-\mu .
\tag{14}
\]
由于 \(t\ge1,\ \rho\ge0,\ \mu\le0\)，式 (14) 只在 \(t=1,\ \rho=0,\ \mu=0\) 时不给正下界。先给出全局加权界，再收紧剩余共根情形。

**全局加权结算。** 若 \(t\ge2\)，严格交错由 (11) 排除，严格分离和有锁共根由 (13) 排除，无锁共根由 (14) 排除。因此任意实际 767 母体都有 \(t\le1\)，给出 (1)。这一证明链直接使用参数无关 M0 和实际端点匹配。代 \(b=25\) 得 \(n+w\le76\)，\(w\ge1\) 子类满足 \(n\le75\)。

**共同实际根的双向补偿。** 现在取 \(x_e=y_f=z\notin\Gamma\)，以同一实际点 \(z\) 分别提供有效末根和有效首根。设 \(c=z\)，沿 §2 从所有实际末对 \((j,r)\) 收集 \(r\in I,\ r<z,\ j\in(S\setminus A_H)\cup C_0\) 的前驱 \(\mathcal R\)，从所有实际首对 \((s,k)\) 收集 \(s\in I,\ s>z,\ k\in(T\setminus B_H)\cup C_0\) 的后继 \(\mathcal Q\)。左扇只用 \(j<r<z\)，右扇只用 \(z<s<k\)。因此仍有 \(\mathcal R\subseteq P\setminus A_H,\ \mathcal R<z\) 及 \(\mathcal Q\subseteq Q\setminus B_H,\ \mathcal Q>z\)。低帽给源在 \(\mathcal R\) 的红六末点不晚于相应低根，高帽给末点在 \(\mathcal Q\) 的红六首点不早于相应高根，分别严格早于或晚于 \(z\)。故尾替换或头替换到 \(z\) 仍适用，各自形成同端蓝三与红六的 weak7。M0 给新增普通点相应的蓝五限制，所以 \(K_+\sqcup\mathcal R\) 与 \(K_-\sqcup\mathcal Q\) 仍为实际 756。

切分 \(B=(I\cap(-\infty,z))\setminus\Psi,\ A=(I\cap(z,\infty))\setminus\Omega\)。\(z\in I\) 在 \(K_\pm\)、中间域 \(M\) 及普通增广集 \(\mathcal R,\mathcal Q\) 外，又被严格切分从 \(B,A\) 排除。左扩域避开 \(\Psi\) 且新增点无 ambient 入蓝五，右扩域反向避开 \(\Omega\) 且新增点无 ambient 出蓝五。左扩域红六只能终于 \(B\)，因为 \(B_H\) 的锁源缺席，\(\mathcal Q\) 的末点由上述头替换排除。前驱在 \(B_H\cup B\cup C_0\) 与 \(z\) 的左扇冲突，在 \(\mathcal Q>z\) 则违顺序，来自 \(P_H\setminus A_H\) 的前驱必在 \(\mathcal R\)。右扩域反序只可能从 \(A\) 启动，第二点在 \(A_H\cup A\cup C_0\) 与 \(z\) 的右扇冲突，在 \(\mathcal R<z\) 违顺序，来自 \(Q_H\setminus B_H\) 的后继必在 \(\mathcal Q\)。因此同 §2 的实际删点论证给匹配下界 \(|B|-\kappa_-+\tau_Q-\tau_R,\ |A|-\kappa_++\tau_R-\tau_Q\)，其余端口仍在 (6) 的容器内。

令 \(\delta_l=|\Omega\cap I\cap(-\infty,z)|,\ \varepsilon_h=|\Psi\cap I\cap(z,\infty)|\)。由于 \(z\) 不在两锁集，人口恰比 §2 的计算少一个共根，
\[
N=|A|+|B|=q+\sigma+\alpha+\beta+u+v+\delta_l+\varepsilon_h-1 .
\]
两侧 \(\tau_R,\tau_Q\) 的增广与剪枝照样相消。由 (7) 在同一份 \(M\) 匹配上交会，得
\[
\begin{aligned}
\ell
&\ge N-\kappa_--\kappa_+
 -(c_--w+a+v-m)-(c_+-w+d+u-m)-m\\
&=t-1+\delta_l+\varepsilon_h-\mu .
\end{aligned}
\tag{CR}
\]
若下界为正且 \(m=0\)，即与空匹配矛盾。否则实际交会给 \(j<r<z<s<k\)，两帽给同端蓝四与中间红五，违反 weak7。于是 \(t=1\) 时，只要 \(\delta_l+\varepsilon_h-\mu>0\) 即排除该配置。对余下配置，\(\mu=0,\ \delta_l=\varepsilon_h=0\)。这将 \(I\) 内的左锁都推到 \(z\) 右侧，\(I\) 内的右锁都推到 \(z\) 左侧，因此 \(\rho=0\)。两锁集在 \(I\) 外的位置未用于这项结论。两位同会话数学协作者逐项核对了共根切分、相邻对定位及此补偿式。

由 (1)，当 \(n=3b+1\) 时必有 \(w=0\)。结合 (14) 与 (CR)，剩余人口临界接口为
\[
\begin{gathered}
t=1,\qquad w=0,\qquad x_e=y_f=z\in I\setminus\Gamma,\qquad \mu=0,\\
\Omega\cap I\subseteq(z,\infty),\qquad
\Psi\cap I\subseteq(-\infty,z)\qquad(\rho=0).
\end{gathered}
\tag{15}
\]

**共根可加入实际核。** 在 \(z\in I\setminus\Gamma\) 时，\(M^+=D_{\rm all}\sqcup\{z\}\) 是实际 766。若有红六，其源只可能在 \(A_H\cup\{z\}\)，末点只可能在 \(B_H\cup\{z\}\)。\(A_H\) 源需要域外 \(\Omega\)，\(B_H\) 末点需要域外 \(\Psi\)。两锁均避开 \(D_{\rm all}\) 与 \(z\)。余下要求一条红六从 \(z\) 到 \(z\)，违严格点序。其余禁形随诱导限制继承。

增广域的实际红五端点像可能变大。特别是 \(R_5(j\to z)\) 和 \(R_5(z\to k)\) 无法直接推出所需的 \(R_5(j\to k)\)，因为连接处的连续三元组没有相应的同色保证。式 (6)–(7) 只对旧中间域证明。下一人口单位需要为 \(M^+\) 重新证明相容的端点扣除或补上一份可与两侧同接的中间供给。式 (15) 尚未排除，因此 767、777 的人口工作界仍为 \(76,77\)。

**内在根与策略审计。** 在 (15) 的人口临界余类中，\(w=0\)，定义只依赖母体的两族实际红六根
\[
\begin{aligned}
E_*&=\{r\in I:\text{某实际红六末对为 }(j,r),\ j\in S\cup T\},\\
F_*&=\{s\in I:\text{某实际红六首对为 }(s,k),\ k\in S\cup T\}.
\end{aligned}
\]
此时 \(W=S\setminus\Omega,\ W'=T\setminus\Psi\)，故 \(E^+\subseteq E_*\)、\(F^+\subseteq F_*\)，而 \(z\) 同时属于两族。若 \(E_*\) 有 \(r<z\)，取实际末对 \((j,r)\)。若 \(j\in T\)，按增强根定义 \(r\in E^+\)，矛盾。否则 \(j\in P\)，故 \(j\notin\Omega\)。\(r\in I\) 且 \(r<z\)，由 \(\Omega\cap I\subseteq(z,\infty)\) 又有 \(r\notin\Omega\)。两点同在 \(W\)，从而 \(r\in\widehat E\)，也矛盾。反向若 \(s>z\)，其后继在 \(S\) 则直接触发 \(F^+\)，否则后继在 \(Q\) 避开 \(\Psi\)，且 \(\Psi\cap I\subseteq(-\infty,z)\) 给 \(s\notin\Psi\)。两点同在 \(W'\)，触发 \(\widehat F\)，矛盾。于是
\[
\min E_*=\max F_*=z.
\]
这说明余类的增强极值由母体全部实际路径决定。只更换 canonical 核、锁集或纤维代表，无法移动最终极值；换核若要产生新收益，须提供其他实际矛盾。待证入口是直接排除临界人口下的内在共同极值，或在 \(M^+\) 上证明实际红五匹配增广与两侧供给相容，补足一单位实际供给。

## 附录 A. 任意 \(w\) 的单向补偿交叉核对

取 \(t\ge2\)。先设 \(x<y\)。令 \(W_{\rm alt}=(S\setminus A_H)\cup C_0\)，从全部实际红六末对 \((j,r)\) 中收集前驱 \(j\) 到 \(\mathcal R\)，要求 \(j,r\in W_{\rm alt}\) 且 \(r<y\)。根 \(y\) 的左扇覆盖 \(T\cup V\)，故 \(j\in T\) 或 \(j\in C_0\) 均与末帽冲突。于是 \(\mathcal R\subseteq P\setminus A_H\)，在 \(H_L\) 外。各点有实际入红五，M0 给无 ambient 出蓝五。低根可以落在 \(\Omega\)。

令 \(\tau=|\mathcal R|\)。\(K_+^*=K_+\sqcup\mathcal R\) 无蓝五，旧潜在蓝五仍需 \(\Omega\)，新普通点不出蓝五。若有红六，源只能在 \(A_H\) 或 \(\mathcal R\)。前者需缺席的锁，后者取对应的实际低末对 \((j,r_j)\)。其帽与 weak7 迫末点不晚于 \(r_j<y\)，而全域点都有 ambient 入红五。尾替换为 \(y\) 后与 \(B_3(j,r_j,y)\) 同端，矛盾。故 \(K_+^*\) 是实际 756，\(\tau\le\kappa_+\)。令 \(\widetilde W=W_{\rm alt}\setminus\mathcal R\)，由定义其全部实际末对的根族 \(\widetilde E\) 无根低于 \(y\)。设 \(e_y=\mathbf1[y\in\widetilde E]\)，取
\[
B=\bigl((I\cap(-\infty,y])\setminus\Psi\bigr)
     \setminus(\{y\}\cap\widetilde E),\qquad
A=(I\cap(y,\infty))\setminus(\Omega\cup\Psi).
\tag{16}
\]

**左外匹配。** \(K_-\sqcup B\) 不交，避开 \(\Psi\)，新增 \(B\subseteq S\) 无 ambient 入蓝五，故全域无蓝五。所有实际红六只能终于 \(B\)，因为 \(K_-\) 唯一有终点角色的 \(B_H\) 需要 \(\Psi\) 源。若末前驱在 \(B\)、\(C_0\) 或 \(P_H\setminus(A_H\cup\mathcal R)\)，它与末根均在 \(\widetilde W\)，会触发已排除或已删掉的 \(\widetilde E\) 根。因此全部实际末对的端口落在 \((Z_-\setminus C_0)\cup A_H\cup\mathcal R\cup B_H\)。用全部末对建图，实际删点覆盖后余域为 756，故容量与 König 给匹配至少 \(|B|-\kappa_-\) 条。删 \(\mathcal R\) 端口边至多 \(\tau\) 条。删 \(B_H\) 前驱边 \(\epsilon_L\) 条，这类前驱在 \(T\)，若末根严格低于 \(y\)，根扇与末帽冲突，因此只可能终于 \(y\)。匹配根无重复，故 \(e_y+\epsilon_L\le1\)，即使 \(y\in\Omega\) 也成立。所得左供给端口在 \((Z_-\setminus C_0)\cup A_H\)，边数至少
\[
|B|-\kappa_--\tau-\epsilon_L .
\tag{17}
\]

**右外匹配。** \(K_+^*\sqcup A\) 不交，避开 \(\Omega\)，新增 \(A\subseteq T\) 无 ambient 出蓝五，故全域无蓝五。源在 \(A_H\) 的红六需缺席锁；源在 \(\mathcal R\) 的红六仍被同一低帽和尾替换排除，因为新增 \(A\) 点亦有入红五。故所有实际红六从 \(A\) 启动。第二点在 \(Q_H\cup A\cup C_0\) 会使原 \(\widehat F\) 有根晚于 \(y\)，在 \(A_H\subseteq S\) 违根 \(x\) 的扇与首帽，在 \(\mathcal R\) 违顺序，故右供给只在 \(Z_+\setminus C_0\)。容量与 König 给至少 \(|A|-\kappa_++\tau\) 条边。再对每个 \(\psi\in\Psi\cap I\cap(y,\infty)\) 取一位实际右 owner \(b_\psi\)。其入蓝五末对 \((\psi,b_\psi)\) 接出红五，蓝桥给 \(B_6\)，故红桥兑现实际红六首对 \((\psi,b_\psi)\)。锁根在 \(A\) 外，各纤维代表不同，且 \(B_H\cap Z_+=\varnothing\)，可将这些实际首对加入右匹配。记 \(p_h=|\Psi\cap I\cap(y,\infty)|\)，所得端口在 \((Z_+\setminus C_0)\cup B_H\)，边数至少
\[
|A|-\kappa_++\tau+p_h .
\tag{18}
\]
外匹配在负数下界时可取空匹配，较弱的代数下界仍有效。

置 \(\delta_l=|\Omega\cap I\cap(-\infty,y]|\)，\(\rho_h=|\Omega\cap\Psi\cap(y,\infty)|\)。由 (3)、(16) 和 \(y\notin\Psi\)，
\[
N=|A|+|B|=q+\sigma+\alpha+\beta+u+v+\delta_l+\rho_h-e_y .
\tag{19}
\]
沿 §1 的同一份中间匹配，先各扣 (7)，再扣 \(m\) 得共用中间边数
\[
\begin{aligned}
\ell
&\ge |B|-\kappa_--\tau-\epsilon_L+|A|-\kappa_++\tau+p_h\\
&\qquad -(c_--w+a+v-m)-(c_+-w+d+u-m)-m\\
&=N-2q-\alpha-\beta+2w-a-d-u-v+m+p_h-\epsilon_L\\
&=t+\delta_l+\rho_h+p_h-e_y-\epsilon_L-\mu
 \ge t-1\ge1 .
\end{aligned}
\tag{20}
\]
\(\tau\) 的容量收益与删边损失恰相消。若 \(m=0\)，正下界已矛盾；否则得到一条实际中间 \(R_5(j\to k)\) 及实际末、首对 \((j,r),(s,k)\)，其中 \(j<r\le y<s<k\)。两帽给同端 \(B_4(j,r,s,k)\)，违反 weak7。

当 \(x\ge y\)，共同中间稿 §2 已对任意 \(t\ge2\) 建立非交错排除。它在 \(D_{\rm all}\setminus C_0\) 上用同一实际中间匹配，严格分离时用 owner 根序选割，合计至多丢一条 owner 边，共根时只丢共同根一次。相应交会下界为 \(t+\rho-1\ge1\)。这条路线结合上文的单向补偿，也能独立排除 \(t\ge2\)。它与 §2–3 的增强根证明采用同一实际中间匹配，作为对旧单向补偿的加权延伸。[非交错根序定理](N7_COMMON_MIDDLE_COMPATIBILITY_AND_WEIGHTED_BOUND_20261103.md)

同会话两位不同协作者分别重算了严格分离及有锁共根的交会式 (13)，并逐项核对了 §2 双向扩域、真实容量与删边补偿，未报告新缺口。该核对属于同会话局部数学核对。全部新增数学为 **unreviewed / unaccepted**。未进行独立复审、外部 Claude 调用、科研运行或历史证书重放。
