# N7 regular 共同根的加权人口界与临界分支排除

2026-11-04 · **同会话工作证明，unreviewed / unaccepted**。数学由主会话定稿，指定 native gpt-6.1-sol/high 文档执行者忠实转写并做文档检查。主定理适用于任意人口、\(w=0\) 的指定 regular 共同根接口；附录的严格交错、三满核和低参数例分别使用不同前提。

## 1. 实际域、共同根前提与加权结论

母体 \(X\) 是完整有序 rank-3 signotope：四点 packet 至多换色一次，禁 \(B_6,R_7,\mathrm{weak7}\)。路径长度计实际顶点；weak7 的两条异色路径必须有同一对实际首末点，长度和至少为 \(9\)。\(b\) 是实际 756（禁 \(B_5,R_6,\mathrm{weak7}\)）及其换色模型的共同有效整数容量。所有核、路径和角色都在指定实际诱导域重算。

记
\[
\begin{aligned}
S&=\operatorname{Src}_{R_6}(X),&T&=\operatorname{End}_{R_6}(X),&I&=S\cap T,\\
P&=S\setminus T,&Q&=T\setminus S,&D&=X\setminus(S\cup T),\quad |D|=b+q,\\
U&=\operatorname{Src}_{R_5}(D),&V&=\operatorname{End}_{R_5}(D),&w&=|U\cap V|.
\end{aligned}
\tag{1}
\]
固定 \(w=0\)，但不先固定 \(n=|X|\)；令 \(\sigma=n-3b\)。采用 [参数无关 M0，审计稿 §2](N7_7677_PROOF_OBLIGATION_AUDIT_20261103.md)：\(H_L,H_R\) 是包含 \(D\) 的实际 766，人口分别为 \(2b-\alpha,2b-\beta\)。左、右 owner 集为 \(A_H\subseteq P,B_H\subseteq Q\)，唯一锁集为 \(\Omega,\Psi\)，
\[
u=|A_H|-|\Omega|\ge0,\qquad v=|B_H|-|\Psi|\ge0,\qquad
D_{\rm all}=H_L\cap H_R=D\sqcup A_H\sqcup B_H.
\tag{2}
\]
每个左 owner 有 ambient 入红五、出蓝五，其全部出红六末点和出蓝五第二点锁向同一 \(\omega\in\Omega\)；右 owner 完全反序。交叉锁与 owner 不重合。M0 的强普通点性质、完整根扇和实际首末帽均沿用原域。[M0 接口与增强根的展开](N7_WEIGHTED_BILATERAL_COMPENSATION_AND_ENLARGED_ROOTS_20261103.md)

令 \(W=S\setminus\Omega,W'=T\setminus\Psi\)。\(\widehat E\) 收集全部实际红六末对两点同在 \(W\) 的末根；\(\widehat F\) 收集全部实际红六首对两点同在 \(W'\) 的首根。增强根为
\[
\begin{aligned}
E^+&=\widehat E\cup\{r\in I:\text{某实际红六末对为 }(j,r),\ j\in T\},\\
F^+&=\widehat F\cup\{s\in I:\text{某实际红六首对为 }(s,k),\ k\in S\}.
\end{aligned}
\tag{3}
\]
**主定理的 regular 共同根前提**是两增强根族非空，且
\[
\min E^+=\max F^+=z\in I\setminus\Gamma,\qquad
\Gamma=(\Omega\cup\Psi)\cap I,\qquad
\Omega\cap I\subseteq(z,\infty),\quad\Psi\cap I\subseteq(-\infty,z).
\tag{4}
\]
也就是 \(I\) 内早于 \(z\) 的左锁数和晚于 \(z\) 的右锁数均为零。锁可以存在于别处。本结论不覆盖任意共同根或锁根。

