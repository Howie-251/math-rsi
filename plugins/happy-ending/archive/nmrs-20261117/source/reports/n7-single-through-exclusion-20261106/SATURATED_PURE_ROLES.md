# 双满纯角色 P=Q=b 的临界整类排除

日期：2026-11-06。

本文忠实记录主会话冻结的完整参数化证明，状态为 **same-session、未外审、未接受**。指定 native Sol/high 只整理文档与检查引用，不自行补证。本轮无外审、科研运行或求解。

本轮排除 $n=3b$、$|P|=|Q|=b$、$|I|\ge2$ 的整个类。结合既有空交叠与本目录唯一交叠排除，75 点残余至少一侧纯角色未满。全局工作界仍为 **40／49／75／76**，不是全局 74／75。

## 1. 模型、参数与主定理

母体 $X$ 是有限完整 ordered rank-3 signotope，禁 $B_6,R_7,\mathrm{weak7}$。四点 packet 按 $abc,abd,acd,bcd$ 至多变色一次；路径长度按实际点数计且对子序列遗传。weak7 禁止同一对实际首末点的异色路径长度和至少为 9。

设 $b$ 为 756（无 $B_5,R_6,\mathrm{weak7}$）及换色756（无 $R_5,B_6,\mathrm{weak7}$）的共同有效整数容量。定义全部 ambient 红六源末及不交角色

$$
S=\operatorname{Src}_{R_6}(X),\quad T=\operatorname{End}_{R_6}(X),\quad
I=S\cap T,
$$

$$
P=S\setminus T,\quad Q=T\setminus S,\quad
D=X\setminus(S\cup T).
$$

**主定理。** 不存在同时满足

$$
|X|=3b,\qquad |P|=|Q|=b,\qquad
I=\{z_1<\cdots<z_i\},\quad i\ge2
$$

的实际母体。

以下反设有这样的母体。实际人口恒等式给

$$
|D|=b-i.
$$

本证明先按一般有效容量 $b$ 完成，再代入 $b=25$；不先假设所需路径有纯 $D$ 内部见证。

## 2. 双满纯角色把完整 M0 压成单例纤维

调用[参数无关 M0：审计稿 §2](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7677_PROOF_OBLIGATION_AUDIT_20261103.md>)。$H_L,H_R\supseteq D$ 是同一母体中的实际 balanced 核，人口 $2b-\alpha,2b-\beta$。owners 为 $A_H=H_L\cap S\subseteq P$、$B_H=H_R\cap T\subseteq Q$，锁集为 $\Omega\subseteq T\setminus H_L$、$\Psi\subseteq S\setminus H_R$。每个左 owner 有 ambient 入红五、出蓝五，其全部出红六末点及出蓝五第二点为同一实际锁，每锁都有 owner 供应；右侧反序。完整补集为

$$
X\setminus H_L=(S\setminus A_H)\cup\Omega,\qquad
X\setminus H_R=(T\setminus B_H)\cup\Psi.
$$

令

$$
u=|A_H|-|\Omega|\ge0,\quad v=|B_H|-|\Psi|\ge0,
\quad\delta=|\Omega\cap I|,\quad\varepsilon=|\Psi\cap I|,
$$

$$
C=\operatorname{End}_{R_5}(H_L),\quad C'=\operatorname{Src}_{R_5}(H_R),
\quad Z_+=C\cap D,\quad Z_-=C'\cap D,
$$

$$
Q_H=Q\cap H_L,\qquad P_H=P\cap H_R.
$$

旧实际短帽

$$
K_+=Z_+\sqcup Q_H\sqcup A_H,\qquad
K_-=Z_-\sqcup P_H\sqcup B_H
$$

无蓝五、红六。左侧真实人口为

$$
|K_+|=b+u+\delta+|Z_+|.
$$

容量 $b$ 迫全部非负项为零。反序得到

$$
u=\delta=|Z_+|=0,\qquad v=\varepsilon=|Z_-|=0.
$$

因此

$$
\Omega\subseteq Q,\qquad\Psi\subseteq P,
\qquad\alpha=\beta=i,
$$

