# N7：共同中性 through 点的残余增广与完整 MUS 支持排除

日期：2026-10-29，新一轮理论推进。本稿由主会话 Astra 确定数学结论后，文档执行者忠实整理授权生成分支及其实际旧依赖。全部新增数学 **unreviewed/unaccepted**。主会话和生成协作者的推导、依赖核对与交叉质询不是独立数学审阅。科学检查、研究代码、枚举、solver、proof checker、证明重放均为 **0**；外部审阅、独立审阅均为 **0**，没有调用 Claude 或请求导出。

本轮确实得到两个限定范围的支持排除：canonical H 取满2b时，实际残余增广给出 |R|+w≤b+5，从而共同等号 X_(3b+5) 必有 w=0，排除此前仍开放的整个 w≥1 共同实现类；完整 MUS 中，五点红横截的唯一 private 红路径还受到新的实际支持禁形。二者都没有排除所有 X80，w=0 仍开放；当前全局链保持 **40/50/80/81**，不宣称 C49、Q79 或 F777≤80。

## 1. 来源、当前证据与模型边界

本轮三条来源为 [A：joint role 与实际残余增广，最终强化见§8](N7_BRANCH_A_JOINT_ROLE_EQUALITY_RIGIDITY_20261029.md)、[B：满756状态与实际 attainment 的支持分析，最终范围见§14](N7_BRANCH_B_FULL756_STATE_ATTAINMENT_RIGIDITY_20261029.md)、[C：完整 MUS 的 unique-private 支持排除](N7_BRANCH_C_COMPLETE_MUS_SUPPORT_REDUCTION_20261029.md)。B 为 A 提供证明接口与状态范围支持，不是独立数值界路线。[上一轮共同饱和主稿](N7_H50_R30_COMMON_SATURATION_AND_FULL_SUPPORT_BARRIERS_20261029.md) 及其全部历史文件保持只读；其中曾留下的 U_D 蓝终点可能性由本轮新证明进一步排除，不回写历史。

工作模型是完整有序 rank-3 signotope：实际三元组恰着红 R 或蓝 B；每个 a<b<c<d 的 packet 按 abc、abd、acd、bcd 排列，至多换色一次。单色 k 路径有 k 个严格递增的实际顶点，全部连续三元组同色。packet 首尾同色迫全包同色，给同色路径的子序列遗传。weak7 是同一对实际首末点的反色路径，长度和达到9，可保端点缩短，不要求内部不交。

767 母体 X 禁 B6、R7、weak7；766 配置禁 B6、R6、weak7；756 配置禁 B5、R6、weak7。b 始终是756及其换色对偶的有效共同上界，不是“极大规模恰为b”的断言。先证明参数化结果，最后取 b=25。

[当前 cardinality-layer theorem](../../09-03-35-state-cardinality-charging/research/cardinality-layer-theorem.md) 与 [C8 人工正式验收](../../09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md) 记录限定完整模型中 C1—C10 全部 accepted、pending 空、N≤25。该人工接受保留 same-family/provisional assurance，exact reviewer backend/model/actual effort 未报告、不可验证；它不证明无条件几何界，也不证明25点实际存在。旧 C7/C9/C10 的历史数字和原依赖图不重写。

旧结构草稿、固定证书/公式检查、全类语义迁移与正式/独立接受分别记账。[Through14 固定字节 strict-RUP](../../../../tmp/balanced49_abstract_port_20261026/through14_replay_result.json)、[Joint17 公式绑定](../../../../tmp/balanced49_remaining_hr_20261027/joint17_binding/result.json)、[Joint17 完整 strict-RUP](../../../../tmp/n7_global_proof_completion_20261027/joint17/result.json) 保留原 PASS 范围，其全类语义迁移仍未独审、未接受；本轮没有重放。独立 H50 的 m9..13、共同 X80 的 m,m′9/10 和 j,t15/16 仅沿用其研究层级，不由本轮升级。

[Closure schema 结果](../../../../tmp/n7_global_proof_completion_20261027/closure/result.json) 虽 PASS，但 actual_cnf_equality_checked=false、UNSAT_checked=false；[获取停止回执](../../../../tmp/n7_global_proof_completion_20261027/closure_acquisition/abort_receipt.json) 为 ABORTED_BUDGET_FEASIBILITY、source_acquisition_complete=false、CNF_binding=false。Closure 未闭合，不能登记 C≤49。

