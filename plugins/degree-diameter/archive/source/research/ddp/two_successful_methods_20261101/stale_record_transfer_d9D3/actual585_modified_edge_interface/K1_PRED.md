# K1事前预测：一条p0-owner删边与三条远边

固定 p0 的port index0=actual585 vertex0，不换port、不借未验证传递性。旧k0/PORT16/固定sigma NO均不重跑；继承其ALL2080与ELIGIBLE字面数据。新规则恰有一条cut的端点owner是p0，其余三条cut的C16避免p0。

**正预测P1：** 存在一个真实p0-owner cut与三个far cuts，四个16-mask两两不交、八个core端点互异。四mask union大小64，唯一遗漏t必须与p0-owner cut的另一owner a匹配，另三cut的ownerpairs强制匹配。

**待检验P2：** 至少一个这样的必要端口packing同时让新根到全部520core至多3步。端口packing PASS不当图；若首packing corefail，在同一累计预算中继续固定k1完整域，到首allnewrootpass或完整NO/UNKNOWN。

65位mask用原port索引：旧64位far mask整体左移1，bit0明确对应actual p0=0；owner mask同样左移并置bit0。复用64owner masks和1568far masks，无新源路线/field/BFS计算来建立packing域。寻找1owner+3far，其union留一个非p0端口；原sigma单边也保留，因为含owner的新k1组合不是旧k0四远边子域。

若有packing，允许为新根core覆盖问题一次读取literal，并一次生成所需core目标R2支持（集合组合，不BFS/源D3验收）；全部cut端点均为新根pin，删pin内部边不改变到pin集距离。A-A matching不参与新根到core的<=3路，故恰检查旧B2(P9)∩core=520。保存各packing/corestage、缺点及支持。首全新根覆盖成功只交root，仍无剩56A匹配/旧旧D3证明，不生产完整586边表。

累计case cap20CPU，继承1.881081201；新准备预留0.20，独立scope-reader预留0.30，所有实际输出/失败计入。单worker，数值进程硬cap17/软16.8留收尾，0sourceD3/field/oldk0/PORT16重验、0solver/Lean/外审；完成即STOP，不另p0/5cut/seed。
