# N7：缺额一的联合稳定性与完整链接紧割

日期：2026-10-29。用户授权继续结构研究，主会话批准以下数学内容，native Sol/high文档执行者只作转写。全部新增数学 **unreviewed/unaccepted**；主会话与生成协作者的手工核对不是独立审阅。本轮未调用外部Claude或其他外部服务，没有科学代码、枚举、SAT、solver、proof checker或证书重放。PowerShell文档检查仅核文字、链接、公式与固定算术，不认证数学。旧稿、接受/assurance、任务metadata、sealed对象与运行不变。

上一轮工作证明草稿保持

\[
N_{\rm sig}(7,6,7)\le3b+4,\qquad
N_{\rm sig}(7,7,7)\le3b+5. \tag{1}
\]

本轮针对候选 |X|=3b+4研究第二单位，但尚未排除全部候选。本稿给三类机制的排除或归约及完整匹配归约，不登记新的全局上界。

## 1. 模型、目标与精确缺额账本

沿用 [三匹配主稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMMON_SATURATION_THREE_MATCHING_OBSTRUCTION_20261029.md>)、[R7原始论证](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md>) §2—3及 [R20原始论证](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>) §5的模型与工具。完整有序rank-3 signotope的四点packet依次为abc、abd、acd、bcd，至多换色一次。路径长度按实际顶点计，单色路径对子序列遗传。weak7使用同一对实际首末点的反色路径，长度和至少9，内部允许相交。767禁B6、R7、weak7；766禁B6、R6、weak7；756禁B5、R6、weak7。b为756及其换色模型的共同有效正整数上界。D7指禁B5、weak7且内部End_R5∩Src_B4为空的残余类，容量≤b+5，不能省略junction条件。

设候选 |X|=3b+4。原canonical分解 X=H⊔R，H是766，R是D7。令

\[
d=2b-|H|,\quad T0\subseteq R\text{为最小R6横截},\quad
\tau=|T0|\le5,\quad K0=R\setminus T0,\quad
\varepsilon=b-|K0|. \tag{2}
\]

K0是756，所以d、ε与5−τ均非负。由实际不交计数得

\[
1=d+\varepsilon+(5-\tau). \tag{3}
\]

因此恰有三类账本

\[
(|H|,|K0|,\tau)=(2b-1,b,5),\ (2b,b-1,5),\ (2b,b,4). \tag{4}
\]

正反两方向各自都有此账本；其类型可以不同。只研究双满核的子类，不能宣称覆盖全部候选，也不能把满核封闭或角色等式无条件搬到|H|=2b−1的分支。

## 2. 任意d的联合缺额引理

沿原canonical H、R、G定义

\[
\Omega=\{w\in R:\text{存在从H到w的ambient R6}\},\quad
S0=R\cap\operatorname{Src}_{R6}(X),\quad
J0=R\setminus(\Omega\cup S0). \tag{5}
\]

新的联合结论是

\[
|\Omega|+|J0|\le d,\qquad
|R\setminus\operatorname{Src}_{R6}(X)|\le d. \tag{6}
\]

它适用于全部d，不仅d=1。此前R20对两批分别给≤d，直接合用只能得到2d；本节在同一实际扩充核内重证注入，联合使用同一预算。

首先令K=H∪J0。R20 §5.5的全路径论证给K是实际766：H—H两端的ambient R6被原canonical端点封闭排除；H→J0不可能，因为J0避Ω；从J0启动的任何ambient R6也不可能，因为J0避S0。于是重算

\[
Z_K=K\setminus\bigl(\operatorname{Src}_{B5}(K)\cup
\operatorname{End}_{R5}(K)\bigr),\qquad
|Z_K|\le2b-|K|=d-|J0|. \tag{7}
\]

两个角色不交由joining给出；删除一个角色后的两个实际补集分别受756与换色756约束，故有该neutral界。这里K仅被证明为766，没有把它称作canonical。

对每个w∈Ω，在全部从H到w的R6中选最早起点a。原canonical结构使a∈G。若a是K内部B5源，其第二点属于K，必与w不同；G给a的入R5前供，三链即矛盾。若a是K内部R5终点，取该入R5末前驱f。G给任意一条从a启动的ambient B5；三链迫其第二点恰为w。桥χ(f,a,w)蓝会前接f得到B6，故桥红。把w接到K内入R5后，得到起点早于a的ambient R6：该首点若在H则违反a最早；若在J0则违反其全ambient非源身份。

