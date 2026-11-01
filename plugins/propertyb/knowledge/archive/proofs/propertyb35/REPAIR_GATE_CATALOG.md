# 已证 signed 修复门的调用接口

修复集 R 要求击中每个正集，并且不包含任何负集。所有正负族均带索引：相同集合可以有多个索引，数量和逐点出现均保留重数。记 Pk、Nk 分别为大小 k 的正、负集数量，D 为逐点正负**总索引出现**上限；U 为正族并集。表中“任意”指任意有限数量／底集，“0”是必须不存在，“—”是不另加限制。除特别列出的行外，D=7。源码节名是实际调用依据，本目录不改变原定理或其审阅状态，也不将本目录核对称为跨模型审阅通过。

## 小正族与一般纯四集门

|正族数量与大小|额外正限制|N1|N2|N3≤|N4≤|L上限|D|额外几何|准确源码节|
|---|---|---:|---:|---:|---:|---:|---:|---|---|
|≤4，每集≥2|无|0|0|3|任意|任意|7|—|[FOUR_SMALL_POSITIVE_THREE_TRIPLE_REPAIR](FOUR_SMALL_POSITIVE_THREE_TRIPLE_REPAIR.md)，「定理」|
|≤5，每集≥2|无|0|0|0|任意|任意|7|—|[FIVE_SMALL_POSITIVE_ZERO_TRIPLE](FIVE_SMALL_POSITIVE_ZERO_TRIPLE.md)，开篇命题|
|≤5，每集2..4|无|0|0|1|任意|任意|7|—|[FIVE_SMALL_POSITIVE_ONE_TRIPLE](FIVE_SMALL_POSITIVE_ONE_TRIPLE.md)，「定理」|
|≤5，每集2..4|**P2≤3**|0|0|2|任意|任意|7|—|[FIVE_SMALL_POSITIVE_TWO_TRIPLES_REPAIR](FIVE_SMALL_POSITIVE_TWO_TRIPLES_REPAIR.md)，「命题」；禁两七度外点的实际桥见末节|
|≤5，全部四集|无|0|0|10|32|任意|7|—|[FIVE_POSITIVE_TEN_TRIPLES_REPAIR](FIVE_POSITIVE_TEN_TRIPLES_REPAIR.md)，「定理」|
|≤5，全部四集|无|0|0|合计约束|合计约束|任意|7|**N3+N4≤35**|同文件，「扩展：负三／四集总数至多35」|
|≤6，全部四集|无|0|0|6|35|任意|7|—|[SIX_POSITIVE_SIX_TRIPLES_REPAIR](SIX_POSITIVE_SIX_TRIPLES_REPAIR.md)，「定理」|
|≤7，全部四集|无|0|0|4|35|任意|7|—|[SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR](SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md)，§C「扩展：至多35个负四集」；原主定理仅N4≤22|
|≤7，全部四集|无|0|0|2|22|任意|7|—|[SEVEN_POSITIVE_FOUR_SET_REPAIR](SEVEN_POSITIVE_FOUR_SET_REPAIR.md)，「扩展：至多22个负四集」；此行已被上一行包含，保留旧接口|
|≤8，全部四集|无|0|0|0|27|任意|7|—|[FIVE_POSITIVE_SIGNED_REPAIR](FIVE_POSITIVE_SIGNED_REPAIR.md)，§3「A useful zero-triple corollary for at most eight positives」|
|≤11，全部四集|无|0|0|0|17|**18**|7|—|[ELEVEN_POSITIVE_FOUR_SET_REPAIR](ELEVEN_POSITIVE_FOUR_SET_REPAIR.md)，「定理」|

## 新合并接口：负二与少量正集