置
\[
\begin{aligned}
C&=\operatorname{End}_{R_5}(H_L),&C'&=\operatorname{Src}_{R_5}(H_R),\\
Z_+&=C\cap D,&Z_-&=C'\cap D,\qquad c_\pm=|Z_\pm|,\\
P_H&=P\cap H_R,&Q_H&=Q\cap H_L,\\
K_+&=Z_+\sqcup Q_H\sqcup A_H,&K_-&=Z_-\sqcup P_H\sqcup B_H,\\
\kappa_+&=b-|K_+|=q+\alpha-c_+,&\kappa_-&=b-|K_-|=q+\beta-c_-.
\end{aligned}
\tag{5}
\]
\(K_\pm\) 为实际 756，\(\kappa_\pm\ge0\)。取
\[
A=(I\cap(z,\infty))\setminus\Omega,\qquad
B=(I\cap(-\infty,z))\setminus\Psi.
\tag{6}
\]
在实际域 \(K_-\sqcup B\) 内，\(L\) 是全部实际红六最后相邻对的前驱集合；在 \(K_+\sqcup A\) 内，\(R\) 是全部实际红六第一相邻对的后继集合。这里保留全部实际相邻对，不只保留选定匹配。

定义
\[
\begin{aligned}
\ell_0&=|B|-\kappa_-,&r_0&=|A|-\kappa_+,\\
e_L&=|L|-\ell_0,&e_R&=|R|-r_0,\\
\widetilde C&=(Z_-\setminus L)\cup(Z_+\setminus R),&
H&=(Z_-\setminus L)\cap(Z_+\setminus R),\\
h_U&=|H\cap U|,&h_V&=|H\cap V|,\\
h_0&=|H\setminus(U\cup V)|,&d_D&=|\widetilde C|-q.
\end{aligned}
\tag{7}
\]
因 \(w=0\)，三种重合点的实际角色互斥。令
\[
\Lambda=h_0+\max(u+h_U,\ v+h_V).
\tag{8}
\]
**加权共同根定理。** 在上述全部前提下，任意人口满足
\[
\boxed{\ n+\Lambda\le3b\ }.
\tag{9}
\]
权重依赖于这份指定 regular 共同根接口，不能改成 \(n+w\) 的一般上界。

**临界推论。** 若另有 \(n=3b\)，则
\(u=v=h_U=h_V=h_0=0\)，只剩 \(e_L=1\)、\(e_R=1\)、\(d_D=1\) 三种分支。特别，重复 owner 分支 \(u+v=1\) 和实点重合分支 \(|H|=1\) 均被整类排除。

## 2. 端口分类与一般人口的精确账

左外域无蓝五，全部红六终于 \(B\)。若其最后前驱在 \(S\)，前驱与低根都避开 \(\Omega\)、同在 \(W\)，触发早于 \(z\) 的旧末根，违反 (4)。若前驱在 \(T\)，则触发早于 \(z\) 的增强末根，也矛盾。因此 \(L\subseteq Z_-\)。反序得 \(R\subseteq Z_+\)。此分类确实使用 (4) 的零锁补偿前提。

匹配与实际容量给
\[
|L|\ge|B|-\kappa_-=\ell_0,\qquad
|R|\ge|A|-\kappa_+=r_0.
\tag{10}
\]
每个 \(l\in L\) 有实际末对 \((l,r)\)，其中 \(r<z\)；每个 \(k\in R\) 有实际首对 \((s,k)\)，其中 \(s>z\)。相应两帽禁止任何 ambient 红五从 \(L\) 到 \(R\)：若有，就得到同端蓝四，长度和为 \(9\)。

因为 \(U\subseteq Z_-,V\subseteq Z_+\)，且不存在 \(L\to R\) 红五，
\[
C_D=(U\setminus L)\sqcup(V\setminus R)\subseteq\widetilde C
\tag{11}
\]
命中 \(D\) 内全部红五的端点。删除后是实际换色 756，故 \(|C_D|\ge q\)，\(d_D\ge0\)。此外
\(H\setminus(U\cup V)\subseteq\widetilde C\setminus C_D\)，所以
\[
h_0\le|\widetilde C|-|C_D|\le d_D.
\tag{12}
\]
这里按实际点计数，不把源、末角色副本重复收费。

