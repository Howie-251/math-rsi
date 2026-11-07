# N7：78/79 接口核查、加权 through 稳定性与下一临界层

日期：2026-10-31。状态：**工作证明；全部新增 unreviewed/unaccepted，未独立审阅、未接受**。本文忠实转写主会话确定、批准的同会话手工接口核查与新数学。既有原生 Sol/high 文档执行者只负责转写及文档一致性，不自行研究、补证或承担独立 review。生成协作者互检与 `PASS_DOCUMENT_ONLY` 均不是独立数学验证，不升级旧接受或 assurance 状态。

本轮同会话逐接口手工核查**未发现阻断性缺口**，这一结论保持同会话核查的保证层级。新的全模型参数工作定理为

\[
\boxed{|X|+w(X)\le3b+3\quad\text{对每个 767 配置 }X.} \tag{1}
\]

其中 w由全部 ambient 红六源终之外的中性区定义，见 §1。它加强结构稳定性，**不再降低无条件 78/79**。本稿完整证明任意 w下的换核归一化、两 η1、混合 η及两 η0排除，保留 η0情形可能存在的共同根。下一层只排双满标准接口中 e+f≥8的机制；其余明确低根组合与亏二机制仍未关闭，77/78尚未成为全局工作界。

唯一新增文件为本文及 `tmp/n7_7879_audit_weighted_through_20261031/DOCUMENT_CHECK.json`。旧两稿、其他旧稿、task.json、metadata、接受/assurance、指针、运行、CNF、proof、runtime均保持；不提交、不归档。主会话未调用外部Claude、未对外发送研究材料，仅只读核对既有公开文献PDF，见§1；文档执行者本人未调用外部服务。未执行科研代码、枚举、SAT、solver、证明器或证书重放；PowerShell仅作文档操作与检查。

## 1. 模型、极值含义与原始依赖

模型为完整有序 rank-3 signotope。对 a<b<c<d，packet按 abc、abd、acd、bcd排列，至多换色一次。单色路径按**实际点数**计长，连续三元组同色决定实际路径，路径对子序列遗传。weak7比较同一对实际首末点的反色路径，长度和至少9，内部允许共享。

767禁 R7、B6、weak7；766禁 R6、B6、weak7；756禁 R6、B5、weak7，换色模型禁 R5、B6、weak7。b为756及换色模型共同有效容量。D7指无B5、无weak7且内部 End_R5∩Src_B4为空的实际配置，容量至多b+5、R6横截数至多5。

N_sig是相应完整模型的**最大人口容量**，不是“必出现禁形的最小阈值”。因此排除大小 M的全部配置、结合原≤M界，才得到容量≤M−1；数值传播不另添或漏减一个点。

对任意767 X，始终用全部 ambient角色定义

\[
S=\operatorname{Src}_{R6}(X),\quad T=\operatorname{End}_{R6}(X),\quad
D=X\setminus(S\cup T),\quad
U=\operatorname{Src}_{R5}(D),\quad V=\operatorname{End}_{R5}(D),\quad
C_0=U\cap V,\quad w=|C_0|. \tag{2}
\]

Src、End在注明的实际点集内部计算，ambient才指X。所有through点实际属于D，所以不在S或T中。

直接依赖及其适用范围：

- [78/79 全局工作界稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_DEFECT_ONE_PREDECESSOR_COMPRESSION_AND_GLOBAL_BOUND_20261031.md>) §2—8：canonical d0/1穷尽、有效W、完整port、跨H0根扇、两/一末前驱压缩及共享pair的R8。
- [纯核根分离与单侧满标准稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_PURE_CORE_ROOT_SEPARATION_AND_INTERLEAVED_REPARTITION_20261030.md>) §1—3、§7：双满及单侧满标准的实际纯核供应、Hall与小人口处理。
- [旧联合 through 容量稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_JOINT_THROUGH_SATURATION_AND_ORDERED_CUTS_20261030.md>) §1—3：旧全模型 |X|+w≤3b+4、任意canonical缺额的实际D7增广。
- [联合 neutral 与重分划稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_TIGHT_CUT_JOINT_NEUTRAL_AND_REPARTITION_DICHOTOMY_20261029.md>) §1—2：完整三链、原G角色及联合预算。
- [亏一完整外图稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_DEFECT_ONE_JOINT_STABILITY_AND_LINKAGE_CUTS_20261029.md>) §4：保留全部B4第二点、实际删点得到的good/Hall。
- [R7 原始工具](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md>) §1—3：实际路径、完整signotope分解、三链与五横截。
- [R20 精确归约](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>) §0—4：合法chart删根、反向实际添点与精确+1。

上述来源保证层级均保持。新加权证明只把**旧**加权式作为入口：

\[
|X|+w\le3b+4,\qquad
N_{\rm sig}(7,6,7)\le3b+3,\quad
N_{\rm sig}(7,7,7)=N_{\rm sig}(7,6,7)+1\le3b+4.
\tag{3}
\]

其中后两个是上一稿的无条件参数工作结论与旧精确关系；本轮不把待证 (1)反向用于自己的入口。

