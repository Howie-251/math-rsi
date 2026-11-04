# N7：全局联合through容量、顺序紧割与单锚product禁形

日期：2026-10-30。用户授权继续结构研究；本稿忠实转写主会话批准并经生成协作者交叉核对的数学。全部新增 **unreviewed/unaccepted**，生成核对不是独立审阅，文档执行者不自行补证。未调用外部Claude或其他外部服务，未运行科学代码、枚举、SAT、solver、proof checker或证书重放。PowerShell仅用于文档转写、链接、公式编号、UTF-8与固定算术检查；该检查不认证数学。

本轮主定理对全部767配置X给出；下式的D由全部ambient R6源、终点的补集定义

\[
|X|+|\operatorname{Src}_{R5}(D)\cap\operatorname{End}_{R5}(D)|\le3b+4. \tag{1}
\]

它排除全部候选|X|=3b+4的共同through正数分支。证明先建立双满标准接口中间引理，再通过任意canonical缺额的实际删除与增广兑现该接口，不从临界w=0外推任意w。本轮还闭合固定交替符号下的完整合法蓝根小循环结构，positive w存在性仍未证明。它仍不是无条件数值第二单位，保留上一轮工作证明草稿

\[
N_{\rm sig}(7,6,7)\le3b+4,\qquad
N_{\rm sig}(7,7,7)\le3b+5. \tag{2}
\]

## 1. 模型、来源与双满标准接口

继承 [三匹配主稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMMON_SATURATION_THREE_MATCHING_OBSTRUCTION_20261029.md>)、[缺额一与链接紧割稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_DEFECT_ONE_JOINT_STABILITY_AND_LINKAGE_CUTS_20261029.md>)、[联合neutral与重分划二分稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_TIGHT_CUT_JOINT_NEUTRAL_AND_REPARTITION_DICHOTOMY_20261029.md>)，以及 [R7](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md>) §2—3与 [R20](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>) §4—5的原始工具。旧依赖的保证边界原样保留，不在本轮重审或升级接受。

X是完整有序rank-3 signotope，任意a<b<c<d的packet依次为abc、abd、acd、bcd，至多换色一次。单色路径长度按实际顶点计，且对子序列遗传。weak7比较同一对实际首末点的反色路径，长度和至少9，内部可交叠。母体767禁B6、R7、weak7；766禁B6、R6、weak7；756禁B5、R6、weak7，换色模型禁R5、B6、weak7。b为756及换色模型的共同有效上界。所有Src、End在注明的实际集合内部计算，ambient身份则在X内计算。

全局证明先使用以下双满标准中间接口，不能替换成“任意两个满766子集”：

- S是全部ambient R6源，T是全部ambient R6终点；H=X\S、H′=X\T均为实际766且大小2b。
- S具有canonical或已证promotion给出的unrestricted B4末点延长：任何末点在S的ambient B4都能保留首pair延为ambient B5，早期点不必在S。T具有反向首点延长。
- S∩End_R5(X)∩Src_B5(X)为空；反向T∩Src_R5(X)∩End_B5(X)为空。

此前双满canonical接口或已严格证明的J0提升提供这些性质；任意重分块不自动继承它们。§2仅在上述接口内使用封闭与混合禁形，§3将由真实任意缺额promotion在需要时兑现两向接口。

## 2. 中间引理：双满标准接口的共同through容量

设r=|S|=|T|=|X|−2b，定义

\[
I=S\cap T,\quad P=S\setminus T,\quad Q=T\setminus S,
\quad D=X\setminus(S\cup T),\quad
U=\operatorname{Src}_{R5}(D),\quad V=\operatorname{End}_{R5}(D). \tag{3}
\]

### 2.1 中性区两族人口与共同through增广

满H角色分划为End_R5(H)⊔Src_B5(H)=H，两族各b。Q不能启动ambient B5，因为入R6与出B5的两色joining给R7或B6；故Q⊆End_R5(H)，V也包含于该端点族。删除D的全部V后无R5，换色756容量给|V|≥|D|−b；另一方面|V|≤b−|Q|，而|D|=2b−|Q|。两边取等，反序同理，得到参数q≥0与完整身份

