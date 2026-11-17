# 唯一 ambient 红六交叠点整类的严格容量界

日期：2026-11-06。

本文完整记录主会话冻结的参数化证明。数学由主会话与两位数学协作者逐步同会话推导并核回；指定 native Sol/high 执行者只做忠实文档整理及引用检查。保证层级为 **same-session、未外审、未接受**，不是独立审查。用户禁止外部审查，本轮科研运行、求解与外审均为 0，不创建新 Goal。

本轮排除整个 75 点唯一交叠类，而非仅排除无外跨或极端端点子类。现行 757／766／767／777 全局工作界仍为 **40／49／75／76**；多交叠情形尚未排除，不能宣布全局 74／75。

## 1. 模型、容量与主定理

$X$ 是有限完整 ordered rank-3 signotope：所有递增三元组完整染红蓝；每个四点 packet 按 $abc,abd,acd,bcd$ 的次序至多变色一次。实际单色路径的长度按点数计，路径的有序子序列仍为同色路径。

767 母体指禁止 $B_6,R_7,\mathrm{weak7}$。weak7 禁止同一对**实际首末点**的异色路径长度和至少为 9，不要求内部不交。$N_{\rm sig}$ 记最大避免人口，不是 forcing threshold。

设 $b$ 是以下两类换色对偶短帽域的共同有效整数容量上界：

$$
\begin{array}{ll}
756:&\text{无 }B_5,R_6,\mathrm{weak7},\\
\text{换色 }756:&\text{无 }R_5,B_6,\mathrm{weak7}.
\end{array}
$$

并沿用 balanced 域（无 $B_6,R_6,\mathrm{weak7}$）的有效容量

$$
C\le2b-1.
$$

这项严格容量的原证明见[双色实际路径交替环与 balanced 严格容量](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n766-strict-capacity-20261105/PROOF.md>)。$b$ 不必最优，也不要求存在达到 $b$ 点的实际构造。旧进口保持其原有保证层级。

所有源、末身份均由同一 ambient $X$ 中的**全部实际红六**定义：

$$
S=\operatorname{Src}_{R_6}(X),\qquad
T=\operatorname{End}_{R_6}(X),\qquad I=S\cap T.
$$

**主定理。** 在上述模型与容量输入下，若 $I=\{z\}$，则

$$
\boxed{|X|\le3b-1.}
$$

特别地，取既有有效 $b=25$，整个唯一交叠类人口至多 74。

本定理不要求 $z$ 为极端端点、不要求无外跨红六、不要求 $D$ 排序，也不要求 $D\cup\{z\}$ 无红五。证明不先进口 $D$ 无红五或 $w=0$。

## 2. 基本端点禁配与唯一可能的取等人口

记

$$
P=S\setminus\{z\},\qquad Q=T\setminus\{z\},\qquad
D=X\setminus(S\cup T),\qquad n=|X|.
$$

$S$ 的任何点都不能结束 ambient $B_5$：若蓝五终于 $s\in S$，取其末前驱 $w$ 与从 $s$ 出发的实际红六第二点 $u$。桥 $\chi(w,s,u)$ 为红则前接得到 $R_7$，为蓝则延长得到 $B_6$，均矛盾。全序反向给出 $T$ 的任何点不能开始 ambient $B_5$。

因此 $P,Q$ 各无 $B_5$。$P$ 也无 $R_6$，否则其末点既在 $P$ 又在 $T$；$Q$ 无 $R_6$ 对偶。短帽容量给

$$
|P|\le b,\qquad |Q|\le b.
$$

删除全部实际源点命中每条红六，所以 $X\setminus S$ balanced，人口至多 $2b-1$；$X\setminus T$ 同理。因此

$$
n\le |S|+2b-1\le(b+1)+(2b-1)=3b.
$$

以下反设 $n=3b$。左右不等式均必须取等，得到

$$
|P|=|Q|=b,\qquad |S|=|T|=b+1,\qquad |D|=b-1.
$$

## 3. 完整参数无关 M0 的准确旧进口

调用[证明义务审计 §2：参数无关 M0 归一化](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7677_PROOF_OBLIGATION_AUDIT_20261103.md>)。该构造适用于任意实际 767 母体，不先要求 $w=0$，也不先要求某一人口临界层。本文仅使用以下完整性质。

