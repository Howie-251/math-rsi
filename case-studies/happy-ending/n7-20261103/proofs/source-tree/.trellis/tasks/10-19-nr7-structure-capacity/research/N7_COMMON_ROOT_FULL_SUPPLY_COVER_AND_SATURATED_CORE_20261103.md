# N7 共根层的全供给覆盖与饱和中性核

2026-11-03 · **同会话工作证明，unreviewed / unaccepted**。数学由主会话及同会话协作者推导并交叉核对，指定文档执行者负责转写与文档检查。

**定理 A。** 在上一稿尚余的 \(n=3b+1\) 共根临界接口中，每个非空左、右 owner 纤维恰有一位 owner。因此含多 owner 纤维的整类配置排除。

**定理 B。** 同一接口中存在实际 \(b\) 点中性核 \(K\subseteq D\)。它没有实际红五，是换色 756。对每个 \(x\in X\setminus K\)，\(K\cup\{x\}\) 是实际 766，且包含一条使用 \(x\) 的实际红五。所有外点共用这个 \(K\)。

**定理 C。** 同一中性核支持饱和左、右 owner 的实际红五匹配。它们与外供给匹配合成严格次序的锁到根注入，排除整个锁集中位置反向或违反次序匹配预算的配置。

**定理 D。** 在同一共根临界接口，若 \(f_{\rm full}\) 是缺额零的侧数，则 \(q\ge f_{\rm full}\)。因此 \(q=0\) 且至少一侧满，以及双满且 \(q=1\) 的两类配置均排除。

## 1. 共根余类与全部外供给

沿用完整有序 rank-3 signotope 模型。767 母体 \(X\) 禁 \(R_7,B_6,\mathrm{weak7}\)，766 禁 \(R_6,B_6,\mathrm{weak7}\)，756 禁 \(R_6,B_5,\mathrm{weak7}\)，换色 756 禁 \(R_5,B_6,\mathrm{weak7}\)。weak7 只要求同一对实际首末点的异色路径长度和至少 \(9\)。内部点可以共享。\(b\) 是 756 和换色 756 的共同有效整数人口上界。[模型、参数无关 M0 与容量输入](N7_7677_PROOF_OBLIGATION_AUDIT_20261103.md)

令 \(S,T\) 为 ambient 红六首、末点集，\(I=S\cap T,\ P=S\setminus T,\ Q=T\setminus S,\ D=X\setminus(S\cup T)\)，且 \(|D|=b+q\)。在 \(D\) 内记 \(U=\operatorname{Src}_{R_5}(D),\ V=\operatorname{End}_{R_5}(D)\)，\(w=|U\cap V|\)。取完整双向 M0 核 \(H_L,H_R\)，人口分别为 \(2b-\alpha,2b-\beta\)。左 owner \(A_H=H_L\cap S\subseteq P\)，右 owner \(B_H=H_R\cap T\subseteq Q\)。设 \(a=|A_H|,\ d=|B_H|\)，左锁集 \(\Omega\subseteq T\setminus H_L\)，右锁集 \(\Psi\subseteq S\setminus H_R\)，并记
\[
o=|\Omega|,\quad p=|\Psi|,\quad u=a-o,\quad v=d-p,\quad
\delta=|\Omega\cap I|,\quad \varepsilon=|\Psi\cap I|,\quad
\Gamma=(\Omega\cup\Psi)\cap I .
\tag{1}
\]
每位 owner 唯一锁定相应红六另一端和蓝五相邻点，每个锁有实际供给，故 \(u,v\ge0\)。已有 \(A_H\cap\Psi=B_H\cap\Omega=\varnothing\)，以及 \(D_{\rm all}=H_L\cap H_R=D\sqcup A_H\sqcup B_H\)。

