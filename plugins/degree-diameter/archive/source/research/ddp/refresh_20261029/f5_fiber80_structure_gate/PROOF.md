# 新S80纤维：精确16度条件及C25控制器必要结构

本文件为新source/rules的数学推导，不是旧固定3750点源的诱导保留。旧3750诱导域已关闭，未重跑。本次原预测是在C25上取25×80=2000点；第1–8节逐步推出必要结构，第9节进一步推出矛盾。当前本地最终结论为：所述normal-preserving S80 chart框架若D≤3，则N≤24、阶数≤1920，不能破该目标。root及两个互补代理已独立静态核对，跨模型实际SUCCESS/SOUND AS STATED见reviews/ddp/new_fiber_route_obstructions_20261030.DISPOSITION.md；尚未Lean形式化，没有构造2000点图或运行C25求解。

## 1 四方向的0/4线结构

在F5³中令a=x−y、b=z，取

    S80={a≠0,b≠0}，|S80|=5×4×4=80。

方向ell0=e0、ell1=e1改变a而固定b；方向ell2=e2、ell3=(1,1,1)改变b而固定a。故每个方向的25条平行线中，恰5条全空（另一normal为0），其余20条各保留4点。每条经过保留点的方向线都恰有4个保留点。

## 2 一般chart约束，不要求T_p S80=S80

令inv=(1,0,3,2)，边关系为

    y=T_p x+t ell_inv(p)，t∈F5，x,y∈S80。

要求T1=T0^{-1}、T3=T2^{-1}及T_p ell_p=ell_inv(p)。A类ports0/1保持b=0超平面，B类ports2/3保持a=0超平面；即相应normal经T只乘非零标量。此时源x的另一normal非零，整条target噪声线不是空线，因而恰给4个保留邻点。

可直接使用全部下列一般矩阵条件，而不枚举模板：

    T0 = [[0,A,B],[1,C,D],[0,0,lambda]]，A·lambda≠0；
    T1 = T0^{-1}；

    T2 = [[P,Q,1],[P−mu,Q+mu,1],[R,U,1]]，
         mu·(P+Q−R−U)≠0；
    T3 = T2^{-1}。

T0的det为−A lambda，且b∘T0=lambda b；T2的det为mu(P+Q−R−U)，且a∘T2=mu a。两逆矩阵自动满足反向条件。若要求normal值完全不变，可进一步固定lambda=mu=1，但非零缩放已足够。

因此任意simple4regular、inv相容的controller上，四port目标层互异，所得关系为simple无向16正则图，阶数80N。这里没有保证直径。

## 3 线关系为K4,4及六回退像的76界

每个非空source p线有4个保留点。T_p把完整p线送到完整target inv(p)线；后者非空且有4点。因此相应两组保留点之间恰为K4,4，source线的4点有同一个direct邻集D，|D|=4。

固定x∈S80及port p。对任意q≠p，控制词q,inv(q),p在source返回q-line(x)的全部4个保留点，再取其p邻集。四个不同source p线被T_p送到四条不同target inv(p)线，故像恰有16点，并包含D（返回点可取x）。

对任意target port r≠inv(p)，控制词p,r,inv(r)从D的4点各返回其r线的4点。四条r线互不相交，故像也恰16点，并包含D。

共六像，全部包含同一个D，因而其并至多

    4+6(16−4)=76。

三次遍历同一edge的回退词p,inv(p),p仅给D，已包含在基线中。这里不要求任何T_p保持S80，只用上述K4,4和逆向线关系。

若控制edge u−v不属于triangle，也不在任何simple4cycle中，则没有控制两步路线，也没有非回退三步路线；全部≤3路线正是direct和这些回退词。于是固定源点至目标80点最多覆盖76，D3失败。

**必要结论：每条非triangle控制edge都必须在某个4cycle中。** c4在下文数全部无向simple4cycles，包括有弦者，不仅诱导四圈。

## 4 非邻控制点的word预算

固定控制root，记t为其triangle数、c4为其4cycle数，n2为不同非邻控制点中有两步路线者的数目。

同fiber长度0/2的终点位于四方向保留线之并，至多且本规则中恰为1+4(4−1)=13点。若t=0则无三步闭控制word，覆盖不了80点，故每root t≥1（使用较松的17界也足够）。

4regular控制器的NB2 word共12条，其中2t条结束于邻点，其余12−2t条结束于非邻点，所以n2≤12−2t。

NB3 word共36条；其中2t条结束于root，2c4条结束于邻点，其余

    36−2t−2c4

条结束于不同非邻点。这里非回退三步词若结束于某邻点，就唯一形成穿过root的有向4cycle，计数精确。

