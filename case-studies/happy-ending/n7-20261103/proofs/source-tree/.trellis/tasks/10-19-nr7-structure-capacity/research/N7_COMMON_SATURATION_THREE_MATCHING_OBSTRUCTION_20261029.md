# N7：共同饱和的三匹配障碍与单 cut 根链矛盾

日期：2026-10-29。本文为主会话批准内容的中文证明草稿，全部新增数学 **unreviewed/unaccepted**。主会话与生成协作者的推导核对属于生成过程，不是独立审阅。用户本轮明确不调用外部 Claude；外部审阅、独立审阅、科学程序、枚举、SAT、solver、proof checker 与证书重放均为0。本文的文档检查只核文字、链接、公式界定符及有限算术，不认证数学。旧接受、assurance、任务元数据与运行均不变。

主结论是固定 weak 参数7的参数化草稿：若正整数 b 是完整模型756的有效上界，则

\[
N_{\rm sig}(7,6,7)\le3b+4,\qquad N_{\rm sig}(7,7,7)\le3b+5. \tag{1}
\]

代入已接受的限定模型上界 b=25，工作证明链成为40/50/79/80；历史40/50/80/81保留为此前记录。这里的79/80是新草稿推论，尚未正式接受，不把生成结果写成已验收上界。

## 1. 模型、来源与精确命题

X 为有限全序集，三元组着色 χ∈{B,R}。完整有序 rank-3 signotope 条件为：任意 a<b<c<d，packet (abc,abd,acd,bcd) 至多换色一次。B_k、R_k 指 k 个实际顶点的单色路径，长度按顶点计；连续三元组同色，packet 保证其子序列仍同色。weak7 指共享同一对实际首末点的反色路径，长度和至少9；内部允许相交。

N_sig(7,p,r) 是同时禁 B_p、R_r、weak7 的配置规模上界问题。特别767禁 B6、R7、weak7，766禁 B6、R6、weak7，756禁 B5、R6、weak7。换色后的756禁 R5、B6、weak7，也使用同一 b。以下 Src、End 都是指定实际配置内部全部路径的起点、终点集合，标 X 时才指 ambient 身份；删点后须重算。反序同时给出相应对偶论证，不能把反向残余直接称作原顺序下的 D7。

定理假设仅为正整数 b 对756有效，结论为(1)。a=16不参与此新定理，只在旧757推论中使用。数值 b=25 的接受依据是 [C8 人工正式接受](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md>)：其模型范围及 same-family/provisional、exact reviewer backend/model/actual effort 不可验证说明原样保留。它不是极大规模等于25的存在断言。

本稿直接来源为 [R7](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md>) §2—3、[R20](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>) §4—5、[R21](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R21_GLOBAL_CAPACITY_AND_SUPPLY_REALIZABILITY.md>) §2.4与§3、[R25](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R25_GLOBAL_EXTREMAL_STRUCTURE_AND_JOINT_REALIZABILITY.md>) §3.2，以及 [最新残余端点稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_RESIDUAL_ENDPOINT_RIGIDITY_AND_FORCED_ROLE_EQUALITIES_20261029.md>) §3、5、6。旧综合稿只属策略历史，不作证明前提。下文重新给出所需接口，未把旧草稿的保证等级升级。

## 2. 继承工具与 canonical 零缺额封闭

R7 的 canonical 分解给767配置的实际不交并 X=H⊔S0，其中 H 是766，|H|≤2b；S0 是 D7 残余，即禁 B5、weak7，且内部 End_R5∩Src_B4 为空，故 |S0|≤b+5。D7是带此 junction 条件的模型，不是任意禁 B5 的模型。该容量由残余全部 R6 终点是至多六个右红根、六根时删除第二根以外五根即可横截全部 R6、删后应用756得到。canonical P+ 的 fan 还保证：任何 ambient 蓝路径只要末点在 P+，即可在末尾追加该点的 p；早期顶点允许在 P+ 之外。

R7 三链接口是：同点 s 有入 R5、从 s 到 t 的出 R6、以(s,h)开始的出 B5，若 h≠t，则产生 B6、R7或 weak7。实际路径允许共享其他顶点；不能省略第二点与红终点不同的条件。

