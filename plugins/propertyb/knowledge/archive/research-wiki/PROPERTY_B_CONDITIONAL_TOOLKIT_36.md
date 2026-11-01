# 面向 m(5)≥36 的条件工具集

2026-10-20。这里保留六项已有明确结论的工具，供后续证明复用。**条件结论本身**与**任意原始输入是否满足应用条件**分开陈述；应用条件尚未保证，不会抹去工具的数学价值，也不能被省略为整支染色结论。

本页是证明导航与接口摘要，不新建claim，不把六项统一标为正式proof-checker验收。纸面证明、实际有限核与跨模型审阅的范围分别见原始证据；没有新增Lean。完整m(5)≥36仍未证明。原有基础工具见[可复用引理总页](PROPERTY_B_REUSABLE_LEMMAS.md)。

|工具|已经得到的结论|应用时还要提供什么|
|---|---|---|
|六星宏观染色|某六度中心W≤25即原H可染；全λ≤2且r≥8时可保证该入口|一般多六度输入中找到这样的中心，或另证全λ≤2|
|三划分共同关联|无三重同块点对时，二重同块图边数≤⌊(3N−f₃)/2⌋|把共同划分记录接到真实原边，并控制λ超过记录次数的部分|
|匹配事件门|至多35条五边，19-hit且边界有相容剩余对即可染|保证所需匹配及相容对实际存在|
|整数匹配权|24点整数权、总权≤74、每点加权度≥5，必有完美匹配权≥7|同时控制双命中扣除t；最大化权重本身不够|
|共同最紧二蓝面|最优唯一低坏边源不可能满足8≤b≤13、u=0、N₂=15−b|把待处理源归到该紧面，或处理u>0及非紧N₂|
|三低共同补色与共享超额|三低同边且D−5α≤17即原H可染；与共享低迹补盖接成r≥7纸面闭合候选|r=3…6且低迹≤2的实际输入仍需处理；新scope验收见下文|

## 1. 六星宏观随机染色：W≤25门及低点共同求和

**实际对象与假设。** H为25点、35条互异五元边、pair-cover超图，z度恰6。六条z星边删z后是24点的六个四块Q₁,…,Q₆。定义

$$
W_z=\sum_{f\not\ni z}\sum_{i=1}^6\binom{|f\cap Q_i|}{2}
   =\sum_{xy\text{同一}z\text{块}}(\lambda_{xy}-1).
$$

**准确结论。** 若Wz≤25，则原H具有Property B。若另有全部点对λ≤2，且六度点总数r≥8，则H具有Property B；后一条件保证至少一个中心满足前一入口，并非附加猜想。

**主证明思想。** 随机选四块各取一蓝三红，另两块全蓝，z红；六条星边恒proper。避z五边的六种块占用给概率包络

$$
p(f)\le\frac3{256}+\frac{403}{15360}
                 \sum_i\binom{|f\cap Q_i|}{2}.
$$

29条原边共同求和得失败概率≤(5220+403Wz)/15360；Wz≤25时至多15295/15360<1，直接返回原H染色。

对全部低点共同计数，令ℓ(e)为原边内六度点数。λ≤2时，

$$
\sum_zW_z\le\sum_e\ell(e)\binom{5-\ell(e)}2
 \le36r-3\binom r2<26r\quad(r\ge8).
$$

这里用到Σeℓ(e)=6r及ΣeC(ℓ(e),2)=C(r,2)，后式来自低点对共度一。

**原文证据。** [规范证明](../proofs/propertyb35/TWENTYFIVE_MACRO_STAR_COLORING.md)；[独立精确小核](../context/propertyb35-paper/round01/twentyfive/macro_star_coloring_20261020/CHECK.py)及[记录](../context/propertyb35-paper/round01/twentyfive/macro_star_coloring_20261020/RESULT.json)，核了六种占用和随机样本，未枚举H。

**未来复用与缺失caller。** 可先寻找低W中心再调用此门，或以共同低点预算代替逐星最坏值。一般25点多六度图并未自动满足λ≤2或存在W≤25中心；共同恒等式中的高共度额外项仍需控制。该推论不关闭一般r≥3分支。

**含低边线性的条件族。** 令L为全部六度点、r=|L|，F为与L相交的原边族、m=|F|。若F任意两边交至多一点（等价于每个高点对至多在一条F边中出现），则r≥11时H可染。准确共同收费为

$$
\sum_{z\in L}W_z\le30(35-m),\qquad
m\ge\frac{36r}{r+5}.
$$

