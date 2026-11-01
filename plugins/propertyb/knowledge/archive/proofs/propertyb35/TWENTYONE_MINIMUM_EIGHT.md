# 二十一点最小度八：完整纸面证明

## 定理与本稿状态

设H是21点上的35条互异五元边，覆盖每个不同点对，且所有点度至少8。则H具有Property B。

本稿完整覆盖上述δ8实际分支，纸面结论现为 **sound-modulo-imports（声明进口下成立）**；不另假设共度上限、正则性、critical或内部证书。[fresh独立审计](../../context/propertyb35-paper/round01/audit-twentyone-minimum-eight-20261020/native/PROOF_AUDIT.md)为PASS_WITH_DECLARED_IMPORTS（same-family／provisional），并实际重放了所列新有限域；[Grok](../../context/propertyb35-paper/round01/audit-twentyone-minimum-eight-20261020/GROK_FULL_DELTA8_RESPONSE.md)与[Gemini](../../context/propertyb35-paper/round01/audit-twentyone-minimum-eight-20261020/GEMINI_FULL_DELTA8_RESPONSE.md)均已有效完成这条完整分支的静态审阅，两者均未执行程序。准确范围、声明进口及回应转录更正见[审阅状态](../../context/propertyb35-paper/round01/audit-twentyone-minimum-eight-20261020/REVIEW_STATE.json)。全21点其他分支及m(5)≥36不由本稿宣称完成；已验收全局下界仍34，旧35 Lean暂停。

## 1. 从原H到完整十五度谱

反设原H非B。记b为八度点数，e=Σ_v max(d(v)−9,0)。总度175给

    175=8b+9(21−b)+e，故b=14+e。

其余g=7−e点度至少9；其正盈余形成e的整数分拆，长度≤g。e≥7不可能：b≥21，唯一候选b=21又迫所有点恰8度，与e=7矛盾。所以e∈{0,…,6}，完整15谱如下。这里允许没有度恰9的点，包含8^20,15。

|源ID|e|正盈余分拆|完整degree多重集|
|---:|---:|---|---|
|0|0|空|8^14,9^7|
|1|1|1|8^15,9^5,10|
|2|2|1+1|8^16,9^3,10^2|
|3|2|2|8^16,9^4,11|
|4|3|1+1+1|8^17,9,10^3|
|5|3|1+2|8^17,9^2,10,11|
|6|3|3|8^17,9^3,12|
|7|4|1+1+2|8^18,10^2,11|
|8|4|1+3|8^18,9,10,12|
|9|4|2+2|8^18,9,11^2|
|10|4|4|8^18,9^2,13|
|11|5|1+4|8^19,10,13|
|12|5|2+3|8^19,11,12|
|13|5|5|8^19,9,14|
|14|6|6|8^20,15|

## 2. 完整强点对门只允许四个唯一例外

[完整实际strong-pair门](../../context/propertyb35-paper/round01/middle/delta8_strong_pair_transfer_20261020/REPORT.md)从上述真实15谱，按点度重数生成全部20种选点度对、所有5≤c≤min(d_u,d_v)，共100参数。两个旧固定双锁位置的零配额严格证书排掉96参数；其数学输入只依赖21点、35实际原边索引和两个选点的真实degree／共度，不借全局小共度假设。

仅下列四个参数未由该双锁门排除：

|源ID|完整degree谱|唯一可达的例外点对|其共度|
|---:|---|---|---:|
|8|8^18,9,10,12|(d_u,d_v)=(10,12)|5|
|9|8^18,9,11^2|(11,11)|5|
|11|8^19,10,13|(10,13)|5|
|12|8^19,11,12|(11,12)|5|

每谱都有唯一的所示实际高点对{u,v}（源9恰两名11度点，也只有一个这样的无序对）。全部c≥6参数已严格排除；其他degree组合的c=5也严格排除。因此非B原H只有两种可能：

1. 全部点对共度≤4；
2. 属于上述四谱之一，恰有指定高点对{u,v}共度5，其余所有点对共度≤4。

第一种由[完整小共度定理](TWENTYONE_MINIMUM_EIGHT_SMALL_CODEGREES.md)直接可染，矛盾。以下只处理第二种。没有将强pair门未过的三锁库存当成H分类，亦不依赖其余24个三锁尾的进一步修复。

## 3. 同一原H的非单交图每点度至少四

令Γ以35条原边为节点，交大小不等于1时相邻；q(F)为节点度。记n_j为交大小j的无序不同原边对数，E=Σ_{j≠1}n_j=595−n1。

[21／22通用q≤2染色门](TWENTYONE_TWENTYTWO_MINIMUM_NONUNIT_DEGREE_THREE.md)不带pointdegree或共度角色，先给非B时q≥3。[无全局高点超额限制的最小度八q3门](../../context/propertyb35-paper/round01/middle/min_degree_eight_singleton_star_20261020/PROOF.md)再排q=3：3276完整迹标签经安全前缀后119配置，仅筛F内degree≥8就余25；F内超额≤4是该有限域的结论。23份五锁严格，余C/D由共同外八度星恢复70份六锁，全zero-quota严格，最大141/143。

