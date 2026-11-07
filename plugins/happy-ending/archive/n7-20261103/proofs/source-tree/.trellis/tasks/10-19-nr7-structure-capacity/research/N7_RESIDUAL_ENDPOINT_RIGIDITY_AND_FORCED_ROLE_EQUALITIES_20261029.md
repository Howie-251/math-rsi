# N7：残余端点刚性、强制角色等号与完整共同支持

日期：2026-10-29，新一轮理论生成。全部新增数学 **unreviewed/unaccepted**。本稿由主会话 Astra 确定数学及生成协作者核对依赖后，文档执行者忠实整理；这些生成核对不是独立数学审阅。本轮科学检查、代码实验、枚举、SAT、solver、proof checker、证书重放均为0，外部及独立审阅均为0。未调用 Claude、未请求导出，未改变历史、接受、配置、任务状态或运行。

本轮证明共同等号情形中的两个角色预算必须取等，并排除 canonical 残余的整个六端点分支：两方向均恰有五个实际红六点端点/源点。完整第二点支持图满足 Hall，产生另一个实际残余 K′∪E；每个合法40点覆盖的增广点也有有限的次序定位。它们仍未排除五端点、双角色等号的共同实现，不能推出 C49、Q79 或 F777≤80。

## 1. 来源、模型与证据分账

本轮来源为 [A：残余等号与端点](N7_BRANCH_A_RESIDUAL_EQUALITY_ENDPOINTS_20261029.md)、[B：zero-through 后的角色等号](N7_BRANCH_B_ZERO_THROUGH_ROLE_EQUALITY_20261029.md)、[C：成对饱和757覆盖及最终§6](N7_BRANCH_C_PAIRED_SATURATED_757_COVERS_20261029.md)。它们是同一次协作生成的结果，不计作三个独立证明或独立审阅。此前 [neutral-through 主稿](N7_NEUTRAL_THROUGH_RESIDUAL_AUGMENTATION_AND_MUS_SUPPORT_20261029.md) 及 [上一 A 的最终参数化§8](N7_BRANCH_A_JOINT_ROLE_EQUALITY_RIGIDITY_20261029.md) 的 w0 定理继承，不重计本轮新收益。

X 是完整有序 rank-3 signotope：三元组恰着红R或蓝B；四点 a<b<c<d 的 packet 按 abc、abd、acd、bcd 排列，至多换色一次。路径长度计实际顶点，连续三元组同色；packet 给同色路径子序列遗传。weak7 比较同一对实际首末点的反色路径，长度和达到9，不要求内部不交。母体767禁 B6、R7、weak7；766禁 B6、R6、weak7；756禁 B5、R6、weak7；747禁 B4、R7、weak7。所有诱导路径与身份均在指定实际集合内部重算。

a16、b25是当前有效工作上界，不能据此断言极大规模恰等16、25。[当前 cardinality theorem](../../09-03-35-state-cardinality-charging/research/cardinality-layer-theorem.md) 与 [C8 人工接受](../../09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md) 记 C1—C10 全部 accepted、pending空；限定模型上界25保留 same-family/provisional，exact reviewer backend/model/actual effort不可验证。旧结构草稿与该接受层级分开。

[Through14固定字节结果](../../../../tmp/balanced49_abstract_port_20261026/through14_replay_result.json)、[Joint17公式绑定](../../../../tmp/balanced49_remaining_hr_20261027/joint17_binding/result.json)、[Joint17完整strict-RUP结果](../../../../tmp/n7_global_proof_completion_20261027/joint17/result.json) 保留原固定对象PASS范围。全类语义证明分别见 [Through14共同赋值与语义迁移](BALANCED49_COMMON_ASSIGNMENT_AND_REMAINING_H49_BRANCH_20261027.md) 和 [Joint17全缺额联合定理](N7_GLOBAL_DEFICIT_FRAME_AND_JOINT_THEOREM_20261027.md)，仍未独审、未接受，不能仅从PASS回执推出全类范围。m9/10等数字只作继承研究范围的条件推论，不是本轮参数化定理的假设。[Closure结果](../../../../tmp/n7_global_proof_completion_20261027/closure/result.json) 的PASS仅为schema，UNSAT_checked=false、actual_cnf_equality_checked=false；[获取停止](../../../../tmp/n7_global_proof_completion_20261027/closure_acquisition/abort_receipt.json) 仍不完整、CNF_binding=false。没有C49闭合。

