# 29点旧根域：更正owner锁接口后的中性21排除

日期：2026-11-13。状态：同会话纯解析工作证明，未外审、未获原题整证接受。本轮无科研程序、求解或新证书运行。只修改本独占稿。

## 1. 必须先读的更正与最终范围

本稿早期版本把“红六的倒二点是左owner $a$、末点是 $t$”错误地推出“$t$ 就是 $a$ 的终锁”。完整M0只锁定**从 $a$ 启动的红六**的末点。正确结论只有 $\omega(a)\le t$，允许严格小于。

因此早期版本中的“由满核直接迫 $\max\mathcal F\le\min\mathcal G$”“$\mathcal F\setminus\{\max\mathcal F\}\subseteq\Omega$”及依赖它们的中性22整层排除，全部撤回。本文件已重写，不能引用早期§§4—14作为成立的结论。中性21排除在本文用有序／严格交错分流修复；中性22仅保留准确条件工具，尚未整层排除。

**本稿当前结论：**
$$
\boxed{n=75\Longrightarrow22\le d\le28.}
$$
上端28和排除 $d\le20$ 为既有进口；本稿修复后的新增部分仅排除 $d=21$。一般全局74未证明。

## 2. 同一母体及准确原件

$X$ 是完整有序rank-3 signotope，禁止 $R_7,B_6,\mathrm{weak7}$。路径长度按点数，且对子序列遗传。weak7禁止同一对实际外端的异色路径长度和至少九，内部允许重合。
$$
S=\operatorname{Src}_{R_6}(X),\quad E=\operatorname{End}_{R_6}(X),\quad
T=S\cap E,\quad P=S\setminus E,\quad Q=E\setminus S,\quad
D=X\setminus(S\cup E).
$$

全部核、锁、owner和路径均在同一 $X$ 中。完整M0给实际balanced核 $H_L,H_R\supseteq D$，左owner $A_H=H_L\cap S\subseteq P$、锁 $\Omega\subseteq E\setminus H_L$；右owner $B_H=H_R\cap E\subseteq Q$、锁 $\Psi\subseteq S\setminus H_R$。每个左owner有ambient入红五、出蓝五；全部出红六末点和出蓝五第二点为同一锁。右侧反向。每锁有供应，交叉锁排除给
$$
D_{\rm all}=H_L\cap H_R=D\sqcup A_H\sqcup B_H.
$$

实际短帽和余项为
$$
K_L=Z_+\sqcup Q_H\sqcup A_H,\quad
K_R=Z_-\sqcup P_H\sqcup B_H,
$$
$$
Z_+=D\cap\operatorname{End}_{R_5}(H_L),\quad
Z_-=D\cap\operatorname{Src}_{R_5}(H_R),\quad
Q_H=Q\cap H_L,\quad P_H=P\cap H_R,
$$
$$
k_L=25-|K_L|,\quad k_R=25-|K_R|,\quad
\kappa_L=|A_H|-|\Omega|,\quad\kappa_R=|B_H|-|\Psi|.
$$

旧根域及其域内全部实际红六根为
$$
W=S\setminus\Omega,\quad\mathcal G=\operatorname{End}_{R_6}(W),\qquad
W'=E\setminus\Psi,\quad\mathcal F=\operatorname{Src}_{R_6}(W').
$$
记 $f=|\mathcal F|,g=|\mathcal G|,y=\max\mathcal F,x=\min\mathcal G$。

采用以下准确原件：

