# 二十一点唯一六度、恰二或三七度：完整纸面证明

## 定理与本稿状态

设H是21点上的35条互异五元边，覆盖全部不同点对，最小度六且唯一六度点为x，恰有a∈{2,3}个七度点。则H有Property B。

本文是完整实际A2／A3两支的自然语言装配候选：使用下述局部门与全局两翻判据，完整必要整数域由两个不同生成法逐键核对。第6节A2四谱全严格；第7节A3中间必要档33键由第8节低中心Γ门统一排除。33键不是H分类或实际H。主链不使用旧T34临界性／T33黑箱、Γ最大度29、threshold T或degree-prefix DP。全21／36均不由本稿宣称完成，最终root与指定跨家族验收另记。

## 1. 从原H强迫完整四谱，兼保A3诊断域

反设H非B。以下同时处理七度点数a∈{2,3}。令b为八度点数，e=Σ_v max(d(v)−9,0)。175总度给

    e=2a+b−11≥0。

x的共度行和为24，覆盖其他20点，所以Σ_{v≠x}(λ(x,v)−1)=4。若r名七度点非unit，则八度非unit至多4−r名。由[六unit8池定理](../../context/propertyb35-paper/round01/twentyone-high/unique6_with7/new_structure_20261020/SIX_UNIT8_POOL_PROOF.md)，非B时unit8至多五，故

    11−2a≤b≤9−r≤9，e≤2a−2≤4。                     (1)

其余20−a−b个点度均≥9，写其正盈余为e的整数分拆。因为e≤4，分拆长度不超过四，而这些点至少八名，任何分拆都可放入；不需要标签／星布局假设。忽略r并取其必要并集即可：A2恰四个degree谱，A3十二谱，合计十六，没有因固定r漏掉一整谱。

|a7|b8|正盈余分拆|e|W|最大点度|
|---:|---:|---|---:|---:|---:|
|2|7|空|0|649|9|
|2|8|1|1|650|10|
|2|9|1+1|2|651|10|
|2|9|2|2|652|11|
|3|5|空|0|650|9|
|3|6|1|1|651|10|
|3|7|1+1|2|652|10|
|3|7|2|2|653|11|
|3|8|1+1+1|3|653|10|
|3|8|1+2|3|654|11|
|3|8|3|3|656|12|
|3|9|1+1+1+1|4|654|10|
|3|9|1+1+2|4|655|11|
|3|9|1+3|4|657|12|
|3|9|2+2|4|656|11|
|3|9|4|4|660|13|

例如第一谱为6,7²,8⁷,9¹¹。一般完整degree列表是6、a个7、b个8、20−a−b个九基线加上该分拆，长度21且总度175。

## 2. 对同一原H的实际结构进口

1. [实际A2／A3强共度归约](../../context/propertyb35-paper/round01/middle/generic_high_degree_pair_gates_20261020/REPORT.md)给非B全λ≤4，已包含center6的λ5、全部7…13高pair门与仅可达A3四尾，而非借A1 Δ9门。
2. [三重四核实际门及§7](../../context/propertyb35-paper/round01/middle/generic_quad_core_multiplicity_three_20261020/PROOF.md)给非B的n4≤13。通用四锁6923标签／3809代表留下四个10^4必要尾，真实A3共同六度unit星将四尾恢复为23份五锁全strict；A2 e≤2已不可能落四尾。之后由通用六星C≥164896、删星29／20非1交rank≥11得Hbar四交≤6；每条x边跨星四交≤1、星内≤1，合计13。没有导入A1 n4≤8／rank19。
3. [实际Γ最小度四](TWENTYONE_UNIQUE_SIX_TWO_OR_THREE_SEVEN_MINIMUM_NONUNIT_DEGREE_FOUR.md)给全q_Γ(F)≥4。该定理的q3证明独立于强共度门，不与本稿循环。
4. Γ是35点简单图，自动q_Γ(F)≤34；本稿不使用更强的29界。[旧局部导入](../../context/propertyb35-paper/round01/middle/generic_quad_core_multiplicity_three_20261020/IMPORT_SCOPE.md)仍为有用独立结果，但已从本证明依赖中删除。
5. [新c14门](../../context/propertyb35-paper/round01/middle/generic_c3_fourteen_gate_20261020/PROOF.md)由全λ≤4和e≤4给C3≤13n3。exactcross14的7812／1144全zero配额及旧t15／16必要域完整覆盖，不要求至多一个七度点。

