# 二十四点七高点、两内部边、恰三四迹的二染色

## 定理与证明依据

设H为24点35条互异五元边的点对覆盖超图，最小度至少七、无全七度边；高点集P={v:d(v)>7}恰七点，恰两条边完全位于P，非内部高迹恰三条四迹，没有三迹。则H可二染色。

这是完整库存

$$(n_2,n_3,n_4)=(4,0,3),\qquad n_1=26$$

的完整二染色定理。高迹允许P迹重复、二迹保留重数，missing两种形状均覆盖。有限域只枚举P端真实必要迹，不生成外17点或整H。主代理已全文审阅覆盖证明及两种程序相对已审前一库存的参数、域、门和35迹绑定差分，并独立编译运行第二实现PASS。本新增实际caller的Gemini专项尚未审阅，不以旧门审阅代替新caller审阅。

第一生成覆盖573834份必要高迹/J源，未覆零。不同高迹轨道构造和J生成的第二实现逐键集合相等；20084190个原35迹角色以及每源自身blue/tag/完整门前提均已本机PASS。第一完整生成CPU约0.059秒，第二完整域与角色重建约0.30秒。

## 1. 原H的完整必要P域

总度175与七度基线168迫使P七点全八度，L十七点全七度。无全七度边保证每条原边遇P，故没有被省略的零P迹边。

两内部边记为P\f1、P\f2。两missing二对不同，重标号后仅两形：

- case0：f1=01,f2=02，内部mask124、122；
- case1：f1=01,f2=23，内部mask124、115。

P固定{0,…,6}。令c_i为内部出现次数，三条四迹记无序可重复多重集{K1,K2,K3}，h_i为四迹出现次数。J是二迹多重图，无自环，重数j_ij、度s_i。由内部数和三／四迹预算

$$n_2+2n_3+3n_4=13,\qquad n_1=20+n_3+2n_4$$

得到J恰四条、单迹恰26条。实际单迹数唯一恢复为

$$u_i=8-c_i-h_i-s_i.\tag{1}$$

完整必要源域保留全部j_ij≥0，满足：

1. Σj_ij=4，u_i≥0；
2. 每个P点对被内部、某四迹或同点对J至少覆盖一次；
3. 原i星覆盖L17点，故外部关联数满足

   $$4u_i+3s_i+h_i\ge17
   \iff s_i+3h_i\le15-4c_i.\tag{2}$$

这些只剔除不可能的必要P源，不附加外部布局、可实现性或J简单性假设。每个实际H必按式(1)(2)落入域；没有声称域中每份源都有实际H。

## 2. 真群高迹归约与实际运输

分别取保持无序内部边族的完整P点置换群。两形状群阶均48：case0为S4×C2，case1为S3×(S2≀S2)。35种四集的无序可重复三元组共C(37,3)=7770。

[QUAD_JOBS.py](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/QUAD_JOBS.py)从全部5040个P置换中筛真群，枚举全部7770个多重集，再按完整群像取轨道最小代表。case0得332轨道，case1得298轨道，共630；两形状各自轨道大小和均为7770。保存[JOBS.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/JOBS.json)和[JOBS.tsv](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/JOBS.tsv)。

固定高迹代表后，不对J再取商，保留全部带标签J。对实际H，取一份保持内部边族的置换π将其三高迹送到代表，J与单迹次数同时运输。该源保存自己的蓝集Q与门；返回原H使用π⁻¹(Q)。重命名同时运输所有原边索引，不在不同J之间共用blue。

第二实现从保持内部族而非missing族重新生成群，直接对7770个三四迹多重集求最小像，逐键比较630代表与轨道大小；不是只比较轨道数量。

## 3. 每源的35条原迹与完整signed系统

每份源恰为：2内部、3四迹、4二迹、26单迹，共35条带索引原迹。selector尝试1至4个P蓝点Q，其余P红：

- 两内部边均须P端双色；
- 不选有全蓝四迹的Q，以免出现本菜单不处理的正单集；
- P端全红四迹产生真实负单集，逐原边保留，不能丢弃；
- 全蓝二迹产生正三集，全红二迹产生负三集；
- 蓝点i的u_i份单迹产生正四集，红点i的u_i份单迹产生负四集；
- P端双色原边已proper，不需外部约束。

没有零P迹边，故每条原边至多贡献一个符号。任意实际L点的正负总indexed出现次数≤其原度七。地面为原L17。这一D7来自原H，不是未知外部布局的附加证书。