## 2. 参数化 canonical 入口：只要求 H 取满2b

本节及第3—5节只假设：X 是实际767配置；b 是上述有效容量，继承 C7≤2b 和残余 D7≤b+5；X 的 [R7 §2—3 canonical 分解](RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md) 为

\[
X=H\sqcup R,\quad H=P_-\cup G,\quad R=P_+\setminus G,
\qquad |H|=2b. \tag{1}
\]

这里固定同一全局点对次序 λ，p(v) 是最小关联对的另一端点，P+={v:p(v)>v}、P−={v:p(v)<v}；G 为 P+ 内同时结束 R5、开始 B4 的点。H 是实际766；R 无 B5，内部无 End_R5(R)∩Src_B4(R)。

关键 fan 的量词是：**任一 ambient 蓝路径，只要末点 v 在 P+，就能追加 p(v)；前面的实际顶点可以任意来自 X。** 任一从 P− 启动的 ambient 红路径可前接 p(首点)。不能把它缩成 P+ 内部路径的结论。

定义全 ambient 红六点源终

\[
S=\operatorname{Src}_{R6}(X),\qquad T_6=\operatorname{End}_{R6}(X),
\qquad D=X\setminus(S\cup T_6).
\]

[R20 §5.2—5.6](RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md) 以 d=2b−|H|=0 给出

\[
S=R,\quad\text{没有 H 点启动任何 ambient R6},
\quad\forall r\in R\ \exists R6(r,H^5). \tag{2}
\]

最后一条也可在封闭后直接兑现：H+r 有2b+1点，若无 R6 就超过766上界；路径只能从 r 启动，其余五点全在 H。所有替代路径保留，终点可不同。R20 的封闭来自 ambient 两端论证、固定实际终点下降到 neutral 点和实际 H∪U 容量，不仅仅是“H 内无 R6”。

现在在 **D 内部重算**

\[
U_D=\operatorname{Src}_{R5}(D),\quad V_D=\operatorname{End}_{R5}(D),
\quad C_D=U_D\cap V_D,\quad w=|C_D|. \tag{3}
\]

C_D 是实际内部 D 红五点 through 集，不是满50的 through 原子，不是补集 D\(U_D∪V_D)，也不是任意 ambient 红五点 through 集。D 依定义既不含 ambient R6 源，也不含 ambient R6 终点。本节不假设反向核 H′ 满、不设 q/j 人口，也不假设 j+m′=b。

## 3. 旧 mixed-role 换点定理在这个较宽范围仍成立

先说明满2b的内部 cover。若 Z 是实际766且 |Z|=2b，令 L_Z=Src_B5(Z)、F_Z=End_R5(Z)。两者不交：入 R5 与出 B5 在同一点的 joining 红则给 R6，蓝则给 B6。Z\L_Z 无 B5、R6，大小≤b；Z\F_Z 换色后同样≤b。因此两端集各至少 b，互不交且总人口2b，故

\[
\operatorname{Src}_{B5}(Z)\sqcup\operatorname{End}_{R5}(Z)=Z. \tag{4}
\]

**引理：** 在(1)—(2)下，

\[
S\cap\operatorname{End}_{R5}(X)\cap\operatorname{Src}_{B5}(X)
=\varnothing. \tag{5}
\]

这是 [R25 §3.2、3.4](RESET_R25_GLOBAL_EXTREMAL_STRUCTURE_AND_JOINT_REALIZABILITY.md) 的旧实际交换机制，以下完整保留其不依赖 |R| 的原因。

假设 a 有三个角色，固定一条入 R5 终于 a。任取一条从 a 出发、终于 h 的 R6，及一条第二点为 c 的出 B5。旧 R7 三链引理说，若 c≠h，则有 B6 或 weak7，矛盾。固定任一出蓝路径遍历全部出红路径，再反向固定，得到所有出 R6 的终点与所有出 B5 的第二点都是同一实际 h。由(2)可选纯 H 尾，故 h∈H。

实际换点 Z_a=(H\{h})∪{a}，大小2b。其 R6 不可能从旧 H 点启动，也不可能从 a 启动，因为那会要求已删除的终点 h。因此 Z_a 是766。a 也不启动内部 B5，因为每条 ambient B5 从 a 出发都以 h 为第二点。内部重算(4)迫 Z_a 内有 R5 终于 a，前四点全在旧 H，末前驱记 u。