\[
|D|=b+q,\quad |U|=|V|=q,\quad
|P|=|Q|=b-q,\quad |I|=r-b+q, \tag{4}
\]

\[
\operatorname{End}_{R5}(H)=Q\sqcup V,\quad
\operatorname{Src}_{B5}(H)=D\setminus V,\quad
\operatorname{Src}_{R5}(H')=P\sqcup U,\quad
\operatorname{End}_{B5}(H')=D\setminus U. \tag{5}
\]

令C=U∩V、w=|C|。U中点不能结束ambient B5：接其D内部R5后供，桥蓝则B6，桥红则得终于D的R6，违反D∩T为空。反向同理，V中点不能启动ambient B5。

S点也不能结束ambient B5：其出R6与入B5的joining，红桥给R7、蓝桥给B6。因此W=S∪U的每点均非ambient B5终点，W及其诱导子集都无B5。任何末点在W的ambient B4都能保首pair延为B5：末点在S使用标准fan；末点在U则接D红5的下一点，红桥会形成终于D的R6，故桥蓝。S∪C因此无B5且无junction：S上的End_R5+Src_B4通过延长违反混合禁形，C⊆V上的B4启动会变成ambient B5源，亦不可能。故S∪C是实际D7；反向T∪C亦然。由旧D7容量先得

\[
r+w\le b+5. \tag{6}
\]

### 2.2 排除增广残余取等与完整第二点Hall

反设r+w=b+5。W内部全部junction G_W=End_R5(W)∩Src_B4(W)只能落在U\C。删除全部G_W后是D7，故

\[
b+5-w+q-|G_W|\le b+5,
\qquad G_W=U\setminus C. \tag{7}
\]

取E=End_R6(S∪C)。由于C在D而不是ambient R6终点，E⊆I。删除E后属756，其容量给|E|≥5；旧D7根论证给|E|≤6。

将E右红根提升到整个W。若W有B3(e,x,y)，取S∪C内终于e的R6，末前驱记t。桥χ(t,e,x)红会延成R7；蓝则给B4(t,e,x,y)，可延成从t启动的B5。若t∈S，违反混合禁形；若t∈C，违反C无ambient B5源。因此对所有W内e<x<y、e∈E都有χ(e,x,y)=R。

每个u∈U\C都有W内部入R5与某条B4(u,i,x,y)。把后者保首pair延成B5，再接入R5的末前驱；蓝桥得B6，红桥则得到最后pair为(u,i)的ambient R6。因此i∈T∩W=I，且i∉E，因为B3(i,x,y)违反右根性质。该实际R6还给全ambient蓝fan

\[
\chi(u,i,z)=B\quad\text{对所有ambient }z>i. \tag{8}
\]

否则追加z即R7。以全部这样的u—i为边，保留所有替代路径。对任意J⊆U\C，实际诱导集

\[
Z_J=((S\cup C)\setminus N(J))\cup J \tag{9}
\]

是D7：基底S、C上的junction分别被混合禁形或无B5源排除，J上全部B4第二点都已删除。容量给b+5−|N(J)|+|J|≤b+5，故普通Hall成立。目标I\E有q+5−w−|E|点，源有q−w点，迫|E|≤5。因此E恰五点，目标大小q−w，并有perfect匹配

\[
\alpha:U\setminus C\longrightarrow I\setminus E. \tag{10}
\]

反向得到F=Src_R6(T∪C)恰五点，以及perfect匹配β:I\F→V\C；每条匹配边i→v都有左ambient fan χ(z,i,v)=B，对所有z<i成立。

### 2.3 删除actual共同点后的中间perfect匹配

仅使用D内部全部R5端点边，在U\C与V\C的副本之间建图。若最大匹配ν<q−w，König定理给端点副本cover大小≤q−w−1。把cover对应的实际顶点连同actual C一起删，实际删除规模至多q−1。每条D内部R5若有端点在C便被C命中；否则它的端点边由cover命中。剩余D至少b+1点且无R5、B6、weak7，违反换色756容量。

所以存在perfect匹配

\[
\rho:U\setminus C\longrightarrow V\setminus C, \tag{11}
\]

每边由实际D内部R5见证。C在左右副本中都出现，但实际只删除一次；这不是给每条路径分配独占资源。

### 2.4 三匹配顺序比较与private根链

令A=I\E、B=I\F，复合φ=β^{-1}ρα^{-1}:A→B。若a<φ(a)=b0，置u=α^{-1}(a)、v=ρ(u)，则u<a<b0<v。两个全ambient fan给B4(u,a,b0,v)，而中间实际R5从u到v，同一对实际端点形成weak7，矛盾。因此φ(a)≤a，所有cut满足

\[
|E_{\le c}|\ge|F_{\le c}|. \tag{12}
\]

S∪C有b+5点，任何少于五点的R6横截删除后仍超过b且为756，故其最小横截数恰5，E为minimum。写E={e1<…<e5}，取e2-private R6，其首点a*不等e1，不能晚于e1，否则右根e1前接得R7，故a*<e1。同端weak7又迫χ(a*,e1,e2)=R，继而得实际R6(a*,E)。反向有R6(F,b*)，其中F={f1<…<f5}、b*>f5。

取cut e2，(12)迫e2<f3。七个实际有序点a*、e1、e2、f3、f4、f5、b*通过E右根及两端红6拼成R7，矛盾。q−w=0时三组空匹配与同一根链论证仍适用。取等情形因此不可能，(6)严格一单位，得

\[
r+w\le b+4,\qquad |X|+w\le3b+4. \tag{13}
\]

这是双满标准接口中间引理。它把旧双满through式|X|+w≤3b+5改进一单位；下一节在任意canonical缺额中兑现该接口，得到全部767的带through公式。

### 2.5 候选临界规模下的整类收益

在双满标准接口内，若|X|=3b+4，则w=0，包括原S、T仅四根或横截数为4的情形：增广后的五根与τ=5是在取等反证中重新证明的，不是额外假设。条件w≥1给|X|≤3b+3；下一节将这一带权式推广到全模型，但不能把w≥1子类的条件界升级为无条件N767≤3b+3。

## 3. 任意canonical缺额的实际增广与全局升格

### 3.1 全ambient定义与统一canonical预算

现在X是任意767配置，不要求双满。令S=Src_R6(X)、T=End_R6(X)、D=X\(S∪T)，并在D内部定义U=Src_R5(D)、V=End_R5(D)、C=U∩V、w=|C|。这些全ambient定义不依赖所选canonical分解；反序交换S、T及U、V，保持D、C、w不变。一般情形不预设|S|=|T|或两补核满。

取原canonical分解X=H0⊔R0，与§2双满H区分，令

\[
d=2b-|H0|,\quad
\Omega=\{e\in R0:\text{存在H0-origin ambient R6终于e}\},\quad
S0=R0\cap\operatorname{Src}_{R6}(X),\quad
J=R0\setminus(\Omega\cup S0),\quad B0=H0\cup J. \tag{14}
\]

定义M=R0∩Src_R6(X)∩End_R5(X)∩Src_B5(X)。三链锁定每个s∈M的全部出R6终点及全部出B5第二点为同一h(s)。引用联合neutral稿§2已证明的任意d联合式

\[
|J|+|M|+g\le d,\qquad
 g=|\Omega\cup(h(M)\setminus B0)|. \tag{15}
\]

该旧引理的全部实际核与终点注入证明及原保证边界继承，不作为本轮独立审阅。再置

\[
M_R=\{s\in M:h(s)\in R0\setminus J\},\quad
j=|J|,\quad m=|M_R|,\quad\eta=d-j-m\ge0. \tag{16}
\]

### 3.2 实际删除后加回共同through的D7

取实际诱导集

\[
W0=(R0\setminus(J\cup M_R))\sqcup C,\qquad
|W0|=|R0|-j-m+w. \tag{17}
\]

计数需要按actual集合核实：M_R与J不交，因为前者是ambient源而后者非源；R0∩D⊆J，所以R0\J与C不交。C可能原在J中，但先删J后加回C，只计算一次，不按两侧副本重复收费。

W0无ambient B5终点。R0⊆P+，unrestricted fan会把末点在R0的B5延长成B6；C⊆U则由D内部红5后供的joining禁止成为B5终点。每条末点在W0的B4都能保首pair延成ambient B5：R0点用fan，C点用D红5下一点，红桥会形成终于D的R6。

内部junction不能落C，因为C⊆V无ambient B5源。若junction落在保留点r∈R0\J，它同时结束ambient R5并启动ambient B5。若r不是ambient R6源，由R0\J的定义必有r∈Ω⊆T；但T不能启动B5，矛盾。因此r∈M。r没有被删，故r∈M\M_R，h(r)不在R0\J。又h(r)是ambient R6终点，C⊆D，故h(r)也不在C。于是h(r)不在W0。可是W0内部从r启动的B4可保首pair延为B5，其第二点在W0，并被三链锁定必须等于h(r)，仍矛盾。

因此全部junction排除，W0为实际D7。由其容量及|R0|=|X|−2b+d，得到

\[
|X|+w\le3b+5-\eta. \tag{18}
\]

### 3.3 零剩余缺额迫任意大小的真实promotion

由(15)—(16)有

\[
\eta\ge(|M|-m)+g. \tag{19}
\]

若η=0，右侧非负项迫M=M_R且g=0。若M_R非空，某h(s)∈R0\J=X\B0，便使g≥1，矛盾。故M=M_R为空、Ω为空，且j=d。

此时B0=H0∪J由旧实际扩充核论证为766，大小|H0|+d=2b，并且没有任何B0-origin ambient R6：H0→H0由canonical端点封闭排除，H0→R0由Ω为空排除，J本来就不是ambient R6源。因此全部ambient源恰为S=R0\J，B0=X\S。S继承原P+的unrestricted末点fan；S上的混合角色交集为空，因为原M为空。于是§1全部正向满标准接口被真实兑现。

这是任意|J|=d的实际promotion，不是只在亏一单点情形成立，也不是对任意满766子集套canonical封闭。

### 3.4 两向兑现与全部767的主式

若反设|X|+w≥3b+5，(18)迫η=0且取等。反序保持全ambient D、C、w，重复同一论证也迫反向零剩余缺额，因而同时兑现§1两向满标准接口。调用§2中间引理却给|X|+w≤3b+4，矛盾。因此对全部767配置成立

\[
|X|+w\le3b+4,\qquad
w=|\operatorname{Src}_{R5}(D)\cap\operatorname{End}_{R5}(D)|,
\quad D=X\setminus(\operatorname{Src}_{R6}(X)\cup\operatorname{End}_{R6}(X)). \tag{20}
\]

所有临界|X|=3b+4均有w=0，覆盖canonical亏一单Ω、单M、全空机制中的through正数部分；这不等于排除这些机制的w=0共同实现。任意w≥t给全模型子类的条件界|X|≤3b+4−t，但没有证明所有候选都具有positive through。

### 3.5 R20合法root/chart的条件传播

对任意777配置Z，取任何已经证明合法的归一化、删根及所需翻色，例如R20的原最左pivot及反序后的最右pivot；不包括任意内部pivot。所得767配置Y满足|Y|=|Z|−1。由(20)得

\[
|Z|+w(Y)\le3b+5. \tag{21}
\]

若任一R20合法chart使w(Y)>0，就有|Z|≤3b+4；临界|Z|=3b+5必须在每个这种合法chart中都w(Y)=0。这里没有声称随意换chart仍保B6帽，也没有证明一定存在positive w的合法chart；它只是下一方向的精确目标。

### 3.6 全部合法蓝根chart至多六个且构成单一合法循环

固定777母体Z的同一交替符号ω。定义𝓡为确实存在一个保留ω的合法chart，使实际点r最左且所有含r的三元组全蓝的根点集合。这里只收集已经实际存在的合法blue-root charts，不假定任意内部pivot合法；以R20已证明的合法根归一化及下述red/blue转换为入口。

对每个r∈𝓡，chart唯一：其余两点的次序由

\[
x\prec_r y\quad\Longleftrightarrow\quad\omega(r,x,y)=B \tag{22}
\]

完全确定。记删根所得767为Y_r。blue根会把Y_r中的B6前接为B7并形成weak7，故Y_r无B6；其R7也由母体遗传禁止。

**根集的平衡与六点界。** 对任意四点packet(A,B,C,D)，使用R20 §2的cofactor刻画

\[
c=(D,-C,B,-A),\qquad
c'_j=\operatorname{sgn}(\pi)c_{\pi(j)}. \tag{23}
\]

有效包平衡当且仅当cofactor两正两负；不平衡有效包则具有唯一少数号点。由(23)，当两个chart都有效时，少数号对应的实际点身份不变。

若𝓡中四点不平衡，取其少数号点v∈𝓡，将v置于其合法最左blue-root chart。新包只能BBBB或BBBR。前者平衡，后者少数号在第三位，不在作为根的第一位，都与实际少数号点为v矛盾。因此𝓡每个四点均平衡，R20的weak刻画给|𝓡|≤6。

**完整合法循环的生成。** 在任一blue-root r chart中取当前全体Z的最右点s。先全反序并按ω更新颜色，再对现最左的s执行R20 §3已证明合法的径向归一化，得到red-root。保持s最左，只反序其余点，并按同一ω重新着色，便得到blue-root。最后一步的非根四点包被反序且全翻色，仍合法；含根包前三项为BBB，亦合法。所以s∈𝓡，整套操作没有使用任意内部pivot。

任一r-chart内，𝓡全部三元组蓝：含r的三元组本已蓝，含r四点包前三项BBB且已证明平衡，故第四项也蓝。因交替符号的循环三元排列保持符号，新s-chart在𝓡上的次序恰把旧最后点s移到首位，其余保持。当前全体Z的最右点必为𝓡最右点，因为它本身由上述操作成为可用root。因此反复该合法操作就是𝓡的完整右轮转，周期m=|𝓡|，遍历全部唯一blue-root charts，而不只是某个选定子循环。

若|Z|≥3，m≥3。在r-chart取r<x<s；χ(r,x,s)=B。reroot到s后，ω(s,r,x)=B使r早于所有其余x，故r不是新最右点；新最右t∈𝓡且不同于r、s。因此临界母体满足

\[
3\le m=|\mathcal R|\le6. \tag{24}
\]

这是完整结构定理，不是执行枚举或计算搜索。

**全翻色、删根配置与下一步精确目标。** 对全局翻色−ω，其blue-root r归一化的其余点次序是ω的r-chart反序；删根后三元颜色中的“全翻色+反序奇偶”抵消，保持原色。因此该表示只把Y_r反序，交换源终而不改w。R20 red-root后删根翻色与此表示相容。

对m≤6个全部实际合法blue-root charts，全局带权式给|Z|+w(Y_r)≤3b+5，于是

\[
|Z|+\max_{r\in\mathcal R}w(Y_r)\le3b+5. \tag{25}
\]

再降一单位的精确充分目标是：临界|Z|=3b+5的这个完整合法root循环，不可能全部w(Y_r)=0。目前未证明这一最后命题。不同charts的预算不能独立相加，也没有已证明的严格下降量或第二单位。该小循环排除“任意80点都可当root”的无效路线，仍保留原紧割主攻与路径重分块竞争路线。

## 4. 五根w=0分支的ambient顺序紧割归约

本节明确限定在尚余的双满标准接口、|X|=3b+4、两侧五根且τS=τT=5分支。主定理已给w=0，即U、V不交；四根或τ4分支不在本节结论内。本节给结构归约，未排除此整支。

### 4.1 扩大中间图与两个精确cut

外侧仍使用全部蓝fan支持，中间图扩大为全部ambient R5(u,v)，u∈U、v∈V，内部允许经过D之外。每条完整链仍受三匹配同端比较约束。旧Menger计数给最大链接至少q−2，满q−1链接已被根链矛盾禁止，所以最大链接恰q−2，q≥2。

写E={e1<…<e5}、F={f1<…<f5}。private根链不只排除e2<f3，也排除e3<f4：若后者成立，a*、e1、e2、e3、f4、f5、b*会形成实际R7。q−2链接覆盖A=I\E及B=I\F各自除一个点外的副本，每条链仍给b0≤a，因而所有cut均满足

\[
|F_{\le c}|-|E_{\le c}|\le1\quad\text{对所有cut},\qquad e2=f3,\quad e3=f4. \tag{26}
\]

在c=f3处，全cut不等式迫E_≤f3至少两点，即e2≤f3；private根链又排除e2<f3，所以e2=f3。同理在c=f4处迫e3≤f4，而private根链排除e3<f4，故e3=f4。这是同一实际根点的身份重合，不只是人口相等；因此c=e2、e3时前缀差值均恰为1，ordered-tight-core仍未被排除。

对c∈{e2,e3}定义外邻集

\[
L_c=N_\alpha(A_{\le c})\subseteq U,\qquad
R_c=N_\beta(B_{>c})\subseteq V. \tag{27}
\]

若L_c→R_c有任何ambient红5，选对应两侧支持a≤c<b0，则u<a≤c<b0<v，两个fan给B4(u,a,b0,v)，与该红5同端形成weak7。因此两侧之间没有ambient R5边。

外侧Hall给|L_c|≥|A_≤c|、|R_c|≥|B_>c|。中间perfect匹配与无L_c→R_c边给|L_c|+|R_c|≤q；而cut差恰1又给|A_≤c|+|B_>c|=q，遂全部取等：

\[
|L_c|=|A_{\le c}|,\quad |R_c|=|B_{>c}|,\quad
|L_c|+|R_c|=q,\quad N_R(L_c)=V\setminus R_c. \tag{28}
\]

N_R这里使用扩大后的全部ambient R5端点边。两个cut的邻集单调，L_e2⊆L_e3、R_e2⊇R_e3。

### 4.2 两个实际满核及其位置

实际删除

\[
C_c=(U\setminus L_c)\cup(V\setminus R_c),\qquad
K_c=D\setminus C_c \tag{29}
\]

命中D内全部R5：首点不在L_c时已删首点，否则其终点在N_R(L_c)=V\R_c。换色756容量迫|C_c|=q、|K_c|=b。主定理已证U∩V为空，故还可准确写为

\[
K_c=(D\setminus(U\cup V))\sqcup L_c\sqcup R_c. \tag{30}
\]

相应L、R全部保留，不是只取抽样见证。两侧都非空：F_≤c比E_≤c多一点，给|A_≤c|≥1；E_>c比F_>c多一点，给|B_>c|≥1。每个u∈L_c都有某个支持a∈A_≤c，故u<a≤c；每个v∈R_c都有支持b0∈B_>c，故v>b0>c。因此

\[
\min K_c<c<\max K_c. \tag{31}
\]

### 4.3 ambient双端封闭与新增ports

先证明一般端点身份：任意ambient R5若首末都在D，则首点必在U。否则其首点是H′内部B5终点，入蓝5与出红5的joining，蓝桥给B6，红桥给终于D的R6，均矛盾。反向同理，末点必在V。

若这样的R5两端均在K_c，(30)便使首点落L_c、末点落R_c，与ambient紧割矛盾。所以

\[
\text{没有任何ambient R5以 }K_c\text{ 的两点为双外端点，内部允许任意经过X。} \tag{32}
\]

对每个i∈I，K_c+i有b+1点，换色756容量迫R5。该路径必须使用i；由(32)，i又必须是端点。全部入型R5(k1,k2,k3,k4,i)满足

\[
\chi(k4,i,z)=B\quad\text{对所有ambient }z>i, \tag{33}
\]

否则追加z形成从D启动的R6。全部出型R5(i,k1,k2,k3,k4)满足

\[
\chi(z,i,k1)=B\quad\text{对所有ambient }z<i, \tag{34}
\]

否则前接z形成终于D的R6。

这些新增ports k4、k1不必在U或V。它们不能自动回填四层网络，也不能由每个i均有端点化供应就断言全部外根共同不相容。本节留下的是两个ordered-tight-core与全部外部roots共同实现的问题，不是整支排除。

## 5. 添红四点的完整辅助容量与满核方向校准

### 5.1 参数化添点定理

任取禁R4、B6、weak7的Y，在其前加红4点块J。定义1J+2Y三元组红，2J+1Y三元组蓝，J内部红，Y内部保持。四点packet只可能是旧包，或

\[
RRR\chi,\qquad BBRR,\qquad RBBB,\qquad RRRR, \tag{35}
\]

均合法，故得到完整signotope。混合红路径若至少三点，则至多用一个J点；Y无R4，所以混合红长≤4。混合蓝路径至多三点；旧Y禁B6，J内部也无B6。同实际端点跨块的红蓝长度和≤7，端点同在旧块或新块时分别继承原禁形，因此无weak7。新J⊔Y属于换色756，从而

\[
|Y|+4\le b. \tag{36}
\]

这是任意Y的参数化容量定理，不声称它是数值最强结论。

### 5.2 全R4横截与端点图匹配的收益审计

令K为实际满b换色756核。若删除至多三点即可命中全部R4，余集Y禁R4、B6、weak7，(36)会迫其规模≤b−4，与余集至少b−3矛盾。因此τ_R4(K)≥4。

同时，已有有效上界a适用于N_sig(7,4,7)。任何禁R4、B6、weak7子集换色后禁B4、R6，亦属于该a所约束的模型。删除K全部R4的一个最小横截后，故有b−τ_R4(K)≤a。合并得

\[
\tau_{R4}(K)\ge\max\{4,b-a\}. \tag{37}
\]

完整R4端点图也有至少同界的匹配。否则König端点副本cover小于该界，删除其实际顶点至多同样多，便命中全部R4，违(37)。这里副本cover只用于完整端点图，actual顶点按集合删除，不给每条路径收费。换色后得到满P、Q的B4横截与端点图匹配对应结论。

a=16、b=25时下界是9。这个9来自旧a输入，不是本轮新证书；本轮参数化添点给出的4也不是新数值改善。二者统一写作(37)，避免把较弱辅助结论误记为上界突破。

### 5.3 满核加四根的条件实际构造

若Y本身是满b换色756核K，它可能含R4。沿同一添点规则，J⊔K仍属于767：混合红长≤5，混合蓝长≤3，跨块同端红蓝和≤8，旧块与新块端点继承禁形。K必含R4，否则(36)对Y=K会给b+4≤b。

所以每个新根e∈J均有R5(e,K^4)，没有反向入型，所有四个根都可以全出向。此构造条件于满K存在，不宣称有效上界b必可实现；它真实保留整个满核，而非抽掉其饱和条件。

因此“满K+红四J+插入端点化”本身不能限制出方向根数≤2。但该构造没有原P、Q外供和双蓝覆盖，不是q=0反例，也不否定完整双满母体中更强的共同不相容性。其策略价值是校准下一步必须使用的额外接口。

## 6. 竞争路线：单锚product禁形与拟阵支持界

### 6.1 完整单锚定理

设p≥3，实际配置禁B_(p+1)、R_(p+2)及同端R_(p+1)+B3。不可能存在固定点w与p−1条两两不交且避开w的实际红p+1块A_i，使所有product选择均为蓝p：

\[
\{w,x_1,\ldots,x_{p-1}\},\qquad x_i\in A_i. \tag{38}
\]

定理允许配置中有额外路径，不要求这些红块组成全部红族。

先复述完整延拓引理。若A是红p+1块，D是与A不交的蓝p−1集，且每个D+a、a∈A均蓝p，则D在(min A,max A)内至多一点，且不能全在A的一侧。若有两个内部点d<e，D+min A与D+max A使packet(min A,d,e,max A)首尾蓝，故全蓝，产生与A同端的B3，矛盾。若D全在右侧，设x、y是A末两点、d为D首点；χ(x,y,d)红则给R_(p+2)，蓝则结合D+y拼成B_(p+1)。左侧由反序同理。

现在取含全局最早红点的块A。若w>max A，每次选择其他红块代表与w组成D，必须恰有一个点在A内部。因为w在右侧，这迫恰有一个其他块C全部在A内，其余块全部在A右侧：两个块都能取内点会违反内部至多一点；没有内点或C能取外点又会使D全右。对C改从A选择max A，同时保留w与其余块代表，得到全在C右侧的D′，但其每个C延拓仍是蓝product，违反单侧引理。因此

\[
w>\min A\quad\Longrightarrow\quad w\in(\min A,\max A). \tag{39}
\]

反序对含全局最晚红点的块B得到w<max B⇒w在B内部。w不可能在所有红点之外：若全左，反向结论使它进入B内部，矛盾；若全右，(39)使它进入A内部，矛盾。于是A、B都包住w。

A已经含内部点w，任何其他块的代表都不能再在A内部，否则D有两个内点。min A又是全局最早红点，所以所有其他块都只能在A右侧。如果A≠B，B便不可能包住w；如果A=B，则任意另一块的代表与w都在A内部，同样矛盾。p≥3保证至少有两个红块。单锚定理成立。

### 6.2 多private拟阵分支的支持界改进

沿前稿允许全部multi-private的竞争二分，在满足基交换的情形，全部最小红横截是秩一、秩二块的基product，块为实际红clique，大小至多p+1，总秩p，G为全部最小横截的并。

若是p个秩一块且其中p−1块均满p+1，从剩余块任取一点w，全部基product蓝，便违反单锚定理。因此至少两个块短于p+1，得到

\[
|G|\le p(p+1)-2. \tag{40}
\]

若存在秩二块，块数至多p−1，仍有

\[
|G|\le p^2-1. \tag{41}
\]

先保留参数式，最后代p=5为28与24。一般分支的旧29因单锚禁形强化为28；含秩二块时24不变。它们是全部最小横截支持界，不是UNSAT核规模，更不是N界。前稿非拟阵型的18/19点单次完整交换失败支持证书保留原量词与范围，本轮没有新增该型结论。G外点及全部额外红约束不删除。

## 7. 本轮关闭范围、仍开接口与数值分账

本轮主结果是对全部767配置的全局带through联合容量定理(20)，完整关闭全部临界|X|=3b+4的positive-through类，同时关闭完整单锚product机制。全局推广通过任意canonical缺额的实际D7删除/增广与任意大小J的真实promotion得到；双满标准接口及其全部条件仍作为证明中间引理保留。它不要求原S/T已是五根或τ5。固定ω下全部合法blue-root charts还已证明构成至多六点的单一合法循环；循环内positive w存在性仍未解，不能把该结构定理计为第二单位。

仍未证明的是五根w=0的ordered-tight-core与全部外部roots共同不相容、四根w=0或τ4分支，以及canonical d=1下单Ω、单M与全空机制的w=0共同实现。全局主式已覆盖这些机制的through正数部分，不能把这一点写成所有亏一例外已排除。§4精确归约后的ports未必在U/V，不能凭“补回网络”自动闭合。§5的满核加红四根条件构造说明单凭满核与端点化无法限制所有根的方向，必须用原P/Q外供、双蓝覆盖等完整母体接口。

辅助R4横截与匹配下界是结构容量结论，数值9来自旧a输入；单锚支持界28/24也不是全局极值收益。前稿接受、assurance与历史记录保持，新数学均未接受。

旧757、766及当前工作证明链仍为

\[
N757\le a+b-1,\qquad C766\le2b,\qquad
N767\le3b+4,\qquad N777\le3b+5. \tag{42}
\]

a=16、b=25代入仍是40/50/79/80。条件w≥1给

\[
|X|\le3b+3,\qquad b=25\text{时 }|X|\le78, \tag{43}
\]

但它不推出无条件N767≤78。未来只有完整排除所有候选|X|=3b+4，才可得到目标N767≤3b+3、N777≤3b+4，数值78/79；本轮尚未达到。无条件数值上界新增收益0。

## 8. 文档检查与保证边界

本轮只新增本文及 [文档检查回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_joint_through_20261030/DOCUMENT_CHECK.json>)。本地链接均为尖括号包裹、含字面空格的真实绝对路径。回执记录UTF-8、公式界定符、唯一编号、本地目标与固定算术；PASS_DOCUMENT_ONLY只表示文档层检查通过，不认证数学。

全部新增unreviewed/unaccepted；主会话与生成协作者交叉核对不属独审。外部审阅、外部服务、科学代码、枚举、SAT、solver及证书重放均为0。旧文、状态、接受/assurance、任务metadata、配置、sealed证据与运行未改；本稿没有宣布长期研究完成，也没有打开页面。