1. [完整M0原件§3](../../../../reports/n7-single-through-exclusion-20261106/PROOF.md)。
2. [人口稿§10](N7_HOT_PORT_LOCKS_AND_BLUE_THROUGH_POPULATION_20261112.md)：$|W|,|W'|\le29$，实际红六横截至多4，$\mathcal F$ 是ambient冷入族子集、$\mathcal G$ 是ambient冷出族子集，故各至多5；$n-d+\kappa_L+z_+\le54$ 及镜像式。
3. [有序冷臂稿§2—3](N7_NEUTRAL29_ORDERED_COLD_ARMS_20261112.md)：冷入 $a$ 对 $e<u<a,e\in E$ 有 $\chi(e,u,a)=R$；冷出反向。
4. [29点端点命题10.1](N7_NEUTRAL28_COALESCING_COLD_BOUNDARY_20261112.md)：在 $n=75,d=21$ 中，$\mathcal F$ 的前两根是ambient $E$ 的前两点，$\mathcal G$ 的后两根是ambient $S$ 的后两点。该原证只用29点域的四点最小横截、根冷性及虚拟扇，不使用本稿已撤回的owner等锁推论。
5. [旧t0严格交错取等§2，式(5)](N7_T0_CRITICAL_LAYER_AND_SATURATION_BARRIERS_20261103.md)及[增强根定义§3](N7_WEIGHTED_BILATERAL_COMPENSATION_AND_ENLARGED_ROOTS_20261103.md)：$n=75,w=0$ 且增强末根极值 $x_e<y_f$ 时，每个非标签cut $c\in(x_e,y_f)$ 满足 $\Omega\cap T\cap(-\infty,c)=\varnothing$、$\Psi\cap T\cap(c,\infty)=\varnothing$。这是旧结果，不作为本轮新定理重复申报。
6. [双满纯角色整类排除](../../../../reports/n7-single-through-exclusion-20261106/SATURATED_PURE_ROLES.md)：$n=75,p=q=25,t\ge2$ 不可能。

短帽25和换色短帽25保持其原接受范围；本稿不重放历史证书。

## 3. 可靠的普通端口共同增广

设 $y\in T$ 是ambient冷入点，令 $\mathcal R_y$ 收集全部实际红六末对 $(z,t)$ 中满足
$$
z\in S\setminus A_H,\quad t\in T,\quad t<y
$$
的物理前驱 $z$。则
$$
\boxed{|\mathcal R_y|\le k_L.}\tag{1}
$$

证明如下。若 $z\in E$，冷入 $y$ 的红扇和原红六末帽在 $(z,t,y)$ 冲突。因此 $z\in P\setminus A_H$，有ambient入红五；它自动避开 $\Omega\subseteq E$，强普通点性质使其无ambient出蓝五。

对每个 $z$ 固定一份原实际末对 $(z,t_z)$。整个 $K_L\sqcup\mathcal R_y$ 无蓝五：旧潜在源要求缺席的 $\Omega$，新增点不补锁且无出蓝五。潜在红六的源只能是新增某个 $z$，因为旧owner终锁仍缺席，其它旧点无源身份。

该红六末点 $r$ 不能晚于 $t_z$，否则蓝三 $(z,t_z,r)$ 与之同端；也不能等于 $t_z\in T$，因为全增广域只含 $D,P,Q$。所以其第五点早于 $r<t_z<y$。其第四点有ambient入红五，取该入红五倒二 $d_0$。桥 $(d_0,v_4,v_5)$ 为蓝，否则入红五接原红六末两点成红七。若 $(v_4,v_5,y)$ 为蓝，就有终于冷入 $y$ 的蓝四；故为红，可将原红六末点换成 $y$，与蓝三 $(z,t_z,y)$ 同端。矛盾。

因此整个增广域仍是实际短帽，容量25给(1)。这里是一次同时增广全部点的证明。$t\in T$ 是必要范围，用于排除 $r=t_z$，不推广到任意纯末。

镜向：对冷出 $x\in T$，全部首对 $(s,v)$ 中 $s\in T,s>x,v\in E\setminus B_H$ 的物理后继集 $\mathcal Q_x$ 满足
$$
|\mathcal Q_x|\le k_R,\qquad K_R\sqcup\mathcal Q_x\text{ 是实际短帽}.\tag{2}
$$

## 4. 正确的owner锁不等式与反角色

若实际红六末对为 $(a,t)$、$a\in A_H$，则
$$
\boxed{\omega(a)\le t.}\tag{3}
$$
否则末帽给蓝三 $(a,t,\omega(a))$，与owner从 $a$ 到其锁的红六同端，违weak7。镜向，实际首对 $(s,b)$、$b\in B_H$ 只保证
$$
\boxed{\psi(b)\ge s.}\tag{4}
$$
不要求相等。

owner仍能兑现它自己的真实相邻对：入红五接出蓝五 $(a,\omega,\ldots)$ 时，桥蓝造蓝六，所以桥红，得到红六末对 $(a,\omega)$；右owner反向得到红六首对 $(\psi,b)$。

每左纤维最早owner不结束 $H_L$ 内红五，否则接它的出蓝五，会得到同纤维更早owner或蓝六。每右纤维最晚owner不开始 $H_R$ 内红五。若 $\kappa_L=\kappa_R=0$，两侧每纤维单例，全部owner均有此反角色排除。

