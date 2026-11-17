# N(7,r,s) 截至 2026-11-07 的结构综合与下一步路线

现有完整 signotope 模型的全局**工作上界**仍为 **757／766／767／777 = 40／49／75／76**。本轮实质推进是下文完整证明的**端口有向路共同增广引理**：它把旧四端口预算提升为同一对纯末／纯源下的实际端口总路长预算，饱和时还迫出全量中性红桥，给出比泛路线更具体的下一义务。它尚未排除全部75点残余，不给出全局74／75，也不主张文献首创。

11 月 6 日的唯一交叠、双满纯角色整类排除，已将75点残余缩到多交叠、至少一侧纯角色未满的实际母体；三满域的共同不相容、regular 纯增强共根同步以及严格交错末端共同实现仍未证明。

本文日期为 2026-11-07；第2节记录本轮主会话冻结推导，其余最新结构原件的记录日期均为2026-11-06。历史由[11/05 证据台账](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-structural-roadmap-20261105/evidence-ledger.md>)和[11/06 综合](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-structural-roadmap-20261106/synthesis.md>)恢复，既有结构以本报告逐项链接的冻结原件为准。11/05 台账早于当日后来完成的 C49 证明，其中的 C50、未找到新增报告等表述是当时截面的状态，不能作为当前状态。

本文是忠实汇编与同会话诊断，不是独立数学审查。既有接受、机器核验、固定公式结果和新工作证明分别保留原保证；本次没有科研计算、求解、证书重放或接受升级。

## 1. 原对象、符号与可传播的数值关系

$N_{\rm sig}(7,r,s)$ 指完整有序 rank-3 signotope 中，无蓝 $r$、红 $s$ 和 weak7 的**最大避免人口**。四点 packet 至多变色一次，路径长度按实际点数计；weak7 禁止同一对实际首末点的异色路径长度和至少为 9，内部允许重合。换诱导域或合法 chart 后，路径及角色必须按新的实际输入重算。避免人口与 forcing 阈值相差的那一步不能省略，更不能直接认领几何上界。

记 $a=16$ 为 747 有效界，$b=25$ 为 756 及其换色对偶的共同有效界；容量 $A,C,Q,F$ 分别对应 757、766、767、777。现有工作证明关系是

$$
A\le a+b-1,\qquad C\le2b-1,\qquad Q\le3b,\qquad F=Q+1.
$$

代入得到 $(A,C,Q,F)\le(40,49,75,76)$，不主张这些上界全部取等。$b\le25$ 的限定域人工接受见[C8 记录](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md>)；实际 25 点见证及既有独立核验见[E21](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n756-professor-review-20261027/evidence/E21/verification.json>)。二者各有作用，后续长链不因 $b$ 的接受而自动接受。

**传播桥 $Q\le C+b$ 尚未证明。** 若真，由 C49 与 $b=25$ 得 $Q\le74,F\le75$。目前实际可用的旧响应式是

$$
Q\le\min\{3b,C+b+5,A+C-1\}
\le\min\{75,79,88\}=75.
$$

所以单独把 $C$ 改为 48 或把 $A$ 改为 39，仍不降低现行 $Q75$。条件传播应明确写为

$$
C\le2b-\delta,\quad Q\le C+b-\gamma
\ \Longrightarrow\ 
Q\le3b-\delta-\gamma,\quad F\le3b-\delta-\gamma+1.
$$

Q75 的实际承重稿是[替锁与 75／76 工作界](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCK_REPLACEMENT_COMMON_ROOT_EXCLUSION_AND_7576_BOUND_20261103.md>)，不是未证的新桥。

文献构造给另一端的对照。[Baek–Balko，SoCG 2025，Theorem 4](https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/html/LIPIcs.SoCG.2025.13/LIPIcs.SoCG.2025.13.html)的几何split强迫阈值为 $1+L$，其中

$$
L(n,r,s)=\sum_{i=n-r+2}^{s}\binom{n-2}{i-2}.
$$

