# N7：锁端口吸收、Ω端点兑现与完整约束族重分划

日期：2026-11-01。状态：**工作证明；全部新增 unreviewed/unaccepted，未独立审阅、未接受**。本文仅忠实转写主会话批准的参数结构与完整证明。主会话及生成协作者的推导、交叉核查属于同会话生成核对，不是独立review。指定native gpt-6.1-sol/high文档执行者只负责转写和文档一致性，不自行补证或认定接受状态。

本轮主线给出锁端口吸收整类排除定理，并以最早Ω源、实际中间匹配与可延长端点兑现其完整接口。η=o∈{1,2}时进一步还原饱和角色族，明确排除高端点人口及满足迟端点/可延长判据的具体Ω类。竞争路线给完整F的前缀不足重分划定理，覆盖singleton外供的全部交错位置。正错位四点交核主攻仍未闭合，无条件工作界不变：

\[
N_{\rm sig}(7,6,7)\le3b+3,\qquad
N_{\rm sig}(7,7,7)\le3b+4.
\tag{1}
\]

所有新排除都带其实际供应、延长与匹配接口，不能把端口在人口式中直接抹去，也不能声称全部η≤2已经覆盖。全部新结构及重分划不重复计数值saving。

唯一新增文件为本文及 `tmp/n7_locked_port_absorption_20261101/DOCUMENT_CHECK.json`。旧稿、task.json、metadata、指针、接受/assurance、运行、CNF、proof、runtime保持，不提交、不归档。未调用外部Claude、未向外发送研究材料，未执行研究代码、枚举、SAT、solver或证明器；PowerShell仅作文档操作和检查。

## 1. 模型、完整角色与主要依赖

完整有序rank-3 signotope的四点packet按abc、abd、acd、bcd至多换色一次。路径按实际顶点计长，由连续三元组同色判定，且对子序列遗传。weak7比较同一对实际首末点的反色路径，长度和至少9，内部可共享。

767禁R7、B6、weak7；756禁R6、B5、weak7，其换色模型禁R5、B6、weak7，共同有效容量为b。766禁R6、B6、weak7，容量≤2b。D7无B5、无weak7且内部End_R5∩Src_B4为空，容量≤b+5、红六横截数≤5。N_sig为最大允许人口容量，不是强迫阈值。

本轮在n=3b+3的下一层研究。由已证全模型工作式n+w≤3b+3先得w=0。定义全部ambient角色与实际中性区

\[
S=\operatorname{Src}_{R6}(X),\quad T=\operatorname{End}_{R6}(X),\quad
I=S\cap T,\quad P=S\setminus T,\quad Q=T\setminus S,
\quad D=X\setminus(S\cup T),\quad
U=\operatorname{Src}_{R5}(D),\quad V=\operatorname{End}_{R5}(D),
\quad U\cap V=\varnothing.
\tag{2}
\]

Src、End在注明的实际点集内计算；ambient表示母体X。所有中间图保留相应点集的全部实际R5端点边，删点按实际点计，不要求不同路径内部不交。

主要依赖均保持原保证层级：

- [最新Hall增广与零through闭合稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_HALL_DEFECT_ROOT_AUGMENTATION_AND_ZERO_THROUGH_CLOSURE_20261101.md>) §1—5：完整外锁、实际Hall增广根、双full与onefull/δ0闭合、一般η≤2归一化；§6为正错位四点交核与F+/E+刚性。
- [加权稳定性稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7879_INTERFACE_AUDIT_AND_WEIGHTED_THROUGH_STABILITY_20261031.md>) §3—8：实际换核、完整port、跨核根扇、全模型加权定理及实际尾替换。
- [78/79参数工作界稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_DEFECT_ONE_PREDECESSOR_COMPRESSION_AND_GLOBAL_BOUND_20261031.md>)：完整临界排除与工作上界。
- [纯核与完整private重分划稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_PURE_CORE_ROOT_SEPARATION_AND_INTERLEAVED_REPARTITION_20261030.md>) §6.1—6.4，尤其§6.2：竞争路线的完整背景、旧位置引理与全部所需交错颜色；本轮不冒称重新证明旧位置引理。
- [联合neutral原稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_TIGHT_CUT_JOINT_NEUTRAL_AND_REPARTITION_DICHOTOMY_20261029.md>) §1—2、[旧through稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_JOINT_THROUGH_SATURATION_AND_ORDERED_CUTS_20261030.md>) §3：三链、联合预算和一般实际归一化。
- [R20精确关系](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>) §0—4：已证合法chart删根与实际反向添点给精确+1。

