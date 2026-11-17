# N7 的 767 与 777 人口工作上界证明义务审计

2026-11-03 · `N7-7677-OBL-20261103` · **同会话核对，新增工作证明 unreviewed / unaccepted**

本次核对完整低前驱补偿及其承重依赖。在下列逐项义务中未发现实质缺口、语义循环或未关闭的 FATAL / CRITICAL 项。\(76,77\) 仍为采用 \(b=25\) 的人口工作上界，独立数学复审待办。本文补写三处 `ADD_DERIVATION`，其中参数无关的 M0 证明解释了早期缺额至多 \(2\) 的论证如何用于缺额 \(3\)。执行者依主会话定稿转写并核对文档。[统一补偿原稿](N7_COMPLETE_LOW_PREDECESSOR_COMPENSATION_AND_UPPER_BOUND_20261103.md) · [人口界更新](../../../../RESEARCH_SYNTHESIS_N7_20261103_UPPER_BOUND_UPDATE.md)

## 1. 输入、量词与依赖

令 \(X\) 为任意有限完整有序 rank-3 signotope，四点 packet 的三元组按字典序排列至多换色一次。\(R_k,B_k\) 是由连续三元组定色的实际 \(k\) 点路径。weak7 禁止同一对实际端点之间两条异色路径长度和至少为 \(9\)，内部允许共享。767 禁 \(R_7,B_6,\mathrm{weak7}\)，766 禁 \(R_6,B_6,\mathrm{weak7}\)，756 禁 \(R_6,B_5,\mathrm{weak7}\)，换色 756 禁 \(R_5,B_6,\mathrm{weak7}\)。

\(b\) 是 756 与换色 756 共用的有效整数人口上界。若输入为实数上界，可先向下取整。核心排除的量词为，对每个满足 \(n=3b+2,\ w=0\) 的 767 母体及任一兑现完整双向 M0 接口的核对，严格交错 \(x<y\) 导致矛盾。\(w\) 只在实际 \(D\) 中取红五首末交集数。\(S,T\) 为 ambient 红六源、末点，\(I=S\cap T,\ P=S\setminus T,\ Q=T\setminus S,\ D=X\setminus(S\cup T)\)。这里 \(Q\) 是点集，\(Q_{\rm cap}=N_{\rm sig}(7,6,7)\) 才是人口极值，\(F_{\rm cap}=N_{\rm sig}(7,7,7)\) 是另一人口极值。

