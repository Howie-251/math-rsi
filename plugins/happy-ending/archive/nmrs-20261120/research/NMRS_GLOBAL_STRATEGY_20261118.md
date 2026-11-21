<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# N(m,r,s)：结构历史、当前瓶颈与下一轮判别

2026-11-18。本文整理主会话已经完成的推导与路线决定。新增数学内容是有限高度面转移、经典三角密度与既有四列缺额接口的连接，给工作上界 **N(20,6,18)≤4749**，比此前4759降低10；另有九参数同一母体的131−δ个标口及三条混色不交六路的必要结构。七、八、九参数的全局工作数值没有变化；下一轮优先检查普通866的**全母体精确达到性**，七参数并行检查**同一实际74点母体的共同物理费用**。

本文为主会话推导及编辑手算校对，**同会话、未独审、未接受**。本轮未执行项目代码、solver、LP、checker或新的科研计算；文献有限数值沿原文进口，没有在本轮重做其枚举。完整数值及旧证据层级见[事实附表](NMRS_BOUND_TABLE_20261118.md)，历史原件导航见[NMRS交接](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/NMRS_CLAIMS_HANDOFF_20261117.md)与[当日后补](NMRS_POSTLEAF_AND_EXACT_ORDER_20261118.md)。

## 1. 对象与现用数值

N(m,r,s)是完整有序rank-3 signotope中，同时避免蓝r点路径、红s点路径和weak m的最大人口。每个递增四点packet按abc、abd、acd、bcd至多变色一次。weak m要求同一对实际首末点的两色路径长度和至少m+2，长度计实际顶点。

令C_m=N(m,m−1,m−1)、Q_m=N(m,m−1,m)、F_m=N(m,m,m)。D_m是R7的真实残余，保留junction禁形；它不是普通N(m,m−2,m)。真实分拆给Q_m≤C_m+D_m，合法chart给F_m=Q_m+1，几何包含再给ES(m)≤F_m+1。

| 范围 | 现用工作值 | 保证 |
| --- | --- | --- |
| 七参数747／756／757／766／767／777 | 16／25／39／49／75／76 | 747、756精确；b25上界沿限定域人工接受，25点抽象存在性另核；39／49／75整链未独立接受。 |
| 八参数C8／D8／Q8／F8 | 193／124／317／318 | 公开有限树实际重放PASS，加项目新signotope桥；新桥未独审。普通866工作上界61，有九洞有限证据。 |
| 九参数C9／D9／Q9／F9 | 688／458／1146／1147 | 原生迹整数证书实际精确重建PASS；全输入连接和装配整链未独审。 |
| 平面强迫工作推论ES(7)／ES(8)／ES(9) | 77／319／1148 | 避免人口经几何包含再加一；319本身已有公开平面结论，不认领新平面数值。 |

原始证据分别见[七参数owner末端](../../nmrs-20261117/source/reports/n7-owner-intervals-20261116/PROOF.md)、[balanced严格容量](../../nmrs-20261117/source/reports/n766-strict-capacity-20261105/PROOF.md)、[最终替锁](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCK_REPLACEMENT_COMMON_ROOT_EXCLUSION_AND_7576_BOUND_20261103.md)、[八参数迁移与receipt](../../nmrs-20261117/source/reports/n79-overlap-20261116/EIGHT-CYCLE-TRANSFER.md)、[九参数RESULTS](../../nmrs-20261117/source/reports/n79-overlap-20261116/direct-cycle-lp/RESULTS.md)。

## 2. 已经改变过原题的结构步骤

### 2.1 R7真实分拆和R20合法chart

R7的关键是从**同一实际输入**、同一全局点对顺序和p选择得到不交的H⊔R：H属于balanced容量域，R保留真实junction排斥。Q≤C+D因此有实际集合接口，不是把两份独立最优模型相加。它把问题压到两个可调用子容量及二者的共同兼容性。[R7§§1—3](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md)

R20改的是全对角出口。在同一时点、相同短帽b≤26输入下，Q仍≤83，旧F≤165被合法chart的一点删添替换为F≤84。此处81点下降来自精确归约F=Q+1，只记一次；不是又改了一遍短帽输入，也不是84点构造。[R20§§2—4及历史表](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md)

### 2.2 b25、取等层与共同替锁

b=N(7,5,6)从26进入25，使此前依赖b的数值统一下降；上界的[C8人工接受](../../nmrs-20261117/source/.trellis/tasks/09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md)保留限定模型、same-family/provisional和backend／effort不可核边界。下界另由[E21完整25点色表核验](../../nmrs-20261117/source/reports/n756-professor-review-20261027/evidence/E21/portable-verification.json)承担，没有随附几何实现。