反fullstandard特指H'=X∖T满2b且其完整mixed禁形、蓝四延长与全ambient角色已兑现，不能用任意满766子集替代。正向有效W⊂S的完整外锁为：r∈W∩End_R5(X)若启动ambient B5，其第二点在T∖W。这个锁点也不在U⊂D。

## 2. 锁端口吸收整类排除工作定理

### 2.1 完整参数接口与实际锁源

假设反向H'=X∖T真实fullstandard，|H'|=2b、|T|=b+3，满角色为Z'=Src_R5(H')=P⊔U，|Z'|=b。令u=|U|，则|D|=b+u。

正向有实际有效D7 W=S∖L，L⊂I为全部所删端口，δ=|L|，W有b+h点，h∈{4,5}，并有上述完整外锁和蓝四延长。置

\[
E=\operatorname{End}_{R6}(W),\ e=|E|\ge h,\qquad
F=\operatorname{Src}_{R6}(T),\ f=|F|\ge3,
\quad q=u+\delta,\quad |I|=u+h+\delta=q+h.
\tag{3}
\]

假设存在δ个实际点组成A⊂W∩P，及双射λ:A→L，每a有ambient入R5和B5(a,λ(a),…)。取该入红五的末前驱joining，桥蓝会给B6，所以桥红，得到末pair(a,λ(a))的实际R6。因此

\[
\chi(a,\lambda(a),z)=B\quad\text{对全部ambient }z>\lambda(a).
\tag{4}
\]

这是新增A→L外边的真实全ambient蓝fan，不是仅在人口中增添δ个位置。

另假设有实际R5中间图，将全部U⊔A匹配到某V†⊂D，覆盖q个源点；路径只须实际，不要求D内部或内部不交。在T∪V†上须已兑现与旧反外图相同的完整延长、junction、根域接口，全部反邻位于I且避F，反匹配至多漏V†的两个点。

**锁端口吸收工作定理。** 上述全部实际接口共同成立时，该临界类不可实现。反序亦然。中间覆盖与反侧完整接口是明确假设，不能宣称所有η≤2自动满足。

### 2.2 原Hall根在吸收后仍有效

原W外图的源层为U，保留全部W∪U内good蓝四第二点，bad为孤点，实际匹配亏损d至多5−h。完整Hall删除证明将bad与Hall只合计损失5−h，不分别再扣。

任Hall子集B⊂U，令Y=(W∖N(B))∪B。最新稿§2已证明Y为实际D7，E_Y=End_R6(Y)属于(W∩T)∖N(B)，且是整个原W∪U的右红根；全部原邻边均避E_Y，不丢原匹配。新增A→L也避E_Y，因为E_Y⊂W而L∩W为空；新增目标L不与原目标W∩T相撞，源A又与U不交。

反full纯前供同时给F<E及F<E_Y。具体地，Z'=P⊔U⊂W∪U，因为L⊂T不含P。任f0∈F，取T内出R6第二点t∈T∩Src_R5(X)，反mixed使t无ambient B5终点。Z'+t有b+1点、无B5，756容量迫R6(p0,z1,z2,z3,z4,t)，前五点全在Z'、p0∈P。

原首pair帽及同端weak迫p0>f0。若p0>e0，e0为E或E_Y中任何根，则完整右根前接e0到前五点产生终于Z'⊂H'的R6，矛盾；p0=e0因P∩I为空排除。因此

\[
F<E,\qquad F<E_Y.
\tag{5}
\]

### 2.3 用actual锁源恢复δ个端口

原左外匹配覆盖u−d点，加入A→L后覆盖q−d点；中间覆盖q点；反侧至多漏两个V†点。因此可复合至少q−d−2条完整链。每链a0→r→v→b0若a0<b0，左蓝fan与反侧全ambient蓝fan给B4(r,a0,b0,v)，与中间实际R5(r→v)同端weak矛盾，所以b0≤a0。

取cut maxF并使用严格根分离，任合法ℓ条完整链给