**多纤维注意。** 不同匹配owner可以同锁，换成每锁一个极端代表会损失人数；未经收费不能声称“替换不减少端口数”。本稿后续新排除仅在 $\kappa_L=\kappa_R=0$ 使用不同owner对应不同锁。

## 5. 一般75点松弛预算

令 $r_L=29-|W|,r_R=29-|W'|$。同一实际人口恒等式给
$$
\boxed{k_L+r_L+\kappa_L+z_+=d-21,\qquad
k_R+r_R+\kappa_R+z_-=d-21.}\tag{5}
$$
其中 $z_\pm=|Z_\pm|$。令 $\alpha=50-|H_L|,\beta=50-|H_R|$，完整补集还给
$$
|W|=25+\alpha+\kappa_L,\qquad |W'|=25+\beta+\kappa_R,
$$
所以
$$
\boxed{\alpha+\kappa_L+r_L=4,\qquad
\beta+\kappa_R+r_R=4.}\tag{6}
$$
任意75候选两核缺额与全锁数各至多4。这不依赖错误的owner等锁推论。

## 6. 中性21层的有序根分支

反设 $d=21$。式(5)的所有非负项为零，故两 $K$ 各满25，两旧根域各29且最小横截各4，两侧纤维单例，$Z_\pm=\varnothing$、$D$ 无红五，$f,g\in\{4,5\}$。

先假设 $y\le x$。取 $L=\mathcal F\setminus\{y\}$、$R=\mathcal G\setminus\{x\}$，各至少三点。实际域 $K_R\cup L$ 无蓝五；红六只能终于 $L$。其末前驱若在 $E$，冷入 $y$ 与末帽冲突；普通 $P$ 前驱属于 $\mathcal R_y$，由 $k_L=0$ 为空。故所有端口为左owner。满25核加 $|L|$ 点的全部实际末对图由容量和Kőnig给匹配至少 $|L|$。镜向得到至少 $|R|$ 个不同右owner。

各选三条边。由(3)—(4)，任意所选左、右owner的实际锁满足
$$
\omega\le t<y\le x<s\le\psi,
$$
其中 $t\in L,s\in R$ 是对应实际匹配行；无需 $\omega=t$ 或 $\psi=s$。两侧owner均单例纤维，因此所选各侧锁互异。

$J=D$ 加这六个owner有27个实际点，且包含于 $D_{\rm all}$。$Z_\pm=\varnothing$ 和owner反角色使 $J$ 内任意红五只能从左owner $a$ 到右owner $b$。两实际帽 $(a,\omega)$、$(\psi,b)$ 给同端蓝四 $(a,\omega,\psi,b)$，矛盾。故 $J$ 无红五，违反换色短帽25。此分支排除。

## 7. 中性21层的严格交错分支：四个自由through点

现在假设 $x<y$。每条 $W$ 内红六的末对都在 $W$，故 $\mathcal G$ 包含于旧完整末根族，并包含于增强末根族 $E^+$；右侧 $\mathcal F\subseteq F^+$。因此增强极值满足
$$
x_e=\min E^+\le x<y\le y_f=\max F^+.
$$

旧t0结论适用于任意 $c\in(x_e,y_f)$，所以可取所有非标签cut $c\in(x,y)$。这里 $w=0$ 已由本层 $D$ 无红五保证。逐cut消费旧式(5)，得到
$$
\Omega\cap T\subseteq[y,\infty),\qquad
\Psi\cap T\subseteq(-\infty,x].\tag{7}
$$
因 $x<y$，两through锁集不交。

记 $\rho_L=|\Omega\cap T|,\rho_R=|\Psi\cap T|$。本层实际短帽人口给
$$
p+\rho_R=25,\quad q+\rho_L=25,\quad
t=4+\rho_L+\rho_R.
$$
所以真实自由through集
$$
T_0=T\setminus(\Omega\cup\Psi)
$$
恰有四点。

由端点命题10.1，若 $y\ne\max S$，则 $y\le b_{g-1}$，因为 $b_{g-1},b_g$ 是ambient $S$ 的最后两点。至少三个点 $\mathcal F\setminus\{y\}$ 严格早于 $y$，本来避开 $\Psi$，由(7)也避开 $\Omega$。另 $b_{g-1},b_g\ge y>x$，本来避开 $\Omega$，由(7)也避开 $\Psi$。这五个不同点都在 $T_0$，矛盾。

