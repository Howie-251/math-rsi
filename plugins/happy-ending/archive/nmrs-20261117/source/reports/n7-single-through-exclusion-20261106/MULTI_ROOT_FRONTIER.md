# 多交叠余类：一侧饱和缺额与纯增强共根接口

日期：2026-11-06。

本文忠实整理主会话冻结的两份不同作用域的参数化结构结果：§§1–8 是一侧纯角色饱和、严格交错的 ordinary 缺额结算；§§9–15 重新进入 regular 纯增强共根余类，不继承前半部的 $P=b$ 前提。状态为 **same-session、未外审、未接受**。native Sol/high 仅执行文档整理及引用检查，本轮无外审、科研运行或求解。两部分均保留准确共同实现义务，未给出新的整类或全局排除；全局工作界仍为 **40／49／75／76**。

## 1. 原模型、一侧饱和与严格交错输入

母体 $X$ 是完整有序 rank-3 signotope，禁 $B_6,R_7,\mathrm{weak7}$。四点 packet 按字典序至多变色一次，实际路径长度按点数计且对子序列遗传；weak7 比较同一对实际首末点的异色路径，长度和至少为 9。$b$ 为 756 及换色756 的共同有效整数容量。

记全部 ambient 红六源末为 $S,T$，以及

$$
I=S\cap T=\{z_1<\cdots<z_i\},\quad
P=S\setminus T,\quad Q=T\setminus S,\quad
D=X\setminus(S\cup T).
$$

本文件固定一般整数缺额 $e$ 的输入

$$
n=|X|=3b,\qquad |P|=b,\qquad |Q|=b-e,
$$

$$
U=\operatorname{Src}_{R_5}(D),\quad V=\operatorname{End}_{R_5}(D),
\qquad w=|U\cap V|=0.
$$

实际人口给 $|D|=b-i+e$。在**同一份**参数无关 M0 系统上，假设两增强根族严格交错：

$$
x_e=\min E^+<y_f=\max F^+.
$$

这里下标 $e$ 保留旧增强根记号，$e$ 本身是纯末人口缺额；两者不能据记号混为同一对象。

## 2. 完整 M0、旧根与基础短帽

沿用[参数无关 M0：审计稿 §2](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7677_PROOF_OBLIGATION_AUDIT_20261103.md>) 的同母体实际 balanced 核 $H_L,H_R\supseteq D$，大小 $2b-\alpha,2b-\beta$。owners 为 $A_H=H_L\cap S\subseteq P$、$B_H=H_R\cap T\subseteq Q$，锁为 $\Omega\subseteq T\setminus H_L$、$\Psi\subseteq S\setminus H_R$。每个左 owner 有 ambient 入红五、出蓝五，全部出红六末点与出蓝五第二点为同一锁，每锁有 owner 供应；右侧反序。两核补集是

$$
X\setminus H_L=(S\setminus A_H)\cup\Omega,\qquad
X\setminus H_R=(T\setminus B_H)\cup\Psi.
$$

令

$$
u=|A_H|-|\Omega|,\quad v=|B_H|-|\Psi|,
\quad\delta=|\Omega\cap I|,\quad\varepsilon=|\Psi\cap I|,
$$

$$
C=\operatorname{End}_{R_5}(H_L),\quad C'=\operatorname{Src}_{R_5}(H_R),
\quad Z_+=C\cap D,\quad Z_-=C'\cap D,\quad c_\pm=|Z_\pm|,
$$

$$
P_H=P\cap H_R,\quad Q_H=Q\cap H_L,
$$

$$
K_-=Z_-\sqcup P_H\sqcup B_H,\qquad
K_+=Z_+\sqcup Q_H\sqcup A_H,
\quad\kappa_\pm=b-|K_\pm|.
$$

这些是实际756。交叉锁排除给

$$
D_{\rm all}=H_L\cap H_R=D\sqcup A_H\sqcup B_H.
$$

