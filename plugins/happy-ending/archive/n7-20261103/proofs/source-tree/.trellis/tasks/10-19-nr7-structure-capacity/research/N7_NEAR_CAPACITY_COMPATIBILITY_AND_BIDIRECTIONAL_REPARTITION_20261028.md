# N_sig(7,r,s)：近容量共同实现审计与双向实际重分块

日期：2026-10-28。**本轮没有新全局上界。** 新增证明、反例及条件操作均unreviewed / unaccepted；数学由主会话生成、自核，native Sol/high仅执行冻结核查并忠实转写，不构成独立review。η、κ及新增全称Γ正扣减均为0；这不是说每个具体X的Γ值为0。b25人工接受与结构40/50/80/81草稿的原有状态均保持。

本轮最核心的主线审计是：“每个外点插入受阻”只需角色对按包含极小，就已等价于已有完整私人路径事实；所有非空插入集受阻也是它的直接推论，**容量插入存在性本身没有加强最优性**。真正新增的容量信息只在双核规模、δ小及其实际共同实现。两个真实容量例又否定一般n,p下把插入点免费端点化的减缩。竞争线给出完整双向搬移的条件定理，并用实际16点母体显示：人口余量不保证接收核合法，而双向搬移与核心重优化可实现一次具体的两单位联合收益。均未推广到假想48或78母体。

## 1. 来源、基线与执行边界

本轮读取项目AGENTS、Trellis workflow及下列原始材料；只沿其原有范围使用，不升级历史证据。

| 来源 | 本轮用途 |
|---|---|
| [截至本日的综合](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_SYNTHESIS_N7_20261028.md>) | 模型、40/50/80/81传播与未闭合边界。 |
| [最优覆盖与联合成本稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LEX_OPTIMAL_COVERS_AND_COUPLED_PARTITION_COST_20261028.md>) | 私人路径、lex副势及单向条件操作的纸面结果。 |
| [最优交叠、完整交换与切口稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_OPTIMAL_OVERLAP_EXCHANGE_AND_CUT_INTERFACES_20261028.md>) | 完整暴露族与旧反例的准确范围。 |
| [全缺额与Joint稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_GLOBAL_DEFICIT_FRAME_AND_JOINT_THEOREM_20261027.md>) | 母体共同实现框架；不将其秩运输到任意核心。 |
| [R23 §9](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md>) | 满25的e=m=0/7/8/10多种实际目录。 |
| [cardinality-layer theorem](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/cardinality-layer-theorem.md>) | 内部状态单射、35态作用域及全局m≥e。 |
| [C8正式接受](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md>) | b25人工接受，保证仍same-family/provisional，backend/effort不可核实。 |

R5已有最优覆盖入口见[R5 §2](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R5_COVER_AUGMENTATION_CAPACITY.md>)。上一轮[EXECUTION_UNAVAILABLE](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_lex_coupled_20261028/EXECUTION_UNAVAILABLE.md>)记录模型容量不足；当轮spec预期不是运行结果。本轮是两个新数学用途的独立授权，不补跑或改写上一轮四例。既有[旧result](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_optimal_overlap_20261028/result.json>)只按其原固定实例范围引用，未重验升级。

[Closure停止回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_proof_completion_20261027/closure_acquisition/abort_receipt.json>)仍为source_acquisition_complete=false、CNF_binding=false、solver/proof调用0；C49不能使用。没有改旧稿、证书、运行、接受、任务状态或MANIFEST。

## 2. 一般最优双核与容量插入入口

设n、p均为≥3的整数，X为有限完整有序rank-3 signotope，无红(p+1)、蓝(p+1)、weak n；b是有效\(N_{\rm sig}(n,p,p+1)\)界。路径长计顶点，四点packet按abc、abd、acd、bcd至多一次变色；weak是同一对实际端点的反色路径长度和达到n+2。诱导子配置所有路径、秩、状态均重算。

合法角色U,V互不交，分别打中X的全部实际红p与蓝p。至少存在\(U=\operatorname{Src}_{R_p}(X),V=\operatorname{End}_{B_p}(X)\)：命中性质由定义给出；若有共同v，蓝p末前驱a与红p首后继c满足a<v<c，χ(a,v,c)蓝则延蓝、红则延红，均得到禁(p+1)。

