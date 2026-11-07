# N7：Hall 缺额的实际增广根与零 through 临界机制闭合

日期：2026-11-01。状态：**工作证明；全部新增 unreviewed/unaccepted，未独立审阅、未接受**。本文忠实转写主会话已批准的数学。生成协作者推导、另一生成协作者逐项交叉检查、主会话核查均属同会话生成与核对，不是独立review。指定native Sol/high文档执行者只负责转写与文档一致性，不自行生成数学、补证或独审。

本轮主成果是：在下一临界层 n=3b+3、w=0，**全部双满standard机制均被排除**，包括昨日剩余(3,3)、(3,4)、(4,3)根数组合；另排除至少一侧η0/full、另一有效方向W=S且无删端口δ=0的η1/2整类，含Ω*非空但δ=0的情形。关键是把Hall缺额兑现成实际D7增广，并将增广后的全部红六终点提升为原大域的根，使原外图完全避开这些新根。

无条件参数工作界仍为

\[
N_{\rm sig}(7,6,7)\le3b+3,\qquad
N_{\rm sig}(7,7,7)\le3b+4.
\tag{1}
\]

尚未得到全局77/78。一般η≤2中的有删端口单满、双方均η≥1等机制不能由本轮已闭合类自动覆盖。完整F混合cut另给精确构造判据，不认领全局上界收益。

唯一新增文件为本文及 `tmp/n7_hall_defect_root_augmentation_20261101/DOCUMENT_CHECK.json`。旧稿、metadata、task.json、接受/assurance、指针、运行、CNF、proof、runtime全部保持，不提交、不归档。未调用外部Claude，未运行科研代码、枚举、SAT、solver、证明器或证书；本轮未浏览新外部来源，既有公开文献引用不虚称本轮复核。PowerShell仅作文档操作与检查。

## 1. 模型、旧加权入口与工作状态

X为完整有序rank-3 signotope。a<b<c<d的packet按abc、abd、acd、bcd至多换色一次。实际单色路径按顶点计长，连续三元组同色决定路径，路径对子序列遗传。weak7比较同实际首末点的反色路径，长度和至少9，内部允许共享。

767禁R7、B6、weak7；766禁R6、B6、weak7；756禁R6、B5、weak7，其换色模型禁R5、B6、weak7。b为756及换色模型共同有效容量。D7无B5、无weak7且内部End_R5∩Src_B4为空，容量≤b+5、R6横截数≤5。N_sig为最大允许人口容量，非强迫阈值。

本轮始终从昨日全模型工作定理进入：

\[
|X|+w(X)\le3b+3.
\tag{2}
\]

所以考察n=|X|=3b+3时，先得w=0。定义全部ambient角色与实际中性区

\[
S=\operatorname{Src}_{R6}(X),\quad T=\operatorname{End}_{R6}(X),\quad
I=S\cap T,\quad D=X\setminus(S\cup T),\quad
U=\operatorname{Src}_{R5}(D),\quad V=\operatorname{End}_{R5}(D),
\quad U\cap V=\varnothing.
\tag{3}
\]

Src、End在注明的实际点集内部计算；ambient表示X。中间图保留全部D内实际R5端点边，所有删除按实际点计，不要求不同路径内部不交。

主要旧依赖保持各自保证层级：

- [昨日接口核查与加权稳定性稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7879_INTERFACE_AUDIT_AND_WEIGHTED_THROUGH_STABILITY_20261031.md>) §3—9：任意缺额实际换核、完整port、全模型加权式、尾替换及下一层接口；§10为亏二原有进展。
- [78/79参数工作界稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_DEFECT_ONE_PREDECESSOR_COMPRESSION_AND_GLOBAL_BOUND_20261031.md>)：完整临界排除、跨核扇与低根路径族的实际击中。
- [纯核根分离稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_PURE_CORE_ROOT_SEPARATION_AND_INTERLEAVED_REPARTITION_20261030.md>) §1—3、§7：标准接口、完整纯核供应及全部实际链。
- [旧联合through稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_JOINT_THROUGH_SATURATION_AND_ORDERED_CUTS_20261030.md>) §1—3：实际D7增广及归一化预算。
- [联合neutral原稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_TIGHT_CUT_JOINT_NEUTRAL_AND_REPARTITION_DICHOTOMY_20261029.md>) §1—2：canonical角色、三链和同一联合预算。
- [R7工具](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md>) §1—3、[R20精确删根关系](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>) §0—4：模型、分解、合法chart与实际添点的精确+1。