r≥12时两式给共同W≤25r；r=11由整数低迹的`(ℓ−2)(ℓ−3)≥0`进一步得6m≥154、m≥26，共同W≤270<275。此处允许总共度λ>2，条件族不依赖30边骨架。尚未证明任意大r输入都满足F线性，不能改写为无条件r≥11染色。

若H内确有30边点对覆盖骨架，则五条附边不含低点，共同W≤150，r≥6即返回染色。另有一项准确子族：**r=19且m=29**时，六条高内部边因简单性恰为六个高点的全部五子集；高点对在F中的加权行和只能为(5,1,1,1,1,1)，迫单位星。把五叶集合对应的实际高内部边加到F，即得到H内真实30边骨架。这不覆盖整个r=19。

真实r=18例子说明两种接口必须区分：F₅²的30条线删去A=F₅×{0}，加入五条`(A\{a})∪{(0,1)}`及一条`(A\{(0,0)})∪{(1,1)}`，得到35条简单pair-cover边，度谱6¹⁸、7、9、10⁴、11；F线性、m=29、最大λ=5、共同W=72，却没有任何30边点对覆盖骨架。其29条含低线都必须保留，而唯一能补齐所缺十个A内点对的第30条边是已删A。故“可在外部补全设计”不等于“H含骨架”；本例仍由线性条件定理染色，不是不可染反例。

上述三项的[自足规范证明](../proofs/propertyb35/TWENTYFIVE_LINEAR_LOW_EDGES.md)内联宏星染色门，不依赖新completion文献；[独立审计](../context/propertyb35-paper/round01/root/global_reassessment_20261020/many_low_design/INDEPENDENT_AUDIT.md)及[精确小核](../context/propertyb35-paper/round01/root/global_reassessment_20261020/many_low_design/INDEPENDENT_CHECK.json)核对解析接口、显式构造与六型概率，状态为same-family/provisional，无新完整r区间闭合。

## 2. 三份四块划分：共同纤维给二重同块上界

**实际对象与假设。** 任意N点集合X，三份划分每块大小至多4；q(x,y)为点对同块的划分份数。假定不存在q=3的点对。令G连接所有q=2点对，f₃为三个方向中大小恰3的纤维总数；一条轴纤维固定另两份划分的块标签。

**准确结论。**

$$
2|E(G)|\le3N-f_3.
$$

特别，20点上每份五个四块时|E(G)|≤30，且允许划分相同时该上界可达。再由Σq=90得m₂≤30、m₁≥30和Σq(q−1)≤60，其中mᵢ为q=i点对数。

**主证明思想。** 每点的三纤维大小a,b,c满足两两之和≤5。大小至少3的纤维彼此顶点不交：四点纤维贡献总度12；三点纤维的两个横向各只能从共同四块中取得一条外边，总度≤8；其余点度≤3。对同一G求总度即得结论。三点纤维可有度4的单点，不能把总度限制误写成逐点≤3。

**原文证据。** [自足证明、取等例及连接边界](../context/propertyb35-paper/round01/root/global_reassessment_20261020/three_partitions_lemma/PROOF.md)。这是一条集合划分定理，不依赖原H枚举。

**未来复用与缺失caller。** 适合多个低度星给出的同一外点集共同划分，可统一约束视图的重叠。应用前须证明跨视图同块记录对应不同原边；即使有q≤λ，仍须控制

$$
q(\lambda-1)=q(q-1)+q(\lambda-q)
$$

中的第二项，以及删去共同星边产生的贡献。因此不能仅由三划分上界推出W≤25。

### 两份四四块划分的19点联合补色门

令S=X⊔T，|X|=16、|T|=3；在S中均匀取9蓝10红，N=92378。P、Q各为同一X的四个四元块划分。两个待补中心分别连接P、Q，并共同连接T；联合补色失败数**至多15228**，不要求两划分独立。

单划分冲突5226，T红／蓝强迫计数3120／3528；相关交数624／264给粗根界16212。进一步按共同四元块数c=0、1、2、4，分别得14388、15228、15144、11874。c=2只对两个根冲突的并扣一次必有交924，其他强迫事件仍用原并界。全部覆盖是四格和四的整数分拆及c四分，**不需要新的矩阵目录**。

若实际原H已核固定费用≤68068、第三中心补色≤7722，则粗16212已严格；用15228给91018<92378、余1360。费用来源和原边分类须另由实际caller提供，不能由局部定理替代。[自足解析门](../context/propertyb35-paper/round01/root/whole_class_followup_20261020/paired_four_partition/REPORT.md)；[实验记录](experiments/propertyb36-paired-four-partition-analytic-gate-20261020.md)。新24点caller的跨家族scope另记，不由25点旧审阅继承；不声称整个24点闭合。