\[
e+f+\ell\le|I|=q+h;
\quad\text{若使用增广根，改为 }e_Y+f+\ell\le q+h.
\tag{6}
\]

必须先计数排除小q，再正式使用这些链数。

h=5时d=0，原普通Hall覆盖全部U，目标(W∩T)∖E有u+5−e点，故e≤5，结合e≥5得e=5。F<E先给q+5≥8，即q≥3。正式取ℓ=q−2，(6)得e+f≤7，与≥8矛盾。

h=4时若原左亏一，Hall给B使def=|B|−|N(B)|=1，Y满b+5，e_Y≥5。F<E_Y先给q+4≥8，即q≥4；原左u−1加A恢复δ后，中间覆盖q，右最多漏二，取ℓ=q−3，得e_Y+f≤7，与≥8矛盾。因此原左必须覆盖全部U。

此时目标u+4−e≥u迫e=4。F<E先给q+4≥7，即q≥3，正式取ℓ=q−2，得e+f≤6，与≥7矛盾。h=4、5两类均排除，完成定理。

本证明用actual锁定源和实际匹配恢复所删端口，没有在人口式中直接删去δ，也没有使用负链数。

## 3. Ω最早源兑现中间图与可延长端点

### 3.1 一般η1/2归一化与最早源

沿最新稿§5的一般实际换核，正向η∈{1,2}，H*为2b−η点766，R*=X∖H*，新Ω=Ω*⊂R*∩T，M*允许非空，且|M*|+|Ω|≤η。全部H*-origin R6终点在Ω；这些源有ambient入R5、出B5，三链将各源的全部红六终点与蓝五第二点锁到唯一Ω点。

令A_H=H*∩S、L=Ω∩S、δ=|L|≥1，W=S∖L为旧有效D7，|W|=b+h，h∈{4,5}，完整外锁已兑现。反向仍fullstandard。

对每ω∈L，在全部H*-origin R6终于ω的路径中选择最早源a_ω。不同ω对应不同源，因为固定源的任意一条B5第二点只能锁到一个实际点。每a_ω启动B5，故不在T，属于P∩W。

\[
A_\delta=\{a_\omega:\omega\in L\},\quad |A_\delta|=\delta,
\qquad A_\delta\cap C_H=\varnothing,
\quad C_H=\operatorname{End}_{R5}(H^*).
\tag{7}
\]

若a_ω∈C_H，取H*内入a_ω红五末前驱，接B5(a_ω,ω,…)；蓝桥给B6，红桥产生比a_ω更早的H*-origin R6终于ω，两色均矛盾。故(7)成立。每a_ω已有§2所需入R5、锁ω的B5及实际红六末pair。

所选a_ω-origin且终于ω的红六只用于最早性；锁边蓝fan来自另一次ambient入a_ω红五与B5(a_ω,ω,…)的joining，所得另一条实际R6才有末pair(a_ω,ω)。不能直接把原a_ω-origin红六的末pair视为(a_ω,ω)。

### 3.2 不需满核的actual中间覆盖

取D0=D⊔A_δ⊂H*∩H'。反满角色Src_R5(H')=P⊔U使Src_R5(D0)⊂U⊔A_δ。删除D0全部实际源后无R5，换色756容量又给源数≥|D0|−b=u+δ，所以

\[
\operatorname{Src}_{R5}(D_0)=U\sqcup A_\delta,
\qquad V^\dagger=\operatorname{End}_{R5}(D_0)\subseteq C_H\cap D,
\quad V\subseteq V^\dagger.
\tag{8}
\]

端点不会在所选最早源中，由(7)排除。若中间最大匹配<u+δ，König删至多u+δ−1个端点对应实际点，D0余至少b+1点且无R5，矛盾。所以actual中间匹配覆盖全部U⊔A_δ。这里不要求V†恰有u+δ点，更不要求K先满b。路径允许经过D0中已纳入的A_H点、允许内部共享，不影响实际端点与同端weak比较。

### 3.3 迟端点的完整反侧兑现

若每个新端点z∈V†∖V都大于maxΩ，则z无ambient B5源。取H*内入z红五，接其假设的出B5第二点t；蓝桥给B6，红桥给H*-origin R6终于t，只能t∈Ω，但t>z>maxΩ不可能。