R20 §5的封闭只用于上述原 canonical H。先由三链逐支排除两外端点都在 H 的 ambient R6，内部点可经过残余。令 L=Src_B5(H)、J=End_R5(H)、Z=H\(L∪J)。joining 给 L∩J=∅，两个补集分别属756及其换色模型，所以 |Z|≤2b−|H|。对每个 H-origin R6 的残余终点，选最早 H 起点；R20 §5.4 用三链及同终点下降证明该起点落在 G∩Z，且不同实际终点注入不同停止点。这是按终点的单射，保留全部替代路径，不是假设供应唯一。

于是 |H|=2b 时 Z为空，ambient R6不能从 H 启动。残余中非 ambient R6源的点加入 H 后仍为766，容量又迫这批点为空。因此

\[
S0=\operatorname{Src}_{R6}(X),\quad
\forall s\in S0\ \exists R6(s,H^5). \tag{2}
\]

最后一句亦可逐点看：H+s 有2b+1点，必含 R6；首点只能是 s，其余五点全在 H。反序得到终点侧。此处没有把任意重新分划所得满核代入 canonical 封闭。

任一实际满766核 K、|K|=2b 都满足两组完整分划

\[
\operatorname{Src}_{B5}(K)\sqcup\operatorname{End}_{R5}(K)=K,
\quad
\operatorname{Src}_{R5}(K)\sqcup\operatorname{End}_{B5}(K)=K, \tag{3}
\]

各族均有 b 点。证明第一式：两个角色重合时，入 R5 与出 B5 的桥色给 R6或B6，故不交；删除任一角色后分别禁 B5或R5，两个补集各至多 b。满核2b遂迫无 neutral、两族各 b；换色给第二式。

还需 R25 的混合角色禁形

\[
S\cap\operatorname{End}_{R5}(X)\cap\operatorname{Src}_{B5}(X)=\varnothing, \tag{4}
\]

其中 S 是(2)的 canonical 全源残余。短证如下。若 s 具有三角色，三链迫全部出 R6终点与全部出 B5第二点为同一 h；纯 H 尾保证 h∈H。实际换点 H_s=H−h+s：旧 H 点不能启动 ambient R6，从 s 出发者全终于已删 h，所以 H_s 是满766；s又不能启动内部 B5。由(3)，有内部 R5终于 s，前四点在旧 H。记末前驱 r，取任一 B5(s,h,…)；桥 χ(r,s,h)蓝则前接 r 得 B6，红则将 h 接到入 R5后，得从旧 H 启动的 R6，均矛盾。这一论证保留所有替代供应。

## 3. 共同取等与中性区的两组人口

旧分解已给 N767≤3b+5。因此只须排除 |X|=3b+5。此时正反两次分解均取等，令

\[
S=\operatorname{Src}_{R6}(X),\quad T=\operatorname{End}_{R6}(X),
\quad |S|=|T|=b+5,
\quad H=X\setminus S,\ H'=X\setminus T,
\quad |H|=|H'|=2b. \tag{5}
\]

S是原序 D7，T在反序下是 D7。定义 I=S∩T，P=S\T，Q0=T\S，D=X\(S∪T)，并写 q=|I|−5，则

\[
|I|=5+q,\quad |P|=|Q0|=b-q,\quad |D|=b+q,
\quad H=Q0\sqcup D,\quad H'=P\sqcup D. \tag{6}
\]

T不能启动 ambient B5：把其入 R6的末前驱与出 B5连接，红桥得 R7，蓝桥得 B6。故 Q0 不在 Src_B5(H)，由(3)落在 End_R5(H)。该族有 b 点，所以 q≥0，且其落 D部分恰 q 点。

令 U=Src_R5(D)、V=End_R5(D)。V包含于上面的 q 点；另一方面删除 V 后 D无 R5，又禁 B6、weak7，换色756给 |D\V|≤b，故 |V|≥q。反序同理得

\[
|U|=|V|=q. \tag{7}
\]

本文允许 U、V相交；没有使用 w0 或 U∩V为空。又令

\[
E=\operatorname{End}_{R6}(S)\subseteq I,
\qquad F=\operatorname{Src}_{R6}(T)\subseteq I. \tag{8}
\]