取任意 ambient B5(a,h,…)。χ(u,a,h) 若蓝，可前接 u 得 B6；故它红。把 h 追加刚才内部 R5，得到从旧 H 启动的 ambient R6，违反(2)。引理得证。

该证明只用满 H、纯 H 尾、封闭、旧三链与新核内部重算，**没有使用满 H′、X80人口或 j 数值**。前接/追加各检查一个新连续三元组；没有采用未经验证的插入。它是旧定理的适用范围核对，不计新独立接受。

## 4. 全路径蓝扩展与三个 ambient 角色排斥

### 4.1 S∪U_D 不含 ambient B5 终点

若 s∈S 结束 B5，取其任一出 R6。设蓝末前驱为 r、红第二点为 u。χ(r,s,u) 蓝则蓝路径追加 u 得 B6，红则红路径前接 r 得 R7。故 s 不可能结束 ambient B5。

若 v∈U_D，选实际 D 内 R5(v,u,u2,u3,d)。若有 ambient B5 终于 v，末前驱为 r，则 χ(r,v,u) 蓝给 B6；红把 r 前接该 D 红五点路径，得到终于 d∈D 的 ambient R6，违反 D∩T6=∅。所以

\[
(S\cup U_D)\cap\operatorname{End}_{B5}(X)=\varnothing. \tag{6}
\]

### 4.2 V_D 不含 ambient B5 源

若 v∈V_D，取 D 内入 R5(d1,d2,d3,r,v)。若 v 启动 ambient B5(v,u,…)：joining χ(r,v,u) 红则原 R5 追加 u 得从 D 启动的 ambient R6，违反 D∩S=∅；蓝则把 r 前接蓝路径得 B6。因此

\[
V_D\cap\operatorname{Src}_{B5}(X)=\varnothing. \tag{7}
\]

这些结论同时覆盖全部 incoming/outgoing 替代供应，没有给不同路径分配独占资源。

### 4.3 末点在 S∪U_D 的每条 ambient B4 都能延长成 B5

若末点 s∈S=R⊆P+，无论 B4 的前三个点属于哪里，R7 unrestricted fan 都允许追加 p(s)，保留原源点。这正是本轮不能遗漏的 ambient 量词；路径可以混用 D、S 和任意五横截点。

若末点 v∈U_D，取任意 D 红五点后供(v,u,u2,u3,d)，记蓝四点路径末前驱为 r。χ(r,v,u) 若红，则(r,v,u,u2,u3,d)是终于 D 的 R6，不可能；故该 joining 蓝，追加 u 得 B5。于是

\[
\forall\text{实际 B4，若末点在 }S\cup U_D,
\quad\text{它可保首点延长为 ambient B5}. \tag{8}
\]

这不是说延长后的整条 B5 仍在 S∪U_D；论证只需要首点成为 ambient 蓝五点源。

## 5. 主定理：实际残余增广及参数化共同容量

**定理。** 在第2节的假设下，

\[
\boxed{|R|+w\le b+5,\qquad |X|\le3b+5-w.} \tag{9}
\]

**证明。** 取实际诱导集

\[
W^*=S\sqcup C_D.
\]

由 C_D⊆U_D 与(6)，它的任何顶点都不能结束 ambient B5，所以 W* 无 B5。若一条内部 B4 从 v 启动，其末点在 W*⊆S∪U_D，由(8)，v 是 ambient B5 源。

若 v∈C_D⊆V_D，这与(7)冲突。若 v∈S，则(5)使 v 不可能结束 ambient R5，因而也不能结束内部 R5。于是

\[
\operatorname{End}_{R5}(W^*)\cap\operatorname{Src}_{B4}(W^*)
=\varnothing. \tag{10}
\]

W* 还遗传 no weak7、no R7。这正是旧 R7 残余 D7 的完整假设：无 B5、无 weak7、内部无 R5终/B4源共点。由旧 D7≤b+5，|W*|=|S|+w=|R|+w≤b+5；再加 |H|=2b 得(9)。证毕。

这里检查了 W* 的**每条实际内部路径**。S 整批纳入，没有删掉五点最小横截 Z，没有只保 private 路径，也没有丢弃遇多个 Z 点或混用 C_D/S 的路径。不同 owners 可共享供应，证明仍成立。它也不调用满756的某一 e 目录、点态收费或跨核状态对应。