其 $L$ 点构造避免split及规定两帽，因而也避免同端weak，并产生本项目signotope域的**构造下界**。对应747／756／757／766／767／777，人口依次为 **16／25／26／30／31／32**；后四个ordinary基线不能写成一般模型容量上界。[Baek v2，Theorem 2.7](https://arxiv.org/pdf/2206.04260)在全部ordered coloring中给747上界16，与构造合并得到 $a=16$。这里的构造下界与本项目工作上界不是相同保证层级。

## 2. 本轮实质推进：端口有向路的共同增广

本节为2026-11-07主会话冻结的同会话引理及短证明，保证状态为 **same-session、未外审、未接受**。基础蓝扇、同端蓝四与安全性证明沿用[FOUR_PORT_AUGMENTATION §§1—4、§6](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/FOUR_PORT_AUGMENTATION.md>)；这里将其四个端口扩为同一实际母体的两条端口有向路。

### 2.1 参数、实际图与两个结论

设 $r\ge5$，完整有序 rank-3 signotope $X$ 禁止 $B_{r+1},R_{r+2},\mathrm{weak}(r+2)$；weak的长度和阈值为 $r+4$。令 $S,T$ 为全部 ambient $R_{r+1}$ 的首、末点集，$D=X\setminus(S\cup T)$。固定

$$
q\in T\setminus S,\qquad p\in S\setminus T,\qquad q<p.
$$

每条实际入 $q$ 的红 $(r+1)$ 路径，以其尾三点 $(u,v,q)$ 给左图递增边 $u\to v$；每条实际出 $p$ 的红 $(r+1)$ 路径，以其头三点 $(p,w,t)$ 给右图递增边 $w\to t$。图取全部这样的实际边，顶点仅取边端口。令 $d_-(q),d_+(p)$ 为各图最长有向路的**顶点数**，两者均至少2。

**端口路长约束：**

$$
\boxed{d_-(q)+d_+(p)\le r.}\tag{P1}
$$

若实际 $C_0\subseteq D\cap(q,p)$ 满足 $C_0\cup\{q\}$、$C_0\cup\{p\}$ 都无 $R_r$，且 $\beta$ 是无 $R_r,B_{r+1},\mathrm{weak}(r+2)$ 域的有效人口容量，则

$$
\boxed{|C_0|+d_-(q)+d_+(p)\le\beta.}\tag{P2}
$$

### 2.2 两条端口路可共同拼成一条蓝路

先看左图连续两边 $u\to v\to w$。若 $\chi(u,v,w)=R$，取第一条边的实际入 $q$ 见证，删末点 $q$ 得 $r$ 点红前缀，后接 $w,q$；第二条边的见证给 $\chi(v,w,q)=R$。这组成禁形 $R_{r+2}$。所以每条左图有向路都是实际蓝路径；右图全序反向同理。

取同一母体中左、右最长有向路，分别记为 $L_*,R_*$。旧蓝扇对任一左端口 $a$ 和右端口 $b_0$ 给实际 $B_4(a,q,p,b_0)$。路径子序列遗传特别给

$$
\chi(a,p,b_0)=\chi(a,q,b_0)=B.
$$

任取左边 $a\to a'$。对 $x>q,x\notin T$，其实际尾三点蓝扇给 $\chi(a,a',x)=B$；取 $x=p$。packet $(a,a',p,b_0)$ 的首、末项都蓝，故全部项蓝，得到 $\chi(a,a',b_0)=B$。

任取右边 $b_0\to b'$，其头三点蓝扇给 $\chi(q,b_0,b')=B$。packet $(a,q,b_0,b')$ 的首、末项同样都蓝，得到 $\chi(a,b_0,b')=B$。

因此把 $L_*$ 后接 $R_*$，内部与两个连接三元组全部为蓝，组成实际 $B_{d_-(q)+d_+(p)}$。禁 $B_{r+1}$ 即给(P1)。特别地，$r=5$ 时不能两图各有连续两边。全母体中，若两类均非空，则所有满足 $d_+(p)\ge3$ 的纯源，都在所有满足 $d_-(q)\ge3$ 的纯末之前；否则其逆序对 $q<p$ 会给禁 $B_6$。

### 2.3 两整路加入中性域仍无红 r

每个 $d\in C_0$ 均可接在左蓝路 $L_*$ 末端：该路末边来自实际尾三点，对 $d>q,d\notin T$ 的蓝扇给所需最后三元组。子序列遗传于是保证任意两个左路点与 $d$ 构成蓝三。右路反序同理，任意 $d$ 与两个右路点也构成蓝三。