严格切分只删掉共同根 \(z\) 一次，人口账为
\[
\begin{aligned}
|A|+|B|&=q+\sigma+\alpha+\beta+u+v-1,\\
\ell_0+r_0&=c_-+c_+-q+\sigma+u+v-1.
\end{aligned}
\tag{13}
\]
并集计数给
\[
|\widetilde C|
=c_-+c_+-|L|-|R|-h_U-h_V-h_0.
\tag{14}
\]
从而得到一般人口的精确式
\[
n+(u+h_U)+(v+h_V)+e_L+e_R+h_0+d_D=3b+1.
\tag{15}
\]
空 owner 集、\(q=0\) 和空端口不增加额外假设；所需非空性只能由实际容量强迫，若强迫的实际路径端口为空便直接矛盾。

## 3. 取等反证：先证最大单侧权重界

先证 \(n+\max(u+h_U,v+h_V)\le3b\)。若反例，(15) 与整数性迫
\[
n+\max(u+h_U,v+h_V)=3b+1,\qquad
e_L=e_R=d_D=h_0=0,\quad
\min(u+h_U,v+h_V)=0.
\tag{16}
\]
不妨 \(v+h_V=0\)。于是 \(v=0\)，所有重合点都在 \(U\)，且
\[
\widetilde C=C_D,\quad |C_D|=q,\qquad
Z_-\setminus L=U\setminus L,\quad
Z_+\setminus R=(V\setminus R)\sqcup H_U,\quad H_U=H\cap U.
\tag{17}
\]
实际域
\[
K=D\setminus C_D,\qquad
J_-=(K_-\sqcup B)\setminus L,\qquad
J_+=(K_+\sqcup A)\setminus R
\tag{18}
\]
都恰有 \(b\) 点；\(K\) 无红五，\(J_\pm\) 为实际 756。这里没有要求 \(n=3b\)、\(u=1\) 或 \(|H_U|=1\)。

### 3.1 每个 owner 的实际私有供给

对任意 \(a\in A_H\)，实际域 \(K\sqcup\{a\}\) 有 \(b+1\) 点，换色容量迫红五。若 \(a\) 是内点，两端都在 \(K\)，由 \(D_{\rm all}\) 的端点容器落在 \(L,R\)，违反禁边。若终于 \(a\)，接其 ambient 出蓝五，蓝桥给 \(B_6\)，红桥给从 \(K\subseteq D\) 启动的红六，也不可能。因此有实际
\[
R_5(a\to k),\quad k\in K\cap R.
\tag{19}
\]
反序，对每个 \(b_0\in B_H\) 有实际 \(R_5(j\to b_0)\)，其中 \(j\in K\cap L\)。这不要求全部左纤维为单例，也不要求所有 owner 之间存在匹配。

每个 owner 的入红五与出蓝五还兑现实际末对 \((a,\omega(a))\)；右侧兑现实际首对 \((\psi(b_0),b_0)\)。把 (19) 接到任一实际右外首对 \((s,k)\)，其中 \(s\in A,s>z\)。若 \(\omega(a)<s\)，两帽给与 (19) 同端的 \(B_4(a,\omega(a),s,k)\)，矛盾；等号因 \(A\) 避开 \(\Omega\) 不可能。反序同理，得到
\[
\Omega>z>\Psi.
\tag{20}
\]
若任一实际末对 \((a,r)\) 满足 \(r\le z\)，用同一私有红五和右外首对又得到同端蓝四。因此所有 owner 末对都满足 \(r>z\)；所有右 owner 首对 \((s,b_0)\) 都满足 \(s<z\)。这里的序关系指全部实际供给。

### 3.2 排除旧共同首根