取使unused最大的全局最优对，记
\[
W=X\setminus(U\cup V),\quad\rho=|W|,\quad
A=X\setminus V,\quad B=X\setminus U.
\]
A无蓝p、B无红p，否则对应角色漏击；其他帽与weak继承，换色后两核均受b控制。因此\(|A|+|B|=|X|+\rho\le2b\)。令
\[
|X|=2b-\delta,\quad d_A=b-|A|,\quad d_B=b-|B|,
\qquad d_A+d_B+\rho=\delta.
\tag{1}
\]

容量给一个全称插入入口：任意T⊆V、|T|=d_A+1时，A∪T有b+1点，继承红(p+1)与weak禁形，故必含蓝p；任意S⊆U、|S|=d_B+1时，B∪S必含红p。如果外点数不足，量词族为空；近48的相关角色足够大，非真空。但下一节说明，在最优覆盖上，这项存在性已经被更强的单点事实支配。

## 3. 核心审计：最优性已使每个单点插入受阻

**命题1（已有私人路径事实的严格推论）。** 对任何全局最优对，不需b或近容量条件，每个v∈V都使A∪{v}含蓝p，每个u∈U都使B∪{u}含红p。实际只需角色对按包含极小，即不能单独删掉任一角色点而仍合法；这比全局最优更弱。更准确地，
\[
B_p(A\cup\{v\})=\{Q\in B_p(X):Q\cap V=\{v\}\},
\]
\[
R_p(B\cup\{u\})=\{P\in R_p(X):P\cap U=\{u\}\}.
\tag{2}
\]
两边都是带完整实际点序的路径族。

证明。若A∪{v}无蓝p，则任何蓝p都不能只由v命中；V\{v}仍命中全部蓝p。U不变且仍不交，已经可以删掉一个角色点，违反包含极小性；unused还增加一点，当然也违反更强的全局最优性。红侧对称。又X=A⊔V，蓝p落在A∪{v}当且仅当它与V的交集包含于{v}；原V必须命中它，所以交集恰为{v}，得精确等式。红侧同理。证毕。

于是每个非空T⊆V的A∪T已经包含某个v的私人蓝p，每个非空S⊆U的B∪S同理。第2节d_A+1点插入的**存在检测**没有增加新的约束，不能把它重新命名为新的共同实现机制；容量真正新增的是A/B大、δ小及两核在同一染色中的全部实际相关性。

仍须保存完整插入族
\[
\mathcal T_B=\{(Q\cap V,Q):Q\in B_p(X)\}.
\]
对任意T⊆V，A∪T含蓝p，当且仅当存在实际Q使Q∩V⊆T。证明只用X=A⊔V与路径的实际点集包含。红侧对称。最优性使每个singleton trace {v}都出现，故按包含关系的极小trace恰是全部singleton。但不能删掉多外点trace的完整路径：若同时从原核删点，原先单点私人见证可能被删，而原来多重命中的暴露路径仍可存活。**只给原核加外点的存在性**与**同时删核点的交换**必须分开，后者仍需全部暴露族。

trace须连同Q的全部首点、末点、内部点和次序保存。d_A≤2只限制一次容量插入最多三个外点；存在检测确可由单点私人见证完成，但不能删去完整多外点路径，也不能将插入点端点化或在不同核间拼接。

## 4. 承重端点减缩在一般n,p下失败：真实b3

曾希望利用“近容量、两核均满、全局最优”把每个单点插入障碍选为以插入点为实际端点，以接入旧点对单调机制。这首先没有超出命题1的插入存在性；即使端点化成立，仍需完成p5错向1+2等全局闭合，不能自动给η1。以下完整反例否定其不带七点专属预算的一般版本。

本节p3、n5的真实容量是
\[
b=N_{\rm sig}(5,3,4)=3.
\]
因为无蓝三意味着全部三元组红，四点就含红四，故规模≤3；全红三点实际存在且两色同端点和≤5，无weak5，达到3。

### 4.1 四点：全局且lex最优，两侧障碍全部内部