本稿假设 \(n=3b+1\) 的候选尚存。由上一稿 §3，\(w=0\)，内在实际根满足 \(\min E_*=\max F_*=z\in I\setminus\Gamma\)。其中 \(E_*\) 收集根在 \(I\)、前驱在 \(S\cup T\) 的所有实际红六末对之末根，\(F_*\) 反向收集首对之首根，要求后继在 \(S\cup T\)。有
\[
\Omega\cap I\subseteq(z,\infty),\qquad
\Psi\cap I\subseteq(-\infty,z),\qquad
\mu=\min(q+a+d,0)=0 .
\tag{2}
\]
故 \(\Omega\cap\Psi=\varnothing\)，且记 \(m=q+a+d\ge0\) 后，\(D_{\rm all}\) 有 \(b+m\) 点并为实际 766。[上轮共根与内在极值](N7_WEIGHTED_BILATERAL_COMPENSATION_AND_ENLARGED_ROOTS_20261103.md)

记 \(C=\operatorname{End}_{R_5}(H_L),\ C'=\operatorname{Src}_{R_5}(H_R)\)，\(Z_+=C\cap D,\ Z_-=C'\cap D,\ c_\pm=|Z_\pm|\)。以 \(Q_H=Q\cap H_L,\ P_H=P\cap H_R\)，基础实际 756 核为
\[
K_+=Z_+\sqcup Q_H\sqcup A_H,\qquad
K_-=Z_-\sqcup P_H\sqcup B_H,\qquad
\kappa_+=q+\alpha-c_+,\quad \kappa_-=q+\beta-c_-.
\tag{3}
\]
每个 \(K_+\) 点启动的 ambient 蓝五，其第二点若存在则在 \(\Omega\)。反序，终于 \(K_-\) 中的蓝五需要倒数第二点在 \(\Psi\)。这些端口性质沿用上轮证明。[基础核与实际端口](N7_WEIGHTED_BILATERAL_COMPENSATION_AND_ENLARGED_ROOTS_20261103.md)

取
\[
B=(I\cap(-\infty,z))\setminus\Psi,\qquad
A=(I\cap(z,\infty))\setminus\Omega .
\tag{4}
\]
由 (2)，这等同于在两边各删 \(\Gamma\)。左实际域 \(K_-\sqcup B\) 无 \(B_5\)，因为 \(\Psi\) 缺席且 \(B\subseteq S\) 无 ambient 入蓝五。右域 \(K_+\sqcup A\) 反序无 \(B_5\)。每条左域红六只能终于 \(B\)，因为 \(K_-\) 里的 \(D,P\) 点不是 ambient 终点，\(B_H\) 末点需要缺席的 \(\Psi\) 源。其末前驱若在 \(S\cup T\)，则使 \(E_*\) 含有早于 \(z\) 的根。因此全部左末前驱在 \(Z_-\)。右域反序，全部实际红六从 \(A\) 启动，第二点都在 \(Z_+\)。

令 \(L\subseteq Z_-\) 收集左域所有实际红六末对的前驱，\(R\subseteq Z_+\) 收集右域所有实际红六首对的后继。顺序给 \(L<z<R\)。两套供给由全体实际路径定义。写
\[
\ell_0=|B|-\kappa_-,\qquad r_0=|A|-\kappa_+.
\tag{5}
\]
左域所有末对的二部图有至少 \(\ell_0\) 条边的匹配。若 \(\ell_0>0\) 且匹配不足，König 定理给少于 \(\ell_0\) 个角色顶点的覆盖。删除对应实际点后，余域超过 \(b\)，所有红六被击中，且蓝五与 weak7 禁形继承，违反 756 容量。右域同理。故 \(|L|\ge\ell_0,\ |R|\ge r_0\)，负的下界也成立。

**禁止任何实际红五从 \(L\) 到 \(R\)。** 若 \(R_5(j\to k)\) 的首末点分别在 \(L,R\)，取兑现这两个端口的实际外对 \((j,r),(s,k)\)。严格切分给 \(j<r<z<s<k\)。红六末帽给 \(\chi(j,r,s)=B\)，红六首帽给 \(\chi(r,s,k)=B\)，于是 \(B_4(j,r,s,k)\) 与红五同端，违反 weak7。外对见证与中间红五无需内部不交。

