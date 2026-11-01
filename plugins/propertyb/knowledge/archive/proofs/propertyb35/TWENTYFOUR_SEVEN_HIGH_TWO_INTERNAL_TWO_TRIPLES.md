# 24点七高点：两内部边、两条三迹的完整库存

## 定理及实际对象

设 $H$ 为24点、35条互异五元边、覆盖全部点对的超图。顶点分为七点集 $P$ 和十七点集 $L$；$P$ 每点度八，$L$ 每点度七，每条原边都遇 $P$。恰有两条原边完全位于 $P$；其余原边中恰有两条的 $P$-迹为三集，没有四迹。则 $H$ 有Property B。

两条高迹保留原边索引，允许它们的P迹相同。本定理完整覆盖 $I=2,(n_2,n_3,n_4)=(9,2,0)$，不覆盖四条或更多三迹的其他库存。相邻missing型完全解析；不交missing型用完整必要P域和独立逐键核验。进口门的既有审阅不冒充本新caller的跨模型审阅。

## 1. 原度预算、signed接口与共同单蓝必要条件

记两内部边为 $I_1,I_2$，$C=I_1\cap I_2$，$c_v$ 为内部边在 $v\in P$ 的出现次数；两条三迹在v的频率为 $h_v$。二迹形成允许平行、无自环多重图 $J$，度为 $s_v$；单迹数为 $u_v$。

原边数和P总度56给

$$n_1+n_2=31,\qquad n_1+2n_2=40,$$

所以 $n_1=22,n_2=9$。每个v的实际度八及17个外点覆盖分别给

$$u_v=8-c_v-h_v-s_v\ge0,\qquad
4u_v+3s_v+2h_v\ge17.\tag{1}$$

后式等价于 $s_v+2h_v\le15-4c_v$，只是外部点对覆盖的必要条件，没有假设外部块互不相交。

固定P端蓝集Q、其余P点红。P迹双色的原边已proper；全蓝P迹给必须被外部红集击中的正约束，全红P迹给不能被包含的负约束。每条尚未proper的原边只给一个带原索引的约束，故外点总indexed次数至多七。每次调用都须让内部原边P端双色；负单／二不可省略。

对任意 $q\in C$，单蓝q使两内部边proper，准确signed为

$$m_4=6-h_q-s_q,\quad N_2=2-h_q,
\quad T=9-s_q,\quad B=22-m_4.\tag{2}$$

无正三或负单。若 $h_q+s_q\ge2$，则 $m_4\le4,N_2\le2$，由[四大正／三负二门](FOUR_LARGE_POSITIVE_THREE_NEGATIVE_PAIRS_REPAIR.md)修复原H。故反设尚未给出染色，可以对同一H全部共同点同时保留

$$h_q+s_q\le1\qquad(q\in C).\tag{3}$$

于是h_q≤1，h1点J孤立，h0点J度至多一。这是实际修复给出的必要归约，不是自由施加到原输入的附加假设。

两不同内部五边的missing二对只有相邻或不交两形。

## 2. 相邻missing型：完整解析证明

重标记missing二对为01、02。此时C={3,4,5,6}，$c=(0,1,1,2,2,2,2)$。内部边均不含0，故每个0q点对（q∈C）必须由高迹或J覆盖。

由(3)，若h_q=0，则s_q=1且J边为0q；若h_q=1，则s_q=0且唯一含q高迹也含0。因此每个C点h_q+s_q=1，u_q=5。任何不含0的三迹必遇C点，却与该点的唯一高迹必须含0矛盾；所以两高迹全部含0，允许重复。

四个C点共20条单迹，其余0、1、2三点共两条；h_0=2，故

$$u_0=6-s_0,\qquad u_1+u_2=s_0-4,$$

从而 $4\le s_0\le6$。令 $H_C=\sum_C h_q$。

### H_C>0且s0≥5

选C中h_q=1的点，它J孤立。蓝对Q={0,q}使两内部和两高迹均proper，无J正三。其余准确为

$$m_4=11-s_0\le6,\qquad T=9-s_0\le4,\qquad B=11+s_0\le17.$$

由[七正四／四负三门的35负四扩展](SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md)修复。