旧基底为 $W=S\setminus\Omega,W'=T\setminus\Psi$。$\widehat E$ 收集全部实际红六末对两点同在 $W$ 的末根，$\widehat F$ 收集首对两点同在 $W'$ 的首根。增强根保持原定义

$$
E^+=\widehat E\cup\{r\in I:\text{某实际红六末对为 }(j,r),\ j\in T\},
$$

$$
F^+=\widehat F\cup\{s\in I:\text{某实际红六首对为 }(s,k),\ k\in S\}.
$$

根扇、强普通点性质、实际帽与头尾替换沿旧原域成立，量词覆盖全部 ambient 实际路径。

## 3. 满纯源侧压出右零缺额及全部左旧末根

右基础短帽的真实人口为 $b+v+\varepsilon+c_-$，容量迫

$$
v=\varepsilon=c_-=\kappa_-=0,\qquad\beta=i-e.
$$

左侧补集人口及短帽人口给

$$
\alpha=i-u-\delta,\qquad
\kappa_+=e-u-\delta-c_+.
$$

$\varepsilon=0$ 使 $\Psi\subseteq P$，因此 $W'=T$，人口 $b+i-e$。删除 $T$ 内全部实际红六源后余域为756，故

$$
|\widehat F|\ge i-e.
$$

$W=S\setminus\Omega$ 的人口为 $b+i-\delta$，其内部红六末点只能在 $I\setminus\Omega$。删尽全部内部末点后容量至多 $b$，所以所有 $i-\delta$ 个候选末点都必须兑现，得到

$$
\boxed{\widehat E=I\setminus\Omega.}
$$

不能将它写为 $I$，左锁仍可能占据交叠点。

[旧严格交错取等，临界层原稿 §2](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_T0_CRITICAL_LAYER_AND_SATURATION_BARRIERS_20261103.md>) 排除根间 cut 的低侧左锁。因此

$$
x_e=z_1,\qquad \Omega\cap I\subseteq[y_f,\infty).
$$

写 $y_f=z_h$。它必为旧首根：若只有增强首对 $(y_f,k)$、$k\in S$，较早有效末根 $x_e$ 的右扇迫 $\chi(x_e,y_f,k)=R$，而该实际首对的红七帽迫其为蓝，矛盾。所以

$$
y_f=z_h\in\widehat F,\qquad h\ge2.
$$

## 4. 每个根间 cut 的全部 ordinary 与精确端口

对每个 $1\le k<h$，取非实际点 cut $z_k<c<z_{k+1}$，令

$$
B_k=\{z_1,\ldots,z_k\},\qquad
A_k=(I\setminus B_k)\setminus\Omega,
\quad |A_k|=i-k-\delta.
$$

$\mathcal R_k$ 收集全部 ambient 实际红六末对 $(p,r)$ 中满足 $r\in B_k,p\in S\setminus A_H$ 的前驱，记 $r_k=|\mathcal R_k|$。完整根工具给

$$
\mathcal R_k\subseteq P\setminus A_H,\qquad r_k\le\kappa_+.
$$

右侧全部高 ordinary 后继 $\mathcal Q_k$ 因 $\kappa_-=0$ 而为空。这使用[双向加权稿 §2 的全部 ordinary 实际增广](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_WEIGHTED_BILATERAL_COMPENSATION_AND_ENLARGED_ROOTS_20261103.md>)：$K_+\sqcup\mathcal R_k$、$K_-\sqcup\mathcal Q_k$ 是实际756，不把旧人口层的最终正交会结论搬到这里。

在左实际外域 $K_-\cup B_k$ 的全部末对中去掉 ordinary 前驱 $\mathcal R_k$，所得全部剩余前驱为 $L_k$；右实际外域 $K_+\cup\mathcal R_k\cup A_k$ 中的全部红六第二点为 $R_k$。旧精确取等式(6)–(9)给

$$
L_k\subseteq A_H,\qquad R_k\subseteq Z_+\sqcup B_H,
$$

$$
\boxed{|L_k|=k-r_k,\qquad
|R_k|=i-k-\delta-\kappa_++r_k.}
$$