既有公开引用 [Bergold–Felsner–Scheucher，*An Extension Theorem for Signotopes*](https://drops.dagstuhl.de/storage/00lipics/lipics-vol258-socg2023/LIPIcs.SoCG.2023.17/LIPIcs.SoCG.2023.17.pdf) 的pair-poset基础接口核对记录保留在昨日稿；本轮没有重新浏览或复核该PDF。

### 1.1 完备外锁、延长与完整外图

有效W⊂S为实际D7，并有**完备外锁port**：r∈W∩End_R5(X)若启动ambient B5，第二点必须在T∖W。这里不能只写“W外”，因为后续必须知道锁点也不在U⊂D。

末点在W∪U的B4可保首pair延成ambient B5。末点在W⊂S，用其出R6第二点，红桥会使原B4末前驱前接出红六成R7，所以蓝；末点在U，用D内出R5第二点，红桥会造终于D的R6，所以也蓝。

W、U均无ambient B5终点，故W∪U无B5。W上的内部junction由完整外锁排除，所以全部junction只在U。对每个good u∈U，保留全部W∪U内部B4(u,i0,x,y)第二点作为邻边；bad点为外图孤点，不能在诱导删点后新生junction。

good u还有内部入R5；把该B4保首pair延成B5，再与入红五末前驱joining，桥蓝给B6，故桥红产生末pair(u,i0)的实际R6。于是i0∈W∩T，并有全ambient蓝fanχ(u,i0,z)=B（z>i0）。反向外图保留全部对应前驱点和全ambient左蓝fan。

## 2. 核心引理：Hall缺额兑现实际增广根

**Hall缺额增广根工作引理。** 在§1.1接口内，任取A⊂U，N(A)为完整外图全部邻点，实际集合

\[
Y=(W\setminus N(A))\cup A
\tag{4}
\]

为D7。令E_Y=End_R6(Y)，则

\[
E_Y\subseteq(W\cap T)\setminus N(A),
\quad E_Y\text{ 的每点是整个原 }W\cup U\text{ 的右红根},
\quad\text{原外图全部邻点均避开 }E_Y.
\tag{5}
\]

证明Y无B5、无weak7由W∪U遗传。W上的junction由完整外锁排除；A点若在Y中成为junction，原W∪U中也有该junction，所以是原good点，但其B4第二点已全部从W删除。原bad点经诱导删点不能新造路径。因此Y为实际D7。

E_Y属于Y∩T；A⊂D无ambient红六终点，所以E_Y⊂(W∩T)∖N(A)。任e0∈E_Y，假设原W∪U中有B3(e0,x,y)。取Y内部终于e0的R6，末前驱p。禁R7迫χ(p,e0,x)=B，于是有B4(p,e0,x,y)，可保首pair延成ambient B5。

若p∈W，该蓝五第二点e0∈W违反完整port。若p∈A，Y红六的前五点给Y内部入p红五；再加B4(p,e0,x,y)，p就是原good点，e0∈N(A)。但e0∈Y∩T只能在W∖N(A)，矛盾。故χ(e0,x,y)=R，E_Y提升为整个原W∪U的右红根。

最后，原外图任何邻点i0都带有B4(u,i0,x,y)，其后三点为B3(i0,x,y)，与E_Y完整右根域冲突。因此所有原邻边都避开E_Y，原外图匹配数不丢失，可把其目标层改为(W∩T)∖E_Y。

这个结论作用于全部原邻边与全部Y内红六，不是选定一条路径的性质。没有把Y当作新canonical，也没有要求Y等于全部全局S。

## 3. n=3b+3的全部双满standard整类排除

### 3.1 满核角色、纯核分离与原匹配

假设已经兑现双满standard：H=X∖S、H'=X∖T各满2b，S/T完整mixed禁形与延长成立。S、T各有b+3点。记P=S∖T、Q=T∖S，满角色给

\[
|D|=b+q,\quad |U|=|V|=q,\quad |I|=q+3,
\quad E=\operatorname{End}_{R6}(S),\quad F=\operatorname{Src}_{R6}(T),
\quad e=|E|\ge3,\ f=|F|\ge3.
\tag{6}
\]

根数下界由删全部端点后的756容量给出。满Z=End_R5(H)=Q⊔V大小b，且无ambient B5源。任e0∈E，取S内入e0红六末前驱p，mixed使p无B5源。Z+p超过756容量，迫首点p、尾五点全部在Z的实际R6，其终点q0∈Q。

原末pair蓝帽和同端weak先迫q0<e0；若q0<maxF，F在T⊔V的完整左根将去首红五追加maxF，产生从Z⊂X∖S启动的R6，矛盾。q0=maxF因Q∩I为空排除。因此

\[
F<E.
\tag{7}
\]

两外图原各有至少max(0,q−2)条匹配。确切地，bad数k_b≤2，完整邻域满足|N(A)|≥|A|+k_b−2；good人口q−k_b与Hall缺额合计只损二。中间全部D内R5图有q-perfect：否则König删至多q−1个端点对应实际点，余至少b+1且无R5，违换色756容量。

完整链a0→u→v→b0若a0<b0，两ambient蓝fan给B4(u,a0,b0,v)，与中间实际R5(u→v)同端weak，所以每链b0≤a0。以后所有cut均只计实际完整链，不以局部边数代替。

### 3.2 假设左Hall还亏二，会产生五个新根

若左最大匹配≤q−2，则Hall给A⊂U，缺额def=|A|−|N(A)|≥2；q<2时这个反设已经不可能，不将负数当匹配规模。按§2得到实际D7 Y，其大小b+3+def≤b+5，所以

\[
\operatorname{def}=2,\quad |Y|=b+5,
\qquad e_Y=|E_Y|\ge5.
\tag{8}
\]

最后根数下界由删E_Y后的756容量给出，E_Y为原S∪U完整右根，全部原左边仍避E_Y。

满对侧Z'=Src_R5(H')=P⊔U有b点，全部无ambient B5终点；H'全局无ambient R6终点。任f0∈F，取T内出红六第二点t，t∈T∩Src_R5(X)，反mixed使t无ambient B5终点。