假设有旧首对 \((z,t_0)\)，\(t_0\in T\setminus\Psi\)。owner 首对限制排除 \(t_0\in B_H\)；强普通点性质与其实际出红五给 \(t_0\) 无 ambient 入蓝五。\(t_0>z\)，不在 \(J_-\) 或 \(\Psi\)。实际 \(J_-\sqcup\{t_0\}\) 有 \(b+1\) 点、无蓝五，迫
\[
R_6(g_1,g_2,g_3,g_4,g_5,t_0).
\tag{21}
\]
末点只能是 \(t_0\)：右 owner 需要缺席的 \(\Psi\)，\(B<z\) 的末点无法使用 \(t_0\)，其余点没有 \(T\) 角色。旧首帽使 \(g_1>z\)；\(g_1=z\) 不可能，因为 \(z\) 不在这个域内。\(g_2\) 避开 \(B_H,B\)，故在 \(P_H\sqcup(U\setminus L)\subseteq S\cup U\)。\(z\) 的右扇可以前接到前五点，得到终于 \(g_5\in J_-\) 的实际红六。\(g_5>z\) 不能在 \(B\)；若在 \(B_H\)，则要求 \(z\in\Psi\)，也不可能。矛盾。

### 3.3 排除旧共同末根，包括全部异常点

假设有旧末对 \((j_0,z)\)。owner 末对限制排除 \(j_0\in A_H\)；\(j_0\in S,j_0<z\)，不在 \(J_+\)，有 ambient 入红五、避开 \(\Omega\)，强普通点性质给它无 ambient 出蓝五。旧潜在蓝五需要缺席的 \(\Omega\)，新增点也不出蓝五，所以 \(J_+\sqcup\{j_0\}\) 无蓝五。容量迫
\[
R_6(j_0,g_2,g_3,g_4,g_5,g_6).
\tag{22}
\]
源只能为 \(j_0\)：\(A_H\) 需要缺席的 \(\Omega\)，\(A>z\) 无法使用 \(j_0\)，其余点没有 \(S\) 角色。末帽和 weak7 迫 \(g_6<z\)。\(g_5\notin A_H\)，因为 owner 末对必须终于 \(z\) 右侧；它也不在 \(A\)。

若 \(g_5\in Q_H\cup(V\setminus R)\)，\(z\) 左扇给 \(\chi(g_5,g_6,z)=R\)。把 \(z\) 接到后五点得到实际 \(R_6(g_2,\ldots,g_6,z)\)。\(g_2\in J_+,g_2<z\)，不能在 \(A\)；若在 \(A_H\) 则要求末锁 \(z\in\Omega\)，其余点没有 \(S\) 角色，矛盾。

剩余情形为实际 \(g_5\in H_U\)。对这个实际点，\(K\sqcup\{g_5\}\) 的容量迫 \(D\) 内红五；\(g_5\in U,g_5\notin V\)，故兑现 \(R_5(g_5\to k)\)，其中 \(k\in R\)。取实际首对 \((s,k)\)，\(s>z\)。实际末对 \((g_5,g_6)\) 与它给同端 \(B_4(g_5,g_6,s,k)\)，矛盾。这个论证逐点覆盖全部 \(H_U\)，不要求只有一个异常点。因此
\[
z\notin\widehat E\cup\widehat F.
\tag{23}
\]

### 3.4 右侧零余量的满域矛盾

因 \(v=0\)，右纤维全部为单例，故
\[
F_-=(J_-\setminus B_H)\sqcup\Psi\sqcup\{z\}
\tag{24}
\]
有 \(b+1\) 个实际点，全部在 \(S\cup U\)，无蓝五。容量迫红六，其末点 \(r\le z\)，因为可能的 \(T\) 角色只有 \(B\sqcup(\Psi\cap I)\sqcup\{z\}\)，而 \(\Psi<z\)。