### 3.1 左核与完整锁

同一 $X$ 中有包含 $D$ 的实际 balanced 核 $H_L$。令

$$
A_H=H_L\cap S\subseteq P,\qquad
\alpha=2b-|H_L|.
$$

收集从 $H_L$ 中点出发的**全部 ambient 实际 $R_6$** 的末点为锁集

$$
\Omega\subseteq T\setminus H_L.
$$

每个 owner $a\in A_H$ 都有 ambient 入 $R_5$、出 $B_5$。它的全部出红六末点及全部出蓝五第二点，均为同一个实际锁 $\omega(a)\in\Omega$；每个锁都有 owner 的实际供应。另有

$$
X\setminus H_L=(S\setminus A_H)\cup\Omega,
\qquad |\Omega|\le\alpha.
$$

强普通点性质为：$S\setminus\Omega$ 中非 owner 的点若有 ambient 入 $R_5$，则没有 ambient 出 $B_5$。

### 3.2 右核与完整反向锁

反序构造给同一母体中的实际 balanced 核 $H_R\supseteq D$，

$$
B_H=H_R\cap T\subseteq Q,\qquad
\beta=2b-|H_R|,\qquad
\Psi\subseteq S\setminus H_R.
$$

$\Psi$ 收集终于 $H_R$ 中点的全部 ambient 实际红六的源。每个右 owner 有 ambient 出 $R_5$、入 $B_5$；其全部入红六源及全部入蓝五末前驱均锁为同一个实际点，且每锁有 owner 的实际供应。并有

$$
X\setminus H_R=(T\setminus B_H)\cup\Psi,
\qquad |\Psi|\le\beta.
$$

强普通点性质反序为：$T\setminus\Psi$ 中非右 owner 的点若有 ambient 出 $R_5$，则没有 ambient 入 $B_5$。

两核属于同一母体的实际诱导域，可以同时使用；完整锁针对全部路径，不只针对某个选定见证。

## 4. 严格 balanced 容量迫单 owner、单锁及满短帽

记

$$
a_c=|A_H|,\quad o=|\Omega|,\quad
u=a_c-o\ge0,\quad \delta=|\Omega\cap I|.
$$

每锁有 owner 供应且每 owner 只有一个锁，故 $u\ge0$。在 §2 的取等人口下，实际补集恒等式给

$$
3b-|H_L|=(b+1-a_c)+o-\delta.
$$

代入 $|H_L|=2b-\alpha$，整理为

$$
\alpha+u+\delta=1.
$$

由于 $H_L$ 是实际 balanced 核，严格容量给 $\alpha\ge1$。三个量均为非负整数，故

$$
\alpha=1,\qquad u=0,\qquad\delta=0.
$$

再由 $o\le\alpha=1$，得到

$$
|A_H|=|\Omega|\in\{0,1\},\qquad\Omega\subseteq Q.
$$

右侧对偶得到

$$
\beta=1,\qquad |B_H|=|\Psi|\in\{0,1\},\qquad\Psi\subseteq P.
$$

定义实际不交域

$$
K_+=(Q\setminus\Omega)\sqcup A_H,\qquad
K_-=(P\setminus\Psi)\sqcup B_H.
$$

它们各有 $b$ 点，且

$$
H_L=D\sqcup K_+,\qquad H_R=D\sqcup K_-.
$$

$K_+$ 无红六，因为它在 $H_L$ 中。它也无蓝五：$Q$ 点不能开始 ambient 蓝五，而 owner 的出蓝五第二点必须在缺席的 $\Omega$。故 $K_+$ 是满 $b$ 点短帽。$K_-$ 反序同理。

## 5. 直接消去 D 的核内红五端点

在实际核内定义

$$
C_D=\operatorname{End}_{R_5}(H_L)\cap D.
$$

若 $d\in C_D$ 能开始 $H_L$ 内的蓝五，取终于 $d$ 的核内红五接桥：蓝桥给蓝六，红桥给核内红六，均矛盾。因此 $C_D$ 中的点不能开始核内蓝五。

于是实际域 $K_+\cup C_D\subseteq H_L$ 仍无蓝五：蓝五不可能从 $C_D$ 开始，也不能从 $Q$ 开始；owner 的第二点仍必须在缺席的 $\Omega$。它亦无红六。由于 $|K_+|=b$ 且 $C_D\subseteq D$ 与之不交，容量迫