E是原序右根，F是反序右根、即原序左根。它们始终是全部实际路径端点集，不是任选五点横截。

## 4. 从容量迫供应，再得两侧匹配

取 W=S⊔U。W每点都不能结束 ambient B5：S点有出 R6，joining 即给 R7或B6；u∈U有 D内部出 R5，若接入 B5，蓝桥延长成 B6，红桥把 B5末前驱接到该 R5前，得终于 D的 R6，违反 D∩T为空。

每条末点在 W的 ambient B4都可保留首 pair 延长为 B5。末点在 S时用 canonical P+ fan；末点是 u∈U时，追加其 D内部 R5的下一点，红桥会形成终于 D的 R6，故桥必蓝。于是 W内部 B4源同时是 ambient B5源。由(4)，W内部 junction只能落 U。

对每个 u∈U，S+u 有 b+6点，禁 B5、weak7；如果 u不是内部 junction，就根本没有 junction，成为超过 b+5的 D7，矛盾。故每个 u均有实际

\[
R5(S^4,u),\qquad B4(u,S^3). \tag{9}
\]

这是存在完整供应；后续全图仍保留全部混合路径，不以所选纯路径替代它们。

旧残余根论证给 |E|≤6，删除 E后 S\E属756，又给 |E|≥5。现在将右根提升到整个 W。取 S内部终于 e∈E的 R6，末前驱 r∈S∩End_R5(X)。若 W有 B3(e,x,y)，桥 χ(r,e,x)红则得 R7，蓝则得 B4(r,e,x,y)，再延长为从 r启动的 ambient B5，违反(4)。所以

\[
e<x<y\text{ in }W,\ e\in E\quad\Longrightarrow\quad\chi(e,x,y)=R. \tag{10}
\]

对任意 W内部 B4(u,i,x,y)、u∈U，先延长为保首 pair(u,i)的 B5。取(9)的入 R5，末前驱 r；桥 χ(r,u,i)蓝会前接 r产生 B6，故红，得到实际 R6，其最后一对为(u,i)。于是 i∈T∩W=I；而 B3(i,x,y)结合(10)又排除 i∈E。

定义完整二部图 G：u—i当且仅当 W存在 B4(u,i,x,y)。全部邻点均在 I\E。对任意 C⊆U，删除全部邻点 N_G(C)，考察实际诱导集

\[
V_C=(S\setminus N_G(C))\sqcup C. \tag{11}
\]

它禁 B5、weak7。junction在 S则由 B4延长违反(4)；在 C则其 B4第二点已被全删。因此 V_C是 D7，容量给

\[
b+5-|N_G(C)|+|C|\le b+5,
\qquad |N_G(C)|\ge|C|. \tag{12}
\]

C=U时，q≤|I\E|=5+q−|E|，联立下界得 |E|=5。因此 A=I\E有 q点，Hall给完美匹配 α:U→A。每条匹配边都有上述实际 R6最后 pair(u,α(u))，故

\[
\chi(u,\alpha(u),z)=B\quad\text{对所有 ambient }z>\alpha(u), \tag{13}
\]

否则把 z接到那条 R6后就成 R7。反序完整重做，得 |F|=5；B=I\F也有 q点，完美匹配 β:B→V，b0<β(b0)，见证是实际 R6的第一 pair(b0,β(b0))，从而

\[
\chi(z,b0,\beta(b0))=B\quad\text{对所有 ambient }z<b0. \tag{14}
\]

b0是实际点，与容量参数 b不同。这两式是全 ambient fan，不只是匹配路径内的颜色。

## 5. 第三匹配：允许 U、V交叠的全部红五点端点图

在 U、V的二部副本之间，以全部 D内部 R5的实际首末点为边。对 C⊆U，记此图全部邻点为 N_R(C)。删除

\[
(U\setminus C)\cup N_R(C) \tag{15}
\]

会命中每条 D内部 R5：首点不在 C时已删首点，否则已删终点。若 |N_R(C)|<|C|，删除并集的规模至多 q−|C|+|N_R(C)|<q，即使 U∩V非空也成立。剩余超过 b点且禁 R5、B6、weak7，违反换色756。因此 Hall成立，可取完美匹配

