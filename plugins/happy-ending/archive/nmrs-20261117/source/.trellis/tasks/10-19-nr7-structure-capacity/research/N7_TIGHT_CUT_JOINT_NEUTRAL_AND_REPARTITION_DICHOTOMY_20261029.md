# N7：紧割纯核供应、联合neutral预算与完整重分划二分

日期：2026-10-29。用户授权继续结构研究；本稿仅转写主会话批准的数学，全部新增 **unreviewed/unaccepted**。主会话与生成协作者的手工核对不是独立数学审阅。native Sol/high文档执行者不自行补证，不调用外部Claude或其他外部服务，不执行科学代码、枚举、SAT、solver、proof checker或证书重放。文档检查只核文本、链接、公式与固定算术，不认证数学。旧稿、状态、接受/assurance、任务metadata及运行保持。

本轮尚未排除整个候选|X|=3b+4。保留工作证明草稿

\[
N_{\rm sig}(7,6,7)\le3b+4,\qquad
N_{\rm sig}(7,7,7)\le3b+5. \tag{1}
\]

下文分别标明完整定理、条件结构和实际校准；不把必要条件的增加称作全局上界进步。

## 1. 模型、来源与本轮接口

主要来源是 [三匹配主稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMMON_SATURATION_THREE_MATCHING_OBSTRUCTION_20261029.md>)、[缺额一与链接紧割稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_DEFECT_ONE_JOINT_STABILITY_AND_LINKAGE_CUTS_20261029.md>)，以及 [R7原始论证](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md>) §2—3与 [R20原始论证](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>) §5。继承各原始保证层级，不把本轮生成核对升级为独立审阅。

模型为完整有序rank-3 signotope：每个三元组着蓝B或红R，任意a<b<c<d的packet按abc、abd、acd、bcd至多换色一次。单色路径长度按实际顶点计，且对子序列遗传。weak7比较同一对实际首末点的反色路径，长度和至少9，内部可交叠。767禁B6、R7、weak7；766禁B6、R6、weak7；756禁B5、R6、weak7，其换色模型禁R5、B6、weak7。b为这两个换色对偶模型的共同有效上界。Src、End均在所注明的实际配置内部计算；标ambient或X才表示母体身份。

canonical分解X=H⊔R中，H为766，R为D7，即禁B5、weak7且内部End_R5∩Src_B4为空，|R|≤b+5。R20给原canonical H的两端封闭：没有两外端点都在H的ambient R6，路径内部允许经过R。原canonical G的每点具有ambient入R5和出B5；H-origin R6的起点只能落G。三链接口为：入R5终于a、出R6从a到e、出B5以(a,h)开始时，h≠e会产生禁形。因此在相关三角色下，所有合法出B5第二点都必须等于同一实际R6终点。

## 2. 任意d的统一mixed、终点与非源预算

沿原canonical H、R、G定义

\[
d=2b-|H|,\quad
\Omega=\{w\in R:\text{有ambient R6从H到w}\},\quad
S0=R\cap\operatorname{Src}_{R6}(X),\quad
J0=R\setminus(\Omega\cup S0),\quad B0=H\cup J0. \tag{2}
\]

再取全部混合角色点

\[
M=R\cap\operatorname{Src}_{R6}(X)\cap
\operatorname{End}_{R5}(X)\cap\operatorname{Src}_{B5}(X). \tag{3}
\]

每个s∈M由三链锁定：它的全部出R6终点与全部出B5第二点为同一实际点h(s)。h(M)表示完整像集，此时不预设h(M)在H。令

\[
E^*=\Omega\cup h(M),\quad Y=E^*\cap B0,\quad
K=(B0\cup M)\setminus E^*. \tag{4}
\]

**联合预算定理。** 对全部d均有

\[
|J0|+|M|+|\Omega\cup(h(M)\setminus B0)|\le d, \tag{5}
\]

等价地