所有这些集合属于固定的同一母体、同一 owner／锁系统，并保留全部实际相邻对。

## 5. 最左 cut 排除非单例纤维

$|L_1|=1-r_1\le1$。旧取等同时给

$$
|\operatorname{End}_{R_5}(H_L)\cap A_H|=u,
\qquad\operatorname{End}_{R_5}(H_L)\cap A_H\subseteq L_1.
$$

若有非单例左锁纤维，它的非最早 owner 在 $L_1$，实际低末帽迫其共同锁低于当前 cut。若该纤维最早 owner 不在 $L_1$，旧满红短帽 $K$ 加入这位 owner 后，容量迫实际私有红五到 $R_1$，配右外首对又迫同一锁高于 cut，矛盾。故整个非单例纤维都必须在 $L_1$，至少占两个点，亦与 $|L_1|\le1$ 矛盾。

因此

$$
u=0,\qquad\kappa_+=e-\delta-c_+.
$$

右侧已有 $v=0$，故两侧全部纤维为单例。结合 $Z_-=\varnothing$ 及单例 owner 反角色排除，实际共同域 $D_{\rm all}$ 中所有红五的源只在 $A_H$，末只在 $Z_+\sqcup B_H$。

## 6. 每个内部根至少消耗一个不同 ordinary 点

对每个 $2\le j\le h-1$，在同一母体定义实际域

$$
H_j=\bigl(D\setminus(Z_+\setminus R_{j-1})\bigr)
\sqcup L_j\sqcup(R_{j-1}\cap B_H).
$$

共同域端点容器使其中全部潜在红五只能从 $L_j$ 到 $R_{j-1}$。任取 $a\in L_j$，它有实际低末对 $(a,r)$、$r\le z_j$；末对屏障迫其唯一锁 $\omega(a)<r$。任取 $v\in R_{j-1}$，有实际首对 $(s,v)$、$s\ge z_j$。所以

$$
a<\omega(a)<s<v.
$$

真实 owner 锁末对与当前首对给同端蓝四，排除全部这些实际红五。因此整个 $H_j$ 无红五。

其真实人口为

$$
\begin{aligned}
|H_j|&=|D|-c_++|L_j|+|R_{j-1}|\\
&=b+1-(r_j-r_{j-1}).
\end{aligned}
$$

换色容量迫 $r_j-r_{j-1}\ge1$。

另一方面，$\mathcal R_k$ 随 cut 单调增加，左域 $K_-\cup B_k$ 也扩大；owner 端口 $L_k$ 不会被 ordinary 删除，因而 $L_k$ 单调增加。结合 $|L_k|=k-r_k$，得到 $r_j-r_{j-1}\le1$。故

$$
\boxed{r_j-r_{j-1}=1,\qquad L_j=L_{j-1}.}
$$

右域中新增 ordinary 点都在全部右源之前，不参与该域从右源开始的内部路径。去掉它们后，右域随 $A_k$ 缩小，故 $R_k$ 单调缩小；再用精确人口得

$$
R_j=R_{j-1}.
$$

所以每个内部根需要一个**不同的实际 ordinary 点**，不能让同一点击穿多个根后重复收费。

## 7. 根数结算及最高根排锁

对内部根求和给

$$
r_{h-1}=r_1+h-2\le\kappa_+,
\qquad r_1\in\{0,1\}.
$$

因此

$$
h-2+r_1\le\kappa_+,\qquad
|\widehat F|\le h\le e-\delta-c_++2.
$$

结合 $|\widehat F|\ge i-e$，得到必要不等式

$$
\boxed{i\le2e+2-\delta-c_+.}
$$

最后排除 $y_f\in\Omega$。取紧邻 $y_f$ 左侧的 cut。若某 owner $a$ 的锁为 $y_f$，它不在 $L$，因为 $L$ 的实际锁严格低于 cut。旧满红短帽 $K$ 加入该 owner 迫实际红五到 $R$；其他源的 $L\to R$ 路径被实际帽排除。