若最后前驱 \(j\in S\)，则 \(j,r\) 都避开 \(\Omega\)、同在 \(W\)，给旧末根 \(r\le z\)，违反增强极值或 (23)。若前驱 \(j=u_0\in U\setminus L\)，实际 \(K\sqcup\{u_0\}\) 的容量、\(C_D\) 的端点覆盖与 \(w=0\) 兑现实际 \(R_5(u_0\to k)\)，其中 \(k\in R\)。取实际首对 \((s,k)\)，\(s>z\)，末对 \((u_0,r)\) 与它给同端 \(B_4(u_0,r,s,k)\)，矛盾。若 \(u+h_U=0\)，完全反序。由此排除 (16)，证明最大单侧权重界。

## 4. 加入无角色重合点与临界推论

若 \(h_0=0\)，§3 已给 (9)。若 \(h_0\ge1\)，由 (12)、(15) 直接有
\[
\begin{aligned}
n+h_0+\max(u+h_U,v+h_V)
&=3b+1-\min(u+h_U,v+h_V)-e_L-e_R-d_D\\
&\le3b.
\end{aligned}
\tag{25}
\]
这证明最终加权式，不新增路径推断。

另取临界人口 \(n=3b\)，则 \(\Lambda=0\)，从而 \(u=v=h_U=h_V=h_0=0\)。代入 (15) 得 \(e_L+e_R+d_D=1\)，只剩三种单单位分支。原来的 \(u+v=1\) 与 \(|H|=1\) 两个整类排除都由此统一得到；重合点始终按真实 \(D\) 内源、末、无角色三种身份分类。

## 5. 剩余三分支的精确边界

当 \(e_L=1\) 时，\(J_-\) 有 \(b-1\) 点，\(J_+\) 有 \(b\) 点；可得旧末根排除。右替锁迫旧首对 \((z,t_0)\)，但 \(J_-\sqcup\{t_0\}\) 只是满 \(b\) 点 756。随后加入 \(z\) 时，实际红六允许正从 \(z\) 启动并终于 \(t_0\)。不能再使用 §3.2 中“\(g_1\ne z\)”的身份排除。\(e_R=1\) 完全反序。

当 \(d_D=1\) 时，由 \(\widetilde C\) 直接删出的 \(\widetilde K=D\setminus\widetilde C\) 只有 \(b-1\) 点。尚未排除另一份更好的实际覆盖；不能声称最大的红五自由核只有 \(b-1\) 点。上述剩余条件也不是已经构造的反例。

## 附录 A. 严格交错下完整低锁关系无分叉

本附录改用 [11 月 3 日严格交错取等结构](N7_T0_CRITICAL_LAYER_AND_SATURATION_BARRIERS_20261103.md) 的前提：\(x_e<c<y_f\)，\(K=D_{\rm all}\setminus C_{\rm phys}\) 为 \(b\) 点红五自由核，保留每个低左锁 \(\omega<c\) 的最早 owner \(a_\omega\)。这与 (4) 的共同根前提不同。

定义**全部实际关系**
\[
j\sim\omega\quad\Longleftrightarrow\quad
\text{存在 ambient }B_5(j,\omega,p_3,p_4,p_5),
\quad j\in Z_+\setminus R,\quad\omega\text{ 为低左锁}.
\tag{26}
\]
此完整关系是 partial matching，而非只说可选出一份匹配。固定 \(\omega\)，令 \(F_\omega\) 为其全部相邻 \(j\)。这些 \(j\) 是覆盖点，不在 \(K\)。实际域
\[
Y=(K\setminus\{a_\omega\})\sqcup F_\omega\subseteq D_{\rm all}
\tag{27}
\]
无红五。若红五终于 \(K\)，末角色在 \(R\)；若源在 \(K\)，它在 \(L\)；若源在 \(F_\omega\)，它已承担末覆盖，角色到实际点的单射迫其源角色也在 \(L\)。两种情形都违反 \(L\to R\) 禁边。若终于 \(j\in F_\omega\)，接其蓝五，蓝桥给 \(B_6\)，红桥给 \(R_6(k\to\omega)\)。源 \(k\) 必为 \(A_H\) 中同一锁纤维的 owner，但 \(Y\) 内该纤维唯一保留的 \(K\)-owner \(a_\omega\) 已被删去，矛盾。实际容量给
\[
b-1+|F_\omega|\le b,\qquad |F_\omega|\le1.
\tag{28}
\]
固定 \(j\)，实际 \(K\sqcup\{j\}\) 迫一条终于 \(j\) 的红五；源分支已由 \(L\to R\) 禁边排除。若 \(j\) 同时邻接 \(\omega_1,\omega_2\)，把**同一条**实际红五分别接到两蓝五，得到同一首点 \(k\) 到两个不同锁的红六，违反 owner 唯一末锁。故另一侧度也至多一。高右锁的完整关系完全反序。

