# N7 的 \(t=0\) 临界层与饱和障碍

2026-11-03 · **同会话工作证明，unreviewed / unaccepted**。数学由主会话定稿，指定文档执行者转写并核验文件。本稿给出空 \(I\) 的参数子类界，并记录 \(t=0\) 的严格交错结构与若干路线的适用边界。

## 1. 模型和空 \(I\) 子类界

模型为完整有序 rank-3 signotope，四点 packet 至多换色一次。路径长度计实际顶点，weak7 禁止两条同实际首末点的异色路径长度和至少 \(9\)。\(b\) 是 756（禁 \(B_5,R_6,\mathrm{weak7}\)）及换色 756 的共同有效整数容量，\(a\) 为 747 的有效容量。母体 \(X\) 是 767（禁 \(B_6,R_7,\mathrm{weak7}\)），\(n=|X|\)。令
\[
S=\operatorname{Src}_{R_6}(X),\quad T=\operatorname{End}_{R_6}(X),\quad
I=S\cap T,\quad D=X\setminus(S\cup T),\quad |D|=b+q.
\tag{1}
\]
\(U=\operatorname{Src}_{R_5}(D)\)、\(V=\operatorname{End}_{R_5}(D)\) 按实际 \(D\) 内路径定义，\(w=|U\cap V|\)，\(t=n+w-3b\)。既有 \(n+\mathbf1[w>0]\le3b\) 与 \(n+w\le3b+1\) 沿用。下一人口层 \(n=3b\) 迫 \(w=0,t=0\)。[既有人口与加权界](N7_7576_DEPENDENCY_AUDIT_AND_SINGLE_THROUGH_EXCLUSION_20261103.md)

**空 \(I\) 子类定理。** 若 \(I=\varnothing\)，则
\[
n+\max(|U|,|V|)\le3b .
\tag{2}
\]
证明不调用 M0。任何 \(S\) 点若有 ambient 入蓝五，与其出红六连接时，蓝桥给 \(B_6\)，红桥给 \(R_7\)。任何 \(U\) 点若有 ambient 入蓝五，与其 \(D\) 内出红五连接时，蓝桥给 \(B_6\)，红桥给终于 \(D\) 的实际红六。故 \(S\sqcup U\) 无蓝五。\(I=\varnothing\) 使 \(S\sqcup U\) 避开全部红六末点 \(T\)，故它是实际 756，\(|S|+|U|\le b\)。反序给 \(|T|+|V|\le b\)。\(D\setminus U,D\setminus V\) 均无红五且继承蓝六和 weak7 禁形，换色容量给 \(|D|\le b+\min(|U|,|V|)\)。相加即得 (2)。特别，只要 \(I=\varnothing\) 且 \(D\) 有实际红五，就有 \(n\le3b-1\)。该结论对整个所述子类成立，无需额外假设 \(w=0\)。

**空 \(I\) 的三满核入口。** 若 \(n=3b,\ I=\varnothing\)，(2) 迫 \(U=V=\varnothing\)，并使三项容量同时取等。因此
\[
|S|=|D|=|T|=b,\qquad H_L=D\sqcup T,\qquad H_R=S\sqcup D .
\tag{3}
\]
\(H_L\) 避开 \(S\)，\(H_R\) 避开 \(T\)，故都是实际满 \(2b\) 点 766。\(D\) 无红五，\(S,T\) 无蓝五。

在任一实际满 766 核 \(H\) 中，红五源与蓝五末点分划 \(H\)，蓝五源与红五末点也分划 \(H\)，四个角色集各 \(b\) 点。连接禁配使两对角色分别不交，删去任一全源或全末角色后进入相应容量域，给各角色至少 \(b\) 点，因而恰好取等。\(S\) 无 ambient 蓝五末点，故在 \(H_R\) 中 \(S=\operatorname{Src}_{R_5}(H_R)\)，\(D=\operatorname{End}_{B_5}(H_R)\)。反向，在 \(H_L\) 中 \(T=\operatorname{End}_{R_5}(H_L)\)，\(D=\operatorname{Src}_{B_5}(H_L)\)。[完整满核入口 §2](N7_FULL_PAIR_FAN_BOUNDARY_AND_TIGHT_CORE_DICHOTOMY_20261029.md)

