# 当前(14,5)94186点图：源绑定与稀有余量类对照

已取得并绑定实际94186点源，确认有3685个可接旧点、共3700个空余槽。但一次固定14邻点的完整覆盖预测被反驳，本轮没有生成94187点图。

公开[Comellas当前条目](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g5.html#145)将94186点图归于 Sami Hani Badaoui 与 Sarah Ellen Mary Vaughan，公布日期为2026年10月22日，说明它修改、增广了 Ryosuke Mizuno 的88452点图。[实际边表](source94186.edges)从该条目的精确链接单次下载，2026-10-27 17:17 UTC完成；7,734,396字节，传输约391.7墙秒。[SOURCE.json](SOURCE.json)保留来源与时间。

旧Mizuno图的[原始说明](https://github.com/rmizuno42/ddp/tree/main/results/degree14-diameter5)给出364状态×F3^5结构：四个自逆控制标签允许固定状态，另有状态相关的纤维内平移边。它的756个degree13点不能直接当作当前图的可接点。作者仓库的[源比较](https://github.com/rmizuno42/ddp/tree/main/verification/external-records-2026-10-23)未恢复新旧顶点对应；本轮也没有恢复对应，不能把当前前88452个标签或连续243点块认作旧纤维。[缓存摘要](ORIGINAL_EXTERNAL_COMPARISON.json)与[机制摘录](ORIGINAL_README_EXCERPT.md)仅作来源说明。

实际一次邻接读取产生如下分布，见[SOURCE_PROFILE.json](SOURCE_PROFILE.json)。

|当前度|顶点数|可接槽|
|---|---:|---:|
|12|15|30|
|13|3670|3670|
|14|90501|0|

边数为657452、最大度14。度缓存为[degree14.u8.bin](degree14.u8.bin)，全部3685个可接点及余量见[free_ports.json](free_ports.json)。度数测量CPU为1.141946663秒；没有重复source全源BFS。

## 一项先冻结、再检验的完整覆盖预测

15个degree12点为

    985, 5183, 26324, 31398, 36671, 37890, 45707, 52155,
    63199, 65367, 67894, 70330, 82700, 84746, 85397.

它们内部无边。其中52155与85397的12点开邻集完全相同；其余104对没有共同邻点。因此该类提供14种不同近端邻域，删去false-twin对中的一个不损失R4并。这个可见结构给出一项有限的路线互补假说：14种邻域代表能否覆盖全94186个旧点。近端分散只是猜测依据，不是直径定理。

[RARE15_PREDICTION.json](RARE15_PREDICTION.json)在实际一跳结构分析之后、R4计算之前冻结了明确正向预测。随后复用既有native深度4 BFS核心，只计算15个单根R4球和全部15个留一位集并，没有从其它3670个可接点中换点或启动优化。

结果全部失败：每个14点子集遗漏9754–11640个旧点。全15点的R4并与去掉85397后的14点并相同，均只覆盖84432点，遗漏9754点；其中409点原degree13、9345点原degree14。全部遗漏标签保存于[RARE15_MISSING.json](RARE15_MISSING.json)，首个为6。因此此15点类别的任何更小邻集也不能完成单点扩张。

[RARE15_RESULT.json](RARE15_RESULT.json)保存全部15种留一计数，[RARE15_STRUCTURE.json](RARE15_STRUCTURE.json)保存真实局部邻接，[RARE15_BALLS.json](RARE15_BALLS.json)及二进制R4球可复用。native覆盖CPU为0.196892秒；含编译与Python整理共1.499629988秒，低于10CPU秒预算。

该反例说明，此源中“近端邻域不相交”不足以保证长路覆盖互补。9754是固定邻集的未覆旧顶点数，不是已生成图的全源无序坏对数。本轮没有生成新候选、没有新根BFS，实际目标图n、D及普通无序坏对均为空。

[RESULT.json](RESULT.json)和[terminal.json](terminal.json)已终态，pending为空。结论只关闭这15个degree12点内的单点保边扩张；当前图的其它3670个degree13可接点仍未搜索，不能声称一般94187点图不存在。按约退出该有限对照，不追加邻点替换；后续须有能覆盖全类旧点的源结构或明确新路由规则作为依据。