这一门不假设全λ≤4，也不假设global e≤4，故在当前唯一λ5原H上仍真实适用。因此

    q(F)≥4，s_F:=34−q(F)∈{0,…,30}，Σ_F s_F=2n1。       (1)

## 4. 一个例外对只增加τ上限二与C4总误差五／六

令

    τ=Σ_{a<b} C(λ(a,b)−1,2)，W=Σ_v C(d(v),2)。

点对覆盖给λ≥1、Σ_{a<b}(λ−1)=350−210=140。对1≤λ≤4有C(λ−1,2)≤λ−1；唯一λ5贡献6，比其在后式中的贡献4只多2。所以

    0≤τ≤142。                                      (2)

对四交外边对G,J，其独占两点a=G\J、b=J\G是任何合法middle的两个不同singleton点，所以c(G,J)≤λ(a,b)。除{a,b}={u,v}外均至多4。例外外边对唯一写为G=K∪{u}、J=K∪{v}；每条含u不含v的G至多对应一个J，反向同理。故这类**无序**不同原边对至多min(d_u,d_v)−5，不另乘方向2。

因此[一个例外点对的一般容量引理](ONE_EXCEPTIONAL_POINTPAIR_CAPACITIES.md)在同一原H给

    C4≤4n4+β，β=min(d_u,d_v)−5，                    (3)

四谱β依次5、6、5、6。不能把所有四交外边对都逐一改付5；这里收费总量只对同一个真实例外对计算。

## 5. 唯一λ5存在时三交middle仍至多十三

固定任意原边G,J且|G∩J|=3，写A=G\J、B=J\G，各二点，K=A∪B。若F是合法middle，即F∩G={g}、F∩J={j}且g≠j，那么g、j分别在A、B中；F不能带G∩J的点，K精确迹必须为一个cross pair。

给K编号0,1在A、2,3在B，精确K迹重数记μ_T，则两实际outer保证μ3,μ12≥1。若c(G,J)≥14，则

    t:=μ5+μ6+μ9+μ10 ≥ c(G,J)≥14。                   (4)

反向不成立：exactcross原边还可能带G∩J中的点。本证明只用(4)的必要方向。

### 5.1 K不含完整例外对时

若{u,v}不包含于K，K内全部六pair共度≤4。四余谱的全部正超额都在u,v上；K至多含其中一名，所以selected超额≤4、最大selected度≤13。直接满足[旧通用c14四锁局部定理](../../context/propertyb35-paper/round01/middle/generic_c3_fourteen_gate_20261020/PROOF.md)，并不需要原H其他点对共度≤4。该局部门已完整覆盖t14及15／16，给H可染，矛盾。

### 5.2 K包含例外对时：14个真实标记族、425库存

K内degree只可能是以下六个多重集，先列真实例外对，再列另两点：

    (10,12;9,8)，(10,12;8,8)，
    (11,11;9,8)，(11,11;8,8)，
    (10,13;8,8)，(11,12;8,8)。

若u,v在同一侧，按标记把它们编号0,1，标记pair为mask3；若分居两侧，编号0,2，标记pair为mask5。另一侧的两低点在同侧情形可固定排序，跨侧且9／8不同则保留两个分配方向。六种多重集因此恰14个marked family。这里只运输同一实际K和原边索引，不假设H有自同构。

标记pair的inclusive共度**恰5**，其他五pair inclusive共度1…4。它们给cross总inclusive预算：same侧为16，cross侧为17。设p为所有三迹重数、q=μ15，恒等

    Σ_cross λ = t+2p+4q。

与t≥14结合得q=0、p≤1，故完整高迹很小。事实上same侧时14条exactcross边各用u/v一次，而五条uv边各用两次，且两批原边不重叠，迫d_u+d_v≥24；但四种高pair的度和仅22或23，故六个same族均空。完整生成仍保留它们，并实际核空。

给定六个inclusive pair数和至多一个三迹，Möbius反演恢复全部精确pair；再从原d_i恢复single，最后由35总边数恢复empty，只保留非负及μ3,μ12≥1。**全部14标记族共425个不同必要库存**（8族非空）；exactcross总数14／15／16分别326／84／15，四迹始终零，三迹总量0／1分别326／99。

[新唯一λ5三交局部门](../../context/propertyb35-paper/round01/middle/c3_unique_high_pair_five_20261020/PROOF.md)只复用三个旧位置(8,9,20,21)、(9,10,20,21)、(9,20,10,21)，所有配额与额外扣除为零。425份全部严格，最大条件排列失败界

    U≤25963/29172<1。

独立VERIFY先以inclusive六pair／Möbius生成全域，与精确迹生成的425键及family归属逐键相等，再展开每份35个不同原边索引、1190有序异边对，逐21位置重放共8925行。所有数值相同且严格，实际PASS CPU3.203568。未选17点没有额外degree或星假设。

由条件排列判据，每个严格库存都给原H的proper染色，矛盾。因此(4)对所有实际三交外边对都不可能，终于在**同一当前H**得到

    C3≤13n3。                                      (5)

## 6. 同P总预算与完整四谱有限覆盖

