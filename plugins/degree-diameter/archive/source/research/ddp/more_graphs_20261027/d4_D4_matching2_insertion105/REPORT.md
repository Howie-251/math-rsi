# 当前104c两matching-edge插入：已闭精确重复，继承停止

本轮没有执行新枚举。唯一账本节点 [ddp-wave2-extension105-d4](../../../../research-wiki/experiments/ddp-wave2-extension105-d4.md) 已完整覆盖所问规则：从固定Bhakar104c源任取两条不相交旧边，删除这两边，新点接四端点，其余边不动。

既有 [原报告](../../breadth_20261027_wave2/extension105_d4/REPORT.md) 与 [终态](../../breadth_20261027_wave2/extension105_d4/terminal.json) 记录全部21528个原始边对及20904个合法不相交边对，无一得到D4。保存代表为105点、210边、全四正则、D5、相对D4的普通无序坏对八；这八仅属于保存的代表图，不是所有候选的统一坏对数。

这是题目要求的同一个两旧边吸收操作，不能与已闭的相邻单点拆分混淆。本轮先查到旧实验，因此没有建立新的正向预测、编译producer或重跑新根覆盖。

当前 [Comellas D4描述](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html#44) 仍列Bhakar104并链接104c。只读比较确认，本地d4_vertex_split/source104.edges与旧完整枚举extension105_d4/source.edges同为104/208，边集完全相等。原D4验收直接继承 [bhakar104_check.json](../../breadth_20261027_wave2/sources/bhakar104_check.json)，其中已检查全部104根；本轮不重验旧源直径。

[RESULT.json](RESULT.json) 和 [terminal.json](terminal.json) 明确标注继承结果与本轮零执行：候选数零、编译零、sourceD4 BFS零、candidate BFS零。当前尝试的actual_n、actual_D及普通坏对数字段为null；历史代表另列inherited_representative，不冒充本轮新图。

固定源与两边操作已经收束。不追加第三条边或局部repair，也不为这次查重新增Wiki节点；后续恢复应直接引用原canonical节点。