后来的收益来自取等时必须共享的对象。三份匹配共用中间匹配；共同根、owner和替锁在同一母体兑现，最终排掉3b+1层，得到Q7≤3b=75。balanced线利用实际替末、安全增广和双色交替环，给一般2b−1并得到C7≤49；owner线再排完整40点757层，得到A≤39。它们各自关闭不同义务，不会自动联动下降Q。[Q75原证](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCK_REPLACEMENT_COMMON_ROOT_EXCLUSION_AND_7576_BOUND_20261103.md)、[C49原证](../../nmrs-20261117/source/reports/n766-strict-capacity-20261105/PROOF.md)、[A39§7.7](../../nmrs-20261117/source/reports/n7-owner-intervals-20261116/PROOF.md)

### 2.3 端点费用、状态注入和共同切片

真实红六支持的物理横截、整路顶点不交打包、首末点匹配是三个不同量。端图的Kőnig覆盖能给物理横截，但物理删中点还可能销毁一整批端边，端图只看原端点会漏收益。任何删后收费都必须重建全部幸存路径，不能只删某条选定见证。[整数覆盖](../../nmrs-20261117/source/reports/n7-owner-intervals-20261116/INTEGER_COVER.md)、[方法损失与净收益](../../nmrs-20261117/source/reports/n7-owner-intervals-20261116/MATCHING_GAIN.md)

另一方面，真实最长末对秩给状态注入，实际pair标签落在后态减前态中；坐标删除给同一母体的真实子域。普通行、平移迹和多洞计数用同端两色路径把一个状态支撑变为必要缺态行，再用共同服务次数或整数权重累加。[状态入口](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/RESTART_SETTING_ANALYSIS.md)、[坐标删除§7](../../nmrs-20261117/source/reports/n78-row-compression-20261115/PROOF.md)、[平移迹](../../nmrs-20261117/source/reports/n79-overlap-20261116/TRANSLATED-PATHS.md)

普适精确入口是：2≤r,s≤m且r+s≤m+3时，weak条件自动，N(m,r,s)=binom(r+s−4,r−2)；Baek四帽精确入口为N(m,4,m)=binom(m−1,2)+1（m≥4），分别见[R12§5](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R12_COMMON_REALIZABILITY_AND_UNIFORM_DEFICIT.md)与[文献原条件核对](../../nmrs-20261117/source/reports/n7-progress-talk-20261117/BOUNDS_AUDIT.md)。记U_m(a,b)=N(m,a+2,b+2)，真实坐标删除在a,b≥1且所用子容量在定义域内时给

$$U_m(a,b)\le\min\left\{\left\lfloor\frac{(a+b)U_m(a,b-1)}b\right\rfloor,
\left\lfloor\frac{(a+b)U_m(a-1,b)}a\right\rfloor\right\},$$

其中所有切片均从同一母体取得，见[坐标删除一般式§7](../../nmrs-20261117/source/reports/n78-row-compression-20261115/PROOF.md)。

九参数688／458说明这条路径能兑现人口改进：标准库checker从坐标差、两条合法链和固定映射重建正权迹，精确扣禁态及列超载，实际PASS。有限支持／算术成功与原输入到这些必要行的证明仍分别记账。[RESULTS及成功日志](../../nmrs-20261117/source/reports/n79-overlap-20261116/direct-cycle-lp/RESULTS.md)

## 3. 当前瓶颈的诊断

### 3.1 七参数：A或C单减一仍不动Q

代入b=25、A=39、C=49，现有接口为

$$Q_7\le\min\{3b,C+b+5,A+C-1,\lfloor9A/4\rfloor,\lfloor9C/5\rfloor\}
=\min\{75,79,87,87,88\}=75.$$

所以A38或C48本身不能由这组接口改进Q75；Q≤C+b仍是未证桥。下一轮应让共同费用变小，或让删后核的有效人口变小，不把旧小帽单减重复列为主目标。[既有策略§3](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_STRATEGY_SYNTHESIS_20261116.md)

11/18还有一个已查清的**方法屏障**。原端图饱和j+ν(H)=25时，单删一个中性内点，每份旧红六仍可剪短成同端红五；若新DAG还保留全部红五端弧，旧端图每条边仍必须支付。因此该全红五图构造费至少26。单删纯末时，删点本身覆盖相应旧边，其余旧边仍有红五，费用至少25。要打破一般红六／红五稳健图，至少有一个未付端对的**全部**旧红六见证内部被付费集双击；这还不是净省一的充分条件。[叶付稿§12.3](N7_POSTLEAF_EXCEPTION_ORDERS_20261118.md)

这不否认物理单口收益：[HKH14原件](../source/reports/n7-postleaf-examples-20261118/REPORT.md)的J=W=∅、ν=3，删真中性第二口4后，全部幸存红六端图只有源0，ν降到1，一费获得两单位匹配下降。删去非路径点5得到13点诱导域后，该口有合法完整未来红扇，标口流κ=2、s=1。但它没有蓝五，不能充当活动真K头或五clean根供给；该小域不证明任意74点都有净收益。它说明应保留实际红六图的灵活性，不把残余红五变成额外收费义务。

### 3.2 八参数：旧矩阵已到九洞，局部可容性仍不足