### s0=4

此时u_1=u_2=0。任取i∈{1,2}。

若h_i≥1，i至多漏掉一条高迹；若有遗漏，遗漏三迹含0、避i，所以必含C点q，选其中一点。若没有遗漏，任选C点q。蓝对Q={i,q}命中全部高迹并使两内部proper。C点的J边只可能为0q，故无正三。正族恰五P4，其余仅负三／四且总负不超过35，D7成立，由[五正四／总负35推论](FIVE_POSITIVE_TEN_TRIPLES_REPAIR.md)修复。

若h_i=0，则另一个非C、非0点的高迹频率至多二，而两高迹在0外共有四次关联，所以H_C≥2；可选C中h_q=1的点。该点s_q=0，i的s_i=7。Q={i,q}恰命中一条高迹，另一条给真实负二。准确signed为5P4、1N2、2T、17B。禁该负二的一点蓝后，五正大小至少三，剩余负三至多二，负四任意，D7不增。由[五正三／四、三负三门](FIVE_POSITIVE_THREE_TRIPLES_REPAIR.md)修复。没有假设两个高迹不同，也没有省略未遇高迹的负二。

### H_C=0

C每点都有J边0q，所以s_0≥4。两高迹只能均为012。由u_1+u_2=s_0−4≤2，某i∈{1,2}有u_i≤1。取任意q∈C，Q={i,q}使两内部、两高迹proper，无J正三。因h_i=2、s_i=5−u_i、s_q=1，准确为

$$m_4=5+u_i\le6,\qquad T=3+u_i\le4,\qquad B=17-u_i.$$

仍由七正四／四负三门修复。这三类穷尽全部可能，整个相邻missing型已解析闭合。

## 3. 不交missing的完整必要域及真群

固定missing二对01、23，内部mask124、115，C={4,5,6}，$c=(1,1,1,1,2,2,2)$。两高迹是35个三子集的允许重复多重集合，共630个。由(3)排除C上频率二者，余314标签高族。

真内部稳定群允许两missing对内交换、交换两对及任意置换C，阶为48。它保持原内部边集合、原度／PL容量、P点对覆盖及(3)。314高族在此真群下有21轨道，保留各完整轨道像，没有将两个高迹错误要求互异。

对每个代表，J必要域完整定义为：21个P对的非负整数重数总和九；原内部、高迹、J共同覆盖每个P对；式(1)成立；共同点另有(3)。等价上容量为

$$s_v\le\min(8-c_v-h_v,\ 15-4c_v-2h_v),$$

C内再与1−h_v取最小值。第一实现先在尚未被内部或高迹覆盖的P对上各放一条基础J边，再递归分剩余重数；每个实际J唯一分解为基础加非负剩余，因此完整。不同轨道代表只压高迹，不再擅自压J，也不假设J简单。

J总九但三位编码仍无损：不交型每点c_v≥1，由u_v≥0得s_v≤7，所以每个j_uv≤7。代码没有用“J总数九所以筛掉八重数”替代此实际容量证明。

完整21job共127862份必要J，全部由自身Q/tag接受，零未接受。第一次只跑两个job的profile为61696份、零残、CPU0.049976秒，因此按预算展开全域；完整GEN CPU0.058822秒。所有必要域都可比真实外部可实现域更宽，未把每个必要源声称为真实超图。

## 4. 完整菜单及原35迹自有见证

每个必要源以(1)恢复22单迹，加两内部、两高迹、九J，共35原P迹。候选蓝集Q大小一至四，两内部均须proper，任何全蓝高迹排除，避免产生未处理正二。全红高迹的负二逐索引保留；J全蓝给正三，不能误用pureP4门。

设准确数量为m4、m3、q负二、t负三、b负四。实际活跃接口如下；每个接受记录同时保存自己的Q和数量，其他未活跃代码分支不承担覆盖。