|正族|N1|N2≤|N3≤|其余负≥4|D|准确源码与实际收益|
|---|---:|---:|---:|---|---|---|
|≤4，各≥4|0|3|任意|任意|7|[四大正集／三负二](FOUR_LARGE_POSITIVE_THREE_NEGATIVE_PAIRS_REPAIR.md)；I1至多三条纯三迹统一，四三迹多数选点|
|≤3，各≥4|0|4|35|任意|无要求|[三大正集／四负二](THREE_LARGE_POSITIVE_FOUR_NEGATIVE_PAIRS_REPAIR.md)；I1四条纯三迹的尾型|
|≤4，各2..4、P2≤3|0|0|4|任意|7|[四混合正集／四负三](FOUR_MIXED_POSITIVE_FOUR_TRIPLES_REPAIR.md)；I1四四迹，禁两点后P2限制来自真实共度|
|≤5，各≥3|0|1|0|仅四集、任意|7|负二任取一点禁蓝后正≥2，直接调用[FIVE_SMALL_POSITIVE_ZERO_TRIPLE](FIVE_SMALL_POSITIVE_ZERO_TRIPLE.md)；I2三三迹相邻missing尾型|

上表前两门完整保留负二，不需要分类外点布局；四大正门的两次换色必须保留原负二索引对点次数的占用。三大正／四负二门与原两负二参数门是不同的充分界，先用真实需要的接口，不要求寻找最优常数。新指定审阅状态见review reconciliation，目录自身不背书跨家族通过。

## 四正集、任意数量最小三元负集的参数门

[FOUR_POSITIVE_AT_LEAST_THREE_REPAIR](FOUR_POSITIVE_AT_LEAST_THREE_REPAIR.md)：整数s≥2、D≥1，≤4正集各大小≥s，所有负集大小≥3，若4(D−1)<3s²即可修复，ground/负条数任意。交叠点留≤2组用s²候选；全不交用所有负3/4共用同一逐点D−1容量的AMGM收费。s3/D7的共同界8/9，s4/D12为11/12，不需要人为T20界，也不允许负一/二存在。root全文独立核推导，Gemini4已有效静态专审，未执行程序；准确范围见review reconciliation。

## 四正大集的锐利无次数界

[FOUR_LARGE_POSITIVE_FORTY_THREE_NEGATIVE_REPAIR](FOUR_LARGE_POSITIVE_FORTY_THREE_NEGATIVE_REPAIR.md)：≤4正集各≥4，所有负集≥3且总索引≤43，即可修复且红集≤4，无ground/次数假设。二重点支撑无二匹配时只有星/三角；强迫三横截扣原负索引后极小四横截严格。44个负三有13点显式不可修复例，故一般界锐利。root已全文核解析证明与反例，并执行8192红集的单反例核验及10星/5三角标量PASS；正向不依赖H枚举。旧总35门为直接推论。新跨家族专项另记。

## 恰八正集：点数与负预算不可互换

|正族数量与大小|额外正限制|N1|N2|N3≤|N4≤|L上限|D|额外几何|准确源码节|
|---|---|---:|---:|---:|---:|---:|---:|---|---|
|**恰8**，全部四集|无|0|0|4|17|**17**|7|—|[EIGHT_POSITIVE_FOUR_TRIPLES_REPAIR](EIGHT_POSITIVE_FOUR_TRIPLES_REPAIR.md)，「命题、依赖和状态」|
|**恰8**，全部四集|无|0|0|3|20|**17**|7|—|[EIGHT_POSITIVE_FOUR_SET_REPAIR](EIGHT_POSITIVE_FOUR_SET_REPAIR.md)，§7「扩展：至多20个负四集」；原主定理N4≤18|
|**恰8**，全部四集|无|0|0|1|20|**18**|7|—|[EIGHT_POSITIVE_ONE_TRIPLE_TWENTY_REPAIR](EIGHT_POSITIVE_ONE_TRIPLE_TWENTY_REPAIR.md)，「定理」；旧19界被包含|
|**恰8**，全部四集|无|0|0|1|19|**18**|7|—|[EIGHT_POSITIVE_18_ONE_TRIPLE](EIGHT_POSITIVE_18_ONE_TRIPLE.md)，「定理」|
|**恰8**，全部四集|无|0|0|2|18|**18**|7|—|[EIGHT_POSITIVE_18_TWO_TRIPLES](EIGHT_POSITIVE_18_TWO_TRIPLES.md)，「定理与依赖」|
|**恰8**，每集3/4|**P3≤1**|0|0|2|19|**18**|7|—|[EIGHT_MIXED_ONE_SMALL_TWO_TRIPLES_REPAIR](EIGHT_MIXED_ONE_SMALL_TWO_TRIPLES_REPAIR.md)，完整定理及独立384标记/2有理证书|
|**恰8**，每集3/4|**P3≤2**|0|0|0|21|**18**|7|—|[EIGHT_MIXED_TWO_SMALL_EIGHTEEN_REPAIR](EIGHT_MIXED_TWO_SMALL_EIGHTEEN_REPAIR.md)，「扩展：至多二十一个负四集」|
|**恰7四集+恰1三集**|P3=1|0|0|0|20|**18**|7|—|[EIGHT_MIXED_POSITIVE_EIGHTEEN_REPAIR](EIGHT_MIXED_POSITIVE_EIGHTEEN_REPAIR.md)，「定理」；已被上一行包含，保留原精确接口|