$$
\operatorname{End}_{R_5}(H_L)\cap D=\varnothing.
$$

反序得到

$$
\operatorname{Src}_{R_5}(H_R)\cap D=\varnothing.
$$

本节直接使用实际满短帽，不依赖旧 $\kappa$ 公式，也不先进口 $D$ 无红五或 $w=0$。

## 6. 唯一交叠点的两侧完整红扇

$S,T$ 各有 $b+1$ 点且无蓝五，容量迫它们各有内部实际红六。唯一交叠保证这些路径分别终于、始于 $z$。固定其实际末／首对

$$
(f,z),\quad f\in P;\qquad (z,g),\quad g\in Q.
$$

### 6.1 禁止以 (z,g) 为末对的蓝五

$T$ 内的红六从 $z,g$ 开始，所以 $g$ 有 ambient 出红五。若 $g$ 不是右 owner，因 $g\in Q$、$\Psi\subseteq P$，强普通点性质禁止任何终于 $g$ 的 ambient 蓝五。若 $g$ 是右 owner，其入蓝五末前驱必须是 $\Psi$ 中的实际锁，而 $z\notin\Psi$。因此两种情形都禁止实际末对为 $(z,g)$ 的蓝五。

### 6.2 左红扇

对任意 $t\in T$ 及任意 ambient 合序中点 $t<x<z$，有

$$
\chi(t,x,z)=R.
$$

反设该项为蓝。始于 $(z,g)$ 的红六不能前接 $x$，否则得红七，所以首帽给 $\chi(x,z,g)=B$。取任意终于 $t$ 的实际红六，其末前驱记为 $v$；红七禁形同样给 $\chi(v,t,x)=B$。于是

$$
B_5(v,t,x,z,g)
$$

实际成立，违反 §6.1。

### 6.3 右红扇

对全序反向执行上述完整论证：内部 $S$ 路径的末对 $(f,z)$ 使 $f$ 有 ambient 入红五；强普通点性质或 owner 锁性质禁止以 $(f,z)$ 为首对的蓝五。由此得到

$$
\chi(z,x,s)=R\qquad(s\in S,\ z<x<s),
$$

中点遍历全部 ambient 合序点。

## 7. 末对屏障与两侧 owner、锁的严格次序

先复述一般实际末对屏障：若某条 $R_6$ 的末对为 $(a,t)$，则不存在实际 $R_6(a,r)$、$r>t$。否则禁红七迫 $\chi(a,t,r)=B$，实际 $B_3(a,t,r)$ 与 $R_6(a,r)$ 同端、长度和为 9，违反 weak7。首对屏障取全序反向。

### 7.1 左 owner 与低锁必须存在

使用 §6 的实际末前驱 $f$。

若 $f$ 是左 owner，则它的实际出红六终锁 $\omega$ 由末对 $(f,z)$ 的屏障满足 $\omega\le z$。又因 $z\notin\Omega$，故 $\omega<z$。

若 $f$ 不是左 owner，它由内部 $S$ 红六有 ambient 入红五。因 $f\in P$ 且 $\Omega\subseteq Q$，强普通点性质给 $f$ 无 ambient 出蓝五。实际 $K_+\cup\{f\}$ 有 $b+1$ 点且无蓝五：$f$ 不补入任何缺席的 $\Omega$ 点，$Q$ 不能开始蓝五，owner 的蓝五仍要用 $\Omega$。容量迫其中存在实际红六。

这条红六的唯一可能源是 $f$：$K_+$ 中的 $Q$ 点没有 ambient 源身份，而 owner 的出红六必须终于缺席的 $\Omega$。因此可写为

$$
R_6(f,h_2,h_3,h_4,h_5,t),\qquad t\in Q\setminus\Omega.
$$

末对 $(f,z)$ 的屏障给 $t<z$。若 $h_5\in Q$，则 §6 的左红扇给 $\chi(h_5,t,z)=R$，把 $z$ 接在此红六后得到红七。故 $h_5$ 必为左 owner，迫 $A_H$ 非空。

§4 已知左 owner 至多一个，记为 $a$，其唯一锁记为 $\omega$。当前路径末对为 $(a,t)$，owner 的实际出红六终于 $\omega$，屏障给 $\omega\le t$。又 $t\notin\Omega$，故 $\omega<t<z$。