|tag|接口|接受数|进口|
|---:|---|---:|---|
|2|q=1,m3=0,m4≤4|1250|禁一点后[四正最小三元门](FOUR_POSITIVE_AT_LEAST_THREE_REPAIR.md)|
|3|q=0,m4+m3≤4|46531|同一四正最小三元门，正原本三／四|
|4|q=0,m4+m3≤5,t≤3|21874|[五正三／四、三负三门](FIVE_POSITIVE_THREE_TRIPLES_REPAIR.md)|
|9|q=0,m3=0,m4≤7,t≤4,b≤35|8494|[七正四／四负三门](SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md)|
|10|q=0,m3=0,m4≤6,t≤6,b≤35|1970|[六正四／六负三门](SIX_POSITIVE_SIX_TRIPLES_REPAIR.md)|
|16|q≤2,m4+m3≤2|7422|禁≤2点后每正仍非空，选≤2红避剩余负≥3|
|17|q≤3,m3=0,m4≤4|20530|[四大正／三负二门](FOUR_LARGE_POSITIVE_THREE_NEGATIVE_PAIRS_REPAIR.md)|
|18|q≤3,m3=0,m4≤3,t≤(4−q)16−1|16295|[三正参数门](THREE_LARGE_POSITIVE_TWO_NEGATIVE_PAIRS_REPAIR.md)，s=4|
|19|q=1,m4+m3≤5,m3≤3,t≤2|3178|禁一点后正二数≤m3≤3，用[五小正两负三门](FIVE_SMALL_POSITIVE_TWO_TRIPLES_REPAIR.md)|
|20|q=1,m4+m3≤5,t=0|318|禁一点后正≥2，用[五小正零负三门](FIVE_SMALL_POSITIVE_ZERO_TRIPLE.md)|

所有需要次数的门均用实际外点D7；禁点时正集删固定蓝点、遇该点的负约束整份删除，其他负集保持原大小。没有补正集提高次数，也没有删去仍可能坏的负二。

## 5. 第二不同构造及逐键完整性

原始源、记录与程序在[证据目录REPORT](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_triples_disjoint/REPORT.md)。具体来源：

- [HIGH_JOBS.py](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_triples_disjoint/HIGH_JOBS.py)、[JOBS.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_triples_disjoint/JOBS.json)：630→314→21真群完整轨道；
- [GENERATE.cpp](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_triples_disjoint/GENERATE.cpp)、[GENERATION.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_triples_disjoint/GENERATION.json)及同目录NECESSARY.bin：完整必要J及各自Q/tag；
- [VERIFY.cpp](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_triples_disjoint/VERIFY.cpp)、[INDEPENDENT_CHECK.json](../../context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/two_triples_disjoint/INDEPENDENT_CHECK.json)：第二完整构造、逐键相等和自身原35迹角色重算。

第二实现从两个有序高迹枚举再去重，不导入第一高族列表；由显式missing两对块置换独立构造48群，恢复全部630、314高族及21代表／每个轨道大小。J则逐顶点选择整份前向星，每个重数直接从缺失P对下界开始，不采用“基础加剩余”构造；容量从u≥0、4u+3s+2h≥17及(3)原式直接测试。

对每个job，存证键进入集合且不允许重复；第二构造每生成一键即断言唯一命中并删除，最后集合为空。同时反向检查每个存证源必要条件。因此不是仅比较总数，而是完整键集逐项相等。

每个记录自己的Q还被用于重建全部35原P迹，逐索引重新分类正负大小并核实际tag。实际本机第二检查PASS：127862键、4475170个原迹角色、CPU0.102047秒；没有借用r=3库存的结果代替本r=2执行。

## 6. 运输及返回原染色

任意满足定理的原H，重标记两内部missing到其标准型。若某共同点违反(3)，第1节已直接给出原染色；否则相邻型由第2节解析覆盖。不交型实际高族落在314标签域，真群把它与同一J送至某代表，J满足该job完整域条件。使用该记录自己的Q；表中的通用门对任意满足实际约束和D7的外部集合成立，故给实际外部红集R。

P重标记逆运输，L点及每条原边外部部分不变。内部和P端双色迹保持proper，正迹被R击中，负迹不被R包含，故全部35原边含两色。两missing型穷尽，定理得证。

本定理仅关闭I2两条P3库存。新caller的跨模型专项审阅范围另记；没有Lean、原H／外17点布局枚举，也不从本子定理推出原35边全称命题已完成。