为使旧容量调用自足，D7≤b+5 的机制如下。对任一该残余配置 W，令 E=End_R6(W)。若 e∈E 启动内部 B3(e,u,v)，取入 R6 的末前驱 r；χ(r,e,u) 红给 R7，蓝给从内部 R5 终点 r 启动的 B4，违反 role 禁配。因此每个 e 都是右红根，E 是红链，|E|≤6。若≤5，删除 E 即横截全部 R6。若 E={e1<⋯<e6}，每条终于 e2 的 R6 必始于 e1：首点晚于 e1 可前接右根 e1 得 R7；首点 a<e1 时，同端 R6+B3 禁形迫 χ(a,e1,e2)=R，进而(a,e1,…,e6)为 R7。故删 E\{e2} 五点已命中所有 R6。删后是756，规模≤b，得到 |W|≤b+5。此处 weak 的实际端点、红7帽和残余 role 都有作用，不能把一般无 B5 配置当 D7。

**共同等号推论。** 若 |X|=3b+5，则旧 canonical 上界 |H|≤2b、|R|≤b+5 迫 |H|=2b、|R|=b+5；(9)因此迫

\[
\boxed{C_D=\varnothing,\quad w=0.} \tag{11}
\]

取 b25，任何 X80 都必须满足 U_D∩V_D=∅。这覆盖全部 q、全部 role-equality 状态及所有替代路径，**不要求 j+m′=25**。本轮因此排除整个此前仍存活的 w≥1 共同实现类，而不是只排某个 private 模板。

条件式本身还说：canonical H50 且 w≥1 的配置满足 |X|≤80−w≤79。但未证明每个候选 w≥1；反而任何等号候选已被迫 w0。因此没有无条件 Q≤79。它也不排独立 H50，C≤50 不变；当 H 未取满2b时，不把(9)当一般缺额定理使用。

## 6. X80 中的两个 common-P 满核与真正剩余供应

本节才追加共同等号假设并取 b25。沿旧 R21/R25，|S|=|T6|=30、H=X\S、H′=X\T6，各50；定义

\[
I=S\cap T_6,\quad |I|=5+q,\quad
P=S\setminus T_6,\quad Q_{\mathrm{side}}=T_6\setminus S,
\quad |P|=|Q_{\mathrm{side}}|=25-q,\quad |D|=25+q.
\]

旧范围1≤q≤10、|U_D|=|V_D|=q。本稿 Q_side 是实际点集，全局数值 Q=N767 另记；C_D 始终只表示(3)的内部 through 集，旧源中 C0 的其他含义不混用。

在 H′ 内重算 K′=Src_R5(H′)、F′=End_R5(H′)、L′=Src_B5(H′)、E′=End_B5(H′)，各25，K′⊔E′=L′⊔F′=H′。令 m′=|K′∩F′|，m 为 H 的相应红 through 数；J=P∩Src_B5(X)、j=|J|，反向蓝终需求为 J_T、t。继承共同范围 m,m′∈{9,10}、j,t∈{15,16}，旧 j+m′≤25、t+m≤25 不重新认领。

canonical endpoint 五横截 Z⊆I，|Z|=5。令

\[
A_0=I\setminus Z,\quad B_0=U_D,\quad
Y=P\sqcup A_0,\quad K'=P\sqcup B_0,
\quad\mathcal U=P\sqcup A_0\sqcup B_0. \tag{12}
\]

两个核 Y、K′各25，|A0|=|B0|=q，交集恰 P。由(6)，整个 U 无 B5：它每个点都在 S∪U_D，没有任何 ambient 蓝五点终点。这比上一轮“mixed B5 只能终于 B0”的定位严格更强；上一轮历史稿不改写。

U 的每条 R6 必同时遇 A0、B0，否则包含在一个756核。它只能终于 A0，所有 B0 点都内部，因为 P 避 T6、D 无红六点源终。容量迫：对每个 a∈A0，K′+a 有 R6、终于 a；对每个 b0∈B0，Y+b0 有 R6、b0内部、终于某 A0。所有替代和多A0/多B0路径均保留。U 本身有 R6，不是756，不能套35态容量目录。

删 A0 或 B0 都截全部 R6，给横截上界q；任何横截删后为756，|U|=25+q迫至少删q。因此 τ_R6(U)=q。定义实际 incidence 图 G：a—b0 为边，当且仅当 U 中有 R6 终于 a 且含 b0。对 A⊆A0，(A0\A)∪N_G(A)横截全部 R6，故