**已落纸面的24点实际caller。** [全四低原边规范](../proofs/propertyb35/TWENTYFOUR_FOUR_LOW_EDGE.md)现覆盖24点、至多35简单五边、pair-cover且某原边至少含四名六度点的H，第五点也允许六度。唯一重复邻点使内部关系穷尽为低低匹配与低到第五点的辐条；同一19点样本中，有辐条界至多89767，无辐条三支至多89693／87871／92002，均小于92378。其实际配对分支使用粗16212已足够，15228保留为通用加强。

由此非B只能低迹≤3；低迹关联给r≤13，r13若取等则26条三低边仅给52份非低关联，11名非低点为覆盖13低各需至少五条，共需55，矛盾。因此r≥13子类也可染。该新scope尚待跨模型审阅，按drafted/provisional记录，不等于24最小度六全支验收；其余输入仍可能有一至十二低点且低迹≤3。证据由同一[partial节点](experiments/propertyb36-paired-four-partition-analytic-gate-20261020.md)集中记录，不新建重复实体。

## 3. 十九命中与一个相容剩余坏事件对

**实际对象与假设。** 任意至多35条互异五元边的H及顶点匹配P，可有未匹配点。边含完整匹配对称被命中。每对独立取反色，未匹配点独立公平着色。剩余边F的单色坏事件概率为1/16。

**准确结论。** 若命中至少19条边，并且在恰有16条剩余边时存在一对相容边，则H具有Property B；剩余≤15条时无需相容条件。这里相容指两边在全部共享随机分量上的相对选端符号相同，等价于其坏事件交概率为正。

**主证明思想及一般k形式。** 对k元边，未命中事件概率为2^(1−k)。若两边共享c个随机分量，则交概率为

$$
\Pr(A_F\cap A_J)=
\begin{cases}
2^{2-2k},&c=0,\\
2^{1-2k+c},&c\ge1\text{且相容},\\
0,&\text{不相容}.
\end{cases}
$$

因此剩余边数少于2^(k−1)时union bound严格；等于该数时，一对坏事件的交概率为正即可给严格扣除。该公式沿用同一分量着色证明，是纸面一般形式，没有新增通用Lean声明。

**原文证据。** [精确充分门](../context/propertyb35-paper/round01/root/global_reassessment_20261020/pairing_nineteen/PROOF.md)及[独立原边读回](../context/propertyb35-paper/round01/root/global_reassessment_20261020/pairing_nineteen/VERIFY.json)。旧实际24点控制H存在19-hit匹配及相容剩余对，失败界63/64。

**未来复用与缺失caller。** 这是无需度数或pair-cover前提的染色接口，可用于任何已找到的好匹配。自动相容条件是共享随机分量至多一，**不是实际原边交数至多一**。普遍19-hit选点和边界相容性尚未保证；旧图否定20-hit保证，却不否定本门或普遍19-hit可能性。

## 4. 整数超额图：权七下界与双命中扣除必须共同选择

**实际对象与假设。** 24点完整图赋非负整数权，总权≤74，每点加权度≥5。

**准确结论。** 存在权至少7的完美匹配。实际24点／35五边／pair-cover／δ≥7输入令wxy=λxy−1，即满足总权74、点加权度4d−23；模4余1并非此引理必要条件。

**主证明思想。** 假设最优权≤6，整数性先把最优正权匹配压成六条权1边、12个未覆盖点。二交换迫每条匹配边要么只有一端连向未覆盖点，要么两端只连同一单点。后者至多一条；前者的零邻接端点共同需要的内部度超过总权预算，矛盾。这一步真实使用整数性，不能套入分数边权对象。

**原文证据。** [证明和边界](../context/propertyb35-paper/round01/root/global_reassessment_20261020/pairing_nineteen/INTEGER_EXCESS_MATCHING.md)；[完整精确receipt](../context/propertyb35-paper/round01/root/global_reassessment_20261020/pairing_nineteen/INTEGER_EXCESS_MATCHING_CHECK.json)。只对一个冻结实际控制H计算最大权并完整读回其182250个最大权匹配，没有新H搜索。

**未来复用与明确反障碍。** 令W为匹配超额权，t为含两个完整匹配对的原五边数，则

$$
h=12+W-t,\qquad
 t=\sum_{\{p,q\}\subseteq P}\#\{F:p\cup q\subseteq F\}.
$$