该实际末点有右首对 $(s,r)$，其中 $s\in A$ 避开 $\Omega$，且 $s\ge y_f$。于是 $s>y_f$。实际 owner 锁末对 $(a,y_f)$ 与此首对给同端蓝四，矛盾。因此

$$
\boxed{\Omega\cap I\subseteq(y_f,\infty),\qquad
y_f\in\widehat E\cap\widehat F.}
$$

## 8. 完成范围与准确未闭义务

本文件在一般 $b,e$ 下证明一侧纯角色饱和、指定增强根严格交错输入的必要结构：右基础短帽满、两侧纤维单例、左旧末根为 $I\setminus\Omega$、最低增强末根为 $z_1$、最高增强首根同时为旧双根，及逐内部根的 distinct ordinary 缺额结算。

仍未闭的是：$\kappa_+$ 允许每个内部根各由一个不同 ordinary 点吸收，尚未证明最后根再消耗一单位。不能把已证的 $h\le\kappa_++2$ 改成 $h\le\kappa_++1$，也不能宣布一侧饱和整类排除。这里不代数值拆 case。

下一数学义务是同一实际输入中的末端共同实现：保留已得相邻端口、ordinary 点与最高旧双根，证明额外实际净收益或矛盾。其他根序或 regular 接口不因本文件自动闭合。

全局工作界仍为 **40／49／75／76**。本目录此前[双满纯角色整类排除](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/SATURATED_PURE_ROLES.md>) 保持，当前一般缺额结算不能冒充新的全局 74／75；恢复见[NEXT_SESSION](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/NEXT_SESSION.md>)。

## 9. 第二部分：重新进入 regular 纯增强共根余类

**作用域重新固定。** §§9–15 使用[REGULAR_COMMON_ROOT §8 的纯增强 $d_D=1$ 余类](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/REGULAR_COMMON_ROOT.md>)，不继承第一部分的 $|P|=b$ 或严格交错前提。母体仍为 $n=3b,w=0$ 的767，使用同一份完整 M0；原 regular 共根条件为

$$
\min E^+=\max F^+=z\notin\widehat E\cup\widehat F,
\qquad z\notin\Omega\cup\Psi,
$$

$$
\Omega\cap I\subseteq(z,\infty),\qquad
\Psi\cap I\subseteq(-\infty,z).
$$

两侧纤维都是单例。以原严格 $z$ 切分形成的全部实际低末前驱、高首后继为 $L,R$；每个 $l\in L$ 有实际末对 $(l,r_l)$、$r_l<z$，每个 $r\in R$ 有实际首对 $(s_r,r)$、$s_r>z$。

恢复下列实际不交域与端点覆盖：

$$
C_-=U\setminus L,\qquad C_+=V\setminus R,\qquad
\widetilde C=C_D=C_-\sqcup C_+,
$$

$$
K=D\setminus\widetilde C,\qquad |K|=b-1,
$$

$$
F_-=P\sqcup I_{<z}\sqcup C_-,\qquad
F_+=Q\sqcup I_{>z}\sqcup C_+,\qquad |F_-|=|F_+|=b.
$$

$F_-,F_+,K,\{z\}$ 两两不交并为 $X$。已有实际中性端口

$$
j\in C_-,\quad k\in C_+,\quad
\text{红六末对 }(j,z),\quad\text{红六首对 }(z,k),
$$

$$
R_5(j,K^3,k),\qquad
K\cup\{j\},K\cup\{k\}\text{ 各为 }b\text{ 点红短帽}.
$$

$F_-\cup\{z\}$ 内红六全部终于 $z$、末前驱为 $j$，$F_+\cup\{z\}$ 内红六全部始于 $z$、第二点为 $k$。这些既有唯一性只针对指定域；以下进一步证明有明确角色限制的 ambient 量词。

## 10. D 桥附近的红扇与跨 z 蓝三

任取 $j<x<z$，有