所有进口都从本节同一个实际H适用；没有把不同源／染色的预算拼接。新四核／c14／Γmin4完整范围的审阅状态分别以其实际证据为准，不借此前A1全稿审阅扩大。

## 3. 原三moment与τ的真实点行下界

令n_j为原35边的无序异边交j的数量，j0…4；W由实际degree谱决定。全λ∈{1,2,3,4}，并记

    τ=Σ_{pointpair} C(λ−1,2)。

350份pair关联覆盖210个点对，Σ(λ−1)=140；因C(z,2)≤z对z0…3，0≤τ≤140。三个精确moment为

    Σn_j=595，Σj n_j=W，ΣC(j,2)n_j=140+τ。

以m=n3、t=n4消元，得唯一

    n1=W−280−2τ+3m+8t，
    n2=140+τ−3m−6t，n0=735−W+τ−m−3t。             (2)

[全局单翻门](GLOBAL_PRIVATE_PAIR_REPAIR.md)已给非B必要n1≥397。另t≤13由第2节，所有n_j≥0。

对任原点v，覆盖其余20点及五元性给Σ_{u≠v}λ(v,u)=4d(v)。逐整数λ≥1有C(λ−1,2)≥λ−2，故其incident τ行

    τ_v=Σ_{u≠v}C(λ(v,u)−1,2)≥4d(v)−40。

这一行是全τ的一部分，不能误除二，所以

    τ≥max(0,4(Δ−10))。                              (3)

同样可得2τ≥Σ_v max(0,4d(v)−40)，但本稿计算只需(3)。它完全来自原pointpair行，不是从图degree放松猜出的cut。

## 4. 共同middle预算：只有35个真实盒，且每盒s∈0…30

对原middle边F，令五个singleton附着数t(F,g)，s(F)=Σ_g t(F,g)。[共同middle恒等式](GLOBAL_TWO_FLIP_SHARED_MIDDLE.md)给

    P:=Σ_{j=0}^4 C_j=Σ_F Σ_{g<h}t(F,g)t(F,h)，Σ_Fs(F)=2n1。

给定s，五组平方和最小时均衡，故每边贡献≤

    f(s)=[s²−(5−r)c²−r(c+1)²]/2，s=5c+r，0≤r<5。

该整数函数凸，差分f(s+1)−f(s)=s−floor(s/5)单调。Γmin4及简单性给s(F)=34−q(F)在0…30。令E=595−n1、X=2E−140=Σ_F(30−s(F))。必须0≤X≤1050，特别n1≤525。

在固定35盒、总质量且每s∈0…30下，将两个内部盒(x,y)（0<x≤y<30）改为(x−1,y+1)，凸性使Σf不减。重复后至多一个内部盒。写X=30u+v，0≤v<30，得到安全上界

    P≤B(n1)=u f(0)+(35−u)f(30)                 若v=0；
    P≤B(n1)=u f(0)+f(30−v)+(34−u)f(30)       若v>0。  (4)

f(0)=0、f(30)=360。此最大盒列表不必是图degree序列，所以只是安全必要松弛；没有对实际Γ进行不保持Gram的threshold压缩。**主证明只需(4)，无需旧threshold T及其DP、临界性或q≤29。** 早先容量25／s≥5的版本保留历史；重新从原16谱生成、仅用容量30及B的两个实现，仍给全部202／33键和每谱最大L完全一致。

## 5. 五容量与精确同P加权界

[一般degree容量证明](../../context/propertyb35-paper/round01/middle/a2_a3_joint_moment_frontier_20261020/CAPACITY_LEMMAS.md)给

    C0≤33n0，C1≤35n1−K_d(n1)，
    C2≤(24+floor(e/2))n2，C3≤13n3，C4≤4n4。       (5)

其中K_d(N)是Σd_v z_v的最小值，Σz=N、0≤z_v≤C(d_v,2)：实际z_v为singleton外边对在v的个数，所以可按degree由小到大填容量得安全下界。六个最大点度和恰54+e，且每两交middle在六exclusive点付两次关联，故C2系数如上。C0排除两个outer；C4的两个exclusive点paircap4给其cap。C3来自新实际门。