四类逐点供应在各自实际域内兑现。对每个 \(s\in S\)，\(D\sqcup\{s\}\) 的换色容量迫一条红五，首点只能是 \(s\)，其余四点在 \(D\)。对每个 \(t_0\in T\)，反序迫 \(R_5(D^4,t_0)\)。对每个 \(d_0\in D\)，\(S\sqcup\{d_0\}\) 无红六，756 容量迫蓝五，末点只能是 \(d_0\)。反序 \(T\sqcup\{d_0\}\) 迫 \(B_5(d_0,T^4)\)。这些存在性给出
\[
R_5(s,D^4),\qquad R_5(D^4,t_0),\qquad B_5(S^4,d_0),\qquad B_5(d_0,T^4).
\tag{4}
\]
它们没有提供完美 \(S\to D\) 或 \(D\to T\) 端点匹配。

若 \(b>20\)，经典红蓝五自由容量 \(\binom{6}{3}=20\) 迫 \(D\) 内有实际蓝五。由满核的另一对角色分划，这条蓝五的首点在 \(D\) 占去 \(H_R\) 的一个非红五末点角色，所以 \(H_R\) 中有红五终于 \(S\)。反向，蓝五末点在 \(D\) 占去 \(H_L\) 的一个非红五源角色，故 \(H_L\) 中有红五始于 \(T\)。这些新路径可含多个 \(S\) 或 \(T\) 点，尚未与 (4) 接成同端禁形或实际容量损失。三满核入口仍开。空 \(I\) 只覆盖根族为空的一部分。例如单侧 \(\widehat E=\varnothing\) 由旧基底容量只迫 \(\alpha=u=0\)，仍可有 \(I\ne\varnothing\)。[经典盒容量与满核供给](RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md) · [旧基底与根工具](N7_WEIGHTED_BILATERAL_COMPENSATION_AND_ENLARGED_ROOTS_20261103.md)

## 2. \(t=0\) 严格交错的实际取等

以下固定 \(n=3b,w=0\) 且两侧有效增强根有 \(x_e<y_f\)。沿用参数无关 M0 及既有双向间隙构造。\(H_L,H_R\) 的缺额为 \(\alpha,\beta\)。左、右 owner 集为 \(A_H,B_H\)，锁为 \(\Omega,\Psi\)，余量 \(u=|A_H|-|\Omega|,\ v=|B_H|-|\Psi|\)。置 \(C=\operatorname{End}_{R_5}(H_L),\ C'=\operatorname{Src}_{R_5}(H_R)\)，\(Z_+=C\cap D,\ Z_-=C'\cap D\)，\(P_H=(S\setminus T)\cap H_R,\ Q_H=(T\setminus S)\cap H_L\)。基础实际 756 核 \(K_+=Z_+\sqcup Q_H\sqcup A_H,\ K_-=Z_-\sqcup P_H\sqcup B_H\)，缺额为 \(\kappa_+=q+\alpha-|Z_+|,\ \kappa_-=q+\beta-|Z_-|\)。交叉锁排除给 \(D_{\rm all}=H_L\cap H_R=D\sqcup A_H\sqcup B_H\)。[M0、实际基础核与双向间隙](N7_WEIGHTED_BILATERAL_COMPENSATION_AND_ENLARGED_ROOTS_20261103.md)

