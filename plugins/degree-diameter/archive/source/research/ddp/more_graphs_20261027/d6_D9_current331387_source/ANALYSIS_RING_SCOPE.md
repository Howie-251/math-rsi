# normal Z6860 的 ramified-ring 迁移：合法性与统一商障碍

**结论：对每个合法 C49 作用，本336140阶群上任意三个inverse-pair生成元都不能给D≤9的Cayley图。** 这比原固定normal向量的商距离10见证更强；二者同属本ring variant，不新增模板或大实验。

本文件只paper核对群、投影及范围；不重复有限c列表，不枚词、不BFS、不构图。原小证保留于 [ramified6860_quotient_gate/RESULT.json](ramified6860_quotient_gate/RESULT.json)。

## 1. 构造确实合法，action不能直接取literal8

令normal模数m=6860=20·343，phase为C49。对单位a满足a49=1，RIGHT law

(j,n)(k,t)=(j+k,n·a^k+t)

定义合法semidirect product，群阶49·6860=336140。

合法exactorder49作用确实存在。在mod343中取8=1+7，有
8^7≡1+49≠1 mod343，
再取七次幂得8^49≡1 mod343，所以其阶恰49。这里用二项式即可，无需大幂数值验证。Root给出的全局例a=3781满足a≡1 mod20、a≡8 mod343，故为单位且全局阶49。literal8本身不是mod6860单位，不能直接当全局action。

原normalized控制(1,0),(36,1),(45,1512)仍定义simple六正则图；g1^-36g2=(0,1)，所以全cyclic normal Z6860与phase C49均被生成，图连通。它是一条新的整数ring规则；旧field中首normal归零所用的(1−a)^-1在本ring不存在，因为a≡1 mod20。不能把旧field gauge完备性移植来声称枚尽任意raw normal赋值。

## 2. 保留的固定控制：C49×Z20距离10

任意合法a的mod20阶同时整除49与|U20|=8，因此a≡1 mod20。投影(j,n)→(j,n mod20)给实际商C49×Z20，固定normal向量的正元投影为(1,0)、(-13,1)、(-4,12)。

debruijn的既存19个c行证书证明target(0,10)的商距离恰10；十步见证为signed counts(-2,-2,6)。这是producer已保存并验证的小算术，本分析未重算列表。完整图若D≤9，其投影也必须九步覆盖该商，故这已经反驳固定控制的每一个合法action。商的exactdistance10不等于整个336140图的actual globalD10，本轮没有这种大图或BFS。

## 3. 更强统一结论：任意三pairs均被C49×Z140阻断

还有mod7投影。a的mod7阶同时整除49与|U7|=6，故a≡1 mod7。由于20与7互素，合起来a≡1 mod140。又140|6860，因此自然映射

π(j,n)=(j,n mod140)

是onto实际交换商Q=C49×Z140的群同态。其阶49·140=6860，kernel有49个元素。这个结论不依赖a是否faithful，也不依赖任何normal规范化。

现在任取connection set S={s1±1,s2±1,s3±1}。交换商内所有≤9步word都可交换合并成三个signed counts(t1,t2,t3)，满足|t1|+|t2|+|t3|≤9。其整数可能数为

sum(k=0..3) 2^k C(3,k) C(9,k)
=1+54+432+672
=1159。

理由是选k个非零坐标、各选正负，再选绝对值为正且总和≤9；后一数为C(9,k)。不同整数三元组投影还可能重合，所以实际商球大小至多1159，不能覆盖6860个商状态。若某generator投影为单位或两项重合，只会减少覆盖，不会绕开上界。

投影不增加walk长度；完整Cayley图若D≤9，就必须九步覆盖整个onto商Q，矛盾。因此对这个normal模数6860、phase49以及任何合法作用，**任意phase/normal的三个inverse-pair Cayley集合都不可能D≤9**。不需要把field gauge误说成完备，也无需再选normal或比较action。

## 4. 精确停止范围

统一结论只针对上述semidirect群及connection set由三个inversepairs形成的Cayley模型，不是任意336140点图不存在，也不是所有degree6构造或所有复合normal模数都不可能。别的模数不自动有Z140交换商；本轮不试其它cofactor、prime、field或生成元类型。

原fixednormal1512/Q20见证仍保留作control，当前更强Q140界将同一个ring variant的closure扩大到任意三pairs。未生成大图，actual_n/actual_D/普通无序坏对为空；新增BFS、word枚举、有限c验证与solver均为零。