因此a∈G∩Z_K。不同w不能选择同一a，因为固定一条G蓝5的第二点不能同时等于两个不同实际w。得到Ω到G∩Z_K的单射，再与(7)合并即(6)。最后R\Src_R6(X)是不交并J0⊔(Ω\S0)，其规模不超过|J0|+|Ω|。此为真实联合注入，不是将两条旧界相加或假定路径供应唯一。

## 3. d=1分支的完整提升与剩余例外

当d=1，(6)排除Ω与J0同时非空。若J0={j}，则Ω为空，K=H+j是满2b的766，并且不存在K-origin ambient R6：旧H的终点若在H由封闭排除，若在R由Ω为空排除；j本身是全ambient非源。

于是S=R−j恰为全部ambient R6源，|S|=b+4。对每个s∈S，K+s超过766容量，故有R6；首点只能是s，后五点全部在K，即每个s都有纯K红5尾。S继承原R的D7条件及原P+的unrestricted蓝末点延长：早期顶点允许在P+之外。

上一稿混合角色禁形的实际换点证明完整适用。若s∈S同时结束ambient R5并启动ambient B5，三链把全部出R6终点与出B5第二点锁到同一h∈K；纯K尾保证该h在K。实际K−h+s无R6而为满766，s不能启动内部B5，满核角色分划迫内部R5终于s，再接h得到K-origin R6或B6，均矛盾。这只需要上述已证的满核、全源、纯尾与封闭接口，不要求K自己是canonical。

因此J0单点的整类提升为“满核+全源残余b+4”。剩余d=1情形仅为

\[
(\Omega,J0)=(\varnothing,\varnothing)
\quad\text{或}\quad(\{w\},\varnothing). \tag{8}
\]

前者R全是源，但不能由此保证纯H尾；后者只有一个H-origin终点，却可能有多个H-origin源。不能删除唯一neutral点就宣称获得满核封闭；(6)的终点单射不是源唯一性定理。

## 4. 双满核接口下的junction与亏一Hall

本节只在两方向均具有已证满核接口时进行，也允许§3已严格提升的方向性接口。设两向K、K′均有2b点，S、T分别为全部ambient R6源、终点，各b+4点；S为原序D7，T为反序D7。两向均有无满核origin R6、纯满核尾或前供、unrestricted蓝末点或首点延长及混合角色禁形。

定义

\[
I=S\cap T,\ q=|I|-4,\ P=S\setminus T,\ Q=T\setminus S,
\quad D=X\setminus(S\cup T). \tag{9}
\]

于是|P|=|Q|=b−q、|D|=b+q。令U=Src_R5(D)、V=End_R5(D)。T不能启动ambient B5；满核角色分划给Q落在K内部R5终点族，D中剩余恰q个位置。再删除D内部全部R5终点，用换色756容量给反向下界；反序同理。因此q≥0且

\[
|U|=|V|=q. \tag{10}
\]

允许U、V相交。令E=End_R6(S)、F=Src_R6(T)。残余旧根界与删除全部端点后的756容量给初始4≤|E|,|F|≤6，而两侧最小横截数τS、τT都在{4,5}。

取W=S⊔U。W无ambient B5终点：S点有出R6，U点有D内部出R5，两色joining分别产生禁形或终于D的R6。每条末点在W的ambient B4都可保首pair延长成ambient B5：末点在S用unrestricted fan，在U则接D内部R5的下一点，红桥会造成终于D的R6，所以桥蓝。混合角色禁形因此排除S上的内部junction。

重算

\[
G_W=\operatorname{End}_{R5}(W)\cap\operatorname{Src}_{B4}(W)
\subseteq U,\quad B_{\rm bad}=U\setminus G_W,\quad k=|B_{\rm bad}|. \tag{11}
\]

删除全部G_W后是实际D7；其规模b+4+k≤b+5，故k≤1。

E的右红根提升到整个W与上一稿相同：取S内终于e的R6末前驱r；若W有B3(e,x,y)，红桥给R7，蓝桥给从r启动的B4，再延长成B5，违混合角色禁形。这里不需要singleton供应。

任一good u∈G_W有W内部入R5，并有内部B4(u,i,x,y)。先将B4保首pair延长成ambient B5，再用该入R5的末前驱连接。蓝桥会给B6，故红，产生最后pair(u,i)的实际R6。因此i∈I\E，且对所有ambient z>i都有χ(u,i,z)=B；否则追加z形成R7。入R5允许经过其他U点，没有强行替换为纯S供应。