W≥7不能代替W−t≥7。旧实际控制H的最大W=12，但全部最大权匹配均h≤18；其19-hit匹配反而W=7、t=0。因此“先最大W、再最小t”在真实范围已失败。原文还给同二点边际、不同t的局部五元trade，说明必须保留四点共同原边信息；它不反驳实际范围的普遍19-hit命题。下一步可复用的是整数下界与联合W−t目标，不能重新沿最大权策略推整支。

## 5. 零单蓝超额的共同最紧二蓝面

**实际对象与假设。** H为25点、35条互异五元边、pair-cover、含六度点的非B输入。在全部“唯一坏边含六度点、且坏边规范为红”的实际源中，依次最小化蓝数b、单蓝超额u=N₁−b、蓝度超额δB=Σ蓝点(d−6)，最后最大化红汇点数|S|。Nᵢ为恰含i个蓝点的原边数；红汇点没有对应的N₄红私有边。

**准确结论。** 这样的最优源不能同时满足

$$
8\le b\le13,\qquad u=0,\qquad N_2=15-b.
$$

这里N₂是二蓝原边数，与第4项的双命中数t是不同对象。

**主证明思想。** 同一批原边容量取等产生共同低端点。任意红汇点的私有交换给逐点跨色费用，再把所有高汇点费用放入一次共享预算；中性交换的max|S|流保留旧高汇点流失。小蓝数由低汇点数量和二蓝图刚性矛盾；b=11由高邻点价格矛盾；b=12、13接已有共同owner／单位点对缺失证明。无需为每个蓝数新铺局部库存。

**原文证据。** [统一规范稿](../proofs/propertyb35/TWENTYFIVE_ZERO_PRIVATE_TIGHT_EXCLUSION.md)；[完整实际源稿](../context/propertyb35-paper/round01/twentyfive/whole_class_attack_20261020/TIGHT_ALL_BLUE_SIZES.md)；[独立阅读记录](../context/propertyb35-paper/round01/twentyfive/whole_class_attack_20261020/TIGHT_ALL_BLUE_REVIEW.md)和[有界整数核](../context/propertyb35-paper/round01/twentyfive/whole_class_attack_20261020/TIGHT_ALL_BLUE_RESULT.json)。审阅是否完成、所含b=12/13进口及范围以这些原始记录为准，本页不统一升级验收。

**未来复用与缺失caller。** 可作为最优唯一低坏边源的整面排除模块，复用共同owner、逐点价格和准确中性流；不只针对某个r的必要表。实际调用须保留源选择域和优化次序。尚未排除u>0或N₂≠15−b的源，也未证明所有源都满足N₂≥15−b所需的低红汇点存在前提。因此该完整紧面排除不等于25点多六度整支修复。

## 6. 三低共同补色及高超额：新门17、r≥7与小r低迹约化

**实际对象与假设。** H为25点、35条互异五元边、pair-cover超图。
取原边 $G=\{a,b,c,u,v\}$，其中a,b,c度恰六，不要求它们是全部低点。
记 $D=d_H(u)+d_H(v)$、$\alpha=\lambda_{uv}-1$。

**准确结论。** 若 $D-5\alpha\le12$，则原H具有Property B。
特别地，全五低原边给D=12、α=0，因此可染。六度点总数r≥18时，
下述实际选边保证全五低原边，故整个r≥18子支闭合。

**主证明思想与实际caller。** 六度点的24份邻点关联恰覆盖其他24点，
故其与每个其他点共度一。a,b,c除G外的五条星边，各自在共同
$S=V\setminus G$ 上给一份五四块划分。令u/v反色，S均匀10红10蓝；
最后分别给a,b,c选允许颜色。只有19条避abc原边单色或某中心同时有
全红、全蓝四块时失败。

单中心冲突数16980；任意两份划分共同冲突至少400。
两类可能单色的避abc原边概率分别为8008/N、6006/N，
$N=\binom{20}{10}=184756$。只扣一对冲突交集的合法union bound给
$$
\Pr(\text{失败})\le
\frac{160650+2002(D-5\alpha)}{184756}.
$$
全五低边时分子184674，余量82，产生原H的实际Bool染色。
若无全五低边，逐边低点数ℓ≤4迫
$\binom r2=\sum_e\binom{\ell(e)}2\le\frac32\sum_e\ell(e)=9r$，
即r≤19，所以r≥20确实进入已证入口。r=18、19再用每个低点的
六条入射边唯一覆盖其余r−1个低点：

* r=19且无五低边时，六项ℓ−1各至多3、和18，故所有含低边均ℓ=4，
  但 $4n_4=6r=114$ 不整除。