\[
\rho:U\longrightarrow V,\qquad
\text{每个 }u\to\rho(u)\text{由实际 D内部 R5见证}. \tag{16}
\]

二部副本只是记账；实际路径首末点严格有序，故无自边。不同匹配边的路径可以共享内部点，本证明不要求其顶点不交，也不要求 U、V的实际并集有2q点。

## 6. 三匹配的顺序障碍

定义同一 I上的等势补集之间的双射

\[
\varphi=\beta^{-1}\circ\rho\circ\alpha^{-1}:A\longrightarrow B. \tag{17}
\]

固定 u，写 a=α(u)、v=ρ(u)、b0=β^{-1}(v)。若 a<b0，则 u<a<b0<v。由两个全 ambient fan，χ(u,a,b0)=B、χ(a,b0,v)=B，所以实际 B4(u,a,b0,v)成立。而(16)给同一对实际端点 u、v的 R5，4+5=9，恰为 weak7，矛盾。因此

\[
\varphi(a)\le a\quad\text{对所有 }a\in A. \tag{18}
\]

任意 cut c，φ把 A的≤c前缀注入 B的≤c前缀，故 |A_≤c|≤|B_≤c|。在同一个实际 I中取补集，得到

\[
|E_{\le c}|\ge|F_{\le c}|\quad\text{对每个 cut }c. \tag{19}
\]

这是通过三组实际匹配与同端 weak比较得到的前缀支配，没有 owner收费、唯一见证或不同母体的最优值拼接。

## 7. 一个 cut上的 private 根链矛盾

写 E={e1<e2<e3<e4<e5}、F={f1<f2<f3<f4<f5}。旧五横截给 τ_R6(S)≤5；若小于5，删后至少 b+1点且属756，矛盾，所以 τ_R6(S)=5。E因而是最小横截，存在 e2-private 的 S内部 R6：它终于 e2，避开其他 E，首点记 a*。

若 a*>e1，由 e1右根性质可前接 e1得到 R7，故 a*<e1。该 private R6与 B3(a*,e1,e2)若并存，会共享实际端点并成 weak7，所以 χ(a*,e1,e2)=R。结合 E右根得到实际

\[
R6(a*,e1,e2,e3,e4,e5),\qquad a*<e1. \tag{20}
\]

反序相同论证给实际

\[
R6(f1,f2,f3,f4,f5,b*),\qquad b*>f5. \tag{21}
\]

现在只取一个 cut c=e2。由(19)，|F_≤e2|≤|E_≤e2|=2，故 e2<f3。于是七个不同且有序的实际点

\[
a*,e1,e2,f3,f4,f5,b* \tag{22}
\]

形成 R7：首连续三元组由(20)；中间(e1,e2,f3)、(e2,f3,f4)因 E、F⊆I⊆S而由 E右根染红；(f3,f4,f5)与(f4,f5,b*)由(21)。这与767矛盾。

若 q=0，三组匹配均为空，A=B为空而 E=F，(19)仍有效；仍通过(20)—(22)的同一根链产生矛盾，不能把空双射的前缀式本身说成矛盾。至此整个 |X|=3b+5共同饱和被排除；没有另设 q数值范围或角色预算。

## 8. 数值传播、依赖边界与第二单位

排除唯一旧上界取等规模后，N767≤3b+4。R20 §4的既有合法 root/chart 恒等式 N777=N767+1给 N777≤3b+5，故(1)成立。旧链 N757≤a+b−1、C766≤2b分别保留；a16、b25代入为

\[
N757\le40,\quad C766\le50,\quad N767\le79,\quad N777\le80. \tag{23}
\]

这是草稿工作推论。几何 ES(7)通过 F+1仅给≤81，不是≤80；本文不作文献原创性或优于已发表几何结果的主张。历史40/50/80/81不改写，接受状态不变。

