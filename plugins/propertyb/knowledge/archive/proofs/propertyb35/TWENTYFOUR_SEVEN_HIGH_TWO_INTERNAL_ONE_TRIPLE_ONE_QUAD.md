# 二十四点七高点、两内部边、唯一三迹与唯一四迹的二染色

## 命题与范围

设H为24点35条互异五元边的点对覆盖超图，最小度至少七、无全七度边。高点集P={v:d(v)>7}恰七点，恰两条原边完全位于P，非内部恰有一条三迹原边和一条四迹原边，其余迹至多二元。则H可二染色。

本稿完整覆盖

$$(n_2,n_3,n_4)=(8,1,1),\qquad n_1=23.$$

它不是全部P7 I2。第一次必要域生成29316487份源零残；另一J生成的完整键集合逐项相等，1026077045个原35迹角色及每源blue/tag/全部门假设PASS。生成CPU约1.53秒，第二验证约17.82秒，没有枚举外17点或原H。本稿给出完整有限局部覆盖与实际二染色连接；主代理验收和本新增caller的指定跨家族审阅另记，不把旧门审阅扩大到这个新域。

## 1. 从实际H到完整必要迹域

总度175、七度基线168及|P|=7迫P点均八度，L=V\P十七点均七度。无全七度边保证每条原边遇P，没有零P迹边需要双符号。

两内部五边写作P\f1、P\f2，两missing二对不同。P重标号为{0,…,6}，无损分为：

- case0：f1=01,f2=02，内部mask124、122；
- case1：f1=01,f2=23，内部mask124、115。

令c_i为内部出现次数；唯一四迹K、唯一三迹T按**不同大小的类型分别标记**，h_i=1[i∈K]、g_i=1[i∈T]。二迹为无自环多重图J，重数j_ij≥0、度s_i。预算

$$n_2+2n_3+3n_4=13,\qquad n_1=20+n_3+2n_4$$

给J八条、单迹23条。单迹数唯一恢复为

$$u_i=8-c_i-h_i-g_i-s_i.\tag{1}$$

完整必要域只要求：

1. Σj_ij=8，各u_i≥0；
2. 每个P点对被内部、K、T或同点对J覆盖；
3. 原i星须覆盖L17点，故

   $$4u_i+3s_i+2g_i+h_i\ge17
   \iff s_i+2g_i+3h_i\le15-4c_i.\tag{2}$$

以上均为同一H的实际必要条件，没有假定未知外部布局、J简单性或其可实现性。每个H必进入域；不声称每份域源都能扩成H。

### 3bit编码仍然无损，但不能由J总数八直接断言

相邻missing形状中c_i=0至多一个点，不交形状则没有这样的点。因此任一J端对{i,j}至少有一端v满足c_v≥1。由u_v≥0得

$$j_{ij}\le s_v\le8-c_v-h_v-g_v\le7.$$

所以每个重数仍能用三位编码，21个点对共63位，完整恢复J且无碰撞。两程序均显式断言每端对至少有一个c≥1端点，并在编码时断言重数<8；没有筛掉j=8来替代证明。

**点的J度s_i可以为八。** 第二实现逐整数恢复容量时包括s=8，没有把每个点的度都偷限为七。编码只要求每条J重数≤7。

## 2. 高迹真群与运输

保持两条无序内部边的完整P置换群，两形状各阶48。共有35种K、35种T，因此不同大小的有类型高迹对(K,T)共1225份；不能将K与T交换，也不把它们当同大小的无序对。

[HIGH_JOBS.py](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/HIGH_JOBS.py)从5040个P置换筛真群，对1225个有类型对求完整轨道。case0得74代表，case1得62代表，共136；各形状轨道大小和均为1225。固定高迹代表后不对J再次取商，保留全部带标签J。

给实际H选择一份保持内部族的π将(K,T)送至代表；J和单迹数同时运输，落入该job的完整必要域。保存该源自身的Q/tag，再用π⁻¹(Q)返回原H。不能为不同J共用某个有利Q。第二实现从保持内部族的全置换重新生成群，对1225份有类型对直接求最小像，逐代表与轨道大小核对。

## 3. 完整35迹与真实小负约束