## 2. 定理 A：角色覆盖实际化迫单例纤维

在 \(D_{\rm all}\) 内，全部实际红五的源与末点分别在以下容器中：
\[
U_c=Z_-\sqcup A_H\sqcup(C'\cap B_H),\qquad
V_c=Z_+\sqcup B_H\sqcup(C\cap A_H).
\tag{6}
\]
每个左纤维最早 owner 不在 \(C\)，每个右纤维最晚 owner 不在 \(C'\)，因此 \(|C\cap A_H|\le u,\ |C'\cap B_H|\le v\)。记 \(U_0=c_-+a+v,\ V_0=c_++d+u\)。两容器的大小分别至多 \(U_0,V_0\)。这里容器可含没有对应实际中间路径的点，仍包含全部实际中间端点。

人口式 \(i=|I|=q+1+\alpha+\beta+u+v+\delta+\varepsilon\) 与 (2)、(4) 给
\[
\begin{aligned}
|A|+|B|&=i-\delta-\varepsilon-1=q+\alpha+\beta+u+v,\\
\ell_0+r_0&=c_-+c_+-q+u+v=U_0+V_0-m .
\end{aligned}
\tag{7}
\]
定义角色覆盖 \(\mathcal C_{\rm roles}=(U_c\setminus L)\sqcup(V_c\setminus R)\)，其中源、末是两个角色副本。记 \(\mathcal C_{\rm phys}\) 为这些角色的实际点像。因为没有实际红五从 \(L\) 到 \(R\)，每条 \(D_{\rm all}\) 中的实际红五至少命中覆盖的一端。若删除少于 \(m\) 个实际点，余域超过 \(b\) 且无红五，继承无蓝六和 weak7，违反换色 756 容量。由此
\[
m\le|\mathcal C_{\rm phys}|
 \le|\mathcal C_{\rm roles}|
 =|U_c|+|V_c|-|L|-|R|
 \le U_0+V_0-\ell_0-r_0=m .
\tag{8}
\]
所有不等式取等。各容器的大小缺额与各供给大小的超额都非负，因此 \(|U_c|=U_0,\ |V_c|=V_0,\ |L|=\ell_0,\ |R|=r_0\)。特别 \(\ell_0,r_0\) 非负，各侧的最大外匹配都饱和所有相应实际供给端口。覆盖中任何两个角色副本的实际点也必不相同。

全部 \(A_H\) 已在源覆盖中，全部 \(B_H\) 已在末覆盖中，因为 \(L,R\subseteq D\)。若某点在 \(C\cap A_H\)，它还在末覆盖中，违反实际点像的单射性。若某点在 \(C'\cap B_H\)，则还在源覆盖中，同样矛盾。故
\[
C\cap A_H=C'\cap B_H=\varnothing,\qquad
u=v=0,\qquad a=o,\quad d=p .
\tag{9}
\]
后两组等式由容器大小取等得到。每个锁至少有一位 owner，于是每个非空纤维恰有一位 owner。这个结论排除了任何一侧存在多 owner 纤维的整类候选。

## 3. 定理 B：同一中性核给全部外点红五

由 (8)–(9)，实际删点集 \(\mathcal C_{\rm phys}\) 含全部 \(a+d\) 个 owner，其余 \(m-a-d=q\) 点在 \(D\)。因此 \(q\ge0\)。删后集合 \(K=D_{\rm all}\setminus\mathcal C_{\rm phys}\) 在 \(D\) 内，有 \(b\) 个点，无红五，是实际换色 756。

进一步，\(U\subseteq Z_-,\ V\subseteq Z_+\)，且 \(w=0\) 给 \(U\cap V=\varnothing\)。集合 \(C_D=(U\setminus L)\cup(V\setminus R)\) 覆盖 \(D\) 内全部实际红五，因为余下首末角色若都不被覆盖，就有实际红五从 \(L\) 到 \(R\)。\(C_D\subseteq D\cap\mathcal C_{\rm phys}\)。若 \(|C_D|<q\)，从 \(D\) 删除它将得到超过 \(b\) 点的换色 756，矛盾。因此 \(C_D=D\cap\mathcal C_{\rm phys}\)，而且
\[
\begin{gathered}
K=D\setminus C_D,\qquad |C_D|=q,\qquad |K|=b,\\
Z_-\setminus L=U\setminus L,\qquad Z_+\setminus R=V\setminus R,\\
Z_-\setminus U\subseteq L,\qquad Z_+\setminus V\subseteq R .
\end{gathered}
\tag{10}
\]
中行由各项包含、覆盖的实际像单射及两个并集相等得到。底行是其直接推论。

对任意 \(x\in X\setminus K\)，\(K\cup\{x\}\) 不含实际红六。任何红六的首、末点都不能在 \(K\subseteq D\)，而首末均为 \(x\) 又违严格点序。蓝六和 weak7 禁形继承，故为实际 766。若它还无红五，则这 \(b+1\) 点违反换色 756 容量。因此存在一条实际红五，且必用 \(x\)，因为 \(K\) 本身无红五。其余四点都在同一 \(K\)。特别 \(K\cup\{z\}\) 有一条实际红五经过 \(z\)。

这一逐点供应结论未指定 \(x\) 在红五中的位置，也未指定能与 \(L,R\) 外供给同接的首末点。

## 4. 定理 C：owner 的实际匹配及全锁序排除

**定理 C。** 每个左 owner 可沿 \(K\cup A_H\) 的一条实际红五匹配接到右供给，每个右 owner 可沿 \(K\cup B_H\) 的一条实际红五匹配接到左供给。由此有两份注入
\[
\Omega\longrightarrow A,\quad \omega\longmapsto s_\omega,\quad
z<s_\omega<\omega,\qquad
\Psi\longrightarrow B,\quad \psi\longmapsto r_\psi,\quad
\psi<r_\psi<z .
\tag{11}
\]
这排除任一锁位置或任一严格次序匹配条件不满足的整个配置类。

\(K\sqcup A_H\subseteq D_{\rm all}\) 是实际 766，人口为 \(b+a\)。其实际红五不能终于 \(A_H\)，因为该路径位于 \(H_L\) 而 \(C\cap A_H=\varnothing\)。若首末都在 \(K\)，该红五位于 \(D_{\rm all}\)，首、末角色分别在 \(U_c,V_c\)。首末实际点都未被 \(\mathcal C_{\rm phys}\) 删除，故首点在 \(L\)，末点在 \(R\)，违反 §1 的同端 weak7 禁形。于是 \(K\sqcup A_H\) 内所有实际红五都从 \(A_H\) 启动，并终于 \(K\cap R\)。对全部此类实际红五建首末点二部图。若最大匹配少于 \(a\)，König 定理给少于 \(a\) 个角色的顶点覆盖。删去其实际点后，余域超过 \(b\) 点且无红五，继承其他禁形，违反换色 756 容量。因此可取饱和 \(A_H\) 的 \(a\) 条实际红五端点匹配。反序在 \(K\sqcup B_H\) 中取饱和 \(B_H\) 的 \(d\) 条实际红五端点匹配。
\[
A_H\longrightarrow K\cap R,\qquad K\cap L\longrightarrow B_H .
\tag{12}
\]

对任一左 owner \(a_0\) 及其锁 \(\omega(a_0)\)，取 ambient 入红五 \((p_1,p_2,p_3,p_4,a_0)\) 及以 \((a_0,\omega(a_0))\) 开始的出蓝五。若 \(\chi(p_4,a_0,\omega(a_0))=B\)，可将 \(p_4\) 前接到出蓝五得到 \(B_6\)。故该桥为红，得到一条实际红六，其末对恰为 \((a_0,\omega(a_0))\)。反序，每个右 owner \(b_0\) 与其锁 \(\psi(b_0)\) 兑现实际红六首对 \((\psi(b_0),b_0)\)。

沿 (12) 取匹配给出的实际红五 \(R_5(a_0\to k)\)，其中 \(k\in K\cap R\)。§2 的取等保证右外最大匹配饱和 \(R\)，故 \(k\) 有匹配首对 \((s,k)\)，其中 \(s\in A\)。若 \(\omega(a_0)<s\)，由两个实际帽得到 \(B_4(a_0,\omega(a_0),s,k)\)，与该红五同端，违反 weak7。又 \(A\) 避开 \(\Omega\)，故 \(s\ne\omega(a_0)\)，从而 \(z<s<\omega(a_0)\)。两次匹配的端点无重复，故不同左 owner 得到不同右根。单例纤维使左 owner 与左锁一一对应，兑现 (11) 的左侧注入。右侧用 \(K\cap L\) 到 \(B_H\) 的匹配及饱和 \(L\) 的左外匹配反序兑现。

尤其整个锁集满足
\[
\Omega\subseteq(z,\infty),\qquad \Psi\subseteq(-\infty,z).
\tag{13}
\]
这项结论涵盖 \(I\) 外的锁。对任意 \(c>z\)，所有位于 \((z,c]\) 的左锁必须有不同的右根严格早于 \(c\)。对任意 \(c<z\)，所有位于 \([c,z)\) 的右锁必须有不同的左根严格晚于 \(c\)。即
\[
\begin{aligned}
|\Omega\cap(z,c]|&\le |A\cap(z,c)| && (c>z),\\
|\Psi\cap[c,z)|&\le |B\cap(c,z)| && (c<z).
\end{aligned}
\tag{14}
\]
任一反向位置的锁或任一违反 (14) 的端口人口都给出实际矛盾。符合严格锁根次序的单例 owner 仍可能出现在待排除的接口中。

还有一个针对实际根见证的后果。给定任一实际 owner 红五 \(R_5(a_0\to k)\) 和任一实际右供给首对 \((s,k)\)，若 \((a_0,r)\) 是实际红六末对，则 \(r\ge s>z\)，否则两帽给出同端蓝四。这里允许 \(r=s\)，只有 \(r=\omega(a_0)\) 时才由 \(s\in A\) 的避锁条件得到严格不等式。因此左 owner 不能作共根或更低末根的前驱，反向右 owner 不能作共根或更高首根的后继。

## 5. 定理 D：满侧与旧根的容量预算

令 \(f_{\rm full}=\mathbf1[\alpha=0]+\mathbf1[\beta=0]\)。下文的满侧是缺额零的实际 fullstandard 侧。缺额零给无锁、无 owner 的补核，反向不能仅凭无 owner 推出缺额零。

由定理 A，\(u=v=0\)。旧基底 \(W=S\setminus\Omega,\ W'=T\setminus\Psi\) 无蓝五，人口分别为 \(b+1+\alpha,b+1+\beta\)。收集所有实际红六末对两点均在 \(W\) 的根为 \(\widehat E\)，反向取首对两点均在 \(W'\) 的根为 \(\widehat F\)。删去 \(\widehat E\) 击中 \(W\) 内全部实际红六，删去 \(\widehat F\) 击中 \(W'\) 内全部实际红六。余域无红六与蓝五，故由 756 容量得
\[
e=|\widehat E|\ge1+\alpha,\qquad f=|\widehat F|\ge1+\beta .
\tag{15}
\]
旧根都在 \(I\)，且 \(\widehat E\) 各根不早于 \(z\)，\(\widehat F\) 各根不晚于 \(z\)。按定义 \(\widehat E\) 避开 \(\Omega\)，\(\widehat F\) 避开 \(\Psi\)。再用 \(\Psi\cap I\subseteq(-\infty,z)\)、\(\Omega\cap I\subseteq(z,\infty)\)，得两根族均在 \(I\setminus\Gamma\)。由 (7) 及 \(u=v=0\)，
\[
N=|I\setminus\Gamma|=q+1+\alpha+\beta.
\tag{16}
\]

**右满侧不使用共根 \(z\) 作为旧首根。** 若 \(\beta=0\)，实际满核 \(H_R=X\setminus T=P\sqcup D\) 有 \(2b\) 点且无 ambient 红六末点。令 \(Z'=\operatorname{Src}_{R_5}(H_R)\)。删去 \(Z'\) 后无实际红五，换色 756 容量给 \(|Z'|\ge b\)。若一条 ambient 蓝五终于 \(Z'\) 中的一点，接该点的核内出红五，蓝桥给 \(B_6\)，红桥给终于 \(H_R\) 的实际红六，皆矛盾。因此 \(Z'\) 各点无 ambient 蓝五末点身份，\(Z'\subseteq H_R\) 是实际 756，故 \(|Z'|\le b\)。另一方面，\(H_R\) 内蓝五末点集至少有 \(b\) 点，因为删去它后余域为实际 756。它与 \(Z'\) 不交，故两集分划 \(H_R\)。

\(P\) 的点无 ambient 蓝五末点，所以 \(P\subseteq Z'\)。由 \(D\subseteq H_R\) 又有 \(U\subseteq Z'\)。删去 \(U\) 后 \(D\) 无红五，故 \(|U|\ge|D|-b=q\)。满核给 \(|P|=b-q\)，两者不交，且 \(|Z'|=b\)，故 \(Z'=P\sqcup U\)。

若 \(z\in\widehat F\)，取其一条实际红六首对 \((z,t_0)\)，其中 \(t_0\in W'\subseteq T\)。\(t_0\) 有 ambient 出红五，且右满侧无 owner，强普通点性质给 \(t_0\) 无 ambient 入蓝五。于是 \(Z'\sqcup\{t_0\}\) 无蓝五且有 \(b+1\) 点，容量迫实际红六
\[
(p_0,z_1,z_2,z_3,z_4,t_0).
\]
它只能终于 \(t_0\)，因为前五点全在 \(H_R=X\setminus T\)。它的首点在 \(S\cap Z'=P\)。若 \(p_0<z\)，实际首帽给 \(B_3(p_0,z,t_0)\)，与该红六同端违反 weak7。\(p_0\ne z\) 因为 \(p_0\in P,\ z\in I\)，故 \(z<p_0\)。增强末根 \(z\) 的右扇覆盖 \(S\cup U\)，而 \(z_1\in Z'\subseteq S\cup U\)，故 \(\chi(z,p_0,z_1)=R\)。将 \(z\) 前接到前五点得到实际红六 \((z,p_0,z_1,z_2,z_3,z_4)\)，终于 \(H_R\)，矛盾。此处只需 \(z\) 是增强末根。于是右满给 \(z\notin\widehat F\)，反序左满给 \(z\notin\widehat E\)。

两旧根族至多共用 \(z\)。零满侧时可用 \(N+1\) 作为根数和上界。一满侧时两族不交，上界为 \(N\)。双满侧时两族不交且都不用 \(z\in I\setminus\Gamma\)，上界为 \(N-1\)。统一结合 (15)–(16) 得
\[
N+1-q=2+\alpha+\beta\le e+f\le N+1-f_{\rm full},
\qquad q\ge f_{\rm full}.
\tag{17}
\]
因此 \(q=0\) 且至少一侧满、以及双满且 \(q=1\) 的整个配置类排除。双满且 \(q\ge2\)、双正缺额且 \(q=0\) 未由此排除。

## 6. 共根插点的相邻点限制

取任意实际入根红六 \((p_1,p_2,p_3,p_4,j,z)\) 和任意实际出根红六首对 \((z,t_0)\)。若 \(K\cup\{z\}\) 中某条实际红五以 \(a_0<z<b_0\) 为 \(z\) 的相邻两点，则
\[
a_0<j<z<t_0<b_0 .
\tag{18}
\]
证明左侧。若 \(a_0=j\)，末帽直接与红三 \((a_0,z,b_0)\) 冲突。若 \(j<a_0\)，四点 packet \((j,a_0,z,b_0)\) 的后两项 \(\chi(j,z,b_0)=B,\ \chi(a_0,z,b_0)=R\) 迫第一项 \(\chi(j,a_0,z)=B\)。再看 \((p_4,j,a_0,z)\) 的 packet，第二项 \(\chi(p_4,j,z)=R\)，末项 \(\chi(j,a_0,z)=B\)，故首项 \(\chi(p_4,j,a_0)=R\)。于是 \((p_1,p_2,p_3,p_4,j,a_0)\) 为实际红六，推出 \(a_0\in T\)，违反 \(a_0\in K\subseteq D\)。右侧反序，若 \(b_0=t_0\) 与首帽冲突，若 \(b_0<t_0\) 则推出 \(b_0\in S\)，同样矛盾。

此限制适用于全部实际根见证。若 \(z\) 是该红五的端点，就没有上述双邻点假设。即使 \(z\) 是红五 \((h,a_0,z,b_0,k)\) 的中央点，(18) 也只给顺序。以 \(j\) 替换 \(z\) 需要边界三元组 \(\chi(h,a_0,j)\) 为红，以 \(t_0\) 替换需要 \(\chi(t_0,b_0,k)\) 为红，两项均未由 (18) 保证。故这一引理只兑现插点限制。

## 7. 11 点策略反例与仍需兑现的供给

取 \(L_5<z<R_5\)，左右各五个实际点。本节的 \(L_5,R_5\) 表示点块。三元组若全在 \(L_5\cup\{z\}\) 或 \(\{z\}\cup R_5\) 内则为红，其余为蓝。单侧四点 packet 全红。跨左右四点的其余 packet 为 RBBB、BBBB 或 BBBR。故这是完整 signotope。

最长红路径有六点，因为含至少三点且跨严格左右块的路径不能为红，而两个含 \(z\) 的六点块分别全红。蓝路径至多四点，因每个严格侧至多取两点，若用 \(z\) 则每个严格侧至多取一点。若同端红路径长度至少三，其实际首末点在同一个含 \(z\) 的全红块中，故同端蓝路径至多两点，长度和至多八。若首末点严格分在左右，红长至多二，蓝长至多四。其余同端路径若红长至多二，长度和也至多六。因此 weak7 被排除。

该母体的全部实际红六是两个含 \(z\) 的六点块，故
\[
S=\{\min L_5,z\},\qquad T=\{z,\max R_5\},\qquad I=\{z\},\qquad
D=K=(L_5\setminus\{\min L_5\})\cup(R_5\setminus\{\max R_5\}).
\tag{19}
\]
\(K\) 有八点且无红五。对每个外点 \(x\in\{\min L_5,z,\max R_5\}\)，\(K\cup\{x\}\) 都有实际红五。特别 \(K\cup\{z\}\) 有终于 \(z\) 及从 \(z\) 启动的红五，但没有从严格左块到严格右块的红五。唯一以 \(z\) 为末根的红六，其前驱是 \(\max L_5\notin S\cup T\)。唯一以 \(z\) 为首根的红六，其后继是 \(\min R_5\notin S\cup T\)。故 \(E_*=F_*=\varnothing\)。

此例反驳仅用中性、逐点红五饱和与 \(z\in I\) 就推出跨侧兼容性的引理。它缺少临界人口、有效共根和现行全局 \(b=25\) 的容量饱和。证明下一人口单位仍需把 \(K\cup\{z\}\) 兑现的新红五与全外供给相容，或直接排除临界母体的内在共根。一般的匹配交换或把经 \(z\) 的两条红五直接拼接，都不能兑现这一步。

本轮排除多 owner 纤维，以及锁位置反向或违反严格次序匹配预算的配置，并由旧根预算排除相应小 (q) 满侧类。得到同一个实际 \(b\) 点中性核的逐点供应及 owner 匹配接口。符合新锁序的单例 owner 和无 owner 的共根临界类仍待排除，因此 757、766、767、777 的人口工作上界仍为 **40、50、76、77**，全局 75、76 尚未得到。新增数学保持 **unreviewed / unaccepted**。