1<2<3<4，χ123=χ124=R、χ134=χ234=B，唯一packet为RRBB，合法。所有二点路径真空同色，红三恰123、124，蓝三恰134、234，没有更长单色路径。两色最长均3，同端点和≤6，所以无weak5与两色四。

取U={2}、V={3}、W={1,4}，A={1,2,4}全红、B={1,3,4}全蓝，两核均满3。两色路径非空且角色不交迫used≥2，显示对达到2，所以ρ2、δ2、d_A=d_B0。全部最优对恰U∈{{1},{2}}、V∈{{3},{4}}，四对均I0；所选对也是lex最优。

向A插3的全部蓝三是134、234，3在两者都为内部点；向B插2的全部红三是123、124，2也在两者都为内部点。不存在可换选的端点见证。它在真实容量饱和、全局且lex最优、δ2下仍否定一般端点减缩。

### 4.2 六点：M=2b、两核均满的完整共同实现

L={l_1<l_2<l_3}<R={r_1<r_2<r_3}，LLL红、RRR蓝、LLR蓝、LRR红。四点包按3L1R、2L2R、1L3R分别为RBBB、BBRR、RRRB，均合法。全部红三是L及\(\{l\}\cup\{r_i,r_j\}\)，共10条；全部蓝三是R及\(\{l_i,l_j\}\cup\{r\}\)，共10条。所有二点路径真空同色，无更长单色路径：红跨块只能一个L加两个R，蓝只能两个L加一个R。故两色最长3，同块端点和≤5、跨块≤6，无weak5。

取
\[
U=\{l_1,r_1,r_2\},\quad V=\{l_2,l_3,r_3\},\quad A=U,\quad B=V.
\]
A全红、B全蓝，给合法对。M=6=2b，由(1)ρ0，故该对全局最优且d_A=d_B0。全部最优恰10对：U=L,V=R，或U为一个L加两个R、V为其补集。所选I4，**不是lex最优**；U=L,V=R才I0。

全部插入障碍如下，未只挑反例点：

| 插入 | 全部该色三点障碍 | 插入点位置 |
|---|---|---|
| l_2进入A | l_1 l_2 r_1、l_1 l_2 r_2 | 全内部 |
| l_3进入A | l_1 l_3 r_1、l_1 l_3 r_2 | 全内部 |
| r_3进入A | r_1 r_2 r_3 | 末点 |
| r_1进入B | l_2 r_1 r_3、l_3 r_1 r_3 | 全内部 |
| r_2进入B | l_2 r_2 r_3、l_3 r_2 r_3 | 全内部 |
| l_1进入B | l_1 l_2 l_3 | 首点 |

正控制U=L,V=R时，每个外部r插入A都有三条两L加r的端点蓝三，每个外部l插入B都有三条l加两R的端点红三。因此不能说所有最优选择都端点化失败；显示的是所选全局最优、非lex对的四个确切失败插入。

两例说明“满双核+全部强制插入”可以真实共同实现，不能仅凭抽象饱和账本导出矛盾。范围仅p3、n5，**不是p5、n7近48反例**：p3同端红三加蓝三的长度和6≤n+1允许共存，p5同端红五加蓝四长度和9则为weak7禁形。后一个参数专属预算尚未被转成全类共同实现定理；本轮反例不否定目标稳定性。

六点构造与一般C≤2b=6还共同给\(N_{\rm sig}(5,4,4)=6=2N_{\rm sig}(5,3,4)\)。因此不使用额外参数关系、声称所有n=p+2且p≥3都有统一η≥1的扣减也被此例否定；这是低参数方法边界，不是七点新上界。

## 5. b25取等审计：没有免费局部收费证书

在一个确属756域的实际核心H内重算状态单射，[cardinality-layer theorem](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/cardinality-layer-theorem.md>)给
\[
|H|=25+e(H)-m(H),\qquad d_H=25-|H|=m(H)-e(H).
\]
R23 §9的满25有实际e=m=0、7、8、10，不得把取等换成e小、e8固定或全ordinary。已接受证明的承重结论是全局m≥e；本轮所读证据没有提供把每个missing态分配给某条实际插入路径或某个端点的局部可加证书，不能另行发明这种收费。