Z'+t超过756容量，迫实际R6(p0,z1,z2,z3,z4,t)，p0∈P、前五点均在Z'。原首pair蓝帽和同端weak迫p0>f0。若p0>e0∈E_Y，E_Y在原S∪U的右根给χ(e0,p0,z1)=R，可前接e0到纯前供前五点，产生终于Z'⊂H'的ambient R6，矛盾。p0=e0因P∩I为空排除。因此

\[
F<E_Y.
\tag{9}
\]

原左匹配仍至少q−2且目标避E_Y，右匹配仍至少q−2，中间q-perfect。先由E_Y≥5、F≥3与(9)得|I|=q+3≥8，故q≥5；然后才正式取q−4条完整链。cut在maxF处给

\[
e_Y+f+(q-4)\le q+3,\qquad e_Y+f\le7,
\tag{10}
\]

与e_Y+f≥8矛盾。因此左最大匹配至少q−1；反序同理右至少q−1。

### 3.3 两侧只亏一后排除所有三/四根组合

原E、F仍满足严格分离(7)。e,f≥3先给q+3≥6，即q≥3，所以两外q−1、中间q-perfect复合的q−2条完整链合法。cut在maxF得到

\[
e+f+(q-2)\le q+3,\qquad e+f\le5,
\tag{11}
\]

与e+f≥6矛盾。

**双满standard整类排除工作定理。** n=3b+3、w=0的全部双满standard配置不可实现；不再把昨日(3,3)、(3,4)、(4,3)列为开放。本定理仍以完整标准接口为进入条件，不把一般零through配置擅自假设成双满。

## 4. onefull与δ=0有效方向的η1/2整类排除

### 4.1 完整接口与人口