两份旧七／八正四集文件另分别有「负约束总数至多21的推论」：七门为N3≤2、N3+N4≤21，八门为N3≤3、N3+N4≤21且L≤17、正数恰8。它们把超额负四集缩为三元子集而不增加逐点出现；这些推论不放宽正族数量或点数前提。

## 九正四集与共同负预算

恰九个正四集、N1=N2=0、N3≤3、**N4任意有限**、L≤18、D7时，[NINE_POSITIVE_JOINT_NEGATIVE_REPAIR](NINE_POSITIVE_JOINT_NEGATIVE_REPAIR.md)给出修复。总关联36+3N3+4N4≤126自动推出N3+N4≤23；完整23预算证明在该文件末节，含981旧域的全部差分与新19份精确证书。原20／21预算已被包含，但不是“≤九正”门，也不允许负一／二集。主代理已全文核查并复算，新增23预算已有Gemini4有效静态专项审阅，实际范围另记。

## 十正四集与至多两个负三集

恰十个正四集、N1=N2=0、N3≤2、**N4任意有限**、L≤18、D7时，[TEN_POSITIVE_TWO_TRIPLES_REPAIR](TEN_POSITIVE_TWO_TRIPLES_REPAIR.md)给出完整修复。40+3N3+4N4≤126只留下原(t,bmax)=(0,21),(1,20),(2,20)；高出现导入九门预算23、双不交三中心用原1333证书的1813成本更新、相交三支持用完整七标签3015域的三比值统一界。全部实际分支已接，root读证明和独立程序并运行精确检查；新增完整装配/任意B扩展已获Grok有效静态专项审阅，未执行计算，实际范围另记。该定理不是“≤十正”，也不能忽略实际负二／一集。

## 至多六个混合正集的已证辅助门

[NINE_POSITIVE_JOINT_NEGATIVE_REPAIR](NINE_POSITIVE_JOINT_NEGATIVE_REPAIR.md)附录B第2节已经完整证明：≤6正3/4、≤3正三、N1=N2=0、N3≤1、N4任意、D7，ground任意。低出现收费31279645/31850496，高出现留下≤3组以8<27修复。该独立signed辅助门不要求原系统恰九正，也不要求两核存在；过去仅藏在附录里，本目录现在显式登记，避免重复证明或让selector漏用。

## 至多七个混合正集

|正族数量与大小|额外正限制|N1|N2|N3≤|N4≤|L上限|D|额外几何|准确源码节|
|---|---|---:|---:|---:|---:|---:|---:|---|---|
|≤7，每集3/4|**P3≤2**|0|0|1|**任意**|任意|7|—|[SEVEN_MIXED_TWO_SMALL_ONE_TRIPLE_REPAIR](SEVEN_MIXED_TWO_SMALL_ONE_TRIPLE_REPAIR.md)，「定理」|
|≤7，每集3/4|**P3≤4**|0|0|**0**|**任意**|任意|7|—|同文件，「无负三集扩展：至多四个正三集」|

旧 [SEVEN_MIXED_POSITIVE_ONE_TRIPLE](SEVEN_MIXED_POSITIVE_ONE_TRIPLE.md)（P3≤1、N3≤1、N4≤20）和 [SEVEN_MIXED_POSITIVE_ZERO_TRIPLE](SEVEN_MIXED_POSITIVE_ZERO_TRIPLE.md)（P3≤1、N3=0、N4≤21）均被上表覆盖，无须继续让实际selector受旧N4上限限制。

