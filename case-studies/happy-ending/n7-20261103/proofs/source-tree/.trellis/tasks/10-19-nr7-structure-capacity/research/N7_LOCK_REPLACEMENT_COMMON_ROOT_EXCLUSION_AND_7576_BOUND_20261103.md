# N7 替锁排除共根与 75、76 人口工作上界

2026-11-03 · **同会话工作证明，unreviewed / unaccepted**。数学由主会话定稿，并经三位同会话数学协作者交叉核对。指定文档执行者负责转写与文档核验。

**参数定理。** 设 \(b\) 是 756 与换色 756 的共同有效整数人口上界。则完整有序 rank-3 signotope 的最大允许人口满足
\[
Q_{\rm cap}=N_{\rm sig}(7,6,7)\le3b,\qquad
F_{\rm cap}=N_{\rm sig}(7,7,7)=Q_{\rm cap}+1\le3b+1 .
\tag{1}
\]
取既有工作输入 \(b=25\)，得到 767、777 的全局人口工作上界 \(75,76\)。

## 1. 证明接口与依赖

实际单色路径按顶点数计长。完整 packet 公理保证路径对子序列遗传。767 禁 \(R_7,B_6,\mathrm{weak7}\)，756 禁 \(R_6,B_5,\mathrm{weak7}\)，换色 756 禁 \(R_5,B_6,\mathrm{weak7}\)。weak7 禁止同一对实际首末点之间的异色路径长度和达到 \(9\)，两路径内部可共享顶点。[完整模型、参数无关 M0 和容量输入](N7_7677_PROOF_OBLIGATION_AUDIT_20261103.md)

令 \(X\) 为任意 767 母体，\(n=|X|\)。\(S,T\) 分别为 ambient 红六的首、末点集，\(I=S\cap T,\ P=S\setminus T,\ Q=T\setminus S,\ D=X\setminus(S\cup T)\)。设 \(U,V\) 分别为实际 \(D\) 内红五的首、末点集，\(w=|U\cap V|,\ |D|=b+q\)。两侧 M0 核记为 \(H_L,H_R\)，左 owner \(A_H=H_L\cap S\)，右 owner \(B_H=H_R\cap T\)，并记 \(P_H=P\cap H_R\)。\(\Omega\subseteq T\) 是左锁集，\(\Psi\subseteq S\setminus H_R\) 是右锁集，\(\Gamma=(\Omega\cup\Psi)\cap I\)。旧基底 \(W=S\setminus\Omega,\ W'=T\setminus\Psi\) 用于下述 \(w=0\) 层。旧末根 \(\widehat E\) 收集所有实际红六末对中两点均在 \(W\) 的末根，旧首根 \(\widehat F\) 反向用 \(W'\) 定义。

| 依赖 | 输入和输出 |
| --- | --- |
| 参数无关 M0、加权界及增强根分类 | 已有 \(n+w\le3b+1\)。若 \(n=3b+1\)，则 \(w=0\)，且只余共同增强根 \(x_e=y_f=z\in I\setminus\Gamma\) 的接口。旧末根全不早于 \(z\)，旧首根全不晚于 \(z\)。[加权与增强根稿 §1–3](N7_WEIGHTED_BILATERAL_COMPENSATION_AND_ENLARGED_ROOTS_20261103.md) |
| 全供给覆盖与实际 owner 匹配 | 临界接口给每锁恰一位 owner，\(|B_H|=|\Psi|\)，全锁序 \(\Psi<z<\Omega\)，以及精确中性覆盖和两侧实际外端口。[全供给稿定理 A–C](N7_COMMON_ROOT_FULL_SUPPLY_COVER_AND_SATURATED_CORE_20261103.md) |
| 两侧满核与旧根排除 | \(J_-\) 是实际 \(b\) 点 756，且 \(z\notin\widehat E\cup\widehat F\)。因此每个旧末根都严格晚于 \(z\)。调用旧稿 §1–3 的满核身份和旧根引理。[旧根稿 §1–3](N7_OLD_ROOT_EXCLUSION_AND_CLEAN_COMMON_ROOT_CLOSURE_20261103.md) |
| 独立的 777 归约支路 | 以完整 packet 的合法 chart 删去 pivot 并换色给上界，反向加最左蓝点给下界，得到 \(F_{\rm cap}=Q_{\rm cap}+1\)。此等式只在 §4 结算时使用。[R20 §4](RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md) · [依赖审计 §1](N7_7677_PROOF_OBLIGATION_AUDIT_20261103.md) |

