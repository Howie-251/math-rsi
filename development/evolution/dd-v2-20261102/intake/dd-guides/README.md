# Degree–Diameter：完整研究原料与可复现构造

从最初27格题目清单，到153个命名合法图、43组参数与47个具体图形式化记录，本包保存研究如何实际推进：预测、尝试、反例、排除、改规则、成功、核验与比较。

**[先读中文入口](START_HERE.txt)**。用户要求ZIP尽量控制在100 MB，因此原始文字、源码、完整Wiki、关键输入与判定结果优先；完整图由[确定性构造程序](constructors/README.md)定义。体积取舍在[归档范围](guide/05_ARCHIVE_SCOPE.md)中列明。

## 代表成果

| 参数 | 已核对主表 | 本地图 | 增加 |
|---|---:|---:|---:|
| (11,5) | 37,628 | **37,631** | **+3** |
| (12,5) | 42,342 | **42,402** | **+60** |
| (16,4) | 16,384 | **16,416** | **+32** |

这些主表数值于2026-11-02复读[Comellas公开主表](https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html)，[包内事实快照](publication/COMELLAS_CURRENT_20261102.json)保留比较口径。(13,5)的51,457点也超过该表51,417点，但已找到公开88,452点构造，单列在完整成果表中。

主表外，直径3的20～26度代表覆盖3,840到7,532点；更高参数包括54度56,862点，以及98度414,132点。其公开方法基线、提升数字、已知更大对手与原作者归属见[43参数成果比较](guide/03_RESULTS_AND_PUBLIC_COMPARISONS.md)。153是命名图实例数，包含同族前缀；一般最大阶最优性未由这些下界构造证明。

## 完整研究轨迹

- [最初问题、人工反馈与时间线](guide/01_INITIAL_PROBLEMS_AND_TIMELINE.md)
- [成功与失败的实际转折](guide/02_RESEARCH_TRAJECTORIES.md)
- [成果与公开比较](guide/03_RESULTS_AND_PUBLIC_COMPARISONS.md)
- [实际耗时与复现范围](guide/04_TIME_COSTS_AND_REPLAY.md)
- [461条机器可读轨迹](guide/trajectory_index.csv)
- [461条原始耗时字段](guide/timings_by_experiment.csv)
- [完整原始方法账本](research-wiki/DDP_METHOD_LEDGER.json)
- [长期追加的人工意见与进展原文](research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md)

上述导读连接原始材料，不替代原始记录。文件仍按原来的research/context/formal等相对结构保存；旧状态、命令和当时的未完成结论保留为历史，不能自动变成当前执行授权。

## 使用

给下一版系统时，从START_HERE.txt开始读，沿轨迹表找到原代码、输入、结果和时间字段，提炼带适用条件和失败边界的知识。用于知识沉淀时可以读取最终结果；若以后做历史断点盲测，则需要另外隔离当时未知的后续材料。

只重建已有图时，按constructors/reproduce_index.csv选择命令。部分大图生成程序需要现有C++17编译器；本包没有启动新搜索或重新执行全部距离/Lean验证。原始有限检查、审阅和形式化分别保留自己的实际范围。