| 证明依赖 | 本稿实际调用 | 保证与新增归属 |
| --- | --- | --- |
| R7 §2—3 | canonical分解、unrestricted fan、三链、D7≤b+5、五横截 | 继承旧证明及原保证等级 |
| R20 §5 | 原canonical满H的H-origin终点注入neutral Z、零缺额封闭与纯H尾 | 有范围的旧工具，非任意重分划封闭 |
| 满766角色分划、R25 §3.2 | 两补集容量与实际换点排混合角色 | 上文复述所需短证，保留旧来源 |
| R21 §3与§2.4 | D内U/V人口、private根链 | 参数化复用，未要求U/V不交 |
| 最新残余端点稿§3、5、6 | singleton供应、右根lift、全第二点图Hall、E/F恰五 | 本文给不含w0和角色预算的等价重推 |
| 本稿§5—7 | 第三Hall、匹配同端weak、单cut根链 | 本轮新增，unreviewed/unaccepted |
| C8接受、a16、R20§4 | b25数值、旧757数值、root传播 | a16仅用于757；新定理本身只需b |

本证明不使用 Through14、Joint17、Closure、C49、m/m′、数值 q范围、w0或 U∩V为空，也不使用 universal z≤4。它未证明 C49、D29或第二单位 Q78。下一单位须处理总缺额1的三类容量账本

\[
(2b-1,b,5),\quad(2b,b-1,5),\quad(2b,b,4). \tag{24}
\]

这些分支需要新的稳定性，不能将本稿满 H、满残余的角色等式及 canonical零缺额封闭直接套用。

## 9. 竞争路线：全邻域残余交换的补集必失败

本节与三匹配正面闭合区别开来。一般换点事实如下：设 H对每个 a∈A⊆X\H均有纯 H的 Rℓ尾；若非空删除集 C⊆H满足 max C<max A，则 max A的尾全部在其后，不会遇到 C。因此(H\C)∪A保留该 Rℓ，不可能成为禁 Rℓ的核。

将它用于(11)。对非空 C⊆U，每个 u至少有一个邻点 i>u，故 max N_G(C)>max C。由(2)，每个 N_G(C)点有纯 H的 R6尾。交换后 V_C的补集恰为

\[
X\setminus V_C=(H\setminus C)\cup N_G(C), \tag{25}
\]

最大新点的纯尾避开全部删点 C，所以该补集必含 R6，确定不是766。特别 C=U时，N_G(U)=I\E，V_U=(P⊔U)⊔E，即旧记号 K′∪E；其残余合法性仍成立，但补集766的此前不确定接口现已被此操作定理否定。此结论只覆盖这些正向全邻域交换，不否定任意完整路径重分划，也不作一般重分划不可能定理。

## 10. 证据状态与文档边界

本轮只新增本稿和 [文档检查回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_three_matching_20261029/DOCUMENT_CHECK.json>)。全部新增数学未独立审阅、未正式接受；接受基例 b与旧结构依赖的各自保证分层保留。检查回执不是科学计算、证明检查器输出或独立审阅。未调用外部服务，未执行研究代码、SAT、solver、证书重放或数学程序；没有修改旧文档、任务元数据、接受记录、配置、sealed对象及运行。

本稿关闭的是旧 X_(3b+5)整个共同饱和的工作证明分支。它不把负面换点障碍计成另一次数值收益，不把新79/80写回历史接受记录，亦不宣告长期任务整体完成。

## 附录 A. 完整路径竞争路线的非局部 product 横截障碍

本附录是主会话另行提供的手工生成结果，不是§3—7定理的依赖，也不是 universal z≤4。先给公式层接口，再给十点代入例；没有运行构造检查程序。

**完整延拓引理。** 令 p≥3。实际配置禁 B_(p+1)、R_(p+2)，且禁同实际端点的 R_(p+1)+B3；例如 no weak n 且 n≤p+2即可保证最后一项。若 A是一条 R_(p+1)，D是与 A不交的 B_(p−1)，并且每个 a∈A都使 D+a成为实际 B_p，则

\[
|D\cap(\min A,\max A)|\le1,
\qquad D\not>\max A,
\qquad D\not<\min A. \tag{A1}
\]

若有两个内部点 d<e，D+min A与 D+max A的蓝色遗传给 packet(min A,d,e,max A)首尾蓝，故全包蓝，得到 B3(min A,d,max A)，与 A同端矛盾。若 D全在 A右侧，令 x、y为 A最后两点，d为 D首点。χ(x,y,d)红则把 d追加到 A形成 R_(p+2)，故蓝；结合 D+y全蓝，(x,y,D)成为 B_(p+1)。全左侧同理由反序排除。

