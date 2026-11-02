# 固定66条实际路径的逐边电压：从NO到可构造单packet？

继承：固定binary240/8regular/D4校准底图，目标C23普通覆盖5520>保存主表5334。四globalcoeff已全12720规范NO，不重跑。

新增自由度：每条实际无向point-edge有独立F23电压，以小label→大label为正，反向取负。不是换field/fold/base；tree gauge只是重标fibres，完整自由度cycle rank721。

具体预测：保存最紧8→70的66条NB≤5paths，在实际signed point-edge flow下至少23个不同，且相对一条路径的flow差rank≥22。若后一项支持，选择22条独立差并解delta_i·theta=i，可立即构造此packet全23phase的实际反向一致电压；不止说容量通过。若rank不足，仅预测反驳，不推不存在。

仅消费TYPED_BASE_ARCS和CRITICAL_PACKET_PATHS，不重新枚NB路径或做BFS。输出960条边标签/每path的稀疏整数flow、相同flow类、差rank与独立rowindices；达到rank22时输出显式960电压及66pathphases，检查phase并集。所有mod23累加来自整数0/1，edge反向取负，空/闭walk按真实flow保留。

CPU硬限3秒，一次脚本；新增准备按0.20计，先前同底图1.496812969保留，新的逐边自由度问题累计上限10CPU。通过单packet不自动全pairs搜索；先观察是否真正移除了上一global obstruction，再选择针对性的diag/allpair必要门。无solver/新base/目标图BFS/Lean/ARIS。