反设实际诱导域 $C_0\cup L_*\cup R_*$ 中有 $R_r$。若它同时用左右路，首末点为某个 $a\in L_*,b_0\in R_*$，已有同端 $B_4(a,q,p,b_0)$，长度和 $r+4$ 违反weak。若只用左路和中性点，使用至少两个左路点时由上述蓝三排除；只用一个左路点 $a$ 时，红路为 $R_r(a,d_1,\ldots,d_{r-1})$。因 $C_0+q$ 无红 $r$，必有 $\chi(q,d_1,d_2)=B$；蓝扇给 $\chi(a,q,d_1)=B$，红路给 $\chi(a,d_1,d_2)=R$，packet $(a,q,d_1,d_2)$ 呈 $(B,?,R,B)$，不可能至多一次变色。只用右路的情形完全反序。

全在 $C_0$ 内时被安全前提排除；全在端口内时，被第2.2节共同拼成的蓝路径及遗传性排除。上述分类覆盖全部实际红路，故整个增广域无 $R_r$。其余禁形由母体诱导遗传，三部分实际不交，容量给(P2)。

### 2.4 三满域的直接用途与准确未闭口

回到 $r=5$ 和实际三满域 $X=A_*\sqcup K\sqcup B_*$。对**同一对**纯末／纯源 $q<p$，按旧接口定义

$$
E=(\mathrm{Bad}_-\cup\mathrm{Bad}_+)\cup(K\setminus(q,p)),\qquad
C_0=K\setminus E.
$$

旧§6给 $C_0$ 每点双向蓝五供应，§4给 $C_0+q,C_0+p$ 安全。由 $|K|=\beta=b$ 及(P2)，得到

$$
\boxed{|E|\ge d_-(q)+d_+(p).}\tag{P3}
$$

若某一端口图存在连续两边，则右侧至少5；由(P1)此时恰为5。若能对某个实际余类找到**同一对** $q,p$ 满足 $|E|<d_-(q)+d_+(p)$，便可排除该类。这是本轮优先动作，而不是继续只追求旧 $|E|\le3$。但尚未证明每个余类都有这样的同对；若所有可用端口对都刚性地只有 $(d_-,d_+)=(2,2)$，便只恢复旧四端口预算，没有额外收益。

固定 $K$ 时，若 $q=\min(T\setminus S)<p=\max(S\setminus T)$，这一极端对使区间外删点数 $|K\setminus(q,p)|$ 最小；它未必使 $d_-+d_+$ 最大。不能把一个端口对的最小删点数与另一个端口对的最大路长拼成(P3)的反面。

### 2.5 路长饱和迫全量中性红桥

另设同一对 $q,p$ 已满足 $d_-(q)+d_+(p)=r$。固定上述左、右最长路，取左路最末点 $a$ 与右路最初点 $b_0$。对每个实际

$$
x\in D\cap(q,p),
$$

不要求 $x$ 有双向蓝供应或属于安全域。左蓝路可由末边蓝扇后接 $x$，右蓝路可前接 $x$。若 $\chi(a,x,b_0)=B$，两条路通过 $x$ 共同成为 $B_{r+1}$，矛盾。因此

$$
\boxed{\chi(a,x,b_0)=R\quad\text{对全部 }x\in D\cap(q,p).}\tag{P4}
$$

同时实际 $B_4(a,q,p,b_0)$ 仍在，故任何同端 $R_r(a,b_0)$ 都被weak禁止。具体在 $r=5$ 时，不存在三个实际中性点 $x<y<z$、均在 $D\cap(q,p)$，同时满足

$$
\chi(x,y,z)=\chi(a,x,y)=\chi(y,z,b_0)=R.
$$

否则三个连续三元组恰给实际 $R_5(a,x,y,z,b_0)$，与上述蓝四同端矛盾。

这一推论将饱和端口路长接回实际红供应，为regular共根等接口提供首个可尝试的共同路径条件，超出单纯计数四个端口。尚未证明每个余类存在路长饱和对，亦未保证上述兼容红三元组必出现；不能据此称regular已解，不能把这里的 $a,b_0$ 替换成其指定 $j,k$。

### 2.6 Regular纯增强余类：饱和时兑现同一 z 的整侧替换

本推论限于[regular纯增强余类及其全量跨根蓝五，MULTI_ROOT_FRONTIER §13](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/MULTI_ROOT_FRONTIER.md>)的实际输入，状态仍为同会话、未外审、未接受。原件给同一对 $q_0<z<p_0$，其中 $q_0\in T\setminus S,p_0\in S\setminus T$；对每个实际入 $q_0$ 红六的末前驱 $a$ 与每个实际出 $p_0$ 红六的第二点 $b_0$，都有

