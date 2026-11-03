# 当前(11,6)186033源：唯一一缺口star及全部双guard检验

没有得到186034点D6图。本轮绑定了官方实际186033点源，发现恰有一个只含一个满度邻点的原型，支持了第一项结构预测；但将该满度邻点删去后，全部合法单guard和双guard均不能补齐全旧图五步覆盖，构造预测被推翻。此固定规则完整结束，不扩大到新的原型或连接方式。

## 实际来源与结构测量

官方 [D6描述页](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g6.html) 列出186033点图及完整压缩邻接表。贡献为Dharunish Yugeswardeenoo在Rishabh Rajiv182618点图上保留全部旧边、增添3415点；本轮的source绑定来自该186033实际文件，没有用旧小图替代。

单次下载文件 [source186033.adjlist.gz](source186033.adjlist.gz) 为5936714字节，耗时67.656349墙秒。输入为186033行、2021634个双向邻接项；规范化实际无向边数1010817，与官方说明相符。[SOURCE_PROFILE.json](SOURCE_PROFILE.json) 记录一次实际解析的结果：

| 旧度 | 点数 |
| --- | ---: |
| 7 | 3 |
| 8 | 11 |
| 9 | 13 |
| 10 | 24658 |
| 11 | 161348 |

空余度顶点24685个，总空余槽24729。对每个v，令satN(v)为其度十一邻点数。最小satN恰为1：没有完整可复制的free-neighborhood star，只有一个satN=1的原型19161，旧度十，唯一满度邻点78477。

[PREDICTION.json](PREDICTION.json) 在实际度测量前预测存在satN≤1原型，这项预测得到支持。其九个合法旧邻点为

~~~
72425,85923,89934,95946,103392,107088,113094,120546,127006
~~~

这九点全部旧度十。完整邻域与度数见 [PROTOTYPES.json](PROTOTYPES.json)。source的D6继承公开来源；本轮没有重新作全源直径BFS。实际邻接同时保存为 [source186033.header.edges](source186033.header.edges) 及32位CSR，以免后续重解析原始文件。

## 固定增点规则与覆盖条件

新点x保留全部旧边，连接上述九点，再允许从其余24676个旧度小于十一的点中选择至多两个不同guard。因此新点度为9、10或11，每条新增边的旧端点均有实际余量。

固定旧图D≤6时，这个扩张达到D≤6，当且仅当所选邻集S在旧图中的闭R5覆盖全部186033点。旧旧点对原有路径全部保留；新旧距离恰为1+dist_G(S,y)。这不是只检查局部损失或把全部free的并覆盖误当成两个guard可覆盖。

[PROBE_PREDICTION.json](PROBE_PREDICTION.json) 在R5查询前冻结：唯一原型的mandatory9加至多两个guard可以完整覆盖。预算30CPU秒，若覆盖mask或双guard决策不能完成，则应记UNKNOWN。

一次mandatory9多源R5遍历覆盖181832点，尚缺4201点，耗时0.010212CPU秒，完整列表见 [MANDATORY_R5.json](MANDATORY_R5.json)。这4201是一个固定邻集的覆盖缺点数，不是全图普通无序坏对数。

配合代理只读测量了遗漏满pin78477的完整邻域：所有24676个合法guard与它的邻域最多共享一个点，故此前D13中的高重合直接代理在这里不存在。相应文件为 [FREE_PIN_PROXY_ANALYSIS.json](FREE_PIN_PROXY_ANALYSIS.json) 与 [core_mechanism/TARGETED_NEIGHBORS.json](core_mechanism/TARGETED_NEIGHBORS.json)。没有为16个弱共邻点另开BFS采样；继续按冻结范围作完整双guard判断。

## 精确有限结果

对4201个缺点同时初始化位向量，沿实际无向边作五轮闭邻域传播，得到每个合法guard可在五步覆盖的缺点mask。每层186033×66个64位字，双缓冲约196.5MB；最终仅保留合法guard的mask约13MB。这是本次搜索输入，不是重验旧源直径，也没有建立24685×186033个完整R5球。

实际24676个guard的mask全部不同且非零。没有一个mask覆盖全部4201点。双guard决策对每个第一mask，求所有未覆target的coverer集合交；交集为空即排除所有可搭配的第二guard。按标签规范化避免同一点重复，全部24676个第一mask均已完整处理，等价覆盖全部304440150个不同guard对。每个缺点均有8662至14747个单guard支持，因此失败是两个guard无法同时满足全部覆盖要求，而不是某个缺点完全没有可选入口。

| 项目 | 结果 |
| --- | ---: |
| 完成的闭邻域传播轮数 | 5 |
| 合法guard | 24676 |
| 不同非零mask | 24676 |
| 完整单guard解 | 0 |
| 完整双guard解 | 0 |
| 双guard第一mask完整处理 | 24676 |
| UNKNOWN / 未试原型 | 0 / 0 |
| 导出186034点D6图 | 0 |
| exact native CPU秒 | 0.907972 |
| exact编译CPU秒 | 1.143902 |
| run_exact实测父子CPU秒 | 2.058606 |

另一次源解析/度分析耗时2.978169CPU秒。预算账面合计2.418606CPU秒含此前measure编译与查询的0.36秒预留；该预留不是单独精测的编译CPU值。

结论见 [EXACT_RESULT.json](EXACT_RESULT.json)、[RESULT.json](RESULT.json) 及 [terminal.json](terminal.json)。完整mask在 [guard_masks.u64le.bin](guard_masks.u64le.bin)，标签顺序在 [guard_labels.txt](guard_labels.txt)，缺点支持数在 [TARGET_SUPPORTS.json](TARGET_SUPPORTS.json)；实现为 [exact_guard.cpp](exact_guard.cpp)、[run_exact.py](run_exact.py)。

零、单、双guard全部不能给D6；条件式地看，每个这样的扩张图其实都恰D7：旧图D6给新根到全部旧点至多七步，覆盖失败又给某点至少七步。这里没有导出代表边表或统计全图普通无序坏对，相关实际成图及坏对总数字段保持null。

已闭范围仅为当前实际186033源的完整free-star规则及其唯一satN=1原型的mandatory9加至多两个guard。它没有排除其他原型的更大替换、不同连接机制或一般186034点图。按本批停止条件，不扩到satN=2，不按缺点数量追加修补，也不更换source。