$$
\chi(j,x,z)=R.
$$

否则实际首对 $(z,k)$ 的首帽给 $\chi(x,z,k)=B$，与假想蓝桥组成 $B_4(j,x,z,k)$，和已得 $R_5(j,K^3,k)$ 同端，违反 weak7。

反序地，对任意 $z<y<k$，有 $\chi(z,y,k)=R$。因此对任意

$$
j<x<z<y<k,
$$

packet $(j,x,z,y)$ 的首项红、第三项 $\chi(j,z,y)$ 由实际末对 $(j,z)$ 的末帽为蓝，迫

$$
\chi(x,z,y)=B.
$$

这里不能进一步推出 $\chi(j,x,y)$ 或 $\chi(x,y,k)$ 为红；相应 packet 允许蓝色。本文件不采用这一已撤回的推断。

## 11. 限定 C± 角色的强 ambient 端口唯一性

**命题。** 对任意 ambient 实际红六末对 $(h,r)$，若 $h\in C_-$、$r\le z$，则

$$
h=j,\qquad r=z.
$$

若 $h\ne j$，实际 $K\cup\{j,h\}$ 有 $b+1$ 点，容量迫 $D$ 内红五。其源只可能在 $L,j,h$，末只可能在 $R$；这里 $w=0$ 排除 $j,h\in U$ 的末角色。$L\to R$ 被低高帽禁止；$j\to R$ 用末对 $(j,z)$ 与 $R$ 高首对禁止；$h\to R$ 用 $(h,r\le z)$ 与同一类高首对禁止，矛盾。

若 $h=j$ 但 $r<z$，实际末对 $(j,r)$ 和首对 $(z,k)$ 给 $B_4(j,r,z,k)$，与实际 $R_5(j,K^3,k)$ 同端，亦矛盾。

反序地，任意 ambient 实际首对 $(s,h)$，若 $h\in C_+$、$s\ge z$，则 $h=k,s=z$。

这是覆盖全部 ambient 路径、但**只限定于 $C_-,C_+$ 角色**的唯一性；不能称为 ambient 全部端口唯一。

## 12. 两个严格容量补域中的新 K 端口

实际补域

$$
Y_+=F_+\cup K\cup\{j\},\qquad
Y_-=F_-\cup K\cup\{k\}
$$

各有 $2b$ 点，由严格 balanced 容量 $C\le2b-1$ 各迫红六。$Y_+$ 的红六源为某个 $s\in I_{>z}$，整条路径不使用 $j<z$。

记其实际第二点为 $v$。若 $v\in T$，首对同在 $W'=T\setminus\Psi$：regular 的 $\Psi\cap I<z$ 排除 $s,v$ 为右锁。于是触发晚于 $z$ 的旧首根，矛盾。若 $v\in U$，$z$ 的右扇可以将 $z$ 前接成红七。若 $v\in C_+$，§11 的角色唯一性也与 $s>z$ 矛盾。因此

$$
v\in K\setminus U.
$$

左侧反序得到实际末对 $(u,r)$，其中

$$
u\in K\setminus V,\qquad r\in I_{<z}.
$$

这两条路径同在原母体，给出实际共同次序

$$
u<r<z<s<v.
$$

$u$ 有 ambient 入红五，$v$ 有 ambient 出红五；不能把这些供应升级为 $D$ 内的 $V/U$ 身份。事实上本结论明确有 $u\notin V,v\notin U$。

## 13. 纯 Q/P 相邻端口给全量跨根蓝五

纯增强根定义已兑现实际末对 $(q_0,z)$、$q_0\in Q$，实际首对 $(z,p_0)$、$p_0\in P$，其中

$$
q_0<z<p_0.
$$

这使用 regular 锁次序排除相邻点仍在 $I$，否则会使 $z$ 成为旧 hat 根。

任取一条实际入 $q_0$ 红六的末前驱 $a$，任取一条实际出 $p_0$ 红六的第二点 $b_0$。三条真实帽立即给

