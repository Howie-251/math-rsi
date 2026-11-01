# 失败转向案例：十点反例推翻泛门，再恢复真实共度限制

## 要检验的论断

36研究中曾希望用一个抽象signed门处理实际局部修复：“至多五个2…4元正集、至多两负三集、任意负四集、每点总出现≤7，总存在击中所有正集且不包含任何负集的红集”。这条泛门为假。下面是完整反例及可执行验证；它不是35边五元nonB超图。

点0…9，五正集P_i={2i,2i+1}。负三T₀={0,2,4}、T₁={1,2,4}。负四为四族：

    {b,5,6,8+c}       b,c∈{0,1}（4个）；
    {3,4,6,8+c}       c∈{0,1}（2个）；
    {b,3,7,8+c}       b,c∈{0,1}（4个）；
    {2,5,7,8+c}       c∈{0,1}（2个）。

逐点正负总次数为6,6,5,7,5,7,7,7,7,7，符合七次预算。每个最小正横截从各P_i选一个点，形成五立方体32顶点。两个负三是两个不交二维面，覆盖8候选；十二负四形成十二条边，覆盖另24候选，四族分布8/4/8/4且互不交。因此每个最小横截恰含一个负集。任意红集若击中全部正集，包含某个最小横截，同样受阻。

## 实际执行

从仓根执行；程序生成全部输入再以集合与独立位集两种方法核验，不读取外部证书、不需要SAT/MILP。复制单程序到工作副本即可，输出不会改archive。

```sh
PB_ARCHIVE="$PWD/plugins/propertyb/knowledge/archive"
PB_REPLAY=$(mktemp -d "${TMPDIR:-/tmp}/mathrsi-signed-XXXXXX")
cp "$PB_ARCHIVE/context/propertyb35-paper/round01/twentyfour/six_high_one_internal_high/two_triple_small_gate/CHECK_COUNTEREXAMPLE.py" "$PB_REPLAY/"
python3 -B "$PB_REPLAY/CHECK_COUNTEREXAMPLE.py"
```

预期`PASS_COUNTEREXAMPLE`、red_subsets1024、repair_count0，输出同名JSON含32份逐横截阻塞索引、243个击中正族的红子集总量与逐点预算。历史约0.00025CPU秒。若结果变动，保留实际集合/次数/未堵红集作为最小失败见证；不是去调求解器容差。

这项小核能反驳泛门，因为反例满足其全部前提，且1024红集穷尽结论对象。它不能反驳原五元命题，因为没有从signed约束构造全部35边、paircover、真实度数的H。

## 从反例读回丢失的原图信息

真实应用不是任意正族。24点原H里，q私有边是{q}∪A_i，A_i四元；固定同两个外点f,g蓝后，正残集A_i\{f,g}。若残集大小二，则原A_i必同时含f,g。设这样的原边r条，便有λ(f,q)≥r、λ(f,g)≥r。

f七度且paircover，真实共度超额

    Σ_(v≠f)(λ(f,v)−1)=4·7−23=5，
    2(r−1)≤5，故r≤3。

所以反例的五个正二集不可能来自这个实际caller，四个也不可能。正确转向是保留“正二集至多三个”的受限门，再证明它能从实际H返回合法修复。不能因为反例不能延拓为H就继续使用已否定泛门；也不能因为抽象门失败宣布原H分支无解。

归档[REPORT](../../../knowledge/archive/context/propertyb35-paper/round01/twentyfour/six_high_one_internal_high/two_triple_small_gate/REPORT.md)给原边共度推导；[受限门完整证明](../../../knowledge/archive/context/propertyb35-paper/round01/twentyfour/six_high_one_internal_high/two_triple_small_gate/RESTRICTED_GATE_PROOF.md)与[规范门](../../../knowledge/archive/proofs/propertyb35/FIVE_SMALL_POSITIVE_TWO_TRIPLES_REPAIR.md)给后续修法。原项目已将受限门接到对应六高一内部库存；不是全部24δ7或m(5)≥36已经闭合。

## 迁移这个案例

以后抽象修复门遭到反例，先核反例是否满足所有抽象前提，确认它究竟推翻泛门还是只击中某个证明。然后逐个把抽象正/负集合对应到同一批原边，检查simplicity、共度行超额、删同点造成的共同容量。这里关键不是再跑更大signed目录，而是恢复被压缩掉的“所有二残集含同两外点”这一共同来源。
