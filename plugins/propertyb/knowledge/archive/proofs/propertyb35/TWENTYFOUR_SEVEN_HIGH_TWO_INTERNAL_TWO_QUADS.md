# 二十四点七高点、两内部边、恰两四迹的二染色

## 定理与证明依据

设H为24点、35条互异五元边的点对覆盖超图，最小度至少七、无全七度边。令P={v:d(v)>7}，假设|P|=7，恰两条边完全位于P，且非内部高迹恰为两条四迹、没有三迹。则H可二染色。

这是库存

$$(n_2,n_3,n_4)=(7,0,2),\qquad n_1=24$$

的完整二染色定理。相邻missing与不交missing均包括，四迹允许同P迹重复，不预设其外部单点相同。所有有限必要源均有其自身的蓝集和门见证。有限分类只涉及七个P点的真实迹，不涉及外部17点布局或整H分类。

完整必要域按高迹真群归约后共7944059份高迹/J源，第一生成未覆0；不同J构造的第二实现逐键集合相等，全部278042065个原35迹角色重建及实际门假设PASS。主代理已全文核数学覆盖、实际D7、运输与两种程序，并独立编译运行第二实现得到上述PASS。本新增库存的跨家族专审另行记录，不用旧修复门审阅替代实际caller审阅。

## 1. 从原H到两种实际missing形状

总度175、七度基线168及|P|=7迫使P七点均八度，L=V\P十七点均七度。无全七度边保证每条原边遇P，因此没有被漏去的零P迹边。

两内部五边写作P\f1与P\f2，其中f1、f2是不同二对。重标号可无损取两种形状，固定P={0,…,6}：

- case0相邻：missing为01、02，内部mask为124、122；
- case1不交：missing为01、23，内部mask为124、115。

令c_i为内部出现次数。两个四迹按无序允许重复的多重集{K1,K2}记录，令h_i为其出现次数。二迹原边组成无环多重图J，重数j_ij≥0，s_i=Σ_j j_ij。由边数与P关联数

$$n_2+2n_3+3n_4=13,\quad n_1=20+n_3+2n_4$$

得到n2=7,n1=24。各点单迹原边次数唯一为

$$u_i=8-c_i-h_i-s_i.\tag{1}$$

## 2. 完整必要P源域

对每个高迹对，保留全部J非负整数重数，满足且仅使用下列必要条件：

1. $\sum_{i<j}j_{ij}=7$；
2. 式(1)各u_i≥0；
3. 每个P点对至少被某内部边、某四迹或一条同点对J边覆盖；
4. 对每个P点i，原i星须覆盖全部17个L点，其外部关联数给

   $$4u_i+3s_i+h_i\ge17
   \iff s_i+3h_i\le15-4c_i.\tag{2}$$

所有条件从同一H得出。没有额外要求某度谱、某四迹内部相交型、J简单性或外部布局，故每个实际H均落入这个必要域。反之，不声称每个源能由实际H实现。

### 高迹真群与运输

对每种missing形状，取保持无序内部边族的完整置换群；其阶均为48，分别同构于S4×C2与S3×(S2≀S2)。35种四迹的无序可重复二元组共有630份。[QUAD_JOBS.py](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_quads/QUAD_JOBS.py)从定义列出全部5040点置换，保留真群后保存每个高迹轨道及其完整像。两形状分别46与41轨道，共87；各轨道大小之和各为630。

四迹对取商后，**不对J再取商**：对每个固定高迹代表保留全部带标签J。给实际H选把其高迹对送至代表的真群置换π，其J与u随π运输，必落入对应完整域。保存的蓝集Q拉回为π⁻¹(Q)，同一原边索引的颜色和外部signed约束随之运输。不能把一份源的Q移用于另一份J。

两份程序独立使用“保持missing族”与“保持内部族”重建同一个群及630个高迹对的轨道像，两种定义等价；实际逐轨道键和大小都已比较。

## 3. 每个源的全部35迹与signed调用

第一生成按P源自身的Q尝试1至4蓝点，不复制正集补数。每条内部边必须在P端proper。若某四迹完全蓝，外部正集只有一元，以下有限门目录不接，故不选这样的Q。对其他边按原边索引逐份恢复：