\[
q-|A|+|N_G(A)|\ge q.
\]

Hall 给完美匹配，每条匹配 incidence 有 b0<a。按实际顺序列 b1<⋯<bq、a1<⋯<aq，得到 bi<ai；否则前i个 A0 点不可能有i个更早 B0 邻点。等价地每个 cut 上 #A0前缀≤#B0前缀。这不是内部不交路径族，不是 R6首末点匹配，也不保证 matched b0 对 rank attainment 必不可少。

在主 equality j+m′=25 中，旧身份给 J=K′\F′、U_D⊆F′。再加本轮 w0 与 L=Src_B5(H)=D\V_D，得到

\[
U_D\subseteq F'\cap L=M_- . \tag{13}
\]

这些点在 H′ 有入红五点供应，在 D 有出红五点供应，在 H 还启动蓝五点。对 z∈M−，任一 ambient B5 的第二点只保证属于 T6；选 **H 内部** B5 才进一步落入 Q_side。不得省去这个限定。主 equality 的 w0 分支仍未排；也没有新定理 j+m′<25。

## 7. B 的支持作用：状态等号不能伪造逐点刚性

### 7.1 满25只有两个计数相等

对实际756核 V，accepted theorem 的25 ordinary/10 exceptional目录与精确状态单射给

\[
|V|=25+e(V)-m_{\mathrm{miss}}(V),\qquad
m_{\mathrm{miss}}(V)\ge e(V). \tag{14}
\]

|V|25 直接给 m_miss=e。实际证明依次是 terminal-pair recurrence 的不同 owner 状态单射、占用态分区的精确恒等式、逐层排 global bad-cell；不是一个逐 owner 非负 slack 之和，也没有 exceptional owner 到指定 ordinary 孔的已证收费单射。在精确恒等式下，标量 m_miss≥e 与 |V|≤25 等价，因此单靠取等没有额外 ownerwise 刚性。

给定同一个染色的 states 唯一，不表示不同诱导核的对应 states 相同。对 v∈P，只能由遗传性得

