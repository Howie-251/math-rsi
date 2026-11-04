# N7：H50 与 R30 的共同饱和、全支持约束及未闭合障碍

日期：2026-10-29。本稿由主会话 Astra 确定数学结论后，文档执行者忠实整理三条授权生成分支及其旧依赖。全部新增数学为 **unreviewed/unaccepted**。主会话的逐步推导、生成协作者交叉质询和来源自检均不是独立审阅。本轮科学检查、代码实验、枚举、solver、proof checker、证明重放均为 **0**；外部审阅与独立审阅均为 **0**，没有调用或请求 Claude。

本轮没有排除完整 X80，没有证明新的完整临界参数或接口子类不可能，也没有实际构造临界 X50/X80 反例。留下的是更具体的同母体必要条件、三条有序不交红五点路径的旧工具推论，以及两个错误闭合步骤的完整修正。当前链仍为 **40/50/80/81**；不宣称 C≤49、Q≤79 或 F777≤80。

## 1. 目标、方法审计与证据层级

本轮主目标是：对每个完整 767 配置 X，若 |X|=80，其 canonical 分解为 H⊔R、|H|=50、|R|=30，则在同一实际染色中导出禁形或严格容量节省。若这个全称目标成立，旧根归约才会给 Q≤79、F777≤80；它本身不证明独立的 C≤49。本轮没有达到该目标。

三个生成来源分别为 [A：共同等号与同根供应](N7_BRANCH_A_H50_R30_JOINT_EQUALITY_20261029.md)、[B：紧核缺角与共同支持](N7_BRANCH_B_TIGHT_MISSING_CORNER_JOINT_SUPPORT_20261029.md)、[C：MUS 下降与同时修复](N7_BRANCH_C_MUS_DESCENT_AND_SIMULTANEOUS_REPAIR_20261029.md)。上一份 [完整 pair 扇主稿](N7_FULL_PAIR_FAN_BOUNDARY_AND_TIGHT_CORE_DICHOTOMY_20261029.md) 的结果沿用，不重新登记。

| 方法 | 本轮实际检验的闭合步骤 | 有效保留与停止理由 |
|---|---|---|
| 同一 t 的 private R6 与纯 H 尾 | 两条仅交 t 的红六点路径能否直接拼出禁形 | 得实际蓝桥及全终点间隙限制；没有共同实际中间 pair，不能拼长蓝路径 |
| 紧核缺角的三条实际 B5 | 原载体补入第三点后，能否用 no B6 关闭两个 gate | 原 cap6 论证漏第二个新连续三元组，撤回；修正为对全部替代见证的条件红 gate 传播 |
| 同一临界赋值的全阻挡修复 | 修复后能否下降到一个新的单违例临界赋值 | 新违例可以多条；rollback 重开旧阻挡，招募原 Y 点又产生完整 all-K 违例族 |
| 两个共享 P 的实际满25核 | 可否把两个不同 q 点补全视为合法可交换资源 | 两核都实际存在于反设母体，但并集与中间交换未证避开 mixed B5/R6 |

三种方法的实际作用还须分清。A 的三块推论在已列 R/H 前提下，实质使用残余 role 禁配、τ=5 的 private 路径、no R7 及同端 R6+B3 的 weak 禁形；推论本身不再额外使用 packet。packet 承担 canonical/满核入口与同色子路径遗传，不能据三块推论宣称已攻克共享三元色的 packet 共同兼容。容量取等比一般最小性额外给出的是每个 r 的纯 H 尾和横截数恰为5。B 则直接在两个四点包中迫 gate，weak 只沿母体禁形及此前满核入口使用，没有新的同端闭合；容量给出两插入见证族，却不保证两族碰撞。C 的修复与 rollback 等式本质上适用于一般完整约束族，只有实际端点 fan 和末间隙屏障使用 weak 与 no R7，仍缺由 MUS 迫出所需位置关系的步骤，不能称为 signotope 支持排除。旧 private 路径、条件交换及重复收费都不构成新的容量信息或收益。

数值与证据分层如下。

1. a=16、b=25 是当前有效工作输入。b25 的 [C8 人工正式验收记录](../../09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md) 记 C1—C10 全部 accepted、pending 空；assurance 仍为 same-family/provisional，exact backend/model/actual effort 未报告、不可验证。此限定模型验收不等于无条件几何极值结论，也不提供25点例。
2. 结构迁移、交换及饱和论证保留各自研究草稿层级；本轮没有升级其正式接受或独立审阅状态。
3. [Through14 固定字节 strict-RUP 元数据](../../../../tmp/balanced49_abstract_port_20261026/through14_replay_result.json)、[Joint17 公式绑定](../../../../tmp/balanced49_remaining_hr_20261027/joint17_binding/result.json) 与 [Joint17 完整固定字节 strict-RUP 结果](../../../../tmp/n7_global_proof_completion_20261027/joint17/result.json) 各在其固定证书/公式范围内 PASS。本轮只读元数据，没有重新执行；全类语义迁移仍未独审、未接受。
4. [Closure schema 结果](../../../../tmp/n7_global_proof_completion_20261027/closure/result.json) 的 PASS 仅覆盖固定规则及符号 schema，actual_cnf_equality_checked=false、UNSAT_checked=false；[获取停止回执](../../../../tmp/n7_global_proof_completion_20261027/closure_acquisition/abort_receipt.json) 为 ABORTED_BUDGET_FEASIBILITY，source_acquisition_complete=false、CNF_binding=false。Closure 未闭合，不能据此登记 C49。
5. 本轮没有新的 formal/independent acceptance。requested native Sol/high 是文档执行角色记录，不由角色名推断实际 backend 或 effort 已被独立核实。