## 三正集与负二集的无次数参数门

[THREE_POSITIVE_FOUR_NEGATIVE_PAIRS_REPAIR](THREE_POSITIVE_FOUR_NEGATIVE_PAIRS_REPAIR.md)：整数k≥2，≤3正集各大小≥k，负二≤k、其余负集大小≥4，即可修复且红集≤3。ground/逐点次数/大负条数均不限。交点给k个两红，若全堵迫全部负二组成同一星，禁该点蓝后≤3红即安全；三正不交给k³>k²。k4直接处理≤3P4/≤4N2/零T/任意B，实际I1七三迹一四迹的单蓝分流已接。主代理全文核数学；新的跨家族专项另记。

## 五正最小三元与一个负二集

- [FIVE_POSITIVE_THREE_TRIPLES_REPAIR](FIVE_POSITIVE_THREE_TRIPLES_REPAIR.md)：≤5正集各大小≥3、N1=N2=0、N3≤3、N4任意、D7；无ground上限。正≥3高点、重复点是否遇T、全不交三分流为短解析证明。
- [EIGHT_POSITIVE_ONE_NEGATIVE_PAIR_REPAIR](EIGHT_POSITIVE_ONE_NEGATIVE_PAIR_REPAIR.md)：恰8P4、N1=N3=0、N2≤1、N4≤21、L18/D7。按负二两端的正频率≤2/≥4/3,3穷尽。
- 同文件推论：≤7P4、N1=N3=0、N2≤1、N4任意、D7，ground任意有限；选端蓝后至多四正三，或红蓝端后余至多二正，均接旧门。

- [NINE_POSITIVE_ONE_NEGATIVE_PAIR_REPAIR](NINE_POSITIVE_ONE_NEGATIVE_PAIR_REPAIR.md)：恰9P4、N1=N3=0、N2≤1、N4≤17、L17/D7。完整证明用五正3T、既有六mixed1T、旧981的5783/7266完整容量标记及E6的19916标签/741轨道；root读证明/第二实现并实际执行PASS。当前尚无新的完整P7库存由此直接闭合，不能把通用门与实际收益混同。

[共同小负点推论](COMMON_SMALL_NEGATIVE_POINT_REPAIR.md)：≤5正集各≥4，负三≤3、负四任意，全部负一／二集有同一个公共点f，D7/任意ground，则固定f蓝后接五正最小三元门。不可把多个不同禁红点误算成一个。

## 大正并与负二集门

|正族数量与大小|N1|N2≤|N3≤|N4≤|L上限|D|**额外几何**|准确源码节|
|---|---:|---:|---:|---:|---:|---:|---|---|
|**恰5**，全部四集|0|0|9|任意|任意|7|**\|U\|=17**|[TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_PARTIAL](TWENTYFOUR_SEVEN_HIGH_THREE_INTERNAL_PARTIAL.md)，「小正族引理」，引理B；这条是自含的一般signed引理|
|**恰6**，全部四集|0|0|15|合计约束|**17**|7|**\|U\|≥15、N3+N4≤27**|[SIX_POSITIVE_LARGE_UNION_TOTAL_TWENTY_SEVEN_REPAIR](SIX_POSITIVE_LARGE_UNION_TOTAL_TWENTY_SEVEN_REPAIR.md)，完整定理/强迫C3、M3=14/15解析|
|≤6，全部四集|0|0|8|20|任意|7|**\|U\|≥14**|[SIX_POSITIVE_LARGE_UNION_REPAIR](SIX_POSITIVE_LARGE_UNION_REPAIR.md)，「定理」|
|**恰5**，全部四集|0|4|1|22|任意|7|**\|U\|≥17**|[FIVE_SPARSE_POSITIVE_SMALL_NEGATIVE_REPAIR](FIVE_SPARSE_POSITIVE_SMALL_NEGATIVE_REPAIR.md)，「定理」|
|**恰4**，全部四集|0|4|0|23|任意|7|**\|U\|≥14**|同文件，「四正四集推论」|
|**恰5**，全部四集|0|3|3|21|任意|7|**\|U\|≥17**|同文件，「三个负二集的稀疏推论」，第1项|
|**恰4**，全部四集|0|3|2|22|任意|7|**\|U\|≥14**|同节，第2项|
|**恰3**，全部四集|0|3|1|23|任意|7|**\|U\|≥11**|同节，第3项|
|**恰2**，全部四集|0|3|任意|任意|任意|**无要求**|**\|U\|≥8**（两集不交）；负集除二集外允许任意大小≥3|同节，第4项|

