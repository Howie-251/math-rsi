# 固定seed11的 direct-SAT at-most-5：精确纸面接口

状态：所述前缀计数与正coverage CNF在以下实际列/行绑定前提下精确。只作纸面推导，不读/运行求解器、LP/MIP、图、BFS、field、Lean、安装或负证书验证；数值与实际CNF输出由sole owner负责。本文件不把已有MIP的限时旧10-extras返回当SAT/UNSAT结论。

## 1. 变量和边界

固定本次seed11（source-guided v12312，不换seed）。复用已保存的current16416闭R3表：1744行是真实尚未被seed覆盖的target holes；3771列是实际available extra pin的覆盖代表。令x_i表示是否选第i列，i=1..n，n=3771。

前缀辅助s_(i,j)取j=1..5，编码ID为

    id(s_(i,j))=3771+(i−1)*5+j。

辅助区间与x_1..x_3771不重叠。i=1时加 `¬s_(1,j)`（j=2..5）；i≥2才引用s_(i−1,j)，不能误引用不存在的i=0变量。

全套约束为：

    ¬x_i ∨ s_(i,1)                              (全部i)
    ¬s_(i−1,j) ∨ s_(i,j)                        (i≥2,j=1..5)
    ¬x_i ∨ ¬s_(i−1,j−1) ∨ s_(i,j)              (i≥2,j=2..5)
    ¬x_i ∨ ¬s_(i−1,5)                           (i≥2)
    ¬s_(1,j)                                   (j=2..5)。

没有要求辅助变量反向等价于真实count，仍足以精确表达存在辅助extension iff sumx≤5。

## 2. completeness：每个≤5解都有辅助extension

对给定binary x，令q_i=sum_(k≤i)x_k。若q_n≤5，取

    s_(i,j) := [q_i≥j]。

x_i为真时q_i≥1，满足首类；前缀计数单调，满足carry；若x_i且q_(i−1)≥j−1，则q_i≥j，满足递推。overflow前件x_i且q_(i−1)≥5会迫q_i≥6，与q_n≤5矛盾，所以全部overflow满足。q_1≤1也使初始j>1单位子句满足。因此未给辅助变量多余自由度并不会丢掉任何合法≤5个extra pins。

## 3. soundness：第六个true必触overflow

由上述正向递推归纳：只要q_i≥j且1≤j≤5，任意满足CNF的赋值都被迫有s_(i,j)=true。新增true可由首类/递推提高阈值，未新增则由carry维持阈值。

若x中有至少六个true，取第六个true的位置i。此前q_(i−1)=5，故s_(i−1,5)被迫true；又x_i=true，直接违反 `¬x_i∨¬s_(i−1,5)`。因此无论把其余辅助变量如何取值，sumx≥6都无extension。辅助量仅有正向含义就已足够，不必加双向计数或排序预剪。

## 4. 1744正OR与实际pin cover

对每个实际hole target t，子句为

    OR {x_i : 实际current图d(pin_i,t)≤3}。

每行均为正coverage OR，因此其满足恰表示该未被seed覆盖的target被至少一个选中extra pin覆盖。seed已覆盖的其余targets无需再加行。必须保留全部1744真实hole行；若某行没有任何列，空OR就是false，不得删掉而变成宽松模型。

列压缩也可保持精确，但代表必须是实际available pin：若多个pins对全部1744 holes的mask完全相同，选其中两个不会增加覆盖；在≤5预算下总可只选一个实际代表。因此将相同mask压成一列不丢可行cover；空mask列也没有必要选。这个理由只用于本次无其他pin间约束的单Z覆盖，不能拿去压缩需要pin-pair兼容性的另一模型。当前列/行来源由已有实际mapping负责，本paper不重新计算或验证其mask。

结合第2、3节，CNF可满足 **当且仅当** 存在≤5个这些实际extra pins，与固定seed11合起来覆盖当前图全部16416 vertices的闭R3。总distinct pins≤16。这里只用实际可用pin和真实coverage OR，不依赖MIP的LP relaxation、旧objective或是否开始branching。

## 5. 返回状态与实际图边界

* 若solver返回SAT，需从x区提取actual pin labels，忽略s辅助变量；手检真实pin distinctness、currentdegree<16、extra数量≤5、seed∪extra的literal闭R3 union全覆盖。之后保全部accepted16416旧边，只增Z与这些pins，方可写实际16417/max16候选并交fresh验收。不能把SAT字符串或辅助赋值直接当实际图。
* 若返回rawUNSAT，它只是此**固定seed11、实际3771覆盖代表、1744holes和≤5extras** CNF的solver报告；没有DRAT/LRAT等负证书检查或Lean闭合，本paper不将其冒作认证familyNO，更不排其他seed、一般16-pin cover或一般(16,4)。
* 时间到无结论保持UNKNOWN，不再换seed、续相同solver时钟或发第二window。本case没有因从MIP改为SAT而清零先前成本。

cover若命中，`AVAILABLE_PIN_EXTENSION_PAPER.md`的通用SingleExtension可给genuineWalk≤4；最大度16且16417>(16+1)^3=4913足以数学排D3。具体Lean仍待新图实际输入/cover/degree证据闭合，不借旧16416 PASS提前计数。完成纸面后停止。