对任一不同非邻控制目标，若没有NB3 word，则至多4条NB2 word（共同邻点至多4），每条最多4²=16终点，总≤64<80。因此每个非邻目标至少需要1条NB3。若该目标也没有两步控制路线，则单个三步word最多4³=64<80，至少需2条NB3。

非邻目标数N−5，故必须

    36−2t−2c4 ≥ (N−5)+(N−5−n2)
                  ≥ 2N−22+2t，

即N≤29−2t−c4。

## 5 目标controller阶数只能25，不能漏掉N27

要超过1920点，80N>1920迫N≥25。由t≥1，上界先给N≤27。

* N26：上界迫每root t=1。每个顶点恰在一个triangle中，triangles遂将顶点分成三元块，3不能整除26，矛盾。
* N27：上界迫每root t=1、c4=0。每root还有两条非triangle边，而第3节迫这些边在C4中，矛盾。

故目标只能N25。仅靠N26的整除论证不能排N27，76边门是必要步骤。

## 6 N25进一步迫t1/c41或t2/c40

初步不等式给每root 2t+c4≤4。因此只有t=1,c4≤2，或t=2,c4=0。

当t=1，root的两个非triangle边都需要C4，故c4≥1。还可以排c4=2：

此时任一穿过root的4cycle，其对顶点必为非邻点；若对顶点也邻root，则其两条半圈分别给两个不同triangles，违反t=1。令m_y为非邻点y的共同邻点数，则

    sum m_y=10，c4=sum binom(m_y,2)=2。

所以只能两个目标各有m_y=2，其余有支持者m_y=1，得到n2=8。NB3供给为36−2−4=30，而20个非邻目标需求至少20+(20−8)=32，矛盾。

因此精确局部必要条件为

    t=1时c4=1；t=2时c4=0。

对t=2，两个triangles不能共edge，否则它们另两顶点与共享edge形成穿过root的4cycle。于是其四条incident边全属于两个edge-disjoint triangles。t=1顶点恰有两条非triangle边。

## 7 必要的全局triangle/C4分解

所有triangles彼此edge-disjoint。t2顶点无非triangle边/无4cycle；t1顶点有两条非triangle边且恰在一个4cycle中。两条边都须在某C4中，故唯一C4必须同时使用它们。于是每个这样的4cycle四边都为非triangle边，且这些4cycles两两不共顶点，覆盖全部t1顶点。

设k为t2顶点数，则t1顶点25−k。按triangle和C4顶点incidence计数：

    25+k=3T，25−k=4C。

解得k∈{5,17}，仅有两种全局inventory：

    10个edge-disjoint triangles + 5个vertex-disjoint C4，5个t2顶点；
    14个edge-disjoint triangles + 2个vertex-disjoint C4，17个t2顶点。

这些是完整必要inventory，不是对称性假设，也不是充分构造。

对于另代理正prepare的固定三K3链加六K3（已9个triangles、2个链center为t2、23个free顶点额外度2），新增triangle不能使用任何fixed triangle edge，否则与已有triangle共edge。因此若保持该fixed motif，extra2factor必须分别具有cycle type

    3+4+4+4+4+4，或3+3+3+3+3+4+4。

这仍未排除cross-created额外4cycle、覆盖不足或chart困难；是否据此改模型由root决定。本文件没有求解controller，也不把固定motif的必要cycle type外推为所有controller必须含该motif。

## 8 本轮小检查与精确边界

check_once.py仅在125点坐标集上验证S80线结构及一组明确charts。该组T_p S80均不等于S80（A ports各有20个image点在S外，B ports各16个），但每个(p,x)仍恰4邻点。1280个reverse pairs相容，1920个pre/post像均恰16且含direct4。

该组实际六像并大小为43或55，这只是所选chart的局部诊断，不作为通用覆盖界或优化成果；通用上界76来自第3节证明。CPU0.025032128秒，1worker，0solver、0controller lift、大图BFS0。没有枚chart家族，也没有造2000点图。

本source/rules并非旧C30/3750诱导保留，不能用旧UNSAT/LRAT直接排；本轮也未恢复旧域、C21 uniform100或其它92/100族。控制器必要门不能代替实际全2000点验收。

## 9 后续独立纸面排除：当前S80/chart框架不能超过1920

本节是根代理提出的新预测的独立反例攻击后所得本地证明；未追加数值、controller生成或solver。承重前提仍是第1–2节：每层同一S80、A类steps只将被动normal b乘非零标量、B类steps只将被动normal a乘非零标量，且每步噪声使新active normal可唯一选择F5*中的四值。所有charts反向相容，port types由两组inverse pairs(0,1)、(2,3)定义。

### 9.1 Mixed三步词：固定(a',b')最多四个hidden值