任ambient B4(z,t,x,y)也可用H*内入z红五末前驱向左延长：红桥会造终于t>maxΩ的H*-origin R6，所以桥必须蓝，保末pair延为B5。T、旧V处的延长沿旧证明成立。因此T∪V†无B5，其内部反向junction只在V†。

具体地，T上的反junction将内部B4延为B5；与出R5 joining先迫倒数第二点属于S。该点若在D，身份矛盾；若在T，则被full反mixed排除。删所有反good后为反序D7，base T有b+3点，bad数≤2；对全部good邻域作实际删点，Hall缺额与bad合计至多二，反匹配最多漏V†两点。

所有反邻在I：joining产生首pair为该邻点与端点的R6，邻点成为S；它又在T∪V†，而V†⊂D，所以必须在I。

F的完整左根须在新域T∪V†重证。若有B3(x,y,f0)在该域，取T内部出f0红六首pair(f0,t)。χ(y,f0,t)红可前接y成R7，所以蓝，得到B4(x,y,f0,t)。利用刚证明的整个新域左延，保留末pair延成ambient B5，其末pair(f0,t)都在T；t又启动ambient R5，违反完整反port。因此F在整个T∪V†为左红根。原反邻带有该域内相反蓝三，故全部避F。于是§2全部接口实际兑现，整个迟端点类排除。

该兑现不要求M*=0，包含η2单Ω残余M*的情形。迟端点条件不是自动成立，不能据此称所有删端口机制关闭。

### 3.4 可延长端点判据与准确未覆盖类型

称新端点z为可延长端点，指z无ambient B5源，且每个ambient B4(z,t,x,y)均能保留末pair向左延成ambient B5。令R(z)为全部D0内实际R5终于z的起点族，非空且R(z)⊂U⊔A_δ。下列任一条件足够：

\[
R(z)\cap U\ne\varnothing;\qquad
|R(z)\cap A_\delta|\ge2;\qquad
\exists a\in R(z)\cap A_\delta:\ z>\lambda(a).
\tag{9}
\]

若有U入供，潜在B5第二点或B4左延红桥将造从U启动的ambient R6，违U⊂D。若有两个不同A_δ入供，红桥终点必须同时等于两个不同锁端，潜在B5不可能；对任B4也至少可选一个锁端不同于其第二点的入供，迫蓝桥完成左延。若z>λ(a)，其后第二点t>z不可能等λ(a)，同理两项性质成立。

只要完整中间图在旧V及这些已证可延长新端点上仍有覆盖U⊔A_δ的匹配，就可调用§2吸收；不要求所有V†都可延长。特别地，全部新端点满足(9)即可。

未满足该充分判据的新端点必有R(z)={a}且a<z<λ(a)，左不等式来自实际R5(a→z)，即“早且独占来源”。R(z)收集的是D0内全部入供源，不是ambient全部入供源。这只描述当前未覆盖类型，不断言其实际不可延长或已经存在。开放问题是完整覆盖匹配能否避开这类端点，或这类端点能否与满对核共同实现。

## 4. η=o的角色饱和与具体全族覆盖

### 4.1 全部最早源占满neutral缺额

现额外设η=o=|Ω|∈{1,2}。对每个Ω点取全部H*-origin入供中的最早源，组成A0，|A0|=η。令C_H=End_R5(H*)、B_H=Src_B5(H*)。二者不交，由核内R5/B5 joining排R6或B6；删除角色的容量分别给|C_H|、|B_H|≥b−η。

A0不在C_H，由§3.1最早性证明；也不在B_H，因为其蓝五第二点锁Ω在H*外，不能是核内B5源。η个neutral占满全部缺额，所以

\[
H^*=C_H\sqcup B_H\sqcup A_0,
\qquad |C_H|=|B_H|=b-\eta.
\tag{10}
\]

全部A_H都不在B_H。η=1时a=|A_H|∈{1,2}，除a0外的A_H均在C_H；η=2时a=o=2，A_H=A0。因此统一|C_H∩A_H|=a−η。

K=C_H⊔A0有b点。H*内部无R6；K点若有ambient B5，其第二点必在Ω：C_H用核内入R5 joining，A0用唯一锁。因此Ω在K外，K内部无B5，K为实际满b的756核。

### 4.2 角色包含及正确人口式