设反方向η0/full：H'=X∖T满2b、T有b+3点。正方向有有效D7 W=S、完整外锁与蓝四延长，无删端口δ=0，|S|=b+h，h∈{4,5}。允许Ω*非空，只要它没有留在全局S的删端口。

满反角色Z'=P⊔U大小b。记u=|U|、v=|V|，得到

\[
|D|=b+u,\qquad v\ge u,\qquad |I|=u+h,
\qquad E=\operatorname{End}_{R6}(S),\ e\ge h,\quad
F=\operatorname{Src}_{R6}(T),\ f\ge3.
\tag{12}
\]

左外匹配至少max(0,u−(5−h))，右至少max(0,v−2)。中间覆盖全部U：否则König删至多u−1个端点对应实际点，余D至少b+1且无R5，违换色756容量。无through，满纯前供同§3.2给严格F<E。

### 4.2 h=4：Hall缺额一的满增广

若左不能覆盖全部U，Hall给def≥1。Y=(S∖N(A))∪A为D7，base有b+4点，故def=1、Y满b+5、e_Y≥5。§2给所有原左边避E_Y，E_Y在原S∪U为右根。反满纯前供同§3.2证明F<E_Y。

|I|=u+4≥e_Y+f≥8先迫u≥4；原左u−1、右最多漏二、中间覆盖全部U，可复合u−3条完整链。cut给

\[
e_Y+f+(u-3)\le u+4,\qquad e_Y+f\le7,
\tag{13}
\]

与≥8矛盾。故左覆盖全部U。目标I∖E大小u+4−e≥u迫e≤4，结合e≥4得e=4。严格F<E又先迫u+4≥7，即u≥3；左覆盖u、右最多漏二，得到u−2完整链。cut给e+f≤6，与e+f≥7矛盾。

### 4.3 h=5：普通Hall直接矛盾

base满b+5，左普通Hall覆盖全部U，目标I∖E迫e=5。严格F<E先给u+5≥8，即u≥3；左u、右最多漏二、中间覆盖u，得到u−2完整链。cut给

\[
e+f+(u-2)\le u+5,\qquad e+f\le7,
\tag{14}
\]

与e+f≥8矛盾。

**onefull零删端口工作定理。** 至少一方向η0/full、另一有效方向W=S且δ=0的η1或η2全部不可实现，反序亦然。δ=0必要；δ≥1的cut多出端口单位，可能出现5+3=8等号，本证明没有排除该类，不能直接泛化。

## 5. 一般η≤2归一化与本轮准确覆盖

### 5.1 任意原缺额的实际换核

在n=3b+3、w=0，沿旧canonical X=H0⊔R0定义原Ω、J、M、M_R与三链h。旧实际增广预算n+w≤3b+5−η迫每侧0≤η≤2。取

\[
H^*=H_0\cup J\cup M_R,\quad R^*=X\setminus H^*,\quad
\Omega^*=\Omega\cup h(M_R),\quad M^*=M\setminus M_R,
\quad |H^*|=2b-\eta,\quad |M^*|+|\Omega^*|\le\eta.
\tag{15}
\]

全部H*-origin R6终点都在Ω*，这些源保留ambient入R5、出B5，分别来自原G或原M_R。每个源由三链锁到唯一Ω*终点。

令o=|Ω*|、A_H=H*∩S、a=|A_H|。不同Ω*终点需要不同源，所以a≥o。取实际有效基底

\[
W=S\setminus\Omega^*=(R^*\setminus\Omega^*)\sqcup A_H,
\qquad |W|=b+3+\eta-o+a=:b+h.
\tag{16}
\]

W⊂S无ambient B5终点，蓝四末点可保首pair延长。A_H上的蓝五第二点锁到Ω*⊂T且在W外；残余M*的第二点h(M*)在H*∩T，而A_H点启动B5故A_H∩T为空，所以该锁点也在W外。完整锁点均为T∖W，内部junction被延长后排除，W为实际D7。

容量给h≤5。于是