本稿先在临界接口内证明矛盾，再从已证的加权界取得人口界。旧根稿的 clean 侧排除与当时的双有锁余类只作历史定位。

## 2. 用右锁替换右 owner，加入共根

反设 \(n=3b+1\)，因而 \(w=0\)。令
\[
B=(I\cap(-\infty,z))\setminus\Psi,\qquad
A=(I\cap(z,\infty))\setminus\Omega .
\tag{2}
\]
\(L,R\) 是此前严格切分两侧的全部实际外供给端口。特别对任意 \(k\in R\)，有实际红六首对 \((s,k)\)，其中 \(s\in A\) 且 \(s>z\)。上一轮全供给等号给实际满核和精确中性覆盖
\[
J_-=P_H\sqcup B_H\sqcup B\sqcup(U\setminus L),\quad |J_-|=b,
\qquad
C_D=(U\setminus L)\sqcup(V\setminus R),\quad |C_D|=q.
\tag{3}
\]
\(C_D\) 击中实际 \(D\) 内的全部红五。两项不交由 \(w=0\) 保证。每个右锁有恰一位右 owner，记 \(d=|B_H|,\ p=|\Psi|=d\)。

在实际母体内取
\[
F=(J_-\setminus B_H)\sqcup\Psi\sqcup\{z\}
 =P_H\sqcup B\sqcup\Psi\sqcup(U\setminus L)\sqcup\{z\}.
\tag{4}
\]
这里 \(F\) 表示一个实际点域。\(P_H,U\setminus L\) 在 \(H_R\) 内，\(\Psi\subseteq S\setminus H_R\) 在其外。\(B\) 按定义避开 \(\Psi\)，且 \(U\setminus L\subseteq D\) 与所有 \(S\) 角色不交。共根 \(z\) 在 \(I\) 内，避开 \(J_-\) 和 \(\Psi\)。所以式 (4) 真的是不交并，且
\[
|F|=b-d+p+1=b+1 .
\tag{5}
\]

\(F\subseteq S\cup U\)。其中 \(S\) 点无 ambient 蓝五末点身份。否则在该点将入蓝五与出红六连接，蓝桥形成 \(B_6\)，红桥形成 \(R_7\)。\(U\) 点也无 ambient 蓝五末点身份，因为可接它在 \(D\) 内的实际出红五，蓝桥形成 \(B_6\)，红桥形成终于 \(D\) 的实际红六。故 \(F\) 无蓝五，且 weak7 禁形从母体继承。人口超过 \(b\)，756 容量迫一条实际 \(R_6(a_1,a_2,a_3,a_4,j,r)\) 在 \(F\) 内。因为 \(r\in T\)，其末点必在
\[
F\cap T=B\sqcup(\Psi\cap I)\sqcup\{z\},\qquad r\le z.
\tag{6}
\]
式 (6) 用 \(P_H\subseteq P\)、\(U\setminus L\subseteq D\) 以及全锁序 \(\Psi<z\)。

## 3. 实际末前驱的两种情形

**若 \(j\in S\)。** 此时 \(j<r\le z\)，而 \(\Omega\) 全在 \(z\) 右，故 \(j,r\) 都在 \(W=S\setminus\Omega\)。实际红六末对 \((j,r)\) 使 \(r\in\widehat E\)。但旧末根全严格晚于 \(z\)，矛盾。

**若 \(j\in U\setminus L\)。** 写 \(u_0=j\)。对任意 \(k\in R\)，取兑现 \(k\) 的实际首对 \((s,k)\)，\(s\in A\)。因
\[
u_0<r\le z<s<k,
\tag{7}
\]
实际末帽给 \(\chi(u_0,r,s)=B\)，实际首帽给 \(\chi(r,s,k)=B\)。于是 \(B_4(u_0,r,s,k)\) 是实际蓝四。任何 ambient 红五从 \(u_0\) 到 \(k\) 都会形成同端 weak7，故这种红五不存在。