定义Q_H=Q∖(Ω∖S)=Q∩H*，不能把仍留在Ω中的未删端点当作Q_H。若ζ∈(Q_H∪V)∖C_H，ζ不在A0，且无ambient B5源。K+ζ⊂H*无R6；K的潜在B5第二点都锁Ω在外，ζ也不能启动B5，所以仍无B5，大小b+1矛盾。故Q_H⊔V⊂C_H。

反full给|P|=b−u，人口恒等式为

\[
|Q|=b-u-a-\delta,\qquad
|Q_H|=b-u-a-\eta,\qquad
|C_H\cap A_H|=a-\eta.
\tag{11}
\]

由H*=D⊔Q_H⊔A_H及(10)计算

\[
|C_H\cap D|
=(b-\eta)-(b-u-a-\eta)-(a-\eta)=u+\eta.
\tag{12}
\]

所以V⊂C_H∩D、u≤v=|V|≤u+η，Z=(C_H∩D)∖V至多η点。

### 4.3 全部最早源的perfect及δ<η的正确限制

取D_all=D⊔A0。完整源族为U⊔A0，端点族包含旧V且属于C_H∩D。容量给端点数至少u+η，与(12)上界相等。因此

\[
\operatorname{Src}_{R5}(D_{\rm all})=U\sqcup A_0,
\qquad\operatorname{End}_{R5}(D_{\rm all})=C_H\cap D,
\quad\text{中间图有 }(u+\eta)\text{-perfect}.
\tag{13}
\]

若δ<η，仅保留该匹配中对应U⊔A_δ的中间边，仍覆盖u+δ个所需源，端点仍在C_H∩D。不能把整个端点族硬说成u+δ点。

若Z全部在maxΩ右侧，或者全部满足§3.4可延长判据，反侧图在C_H∩D兑现，吸收定理排整个类。判据中的入供域也可用D_all，A0各源锁端仍不同；不必局限于删端口选源A_δ。

### 4.4 η2单Ω的额外高端点整类

设η=2、Ω={ω}、δ=1。一般归一化给A_H={a}，a为最早源且a∉C_H，允许M*为单点。C_H、B_H各至少b−2，a为neutral又给|C_H|≤b−1，所以|C_H|只能为b−2或b−1。

K=C_H∪{a}⊂H*内部无R6，K上所有潜在B5第二点只可能是H*外的ω，因此K内部也无B5。此时Q_H=Q、|Q|=b−u−3。

若|C_H|=b−1，K满b，K+ζ的容量论证迫Q⊂C_H，从而|C_H∩D|=u+2。若|C_H|=b−2，K有b−1点；Q∖C_H若至少两个点，加到K便得到H*中b+1点、无B5且无R6的配置，矛盾。因此|Q∖C_H|≤1，给|C_H∩D|≤(b−2)−(|Q|−1)=u+2。

始终V⊂C_H∩D，且D0=D∪{a}的端点族V†包含V并在C_H∩D。故v=u+2迫V†=V，原反图直接够用，无新端点延长障碍；§2吸收排除此整类，不要求M0。其他低v尚未整类关闭，§3一般迟端点/可延长端点判据仍适用。

### 4.5 实际闭合类与边界

| 参数机制 | 本轮已兑现的整类排除 |
|---|---|
| η=1、Ω单点、δ=1，高端点v=u+1 | C_H∩D=V无新端点，a=1或2均关闭 |
| 同上低端点v=u | 唯一额外端点z>ω时关闭；可延长判据也适用 |
| η=2、|Ω|=2、δ=1或2，高端点v=u+2 | C_H∩D=V，全部关闭 |
| 同上低端点人口 | 额外一或二点全>maxΩ时关闭；全满足可延长判据也可关闭 |
| η=2单Ω、δ=1，允许M*非空 | v=u+2整类关闭；一般迟/可延长端点条件也适用，其余低v未整类关闭 |

以上是实际覆盖，不是所有Ω机制已闭。§3与本节重合是同一次端口吸收兑现，不能重复认领数值saving。

## 5. 正错位主攻：全ambient压缩、双根域与短桥校准