定义good点到I\E的完整邻图，保留全部内部B4第二点。对任意C⊆G_W，取

\[
Z_C=(S\setminus N(C))\sqcup C\sqcup B_{\rm bad}. \tag{12}
\]

它是D7：S上的junction被混合角色禁形排除；C上的B4第二点全被删除；bad点本来就不是W的junction，诱导删点不会新造路径。容量给

\[
|N(C)|\ge|C|+k-1. \tag{13}
\]

若k=1，good图有普通Hall，覆盖q−1个good点；若k=0，Hall亏损至多1，可取q−1条匹配边。q=0按空匹配处理，不将q−1解释为负的匹配规模。对q≥1，结合目标侧大小得到

\[
q-1\le|I\setminus E|=q+4-|E|,
\qquad4\le|E|\le5. \tag{14}
\]

q=0时E⊆I且|I|=4，端点界同样成立。反序完全同理得4≤|F|≤5。因此六根分支已被整体排除；此结论不要求τS或τT为5。bad点与Hall缺额共同只损失一个单位，不能把两者独立记成两次损失。

## 5. 所有匹配的四层完整链接归约

进一步限定

\[
|E|=|F|=5,\quad\tau_S=\tau_T=5,\quad
A=I\setminus E,\ B=I\setminus F,\quad|A|=|B|=q-1,\quad q\ge1. \tag{15}
\]

构造完整四层副本网络A→U→V→B。外边来自全部good蓝扇支持：A与U之间使用§4全部实际B4首pair，V与B之间使用反向全部支持；中间边是全部D内部R5实际端点边。每层每个副本容量1；同一实际点可以在不同层出现。外侧α图能饱和A，β图能饱和B；中间图由上一稿第三Hall有perfect匹配，其删点并集证明允许U、V重叠。

若存在q−1条分层副本点不交完整链，它们构成A到B双射。每条链记为a→u→v→b0；若a<b0，两个全ambient蓝fan给B4(u,a,b0,v)，中间实际红5给同端u→v，于是weak7矛盾。故每链均有b0≤a，双射给所有cut的E前缀数≥F前缀数。

τS=τT=5提供private根链：写E={e1<…<e5}、F={f1<…<f5}，有实际R6(a*,E)与R6(F,b*)，a*<e1、b*>f5。取cut e2，前缀支配迫e2<f3，遂由根颜色拼成实际R7(a*,e1,e2,f3,f4,f5,b*)，矛盾。

所以本子类中有满链接的整类被排除，包括q=1时的空完整链接。这里无需要求中间所用配对能够扩展成perfect；也不能先固定某组α、β、ρ，再把该组不连通当作完整网络无链接。单问两遗漏点之间有没有一条红边，亦没有覆盖所有完整链。

## 6. 无满链接的精确紧割与实际满核

对§5的完整有限整数点容量网络应用Menger。令最小点割分别为Z_A、Z_U、Z_V、Z_B，大小记a、x、y、z，总和t。定义