\[
D_P(v)\subseteq D_Y(v)\cap D_{K'}(v), \tag{15}
\]

不能比较后两者谁包含谁。对于共同 terminal pair u<v∈P，各色最大路径长度 L_c 满足

\[
L_c^P\le L_c^Y\le L_c^P+q,\qquad
L_c^P\le L_c^{K'}\le L_c^P+q,
\qquad |L_c^Y-L_c^{K'}|\le q.
\]

证明是从达到路径删掉至多q个补全点，保留共同末 pair。若 Y 的最大长度严格更大，全部 attaining Y 路径都用 A0；反向同理。一个补全 owner 可同时支撑很多 pairs，不能逐次收费。一个差异 state cell 需要其两色坐标的实际见证并集遇补全点，不表示两条见证各自都遇它。只有早于全部 A0∪B0 的 P 初始段，两个 predecessor 域才相同，从而 states 真相等。

J 的每点都不结束 ambient R5，故在 Y、K′中各落低3×3子目录的20个 ordinary states；exceptional owners 只能在核\J，于主 equality 得 e(Y),e(K′)≤m′。这不固定各核 occupied image，也不把 B0 的 H′-through 身份变成 K′内部 R5 attainment。

旧 [R23 §11.2](RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md) 的状态固定证明有显式共同有限像集、逐 owner 单调性和双射，再由面积总和不变迫每点固定。当前(15)只有从 P 到两核的两个独立增长，缺共同像集和核间单调双射，不能搬用。旧 e0/e7/e8/e10满25例的各自范围沿用，也不能据其独立存在证明这些核嵌入当前 X80。

### 7.2 蓝自由 U 给高度信息，但不属于756目录

U 中每个 a∈A0 有 incoming R6，且 X 无 R7，故 incoming red maximum恰6、对应红高度5。K′ 中每个点不属于 ambient T6，因此其 U-incoming red maximum至多5、红高度≤4；U 无 B5使蓝高度≤3。

所以 U 的 A0 states 已超出旧3×4盒，不能对 U 套35态756 theorem。K′的25个 U-labels仍可单射并落旧盒，其 missing ordinary=exceptional只是25个不同标签的计数恒等式；这些 labels 未必是实际诱导 K′的内部 states，不能把它们当 accepted charging 的另一次实例或共同 catalog。

纯插入确有部分内部 attainment：Y+b0 的 R6 删掉内部 b0，得到 Y 内终于某 a∈A0 的 R5；K′+a 的 R6 删最终 a，得到 K′内终于其末前驱的 R5，末前驱位于 (P\J)∪B0。前者不迫不同 b0 给不同 a，后者不迫末前驱就是 matched b0，甚至不迫它属于 B0。

全路径 Hall 图必须包含多B0/多A0的路径。只保 pure Y+b0 或 K′+a 见证形成较小图后，原横截论证不再自动命中其他 mixed 路径，因此不能声称较小图仍 Hall。即使 q1，b0也可位于红六点路径的较早内部位置，删 a 所得 R5 的终点仍未必 b0。状态比较、全路径 matching和这些 attainment 都支持 A；它们没有构成第二条独立界证明。

## 8. 主线的尝试、修复与准确停止机制

最初残余构造取 W=J⊔I⊔C_D，使用(6)排蓝终点，再由 incoming R6/R5 分别排 I、C_D 上内部 B4 源，J 则由(5)排红终点，得 j+q+w≤b（b25时 I大小5+q）。其反序式也成立；primary equality 中得 q+w≤m′。这是本轮发展中的较弱必要式，不是独立 owner pairing。最终使用 unrestricted canonical fan，把 J⊔I 扩成整个 S，才得到 W* 与所有 w≥1 的排除。w0后旧弱式退化为 J⊆P 等既有计数，不再登记一次额外收费。

| 尝试 | 新增实际输入及所得 | 首个未闭合步骤与处理 |
|---|---|---|
| 同一 B0 点的红前后供 gluing | primary equality 给 H′入 R5 与 D出 R5，full-core纯供可选前供始于J；相邻 joining在 H′内因无R6而蓝 | mixed carrier相邻点未必属于该 supplier pair；把蓝源当蓝终、蓝终当蓝源不能得B6；停止直接角色误接 |
| 全50交换 H*=(H′\B0)∪A0=Y∪E′ | 保留同一实际母体全部颜色 | E′不在 U 内，仍可能有始于P、终于A0、经过E′且避B0的R6；未证明H*是766，不调用其满核cover |
| 对满25等号作逐点收费 | (14)与共同P真实状态增长 | 没有 pointwise slack/固定共同像集/核间单调双射；修复为第7节精确全见证限制 |
| 用单点插入图替换全路径Hall | 每个纯插入确有R6及删点后的内部R5 | 多B0路径仍可能避较小图的“终点横截”；不丢弃这些路径，不声称 matched owner attainment |
| 把W*的C_D扩为全部U_D | equality给U_D的H′红前供，D给红后供 | U_D\V_D已经是ambient B5源；红前供可能从S、纯版本从J开始，红joining可产生从S到I的合法R6，不是禁D-origin；现有同一增广机制不能吸收这些点 |

最后一行是本轮具体停止机制：没有理由把 U_D\V_D 假装仍有 D 内入红五点供应。w0已迫 U_D、V_D不交；主 equality 的 U_D⊆F′没有补出那个内部 D 身份。停止的是这种自动扩大 residual 的推法，不是宣告整个共同实现主线无路可走。

## 9. C：完整 MUS 的五横截与唯一 private 路径

这是一条独立竞争支持结果，不把 MUS 赋值等同 canonical H/R。仍在实际767母体中，F 是按完整路径要求计的包含极小不可满足族：每条红 R6 必同时遇角色 K、Y，每条蓝 B5 必遇 K；红的两个要求捆绑。F_R 表示全部红成员。以下 S_M 是 F_R 的横截，区别于 ambient 红六点源 S。

**引理一：** F_R 无≤4点横截；每个五点横截 S_M 本身是实际蓝 B5，且作为完整路径成员属于 F。

证明：赋 Y=S_M、K=X\S_M。全部红成员遇 Y，且每条有6点、|S_M|≤5，故也遇 K，红要求全满足。蓝成员失败恰当它五点全部在 S_M。≤4点时不可能，矛盾；恰5点时只可能是集合 S_M 本身，故 unsatisfiability迫该蓝成员存在。每个五横截因无四横截而包含极小，每个 s∈S_M 都有 private 红成员。

写 S_M={s1<⋯<s5}，固定 s∈S_M，D_M=S_M\{s}。设 A 是红 private 成员，|A|6、A∩S_M={s}。

**引理二：** A 是 s 的唯一 private 完整红成员，当且仅当对每个 x∈A\{s}，D_M∪{x}仍命中 **全部** F_R。

正向：A被x命中，任何其他红成员若避D_M，就因原横截性也是s-private，与唯一性冲突。反向：任何s-private红成员B都避D_M，于是五个x∈A\{s}全在B；B还含s，六点已满，所以B=A。

在等价条件下，引理一迫六个不同实际蓝成员

\[
Q_x=D_M\cup\{x\}\in F,\qquad x\in A. \tag{16}
\]

x=s 时就是原 S_M，另外五个是全部 replacements。D_M 四点都在 A 外，且是实际 B4。这是完整约束族迫出的共存蓝扩展族，不是随意挑选两条路径。

**引理三：六个分离的临界赋值。** 对每个 x∈A，由 F 的路径级极小不可满足性，存在满足 F\{Qx} 的赋值 σx；它必使 Qx 全在 Yx，否则满足所有 F。其余每个 Qy仍需遇Kx，而共同 D_M全在Yx，所以每个 y∈A\{x}都在Kx。于是

\[
D_M\cup\{x\}\subseteq Y_x,\qquad
A\setminus\{x\}\subseteq K_x. \tag{17}
\]

六份 σx 是分别存在的赋值；它们在 X\(D_M∪A) 上可能完全不同，不能合并成一个共同临界赋值。实际六条蓝路径(16)则属于同一个固定 X。

## 10. C 的实际 packet/weak/cap 支持排除

设 A=(a1<⋯<a6)，a=a1、bA=a6。本节 bA 是路径末点，区别于容量 b。

**定理：** 在第9节唯一 private 假设下，

\[
|D_M\cap(a,b_A)|\le1, \tag{18}
\]

且 D_M 不可能全部位于 a 左侧，也不可能全部位于 bA 右侧。

若 d<e 是 D_M 中两个位于(a,bA)的点，蓝 Q_a 给 χ(a,d,e)=B，蓝 Q_bA 给 χ(d,e,bA)=B；这是 packet(a,d,e,bA)的首尾，故全包蓝。于是 B3(a,d,bA)与实际红六点 A同端，长度和9，构成 weak7，矛盾。

若 bA<d1<d2<d3<d4 是整个 D_M，χ(a5,bA,d1)红会把 d1追加 A 得 R7，故必蓝。Q_bA给 χ(bA,d1,d2)=B，D_M自身后两个连续三元组也蓝。因此(a5,bA,d1,d2,d3,d4)是 B6，矛盾。左侧同理：若 d1<d2<d3<d4<a，noR7迫 χ(d4,a,a2)=B，Q_a给 χ(d3,d4,a)=B，加 D_M前两蓝三元组，得到 B6(d1,d2,d3,d4,a,a2)。两端证明都逐一给出全部连续三元组，是前接/追加，不是漏掉第二个 gate 的插入。

若唯一 private 点 s=s1，D_M 全晚于 s1，而 a≤s1；D_M无点在a左侧。全在bA右侧已排，所以至少一点在(a,bA)，(18)又只许一点，A避D_M保证无端点相等，得到

\[
\boxed{s_2<\max A<s_3.} \tag{19}
\]

反序地，若 s=s5，则

\[
\boxed{s_3<\min A<s_4.} \tag{20}
\]

因此 genuine complete-path MUS 中，“五点红横截、某点恰一条 private 红路径，并且该路径区间含两个其他横截点或把其余四点全放一侧”的整类支持签名被排除；极端点还必须满足(19)—(20)。这次区别于旧修复账本：完整 unsatisfiability确实迫出全部替代蓝路径，packet与同端weak在这些同一实际支持上闭合。

范围仍受限：没有证明每个 MUS 都有五点红横截，也没有证明某横截点必有唯一 private 成员。若每点都有多条 private，(16)不能自动成立；唯一性下仍允许 D_M跨越红端点且内部至多一点的剩余位置。纯红 F 若有≤5点红横截，前述赋值已满足全部红要求，因此其红横截数至少6；这不排所有纯红 MUS。没有下降势函数、没有一般更小横截、没有 z≤4，也没有构造真实 MUS 或临界 X。

## 11. 方法作用、旧新归属和数量结算

| 本轮断言 | 真实覆盖与用途 | 不作的升级 |
|---|---|---|
| 参数化残余增广(9) | 对任意canonical H=2b的767母体，完整W*路径族，C_D为内部D-through | 不要求H′满；不外推H未满的一般缺额式 |
| X80强制w0 | 排全部q/e/role-equality状态的w≥1共同实现类，含所有五Z及multi-Z路径 | 不排w0；不证明j+m′<25、Q79或C49 |
| common-P蓝自由及incidence Hall | 完整mixed路径图、τ=q、匹配b0<a和prefix domination | 不等于路径内部不交、private图Hall或state transport |
| 满25状态等号分析 | m_miss=e、实际共同P遗传比较、纯插入内部attainment | 不存在已证pointwise charge或跨核state equality；B不是独立界路线 |
| C unique-private禁支持 | 完整F_R横截与真正F蓝成员，六个分离临界赋值，实际packet/weak/cap排除 | 不排一般MUS、纯红MUS，不降z |

A 的新实质是找到严格符合旧 D7 定义的**更大实际集合**，使容量对其全部路径兑现。旧三链、canonical fan、满核 cover、残余五横截均是旧工具；新结论来自同时保存实际 D 的两个 supplier 方向和 unrestricted ambient 蓝扩展，不是把人口、路径次数或相同缺额重复相加。packet通过旧canonical/路径遗传与实际供应合法性进入，weak通过旧三链/封闭和D7五横截起作用；不能把(9)说成又接受了一份新证书。

B 的标量分析只审计 accepted theorem 的数学接口。state injection 与 counted equality没有逐点非负松弛；状态 labels 不对应另一个实际诱导核时，也不能越域调用35态定理。全路径matching保留multi-B0所有见证，是正确量词所需，不是额外独占成本。

C 的引理一、二属于完整约束语义，(17)才用 MUS极小性；真正的signotope支持排除在第10节，用实际packet把两条强制蓝扩展接成同端B3，再与红R6构成weak，另以两单色帽排两侧摆放。完整F迫(16)不可省略；任意两条单独路径不满足这个MUS支持定理的前提。六个σx未被合并，所以没有重犯上一轮“修复后自动成为单违例临界态”的错误。

旧三有序R5、完整pair扇、既有m/q范围及旧R25排除均只沿用。没有实际X50/X80新构造或反例，没有文献范围原创声明；一组满足旧标量式但被新式排除的形式参数，不当作曾实现的signotope。所有本轮证明仍未独审、未接受。

旧工作链

\[
N_{757}\le a+b-1,\quad C\le2b,\quad Q\le C+b+5,
\quad F_{777}=Q+1
\]

仍代 a16、b25 得40/50/80/81。新**条件**loss=w与全局新界分开：w≥1整类已排，但w0允许等号。全局直接数值下降、递推下降、新外部界收益均为0，旧accepted输入的传播不重计；没有新全局上界。

## 12. 文件边界与唯一下一问题

[来源清单](../../../../tmp/n7_neutral_through_20261029/SOURCE_MANIFEST.json) 固定本轮有限明确读源和保护入口的当前bytes/SHA256；[机械文档检查](../../../../tmp/n7_neutral_through_20261029/DOCUMENT_CHECK.json) 仅核路径/链接/UTF-8/公式标号及有限字节。它不是数学、科学、形式证明或独立审阅，不按旧hash恢复来源。执行者只新建本主稿和本轮新回执目录；此前主稿、分支、回执、task入口/状态、接受/assurance、配置、指针、sealed证据与运行均未改写，没有Git mutation、提交或归档。requested native Sol/high是执行角色记录，不据此自动验证实际backend/effort。

最后只保留一个问题：**在已经被迫 w=0 的同一 X80 中，进一步取尚存主等号 j+m′=25，U_D∩V_D=∅ 而 U_D⊆F′，其完整入红五点、出红五点、蓝供应以及全部 mixed R6 的共同兼容，能否迫真实禁形或严格合法重分划？** 具体未控的是 U_D\V_D上的 H′入供与D出供、经过E′及多个A0/B0/Z的完整红六点家族；前者的红joining仍可能始于S，后者不能从全路径Hall中删除。必须在同一实际颜色和端点上兑现所有路径约束，不能仅把U_D换名为已有C_D或把H′-through运输成K′内部attainment。这个w0共同实现问题本轮仍未解。

全部新增 **unreviewed/unaccepted**；科学检查0、外部审阅0。当前仍为 **40/50/80/81**，没有新全局上界。