因此 $y=\max S=b_g$。因 $y\in\mathcal G$，它避开 $\Omega$，又 $\Omega\cap T$ 只能在 $y$ 及其右方，而 $T\subseteq S$ 无点晚于 $y$。故 $\rho_L=0$。

镜向：若 $x\ne\min E$，则 $a_2\le x$；$\mathcal G\setminus\{x\}$ 至少三点晚于 $x$ 自由，$a_1,a_2\le x<y$ 也自由，给五点矛盾。因此 $x=\min E=a_1$，而 $x\in\mathcal F$ 避开 $\Psi$，故 $\rho_R=0$。

于是 $p=q=25,t=4$，违反旧双满纯角色整类排除。这闭合严格交错分支。与§6合并，d21整层排除已用正确M0接口修复。

## 8. 中性22层保留的条件性四／四工具

以下只是条件工具，不是已经证明所有d22输入均满足的分类。假设某d22输入额外满足：
$$
k_L=k_R=1,\quad r_L=r_R=\kappa_L=\kappa_R=z_+=z_-=0,\quad f=g=4,
$$
$$
\mathcal F=(a_1,a_2,a_3,y),\quad\mathcal G=(x,b_2,b_3,b_4),
\quad a_3\le x<y\le b_2,
$$
且唯一普通端口集分别是 $\mathcal R_y=\{z\}$、$\mathcal Q_x=\{v\}$，有实际末对 $(z,x)$、首对 $(y,v)$。则该条件输入不可能。

证明采用主调度给出的具体帽补偿：$z<x<y<v$，并有
$$
\chi(z,x,t)=B\ (t>x),\qquad \chi(s,y,v)=B\ (s<y).
$$
$K_R\cup\{v\}$ 是真实满25核。加三低根 $L=\{a_1,a_2,a_3\}$ 后，新红六若终于 $v$ 且使用 $L$，源不晚于 $x<y$，与该首帽给的同端蓝三冲突；不用 $L$ 则本已被新核排除。红六只能终于 $L$，且无法使用晚于它的 $v$。其末对图因此给三条匹配，端口仅左owner或 $z$；扣 $z$ 一条后留两个不同左owner，锁满足 $\omega\le L\le x$。

反向，$K_L\cup\{z\}$ 加三高根 $R=\{b_2,b_3,b_4\}$ 给三条首对匹配，扣 $v$ 一条后留两个不同右owner，锁满足 $\psi\ge R\ge y$。$D$ 加四owner为26点同一实际域。任意中间红五只能从左owner到右owner，$\omega\le x<y\le\psi$ 给同端蓝四，违反换色短帽25。

这里两实际匹配根与owner锁只需正确的不等式，不要求相等。未闭事项是从任意d22输入无遗漏地推出上述条件，或排除其它分支；此前错误根序和多纤维无损替换不能填补这项义务。

## 9. 当前交接

已修复：d21的有序／严格交错全分流，故75点必要窗为22至28；一般普通端口共同增广预算和两核缺额至多4保持有效。保留：一个有显式额外假设的d22四／四排除工具。

已撤回：满核自动迫根序、倒二owner的末点自动为其锁、任意多纤维代表替换不损人数、由这些推论导出的d22整层排除。不用文档条数、同会话重读或未运行的外审升级数学接受状态。

## 10. 中性22且双旧根域29：两端不可同时非极值

本节给新的可靠局部推进，反设 $n=75,d=22,r_L=r_R=0$ 且 $x<y$。调用旧75层的 $w=0$ 进口（其出处见旧t0稿§1所列 $n+\mathbf1[w>0]\le75$），所以§7的旧严格交错cut结论仍适用，给
$$
\Omega\cap T\subseteq[y,\infty),\qquad
\Psi\cap T\subseteq(-\infty,x].
\tag{10.1}
$$
两through锁集不交。按(5)，两侧 $k+\kappa+z$ 各为1，实际人口得
$$
t=5+\rho_L+\rho_R,
\quad |T\setminus(\Omega\cup\Psi)|=5.
\tag{10.2}
$$
两旧根域29、最小覆盖4，故 $f,g\in\{4,5\}$，且29域的前两／后两端点命题沿其原证明适用。