令K_d(n)为degree旗成本多重集（每点v放C(d(v),2)份权d(v)）中最小n份权之和，S6为六个最大原点度之和。除(3)、(5)外，[一般middle容量引理](../../context/propertyb35-paper/round01/middle/a2_a3_joint_moment_frontier_20261020/CAPACITY_LEMMAS.md)给

    C0≤33n0，C1≤35n1−K_d(n1)，
    C2≤floor((S6−6)/2)n2。                          (6)

这些degree容量不要求全局λ≤4。全部C_j共享P=Σ_j C_j。由(1)及[共同middle恒等式](GLOBAL_TWO_FLIP_SHARED_MIDDLE.md)，若f(s)是把s均衡分成五组的跨组乘积和，则

    P≤Σ_F f(s_F)≤B(n1),
    B(n)=360 floor(2n/30)+f(2n mod30)。              (7)

这是35个0…30整数盒的凸最大值，不假设最大盒列表是图。没有T、prefix、critical、qmax29、n4≤13或额外wedge限制。

[全局单翻门](GLOBAL_PRIVATE_PAIR_REPAIR.md)给非B时n1≥397，而(1)给n1≤525。记t=n4、m=n3。原三矩和(2)给完整必要整数域

    n1=W−280−2τ+3m+8t，
    n2=140+τ−3m−6t，
    n0=735−W+τ−m−3t，                              (8)

全部n_j≥0、397≤n1≤525、0≤τ≤142。对最大度点，逐λ有C(λ−1,2)≥λ−2，仍给真实行界τ≥max(0,4Δ−40)，包括λ5而不失效。

对每个域键，把(3)、(5)、(6)的五容量，从j=4到0填入(7)同一个P预算；因权w=(36,120,330,792,1716)递增，该贪心即安全松弛的最大加权和。记分配为Ĉ_j，令

    2L=6864n1+Σ_j w_j Ĉ_j。

[原H两翻判据](GLOBAL_TWO_FLIP_PATH_REPAIR.md)保证L<2722720即H可染。全部四谱的完整整数覆盖如下：

|源ID|谱|W|τ下界|C2系数|β|完整域键|max L|strict余量|
|---:|---|---:|---:|---:|---:|---:|---:|---:|
|8|8^18,9,10,12|651|8|24|5|77912|2713662|9058|
|9|8^18,9,11^2|650|4|24|6|79183|2716104|6616|
|11|8^19,10,13|655|12|24|5|79125|2718702|4018|
|12|8^19,11,12|653|8|24|6|79650|2720004|2716|

合计315870键，全部严格，无余键。主实现按n1/t/m奇偶恢复τ；独立实现按τ/t/m直接恢复moment，另用五组乘积、缺口盒及degree旗分组重算。全部域计数、每键目标、各谱最大值及其见证均一致；独立实际PASS CPU0.588123。

[RESULT.json](../../context/propertyb35-paper/round01/middle/delta8_one_exception_scalar_20261020/RESULT.json)最初把C3≤13n3列为条件输入；第5节现已为同一个实际H供给该条件，所以此处没有隐藏的未证假设。全部315870只是必要整数松弛，不是H分类；严格上界对其全域成立，自然覆盖原H的真实moment。

## 7. 最终原对象连接与声明进口

从任意满足定理输入的H，反设非B后先得到完整15度谱和强pair二分。全λ≤4情形由小共度定理排；否则只剩唯一高pairλ5的四谱，(1)–(8)均作用于这个同一原H。第5节真实K的c≥14局部染色使实际C3≤13n3；第6节完整域严格判据最后直接输出原35条边的proper染色。没有用概率界未过、未搜到H、多模型意见或局部表数量替代原染色结论。

主要数学进口为条件排列概率引理、one-red安全前缀、通用q≤2门、全局单翻／两翻判据及一般middle容量计数；各局部门正文解释实际输入握手与有限证书。源文件与独立证据入口：

- `TWENTYONE_MINIMUM_EIGHT_SMALL_CODEGREES.md`：全λ≤4完整条件分支，保持独立冻结。
- `middle/delta8_strong_pair_transfer_20261020/REPORT.md`、`VERIFY_RESULT.json`：完整100个strong-pair输入与各原谱支持。
- `middle/min_degree_eight_singleton_star_20261020/PROOF.md`、`SCOPE_CHECK.json`、`INDEPENDENT_VERIFY.json`：无e上限的Γmin4。
- `ONE_EXCEPTIONAL_POINTPAIR_CAPACITIES.md`：唯一例外对的两个一般误差引理。
- `middle/c3_unique_high_pair_five_20261020/PROOF.md`、`DOMAIN.json`、`VERIFY_RESULT.json`：完整14标记族／425严格库存。
- `middle/delta8_one_exception_scalar_20261020/RESULT.json`、`audit/CHECK.json`：两参数化315870全strict。

以上middle相对路径从`context/propertyb35-paper/round01/`解析。本新完整scope仍pending fresh及Grok／Gemini整篇审阅；没有修改冻结A2／A3 U01–U16、运行Lean或访问编码理论项目。