\[
A'=A\setminus Z_A,\qquad
L=N_\alpha(A')\setminus Z_U,\qquad
J=N_R(L)\setminus Z_V. \tag{16}
\]

无存活完整链意味着N_β(J)⊆Z_B。外侧Hall与中间perfect给

\[
|L|\ge q-1-a-x,\qquad
|J|\ge|L|-y,\qquad |J|\le z+1. \tag{17}
\]

由此t≥q−2；满链接失败又给t≤q−2。因此q≥2，且

\[
t=q-2,\quad|L|=y+z+1,\quad|J|=z+1,\tag{18}
\]

\[
N_\alpha(A')=L\sqcup Z_U,\quad
N_R(L)=J\sqcup Z_V,\quad
N_\beta(J)=Z_B. \tag{19}
\]

特别|N_R(L)|=|L|。这些等式是完整最小割的取等条件，不是只挑某条匹配后的局部剩余。

实际删除

\[
C=(U\setminus L)\cup N_R(L) \tag{20}
\]

命中全部D内部R5：首点不在L时删首点，否则删其终点。复制计数为q，故实际并集至多q；换色756容量又迫

\[
|C|=q,\qquad|D\setminus C|=b,\qquad
(U\setminus L)\cap N_R(L)=\varnothing. \tag{21}
\]

所以精确剩余是紧割与一个实际满b的换色756核共同实现；它没有超容，不能据此继续扣一个单位。

纯网络校准说明只知道三个图分别具有所需匹配并不足够：一支A→u1→v1，但v1不接B；另一支u2→v2→B，但u2无A入边；其余q−2位置为完整链。三图分别有所需匹配，最大完整链接却只有q−2条。这只是支持网络，不是完整signotope反例，不证明该紧割可在候选X中实现。

## 7. 竞争路线：排除处处唯一private的完整机制

**定理。** 设p≥3，实际完整有序rank-3配置禁B_(p+1)、R_(p+2)及同端R_(p+1)+B3。取实际红R_(p+1)成员与蓝B_p成员的完整角色约束：每个红成员同时遇K、Y，每个蓝成员遇K，K⊔Y为全体顶点。若该完整约束族UNSAT且红族横截数τ=p，则存在某个最小横截S与s∈S，至少两条不同的完整红成员A满足

\[
A\cap S=\{s\}. \tag{22}
\]

该结论排除“所有最小横截、每点处处唯一private”的整个机制类，允许任意额外重叠红成员及不属于任何最小横截的点。不要求MUS，也不说指定S一定分叉；它不处理多private完整族或τ≥6，不产生数值改进。

### 7.1 从全部最小横截得到真正基交换

令ℬ为全部大小p的红横截。对每个S∈ℬ置Y=S、K为其余点，所有红约束都满足：S命中每个红成员，而红成员有p+1点，不能全落在Y。UNSAT故迫一条蓝B_p全落S；S恰有p点，所以每个S本身是实际蓝B_p。

每个s∈S至少有一个private红成员，否则S−s仍为红横截，违最小性。反设处处恰有一个，记A_s。任取x∈A_s，S−s+x仍命中全部红成员：除A_s外所有红成员都遇S−s，而A_s遇x。反过来，替换成功必有x∈A_s，因为它必须重新命中A_s。

对任意基候选S、T∈ℬ与s∈S\T，T命中A_s，选x∈A_s∩T。由A_s∩S={s}且s∉T，x∈T\S，故S−s+x∈ℬ。这是真正的基交换公理。于是ℬ是地集

\[
G=\bigcup_{S\in\mathcal B}S \tag{23}
\]

上秩p拟阵的全部基。每个A_s全部落在G，因为其中每点均可替换进入某个基；并且A_s正是关于基S和基点s的fundamental cocircuit，即含s的成功替换点集。它有p+1点且是实际红路径。地集外的额外红约束没有被删除：每次替换仍验证原完整红族，所以它们一直被保留。

### 7.2 全部circuit至多三点

任取circuit C与x∈C，将独立集C−x扩成基B。B+x有p+1点，不能是蓝路径，故包含实际红三元组T。B本身是蓝路径，迫x∈T。对每个y∈C−x，B−y+x是基，因而全蓝，迫y∈T。因此C⊆T，|C|≤3；若|C|=3，它本身是实际红三元组。G无loops，因为其中每点都属于某个基。

### 7.3 自足的秩一、秩二分块

固定基B。每个非基点x的fundamental circuit在B上的支持大小为1或2。两个不同的二点支持不能相交。否则设x支持{a,b}、y支持{b,c}。有

\[
\operatorname{cl}\{x,a\}=\operatorname{cl}\{a,b\},\qquad
\operatorname{cl}\{y,c\}=\operatorname{cl}\{b,c\}. \tag{24}
\]

fundamental circuit的唯一性及B独立保证y、c不在前一个闭包中，x、a不在后一个闭包中。因此{x,a,y,c}的每个三点子集都独立，而四点全在cl{a,b,c}，形成四点circuit，与§7.2矛盾。

所以不同的二点支持两两不交。把B划成这些二点块及剩余单点块，每个非基点按支持分配；单支持基点若属于二点块，也归该块。所得各块G_i秩1或2，秩总和为p。为说明这是直和分块，对任意Z_i⊆G_i，分别把其基扩到块基，得到

\[
p\le r\!\left(\bigcup_i Z_i\right)+
\sum_i\bigl(r(G_i)-r(Z_i)\bigr). \tag{25}
\]

结合秩的次可加性及Σr(G_i)=p，得r(∪Z_i)=Σr(Z_i)。因此全部基恰为各块基的product。

每个秩二块至少有三个parallel classes：产生二点支持的a、b、x分别属于三个不同类。来自三个不同类的三元组是circuit，故红。若三元组至多占两个类，选另一个类P；整个三元组落在G_i\P中。选另一基点在P，可将G_i\P实现为某个基的fundamental cocircuit，所以它也是实际红路径，其所有三元组红。于是整个秩二块全红。

该块删去任一parallel class后的cocircuit已有p+1点，故块至少有p+2点，与禁R_(p+2)矛盾。只剩p个秩一块；每块为fundamental cocircuit，是实际红p+1路径，两两不交，而且所有product横截都是实际蓝B_p。

### 7.4 用实际顺序排除最终product

为使论证自足，复述上一稿附录A的延拓引理。若A是红p+1路径，D是与A不交的蓝p−1路径，且每个D+a、a∈A都是蓝p，则D在(min A,max A)内至多一点。若有两个内部点d<e，D+min A与D+max A的蓝色遗传使packet(min A,d,e,max A)首尾蓝，故全包蓝，出现B3(min A,d,max A)，与A同实际端点的红p+1路径冲突。

D不能全在A右侧：设x、y是A最后两点，d是D首点；χ(x,y,d)红则把d接到A得红p+2，否则它蓝，结合D+y全蓝，(x,y,D)成为蓝p+1。全左侧由反序同理排除。

现选包含全局最早红顶点的红块A。其他p−1块的任意product横截D没有点在min A左侧，不能全在max A右侧，且内部至多一点，所以恰一内点。两个其他块不能都含内部点，否则可同时选择这两点。因此恰有一个其他块B全在A内部，其余块全部在A右侧：若该B有外点，选择其外点及其他块点就得到全右侧D，违引理。

取max A及除A、B外各块的一点，得到p−1点集D′，全在B右侧；但每个D′+b0、b0∈B都是蓝product横截，再违单侧引理。矛盾。额外重叠红成员不影响此步，因为这里只需已得到的p个实际红块与全部实际蓝product。反设处处唯一private遂被排除，定理成立。

## 8. 收益分账与下一步精确靶点

本轮新的完整手工证明包括：任意d的联合缺额上界、d=1时J0非空整类归约、双满接口六根整类排除、五根τ5满链接整类排除，以及全局处处unique-private机制排除。四层完整网络把剩余精确归约到紧割与实际满b换色756核共同实现。这些排除与归约没有覆盖全部候选|X|=3b+4，本轮新全局收益为0。

先保留参数链，再代数值。旧757界a+b−1、766界2b以及上一稿草稿(1)仍给

\[
N757\le a+b-1,\quad C766\le2b,\quad
N767\le3b+4,\quad N777\le3b+5. \tag{26}
\]

b=25的限定模型接受依据是 [C8正式接受记录](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md>)，其same-family/provisional及精确backend/model/actual effort不可验证的保证边界不变。a=16只参与旧757数值，代入仍为

\[
40/50/79/80. \tag{27}
\]

其中新结构所涉79/80保持上一轮未正式接受的工作证明草稿层级，旧历史40/50/80/81不改写。若未来完整排除|X|=3b+4，才可得到目标式

\[
N767\le3b+3,\quad N777\le3b+4;
\qquad b=25\text{时为 }78/79. \tag{28}
\]

(28)仅为目标，不列入已证结果。

下一步保留以下精确靶点：

- 双满方向中的四根或τ4情形，不能套用五根τ5的private根链。
- 五根τ5下，§6紧割与满b换色756核的共同实现；继续研究须处理该实际核，不能仅以“改选匹配”空谈闭合。
- 单方向亏一的剩余(Ω,J0)=(空,空)、({w},空)，及其与反向分支的组合；唯一终点不等于唯一源，纯尾与封闭仍须另证。
- 竞争路线的多private完整族。任何新交换必须同时保证两个块的全部路径帽；上一稿已排除的全邻域残余补集交换不再重启。

以上均未闭合。没有把三个图各自有匹配、抽象支持网络、一次合法残余交换或一个满核重新包装为第二单位。拟阵论证允许额外重叠红约束与G外点，但不扩展成一般多private排除。

## 9. 文档证据与状态

本轮只新增本文及 [文档检查回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_defect_one_20261029/DOCUMENT_CHECK.json>)。所有实际本地链接均使用尖括号包裹、含字面空格的真实绝对路径。文档检查记录公式界定符、唯一编号、本地目标、固定参数代入及文本一致性；它不是科学执行、独立数学审阅或接受依据。

全部新增unreviewed/unaccepted，手工生成核对非独立审阅。外部审阅与外部服务0，研究程序、枚举、SAT、solver及证书重放0。原主稿、历史文件、接受/assurance、任务metadata、配置、sealed证据及运行保持；本稿不宣告长期研究完成。