设正四/正三数为m4,m3，负单/负三/负四数为n,t,b；没有负二。可能n=0,1,2,3，所有情况保留；本次接受源都由下列合法门之一处理。m=m4+m3。

|tag|实际完整前提|源数|准确进口|
|---:|---|---:|---|
|2|n=1,m3=0,m4≤4|437843|禁该真实负单点蓝，正四缩≥3，再调用四正参数门|
|3|n=0,m≤4|1463|[四正≥3／负≥3参数门](FOUR_POSITIVE_AT_LEAST_THREE_REPAIR.md)，s3/D7，任意负数量|
|4|n=0,m≤5,t≤3|17798|[五正最小三元3T](FIVE_POSITIVE_THREE_TRIPLES_REPAIR.md)，任意B/D7|
|5|n=0,m≤6,m3≤3,t≤1|24615|[九门附录B的六混合辅助门](NINE_POSITIVE_JOINT_NEGATIVE_REPAIR.md)，任意B/D7|
|6|n=0,m≤7,m3≤2,t≤1|1205|[七混合两正三／一负三门](SEVEN_MIXED_TWO_SMALL_ONE_TRIPLE_REPAIR.md)，任意B/D7|
|7|n=0,m≤7,m3≤4,t=0|2|同文件T0扩展，任意B/D7|
|8|n=0,m=8,m3≤1,t≤2,b≤19|1456|[混合八正／至多一正三／两负三门](EIGHT_MIXED_ONE_SMALL_TWO_TRIPLES_REPAIR.md)，L18/D7|
|9|n=0,m3=0,m4≤7,t≤4,b≤35|66022|[七正四4T门§C](SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md)|
|12|n=0,m3=0,m4=8,t≤3,b≤20|22561|[原八正四门§7的3T20B推论](EIGHT_POSITIVE_FOUR_SET_REPAIR.md)，L17/D7|
|13|n=0,m3=0,m4=9,t≤3|869|[九正四联合预算门](NINE_POSITIVE_JOINT_NEGATIVE_REPAIR.md)，L18/D7，任意B|

这里tag12与先前(7,0,2)库存的进口不同：本库存m4=8时b=26−8=18，故程序的八门并集条件只能由t≤3/b≤20一项成立，准确依赖原八门3T20B，不能引用只容17B的4T门。全部tag12记录均由式b=18及完整判据保证该条件。

tag2中固定的点f是那条全红四迹原边的唯一实际外点。把f留蓝会满足该负单约束，其他含f负约束整份删除；未遇f负约束仍是负三/四，不做截取。正四删f后仍至少三，至多四正和D7保留，四正参数门修复自由点。没有把不同正集中的同一f算成多个不同禁点。

正三的出现全部保留；m3不为零的记录不调用P4-only门。表中列出所有非零使用门，其余代码菜单均未被本次证明使用。没有调用未证新门。

## 4. 第一完整生成与有界profile

先profile前五个高迹轨道：1560个必要源，0残，约0.0004CPU秒，结果保存[PROFILE_FIRST_FIVE.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/PROFILE_FIRST_FIVE.json)。该规模允许完成全部630轨道，实测约0.059CPU秒。

第一J生成把所有未被内部／高迹覆盖的P点对各强制一条J，随后对21点对分配剩余重数。端点残容量取

$$s_i\le\min(8-c_i-h_i,15-4c_i-3h_i).$$

任何实际J包含强制基础，其非负剩余向量必经唯一递归路径；没有因选点或门结果筛掉必要源。

|missing形状|高迹轨道|完整必要源|未覆|
|---|---:|---:|---:|
|01/02相邻|332|138008|0|
|01/23不交|298|435826|0|
|合计|630|573834|0|

每个J点对重数≤4，21重数各用三位的63位编码完全恢复J，不是哈希。[NECESSARY.bin](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/NECESSARY.bin)每源16字节保存J、job、该源自己的Q/tag和m4/m3/t/b，共9181344字节，等于573834×16。[GENERATION.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/GENERATION.json)逐轨道记录计数与零残，[NONGATED.tsv](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/NONGATED.tsv)为空。

## 5. 第二完整构造与35迹绑定

[VERIFY.cpp](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/VERIFY.cpp)不调用第一J递归：逐顶点分配向后各点对的**原J重数**，每条边在自己的位置施加未覆Ppair下界；端点容量另从u≥0及4u+3s+h≥17逐整数s恢复，不先加完整强制基础再递归。

