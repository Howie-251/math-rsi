# 七个最小度七谱：唯一共度五点对的完整修复

## 定理、范围与状态

设H是21点上的35条互异五元边，覆盖所有不同点对。定义

    A_a = 7^a,8^(18-2a),9^(a+1),10,12；
    B_a = 7^a,8^(18-2a),9^(a+1),11,11。

若实际原点度多重集为A_a、a∈{1,2,3,4}，或B_a、a∈{1,2,4}，则H具有Property B。

这正是99谱诊断中的IDs56、57、61、62、66、71、72。本文完整连接原H、唯一强对、三交容量和共同moment；不是全部min7或全局36的结论。新论证目前为本地自然语言候选，数学审阅same-family/provisional，指定跨家族审阅由主代理另记。有限核已按下文实际执行。

## 1. 原H的强对及Γ最低度

反设H非B。每个所列谱恰21点、总度175，最小原点度七，总高于九度盈余e=4。它只有两个高于九度的点u,v，度数为(10,12)或(11,11)，其余点度7、8或9。

复用 `../min_degree_seven_low_excess_strong_pairs_20261020/RESULT.json` 的完整实际degree-pair投影。该记录为每个实际存在的degree对完整检查c=5,…,min(du,dv)，同度需有两名实际点；每个使用的旧证书均为21点35原索引的zero-quota局部门，不使用自由点度数。除指定高点对uv的c=5之外，所有c>=5均严格；uv的c>=6也严格。因此

    所有其他原点对lambda<=4，且lambda(u,v)<=5。

不把uv/c5的未严格界当作实际存在，只分它是否发生。

在35条实际原边上定义Γ：不同边交大小不等于一时相邻。通用q<=2门给非B时Γ最低度至少三。`../min_degree_seven_clean_star_20261020/SHARP_CLEAN_POOL.md` 的实际q3分类，在21/35/simple/paircover/原最小度>=7条件下，把任何q3边压到degree(7,10,10,10,9)的B型；该分类不要求全lambda<=4。本七谱的十度点数至多一，故不能有这条实际边，得到

    Γ最低度至少四。

这个Γ结论不依赖后文C3容量或scalar，不产生循环。

若lambda(u,v)<=4，则全局lambda<=4，总e4，旧通用c14门给C3<=13n3；上述七谱原99谱共同moment计算均全strict，已经返回原H染色。本文以下只处理仍须允许的**实际lambda(u,v)=5**。

## 2. 唯一五共度时tau及四交容量的实际修正

令

    tau=sum_{pointpair} C(lambda-1,2)，
    n_j=#无序不同原边对交大小j，W=sum_v C(d(v),2)。

paircover给sum_pair(lambda-1)=350-210=140。lambda=1…4时C(lambda-1,2)<=lambda-1，唯一lambda5贡献6而在140中贡献4，所以

    tau<=142。

更强的下界来自同一实际uv行。对端点x=u或v，固定lambda(x,other)=5之后，其余19个邻点的sum(lambda-1)=4d(x)-24。逐项C(r,2)>=r-1且非负，故该端点行的tau贡献至少

    L_x=6+max(0,4d(x)-43)。

两端点行只共享uv这一份贡献6，其余pointpair不同，因此整个tau至少L_u+L_v-6。由此

    tau>=11 对高点对(10,12)；
    tau>=8 对高点对(11,11)。                         (1)

独立scalar核还通过把剩余excess均衡放入19槽的精确凸最小值复算了这些端点行界。

对一个四交原外边对G,J，若exclusive点为a,b，则每个valid middle都必须含a,b，故c(G,J)<=lambda(a,b)。exclusive pair不是uv时通常容量<=4；是uv时容量<=5。exclusive pair恰uv的无序原边对数至多

    b=min(d(u),d(v))-5，

因为它唯一写成G=K+u、J=K+v；每条u-only边至多有唯一替换partner，反向同理。没有再乘两个方向。又它们至多n4个，所以通常可用

    C4<=4n4+min(n4,b)。

还须保留tau与原pointpair的共同关系：uv已经贡献tau6；若tau<=8，其他任何lambda4会另贡献3，不可能。因此该范围内所有其他pointpair实际上都<=3，得到更强容量。统一写为

    beta(tau)=3，tau<=8；beta(tau)=4，tau>=9，
    C4<=beta*n4+(5-beta)*min(n4,b)。                 (2)

在本域低tau情形实际只有B型tau=8。式(2)对同一个H成立，不是把不同pointpair配置分别优化后拼接。

## 3. 三交容量仍可完整压到十三

取任意三交原外边对G,J，写A=G\J、B=J\G，各两点，K=A∪B。valid middle在K的迹只能是cross pair。令四个exactcross迹总数为t，则

    t>=c(G,J)。

反向不必成立，因为cross迹仍可能碰到G∩J。要排除c>=14，只需完整检查t>=14必要库存。

若K不同时含u,v，其内部所有pointpair<=4，且selected高盈余<=4，旧通用c14门直接适用，给c<=13。若K同时含u,v，另外两点degree必在7…9。旧 `../c3_unique_high_pair_five_20261020/PROOF.md` 的425库存局部门已覆盖other degree(8,8)和(8,9)；其定理没有自由点最低度八的前提，可以用于当前实际H。

剩余other degree只有(7,7)、(7,8)、(7,9)、(9,9)。以下只补这些新域，不重跑旧425项。

### 3.1 完整20个标记family

