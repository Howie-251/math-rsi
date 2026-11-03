# 独立预登记：cap31的唯一balanced K(t,t)修补方案

2026-11-01，先于唯一tiny scalar执行。继承固定literal15factor的已实际g=(5,4,1,0,0,0)，不重跑32subsets；B仅使用给定genuine585 GQ polarity factor的projection性质，不读585数据或重算Steiner。

纸面初查支持：325≤6p_h+Σneighbor p_g；min helperdegree需9..16。K(t,t)的F-target bound把t限在8..19，p=31−t限12..23；至多两heavy A rows可推出C(p)，交集扣重数给(t−1)325≤t((t+3)p+C(p))。正预测是所有这些t都违反该必要式。

重点不能省略：S_h的row≥8需要GQ unique point-to-line 3path（不同B absolute d,b的2support与b的8个非absolute邻点恰交1）；row9与absolute无commonneighbor本身不够。h–ownFpin–helper–Fpin这条F-target路线存在，但K(t,t)中全部helper pins已被两part pin union计入。C(p)仅在p≤23使用；actual pins可不均匀、可同class多副本，g按不同own class计，重复pins不增强mandatory support。

只一次d0..31／t1..31标量计算，总≤2CPU，0旧factor/subset/585/source8775/field/BFS/solver/Lean/paidreview。即使支持，也仅排当前固定mandatory模型的balanced complete bipartite helper图；任意nonclique、unbalanced、改源/改旧边继续开放，本轮完成后停止。
