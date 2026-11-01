# 九正四集、一个负二集：本轮完整候选与确定性范围

本轮得到候选通用定理：**L≤17、恰9P4、至多1N2、T=0、B≤17、D7时可修复**。完整推导在[PROOF.md](PROOF.md)，未修改规范、导航、旧Goal。原P7动机中的Fano结构、某个蓝三点的存在或9P4接口均未在本轮假设为真；实际应用仍须另证caller。

原命题先按最大正次数及负二端点分流：任意点正次数≥4时，令其红、负二一端蓝，余≤5个大小≥3正集和≤3T，直接新五正门。某端≤2时禁该端，归九混合≤2P3／零T／B17／L16。两端都3且其他点≤3时，选择活跃原B较少的一端红、另一端蓝，得到六混合≤3P3；T≤1复用已有九正规范附录B§2的六混合辅助门，T=t∈{2,3}时原两端共享负边给**B'≤17−2t**，不能把B17重新全部使用。

两个剩余通用引理均已完整覆盖。低端点引理的双三中心分流保留新负二，必要时禁端后fourSmall3T；高端点六混合若有正三重点，迫三负三后转色成≤4个min2正集／≤2T。低正出现部分使用[强迫小横截预算](../../../../../proofs/propertyb35/FORCED_SMALL_TRANSVERSAL_BUDGET.md)：先让每份C3消耗不同原T，再只计不含任何C3的minimal C4，同一批原预算不返还。

|精确子域|完整计数|严格结论|
|---|---:|---|
|低端点九混合：旧981图上1/2容量3标记、U≤15、M3≤4|5783标记行|minimalC4−(29−4M3)≥7|
|共享预算六混合：旧981上0..3容量3标记、U≤15、M3≤3、E≥7|7266标记行|minimalC4−(23−4M3)≥13|
|唯一新E6容量333444边界|19916标签，741个S3×S3轨道|737型直接界，3型core度预算，1型C5|

前两行是**完整已验旧图域上的容量位置标记**，不是新图分类，也不是将容量四直接当容量三。所有实际容量标记在送到旧S6代表时随置换运输，枚举该代表全部允许标记即覆盖。没有按负布局取商或分别换正负标号。

E6第一生成器从十五端对取六的38760个多重组合筛容量／M3，第二实现按顶点向后星递归完整生成。第二实现得到的19916标签键与741代表全部真实S3×S3群像逐项相等，没有遗漏、额外或重复。每个实际二重点保留独立边点，平行边不会合并。

三个18候选边界的pairfamily分别为两种K1,2及一种2K2。前者公共点正2、负cap5，使总堵≤11<18；后者四core点负关联总cap20，使总堵≤16<18。唯一M2=0边界有三个隔离三集与三个容量四标签的双三角，其C3=C4为空，必须用324个C5；实际三／四目标扩展最大12／4，3T13B至多堵88<324。这不是反例，也没有因候选为空而删输入。

## 保存产物及独立验核

* `LOW_ENDPOINT_PROFILE.py/json`：5783行，发现计数为64项容斥及C3上闭包容斥。
* `HIGH_SHARED_PROFILE.py/json`：7266行，同一旧域、新准确共享预算。
* `E6_PROFILE.py/json`：完整E6域、741代表、轨道大小和三种低界边界。
* `INDEPENDENT_CHECK.py/json`中的结果文件为`INDEPENDENT_RESULT.json`。只用标准库，不导入发现或旧生成器代码；从旧981数学过滤条件重建全部标记key，不只读取保存行。随后用直接三／四点子集覆盖OR计数复算，与发现的容斥不同。两标记域共9462个不同图／容量键经过直接计数。
* 同一独立程序用完整向后星生成E6标签域，对照741代表全部群像；再直接核三型pairfamily、core正次数及负度标量，并直接枚举唯一型的全部C5及其三／四目标扩展。

`INDEPENDENT_RESULT.json`为PASS。发现三个程序合计CPU约1.1秒，第二实现CPU约0.54秒。没有求解器、LP、SAT、负边布局搜索或H枚举。此结果是本机确定性候选证据，通用归约及新门仍由主代理核查并决定是否promote；未冒称Grok/Gemini已审。

## 复算

    python3 context/propertyb35-paper/round01/twentyfour/nine_positive_one_pair_20261020/LOW_ENDPOINT_PROFILE.py
    python3 context/propertyb35-paper/round01/twentyfour/nine_positive_one_pair_20261020/HIGH_SHARED_PROFILE.py
    python3 context/propertyb35-paper/round01/twentyfour/nine_positive_one_pair_20261020/E6_PROFILE.py
    python3 context/propertyb35-paper/round01/twentyfour/nine_positive_one_pair_20261020/INDEPENDENT_CHECK.py

本轮不判断实际P7库存必能进入新九负二门，也不改变完整m(5)目标状态。
