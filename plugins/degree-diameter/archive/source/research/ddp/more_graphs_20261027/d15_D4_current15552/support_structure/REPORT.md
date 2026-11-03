# 15552 缓存支持结构：没有重复行，free 图为 216 个三角形

仅执行一次已冻结的缓存计数器，结果完整结束。事前“至少存在一个完全相同的 target 支持行、可无损减少模型行数”的预测被推翻。原 IP 的 UNKNOWN 保持原状，没有重启或改变预算。

## 精确支持相同的约束不存在

读取已有 [COVER_CSC](../single_vertex_R3_cover/COVER_CSC.bin)，将 15552 个 target 的全部 648 列支持表示为定长 bit arrays，按完整数组的字典序精确分组。结果：

~~~text
原 target rows          15552
不同支持 rows           15552
重复组                  0
可删除的重复 rows        0
合并前后 nonzeros       1496880 → 1496880
~~~

因此，本轮想用的“相同覆盖行合并”没有任何降维作用。648 个二元 pin 变量、15552 个互不相同的覆盖行及一个 cardinality≤15 条件仍须同时满足；这个事实不等同 IP 不可行。

所有组的 representative、member IDs 与支持大小保存在 [EXACT_ROW_GROUPS](EXACT_ROW_GROUPS.jsonl)，没有写入重复的大型支持数组。代表索引 [UNIQUE_ROW_REPRESENTATIVES](UNIQUE_ROW_REPRESENTATIVES.i32le.bin) 保留全部 15552 个目标，故没有导出一个假压缩模型，也没有再次求解。这里只做 exact equality，没有做支持包含关系或其它简化搜索。

## 原 648 个 free 点的诱导结构

通过已有 R3_MASKS 的 eligible ID 映射与实际源边表，只取 free–free 边。实际 648 点、648 边，所有 free 诱导度均为 2，组件恰为 216 个互不相交 C3，没有其它组件类型。完整顶点/邻接见 [FREE_COMPONENTS](FREE_COMPONENTS.json)。这里的连通扫描是组件 DFS，不是普通图距离 BFS。

这提供真实局部结构：仅靠 F 内的一步支配，需要至少每个三角形选一点，共 216 个 pin；它与前一张 972 源的 36 条 free-path、gamma48 很不同。但当前单点条件使用整个旧源的 R3，路线可以经过非 free 点到达其它三角形，因此 216 不能充作本次 15-pin R3 覆盖的下界。三角形内的三个 pin 也不能未经列支持比较就视为可互换变量。没有据此启动任何新 helper 或模板。

## 硬预算与此前运行时间的准确解释

新 worker 与 native 子进程均设置 resource/RLIMIT_CPU=(3,3)。native CPU 0.028769 秒，编译 CPU 1.303613315 秒，整批 CPU 1.334735657 秒，在硬限内。新普通 BFS、R3 球、solver、候选图、label 重新分块试验均为 0。父代理已检查的 64×243 非 equitable 结论直接继承，本轮没有按其它因数试标签。

这次说明数据读取、约 150 万非零支持的精确分组和 free 组件计数都很便宜。此前时间主要耗在 IP 调用阶段：旧 solver 单次 22.983918811 CPU，已有 R3 准备仅约 0.028 CPU；内部 time_limit 没限制住整次调用，而当时没有 worker CPU 硬限。旧记录没有把 presolve、LP、分支分别计时，不能再声称具体某一内部阶段是唯一原因。没有任何新 solver 用来诊断它。

当前卡点是实际离散覆盖选择仍未解决，且“完全重复支持行”这条便宜缩模途径为空；不是原数据未取得、距离球未算，亦不是已证明不存在 15-pin 解。保存数据等待新的具体判断，不自动延长 IP。

证据：[事前预测](PREDICTION.json)、[完整计数](RESULT.json)、[计数程序](counter.cpp)、[硬限入口](run.py)。此前源 profile 与原报告未改写。