## 2. 精确模型、记号与当前数量链

X 是有限全序点集。每个实际三元组 a<b<c 恰着红 R 或蓝 B 一色；对每个 a<b<c<d，按 abc、abd、acd、bcd 排列的四元包至多换色一次。这是完整有序 rank-3 signotope 模型。

c-k 路径指严格递增的 k 个实际顶点，其全部连续三元组均为 c；路径长度计顶点。四包首尾同色迫全包同色，归纳得同色路径对子序列遗传。weak7 使用同一对实际首末点的异色路径，长度和达到9；可保端点缩短到阈值，不要求内部不交。两点路径真空成立，故单色7路径也被排除。

N757 禁 B5、R7、weak7；C=N766 禁 B6、R6、weak7；Q=N767 禁 B6、R7、weak7；F777 禁 B7、R7、weak7。b 是 N_sig(7,5,6) 及其换色对偶的有效工作上界，本轮取 b=25；不据此声称极大规模恰为25。所有 Src/End、路径和身份均在下标所指实际诱导配置内部重算，不继承母体的内部路径身份。

为避免字母混用，本文在 X80 中记

\[
S=\operatorname{Src}_{R6}(X),\qquad T_6=\operatorname{End}_{R6}(X),
\]

并以 **Z** 表示 R 内红六点路径的五点最小横截；Z 就是任务叙述的 T_small，绝不是 T6。共同中性集记 D；独立满50核的双终原子另写 D_H。红五点终集写 F_H 等，不与 F777 混用。

旧链是

\[
N_{757}\le a+b-1,\qquad C\le2b,\qquad Q\le C+b+5,
\qquad F_{777}=Q+1.
\]

代 a16、b25 得40、50、80、81。根端的等式与反向添点来自 [R20 §2—4](RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md)，本轮不重新认领。若只参考旧普通容量26/30/31/32，粗 gap 仍为14/20/49/49；几何历史口径不与完整模型混用。

## 3. canonical 入口为何合法，五点横截为何恰取等

### 3.1 R 无 B5 的来源不能省略

[R7 §1—3](RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md) 固定全局点对线性扩张 λ。对每点 x 取 λ 最小的关联对 xp(x)，置 P+={x:p(x)>x}、P−={x:p(x)<x}。其 fan 性质保证：末点在 P+ 的任何实际蓝路径都可追加 p(末点)，起点在 P− 的任何实际红路径都可前接 p(起点)。p(P+)⊆P−，反向同理。

令 G⊆P+ 为 P+ 内部同时结束 R5、开始 B4 的实际点集。canonical 分解为

\[
H=P_-\cup G,\qquad R=P_+\setminus G.
\]

H 是实际766，R 无 B5，并且 R 内不存在同时结束 R5、开始 B4 的点。R 无 B5 是因为 P+ 内 B5 可追加 p 成 ambient B6；不能只由 X 无 B6 推断。残余 role 禁配由删除全部 G 及遗传性得到。

### 3.2 残余红六点终集给五点横截

令 E=End_R6(R)。若 e∈E，取终于 e 的 R6 末对 u<e。若 e 启动内部 B3(e,q,r)，则 χ(u,e,q) 为红会产生 R7，为蓝会给从 u 启动的 B4(u,e,q,r)；而 u 结束原红路径的 R5 前缀，违反残余 role 禁配。因此 E 中任何点都不启动内部 B3。

所以 E 的全部三元组红，且 |E|≤6。若 |E|≤5，E 本身命中全部 R6。若 |E|=6，写 e1<⋯<e6。任一终于 e2 的 R6，其首点记 a。a>e1 时可前接右根 e1 得 R7；a<e1 时，为免把 a 前接 E 的 R6 成 R7，必须 χ(a,e1,e2)=B，而该 B3 与 a→e2 的 R6 同端点，构成 weak7。因此 a=e1。于是删 E\{e2} 已命中全部 R6，横截数 τ_R6(R)≤5。

现在反设 |X|=80。由 |H|≤50、|R|≤b+5=30，两侧必为50、30。对任意最小横截 Z，Y=R\Z 无 B5、R6、weak7，故 |Y|≤25；因此 |Z|≥5。结合上界：

