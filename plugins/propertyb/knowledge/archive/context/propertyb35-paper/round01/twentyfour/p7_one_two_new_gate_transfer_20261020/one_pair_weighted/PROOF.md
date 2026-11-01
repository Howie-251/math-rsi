# 七高点、一条二迹、单迹总数27的统一加权三蓝修复

## 定理

设H为24点、35条互异五元边的点对覆盖超图，最小度七，无全七度边，高点集P恰七点。下列两个库存均具有Property B：

* 恰一内部边，$(n_2,n_3,n_4)=(1,2,4)$；
* 恰两内部边，$(n_2,n_3,n_4)=(1,3,2)$。

证明统一使用同一加权公式。完整702个quad位置、1590494份必要源全部严格；两种不同生成／候选实现核对完整键集及全部原迹分类，最小余量1。本机计算范围如下文，不冒称指定跨家族专项审阅已完成，不扩称所有一／二内部或全局下界完成。

## 1. 真实原迹、容量和候选

175总度相对24点七度基线只盈余七，故七高点全八度，外部L恰17点全七度。无全七度边保证P击中所有原边。记ci为内部出现，ai为高三迹原频率，bi为高四迹原频率，J为唯一二迹，si=1_{i∈J}。实际单迹数为

$$u_i=8-c_i-a_i-b_i-s_i\ge0.$$

两库存均恰27单迹：I1为56−5−6−16−2=27，I2为56−10−9−8−2=27。全部高迹允许重复，a、b保留每条原边索引。

任意三点蓝集Q自动使内部五边proper。预先排除Q等于某个高三迹，以及J⊆Q；后者会产生正外部三集，不能无视后套pure门。令A为不同高三迹，D为全部不同高迹，取

$$\mathcal C=\{Q\in{P\choose3}:Q\notin A,\ J\nsubseteq Q\},$$
$$m_Q=\sum_{i\in Q}u_i,\quad t_Q=\boldsymbol1_{Q\cap J=\varnothing},
\qquad\lambda_Q=(12-m_Q-t_Q)_+.$$

令W为所有候选权和，M为对每个不同高迹T累加Q∩T=∅的权，Δ=W−M。非负权并界给出：**若Δ>0，则存在proper全部高迹的候选Q，且mQ+tQ≤11。** 候选先排全蓝三迹，高四迹不可能被三点Q全包含；所以命中高迹就保证proper。正整数权迫m+t≤11。

对相同P迹只逻辑合并其相同颜色阻断事件，计算ai、bi、ui时不合并原边索引。这个统一判据不选择输入相关的新权，也不把已找到的单个Q当作点质量。

## 2. missing形状、群及全部quad位置

I1唯一内部标准化为01234，稳定子群S5×S2阶240。四个四迹从35种四集选允许重复多重集，原始域C(38,4)=73815。

I2两个内部的missing二对互异，仅有相邻01,12或不交01,23两形。相邻群固定共同缺失点1，交换端点0、2并任意置换其余四点，阶48；不交群交换两missing边及各端点，并任意置换另外三点，阶48。两个四迹原始域C(36,2)=630。

各群一次共同作用于全部quad多重集，按最小像取代表，结果为：

|case|内部标准形|原始quad多重集|quad轨道／job|必要源|最小Δ|
|---:|---|---:|---:|---:|---:|
|0|01234|73815|615|498738|3|
|1|missing01,12|630|46|264619|1|
|2|missing01,23|630|41|827137|3|
|合计||75075|702|1590494|1|

`QUAD_ORBITS.py/json`完整生成群及其作用：对全部原始quad多重集，首次遇到者生成所有群像、保留最小代表，轨道像互不相交且恢复全部原始键。数据保存全部702代表、各轨道大小及**全部75075个带标签quad多重集键和每键实际transport置换索引**，并非只保存轨道数。

独立`VERIFY_QUAD_TRANSPORTS.py`按群结构因子生成240／48／48元素，不用主程序的S7过滤法；核完整群集合、全部75075键、每个轨道全像及具体运输。`QUAD_TRANSPORT_CHECK.json`为PASS。后述C++第二实现又从S7筛群，对全部75075原始多重集分别求规范像，独立得到完整615／46／41代表列表，先与输入702个job键逐项相等。

任意实际H先标准化内部，再用该内部稳定子群共同运输全部quad到代表，同时运输三迹、J、点频率和候选。不同迹不能分别重标；同一置换保持全部必要条件及权，故实际输入必落某job，最终颜色用其逆置换返回。

## 3. 每job的完整必要域

固定quad代表后，I1两个三迹的多重集有C(36,2)=630份，I2三个三迹有C(37,3)=7770份；唯一J在全部21对中选择。仅筛原H必满足的条件：

1. 所有ui≥0；
2. 内部、高迹、J共同覆盖每个P点对；
3. 原i-star覆盖L全部17点，因此外部关联总数

$$4u_i+2a_i+b_i+3s_i\ge17,$$

等价于si+2ai+3bi≤15−4ci。没有假设star中外部集不重叠。

主生成器`GENERATE.cpp`用非降序三迹索引递归，穷尽每个job的三迹多重集，再遍历21个J。提前筛2ai+3bi≤15−4ci安全，因为si≥0；若高迹／内部尚未覆盖的P对多于一个，单个J无法补齐，可安全剪枝。其余条件逐源重算。

全部702job完整结束，1590494必要源均Δ>0，最小Δ1，最低proper m+t的最坏值11；不存在首失败或中止。逐job原始三迹数、J迭代数、必要源数与最小Δ保存于`GENERATION.json`。主计算约0.947 CPU秒。必要域允许不能共同实现外部布局的源，扩大域不影响实际覆盖。