本节是辅助结构与方法边界，不作为整个错位类的排除。沿最新Hall稿§6的η2 nonΩ/M0接口：E、F各五根，x=e1=f3<a=e2<β=f4<y=e3=f5，P0/Q0各两点，K/K'满b且恰四点交，u=v=q≥1，F+=F、E+=E以及全部受限端口保持。

### 5.1 P0/Q0压缩推广到全部ambient相邻点

P0恰为全部ambient入x或a红六中落在S的末前驱。任这样的p∈S，若p也在T，F根y在T∪V的左根给χ(p,e,y)=R（e∈{x,a}），但原末帽给蓝，矛盾，所以p∈P。

若p∉P0，K+p有b+1点，全部点有ambient End_R5身份。旧稿已得K所有点均无ambient B5源；M0使新p也无ambient B5源，所以K+p无B5，容量迫R6。首点只能在P0∪{p}，每个可能首点r的相应低根帽均迫强制终点≤e_r≤a<y。第四点有End_R5身份，可尾替换到y，与B3(r,e_r,y)同端weak，矛盾。因此没有新p。反序得到Q0恰为全部ambient出β或y红六中落在T的第二点。

### 5.2 两个b+2点域的全部红六与τ=2

定义

\[
Z_-=K'\cup\{a,\beta\},\qquad Z_+=K\cup\{a,\beta\},
\qquad |Z_-|=|Z_+|=b+2.
\tag{14}
\]

Z_-每点都无ambient B5终点且有ambient Src_R5身份，Z_+每点都无ambient B5源且有ambient End_R5身份，故两域均无B5。

Z_-内红六若终于Q0，原首帽迫其首点≥对应f∈{β,y}>x；全部点有Src_R5身份，头替换到x造成同端weak。其他可能终点只能a、β，所以全部红六终于a或β。对偶Z_+全部红六只从a或β启动。

删任一点后仍有b+1点且无B5，容量迫R6；{a,β}又命中全部红六，所以

\[
\tau_{R6}(Z_-)=\tau_{R6}(Z_+)=2.
\tag{15}
\]

由§5.1及旧全ambient受限端口，Z_-终于β的末前驱在U，终于a的末前驱在P0∪U；Z_+始于a的第二点在V，始于β的第二点在Q0∪V。

q=1时删唯一u∈U，Z_-仍有b+1点，迫红六只能终于a，前五点全在P，因为Q0>β>a。反向删唯一v∈V，迫R6(β,Q^5)。这不意味着它们可与原R6(P^4,u,β)、D内R5(u→v)、R6(a,v,Q^4)拼接；q=1仍未排除。

### 5.3 条件实际短桥的两种packet与失败路径

先任选一条pure K'入β红六和一条pure K出a红六，分别记末前驱u、第二点v。旧稿的全ambient限制给u∈U_β∩U、v∈V_a∩V。额外要求**这同一对**u、v有D内R5(u→v)，并满足u<a<β<v；不把任意受限u/v都说成有指定pure供应。

两条实际pure路径写为R6(p1,p2,p3,p4,u,β)、R6(a,v,q2,q3,q4,q5)。两帽给χ(u,a,v)=χ(u,β,v)=B。若packet(u,a,β,v)全蓝，B4与该D内红五同端weak；因此其仅可能为RBBB或BBBR。

在RBBB型，若χ(p4,u,a)=R，packet(p4,u,a,β)全红，再由packet(p3,p4,u,a)首尾红得χ(p3,p4,a)=R，产生实际R6(p1,p2,p3,p4,a,β)。末pair(a,β)落在S，违反β∉E+。故χ(p4,u,a)=B，packet又迫χ(p4,a,β)=R，并有实际B4(p4,u,a,v)。

但是同型packet(a,β,v,q2)=(B,?,R,?)迫末项红，允许实际R6(β,v,q2,q3,q4,q5)。其第二点v不在T，不违反F+刚性。BBBR型的完整反序允许将入β红六末点换成a，末前驱u不在S，不违反E+刚性。这样的平移本身不是矛盾。

新B4虽禁止p4→v红五，但ambient Src_R5(p4)只给某个实际终点，不保证指定终点v的红五。不能把它代替正确同实际端点的供应。u<a<β<v只是本节条件位置，不覆盖所有错位模型。本轮整个正错位分支仍开放，含q=1；以上辅助不计数值收益。

## 6. 完整F竞争定理：右继为源或整个前缀不足