\[
|Z|=5,\qquad |Y|=25,\qquad
\operatorname{End}_{R5}(Y)\cap\operatorname{Src}_{B4}(Y)=\varnothing. \tag{1}
\]

最后一条来自残余 R，不能把 Y 当任意满756后删除该条件。

### 3.3 零缺额封闭与全部纯 H 尾

[R20 §5](RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md) 的参数化论证给：ambient R6 不可能两端都在 H；H-origin R6 的不同实际终点注入 H 的 neutral 点，后者至多 d=2b−|H|；同时 R 中不是 ambient R6 源的点至多2d。证明使用固定实际终点下降和旧三链，覆盖内部经过 R 的全部路径，不局限于 H 内部路径。

d=0 时得到

\[
S=R,\quad |S|=30,\qquad \text{任何 H 点都不启动 ambient R6}. \tag{2}
\]

对每个 v∈R，实际 H+v 有51点；若无 R6，它是超过 C50 的766。因此必有 R6，且由(2)只能始于 v，其余五点全在 H。**每条** H+v 内 R6 都如此，终点可随替代路径变化。反序同理得到 |T6|=30、H′=X\T6 是满50，并有全部纯 H′ 前供。

## 4. 同一五根的全部 private 家族与端点定位

对同一个最小 Z、每个 z∈Z，保留完整家族

\[
\mathcal P_z=\{P\subseteq Y+z:P\text{ 为实际 R6}\},\qquad
\mathcal Q_z=\{Q\subseteq H+z:Q\text{ 为实际 R6}\}.
\]

二者都非空。Pz 非空来自最小横截的 private-path 性质：否则 Z\{z} 已命中全部 R6。每条 Pz 恰遇 Z 于 z，起初不能限定 z 的位置。每条 Qz 由(2)始于 z。两条只共享 z，不因此共享可拼接 pair。遇多个 Z 点的路径、混合 H/Y 路径以及所有替代 private 路径仍是 ambient 约束，不因以上显示 singleton 家族而消失。

可以特别选择 endpoint 横截以得到可靠定位。

* |E|=5：取 Z=E。任意 P∈P_ei 的终点属于 E，又只遇 E 于 ei，故它必终于 ei；五根全部定位。
* |E|=6：取 Z=E\{e2}。对 z∈{e3,e4,e5,e6}，private 路径不能终于 e2，因为该路径就必须始于 e1，会多遇一个 Z 点；也不能终于别的 Z 点。因此这四根全部定位。z=e1 的 private 路径可能终于 e1 或 e2，不能擅自删除后一分支。

这只是所选合法 endpoint 横截的性质，不 endpointize 任意最小横截的全部路径。

对任一已定位根 z、任一 P∈Pz，记其末前驱 u；任一 Q∈Qz，记第二点 h，则 u<z<h，且

\[
\chi(u,z,h)=B. \tag{3}
\]

若红，把 h 追加 P 即得 R7；也可把 u 前接 Q。这个单点追加确实只新增一个连续三元组。结论对所有同 z 替代选择成立，但仅给 B3，不给 B6 或同端点 weak7。

另一个全称 fan 事实是：任意实际 R6 从 a 到 b，则对每个实际 a<x<b，

\[
\chi(a,x,b)=R. \tag{4}
\]

否则 B3(a,x,b) 与该 R6 同端点构成 weak7；x 可以不在原路径上。

## 5. 三条有序不交 H 红五点路径：参数无关引理及完整证明

先把数值代入之前的旧机制抽出。**参数无关支持引理。** 设 X 是完整有序 signotope，无 B6、R7、weak7；H、R 是 X 的两个不交实际子集。假设 R 内没有同时结束 R5、开始 B4 的点，τ_R6(R)=5，并且对每个 r∈R 至少有一条实际 R6(r,H^5)。则 H 含三条实际 R5 路径 A<B<C，即 A 的所有点早于 B 的所有点，B 的所有点早于 C 的所有点。这里不要求 |H|=50、|R|=30，也不调用满容量目录；结论由旧 R7/R20/R21 机制抽出，未证其排除任何尚存临界接口。

**右根与五/六终点。** 令 E=End_R6(R)。若 e∈E 启动 R 内 B3(e,u,v)，取一条终于 e 的 R6，末前驱为 p。χ(p,e,u) 若红则追加 u 得 R7，故必蓝；于是 B4(p,e,u,v) 从一个内部 R5 终点 p 出发，违反残余 role 条件。所以每个 e 都是右红根：以 e 为首点、后两点在 R 的三元组全红。特别 E 全红，|E|≤6；E 命中所有 R6，τ=5 又给 |E|≥5。

若 |E|=6，写 e1<⋯<e6。任一终于 e2 的 R6 首点 a 若在 e1 之后，右根 e1 可前接成 R7。若 a<e1，weak7 迫 χ(a,e1,e2)=R，而 E 是红链，所以 (a,e1,…,e6) 是 R7。故只能 a=e1。于是 Z=E\{e2} 命中全部 R6，大小5，按 τ=5 是最小横截。若 |E|=5，则 Z=E 自身就是最小横截。两种情形的全部 private 路径均存在，且具有第4节证明的端点定位；该证明只用这里已列假设。