`NECESSARY.tsv`逐源保存 job、三迹非降序索引的无损六位打包数、J mask、Δ、本源蓝集、实际m／t、W／M。三迹索引按数值递增的35个三点mask编号。job、打包数、J共同唯一确定全部源；这是精确编码，不是哈希。未使用其它源首成员的蓝点作非法运输。

## 4. 独立域、补集候选及全部35迹核验

`VERIFY.cpp`独立重建完整702job后，先选J，再用35种三迹的重数向量递归（总重数二或三），而非主程序的非降序索引在外、J在内。每个多重集对应唯一向量。部分点频率剪枝直接使用当前ui上界和4ui+2ai+bi+3si：未来增加一份三迹关联使该容量上界减少二，不能恢复已违反者，故剪枝不漏必要源。最后独立检查P点对覆盖。

候选改枚举四点红补集S，Q=P\S。J⊆Q等价于J∩S为空；t=1等价于J⊆S；Q漏高迹T等价于T⊆S。权写成

$$\lambda_Q=(\sum_{i\in S}u_i-15-\boldsymbol1_{J\subseteq S})_+.$$

用这套不同表示重算全部精确W、M、Δ以及最低proper m+t；每源均与原存证相等。源key映射无重复，每个独立生成源须找到并移除其存证，最后恰为空。因此是**1590494份完整必要源键集合相等**，不是只比总数／分型数。

对本源自身蓝Q再展开全部35个原P迹索引，逐项检查proper或其唯一未排除单色风险，恰有

$$8-t\text{条proper},\quad m\text{正四},\quad t\text{负三},\quad27-m\text{负四}.$$

全部小正及负一／二均为零，唯一J不全蓝；每个P点原度精确八，总外部关联精确119。全部**55667290条原索引分类**通过。

`INDEPENDENT_CHECK.json`为PASS：完整键集、全部精确量、自身蓝点和35迹分类通过，分case源数498738／264619／827137。独立执行约2.16 CPU秒，峰值92585984字节，远低于30CPU秒／1GB；只用整数和标准库，断言实际启用。完整75075quad运输另有独立PASS。这里是不同算法的本机确定性核验，不冒充跨家族数学审阅。

## 5. 准确修复门和原染色返回

实际H进入必要域后，取得Q使高迹proper、J不全蓝且m+t≤11。其余风险精确为

$$mP4,\qquad tT3\ (t\in\{0,1\}),\qquad(27-m)B4,\quad |L|=17,\quad D7.$$

因为P击中每条原边，每条未proper边只贡献一种符号的外部约束，每个L点signed总出现≤其原度七。

|m|实际前提|已证门|
|---:|---|---|
|0至7|t≤1，B≤27|[七正四／4T35B](../../../../../../proofs/propertyb35/SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md)|
|8|t≤1，B19，L17|[八正四／3T20B](../../../../../../proofs/propertyb35/EIGHT_POSITIVE_FOUR_SET_REPAIR.md)|
|9|t≤1，B18|[九正四／3T任意B](../../../../../../proofs/propertyb35/NINE_POSITIVE_JOINT_NEGATIVE_REPAIR.md)|
|10|t≤1，B17|[十正四／2T任意B](../../../../../../proofs/propertyb35/TEN_POSITIVE_TWO_TRIPLES_REPAIR.md)|
|11|m+t≤11迫t0，B16|[至多十一正四／0T17B／L18](../../../../../../proofs/propertyb35/ELEVEN_POSITIVE_FOUR_SET_REPAIR.md)|

八／九／十正条数是实际恰好，其余≤条数直接满足，无padding。修复实际L，得到红集R，L\R蓝，保持P上Q蓝、其余红。蓝单迹由正四含红外点，红单迹由负四含蓝外点；J若红红由唯一负三含蓝外点，若跨色已proper；内部和所有高迹保持P端双色。以上穷尽35原边，逆运同一P置换，得到原H的Property B染色。

## 复现

所有新文件只在本独立目录，canonical和导航由主代理维护。源码／数据为`QUAD_ORBITS.py/json`、`JOBS.tsv`、`VERIFY_QUAD_TRANSPORTS.py`、`QUAD_TRANSPORT_CHECK.json`、`GENERATE.cpp`、`GENERATION.json`、`NECESSARY.tsv`、`VERIFY.cpp`、`INDEPENDENT_CHECK.json`。在项目根目录使用Python标准库及C++17：

```sh
python3 context/propertyb35-paper/round01/twentyfour/p7_one_two_new_gate_transfer_20261020/one_pair_weighted/QUAD_ORBITS.py
python3 context/propertyb35-paper/round01/twentyfour/p7_one_two_new_gate_transfer_20261020/one_pair_weighted/VERIFY_QUAD_TRANSPORTS.py
c++ -O3 -std=c++17 context/propertyb35-paper/round01/twentyfour/p7_one_two_new_gate_transfer_20261020/one_pair_weighted/GENERATE.cpp -o /tmp/propertyb35-one-pair-weighted-full
/tmp/propertyb35-one-pair-weighted-full context/propertyb35-paper/round01/twentyfour/p7_one_two_new_gate_transfer_20261020/one_pair_weighted
c++ -O3 -std=c++17 context/propertyb35-paper/round01/twentyfour/p7_one_two_new_gate_transfer_20261020/one_pair_weighted/VERIFY.cpp -o /tmp/propertyb35-one-pair-weighted-independent
/tmp/propertyb35-one-pair-weighted-independent context/propertyb35-paper/round01/twentyfour/p7_one_two_new_gate_transfer_20261020/one_pair_weighted
```

完整链为实际H→共同内部／quad运输→完整必要高族与J→统一整数加权余量→proper Q和m+t≤11→真实signed修复门→原35边双色。局部分类不要求实现外部布局，不是用原H枚举替代全称证明。
