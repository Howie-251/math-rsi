# 七高点、唯一内部边、四三迹和三四迹的统一加权三蓝修复

## 定理

设H为24点、35条互异五元边的点对覆盖超图，最小度七，无全七度边。设高点集P恰七点，内部原五边恰一条，非内部P迹库存为

$$ (n_2,n_3,n_4)=(0,4,3). $$

则H具有Property B。

下面给出完整实际输入连接及有限精确证据。必要域不是原H／外部布局枚举；统一加权公式与两内部 $(0,5,1)$ 相同。本机完整双生成／精确计数已经完成，新候选仍由主代理验收并另记跨家族审阅，不据本稿称全部P7或全局下界完成。

## 1. 真实迹预算

总度175只有七份超出24点七度基线的盈余，故P全部八度，外部L恰17点全部七度。无全七度边使每条原边遇P。

令唯一内部五边C={0,1,2,3,4}，其补集为{5,6}；任意实际内部边经一次P置换可归到此形。令ci=1_{i∈C}，ai为四条三迹的原索引频率，bi为三条四迹的原索引频率。实际单迹数唯一为

$$ u_i=8-c_i-a_i-b_i\ge0,\qquad
\sum_i u_i=56-5-12-12=27.$$

完整35条原迹为一内部、四三迹、三四迹、27单迹。不同原边可有相同三／四迹，ai、bi保留全部原索引；不假设高迹互异。

## 2. 同一统一权及实际修复接口

三点蓝集Q自动使内部五边proper。记A为不同的高三迹集合，D为所有不同高迹（包括四迹）。取

$$\mathcal C={P\choose3}\setminus A,\qquad
\lambda_Q=(12-\sum_{i\in Q}u_i)_+,$$
$$W=\sum_{Q\in\mathcal C}\lambda_Q,\qquad
M=\sum_{T\in D}\ \sum_{\substack{Q\in\mathcal C\\Q\cap T=\varnothing}}\lambda_Q,
\qquad\Delta=W-M.$$

所有权非负。如果Δ>0，漏掉某高迹的候选总权至多M，故有一份正权候选命中全部高迹。候选已排除完整高三迹，故不全蓝包含三迹；三点Q不可能全蓝包含四迹。因此该Q使所有高迹proper，且整数正权迫

$$m=\sum_{i\in Q}u_i\le11.$$

这只是把相同P迹的**颜色阻断事件**去重；ai、bi、ui始终保留原索引。统一权未按已找到的单个Q硬编码，不依赖外部布局。以下完整必要域核得Δ≥3。

## 3. 三个四迹的101个完整轨道

唯一内部C的稳定子群恰是S5×S2，阶120·2=240：C中点任意置换，补集两点任意置换。所有35个P四集的三重无序多重集共有

$$\binom{35+3-1}{3}=7770$$

个带标签源。对每源使用同一个稳定子群运输三个四迹（保留重复），得到恰101个轨道。其完整性不只由数值101判断：

* `QUAD_ORBITS.py`按群结构因子生成全部240元素，逐7770多重集生成全部像，对尚未标记的源保留最小像；每轨道像集合与旧轨道不交并恰覆盖全部7770键。
* `QUAD_ORBITS.json`保存全部240群元素、101个代表、各轨道大小以及**每个7770四迹多重集键的实际运输置换索引**；`JOBS.tsv`保存完整101代表。
* `VERIFY_QUAD_TRANSPORTS.py`改为遍历S7全5040置换并筛保持C者，独立得到同一完整群；逐键检查7770全域、每个轨道的全部像和每个实际transport。结果`QUAD_TRANSPORT_CHECK.json`为PASS。
* 后述C++独立实现还对全部7770源的240像分别求最小值，独立重建完整101个job键，并先与输入job列表逐项相等，防止生成和回放同时漏整个位置。

任意实际H归一化C后，再由此群将其三四迹共同移至某代表，同时运输全部三迹、点频率、单迹数和候选。不同高迹不分别重标。由于群保持C，以下必要条件及统一权不变；最终颜色再通过同一置换逆运回原标号。

## 4. 每个代表的完整必要域

固定一个三四迹代表。四个P3从35个三集选允许重复的多重集，共

$$\binom{35+4-1}{4}=\binom{38}{4}=73815$$

份。101个job的原始组合总数为7455315。只筛实际H必满足的三项：

1. 全部ui=8−ci−ai−bi非负。
2. 每个P点对至少被内部C、某高三迹或某高四迹包含。无二迹、单迹不覆盖两个不同P点。
3. 原i-star覆盖全部17外点，故其外部关联总数

$$4u_i+2a_i+b_i\ge17,$$

等价于2ai+3bi≤15−4ci。此关联上界仅支配并集，不假设各外部集互不相交。

`GENERATE.cpp`逐四个三迹非降序索引枚举，每个多重集唯一一条赋值路径。逐源从实际索引重算a、u及三组筛选，完整接受**390116份必要高族**；全部101job均完整跑完73815份，没有停止或失败。每份逐35候选精确计算W、M、Δ，得到

$$\Delta\ge3,\qquad
\max_{\text{必要源}}\min_{Q\text{ proper}}\sum_Q u_i=11.$$

各job原始数、必要源数、最小Δ和最大最低私和完整保存于`GENERATION.json`。主生成约0.303 CPU秒。域只保留必要条件，不要求每份源都可共同实现L关联；不能实现者的保留是安全放宽。

## 5. 完整独立核验与原迹绑定