因此 \(u_0\) 可从 (3) 的中性覆盖中删去。因为 \(w=0\)，\(u_0\in U\) 且 \(u_0\notin V\)。任何不从 \(u_0\) 启动的实际 \(D\) 内红五仍有原覆盖，从 \(u_0\) 启动的红五则只能终于 \(V\setminus R\)，也仍被覆盖。若 \(R=\varnothing\)，后一结论直接成立。若 \(q=0\)，\(u_0\in C_D\) 已矛盾。其余情形，\(C_D\setminus\{u_0\}\) 是实际 \(q-1\) 点覆盖。将它从 \(D\) 删去，得到
\[
|D\setminus(C_D\setminus\{u_0\})|=b+q-(q-1)=b+1 .
\tag{8}
\]
这个实际诱导域无红五，继承蓝六和 weak7 禁形，违反换色 756 容量。

**等价的实际红五见证。** 令 \(K=D\setminus C_D\)。它有 \(b\) 点且无红五。对上面被迫出现的 \(u_0\in U\setminus L\subseteq C_D\)，实际域 \(K\sqcup\{u_0\}=D\setminus(C_D\setminus\{u_0\})\) 有 \(b+1\) 点。它继承蓝六与 weak7 禁形，故换色 756 容量直接迫一条实际红五 \(P_0\) 完全在其中。\(C_D\) 覆盖全部 \(D\) 内红五的端点，而 \(P_0\) 避开 \(C_D\setminus\{u_0\}\)，故其一个实际端点必为 \(u_0\)。又 \(w=0\) 给 \(u_0\notin V\)，所以 \(u_0\) 必为 \(P_0\) 的首点。另一端点 \(k\) 属于 \(V\setminus C_D\subseteq R\)。若 \(R=\varnothing\)，被容量迫出的这个端点已经给出矛盾。否则取兑现 \(k\) 的实际右首对 \((s,k)\)。同一条 \(P_0\subseteq K\sqcup\{u_0\}\) 接合新迫出的末对 \((u_0,r)\) 和右首对 \((s,k)\)。由 (7)，两帽给 \(B_4(u_0,r,s,k)\)，与 \(P_0\) 共享实际首末点，违反 weak7。这里所需的端点相容性来自实际容量及精确端点覆盖。

\(F\subseteq S\cup(U\setminus L)\) 已穷尽末前驱两种情形，故整个共根临界接口不存在。这一论证用等人口替换和加入 \(z\) 迫出实际红六。它的末对同时面对全部实际右供给，用同端禁形回收一个中性覆盖点，兑现临界层所差的一单位容量。已有中间核及其端点容器保持原用途，新增矛盾发生在 (4) 和 (8) 的两个实际诱导域中。

## 4. 全局结算与保证范围

任意 767 母体先由既有 \(n+w\le3b+1\) 得 \(n\le3b+1\)。§2–3 排除等号层后，由整数性得 \(n\le3b\)。独立的 R20 合法 chart 归约给 \(F_{\rm cap}=Q_{\rm cap}+1\le3b+1\)。因此 (1) 成立。[R20 的实际删点与添点证明](RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md)

加权工作界仍为 \(n+w\le3b+1\)。合用两项可写为
\[
n\le\min(3b,\ 3b+1-w).
\tag{9}
\]
以既有 \(a=16,b=25\) 计，757、766、767、777 的人口工作上界依次为 **40、50、75、76**。其中 757、766 沿用 \(a+b-1,2b\)，本轮人口下降只发生在 767 和 777。\(b=25\) 继承已有人工接受及其原 same-family/provisional 保证。[历史容量输入](../../../../RESEARCH_SYNTHESIS_N7_20261103.md)

本稿排除了上一稿记录的双有锁余类，也覆盖无 owner 情形，因为在 \(p=d=0\) 时 (4) 仍是实际 \(b+1\) 点域。早期 \(76,77\) 及当时的开放余类按原状作为历史记录，现行工作界以本稿为准。[前轮 clean 侧更新](../../../../RESEARCH_SYNTHESIS_N7_20261103_CLEAN_CLOSURE_UPDATE.md)

新增工作证明仍为 **unreviewed / unaccepted**。同会话交叉核对尚未构成独立数学复审。本轮无外部 Claude 调用、科研运行、枚举、求解或历史证书重放。[文档核验回执](N7_7576_DOCUMENT_RECEIPT_20261103.md)