$$
B_5(a,q_0,z,p_0,b_0),\qquad\chi(a,z,b_0)=B.
$$

另加前提 $d_-(q_0)+d_+(p_0)=5$。任取左最长路的末边 $(a',a)$，独立任取右最长路的首边 $(b_0,b')$。若 $\chi(a',a,z)$、$\chi(z,b_0,b')$ 都蓝，则左路、$z$、右路共同成为6点蓝路：两路内部为蓝，两个邻接三元组由假设为蓝，中间三元组 $\chi(a,z,b_0)$ 由原件为蓝，违反禁 $B_6$。

两侧最长路可以任意独立选择。因此至少有下列一项成立：

$$
\begin{aligned}
&\text{每条左最长路末边 }(a',a)\text{ 都满足 }\chi(a',a,z)=R;\\
&\text{每条右最长路首边 }(b_0,b')\text{ 都满足 }\chi(z,b_0,b')=R.
\end{aligned}\tag{P5}
$$

第一项成立时，对每条支持相应末边的实际入 $q_0$ 红六，把末点 $q_0$ 换为 $z$，其余连续三元组保持、最后一项由(P5)为红，便兑现末对为 $(a,z)$ 的实际红六。第二项成立时，对每条支持相应首边的实际出 $p_0$ 红六，把源点 $p_0$ 换为 $z$，同理兑现首对为 $(z,b_0)$ 的实际红六。

这给出**同一个 $z$ 的整侧实际替换**，未假设两侧同时成立，也未证明这些新端口属于先前唯一性限制的 $C_-/C_+$ 角色，故不能自动认作 $j/k$。若两路长之和只有4，本推论没有得到；尚未证明该regular余类必有路长饱和对。这里 $z\in I$，不是(P4)所量化的中性点，不将两项红／蓝结论混用。

## 3. 历史进展：输入收益与结构收益分账

| 日期或阶段 | 757／766／767／777 工作账 | 实际变化 |
|---|---|---|
| 初期 | 45／58／103／206 | 初期工作账 |
| R5 | 44／58／101／201 | 实际覆盖的严格交叠 |
| R6，$b=28$ | 43／56／98／195 | 输入变化及当时传播 |
| R7 | 43／56／89／177 | H／R 不交分解、五点横截 |
| R8，$b=26$ | 41／52／83／165 | 输入变化及当时传播 |
| R20 | 41／52／83／84 | 合法 chart 的精确关系 $F=Q+1$ |
| R23，$b=25$ | 40／50／80／81 | 新输入经旧链传播 |
| 2026-10-29 | 40／50／79／80 | 三匹配 |
| 2026-10-31 | 40／50／78／79 | 前驱压缩 |
| 2026-11-02 | 40／50／77／78 | 锁区间 |
| 2026-11-03 | 40／50／76／77，再至 40／50／75／76 | 共同中间、补偿、替锁逐步闭合 |
| 2026-11-05 后续 | 40／49／75／76 | 实际替末、交替环无环、完整路径安全增广得到 C49 |
| 2026-11-06 后续 | 40／49／75／76 | 唯一交叠与双满纯角色整类排除；未满多交叠继续开放 |

历史来源见[R1—R27 记录](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_REVIEW_R1_R27_20261026.md>)及[11/05 台账](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-structural-roadmap-20261105/evidence-ledger.md>)。$b:29\to28\to26\to25$ 是输入改进，不能和同一步结构收益重复计算。R20 与 C49 的一般结构操作仍是有效范例；历史轮次、文档数量或 UNSAT 次数不代表完成度。

## 4. 当前 75 点反例必须进入的实际范围

对同一 767 母体 $X$，定义全部 ambient 红六的源、末点集及不交角色

$$
S=\operatorname{Src}_{R_6}(X),\quad T=\operatorname{End}_{R_6}(X),\quad
I=S\cap T,\quad P=S\setminus T,\quad T_0=T\setminus S,
$$

$$
D=X\setminus(S\cup T),\quad
U=\operatorname{Src}_{R_5}(D),\quad V=\operatorname{End}_{R_5}(D),\quad
w=|U\cap V|.
$$

本报告用 $T_0$ 表示原结构文件常记的纯末集 $Q$，避免与容量 $Q=N_{\rm sig}(7,6,7)$ 混淆。

任意 75 点输入的当前必要条件是

