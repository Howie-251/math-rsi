# Petersen合作骨架：确有短内部路线，完整端口分配仍无383图

14helper tree/单环的失败指出叶和无port父点的远cell覆盖弱点。这次改变结构：Petersen10 cubic骨架细分9条edge，H19/m24，全部helper都有oldspokes（10原点各1、9细分点各2），恰用自然364的28freeports；若成功为383点766边全4regular。

先预测至少一个细分pattern仍能Hdiam≤4。完整5005 labelled patterns确有235个diam4，其余4770是diam5；预测支持。这里5005是参数数，非非同构图/新成果。原Petersen全部120automorphisms把235个分成6个helper轨道，不假设旧28ports对称。

随后建立完整assignment模型：每port唯一owner，每helper给定capacity，总28容量自动exact；全部19×364 helper-old覆盖写成6916个正OR，半径由R_(4−Hdist)指定。因为旧ports彼此距5，≤5路径不能穿旧host回helper，故这些OR与完整383 D≤5充要；oldold继承、H-H已diam4。R0/R1从已有邻接读取，R2–R4全旧缓存，不新source BFS。

首次预算5orbit，各唯一5秒上限均快速rawUNSAT；第6是此前从未测的orbit，在实际总solver1.115CPU的反馈后明确重评，使用同40CPU累计预算补一个新窗口，亦rawUNSAT。没有重启前5solver。完整6orbit均已测，但全部UNSAT未proofchecked，因此保存原始证据，不包装为形式化整族排除，没有383edgefile。

为判断失败类型，只对orbit0的coverage分组做一次有预算二分：helpers0..8和0..3各rawUNSAT；0..1的2秒子模型UNKNOWN，按预测停止。故只能说前四helper要求已在原始求解中冲突，尚不能区分单helper自身不够还是两个/多个helper共享assignment不兼容。不能冒已得到最小UNSAT核，也没有继续优化坏点对。

全case9.371241682/40CPU，包含前metric、读取/建模、6主模型和3诊断子模型。helper metric共95095个小图根查询；source/目标383 BFS、旧球重算、Lean/ARIS均0。本阶段仍0新合法目标图/参数/Lean。

停止这个Petersen19骨架，不自动换细分数或重启seed/限时模型。下一换(3,9)的实际600点源，先查“两cut＋两个相邻helper”的旧scope；旧3/4cut样本不能替它作结论，全部2+2分割有3种而不只2种。