\[
|J0|+|M|+|\Omega|+
|h(M)\setminus(B0\cup\Omega)|\le d. \tag{6}
\]

特别|J0|+|M|+|Ω|≤d。该精确式将mixed点、H-origin终点、全ambient非源以及额外像终点放在同一neutral预算中；它不是分别套界后相加。

### 2.1 实际删像核K

前稿已证B0为实际766，且Ω∩B0为空、M∩B0为空。M及任意H-origin源均启动ambient B5，故不属于T=End_R6(X)：若入R6与出B5共点，两色joining给R7或B6。E*⊆T，因而M∩E*为空。

K内的R6若从H启动，其终点必落Ω，因为H—H两端已由canonical封闭排除；若从J0启动，违反其全ambient非源身份；若从M启动，终点必为已删h(s)。所以K无R6，其余禁形遗传，K是实际766，且

\[
|K|=|H|+|J0|+|M|-|Y|. \tag{7}
\]

在这个实际K内重新计算两个角色及其neutral

\[
Z_K=K\setminus\bigl(\operatorname{Src}_{B5}(K)\cup
\operatorname{End}_{R5}(K)\bigr),\quad
|Z_K|\le d-|J0|-|M|+|Y|. \tag{8}
\]

两个角色不交来自joining；删除任一角色后的两个补集分别受756或换色756容量约束，因此得到(8)。没有把K当作新的canonical核。

### 2.2 全部像终点的共同注入

对每个e∈E*，在全部H∪M-origin且终于e的R6中选择最早起点a。若a∈H，则a∈G，有ambient入R5和出B5；若a∈M，则定义直接给同样的两项供应。三链迫a的所有出B5第二点均为e。

a启动B5，故不是R6终点，因而a∉E*且确在K。它不能是K内部B5源，因为那条B5的第二点必须是已删e。若K内部R5终于a，记末前驱f；桥χ(f,a,e)蓝会前接f到B5形成B6，故桥红。把e接到该入R5后便得到首点早于a、仍终于e的R6。新首点若在J0，违反全ambient非源；若在H∪M，违反对同e的最早选择。因此a也不是K内部R5终点，故a∈Z_K。

不同e不能选择相同a：固定a的任意一条B5，其第二个实际点不可能同时等于两个不同e。所以E*注入Z_K，结合(8)，再取消Y=E*∩B0，就得到(5)—(6)。这是对同一实际核的全像终点注入，完整保留替代供应与共享。

### 2.3 d=0与d=1的准确机制

d=0时，(6)直接给J0=M=Ω为空，原canonical封闭因此成为全源封闭；残余每点都是ambient R6源。满H插入容量又给每点纯H红5尾。因此上一轮三匹配主证明可用这一共同引理替代分开的R20零缺额与R25混合角色排除；旧文及其保证状态不改写。

d=1时，只允许下列四种机制：

- J0、M、Ω全空。
- 仅J0为单点；前稿已把这一整类提升为满核接口。
- 仅Ω为单点，此时M必空。
- 仅M为单点，此时J0=Ω为空，精确额外终点项又迫h(M)⊆H。

两类例外不能并存。整个Ω非空且M非空的机制类已被排除，但单Ω、单M及全空类仍未全部排除，不能宣称候选|X|=3b+4已被排除。

## 3. 紧割条件下的全部删除点纯核供应

本节沿前稿的五根、τ5、无满链接紧割条件，不声称任意候选都进入此结构。使用前稿中性区D及其内部R5源终集U、V；允许U、V交叠。紧割给L⊆U、N=N_R(L)，且

\[
C=(U\setminus L)\sqcup N,\quad K=D\setminus C,\quad
|K|=b,\quad K\text{禁R5、B6、weak7}. \tag{9}
\]

这里K是换色756满核，与§2临时核K只在各自节内使用；Ω、J0始终是canonical预算集合，不与U、V混名。

