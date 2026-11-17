# N7 共根层的旧根排除与 clean 侧闭合

2026-11-03 · **同会话工作证明，unreviewed / unaccepted**。数学由主会话推导，同会话协作者逐项反审，指定文档执行者负责转写和文档核验。

**旧根排除定理。** 在 \(n=3b+1\) 的共根临界余类中，\(z\notin\widehat E\cup\widehat F\)，无论两侧缺额及 owner 如何。因而 \(q\ge2\)。

**Clean 侧闭合定理。** 在同一临界层，若至少一侧 clean，则配置不存在。此结论适用于所有 \(q\) 及缺额，故该子类的 767 人口至多 \(3b\)。

## 1. 输入与依赖

沿用完整有序 rank-3 signotope。767 禁 \(R_7,B_6,\mathrm{weak7}\)，756 禁 \(R_6,B_5,\mathrm{weak7}\)，换色 756 禁 \(R_5,B_6,\mathrm{weak7}\)。weak7 禁止同一对实际首末点之间存在长度和至少为 \(9\) 的异色路径。\(b\) 为 756 与换色 756 的共同有效整数容量。令 \(S,T\) 为 ambient 红六源、末点集，\(I=S\cap T,\ P=S\setminus T,\ Q=T\setminus S,\ D=X\setminus(S\cup T)\)，且 \(|D|=b+q\)。\(U,V\) 是 \(D\) 内红五首、末点集。设 \(H_L,H_R\) 是缺额 \(\alpha,\beta\) 的实际 M0 核。记 \(A_H=H_L\cap S,\ B_H=H_R\cap T,\ P_H=P\cap H_R,\ Q_H=Q\cap H_L\)。左、右锁集分别为 \(\Omega\subseteq T,\ \Psi\subseteq S\)，并记 \(\Gamma=(\Omega\cup\Psi)\cap I\)。[参数无关 M0 与容量](N7_7677_PROOF_OBLIGATION_AUDIT_20261103.md)

固定 \(n=3b+1\) 的候选。加权界迫 \(w=|U\cap V|=0\)。已有内在共根 \(z=\min E_*=\max F_*\in I\setminus\Gamma\)，增强根极值 \(x_e=y_f=z\)，且 \(\mu=0\)。旧基底为 \(W=S\setminus\Omega,\ W'=T\setminus\Psi\)。旧根 \(\widehat E,\widehat F\) 分别收集全部 ambient 实际红六末对、首对的根，要求对应相邻对的两点都在 \(W,W'\) 内。增强末根 \(z\) 的右扇给 \(\chi(z,x,y)=R\) 对所有 \(z<x<y\in S\cup U\)，其中中点 \(x\) 可取任意合序 ambient 点。增强首根有反向扇。[加权界、增强根与内在根](N7_WEIGHTED_BILATERAL_COMPENSATION_AND_ENLARGED_ROOTS_20261103.md)

上一稿的全供给等号排除了多 owner 纤维，故两侧纤维余量 \(u=v=0\)。实际 owner 匹配与两侧饱和外供给进一步给
\[
\Omega\subseteq(z,\infty),\qquad \Psi\subseteq(-\infty,z).
\tag{1}
\]
取 \(B=(I\cap(-\infty,z))\setminus\Psi,\ A=(I\cap(z,\infty))\setminus\Omega\)。写 \(Z_-=D\cap\operatorname{Src}_{R_5}(H_R)\) 与 \(Z_+=D\cap\operatorname{End}_{R_5}(H_L)\)，原基础核为 \(K_-=P_H\sqcup B_H\sqcup Z_-\)、\(K_+=Q_H\sqcup A_H\sqcup Z_+\)。在实际域 \(K_-\sqcup B,\ K_+\sqcup A\) 中收集全部红六末对前驱和首对后继，所得端口集分别为 \(L\subseteq Z_-\)、\(R\subseteq Z_+\)。每个 \(j\in L\) 有实际末对 \((j,r)\) 且 \(r\in B\)，每个 \(k\in R\) 有实际首对 \((s,k)\) 且 \(s\in A\)。[全供给等号、饱和中性核与 owner 匹配](N7_COMMON_ROOT_FULL_SUPPLY_COVER_AND_SATURATED_CORE_20261103.md)

本稿只调用该稿定理 A–C。依赖顺序为参数无关 M0 与增强共根分类，继而全供给覆盖等号与 owner 匹配，再到下文满核和旧根排除，最后用旧根排除关闭 clean 侧。上一稿定理 D 的满侧根数界是可比较的旧结论，不用于下文推导。

## 2. 两侧满核及 owner 相邻对限制