**全部替代尾的末间隙屏障。** 复用 [R20 §6.3](RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md) 的论证：若 R 中实际 R6 的末对为 u<z，任何从 u 启动的 ambient R6 都终于 ≤z。否则设其终点 h>z，为免原 R6 追加 h 成 R7，χ(u,z,h) 必蓝；但 B3(u,z,h) 又与第二条 R6 同端点，构成 weak7。

由引理假设，u 至少有一条纯 H 尾 R6(u,H^5)。其末点在 H，不等于 z∈R，故整个五点 H 支持都在 (u,z) 内；而且 u 的每条纯 H 尾均如此。z 的任何纯 H 尾则全在 z 之后。这是真实按序分离，不是给每根分配独占容量。

**|E|=5 的证明。** 取 Z=E，选一条终于 e1 的 private R6，末前驱为 u。u 的 H 尾给 A⊂(u,e1)。再说明旧 [R21 §2.4](RESET_R21_GLOBAL_CAPACITY_AND_SUPPLY_REALIZABILITY.md) 的实际 R6(a,e1,…,e5) 如何得到：选 e2-private 路径，首点 a 避 e1；若 a>e1，右根 e1 可前接成 R7，所以 a<e1。χ(a,e1,e2) 若蓝，则与 a→e2 的 R6 同端点成 weak7，故为红。E 自身是红链，因此 (a,e1,…,e5) 是实际 R6。其末对 e4<e5 迫 e4 的 H 尾 B⊂(e4,e5)。最后 e5 的 H 尾给 C⊂(e5,∞)。于是 A<B<C，三条支持不交。

**|E|=6 的证明。** 取 Z=E\{e2}，选终于 e3 的 private R6，末前驱为 u；其 H 尾给 A⊂(u,e3)。E 自身是实际 R6，末对 e5<e6 迫 e5 的 H 尾 B⊂(e5,e6)。e6 的 H 尾给 C⊂(e6,∞)。同样 A<B<C。

两种 endpoint 情形已穷尽，参数无关引理得证。canonical 等号情形由第3节供应该引理的全部假设，再代 b25 即得 H50+R30 的实际支持推论。这个推论由旧 R7/R20/R21 机制在同一实际 X 组合得到；形式上，它当然排除不具该支持结构的嵌入，但本轮没有证明它移除了此前仍存活的完整临界参数/接口类，不记为新硬排除或突破，也不给数值收益。

最后的三块闭合尝试仍失败。无 R6 使 A 的末 pair 与 B 的首 pair 形成 B4，也使 B 的末 pair 与 C 的首 pair 形成另一个 B4；两次使用的中间 pair 不同。要拼成 B6，需在 B 中找到同一实际 x<y，同时满足

\[
\chi(\operatorname{last}A,x,y)=B,\qquad
\chi(x,y,\operatorname{first}C)=B.
\]

前述两个 B4 不保证这一共同 pair。Through14 也不自动补上：R5 首点是源、末点是终，均不因此拥有源终双角色；这里没有得到14个不同的实际 through 点。

## 6. 共同嵌入的继承参数范围与两个共享 P 的满25核

### 6.1 同母体身份和旧换点定理

置

\[
I=S\cap T_6,\quad |I|=5+q,\quad
P=S\setminus T_6,\quad Q=T_6\setminus S,\quad
D=X\setminus(S\cup T_6).
\]

本节局部 Q 是实际点集 T6\S，不是第2节的全局数量 Q=N767。于是 |P|=|Q|=25−q、|D|=25+q，H=Q⊔D、H′=P⊔D。旧 R21/R24 已给1≤q≤10；历史 R21 的 b26/n83 数字不直接搬来，本文用其一般 b 论证代 b25/n80。

在 H 内重算 K=Src_R5(H)、E_H=End_B5(H)、L=Src_B5(H)、F_H=End_R5(H)，各25，K⊔E_H=L⊔F_H=H；H′ 对应加撇。令 m=|K∩F_H|、m′=|K′∩F′_H|。

[R25 §3](RESET_R25_GLOBAL_EXTREMAL_STRUCTURE_AND_JOINT_REALIZABILITY.md) 的旧实际换点定理是

\[
S\cap\operatorname{End}_{R5}(X)\cap\operatorname{Src}_{B5}(X)=\varnothing, \tag{5}
\]

并有反序对偶。其关键不是人口估算：假设 a 有这三个角色，旧三链迫从 a 的每条 R6 终点与每条 B5 的第二点为同一 b；纯 H 尾给 b∈H。实际换点 H_a=(H\{b})+a 仍无 R6，且 a 无内部 B5。满50分划于是迫内部 R5 终于 a；其末前驱 h 与 B5(a,b,…) 的 joining 为免 B6 必红，追加 b 得从旧 H 启动的 ambient R6，违反(2)。这就是旧定理的合法交换及全替代封闭，不是本轮新排除。