* r=18且无五低边时，六项和17，故每低点恰一条ℓ=3及五条ℓ=4，
  于是 $3n_3=18$、$4n_4=108-18=90$，仍矛盾。

因此r≥18都确实进入全五低边染色入口，无新枚举。

**证据与范围。** [规范证明](../proofs/propertyb35/TWENTYFIVE_FIVE_LOW_EDGE.md)
内联所有原图归约、概率及最终补色。
[局部完整证明](../context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/partition_joint/PROOF.md)
覆盖19834个行排序终态、264个行列轨道；
[独立逐染色核验](../context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/partition_joint/independent/REPORT.md)
以48,775,584个代表／红集对直接重放，
[比较记录](../context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/partition_joint/independent/COMPARISON.json)
全部一致；[root重编重放](../context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/partition_joint/root_replay/ROOT_REPLAY.json)
再次PASS。未做Lean，跨家族审阅在途；当前送审仅含原r≥20范围，
新增r=18、19选边推论尚不在该次审阅范围内。

**接入旧宏星门后的进一步收益。** [至少十七低点定理](../proofs/propertyb35/TWENTYFIVE_MANY_SIX.md)完整处理r=17：若无全五低边，低点缺陷2迫两种入射型，整除给8名pair型／9名triple型及4/6/19条低迹2/3/4原边；其余6边全高。共同高点对的低迹互不相交给共度≤13，任取triple型低点有W≤24，直接调用第1组宏星门。无需新增局部表。该新收尾已有Gemini单独有效静态审阅，未将旧回复扩大。

### 新共同marked门：阈值由12提高到17

**实际对象、准确结论。** 仍是同一H、同一三低共边G和q=D−5α。若q≤17，则H可染；特别，恰三名六度点且三点同边的输入可染。证明不假定只有这三个低点。

**证明机制。** 在共同S20的两份划分上保留同一对数J=|BP∩BQ|与标记共同四横截集的Kmax，而非分别取不兼容极值。完整局部域给J−15Kmax≥324。对任意四点T，T全色事件与共同冲突根A=BP∪BQ的交至少e=660−Kmax；第三中心及19条实际避中心边统一相对A扣交，得到q≤17的原H染色入口。

**精确证据。** [新规范M17](../proofs/propertyb35/THREE_LOW_EDGE_BALANCED_EXTENSION.md)；[局部覆盖／主计数](../context/propertyb35-paper/round01/root/whole_class_followup_20261020/marked_partition/PROOF.md)及[不同方法完整重放](../context/propertyb35-paper/round01/root/whole_class_followup_20261020/marked_partition/independent/REPORT.md)。冻结264矩阵上全部17304正格四匹配支持均独立字面计数，2239230个六红子集全一致，最小J−15Kmax=324。17304是格支持数，对应112089个带点标签T；格内标签对称已证明，不能混用两种口径。

### 新统一实际caller：至少九名六度点

**假设与结论。** 同一25/35/pair-cover H，L为全部六度点、r=|L|。在M17及第1组W25进口下，r≥9整个子支有完整纸面推导，不要求额外λ上限、含低边线性或骨架。

高点令t=d−7，则总t为r。非B时每三低边的高点t和至少四，每四低边的唯一高点t至少五。固定任一低点，其六星恰好收取同一批高点的全部t一次，故4a3+5a4≤r，且a3+2a4−a1=r−7。两式统一排r≥12；r11、r10分别由四低边关联22及两共同高点四低迹覆盖10的整除矛盾排除。

r9完整整数关联只余五库存，四低高点的共同三分约束排四项；余(n0,…,n4)=(11,0,18,6,0)。六条三低边的高pair图由成本24+5Σw≤27迫单位简单图；每重顶点度三，共同低三元迹迫两棵顶点不交K1,3，重型允许(4,4)或(4,5)。删去两重高点后点对超额总量≤17，每个低点的真实W≤17，W25返回染色。

**原文及未来复用。** [r≥9规范完整稿](../proofs/propertyb35/TWENTYFIVE_NINE_OR_MORE_SIX.md)；[r≥10规范短证](../proofs/propertyb35/TWENTYFIVE_TEN_OR_MORE_SIX.md)；[r9/10完整同一H推导及小整数receipt](../context/propertyb35-paper/round01/root/whole_class_followup_20261020/r13_after_m17/REPORT.md)。可复用的核心是：低点单位共度将不同原边费用化为同一个全体高点预算，再以共同低迹划分而非各视图独立极值接回真实W。M17亦可用于一般三低同边，但仍须实际证明q≤17。