115行[milestone9](../../nmrs-20261117/source/reports/n866-joint-label-order-20261117/milestone9/README.md)有实际≤8预算proof与checker PASS，同时有九洞向量，故该矩阵最小洞数恰9。后继[271行delivery核验](../SOURCE_MAP.md#excluded-sources)PASS，九洞向量仍活。行数从115增到271没有把普通866的工作上界61降下去；不能把矩阵可行当61点signotope存在。

[14角共同字表实例](../source/reports/n866-overlap-order-20261118/DIAMOND_INTERFACE.md)在1357四轴cube删两角，给真实完整signotope、无蓝五／红六／weak8，并有同一可容差格标签。它否定只靠这些角、共享次序及可容增长就排除的方案，但未实现指定精确末对理想，也没有扩到61态。

精确达到性是另一层要求：[HAND_BRANCHES§§4—6](../source/reports/n866-global-order-20261118/HAND_BRANCHES.md)对占用singleton差对1357→2357迫真实蓝五外前驱，对1457→1458迫红五外前驱；各有九个当前占用候选。全精确域有符号行实际各有十项，当前mask各缺一才剩九，不能省项全称化。单个精确末对(4,4)又有真实8点例，故“两个最长异色臂同末对”本身不足以排除；需要连接**不同pair的同时达到性**。

### 3.3 九参数：纯LP上限不是全对象上限

D9深三全部47635条正需求原生迹，有精确分数可行点总缺额123539833/10^6≤124；整数对偶证书严格超过123，迫缺额至少124。二者仅锁定该纯LP族缺额上取整恰124。继续复用同一行族的纯LP不能迫125，但整数分支、新路径条件和共同精确达到性仍未被排除。这个分数点不证明458可达。988深三时限无证书，也不能覆盖成功深二688。[原始停止点](../../nmrs-20261117/source/reports/n79-overlap-20261116/direct-cycle-lp/RESULTS.md)

## 4. 本次新推导：有限高度面转移

### 4.1 从同端pair证据到Turán击中数

沿[TRANSLATED-PATHS§5.2](../../nmrs-20261117/source/reports/n79-overlap-20261116/TRANSLATED-PATHS.md)，令a+b=m、a,b≥3，高度宇宙大小v=b−1≥a。p为同一实际输入的非蓝洞数（红内部洞及私洞）。每个红洞按实际列高最多标a个不同(a−1)脸，私洞最多标一个。对任意a高度集V，原稿用**同一个pair的两端路径证据**迫该V至少含一个已标脸；不是逐V选择互不相容的标签。

记T(v,a,a−1)为v点上击中每个a集的(a−1)集最小数，标脸族为\(\mathcal D\)。于是

$$|\mathcal D|\ge T(v,a,a-1),\qquad |\mathcal D|\le ap,$$
$$\boxed{p\ge\left\lceil\frac{T(v,a,a-1)}a\right\rceil.}\tag{1}$$

更细的\(|\mathcal D|\le a p_{\rm red}+p_{\rm priv}\)仍有效；式(1)只用其共同上界。它把原来的单次覆盖计数提升为可调用有限极值下界，未把脸覆盖可行性当实际signotope实现。

### 4.2 任意有限种子及逐顶点递推

固定a，简写T(v)=T(v,a,a−1)。每个k≥a的诱导高度集也须击中其中全部a集。对所有k集双计数，每个脸出现于\(\binom{v-a+1}{k-a+1}\)个k集，故

$$|\mathcal D|\binom{v-a+1}{k-a+1}\ge\binom vk T(k),$$
$$\boxed{T(v)\ge\left\lceil\frac{\binom v{a-1}}{\binom k{a-1}}T(k)\right\rceil\quad(v\ge k\ge a).}\tag{2}$$

对j个顶点删去每一个顶点，每个(a−1)脸保留j−a+1次，得到逐层整数式

$$\boxed{T(j)\ge\left\lceil\frac{j\,T(j-1)}{j-a+1}\right\rceil.}\tag{3}$$

实际只需把已保证的整数下界代入右侧，不要求知道中间T(j)精确值。逐层取整可强于直接套一次式(2)。

### 4.3 四列的现有洞消元与单调性

取a=4、m≥14，n=m−2、v=m−5=n−3，并令

$$g=\left\lfloor\frac{(m-3)^2}{4}\right\rfloor,\qquad
c_n=\begin{cases}n+2,&n\text{偶},\\n,&n\text{奇}.\end{cases}$$

原[§6](../../nmrs-20261117/source/reports/n79-overlap-20261116/TRANSLATED-PATHS.md)在同一共同图上已经给

$$H\ge g+p-\left\lfloor\frac{12p}{c_n}\right\rfloor.\tag{4}$$

此域c_n≥12，p增一时取整项至多增一，所以右侧对整数p非减。式(1)—(3)给任何有效有限下界P≤p后，都可直接代入(4)；不必重新优化原普通行矩阵。其原输入条件、真实同端路径及蓝／非蓝洞分类均沿原稿。

### 4.4 13点有限进口给N(20,6,18)≤4755

有限进口为T(13,4,3)=112。来源是[Jing Zou，1992学位论文](https://repository.rit.edu/theses/651/)的13点有限结论；RIT原记录明确列出T(13,4,3)已确定。[Chung–Lu原文第2页](https://cseweb.ucsd.edu/~fan/research/papers/upper_bound.pdf#page=2)列n=3k+1的公式，并明确n≤13已经核验。此处只用其**已核有限范围**，不假设未解决的一般tetrahedron猜想。

按其极值三图记号，手算n=13、k=4：

$$\operatorname{ex}_3(13,K_4^{(3)})=
\frac{4(5\cdot4^2+2\cdot4-1)}2=\frac{4\cdot87}2=174,$$
$$T(13,4,3)=\binom{13}3-174=286-174=112.$$

再沿(3)：

$$T(14,4,3)\ge\left\lceil\frac{14\cdot112}{11}\right\rceil=143,$$
$$T(15,4,3)\ge\left\lceil\frac{15\cdot143}{12}\right\rceil=179,
\qquad p\ge\lceil179/4\rceil=45.$$

对m=20，n=18、v=15、c_n=20、g=72。代入(4)：

$$H\ge72+45-\left\lfloor\frac{540}{20}\right\rfloor=90,$$
$$\boxed{N(20,6,18)\le\binom{20}4-90=4845-90=4755.}\tag{5}$$

此前原稿使用p≥35，给86洞、4759；这里增至90洞、4755。有限T13沿文献进口，新转移及人口推论是本项目未独审工作推论。本轮没有新增科研计算或有限枚举，也未因此改动ES(7)、ES(8)、ES(9)。

不使用13点有限数也有可手算的基线。从T(4,4,3)≥1开始反复用(3)：

| j | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 保证的T(j,4,3)下界 | 1 | 3 | 6 | 11 | 18 | 27 | 39 | 54 | 72 | 94 | 120 | 150 |

因此p≥ceil(150/4)=38，H≥72+38−floor(456/20)=88，给**N(20,6,18)≤4757**。这是式(1)、(3)、(4)的无13点数版本，不声称这些递推下界全部精确。

### 4.5 共同图的三角直线：自足次界4750／4754

原四列图归约还有一个可直接加强的接口：设蓝洞图的补图有n点、e条边、t个三角，原证明给t≤4p。对任意简单图，经典二部／三部临界点间的三角直线为

$$\boxed{t\ge\frac{4n}{9}\left(e-\frac{n^2}4\right).}\tag{5a}$$

这是Bollobás凸包直线的一个特例，不认领为新图论定理；经典关系也见[Reiher原文引言第685页](https://annals.math.princeton.edu/wp-content/uploads/annals-v184-n3-p01-p.pdf#page=3)。这里给出可自足核验的证明。

在固定图上取非负权x_i、总和1，置E=Σ_edge x_i x_j、L=Σ_triangle x_i x_j x_k。在所有权重中，取L−4E/9最小且正支撑最少者。若正支撑中两点不邻，它们不共边也不共三角，固定两权之和后目标沿分配线性；可以把权重全并到其中一点且不增目标，矛盾。因此正支撑为团。

在团支撑上，记s_j=Σ_i x_i^j，由E=(1−s_2)/2、L=(1−3s_2+2s_3)/6，得

$$18\left(L-\frac49E+\frac19\right)=1-5s_2+6s_3.$$

固定两个正权x,y之和u，其相关项为

$$-5(x^2+y^2)+6(x^3+y^3)=-5u^2+6u^3+(10-18u)xy.$$

若末项系数非负，令xy=0会降低目标或保持目标而减支撑，均与选择矛盾；若系数负，极小必须使xy最大，即x=y。因此极小权为某个k团的等权，右侧等于(k−2)(k−3)/k²≥0（k=1亦成立）。所以全权域L−4E/9≥−1/9。取原图各顶点均权1/n，E=e/n²、L=t/n³，即得(5a)。

记e=floor(n²/4)+d，\(\theta=n^2/4-\lfloor n^2/4\rfloor\)。由t≤4p及(5a)，

$$d\le\left\lfloor\theta+\frac{9p}{n}\right\rfloor,
\qquad H\ge g+p-\left\lfloor\theta+\frac{9p}{n}\right\rfloor.\tag{5b}$$

n≥12时右侧对整数p非减；可与旧式(4)逐输入取强者。m=20时n=18、θ=0、g=72，新式d≤floor(p/2)。13点有限进口给p≥45，故H≥72+45−22=95，得到**N(20,6,18)≤4750**。不引13点有限数时p≥38，H≥72+38−19=91，得到**N(20,6,18)≤4754**。两项均不调用Reiher的完整曲线定理。

### 4.6 再排95洞层：主工作上界4749

现在额外调用[Christian Reiher，Annals 2016，Theorem 5.1及Claim 2.1](https://annals.math.princeton.edu/wp-content/uploads/annals-v184-n3-p01-p.pdf)。其加权图定义允许每顶点权1/18、每边权0／1，直接得到有限18点图的界，不需要把渐近式当有限式。其r=3、s=2分段，在e/18²∈[1/4,1/3]时给

$$t\ge x^2(18-2x),\qquad x=6+\frac{\sqrt{324-3e}}3.\tag{5c}$$

这里x,x,18−2x是密度公式中的实部大小，不是在构造原图。若反设H≤95，由H=72+p−d、d≤floor(p/2)、p≥45，必有ceil(p/2)≤23，故p≤46；两端约束准确留下

$$ (p,d)=(45,22)\quad\text{或}\quad(46,23).$$

对应e=81+d分别为103、104，都在所需区间81≤e≤108内。由原图t≤4p，分别最多180、184个三角，但(5c)手算给

| p,d | e | 原图三角上界 | Reiher有限下界 |
| --- | ---: | ---: | --- |
| 45,22 | 103 | 180 | \(186-10\sqrt{15}/9>180\) |
| 46,23 | 104 | 184 | \(192-8\sqrt{12}/9>184\) |

两严格比较均可直接用sqrt(15)<4、sqrt(12)<4核验，不使用浮点求解。两类全排，得H≥96，最终

$$\boxed{N(20,6,18)\le4845-96=4749.}\tag{5d}$$

本次层级因而是：原登记4759；有限高度面配旧图接口4755（不引13点数为4757）；再用自足三角直线4750（不引13点数为4754）；13点有限数加Reiher有限曲线给主值4749。经典外部定理及有限13点结论是进口，它们与同一实际状态／普通行图连接后的上界是本任务工作推论。没有做新枚举或证书重放，不继续逐单位扩尺寸，也没有改动近对角全局上界。

### 4.7 族的三次保证系数与可选密度进口

对v≥13，式(2)给

$$p\ge\frac{112}{4\binom{13}3}\binom v3
=\frac{112}{24\cdot286}n^3-O(n^2).$$

在(4)中g=O(n²)，12p/c_n的扣除对这个代入下界为O(n²)。故

$$\boxed{H\ge\frac7{429}n^3-O(n^2),}\tag{6}$$

把原保证系数1/80提高到7/429，差为131/34320>0。这只是已保证缺额的下界系数，未主张最优常数、取等构造或极限存在值。

还可把文献tetrahedron密度上界u作为独立可选进口。取标脸族的补三图G，它无K4^(3)。把每个顶点替换成同样大小q的独立簇，原边扩成跨三簇的全部边；所得blow-up仍无K4^(3)。若G有v点e条边，极限密度为6e/v³，因此π(K4^(3))≤u推出**有限**e≤uv³/6。于是

$$T(v,4,3)\ge\binom v3-\frac{uv^3}6,
\qquad\boxed{H\ge\frac{1-u}{24}n^3-O(n^2).}\tag{7}$$

例如[Jeong、Park、Im、Lee、Yang的作者预印本v2](https://arxiv.org/abs/2609.27495v2)声明u=14993367693127837/26880000000000000<0.557789。这里将它列为可选文献定理进口，没有重放其证书或Lean。上述有限主值4749及中间4755均不依赖此近期密度值，也不依赖5/9猜想；4749的额外进口是Reiher普通图三角定理。

## 5. 第一优先：866全母体精确达到性

### 5.1 最短必须闭合的接口

固定一份**原始完整实际母体**，保持同一实际状态次序及同一三元色。对c∈{蓝,红}，以顶点数计的最长末对路径长满足

$$\ell_c(x,y)=\max\left(\{2\}\cup
\{1+\ell_c(z,x):z<x,\ \chi(z,x,y)=c\}\right).\tag{8}$$

真实pair秩是\(\sigma(x,y)=(\ell_B(x,y)-1,\ell_R(x,y)-1)\)，真实状态是这些入pair秩的下闭包。式(8)既要求每个宣称达到的坐标有真实前驱，又要求全部前驱不会产生更高坐标；所有pair、前驱和颜色须同时使用一份共同赋值。可容差格标签只给增长条件，不能代替此递推。

当前最短目标是：把旧九洞向量中各singleton差对及其精确前驱要求接到同一母体，证明**所有要求能否同时分配**。优先复用1357→2357、1457→1458的候选表、不同最大格需不同前驱、异色达到臂在共同末对之前不能共点，以及重叠packet共享同色。[当日精确达到性原件](../source/reports/n866-global-order-20261118/HAND_BRANCHES.md)

删诱导域、做可容切片或压缩后，保留的标签未必仍是删后重算的精确秩。因此新必要行必须证明直接适用于**原全域**，或先证明存在完整的精确重赋值；不能把(8)作为所有可容切片的新公理。

### 5.2 下一试验、覆盖和淘汰条件

先用一个已封存九洞代表作验针：手推／未来有界模型中，哪些pair的外前驱需求首次不能共用，能否提取一个有语义证明的有符号必要行。排掉这个代表只关闭其自身次序／赋值分支；若无矛盾，读取具体共同赋值，判断问题在精确递推遗漏还是这个局部支撑本来可实现。14角和8点实例已阻止把单个菱形或单末对反复当排除目标。

真正改变数值需要覆盖相应**全部**原输入与预算。t为普通866已保证的洞数，下游现有响应为

$$H_C\ge\left\lceil\frac{210+8t}{5}\right\rceil,
\qquad H_D\ge\left\lceil\frac{1708+51t}{79}\right\rceil,$$
$$F_8\le407-\max\{59,H_C\}-\max\{30,H_D\}.\tag{9}$$

| 已保证t | 普通866上界 | 两式给的C／D洞数 | 条件性F8出口 |
| ---: | ---: | --- | ---: |
| 9（现有） | 61 | 57／28 | 318 |
| 10 | 60 | 58／29 | 318 |
| 11 | 59 | 60／29 | 317，仍借公开残余30洞 |
| 12 | 58 | 62／30 | 315，两侧数值不需193／124两棵公开树 |

原双侧响应与真实坐标删除见[旧路线§7](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/NMRS_STRUCTURAL_ROADMAP_20261117.md)、[九洞输入实际接回§16](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_N8_CLEAN_ROOT_RECTANGLES_20261117.md)。t=11须排除全集≤10洞，t=12须排除全集≤11洞；不能把一份代表被排或新行能切九洞写成已经完成这些预算。

淘汰标准是：若一批新约束只重复旧可容增长，或仅排一个mask的部分次序却不能给可推广的全域必要关系，就停止原样扩批；改用共同精确前驱、另一组pair或跨C／D接口。下一轮有限执行若进行，须另行冻结完整输入、语义覆盖、受控预算与实际checker绑定；本报告没有启动它。

### 5.3 同一866主线的物理入口：两份可延weak7支持

另一个首个普适探针可直接使用实际路径，不依赖状态表示。对任意X∈(8,6,6)，令\(\mathcal W\)为全部实际weak7的七点完整支持。删去其物理横截后，余域属于(7,6,6)，故由现用C7≤49得到

$$|X|\le49+\tau_{\mathcal W}(X).\tag{9a}$$

每份真实weak7只能有5点臂与4点臂：两色均禁六，长度和至少9；若为5+5则已产生被禁weak8。单色路径闭包使两臂除共同首末外不交，故并恰七点。59点反设于是有τ_W≥10。

在该59点实际母体中任意预留至多两点，避预留的余域至少57点，必有一份W；取**任意**这样的首份并连预留删去，仍至少50点，故又有一份W。两份物理不交，且均避预留，先选的任意首份都可延。两份支持保留原共同次序；其中四点短臂不能插入任何点成为同端同色五路，否则与其原对侧五点臂组成weak8。

未闭出口是把所有重叠／接续支持共同起来：对任意59点母体生成≤9点完整支持横截，或直接迫weak8。若完成，则排59点，得到N(8,6,6)≤58、t≥12，再由(9)得F8≤315。当前只有(9a)及上述可延双支持为必要结构，尚无九点共同截。它把七参数49真实接到八参数，作为本节精确达到性主线的替代入口，不另开只累加九洞向量局部行的项目。

## 6. 七参数平行线：共同批次的实际费用

### 6.1 用全部幸存红六结算

固定任意74点767母体X。已付删集J、j=|J|应包含使剩余首末池分离所需的贯穿点；再选实际物理支付F⊂X\J。用Y=X\(J∪F)的**全部**幸存红六重建端图H_F。左右取原剩余源池和末池，含孤点；二部性须由该实际接口保证。Kőnig覆盖投影到物理点后给

$$\tau_{R_6}(X)\le j+|F|+\nu(H_F).\tag{10}$$

目标是可生成地选择同一J、F，使右侧≤24；删后至少50点无红六，违C7≤49。也可让费用稍大、但用更小删后核人口结束反证。若排尽74点，由遗传性得到**Q7≤73、F7≤74、ES(7)≤75**，目前这些只是目标响应。

五clean根给入口和真实中性口供给，不能直接等同于五份可独立退款。选择过程必须核未付端对的全部替代路、共享臂及重算后的路径端身份。[clean整类及§17条件费用](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_N8_CLEAN_ROOT_RECTANGLES_20261117.md)、[共享臂偏序](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_SHARED_ARM_POSETS_20261117.md)

已有[17点真K完整正例](../../nmrs-20261117/source/reports/n7-neutral-five-full-arms-20261117/REPORT.md)实现五条I及完整长臂，I头图恰为K5,5，实际红六却同终一个末点；I头图与红六首末图不能混同，这也不是五份幸存独立退款。

下一条可读证明应组织成一个覆盖任意母体的简洁二分：对由同一clean根／真口接口产生的共同批次，要么它经全部替代路核验后满足(10)的净收益；要么失败见证在同一母体中迫出足够小的残核人口或另一份合格批次。二分必须证明覆盖、选择可兑现，不能只陈述“若有好批次则成功”，也不能把各分支的最优批次相加。这是尚待证明的组织目标。

### 6.2 避免把旧方法屏障再带回来

[叶付稿§13](N7_POSTLEAF_EXCEPTION_ORDERS_20261118.md)只保留幸存红六P→Q与蓝五Q→clean根／真口的稀疏DAG。它允许物理删路后对应红端约束真正退出，绕开全红五单付屏障；但必须重算全部相关红六、蓝五和前驱闭包，不能仅用“图变稀”认领省费。

HKH14／13点正例可作这条接口的语义校准：它确有同一口的全见证支配及净收益，却不满足临界活动K供给。未来一个满足五clean入口的小例若显示单批全见证收益，才比继续重复无活动K例增加更多信息；小例失败也不能否定74点近饱和性质。

备用接口保持\(\tau_{R_6}\le\mu+8\)、\(|X|\le57+\mu\)，μ为双向分叉完整支持并的物理横截。μ≤16即够；μ=17的joint57层可作为选择过程的条件支。排一层仍留下μ≥18，故不把joint57模板穷尽列为独立主线。[双向核原稿](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_74_BIDIRECTIONAL_RED_FOURS_20261117.md)、[joint57原稿](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_74_JOINT57_ORDERED_ANCHORS_20261117.md)

若共同费用批次反复只复现25，且没有新的失败域或小核连接，就淘汰该具体选择规则；不把相同j+ν基线换名继续扩批。共享臂的精确等式、无分叉64和双向57仍保留为有条件工具。

## 7. 八参数互补：带余量的共同中性I批

沿同一实际R7分拆X=H⊔R，置

$$\delta=(193-|H|)+(124-|R|)\ge0.$$

共同两型匹配先迫至少58−δ个端点互异见证；同一匹配中II型与红末I型的块数**合计**至多21。仅将余下I型边的中性右端定义为Y；配对根与该右端是不同物理角色，不能互称。由[共同锁块稿§9](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_N8_COMMON_LOCK_BLOCK_CAPACITY_20261117.md)，已有

$$\boxed{|Y|\ge37-\delta.}\tag{11}$$

这里Y来自一份共同选择；完整路径支持仍可相交，不能当全路顶点不交打包。上述合并块界21也可以用新866≤61经真实坐标删除所得867≤109接回，来源见[clean稿§16](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_N8_CLEAN_ROOT_RECTANGLES_20261117.md)；带余量推论见[旧路线§§5—6](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/NMRS_STRUCTURAL_ROADMAP_20261117.md)。

若对δ=0、1、2的**全部**实际母体统一证明同一可用批次|Y|≤34，则(11)迫δ≥3；其余δ≥3输入已够，故Q8≤314、F8≤315。只排δ=0只能迫δ≥1，给F8≤317，不能认领315。

下一试验应同时保留H／R低缺额占态、活动I的长红头／蓝前缀、共享真口、共同尾末和实际次序，检查一小批根是否迫额外洞或增广。若抽象共同根本身可实现，就保留正例并转入近饱和预算，不能继续猜无条件“七个I头不可能”；[两份完整23点Q8封存原件](../source/reports/n8-neutral-seven-orders-20261117/SEALED_HANDOFF.md)已分别实现七条中性I共缝及七条分离，带完整长臂和共同p／K／L身份，故仅找到七条不是胜利。两份独立单侧洞矩阵并列只重现59+30，不产生新的共同缺额。

## 8. 九参数新共同结构及后继顺序

### 8.1 同一匹配中的131−δ个真实标口

这项本轮推论使用一般m≥6的[共同锁块§9](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_N8_COMMON_LOCK_BLOCK_CAPACITY_20261117.md)及[带余量Hall共同匹配](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/NMRS_STRUCTURAL_ROADMAP_20261117.md)。令c,d分别为C_m、D_m的有效上界，δ=c+d−|X|。同一匹配有

$$\nu\ge d-N(m,m-3,m)-\delta.$$

其中合并块型边数q受完整提取的共同容量约束

$$q\le\left\lfloor\frac{N(m,m-1,m-2)}{m-3}\right\rfloor.$$

去掉这些块型边，余下标口形成同一母体的真实域Y，禁两色(m−2)点路径。九参数代d=458、N(9,6,9)≤264、N(9,8,7)=N(9,7,8)≤380，得到

$$\boxed{|Y|\ge458-264-\lfloor380/6\rfloor-\delta=131-\delta.}\tag{12}$$

264来自既有真实坐标删除列算，380来自普通行界，原件见[交接§6.1](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/NMRS_CLAIMS_HANDOFF_20261117.md)与[事实附表](NMRS_BOUND_TABLE_20261118.md)。这里没有从D9分数可行点构造Y；Y是任意真实Q9输入经共同匹配提取的物理点域，各点仍带同一九参数母体的长见证。

若Y中某一色六点路全部被物理删集S击中，Y\S就无该色六路，另一色七路也不存在；由换色及N(9,6,7)≤117，\(|Y\setminus S|\le117\)。因此两色各自的物理六路横截数均满足

$$\boxed{\tau_{B_6}(Y),\ \tau_{R_6}(Y)\ge\max(0,14-\delta).}\tag{13}$$

特别在δ=0或1时，对任意预定的三个红／蓝选择，可以依次选该色一条六点路、删去其六点。两次后仍至少130−12=118>117点，所以第三项所需颜色的六点路仍存在。由此得到**遵从任意预定的三个红／蓝选择的三条物理不交六点路**。它们可以混色；不是两色各三条所组成的六路同时不交。每个点的ambient长见证仍来自原同一母体，删掉路径点后也不把见证重新换成另一份模型。

这给九对角一个独立于纯LP天花板的新必要结构。后继只检查这18个标记角色与其ambient长见证在共同次序、共同pair上的相容性：若能对δ=0、1全部输入迫冲突，则δ≥2，Q9≤1144、**F9≤1145**。目前未完成该排除，1145不列为现值。若这组必要角色可以同域实现，应保留正例并停止把它单独当矛盾，不新增未接回人口的模板。

### 8.2 路线顺序与停止判据

| 顺序与范围 | 下一项必须产出的判别 | 应停止原样延伸的情形 |
| --- | --- | --- |
| 第一：866精确达到性 | 一个代表的同时外前驱验针，提取适用于原全域的必要关系；再覆盖≤10／≤11预算。 | 只增加可容标签行、切部分次序而不接完整预算，或重复已存在的14角／单末对例。 |
| 并行：七参数共同物理费用 | 任意74点母体可选同一批次，使预付点数、追加物理点数及删后匹配数之和≤24，或用更小核反证。 | 仅破坏代表路、全红五单付屏障重现，或各条件支之间缺覆盖。 |
| 互补：八参数低缺额I耦合 | 对δ=0、1、2全预算控制共同Y，或等价地迫联合洞≥92。 | 只排零缺额，或独立相加两个局部最优洞界。 |
| 后继：九参数共同角色与真实D9 | 优先读(12)—(13)的18个共同角色；另可在真实582态域对≤124洞做完整整数分支，或加入有原输入证明的新路径行。 | 仍在同一47635行纯LP上追更高分数最优，或混用普通容量与真实D9；局部角色可实现却仍强猜其不可能。 |
| 可复用一般族：固定列平移 | 用(1)—(3)接入已核有限T种子，连接同一普通行图；四列本轮主值4749。 | 只扩大有限表而不改善实际系数／参数，或将受限容量当ES阈值。 |
| 高风险：六个完整split互不交 | 从任意输入抽出完整支持，证明六份物理不交支持不可能。 | 只排六个区间模板，或把各支持的局部见证当作共同全输入。 |

split备选沿Baek–Balko的split-free容量L与完整支持打包：\(|X|\le L+(m+1)\nu_{\rm split}\)。767中L=31；若真能普适排六份完整不交支持，则ν_split≤5，给31+8×5=71。这个排除尚未证明，故仅高风险备选，不能写成现用Q7界。[原归约与完整支持条件](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_STRUCTURAL_SYNTHESIS_AND_PRIORITIES_20261115.md)、[既有策略§6](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_STRATEGY_SYNTHESIS_20261116.md)

各路线都以是否减少原题的真实未闭义务决定继续，不能用新文件、行数或局部SAT／UNSAT收据替代数学连接。尤其依赖计算的低预算排除需要完整覆盖及实际checker；完整解析证明也可给全域出口。必要投影SAT只说明该投影存活。

## 9. 本次审阅与交付状态

本次新任务的路线审阅原件为[deep脱敏回执](../SOURCE_MAP.md#excluded-sources)。请求记录为claude-review-deep／max、wire model claude-fable-5-1-reversed、只读Read／Grep／Glob；CLI初始化报告claude-fable-5-1-reversed[1m]。实际**CLI退出1、工具读取0、数学意见为空**，review_complete=false、acceptance_status=unaccepted、automatic_retry=false；backend与effort仍不可核。没有重试，没有独审通过结论。它是对本次新任务的一次路线审阅申请，与历史失败任务分列。

因此本文4749、有限高度面转移、三角密度连接、九参数共同角色及路线优先级仅由主会话推导、编辑原件核对和手算校验承担；外部定理沿上述明确原文进口。已有有限PASS继续保留其固定范围；它们不接受本文新推论，也不升级七／八／九整链。本次仅新增本文，并在同一编辑者的事实附表补一条新推导指向；未改旧证明、封存运行、接受记录、任务指针、wiki、Goal、CNF或proof。