|原P迹|P端全蓝|P端全红|P端双色|
|---|---|---|---|
|内部五迹|不允许|不允许|原边已proper|
|四迹|不选|负单集|原边已proper|
|二迹|正三集|负三集|原边已proper|
|单迹i|正四集，共u_i份|负四集，共u_i份|不发生|

因此每个源恰由2内部+2四迹+7二迹+24单迹=35份原迹组成。所有符号计数均从这35份重新分类，而非只套单点和公式。设m4,m3为正四/正三数，n为负单数，t为负三数，b为负四数。此库存没有负二集；负单n可能为0、1、2，均保留。

所有约束只来自P端单色的原边，每条原边至多一个符号，所以任意真实外点在正负全部原索引中的总出现次数≤其原度七。地面是原L17。这不是要求未知外部布局预先给D证书。

### 实际非零使用的门

|tag|实际接口|完整源数|数学进口|
|---:|---|---:|---|
|1|无正集，取外红R=空|25833|全部负集非空，直接安全|
|2|恰一个负单、无正三、正四≤4|5780699|固定该负单点f蓝，正缩至≥3，含f负索引整份删除，再用下行四正参数门|
|3|无小负、正3/4总数≤4|1309953|[四正参数门](FOUR_POSITIVE_AT_LEAST_THREE_REPAIR.md)，s3/D7，负条数任意|
|4|无小负、正3/4总数≤5、负三≤3|285426|[五正最小三元3T门](FIVE_POSITIVE_THREE_TRIPLES_REPAIR.md)，D7，负四任意|
|5|无小负、正3/4总数≤6、至多3正三、负三≤1|56|[九正门附录B第2节的独立六混合引理](NINE_POSITIVE_JOINT_NEGATIVE_REPAIR.md)，D7、任意ground/负四|
|9|纯正四≤7、负三≤4、负四≤35|535878|[七正四4T门§C加强](SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md)|
|12|恰八正四、负三≤4、负四≤17|6214|[八正四集／四负三集门](EIGHT_POSITIVE_FOUR_TRIPLES_REPAIR.md)，L17/D7|

tag12在本库存满足b=24−m4=16，故全部6214份实际记录均满足四负三／17负四门。程序虽保留两个已证八门的并集条件，本库存不依赖原八门§7仅三负三／20负四的条款来覆盖t=4。

tag2没有漏掉负单：其真实四迹原边外部部分恰为一个实际点f。固定f蓝就满足该负约束；所有其他含f负约束整份删除，其余仍为负三或负四，不作截取。原正四删f后至少三，至多四个正索引和D7均保留，四正参数门没有ground上限。不同正集可共享f，无需为它们分别计不同禁点。

其他已证菜单也写在代码中，但本次记录的非零使用恰为表中七类，证明不依赖从未使用的门。特别没有新增通用12正门，也没有为使用新三正负二门而假删负三；sharp43在本D7域被四正参数门包含，没有产生额外实际调用。

## 4. 第一完整生成与每源存证

[GENERATE.cpp](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_quads/GENERATE.cpp)先把尚未由内部或高迹覆盖的P点对强制为J下界一，剩余七条J关联按21点对递归。每步同时保留端点残容量

$$s_i\le\min(8-c_i-h_i,\,15-4c_i-3h_i).$$

这只做必要条件剪枝；所有实际J都包含强制基础，且其非负剩余重数依次经过递归，不会被丢掉。每个二迹重数≤7，所以21重数可各用三位，恰编码为63位整数。它是完整重数向量的无碰撞编码，不是哈希。

先profile两个高迹轨道（59412必要源，0残，约0.014CPU秒），随后完成全部87轨道：

|missing形状|高迹对轨道|必要源|未覆|
|---|---:|---:|---:|
|相邻01/02|46|1576338|0|
|不交01/23|41|6367721|0|
|总计|87|7944059|0|

[GENERATION.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_quads/GENERATION.json)逐高迹轨道保存完整数量、轨道大小、强制点对数及未覆数；[NECESSARY.bin](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_quads/NECESSARY.bin)每源16字节保存J完整编码、job、该源自身Q/tag、m4/m3/t/b。总文件127104944字节，与7944059×16精确相等。没有以计数相同代替输入集相同，也没有只保留少数抽样Q。

## 5. 第二实现的完整域与原迹重放