两种情形统一得到唯一左 owner 与唯一低锁，并有

$$
a<\omega<z.
$$

### 7.2 右 owner 与高锁必须存在

对实际首后继 $g$ 完全反序论证，得到唯一右 owner $b_0$ 与其唯一锁 $\psi$，满足

$$
z<\psi<b_0.
$$

于是同一母体的四点满足

$$
a<\omega<z<\psi<b_0.
$$

## 8. 同一中间域迫出 a 到 b0 的实际红五

实际中间域

$$
M=D\sqcup\{a,b_0\}
$$

有 $b+1$ 点。因 $a\ne\psi$、$b_0\ne\omega$，结合 §4 的核分解，有 $M\subseteq H_L\cap H_R$。因此 $M$ 是实际 balanced 域；换色短帽容量迫其中存在 $R_5$。

先排除两个 owner 的错误端点角色。左 owner $a$ 不属于 $\operatorname{End}_{R_5}(H_L)$。否则取核内终于 $a$ 的红五，再取 owner 的实际出蓝五 $B_5(a,\omega,\ldots)$。连接桥为蓝则给蓝六；为红则得到从 $H_L$ 中严格早于 $a$ 的点启动的 ambient 红六。但 $H_L\cap S=\{a\}$，矛盾。

反序地，右 owner $b_0$ 不属于 $\operatorname{Src}_{R_5}(H_R)$。

结合 §5 对全部 $D$ 点端点身份的排除，$M$ 内所迫红五只能始于 $a$、终于 $b_0$，其余三个实际点都在 $D$。因此有实际

$$
R_5(a,D^3,b_0).
$$

## 9. 实际 owner 锁对与同端 weak7 矛盾

不能仅凭锁标签调用帽，先兑现两条实际相邻对。

取 owner $a$ 的实际入红五和实际出蓝五 $B_5(a,\omega,\ldots)$。若连接桥为蓝则得到蓝六，故桥红。将 $\omega$ 后接入红五，得到实际红六，末对恰为 $(a,\omega)$。

右侧取实际入蓝五 $B_5(\ldots,\psi,b_0)$ 与 owner $b_0$ 的实际出红五。连接桥同样必红，得到实际红六，首对恰为 $(\psi,b_0)$。

由 $\omega<\psi$，这两条实际红六的红七帽分别给

$$
\chi(a,\omega,\psi)=B,\qquad
\chi(\omega,\psi,b_0)=B.
$$

所以同一母体有实际

$$
B_4(a,\omega,\psi,b_0).
$$

它与 §8 的实际 $R_5(a,D^3,b_0)$ 有完全相同的首末点，长度和为 $4+5=9$，违反 weak7。反设 $n=3b$ 不成立；结合 §2 的 $n\le3b$ 与整数性，主定理得证。

## 10. 数值范围、历史与剩余

取既有有效 $b=25$，整个 $I=\{z\}$ 类均至多 74 点。本证明关闭此前 75 点唯一交叠的全部分支，包括外跨红六、任意中性域排序及旧闭包失败接口，不需要再分别排除它们。

[上一轮外跨／共享 D 主稿](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-critical-crossing-and-joint-roots-20261106/PROOF.md>) 保留为历史成果入口，本文不修改其任何文件，也不把其中未闭状态冒充当时已闭。本文的完整证明使用参数无关 M0 与严格 balanced 容量，旧进口与本轮新推导保持区分。

旧 $I=\varnothing$ 整类已由[balanced 严格界的无 through 桥 §5.1](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n766-strict-capacity-20261105/PROOF.md>) 排除 75 点。因此当前任何 75 点残余必须满足

$$
|I|\ge2.
$$

多交叠类仍开放。全局工作界保持 **40／49／75／76**，不是全局 74／75；本轮同会话解析证明没有独立外审、科研运行或接受升级。恢复入口见[NEXT_SESSION](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/NEXT_SESSION.md>)。

不依赖唯一交叠的一般四端口工具及多交叠的限定 caller 另见[FOUR_PORT_AUGMENTATION](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/FOUR_PORT_AUGMENTATION.md>)；它不参与上述唯一交叠主定理的证明，也未关闭多交叠全类。