**任意 owner 相邻对。** 对每个 \(b_0\in B_H\)，上一稿的实际中间匹配给 \(R_5(j\to b_0)\)，其中 \(j\in L\)。取一个兑现 \(j\) 的实际外末对 \((j,r)\)，有 \(r<z\)。若任何实际红六首对 \((s,b_0)\) 有 \(s>r\)，则两帽给 \(B_4(j,r,s,b_0)\)，与该红五同端，违反 weak7。故 \(s\le r<z\)，不要求 \(s\in I\)。反序，对每个 \(a_0\in A_H\)，任意实际红六末对 \((a_0,r)\) 必满足 \(r\ge s>z\)，其中 \(s\) 可取兑现匹配端口的实际右首根。一般相邻对允许 \(r=s\)，这里只需 \(r>z\)。

**满 756 核。** 定义
\[
J_-=(K_-\sqcup B)\setminus L,\qquad
J_+=(K_+\sqcup A)\setminus R .
\tag{2}
\]
上一稿全供给等号给 \(|K_-\sqcup B|=b+|L|,\ |K_+\sqcup A|=b+|R|\)。删 \(L\) 击中左域全部红六，删 \(R\) 击中右域全部红六。两域原本无蓝五，所以 \(J_-,J_+\) 都是实际满 \(b\) 点 756。用 \(Z_-\setminus L=U\setminus L,\ Z_+\setminus R=V\setminus R\)，它们的实际身份为
\[
J_-=P_H\sqcup B_H\sqcup B\sqcup(U\setminus L),\qquad
J_+=Q_H\sqcup A_H\sqcup A\sqcup(V\setminus R).
\tag{3}
\]
特别 \(z\) 不在二者内，且 \(J_-\) 避开 \(\Psi\)，\(J_+\) 避开 \(\Omega\)。已有精确 \(q\) 点中性覆盖
\[
C_D=(U\setminus L)\cup(V\setminus R),\qquad |C_D|=q.
\tag{4}
\]
此覆盖击中 \(D\) 内全部实际红五。

## 3. 共根从两族旧根中排除

假设 \(z\in\widehat F\)，则存在实际首对 \((z,t_0)\)，其中 \(t_0\in T\)，且 \(t_0>z\)。若 \(t_0\in B_H\)，§2 的任意 owner 首对限制会要求 \(z<z\)，矛盾。因此 \(t_0\) 为右侧普通点。它有 ambient 出红五，故由强普通点性质没有 ambient 入蓝五。由 (3)，\(J_-\) 的 \(T\) 点只在 \(B_H\) 或 \(B\)，后者均早于 \(z\)，所以 \(t_0\notin J_-\)。由 (1)，\(t_0\notin\Psi\)。

\(J_-\sqcup\{t_0\}\) 无蓝五。终于 \(K_-\) 点的 ambient 蓝五需要倒数第二点在 \(\Psi\)，该锁集仍缺席；\(B\subseteq S\) 无 ambient 蓝五末点；\(t_0\) 的末点身份已排除。因此 \(b+1\) 点实际域必须含红六。它一定使用 \(t_0\)，因为 \(J_-\) 自身无红六。若末点在 \(P_H\) 或 \(U\setminus L\)，则不在 \(T\)；若在 \(B_H\)，则需要缺席的 \(\Psi\) 源；若在 \(B\)，则末点早于 \(z<t_0\)，无法使用 \(t_0\)。故红六只能为
\[
(g_1,g_2,g_3,g_4,g_5,t_0),\qquad g_1,\ldots,g_5\in J_-.
\tag{5}
\]
若 \(g_1<z\)，实际首对 \((z,t_0)\) 的帽给 \(B_3(g_1,z,t_0)\)，与该红六同端矛盾。\(g_1=z\) 也不可能，故 \(g_1>z\)。第二点 \(g_2\notin B_H\)，因为实际首对 \((g_1,g_2)\) 的首点晚于 \(z\)。也有 \(g_2\notin B\)，因为 \(g_2>g_1>z\)。因此 \(g_2\in P_H\cup(U\setminus L)\subseteq S\cup U\)。

增强末根 \(z\) 的右扇给 \(\chi(z,g_1,g_2)=R\)。把 \(z\) 前接到 (5) 的前五点，得到实际 \(R_6(z,g_1,g_2,g_3,g_4,g_5)\)，终于 \(J_-\) 中晚于 \(z\) 的点 \(g_5\)。它不能终于 \(P_H\) 或 \(U\setminus L\)，也不能终于早于 \(z\) 的 \(B\)。若终于 \(B_H\)，首点必须在 \(\Psi\)，而 \(z\notin\Psi\)，仍矛盾。故 \(z\notin\widehat F\)。反序同证 \(z\notin\widehat E\)。