`NECESSARY.tsv`每份源保存 job、四个三迹索引的无损六位打包数、精确Δ、本源自己的蓝三元组、实际m、精确W和M。三迹索引为数值递增的35个三点mask。打包只是24位的一一编码，不是哈希。

`VERIFY.cpp`不用主生成器的四层非降序循环，而按35种三迹的重数向量递归，总重数四。各向量唯一对应一份多重集。部分频率剪枝时，直接检验当前单迹上界以及4ui+2ai+bi：每增加一份三迹关联，这个外部容量上界减少二，已经低于17的分支以后不可能恢复，故安全。最终独立检验全部P点对覆盖。

候选改用全部四点红补集S，Q=P\S。权写成

$$\lambda_Q=(\sum_{i\in S}u_i-15)_+,$$

排除Q包含高三迹者，漏高迹T改按T⊆S计数。用此不同候选表示重算全部精确W、M、Δ和最低proper私和，与原存证逐项相等。

程序以无重复键映射读入原存证，独立每生成一个必要源必须找到该键并移除，最后映射恰为空。故是**390116份完整必要源键集合相等**，不是仅比总数或每job计数。输入的101个quad job还在此前从全S7独立重建并完整核对。

对每键还按本源自己的Q展开全部35条P迹逐项分类，共**13654060条原索引**：精确为8条已proper、m个正外部四集、27−m个负外部四集；所有小正、小负和负三计数均为零。每点P总度精确为八，所保存Q确为三点且私和恰m≤11。

`INDEPENDENT_CHECK.json`为PASS：完整键集、全部W/M/Δ、自身见证及原迹分类通过，最小Δ3、最坏最低私和11。独立执行约0.36 CPU秒，峰值23904256字节，低于30CPU秒／1GB。全部检查为整数，未用求解器或浮点；编译未使用`-DNDEBUG`，断言实际启用。

## 6. 真实signed门与返回原染色

实际H经前述共同运输进入完整必要域，取得proper三蓝Q且m≤11。固定Q蓝、其余P红。高迹和内部已proper，只有27单迹留下风险：蓝单迹给正四，红单迹给负四。真实signed系统精确为

$$mP4,\quad0T,\quad(27-m)B4,\quad |L|=17,\quad D7.$$

每个未proper原边只贡献一份signed约束，所以每个L点的正负总出现不超过其原度七。没有零P边需要双符号计数，也没有正二／三或负二遗漏。

各m对应的已证门为：

|m|实际B|已证修复门|
|---:|---:|---|
|0至7|27−m≤27|[七正四／4T35B](../../../../../../proofs/propertyb35/SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md)|
|8|19|[L17八正四／3T20B](../../../../../../proofs/propertyb35/EIGHT_POSITIVE_FOUR_SET_REPAIR.md)|
|9|18|[九正四／3T任意B](../../../../../../proofs/propertyb35/NINE_POSITIVE_JOINT_NEGATIVE_REPAIR.md)，原total20也足够|
|10|17|[十正四／2T任意B](../../../../../../proofs/propertyb35/TEN_POSITIVE_TWO_TRIPLES_REPAIR.md)，原B18也足够|
|11|16|[至多十一正四／L18／0T17B](../../../../../../proofs/propertyb35/ELEVEN_POSITIVE_FOUR_SET_REPAIR.md)|

八／九／十正数是实际恰好条数，其他门的≤正数也直接满足，没有padding。用相应门得到实际L红集R，L\R蓝；蓝单迹因其正四被R击中含红外点，红单迹因其负四不全在R中含蓝外点。内部和高迹保持P端双色，穷尽原35边。最后逆运P置换，得到原H的Property B染色。

## 文件及重放

所有新证据仅在本独立目录；不修改旧证明、canonical或导航。完整入口为本稿，计算文件为`QUAD_ORBITS.py/json`、`JOBS.tsv`、`VERIFY_QUAD_TRANSPORTS.py`、`QUAD_TRANSPORT_CHECK.json`、`GENERATE.cpp`、`GENERATION.json`、`NECESSARY.tsv`、`VERIFY.cpp`、`INDEPENDENT_CHECK.json`。

在项目根目录运行，Python只用标准库，C++只用C++17标准库：

```sh
python3 context/propertyb35-paper/round01/twentyfour/p7_one_two_new_gate_transfer_20261020/three_blue_weighted_i1/QUAD_ORBITS.py
python3 context/propertyb35-paper/round01/twentyfour/p7_one_two_new_gate_transfer_20261020/three_blue_weighted_i1/VERIFY_QUAD_TRANSPORTS.py
c++ -O3 -std=c++17 context/propertyb35-paper/round01/twentyfour/p7_one_two_new_gate_transfer_20261020/three_blue_weighted_i1/GENERATE.cpp -o /tmp/propertyb35-i1-three-blue-full
/tmp/propertyb35-i1-three-blue-full context/propertyb35-paper/round01/twentyfour/p7_one_two_new_gate_transfer_20261020/three_blue_weighted_i1
c++ -O3 -std=c++17 context/propertyb35-paper/round01/twentyfour/p7_one_two_new_gate_transfer_20261020/three_blue_weighted_i1/VERIFY.cpp -o /tmp/propertyb35-i1-three-blue-independent
/tmp/propertyb35-i1-three-blue-independent context/propertyb35-paper/round01/twentyfour/p7_one_two_new_gate_transfer_20261020/three_blue_weighted_i1
```

完整链为实际H→唯一内部及三quad共同运输→完整必要高族→统一加权余量→proper低私和三蓝→真实signed修复门→原35边双色。独立计算是不同算法的本机确定性验证；指定跨家族审阅由主代理另行登记，不与之混同。