owners 与锁一一对应，所有纤维都是单例，$K_\pm$ 各有 $b$ 点。$D$ 内红五的源末属于 $Z_-,Z_+$，所以也在此时被排除；无需预先进口 $w=0$。

旧纤维代表界进一步给

$$
A_H\cap\operatorname{End}_{R_5}(H_L)=\varnothing,\qquad
B_H\cap\operatorname{Src}_{R_5}(H_R)=\varnothing.
$$

交叉锁排除给实际共同域

$$
D_{\rm all}=H_L\cap H_R=D\sqcup A_H\sqcup B_H.
$$

由完整源末容器、$Z_\pm=\varnothing$ 及 owner 的上述反角色排除，$D_{\rm all}$ 内所有实际红五只能是

$$
A_H\longrightarrow B_H.
$$

基础核、纤维与容器的旧来源为[加权双向补偿稿 §§1–2](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_WEIGHTED_BILATERAL_COMPENSATION_AND_ENLARGED_ROOTS_20261103.md>) 与[临界层原稿 §2，式(6)–(9)](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_T0_CRITICAL_LAYER_AND_SATURATION_BARRIERS_20261103.md>)。本文件下文实际删点重证端口人口，不调用旧匹配结论。

## 3. 每个交叠点同时是两种旧根

$S$ 无蓝五且 $|S|=b+i$。它的内部红六末点全在 $I$。删除全部内部实际红六末点后，余域无蓝五、红六，人口至多 $b$，因此内部末点至少有 $i$ 个。于是每个 $z_j\in I$ 都是 $S$ 内实际红六的末点。

反序，每个 $z_j$ 都是 $T$ 内实际红六的源。

因 $\Omega\subseteq Q$、$\Psi\subseteq P$，完整基底 $W=S\setminus\Omega=S$、$W'=T\setminus\Psi=T$。所以旧根族恰为

$$
\widehat E=\widehat F=I.
$$

每个 $z_j$ 均具有完整的双向 ambient 红扇：

$$
\chi(t,x,z_j)=R\quad(t\in T,\ t<x<z_j),
$$

$$
\chi(z_j,x,s)=R\quad(s\in S,\ z_j<x<s).
$$

中点 $x$ 遍历全部合序 ambient 点，不限制为某个已选诱导域。

## 4. 任意相邻 cut 的全部 ambient 普通端口为空

对每个 $k=1,\ldots,i-1$，取非实际点的 cut $z_k<c<z_{k+1}$，令

$$
B_k=\{z_1,\ldots,z_k\},\qquad
A_k=\{z_{k+1},\ldots,z_i\}.
$$

沿旧完整普通集定义，$\mathcal R$ 收集**全部 ambient 实际红六末对** $(j,r)$ 中满足 $r\in I,r<c,j\in S\setminus A_H$ 的前驱；$\mathcal Q$ 反序收集全部实际首对 $(s,h)$ 中满足 $s\in I,s>c,h\in T\setminus B_H$ 的后继。

两侧根扇使它们分别位于 $P\setminus A_H$、$Q\setminus B_H$。旧局部实际增广证明给

$$
K_+\sqcup\mathcal R\text{ 为实际756},\qquad
K_-\sqcup\mathcal Q\text{ 为实际756}.
$$

该局部证明使用低／高实际帽、完整头尾替换与普通点无相应蓝五供应；不需要旧稿最终 $t\ge1$ 的正交会结论。现在 $K_\pm$ 已满 $b$，故

$$
\mathcal R=\mathcal Q=\varnothing.
$$

此结论的作用域是定义中**全部 ambient 相邻对**，不是仅当前外域内选出的见证。

## 5. 每个 cut 给实际 owner 端口满红短帽

令 $L_k$ 为 $K_-\cup B_k$ 内全部实际红六的末前驱，$R_k$ 为 $K_+\cup A_k$ 内全部实际红六的第二点。

左域的红六只能终于 $B_k$：右 owner 的入红六需要缺席的 $\Psi$。末前驱中普通点由 §4 排除，反向角色由根扇排除，且 $Z_-=\varnothing$，所以 $L_k\subseteq A_H$。右侧反序给 $R_k\subseteq B_H$。

删去这两族全部实际点，分别命中外域全部红六；余域为实际756。容量直接给

