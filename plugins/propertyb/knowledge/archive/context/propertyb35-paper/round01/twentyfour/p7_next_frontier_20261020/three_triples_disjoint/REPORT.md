# I2(7,3,0)：完整不交missing域与独立逐键核验

规范全文：[TWENTYFOUR_SEVEN_HIGH_TWO_INTERNAL_THREE_TRIPLES.md](../../../../../../proofs/propertyb35/TWENTYFOUR_SEVEN_HIGH_TWO_INTERNAL_THREE_TRIPLES.md)。该稿内联两missing形状的实际H→signed→修复连接；相邻型完全解析，不交型用本目录完整必要域。新I2 caller的跨家族专项审阅尚待；不能借用进口通用门的审阅scope。

## 实际域与结果

固定P=0…6，内部五边mask124、115，missing01、23，C={4,5,6}。三个P3高迹为35个三子集的三份**允许重复多重集合**。完整7770标签中，单蓝共同点修复归约h+s≤1留下h_C≤1的1266高族；真48群取商恰64轨道。J总七条，允许任意平行重数；u=8−c−h−s≥0、外覆盖4u+3s+2h≥17、Ppair覆盖及C上h+s≤1全保留。

完整64job必要J共126927；每个记录自己的P蓝集Q与门tag，未接受数0。直接逐源35原迹角色重分类4442445项。三高迹全红的负二始终保留；全蓝高迹不入本次P3/P4正菜单，避免误把正二当正三。J全蓝给正三，不能走pureP4门。

|步骤|结果|进程CPU秒|
|---|---|---:|
|HIGH_JOBS.py|7770→1266→64，48群完整像|0.011573|
|GENERATE.cpp|126927必要键，0未接受，4442445角色|0.052101|
|VERIFY.cpp|第二完整高族/J构造逐键相等，4442445角色与自身Q/tag重放PASS|0.104275|

第二实现按有序三高迹去重恢复域，显式missing对块置换恢复群；J按逐顶点整星直接分配，不采用第一实现先放mandatory基础后分剩余的方法。对每job保存键集合逐生成删除、断言唯一并最后为空；不仅比较计数。所有原记录反向检查必要条件，逐35索引重建，再用独立accepts分支核各tag实际假设。

NECESSARY.bin大小2030832字节，126927条16字节记录：低63位为numeric-mask升序21个三位J重数；随后uint16 job，以及六个uint8字段blue/tag/m4/m3/t/b。J总七，所以每个重数≤7，三位编码不漏输入。小负数由高族与每源Q重新推导，不由另一个源借用。代码沿用本项目已审双J构造的接口，在本新参数下重新生成/核验，不重跑此前库存。

实际活跃tag计数：2:3208，3:36008，4:24664，9:8266，10:754，13:1，16:6275，17:22237，18:16190，19:7796，20:1528。准确进口、禁点桥梁及范围在规范第4节完整展开；其他未活跃tag不承担覆盖。

## 重放命令

在项目根目录执行，断言必须启用（不传-DNDEBUG）：

```sh
python3 context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_triples_disjoint/HIGH_JOBS.py
clang++ -std=c++17 -O3 context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_triples_disjoint/GENERATE.cpp -o /tmp/propertyb_i2_three_triples_generate
/tmp/propertyb_i2_three_triples_generate context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_triples_disjoint
clang++ -std=c++17 -O3 context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_triples_disjoint/VERIFY.cpp -o /tmp/propertyb_i2_three_triples_verify
/tmp/propertyb_i2_three_triples_verify context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_triples_disjoint
```

若只核现存证据，编译及运行最后两行即可；VERIFY本身重建完整高族和J域。原两个job探索证据仍保留在同级i2_three_triples_pilot，不覆盖其首次遗漏菜单的nongated记录。本新完整域已有独立核验，无需从那两个job外推。

本轮没有原H／外17点／自由负布局枚举，没有Lean、wiki或导航改动。本次完整纸面子定理只覆盖I2(7,3,0)，不代表整个24点或原35边目标完成。