令 J=P∩Src_B5(X)、j=|J|，J_T=Q∩End_B5(X)、t=|J_T|。删 ambient 全部 B5 源/终得到实际757≤40，且每核内部蓝源/终各25，故 j,t≥15。又 J⊆K′ 且由(5)避 F′_H，因此 j≤25−m′；对偶 t≤25−m。

Joint17 的继承研究层下界 m,m′≥9 与旧 R25 上界≤10 联用，得到

\[
m,m'\in\{9,10\},\qquad j,t\in\{15,16\}. \tag{6}
\]

j16 迫 m′9，m′10 迫 j15；另一方向对偶。这个组合已经隐含在旧结果中，不是本轮又排除了 m11..13。独立 H50 的继承研究范围仍是9≤m≤13；(6) 额外使用共同嵌入 X80。q1..10 仍未被整体排除。

### 6.2 Y 的终点计数和 common-P 身份

所选 endpoint 横截 Z⊆E⊆I。T6 的任何点都不能启动 ambient B5：入 R6 与出 B5 在根处的 joining，红给 R7、蓝给 B6。因此 J 避 Z，且 J⊆Y。由(5)，

\[
\operatorname{End}_{R5}(Y)\subseteq Y\setminus J.
\]

删全部内部 R5 终点后无 B5、R5，经典容量 C(4,4)=20 给下界5。因此

\[
5\le|\operatorname{End}_{R5}(Y)|\le25-j\le10; \tag{7}
\]

j16 时上界9。R30 本身的红五点终集 V 只有10≤|V|≤30−j≤15，不能与(7) 重复收费。没有证明 Y 有11个红五点终点，也没有证明(7) 上端取等。

旧 R21/R25 给 U_D=Src_R5(D)、V_D=End_R5(D)，各 q，以及实际核心身份