由 \(u=v=0\)，旧基底人口分别为 \(b+1+\alpha,\ b+1+\beta\)。分别删除全部旧末根、旧首根即击中各基底内全部红六，因而容量给 \(|\widehat E|\ge1+\alpha,\ |\widehat F|\ge1+\beta\)。旧根都在 \(I\setminus\Gamma\)，因为 \(\widehat E\) 按定义避 \(\Omega\) 且不早于 \(z\)，\(\widehat F\) 按定义避 \(\Psi\) 且不晚于 \(z\)，再用 (1)。两族现在不交且都避开 \(z\in I\setminus\Gamma\)。由 \(|I\setminus\Gamma|=q+1+\alpha+\beta\) 得
\[
2+\alpha+\beta
\le|\widehat E|+|\widehat F|
\le |I\setminus\Gamma|-1=q+\alpha+\beta,
\qquad q\ge2.
\tag{6}
\]
这里不要求任一侧满。它严格加强只在满侧扣除旧根得到的预算，并同时排除所有 \(q=0,1\) 的临界配置。

## 4. 任一 clean 侧的共根配置排除

\(J_-\sqcup\{z\}\) 有 \(b+1\) 点且无蓝五，因为 \(\Psi\) 缺席，\(B\subseteq S\) 与 \(z\in S\) 都无 ambient 入蓝五。由容量，它含实际红六，且必使用 \(z\)。该红六末点不能在 \(P_H\) 或 \(U\setminus L\)，不能在需要 \(\Psi\) 源的 \(B_H\)，也不能在早于 \(z\) 的 \(B\)，故必须终于 \(z\)。

若末前驱在 \(P_H\cup B\)，它在 \(S\) 且避开 \(\Omega\)，因为 \(P_H\subseteq P\)，而 \(B\) 全在 \(z\) 左侧。\(z\) 也避开 \(\Omega\)。实际末对两点同在 \(W\)，会触发 \(z\in\widehat E\)，已由 §3 排除。若末前驱为 \(u_0\in U\setminus L\)，则有实际末对 \((u_0,z)\)。任意 \(k\in R\) 都有实际首对 \((s,k)\)，且 \(s>z\)。两帽给 \(B_4(u_0,z,s,k)\)。因此任何实际红五从 \(u_0\) 到 \(k\) 都违反 weak7。

于是 \(u_0\) 可从 (4) 的精确中性覆盖中删去。对 \(D\) 内任意实际红五，若不从 \(u_0\) 启动，其原有覆盖不受影响，因为 \(U\cap V=\varnothing\)，\(u_0\) 无末点角色。若从 \(u_0\) 启动，则其末点在 \(V\setminus R\)，仍被覆盖。这给一个只含 \(q-1\) 点的实际覆盖。删后余域有 \(b+1\) 点、无红五，继承蓝六和 weak7 禁形，违反换色 756 容量。

所以 \(J_-\sqcup\{z\}\) 中每条被容量迫出的实际红六的末前驱都必须在 \(B_H\)。反向 \(J_+\sqcup\{z\}\) 中每条实际红六的第二点都必须在 \(A_H\)。只要 \(B_H=\varnothing\) 或 \(A_H=\varnothing\) 就矛盾。完整 M0 接口中，一侧 clean 等价于该侧无 owner，也等价于无锁，因为 owner 与锁有实际唯一性和供给。clean 侧可有正缺额，故这项排除覆盖满侧和有缺额的 clean 侧。

## 5. 双有锁余类与人口账

若仍有候选，则两侧都有 owner，且都是单例纤维。由 §4 的实际红六，有一个 \(b_0\in B_H\) 使 \((b_0,z)\) 为实际末对，一个 \(a_0\in A_H\) 使 \((z,a_0)\) 为实际首对。其实际锁和这些点满足
\[
\psi(b_0)<b_0<z<a_0<\omega(a_0).
\tag{7}
\]
这是余类中的实际路径约束，双有锁类仍待排除。

由既有全局 \(n+w\le3b+1\) 与本稿临界排除，至少一侧 clean 的 767 子类满足 \(n\le3b=75\)（\(b=25\)）。无条件 757、766、767、777 的人口工作上界仍为 **40、50、76、77**，全局 75、76 尚未得到。现行 \(b=25\) 沿用历史人工接受及其原 same-family/provisional 保证。[既有全局人口账](../../../../RESEARCH_SYNTHESIS_N7_20261103_COMMON_ROOT_UPDATE.md)

本轮新增数学保持 **unreviewed / unaccepted**。未进行独立数学复审、外部 Claude 调用、科研代码运行、枚举、求解或历史证书重放。[文档回执](N7_OLD_ROOT_CLEAN_CLOSURE_DOCUMENT_RECEIPT_20261103.md)