**纯核供应定理。** 每个s∈U\L都有实际R5(s,K^4)，其终点属于V\N；每个t∈N都有实际R5(K^4,t)，其首点属于L。

证明第一项。在K+s中，换色756容量迫R5。若它不从s开始，其首点在U∩K⊆L，终点便必须落N_R(L)=N，但N全被删除，矛盾。所以该R5始于s，其余四点全在K，终点属于V\N。

第二项同样在K+t中迫R5。若不终于t，其首点在K或t，并且属于L：K内源点属于U∩K⊆L；若t本身是源，由N∩(U\L)=空也得t∈L。终点却在K，同时必须落N，矛盾。因此该R5终于t，前四点全在K且从L启动。

这给出全部删除点的纯K供应，不是选方便见证的局部陈述；但并不保证跨割R5从L到V\N存在。后一个跨割通道正是完整紧割禁止的边，不能把纯入、纯出供应直接当作它。

## 4. 共点拼接的正确长度与七点实际校准

设Y=(y1,…,y4)支持实际R5(s,Y)，X=(x1,…,x4)支持实际R5(X,t)。若共有有序对p<r，它们在Y中的索引为(i,j)，在X中的索引为(h,k)，则实际拼接

\[
s,\ Y_{\le p},\ r,\ X_{>r},\ t
\quad\text{有 }i-k+7\text{ 点}, \tag{10}
\]

\[
X_{\le p},\ r,\ Y_{>r}
\quad\text{有 }h-j+5\text{ 点}. \tag{11}
\]

第一条属于D内部，禁R6；第二条首点在L、末点在V\N，禁跨割R5。因此

\[
i\le k-2,\qquad h\le j-1. \tag{12}
\]

第二条长度是h−j+5，不是+6。这些索引限制没有证明|X∩Y|≤2；三点共有确实可以发生，不能用无索引的共点自动拼接代替完整路径检查。

给一个实际七点校准。顺序为

\[
s<a<x<b0<y<c<t. \tag{13}
\]

b0是点，与容量参数b区分。三元组全部染红，唯

\[
(s,a,x),\quad(x,b0,y),\quad(y,c,t) \tag{14}
\]

染蓝。这三组各为全序中的连续三点，任意两组最多共有一点，四点不可能含其中两组；任意四点packet至多一个蓝项，而且只可能位于首或末。因此配置满足完整packet条件。

B4不可能，因为其两个连续蓝三元组须共有两点。R6也不可能：七点删任意一点后仍保留至少一条蓝三元组，因为三组蓝三元组总交为空；路径遗传排除红六点。红长≤5、蓝长≤3，故同端长度和≤8，无weak7。

实际K={a,x,b0,y,c}无R5，而

\[
R5(s,a,b0,y,c),\qquad R5(a,x,b0,c,t) \tag{15}
\]

的四点支持共有a、b0、c。仍然没有R5从a到c：该五点区间恰含蓝三元组(x,b0,y)。这否定“共有三点即可无索引自动拼接”的捷径。K仅有五点，不是满b=25的核，更不是临界母体反例；它不撤销上文以饱和容量得到的纯核供应定理。本例为手工理论校准，本轮没有计算枚举声明。

## 5. 四根q=0的集中结构与受限端点缺口

本节仅给双满核q=0分支的已证接口，未排除整个q=0。沿前稿S、T、I、P、Q、D的定义，有

\[
I=E=F,\quad|I|=4,\quad|P|=|Q|=|D|=b,
\quad H=Q\sqcup D,\quad H'=P\sqcup D,\quad|H|=|H'|=2b. \tag{16}
\]

P、Q均为756，D是换色756，禁R5、B6。满核角色分划给

\[
\operatorname{Src}_{B5}(H)=D,\quad\operatorname{End}_{R5}(H)=Q,
\quad\operatorname{Src}_{R5}(H')=P,\quad\operatorname{End}_{B5}(H')=D. \tag{17}
\]