对每源尝试P蓝集Q大小1至4，其余P红。两内部原边须P端双色；不选有全蓝K或全蓝T的Q，避免本菜单不处理的正单／正二。

其余逐原边索引恢复：

|P迹类型|P端全蓝|P端全红|P端双色|
|---|---|---|---|
|内部五迹|不选|不选|原边已proper|
|四迹K|不选|**负单集**|原边已proper|
|三迹T|不选|**负二集**|原边已proper|
|二迹J|正三集|负三集|原边已proper|
|单迹i|u_i个正四集|u_i个负四集|不发生|

源恰为2内部+1K+1T+8二迹+23单迹=35个原索引。正三、负单和负二全部保留；不能沿用纯四高迹代码中“没有负二”的假设。

令m4,m3为正四／正三数，n1,n2为负单／负二数，t,b为负三／负四数。n1,n2各为0或1。所有约束每条原边至多一个符号，故任一真实外点的总indexed出现次数≤原度七，地面原L17。原外部集发生相交不影响此D7支配。

### 两个带小负的短门

**门A。** 若恰一个小负索引（单或二），m3=0,m4≤4，则修复。任取该负集一点f固定蓝，所有含f负索引整份删除；剩余负集大小至少三。正四删f后至少三，至多四个正索引和D7保留，调用[四正最小三元参数门](FOUR_POSITIVE_AT_LEAST_THREE_REPAIR.md)的s3/D7。不能只让负单使用该门，也不能把负二截成负单。

**门B。** 若小负总数≤2且正3/4总数m≤2，则修复；不需D或ground上限。每个小负任选一个点禁蓝，所得F大小≤2，不要求两负集相交。每个正集原大小至少三，删F后仍非空，各取一点共至多两红。小负因遇F安全，其余负集大小至少三，不能包含于至多两红。因此全部约束满足。

### 本次全部非零使用菜单

|tag|完整前提|源数|准确进口|
|---:|---|---:|---|
|1|无正集|958044|R=空，所有负集非空|
|2|n1+n2=1,m3=0,m4≤4|21282007|上面门A|
|16|n1+n2≤2,m≤2|3105767|上面门B|
|3|无小负,m≤4|2773089|[四正参数门](FOUR_POSITIVE_AT_LEAST_THREE_REPAIR.md)，s3/D7，任意负≥3|
|4|无小负,m≤5,t≤3|716066|[五正最小三元3T门](FIVE_POSITIVE_THREE_TRIPLES_REPAIR.md)，任意B/D7|
|8|无小负,m=8,m3≤1,t≤2,b≤19|3|[混合八正一小／两负三门](EIGHT_MIXED_ONE_SMALL_TWO_TRIPLES_REPAIR.md)，L18/D7|
|9|无小负,纯P4,m4≤7,t≤4,b≤35|481505|[七正四4T门§C](SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md)|
|13|无小负,纯P4,m4=9,t≤3|6|[九正四联合负门](NINE_POSITIVE_JOINT_NEGATIVE_REPAIR.md)，L18/D7，任意B|

没有把正三代入P4-only门；带小负的记录只使用门A/B或无正直接成功。小负两个外点是否相同无需额外假设。

## 4. 完整生成和第二构造

先profile两个高迹job：93054必要源、0残，约0.020CPU秒，保存[PROFILE_FIRST_TWO.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/PROFILE_FIRST_TWO.json)。随后完整136job实测约1.53CPU秒：

|missing形状|高迹轨道|完整必要源|未覆|
|---|---:|---:|---:|
|01/02相邻|74|3870656|0|
|01/23不交|62|25445831|0|
|合计|136|29316487|0|

第一J生成先给未覆P点对各一条强制J，再将剩余重数依21点对递归分配，端点容量同时满足式(1)(2)。任一实际J都含该基础，且其剩余非负重数经过唯一递归路径，所以必要覆盖无损。门选择在域生成之后执行，未因找不到门而删源。

[NECESSARY.bin](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/NECESSARY.bin)每源16字节，little-endian `<QH6B`：63bit完整J、job、该源自己的blue/tag/m4/m3/t/b。负单／负二由job高迹和blue唯一恢复，不被省略。文件469063792字节，恰为29316487×16。逐job计数和门计数保存[GENERATION.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/GENERATION.json)，[NONGATED.tsv](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/NONGATED.tsv)为空。