## 2. 先定参数化共同等号框架

令 b 是756及其换色对偶的有效容量，使用旧 C7≤2b、D7≤b+5及共同等号结构。反设实际767母体

\[
|X|=3b+5,\quad X=H\sqcup R,\quad |H|=2b,\quad |R|=b+5.
\]

此处是 [R7§2—3](RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md) 的 canonical 分解 H=P−∪G、R=P+\G。其 unrestricted fan 允许**任意 ambient 蓝路径**只要末点在P+就追加p(末点)，不要求其他顶点同侧。[R20§5](RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md) 的零缺额封闭给

\[
S=\operatorname{Src}_{R6}(X)=R,\quad T=\operatorname{End}_{R6}(X),
\quad |S|=|T|=b+5,
\quad H'=X\setminus T,\quad |H'|=2b.
\]

H不能启动任何ambient R6；每个s∈S有纯H尾R6(s,H^5)。反序给H′不能结束ambient R6及相应纯前供。

置 I=S∩T、|I|=5+q，P=S\T、Q0=T\S，|P|=|Q0|=b−q，D=X\(S∪T)、|D|=b+q。Q0是实际点集，区别于全局数量Q=N767。在D内部定义 U_D=Src_R5(D)、V_D=End_R5(D)，各q点。继承上一轮

\[
U_D\cap V_D=\varnothing. \tag{1}
\]

本轮不用重新证明w0，也不把它当作又一次排除。R25同体身份给 K′=Src_R5(H′)=P⊔U_D，F′=End_R5(H′)，L′=Src_B5(H′)、E′=End_B5(H′)，各b，K′⊔E′=L′⊔F′=H′；m′=|K′∩F′|。H的相应红through数记m，蓝源L、红终核心F_H=Q0⊔V_D。J=P∩Src_B5(X)=P∩L′，j=|J|；反向 J_T⊆Q0、t=|J_T|。旧预算仅有j+m′≤b、t+m≤b。

使用 [R23§5](RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md)、[R25§3—7及附录](RESET_R25_GLOBAL_EXTREMAL_STRUCTURE_AND_JOINT_REALIZABILITY.md) 的全部实际供应，先保留下列已证明全称事实。令

\[
W=S\sqcup U_D.
\]

W每点都不是ambient B5终点，故W无B5；每条末点在W的ambient B4都可保首点延长成B5；且

\[
S\cap\operatorname{End}_{R5}(X)\cap\operatorname{Src}_{B5}(X)
=\varnothing. \tag{2}
\]

S终点的B4延长用canonical unrestricted fan；U_D终点则接其D内部R5首后继，红桥会产生终于D的R6，故桥蓝。U_D无B5终点来自同一D后供的两色joining；S无B5终点来自出R6与入B5的joining。(2)是旧满H合法换点：三链迫所有出R6终点与出B5第二点为同一h∈H，换H−h+s后重算满核cover，得到入R5，再接h矛盾。这里不假设供应唯一，也不丢弃multi-U_D路径。

旧D7容量的确切接口是：无B5、无weak7且内部无“R5终点同时为B4源点”的实际诱导配置，规模≤b+5。它不要求该配置本身是某个canonical residual。旧证明由内部R6终集成为≤6右红根、六根时删除第二根以外五点横截全部R6、删后756得到；不是任意无B5配置的容量。

## 3. 完整junction删除与每个u的纯供应