$$
\boxed{w=0,\qquad |I|\ge2,\qquad
\min\{|P|,|T\setminus S|\}\le b-1=24.}
$$

三项分别有实际来源，不能互相替代：

- 正 $w$ 类至多 $3b-1$，故 75 点必 $w=0$；准确旧式为 $n+\min(w,1)\le3b$ 与 $n+w\le3b+1$，未证 $n+w\le3b$。[单 through 审计](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7576_DEPENDENCY_AUDIT_AND_SINGLE_THROUGH_EXCLUSION_20261103.md>)
- $I=\varnothing$ 已由 C49 的无 through 桥排除；唯一交叠主定理进一步证明 $I=\{z\}\Rightarrow |X|\le3b-1$，不需极端点、无外跨或 $D+z$ 安全假设。[C49 §5.1](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n766-strict-capacity-20261105/PROOF.md>)、[唯一交叠 PROOF](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/PROOF.md>)
- 双满纯角色定理排除 $n=3b,|P|=|T_0|=b,|I|\ge2$ 整类；它没有排除一侧满或两侧均未满的全部输入。[SATURATED_PURE_ROLES](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/SATURATED_PURE_ROLES.md>)

此外，每个命中全部实际红六的顶点集 $K$ 都满足 $|K|\ge75-C\ge26$；特别 $|S|,|T|\ge26$。这不是一个新的下界构造，而是反设 75 点后的必要条件。不能用小稀疏例冒充该临界母体。

## 5. 主要结构资产及其准确调用边界

**C49 的一般证明。** 对一般 $p\ge4$，双短帽有效容量 $b$ 给 balanced 容量 $2b-1$；承重机制是实际路径替末、双色交替环无环和安全增广，不依赖 Through14／Joint17／Closure 的固定公式结果。[原证明与验证](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n766-strict-capacity-20261105/VERIFICATION.md>) 同时保留 24 点双 through 反例及 30 点 neutral 等号族，不能借 strict 容量把旧 neutral 注入预算直接少付一单位。

**唯一交叠的闭合链。** 反设 $n=3b$ 迫两纯角色满；参数无关 M0 与 strict balanced 容量迫每侧缺额 1、至多单 owner／单锁；满短帽消去 $D$ 核内红五端点；实际根扇与末／首对屏障迫 $a<\omega<z<\psi<b_0$；同一中间域迫 $R_5(a,D^3,b_0)$，真实 owner 供应兑现锁末／首对，再得同端 $B_4$ 矛盾。锁标签本身不提供实际帽。[PROOF §§3—9](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/PROOF.md>)

**双满纯角色的闭合链。** 满容量在同一 M0 系统中压出单例纤维、$Z_\pm=\varnothing$、旧根等于 $I$；相邻 cuts 的实际 owner 集合在 $i\ge3$ 时组成 $b+1$ 点红短帽，$i=2$ 时以纯源跨越引理和完整根扇导出纯末点成为红六源的矛盾。其他 owner 的私有红五内部允许包含已有 owner，不能写成纯 $D^3$。[SATURATED_PURE_ROLES §§2—9](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/SATURATED_PURE_ROLES.md>)

**全域 M0 根族非空。** 75 点、$w=0$ 时，实际双 balanced 核的缺额至少 1，旧基底人口超过 $b$，从而旧根及增强根双方均非空。可以定义 $x_e=\min E^+,y_f=\max F^+$，按严格交错、严格分离、共根三种次序组织；空根不是额外当前分支。有效根不是 ambient 极端纯源／纯末，且共根不等于唯一交叠。[ROOT_AND_M0_INTERFACES §1](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-critical-crossing-and-joint-roots-20261106/ROOT_AND_M0_INTERFACES.md>)

**一般四端口工具。** 对 $r\ge5$，纯末 $q$ 在纯源 $p$ 之前，中性 $C_*\subseteq(q,p)$ 满足 $C_*+q,C_*+p$ 无 $R_r$，则任意实际入 $q$、出 $p$ 路径的四个相邻端口同时加入仍无 $R_r$；红短帽容量 $\beta$ 给 $|C_*|\le\beta-4$。中性点有 ambient 双向蓝 $r$ 供应时安全条件自动成立。旧双满纯角色 caller 已被更强整类定理覆盖；未满输入必须重证安全或供应。[FOUR_PORT_AUGMENTATION §§1—5](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/FOUR_PORT_AUGMENTATION.md>)

