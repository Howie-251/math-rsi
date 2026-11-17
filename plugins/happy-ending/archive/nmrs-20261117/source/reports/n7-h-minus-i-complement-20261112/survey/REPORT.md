# 已有模型与二块连接的有限普查

Linux完成六个模型的完整颜色物理DP，结果见[summary.json](summary.json)。所有模型均满足packet、无R7/B6/weak7；这里h为实际蓝五首末交集大小，i为全部R6/B5首末四集合之并的补集大小。

|case|n|h|i|h−i|
|---|---:|---:|---:|---:|
|actual21|21|5|5|0|
|weak6-21|21|7|1|6|
|standard25|25|0|25|−25|
|swapped25|25|1|10|−9|
|join30-right|30|1|0|1|
|join30-left|30|1|2|−1|

输入快照为actual21.tsv、weak6-21.tsv、standard25.tsv；标准25点来自canonical Happy Ending archive的 `source/working/package/proofs/sat-756/color.tsv`。前两例分别来自 `reports/n7-blue-through-local-20261112/full-k21/colors.tsv` 与 `reports/n7-blue-through-weak6-20261112/free21/colors.tsv`。每例子目录含重新标准化的完整颜色、全部端对精确长度、四角色与人口结果。

[probe.py](probe.py)给完整独立递推和构造。两个30点例由换色25点与全蓝5点按两种次序作全红混合三元组连接：packet保持，红长为两块红长之和至多6，至少三点的蓝路不跨块，因此同端异色长和仍≤8；随后仍对全部颜色作DP检验。这里不是全标准模型分类。

这里只做有限普查，无求解器、无外部审查。其后唯一自由25点测试找到反例，见[主报告](../REPORT.md)。复现：在对应Linux目录运行 `python3.12 -B probe.py`；脚本为create-only，应复制源和三个输入至新目录，不能在封存目录重跑。最终绑定覆盖全部案例文件；本地传输收据另列。