主会话还只读核对既有公开引用 Bergold–Felsner–Scheucher，[*An Extension Theorem for Signotopes*，SoCG 2023](https://drops.dagstuhl.de/storage/00lipics/lipics-vol258-socg2023/LIPIcs.SoCG.2023.17/LIPIcs.SoCG.2023.17.pdf)。原文§1.1、印刷页17:3的正号点对次序为ab≺ac≺bc，负号取反序；§2、印刷页17:5将全部这些关系的传递闭包作为偏序，并引其[9, Lemma 10]。项目R=+、B=−与R7一致。原文packet用逆字典序，项目用正序，整体反转仍保持至多一次换色。这只核对global pair-poset基础接口，不借用几何可实现性；未向该公开来源或其他外部服务发送未发表研究材料。

## 2. 同会话逐接口手工核查账本

下表转写主会话已完成、批准的手工核查结论。结论为“未发现阻断性缺口”，**不是独立review、形式验证或accepted**。旧证明正文保持，不通过改写旧稿掩盖假设。

| 接口与原位置 | 本轮核对的实际逻辑及边界 | 同会话核查结论 |
|---|---|---|
| 全局点对偏序及公开原文 | 正负点对顺序、传递闭包与R7映射一致；packet整体反序保持至多一次换色；只读公开PDF基础接口 | 不借几何可实现，不构成整篇证明独审 |
| 78/79稿§2，canonical分类 | n=3b+4、H0≤2b、R0≤b+5迫d∈{0,1}；同一个联合预算穷尽d0、J1、非Ω/M0、非Ω/M1、单Ω；J1通过实际promotion进入满标准 | 未发现漏类；未把未提升方向预设为满核 |
| 两旧稿的fullstandard接口 | 全部ambient S/T、完整B4延长、mixed禁形均需canonical或真实promotion兑现；任意两块满766不自动够用 | 接口范围保留 |
| 78/79稿§3.3，Ω唯一A_H | 所有H0-origin源的蓝五第二点锁ω；实际W=S∖{ω}为D7，|W|=b+4+|A_H|≤b+5且A_H非空，才得唯一a | 唯一性有容量证明，不是预设 |
| 完整ambient port | W上入R5点若能启动ambient B5，第二点必须在W外；对侧倒数第二点同理；不是只禁内部B5 | 后续跨核B5确可触发该接口 |
| good/Hall完整族 | 全部内部junction、全部B4第二点均保留；删全部good/全部邻点后的实际D7容量给Hall，bad与缺额不能独立多扣一次 | 没有以所选少量路径代替完整族 |
| 中间负缺额 | d_D≤0取空匹配，μ=min(0,d_D)保留；d_D>0才用König cover的d_D−1反证，实际删点数≤副本数 | 无负匹配规模；重叠实际点不重复收费 |
| τ=5与六根 | 满b+5有效W的横截数为5；E/F根数先保留5或6，直到等号链真正迫5 | 未把所有六根当minimum五横截 |
| 双非Ω强制终点 | 两普通末前驱加缺一C迫R6；终点允许等原e_p或等另一个p；删至多另一p后仍保留首p+四C点 | 这些边界没有被擅排 |
| 跨H0新根域 | 通过H0入R5、内部无R6、对侧完整port新证扩张；不从旧T∪V根域借用；Ω时H0并非全局无源 | 根域有独立于旧根域的完整推导 |
| Ω的a∉C/B_H | a不在B_H由锁ω在核外；a若有核内入R5，两色桥给B6或更早H0-origin源，违唯一性 | 修补K=C+a确有b点 |
| Ω终点q与删a | a不属T排q=a；q=e因核/残余实际身份排除；删除唯一a后仍保留首p+四C点，再用跨核扇 | 旧“尾末前驱为a”逃逸已处理 |
| 双Ω精确等号 | cut只迫δ=ε=1、μ=0、w_ω=r=1、n_ν=0、k=e−4；准确位置是ω<f*<ν且f*∈E，不是全E<ν | ω=ν更早即矛盾 |
| 双Ω反序与R8 | 反序后e=f=5，f5=e2、e1=f4；两红五共享同一实际有序pair(x,y)，八点严格有序且无重复 | 拼接使用共享pair，不是共享单点自动拼链 |
| 单侧满原纯核供应 | 满Z'+t或Z+p的实际容量迫纯供；端点由全ambient S/T定义定位；严格根分离后先计数，再使用u−1/q−2等链数 | 没有负的小q链接；任意H尾未冒充完整纯核尾 |
| 本轮η0加权根序与探索修正 | 临时过强候选F<E已修正为maxF≤minE，允许至多一个共根；对偶强化fan先于根序独立证明；t∈C0只给弱序，单满u≥2、双满u≥3后才计链 | 同会话Ω协作者逐式交叉核对；不是独审；旧78/79稿w=0无增广C，其严格分离仍有效，不是旧稿漏洞 |
| 最大人口与R20 | N为最大允许人口；R20仅用已证合法chart及反向实际添点给精确+1，不用任意pivot | 未发现off-by-one或chart范围扩张 |
| b=25输入状态 | 本轮未读新证书、未核验证书；25继续是既有用户授权工作输入，用户报告UNSAT/证书验证中/旧accepted三层保持 | 不把输入状态冒充独立验证 |

因此本轮继续保留78/79为**未独审、未接受的参数手证工作界**。这个账本只记录同会话已完成核查，不替代独立数学审阅。

## 3. 任意缺额的实际换核归一化

### 3.1 反设加权取等及η预算

反设旧加权上界取等，记 n=|X|，n+w=3b+4。任取原canonical X=H0⊔R0，定义原Ω、J、M与三链锁h：Ω为全部H0-origin红六终点，J=R0∖(Ω∪S)，M=R0∩S∩End_R5(X)∩Src_B5(X)。置

\[
d=2b-|H_0|,\quad
M_R=\{m\in M:h(m)\in R_0\setminus J\},\quad
j=|J|,\quad m=|M_R|,\quad
g=\left|\Omega\cup\bigl(h(M)\setminus(H_0\cup J)\bigr)\right|.
\tag{4}
\]

旧联合预算及旧实际D7增广 (R0∖(J∪M_R))∪C0给

\[
j+|M|+g\le d,\qquad
n+w\le3b+5-\eta,\qquad
\eta=d-j-m\ge(|M|-m)+g\ge0.
\tag{5}
\]

由取等n+w=3b+4，η∈{0,1}。这里**不限制原d、j、m各自很小**，更不沿用旧n=3b+4时d0/1的分类替代本轮归一化。

### 3.2 换成实际H*与新Ω*

作实际换核

\[
H^*=H_0\cup J\cup M_R,\quad R^*=X\setminus H^*,\quad
\Omega^*=\Omega\cup h(M_R),\quad M^*=M\setminus M_R.
\tag{6}
\]

因为h(M)∖(H0∪J)=h(M_R)，有|Ω*|=g。Ω*⊂T；M_R各点启动B5，不能是R6终点，故M_R∩T为空。原Ω又与H0、J不交，因此Ω*确在R*中。

全部H*-origin R6若从H0启动，终点在原Ω；若从M_R启动，终点在h(M_R)；J点是全局非源。所以全部这类终点都在Ω*，H*内部无R6，继承B6/weak禁形而为实际766。全部这些源仍有ambient入R5、出B5：来自原G角色或M_R定义，可使用三链。

\[
|H^*|=2b-\eta,\quad
R^*\setminus\Omega^*\subseteq S,\quad D\subseteq H^*,\quad
h(M^*)\subseteq H_0\cup J\subseteq H^*,\quad
\eta\ge|M^*|+|\Omega^*|.
\tag{7}
\]

M*恰为剩余残余mixed族；不能混淆原Ω与新Ω*。尤其原Ω为空但M_R非空时，可以转成新Ω*非空，不能称H*全局source-free。

η=0时g=0，M_R若非空其像会使g≥1，故M_R也为空；随后M*、Ω均空。H*=X∖S满2b且全局无R6源，R*=S，完整延长与mixed接口真实兑现，成为fullstandard。

η=1时|H*|=2b−1、|R*|=b+5−w，由(7)只剩：新Ω*=∅且M*为空或单点锁H*；或新Ω*={ω}且M*=∅。

## 4. 有效基底、强化根扇及两η1的通用cut

### 4.1 加回actual through的有效D7

新Ω*=∅时H*=X∖S全局无源，取W=S∪C0，大小b+5。这里包括M*1，需单独兑现D7：S、C0均无ambient B5终点，任B4末点在S或C0可保首pair延长；C0又无ambient B5源。S上的潜在junction只能落在M*，但其B5第二点h(M*)∈H*∩T，既不在S，也不在C0⊂D，故在S∪C0外，内部junction不可能。因此W为实际D7。完整port也由同一个外锁点给出；M*0时这一异常为空。

新Ω*={ω}时，A_H=H*∩S非空，每个a0∈A_H的全部R6终点及全部B5第二点都锁ω。取

\[
W=(S\setminus\{\omega\})\cup C_0
=(R^*\setminus\{\omega\})\sqcup A_H\sqcup C_0.
\tag{8}
\]

S点无ambient B5终点；C0⊂U也无ambient B5终点，故W无B5。任何末点在S或U的B4可保首pair延成B5。W内部junction若在R*∖{ω}会违反M*=∅；若在A_H，第二点锁ω但ω不在W；若在C0，因C0⊂V根本无ambient B5源。故W为D7。

由|W|=b+4+|A_H|≤b+5及A_H非空，得A_H={a}。a启动B5所以a∉T。取δ=1[ω∈S]，统一得到

\[
|W|=b+5,\quad
S=(W\setminus C_0)\sqcup\delta\{\omega\},\qquad
T=(W'\setminus C_0)\sqcup\varepsilon\{\nu\}.
\tag{9}
\]

此处(9)同时列出两η1反向对应基底。无相应端口时δ或ε项按0解释。

完整port保持：r∈W∩End_R5(X)若有ambient B5，其第二点必须在W外，且是T点；C0点根本无B5源，M*或a的第二点分别锁向外部终点。对侧t∈W'∩Src_R5(X)的ambient B5倒数第二点必须在W'外。所有C0⊂D⊂H*，故C0⊂C_H:=End_R5(H*)。

### 4.2 根域与强化跨核扇

两η1时E=End_R6(W)、F=Src_R6(W')，τ(W)=τ(W')=5，5≤e=|E|,f=|F|≤6。保留完整根域W∪U0、W'∪V0，其中U0=U∖C0、V0=V∖C0。根提升仍是：若E点启动蓝三，取W入红六末前驱，禁R7迫蓝桥得到B4，再延B5，其第二点在W内而违完整port；反序同理。因此

\[
E\subseteq I\setminus\delta\{\omega\},\quad
F\subseteq I\setminus\varepsilon\{\nu\},\quad I=S\cap T,
\qquad5\le e,f\le6.
\tag{10}
\]

**强化跨核根扇。** 对f0∈F、x∈C_H、任意ambient y，若x<y<f0且y∉Ω*，则

\[
\chi(x,y,f_0)=R. \tag{11}
\]

反设蓝，取W'内出f0红六第二点t。χ(y,f0,t)红可前接y成R7，所以蓝。取H*内入x红五末前驱d0；若χ(d0,x,y)红，可追加y产生H*-origin R6终于y∉Ω*，矛盾。所以桥蓝，得到B5(d0,x,y,f0,t)。t∈W'且是ambient R5源，倒数第二点f0也在W'，违完整port。

这里y无需属于H*；新Ω*=∅时y可任意ambient。一般情形必须保留y∉Ω*条件，不能擅自删掉。

### 4.3 through点不能作严格低根末前驱

令f*=maxF。任W内终于e0<f*的R6，其末前驱p使χ(p,e0,f*)=B，否则原红六追加f*成R7。若p∈C0，则p∈C_H且e0∈W∩T避开Ω*，(11)又迫该三元组红，矛盾。因此

\[
\text{全部严格低根路径的实际末前驱均不在 }C_0.
\tag{12}
\]

任意w个through点都不增加后文实际击中集合的大小，而非每个through点分别收费。

### 4.4 完整good/Hall及删actual C0一次的中间匹配

W∪U0的junction不能在W：内部B4延成B5后第二点仍在W∪U0，然而其外部锁点是T点，不能在U0⊂D。删全部good后为D7，大小b+5+|U0|−|good|≤b+5，迫全部U0都是good。对侧全部V0同理。

good点u的内部入R5与B4(u,i0,x,y)延长后joining，蓝桥给B6，故桥红产生末pair(u,i0)的实际R6；i0落在(I∖δ{ω})∖E，并带全ambient蓝fanχ(u,i0,z)=B（z>i0）。保留全部这样的第二点。对C1⊂U0，实际(W∖N(C1))∪C1为D7，容量给普通Hall。反向全部V0也有普通Hall。

记i=|I|。由n=3b+4−w及|S|=b+5−w+δ、|T|=b+5−w+ε，定义

\[
d'=|D|-w-b=i-6-\delta-\varepsilon,\qquad
\ell=\max(0,d'),\quad\mu=\min(0,d').
\tag{13}
\]

中间图仅保留端点在U0、V0的全部D内R5。d'≤0时取空匹配；d'>0而最大匹配≤d'−1时，König cover至多d'−1个端点副本。先删actual C0一次，再删cover对应实际点；每条R5若有端点在C0便被前者命中，否则由cover命中。总实际删点至多w+d'−1，余D至少b+1点且无R5，违换色756容量。因此有ℓ条中间匹配。

外匹配覆盖全部U0/V0，可复合全部所选ℓ条边为完整链a0→u→v→b0。若a0<b0，两个全ambient蓝fan给B4(u,a0,b0,v)，与中间实际R5(u→v)同实际端点，违weak7，故b0≤a0。

以A=(I∖δ{ω})∖E、B=(I∖ε{ν})∖F为副本目标层，任cut c得到

\[
|F_{\le c}|-|E_{\le c}|-
\delta\mathbf1[\omega\le c]+\varepsilon\mathbf1[\nu\le c]
\le|A|-\ell=6+\varepsilon-e+\mu.
\tag{14}
\]

这保留全部实际完整链、全部正负缺额及重合端口；没有把actual C0在左右副本重复删除。

## 5. 两η1：双新Ω0与含新Ω1完整排除

### 5.1 双新Ω0：through不增两末前驱成本

H*全局source-free，大小2b−1。C_H=End_R5(H*)至少b−1点，全部无ambient B5源：核内入R5与出B5joining，桥蓝给B6，桥红给从H*启动的ambient R6，矛盾。

考虑所有严格低根E_<f*对应的全部W内R6。(12)先排through末前驱。若出现两个不同的非M*普通S末前驱p1、p2，C_H+p1+p2至少b+1点且无B5、继承weak禁形，容量迫R6，首点只能某p。记其强制终点z、p原对应终点e_p<f*。原入红六末pair的蓝帽与同端weak给z≤e_p，允许z为另一p或等e_p。

强制红六除首p外至多一个非C_H点，所以保留p与四C_H点得R5(p,c1,c2,c3,c4)，c4≤z≤e_p<f*。强化跨核扇(11)接f*，得到R6(p,c1,c2,c3,c4,f*)；原末pair给B3(p,e_p,f*)，同端weak矛盾。

所以普通末前驱至多一个，加唯一可能M*点，全部低根路径由至多ρ=2个实际点击中。令k=|E_<f*|，τ(W)=5给k≤e−3；(14)在δ=ε=0、c=f*处又给

\[
k\le e-3,\qquad
k\ge e+f-7-\mu\ge e-2,
\tag{15}
\]

矛盾。此处Ω指新Ω*；没有将原Ω0但换核后新Ω1误列入本类。

### 5.2 至少一新Ω1：修补K与删除a

不妨Ω*={ω}、M*=∅。H*唯一红六源a不属T。令C_H=End_R5(H*)、B_H=Src_B5(H*)。二者不交且各至少b−1点；a不在B_H，因其蓝五第二点锁ω在H*外。若a∈C_H，取核内入a红五末前驱d0、ambient B5(a,ω,…)；桥蓝给B6，红给比a更早的H*-origin红六源，违唯一性。因此

\[
H^*=C_H\sqcup B_H\sqcup\{a\},\quad
|C_H|=|B_H|=b-1,\qquad K=C_H\sqcup\{a\},\ |K|=b.
\tag{16}
\]

每个c∈C_H若启动B5(c,h,…)，用核内入c红五joining；蓝桥给B6，红桥给H*-origin R6终于h，故h=ω。连同a，K内全部ambient B5源的第二点都锁ω。

任严格低根e0<f*的W内R6，末前驱p先由(12)排除through。若p≠a，则p∈R*∖{ω}，原剩余M*=∅使p无ambient B5源。K+p恰b+1点、没有ω，故无B5；容量迫R6，首点只能p，因为全部H*-origin红六终点ω在集合外。写为

\[
R6(p,z_1,z_2,z_3,z_4,q),\qquad z_i,q\in K.
\tag{17}
\]

q≠a，因为a∉T，所以q∈C_H。原末pair蓝帽与weak给q≤e0；q=e0因核/残余身份不可能：e0∈W∩T，不是a或through，故在R*而q∈H*。于是q<e0<f*。

删除至多一个a，保留首p与四C_H点，得到R5(p,c1,c2,c3,q)。用(11)接f*，与B3(p,e0,f*)同实际端点矛盾。因此全部低根末前驱只能a，ρ=1，k≤e−4。

### 5.3 精确等号与双Ω共享pair的红八

令r=1[f*∈E]、w_ω=1[ω≤f*]、n_ν=1[ν≤f*]；此处w_ω是指标，不是through人口w。由(14)

\[
k\ge e+f-6-\varepsilon-\delta w_\omega
+\varepsilon n_\nu-r-\mu,\qquad k\le e-4.
\tag{18}
\]

故f≤3+δ+ε+μ≤5，而f≥5。唯一边界为δ=ε=1、μ=0、f=5；精确式还迫w_ω=r=1、n_ν=0、k=e−4，即

\[
\omega<f^*<\nu,\qquad f^*\in E.
\tag{19}
\]

不声称全E<ν。ω=ν时指标已矛盾。反侧也为新Ω1，完整反序同证得e=5。正向f5=e2、反向e1=f4；记x=e1=f4<y=e2=f5。E、F各自红五，两条实际红五共享同一有序pair(x,y)，得到

\[
R8(f_1,f_2,f_3,x,y,e_3,e_4,e_5).
\tag{20}
\]

八点严格有序、无重复，连续红三元组来自两红五，子序列给禁用R7。至此两η1全部排除。

## 6. 至少一η0：满核纯前供与非严格根序

### 6.1 η0增广基底、完整根域及反向满核角色

先显式兑现η0的增广接口。正向η0时H*=X∖S满2b，weightedcritical给|S|=b+4−w，故W0=S∪C0大小b+4；反向对应W'=T∪C0也有b+4点。S的标准mixed禁形排除其内部junction，C0⊂U∩V没有ambient B5源或终点；末点在S或U的蓝四可保首pair延长。于是W0无B5、无内部junction，继承weak禁形，为实际D7。W0上的完整port由S标准mixed与C0无B5源给出；反向完全同理。

这些base的完整根域分别是W0∪U0、W'∪V0。证明与§4.2相同：假设根点启动蓝三，取base内入红六末前驱，禁R7迫蓝桥得到B4，保首pair延B5后第二点仍在base内，违反完整port；反序给左根。此处不调用τ=5，删全部根后的756容量只先给根数≥4。故下文的port、完整根域并非借用仅在两η1下列出的结论。

不妨反向η0，则H'=X∖T满2b，且全局无ambient R6终点。令P=S∖T，满核角色给

\[
Z'=\operatorname{Src}_{R5}(H')=P\sqcup U,\quad |Z'|=b,
\qquad Z'\cap\operatorname{End}_{B5}(X)=\varnothing.
\tag{21}
\]

具体地，P点有R6后供，U点有D内R5后供，均不能是ambient B5终点，故落入满H'的Src_R5角色。又|D|=2b−|P|，删除U给|U|≥b−|P|，满角色给反向不等式，故取等并得到完整身份。

### 6.2 强化右扇：第二点可为任意ambient点

设正向有效W具有完整port，E=End_R6(W)。对e0∈E、y∈Z'、任意ambient x，若e0<x<y，则

\[
\chi(e_0,x,y)=R. \tag{22}
\]

若蓝，取W内入e0红六末前驱p；χ(p,e0,x)红可追加x成R7，故蓝。取H'内出y红五第二点z；χ(x,y,z)红可前接x成终于H'的ambient R6，违H'全局无终点，所以也蓝。得到B5(p,e0,x,y,z)，源p∈W∩End_R5(X)、第二点e0∈W，违反完整port。

### 6.3 关键根序只能是maxF≤minE

令e*=minE，F=Src_R6(W')，W'=T∪C0。任取f0∈F及W'内出f0红六第二点t。

若t∈T，反向mixed使t无ambient B5终点。Z'+t有b+1点、无B5且继承weak禁形，容量迫R6；Z'没有ambient R6终点，故其末点只能t，首点p0∈Z'∩S=P，写纯前供R6(p0,z1,z2,z3,z4,t)。

原首pair(f0,t)的全左蓝帽及同端weak迫p0>f0，等号又因P∩T为空排除。若p0>e*，p0,z1∈Z'⊂W∪U0，E的完整右根可前接e*到纯前供前五点，产生终于Z'⊂H'的R6，矛盾。p0=e*因P∩I为空排除，故f0<p0<e*。

若t∈C0，则t∈U⊂Z'。f0>e*时(22)迫χ(e*,f0,t)=R，可前接e*到出f0红六成R7，故只能推出f0≤e*。

合并两类得到

\[
\max F\le\min E,\qquad |E\cap F|\le1.
\tag{23}
\]

**这里不能声称严格F<E**；through作为红六第二点时必须保留共同根。以下cut均为这个可能共根留出一单位。

### 6.4 正η1、反η0的完整链接与矛盾

令U0=U∖C0、V0=V∖C0，u=|U0|、v=|V0|。正向W=(S∖δ{ω})⊔C0有b+5点，反向W'=T⊔C0有b+4点。令I_W=I∖δ{ω}，由(21)得到

\[
|I_W|=u+5,\quad |I|=u+5+\delta,\quad
|D|=b+w+u,\quad v\ge u,
\quad E\subseteq I_W,\ F\subseteq I.
\tag{24}
\]

左侧全部U0 good且普通Hall覆盖U0；目标I_W∖E的大小u+5−e≥u，删E容量又给e≥5，所以e=5、左外perfect大小u。

右侧base W'有b+4点，bad与Hall合计只损一单位，给至少max(0,v−1)条匹配，且f≥4。中间先删actual C0一次后，König迫匹配覆盖全部U0：若最大匹配≤u−1，cover加C0实际删除至多w+u−1，余D至少b+1点且无R5，矛盾。右侧外匹配最多漏一个V0，因此可得u−1条完整链；在使用这一数目之前先由(23)计数：

|I|≥e+f−1≥8，故u≥3−δ≥2。

所以u−1链接规模合法。逐链顺序比较给

\[
|F_{\le c}|-|E_{\le c}|-\delta\mathbf1[\omega\le c]\le1.
\tag{25}
\]

取c=maxF，由(23)知E前缀至多一个点，于是f≤1+1+δ≤3，违f≥4。混合η全部排除，反序亦然。

### 6.5 两η0：两外侧各只亏一单位

两η0时W=S∪C0、W'=T∪C0各有b+4点。满核角色给

\[
|U|=|V|=u+w,\qquad |I|=u+4,\qquad e,f\ge4.
\tag{26}
\]

两外图各至少u−1条匹配，中间删actual C0一次后有u-perfect。§6.2—6.3同证maxF≤minE、共根至多一个。先据|I|≥e+f−1≥7得u≥3，所以u−2完整链数合法。

外匹配的两个V0像各至多漏一个点，中间perfect复合给至少u−2条完整链；由实际同端禁形逐链得b0≤a0，故

\[
|F_{\le c}|-|E_{\le c}|\le6-e.
\tag{27}
\]

c=maxF时E前缀至多1，得到f−1≤6−e，即e+f≤7，与e+f≥8矛盾。两η0排除。

## 7. 全模型加权工作定理及条件传播

反设旧界取等n+w=3b+4，经§3实际归一化，两方向η分别只有0/1。两η1由§5排除，混合η与两η0由§6排除，全部组合覆盖。因此

\[
\boxed{|X|+w(X)\le3b+3\quad\text{对全部767配置成立}.}
\tag{28}
\]

这是完整新证明，不是将旧w=0定理直接换符号。它只用了旧加权3b+4作为入口，不依赖待证加权3b+3的循环调用。

对任意t≥0，w(X)≥t的子类满足|X|≤3b+3−t。对于777母体Z，只取R20已经证明合法的root/chart删根所得767配置Y，|Y|=|Z|−1，得到

\[
|Z|+w(Y)\le3b+4.
\tag{29}
\]

同一母体、同一有效chart运输框架内的全部**已证合法**root charts可取其中最大w；不能把任意pivot宣称为合法。只有某个合法chart具有positive through时，才得到777的相应条件下降。

## 8. 新尾替换工作引理

设对侧W'具有完整port，F=Src_R6(W')。若实际有

\[
R6(v_1,v_2,v_3,x,y,z),\qquad
x\in\operatorname{End}_{R5}(X),\quad f_0\in F,\quad y<f_0,
\tag{30}
\]

则χ(x,y,f0)=R，且R6(v1,v2,v3,x,y,f0)为实际红六。无需z<f0；用于尾端推进时z<f0只是一个充分位置。

证明取ambient入x红五末前驱d0。若χ(d0,x,y)=R，可将y、z接到该红五成R7，故χ(d0,x,y)=B。若χ(x,y,f0)=B，取W'内出f0红六第二点t；χ(y,f0,t)红会前接y成R7，所以蓝。于是B5(d0,x,y,f0,t)，其末点t∈W'且是ambient R5源，倒数第二点f0也在W'，违完整port。

因此χ(x,y,f0)=R。新顺序v1<v2<v3<x<y<f0保证实际路径，其他连续红三元组继承原红六。

本引理不要求x属于某个C_H，可用于亏二全尾结构研究；它尚未排除全部亏二机制，不能把替换能力直接计成新的全局saving。

## 9. 下一临界层：双满标准的大根数整类排除

### 9.1 新界先迫下一层w=0

若|X|=3b+3，由(28)先得w=0。现在**额外要求**双满standard：H=X∖S、H'=X∖T各满2b，延长与mixed禁形已经兑现。此时S、T各b+3点，满核角色给参数q：

\[
|D|=b+q,\quad |U|=|V|=q,\quad |I|=q+3,
\qquad E=\operatorname{End}_{R6}(S),\quad
F=\operatorname{Src}_{R6}(T),\quad e,f\ge3.
\tag{31}
\]

不能把一般下一层配置都假设成双满standard。

### 9.2 纯核根严格分离与外侧亏二

此处没有through额外点，旧满Z+p纯尾给严格F<E，证明完整保留如下。Z=End_R5(H)=Q⊔V满b且无ambient B5源，Q=T∖S。任e0∈E，取S内部终于e0红六末前驱p；mixed禁形使p无B5源。Z+p有b+1点，容量迫R6首只能p、尾五点全在Z，终q0∈Q。原末pair蓝帽与同端weak迫q0<e0。若q0<maxF，Z内最后两点均在T⊔V，F完整左根将去首后的红五追加maxF，产生首点在Z⊂X∖S的R6，矛盾；等号q0=maxF因Q∩I为空排除。因此maxF<q0<e0，对全部E得到严格分离。

S有b+3点。令bad数为k_b，删除全部good后D7容量给k_b≤2。对任意good子集A1，实际(S∖N(A1))∪A1∪bad为D7，给

\[
|N(A_1)|\ge|A_1|+k_b-2.
\tag{32}
\]

good人口q−k_b、Hall缺额至多2−k_b，所以外匹配至少q−2；两侧同理。中间完整D内R5端点图由容量有q-perfect，故可复合至少max(0,q−4)条完整链。

若e+f≥8，严格F<E先给|I|=q+3≥e+f≥8，即q≥5，再正式使用q−4条完整链。逐链同端禁形给b0≤a0，cut在maxF处得到

\[
e+f+(q-4)\le q+3,\qquad e+f\le7,
\tag{33}
\]

矛盾。因此下一层双满standard中e+f≥8整类不可实现，剩余根数组合仅为(3,3)、(3,4)、(4,3)。这只列仍未排除的组合，不声称它们可实现。

### 9.3 当前价值方向与准确开放边界

下一层仍需处理w=0的低根机制及canonical亏二预算；§8完整尾替换提供一种已证工具，尚未兑现全机制排除。另一条方向是合法root cycle能否强迫至少一个合法chart的w>0；若不能得到这样的进入结论，不能将更多必要条件堆积当全局下降。

完整F竞争路线的既有右继红源、全源/全终条件分划均保留，但一般机制尚未闭合，本轮没有独立数值收益。不得因主线加权稳定性就宣称任意更小完整F可满足。

## 10. 研究边界附录：双亏二非Ω/M0的中间根对齐

本节不抢占主加权定理，也不作为全局收益。只考虑双非Ω、两侧canonical亏二d=2、M0、w=0，实际H=X∖S大小2b−2、S大小b+5；反向同理，S、T均为满D7，完整mixed接口已兑现。未将任意其他η2或含Ω亏二机制归入此类。

### 10.1 三个普通低根末前驱被尾替换排除

取C_H=End_R5(H)，则|C_H|≥b−2，且全部无ambient B5源。每个低根普通末前驱都属于ambient End_R5，M0又使其无ambient B5源。

若有三个不同的低根末前驱组成P，C_H⊔P至少b+1点、无B5且继承weak禁形，容量迫R6首点为某p∈P。记原p对应的低根终点e_p<f*=maxF；原末pair蓝帽与同端weak迫强制终点z≤e_p<f*，仍允许z等另一P点或原终点。

强制红六全部点在C_H⊔P中，每点都有ambient End_R5身份，所以其第四点满足§8尾替换假设。用尾替换将末点换为f*，得到首点同为p的实际R6(p→f*)；与B3(p,e_p,f*)同端weak矛盾。因此全部普通低根末前驱至多两个，兑现ρ≤2。这里是亏二的新增尾替换论证，不是把旧亏一的ρ2原样迁移。

### 10.2 双亏二cut的精确等号

两侧满D7的全部U/V good，普通Hall覆盖全部外侧。n=3b+3、|S|=|T|=b+5，i=|I|，中间仍用完整实际端点图，令

\[
d_D=i-7,\quad\ell=\max(0,d_D),\quad\mu=\min(0,d_D),
\qquad |F_{\le c}|-|E_{\le c}|\le7-e+\mu.
\tag{34}
\]

ρ≤2及τ(S)=5给k≤e−3；cut在f*处又给k≥e+f−8−μ，所以

\[
f\le5+\mu. \tag{35}
\]

双方e,f≥5，反序同理，最终e=f=5、μ=0，且严格低根恰两个。写E={e1<⋯<e5}、F={f1<⋯<f5}，精确等号给

\[
\max F=e_3,\qquad \min E=f_3.
\tag{36}
\]

若e2=f4，E/F共享实际有序红三点(e1,e2,e3)，两条红五直接拼成

\[
R7(f_1,f_2,e_1,e_2,e_3,e_4,e_5),
\tag{37}
\]

矛盾。因此整个“双亏二非Ω/M0且中间根对齐”类已排除。

### 10.3 错位分支与饱和核仍只是精确身份

e2≠f4时尚未排除。所缺跨桥χ(f2,e1,e2)或χ(f4,e3,e4)不能由现有根域自动赋红；private根链的外点未必属于对侧域，不能把E∪F一概称为全红。

全部低根普通末前驱的实际集合P0恰有两个点。K=C_H⊔P0无B5；若其中有R6，首点为某p∈P0，原对应低根蓝帽限制其终点，§8尾替换再次产生同端weak。因此K也无R6，为实际756。结合|C_H|≥b−2与容量上界得到

\[
|P_0|=2,\qquad |C_H|=b-2,\qquad |K|=b.
\tag{38}
\]

这只给精确饱和身份，不是额外突破。当前可以区分已排的中间对齐类与仍开的错位中间根类；优先研究剩余低根3/4与错位饱和核。含Ω亏二、其他η2仍需完整路径族的统一处理，不能把全部亏二都列为已排。

## 11. 参数后代数值、核查结果与保证边界

本轮无条件参数工作界保持

\[
N_{\rm sig}(7,6,7)\le3b+3,\qquad
N_{\rm sig}(7,7,7)\le3b+4,
\tag{39}
\]

新增的是带w式(28)，不是另一次无条件人口下降。最后代入既有用户授权工作输入b=25，得到

\[
|X|+w(X)\le78,\qquad
N_{\rm sig}(7,6,7)\le78,\qquad N_{\rm sig}(7,7,7)\le79.
\tag{40}
\]

只有w≥1的767子类才有≤77；只有某个已证合法777删根chart具有w(Y)≥1，才有母体≤78。这些77/78是**条件子类界**，全局77/78仍未证明。

| 本轮事项 | 参数结论或覆盖 | 数值/状态 |
|---|---|---|
| 78/79原证明同会话接口核查 | 未发现阻断性缺口 | 不是独审、不是accepted |
| 新全模型through稳定性 | n+w≤3b+3 | b=25时n+w≤78 |
| 无条件767/777工作界 | 3b+3、3b+4 | 仍为78/79，本轮额外saving为0 |
| positive-through 767子类 | w≥1⇒n≤3b+2 | b=25时≤77，条件界 |
| 合法chart positive-through 777子类 | w(Y)≥1⇒母体≤3b+3 | b=25时≤78，条件界 |
| 下一层双满standard | w=0，排e+f≥8 | (3,3)/(3,4)/(4,3)未排；亏二仍开 |
| 双亏二非Ω/M0 | 普通低根末前驱≤2；排e2=f4中间根对齐 | 错位中间根与其他η2仍开；饱和K身份不另计收益 |
| 完整F一般机制 | 本轮未关闭 | 不另计saving |

b=25的证书本轮没有核验、没有读取新证书；继续作为既有用户授权工作输入。用户报告UNSAT、证书验证中及旧正式accepted状态严格分层，不合并、不升级。

本文全部新增 **unreviewed/unaccepted**。同会话主会话与生成协作者手工核查、局部生成互检及文档`PASS_DOCUMENT_ONLY`均不是独立数学验证。指定native Sol/high仅作转写角色记录，未报告backend/实际effort不作验证结论。

文档回执为 `tmp/n7_7879_audit_weighted_through_20261031/DOCUMENT_CHECK.json`，仅核严格UTF-8、公式号连续唯一、本地链接存在、固定参数数字、旧两稿hash及指定两新路径写入。旧稿、任务metadata、接受/assurance、运行与所有科研产物保持；本轮文档完成不代表长期任务完成。