每个p0∈P都有R5(p0,D^4)：D+p0超过换色756容量，迫出R5，而首点只能是p0，因为H′内部全部R5源是P。反序同理，每个q0∈Q都有R5(D^4,q0)。p0、q0在这里表示实际点，q=0仍是分支参数。

每个d0∈D又有B5(P^4,d0)与B5(d0,Q^4)：P+d0、Q+d0超过756容量而无R6，迫B5。前一条终点只能是d0，因为S无ambient B5终点；后一条首点只能是d0，因为T无ambient B5源。

每个e∈I都有

\[
R6(P^5,e),\qquad R6(e,Q^5). \tag{18}
\]

P+e⊆S无B5且超过b，756容量迫R6，终点只能是e，因为P避开T；反序给后一项。

原向canonical G为空。原满核证明给G⊆Src_B5(H)=D，但D每点都结束H′内部B5；unrestricted P+末点fan禁止P+点结束ambient B5，而G⊆P+，所以G为空。反向同理。因此仅在本q=0分支，canonical结构集中为S=P+、H=P−，不能把这项识别迁移到其他q或一般重分划。

任取e_i<e_j，取前者纯前供的末前驱p0、后者纯尾的第二点q0。R7禁形分别给

\[
\chi(p0,e_i,z)=B\ (z>e_i),\qquad
\chi(z,e_j,q0)=B\ (z<e_j). \tag{19}
\]

于是实际B4(p0,e_i,e_j,q0)成立。如果还能迫出同一实际p0→q0的R5，就会形成weak7。但目前四组纯P/D/Q供应没有给这些受限端点的R5，不允许直接拼接成同端禁形。本节的集中结构因而仍是条件接口，并非q=0整类排除。

### 5.1 所有点对线性扩张只会回到原满分解

这是已闭合的操作障碍，与q=0实际配置是否存在分开。固定上述同一个实际全序与着色，任取点对偏序的线性扩张λ，重作canonical分解，均不能经既有提升得到不同的满核。

S=P⊔I每点都是ambient R6源，不能落P−，否则前接fan产生R7，所以S⊆P+。D每点结束ambient B5，不能落P+，否则追加fan产生B6，所以D⊆P−。Gλ的点同时结束ambient R5、启动ambient B5：S上的M为空，D不在P+，Q⊆T又禁止ambient B5源，故Gλ为空。

因而只有Q在P+的部分可以变动。记Q+=Q∩P+，则Rλ=S⊔Q+、Hλ=D⊔(Q\Q+)。D7容量给b+4+|Q+|≤b+5，所以|Q+|≤1。若Q+为空，就是原分解。若Q+={j}，Hλ包含于原H，而原H不含ambient R6源，故Ωλ为空；全部实际源仍恰为S，J0λ={j}。前稿已证的联合缺额提升把j加回核，恰好回到原H=D⊔Q与原S。

所以所有λ只得到原满分解，或一步提升后归回原满分解。“只改λ便自动逃出q=0”的操作路线已完整排除；此结论不排除q=0实际配置，也不排除改变全局有效chart或非canonical重分块，不能计为新上界。

## 6. 竞争路线：允许全部multi-private的完整结构二分

设p≥3，实际配置禁B_(p+1)、R_(p+2)及同端R_(p+1)+B3。取所研究完整路径角色约束族F：红成员为实际R_(p+1)，每个必须同时遇K、Y；蓝成员为实际B_p，每个必须遇K，K⊔Y为全体顶点。假设F为UNSAT，且其红族横截数τ=p。这里F可以是所研究的完整约束子族或MUS，所有成员都保留。

令ℬ为F全部大小p的最小红横截。每个S∈ℬ都成为实际蓝p：置Y=S即可满足全部红约束，UNSAT迫一条蓝p全落S。因此任意红成员与任意基候选S恰交1或2点；若交三点，同一实际三元组会因路径遗传同时红蓝。