全部C_j≥0且共享ΣC_j=P≤B，不能分别花五次P。权w=(36,120,330,792,1716)递增，所以按j4→0贪心填(5)到总B，恰为该标量松弛的最大加权和。令其分配为Ĉ。

[原H全局两翻修复](GLOBAL_TWO_FLIP_PATH_REPAIR.md)给，只要

    L:=3432n1+(1/2)Σ_j w_j Ĉ_j <2722720，          (6)

原H即有proper染色。原C被同H的Ĉ目标支配，故计算的是同一原H的实际修复概率上界；没有要求Ĉ或盒极值实际可实现。

## 6. 完整有限整数覆盖与A2四谱严格表

第一个实现对每个第1节degree谱，完整生成τ0…140、t0…floor((140+τ)/6)、m0…floor((140+τ−6t)/3)，由(2)恢复所有n_j，保留非负和n1≥397。这个起始16谱域有1,357,926带谱键；旧wedge给1,355,158，旧cap14＋T给35083，均仅作完整旧结果crosscheck。新t≤13时wedge整数凸下界为0，主证明不需再导入该额外条件。

第二实现先固定全部n1=397…525、t=0…13，再取m0…floor((W−n1−4t)/3)，检查W−280+3m+8t−n1为偶数，以其半值恢复τ，及

    n2=(W−n1−3m−4t)/2，n0=595−n1−n2−m−t。

保留0≤τ≤140、非负与(3)。这覆盖且仅覆盖当前显示条件的全部整数必要域，未读取旧35083／5813的幸存列表。两种域构造先后给无行cut的202键及加(3)后的33键逐项相等。

A2四谱在全部上述必要域上得到下列**最大**L，非只检查已存少数候选：

|b8|正盈余分拆|最大L|距2722720严格余量|
|---:|---|---:|---:|
|7|空|2713872|8848|
|8|1|2718744|3976|
|9|1+1|2719626|3094|
|9|2|2716860|5860|

若存在原非B A2，它必落四谱之一及本整数域，原L不超过对应表项；由(6)又可染，矛盾。因此第1节的A2完整定理成立。尚不为此候选的独立最终验收状态命名，也不把全36标为完成。

## 7. A3的33份中间必要键及独立完整证据

在尚未加第8节低中心门时，A3十二谱中b5空、b6分拆1、b8分拆1+2三谱已由同样必要域排尽，其余九谱共33必要aggregate键：

|b8|正盈余分拆|余键数|
|---:|---|---:|
|7|1+1|1|
|7|2|1|
|8|1+1+1|3|
|8|3|1|
|9|1+1+1+1|6|
|9|1+1+2|3|
|9|1+3|4|
|9|2+2|6|
|9|4|8|

[NO_CRITICAL_SURVIVORS33.json](../../context/propertyb35-paper/round01/middle/a2_a3_min4_cap13_closure_20261020/NO_CRITICAL_SURVIVORS33.json)逐键保存degree绑定／n／τ／P／五caps／同P分配和精确2L，不称33个H类。[NO_CRITICAL_BEFORE_ROW202.json](../../context/propertyb35-paper/round01/middle/a2_a3_min4_cap13_closure_20261020/NO_CRITICAL_BEFORE_ROW202.json)保留前一必要档。原容量25的RESULT／CHECK／SURVIVORS33文件仍保留，不覆盖历史。

[NO_CRITICAL_FILTER.py](../../context/propertyb35-paper/round01/middle/a2_a3_min4_cap13_closure_20261020/NO_CRITICAL_FILTER.py)从a,b及e递归分拆生成十六谱，完整原moment域，以容量30盒界独自支配P，保存[NO_CRITICAL_RESULT.json](../../context/propertyb35-paper/round01/middle/a2_a3_min4_cap13_closure_20261020/NO_CRITICAL_RESULT.json)，实际CPU2.972322。其T表只用于复现旧35083作对照，不参与新P或maxL。新[NO_CRITICAL_CHECK.py](../../context/propertyb35-paper/round01/middle/a2_a3_min4_cap13_closure_20261020/NO_CRITICAL_CHECK.py)不导入T，改用high-excess重数hist生成十六谱，按另一奇偶参数化完整重生；独立35-slot精确标量knapsack核全部1051个X状态的(4)，按degree成本层填K_d，重算全部分配与有理L。所有202／33全key及分配与原档完全相等，A2四谱完整max也相等，[NO_CRITICAL_CHECK.json](../../context/propertyb35-paper/round01/middle/a2_a3_min4_cap13_closure_20261020/NO_CRITICAL_CHECK.json)实际PASS2.863732CPU。连同原容量25两个实现，本轮四run总CPU11.734173<15，无H／自由外点布局搜索、无Lean／v2或导航／旧主稿修改。

