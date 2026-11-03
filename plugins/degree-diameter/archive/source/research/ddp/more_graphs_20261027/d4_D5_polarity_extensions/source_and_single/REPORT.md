# (4,5)自然H3源：真实28端口，单点扩张被统一覆盖条件排除

这次转向原(4,5)参数，没有继续H9或(12,5)生产。公开Delorme364源是364点、728边、全4正则，不能保留所有旧边再连接新点。另有现成几何定义的自然H3极性图：364点、714边，度数3的28点、度数4的336点。两者不能把余度混用。

本次直接读取 `research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/Q_data.json['H3_graph']`，原样导出简单图 [source364.edges](source364.edges)，没有从公开728边图随机删除14边。既有 [source_local_check.json](../../../breadth_20261027_wave4/controller364_quotient/source_local_check.json) 已记录自然源的相同度谱。实际端口、文件绑定与共享缓存格式保存在 [PORT_BINDING.json](PORT_BINDING.json)。

自然源的D≤5由极性投影继承：H3 incidence graph直径6，任意point p到polarline π(q)的距离为奇数，故至多5；商投影给出p到q的≤5walk，删除loop步骤不增距。Moore(4,4)=161<364，所以恰D5。这里没有重新跑已知源的全根BFS。

**事前预测。** [PREDICTION.json](PREDICTION.json) 预测绝对端口彼此相距5，因此每个端口的R4球不能覆盖其它端口。程序只从28个实际spare ports各生成一次深度4球，同时保存R2、R3快照，得到：

- 每个R2球有13点，28球恰好分割全部364点。
- 每个R3球有40点，每个R4球有121点。
- 每个R3/R4球与28端口集合的交均只有其自身。
- 全28个R4球的并覆盖全部364点。

故只允许从这些余度点选邻居时，R4 set-cover最优值**恰为28**，不是4。任意新增点的degree≤4，至多选择四个端口，必漏其它至少24个绝对点。所有 \(\binom{28}{4}=20475\) 四点集合及更小集合被同一证明排除；实际组合循环次数0，不能写成执行了20475次全图测试。没有365候选图，也没有solver或随机seed。

这也提供同源双点任务的便宜必要障碍：相邻新点各至多连3个旧端口A/B时，新根条件R4(A)∪R3(B)在端口集合上至多覆盖6/28，因此无需扫描数百万对三元组。该任务由另一producer持有，本代理只交付同一缓存，不重复计算或修改其文件。

[PORT_BALLS.json](PORT_BALLS.json) 保存28行R3/R4的六word精确位集及遗漏类；[PORT_CLASSES.json](PORT_CLASSES.json) 保存R2的28个完整分区。二进制 [R3.u64le.bin](R3.u64le.bin)、[R4.u64le.bin](R4.u64le.bin) 各1344bytes，按PORT_BINDING的升序端口排列，每行6个little-endian uint64、vertex0为bit0、高20bits为0。它们同时供单点和双点生产器使用。

这次实际成本为28个端口的depth4预处理，CPU0.039194522秒；source full BFS为0，旧public源BFS重跑0，newgraph0。程序为 [run.py](run.py)，完整终态见 [RESULT.json](RESULT.json) 与 [terminal.json](terminal.json)，pending=[]。

关闭范围仅为此明确自然364源、保留旧边、从全部实际spare ports新增一个degree≤4点；不能据此说一般365点图不存在。原公开全4regular源则在保边单调扩张上没有端口。后续若改变旧边或整体连接机制，属于未被这里排除的新问题，本任务不自行启动。