在W内部重算完整集合

\[
G_W=\operatorname{End}_{R5}(W)\cap\operatorname{Src}_{B4}(W).
\]

若某g∈G_W落S，其内部B4可ambient延长成B5，内部R5又使它成为ambient红五点终点，违反(2)。故G_W⊆U_D。删除所有G_W后，任何残留内部junction也会是原W的junction，已被删除，因此W\G_W确实属D7。容量给

\[
b+5+q-|G_W|\le b+5,
\qquad \boxed{G_W=U_D}. \tag{3}
\]

这对所有完整路径成立，和见证共享无关。还可逐点加强：对任意u∈U_D，S+u有b+6点；由相同扩展与(2)，它的junction只能在u。若u不是junction，整集是超过b+5的D7，矛盾。所以每个u都有实际

\[
R5(S^4,u),\qquad B4(u,S^3). \tag{4}
\]

两族全部替代见证保留，不把singleton供应当W全部路径的替代。容量取等在这里真正迫出内部attainment；没有用“满756普通态必填满”或逐owner状态收费。

## 4. 角色预算必须取等，严格分支被排

(4)使U_D每点都成为ambient R5终点。D避T，而旧同体身份End_R5(X)=T⊔F′，故U_D⊆F′。由K′=P⊔U_D和H′=L′⊔F′、P∩L′=J，得到