[VERIFY.cpp](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_quads/VERIFY.cpp)不调用第一递归生成器：

1. 从保持内部边族的全部置换独立重建高迹真群、直接对630份四迹对求最小像和轨道计数，逐键核对87份job。
2. 对固定job，先读其所有第一实现的完整J键，确认没有重复；然后按顶点0…6依次分配向后邻点的**原J重数**，在每个点对使用必要下界，而不是先加全局基础再分配剩余。容量另从u≥0与外部关联式$4u+3s+h\ge17$逐整数s恢复。
3. 每个第二生成的J键必须恰删除第一键集合中一个元素；每job结束集合须为空，生成数与源数须相等。因此验证的是全部输入集相等，不只是总数。
4. 对每条保存源，从2+2+7+24全部35迹stub独立重建正负大小，核对该源自己的Q、门tag及完整计数，负单/正三均保留；逐tag检查全部数学前提。没有只信第一实现的m/t/b公式。

本机启用assert的结果：全部7944059键相等、278042065个原35迹角色重建、每源Q和门假设全部PASS；第二实现CPU约4.27秒。两种实现由同一执行者编写，构造方法不同；主代理已独立读源码并实际编译运行第二实现PASS。这不是不同人员的独立实现，也不是跨模型执行复现。

## 6. 从已证门返回原H

对任意假设中的H，按§1取实际missing形状，再按§2运输其真实高迹/J/u至一份必要源。该源存有自己的Q和§3某一已证门。给P中Q染蓝，其余P染红，真实外部signed系统满足该门的完整假设，故取得外红集R；tag2先固定其真实唯一负单点蓝，再取得R。

恢复运输后，P端已双色的原边仍proper；P端全蓝边的正外集被R击中，故有红点；P端全红边的负外集未包含于R，故有蓝点。全部35原边因此proper。该连接只使用完整必要域的覆盖，并不假设每份域源可由H实现。

这个原H到有限源、实际修复门及原35边的连接证明了定理；没有额外假设局部证书存在。定理仅覆盖上述库存，不把其他I1/I2库存或完整m(5)下界计为已证。

## 7. 复现

在项目根目录运行：

```sh
python3 context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_quads/QUAD_JOBS.py
/usr/bin/clang++ -std=c++17 -O3 context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_quads/GENERATE.cpp -o /tmp/propertyb35-p7-two-quads-generate
/tmp/propertyb35-p7-two-quads-generate context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_quads 87
/usr/bin/clang++ -std=c++17 -O3 context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_quads/VERIFY.cpp -o /tmp/propertyb35-p7-two-quads-verify
/tmp/propertyb35-p7-two-quads-verify context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_quads
```

不要加`-DNDEBUG`。第一完整生成CPU约0.44秒，第二初次约4.27秒；原JSON保存各次实际耗时。没有SciPy、Lean、MCP或外部17点布局。

## 8. 本机证据索引

- [QUAD_JOBS.py](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_quads/QUAD_JOBS.py)：真实稳定群与高迹轨道生成。
- [JOBS.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_quads/JOBS.json)：87个高迹代表及轨道大小。
- [JOBS.tsv](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_quads/JOBS.tsv)：两实现共同读取的高迹代表输入。
- [PROFILE_FIRST_TWO.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_quads/PROFILE_FIRST_TWO.json)：前两个轨道的有界规模测量。
- [GENERATE.cpp](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_quads/GENERATE.cpp)：强制基础加剩余J重数的完整生成与selector。
- [GENERATION.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_quads/GENERATION.json)：87轨道计数、完整状态、零残及门计数。
- [NECESSARY.bin](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_quads/NECESSARY.bin)：7944059份完整J键及其自身blue/tag/计数存证。
- [NONGATED.tsv](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_quads/NONGATED.tsv)：完整运行空残文件。
- [VERIFY.cpp](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_quads/VERIFY.cpp)：另一种顶点星J生成、完整键集合比较及35迹重建。
- [INDEPENDENT_CHECK.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_quads/INDEPENDENT_CHECK.json)：完整逐键与278042065角色检查PASS。

研究说明保存在 [原始覆盖报告](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_quads/REPORT.md)。上文已完整内联有限域定义、覆盖证明、运输、每种实际门和返回原染色，不以该报告链接代替证明。