把A编号0,1，B编号2,3，exact迹重数为mu_T。两实际outer给mu3>=1、mu12>=1。指定inclusive pair恰五，其他五个inclusive pair在1…4。

指定uv同侧时，四个cross cap总16；跨侧时总17。令q为full4数、p为全部triple数，精确cross-inclusive预算给

    t+2p+4q<=16或17。

结合t>=14，必q=0、p<=1。指定pair同侧实际不可能：d(u)+d(v)=22，但uv共度五和14个cross exact迹是不相交的关联来源，要求d(u)+d(v)>=2*5+14=24。程序仍完整生成同侧family，得到空域。

每种高点degree pair和other degree multiset，保留同侧一family；跨侧时若两other degree不同，保留两种侧向安排，否则一family。两种高pair×四种other组合，共20family（同侧8、跨侧12）。给定cross／triple／两侧exactpair后，以实际degree唯一恢复singleton和empty，保留全部非负。

|高pair|other degree|新完整库存|
|---|---|---:|
|10,12|7,7|7|
|10,12|7,8|31|
|10,12|7,9|49|
|10,12|9,9|98|
|11,11|7,7|10|
|11,11|7,8|38|
|11,11|7,9|62|
|11,11|9,9|120|
|合计|—|415|

新域含exactcross t=14/15/16/17的317/83/13/2份；最后两份t17是本次真实新输入，未错误沿用旧域的t<=16。325份无三迹、90份恰一三迹。

### 3.2 原H的415份严格证书

只用已存在的三份固定四锁位置

    (8,9,20,21)，(9,10,20,21)，(9,20,10,21)，

全部配额零，计算已证条件排列界sum_k min(A_k,B_k,C_k)。415项全部strict，最大34904/36465<1。给实际K同一重编号并运输固定位置，便得到同一个原H的proper染色。

`C3_GATE.py`按exact cross/triple高迹生成；`VERIFY_C3.py`独立从六inclusive pair及Möbius扣除恢复，全部415标记键逐键相等。后者展开每份35个不同原索引，以下降阶乘注入公式重算1190个有序异边对和21个pivot，8715行全部相等且strict。旧425域不在此次重放范围。

因此所有实际三交外边对都有c<=13，在同一个H上

    C3<=13n3。                                         (3)

## 4. 共同moment及七谱完整严格核

三个原moment在lambda5时仍精确给

    n1=W-280-2tau+3m+8t，
    n2=140+tau-3m-6t，
    n0=735-W+tau-m-3t，m=n3，t=n4。

原single-flip必要界n1>=397；Γ最低度四给每个singleton邻居数s(F)<=30、sum s=2n1，故n1<=525。设f(s)为五组均衡最大交叉和，则35盒凸上界为

    P=sum Cj<=floor(2n1/30)*f(30)+f(2n1 mod30)。

只把它作为实际H的安全松弛，不假定极端盒列表可实现为图。所有Cj共用这个P，并同时用

    C0<=33n0，C1<=35n1-K_d(n1)，
    C2<=floor((S6-6)/2)n2，C3<=13n3，及式(2)的C4。

K_d以实际degree的C(d,2)容量按低degree优先填；S6是实际六最大degree之和。按递增正权(36,120,330,792,1716)倒序填这些容量给最安全加权上界2L=6864n1+sum w_j Chat_j。原两翻门在2L<5445440时给H合法染色。

完整域取式(1)至tau142、三个moment全部非负、397<=n1<=525；没有额外n4cap、wedge、T、threshold图或临界性。

|ID|谱|完整键数|max2L|严格L余量|
|---:|---|---:|---:|---:|
|56|A1|77092|5424972|10234|
|57|B1|77912|5428920|8260|
|61|A2|77973|5432574|6433|
|62|B2|78774|5430684|7378|
|66|A3|78826|5436060|4690|
|71|A4|79695|5443872|784|
|72|B4|80498|5442192|1624|

七谱550770键全strict，和非B矛盾，定理成立。余量是标量松弛的严格余量，不是实际图计数或最优性声明。

`SCALAR.py`以tau/n4/n3生成；`VERIFY_SCALAR.py`独立以n1/n4/n3及奇偶反演生成，另用19槽凸最小值核端点row、degree成本prefix及35盒缺口式重算。每谱完整计数、最大目标均相同，余键全部零。

## 5. 实际执行、进口与验收边界

实际执行：C3 primary0.161580 CPU秒，独立完整域／35索引重放2.884735秒；最终scalar0.944476秒，独立scalar1.306797秒。首个条件scalar pilot0.940296秒保存在SCALAR_INITIAL_RESULT.json；它只有ID72/tau8一余键，最终使用式(2)的共同tau信息排除。总计算约6.24 CPU秒，低于15秒；没有扩新布局或重复95个旧strongpair门。

主要产物为C3_DOMAIN.json、C3_RESULT.json、C3_VERIFY_RESULT.json、SCALAR_RESULT.json、SCALAR_VERIFY_RESULT.json；完整源程序同目录。声明进口是通用条件排列、single/two-flip、Gamma min3、实际q3唯一B型分类、95个旧selected-pair证书、旧generic c14与旧425 single-exception c14、以及lambda<=4子情形的99谱scalar。本文的新scalar不把未strict输入当反例，不以模型意见替代实际覆盖。

本定理只针对列出的七个degree谱。尚无本次指定跨家族完整审阅或Lean证明，主代理负责最终验收、48+7范围装配及全局开放分支；无v2访问。