取间隙 \(x_e<c<y_f\)，其中 \(c\) 不是实际点。记 \(\Gamma=(\Omega\cup\Psi)\cap I\)，取 \(A=(I\cap(c,\infty))\setminus\Omega,\ B=(I\cap(-\infty,c))\setminus\Psi\)。\(\mathcal R\) 收集所有实际红六末对 \((j,r_0)\) 的普通前驱，要求 \(r_0\in I,\ r_0<c,\ j\in S\setminus A_H\)。\(\mathcal Q\) 收集所有实际红六首对 \((s_0,k)\) 的普通后继，要求 \(s_0\in I,\ s_0>c,\ k\in T\setminus B_H\)。因 \(w=0\)，基底无额外的 \(C_0\) 项。原加强扇与相应的实际帽给 \(\mathcal R\subseteq P\setminus A_H,\ \mathcal Q\subseteq Q\setminus B_H\)，其中 \(P=S\setminus T,\ Q=T\setminus S\)。记 \(r=|\mathcal R|,\ h=|\mathcal Q|\)。定义
\[
\mu=\min(q+|A_H|+|B_H|,0),\qquad
\delta_{\rm low}=|\Omega\cap I\cap(-\infty,c)|,\qquad
\varepsilon_{\rm high}=|\Psi\cap I\cap(c,\infty)|.
\]
既有双向式的交会下界为 \(t+\delta_{\rm low}+\varepsilon_{\rm high}-\mu\)。此处 \(t=0\)，任一低侧左锁、高侧右锁或负截断都会迫严格正的交会数。故
\[
\delta_{\rm low}=\varepsilon_{\rm high}=0,\qquad
\mu=0,\qquad m=q+|A_H|+|B_H|\ge0 .
\tag{5}
\]
实际左扩域为 \(K_-\sqcup\mathcal Q\sqcup B\)，实际右扩域为 \(K_+\sqcup\mathcal R\sqcup A\)。取全部实际外相邻对，在左侧删 \(\mathcal R\) 前驱，在右侧删 \(\mathcal Q\) 后继，得全部剩余端口 \(L\subseteq Z_-\sqcup A_H,\ R\subseteq Z_+\sqcup B_H\)。容量给匹配下界
\[
\ell_0=|B|-\kappa_-+h-r,\qquad
r_0=|A|-\kappa_++r-h .
\tag{6}
\]
实际两帽禁止任何 ambient 红五从 \(L\) 到 \(R\)。