假设 $x>\min E$ 且 $y<\max S$。于是 $a_2\le x<y\le b_{g-1}$。两个实际点集
$$
\bigl(\mathcal F\setminus\{y\}\bigr)\sqcup\{b_{g-1},b_g\},\qquad
\{a_1,a_2\}\sqcup\bigl(\mathcal G\setminus\{x\}\bigr)
$$
均只含自由through点，人口分别为 $f+1,g+1$。由(10.2)必须 $f=g=4$，且两集均等于同一自由五点集。因 $a_1,a_2\le x<y\le b_3,b_4$，移去这四个互异外点，得到
$$
c=a_3=b_2,\qquad x<c<y.
\tag{10.3}
$$
$c$ 同时属于冷入、冷出族，是真实双冷点。取 $e=a_1,p=a_2,q=y,s=b_4$，有
$$
e<p<c<q<s,\qquad e\in E,\ s\in S.
$$
实际 $\mathcal F$ 红四给 $\chi(p,c,q)=R$，而[双冷空矩形定理§4](../../../../reports/n7-ordered-red-six-port-cut-20261113/N7_DOUBLE_COLD_PIVOT_CROSSING_EXCEPTIONS_20261113.md)强制该三元组蓝。也可直接前后接冷扇得到以 $c$ 为第三点、首点在 $E$、末点在 $S$ 的实际红五，被该原件§3排除。故
$$
\boxed{n=75,d=22,r_L=r_R=0,x<y\Longrightarrow
x=\min E\ \text{或}\ y=\max S.}
\tag{10.4}
$$
此进口是已经写出的同会话纯解析定理，不依赖其同目录SAT试验；本稿没有升级其外审状态。

### 10.1 恰一个端点极值时的重叠根

设 $y=\max S$ 而 $x>\min E$。由(10.1)及 $y\in\mathcal G$ 避开 $\Omega$，$\rho_L=0$。$\{a_1,a_2\}\sqcup(\mathcal G\setminus\{x\})$ 为自由点集，(10.2)迫 $g=4$，且自由集恰为
$$
\{a_1,a_2,b_2,b_3,y\}.
$$
所有 $\mathcal F$ 点避开 $\Psi$，而through左锁已空，故 $\mathcal F$ 包含在这个自由五点集内。若 $f=5$，它就是按序的 $(a_1,a_2,b_2,b_3,y)$，其中第三点 $b_2$ 双冷、首点 $a_1\in E$、末点 $y\in S$；双冷红五引理矛盾。因此
$$
f=g=4,\qquad
\mathcal F=\{a_1,a_2,c,y\},\quad c\in\{b_2,b_3\}.
\tag{10.5}
$$
若 $\rho_R>0$，还必有 $x>a_2$ 且 $x\in\Psi\cap T$：若 $x=a_2$，不晚于 $x$ 的 $E$ 只有两个已避开 $\Psi$ 的F根，迫 $\rho_R=0$；若 $x>a_2$，它不在上述自由五点中，又不在 $\Omega$，故是through右锁。由(10.1)，它是此族的最大实际点。全序反向给另一单端极值型的对应结论。

若两端都极值 $x=\min E,y=\max S$，只能先得 $\rho_L=\rho_R=0$，进而 $p=q=24,t=5$。本节没有排除这一输入，也没有排除单端极值重叠型或有一个旧根域只有28点的d22分支，故最终窗口仍为22至28。

## 11. 普适五冷族：全局首末、禁第三交点与五／五交形

本节不假设75点、不假设 $d$、M0取等或29点旧根域。定义ambient冷贯穿族
$$
A=\{a\in T:a\text{不能结束ambient }B_4\},\quad
B=\{b\in T:b\text{不能开始ambient }B_4\}.
$$
采用已经纯解析证明的 $|A|,|B|\le5$、各自全红及红五虚拟扇。若有五个冷入贯穿点，就可将其按序记为 $A=(a_1,\ldots,a_5)$；冷出相同。

### 11.1 五个冷入点的前两点是全E前两点

若有 $e\in E,e<a_1$，冷入红扇给实际红五
$$R_5(e,a_1,a_2,a_3,a_4).$$
其首点 $e$ 有入红六、第三点 $a_2$ 冷入，虚拟末扇迫 $\chi(a_3,a_4,a_5)=B$，违 $A$ 全红。

若有 $e\in E\cap(a_1,a_2)$，同样由冷入扇给
$$R_5(a_1,e,a_2,a_3,a_4),$$
首点仍在 $E$、第三点仍为 $a_2$，得到同一矛盾。因此
$$
\boxed{|A|=5\Longrightarrow a_1=\min E,\quad E\cap(a_1,a_2)=\varnothing.}
\tag{11.1}
$$
镜向
$$
\boxed{|B|=5\Longrightarrow b_5=\max S,\quad S\cap(b_4,b_5)=\varnothing.}
\tag{11.2}
$$
这是真正普适结论；29点旧根域只是其中一个caller。此处 $e\in E$ 是实质前提，不无证明地将中性红五末点或其它弱代理代替它。