### 新增r=8：四低共同高点与无quad的缺失二低

**实际覆盖。** 同样25/35/pair-cover，恰八名六度点。M17的共同预算给六星仅A=(0,5,1,0)、B=(1,3,2,0)、C=(1,4,0,1)，C数只能0、4、8；各分支穷尽同一实际H，不新增计算表。

* C8：所有四低边使用唯一高点Q，tQ≥5；两条四低边覆盖八低，Q其余边全高，但只有九条全高边，dQ≤11<12。
* C4：唯一四低高点Q至少七条全高边，避Q全高边≤3。取C型低点z，Q的超额行完全不进入Wz，故Wz≤26；(3,2)型只能是避Q全高边，数m≤3。细宏星门给326Wz+308m≤9400<10139，返回染色。
* C0：B数b只能1、4、7。b7正t高点的两条F3至多覆盖六低，不足七B。b4四F3高pair单位简单图仅余2P3，两中心t4，实际删中心超额≤17使B低W≤17。b1的唯一B点z两条F3耗尽全部t；第三F3须共享正t高点x，其两F3覆盖六低，剩余二低已同在另一F3；唯一一低边含z不可用，补盖二低必须用二低边而重复低pair，矛盾。

**源稿与复用处。** [r≥8新规范](../proofs/propertyb35/TWENTYFIVE_EIGHT_OR_MORE_SIX.md)；[有四低C8/C4完整推导](../context/propertyb35-paper/round01/root/whole_class_followup_20261020/r8_quad/REPORT.md)、[C0的b1/4/7完整独立推导](../context/propertyb35-paper/round01/root/whole_class_followup_20261020/r8_no_quad/REPORT.md)。这给r=8整支，在r≥9旧链上形成r≥8纸面候选；仍只用M17与宏星已有实际接口。最可复用的新步是低迹的“已盖六低、缺失二低”共同补盖，而非扩大局部视图。

### 新增r=7整支及r=3…7的统一低迹门

**准确结论及原文。** [至少七名六度点规范](../proofs/propertyb35/TWENTYFIVE_SEVEN_OR_MORE_SIX.md)完整覆盖r≥7：r≥8准确引用EIGHT，r7只用M17，以三种六星型、五份关联库存及共同低迹补盖排除。没有把新caller的静态核读当成旧门之外的独立确定性验证。

[小r低迹规范](../proofs/propertyb35/TWENTYFIVE_SMALL_LOW_TRACES.md)说明：25/35/pair-cover且3≤r≤7非B时，所有原边低迹≤2。统一quad中心W≤26、m32≤3，细门9400；排quad后实际triple高pair共度一，中心W≤26、纯高避pairm32≤5，细门10016<10139。两种上界都来自同一原H，不拼不兼容视图。准确剩余库存为n1=r(7−r)、n2=C(r,2)、n0=35−r(13−r)/2。

[完整r7源稿](../context/propertyb35-paper/round01/root/whole_class_followup_20261020/r7/REPORT.md)与[统一门独立检查](../context/propertyb35-paper/round01/root/whole_class_followup_20261020/small_r_shared_gate/ROOT_TRIPLE_CHECK.md)保留数学输入；小CHECK仅核三型／五库存、CPU0.000266秒，没有H枚举。root已全文核两规范；后续Grok1285及Gemini1286已各有效静态核此新caller，准确范围见下。纸面记录仍不升级为verified claim。可复用处是固定高点低迹的奇偶补盖与共同全高边收费，不提供r3…6纯一低／二低核心的染色结论。

**当前审阅与缺口。** marked局部完整主算及独立重放PASS；M17/TEN/NINE已有Gemini1274与Grok1275的有效静态声明进口意见，r8已有Grok1280有效静态意见。新增[Grok1285返回](../context/propertyb35-paper/round01/root/whole_class_followup_20261020/GROK_R7_SMALL_RESPONSE.json)为有效end_turn，实际grok-4.7-build/xhigh，静态核SMALL/SEVEN及M17／宏星接口；[Gemini1286返回](../context/propertyb35-paper/round01/root/whole_class_followup_20261020/GEMINI_R8_R7_SMALL_RETRY1_RESPONSE.json)为有效SUCCESS，CLI gemini-4-argon-high/high，全文静态核SMALL/SEVEN/EIGHT、宏星、M17，并手核六型概率和实际计数。root已全文处置两份新scope，未发现实质问题。两者均未执行程序或Lean，没有代替264／17304的确定性核验，也不外推r3…6可染或新24点caller。早先未完成调用没有计入认可；[完整处置](../context/propertyb35-paper/round01/root/whole_class_followup_20261020/REVIEW_RECONCILIATION.md)保留各轮原范围及Grok旧s3摘要的明确更正。纸面数学仍按drafted/provisional记录，不新建或升级verified claim。