必须区分量词：τ=p指F的红族，不是79点母体全部R6的横截数。对于候选|X|=3b+4，母体全部R6横截数至少

\[
\tau_{R6}(X)\ge |X|-2b=b+4. \tag{20}
\]

所以p=5的竞争路线仅针对局部约束族，不给全局z删除界。

### 6.1 情形I：全部最小横截满足基交换

若ℬ满足基交换，则G=∪ℬ上得到秩p拟阵。前稿circuit≤3及秩一、秩二直和分块的论证仍适用：基是实际蓝p，B+x不能是蓝p+1，故其红三元组把fundamental circuit压到至多三点；两个相交的不同二点基支持会产生四点circuit，因而二点支持两两不交，得到秩1或2的直和块。此处不再假设唯一private。

对于基S和s∈S，fundamental cocircuit的正确式为

\[
C(S,s)=\bigcap\{A\in F_R:A\cap S=\{s\}\}. \tag{21}
\]

它含s，因为单点替换成功当且仅当新点命中全部s-private红成员。该集合是某条实际红路径的子集，因而是红clique且大小≤p+1，但不必本身是完整红成员。

秩二块仍全红：来自三个不同parallel classes的三元组是circuit，故红；至多占两个类的三元组落在删去第三类的某个fundamental cocircuit中，也红。秩一块自身亦是cocircuit而红。所以各块G_i均为实际红块，秩1或2，且

\[
|G_i|\le p+1,\qquad\sum_i r(G_i)=p,\qquad
\mathcal B=\text{各块基的product},\qquad |G|\le p(p+1)-1,\qquad
\text{若有秩二块，则 }|G|\le p^2-1. \tag{22}
\]

先由块大小与秩总和得到粗计数|G|≤p(p+1)。若取等，必恰有p个秩一块且每块均有p+1点，全部product基为蓝。三匹配主稿附录A的完整product几何引理遂给矛盾：取最早红块A，其他块的任意横截D不能全在A单侧，且在A跨度内至多一点；这迫唯一另一块B全在A内部、其余全在A右侧，再用max A与其余块点构成全在B右侧却可处处蓝延拓的D′，违单侧引理。这里只需这些实际红块与全部蓝product，不要求它们是整个红族。因此一般强化为|G|≤p(p+1)−1。若有秩二块，则块数≤p−1，还直接有|G|≤(p−1)(p+1)=p²−1。

每个原红成员A的G-trace含至少一个块的cocircuit：命中全部基等价于补集不满秩，直和中必有一块失秩。其拟阵秩至多2；否则一组三个独立红点可扩到蓝基，矛盾。选择trace所含的一个块cocircuit，得到准确两型。若所选cocircuit位于秩二块，它已有秩2，trace不能再含任何块外点，但可在该块内再含被删parallel class的一部分点。若所选cocircuit位于秩一块，它就是整个块；trace在该块之外至多再占一个其他块的秩一子集，即另一秩一块的任意子集，或某秩二块单一parallel class的子集，不能同时占两个额外块。类型的选择不必唯一。G外点及全部额外红约束仍保留，没有因拟阵表示而删除。

与上一稿处处unique-private不同，这里的cocircuit可以短于p+1；短cocircuit与外部供应尚未被排除，不能再以每块恰p+1的product矛盾覆盖此支。

### 6.2 情形II：完整基交换失败

若不满足基交换，取S、T∈ℬ及s∈S\T，使对每个x∈T\S，S−s+x都不是红横截。对每个s-private完整红成员A取trace A∩T。每个trace非空、大小≤2，且包含于T\S。所有候选替换失败，等价于这些trace的总交为空；这一量词覆盖全部private红成员，不是只挑一个blocker。