主会话只读核对了 Bergold、Felsner、Scheucher 的 SoCG 2023 论文 *An Extension Theorem for Signotopes*。§1.1，p. 17:3 给出 rank-3 点对方向，红对应正号时为 \(ab<ac<bc\)，蓝反向。§2，p. 17:5 陈述该关系的传递闭包为偏序，并引用 Felsner–Weil Lemma 10。论文的删除次序与本项目 packet 字典序互为反向，至多一次换色在反向下保持。故可在整个 \(X\) 的点对上取同一个线性扩张，满足 R7 的最小关联对论证所需的偏序假设。该外部定理提供组合点对偏序。[公开论文 PDF](https://drops.dagstuhl.de/storage/00lipics/lipics-vol258-socg2023/LIPIcs.SoCG.2023.17/LIPIcs.SoCG.2023.17.pdf)

数值替换 \(b=25\) 沿用 C8 人工接受的容量输入及其原 same-family/provisional 保证。采用容量上界只需要禁止超过 \(25\) 的人口。既有 25 点存在性回执是另一条证据。历史容量证书及存在性回执均未重放。早期综述中的 \(a=16\) 属于另一容量线，此处 \(a\) 是左 owner 数。[早期综述的容量来源](../../../../RESEARCH_SYNTHESIS_N7_20261103.md)

依赖箭头按前提到结论排列。段落列出各边实际传递的结论。

1. **完整 packet、点对偏序与 756 容量 → 原 canonical 分解。** R7 §2 用最小关联对得到不要求同域的 fan，§3.1 的三链桥接约束所有实际终点与第二点，§3.2 从 \(P_-\cup G\) 和 \(P_+\setminus G\) 得实际 766 核与残余。§3.3 给 \(D_7\) 的红六横截至多 \(5\)，删后为 756，所以容量至多 \(b+5\)。[R7](RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md)
2. **原 canonical 核 → ambient 两端封闭 → 任意缺额联合预算。** R20 §5.2 排除两个实际端点同在原核 \(H_0\) 的 ambient 红六。10-29 稿 §2，式 (5)–(8) 以实际扩核、删像核和共同注入同时收费，给 \(j+|M|+g\le d_0\)，这里 \(d_0=2b-|H_0|\)。这两步分别供给“原核源的终点尽在域外”和参数无关的预算。[R20](RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md) · [任意缺额预算](N7_TIGHT_CUT_JOINT_NEUTRAL_AND_REPARTITION_DICHOTOMY_20261029.md)
3. **联合预算 → 真实 through 增广 → 两次换核。** 10-30 稿 §3.1–3.3 对实际 \((R_0\setminus(J\cup M_R))\sqcup C_0\) 证明 \(D_7\)，由容量给 \(n+w\le3b+5-\eta_*\)。10-31 稿 §3.1–3.2 给实际 promotion。11-02 锁纤维稿 §2 给残余 mixed 源换入、锁像换出。下节分离这两次实际换核与任何临界层数值上限。[实际 through 联合预算](N7_JOINT_THROUGH_SATURATION_AND_ORDERED_CUTS_20261030.md) · [promotion](N7_7879_INTERFACE_AUDIT_AND_WEIGHTED_THROUGH_STABILITY_20261031.md) · [消去 mixed](N7_LOCK_FIBER_NORMALIZATION_AND_DOUBLE_OMEGA_EXCLUSION_20261102.md)
4. **M0 → 完整端口、双向根扇、头尾替换、纤维界 → 加权界与临界分类。** 锁纤维稿 §3 的加强根扇使用完整端口，§5.1–5.2 给交叉锁排除和纤维代表界。10-31 稿 §7 的旧加权界 \(n+w\le3b+3\) 限定下一加权取等层。共同中间稿 §1–4 再得到 \(n+w\le3b+2\)，其 §2 同时给非交错排除。跨角色稿 §5 给满侧纯前供。统一补偿稿再处理下一人口临界层的严格交错。双 clean 增广稿和有锁分阶段稿在统一稿中是历史交叉证据。综述记录前述结果及输入出处，证明箭头不经过综述中的人口结论。[锁纤维与根工具](N7_LOCK_FIBER_NORMALIZATION_AND_DOUBLE_OMEGA_EXCLUSION_20261102.md) · [共同中间与加权界](N7_COMMON_MIDDLE_COMPATIBILITY_AND_WEIGHTED_BOUND_20261103.md) · [跨角色根序与满侧](N7_CROSS_ROLE_ROOT_ORDER_AND_SEPARATED_CLASS_EXCLUSION_20261103.md)
5. **平行支路。** R20 §2 用四点交替延拓给 weak7 的 balanced packet 局部刻画，以 \(\omega\) 保证合法 chart 之间的禁形不变。§3 对原最左 pivot 给径向次序、非 pivot 四点的符号排列及其穷尽条件，实际输出合法 chart 并使 pivot 无蓝三参与。§4 从 777 删 pivot 后换色进入 767，从任意 767 在左加蓝点进入 777，得到 \(F_{\rm cap}=Q_{\rm cap}+1\)。此支路使用完整 packet 模型与局部 chart 论证，独立于 767 的数值上界。最后才和统一补偿的 \(Q_{\rm cap}\le3b+1\) 合流。[R20 的局部刻画、符号表与精确归约](RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md)

## 2. 参数无关的 M0 归一化 · ADD_DERIVATION

**引理。** 对任意上述 767 母体，置 \(U=\operatorname{Src}_{R_5}(D),\ V=\operatorname{End}_{R_5}(D),\ C_0=U\cap V,\ w=|C_0|\)。取 R7 的实际 canonical 分解 \(X=H_0\sqcup R_0\)，其中 \(H_0=P_-\cup G\)，\(G\) 是 R7 的内部入红五、出蓝四交会点。可在同一 \(X\) 上构造左右两个完整 M0 核。每个方向的新核实际为 766，包含 \(D\)，缺额不增于 promotion 后缺额，且锁数至多新缺额。构造使用任意缺额联合预算。

**证明。** 正向定义 \(\Omega\) 为所有从 \(H_0\) 启动的 ambient \(R_6\) 的末点集。R20 的两端封闭给 \(\Omega\subseteq R_0\cap T\)。记 \(J=R_0\setminus(\Omega\cup S)\)，且取完整集合 \(M=R_0\cap S\cap\operatorname{End}_{R_5}(X)\cap\operatorname{Src}_{B_5}(X)\)。三链给每个 \(s\in M\) 一个唯一 \(h(s)\)，使它所有出红六终点及所有出蓝五第二点均为 \(h(s)\)。出蓝五与入红六若在同一点相接，蓝桥给 \(B_6\)，红桥给 \(R_7\)，故 \(M\subseteq P\)，而 \(h(M)\subseteq T\)。

置 \(M_R=\{s\in M:h(s)\in R_0\setminus J\}\)，\(H^*=H_0\cup J\cup M_R\)，\(R^*=X\setminus H^*\)，\(\Omega^*=\Omega\cup h(M_R)\)，\(M^*=M\setminus M_R\)。\(J\) 全为非源，\(M_R\subseteq P\) 与 \(T\) 不交，所选像 \(h(M_R)\) 在 \(R_0\setminus J\)。于是 \(\Omega^*\subseteq R^*\cap T\)。任何从 \(H^*\) 启动的红六若源在 \(H_0\) 则终点在 \(\Omega\)，若源在 \(M_R\) 则在 \(h(M_R)\)。每个像都有实际供应，且所有终点在域外，故 \(H^*\) 无内部 \(R_6\)。它继承 \(B_6\) 与 weak7 的禁形，确为 766。

\(R^*\setminus\Omega^*\subseteq S\)，且 \(D\subseteq H^*\)，因为 \(R_0\cap D\subseteq J\)。原核 \(P_-\) 点作为红六源会由 fan 前接为红七，故原核的源只能来自 \(G\)。\(G\) 中的源有入红五，并有通过 \(P_+\) fan 延长的出蓝五，新增的 \(M_R\) 源也有这两项 ambient 身份。三链适用于这些源，因此 \(H^*\cap S\subseteq P\)，每位 owner 都有唯一锁。\(h(M^*)\subseteq H_0\cup J\subseteq H^*\)，且 \(H^*\cap T\) 不含源，所以 \(\Lambda=h(M^*)\subseteq Q\)。令
\[
\eta_*=2b-|H^*|,\qquad
H_{\rm new}=(H^*\setminus\Lambda)\sqcup M^*,\qquad
\Omega_{\rm new}=\Omega^*\sqcup\Lambda.
\]
旧 owners 保留，仍锁向 \(\Omega^*\)。新 owners \(M^*\) 都锁向 \(\Lambda\)。这些就是新核的全部源，两组锁都有实际供应且在域外。因此新核仍为 766，且新锁集精确等于从新核启动的 ambient 红六末点集。

设 \(d_0=2b-|H_0|\)。任意缺额联合预算给 \( |J|+|M|+|\Omega^*|\le d_0\)，因为 \(h(M)\setminus(H_0\cup J)=h(M_R)\)。故
\[
\eta_*\ge |M^*|+|\Omega^*|,\qquad
\eta_{\rm new}=\eta_*-|M^*|+|\Lambda|\le\eta_*,
\qquad
|\Omega_{\rm new}|\le\eta_{\rm new}.
\]
交换只删 \(Q\) 点、添 \(P\) 点，保留 \(D,C_0\)。所有 ambient 身份继续在同一 \(X\) 计算。每次诱导核的红六禁形都已对全部路径重新兑现。

最后验证普通点性质。若 \(z\in S\setminus\Omega_{\rm new}\) 是非 owner 且有 ambient 入 \(R_5\) 和出 \(B_5\)，它在新核外。新删的 \(\Lambda\subseteq Q\) 不含 \(z\)，所以 \(z\) 本在 \(R_0\)，由完整定义属于 \(M\)。但 \(M_R\) 已 promotion，\(M^*\) 已换入，二者均在新核内，矛盾。于是 \(W=(S\setminus\Omega_{\rm new})\cup C_0\) 的有入红五非 owner 点没有 ambient 出蓝五，\(C_0\subseteq V\) 的点由 joining 同样无出蓝五。owner 的蓝五第二点在缺席的锁集。\(S\cup U\) 无 ambient 蓝五末点，且其中任意蓝四末点可用实际红路径的后继保首对延为蓝五。故 \(W\) 无蓝五，并由完整端口排除内部红五末点兼蓝四源，是实际 \(D_7\)。右侧反序构造保有完整反端口；两次构造各自作用于同一母体的子集，故可同时取用。

以上各步无需 \(\eta_*\le2\) 或 \(w=0\)。加权取等层 \(n+w=3b+3\) 才由实际增广预算得 \(\eta_*\le2\)；下一层 \(n=3b+2\) 先用 \(n+w\le3b+2\) 得 \(w=0\)，再从同一预算得 \(\eta_*\le3\)。若新缺额为零，锁集为空，全部 \(H_{\rm new}\) 源随之为空，而核外去锁后全为 \(S\)，故 \(H_{\rm new}=X\setminus S\) 实现满标准核，右侧同理。[原预算与增广](N7_JOINT_THROUGH_SATURATION_AND_ORDERED_CUTS_20261030.md) · [原 promotion](N7_7879_INTERFACE_AUDIT_AND_WEIGHTED_THROUGH_STABILITY_20261031.md) · [原交换与完整根工具](N7_LOCK_FIBER_NORMALIZATION_AND_DOUBLE_OMEGA_EXCLUSION_20261102.md)

## 3. 统一补偿义务台账

下表式号与节号默认指统一补偿稿。核指实际诱导子域，图中的两端角色各有一个副本。\(q=|D|-b\) 为整数，可负。\(\alpha,\beta\) 为两核缺额，\(a,d\) 为 owner 数，\(o,p\) 为锁数，\(u=a-o,\ v=d-p\) 为纤维余量。\(\tau\) 数的是不同低前驱实际点，\(e_y\) 为根指示量，\(\epsilon_L\) 为匹配删边数。\(B,A\) 分别为切分的低根域和高根域。

| 义务 | 实际域与要兑现的条件 | 同会话核对结果及位置 |
| --- | --- | --- |
| OB-01 packet 遗传 | 路径的连续三元组同色 | 四点首尾三元组同色迫其余两项同色。删除内部点时，新连续三元组是原相邻四点 packet 的同色项；删首尾无需补色。逐点删除给任意子序列。weak7 等禁形随诱导限制继承。见 R7 §1 与原稿 §1。 |
| OB-02 根确实存在 | \(W,W'\) 是实际 \(D_7\)，临界 \(t=n+w-3b=2\) | \(w=0\) 使 \(C_0\) 为空；\(\lvert W\rvert-b=t+\alpha+u>0\)，反向同样。无 \(B_5\) 的实际基底若无 \(R_6\) 即为 756，违反容量。内部实际红六的相邻末对、首对兑现 \(\widehat E,\widehat F\) 非空，且两根族都在 \(I\)。见共同中间稿 §1 与原稿 §1.1。 |
| OB-03 根扇与尾替换 | \(y\) 的实际首对两点在原 \(W'\)，中点可取 ambient 点 | \(R_7\) 禁止延伸，给帽。反色桥经帽成蓝四，再保端对延为蓝五，与完整端口冲突。尾替换的假想 \(B_5(d_0,v_4,v_5,y,t_y)\) 由同一实际首对触发完整反端口；允许 \(t_y\) 是右 owner。见 §1.1，式 (4) 与尾替换段。 |
| OB-04 基础实际核 | \(K_+\subseteq H_L,\ K_-\subseteq H_R\) | \(D,Q,P\) 的普通角色与 owner 互不交。核内入红五与出蓝五在末点接桥时，蓝给 \(B_6\)，红给从该核启动的 \(R_6\) 并将蓝五第二点锁到域外；反向同理。实际无蓝五与红六，故 \(\kappa_+=q+\alpha-c_+\ge0,\ \kappa_-=q+\beta-c_-\ge0\)。见 §1.2，式 (5)–(6)。 |
| OB-05 完整低前驱 | 先固定全部实际末对，两点在 \(S\setminus A_H\)，根 \(r<y\) | 若前驱在 \(T\)，根 \(y\) 的左扇与末帽冲突。因此 \(\mathcal R\subseteq P\setminus A_H\)，在 \(H_L\) 外且在 \(W\) 内。其入红五由实际末对兑现，M0 给无 ambient 出蓝五。低根可在 \(\Omega\)。见 §2 首两段。 |
| OB-06 同时增广 | \(K_+^*=K_+\sqcup\mathcal R\) | 所添点避开 \(\Omega\)，且无出蓝五。潜在红六的源只能是 \(A_H\) 或 \(\mathcal R\)。前者需域外锁，后者用固定低末对的帽及 weak7 把终点压到 \(r_z<y\)，再尾替换到 \(y\) 与同端蓝三冲突。每点都具 ambient 入红五。容量改善恰为实际新点数 \(\tau\)。见 §2，式 (7)。 |
| OB-07 剩余根下界 | \(\widetilde W=S\setminus(A_H\cup\mathcal R)\) 在 \(\mathcal R\) 固定后形成 | 若 \(\widetilde E\) 有 \(r<y\)，其前驱按原定义应在 \(\mathcal R\)。只用全部相邻对定义，无需 \(\widetilde W\) 的 \(D_7\) 身份、\(\widetilde E\) 的 clique 性或非空。见 §2 末段。 |
| OB-08 扩域人口 | \(B\) 加 \(K_-\)，\(A\) 加 \(K_+^*\) | \(A,B\subseteq I\) 与旧核的 \(D/P/Q\) 角色及新增 \(\mathcal R\subseteq P\) 均不交，见下节补写。只须分别避 \(\Psi,\Omega\)；低域可含左锁，新增点的 \(S/T\) 身份禁止相应蓝五端点。人口式 (10) 计晚侧双锁交集一次，并单扣 \(y\) 指示量。见 §3，式 (8)–(10)。 |
| OB-09 全外图定位 | 两扩域内所有实际 \(R_6\) 的末对或首对 | 左侧必终于 \(B\)，普通 \(P_H\) 或 \(B\) 前驱触发 \(\widetilde E\) 时排除，保留 \(Z_-,A_H,\mathcal R,B_H\) 的实际角色。\(B_H\) 前驱只能终于 \(y\)，故 \(\mathcal R\) 删边至多 \(\tau\)，\(e_y+\epsilon_L\le1\)，包括 \(y\in\Omega\) 的情形。右侧源只能在 \(A\)，新增 \(A\) 有 ambient 入红五，尾替换仍适用；第二点在 \(Q_H\cup A\) 触发原 \(\widehat F\)，在 \(A_H\) 违右扇与首帽，在 \(\mathcal R\) 违顺序。故第二点在 \(Z_+\)。见 §3.1–3.2，式 (11)。 |
| OB-10 添右锁边 | 每个 \(\psi>y\) 的不同右纤维取一位代表 | 入蓝五的实际末对 \((\psi,b_\psi)\) 与 owner 的出红五接桥。蓝给 \(B_6\)，红给实际首对为该对的 \(R_6\)。锁根在 \(A\) 外，代表在 \(B_H\)，与 \(Z_+\) 不交；每纤维一条保证匹配。见 §3.2。 |
| OB-11 中间域与纤维界 | 全部 \(D_{\rm all}=H_L\cap H_R\) | 交叉 owner 与锁若重合，双向唯一性使相应蓝五沿同一对合成 \(B_8\)，继承 \(B_6\)。故交集为 \(D\sqcup A_H\sqcup B_H\)。最早左 owner 与最晚右 owner 由红桥违反代表极值、蓝桥违反 \(B_6\)，各排除一个核内端点角色。源容器纳入全部 \(A_H\)，末容器纳入全部 \(B_H\)，包括没有相应中间红五角色的外端口。见 §1.1 式 (2)，§4 式 (12)–(13)。 |
| OB-12 König 实际删点 | 全部相应实际路径形成有限二部图 | 删覆盖的角色副本对应的实际点集合，重合只使实删数减少。剩域中的路径也在原域，故不可能新出现未覆盖路径。外图适用 756，内图适用换色 756。外图若人口减 \(b\) 非正，非负的匹配数已给所需下界。见 §3.1–3.2、§4。 |
| OB-13 一份中间匹配 | \(m=\max(q+a+d,0)\)，\(\mu=\min(q+a+d,0)\) | 取恰 \(m\) 条中间实际红五端点边，允许 \(q<0\) 或 \(m=0\)。匹配首末像都在各自容器，容器减 \(m\) 上界控制未覆盖的供应端口，不需要让任意中间边都有外部供给。见 §4，式 (12)–(14) 与下节补写。 |
| OB-14 交会与终端矛盾 | 同一中间匹配上的两外像 | 左失去的 \(\tau\) 和右实际增广多出的 \(\tau\) 各扣或加一次。式 (15) 给 \(\ell\ge1\)，若 \(m=0\) 即矛盾。否则相交边给 \(z<r\le y<s<t\)，两帽给 \(B_4(z,r,s,t)\)，与中间 \(R_5(z\to t)\) 同端违反 weak7。见 §4。 |
| OB-15 全局量词 | 任意 767、共同有效容量 \(b\) | 加权界先给 \(n\le3b+2\)，取等迫 \(w=0\)。由任意缺额预算及 M0，实际归一化缺额至多 \(3\)。任一满侧由 onefull 排除；双正缺额时 \(x\ge y\) 用非交错，\(x<y\) 用统一补偿。整数性给 \(Q_{\rm cap}\le3b+1\)，独立 chart 等式给 \(F_{\rm cap}\le3b+2\)。代 \(b=25\) 得 \(76,77\)。见 §5、共同中间稿 §1–4、跨角色稿 §5、R20 §4。 |

## 4. 两处计数补写 · ADD_DERIVATION

**扩域不交。** \(K_-=Z_-\sqcup P_H\sqcup B_H\) 落在 \(D\sqcup P\sqcup Q\)，因此与 \(B\subseteq I\) 不交。\(K_+^*=Z_+\sqcup Q_H\sqcup A_H\sqcup\mathcal R\) 同样落在 \(D\sqcup Q\sqcup P\)，与 \(A\subseteq I\) 不交。故左右实际扩域人口恰为 \(b-\kappa_-+|B|\) 与 \(b-\kappa_++\tau+|A|\)。左域避 \(\Psi\) 即可兑现反向锁约束，右域避 \(\Omega\) 即可兑现正向约束。\(y\notin\Psi\)，若 \(y\in\Omega\) 仍按 \(e_y\) 单独处理。[统一稿 §1.2、§2、§3](N7_COMPLETE_LOW_PREDECESSOR_COMPENSATION_AND_UPPER_BOUND_20261103.md)

**中间匹配像。** 写 \(U_{\rm all}=Z_-\sqcup A_H\sqcup(C'\cap B_H)\)，\(V_{\rm all}=Z_+\sqcup B_H\sqcup(C\cap A_H)\)。任一中间红五完全在两核内，首点属于 \(C'\)，末点属于 \(C\)，按 \(D_{\rm all}\) 的三角色分解分别进入 \(U_{\rm all},V_{\rm all}\)。固定中间匹配的首末像 \(J_U,J_V\)，各有 \(m\) 点，分别包含在这两个容器中。若 \(L_{\rm port}\) 与 \(R_{\rm port}\) 是剪枝后实际外匹配的供给端口集，则 \(L_{\rm port}\subseteq Z_-\cup A_H\subseteq U_{\rm all}\)，\(R_{\rm port}\subseteq Z_+\cup B_H\subseteq V_{\rm all}\)。因此
\[
|L_{\rm port}\setminus J_U|\le c_-+a+v-m,\qquad
|R_{\rm port}\setminus J_V|\le c_++d+u-m.
\]
外匹配保证同侧端口不重复；各侧覆盖的端口分别一一指向中间匹配的边，故取两边数和减 \(m\) 是它们共用中间边数的下界。令 \(N=|A|+|B|\)，代入实际容量、纤维余量与 \(m=q+a+d-\mu\)，得
\[
\begin{aligned}
\ell
&\ge N-\kappa_--\tau-\epsilon_L-\kappa_++\tau+p_h
 -(c_-+a+v-m)-(c_++d+u-m)-m\\
&=N-2q-\alpha-\beta-a-d-u-v+m+p_h-\epsilon_L\\
&=2+\delta_l+\rho_h+p_h-e_y-\epsilon_L-\mu\ge1.
\end{aligned}
\]
即使某容器成员没有中间红五角色，也只增加可扣的未覆盖数。没有为任何中间边预设外供给。[统一稿 §3–4，式 (10)–(15)](N7_COMPLETE_LOW_PREDECESSOR_COMPENSATION_AND_UPPER_BOUND_20261103.md)

## 5. 承重分支与边界复核

**加权界。** 共同中间稿 §3 的双 clean 证明在实际 \(D\setminus C_0\) 取 \(q-w\) 条红五匹配。根横截与容量给 \(q\ge w\)，而外路径分类使用加强 \(W,W'\) 排除 \(C_0\) 作端口。补偿下界为 \(2+r+s_0-k\ge1\)，空中间匹配也被覆盖。§4 由 \(t=3,\ h_L,h_R\le5\) 及缺额至多 \(2\) 得四种非空锁类型 \((1,1,1),(1,1,2),(2,1,1),(2,2,2)\)。纤维代表 \(D_0\) 和普通供给修补分别进入实际容量核。低、高锁添边的根及端口与各自普通边分离。四型中前三种非 \((1,1,1)\) 型由纤维计数给正交会，剩余 \((1,1,1)\) 型分别以另一侧同型的满代表核或另一侧 clean 的普通修补兑现。满侧纯前供推导只用完整接口及满侧实际容量。它推出根序后，所调用的共同中间稿 §2 非交错排除只需 \(t\ge2\)。由加权取等层全覆盖排除 \(n+w=3b+3\)，该推导先于 767 的新人口下降。[共同中间稿 §3–4](N7_COMMON_MIDDLE_COMPATIBILITY_AND_WEIGHTED_BOUND_20261103.md)

**非交错。** 共同中间稿 §2 中，\(T\to S\) 的蓝四两端各可用红六帽补一点成 \(B_6\)。由此所有 owner 首根不晚于所有 owner 末根。在 \(x>y\) 情形，用最晚可用 owner 首根紧左割，或在缺少晚于 \(y\) 的 owner 首根时用 \(y\) 紧右割，合计 owner 损失至多一。\(x=y\) 用严格割只删共同根一次。\(t\ge2\) 时根数下界兑现中间匹配规模为正，交会下界是 \(t+\rho-1\ge1\)。[共同中间稿 §2](N7_COMMON_MIDDLE_COMPATIBILITY_AND_WEIGHTED_BOUND_20261103.md)

**Onefull。** 以右满为例，\(H_R=X\setminus T\)，内部红五首点 \(Z'\) 与内部蓝五末点因接桥禁形不交。两类由删点容量各至少 \(b\) 个，故分划 \(H_R\)，实际纯前供 \(Z'=P\sqcup U\) 满 \(b\)。对首对 \((f_0,t_0)\) 的 \(T\) 后继，加 \(t_0\) 入 \(Z'\) 迫一条终于 \(t_0\) 的实际红六，其前五点全在 \(H_R\)，首点 \(p_0\in P\)。首帽及加强右扇给 \(f_0<p_0<e_0\) 对所有末根 \(e_0\)。若 \(t_0\in C_0\)，加强扇排除 \(e_0<f_0\)，给弱不等式。故满侧只推出 \(y\le x\) 所需的完整根序，随后用非交错排除，另一侧缺额无需额外限制。[跨角色稿 §5](N7_CROSS_ROLE_ROOT_ORDER_AND_SEPARATED_CLASS_EXCLUSION_20261103.md)

边界核对覆盖低根落在 \(\Omega\)、\(y\in\Omega\)、右尾替换使用 owner、\(m=0\)、负 \(q\)、非正外匹配下界、空剩余根集以及缺额 \(3\)。三处 `ADD_DERIVATION` 只兑现已用条件与隐含计数。独立复审、历史 SAT 及证书重放均未发生。本轮无外部 Claude 调用、无未公开研究材料外传，也无科研代码、枚举或求解运行。[文档核验回执](N7_7677_PROOF_OBLIGATION_AUDIT_DOCUMENT_RECEIPT_20261103.md)
