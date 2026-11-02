# 字面源与旧范围核对

目标固定为`research/ddp/refresh_20261029/f5_full_d20_D3/PARAMETERS.json`定义的3750点20正则D3图，现研究删除顶点后的诱导子图。

定向检索唯一method ledger、各实验节点、refresh_20261029相关报告，以及research/ddp与context中的3750/F5 induced/vertex-deletion/transversal-deletion表述，没有找到此前对这个字面源的诱导子图范围完成记录。一次宽关键词命中旧20261019用户快照，实际只是链接UUID中包含f5，所述对象为旧DD82，已排除为无关命中。

最近而不同的已闭范围：

* `f5_d20_edge_criticality_20261029/`保留全部3750点、只删边，不能据此直接排删顶点，因为删顶点可能同时移除关键路径端点。
* `f5_d10_closed_route_diagnosis/`固定三元/二元噪声集合的十度边选择域，保留原顶点集，也不是本次诱导子图。
* d15的6912点matroid相关对象属于不同源与参数，不作为这里的旧排除。

本次只有静态数学推导与小型字面参数读取，没有新图、删除集枚举、BFS、SAT或controller生成。一般诱导搜索未执行，未读完整3750点边表。