$$
\boxed{B_5(a,q_0,z,p_0,b_0).}
$$

此结论对全部这些实际路径选择成立。于是 $a\notin T,b_0\notin S$。

若 $a\in P$，它作为实际末前驱有 ambient 入红五，又开始这条蓝五。M0 强普通点性质迫它是左 owner，而且蓝五的第二点明确为 $q_0$，故其锁为 $q_0$。若 $a\in D$，因 $V$ 不能开始 ambient 蓝五，必有 $a\in D\setminus V$。对偶地，每个 $b_0$ 属于 $D\setminus U$，或者是锁为 $p_0$ 的右 owner。

若 $q_0\notin\Omega$，全部 $a\in D\setminus V$。再用 §11：$a$ 不能在 $C_-$，因为其实际末根 $q_0<z$；也不能在 $C_+\subseteq V$。所以

$$
q_0\notin\Omega\quad\Longrightarrow\quad
\text{全部实际入 }q_0\text{ 红六末前驱 }a\in K\setminus V.
$$

反序地，$p_0\notin\Psi$ 时，全部实际出 $p_0$ 红六第二点 $b_0\in K\setminus U$。

低左锁 $q_0<z$ 和高右锁 $p_0>z$ 不能同时存在，沿用 regular 稿的低／高 owner 不相容引理。因此至少一侧的全量中性结论成立；不能默认两侧同时成立。

## 14. 至少一份纯角色蓝五与统一人口缺额

若 $q_0\notin\Omega$，实际 $F_-\cup\{q_0\}$ 有 $b+1$ 点且无红六。证明按全部可能末点分类：

- 若红六终于低 $I$ 点 $r<z$，末前驱在 $S$ 会触发旧末根，在 $q_0\in T$ 会触发增强末根，在 $C_-$ 则违反 §11，全部排除。
- 若红六终于 $q_0$，末前驱在 $C_-$ 同样违反 §11；若在 $S$，§13 的实际蓝五迫它是锁为 $q_0$ 的 owner，与 $q_0\notin\Omega$ 矛盾。

容量因此迫实际

$$
B_5(F_-^4,q_0).
$$

末点只能为 $q_0$，因为 $F_-$ 没有 ambient 蓝五末点。对偶地，$p_0\notin\Psi$ 迫 $B_5(p_0,F_+^4)$。至少有一份这样的实际蓝五，不能假设两份同时存在。

为避免与实际点 $q_0$ 混淆，重新将中性人口偏差记为

$$
|D|=b+q_{\rm def},\qquad q_{\rm def}\ge1.
$$

实际 balanced 域 $X\setminus T=D\sqcup P$、$X\setminus S=D\sqcup Q$ 的人口至多 $2b-1$，给

$$
|P|,|Q|\le b-q_{\rm def}-1.
$$

因此在**本部分指定 regular 余类**中，$b=25$ 时两侧都至多 23；不能把它写成所有75点残余的无条件结论。

设 $c_-=|C_-|,c_+=|C_+|$，则 $c_-+c_+=q_{\rm def}+1$。$|F_\pm|=b$ 再给

$$
|I_{<z}|\ge c_+,\qquad |I_{>z}|\ge c_-,
\qquad\boxed{i\ge q_{\rm def}+2.}
$$

这些只精确缩小实际余类，不构成匹配结论或全域排除。

## 15. 纯增强余类的最小同步义务

下一步须把 §12 的两个 $K$ 内新端口、§13 的全量跨根蓝五，以及共享同一 $K$ 的两满红短帽 $K\cup\{j\},K\cup\{k\}$ 同步成以下至少一项：一次实际 $b+1$ 点红短帽增广；同端 $B_4(j,k)$；或始于／终于 $D$ 的实际红六。

目前尚未做到。不能把蓝五端点 $a,b_0$ 替换成 $j,k$，也不能在多条路径中各选有利见证后未经共同检验就拼合。本部分只保存辅助结构，不给新的全局数值界；两部分的作用域与各自未闭义务保持分开。