$$
|L_k|\ge k,\qquad |R_k|\ge i-k.
$$

每个 $a\in L_k$ 有实际末对 $(a,r)$，其中 $r\le z_k$。通常末对屏障与 owner 的实际出红六迫

$$
\omega(a)<r\le z_k;
$$

严格性来自锁在 $Q$、根在 $I$，不能相等。每个 $b_0\in R_k$ 有实际首对 $(s,b_0)$、$s\ge z_{k+1}$，反序屏障给

$$
\psi(b_0)>s\ge z_{k+1}.
$$

owners 的入红五／出蓝五实际兑现红六末对 $(a,\omega(a))$，右侧兑现首对 $(\psi(b_0),b_0)$。两帽给实际 $B_4(a,\omega(a),\psi(b_0),b_0)$，因此禁止全部 ambient $R_5(L_k,R_k)$。

共同域的红五只可能从 $A_H$ 到 $B_H$，故实际域

$$
K_k=D\sqcup L_k\sqcup R_k
$$

无红五。换色容量给

$$
b-i+|L_k|+|R_k|\le b.
$$

结合两侧下界，全部取等：

$$
\boxed{|L_k|=k,\qquad |R_k|=i-k,\qquad |K_k|=b.}
$$

$K_k$ 为实际满红短帽。整个推导用全部路径与实际删点，没有匹配最优化。

## 6. i 至少三时，相邻 cuts 的实际集合共同矛盾

若 $i\ge3$，取内部根 $z_j$，$2\le j\le i-1$。在**同一 owner／锁系统**内，$L_j$ 有 $j$ 个点，其锁严格早于 $z_j$；$R_{j-1}$ 有 $i-j+1$ 个点，其锁严格晚于 $z_j$。

因此每个 $L_j\to R_{j-1}$ 的实际红五都被真实锁末／首对的同端蓝四禁止。实际域

$$
D\sqcup L_j\sqcup R_{j-1}
$$

无红五，却有

$$
(b-i)+j+(i-j+1)=b+1
$$

点，违反换色短帽容量。故 $i\ge3$ 的整个双满纯角色类不存在。

这里共同使用两个相邻切分的实际集合，没有分别改选 owner 系统，也没有把各自存在的见证当作可独立优化的匹配。

## 7. i=2 的唯一 cut 与其他 owner 的高锁

以下 $I=\{z_1<z_2\}$。唯一 cut 给

$$
L_1=\{a_0\},\qquad R_1=\{b_0\},
$$

$$
a_0<\omega_0<z_1<z_2<\psi_0<b_0,
$$

以及满红短帽

$$
K=D\sqcup\{a_0,b_0\},\qquad |K|=b.
$$

固定任意其他左 owner $a\ne a_0$。实际 $K\cup\{a\}\subseteq D_{\rm all}$ 有 $b+1$ 点，容量迫红五。端点只能是 $a$ 或 $a_0$ 到 $b_0$；$a_0\to b_0$ 已被锁蓝四禁止。因此有实际

$$
R_5(a,\ldots,b_0).
$$

其内部**允许包含 $a_0$**，不能写成纯 $D^3$ 见证。

若 $\omega(a)<\psi_0$，真实锁末／首对给与这条红五同端的蓝四，矛盾。所以 $\omega(a)\ge\psi_0$。又 $\Omega\subseteq Q$、$\Psi\subseteq P$ 不交，不能相等，得到

$$
\boxed{\omega(a)>\psi_0>z_2\quad(a\in A_H\setminus\{a_0\}).}
$$

## 8. 一般纯源跨越引理

**引理。** 若有实际

$$
R_6(v_1,v_2,v_3,h,f,z),
$$

则不可能另有实际 $R_6(p,r)$，其中 $p\in P$ 且

$$
f<p<z<r.
$$

**证明。** 因 $p\notin T$，必有 $\chi(h,f,p)=B$，否则将原红六末点换为 $p$，得到终于非 $T$ 点的红六。原红六给 $\chi(h,f,z)=R$；packet $(h,f,p,z)$ 的前两项为蓝、红，迫

$$
\chi(f,p,z)=R.
$$

