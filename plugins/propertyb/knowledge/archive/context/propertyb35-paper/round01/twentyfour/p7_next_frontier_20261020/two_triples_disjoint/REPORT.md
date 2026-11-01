# I2(9,2,0)：完整两P3库存的证据

全文规范：[TWENTYFOUR_SEVEN_HIGH_TWO_INTERNAL_TWO_TRIPLES.md](../../../../../../proofs/propertyb35/TWENTYFOUR_SEVEN_HIGH_TWO_INTERNAL_TWO_TRIPLES.md)。其中相邻missing完全解析，不交missing用本目录全必要P域。本次没有展开r4/5/6，没有使用外17点布局或原H枚举；新caller跨模型审阅待主代理，不能借用进口门的scope。

## 完整域与执行

不交missing01、23，内部mask124、115，C456。两三迹允许重复，完整630高族；实际单蓝归约h+s≤1后，C频率≤1保留314标签，真48群21轨道。

J九条，21对非负重数，允许平行；u=8−c−h−s≥0，4u+3s+2h≥17，Ppaircoverage及C上h+s≤1全部保留。每点c≥1使s≤7，故J九条也无八重边，三位编码无损。

|步骤|结果|CPU秒|
|---|---|---:|
|HIGH_JOBS.py|630→314→21，完整真群像|0.007422|
|先两个job profile|61696必要J，零未接受|0.049976|
|GENERATE完整21job|127862必要J，零未接受|0.058822|
|VERIFY第二构造|逐键相等、4475170原35迹角色重算PASS|0.102047|

第一次构造在缺失P对上先放mandatory基础边再分配剩余重数；第二构造逐顶点整星直接分全部重数，逐键删除存证集合。两种高族枚举也分别为无序多重集合与有序二高迹去重，群分别从全P置换过滤与missing对块置换独立恢复。完整对象域逐键相等，不只总数相等。

NECESSARY.bin共2045792字节，127862条16字节记录：uint64低63位是numeric-mask升序21个J三位重数，uint16 job，六个uint8字段blue/tag/m4/m3/t/b。每个源自己的Q按原35迹直接重分类，原P3全红给负二始终保留；全蓝高迹排除，防止把正二误走P3/P4门。所有活跃tag及数学进口在规范第4节逐项内联。

## 重放

在项目根目录，启用断言，不传-DNDEBUG：

```sh
python3 context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_triples_disjoint/HIGH_JOBS.py
clang++ -std=c++17 -O3 context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_triples_disjoint/GENERATE.cpp -o /tmp/propertyb_i2_two_triples_generate
/tmp/propertyb_i2_two_triples_generate context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_triples_disjoint
clang++ -std=c++17 -O3 context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_triples_disjoint/VERIFY.cpp -o /tmp/propertyb_i2_two_triples_verify
/tmp/propertyb_i2_two_triples_verify context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_triples_disjoint
```

只核现存源时执行最后两行即可，Verifier自身完整重建高族/J域并重放全部35角色。PROFILE_FIRST_TWO.json保留实测前两job估时，没有把prefix当完整域；完整GENERATION.json明确complete=true。新结果没有覆盖r3证据或修改导航、wiki、Lean。