插锁所得 \(B_5(j,\omega,p_3,p_4,p_5)\) 可改选成 \(B_5(a_\omega,\omega,p_3,p_4,p_5)\)：实际末对 \((a_\omega,\omega)\) 的末帽给第一个三元组为蓝，其余三元组沿原路径。这只是存在性改选，不能从全部路径分析中删掉中性首点。\(|F_\omega|=0\) 或 \(1\) 的无分叉情形仍开放；本附录没有人口下降。

## 附录 B. 三满核的端点图仍未闭合

当 \(I=\varnothing,n=3b\) 时，既有结论给 \(S,D,T\) 各 \(b\) 点，\(H_L=D\sqcup T,H_R=S\sqcup D\) 均满 766，\(D\) 无红五，\(S,T\) 无蓝五，并有四类实际私有供应。[三满核入口与供应](N7_T0_CRITICAL_LAYER_AND_SATURATION_BARRIERS_20261103.md)

令 \(G_6\subseteq S\times T\) 为全部 ambient 红六的实际首末点图。则
\[
\nu(G_6)=b.
\tag{29}
\]
这是实际首末点的匹配，不宣称相应红六内部顶点互不相交。若匹配不足 \(b\)，König 给少于 \(b\) 个 \(S,T\) 角色的覆盖。两集不交，删去这些实际点即截断全部红六，余下超过 \(2b\) 点的实际 766，违反 \(2b\) 容量。

纯 \(D^4\) 图 \(G_6^D\) 只保留实际 \(R_6(s,D^4,t_0)\)。它无孤点：纯 \(R_5(s,d_1,d_2,d_3,d_4)\) 接纯 \(B_5(d_4,t_1,t_2,t_3,t_4)\)，蓝桥会给 \(B_6\)，故红桥兑现 \(R_6(s,D^4,t_1)\)；右侧反序。但 \(G_6\) 的完美匹配不能直接运输为 \(G_6^D\) 的完美匹配。对纯图 Hall 坏集删点后，仍可能存在内部使用多个 \(S,T\) 点的红六。无孤点不等于 Hall 条件。纯 \(S\to D\) 红五图甚至不可能完美匹配：所有纯红五末点都避开 \(D\) 最早的三个实际点。

若 \(b>20\)，\(S\sqcup T\) 不能是 766。否则它是满 \(2b\) 点 766；\(S\) 无 ambient 蓝五末点、\(T\) 无 ambient 蓝五首点，角色分划迫 \(S=\operatorname{Src}_{R_5}=\operatorname{Src}_{B_5}\)、\(T=\operatorname{End}_{R_5}=\operatorname{End}_{B_5}\)。于是 \(S,T\) 各自同时无红五、蓝五，经典容量各至多 \(20\)，矛盾。这仍未排除三满核母体。

## 附录 C. 757 的真实联合插点反例

取实际点集 \(X=\{1,\ldots,10\}\)，
\[
C_1=\{1,2,3,4\},\quad C_2=\{4,5,6,7\},\quad C_3=\{7,8,9,10\}.
\tag{30}
\]
三元组染蓝当且仅当同属某个 \(C_i\)，其余染红。packet 只有 BBBB、BRRR、RRRB、RRRR，故完整合法。蓝四恰为三个 \(C_i\)，无蓝五。任何红链 \(P_0\) 在每个 \(C_i\) 至多取两点，因而
\[
|P_0|+\mathbf1[4\in P_0]+\mathbf1[7\in P_0]\le6,
\tag{31}
\]
所以无红七。若实际首末点同属某 \(C_i\)，其间全蓝，红路径至多两点；否则不存在同端蓝三。因此异色路径同端长度和至多八，是实际 757。