它按job读取第一实现全部完整键、拒绝重复；每个第二生成键须恰删掉其中一个，末尾集合必须为空。故比较的是全部输入集，而非仅数量。不同J构造的完整573834键集合逐项相同。

对每份源，又显式展开2+3+4+26的全部35条trace stub，按其自身Q重新分类正负集大小，核对m4/m3/n/t/b及实际tag的完整门假设。原负单、原正三皆计入；35条角色总计20084190。所有断言均启用，本机第二实现PASS，初次CPU约0.30秒；主代理独立编译运行约0.398秒。

两套程序由同一执行者按不同构造实现；主代理已独立读源码差分并亲自编译运行第二实现，得到完整键与原迹绑定PASS。这不称为不同人员独立实现或跨家族执行复现。

## 6. 返回原H的染色

任意本库存H经§1必要式及§2真群运输，落入保存域的一份实际P源。取得该源自己的Q/tag，按§3建立真实外部signed系统并调用其已证门，得到外红集R（tag2先固定其真实f蓝）。

把Q染蓝、P\Q染红、L中R染红而其余染蓝。P端双色的原边已有两色；全蓝P迹的外部正集被R击中；全红P迹的外部负集未包含于R，故仍有蓝点。全部35原边proper。运输回原标签不改变结论。

因此本库存完整必要域零残给出上述原H的Property B，不依赖每份放松源可实现。因此证明只覆盖指定库存；它不把其他I1/I2库存或完整m(5)下界计为已证。

## 7. 证据与复现命令

- [QUAD_JOBS.py](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/QUAD_JOBS.py)、[JOBS.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/JOBS.json)、[JOBS.tsv](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/JOBS.tsv)：7770三四迹多重集、真群及630代表；
- [GENERATE.cpp](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/GENERATE.cpp)、[GENERATION.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/GENERATION.json)：强制基础J完整生成、每源菜单与零残；
- [PROFILE_FIRST_FIVE.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/PROFILE_FIRST_FIVE.json)：先做的小profile；
- [NECESSARY.bin](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/NECESSARY.bin)：完整源和自身Q/tag，结构同先前库存的little-endian `<QH6B`；
- [VERIFY.cpp](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/VERIFY.cpp)、[INDEPENDENT_CHECK.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/INDEPENDENT_CHECK.json)：另一J构造、全键相等、完整35迹与门绑定。

项目根运行：

```sh
python3 context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/QUAD_JOBS.py
/usr/bin/clang++ -std=c++17 -O3 context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/GENERATE.cpp -o /tmp/propertyb35-p7-three-quads-generate
/tmp/propertyb35-p7-three-quads-generate context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads 630
/usr/bin/clang++ -std=c++17 -O3 context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/VERIFY.cpp -o /tmp/propertyb35-p7-three-quads-verify
/tmp/propertyb35-p7-three-quads-verify context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads
```

禁止加`-DNDEBUG`；实际结果为PASS。不依赖概率位置DP、外部布局、优化器、MCP或Lean。

## 8. 完整本机证据索引

- [QUAD_JOBS.py](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/QUAD_JOBS.py)：7770份三四迹多重集、真群和轨道生成。
- [JOBS.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/JOBS.json)：630份高迹代表与实际轨道大小。
- [JOBS.tsv](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/JOBS.tsv)：两实现共同读取的高迹代表输入。
- [PROFILE_FIRST_FIVE.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/PROFILE_FIRST_FIVE.json)：前五轨道的有界规模测量。
- [GENERATE.cpp](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/GENERATE.cpp)：强制未覆点对基础加剩余重数的J完整生成与selector。
- [GENERATION.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/GENERATION.json)：630轨道完整计数、每门源数及未覆零。
- [NECESSARY.bin](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/NECESSARY.bin)：573834份完整J键及每源自身Q/tag/计数。
- [NONGATED.tsv](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/NONGATED.tsv)：空的完整残余源文件。
- [VERIFY.cpp](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/VERIFY.cpp)：另一种顶点星J生成、全键比较和35迹独立分类。
- [INDEPENDENT_CHECK.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/INDEPENDENT_CHECK.json)：573834全键与20084190原迹角色PASS。

原研究报告为 [REPORT.md](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_quads/REPORT.md)。本文已完整写入必要域、无损覆盖、真群运输、实际门前提及原H二染色证明，不以报告链接代替证明正文。