**旧工具仍有条件价值。** 全路径 net-augmentation 要把同一接收域的缺额只计一次；共同红 join 的路径产品不保证一般 $\tau\le2\nu$；critical-cover 的二根释放、nested 的纯 packet 嵌套与 outer-short 四环属于各自完整域的成果，尚不覆盖全部 multiple roots。[净增广](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-net-augmentation-20261105/PROOF.md>)、[路径产品与反例](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-757-766-structure-20261105/PROOF.md>)、[critical-cover](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-critical-cover-continuation-20261105/PROOF.md>)、[nested 验证](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-nested-path-and-active-core-20261105/VERIFICATION.md>)

## 6. 当前优先义务：真正三满域的共同实现

[THREE_SATURATED_DOMAINS](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/THREE_SATURATED_DOMAINS.md>) 已将**整个严格分离余类**及指定 regular $e_L=1/e_R=1$ 分支，经全替锁归约为真正不交分划

$$
X=A_*\sqcup K\sqcup B_*,\qquad |A_*|=|K|=|B_*|=b.
$$

其中 $A_*,B_*$ 是实际756，$K\subseteq D$ 无红五，$A_*$ 各点无 ambient 入蓝五，$B_*$ 各点无 ambient 出蓝五。这里的 $A_*$ 是实际集合，不是容量 $A$；原 M0 owners 可以非空。旧重叠蓝核和缺席锁不能在全替锁前当成这份分划。

对两侧完整实际失败集

$$
\mathrm{Bad}_-=\{k\in K:A_*+k\text{ 含 }R_6\},\qquad
\mathrm{Bad}_+=\{k\in K:B_*+k\text{ 含 }R_6\},
$$

已有定理给两侧各自非空。对**同一对**纯末／纯源 $q<p$，定义同一份实际并集

$$
E=(\mathrm{Bad}_-\cup\mathrm{Bad}_+)\cup(K\setminus(q,p)).
$$

原一般四端口工具给 $|E|\ge4$；本轮第2节将它加强为同一对端口下 $|E|\ge d_-(q)+d_+(p)$。下一义务应据实际端口图，寻找 $|E|<d_-+d_+$ 的同对矛盾；没有连续两边的刚性情形仍须处理。两侧 Bad 非空不意味着共享一点；不能分别优化三个集合后相加。[四端口稿 §6](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/FOUR_PORT_AUGMENTATION.md>)

regular 单侧余量还有更强的实际入口：最小旧首端口 $t_*$、跨域红六末前驱 $p_5\in A_H\sqcup C_-$、私有红五及高根位于 $(z,t_*]$。这组共同实现未被排除，不能把归约本身记为整支闭合。[三满域稿 §§4—7](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/THREE_SATURATED_DOMAINS.md>)

## 7. 第二义务：regular 纯增强共根的共享 K 同步

此线严格限于 regular 共根、$e_L=e_R=0,d_D=1$；不覆盖任意共根。额外覆盖点非空的类和含任一旧共根的类均已排除，剩余为

$$
\widetilde C=C_D,\qquad z\notin\widehat E\cup\widehat F.
$$

有 $|K|=b-1$，实际 $R_5(j,K^3,k)$，共享同一 $K$ 的 $K+j,K+k$ 都是满 $b$ 点红短帽。已有 $B_3(j,z,k)$ 的长度和仅为 8，尚不违反 weak7。指定两个外域内的相邻端口唯一；后续 ambient 唯一性也只限 $C_-/C_+$ 角色，不能扩大为所有 ambient 端口唯一。[REGULAR_COMMON_ROOT §§6—8](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/REGULAR_COMMON_ROOT.md>)

[MULTI_ROOT_FRONTIER §§9—15](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/MULTI_ROOT_FRONTIER.md>) 进一步给两个严格容量补域的实际新端口

$$
u<r<z<s<v,\qquad u\in K\setminus V,\quad v\in K\setminus U,
$$

以及纯末／纯源端口 $q_0<z<p_0$ 的全量实际 $B_5(a,q_0,z,p_0,b_0)$。至少一侧所有相邻端口落在 $K$，至少有一份纯角色蓝五，不能默认两侧同时成立。$u,v$ 的 ambient 红五供应也不是 $D$ 内 $V/U$ 身份。

这一**指定余类**若 $|D|=b+q_{\rm def}$，则 $q_{\rm def}\ge1$，且