在实际 \(D_{\rm all}\) 内用源、末容器 \(U_c=Z_-\sqcup A_H\sqcup(C'\cap B_H)\)、\(V_c=Z_+\sqcup B_H\sqcup(C\cap A_H)\)。角色覆盖 \((U_c\setminus L)\sqcup(V_c\setminus R)\) 命中全部红五的端点。其实际点像记为 \(C_{\rm phys}\)。由换色容量、容器界和间隙人口式，
\[
m\le |C_{\rm phys}|\le |U_c|+|V_c|-|L|-|R|\le m .
\tag{7}
\]
全取等，故 \(|L|=\ell_0,\ |R|=r_0\)，且角色映到实际点单射。左外匹配在删普通前驱前至少有 \(|B|-\kappa_-+h\) 条，删后至多 \(|L|\) 条，故其恰有 \(r\) 条边因 \(\mathcal R\) 而被删，全部 \(\mathcal R\) 都在左实际域内。由于 \(\mathcal R\subseteq (S\setminus T)\setminus A_H\)，这给 \(\mathcal R\subseteq P_H\)。反向给 \(\mathcal Q\subseteq Q_H\)。容器等号又给
\[
|C\cap A_H|=u,\quad C\cap A_H\subseteq L,\qquad
|C'\cap B_H|=v,\quad C'\cap B_H\subseteq R.
\tag{8}
\]
例如 \(C\cap A_H\) 的点都承担末覆盖，因为 \(R\) 不含左 owner，故不得再承担源覆盖。这些等式允许 \(u,v>0\)。

实际删点核为
\[
\begin{aligned}
J_-&=(K_-\sqcup\mathcal Q\sqcup B)\setminus(\mathcal R\sqcup L),\\
J_+&=(K_+\sqcup\mathcal R\sqcup A)\setminus(\mathcal Q\sqcup R),\\
K&=D_{\rm all}\setminus C_{\rm phys}.
\end{aligned}
\tag{9}
\]
两侧删点击中所有实际红六，并继承无蓝五，由 (6)–(7) 各剩 \(b\) 点，故 \(J_\pm\) 是满 756。\(K\) 有 \(b\) 点、无红五，是实际 766 的诱导子域。

**纤维二分。** 任一左纤维或者为单例、owner 不在 \(L\) 且锁在 \(c\) 右侧，或者所有 owner 都在 \(L\)、锁 \(\omega\in T\setminus S\) 且 \(\omega<c\)。若 \(a_0\in A_H\cap L\)，取兑现它的低末对 \((a_0,r_{a_0})\)。若 \(\omega>r_{a_0}\)，帽与从 \(a_0\) 到 \(\omega\) 的实际红六构成同端 weak7。等号也不可能，因为 \(r_{a_0}\in I\) 且低侧无左锁。故 \(\omega<r_{a_0}<c\)，且 \(\omega\notin I\)。

等号 \(|C\cap A_H|=u\) 使每个纤维的所有非最早 owner 都在 \(C\cap A_H\subseteq L\)。若最早 owner \(a_0\notin L\)，它是纯源覆盖点，因为最早 owner 不在 \(C\)。\(K\sqcup\{a_0\}\) 的换色容量迫一条实际红五，端点覆盖迫其源为 \(a_0\)、另一端在 \(R\)。连接 \(a_0\) 的实际锁末对与该端点的实际右首对，若锁在 \(c\) 左侧便产生同端蓝四，故锁在 \(c\) 右侧。锁恰在间隙 \(c\) 处不可能。这排除同纤维有任何在 \(L\) 的 owner，故该纤维为单例。反序得右纤维二分。\(K\) 保留低左纤维的最早 owner 和高右纤维的最晚 owner，因而 \(K\) 一般不能当作纯中性核。

**满侧整类排除。** 若 \(\alpha=0\)，则 \(A_H=\Omega=\varnothing\)。\(V\subseteq Z_+\)，删 \(V\) 后的容量给 \(|V|\ge q\)，故 \(0\le\kappa_+=q-|Z_+|\le0\)。实际增广 \(K_+\sqcup\mathcal R\) 的容量迫 \(\mathcal R=\varnothing\)。但低根 \(x_e\) 有实际末对，其前驱在 \(S\cup T\)。高根 \(y_f\) 的左扇与末帽排除该前驱在 \(T\)，故它是位于 \(S\setminus(T\cup A_H)\) 的低普通前驱，必须在 \(\mathcal R\)，矛盾。反序排除 \(\beta=0\)。所以严格交错只能双正缺额。这是旧满侧工具在 \(t=0\) 的重核，人口界无新下降。

## 3. 低锁插点为何停在蓝五

取 §2 的低左锁 \(\omega\in T\setminus S,\ \omega<c\)。\(J_+\) 避开全部左锁，故 \(J_+\sqcup\{\omega\}\) 恰有 \(b+1\) 点。每点有 ambient 入红五。若有红六，必用 \(\omega\)，其源只能在 \(A,\mathcal R,A_H\)。从 \(A>c\) 启动无法使用 \(\omega\)。从 \(j\in\mathcal R\) 启动时，原低末对帽迫其末点不晚于对应低根 \(r_j<c\)，第四点有 ambient 入红五，故可尾换 \(y_f\)，与原帽给的同端蓝三冲突。从 \(A_H\) 启动时，唯一锁迫其终于 \(\omega\)，再尾换 \(y_f\) 便违反唯一锁。故这个实际域无红六，容量迫蓝五
\[
B_5(j,\omega,p_3,p_4,p_5),\qquad j,p_3,p_4,p_5\in J_+ .
\tag{10}
\]
其首点不能在 \(A,\mathcal R,Q_H\) 或 \(\{\omega\}\)，这些点无 ambient 出蓝五。基础核其余点的出蓝五第二点在 \(\Omega\)，而新域唯一的左锁是 \(\omega\)，故第二点正是 \(\omega\)。

保留两种首点情形。若 \(j\in A_H\)，它是 \(\omega\) 的 owner。若 \(j\in Z_+\setminus R\)，它是末覆盖点。\(K\sqcup\{j\}\) 的容量迫实际红五，并且 \(j\) 必为其一个端点。若红五从 \(j\) 启动，则 \(j\) 的源角色不能再承担覆盖，否则违反 (7) 的实际点单射，故 \(j\in L\)，另一端在 \(R\)，违反 \(L\to R\) 禁边。于是有实际红五终于 \(j\)。接上 (10) 时蓝桥给 \(B_6\)，故红桥兑现一条终于 \(\omega\) 的红六。源是 \(K\) 内同纤维的最早 owner \(a_0\)，因为 \(K\) 只保留该纤维这一位，且 \(j\) 属于中性域。由此得到实际 \(R_5(a_0\to j)\)。反序同理。若在 \(K\) 中换出 \(a_0\) 并换入 \(\omega\)，得到实际 \(b\) 点 766，除已移出的 \(a_0\) 外，所有保留 owner 的外锁仍缺席，新增 \(\omega\) 不会成为红六源，而 \(K\) 中没有其他同纤维 owner。新域已离开 \(D_{\rm all}\)，新增红五不受原端点覆盖控制，换后无红五仍待证。

## 4. 其他 \(t=0\) 根序的容量缺口

若严格分离 \(x_e>y_f\)，此前 \(t\ge1\) 的排除不适用。零松弛切分转移的探索可在有条件时把左右供给接到同一条实际 \(R_5(u_0\to v_0)\)。若外对为 \((u_0,r_0),(r_0,v_0)\)，两帽只给同端 \(B_3(u_0,r_0,v_0)\)。与红五总长为 \(8\)，仍缺实际一顶点。这里记录的是条件转移的缺步。

共根 \(z\notin\Gamma\) 时，严格切分删掉 \(z\) 一次。设 \(\delta_{\rm low}\) 数 \(I\) 内早于 \(z\) 的左锁，\(\varepsilon_{\rm high}\) 数 \(I\) 内晚于 \(z\) 的右锁。沿用双向切分在两侧各避本侧锁，\(t=0,w=0\) 的人口账为
\[
|A|+|B|=q+\alpha+\beta+u+v+\delta_{\rm low}+\varepsilon_{\rm high}-1 .
\]
所以角色覆盖上界为 \(m+1-\delta_{\rm low}-\varepsilon_{\rm high}\)。尤其在两项锁补偿都为零的子类中，上界允许 \(m+1\)，原来迫单射的 \(m\) 等号不再得到。此前精确覆盖、单例纤维和替锁矛盾的整条证明因此未覆盖该子类。空根族还包括 \(I\) 非空的单侧空族。本节保留这些情形，未给出完整排除。

## 5. 空 \(I\) 路线的实际反例

**空 \(I\) 不迫源侧无红五。** 对整数 \(p\ge3\)，取块 \(A_p<P_{p-1}<t_0\)。仅将恰含两个 \(A_p\) 点与一个 \(P_{p-1}\) 点的三元组染蓝，其余染红。全部 packet 为 RRRR、RBBB、BBRR 或 BRRR。红路径若不含 \(P_{p-1}\)，长度至多 \(p+1\)。若含它，至多有一个 \(A_p\) 点，长度也至多 \(p+1\)。蓝最长为三，实际蓝三的首末只能从 \(A_p\) 到 \(P_{p-1}\)，这对端点间的红路径至多 \(p\) 点。蓝两点与红 \(p+1\) 的长度和也只有 \(p+3\)。故无 \(R_{p+2},B_{p+1},\mathrm{weak}(p+2)\)。

每个 \(A_p\) 点可前接到 \(P_{p-1}\sqcup\{t_0\}\) 得实际红 \(p+1\)。任意红 \(p+1\) 都需用 \(t_0\) 作末点、用 \(A_p\) 点作首点。于是
\[
\operatorname{Src}_{R_{p+1}}=A_p,\qquad
\operatorname{End}_{R_{p+1}}=\{t_0\},\qquad I=\varnothing .
\tag{11}
\]
\(A_p\) 内本身有红 \(p\)。取 \(p=5\)，得实际十点 767，\(S\) 有红五。三元组 \((a_4,a_5,p_1)\) 为蓝，直接挡住沿源块尝试的同色拼接。该例缺少三核等大饱和，因此并未达到 \(n=3b\)。

既有十三点 756 反例的颜色对偶属于换色 756，也属于 767。该对偶的中性域有蓝五及逐点双向蓝五供应，说明这些条件仍不足以单独排除三满核。需要在同一饱和母体上联合使用 §1 的四类私有供应及实际端点身份。[既有三块反例族](N7_THROUGH_CLIQUE_COUNTERFAMILY_AND_LOWER_PARAMETER_FRONTIER_20261103.md)

## 6. 相邻双点复制的整族阻断

取 \(p\ge3\)，母体禁 \(R_{p+1},B_{p+1},\mathrm{weak}(p+2)\)。选点集 \(T_{\rm dup}\)，将每个选点 \(v\) 复制为相邻 \(v^-<v^+\)。每对可独立取 F 或 G。F 规定 \(\chi(x,v^-,v^+)=B\) 对 \(x<v\)，\(\chi(v^-,v^+,y)=R\) 对 \(v<y\)。G 交换这两色。来自三个不同原点的三元组继承原色。若一对复制点居 packet 首或末，新包为 \(\theta\theta cc\) 或 \(cc\theta\theta\)。若该对居中，新包为 \(\neg\theta,c,c,\theta\)。若有两对复制点，新包为 \(\theta\theta\phi\phi\)。均至多换色一次，故扩张完整合法。

若输出还禁 \(R_{p+2},B_{p+1},\mathrm{weak}(p+2)\)，则 \(T_{\rm dup}\) 中无实际红 \(p\) 和蓝 \(p\)。对一条在 \(T_{\rm dup}\) 中的红 \(p\)，记两端 \(a_0<b_0\)，分别看它们的取向。

- FF 时，用 \(a_0\) 的双点得到 \(R_{p+1}\)，与 \(B_3(a_0^-,b_0^-,b_0^+)\) 同端。
- GG 时，用 \(b_0\) 的双点得到 \(R_{p+1}\)，与 \(B_3(a_0^-,a_0^+,b_0^+)\) 同端。
- GF 时，原红 \(p\) 提升到以 \(a_0^-,b_0^+\) 为端点的实际路径，四个端点复制点构成同端蓝四。
- FG 时，两个端点都用双点，直接得到 \(R_{p+2}\)。

前三项的异色长度和均为 \(p+4\)。若 \(T_{\rm dup}\) 有实际蓝 \(p\)，只要首点取 G 或末点取 F，双点延长即给 \(B_{p+1}\)。余下 FG 的四个端点复制点构成红四，与原蓝 \(p\) 的提升路径同端，长度和为 \(p+4\)。所以由经典杯帽容量，
\[
|T_{\rm dup}|\le\binom{2p-4}{p-2}.
\tag{12}
\]
取 \(p=5\)，至多复制二十个点。故从满 \(2b\) 点 766 出发，这一整族独立取向的相邻双点复制至多得到 \(2b+20\) 点 767。在现行容量输入下，该机制无法把满 766 推过现有 767 人口工作界，范围限于上述复制扩张。

757 的 canonical 支持 DAG 仍只兑现单点。唯一单色汇点的混合蓝四会离开受限支持类，也未增长到蓝五。第二单位要求命中同时加入两点才出现的全部新蓝四，仍缺实际双点证书。[单点增广与联合路径边界](RESET_R5_COVER_AUGMENTATION_CAPACITY.md) · [第二单位重叠](RESET_R6_OVERLAP_TWO_AND_766_TRANSFER.md)

## 7. 合法蓝根换 chart 的负对照

从 767 添最左蓝根 \(p_0\) 得 777。对当前 chart 全反序并保持颜色，在原最大点 \(q_0\) 作 R20 红径向归一化，删 \(q_0\) 再换色，所得 767 是同一 777 交替符号 \(\omega\) 的合法蓝根移动所对应的删根域。旧点 \(x<y<q_0\) 在新序中满足 \(x<'y\) 当且仅当 \(\chi(x,y,q_0)=B\)。原新增的 \(p_0\) 成为新最小点。另一种全反序同时按奇偶翻色的操作中，原新增点成为新最大，做两次可复原。这里使用前一种根移动。合法蓝根只在有限轨道内变换，不能任取内部 pivot。[R20 合法径向归一化](RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md) · [合法根循环 §3.6](N7_JOINT_THROUGH_SATURATION_AND_ORDERED_CUTS_20261030.md)

取 \(U_6<V_5\)，块内分别全红、全蓝，混色规定 \(UUV=B,\ UVV=R\)。packet 合法。跨块单色路径至多三点，块内红至多六、蓝至多五，同端长度和至多八。故是实际 767，且唯一红六是 \(U_6\)，中性域删去 \(u_1,u_6\) 后无红五，\(w=0\)。

添 \(p_0\) 后，合法蓝根恰是 \(p_0,v_5,u_6,u_1\)，上述移动按该序循环。删 \(p_0\) 给原型。删 \(v_5\) 后次序为 \(p_0<V_4<U_6\)，块内仍是 \(V\) 蓝、\(U\) 红，混色为
\[
p_0VV=B,\quad p_0UU=B,\quad p_0VU=R,\quad VVU=R,\quad VUU=B .
\tag{13}
\]
唯一红六仍为 \(U_6\)，中性域无红五。删 \(u_6\) 后，反序 \(V_5\) 加 \(p_0\) 构成红六块，其后是反序 \(U_5\) 蓝块，仍为原正 join 型。删 \(u_1\) 是第二型重标。穷尽性可用不平衡 packet 的少数号点验证。\((p_0,\text{三个 }U)\) 排除 \(u_2,\ldots,u_5\)，\((p_0,\text{一个 }U,\text{两个 }V)\) 排除 \(v_1,\ldots,v_4\)。其余四点由实际合法移动兑现。四个实际蓝根 chart 都有 \(w=0\)。

这个反例否定脱离 \(n=3b\) 共同饱和条件的普遍“合法换根必迫 \(w>0\)”。适用范围是上述归一化蓝根 chart。

## 8. 人口账与仍待兑现的兼容性

当前无条件人口工作链为
\[
N_{\rm sig}(7,5,7)\le a+b-1,\quad
N_{\rm sig}(7,6,6)\le2b,\quad
N_{\rm sig}(7,6,7)\le3b,\quad
N_{\rm sig}(7,7,7)=N_{\rm sig}(7,6,7)+1\le3b+1.
\tag{14}
\]
采用历史 \(a=16,b=25\)，为 **40、50、75、76**。新子类结论是 \(I=\varnothing\) 且 \(D\) 有红五时 \(n\le3b-1\)，代入为 **74**。复制上限 \(2b+20=70\) 只约束这一扩张机制，未排除满 766。全局 **74、75** 尚未取得。既有正 through 界沿用，不计为本轮新增。\(b=25\) 保持历史人工接受及 same-family/provisional 保证。[既有人口界](N7_LOCK_REPLACEMENT_COMMON_ROOT_EXCLUSION_AND_7576_BOUND_20261103.md) · [历史输入](../../../../RESEARCH_SYNTHESIS_N7_20261103.md)

**策略审计。** 当前有陷入局部最优的实质趋势。反复把 \(t=1\) 的精确覆盖、单例纤维和中性核搬到 \(t=0\)，只能得到同一类型的必要条件。共根的额外一单位、严格交错保留在 \(K\) 内的 owner，以及外核里原有的邻点，都未兑现新人口增量。推进应针对这些实际缺口。

1. 先研究同一母体内 \(S,D,T\) 各 \(b\) 点时 \(S\sqcup D\) 与 \(D\sqcup T\) 的共同饱和。把 (4) 的四类私有供应接到同一对实际端点，目标是排除完整三满核。
2. 严格交错须联合处理 \(K\) 内保留的 owner，以及 (10) 的两类实际蓝五首点。新添低锁后的外域已迫蓝五，下一步需要真正的覆盖修复或兼容矛盾。
3. 严格分离须补足共享根两帽与同端红五所差的一个实际顶点。

研究清单同时保留共根覆盖预算和 \(I\ne\varnothing\) 的单侧空根族。757 并行研究命中所有联合新蓝四的双点交换，766 并行研究同一满母体的两色全端点图兼容。暂停无条件源侧无红五、单纯合法换根强迫正 through 和独立混合相邻复制的数值传播。以上是待验证的研究方向。

新增数学为 **unreviewed / unaccepted**。本轮未进行独立数学复审、外部 Claude 调用、科研运行、枚举、求解或证书重放。[文档核验回执](N7_T0_CRITICAL_DOCUMENT_RECEIPT_20261103.md)