上述负二集门允许先合并完全相同的负二集，因为它们的逻辑避免要求相同；原输入仍先满足表列数量和总出现上限。该特定去重理由不等于可以任意忽略不同原边索引的度数。

同一稀疏规范末尾现已稳定的「统一参数推论」还包含上述多种格：取整数0≤R≤4、0≤S≤3，令T=9−2R−S≥0、B=18+R+S。若正族**恰5−S个四集**、正并≥17−3S，负族满足N1=0、N2≤R、N3≤T、N4≤B，且D7，则可修复，L无上限。R/S是数值参数，不能独立增加T或B而保持这一接口。此扩展的跨模型审阅范围另记，不由目录背书。

## 特殊预算及直接概率接口

若实际总出现预算不是七，仍有 [FIVE_POSITIVE_SIGNED_REPAIR](FIVE_POSITIVE_SIGNED_REPAIR.md) §1、§2：

|正族|N1/N2|N3≤|N4≤|D|L|
|---|---|---:|---:|---:|---|
|恰5四集|0/0|4|28|14|任意|
|恰5个3/4集|0/0|2|28|14|任意|
|≤5四集|0/0|4|28|10|任意|
|≤5个3/4集|0/0|2|28|10|任意|

§2中的补齐仅在已证明的D10→D14额度下进行，不是一般padding规则。

[RANDOM_TRANSVERSAL_REPAIR](RANDOM_TRANSVERSAL_REPAIR.md) 的「一般非均匀定理」还允许任意非空正族和任意负族：给每正集分布πi，若 Σ负集F ∏_{x∈F}[1−∏i(1−πi(x))]<1 即可修复，无额外L/D条件。其「小负集的完整容斥版」「一个共现点对的通用扣除」「最大正出现至多二时的二重点负出现预算」可直接加强该界。它们都需要在真实输入上证明相应严格概率和，不能仅凭约束条数默认调用。

[OCCURRENCE_CHARGED_REPAIR](OCCURRENCE_CHARGED_REPAIR.md)「一般定理」将同一判据按正关联收费；类型集合必须覆盖实际所有点类型。其七度3/4五类型实例附有**最大正出现≤2**前提，不是完整混合门的替代。

## 三条实际选择提醒

1. **不任意padding。** 恰八门不能靠复制正集处理不足八个的输入；复制会增加总出现。优先选真实“≤”门，或者单独证明所用补齐的度数额度。
2. **17点门不能用于18点。** 可将候选红集限制在一个已证明足够的子域，但必须证明所有正约束在该域仍按所用门成立；不能只删去一个底集点后继续沿用原正集参数。
3. **正负小迹必须完整恢复。** 全蓝三P迹产生正二集，全红三／四P迹产生负二／一集，均不能省略。这里表内N1均为零；出现负一集时须真固定该点蓝并相应缩短正集，出现负二集时须选相应稀疏门或另作合法修复。若原边避开所有固定点，它同时有两种单色风险，不能按“每边至多一个约束”直接推D≤原点度。

## 共同阻断和蓝关联的通用规约

[FORCED_SMALL_TRANSVERSAL_BUDGET](FORCED_SMALL_TRANSVERSAL_BUDGET.md)：没有负一/二时，若全部三点横截都被堵，它们各自强迫一份不同原负三。极小四点横截不再被这些已用索引堵住，需在剩负条数和每点容量中同时扣除。不可将强迫负三既计入三点堵界，又当作可自由堵四点的剩预算。

真实P7部分染色只有mP4/rN2/bB4时，点对覆盖给蓝a点满足r+b≥34−7a；因此两蓝绝不能直接调用新的九正N2≤1/B17门。推导与实际范围见 `context/propertyb35-paper/round01/twentyfour/nine_positive_one_pair_20261020/TRANSFER_DIAGNOSIS.md`，它能在扫描前排除不可能的caller。