原末帽给 $\chi(f,z,r)=B$。实际 $R_6(p,r)$ 与 weak7 禁止同端蓝三，迫 $\chi(p,z,r)=R$。于是 packet $(f,p,z,r)$ 的后两项为蓝、红，迫 $\chi(f,p,z)=B$，矛盾。

$p=f$ 的边界由通常末对屏障直接排除。两条路径不要求内部属于同一诱导域。证毕。

## 9. i=2 的最终完整路径矛盾

实际域 $S\setminus\{a_0\}$ 有 $b+1$ 点且无蓝五，容量迫内部红六。

若其末点为 $z_1$，末前驱属于 $P$。由 §4 对唯一 cut 的**全部 ambient 普通低前驱为空**，它必须是 owner；$a_0$ 已删除，其他 owner 的锁由 §7 全部晚于 $z_2$，违反末对屏障。因此该内部红六终于 $z_2$，记末前驱为 $f$。

若 $f=z_1$，末帽给 $\chi(z_1,z_2,\psi_0)=B$，但 $z_1$ 的右扇因 $\psi_0\in S$ 迫其为红，矛盾。其他 owner 同样因高锁排除，而 $a_0$ 缺席。所以

$$
f\in P\setminus A_H.
$$

它有 ambient 入红五，强普通点性质给无 ambient 出蓝五。实际 $K_+\cup\{f\}$ 有 $b+1$ 点、无蓝五，容量迫

$$
R_6(f,h_2,h_3,h_4,h_5,t).
$$

源只能是 $f$，原 owner 需要缺席的 $\Omega$；末点 $t\in Q\setminus\Omega$。实际末对 $(f,z_2)$ 的屏障给 $t<z_2$。

若该路径尾部出现任何其他 owner $a\ne a_0$，则

$$
f<a<t<z_2<\omega(a),
$$

其实际出红六 $a\to\omega(a)$ 与终于 $z_2$、末前驱为 $f$ 的内部红六违反 §8 的纯源跨越引理。因此路径唯一可能使用的 owner 是 $a_0$。

若 $h_5\in Q$，$z_2$ 左扇给 $\chi(h_5,t,z_2)=R$，将 $z_2$ 后接原红六成红七。故

$$
h_5=a_0,\qquad h_2,h_3,h_4\in Q,\qquad h_4<a_0<z_1.
$$

现在同一母体中有实际

$$
R_6(h_2,h_3,h_4,z_1,z_2,\psi_0).
$$

逐个连续三元组的来源为：第一项 $\chi(h_2,h_3,h_4)=R$ 来自刚取得的红六；第二项 $\chi(h_3,h_4,z_1)=R$ 用 $z_1$ 左扇；第三项 $\chi(h_4,z_1,z_2)=R$ 用 $z_2$ 左扇；第四项 $\chi(z_1,z_2,\psi_0)=R$ 用 $z_1$ 右扇。

但该红六源点 $h_2\in Q=T\setminus S$，与 ambient 源定义矛盾。$i=2$ 也不存在；结合 §6，主定理得证。

## 10. 当前残余与其他工具的准确地位

取 $b=25$，75 点且 $|P|=|Q|=25,|I|\ge2$ 的整个类已排除。旧 $I=\varnothing$ 类由[严格 balanced 容量的无 through 桥 §5.1](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n766-strict-capacity-20261105/PROOF.md>) 排除；$|I|=1$ 的整个类已由[本目录唯一交叠主证明](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/PROOF.md>) 排除。

因此任意当前 75 点残余必须满足

$$
\boxed{|I|\ge2,\qquad |P|\le24\ \text{或}\ |Q|\le24.}
$$

这里只排除了双满纯角色。一侧纯角色满 $b$ 的进一步结论仍未闭，不在本文预写。

[一般四端口定理](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/FOUR_PORT_AUGMENTATION.md>) 仍有效，但其原 $|P|=|Q|=25$ caller 已由本文更强整类结论关闭，不再列为当前残余方向。严格分离与 regular 共根文件保留各自准确适用域，不能据本文将其未满纯角色残余自动关闭。

全局工作界仍为 **40／49／75／76**。没有外审、计算或接受升级，也没有全局 74／75；恢复入口见[NEXT_SESSION](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/NEXT_SESSION.md>)。