$$
|P|,|T_0|\le b-q_{\rm def}-1,\qquad |I|\ge q_{\rm def}+2.
$$

因此数值上两纯角色都至多23、$|D|\ge26$，只能在此作用域内使用。未闭义务是把两个 $K$ 内新端口、全量蓝五和两满红短帽同步成一次真实 $b+1$ 红短帽增广、同端 $B_4(j,k)$ 或 $D$ 端点红六。不能把 $a,b_0$ 自动换成 $j,k$；原件已撤回的跨三元组红色推断不参与证明。

## 8. 第三义务与独立备选

**严格交错、一侧饱和。** [MULTI_ROOT_FRONTIER §§1—8](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/MULTI_ROOT_FRONTIER.md>) 限于 $|P|=b,|T_0|=b-e,x_e<y_f$。已得两侧单例纤维、$\widehat E=I\setminus\Omega$、最高增强首根 $y_f=z_h\in\widehat E\cap\widehat F$、$\Omega\cap I>y_f$，并有

$$
h-2+r_1\le\kappa_+=e-\delta-c_+,\qquad
i\le2e+2-\delta-c_+.
$$

每个内部根消耗一个不同实际 ordinary 点，当前计数恰好一换一。最高根还要再耗一单位尚未证明，不能把 $h\le\kappa_++2$ 改成 $h\le\kappa_++1$，也不能宣布一侧饱和全排。下一步是保留同一系统的端口、ordinary 点和最高旧双根，解决实际末端共同实现，而非继续代数值拆 case。

**合法换根备选。** R20 的工作理论将合法根限制在共同合法循环，不能任取内部 pivot。三合法根条件下，共同非根域 73 点可得到三类型传递与缺型域安全扩张；缺型域人口至多 $C-1=48$。若再取得短帽 $A_*$ 与缺型域 $U_*$ 的共同覆盖、且交叠非空，即可把73压到72；该覆盖未构造，三类型传递不自动给三链分划。[ROOT_AND_M0_INTERFACES §3](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-critical-crossing-and-joint-roots-20261106/ROOT_AND_M0_INTERFACES.md>) 只覆盖该条件输入，不穷尽所有合法根数。

**长期传播目标。** 对一般 $p\ge4$，定义

$$
b_p=N_{\rm sig}(p+2,p,p+1),\qquad
c_p=N_{\rm sig}(p+2,p+1,p+1),\qquad
q_p=N_{\rm sig}(p+2,p+1,p+2).
$$

在禁 $B_{p+1},R_{p+2},\mathrm{weak}(p+2)$ 的实际母体中，寻找红 $(p+1)$ 物理横截 $K$，且 $K$ 本身无红 $(p+1)$、无蓝 $p$，可推出 $q_p\le c_p+b_p$。这个充分分划强于数值桥；目前未证。更弱的75点里程碑是 $\tau_{R6}\le25$，配合 C49 即排除75；只证明这一临界 $\tau\le b$ 不能自动得到全参数、全人口的分划定理或通用桥。选择最大balanced域或再最小化坏路径势函数只能说明对象如何选，不能代替全路径交换存在性。[11/06 综合 §5](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-structural-roadmap-20261106/synthesis.md>)

**757／766第二单位交叠。** 可另争取完整实际短帽覆盖中的第二个交叠点，目标分别为 $A\le a+b-2=39$、$C\le2b-2=48$；目前还缺对全部相应临界域的证明，不能把已闭的局部根循环当作全域覆盖。它们可作为独立容量成果；单独取得仍不降低当前Q75。若传播桥成立，C48才可传成Q73／F74。[critical-cover](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-critical-cover-continuation-20261105/PROOF.md>)、[nested完整范围](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-nested-path-and-active-core-20261105/VERIFICATION.md>)

## 9. 局部最优诊断：有真实阻挡，但不能宣称方法走死

$Q:80\to75$、$C:50\to49$，以及最新两个整类闭合都是实际结构进步。需要停止的是与当前反例范围脱节的细化，以及把新的必要式当作净收益。以下阻挡已有原件支持。