### 6.1 完整参数背景与旧位置引理

设p≥3，完整有序signotope禁B_(p+1)、R_(p+2)及同实际端点R_(p+1)+B3。F保留全部原红R_(p+1)成员和蓝Bp成员；目标K⊔Y=X使每红同时遇K/Y，每蓝遇K。

红横截数为p，全部minimum横截恰是p个不交rank1红块G_i的全部product bases；每块至少2点，每个basis为实际Bp。令G=∪G_i，每个原红H的trace H∩G包含某完整块。

固定恰p点块A={a1<⋯<ap}及basis S0=D_p⊔{s}，|D_p|=p−1、D_p<A、s∈A。该位置全部s-private原红均遇G外，所以全部恰为A⊔{v}，V_p收集完整外供、非空。

依赖[纯核与完整private重分划稿的旧位置引理](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_PURE_CORE_ROOT_SEPARATION_AND_INTERLEAVED_REPARTITION_20261030.md>) §6.2：

\[
v<d^*:=\max D_p<A\quad(v\in V_p),\qquad
V_p\cup\{d^*\}\subseteq\operatorname{Src}_{R_{p+1}}(X).
\tag{16}
\]

旧证明通过d*⊔A红(p+1)及全部外点位置分类给出(16)；本轮不冒称这是新证。

写D_p={d1<⋯<d_(p−1)}，d0=−∞，V_j=V_p∩(d_(j−1),d_j)。因为全部v<d*，这些间隙覆盖V_p。

### 6.2 前缀不足工作定理与完整红约束

**工作定理。** 若每个非空V_j均满足下列二者之一，则Y=D_p∪V_p、K=X∖Y满足完整F：

\[
d_j\in\operatorname{Src}_{R_{p+1}}(X)
\quad\text{或}\quad
j+|\{v\in V_p:v<d_j\}|\le p-1.
\tag{17}
\]

红侧证明针对全部原成员：H若遇D_p就遇Y；否则S0横截迫H为s-private，恰A+v，故遇V_p。又Y∩G=D_p，每块至少2点而D_p在每块至多1点，Y不能含任何整块；trace条件使每个H还遇K。因此完整红约束成立。

### 6.3 全部所需交错颜色及蓝路径形状

令a=ap。由实际红v⊔A与同端weak，v<d时χ(v,d,a)=R，v<w∈V_p时χ(v,w,a)=R。若d<v，则d<v<d*<a，packet(d,v,d*,a)末两项为B、R，迫前两项B，故χ(d,v,a)=B。

据此三类packet给VDD、VDV红与DVD蓝：v<d<e时packet(v,d,e,a)=(?,R,R,B)；v<d<w时packet(v,d,w,a)=(?,R,R,B)；d<v<e时packet(d,v,e,a)=(?,B,B,R)。不声称其他交错颜色都固定。

一般joining禁止Bp终于ambient红(p+1)源：取蓝末前驱与红第二点，桥蓝给B_(p+1)，桥红给R_(p+2)。所以V_p点不能是Bp终点。

若Y有Bp，因D_p仅p−1点必含V点，末点只能d∈D_p。VDD/VDV红迫蓝路径形状

\[
D_L<V_C<d,\qquad D_L\subseteq D_p,\quad
\varnothing\ne V_C\subseteq V_p.
\tag{18}
\]

### 6.4 将最后点降到右继并结算全部前缀

令v*=maxV_C，d_j=σ(v*)≤d。若d_j<d，对任v<w∈V_C，packet(v,w,d_j,d)=(?,B,R,R)迫χ(v,w,d_j)=B；新DVD三元组蓝，全部D三元组蓝，其余继承原蓝路径。因此把末点d换成d_j仍为实际Bp。若d_j=d直接保留原Bp。

d_j若为ambient红(p+1)源，joining已矛盾；否则按(17)，该路径全部落在Y≤d_j，其总人口为

\[
|Y_{\le d_j}|=j+|\{v\in V_p:v<d_j\}|\le p-1,
\tag{19}
\]

不可能承载实际Bp。因此Y无Bp，全部原蓝成员遇K，完整F分划得证。量化的是全部F与全部V_p，不选有利见证。

### 6.5 最右k源推论与singleton全交错闭合

