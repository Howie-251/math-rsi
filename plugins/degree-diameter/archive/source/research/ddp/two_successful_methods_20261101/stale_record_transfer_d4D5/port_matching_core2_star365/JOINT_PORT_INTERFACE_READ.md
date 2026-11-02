# Natural364：先联合设计portmatching与四corepins的读取接口

本轮只读既有PRED/NOTE/RESULT、sample代码及相邻port缓存元数据。无源解析、BFS、新距离/球查询、匹配计算、solver或追加样本。原规则仍UNKNOWN；未定位同规则的严格全域排除，旧保边/pureappend排除不包含这里的删旧边与加旧旧边。

## 旧样本实际怎样选

源是自然H3极性图364/714，28个degree3ports、336个degree4core，不是公开364/728正则图。固定seed202611010405的mt19937_64先从630条core-core边池用rng()%630取两个索引、排序并拒共端点；再独立shuffle全部28ports，相邻两项成14对，排序pair及matching。两cut索引加完整matching作canonical key。10115次draw得到10000个不同合法配置，duplicate0，全部newroot364 R5失败，旧根BFS0。它是matching与cuts独立随机选择的样本，不是matching已按覆盖设计的穷尽。

首配置cuts为(43,58)、(151,314)，故固定P={43,58,151,314}。saved首坏点0距newroot6，真实最短路为364–43–54–56–360–345–0；M(2)=256。后面没有进入旧旧检验，不能把新根失败说成旧路线损伤的实测。

## 首缺点可定位到现成义务

旧 `source_and_single/PORT_CLASSES.json` 的R2类按port排序，port2的类含0。28个R2类恰分割全部364点，因此0的唯一port owner为2。β=dG(2,0)未查新数据；目前只知β∈{1,2}，不虚构具体值。

令T=G−两cuts。所有cut端点都在P，故dT(P,t)=dG(P,t)：取最短的source P到t路径，若穿cut，可从该cut下游的P端点重新出发，尾段严格更短，矛盾。因此一条最短P路线必避cuts。结合已有newroot距0为6和saved的P到0五边旧尾路，逻辑推出dG(P,0)=5；这是旧证据推论，不是新BFS。

## Exact joint-mate条件

不同原ports距5（已有R3/R4 port证书及sourceD5）。newroot起的简单≤5路径不返回newroot；若用了两条matching边，两者间必须有连接不同ports的oldT段，长至少5，加两matching步已超5，故最多用一条新matching边。

未用matching时，新根可覆盖的正是source闭R4(P)。考虑hole t，即dG(P,t)>4。若用matching a–b，路线代价为

`1 + dT(P,a) + 1 + dT(b,t) <=5`。

P只含core，故dT(P,a)≥1，尾段至多2。因此b必是t的唯一R2 owner o(t)。令β_b(t)=dG(b,t)≤2；其≤2源尾路若碰P，则dG(P,t)≤2，与hole矛盾，所以该尾路自动避cuts。前腿到P距离又由上面的不变式保留，故hole的精确条件为

`dG(P,mate(b)) + β_b(t) <=3`。

这给首坏点0的强制义务：port2必须配给满足dG(P,a)+β≤3的a。当前mate256违反该条件是由saved失败与上述精确引理推出；没有另查dG(P,256)或β的数值。

对每port b，将其R2类中全部holes合并。若类无hole，L_b为所有其它ports；否则

`L_b={a!=b: dG(P,a)<=3−max_(hole t in class b) β_b(t)}`。

无向允许边{a,b}必须同时满足a∈L_b、b∈L_a。于是这个28点允许图存在perfectmatching，恰等价于固定P的新根R5覆盖全部旧364点。不是只修0后继续随机配其余点，也不能忽略某对的另一端所承担的类覆盖义务。所有原port pairs均非旧边，degree规则不新增困难。

## 唯一未测预测与最小数据

只保一个可推翻预测：**固定上述首P，存在另一个28port perfectmatching满足全部精确allowed-mate条件，使newrootR5全覆盖。** 不预言旧旧D5或完整365成功，不换cuts、不扫全cutpair、不续seed。

最小新数据是这四个corepin各自的闭sourceR4支持，用于得到完整hole集合。旧R2类/portR3R4位集已在 `source_and_single/{PORT_CLASSES.json,PORT_BALLS.json,R3.u64le.bin,R4.u64le.bin}`；port的R1邻接与R2类能补β和<=1/2阈值，现成portR3给<=3阈值。无需重做28port球或source全D5。本轮没有执行这些新支持或label查询，所读接口也没有四coreR4/全geodesic矩阵可直接套用。

若未来matching门通过，旧旧路线仍须最终候选检查；本门不授权solver、matching枚举或图生成。读取整理保守0.3 CPU秒/cap1，当前停止，只写本md/json，STATE/ROUND/pages/Wiki不改。