| 阻挡 | 真实证据 | 对当前选线的影响 |
|---|---|---|
| 端点 Hall 不控制物理共享 | 23 点757／766完整模型的端点图有饱和六匹配；92条实际R6独立重建后，唯一最小物理横截为 $\{0,14,18\}$，$\tau=3$ | 否定普适 full-Hall 排除，不否定内部点短帽分划或临界 $\tau\le25$ |
| 严格局部增益会陷入平台 | 既有12点实际例：原四点横截释放至多两点不能严格收益，但整体四换二可把 used 4 降到2；两换二可以走平台 | 不能要求每一步严格人口下降，也不能宣称所有有界交换失败 |
| 单点 private 族不覆盖联合暴露 | 既有6点例：命中全部单点 private 族仍漏掉同时被两个释放点命中的红五 | 必须控制全部实际暴露族，并保持同一接收域 |
| 根数与 ordinary 缺额相互抵消 | 最新严格交错接口 $r_j-r_{j-1}=1$ | 缺少最高端额外一单位，重复结算不产生新界 |
| 已闭域持续细分 | 空交叠、唯一交叠、双满纯角色75点层已分别整类关闭 | 不再以排全局75为由重开这些旧 caller |
| 局部固定排除没有全类覆盖 | fixed24只约束固定23点色表及指定插入域；physical31首片外部终止未决 | 扩大同一搜索不能替代任意母体至有限核的覆盖定理 |

反例与状态来源为[clique-source 验证](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-clique-source-hall-20261105/VERIFICATION.md>)、[物理横截原数据](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_hall_counterexample_transversal_20261106/transversal.json>)、[10/28 最优覆盖 §5—6、§9](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_OPTIMAL_OVERLAP_EXCHANGE_AND_CUT_INTERFACES_20261028.md>)。这些小例不是接近49／75的极值实例，不否定带临界共同条件的全局最优命题。

后续有价值的成果应当覆盖当前某个完整残余类、给出真实净增广，或提供迫使改线的实际反例。仅增加标签、改名复推加权 through、未证少付一单位、独立选择有利路径后相加，都不改变现行上界。

## 10. 机器证据与审阅状态

历史机器结果只按原回执记录，本次未执行：E21 25点见证既有核验为 pass；Joint17 有固定公式 strict-RUP PASS；Closure 的 schema PASS 同时保留 `UNSAT_checked=false`、`CNF_binding=false`，不能作 C49 证据；outer-short 的 $p=5$ 结论来自1…15 active-prefix checked UNSAT加覆盖归约；physical31首片600秒外部TERM、exit $-15$ 且无solver状态，不能作SAT、UNSAT或成功checker。具体绑定与边界见[11/05 台账 §4](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-structural-roadmap-20261105/evidence-ledger.md>)、[outer-short 验证](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_outer_short_upto15_certificate_20261105/VERIFICATION.md>)、[physical31 RESULT](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_physical_cover31_20261106/solve_slice01_evidence/solve_slice01_cuts000/RESULT.json>)。

历史审阅亦不合并成接受：11/04 有限抽查保持 provisional；11/05 审阅失败未返回意见；11/06 deep/max 新任务失败、内容为空、工具调用0，没有数学 verdict。[11/05 审阅状态](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-structural-roadmap-20261105/review-state.json>)、[11/06 分层状态](<D:/科研/math agent/erdos-szekeres-sat-main/.aris/traces/research-review/2026-11-06_n7-structure-synthesis/status.json>)

本次新的外部 Claude 审阅因**自动审批拒绝向外部 Claude 披露私有研究资料**而未执行，没有产生新的独立意见、verdict、backend模型或实际effort证据。本文及11/06新增结构的保证仍为 **same-session、未外审、未接受**；同会话核读和忠实实施不能改称独立审核。

## 11. 恢复顺序与交付边界

从[最新 NEXT_SESSION](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-single-through-exclusion-20261106/NEXT_SESSION.md>)恢复，并消费本轮第2节新引理：优先在真正三满域中共同控制同一对端口的 $|E|$ 与 $d_-+d_+$，处理有连续边和刚性 $(2,2)$ 两种情况；若路长饱和，进一步把(P4)的全量中性红桥与实际红供应同步。其次同步regular纯增强共根共享 $K$ 的实际路径，再处理严格交错的最高端共同实现。合法换根保留为机制不同的条件备选。三类接口尚未覆盖或排除全部未满多交叠，非regular共根等范围继续留开。

本报告只更新本新综合文件，不改旧证明、旧任务状态、接受记录、封存CNF／proof、运行作业或工作流规则；未创建Goal或wiki。所有新结构仍须按原量词、同一实际母体、完整路径和共同成本接回当前75点层，才能得到新的无条件人口下降。