## 8. 真实低中心q4门：33键共同E≤72却必E≥73

[唯一六度中心的q4局部门](../../context/propertyb35-paper/round01/middle/four_nonunit_degree_six_center_20261020/REPORT.md)说：H21／35simple，F含唯一六度x；其他F点度≥7、F中七度点≤3、F上总高点盈余≤4、F内十pair共度≤4，六条x边覆盖其余20点，若q_Γ(F)=4则H可染。它不要求Γ其他节点先有min4，因而与第2节min4进口无循环。

这些条件在当前两个实际分支中同时成立：唯一六度及minimum6给F其他点≥7；a≤3给F中七度点≤3；(1)给其局部high-excess≤4；强共度门给全λ≤4；paircover给x-star覆盖20点。因此在非B假设下，六条过x原边都不能q4，结合已得全q≥4，便每条过x边的q≥5。其他29条原边q≥4。对**同一原35边图Γ**握手得

    2E=Σ_F q(F)≥6·5+29·4=146，故E≥73。           (7)

局部门的完整必要域为23751个四异常迹multiset／1563个marked S4轨道。四异常迹可重复、可空；把x固定为label0。实际paircap／x-star重复成本四／其余点原度与全部safe-anchor failure sets只留下40有标签迹＋附着输入／5联合轨道；五份完整35原迹在既有16位置菜单zero-quota全strict，最大233003/240240。另一实现从全部23751标签按incidence signatures与互补组合数恢复全域／70阈值组／5联合尾，并逐35索引、1190异边对×21位置核每张证书。[INDEPENDENT_RESULT](../../context/propertyb35-paper/round01/middle/four_nonunit_degree_six_center_20261020/INDEPENDENT_RESULT.json)和[FIVE_LOCK_FULL5](../../context/propertyb35-paper/round01/middle/four_nonunit_degree_six_center_20261020/FIVE_LOCK_FULL5.json)保存真实结果。此处只调用这一完整已交付局部定理，不在本稿重跑它或改其代码。

另一方面，第7节全部33中间键均有E=595−n1≤72，精确分布E70／71／72分别24／7／2。无行τcut的202键仍有E最高77，所以(3)不能从本链删除；不是把E≤72当全moment域的未经证明性质。加入(3)后的完整域和(6)恰只留这33键，故(7)排尽所有A3必要键，矛盾。

至此A2已由第6节严格表、A3由完整33键及同H的(7)都回到原proper染色／反证，得到开头两支完整纸面候选。局部有限核的充分概率界、必要moment放松、共同盒上界与低中心门各保持其真实输入域；没有假定任何最优盒列表／aggregate键可实现，也没有升级整个21或36。新装配与新增进口的最终root／fresh／指定跨模型验收仍按实际进行。

## 9. 规范稿与历史档的边界

本规范固定上述无threshold T、无旧T34／critical、q∈4…34的完整两支版本。研究目录最早的A2-only／33残说明已由本稿第8节加强；原`FILTER.py`／`RESULT.json`、`CHECK.py`／`CHECK.json`及容量25的202／33数据作为历史证据保持不变，不再作为主证明的额外前提。当前研究`PROOF.md`／`REPORT.md`已同步最终实际连接，但规范入口以本文件为准。

最终计算输入为`NO_CRITICAL_FILTER.py`／`NO_CRITICAL_RESULT.json`、`NO_CRITICAL_CHECK.py`／`NO_CRITICAL_CHECK.json`、`NO_CRITICAL_SURVIVORS33.json`及`CHECK_ASSEMBLY.py`／`ASSEMBLY_CHECK.json`；后者只核33→E矛盾及导入凭据，不冒充重新生成低中心q4局部门。旧IMPORT_SCOPE仍是独立已核局部结果，但不在当前定理依赖中。新的fresh整篇与跨家族审阅以本规范及这些实际输入为范围；未返回者不记认可。全m(5)≥36、其他21–25未闭分支及旧35 Lean paused状态均不改变。
