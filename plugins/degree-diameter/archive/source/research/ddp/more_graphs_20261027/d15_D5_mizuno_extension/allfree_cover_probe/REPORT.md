# (15,5)全2498空余点：固定64次构造未命中

本批64个完整15pin构造全部失败，没有生成100133点图。20球平均比例高于D14对照的预测仍得到实测支持，但本次操作预测“至少一个固定构造完成全cover”被反驳；任意≤15pin cover是否存在仍未决。

基图是已绑定的[实际100132点源](../source100132.edges)，749732边、最大度15，有2498个可接点、2516个空余槽。公开来源、首20球和完整spare-star筛见[源报告](../REPORT.md)。本批使用全部2498空余点，不假设旧100000纤维标签对应，也不重复source全源BFS。

## 同算法、不同参数的固定对照

[PREDICTION.json](PREDICTION.json)在新球及构造计算前冻结。沿用D14批次相同的生成规则：先按每个旧点的全候选支持度找最稀少目标，按静态逆支持权重和、球大小、标签排序选出64个不同首pin。每次构造后续都以最稀少未覆目标为约束，选完整未覆增益最大的合法pin，平手规则固定，最多15pins。不换点、不回溯、不调用solver，不在失败后增加起点。

复用首20个球，仅一次计算其余2478球；前100新球只处理一次。全部缓存完整后计算全旧点支持度，并完成全部64次构造。[FROZEN_FIRST_PINS.json](FROZEN_FIRST_PINS.json)保留实际首选列表，[RESULT.json](RESULT.json)保留所有64个完整邻集及未覆点数。

|量|实测|
|---|---:|
|复用 / 新算R4球|20 / 2478|
|全2498球union未覆盖旧点|0|
|每个旧点的候选支持度|364–651|
|完整构造|64/64|
|完整命中 / 新图|0 / 0|
|本批最少未覆旧点|1848|
|native CPU秒|2.01014|
|含编译、缓存和整理总CPU秒|4.066048549|

allfree union和正支持度只是必要条件，不能当成≤15球cover。本批未覆数是固定邻集到旧点的R4缺项，不是任何新图的普通无序坏对。所保存集合和全部遗漏见[best_construct.json](best_construct.json)，不以该数字作为继续微调的理由。

完整缓存为[allfree_R4.u64le.bin](allfree_R4.u64le.bin)，按[BALLS_META.json](BALLS_META.json)的2498个实际标签顺序排列；每行1565个little-endian uint64。[target_support.u16le.bin](target_support.u16le.bin)按旧点标签保存支持数。[INTERFACE.json](INTERFACE.json)绑定源、度数、所有缓存和终态，后续无需重算这些球。

[adapt.py](adapt.py)仅将既有D14生成程序的实际source、degree cap、20球缓存及构造上限改为D15参数，不运行旧D14范围；[probe.cpp](probe.cpp)和[run.py](run.py)可复现本次固定规则。

[terminal.json](terminal.json)已终态，pending为空。实际目标图n、D及普通无序坏对为null；新根BFS与source全源BFS均为0。按约立即停止，不利用剩余CPU续起点、改pins或启动MIP。完整64生成集合失败不等于全部15pin集合失败，也不排除一般100133点图。