### 11.2 两个普适禁交与相邻交点的极值代价

若 $a_3\in B$，则实际红五 $A$ 的首点在 $E$、末点在 $S$、第三点双冷，违反双冷红五引理。因此
$$
\boxed{|A|=5\Longrightarrow a_3\notin B,\qquad
|B|=5\Longrightarrow b_3\notin A.}
\tag{11.3}
$$

若 $a_4\in B$，虚拟扇 $\chi(a_4,a_5,s)=B$ 对每个 $s>a_5$，而冷出 $a_4$ 对任何 $s\in S,s>a_5$ 强制同一三元组红。因此
$$
\boxed{a_4\in B\Longrightarrow a_5=\max S.}
\tag{11.4}
$$
镜向
$$
\boxed{b_2\in A\Longrightarrow b_1=\min E.}
\tag{11.5}
$$

此外，五冷虚拟扇本身给 $a_5\in B$：若它开始蓝四，前接 $a_4$ 会得到以 $a_4\in E$ 开始的蓝五，与红六锚禁配。镜向 $b_1\in A$。这是既有五冷自产共冷事实，在此接到(11.1)—(11.5)。

### 11.3 五／五交形的六格必要分类

设 $|A|=|B|=5$，令 $x=b_1\in A,y=a_5\in B$。既有[有序五／五全解析排除§4](N7_NEUTRAL29_ORDERED_COLD_ARMS_20261112.md)给 $x<y$，包括共点端型已被该原件排除。由(11.3)
$$
x\in\{a_1,a_2,a_4\},\qquad y\in\{b_2,b_4,b_5\}.
$$
再由(11.1)—(11.5)，$x=a_4$ 必有 $y=b_5$；$y=b_2$ 必有 $x=a_1$。所以只剩下列六个必要位置组合：

| $x$在A中的位置 | $y$在B中的允许位置 |
| --- | --- |
| $a_1$ | $b_2,b_4,b_5$ |
| $a_2$ | $b_4,b_5$ |
| $a_4$ | $b_5$ |

这是位置分类，不是这些组合已存在的声明。其中 $(x,y)=(a_1,b_2),(a_2,b_4),(a_4,b_5)$ 都只有 $\{x,y\}$ 两个共冷点：其它可能交点被先后次序或(11.3)—(11.5)排除。组合 $(a_1,b_4)$ 至多再有 $a_2=b_2$；组合 $(a_2,b_5)$ 至多再有 $a_4=b_4$。只有 $(a_1,b_5)$ 可能有四个共冷点。

### 11.4 四个共冷点迫唯一中间次序

若 $|A\cap B|=4$，(11.3)使两个不共同点恰为 $a_3,b_3$，所以按序共有点满足
$$
a_1=b_1=c_1,\quad a_2=b_2=c_2,\quad
a_4=b_4=c_3,\quad a_5=b_5=c_4,
$$
其中 $c_1,c_2$ 是全 $E$ 前两点、$c_3,c_4$ 是全 $S$ 后两点。两不共同点都在 $(c_2,c_3)$，但其次序不能任意：
$$
\boxed{b_3<a_3.}
\tag{11.6}
$$
若反设 $a_3<b_3$，冷出 $c_2$ 与 $b_3\in S$ 给 $\chi(c_2,a_3,b_3)=R$；冷入 $c_3$ 与 $a_3\in E$ 给 $\chi(a_3,b_3,c_3)=R$。结合A内红三，得到实际
$$R_5(c_1,c_2,a_3,b_3,c_3).$$
首点 $c_1\in E$、第三点 $a_3$ 冷入，虚拟扇迫 $\chi(b_3,c_3,c_4)=B$，违B全红。两个不共同点不可能相等，所以仅剩(11.6)。

若(11.6)成立，两冷扇还给实际红六
$$R_6(c_1,c_2,b_3,a_3,c_3,c_4).$$
这是额外真实结构，尚非矛盾：其第三点 $b_3$ 未知冷入、第四点 $a_3$ 未知冷出，不能错误套用前述虚拟扇。该六点型与表中其它剩余格仍需原caller的额外H17或人口条件处理，本节不声称排除全部五／五。

