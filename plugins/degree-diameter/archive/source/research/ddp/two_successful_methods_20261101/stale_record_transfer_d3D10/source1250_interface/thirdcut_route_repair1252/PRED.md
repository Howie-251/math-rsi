# Frozen object4536：一次targetpilot＋完整pin-transfer

已读READ_GATE和THIRDCUT_ROUTE_PAPER。固定sourceConderC1250.2、anchor[0,1]、secondedge_id1515=[869,1178]、x[0,1178]/y[1,869]，savedB t1058。不重跑旧A/B或sourceD10。

P1（确定短路、仍需actual图绑定）：保x1178，则x→1178=1/y≤2。pilot取第三边g=t1058与三个旧邻点h，移p0/1/869；p0给x→t=1/y≤2，p1/869给y→t=1/x≤2。检验9个actualmodified图、bothnewrootsR10。

P2（可推翻正预测）：冻结base全部合法transfer里至少一个通过both newrootR10。它仍不是完整D10预测；只有bothpass才逐所有1250旧labels ordinaryBFS至firstfail或完整hit。

P3（root在结果未知时并行提出，pre-run录入）：pilotg=t时移p0或p1，会使withdrawn旧pin p自身成为x→p>10反例；p869未排。记录每pilot的精确x→withdrawnp及路径，若反驳保actualcounterexample，不因此停止其余合法域。

literal域数预测：eligible thirdedges1865，3可移pin×两orientation再原nonedge过滤＝11178；pilot9。源码按actual域运行，若计数不同记录差异而非硬筛。fullstage跳过已pilot9，不重复旧two-cutgraph。

每config记录savedt修复、新x／另一helper失败、oldold失败，首反例给实际最短路径与edge角色，不优化总badscore。first完整1252hit保存全边表／生成规则／allrootstats，停交fresh；fullNO只闭此frozenbase/保x1178transfer域，不全三cut或一般3D10。

总20CPU包括read0.529389544、新prep0.5、编译与父子actualCPU，单worker。source一次literalparse，仅inputbinding，不sourceD10验证；不solver/field/Lean/ARIS或随机seed。