\[
\begin{array}{c|c}
\eta=0 & \text{真实fullstandard},\ h=3,\ \delta=0\\
\eta=1 & h\in\{4,5\}\\
\eta=2 & h=5,\ a=o
\end{array}
\qquad
\delta=|\Omega^*\cap S|\le o\le\eta,\quad
S=W\sqcup(\Omega^*\cap S).
\tag{17}
\]

η=0的fullstandard由旧真实换核结论兑现，不是把任意满766自动当标准。原Ω与新Ω*区分保持，原缺额d/j/m无需各自很小。

### 5.2 已排与未覆盖目录

| 归一化机制 | 本轮状态 |
|---|---|
| 双η0/fullstandard | §3全部排除，含旧三/四根剩余 |
| 至少一η0，另一η1或η2且δ=0 | §4全部排除，允许Ω*非空 |
| 至少一η0，另一δ≥1 | 尚未整类排除；端口修正不可省略 |
| 两侧η≥1 | 不由§3—4自动覆盖；按其完整混合预算继续研究 |

不能用“已补齐三/四根”暗示一般n=3b+3全部机制已经覆盖；它们是双满standard内部的旧开放根数组合。

## 6. 双亏二错位主线的精确剩余模型

本节沿昨日§10的双亏二η2、nonΩ、M0、w=0接口：S、T各b+5点，H=X∖S、H'=X∖T各2b−2点且分别全局无R6源、终点。昨日完整尾替换与两末前驱压缩已给E、F各五点、μ=0，令

\[
E=\{e_1<\cdots<e_5\},\quad F=\{f_1<\cdots<f_5\},
\qquad x=e_1=f_3,\quad y=e_3=f_5,\quad a=e_2,\quad\beta=f_4.
\tag{18}
\]

这些结论是本节入口，不表示全部η2已归入此模型。

### 6.1 错位方向的整类排除与实际双末前驱

所有cut满足F前缀−E前缀≤2。若β<a，cut β有F前缀4点、E前缀仅x一点，差为3，矛盾，故该错位方向整类排除。a=β时两红五共享实际红三点(x,a,y)，拼出R7(f1,f2,x,a,y,e4,e5)，昨日已排。因此真正剩余顺序是x<a<β<y。

严格低于y的E根x、a，全部S内入R6的末前驱实际集合P0恰两点；对偶严格高于x的F根β、y，全部T内出R6第二点实际集合Q0恰两点。昨日尾替换已证

\[
|P_0|=|Q_0|=2,\qquad
C_H=\operatorname{End}_{R5}(H),\ |C_H|=b-2,\quad K=C_H\sqcup P_0,
\quad
C'_H=\operatorname{Src}_{R5}(H'),\ |C'_H|=b-2,\quad K'=C'_H\sqcup Q_0,
\tag{19}
\]

K、K'均为满b点实际756核。这些集合收集全部相关实际末前驱/第二点，不选有利的单一路径。

事实上P0⊂P=S∖T。若p∈P0也在T，取其对应e_p∈{x,a}。p<e_p<y，F根y在T∪V的左根给χ(p,e_p,y)=R；原入e_p红六末pair的帽却给蓝，矛盾。反序得Q0⊂Q=T∖S。

任p∈P0、q0∈Q0分别选其原对应终点e_p∈{x,a}、首点f_q∈{β,y}，有p<e_p≤a<β≤f_q<q0。两帽给实际B4(p,e_p,f_q,q0)，因此

\[
\text{全部 }P_0\times Q_0\text{ 均不存在ambient R5；}
\text{也不存在可保端点缩为R5的更长红路径。}
\tag{20}
\]

否则与该蓝四同实际端点形成weak7。这里禁配保留整个两点乘两点矩形，而非某一对。

### 6.2 角色还原：两个缺二角色族恰是Q⊔V、P⊔U

先证Q⊔V⊂C_H。反设ζ∈(Q∪V)∖C_H。ζ不在S或K，且有ambient End_R5身份：Q点是R6终点，V点在D内结束R5。ζ无ambient B5源，Q由入R6 joining排除，V由D内入R5 joining排除。

K+ζ有b+1点、无B5，容量迫R6，首点只能在P0，因为C_H全局无源、ζ也非S。设首为p，原对应根e_p<y；其帽与weak迫强制终点≤e_p<y。K+ζ每点都具有ambient End_R5身份，所以新尾替换可将该红六末点换成y，与B3(p,e_p,y)同端weak矛盾。故所需包含成立。