当A∪T已经含禁蓝五，它已离开原35态短帽域，不能直接套状态目录来给新增外点收费；新增路径也可能终于原有点，正如第4节的内部插入。此处未提取新的端点取等限制，停止目录扩张，不运行状态枚举。

δ0/1/2的账本最后再代入：M50时ρ=d_A=d_B0；M49时ρ0且两缺额和1，或ρ1且两核均满；M48时ρ0对应(23,25)/(24,24)/(25,23)，ρ1对应(24,25)/(25,24)，ρ2对应(25,25)。没有排除任何规模。实际源核的尾结构也不能运输到任意最优A/B。只保留一个主问题：p5、n7全部插入族的**内部位置**怎样通过共同weak预算迫实际冲突或完整覆盖增广，而非先假设外点就是端点。

## 6. 同一实际分块的联合成本与大接收核限制

一般设母体X无红(p+2)、蓝(p+1)、weak n，实际不交分块X=K⊔Y⊔Z，K无两色(p+1)，Y无蓝p、红(p+1)。在诱导K内重算最优ρ(K)，则
\[
|K|+\rho(K)\le2b,\quad |Y|\le b,
\qquad |X|\le3b+|Z|-\rho(K).
\tag{3}
\]
七点定义\(g=5-|Z|+\rho(K)\)，Γ为全部实际合法分块的g最大值。分块有限且非空，空K/Y、全删Z也合法，已有全类z≤5另给Γ≥0，故M≤3b+5−Γ。这只是组合入口，不是本轮新的正扣减。

若M=3b+3，记\(d_K=2b-|K|,d_Y=b-|Y|\)，由不交计数
\[
|Z|=3+d_K+d_Y.
\tag{4}
\]
已有|Z|≤5时，d_K+d_Y≤2，所以K≥2b−2、Y≥b−2；b25即核心≥48、接收核≥23。任何单向搬入D且Y∪D仍合法，必须满足|D|≤d_Y；满Y不能直接吸收非空D。但人口余量只是必要条件，下一节给完整反例。

## 7. 全类条件定理：保留全部路径的双向搬移