非空且大小≤2的集合族总交为空，必有两条不交trace，或有三条trace恰为{x,y}、{y,z}、{z,x}。证明：若无不交对，则所有两两相交；若有singleton，它会成为公共点，矛盾。否则取两个不同二元集xy、yz，为排除公共y必须有xz，于是得到三角。

因此一次完整交换失败由至多三条实际private红路径同时阻挡全部候选。三角情形中，xyz属于蓝T，而sxy、syz、szx都是红；完整packet条件迫s在[min{x,y,z},max{x,y,z}]之外。若s在内部，唯一蓝项会在packet中间，产生两次换色。

相应实际支持大小满足

\[
\text{两条不交trace型}\le4p-2,\qquad
\text{三角trace型}\le5p-6. \tag{23}
\]

S∪T至多2p点。两条型每个红成员已含s与至少一个T点，新增至多p−1，共至多4p−2；三角型每条已含s与两个T点，新增至多p−2，共至多5p−6。这些是一次完整交换失败的证书规模，不是小UNSAT核。S、T必须仍是原F中的全局最小横截，不能只在选出的少数红成员内重算最小性。

两种情形穷尽全部τ=p、多private完整角色族，但两支仍有开放结构，不登记新的z或数值。先保留(22)—(23)参数式，最后代p=5：拟阵型|G|≤29，若含秩二块则≤24；两条与三角交换失败证书分别至多18、19点。这些数均不是新的极值上界或临界母体反例规模。

## 7. 收益分账、精确靶点与证据边界

本轮核心新结论是§2任意d的统一联合缺额定理，并完整排除mixed、H-origin终点、非源例外共同超出同一d预算的机制。d=1下Ω与M共同非空的整个类因此不可能。紧割全部删除点的纯核供应、q=0集中结构、q=0固定全序/着色下全部λ归回原分解，以及允许所有multi-private的竞争完整二分，也都有明确的已证范围；它们尚未联合排除整个临界候选。

七点例只否定无索引的局部拼接捷径，是方法校准与纠错，不是原极值目标的反例。十八、十九点只是单次完整交换失败的支持证书上限，二十九点及含秩二块时的二十四点只是拟阵地集界；不能将它们写成小UNSAT核、全局z界或新临界构造。

旧757与766链及上一轮工作草稿保持

\[
N757\le a+b-1,\quad C766\le2b,\quad
N767\le3b+4,\quad N777\le3b+5. \tag{24}
\]

代a=16、b=25仍为

\[
40/50/79/80. \tag{25}
\]

上一轮79/80属于未正式接受的工作证明草稿，历史40/50/80/81及原接受/assurance保持。本轮全局新增收益0。若未来完整排除|X|=3b+4，才可得

\[
N767\le3b+3,\quad N777\le3b+4;
\qquad b=25\text{时为 }78/79. \tag{26}
\]

(26)只是未证目标。本稿不能称新上界突破。

下一步优先研究满K的全核覆盖或合法极值交换、四根分支受限同端端点的attainment，以及统一预算后单Ω、单M与全空三类。任何新交换都须同时检查两块的全部路径帽；已排除的全邻域补集交换及只改λ路线不再重复当作候选逃逸。对竞争二分，必须保留原完整F及全局最小横截量词：拟阵型的短cocircuit与G外供应仍开，非拟阵型的至多三条private阻挡也尚非UNSAT结论。

本轮只新增本文及 [文档检查回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_tight_cut_joint_neutral_20261029/DOCUMENT_CHECK.json>)。全部本地引用使用尖括号包裹、含字面空格的真实绝对路径。PowerShell检查仅记录文档文本、UTF-8、本地目标、公式界定符与编号、固定数值代入；不是科学执行、独立数学审阅或接受依据。

所有新增unreviewed/unaccepted，手工生成核对非独审；外部服务、外审、研究程序、枚举、SAT、solver与证书重放均为0。旧稿、接受/assurance、任务metadata、配置、sealed证据和运行保持，本稿不宣告长期研究完成。