用h=y作hidden坐标，则S80同构F5*_a×F5*_b×F5_h。A步选择新active值a_i∈F5*，被动b_i=lambda_i b_{i−1}；B步选择新active值b_i∈F5*，被动a_i=mu_i a_{i−1}。从前一完整点和所选新active normal，噪声参数以及下一完整点均唯一确定，因为相应noise对active normal非零。

对一个同时包含A、B的三步词，固定终点normal(a',b')后，每种type的最后一次active normal由终点值和后续被动缩放唯一决定。仅剩重复type较早的active normal自由，恰有四种选择。因此最多四个路径终点hidden值，可能更少。逐个type序列可见：

| 词型 | 自由active值 | 被终点固定的另两active值 |
|---|---|---|
| AAB | a1 | a2=a'/mu3，b3=b' |
| ABA | a1 | b2=b'/lambda3，a3=a' |
| BAA | a2 | b1=b'/(lambda2 lambda3)，a3=a' |
| ABB | b2 | a1=a'/(mu2 mu3)，b3=b' |
| BAB | b1 | a2=a'/mu3，b3=b' |
| BBA | b1 | b2=b'/lambda3，a3=a' |

这不是endpoint rank猜测，也不要求三步满秩。对仿射charts，hidden终值是剩余自由level的仿射函数；系数非零时恰四个不同值，系数零时至多一个。只用≤4已足够。

Pure AAA词保持目标b=lambda3 lambda2 lambda1 b0，只落一个b-strip；pure BBB同理只落一个a-strip。

### 9.2 t2,c4=0根的路线供需完全tight

假设存在N25合法lift。第5节和2t+c4≤4给每root t∈{1,2}。若全为t1，则triangles分成25顶点的三元块，不可能。因此必存在一个t2,c4=0根；此存在性不必依赖更强的5/17 inventory。

在这个root，12条NB2中4条结束于邻点，8条结束于非邻点；c4=0迫后8条终点互异（两条到同点会形成4cycle）。所以有8个dist2非邻目标，各有唯一NB2；其余12个非邻目标必须distance3。

NB3非邻供给为36−4=32。第4节已证每个dist2目标至少1条NB3，每个dist3目标至少2条；最低需求8+12×2=32，恰等供给。因此8个dist2目标各恰一条NB3，其余12个目标各恰两条。

### 9.3 唯一NB2不能same-type，故两个triangles必须monochrome

若某个dist2目标的唯一NB2是AA，则它只覆盖一个目标b-strip。该目标又只有一条NB3：若mixed，则在每个(a',b')上最多四hidden值，取b'在NB2的strip外即至少遗漏一个目标；若pure，则NB2 strip与这一个pure strip之并仍不能覆盖16种非零(a',b')。BB完全相同。因此该根所有非邻NB2必须mixed。

非回退same-type NB2恰为00、11、22、33，共四条。它们不能结束于非邻点，也不能结束于root，故全在四条adj-ending NB2中。

root的每个triangle给两条adj-ending NB2。两条都same-type，就迫该triangle三条edge同属A或同属B。t2,c4=0的两个triangles不共edge，恰用掉root全部四edge，而root只有两条A、两条B，所以一个是纯A三角形、另一个是纯B三角形。

### 9.4 同fiber选一个完全未覆盖的quotient

固定任一保留源点，normal为(a0,b0)。长度0/2回退的终点都在a=a0或b=b0两个strip中。

长度3的闭控制词恰来自这两个triangles的正反两个方向，没有其它闭三步词。纯A三角形一方向的被动b缩放记Lambda，反向由edge反向相容给Lambda^{-1}，故它们只覆盖

    b=Lambda b0，或 b=Lambda^{-1} b0。

纯B三角形类似，只覆盖a=M a0或a=M^{-1} a0。此处允许逐边不同charts、任意三角形holonomy；只用normal缩放与反向为逆，不假设holonomy恒等。

F5*有四值，所以总能取

    a'不在{a0,M a0,M^{-1}a0}，
    b'不在{b0,Lambda b0,Lambda^{-1}b0}。

这两个集合各至多三值。对应(a',b')的五个hidden目标全部保留，却无任何≤3控制/仿射路线可达，矛盾。

### 9.5 精确结论及不外推范围

N25也被排除；结合第5节对N26、27及word预算对更大N的排除，当前S80、inverse-paired两type charts框架若D≤3，必须N≤24，阶数至多24×80=1920。

因此该规则不能改善(16,3)=1920；无需C25 solver或新cycle生成。没有把未启动模型冒作UNSAT，也没有为本结论启动任何求解。这不是一般16度D3图上界，不排改变S80形状/normal层数、使被动normal不再独立缩放、非uniform fibers、改变噪声关系或不使用这个两type chart框架的其它构造。
