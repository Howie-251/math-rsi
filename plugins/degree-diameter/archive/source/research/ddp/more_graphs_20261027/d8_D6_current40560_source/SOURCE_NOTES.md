# (8,6) 当前40560：配方推出全8正则，停止保边扩点

Fresh [主表](https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html) 的8D6格仍为40 560；[官方D6说明](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g6.html) 列 H7+，归于 Dharunish Yugeswardeenoo（2026-10-07）。唯一ledger按40560精确检索未见该当前源的独立profile条目；本轮只作来源和配方判断，0新实验。

真实描述不是未知的“可能非正则修改”：基图是39216点、全8正则的H(7) incidence graph。在336条spread线上各细分4条flag，共1344个新点；每条线上4新点成K4，各新点另有恰3条external边。

这已经给出完整度数账：
旧点每条被细分边都以一条新incident边替代，degree仍为8；
每新点有2个old邻居、3个K4邻居和3个external邻居，degree恰8。
所以作者定义的40560图全8正则，推得边数162240、free点0、空位0。这是配方推论，不冒充实际literal统计。

保持全部旧边、cap8的任何连通增点都必须接入某个旧点，而所有旧点均已满。因此已成功的spare-neighborhood/wholeN/proxy append入口在此固定源没有对象，**不值得为这个问题下载literal或跑actual profile**；本轮到此停止，不转删边、不启动solver或其它source。

完整D6只继承当前公开源报告，本轮没有从局部配方重新证明D6，也没有source BFS。现成本地metadata已列精确literal [deg8_diam6_n40560.txt](https://zenodo.org/api/records/23691325/files/deg8_diam6_n40560.txt/content)，2090250 bytes；本轮未下载。该label/完整边表尚无本轮绑定，丝毫不影响配方层面的满度停止结论。详细已知/缺口见 [PROVENANCE.json](PROVENANCE.json)。
