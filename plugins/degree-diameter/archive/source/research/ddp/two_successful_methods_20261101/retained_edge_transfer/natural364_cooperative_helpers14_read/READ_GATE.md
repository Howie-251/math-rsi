# 自然364/714：14-helper合作扩张的旧范围与浅树接口

准确旧范围是1–13个helper严格NO，并非任意有限H严格NO。限定为自然364点/714边极性源、保留全部源边、没有新增old–old边、maxdegree4，只经28个degree3端口接helper。证据是 `research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/MULTI_VERTEX_PORT_BARRIER.md` 和 `helper13_tree_probe/REPORT.md`。两份原文都明确14尚未构造或搜索。本门不覆盖公开364/728的全4正则Delorme源，也不重复196371次Hall门。

原计数证明要求28端口各接一个helper，且H连通。端口两两旧距5：任何长度≤5的新点到旧端口的路线只能从该端口进入旧源，不能先从别的端口通过旧源再到它。不同H分量之间经旧源的过渡至少7步。于是4k≥28+2|E(H)|≥28+2(k−1)，得k≥13。k13强制H为树且各helper总degree4；树径≤4。旧3276个三端口集合以及81900个“三端口＋parent端口”缓存检查完整关闭k13。

本次只读可以进一步推出：**14个helper的浅树也没有剩余接口**，不需新mask检查。

1. 若k14且H为树，最大helper总端口容量为4·14−2·13=30，而必须连接28个实际旧端口，因此所有helper合计只有2个未用degree slot。每个H叶子都有至少一个旧端口；否则一个叶子独自就空3个slot。
2. 从任意helper到叶子的附着端口需≤5步，迫H距离≤4；树的直径由叶子取得，故diam(H)≤4。取半径2的中心，令其b≤4个分支各有k_i≤3个第二层叶子，则1+b+Σk_i=14。只能b=4、Σk_i=9，所以至少一个k_i=3。
3. 该满分支的parent和中心都为H-degree4、没有旧端口。取此分支的任意叶子，令其旧端口集合T，1≤|T|≤3。其同分支兄弟只能贡献各自R2单元；别的分支parent只能贡献各自R1；别的第二层叶子只能贡献其旧端口本身。它们都不能覆盖一个foreign第二层叶子的端口q所对应的R2(q)内部。
4. foreign第二层叶子必然存在且各有旧端口。所以该叶子覆盖全部旧源的必要条件，是至少一个q∉T的R2(q)\{q}完全包含在R4(T)中。旧 `helper13_tree_probe/CAPACITY.json` 已实际验证所有3276个三元组的good(T)均为空；对于|T|<3可补足为不含q的三元组，单调性同样排除。故所有这种14-helper树均NO。

这是将已保存的完整局部障碍应用于k14树的纸面推论，不是执行了14树枚举、端口assignment或新目标图验证。未由本门宣称任意14-helper H不存在：k14时28spokes与degree预算仅迫|E(H)|≤14；排树后仍可能是连通unicyclic H，且必须恰有14条H边、每个helper总degree4，附着端口数a_h=4−d_H(h)。这是真正尚需纸面判断的最小剩余结构接口，本门不选cycle、搜拓扑或分配端口。更大k也未被本次结论关闭；新增old–old边、删改源边和其他源都在此范围之外。

若日后研究这个剩余结构，exact helper-to-old condition已有小缓存接口：给定H与互不相交、并为全部28端口的P_h，对每个helper h须有

    union_{g: d_H(h,g)≤4} R_{4−d_H(h,g)}(P_g) = V(source).

长度≤5路线不可能包含一次不同旧端口间的旧源穿越再返回H（至少7步），所以这个是helper到旧点的精确覆盖式。还须确保helper间距离≤5；保留源边直接继承所有old–old D5。这不是一份已找到的端口分配，也不把必要的H条件冒称可行图。

最小可复用数据均在 `research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/`：

- `source_and_single/PORT_BINDING.json`：唯一自然源 `source364.edges`、28实际端口升序、source714边与度谱、原几何D5证明。端口是[2,11,24,56,66,74,85,98,104,116,117,126,195,200,215,216,230,237,249,256,267,298,307,320,331,341,343,356]。
- `source_and_single/PORT_BALLS.json`：28行exact R3、R4，每行6个uint64，vertex0为bit0；对应 `R3.u64le.bin`、`R4.u64le.bin`，小端；bits364..383为零。R3大小40，R4大小121，R3/R4在port集合上均只含自身。
- `source_and_single/PORT_CLASSES.json`：28个完整R2单元，每个13点，分割全部364点；包含R2类成员及R3/R4 port-incidence identity。R0从端口标签直接给出；R1如实际后续公式需要，应定位旧缓存或届时另授权新小数据，不能把R2当R1。
- `helper13_tree_probe/CAPACITY.json` 与 `triple_good_sets.json`：全部3276三元组，maximum_good_count=0；本次14-tree推论直接需要的唯一覆盖障碍。
- `helper13_tree_probe/PARENT_PORT_CAPACITY.json` 与 `parent_port_good_counts.u8.bin`：全部81900(T,p)，maximum_good_count=0，uint8按lex三元组、再升序外部parent端口排列。该更强旧障碍可继承，未重新执行。

此次只读/整理保守费用0.5 CPU秒；sourceparse=0、geometry=0、旧源/新球BFS=0、Hall=0、树枚举=0、assignment=0、solver=0、新图=0、Lean=0。未修改原结果、Wiki、STATE、ROUND或页面。停止读取门，不自动启动14 unicyclic或更多helpers搜索。