\[
K'\setminus F'=J,
\qquad \boxed{j+m'=b}. \tag{5}
\]

反序同理

\[
\boxed{t+m=b}. \tag{6}
\]

因此候选“排除budget等号、强迫严格”方向被事实推翻：**严格budget才不可能**。本轮排除任一方向严格的整个共同等号分支，不仅是两方向同时严格。代b25及继承m,m′∈{9,10}、j,t∈{15,16}，仅剩(m′,j)=(9,16)或(10,15)，以及(m,t)的相同两种组合。原C的双严格入口m=m′9、j=t15现已不可能；但双40覆盖的j=t15仍可有m=m′10，不把两者混同。

## 5. 将S右红根提升到整个W

令E=End_R6(S)，此处E不表示满H蓝终核心。E⊆I。旧D7证明给|E|≤6；删除E后S\E是756，所以b+5−|E|≤b，得到|E|≥5。于是原来有五/六端点两种情形，且S的R6最小横截数恰5。

**引理。** 每个e∈E都是整个W的右红根：任意e<x<y在W，χ(e,x,y)=R。

取S内部终于e的R6，末前驱r∈S∩End_R5(X)。若W内B3(e,x,y)存在，χ(r,e,x)红则将x追加入R6得到R7；蓝则(r,e,x,y)是末点在W的B4，ambient延长给从r启动的B5，违反(2)。两色都不可能，证毕。x、y允许在U_D，不能把“S内右根”未经论证直接搬到超集。

对任何u∈U_D及**任何**W内部B4(u,i,x,y)，先延长成保留首pair(u,i)的ambient B5，取(4)任意纯入R5(S^4,u)，末前驱r。桥χ(r,u,i)蓝会把r前接B5得B6；故红，将i追加入R5得ambient R6，终点i∈T∩W=I。又其B3后缀(i,x,y)排i∈E。故

\[
\text{每条W内部B4从U_D启动，其第二点都属于 }I\setminus E. \tag{7}
\]

每次操作都只有一个需新验证的连续三元组，且按序无重复；并未把红R6误称为从u启动，它始于入R5的首点。

## 6. 全第二点图的实际删除、Hall及恰五端点

定义完整二部图G_D：u∈U_D与i∈I\E相邻，当且仅当W内部存在实际B4(u,i,x,y)。保留所有混合支持，包括后两点也来自U_D的路径。

对任意A⊆U_D，N(A)是全部这样的第二点，取实际诱导集

\[
V_A=(S\setminus N(A))\sqcup A.
\]

它无B5。若有内部R5终/B4源junction在S，延长B4又违反(2)；若在A，其B4第二点属于已删除的N(A)，不可能。故V_A是D7，容量给

\[
b+5-|N(A)|+|A|\le b+5,
\qquad |N(A)|\ge|A|. \tag{8}
\]

特别A=U_D时

\[
q\le|I\setminus E|=5+q-|E|,
\]

所以|E|≤5，联立旧下界得到

\[
\boxed{|\operatorname{End}_{R6}(S)|=5}. \tag{9}
\]

反序得到F0=Src_R6(T)也恰五点。这排除共同X_(3b+5)中任一方向整个六端点分支，不排独立D7配置的六端点可能性，也不排一般H50。

写A0=I\E、|A0|q，Hall给G_D完美匹配U_D→A0，每条边u<i。排序u1<⋯<uq、a1<⋯<aq，得ui<ai及所有cut的前缀支配。它是第二点incidence匹配，不是路径内部不交，不是private-only图，也不是每个owner独占一条红供应。(8)实际删除是Hall的依据；单看存在q条供应不足以防多对一，不能直接收费。

## 7. 已认证的另一实际残余V=K′∪E及其能力边界

取A=U_D，有N(A)=A0；上节的实际删除已证明

\[
V=W\setminus A_0=P\sqcup U_D\sqcup E=K'\sqcup E
\]

是大小b+5的D7。它的R6只能终于E，因为P避T、U_D在D。对每个e∈E，B5-free的K′+e有b+1点，容量迫R6，且只能终于e。于是

\[
\operatorname{End}_{R6}(V)=E,
\qquad \tau_{R6}(V)=5. \tag{10}
\]

这是全部路径都检查过的合法残余替换，不是仍待验证的条件交换。然而K′+e的R6**可以完全位于P+e**，未必遇U_D；与旧K′+a、a∈A0的mixed插入情形不同，不作相同private-attainment断言。

还有有限的纯支持补充：对每个a∈A0，V+a大小b+6，不能是D7，junction只能在U_D。任一此类B4第二点在A0且V+a仅含a，故存在某u∈U_D及B4(u,a,x,y)、x,y∈V；同时有V+a内入R5终于u。u<a，所以入R5不可能用a，实际全在V。这不迫不同a使用不同u，不能把全G_D的Hall自动限制到这族纯支持图。

V不是新的canonical S：U_D点不启动ambient R6；也未证明X\V是766。不能在V上重用“canonical residual的全部点是ambient源”或满H封闭。E是实际端点集而非任选五横截。每个其他最小Z仍使S\Z为满756，但未证所有Z都是端点集、未证E是唯一横截，也未建立matroid交换。

## 8. 末根附近的完整次序限制

写E={e1<e2<e3<e4<e5}。整个W右根性质给

\[
\max W=e_5,\qquad U_D\cup A_0\cup J<e_4,
\qquad W\cap(e_4,\infty)=\{e_5\}. \tag{11}
\]

特别e4、e5是W最后两个点。初稿只得最后间隙至多一个P\J点，现由旧R21扩根链强化为空；B本轮稿的较弱版本不回写。以下直接证明最终结论。

E是S内部R6的最小五横截，取e2-private R6，其终点必为e2。首点a避e1；若a>e1，前接右根e1得到R7，故a<e1。同端实际a→e2的R6与B3禁形迫χ(a,e1,e2)=R，再由E右根得到实际R6(a,e1,e2,e3,e4,e5)。

若z∈W晚于e5，将z追加该R6，唯一新连续三元组(e4,e5,z)由W右根性质为红，得到R7。若e4<z<e5，插入z只新增(e3,e4,z)、(e4,z,e5)，二者同理由右根为红，也得到R7。因此W∩(e4,∞)={e5}。U_D、A0、J都在W且避E，故它们全部严格早于e4，(11)得证。

这些次序式没有增加另一笔容量loss，也没有产生14个through点；红路径首末点不自动具有双角色。这里不声称所有非E点都在e2前，更早插入会缺第三个新三元组。

## 9. 成对75740覆盖：仍开放的等号接口与所有合法增广点

本节只取b25、j=t15，现必有m=m′10。旧 [R25§7](RESET_R25_GLOBAL_EXTREMAL_STRUCTURE_AND_JOINT_REALIZABILITY.md) 给实际757配置

\[
X\setminus\operatorname{Src}_{B5}(X)=F_H\sqcup(S\setminus J),
\quad |F_H|=25,\quad |S\setminus J|=15.
\]

每个s∈S\J有纯F_H的R6尾：F_H+s共26点、无B5，容量迫R6且从s启动。相应canonical747侧含S\J，大小15或16。若16得到(S\J)+f；若15，另一canonical侧F_H不能加入任何s，准确使用 [R5§2—8](RESET_R5_COVER_AUGMENTATION_CAPACITY.md) 的canonical增广定理，得到某f∈F_H，使A_f=(S\J)+f为747。于是有16∪25、交恰{f}的实际覆盖。反序有g∈K′的另一覆盖。只断言适当选择存在，不声称唯一或可同时加入多个f；任意改选覆盖不自动继承canonical端点身份。

**本轮有限定位：** 对每个合法f∈F_H满足A_f是747，均有f<e4；反序对每个合法g∈K′，均有g>f2，其中F0={f1<⋯<f5}=Src_R6(T)。

先将E右根lift到每一个A_f：取S内部终于e的R6末前驱r，r∈S∩End_R5(X)，由(2)有r∉J，故r∈A_f。若A_f内有B3(e,x,y)，红joining给R7，蓝joining给A_f内部B4，均不可能。因此每个e在A_f也是右红根。

旧 [R21§2.4](RESET_R21_GLOBAL_CAPACITY_AND_SUPPLY_REALIZABILITY.md) 给实际R6(a,e1,…,e5)、a<e1，机制自足如下：E是S的最小五横截，取e2-private R6，其首点a避e1；若a>e1可前接右根e1成R7，故a<e1。χ(a,e1,e2)蓝会与该private R6同端构成weak7，故红；加E右根得到显示的R6。

若f>e5，追加f的唯一新三元组(e4,e5,f)在A_f中红，得R7；若e4<f<e5，在显示R6的e4/e5之间插f，仅新增(e3,e4,f)、(e4,f,e5)，均在A_f且始于E根，故红，又得R7。f∈H而E⊆S，不能相等，所以f<e4。反序即g>f2。

**修复被撤回的更强主张f<e2。** 若e2<f<e3，插入需要验证三个新连续三元组，包括(f,e3,e4)；前两个由右根红，不控制第三个。packet(e2,f,e3,e4)前三项红而允许RRRB，因此不能强迫最后三元组红。e3<f<e4同样缺(f,e4,e5)。这是局部合法packet及证明缺口，不是完整临界反例。

16点747侧确有某内部R6，因为经典noB4/noR6容量15；但它未必用f，未必提供缺失三元组或两个覆盖共同端点。a16上界不是全部16点配置分类，也不是满21-cell经典目录。f∈V_D时不能结束ambient R6，却可为其内部点；f∈Q0时可以是终点，替代路径均须保留。

由第5节lift和F0左根性质，对每个cut c，E_≤c∪(F0)_>c为红clique，人口≤6：混合三元组首点是E右根，纯F0三元组红。这只是旧root-cut类型的顺序限制；不产生第二交点或新人口saving。双40覆盖在m=m′10、j=t15中仍开放。

## 10. 方法作用、失败路线与新旧归属

| 步骤 | 新的有效共同约束 | 首断点与修复或停止 |
|---|---|---|
| 删除完整junction | G_W=U_D，singleton S+u迫纯R5/B4，强制双budget等号 | 不能从H′through直接移植内部attainment；本轮以实际D7容量修复 |
| E右根lift及全第二点图 | 所有mixed B4第二点在I\E；每个子集的实际删除给Hall，排E6及对偶 | private-only图可能漏multi-U_D路径；全图保留全部路径后才可删点计数 |
| V=K′∪E | 认证另一整块D7及恰五实际终点 | V不是canonical S，补集未证766；K′+e未必用U_D，不能再次套源封闭 |
| 红前供下降到K′ | 保留实际S前供和蓝后供 | 前接R6只迫蓝桥，不给红替代前缀；内部替换缺额外三元组，没有严格下降量 |
| paired40合法覆盖 | 每个合法f<e4、g>f2 | 更强f<e2漏第三新三元组；a16不补该颜色，不迫第二共同交点 |

本轮容量等号的实质作用，是让更大的实际诱导集无法仍属D7，从而迫内部junction；实际删除再让完整支持图具有Hall。不是按路径次数或共享owner收费。packet用于路径遗传、旧canonical合法性及插入修复的准确颜色检查；weak通过旧三链/残余五横截、同端private R6+B3以及R5点对比较进入，不能把不同外端供应冒充同端禁形。右根lift并非单凭遗传，必须使用入R6、ambient B4扩展和mixed-role三者。

R5全局点对势需要共享实际首/末点的受限红六点/蓝路径支持才能闭合循环。本轮u—i边是B4首pair，配套R6却从入R5的首点启动，不是u→i红六点；没有反边或闭合有向行走，不能凭匹配和交叠套势函数矛盾。R25附录的复制匹配亦不保证实际R6端点关系传递。

新结果是(3)—(10)及有限次序/合法cover定位，不是旧w0、旧m/q范围或旧三块推论的重复。它们在共同等号框架下排任一严格budget和任一六端点支；没有排整个X80，没有独立H50排除，没有新真实临界构造。全部最小横截的其他可能性保留，不假定endpoint化、唯一性、laminarity或matroid结构。

旧数量链N757≤a+b−1、C≤2b、Q≤C+b+5、F777=Q+1，代a16/b25仍为40/50/80/81。本轮没有全局数值下降、递推下降或新外部界收益。生成自检与文档核对不升级旧接受或任何新数学状态。

## 11. 文档边界与唯一剩余共同实现问题

[来源清单](../../../../tmp/n7_residual_endpoint_rigidity_20261029/SOURCE_MANIFEST.json) 保存本轮有限读源与保护入口当前bytes/SHA256；[机械回执](../../../../tmp/n7_residual_endpoint_rigidity_20261029/DOCUMENT_CHECK.json) 只核链接、路径、UTF-8、公式标号及有限字节，非科学检查或独立数学审阅。本轮所有数学为手工理论生成，未要求新的计算事实，因此不需要科学执行来转写这些证明；机械检查也不替代其未来独立审阅。仅新建本主稿与本轮回执目录；历史、task元数据/指针、接受/assurance、配置、sealed证据和运行均未改写，没有Git mutation、提交或归档。requested native Sol/high是执行角色记录，不能由角色名核实实际backend/effort。

最后只保留一个问题：**在w0、双角色budget等号、两方向各恰五实际残余端点的同一共同等号母体中，新残余V=K′∪E与反向残余及其完整实际红蓝供应，能否共同迫出同端禁形或全部路径均认证的严格重分划？** 具体未控的是完整B4支持未必终于末pair(e4,e5)，强行终端化还需未证明的新三元组；全Hall因此没有把D内红五点与蓝四点供应对齐到同一实际外端。V中的红六点又可以避U_D，多补全点/横截点mixed路径仍可能阻断重分划；不能把V改名为canonical S来跳过这些条件。这里没有完成共同实现矛盾。

全部新增unreviewed/unaccepted，科学检查0、外部审阅0。没有新全局上界，当前仍为40/50/80/81。