该段形成时八个主要开放类仍为八、25余r=3…6且低迹≤2；当前后继r6闭合见末节；非B不能含q≤17三低共边，恰三低且同边已排。条件定理、已接caller与当前审阅范围分别记录；没有声称全25或完整m(5)≥36完成。

### r6纯一低／二低迹的两条共同匹配结构

实际r6输入有6一低、15二低、14纯高边。每高点的二低迹是六低点上的匹配，私有一低次数s只能0／2／4／6；若h_j计其高点数，则h₀=7+h₄+2h₆，至少七高点给完整K6完美匹配。

**第一条。** 相同完美匹配的三高点会占满该匹配的三条高三集；这种满匹配类至多两个。若取三个满类，余Y十高点的含低点关联42、点对关联54，14纯高边的Y关联28+T；由C(k,2)≥2k−3得内部超额≥23+2T，而逐行容量只许≤20+2T，矛盾。

**第二条。** 若有两个满类，令C为其六高点、T_C为其度数超额之和、δ为C内部超出最小十二的点对超额。相同实际纯高边预算给δ≥T_C+1，故T_C≥2。它限制两类对仅六份全局高超额的共同占用，并不排除两个满类。

[完整推导](../context/propertyb35-paper/round01/root/whole_class_followup_20261020/r6_pure_pair/REPORT.md)还给全私有高点h₆≤2及实际involution编码：同块记录数q≠5；Σ_low W=150+𝒟，𝒟=3U₆+U₄−U₂−2U₁−3U₀。𝒟≤5或326𝒟+308Σm≤11939足够调用宏星，但当前没有证明全域保证。剩余是其他私有分解q6类、q4交换类及同一纯高边六星占用的联合控制；不以这些条件结构代替r6染色。[合并partial记录及旧菜单边界](experiments/propertyb36-pure-pair-structure-and-unit8-boundary-20261020.md)保留具体证据，未扩新表。


### 2026-10-20 16:10：24强三低／r≥11与25恰六低

[24三低强门](../proofs/propertyb35/TWENTYFOUR_THREE_LOW_SEVEN.md)
在同一原边、同一19点9蓝10红空间，将实际固定红／蓝四集边组分别取并：
六红扣1595，七红扣2035，七蓝及更多扣616；这些是组内扣交，不重扣自由组件。
故任三six+7+d原边可染。若非B三低边含8，必须alpha0、p0、s8=0、
s_big为2或3且d_big≥9+s_big，故8/8、8/9、8/10也全闭。
[同色四集重叠规范](../proofs/propertyb35/MONOCHROMATIC_FOUR_SET_OVERLAP.md)
给完整解析树界／Bonferroni证明。

[24至少十二低点规范](../proofs/propertyb35/TWENTYFOUR_TWELVE_OR_MORE_SIX.md)
以同一低点重复matching给r12三面q0/3/6，高点行3a+2b=12+K及共享N8≤K≥11≤12−2q；
q0末端唯一big11却有全部12low重复它，强门迫big≥12，矛盾。
结合旧四低≥13门，这一r12层使24δ6余r1…11；下述r11后继再压至r1…10，每边低迹≤3。
配对锐门另有[独立10147标号／43轨精确容斥全项核](../context/propertyb35-paper/round01/root/whole_class_followup_20261020/paired_four_partition/independent_sharp/REPORT.md)，
最大12324、CPU0.246136，非只核极值。

[25恰六低规范](../proofs/propertyb35/TWENTYFIVE_EXACTLY_SIX_LOW.md)
用真实含s0七度独立三元组配六低成九单位锁；完整31416→140必要标记，
128份普通ABC严格、最大1429/1430，含零失败仅024/common-pure及006，由实际选择与行预算排除。
[独立核](../context/propertyb35-paper/round01/root/whole_class_followup_20261020/r6_nine_unit/independent/REPORT.md)
完成140布局运输及3500普通ABC行，CPU0.613576，无quota／DP；374目录仍为声明进口。
所以25现仅余r3…5且低迹≤2，旧r6必要结构和旧菜单失败保留为历史。

上述实际链已root全文核；24红组／强三低／r≥12的Grok1312、Gemini1313，及25r6的Grok1318、Gemini1311均有效静态认可声明进口下成立，均未执行程序。原回应与准确进口见[审阅处置](../context/propertyb35-paper/round01/root/whole_class_followup_20261020/REVIEW_RECONCILIATION.md)。