若|V_p|≤k≤p−1，且D_p最右k点d_(p−k),…、d_(p−1)均为ambient红(p+1)源，则完整F可分划。对其他d_j，j≤p−k−1，故j+|V_p<d_j|≤p−1，直接满足(17)。

特别singleton外供的任意交错位置全部关闭，不要求即时右继是红源，因为d*=d_(p−1)自动为红源。

尚未证明任意临界结构进入这些完整F假设或前缀条件，不报告数值saving。

## 7. 方法边界、参数后数字与剩余目录

完整F的mixedcut构造Y_c=T_{≤c}∪S_{>c}始终包含I=S∩T。若I内存在实际R6成员H，则每个Y_c都包含全部H，红约束“同时遇K/Y”在整个构造族上失败。这只是方法界限，不声称已经构造或必存在这样的I，不能把mixedcut当作全覆盖路线。

本轮的参数工作界继续为(1)，全模型带through式继续n+w≤3b+3。最后代入既有用户授权工作输入b=25：

\[
N_{\rm sig}(7,6,7)\le78,\qquad N_{\rm sig}(7,7,7)\le79.
\tag{20}
\]

全局77/78仍未证明。767的w≥1子类才有≤77，777母体只有某个已证合法删根chart的through正数时才有≤78；合法rootcycle在临界人口必有positive through仍未证明。本轮额外无条件数值saving为0；锁端口吸收、η=o人口兑现及完整F重分划不重复相加。b=25证书本轮未重验证、未读取新证书，用户报告UNSAT/证书验证中/旧accepted层级保持。

竞争定理最后代p=5：|V_p|=1全部交错闭合；|V_p|≤2且d3、d4为红六源时完整F可分划；|V_p|≤3且d2、d3、d4为红六源时可分划，依此类推。这些仍是完整F的条件结构结论，没有任意临界进入或新数值上界。

| 类别 | 本轮准确覆盖与剩余 |
|---|---|
| 旧双full及onefull/δ0 | 最新Hall稿已经整类排除，本轮沿用不重计 |
| 锁端口吸收的全部实际接口成立 | §2整类排除；端口通过actual锁源及middle恢复 |
| 一般η1/2的最早源middle | §3已完整兑现；反侧仍需可延长端点或覆盖匹配判据 |
| 迟端点或可延长端点覆盖全部所需源 | §3调用吸收排除，允许M*非空 |
| η=o=1/2高端点及迟/可延长额外端点类 | §4给具体全族覆盖，不代表全部Ω已闭 |
| 早且独占来源的新端点 | 当前充分判据未覆盖；未断言不可延长或实际存在 |
| 一般onefull正δ | 尚可能被早且独占来源端点阻断覆盖匹配；不能称全闭 |
| 双方η≥1的一般混合机制 | 尚未整类闭合，不由onefull吸收自动覆盖 |
| 正错位四点交核，包括q=1 | 仍开放；全ambient压缩/τ2双域/条件短桥仅为辅助 |
| 完整F前缀不足判据及singleton外供 | §6完整分划，尚无任意临界进入 |
| mixedcut全覆盖 | I内红成员可阻断整个构造族；未证明一般完整F闭合 |
| 合法rootcycle临界positive-through | 尚未证明，正through数值下降继续仅属条件子类 |

下一重点是真正的双根满域交换/实际pair换路定理，以及早且独占来源端点的排除或合法端口换基；保留完整F全族的新分划构造。不把“再找一条U_β→V_a红五”或扩根本身当作已兑现出口，也不能把单参数mixedcut当覆盖所有机制。条件短桥的平移或未指定终点的红五源身份都不是主攻矛盾。

## 8. 文档回执与不变状态

全部新增unreviewed/unaccepted。同会话推导、交叉核对及文档`PASS_DOCUMENT_ONLY`均不是独立数学验证。指定native Sol/high只作角色记录，未报告backend或实际effort不作验证结论。

回执路径为 `tmp/n7_locked_port_absorption_20261101/DOCUMENT_CHECK.json`。检查限严格UTF-8、公式号连续唯一、本地链接、参数代入、三份保护稿hash及task.json原hash/status/completedAt、指定两新路径写入。旧稿与task元数据、指针、接受/assurance、运行和科研产物均不变；长期任务仍in_progress、completedAt=null，不提交不归档。