\[
\boxed{Y=P\sqcup(I\setminus Z),\qquad K'=P\sqcup U_D.} \tag{8}
\]

二者各25、无 B5/R6/weak7，交集恰 P、大小25−q；两种不同 q 点补全属于同一个 X。K′ 是 H′ 的内部红五点源核心，Y 还带(1) 的残余 role 禁配。它们不是可自由交换的抽象 owners。

若 j+m′=25，则 J=K′\F′_H，U_D⊆F′_H，并且

\[
K'\cap F'_H=(P\setminus J)\sqcup U_D.
\]

Y 中红五点终点的可能容器是 (P\J)⊔(I\Z)，同样大小 m′；尚未证明实际终点填满它。若 j+m′<25，在(6) 范围只差1，不能套用上述等号身份。

### 6.3 common-P 并集的完整 mixed-path 定位

主会话随后明确抽出以下实际路径定位；它仍是数学生成及旧身份的组合，不是独立审阅或合法交换成功。令

\[
A_0=I\setminus Z,\qquad B_0=U_D,\qquad
\mathcal U=Y\cup K'=P\sqcup A_0\sqcup B_0.
\]

|A0|=|B0|=q≥1。定义完整实际家族

\[
\mathcal B=\{B\subseteq\mathcal U:B\text{ 是实际 B5}\},\qquad
\mathcal R=\{R_6\subseteq\mathcal U:R_6\text{ 是实际 R6}\}.
\]

每条 B5 或 R6 都必须同时遇 A0、B0：若避 A0 就全在 K′，若避 B0 就全在 Y，均违反这两个满756核的内部禁形。因此它们恰是两个核各自不能单独看见的 mixed-path 家族。

S=P⊔I 不能结束 ambient B5，T6 不能开始 ambient B5，而 A0⊆S∩T6、B0⊆D。因此每条 B∈B 的终点只能在 B0，其 A0 点全部是内部点。对红色，D 不能开始或结束 ambient R6，故每条 R6∈R 的 B0 点全部内部；终点属于 T6，在 U 内又必须避 D 和 P=S\T6，所以只能终于 A0。即

\[
\operatorname{last}(B)\in B_0,\quad B\cap A_0\text{ 全部内部};
\qquad
\operatorname{last}(R_6)\in A_0,\quad R_6\cap B_0\text{ 全部内部}. \tag{9}
\]

式中每条路径均同时遇两个补全部分，路径内部仍可使用任意允许的 P/owners，所有替代见证保留。

若 A0<B0，则 R6 必在其内部 B0 点之后终于 A0，不可能，故 U 无 R6；若 B0<A0，B5 必在其内部 A0 点之后终于 B0，不可能，故 U 无 B5。这仅各消除一种 mixed 违例；|U|=25+q，容量会迫另一种存在，不能据此把 U 宣称为756或得到矛盾。

更精确地，令 v=min(A0∪B0)。若 v∈A0，K′+v 有26点；容量迫 B5 或 R6，且它必须用 v。R6 须终于 v，同时还须用更早的内部 B0 点，但 B0 全晚于 v，故不可能。因此 K′+v 必有 B5，其中 v 是内部点，终点在 B0。若 v∈B0，Y+v 同理有26点；B5 若存在须终于 v 且用更早的内部 A0 点，不可能，所以必有 R6，其中 v 内部，终点在 A0。

这不是最早点矛盾：P 可以有更早的实际点，承载这些路径的首部。该定位尚未排任何此前存活的完整临界接口/参数类；真正未解的是这些带强制终点/内部位置的完整家族，如何与 H 和全部五根扩展共同兼容。

### 6.4 实际蓝源配置的进一步供应为何仍未闭合

旧 R25 给 W_B=Src_B5(X)=L⊔J，现有40或41点；它是内部重算的实际766，并且

\[
\operatorname{Src}_{R5}(W_B)=J,\qquad
\operatorname{End}_{R5}(W_B)=M_-,
\]

有两满25核 L、L′。所以每个 j∈J 都有内部 R5 后供终于某 z∈M−。从这样的 z 出发的任一 ambient B5，其第二点属于 T6：入 R5 的末前驱若蓝连接则给 B6，故连接红，追加这个第二点成 R6，由 ambient 终点身份定位。由于 z∈L，可以选择 H 内部 B5；对**每条这样的 H 内部供应**，其第二点 q0 同时属于 H，故 q0∈H∩T6=Q。W_B 的 j→z 红五点路径因此对全部这些 H 内部蓝后供延长成 j→q0 红六点路径。

这里前提是 **z 有入 R5**，而第二点进一步属于 Q 还必须保留 **H 内部供应** 限定。一般 ambient B5 的第二点可能在 I，不一定在 Q；也不能误写成“从任意 j 出发的 B5 第二点都在 Q”。尝试用这些同 j 供应迫 End_R5(Y)∩Src_B4(Y) 非空，或迫 J 中某点结束 ambient R5，均未成功。J 内可以迫 R4，但 R4 比旧三链所需入 R5 少一点；W_B 红供可能在内部使用其他 J owners，未必与 private Y+z 供应共享实际 pair。没有新的共同端点或 mixed bridge 定理。

## 7. 紧核缺角：漏掉的第二个三元组与修复后结论

本节暂在独立满50的766配置中工作，不与上一节的767母体混淆。沿上一主稿，四原子 L,D_H,T_R,T_B 满足 |T_R|=|T_B|=m、|L|=|D_H|=k=25−m，继承研究范围 m9..13、k12..16。H_B 是 Y_B=X\T_B 内全部实际 B5 的 L×D_H 端点图；内部可使用 L、D_H 点，图有完美匹配。

取实际边(l,d)不属于任何完美匹配，及任意见证 B5 路径 P。标准 Hall 障碍给紧集 U，l∉U、d∈N(U)、|N(U)|=|U|。实际诱导核

\[
W=U\cup T_R\cup(D_H\setminus N(U))
\]

有25点且无 B5。容量对 W+l、W+d 迫完整非空家族

\[
Q:l\to d',\quad d'\in D_H\setminus N(U),\quad Q\subseteq W+l;
\]
\[
R:l'\to d,\quad l'\in U,\quad R\subseteq W+d.
\]

全部路径都 endpoint-localized；否则给缺角(l′,d′)的实际边。原 P 的内部点可能不在 W，不能擅自使用。Q、R 若有三个位于(l′,d′)的共同内部点，旧同端 packet gluing 给 W 内 B5，矛盾；共同 pair 只给允许存在的 B4。

现在显式增加条件：Q、R 共享 x<y，P=(l,x,z,y,d)，且 z∈W。候选(l′,x,z,y,d′)在 W 内，中间三元组蓝；定义

\[
\alpha=\chi(l',x,z),\qquad \gamma=\chi(z,y,d').
\]

W 无 B5 恰迫

\[
\alpha=R\quad\text{或}\quad\gamma=R. \tag{10}
\]

若 α红，packet(l′,x,z,y)为合法 RBBB；若 γ红，packet(x,z,y,d′)为合法 BBBR。局部合法不表示已构造完整 X50。

原被撤回的 cap6 推法声称：左端 l<l′<x、Q=(l,x,q3,q4,d′)时，α红使 packet(l,l′,x,z)迫 χ(l,l′,x)=B，于是插入 l′ 得 B6。**错误是插入新增两个连续三元组**，还要 χ(l′,x,q3)=B。旧 Q 只保证原三元组蓝，不保证这一 mixed triple。

修正结论是，对每条具有所述首 pair 的实际 Q，

\[
\alpha=R\Longrightarrow\chi(l',x,q_3)=R. \tag{11}
\]

否则两个新三元组都蓝才真有 B6。同理，若 y<d′<d、R=(l′,r2,r3,y,d)，则 γ红先迫 χ(y,d′,d)=B；插入 d′ 的另一个新三元组未定，no B6 给

\[
\gamma=R\Longrightarrow\chi(r_3,y,d')=R \tag{12}
\]

对全部相应尾 pair 的替代 R 成立。容量不自动迫这些首/末 pair 位置条件；不存在“下一点必是 W 中立即邻点”的已证结论。

若另有实际蓝证据关闭(11)、(12)两侧，才由(10)得缺角矛盾；本轮未迫这种全族碰撞。最直接的共享支持闭合，如 Q=(l,x,y,q,d′)、R=(l′,r,x,y,d)，已沿共同连续边 x,y 拼成 B6(l′,r,x,y,q,d′)，其四个连续三元组依次来自 R、R、Q、Q，属于旧可靠拼接，不是新三路径定理。另一路共同第三点也回到旧 B5 禁角。

因此本轮没有证明所有实际端点边可延拓，没有迫第三个共同点，也没有新增完整临界子类排除。旧完整扇的双严格 Hall ⇒每条实际载体内部 e=|L≥x|+|D_H≤y|≥2 仍成立，e0 双紧、e1 两 slack 的完整二分仍沿用；但没有迫每个临界母体出现 e≤1 载体。即使未来每条边均可延拓，也不能跳过这个支持密度入口而宣布 C49。

## 8. MUS：完整同时修复、rollback 障碍与下降停点

这里回到767母体。角色赋值是 K⊔Y；每条实际 R6 必同时遇 K、Y，每条实际 B5 必遇 K。F 是按完整路径要求计的包含极小不可满足族，红路径两个要求捆绑。这个任意临界赋值不自动等于 canonical H/R/Z 分划。

取 F 中蓝 Q，固定满足 F\{Q} 的同一赋值 σ，故 Q⊆Y。固定 q∈Q，取完整阻挡族

\[
\mathcal A_q=\{A\in F:A\text{ 红},\ A\cap Y=\{q\}\}.
\]

取其五点 K-traces 的包含极小横截 S。翻 q 到 K、S 到 Y 后，旧 all-K 阻挡已全修复；精确新违例族是

\[
\mathcal V(S)=\{T\in F:q\notin T,\ \varnothing\ne T\cap K\subseteq S\}. \tag{13}
\]

它非空，但不保证 singleton。每个 x∈S 有不同的 private 红 A_x，A_x∩Y={q}、A_x∩S={x}。对任意 T∈V(S)，A_x∩T={x} 若 x∈T，否则交集空。两边共享的唯一原 Y 点 q 被 T 避开，故这确为完整路径交集，不仅是 trace 交。

**失败一：最小化违例数不能自动下降。** 在极小横截中选 |V(S)| 最小只定义了有限最优值；没有构造另一个横截并比较其完整违例族，不能推出值1。F 的极小不可满足性虽保证删指定 T 后另有满足赋值，但那个赋值未必保留 σ 的 q/S/private 支持，不能当作本次修复的下一状态。

**失败二：恢复 S 的点会重开旧阻挡。** 保持 q∈K，若非空 U⊆S 翻回 K，则每个 u∈U 的 A_u 都变成全 K，因为其唯一原 Y 点 q 已在 K、唯一 S 点 u 又回 K。这重开至少 |U| 条不同的完整红要求。只恢复 S 点不能满足 F；但可能同时修掉更多 exits，因此也不能反推总违例数必不减或过程无环。

**失败三：招募原 Y 点要同时处理两完整族。** 保持 S 在 Y，取 U⊆Y\{q} 全翻到 K，置 P0={q}∪U，则

\[
K^*=(K\setminus S)\cup P_0,\qquad
Y^*=(Y\setminus P_0)\cup S.
\]

逐条检查完整路径的全部原 K/Y 点，精确 all-K 红违例族为

\[
\mathcal K(P_0,S)=\{A\in F:A\text{ 红},\ A\cap Y\subseteq P_0,
\ A\cap K\cap S=\varnothing\}, \tag{14}
\]

精确 all-Y 红或蓝违例族为

\[
\mathcal Y(P_0,S)=\{T\in F:T\cap K\subseteq S,\ T\cap P_0=\varnothing\}. \tag{15}
\]

证明就是核对每个原 K 点是否留 K、每个原 Y 点是否已被招募。(15)不含 Q，因为 q∈Q∩P0；其余原路径均有非空 K-trace，因此(15)正是 V(S)中避 U 的子族。两族穷尽全部违例。U 命中所有 V(S)足以修复全部 all-Y exits，却不排(14)：其中可以有多个原 Y 点均在 P0 的红路径，它们不属 A_q，原横截 S 未必命中。没有证明同时使(14)、(15)为空的实际 U，也没有严格下降量。

实际几何信息仍有(4)全端点 fan，以及第5节末 pair 的全终点屏障和其反序式；它们对每个 private 红路径与红 exit 同时成立。但 singleton 交点未必是屏障所需端点/末前驱，fan 不自动给插入所需全部连续三元组。本轮没有迫两族中的冲突 fan，蓝 exits 也未被删除。

纯红 MUS 时，可删红 Q 后交换两角色使 Q⊆Y，沿用同一全阻挡及修复框架；但没有蓝 seed 的反色交集预算，纯红 MUS 仍开放。旧 z≤5 横截基线不变，没有 z≤4、没有更小支持横截，也没有 MUS descent 定理。

另一个 canonical 条件试验准确显示 mixed splice 的阻挡。若实际 private 路径有朝向 P_t=(t,y1,…,y5)全红，t<h1<y1，且 h1 是同 t 的 H 尾首点，则无 H-origin R6 迫 χ(h1,y1,y2)=B；packet(t,h1,y1,y2)又给 χ(t,h1,y1)=χ(t,h1,y2)=R。它是有效条件交叉颜色式，但最后的蓝三元组恰阻止朴素红 splice，不给禁形。不能假定所有 private 路径都从 t 开始。

## 9. 量词、旧新归属与未实现状态

| 明确候选或断言 | 正确量词与本轮结算 |
|---|---|
| 排 H50+R30 | 对每个实际 X80 及其 canonical 分解；未证明 |
| 三有序 R5 支持 | 每个该 X80 都有 A<B<C⊆H；由旧工具导出，完整证明见第5节；没有已识别仍存活整类被新增排除 |
| 同 z 蓝桥与间隙尾 | 对所选 endpoint 横截已定位根的全部 private 路径、全部 H 尾；不能转为任意最小 Z 全 endpoint 化 |
| 所有实际边可延拓 | 对满50两诱导端点图的每条实际边；未证明；紧核三路径闭合失败 |
| cap6 gate 修复 | 仅在第7节显式次序/首末 pair 条件下，对全部相应替代见证成立；不是无条件缺角排除 |
| MUS 严格下降 | 需同一实际赋值、完整 V(S)及(14)—(15)；未证明；纯红支未排 |
| m,m′9/10 与 j,t15/16 | 旧 R25 共同嵌入上界与旧 Joint17 下界的组合，不重计新排除 |
| Y 与 K′ 的 common-P 补全 | 两个实际满25核心同时存在于反设母体；不意味着任意中间交换合法或二者并集避长路径 |
| common-P 完整 mixed 家族定位 | 全部 mixed B5 终于 B0、A0 点内部；全部 mixed R6 终于 A0、B0 点内部；最早补全点只迫相应一种违例，不给矛盾 |

没有把抽象支持系统、局部合法 packet、独立核人口式或尚未排除的参数行当实际临界反例。三有序 R5 也不是 H50 存在性证明。j/t、q/w、不同横截的成本、同一 δ 和不同供应次数均未相加为独占资源。

停止处是具体的：同根仅交一点不能替代同实际 pair；pair-only 插入必须检查两个新连续三元组；rollback 或另取临界赋值不能替代完整同时修复。两个共享 P 的满25核把问题集中到同一实际母体，但本轮未获得将分别存在的全族供应接到同一实际外端点的定理。

## 10. 文档边界与唯一剩余问题

[来源清单](../../../../tmp/n7_h50_r30_joint_20261029/SOURCE_MANIFEST.json) 保留主稿写入前有限明确来源与保护入口的 bytes/SHA256，并记录本轮 A 分支经主会话确认修订后的最终源字节；主会话另提供参数无关引理及 mixed 并集定位的定稿指示。[机械文档检查](../../../../tmp/n7_h50_r30_joint_20261029/DOCUMENT_CHECK.json) 只查路径、链接、重复文件名和这些有限源/保护入口的字节。这不是数学、科学、形式证明或独立审阅，不按旧 hash 恢复任何来源。执行者仅新建本主稿和该新回执目录，没有改写任何来源；历史正文、task 元数据、接受/assurance、配置、任务指针、证据和运行均未修改，没有提交或归档。全部新增仍 unreviewed/unaccepted；本轮科学检查0、外部审阅0。

最后只保留一个具体问题：**在同一实际 X80 中，两个共享 P 的满25核 Y=P⊔A0、K′=P⊔B0 的完整 mixed B5/R6 家族，连同 H 及同一个五点 Z 的全部扩展，能否强迫产生严格容量节省的合法重分划，或同一对实际外端点的 weak7？** 这里 A0=I\Z、B0=U_D，U 中全部 mixed B5 必终于 B0 且 A0 点内部，全部 mixed R6 必终于 A0 且 B0 点内部；最早补全点试验仍允许更早的 P 点，不给矛盾。具体未控的是与 H 交织、可经过多个不同 owners、可遇多个 Z 点且不全包含于任何一个已知核的所有实际路径。严格合法重分划须对这全部路径保证新 H 无 R6、残余侧无 B5 及所需红路径横截/role 条件；同端 weak7 则须在这些共同支持上落实同一实际首末点和长度和9，分别存在的供应仍不够。这个共同实现问题在本轮没有解答。

当前仍为 **40/50/80/81**，没有新全局上界。