令i=|I|、q=i−7。人口为|D|=b+q、|P|=|Q|=b−q−2。删除V的换色容量给v=|V|≥q；Q⊔V⊂C_H且|C_H|=b−2又给v≤q。所以v=q≥0，且包含取等。反序同理得到

\[
|U|=|V|=q\ge0,\quad C_H=Q\sqcup V,\qquad C'_H=P\sqcup U.
\tag{21}
\]

q非负由人口取等推出，不是先验假设。正错位下E∪F恰有八个不同实际点，故i≥8，进一步q=i−7≥1；这只是精确人口身份，不另计saving。

### 6.3 双满756核、四点交与全部I点双纯供

两核还原为

\[
K=(Q\sqcup V)\sqcup P_0,\qquad
K'=(P\sqcup U)\sqcup Q_0,\qquad
K\cap K'=P_0\sqcup Q_0,\quad |K\cap K'|=4,
\quad I\cap(K\cup K')=\varnothing.
\tag{22}
\]

交集恰四点使用P0⊂P、Q0⊂Q及w=0时U∩V为空；全部I点均在两核外。

每i0∈I实际有两方向纯供

\[
R6(i_0,K^5),\qquad R6((K')^5,i_0).
\tag{23}
\]

证明第一项：K中全部点无ambient B5源，i0∈T也无，所以K+i0有b+1点且无B5，容量迫R6。首点不能在C_H；若首点p∈P0，原帽迫终点≤e_p<y，K+i0所有点有ambient End_R5身份，尾替换到y再次造同端weak。因此首只能i0，五尾全在K。

第二项完整反序：K'+i0无B5，因为所有点无ambient B5终点。强制红六若终在Q0，头帽迫首点≥f_q>x；全部点有ambient Src_R5身份，头替换到x造同端weak。因此终只能i0，五前供全在K'。

这两项对每个实际i0分别存在；不指定唯一支持，不要求两纯供或不同i0的内部点不交。

### 6.4 完整三图链接的紧cut与β到a的下降链串

中间D内全部R5图有q-perfect，两外ordinary Hall覆盖全部U、V，共得到q条实际完整链。目标层A=I∖E、B=I∖F各有q+2点，故左右各恰两个unused点。

\[
|F_{\le x}|-|E_{\le x}|=2,
\qquad |F_{\le y}|-|E_{\le y}|=2.
\tag{24}
\]

任一所选完整链族在两个cut同时取等，迫两个unused A点都≤x、两个unused B点都>y，matched边不跨这两个cut。因此在(x,y]内得到实际端点非增的双射A_mid→B_mid；其domain相对image多β、少a。沿副本边可提取从β下降到a的完整链串。

这串由多条实际三图链组成，**不是已经拼接好的一条实际R5**。目前尚未证明能把它与(23)的双纯核供应合成全P0×Q0中某条已禁R5；这才是此精确错位模型的主攻剩余缺口。上述还原与紧cut不单独计作数值突破。

### 6.5 相邻端口扩根不能补缺桥：F+/E+精确刚性

扩大实际根供应族

\[
F^+=\{f\in I:\text{某ambient R6从 }(f,t)\text{ 开始且 }t\in T\},
\qquad
E^+=\{e\in I:\text{某ambient R6以末pair }(s,e)\text{ 结束且 }s\in S\}.
\tag{25}
\]

F+在整个T∪V上具有完整左红根域。取出红六首pair f0,t∈T，t启动ambient R5；若有B3(x0,y0,f0)在T∪V，χ(y0,f0,t)红会前接y0成R7，故蓝，得到B4(x0,y0,f0,t)。按§1.1的反向延长保留末pair成为B5，倒数第二点f0与末点t都在T，违反完整port。相同证明不要求整条出红六都在T内，tailreplacement也只需要这个pair。E+的完整右根域与headreplacement反序同理。

原全部反向外邻点都避F+，因为它们带有原T∪V内的相反蓝三。因此两外完整q匹配及中间q-perfect仍构成q条完整链，只将右目标改为I∖F+，左目标仍为I∖E。cut给

\[
|(F^+)_{\le c}|-|E_{\le c}|\le i-e-q=7-e=2.
\tag{26}
\]

取f*=maxF+。对全部严格低于f*的S内入红六，若普通末前驱有三个不同点p，三点加C_H超过b点且无B5，迫R6首为某p。其原对应低根帽限制强制终点≤e_p<f*；全部点有ambient End_R5身份，tailreplacement到f*又造同端weak。因此全部低根路径的实际前驱至多两个，k≤e−3=2。

由(26)改为严格前缀至多减一个共同根，k≥e+|F+|−8，所以|F+|≤5。原F⊂F+且|F|=5，得F+=F；反序得到E+=E：

\[
F^+=F,\qquad E^+=E.
\tag{27}
\]

所以a=e2不属于F+，全部ambient出a红六的第二点都避T；β=f4不属于E+，全部ambient入β红六的末前驱都避S。相邻端口扩根并不是仍开的突破出口，已被全族刚性封闭。

### 6.6 全ambient受限通道与双核全供的剩余缺口

定义U_β为全部ambient入β红六的实际末前驱，V_a为全部ambient出a红六的实际第二点。若p∈U_β又属于C_H=Q⊔V，source-free H的强化跨核扇给χ(p,β,y)=R，但该入红六末帽给蓝，矛盾。结合(27)已知p避S，得到U_β⊂D∖V；反序V_a⊂D∖U。

满K+a的纯尾不能用P0，因为P0<a，故五尾全部在C_H。满K'+β的纯前供不能用Q0，因为Q0>β，故五前供全部在C'_H。结合上述全ambient角色刚性，这些纯供的出a第二点实际在V、入β末前驱实际在U。因此

\[
U_\beta\subseteq D\setminus V,\quad U_\beta\cap U\ne\varnothing,
\qquad
V_a\subseteq D\setminus U,\quad V_a\cap V\ne\varnothing.
\tag{28}
\]

这是全ambient角色刚性，不是整类矛盾。仍需找到正确同实际端点、次序兼容的通道，将U_β/V_a受限供应与两核全供共同兑现；不能把复制层的β到a下降串当作actual R5，也不能继续推荐“扩大相邻端口根集”作为尚未证明的出口。

## 7. 合法根cycle边界与完整F混合cut竞争定理

### 7.1 合法rootcycle不能直接叠加through预算

同一ω下的已证合法rootcycle有3至6个blue-root charts。目前没有证明临界777母体|Z|=3b+4必有某个合法chart的through正数。不同chart的S/T及D内部R5身份没有已证运输，不能将各chart预算直接相加。

全蓝六点是实际合法777小配置；六点都可作合法blue-root chart，删根后是蓝五，没有R5，故w=0。这否定不带临界人口条件的“必有positive through chart”命题。它不是临界母体反例，也不否定带临界规模的目标。本例为批准的手工校准，没有运行枚举。

### 7.2 完整F的混合cut构造

设p≥3，X禁B_(p+1)、R_(p+2)。完整F的红成员为实际R_(p+1)，蓝成员为实际Bp；保留全部成员。此小节S_p=Src_R_(p+1)(X)、T_p=End_R_(p+1)(X)，避免与主线p=5时S/T混名。

对任cut c，令

\[
Y_c=(T_p)_{\le c}\cup(S_p)_{>c},\qquad K_c=X\setminus Y_c.
\tag{29}
\]

Y_c无任何实际Bp：若蓝p首点≤c，该首点在T_p，入R_(p+1)与出Bp joining，桥红给R_(p+2)，桥蓝给B_(p+1)；否则蓝p全部在c右侧，其末点在S_p，入Bp与出R_(p+1)同样两色joining矛盾。因此每个原蓝成员都遇K_c。

### 7.3 两类完整红约束的精确badcut区间

对每个原红成员H，其首点在S_p、末点在T_p，所以H∩S_p、H∩T_p非空。H漏掉Y_c当且仅当c位于

\[
\left[\max(H\cap S_p),\ \min(H\cap T_p)\right).
\tag{30}
\]

因为不取任何S_p右侧点要求全部H∩S_p≤c，不取任何T_p左侧点要求全部H∩T_p>c。

H全在Y_c只可能在H⊂S_p∪T_p时发生。此时精确badcut为

\[
\left[\max\bigl(H\cap(T_p\setminus S_p)\bigr),\
\min\bigl(H\cap(S_p\setminus T_p)\bigr)\right),
\tag{31}
\]

空max取−∞、空min取+∞；若H有neutral点，则这一“全落Y”区间为空。共同S_p∩T_p点在cut两边都属于Y，只有单终点必须在左、单源点必须在右，故区间判据精确。

任何避开**完整红族全部两类badcut区间**的c，直接给满足全部F的分划：每红同时遇K_c、Y_c，每蓝遇K_c。c=−∞恢复全S_p，c=+∞恢复全T_p。

尚未证明G/private完整结构保证这些区间不能覆盖全部cut。这个定理给构造族的精确判据，不给一般完整F闭合或新上界。本轮主线整类排除来自Hall实际增广根，不来自该竞争归约。

## 8. 参数后数字、完整剩余目录及下一重点

现有全模型参数工作界及合法chart条件传播保持

\[
|X|+w(X)\le3b+3,\quad N_{\rm sig}(7,6,7)\le3b+3,
\quad N_{\rm sig}(7,7,7)\le3b+4.
\tag{32}
\]

本轮在n=3b+3的零through层关闭双full及onefull/δ0等完整机制，但没有排除全部该层。最后代入既有用户授权工作输入b=25，仍为

\[
N_{\rm sig}(7,6,7)\le78,\qquad N_{\rm sig}(7,7,7)\le79.
\tag{33}
\]

若767子类w≥1才有≤77；777母体若某个已证合法删根chart的w≥1才有≤78。这些是条件子类，不能写成全局77/78。既有a=16时N757≤a+b−1=40、C766≤2b=50保持，本轮额外无条件数值saving为0。

| 机制或方法 | 本轮完整覆盖与剩余 |
|---|---|
| n=3b+3双fullstandard | 全部已排，含旧(3,3)/(3,4)/(4,3) |
| onefull，另一η1/2且δ=0 | 全部已排，允许Ω*非空但δ=0 |
| onefull，另一δ≥1 | 仍未整类关闭；有端口修正不能省略 |
| 双η≥1的一般混合机制、含Ω亏二 | 仍需完整路径族统一处理 |
| 双亏二nonΩ/M0的β<a或a=β | 前者由cut差3排，后者由共享红三点排 |
| 双亏二nonΩ/M0的x<a<β<y | 已还原双满756核/四点交/全部I双纯供/下降链串；尚缺被禁P0×Q0实际R5的兑现 |
| 相邻端口扩根F+/E+ | 已证F+=F、E+=E，不能靠此补缺桥；需处理U_β/V_a受限通道与两核全供 |
| 合法rootcycle临界positive-through | 未证进入；全蓝六点仅否定无临界规模的版本 |
| 完整F混合cut | 精确badcut判据已证，未证完整区间族不能覆盖全部cut |

不能把双满内部已关闭的三/四根组合重新列开放，也不能将本轮精确结构还原计作全局数值突破。下一重点是错位四点交核的U_β/V_a受限通道、两核全供与实际红五兑现，带删端口与含Ω的η2统一预算，以及合法chart或完整badcut族是否提供真正进入结论。

b=25证书本轮未重验证、未读新证书，仍为既有用户授权工作输入；用户报告UNSAT、证书验证中及旧accepted状态分层保持。全部新增unreviewed/unaccepted，生成与交叉核查不构成独立数学验证，未报告backend或实际effort不作验证结论。

文档回执为 `tmp/n7_hall_defect_root_augmentation_20261101/DOCUMENT_CHECK.json`，仅核严格UTF-8、公式号连续唯一、本地依赖链接、旧稿hash、固定参数代入及指定两新路径写入。`PASS_DOCUMENT_ONLY`不认证数学、不升级接受/assurance；本轮文档完成不代表长期任务完成。