第二[VERIFY.cpp](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/VERIFY.cpp)不调用第一J递归：按顶点顺序直接分配向后各边的原重数，每对在自身位置施加强制下界；容量另对s=0…8用u≥0及4u+3s+2g+h≥17恢复。逐job每个重建键必须恰删掉第一实现完整键集中的一个，末尾集合为空，故不是只比较总数。全部29316487键相等。

每个保存源又展开2+1+1+8+23的全部35个trace stub，K外大小一、T外大小二，重新恢复所有正负大小，核对m4/m3/n1/n2/t/b和该源自身tag的完整前提。新负二逐项进入门A/B判断，未沿用旧负二恒零断言。全部1026077045个原迹角色重建及门假设PASS，CPU约17.82秒。

两实现由同一执行者按不同构造编写，不宣称他人独立实现或跨家族执行复现。必要域完整定义、群像、原迹绑定和代码／数据供主代理验收。

## 5. 返回原H

对任意命题中的实际H，经§1必要式及§2运输落入保存源。取它自身的blue/tag，真实L17系统满足§3某个已证门或完整短证明，得到外红集R。门A/B固定的实际外点保持蓝，未被修复步骤重新取红。

P端双色的边已有两色；全蓝P迹的外部正集被R击中，故有红点；全红P迹的外部负集未全含于R，故仍有蓝点。全部35原边proper，运输回原标签保留结论。这证明完整库存，而不是以有限放松源的可实现性为额外假设。

其他I1/I2库存及完整36未在本稿证明；旧two/three_quads证据没有修改或重跑。

## 6. 证据和复现

[HIGH_JOBS.py](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/HIGH_JOBS.py)、[JOBS.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/JOBS.json)、[JOBS.tsv](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/JOBS.tsv)保存真群、1225有类型高迹对及136代表；[GENERATE.cpp](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/GENERATE.cpp)、[GENERATION.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/GENERATION.json)保存完整必要域与源见证；[VERIFY.cpp](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/VERIFY.cpp)、[INDEPENDENT_CHECK.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/INDEPENDENT_CHECK.json)保存第二J构造、完整逐键与35迹重建结果。

```sh
python3 context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/HIGH_JOBS.py
/usr/bin/clang++ -std=c++17 -O3 context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/GENERATE.cpp -o /tmp/propertyb35-p7-triple-quad-generate
/tmp/propertyb35-p7-triple-quad-generate context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad 136
/usr/bin/clang++ -std=c++17 -O3 context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/VERIFY.cpp -o /tmp/propertyb35-p7-triple-quad-verify
/tmp/propertyb35-p7-triple-quad-verify context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad
```

不加`-DNDEBUG`。无外17点布局、SciPy、新概率位置DP、MCP或Lean。

## 7. 完整本机证据索引

- [HIGH_JOBS.py](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/HIGH_JOBS.py)：1225个有类型quad/triple高迹对与真群完整生成。
- [JOBS.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/JOBS.json)：136高迹代表及其实际轨道大小。
- [JOBS.tsv](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/JOBS.tsv)：两种J实现共同输入的代表。
- [PROFILE_FIRST_TWO.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/PROFILE_FIRST_TWO.json)：先做的两个job规模/零残记录。
- [GENERATE.cpp](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/GENERATE.cpp)：强制基础与剩余重数的完整J生成和选门。
- [GENERATION.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/GENERATION.json)：全部136job的完整计数与逐门数量。
- [NECESSARY.bin](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/NECESSARY.bin)：29316487份完整J键和每源自身Q/tag/大小计数。
- [NONGATED.tsv](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/NONGATED.tsv)：完整运行的空残文件。
- [VERIFY.cpp](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/VERIFY.cpp)：另一种顶点星J构造、全键比较与35原迹角色重建。
- [INDEPENDENT_CHECK.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/INDEPENDENT_CHECK.json)：29316487键及1026077045原迹角色全部PASS。

原研究报告为 [REPORT.md](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/one_triple_one_quad/REPORT.md)。上文完整给出必要源域、覆盖、运输、两项新短门及旧门的准确条件、原35边返回，不以报告链接代替证明。
