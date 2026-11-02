# 固定σ的一个tight-row：局部重叠/铺砌门
仅paper，0数据/数值/source/BFS/field/SAT；取root指定的一行，其非空packets总大小恰19。
对两个**不同**packet A,B，(A+a)∩(B+b)≠∅ iff b−a∈A−B；若A−B=F19，任意两平移必重叠。
因此总大小19时出现这种pair，整个row的union至多18，严格排这张冻结σ的所有shifts。
若无该pair，仍可能有多packet障碍；不能把pair差集未满误作可铺。
任何row铺砌可共同平移所有packet，故将最大packet shift定0不丢解；只用这一个gauge，勿再叠加t0=0。
按固定次序枚其它nonsingletons的19个rotations，只接受与occupied不交的选项。
固定剩余packet次序时，memo(index,occupied)完整；若自适应换未放packet，memo须另含其集合。
总大小19使“union满19”恰等价于全部packet两两不交；这是tight条件，非一般容量行结论。
每个非固定singleton均可凭自己的shift落到任意空格；nonsingletons放完后恰有相同数量空格，故可全部补齐。
最大packet若也是singleton，先占0并从待补singleton计数中去掉，结论相同。
完整DFS无铺砌只排固定σ；原CaDiCaL20s UNKNOWN历史不能改写为solver UNSAT，但可另记数学row-NO。
DFS命中仅证明这一行可铺，不给其它行共享shift，更不是actualmatching graph；预算截断仍UNKNOWN。
预测为本代表tight-row不可tile，实际若refuted如实保留；不查第二行、不σ2、不新求解或成果计数。