取K上任一最优(U,V)，W=K\(U∪V)。任取T⊆Z、S⊆Y、D⊆K，在实际H=K∪T∪S内取完整障碍族
\[
\mathcal E=R_{p+1}(H)\ \cup\ \{Q\in B_p(H):Q\cap V=\varnothing\}.
\]
若D命中每条实际\(\mathcal E\)路径，且实际\(Y'=(Y\setminus S)\cup D\)无蓝p、红(p+1)，则
\[
K'=(K\setminus D)\cup T\cup S,\quad Z'=Z\setminus T
\]
与Y'构成合法分块，且
\[
\rho(K')\ge\rho(K)-|D\cap W|,\qquad
g'-g\ge|T|-|D\cap W|.
\tag{5}
\]

证明。K'的任一红(p+1)都是H中路径，按假设遇D，不能存活。蓝(p+1)及weak由母体继承，所以K'平衡；Y'两色帽按假设，weak也继承。所有集合原属实际不交三块，新的分块仍不交且覆盖X。

构造
\[
U'=(U\setminus D)\cup T\cup S,\qquad V'=V\setminus D.
\]
它们不交。K'内红p若遇T或S便被U'命中；否则是K\D内旧路径，原有U命中点不可能在被删除的D内，故仍遇U\D。K'内蓝p若避V，则属于H中被D命中的障碍，不可能在K'存活；否则其V命中点也不在D，仍遇V'。因此新角色合法，其unused准确等于W\D，给ρ下界。又删集减少|T|，得g净收益(5)。证毕。

这是完整条件证书，不声称对每个近极值母体都存在。Y'合法还要求\(|D|-|S|\le d_Y\)，但这个人口不等式不能替代实际路径核验。含多个T/S点的全部路径、以及新接收核Y'内的全部路径都必须包括，不能把逐点合法性拼成批量合法性。

## 8. 实际16点：人口余量不能吸收，双向可修复

取A5<B5<d<E5，G=A∪B∪{d}。G内A、B各全红，混合A/B三元组全蓝，含d的G三元组全红；E全蓝；跨G/E的GGE蓝、GEE红。

完整四包核验：G内不含d时，AAAA/BBBB全红，AAAB为RBBB，AABB为BBBB，ABBB为BBBR；含d时为(c,R,R,R)。全E为BBBB；3G1E为(c,B,B,B)，2G2E为BBRR，1G3E为RRRB，全部合法。

G内长红链只能在A或B内后接d，全部红六恰A∪{d}、B∪{d}；含混合A/B的红链在d前至多两点。G内蓝链避d且每个A/B至多两点，最长4。跨G/E红链最多一个G加两个E，蓝链最多一条G内蓝四加一个E。因此全部蓝五为E及“两A、两B、一个E”，共1+10×10×5=501条，红／蓝最长6／5，无红七、蓝六。

同端点预算分尽：A或B内红≤5蓝2；A到B红2蓝≤4；G点到d红≤6蓝2；E内蓝≤5红2；G到E红≤3蓝≤5。最大和≤8，所以完整母体无weak7。不能把母体蓝五漏写成仅E。

令t=a_5，初始
\[
K=(A\setminus\{t\})\cup\{d\}\cup E,\quad Y=B,\quad Z=\{t\}.
\]
K红五仅(A\{t})∪{d}，蓝五仅E。取U={d}、V={e_1}合法，非空两色族与角色不交迫used≥2，故ρ(K)=10−2=8，g=5−1+8=12。接收核Y有5点，b25下d_Y20。

固定T={t}、D={d}，单向K+T−D已修好核心，但Y+D=B∪{d}是实际红六，尽管|D|1≤20也不能吸收。这只否定**指定D的单向操作与人口充分性**，不声称所有单向方案失败。

现在返回S={b_1}。扩展核心H=K∪T∪S中，红六仅A∪{d}，蓝五仅E；因为B只剩一个点，母体500条混合蓝五均不进入H。避V的蓝五族为空，D命中全部红六。新分块
\[
K'=A\cup\{b_1\}\cup E,\quad
Y'=(B\setminus\{b_1\})\cup\{d\},\quad Z'=\varnothing
\]
中Y'全红五，合法。对母体全部红六，A+d由A进K'、d进Y'，B+d由b_1进K'、其余进Y'；全部蓝五都含K'点（E本身或混合路径的E点）。故完整母体分块条件逐条成立。

K'红五仅A、蓝五仅E，故最少used2、ρ(K')=11−2=9，g'=5+9=14，实际收益2。定理构造U'={t,b_1}、V'={e_1}只保留旧8点unused，给ρ≥8；重优化成一个A点加一个E点又增1，必须分开计功。

这个例子两色五都非空、Y非空，但Y不近25，也不是78母体。H中同时含T、S的单色路径确有红2条、蓝30条；其中相关红六／蓝五障碍为0，避V蓝五也为0。所以不能真空声称核查了多点长障碍的非真空拼接。不给定D时的其他单向路线没有被否定。

## 9. 假想78的三核账本与真正的存在缺口

在M=3b+3且|Z|≤5的同一分块，K内最优覆盖核记A_K、B_K，令\(a=b-|A_K|,c=b-|B_K|\)。最优覆盖计数给a+c=d_K−ρ(K)，结合(4)，
\[
a+c+d_Y=2-g.
\tag{6}
\]
g2时三核全满，g1或0时三核缺额总和1或2。这仅定位必须研究的三核共同实现，不形成新矛盾，也不再增加人口标签。

若能对每个假想78母体，在**全部|Z|≤5合法分块**中取g最大的分块，证明其必有第7节双向命题的实际T,S,D证书，且|T|>|D∩W|，则新Z'仍≤5而g严格增加，违反该受限最大性，从而排78、给Q≤77及777≤78。这项存在定理尚未证明。受限最大值不是Γ，不能把不同分块的极值或核心saving相加。

竞争方向的准确缺口是大核心与大Y同时在场时的完整修复：近78要求K≥48、Y≥23，Y的禁蓝五可被搬入点触发。本轮小接收核例不能运输过去。本轮具体+2不能外推全称Γ3；若证明对每个假想78的所选极值分块均有哪怕+1，则前段极值反证确可排78，不要求单次+3。

## 10. 两项一次性有限核查与原始证据

先落盘[冻结数学规格](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_near_capacity_20261028/MATHEMATICAL_SPEC.md>)、[输入与预算](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_near_capacity_20261028/INPUT_MANIFEST.json>)，再实现[科学脚本](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_near_capacity_20261028/verify_near_capacity.py>)。两项用途各仅调用一次，权威Linux新隔离目录，外部wall各180秒／TERM后2秒KILL，CPU175秒、内部deadline150秒、512MiB；总外部预算≤360。无SAT、科学重试、范围扩张、下载、证明重放或Windows科学试跑。

每个母体及所需诱导核心都输出完整颜色、所有packet、所有单色路径、所有同端点最大值；逐子集比较全三元组与连续三元组定义。全部原件在[证据目录](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_near_capacity_20261028/>)，由result逐文件哈希绑定。

| 核查对象 | 顶点／子集数 | 三元组／四包 | 红／蓝最长 | 同端点和最大 |
|---|---:|---:|---:|---:|
| MAIN四点 | 4／11 | 4／1 | 3／3 | 6 |
| MAIN六点 | 6／57 | 20／15 | 3／3 | 6 |
| 竞争完整母体 | 16／65519 | 560／1820 | 6／5 | 8 |
| 初始核心 | 10／1013 | 120／210 | 5／5 | 7 |
| 单向失败接收核 | 6／57 | 20／15 | 6／2 | 8 |
| 扩展核心H | 12／4083 | 220／495 | 6／5 | 8 |
| 新核心 | 11／2036 | 165／330 | 5／5 | 7 |
| 新接收核 | 5／26 | 10／5 | 5／2 | 7 |

MAIN全枚举3^4=81、3^6=729角色配对，分别4、10个全局最优对，全部插入路径连同位置保存；六点正控制的全部外点都有端点见证。竞争两核心枚举used≤2的全部不交角色对，均25个最优对，非空两色路径族给used≥2下界。控制拒绝合成RBRB坏packet、角色交叠、漏击实际路径、S为空时接收核红六及D为空时核心红六；合成坏输入不称模型反例。

[MAIN原始result](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_near_capacity_20261028/main_result.json>)与[竞争原始result](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_near_capacity_20261028/coupled_result.json>)均为`FINITE_CONSISTENCY_PASS_UNREVIEWED_UNACCEPTED`。内部时间分别0.010087417962495238秒、0.4811718750279397秒，峰值RSS17408／18432KiB；[MAIN命令回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_near_capacity_20261028/main_execution.json>)与[竞争命令回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_near_capacity_20261028/coupled_execution.json>)均exit0。各stdout与result字节一致、stderr为空。具体[全部插入](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_near_capacity_20261028/main_insertion_results.json>)与[双向搬移结果](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_near_capacity_20261028/coupled_transfer_results.json>)保留完整见证和未触发范围。

科学源SHA256：`6f7598fccc5b066d4e3e4f28e48fbd6e1209cd11e5a37ff36a73d9f713ae4581`；MAIN result：`a0a29673b9f8be622a4f2d7fe92f673f6c9e2949ce31152226a5550b68c54077`；竞争result：`9dc599e6c9a62bf286b4cd4bcbffc5872c3b0032da194cd38ce7886d4c162938`。有限通过支持这些完整例与条件操作一致，不证明全类存在性或目标容量。

## 11. 全局严格收益仍为零，只保留两条承重问题

当前η=κ=新增全称Γ正扣减=0，结构稿40/50/80/81不变。若独立证明C≤2b−η，同一核心与ρ只能取max，不能相加；条件η1/2/3分别会给C49/48/47、Q79/78/77、77780/79/78，均不是本轮结论。Γ≥3排78也是待证目标，不能把Closure尚未闭合算作η1。

主线只问：p5、n7完整插入族的内部位置能否通过同一母体的weak预算迫实际冲突或完整暴露族增广，得到超出最优私人路径事实的结论？竞争只问：假想78、|Z|≤5的极值分块，能否存在完整双向T,S,D，保证大Y修复且净收益严格为正？停止无七点专属前提的端点promotion、人口headroom直接吸收、省略多点路径和状态目录扩张。没有启动新的科学对象、求解、独立审阅或接受流程。