**十一度拥有／未拥有共同容量与r11后继。** 对24点非B必要结构，设L为全部r名六度点，K_w为唯一重复邻点等于高点w的低点数。若d(w)=11，任何搭八度点的三低边恰含两个已拥有低点和一个未拥有低点；前者点对共度2、后者共度1，故N8(w)≤min(K_w,r−K_w)。这是真实同一H的共享容量，不让各边分别花掉同一未拥有点对。

[完整r11证明](../context/propertyb35-paper/round01/root/whole_class_followup_20261020/twentyfour_r11/REPORT.md)由十四(q,a)必要面开始，十三面用不活跃点共同共度及匹配低点补盖排除。唯一q0a1面中，四seven凸性迫每double恰2seven；余A≤3由3N8≥11(A+B)−64和E≤18迫7³8⁴9⁵11、N8=5，唯一11所有F3搭8。九度／九度任spoke可由两实际固定组内扣交严格，故九度拥有低点只能在double，五点F3关联至多15却须20，矛盾。root已全文逐节核；[小整数核](../context/propertyb35-paper/round01/root/whole_class_followup_20261020/twentyfour_r11/FINAL_RESULT.json)PASS0.003683CPU。新r11跨审待，不借r12意见升级。现在24δ6纸面仅余r1…10。

**23任意四低原边。** [完整条件证明](../context/propertyb35-paper/round01/root/whole_class_followup_20261020/twentythree_internal_map/ALL_INTERNAL_CANDIDATE.md)覆盖low行excess2的全部内部二／三迹；[独立核](../context/propertyb35-paper/round01/root/whole_class_followup_20261020/twentythree_internal_map/independent/REPORT.md)以1293292逐颜色核14型，并独立生成732库存／10209键／558144选项，全部对应、最紧余3，root全文核通过。它去掉旧指定自由中心共度一限制，但仍需实际四低原边，不提供其普遍存在性，不关闭23整类。新scope的Grok1322／Gemini1323均已有效静态认可声明进口下成立，未运行代码；root已全文处置。

**24最小度七的同源工具。** [极小蓝删边源](../proofs/propertyb35/CRITICAL_LOW_EDGE_MINIMAL_BLUE_SOURCE.md)在实际critical低总度G含至少四名七度点时，给同一proper删G染色上至少三个中心m≤3；由全局异色点对盈余至多5排两个m4。Gemini1323已有效静态核正该源态及旧摘要两处更正；仍欠原H共同修复，不将源态当染色。

本批均为完整36目标下的partial记录，不创建verified claim，主要八类仍开放。25r5三K5完整条件例外已root核fresh独立证据，包含非均匀Y；一般r5九单位主域仍开，详见下面的新条件入口。

### 16:25后继：23点r13与25点r5三K5例外

**23点至少十三低点。** 任意四低原边门先给非B低迹≤3及r≤13；r13迫26三低、9纯高，全部低对共度一。十高总度97，故可选实际7/8/9高点与任一低点同边，另一高点未知度的restricted三低门由完整76401必要键全strict接回原染色。[源证明](../context/propertyb35-paper/round01/root/whole_class_followup_20261020/twentythree_three_low/REPORT.md)与[独立实际索引核](../context/propertyb35-paper/round01/root/whole_class_followup_20261020/twentythree_three_low/independent/AUDIT.md)已root全文核；新scope跨审待。因此23δ6纸面仅余r≤12；r12九必要残键仍开。

**25点r5三K5条件例外。** 在r5纯一／二低必要结构中，若十五七度点的高冲突图为三个K5，余五点Y全八度，则该整个条件子类可染。高共度普通锁门与真实低中心收费先将Y权图压为0…3、行和8的148图／六轨；均匀型用同一低星私有块预算，五个非均匀型用精确共同列dual／Farkas，均回到实际W25染色门。[完整源稿](../context/propertyb35-paper/round01/root/whole_class_followup_20261020/r5_nine_unit/common_weight_lp/K5_EXCEPTION_COMPLETE.md)与[fresh独立审计](../context/propertyb35-paper/round01/root/whole_class_followup_20261020/r5_nine_unit/common_weight_lp/fresh_audit/REPORT.md)已root全文核：148图／六轨、5×512有理系数及350普通ABC位置行全PASS，CPU0.488687。新Gemini审阅待；这不处理一般r5九单位主域，25仍r3/4/5，八主要类没有减少。