**Product 横截定理。** 在上述禁形模型中，考虑完整实际路径角色约束：每条红 R_(p+1)必须同时遇 K与Y，每条蓝 B_p必须遇 K，且 K⊔Y是全体顶点。若该完整约束族 UNSAT，则其整个红族不能恰由 p条两两顶点不交的实际 R_(p+1)组成。

反设整个红族正是这 p个不交红块。任取每块一点的 product 横截 S，置 Y=S、K为其余点，全部红约束都满足。因此 UNSAT迫有蓝 B_p全落 S；S恰有 p点，故 S自身是实际 B_p，并属于完整蓝族。这对全部 product 横截成立。

令全局最早红顶点所属块为 A。任取其他 p−1块的 product 横截 D，对每个 a∈A都有 D+a蓝，故(A1)适用。D无点在 min A左边，且不能全在 max A右边，因此恰有一个点在 A区间内部。两个其他块不可能都含内部点，否则选择这两点会使 D有至少两个内部点。于是恰有一个块 B含内部点，其余块全部在 max A右侧；而 B的所有点都必须位于 A内部，否则选择 B的外点及其他各块点，就得到全右侧 D，再违(A1)。

最后选 max A以及除 A、B外各块的一点，组成 p−1点集 D′。这些点全在 B右侧；但任取 b0∈B，D′+b0仍是 product 横截，全部蓝。应用(A1)的单侧禁形即矛盾。此证明不需要 MUS极小性。p=5时，它排除的是整个红族恰为五条互不交 R6的 UNSAT完整角色族；不覆盖红路径重叠、红成员多于五条或一般纯红障碍，也不证明 universal z≤4。

## 附录 B. 六次完整延拓可真实共存的十点例

令

\[
L=\{d1<d2\}<A=\{a1<a2<a3<a4<a5<a6\}<R=\{d3<d4\},
\qquad D=L\cup R. \tag{B1}
\]

全部含至少两个 D点的三元组染蓝，全部 A三元组染红。其余混合三元组按下式完整定义：

\[
\chi(d,ai,aj)=B\iff i+j\le7\quad(d\in L),
\qquad
\chi(ai,aj,d)=B\iff i+j>7\quad(d\in R). \tag{B2}
\]

于是 A是 R6，且六个实际 D+ai全部是 B5。下面的手工说明同时核对完整包及全部路径禁形，而不把七条显示约束误称成全部路径族。

四点包中，3A+1D由指标和的单调性至多换色一次；2A加左右各一 D时包为[c,B,B,反色c]，即 BBBR或RBBB；两个 D在同侧时为 BBcc或ccBB。其余模式恒色。因此这是完整有序 rank-3 signotope。

任何蓝路径至多含两个 A点；含两个 A点时不能同时用左右 D点，因为其 A点对的左右颜色互补，故蓝路径至多五点。至少三点的红路径至多含一个 D点；含左 D时至多四点，含右 D时至多五点，全在 A时至多六点，故无 R7。

同实际端点的红蓝长度和也逐类不超过8。两端均在 A时红长≤6、蓝长≤2；两端均在 D时红长≤2、蓝长≤5。左 D→aj时，红长≤max(2,j−2)、蓝长≤4，和≤8。ai→右 D时，红长≤max(2,6−i)，蓝长在 i=1时≤3、其余时≤4，和仍≤8。这穷尽有序两端类型，所以无 weak7。该十点完整767例是手工理论构造，本轮没有计算验证声明。

显示出的七条约束是 A一条 R6及六条 D+ai蓝5，它们本身可满足：取 K={d1,a1}、Y为其余点，红约束同时遇 K、Y，六条蓝约束都遇 d1。这七条不是 MUS，也不是近饱和 X的实例。该例说明“六个完整延拓/唯一 private强制星”本身可以与完整模型共存；要得竞争路线的矛盾，必须使用其他非局部约束成员。附录A给的是一类完整族排除，附录B给的是局部充分性反检，二者不计入新 Q79证明的必要依赖。