canonical 集 \(A\) 为没有 ambient 蓝四末点的点集：
\[
A=\{1,2,3,5,6,8,9\}.
\tag{32}
\]
\(A\sqcup\{7\}\)、\(A\sqcup\{10\}\) 分别无蓝四，但同时加入两点便含 \(C_3\)。红六恰为从 \(\{1,2,3\}\) 取两点、保留 \(\{5,6\}\)、再从 \(\{8,9,10\}\) 取两点，所以红六源为 \(\{1,2\}\)。canonical \(B=X\setminus\{1,2\}\)，确有 \(7,10\in B\setminus A\)。

该例蓝四最小横截数为二，红六最小横截数为一。取 \(Y=X\setminus\{4,7\}\) 无蓝四、\(Z=X\setminus\{5\}\) 无红六，则
\[
|Y|+|Z|-|X|=8+9-10=7.
\tag{33}
\]
两种最小横截数也给这个联合目标的上界七，故该低参数联合目标恰为七；它与本文的锁集 \(\Omega\) 无关。此例关闭 [R6 §5](RESET_R6_OVERLAP_TWO_AND_766_TRANSFER.md) 的原 canonical 单点兼容命题，不是目标值一或四十点反例，也不否定真正的联合交换。

## 6. 当前人口界与未闭合范围

先保留参数形式。以 \(a\) 为 747 的有效容量，当前无条件人口工作链仍为
\[
N_{\rm sig}(7,5,7)\le a+b-1,\quad
N_{\rm sig}(7,6,6)\le2b,\quad
N_{\rm sig}(7,6,7)\le3b,\quad
N_{\rm sig}(7,7,7)=N_{\rm sig}(7,6,7)+1\le3b+1.
\tag{34}
\]
采用历史 \(a=16,b=25\)，仍为 **40、50、75、76**。新增加权界只在指定 regular 共同根子类给
\[
n+\Lambda\le75.
\tag{35}
\]
若 \(\Lambda\ge1\)，该子类有 \(n\le74\)；零权重情形仍开放。在上述 regular 共同根接口内，临界 \(n=75\) 时只剩 \(e_L=1,e_R=1,d_D=1\)。没有得到全局七十四点界或 777 的七十五点界，也不能把 \(w\) 加进最终公式。旧输入、历史人工接受、same-family/provisional 保证和证书绑定均沿用，不因同会话证明或文档检查而升级。[既有人口界](N7_LOCK_REPLACEMENT_COMMON_ROOT_EXCLUSION_AND_7576_BOUND_20261103.md) · [历史研究综述](../../../../RESEARCH_SYNTHESIS_N7_20261103.md)

共同根的三种剩余分支、严格交错的无分叉低锁、严格分离缺少实际一顶点、根族为空但 \(I\ne\varnothing\) 的情形、空 \(I\) 三满核、757 真正双点联合交换和一般满 766 仍未闭合。附录的反例或必要结构不作这些剩余分支的真实实现。

本轮没有新增全局数值下降。新增数学均为 **same-session、unreviewed / unaccepted**；主会话另行同会话反检也不构成独立复审。本轮未调用外部审阅、运行科研代码、枚举、求解或证书重放。文档执行者只新增本文、根目录更新和文档回执，不改旧任务、runtime、git 内容或旧文档。[根目录更新](../../../../RESEARCH_SYNTHESIS_N7_20261104_COMMON_ROOT_UPDATE.md) · [文档核验回执](N7_T0_COMMON_ROOT_DOCUMENT_RECEIPT_20261104.md)
